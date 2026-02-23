---
title: Ingest Akamai security logs and events
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-akamai
scraped: 2026-02-23T21:26:03.761711
---

# Ingest Akamai security logs and events

# Ingest Akamai security logs and events

* Latest Dynatrace
* Extension
* Updated on Aug 25, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Akamai security logs and events into Dynatrace as security events.

## Get started

### Overview

Dynatrace integration with [Akamaiï»¿](https://dt-url.net/3403xsr) allows you to unify and contextualize security findings across tools and products, enabling central prioritization, visualization, and automation.

Akamai products generate security events and detect suspicious network activity. Dynatrace observes the runtime entities protected by those products. Ingesting security events from Akamai products helps users analyze those logs and findings in the context of their runtime production environments.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* Evaluate, triage, and investigate detection findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")
* Analyze network logs and detections Coming soon

### Requirements

See below for the [Akamai](#akamai) and [Dynatrace](#dt) requirements.

#### Akamai requirements

[Create authentication credentials with the proper permissionsï»¿](https://dt-url.net/0gg3xvi)

#### Dynatrace requirements

* ActiveGate version 1.300+
* Permissions:

  + To run ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
  + To query ingested logs: `storage:logs:read`.
  + Optional To query the extracted security events: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Akamai** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For security logs:

     ```
     fetch logs



     | filter log.source=="Akamai SIEM"
     ```
   * For finding events (if you configured the extension to extract detection events):

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Akamai"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![how it works](https://dt-cdn.net/images/image-20250212-154515-3094-1f68916ee3.png)

Dynatrace integration with Akamai is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Akamai extension

1. It periodically reaches out to [Akamai SIEM APIï»¿](https://dt-url.net/wbe3xyb) and fetches the security events.
2. The raw data is ingested into Dynatrace as logs. If security event extraction is configured, detection events are ingested in addition to the logs mapped to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/z1c3xsm).
3. Data is stored as follows:

   * Logs are stored in the `default_logs` bucket
   * Security events are stored in the `default_securityevents` bucket

   For details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

#### Additional integrations

In addition to the extension, you have the following integration options:

* [Monitor application performance with mPulse integration of Dynatrace metricsï»¿](https://dt-url.net/p1i3xuc)
* [Stream Akamai transactional events and metrics via DataStream 2 into Dynatraceï»¿](https://dt-url.net/zek3xcv)

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

self-monitoring

| Metric name | Metric key | Description |
| --- | --- | --- |
| Ingested logs | sfm.akamai-siem.ingested.logs | The number of log records ingested by the extension. |
| Ingested logs bytes | sfm.akamai-siem.ingested.logs\_bytes | The volume of bytes ingested by the extension as logs. |
| Ingested security events | sfm.akamai-siem.ingested.security\_events | The number of security events ingested by the extension. |
| Ingested security events bytes | sfm.akamai-siem.ingested.security\_events\_bytes | The volume of bytes ingested by the extension as security events. |

## FAQ

### Which data model is used for the security logs and events coming from Akamai SIEM integration?

* [Logs](/docs/semantic-dictionary/model/log "Get to know the Semantic Dictionary models related to Log Analytics.") - all the Akamai SIEM data is ingested as logs. The log follows the basic schema for logs with a few relevant extensions of namespaces, such as [`geo`](/docs/semantic-dictionary/fields#geolocation "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), [`http`](/docs/semantic-dictionary/fields#http "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), and [`url`](/docs/semantic-dictionary/fields#url "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").
* [Detection finding events](/docs/semantic-dictionary/model/security-events#detection-finding-events "Get to know the Semantic Dictionary models related to security events.")

### Which extension fields are added on top of the core fields of the events ingested from Akamai?

* The [`geo`](/docs/semantic-dictionary/fields#geolocation "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") namespace maps the corresponding geolocation information of the actor detected in the log.
* The [`http`](/docs/semantic-dictionary/fields#http "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") namespace maps the corresponding HTTP request fields from the monitored transaction.
* The [`url`](/docs/semantic-dictionary/fields#url "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") namespace maps the corresponding web application/URL accessed as the target of the monitored transaction.
* The `akamai` namespace extracts several Akamai-specific fields for user convenience on top of the original JSON content, which is stored in the `log.content` field.

Some extracted fields from which you can benefit include:

* `akamai.config.id`
* `akamai.attackdata.*`

### Which metrics are extracted automatically with the Akamai extension?



| Metric key | Description |
| --- | --- |
| `log.akamai-siem.volumetric-activity` | The count of events matching volume-based activity, such as request rates exceeded or DoS attacks. |
| `log.akamai-siem.deny_count` | The count of events where the rule action is to block the request (deny). |
| `log.akamai-siem.alert_count` | The count of events where the rule action is to allow the request and log a warning (alert). |
| `log.akamai-siem.monitor_count` | The count of events with monitor rule action type. |
| `log.akamai-siem.total-events` | The total number of events processed from Akamai SIEM, regardless of attack type or severity. |
| `log.akamai-siem.slow-posts` | The count of events matching a slow POST attack, which tries to tie up the site using extremely slow requests and responses. |
| `log.akamai-siem.targeted-web-attacks` | The count of events matching specialized web app attacks such as SQL, PHP, command injections, and cross-site scripting. |
| `log.akamai-siem.generic-web-attacks` | The count of events matching generic web app attacks. These include keywords such as `Trojan`, `Web attack tool`, `Web protocol attack`, and `Web platform attack`. |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest logs and security events from Akamai products.](https://www.dynatrace.com/hub/detail/akamai)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")