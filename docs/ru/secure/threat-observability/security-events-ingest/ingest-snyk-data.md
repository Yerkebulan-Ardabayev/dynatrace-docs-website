---
title: Ingest Snyk vulnerability findings, scans, and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-snyk-data
scraped: 2026-02-21T21:23:58.880546
---

# Ingest Snyk vulnerability findings, scans, and audit logs

# Ingest Snyk vulnerability findings, scans, and audit logs

* Latest Dynatrace
* Extension
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Snyk vulnerability findings, scans, and audit logs into Dynatrace as security events.

## Get started

### Overview

Dynatrace integration with [Snykï»¿](https://dt-url.net/4h03x92) allows you to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

Snyk products ([Snyk Codeï»¿](https://dt-url.net/mr23x60), [Snyk Open Sourceï»¿](https://dt-url.net/7k43x64), [Snyk Containerï»¿](https://dt-url.net/dy63xzt), [Snyk IaCï»¿](https://dt-url.net/6283xq1)) generate vulnerability findings on development artifacts, such as code and containers. The Dynatrace platform observes the corresponding runtime entities associated with those artifacts. Ingesting and enriching vulnerability findings help users to better focus on the top risks that affect their production applications.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* Analyze and detect anomalous user activity Coming soon

### Requirements

See below for the [Snyk](#snyk) and [Dynatrace](#dt) requirements.

#### Snyk requirements

[Generate an API tokenâbased service accountï»¿](https://dt-url.net/6ba3xua) with the required [organization-level permissions on each organizationï»¿](https://dt-url.net/6p03wzw). This can be achieved by creating a custom role (recommended) or assigning the **Organization Admin** or **Group Admin** predefined role to the service account.

**Required permissions**: `View organization`, `View audit logs`, `View container image`, `View project`, `View project history`, `View scans`.

#### Dynatrace requirements

* ActiveGate version 1.299+
* Permissions:

  + To run ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Snyk** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="Snyk"
     ```
   * For finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Snyk"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Snyk"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![how it works](https://dt-cdn.net/images/image-20250210-114410-2266-9b907186a6.png)

Dynatrace integration with Snyk is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Snyk extension

1. It periodically reaches out to Snyk products and fetches the new vulnerability findings, scans, and audit logs.
2. The fetched data is ingested into Dynatrace and mapped to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/z1c3xsm).
3. Data is stored in a bucket called `default_securityevents` (for details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

## FAQ

### Which data model is used for the security logs and events coming from Snyk?

* [**Vulnerability finding events**](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by various Snyk products per affected artifacts and components.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual artifacts.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent user activity logs in Snyk products.

### Which extension fields are added to the core fields of the events ingested from Snyk?

* The `container_image` namespace is added for container findings and scans to store all the container image-related information.
* The `snyk` namespace is added to extract several Snyk-specific attributes on top of the original JSON, which is stored in the `event.original_content` field.

  Examples: `snyk.org.name`, `snyk.project.name`, `snyk.project.tags`, `snyk.target.name`, `snyk.target.reference`, and others.

### Which Snyk issues are imported into Dynatrace?

* If the extension is configured to ingest data at an interval of `n` hours, then whenever the extension runs an ingest, all open issues belonging to projects that had a snapshot taken of them in the last `n` hours will be ingested (on the first ingest, Dynatrace considers all the issues in the previous `m` hours, where `m` is the first ingest interval configured in the monitoring configuration).
* If during the last `n` hours, multiple snapshots were taken for the same project, one set of findings will be ingested **for each snapshot**.
* If no snapshots were taken for a project, no findings will be ingested, even if the project has open issues.

### Why doesn't the number of vulnerability findings in Dynatrace match the number of issues in Snyk?

As explained [above](#imported-issues), issues are ingested each time a project snapshot runs, meaning that if an issue wasn't marked as resolved between snapshot runs, Dynatrace will ingest it twice.

To comply with the Dynatrace Semantic Dictionary, some Snyk issues are split into multiple vulnerability findings when ingested into Dynatrace.

To count the number of Snyk issues from the data in Dynatrace, you can use a `| dedup snyk.issue.id` command.

### What Snyk asset types are supported by Dynatrace for runtime contextualization?



`CONTAINER_IMAGE`: All the findings from Snyk Container coming from the assessment of container images are mapped with the `CONTAINER_IMAGE` value in the `object.type` field, and the `container_image` namespace is added with the corresponding fields:

* `container_image.digest` is set to the container image digest. This value can be used to match the runtime containers.

  For some containers, for example, containers import into Snyk from CLI, the digest is not available.
* `container_image.repository` represents the container repository name.
* `container_image.registry` represents the container registry name.
* `container_image.tags` represents the tags set on the container image.
* `container_image.id` represents the ID of the container image.

For some of the images, for example, those imported from CLI, Snyk doesnât report the container image digest. By default, `container_image.digest` is used for runtime contextualization, but for these cases, `container_image.id` might need to be used.

### How is the risk score for Snyk findings normalized?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

The Dynatrace risk levels and scores are mapped from the original [Snyk severity and scoreï»¿](https://dt-url.net/ek03whg).

* `dt.security.risk.level` is taken from the Snyk severity level and mapped from the original values in `finding.severity`.
* `dt.security.risk.score` is taken from the Snyk severity level and mapped to static scores. The CVSS score (CVSS v3 or v4, for vulnerabilities reported after 2024) reported by Snyk is available in `finding.score`; however, this may not always match the reported severity.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `dt.security.risk.level`) |
| --- | --- |
| critical -> CRITICAL | 10.0 |
| high -> HIGH | 8.9 |
| medium -> MEDIUM | 6.9 |
| low -> LOW | 3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Snyk vulnerability findings, scans, and audit logs.](https://www.dynatrace.com/hub/detail/snyk-1/)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")