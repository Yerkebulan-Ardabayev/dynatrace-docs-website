---
title: Adjust the log message
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/message
scraped: 2026-02-21T21:07:08.609962
---

# Adjust the log message

# Adjust the log message

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 10, 2025

The ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** app automatically extracts and highlights a log message from a record and displays this as a separate column in the results table.

While the full content and all the attributes of your log record can be important to understanding the root cause, being able to quickly scan the messages can speed up finding the relevant logs and diagnosing the problem.

## What is a log message?

In many cases, logs from cloud-native applications or platforms contain a specific field that holds the actual message.

The **Log message** column is a dynamically generated field that shows the readable part of a log entry, if possible.

### Examples

Log record

Log message

```
{



"timestamp": "2025-10-13T10:50:03.205",



"level": "WARN",



"logger": "org.apache.activemq.artemis.core.server",



"message": "AMQ222165: No Dead Letter Address configured for queue answer_queue in AddressSettings",



"context": "default"



}
```

AMQ222165: No Dead Letter Address configured for queue answer\_queue in AddressSettings

```
{



"timestamp": "2025-10-13T08:54:02.009817Z",



"severity": "INFO",



"insertId": "238n5ebl11v8lc1x",



"jsonPayload": {



"message": "\"Starting watch\" path=\"/api/v1/namespaces/external-accounts \" resourceVersion=\"17603423543179000\" timeout=\"7m10s\""



},



"logName": "projects/prod-gke-apigw/logs/container.googleapis.com%2Fapiserver",



"resource": {



"labels": {



"location": "europe-west3",



"project_id": "prod-gke-apigw "



},



"type": "k8s_control_plane_component"



},



"sourceLocation": {



"file": "get.go",



"line": "278"



}



}
```

"Starting watch" path="/api/v1/namespaces/external-accounts " resourceVersion="17603423543179000" timeout="7m10s"

```
{



"time":"2025-11-01T13:03:00Z",



level":"INFO",



"content":"time=\"2025-10-13T08:44:57Z\" level=info msg=\"No status changes. Skipping patch\" application=argocd/unguard-dev-root",



"userId":123



}
```

No status changes. Skipping patch

## Display or hide **Log message** column

By default:

* The **Log message** column is displayed
* The **content** column is hidden

To display or hide the **Log message** column (or any other available columns)

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Run a query to fetch logs.
3. In the upper-right corner of the results table, select  **Column settings**.
4. In the **Columns** window, select or clear checkboxes to display or hide the corresponding columns in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.

   * Use the  search box to help you find columns.
   * Use the  and  controls to change the display order of the columns.
5. Select **Apply** to save your changes and close the **Columns** window.

## How a log message is extracted

A log message is extracted from the log record as part of executing a query and does not incur additional costs against your license. If no message is found from the attributes listed below, the **content** field is displayed as a fallback.

### First-level attributes

For certain technologies, or as a result of your parsing rules, the field with the log message is accessible as a first-level attribute in the log record. The log message is extracted from the following first-level attributes:

* `msg`
* `message`
* `event`
* `description`
* `details`

For your log sources ingested to Dynatrace over the API, write the log message to any of the previous attributes during logging for best results.

As an alternative, extract that readable information to a first-level attribute with just a few steps in an OpenPipeline processor. For details, see [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

### Structured JSON logs

Many loggersâsuch as GCP, Serilog, and log4netâor cloud logging frameworks provide information as structured JSON. When this structured log is stored in the **content** field in Dynatrace, the log message is extracted from the following standard JSON keys:

* `message`
* `@message`
* `msg`
* `@mt`
* `@m`
* `body`
* `eventName`
* `textPayload`
* `protoPayload.@type`
* `protoPayload.message`
* `textPayload.message`
* `jsonPayload.message`
* `messageObject.message`
* `properties.message`
* `properties.statusMessage`
* `properties.status.additionalDetails`
* `properties.log`
* `properties.Result`
* `status`

### Unstructured logs

When your log source outputs information following the popular logfmt styling, the log message is extracted from the unstructured log in the **content**.

The log message is detected in a key/value pair for the following keys:

* `msg`
* `message`
* `Message`