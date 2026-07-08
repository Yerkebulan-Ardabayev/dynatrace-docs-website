---
title: Logging reference for Dynatrace Configuration as Code via Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/reference/logging
---

# Logging reference for Dynatrace Configuration as Code via Monaco

# Logging reference for Dynatrace Configuration as Code via Monaco

* Reference
* 4-min read
* Updated on May 15, 2024

## Debug logging

All Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI) commands accept the optional flag `--verbose` (or `-v` for short).
This flag enables additional debug log output that can help you find the cause of an error.

Regardless of flags, the CLI always writes a verbose log file to a `.log/` folder created in the directory in which the command was executed.

## Log timestamps

By default, logs include timestamps in the timezone of the machine on which they were produced.

To write UTC timestamps instead, set the `MONACO_LOG_TIME=utc` environment variable.

Linux/macOS

Windows

```
MONACO_LOG_TIME=utc monaco deploy manifest.yaml
```

```
$env:MONACO_LOG_TIME=utc



monaco deploy manifest.yaml
```

## Support archive for troubleshooting

For enhanced troubleshooting, use the `--support-archive` flag, which enables the CLI to generate a ZIP archive that contains detailed information about the CLI's operations during execution.

```
monaco --support-archive <command>
```

The generated ZIP archive named `support-archive-<timestamp>.zip` is stored in the CLI's current working directory and includes various information such as regular logs, HTTP request and response data:

* `<timestamp>.log`—all logs produced by the Dynatrace Monaco CLI
* `<timestamp>-req.log`—HTTP requests made to the Dynatrace API
* `<timestamp>-resp.log`—HTTP responses received from the Dynatrace API

Sensitive security information such as the authorization header is excluded from the recorded HTTP request data in these files.

**Known limitation:** The content of multipart POST requests is not logged.

## Structured JSON logging

Dynatrace Monaco CLI version 2.4.0+

To allow the processing of logs by other tools and automation, the CLI supports logging in structured JSON format instead of unstructured text.

To activate structured JSON logging, use the `MONACO_LOG_FORMAT=json` environment variable.

Linux/macOS

Windows

```
MONACO_LOG_FORMAT=json monaco deploy manifest.yaml
```

```
$env:MONACO_LOG_FORMAT=json



monaco deploy manifest.yaml
```

In structured JSON logging mode, the basic log data is extended with metadata fields that supply details about the configuration coordinate, environment, and possibly error that a log line relates to. For details on metadata fields, see the [Metadata log fields](#metadata-log-fields) section.

### Basic log fields

These fields are always present.

| Field | Description |
| --- | --- |
| `level` | The log level - `debug`, `info`, `warn`, or `error`. |
| `ts` | The timestamp of the log line. |
| `msg` | The log message. |

### Metadata log fields

Metadata fields are included based on their availability and relevance to the log line; not all metadata fields are included in all log lines.

| Field | Description | Content |
| --- | --- | --- |
| `coordinate` | The coordinate of the configuration to which this log is related. | ```  {  "reference": "[project]:[type]:[ID]",  "project": "[project]",  "type":"[type]",  "configID":"[ID]"  } ``` |
| `type` | This is logged in some cases in which no full `coordinate` is available. | ```  {  "type":"[type]"  } ``` |
| `environment` | The target [environment](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") to which this log line is related.  This contains information about the environment's `group` and `name`. | ```  {  "group": "[group]",  "name": "[name]"  } ``` |
| `error` | Details about the underlying error. This is only included for warning and error log lines.  This contains information about the `type` of error as well as `details` about the error content.  Details differ based on the type of error.  For the content of errors, please refer to the [code in GitHub﻿](https://github.com/search?q=repo%3ADynatrace%2Fdynatrace-configuration-as-code+%28language%3AGo%29+%2Ferr.*struct+%5C%7B%2F&type=code). | ```  {  "type": "[type of error]",  "details": "[content of the error]"  } ``` |

Some log lines might contain further non-standard fields with specific information related to them. For example, some parsing errors include the full invalid API response content in an additional field.

## Disable logging to files

By default, Monaco writes all log entries to files within the `.logs` folder. Two files containing all log entries and errors, with suffixes `.log` and `-errors.log` are created with all log messages and error messages respectively. To disable this functionality, set the environment variable `FEAT_LOG_FILE_ENABLED` to `0` or `false`.