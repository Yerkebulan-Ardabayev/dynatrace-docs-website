---
title: AWS Lambda log collection
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector
scraped: 2026-05-12T12:00:13.526654
---

# AWS Lambda log collection

# AWS Lambda log collection

* How-to guide
* 7-min read
* Updated on Dec 17, 2025

Dynatrace version 1.263

You can collect logs directly from your AWS Lambda functions and send them to Dynatrace for analysis. The solution is an alternative to the [CloudWatch log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Use AWS log forwarding to ingest AWS logs.") with benefits in terms of cost and latency, and is also easier to set up, in particular if AWS Lambda tracing is already in place. As part of the OneAgent installation process, this feature provides a streamlined solution for collecting logs from your Lambda functions.

## Prerequisites

* For layers with OneAgent version 1.263 and earlier, the Environment ActiveGate must have a trusted (not self-signed) certificate. For more details, see [Custom SSL certificate for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

* An ActiveGate with the Log analytics collector module enabled. See [Log Monitoring API v2 - POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Deploy

For Python, Node.js, and Java Lambda functions, Dynatrace provides a single Lambda layer that enables both trace and log collection. For .NET, Dynatrace provides a standalone layer that collects only logs.

Log collection for Python, Node.js, and Java Lambda functions

To deploy the Dynatrace Lambda extension, follow the instructions from [Trace Python, Node.js, and Java Lambda functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") but with the following two differences:

1. Under **I want to enable**, select **Traces and Logs**.
2. Either select **Create token** to create a new access token or enter [an existing access token with the `logs.ingest` permission](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") into the **Access Token** input field.

If you previously used the Dynatrace Lambda extension without logging, you have to adapt the Lambda Layer Arn as well as the configuration provided in the wizardâby adding the necessary enhancements for the log collector.

Log collection for .NET Lambda functions

For .NET Lambda functions, follow the steps described in [Monitor AWS Lambda with OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup "Prerequisites for monitoring AWS Lambda with OpenTelemetry") but with the following two differences:

1. Under **I want to enable**, select **Logs**.
2. Either select **Create token** to create a new access token or enter [an existing access token with the `logs.ingest` scope](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") into the **Access Token** input field.

If you previously used tracing integration without logging, you have to adapt the configuration as provided in the wizardâby adding the necessary enhancements for the log collector.

Disable Firehose log streaming or CloudWatch log forwarding

If you are currently using it, you must disable Firehose log streaming or CloudWatch log forwarding for functions on which you wish to use this log collection feature in order to avoid duplicate log exports. See [Log monitoring with AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder#unsubscribe "Use AWS log forwarding to ingest AWS logs.") or (lm-stream-logs-with-firehose#unsubscribe).

## Usage

After deployment, collected logs for each future function invocation and initialization can be found in the **Related logs** card on the Lambda function's service page in Dynatrace, and in the **Log viewer**. You can inspect the log details to find the type of the log under the `telemetryevent.type` attribute, among other metadata. Note that the content of `platform` logs will be JSON data, while the content of `function` logs will be plain text.

### Logs in context of traces

To correlate and see application logs with traces in Dynatrace, you need to enrich logs with the trace identifiers. For more details see [Logs in context of traces](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Configure log message enrichment with OpenTelemetry on AWS Lambda.").

## Configuration

### Log event types

Dynatrace collects two [log event typesï»¿](https://dt-url.net/xd038u5), platform events and function logs. To configure which log event types are collected, use the following syntax.

| Configure with | Location | Default value | Syntax |
| --- | --- | --- | --- |
| JSON file | `EventTypes` (property in the `LogCollection` object) | `["platform", "function"]` | Array of strings, for example `"function"`[1](#fn-1-1-def) |
| Environment variables | `DT_LOG_COLLECTION_EVENT_TYPES` | `platform:function` | Colon-separated list of log event types, for example `function`[1](#fn-1-1-def) |

1

Set the value to `["function"]` (or `function`) to collect only function logs.

### Endpoint

OneAgent version 1.275+

The endpoint that is used for exporting logs to is derived from the base URL of your configuration [deployment screen](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java."). You can override the default value by setting the override-value location to a specific full endpoint URL that contains also the path.

| Configure with | Default-value location | Override-value location |
| --- | --- | --- |
| JSON file | `Connection.BaseUrl` | Add the `Endpoint` property to the `LogCollection` object. |
| Environment variables | `DT_CONNECTION_BASE_URL` | `DT_LOG_COLLECTION_ENDPOINT` |

Environment ActiveGate and default value

If you're using an Environment ActiveGate, make sure the [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Understand and learn how to work with monitoring environments.") is included in the default value location or set its value to the full URL of the log ingest endpoint (for example, `https://{activegate-host}:9999/e/{your-environment-id}/api/v2/logs/ingest`).

If you're using Environment ActiveGate (which is usually the case, if you deployed ActiveGate by yourself) and don't have `/e/{your-environment-id}` as part of your `DT_CONNECTION_BASE_URL` (`Connection.BaseUrl`), you need to set either the

* `DT_LOG_COLLECTION_ENDPOINT` environment variable
* or `LogCollection.Endpoint` JSON property

to the full URL of the log ingest endpoint (i.e. `https://{activegate-host}:9999/e/{your-environment-id}/api/v2/logs/ingest`).
The [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Understand and learn how to work with monitoring environments.") is typically the tenant ID.

### Fetch token from AWS Secrets Manager

OneAgent version 1.295+

Instead of specifying the authentication token explicitly in the configuration, you can configure OneAgent to fetch a token stored in [AWS Secrets Managerï»¿](https://docs.aws.amazon.com/secretsmanager).

Prerequisites

* Make sure you granted the `secretsmanager:GetSecretValue` permission for the authentication token secret ARN to the Lambda function monitored by OneAgent. For details, see [Authentication and access control for AWS Secrets Managerï»¿](https://dt-url.net/7n03p10) in the AWS Secrets Manager documentation.
* Make sure the secret value contains only the plaintext authentication token value (without quotes). Note that

  + Secrets with JSON structure are not supported. For details, see [Create an AWS Secrets Manager secretï»¿](https://dt-url.net/fy23pdx) in the AWS Secrets Manager documentation.
  + When you retrieve the secret value, Secrets Manager returns by default only the current secret version (`AWSCURRENT` label). For details, see [What's in a Secrets Manager secret?ï»¿](https://dt-url.net/1f43pq8) in the AWS Secrets Manager documentation.

To fetch the token for log collection, set the token secret ARN either to the environment variable `DT_LOG_COLLECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN` or the JSON property `LogCollection.AuthTokenSecretsManagerArn`.

This option always overrides `DT_LOG_COLLECTION_AUTH_TOKEN` (`LogCollection.AuthToken`). If the fetch fails, the log collector won't be able to export log data.

A fetch accesses AWS Secrets Manager only once, during the Lambda function's initialization phase; this causes an increase of the Lambda function's cold start duration.

To [fetch the token for trace connection](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#aws-secrets-manager "Monitor Lambda functions written in Python, Node.js, and Java."), set another fetch.

### Filtering

OneAgent version 1.291+

By default, logs for the configured log event types are collected for all the following log levels, ordered from the lowest to the highest level:

* `TRACE`
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`
* `FATAL`

For more information, see [AWS log-level filteringï»¿](https://dt-url.net/h503n1u).

To configure from which level to start log collection, for example, starting from `WARN` level, set a filter using the following syntax.

| Configure with | Location | Syntax |
| --- | --- | --- |
| JSON file | `LogCollection.Filter.MinLevel` (`LogCollection` object has property `Filter` which has property `MinLevel`) | `<Log level>`  **Example:** `{"LogCollection": {"Filter": {"MinLevel": "WARN" }}}` |
| Environment variables | `DT_LOG_COLLECTION_FILTER_MIN_LEVEL` | `<Log level>`  **Example:** `WARN` |

For example, if `<Log level>` is `WARN`

* Logs for `TRACE`, `DEBUG`, and `INFO` levels are not collected.
* Logs for `WARN`, `ERROR`, and `FATAL` levels are collected.

To configure log collection filters directly in AWS, see [Using Amazon CloudWatch Logs with AWS Lambdaï»¿](https://dt-url.net/h503n1u). Note that with this option

* Logs are not shown on CloudWatch.
* Dynatrace will not collect logs that are already filtered out in AWS.

## Limitations

* The `extension` event type currently is not supported: if you try to configure the `extension` event type, an error is shown and log collection does not start.
* In the classic AWS Lambda integration, logs collected by the log collector are not associated with traces and are not shown in the trace view in the **Logs** tab, and will only be shown on the **Related logs** card or in the **Log viewer**. However, you may use [manual log enrichment](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") in order to connect your function logs to your traces. See [AWS Lambda logs in context of traces](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Configure log message enrichment with OpenTelemetry on AWS Lambda.") for language-specific examples of manual log enrichment.
* When using the latest AWS Lambda integration, automatic log enrichment is available for structured logs printed with supported logging frameworks.
* If an AWS log event doesn't have a log level and the log message contains the string `[error]` or `[ERROR]`, the log level will be set to `ERROR`. Otherwise `INFO` level is used.
* We do not recommend combining the standalone collector layer with a OneAgent layer. If you want tracing and log collection for your Lambda functions, use the combined **Traces and Logs** layer instead.

* The environment variable `DT_CONNECTION_BASE_URL` can't be copied from the deployment screen. Instead, the value of `DT_CONNECTION_BASE_URL` must be set to a URL in the form of `https://{activegate-host}:9999/e/{your-environment-id}`.

## Troubleshooting

* [Dynatrace does not ingest logs (HTTP 429)ï»¿](https://dt-url.net/hm23mng)

## Related topics

* [Trace Lambda functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.")
* [Log monitoring with AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Use AWS log forwarding to ingest AWS logs.")