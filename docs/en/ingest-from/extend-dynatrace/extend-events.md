---
title: Extend event observability
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-events
scraped: 2026-02-21T21:19:11.823024
---

# Extend event observability

# Extend event observability

* Latest Dynatrace
* 3-min read
* Published Apr 04, 2024

Dynatrace provides a dedicated REST API for the ingestion and management of custom events. The API is available in two principal locations:

* ActiveGate, for event ingestion and querying of existing events
* OneAgent, for event ingestion only

The full API documentation is available at [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

## Manage events with ActiveGate

Dynatrace supports the following API endpoints for querying and ingesting custom events:

| ActiveGate Type | Base URL |
| --- | --- |
| Dynatrace SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/events` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events` |
| Containerized Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/events` |

1

Environment ActiveGates listen by default on port `9999`. If you changed that port, adjust the port in the URL accordingly.

Be sure to specify your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") at the correct location in the URL.

### Authentication

Authentication is handled using an API access token and the [`Authorization`ï»¿](https://developer.mozilla.org/docs/Web/HTTP/Headers/Authorization) HTTP header.

```
Authorization: Api-Token dt.....
```

To obtain an access token, in Dynatrace, go to **Access Tokens**. Depending on whether you want to query or ingest events, your token needs the scopes `events.read` or `events.ingest`, respectively. You can also combine scopes.

For more information on access tokens, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

### Network requirements

* **Unfiltered network ports**

  Make sure the TCP ports used by ActiveGate (either 443 or 9999) are not blocked by a firewall or any other network management solution.
* **Up-to-date SSL trust store**

  To avoid SSL certificate issues with expired or missing root certificates, make sure your system's certificate trust store is up to date.

### curl sample commands

See [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") for a full list of ActiveGate examples for the different request types.

## Send events to OneAgent

In addition to ActiveGate, OneAgent also provides a dedicated HTTP (not HTTPS) endpoint for local-only event ingestion. The following restrictions apply:

* It is a local-only endpoint, exclusively reachable at 127.0.0.1 (localhost)
* Only event ingestion is supported (`POST` request)

Content encoding support

OneAgent does not support content compression using the HTTP header Content-Encoding yet. If you need to use content compression, please export to ActiveGate.

To send events to OneAgent, you first need to enable the Extension Execution Controller (EEC). You can do this globally for the whole environment, for host groups, or only for specific hosts.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

With EEC enabled, the OneAgent installations on the respective hosts will start accepting requests at the URL `http://localhost:14499/v2/events/ingest`.

OneAgent uses by default the TCP port 14499 for this endpoint. You can change the port with [`oneagentctl`](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api#communication-port "Use the Dynatrace API to retrieve the metrics of monitored entities.").

EEC unavailable on container setups

The EEC ingestion endpoint is only available with Full-Stack and Infrastructure Monitoring deployments. It is not available with containerized setups. Use ActiveGate as the export endpoint for container applications.

### Authentication

Being a local-only endpoint, OneAgent does not require authentication.

### Network requirements

* **Unfiltered network ports**

  Being a local-only endpoint, there should not be much network configuration required unless you have restricted local network communication, in which case you need to make sure any such restrictions do not apply to the used TCP port (default 14499).

### curl sample command

The following curl command sends a `POST` request to the local OneAgent endpoint at `/v2/events/ingest`, indicates a JSON content type, and provides the [JSON event data](/docs/dynatrace-api/environment-api/events-v2/post-event#request-body-objects "Ingests an event via the Dynatrace API.") using the `--data` parameter.

```
curl --request POST --url http://localhost:14499/v2/events/ingest --header "Content-type: application/json" --data "{ \"eventType\": \"AVAILABILITY_EVENT\", \"title\": \"Demo title\" }"
```

## Related topics

* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")