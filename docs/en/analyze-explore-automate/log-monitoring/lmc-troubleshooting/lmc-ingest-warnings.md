---
title: Log ingestion warnings (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings
scraped: 2026-02-20T21:24:05.381799
---

# Log ingestion warnings (Logs Classic)

# Log ingestion warnings (Logs Classic)

* Overview
* 2-min read
* Published Oct 10, 2023

Log Monitoring Classic

If your ingested logs donât look as expected, you can check if a particular log record contains warnings regarding issues that occurred for that log in the log ingest and processing pipeline. Look for a `dt.ingest.warnings` attribute in log viewer. It lists warnings about issues that affected a particular log record.

Examples of possible warnings:

Warning

Description

content\_trimmed

The content was trimmed after being received bythe API because it exceeded the event content maximum byte size limit.

content\_trimmed\_pipe

The content was trimmed after processing rules were applied because it exceeded the event content maximum byte size limit.

attr\_count\_trimmed

The number of attributes was trimmed after being received by the API because it exceeded the maximum number of attributes in a single event.

attr\_count\_trimmed\_pipe

The number of attributes was trimmed after processing rules were applied because it exceeded the maximum number of attributes in a single event.

attr\_key\_trimmed

At least one attribute key was trimmed because it exceeded the key maximum byte size limit.

attr\_val\_count\_trimmed

At least one multi-value attribute had the number of values trimmed, after being received by the API, because it exceeded the maximum number of attributes in a single event.

attr\_val\_count\_trimmed\_pipe

After applying processing rules, at least one multi-value attribute had its value number trimmed because it exceeded the maximum number of attributes.

attr\_val\_size\_trimmed

At least one attribute value size was trimmed after being received by the API because it exceeded the value maximum byte size limit.

attr\_val\_size\_trimmed\_pipe

At least one attribute value size was trimmed after processing rules were applied because it exceeded the value maximum byte size limit.

timestamp\_corrected

The timestamp was too far in the future and was corrected to the current time.

common\_attr\_corrected

At least one of the following attributes was corrected: `status`, `loglevel`, or `event.type`.

processing\_batch\_timeout

Batch timeout occurred while executing log processing rules.

processing\_transformer\_timeout

Execution timeout occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_error

Execution error occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_throttled

Execution throttled in one of the processing transformers while executing log processing rules.

processing\_output\_record\_conversion\_error

Output conversion error occurred for some records while executing log processing rules.

processing\_prepare\_input\_error

âPrepare input errorâ occurred in one of the enabled log processing rules.