---
title: Automatic log enrichment
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation
scraped: 2026-02-22T21:21:49.539233
---

# Automatic log enrichment

# Automatic log enrichment

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Apr 07, 2025

Dynatrace automatically enriches logs ingested both via API.

## Transform API-ingested logs

The Log ingestion API automatically transforms `status`, `severity`, `level`, and `syslog.severity` severity keys to the `loglevel` attribute.

The input values for the `status`, `severity`, `level`, and `syslog.severity` severity keys are transformed (transformation is not case sensitive) into output values for the `loglevel` attribute based on the following mapping:

Input value

Output value

Example value

Begins with `emerg` or `f`

`EMERGENCY`

`Emergency`, `fail`, `Failure`

Begins with `e` excluding `emerg`

`ERROR`

`Error`, `error`

Begins with `a`

`ALERT`

`alarm`, `Alert`

Begins with `c`

`CRITICAL`

`Critical`, `crucial`

Begins with `s`

`SEVERE`

`Severe`, `serious`

Begins with `w`

`WARN`

`warn`, `Warning`

Begins with `n`

`NOTICE`

`note`, `Notice`

Begins with `i`

`INFO`

`Info`, `information`

Begins with `d` or `trace` or `verbose`

`DEBUG`

`debug`, `TRACE`, `Verbose`

## Transform all types of logs

Additionally, for each log event, a `status` attribute is created with a value that is a sum of `loglevel` values based on the following grouping:

Included `loglevel` values

Combined `status` attribute value

`SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY`

`ERROR`

`WARN`

`WARN`

`INFO`, `TRACE`, `DEBUG`, `NOTICE`

`INFO`

`NONE`

`NONE`

For example:
The `level` severity key in the Log ingestion API request parameter contains the value `serious`.

1. The `level` severity key is transformed into the `loglevel` attribute with the `serious` value mapped to `SEVERE` based on the above table.
2. The `loglevel` attribute containing the `SEVERE` value is grouped into `status` attribute. Based on the grouping table above, the `status` attribute will contain the `ERROR` value.
3. For the log event details, the log viewer will report the following:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")