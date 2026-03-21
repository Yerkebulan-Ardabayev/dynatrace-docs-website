"""
Dynatrace Managed Metrics Reporter.
Sends custom metrics via Metrics API v2 (POST /api/v2/metrics/ingest).
Uses Metric Ingestion Protocol (text/plain line format).

Ref: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/metric-v2/post-ingest-metrics
"""
import os
import time
import requests
from typing import Dict, Any, Optional

from .structured_logger import get_logger


class DynatraceMetricsReporter:
    """
    Sends pipeline metrics to Dynatrace Managed via Metrics API v2.

    Required env vars:
        DT_MANAGED_URL: Base URL, e.g. https://{domain}/e/{env-id}
        DT_API_TOKEN:   API token with `metrics.ingest` scope
    """

    def __init__(
        self,
        dt_url: Optional[str] = None,
        dt_token: Optional[str] = None,
    ):
        self.dt_url = (dt_url or os.getenv("DT_MANAGED_URL", "")).rstrip("/")
        self.dt_token = dt_token or os.getenv("DT_API_TOKEN", "")
        self.logger = get_logger()
        self._enabled = bool(self.dt_url and self.dt_token)

        if not self._enabled:
            self.logger.warn(
                "metrics",
                "Dynatrace metrics reporter disabled: DT_MANAGED_URL or DT_API_TOKEN not set",
            )

    def report_translation_stats(self, stats: Dict[str, Any]):
        """
        Report translation pipeline stats to Dynatrace.

        Expected keys in stats:
            total, translated, skipped, failed, coverage_pct,
            quota_stopped, remaining, cache_hits, cache_misses
        """
        if not self._enabled:
            return

        ts = int(time.time() * 1000)
        lines = []

        # Coverage
        coverage = stats.get("coverage_pct", 0.0)
        lines.append(f"docs.translation.coverage,pipeline=daily gauge,{coverage:.1f} {ts}")

        # File counts
        for key in ("total", "translated", "skipped", "failed"):
            val = stats.get(key, 0)
            lines.append(f"docs.translation.files.{key},pipeline=daily gauge,{val} {ts}")

        # Remaining (untranslated due to quota)
        remaining = stats.get("remaining", 0)
        lines.append(f"docs.translation.files.remaining,pipeline=daily gauge,{remaining} {ts}")

        # Cache metrics
        hits = stats.get("cache_hits", 0)
        misses = stats.get("cache_misses", 0)
        total_cache = hits + misses
        hit_rate = (hits / total_cache) if total_cache > 0 else 0.0
        lines.append(f"docs.translation.cache.hit_rate gauge,{hit_rate:.2f} {ts}")
        lines.append(f"docs.translation.cache.hits count,delta={hits} {ts}")
        lines.append(f"docs.translation.cache.misses count,delta={misses} {ts}")

        # Quota stopped flag (1 = stopped, 0 = ok)
        quota_stopped = 1 if stats.get("quota_stopped", False) else 0
        lines.append(f"docs.translation.quota_stopped gauge,{quota_stopped} {ts}")

        self._send(lines)

    def report_pipeline_duration(self, stage: str, duration_seconds: float):
        """Report duration of a pipeline stage."""
        if not self._enabled:
            return

        ts = int(time.time() * 1000)
        lines = [f"docs.pipeline.duration,stage={stage} gauge,{duration_seconds:.1f} {ts}"]
        self._send(lines)

    def report_provider_stats(self, provider_stats: Dict[str, Dict[str, int]]):
        """
        Report per-provider API usage.

        provider_stats: {
            "groq": {"calls": 120, "rate_limits": 5, "errors": 2},
            "gemini-flash": {"calls": 340, "rate_limits": 0, "errors": 1},
        }
        """
        if not self._enabled:
            return

        ts = int(time.time() * 1000)
        lines = []

        for provider, data in provider_stats.items():
            calls = data.get("calls", 0)
            rate_limits = data.get("rate_limits", 0)
            errors = data.get("errors", 0)
            lines.append(f"docs.translation.api.calls,provider={provider} count,delta={calls} {ts}")
            lines.append(
                f"docs.translation.api.errors,provider={provider},type=rate_limit count,delta={rate_limits} {ts}"
            )
            lines.append(
                f"docs.translation.api.errors,provider={provider},type=other count,delta={errors} {ts}"
            )

        self._send(lines)

    def report_dead_letter_count(self, count: int):
        """Report number of files in the dead letter queue."""
        if not self._enabled:
            return

        ts = int(time.time() * 1000)
        self._send([f"docs.translation.dead_letter.count gauge,{count} {ts}"])

    def _send(self, lines: list):
        """Send metric lines to Dynatrace Metrics API v2."""
        if not lines:
            return

        payload = "\n".join(lines)
        endpoint = f"{self.dt_url}/api/v2/metrics/ingest"

        try:
            resp = requests.post(
                endpoint,
                headers={
                    "Authorization": f"Api-Token {self.dt_token}",
                    "Content-Type": "text/plain; charset=utf-8",
                },
                data=payload,
                timeout=10,
            )
            if resp.status_code == 202:
                self.logger.debug(
                    "metrics",
                    f"Metrics sent: {len(lines)} lines accepted",
                )
            else:
                self.logger.warn(
                    "metrics",
                    f"Metrics ingest failed: HTTP {resp.status_code}",
                    response=resp.text[:200],
                )
        except requests.RequestException as e:
            self.logger.warn(
                "metrics",
                f"Metrics ingest error: {e}",
            )
