---
title: Ingest Harbor vulnerability findings, scans, and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-harbor-data
scraped: 2026-02-18T21:22:05.768903
---

# Ingest Harbor vulnerability findings, scans, and audit logs

# Ingest Harbor vulnerability findings, scans, and audit logs

* Latest Dynatrace
* Extension
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Harbor vulnerability findings, scans, and audit logs into Dynatrace as security events.

## Get started

### Overview

The Dynatrace integration with [Harborï»¿](https://dt-url.net/hn03wbw) allows you to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

Harbor is a container registry that allows scanning the stored container images with various tools, such as Trivy. It serves the generated vulnerability findings from container images. The Dynatrace platform observes the corresponding runtime entities (the running containers) associated with those images. Ingesting and mapping vulnerability findings to the runtime entities helps users to better focus on the top risks that affect their production applications.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* Analyze and detect anomalous user activity Coming soon

### Requirements

See below for the [Harbor](#harbor) and [Dynatrace](#dt) requirements.

#### Harbor requirements

We recommend using a [robot accountï»¿](https://dt-url.net/my23w6o) for fine-grained authorization. Make sure to

* Store the generated secret for the robot account, as it won't be recoverable after creation
* Refresh the expiry period in due time
* Edit the robot account to enable the permissions below.

| **Permission Type** | **Resource** | **Access Level** |
| --- | --- | --- |
| System permissions | Audit log | List |
|  | Project | List |
|  | Security Hub | List |
| Project permissions | Artifact | List |
|  | Repository | List |

These permissions must be granted for all projects you want Dynatrace to monitor. They ensure Dynatrace can retrieve scan results, audit events, and metadata necessary for accurate vulnerability mapping.

#### Dynatrace requirements

* ActiveGate version 1.300+
* Permissions:

  + To run ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
  + To query ingested data: `storage:security.events:read`.
* Tokens:

  + Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Harbor** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="Harbor"
     ```
   * For finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Harbor"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Harbor"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![ingest mechanism](https://dt-cdn.net/images/image-20250210-114352-2221-6c1861c4fb.png)

Dynatrace integration with Harbor is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Harbor extension

1. It periodically reaches out to Harbor products and fetches the new vulnerability findings, scans, and audit logs.
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

### Why are some scans not being reported?

The Harbor APIs only expose the status of the last completed scan for artifacts. This means that when the extension runs, it can only report the most recent scan that occurred (if any) during the last collection interval.

If the extension is set to collect scan and vulnerability data once per hour and two scans occurred in that last hour, only the details of the most recent one will be reported.

### Which data model is used for the security logs and events coming from Harbor?

* [**Vulnerability finding events**](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by Harbor per container image and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual container images.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent user activity logs in Harbor.

### Which extension fields are added on top of the core fields of the events ingested from Harbor?

The `container_image` namespace is added for container image-related information with the following fields:

* `container_image.digest` represents the container image digest; this value can be used to match to the runtime containers
* `container_image.repository` represents the container repository name
* `container_image.registry` represents the container registry name

The `container_image.tags` field isn't reported by Harbor, so it's not available.

### What Harbor asset types are supported by Dynatrace for runtime contextualization?

`CONTAINER_IMAGE`: All findings from Harbor are generated by vulnerability assessments of container images set with the `CONTAINER_IMAGE` value in the `object.type` field, and the `container_image` namespace is added.

### How do we normalize the risk score for Harbor findings?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

* `dt.security.risk.level` is taken from the severity level set by the configured scanner in Harbor. The values (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, and `NONE`) are mapped as is, with the exception of `Unknown`, which is also mapped to `NONE`.
* `dt.security.risk.score` is mapped to a set of fixed values based on the risk level determined above.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` |
| --- | --- |
| Critical -> CRITICAL | 10.0 |
| High -> HIGH | 8.9 |
| Medium -> MEDIUM | 6.9 |
| Low -> LOW | 3.9 |
| Unknown -> NONE | 0.0 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest Harbor vulnerability findings, scans, and audit logs.](https://www.dynatrace.com/hub/detail/harbor)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")