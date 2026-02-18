---
title: Ingest Tenable vulnerability findings, scan events, and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data
scraped: 2026-02-18T21:22:17.387178
---

# Ingest Tenable vulnerability findings, scan events, and audit logs

# Ingest Tenable vulnerability findings, scan events, and audit logs

* Latest Dynatrace
* Extension
* Updated on Sep 30, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Tenable vulnerability findings, scan events, and audit logs into Dynatrace as security events.

## Get started

### Overview

[Tenableï»¿](https://dt-url.net/2o23xof) provides robust solutions for identifying, prioritizing, and addressing vulnerabilities, which are crucial for reducing cyber risks and securing digital infrastructure. Integrating Tenable findings into Dynatrace can enhance your overall security posture by ensuring comprehensive visibility and streamlined vulnerability management.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

#### Supported Tenable products

* [Tenable Vulnerability Managementï»¿](https://dt-url.net/fy43w0l) (for vulnerabilities and scan events)
* [Tenable Web App Scanningï»¿](https://dt-url.net/og63xed) (for vulnerabilities and scan events)
* [Tenable Oneï»¿](https://dt-url.net/c703wbm) (for audit logs)

  (more coming soon)

#### Tenable requirements

* [Generate an API access and secret keyï»¿](https://dt-url.net/77i3w5n) with the following roles:

  + **Basic** for vulnerability management and web app scanning

    To get full scan details, ensure that the API key configured has access to read scans and scan history as well. See [APIs used to fetch data](#apis) for details of the APIs required.
  + **Administrator** or **Custom** for audit logs

  For details, see [Tenable-Provided Roles and Privilegesï»¿](https://dt-url.net/rv63woq).

#### Dynatrace requirements

* ActiveGate version 1.299+
* Permissions:

  + To run ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Tenable** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For vulnerabilities and asset scans:

     ```
     fetch security.events



     | filter dt.system.bucket=="default_securityevents"



     | filter event.provider == "Tenable"
     ```
   * For audit logs:

     ```
     fetch logs



     | filter log.source == "Tenable"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

Now you can [visualize findings](#visualize), [analyze audit logs](#analyze) and [automate notifications](#automate).

## Details

### How it works

![how tenable integration works](https://dt-cdn.net/images/2024-12-18-16-47-03-1173-dd965318f4.png)

Dynatrace integration with Tenable is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Tenable extension

1. It periodically reaches out to Tenable products and fetches the new findings, scans, and audit logs from the [Tenable APIs](#apis).

   APIs used to fetch data

   * APIs for vulnerability management:

     + [Export assetsï»¿](https://dt-url.net/6c23wk1)
     + [List scansï»¿](https://dt-url.net/qr43wwo)
     + [List scan historyï»¿](https://dt-url.net/ph63wgp)
     + [Get scan detailsï»¿](https://dt-url.net/bs83wh5)
     + [Get asset detailsï»¿](https://dt-url.net/j0a3w41)
     + [Export vulnerabilitiesï»¿](https://dt-url.net/hac3w16)
   * API for audit logs:

     + [View activity logï»¿](https://dt-url.net/dse3wjb)
   * API for web app scanning:

     + [Search scan configurationsï»¿](https://dt-url.net/ig03xj1)
     + [Search scansï»¿](https://dt-url.net/fi23xnz)
     + [Export findingsï»¿](https://dt-url.net/c443xfn)
2. The fetched data is ingested into Dynatrace and mapped to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/z1c3xsm).
3. Data is stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Visualize

1. Open ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** and go to **Tenable**.
2. In **Extension content**, select the desired [ready-made dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents/ready-made-dashboards "Use ready-made dashboards to visualize your data right out of the box.").
3. In the **Product** filter, select **Tenable** to view data reported by Tenable, such as critical vulnerabilities and affected objects.

   ![filter for tenable product](https://dt-cdn.net/images/2024-12-11-20-34-24-686-e8338d8bd3.png)

Example result:

![tenable filtered dashboard](https://dt-cdn.net/images/umsaywsjuo-4308-76ecd2e8b2.png)

### Analyze

Open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to [query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") ingested data, using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

For examples of how you can build your queries, see below.

#### Query for logs over time by action

```
fetch logs



| filter log.source == "Tenable"



| makeTimeseries logs=countDistinctExact(id), by:{audit.action}, time:{toTimestamp(received)}, interval:{3h}
```

Example result:

![Logs over time by action](https://dt-cdn.net/images/image-20241209-153005-1988-af39449c8c.png)

#### Query for vulnerability distribution by risk level

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_FINDING"



| filter event.provider == "Tenable"



| dedup {object.id, vulnerability.id}, sort:{timestamp}



| summarize Vulnerabilities=countDistinctExact(vulnerability.id), by:{dt.security.risk.level}



| fieldsAdd order=if(dt.security.risk.level=="CRITICAL", 1, else:



if(dt.security.risk.level=="HIGH", 2, else:



if(dt.security.risk.level=="MEDIUM", 3, else:



if(dt.security.risk.level=="LOW", 4, else:5))))



| sort order asc
```

Example result:

![Vulnerability distribution by risk level](https://dt-cdn.net/images/2024-12-11-19-40-07-1277-3f2f43c90a.png)

#### Query for top 10 scans with the most host coverage

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_SCAN"



| filter event.provider == "Tenable"



| dedup {object.id, scan.id}



| summarize Hosts=countDistinctExact(object.id), by:{scan.name}



| sort Hosts desc



| limit 10
```

Example result:

![Query for top 10 scans with the most host coverage](https://dt-cdn.net/images/2024-12-11-19-42-02-1753-871fb9630c.png)

### Automate notifications

1. Download our [sample workflow for Jiraï»¿](https://dt-url.net/od23qa1) or [sample workflow for Slackï»¿](https://dt-url.net/ko43qsm).
2. Open [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.
3. Adjust the workflow to your needs to create notifications for critical Tenable findings.

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

## FAQ

### Why does my configuration show an error?

Error message: `Failed to assign monitoring configuration to ActiveGate. Reason: Extension com.dynatrace.extension.tenable(<version-number>) not available in cache yet (queued for download)`

If your configuration shows the error message above, it simply means that ActiveGate is still downloading the extension for the cluster. The status should change after a few minutes.

### Why do I see duplicate events?

Duplicate events in the Tenable extension are likely due to the first ingest running multiple times. When a monitoring configuration is assigned to an ActiveGate, the first execution will run an export for a longer timeframe (configurable in the monitoring configuration settings). Anytime the extension is restarted (due to an update, ActiveGate reset, failover, and so on), the first ingest will run again.

You can run a DQL query and [**dedup**](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#dedup "DQL filter and search commands") the events using the `object.id`, `scan.id`, and `finding.id` fields.

* For `VULNERABILITY_FINDING`, the unique ID is `{object.id, finding.id}`.
* For `VULNERABILITY_SCAN`, the unique ID is `{object.id, scan.id}`.

Example:

```
fetch security.events



| filter dt.system.bucket=="default_securityevents"



| filter event.type == "VULNERABILITY_FINDING"



| filter event.provider == "Tenable"



| dedup {object.id, finding.id}, sort:{timestamp}
```

### Why do some scan events have the same start and end times?

When fetching vulnerabilities, the Tenable extension attempts to match the data with recent scan executions. If the scan mentioned in the Tenable vulnerability can't be found (for example, due to missing permissions), the extension creates a scan event based on this finding. These scan events have the same start and end times as when the vulnerability was found.

### Why isn't my data ingested?

If you installed and configured the extension, but data isnât being ingested, follow the steps below.

1. Open the extension and go to **Health** to check the status of the monitoring configuration.
2. If the status isnât `OK`, scroll down to **Logs** and select **Run query** to see the error information.
3. If the error information isnât enough, or the status shows `OK` but you're still not getting data, extract a support archive from ActiveGate to troubleshoot further.

   How to extract a support archive

   1. Find the ActiveGate ID for the ActiveGate running the configuration and extract a support archive. For details, see [ActiveGate diagnostics: Collect and review locally](/docs/ingest-from/dynatrace-activegate/activegate-diagnostics#collect-and-review-locally "Learn how to run ActiveGate diagnostics").
   2. Unzip the support archive and find the extension log file at `COLLECTOR/<id>/remotepluginmodule/log/extensions/datasources/com.dynatrace.extension.tenable/python3.log`.
4. If the information there is still not sufficient for troubleshooting, enable the `Debug logs` flag in the monitoring configuration and contact Dynatrace Support.

Common causes for missed data ingest include:

* No connectivity between the ActiveGate and Tenable cloud

  **Suggestion**: Attempt to curl the Tenable cloud URL from the ActiveGate to ensure connectivity is working.
* Wrong access and/or secret key

  **Suggestion**: Double-check the credentials configured on the monitoring configuration.
* Missing permissions on the API user

  **Suggestion**: Ensure that the API user can call the [APIs used to fetch data](#apis).

## Which extension fields are added on top of the core fields of the events ingested from Tenable?

The `tenable` namespace is added for extracting several Tenable-specific attributes for user convenience on top of the original issue JSON, which is stored in the `event.original_content` field.

**Examples**:

* `tenable.vpr`
* `tenable.last_found`
* `tenable.first_found`
* `tenable.last_fixed`

## What Tenable asset types are supported by Dynatrace for runtime contextualization?

`HOST` - all the findings from Tenable Vulnerability Management coming from hosts scans are mapped with the `HOST` value in the `object.type` field, and the `host` namespace is added with the corresponding fields:

* `host.name` represents the host name as detected by Tenable.
* `host.ip` represents the host IP address scanned by Tenable.
* `host.fqdn` represents the host FQDN as resolved by Tenable.

Runtime contextualization can be done from the `host.ip` field.

### How is the risk score for Tenable findings normalized?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

The Dynatrace risk levels and scores are mapped from the original [Tenable severityï»¿](https://dt-url.net/j103w2v).

Tenable uses the VPR score. However, the severity levels are set from CVSS scores (v2 or v3, depending on the [configurationï»¿](https://dt-url.net/tg23we5)). Therefore, Dynatrace maps the severity to the risk level and then assigns the appropriate risk score based on it.

* `dt.security.risk.level` is taken from the Tenable severity level and mapped from the original values in `finding.severity`.
* `dt.security.risk.score` is mapped from the mapped risk level to a set of static scores.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `dt.security.risk.level`) |
| --- | --- |
| critical -> CRITICAL | 10.0 |
| high -> HIGH | 8.9 |
| medium -> MEDIUM | 6.9 |
| low -> LOW | 3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Tenable vulnerability findings, scan events, and audit logs.](https://www.dynatrace.com/hub/detail/tenable/)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")