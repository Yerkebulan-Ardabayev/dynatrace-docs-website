---
title: Ingest Qualys vulnerability findings, scan events, and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-qualys
scraped: 2026-02-25T21:19:58.097615
---

# Ingest Qualys vulnerability findings, scan events, and audit logs

# Ingest Qualys vulnerability findings, scan events, and audit logs

* Latest Dynatrace
* Extension
* Published Dec 15, 2025
* Preview

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest Qualys vulnerability findings, scan events, and audit logs into Dynatrace as security events.

## Get started

### Overview

Dynatrace integration with Qualys allows users to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

[Qualys Enterprise TruRisk platformï»¿](https://www.qualys.com/enterprise-trurisk-platform) offers a range of products, including [Vulnerability Management, Detection, & Response (VMDR)ï»¿](https://www.qualys.com/apps/vulnerability-management-detection-response), which helps detect and prioritize vulnerabilities for remediation on hosts. The Dynatrace platform observes the corresponding applications and services associated with those hosts. Ingesting and enriching vulnerability findings with runtime context helps users to better focus on the top risks that affect their production applications.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

See below for the [Qualys](#qualys) and [Dynatrace](#dt) requirements.

#### Qualys requirements

To authenticate with a username and password, the user account must have the following permissions:

* **Vulnerability Management module**

  + User Role: **Reader** with API access enabled
  + Asset Groups: access to the relevant asset groups of interest, or to all asset groups
* **Administration module** (needed for the audit log ingest):

  + A **Reader**-type user role is sufficient.
  + To collect activity logs, the role must also include:

    - API access enabled
    - Access to the Administration module (**Action Log Permissions** > **Action Log Access**)

#### Dynatrace requirements

* ActiveGate version 1.310+ that needs to be able to

  + Run Extensions 2.0 framework
  + Reach the Qualys API endpoints
* Permissions: For a list of permissions required, go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
* Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **Qualys** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="Qualys"
     ```
   * For finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Qualys"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="Qualys"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![how it works](https://dt-cdn.net/images/image-20251202-165058-2086-c9122593e9.png)

Dynatrace integration with Qualys is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace Qualys extension

1. It periodically collects security findings and audit logs using [Qualys REST APIï»¿](https://docs.qualys.com/en/vm/api/scans/index.htm#t=get_started%2Fget_started.htm).
2. The fetched data is ingested into Dynatrace and mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.").
3. Data is stored in a bucket called `default_securityevents` (for details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which data model is used for the security events and audit logs coming from Qualys integration?

* [**Vulnerability finding events**](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by Qualys per affected artifacts and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual artifacts.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent user activity logs in Qualys.

### Which Qualys security findings are imported into Dynatrace?

* The Qualys VMDR findings are reported by default.
* On the first ingest run, integration ingests all findings updated in the last `m` hours, where `m` is the first ingest interval configured in the monitoring configuration.
* If the extension is configured to ingest data at an interval of `n` hours, then whenever the extension runs, all vulnerability findings updated in the last `n` hours will be ingested.
* If no new or updated findings were detected, no findings will be ingested.

### Which extension fields are added on top of the core fields of the events ingested from Qualys?

* The `qualys` namespace is added for extracting several Qualys-specific attributes for user convenience on top of the original issue JSON, which is stored in `event.original_content` field.

Example fields:

* `qualys.host.asset_id`: ID assigned to all assets in the subscription that is not exposed in VMDR.
* `qualys.host.tracking_method`: How the host asset is tracked (for example, Cloud Agent, IP, DNS).
* `qualys.detection.first_found`: When the detection was first found on the asset.
* `qualys.detection.last_found` - When the detection was last found on the asset.
* `qualys.detection.times_found`: How many times this detection has been found.
* `qualys.detection.qds_factors`: A map with details on what has contributed to the Qualys Detection Score.

### What Qualys asset types are supported by Dynatrace for runtime contextualization?

`HOST`: all the findings from Qualys VMDR generated from assessment of hosts are mapped set with HOST value in object.type field, and host namespaces are added with the corresponding fields:

* `host.name`: Hostname of the host asset (if available).
* `host.ip`: IP address of the host asset.
* `host.fqdn`: Fully qualified domain name of the host asset (if available).

### How do we normalize the risk score for Qualys findings?

The Dynatrace risk levels and scores are mapped from the original Qualys severities.

* `dt.security.risk.score` is mapped from the Qualys provided severity score to static scores.
* `dt.security.risk.level` is mapped from the Qualys severity score and mapped from the original values in finding.score.

The Qualys Detection Score (QDS) has a range from 1 to 100. To map this to the 10 point Dynatrace security risk score we divide the QDS by 10.

| `dt.security.risk.score` (mapped from `finding.score`) | `dt.security.risk.level` (mapped from `dt.security.risk.score`) |
| --- | --- |
| 9.0-10.0 | CRITICAL |
| 7.0-8.9 | HIGH |
| 4.0-6.9 | MEDIUM |
| 0.1-3.9 | LOW |

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")