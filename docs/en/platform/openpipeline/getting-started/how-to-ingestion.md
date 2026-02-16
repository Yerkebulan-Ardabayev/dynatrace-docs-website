---
title: How to ingest data (events)
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/how-to-ingestion
scraped: 2026-02-16T09:16:32.312673
---

# How to ingest data (events)

# How to ingest data (events)

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Sep 16, 2025

This guide shows you how to ingest an event in Grail via the `platform/ingest/v1/events` endpoint and verify that it's persisted.

The event we will ingest is

```
{



"name": "My first ingested event"



}
```

## Who this is for

This article is intended for development teams managing data ingestion.

## Before you begin

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license that includes [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Authenticate**](/docs/platform/openpipeline/getting-started/how-to-ingestion#authenticate "How to ingest data for a configuration scope in OpenPipeline.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Copy the endpoint path**](/docs/platform/openpipeline/getting-started/how-to-ingestion#path "How to ingest data for a configuration scope in OpenPipeline.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Send an event**](/docs/platform/openpipeline/getting-started/how-to-ingestion#send "How to ingest data for a configuration scope in OpenPipeline.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Verify ingestion**](/docs/platform/openpipeline/getting-started/how-to-ingestion#verify "How to ingest data for a configuration scope in OpenPipeline.")

### Step 1 Authenticate

The `platform/ingest/v1/events` uses access token authentication. To generate an access token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a token name.
4. Find and select the **OpenPipeline â Ingest Events** (`openpipeline.events`) scope.
5. Select **Generate token**.
6. Select **Copy** and then paste the token to a secure location. It's a long string that you need to copy and paste back into Dynatrace later.

### Step 2 Copy the endpoint path

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Events** > **Ingest sources**.
2. Find the ingest source you are interested in.
3. In the **Endpoints path** column, select the endpoint name > ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy**.

### Step 3 Send an event

Run the following sample command to send an event to your environment endpoint `platform/ingest/v1/events` via `POST` request.

The sample command indicates a JSON content type and provides the JSON event data using the `-d` parameter. Make sure to substitute

* `<your-endpoint-URL>` with the URL of the endpoint you copied. It looks like `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events`.
* `<your-API-token>` with the token you generated.
* `My first ingested event` with the name of your event.

```
curl -i -X POST "<your-endpoint-URL>" \



-H "Content-Type: application/json" \



-H "Authorization: Api-Token <your-API-token>" \



-d "{\"name\":\"My first ingested event\"}"
```

Your request is successful if the output contains the 202 response code, for example

```
HTTP/2 202
```

### Step 4 optional Verify ingestion

To verify that your event has been ingested successfully, query it via DQL, for example in **Notebooks**.

1. Go to **Notebooks**.
2. Choose or create a notebook.
3. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** to add a new section with a DQL query input field.
4. Enter the following DQL query

   Make sure to substitute `My first ingested event` with your event name.

   ```
   fetch events



   | filter name == "My first ingested event"
   ```

Your query is successful if the output is a record containing a timestamp, an ingest source, and a name, for example

![Verify event ingest in Notebooks](https://dt-cdn.net/images/verify-event-ingest-1200-05f1ad9526.webp)

## Learn more

OpenPipeline is the unified ingestion component for the Dynatrace Platform. You can ingest various configuration scopes via APIs. To ingest records for a configuration scope via API, you need to

1. Authenticate.
2. Copy the endpoint path.
3. Send a record.
4. Verify ingestion.

For an overview of the available endpoints, refer to [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.").

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")