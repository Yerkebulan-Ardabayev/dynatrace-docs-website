---
title: Push logs with Cloudflare
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-push-logs-with-cloudflare
scraped: 2026-02-24T21:31:34.111761
---

# Push logs with Cloudflare

# Push logs with Cloudflare

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Oct 15, 2025

Cloudflare Logpush supports pushing logs directly to Dynatrace.
You can configure Logpush via the Cloudflare dashboard or via API.

## Prerequisites

Before you configure Cloudflare Logpush, you need the following:

* A Dynatrace API token with the `logs.ingest` scope.
  For more information about tokens, generation, and scopes, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").
* The base URL for your Dynatrace HTTP logs intake.
  An example base URL is `https://abc123.live.dynatrace.com`.

  This is required only if you configure Logpush via API.
* A Cloudflare role with **Log Share** edit permissions.
  For more information, see [Rolesï»¿](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

For more information about the Dynatrace logs ingest API, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Steps

Configure Logpush either via the Cloudflare dashboard or the API.

The Dynatrace API destination may not be backwards-compatible with older jobs.

* If you expect to send your logs directly to Dynatrace, we recommend that you a new job instead of modifying an existing job.
* If you try to change the destination in an existing job, you may observe errors.

### Configure via the Cloudflare dashboard

1. Create the Logpush job

1. Log into your [Cloudflare dashboardï»¿](https://dash.cloudflare.com/login).
2. Select the Enterprise account or domain/zone that you want to use with Logpush.

   * Account: You have access to [account-scoped datasetsï»¿](https://developers.cloudflare.com/logs/reference/log-fields/account/).
   * Domain/zone: You have access to [zone-scoped datasetsï»¿](https://developers.cloudflare.com/logs/reference/log-fields/zone/).
3. Go to **Analytics & Logs** > **Logpush**.
4. Select **Create a Logpush job**.

2. Define the Dynatrace API endpoint

1. While still in your Cloudflare dashboard, select the dataset that you want to push to the storage service.
2. In **Select a destination**, select **HTTP Destination** (or **Dynatrace**, if available).
3. Enter the destination details: the Dynatrace HTTP logs ingest API endpoint for your environment, with the Dynatrace API token and required headers provided as query parameters.

   An example destination is shown below.

   ```
   https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare
   ```
4. Select **Continue**

3. Configure the Logpush job

1. While still in your Cloudflare dashboard, select the dataset that you want to push to the storage service.
2. Configure your Logpush job.

   * **Job name**: Enter a name of your choosing.
   * **If logs match**: Select the events that you want to be included or removed from your ingested logs.
     This option is not available for all datasets.
     For more information, see [Filtersï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/).
   * **Send the following fields**: Choose which logs to push, whether all logs or only select fields.
   * **Advanced Options**:

     + Choose the timestamp format in your logs.
       Options are `RFC33339` (default), `Unix`, or `UnixNano`.
     + Choose a specific sampling rate, or push a randomly-sampled percentage of logs.
       For more information, see [Sampling rateï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#sampling-rate).
     + Enable redaction for `CVE-2021-44228`.
       This will replace every instance of `${` with `x{`.
3. When you are done configuring your job, select **Submit**.

### Configure via API

1. Create a job

To create a job, make a `POST` request to the Logpush jobs endpoint.
An example request using `cURL` is shown in the code block below:

```
$ curl -s https://api.cloudflare.com/client/v4/zones/<ZONE_TAG>/logpush/jobs -X \



-H "X-Auth-Email: <CLOUDFLARE_EMAIL>" \



-H "X-Auth-Key: <CLOUDFLARE_API_KEY>" \



POST -d '{



"name": "dynatrace",



"logpull_options": "fields=ClientIP,EdgeStartTimestamp,EdgeResponseStatus,EdgeResponseBytes,ClientRequestURI,ClientRequestHost,ClientRequestMethod,ClientRequestPath&timestamps=rfc3339",



"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"dataset": "http_requests",



"enabled": true,



"output_options": { "output_type": "ndjson", "batch_prefix": "[", "batch_suffix": "]", "record_delimiter": ","}



}'
```

Replace the following placeholders with the appropriate values:

* `name`: Use your domain name as the job name. Optional
* `destination_conf`: The Dynatrace HTTP logs ingest API endpoint for your environment, with the Dynatrace API token and required headers provided as query parameters.

  + `<ZONE_TAG>`: A hexadecimal identifier that is available from Cloudflare.
  + `<CLOUDFLARE_EMAIL>`: A Cloudflare email address.
  + `<CLOUDFLARE_API_KEY>`: A Cloudflare API key.
  + `<CLOUDFLARE_BASIC_AUTHORIZATION>`: A Cloudflare authorization key.
  + `<DYNATRACE_BASE_URL>`: The Dynatrace HTTP logs intake endpoint for your environment, as described in [Prerequisites](#prerequisites).
  + `<DYNATRACE_API_TOKEN>`: An API token that has the `logs.ingest` scope, as described in [Prerequisites](#prerequisites).
* `dataset`: The category of logs that you want to receive.
  For a full list of supported datasets, see [Datasetsï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).
* `output_options`: Configure fields, sample rate, and timestamp format. Optional
  For more information, see [Log Output Optionsï»¿](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/).

An example JSON response is shown in the code block below.

```
{



"errors": [],



"messages": [],



"result": {



"id": <JOB_ID>,



"dataset": "http_requests",



"enabled": false,



"name": "<DOMAIN_NAME>",



"output_options": {



"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],



"timestamp_format": "rfc3339"



},



"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"last_complete": null,



"last_error": null,



"error_message": null



},



"success": true



}
```

2. Enable a job

To enable a job, make a `PUT` request to the Logpush jobs endpoint.

An example request using `cURL` is shown in the code block below.

* Use the `<JOB_ID>` from the JSON response, as shown in [Create a job](#create).
* Send `{"enabled": true}` in the request body.

```
$ curl --request PUT \



https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/logpush/jobs/{JOB_ID} \



--header "X-Auth-Email: <CLOUDFLARE_EMAIL>" \



--header "X-Auth-Key: <CLOUDFLARE_API_KEY>" \



--header "Content-Type: application/json" \



--data '{



"enabled": true



}'
```

An example JSON response is shown in the code block below.

```
{



"errors": [],



"messages": [],



"result": {



"id": <JOB_ID>,



"dataset": "http_requests",



"enabled": true,



"name": "<DOMAIN_NAME>",



"output_options": {



"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],



"timestamp_format": "rfc3339"



},



"destination_conf": "https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",



"last_error": null,



"error_message": null



},



"success": true



}
```