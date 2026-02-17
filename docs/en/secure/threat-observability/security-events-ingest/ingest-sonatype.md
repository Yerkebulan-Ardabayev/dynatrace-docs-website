---
title: Ingest Sonatype Lifecycle security events and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-sonatype
scraped: 2026-02-17T04:58:11.636475
---

# Ingest Sonatype Lifecycle security events and audit logs

# Ingest Sonatype Lifecycle security events and audit logs

* Latest Dynatrace
* Extension
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Sonatype Lifecycle security events and audit logs into Dynatrace as security events.

## Get started

### Overview

Dynatrace integration with [Sonatype Lifecycleï»¿](https://www.sonatype.com/products/open-source-security-dependency-management) allows users to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

Sonatype offers a range of products to help developers improve their productivity. The [Sonatype Lifecycle productï»¿](https://help.sonatype.com/en/sonatype-lifecycle.html) identifies vulnerabilities in development artifacts, such as code and containers. The Dynatrace platform observes the corresponding runtime entities associated with those artifacts. Ingesting and enriching vulnerability findings helps users to better focus on the top risks that affect their production applications.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

See below for the [Sonatype Lifecycle](#sonatype) and [Dynatrace](#dt) requirements.

#### Sonatype Lifecycle requirements

To enable the extension to collect security data from Sonatype Lifecycle, authentication credentials with appropriate permissions are required. There are two options to provide credentials:

* **Option 1**: [User tokenï»¿](https://help.sonatype.com/en/iq-server-user-tokens.html) Recommended

  + Recommended for service users.
  + Consists of a user code and a passcode.
  + These are disposable credentials that can be revoked at any time without impacting the associated user account.
* **Option 2**: Username and password

  + Uses your accountâs standard login credentials.

**Required permissions**:

To ensure successful data collection, the authenticated user must have the following permissions in Sonatype Lifecycle:

* `View IQ Elements`
* `Access Audit Log` (required only if audit log ingestion is configured)

#### Dynatrace requirements

* ActiveGate version 1.313+ that needs to be able to

  + Run Extensions 2.0 framework
  + Reach the Sonatype API endpoints
* Permissions: For a list of permissions required, go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
* Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Sonatype Lifecycle** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="Sonatype Lifecycle"
     ```
   * For finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Sonatype Lifecycle"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Sonatype Lifecycle"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![how it works - sonatype](https://dt-cdn.net/images/architechture-diagram-2560-277696e6e1.png)

Dynatrace integration with Sonatype Lifecycle is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Sonatype Lifecycle extension

1. It periodically collects security findings and audit logs using [Sonatype REST APIï»¿](https://help.sonatype.com/en/rest-apis.html).
2. The fetched data is ingested into Dynatrace and mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
3. Data is stored in a bucket called `default_securityevents` (for details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which data model is used for the security logs and events coming from Sonatype Lifecycle?

* [Vulnerability finding events](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by Sonatype Lifecycle per affected artifacts and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual artifacts.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent user activity logs in Sonatype Lifecycle.

### Which Sonatype Lifecycle security findings are imported into Dynatrace?

* On the first ingest, we consider findings updated in the last `m` hours, where `m` is the first ingest interval configured in the monitoring configuration.
* If the extension is configured to ingest data at an interval of `n` hours, then whenever the extension runs all vulnerability findings updated in the last `n` hours will be ingested.
* If no new or updated findings were detected, no findings will be ingested.

### Which extension fields are added to the core fields of the events ingested from Sonatype Lifecycle?

The `sonatype` namespace is added for extracting several Sonatype-specific attributes for user convenience on top of the original issue JSON, which is stored in the `event.original_content` field.

**Examples**:

* `sonatype.application_public_id` represents the friendly name of the assessed application.
* `sonatype.application_internal_id` represents the ID of the assessed application.
* `sonatype.commit_hash` represents the hash of a code commit that the assessment belongs to.
* `sonatype.stage` represents the application stage at which the assessment was performed.

### What Sonatype Lifecycle asset types are supported by Dynatrace for runtime contextualization?

`CODE_ARTIFACT`: All the findings from Sonatype Lifecycle coming from the assessment of code artifacts are mapped set with `CODE_ARTIFACT` value in the `object.type` field, and the `software_component` namespace is added with the corresponding fields:

* `software_component.purl` represents the package URL of the vulnerable software component.
* `software_component.ecosystem` represents the ecosystem of the component, such as maven, npm, and others.
* `software_component.type` represents the type of the vulnerable software component.
* `software_component.name` represents the name of the vulnerable library within a code artifact.
* `software_component.version` represents the version of the vulnerable component.

### How is the risk score for Sonatype Lifecycle findings normalized?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

The Dynatrace risk levels and scores are mapped from the original Sonatype Lifecycle scores.

* `dt.security.risk.score` - is mapped from the Sonatype Lifecycle provided severity score to static scores.
* `dt.security.risk.level` - is mapped from the Sonatype Lifecycle severity score and mapped from the original values in `finding.score`.

| `dt.security.risk.score` (mapped from `finding.score`) | `dt.security.risk.level` (mapped from `dt.security.risk.score`) |
| --- | --- |
| 9.0-10.0 | CRITICAL |
| 7.0-8.9 | HIGH |
| 4.0-6.9 | MEDIUM |
| 0.1-3.9 | LOW |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Sonatype vulnerability findings, scans, and audit logs.](https://www.dynatrace.com/hub/detail/sonatype-lifecycle)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")