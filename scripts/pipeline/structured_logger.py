"""
Structured JSON logger for the translation pipeline.
Outputs JSON Lines to stderr for Dynatrace Log Monitoring ingestion.
Each log entry includes: timestamp, level, stage, message, and arbitrary extra fields.
"""
import json
import sys
import time
from datetime import datetime, timezone
from typing import Any, Optional


class PipelineLogger:
    """
    Structured logger that outputs JSON Lines.
    Compatible with Dynatrace Custom Log Source ingestion.
    """

    LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40, "CRITICAL": 50}

    def __init__(
        self,
        pipeline_name: str = "dynatrace-docs-translation",
        min_level: str = "INFO",
        output_file: Optional[str] = None,
    ):
        self.pipeline_name = pipeline_name
        self.min_level = self.LEVELS.get(min_level, 20)
        self._output = None
        if output_file:
            self._output = open(output_file, "a", encoding="utf-8")

    def _emit(self, level: str, stage: str, message: str, **extra: Any):
        """Emit a single structured log entry."""
        if self.LEVELS.get(level, 0) < self.min_level:
            return

        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "pipeline": self.pipeline_name,
            "stage": stage,
            "message": message,
        }
        # Add extra fields, filtering out None values
        for k, v in extra.items():
            if v is not None:
                entry[k] = v

        line = json.dumps(entry, ensure_ascii=False)

        # Write to stderr (captured by CI) and optionally to file
        print(line, file=sys.stderr, flush=True)
        if self._output:
            self._output.write(line + "\n")
            self._output.flush()

    def debug(self, stage: str, message: str, **extra):
        self._emit("DEBUG", stage, message, **extra)

    def info(self, stage: str, message: str, **extra):
        self._emit("INFO", stage, message, **extra)

    def warn(self, stage: str, message: str, **extra):
        self._emit("WARN", stage, message, **extra)

    def error(self, stage: str, message: str, **extra):
        self._emit("ERROR", stage, message, **extra)

    def critical(self, stage: str, message: str, **extra):
        self._emit("CRITICAL", stage, message, **extra)

    # --- Convenience methods for common pipeline events ---

    def file_translated(
        self, file: str, provider: str, chunks: int, duration_ms: int
    ):
        self.info(
            "translate",
            "File translated",
            file=file,
            provider=provider,
            chunks=chunks,
            duration_ms=duration_ms,
        )

    def file_failed(self, file: str, error: str, chunk: int = None, total_chunks: int = None):
        self.error(
            "translate",
            "File translation failed",
            file=file,
            error=error,
            chunk=chunk,
            total_chunks=total_chunks,
        )

    def quota_exhausted(self, provider: str, remaining_files: int):
        self.error(
            "translate",
            "API quota exhausted",
            provider=provider,
            remaining_files=remaining_files,
        )

    def validation_issue(self, file: str, issue_type: str, detail: str):
        self.warn(
            "validate",
            f"Validation issue: {issue_type}",
            file=file,
            issue_type=issue_type,
            detail=detail,
        )

    def pipeline_summary(self, stats: dict):
        self.info("summary", "Pipeline run completed", **stats)

    def close(self):
        if self._output:
            self._output.close()


# Module-level singleton for easy import
_logger: Optional[PipelineLogger] = None


def get_logger(**kwargs) -> PipelineLogger:
    """Get or create the pipeline logger singleton."""
    global _logger
    if _logger is None:
        _logger = PipelineLogger(**kwargs)
    return _logger
