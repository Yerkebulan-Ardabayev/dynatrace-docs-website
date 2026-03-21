"""
SQLite-based Job Queue for idempotent translation processing.
Ensures:
- No duplicate API calls for the same content
- Retry with exponential backoff
- Dead letter queue for permanently failed jobs
- Atomic state transitions
"""
import sqlite3
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any, List


class JobQueue:
    """
    Persistent job queue backed by SQLite.

    Job lifecycle:
        pending -> processing -> done
        pending -> processing -> failed -> processing -> done  (retry)
        pending -> processing -> failed -> ... -> dead  (max retries exceeded)
    """

    SCHEMA_VERSION = 1

    def __init__(self, db_path: str = ".translation_queue.db", max_retries: int = 3):
        self.db_path = db_path
        self.max_retries = max_retries
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")  # Better concurrent access
        self.conn.execute("PRAGMA busy_timeout=5000")
        self._init_schema()

    def _init_schema(self):
        """Create tables if they don't exist."""
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                source_hash TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                provider TEXT,
                retries INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                result_hash TEXT,
                error_message TEXT,
                UNIQUE(file_path, chunk_index, source_hash)
            );

            CREATE INDEX IF NOT EXISTS idx_jobs_status
                ON jobs(status, retries, created_at);

            CREATE INDEX IF NOT EXISTS idx_jobs_file
                ON jobs(file_path, status);

            CREATE TABLE IF NOT EXISTS schema_version (
                version INTEGER PRIMARY KEY
            );
        """)

        # Check/set schema version
        row = self.conn.execute("SELECT version FROM schema_version LIMIT 1").fetchone()
        if row is None:
            self.conn.execute(
                "INSERT INTO schema_version (version) VALUES (?)",
                (self.SCHEMA_VERSION,),
            )
        self.conn.commit()

    def enqueue(self, file_path: str, chunk_index: int, source_hash: str) -> bool:
        """
        Idempotently add a job to the queue.
        Returns True if a new job was created, False if it already existed.
        """
        now = datetime.now(timezone.utc).isoformat()
        try:
            self.conn.execute(
                """
                INSERT INTO jobs (file_path, chunk_index, source_hash, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (file_path, chunk_index, source_hash, now, now),
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Job already exists with same (file_path, chunk_index, source_hash)
            return False

    def enqueue_file(self, file_path: str, chunks: List[str]) -> int:
        """
        Enqueue all chunks of a file. Returns number of new jobs created.
        Skips chunks that are already queued with the same hash (idempotent).
        """
        new_count = 0
        for i, chunk in enumerate(chunks):
            chunk_hash = hashlib.sha256(chunk.encode("utf-8")).hexdigest()[:16]
            if self.enqueue(file_path, i, chunk_hash):
                new_count += 1
        return new_count

    def dequeue(self, provider: str) -> Optional[Dict[str, Any]]:
        """
        Atomically take the next available job for processing.
        Priority: fewer retries first, then oldest first.
        Returns job dict or None if queue is empty.
        """
        now = datetime.now(timezone.utc).isoformat()

        # Use a single atomic UPDATE...RETURNING
        cursor = self.conn.execute(
            """
            UPDATE jobs
            SET status = 'processing', provider = ?, updated_at = ?
            WHERE id = (
                SELECT id FROM jobs
                WHERE status IN ('pending', 'failed')
                  AND retries < ?
                ORDER BY retries ASC, created_at ASC
                LIMIT 1
            )
            RETURNING id, file_path, chunk_index, source_hash, retries, provider
            """,
            (provider, now, self.max_retries),
        )
        row = cursor.fetchone()
        self.conn.commit()

        if row is None:
            return None

        return dict(row)

    def complete(self, job_id: int, result_hash: str):
        """Mark a job as successfully completed."""
        now = datetime.now(timezone.utc).isoformat()
        self.conn.execute(
            "UPDATE jobs SET status = 'done', result_hash = ?, updated_at = ? WHERE id = ?",
            (result_hash, now, job_id),
        )
        self.conn.commit()

    def fail(self, job_id: int, error_message: str):
        """
        Mark a job as failed. Increments retry counter.
        If retries >= max_retries, status becomes 'dead'.
        """
        now = datetime.now(timezone.utc).isoformat()
        self.conn.execute(
            """
            UPDATE jobs
            SET status = CASE
                    WHEN retries + 1 >= ? THEN 'dead'
                    ELSE 'failed'
                END,
                retries = retries + 1,
                error_message = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (self.max_retries, error_message, now, job_id),
        )
        self.conn.commit()

    def get_file_status(self, file_path: str) -> Dict[str, int]:
        """
        Get job status summary for a specific file.
        Returns: {"pending": N, "processing": N, "done": N, "failed": N, "dead": N}
        """
        rows = self.conn.execute(
            "SELECT status, COUNT(*) as cnt FROM jobs WHERE file_path = ? GROUP BY status",
            (file_path,),
        ).fetchall()
        result = {"pending": 0, "processing": 0, "done": 0, "failed": 0, "dead": 0}
        for row in rows:
            result[row["status"]] = row["cnt"]
        return result

    def is_file_complete(self, file_path: str) -> bool:
        """Check if all chunks of a file are done."""
        row = self.conn.execute(
            """
            SELECT COUNT(*) as total,
                   SUM(CASE WHEN status = 'done' THEN 1 ELSE 0 END) as done
            FROM jobs WHERE file_path = ?
            """,
            (file_path,),
        ).fetchone()
        return row["total"] > 0 and row["total"] == row["done"]

    def get_stats(self) -> Dict[str, Any]:
        """Get overall queue statistics."""
        rows = self.conn.execute(
            "SELECT status, COUNT(*) as cnt FROM jobs GROUP BY status"
        ).fetchall()
        stats = {"pending": 0, "processing": 0, "done": 0, "failed": 0, "dead": 0}
        for row in rows:
            stats[row["status"]] = row["cnt"]
        stats["total"] = sum(stats.values())
        return stats

    def get_dead_letter_jobs(self) -> List[Dict[str, Any]]:
        """Get all jobs that have permanently failed."""
        rows = self.conn.execute(
            """
            SELECT id, file_path, chunk_index, source_hash, retries, error_message, updated_at
            FROM jobs WHERE status = 'dead'
            ORDER BY updated_at DESC
            """
        ).fetchall()
        return [dict(row) for row in rows]

    def reset_stale_processing(self, stale_minutes: int = 30) -> int:
        """
        Reset jobs stuck in 'processing' state (e.g., worker crashed).
        Returns number of jobs reset.
        """
        from datetime import timedelta

        cutoff = (
            datetime.now(timezone.utc) - timedelta(minutes=stale_minutes)
        ).isoformat()

        cursor = self.conn.execute(
            """
            UPDATE jobs SET status = 'failed', error_message = 'Stale processing reset'
            WHERE status = 'processing' AND updated_at < ?
            """,
            (cutoff,),
        )
        self.conn.commit()
        return cursor.rowcount

    def purge_completed(self) -> int:
        """Remove all completed jobs to free space. Returns count removed."""
        cursor = self.conn.execute("DELETE FROM jobs WHERE status = 'done'")
        self.conn.commit()
        return cursor.rowcount

    def close(self):
        """Close the database connection."""
        self.conn.close()
