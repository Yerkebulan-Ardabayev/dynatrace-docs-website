---
title: Log ingestion warnings (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings
scraped: 2026-02-25T21:27:24.769440
---

# Log ingestion warnings (Logs Classic)

# Log ingestion warnings (Logs Classic)

* Overview
* 2-min read
* Published Oct 10, 2023

Log Monitoring Classic

If your ingested logs donât look as expected, you can check if a particular log record contains warnings regarding issues that occurred for that log in the log ingest and processing pipeline. Look for a `dt.ingest.warnings` attribute in log viewer. It lists warnings about issues that affected a particular log record.

Examples of possible warnings: