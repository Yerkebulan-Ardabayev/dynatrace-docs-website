---
title: Ingest SonarQube security and quality events, metrics, and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data
scraped: 2026-02-16T21:20:31.743633
---

# Ingest SonarQube security and quality events, metrics, and audit logs

# Ingest SonarQube security and quality events, metrics, and audit logs

* Latest Dynatrace
* Extension
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest SonarQube security and quality events, metrics, and audit logs into Dynatrace as security events.

## Get started

### Overview

The Dynatrace integration with [SonarQubeï»¿](https://www.sonarsource.com/) allows you to unify and contextualize vulnerability findings across DevSecOps tools and products, enabling central prioritization, visualization, and automation of security findings.

SonarQube generates vulnerability findings on development artifacts like code and configuration files. The Dynatrace platform observes the corresponding runtime entities associated with those artifacts. Ingesting and enriching vulnerability findings helps users to better focus on the top risks that affect their production applications.

In this integration, in addition to the audit logs and security events, Dynatrace ingests various SonarQube quality metrics and generates Software Development Lifecycle (SDLC) events to represent assessments of artifacts done within the SDLC pipeline. This allows Dev teams to get a more exhaustive overview of the quality of their applications and services. It also allows SREs to have better visibility and control over the quality of the deployed artifacts from various quality perspectives.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Requirements

[SonarQube Server Web API v1ï»¿](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/)

#### SonarQube requirements

* [Generate an API tokenï»¿](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/managing-tokens/#generating-a-token) with the system administrator and `Browse` permissions on the projects to monitor.

#### Dynatrace requirements

* ActiveGate version 1.313+ that needs to be able to

  + Run Extensions 2.0 framework
  + Reach the SonarQube API endpoint URL
* Permissions: For a list of permissions required, go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
* Generate an access token with the `openpipeline.events_security` and `openpipeline.events_sdlc` scopes and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **SonarQube** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="SonarQube"
     ```
   * For security finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="SonarQube"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For security scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="SonarQube"



     AND event.type=="VULNERABILITY_SCAN"
     ```
   * For SDLC events:

     ```
     fetch events



     | filter event.kind == "SDLC_EVENT"



     AND event.type == "control"



     | filter event.provider=="SonarQube"
     ```
   * For metrics:

     ```
     timeseries {



     Vulnerabilities = sum(sonarqube.code.vulnerabilities),



     Hotspots = sum(sonarqube.security.hotspots),



     `Hotspots reviewed` = sum(sonarqube.security.hotspots.reviewed),



     Bugs = sum(sonarqube.bugs),



     Coverage = sum(sonarqube.code.coverage),



     `Duplicated lines` = sum(sonarqube.code.duplication),



     `Code smells` = sum(sonarqube.code.smells)



     }, interval:3h
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![mechanism sonarqube](https://dt-cdn.net/images/architecture-diagram-1-2560-7fb217b566.png)

Dynatrace integration with SonarQube is an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") running on Dynatrace ActiveGate. Once you enable and configure the Dynatrace SonarQube extension

1. It periodically collects security findings and audit logs using [SonarQube Web API v1ï»¿](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/).
2. The fetched data is ingested into Dynatrace and mapped to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
3. Data is stored in a bucket called `default_securityevents` (for details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## FAQ

### Which data model is used for the security logs and events coming from SonarQube?

* [**Vulnerability finding events**](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by SonarQube per affected artifacts and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual artifacts.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent user activity logs in SonarQube.
* **SDLC control events** indicate a control validation run.

### Which SonarQube security findings are imported into Dynatrace?

* If the extension is configured to ingest data at an interval of `n` hours, whenever the extension runs, all security findings generated in the last `n` hours will be ingested.
* On the first ingest, all findings updated in the last `m` hours are considered, where `m` is the first ingest interval configured in the monitoring configuration.
* If no scans occurred, no findings are ingested, even if the project has open issues.

### Which extension fields are added on top of the core fields of the events ingested from SonarQube?

The `sonarqube` namespace is added for extracting several SonarQube-specific attributes for user convenience on top of the original issue JSON, which is stored in the `dt.raw_data` field.

Example fields:

* `sonarqube.project.name`
* `sonarqube.project.id`
* `sonarqube.revision`
* `sonarqube.revision.author`
* `sonarqube.tags`
* `sonarqube.component`

### What SonarQube asset types are supported by Dynatrace for runtime contextualization?

`CODE_ARTIFACT`: All findings from SonarQube are generated by vulnerability assessments of code artifacts set with the `CODE_ARTIFACT` value in the `object.type` field. The `artifact` and `code` namespaces are added with the corresponding fields:

* `artifact.repository.name`: the repository name which hosts the artifact.
* `artifact.path`: the full path of the file representing the code artifact.
* `code.filepath`: includes the version of the vulnerable component.
* `code.line.number`: the line number where issue has been detected.
* `code.line.offset.start`: the first character number within the line with the issue.
* `code.line.offset.end`: the last character number within the line with the issue.
* `code.line.start`: the line number where the issue starts. Same as `code.line.number`.
* `code.line.end`: the line number where the issue ends.

### How do we normalize the risk score for SonarQube findings?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

The Dynatrace risk levels and scores are mapped from the original [SonarQube severitiesï»¿](https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/issues/#issue-severity).

* `dt.security.risk.level` is taken from the SonarQube severity level and mapped from the original values in `finding.severity`.
* `dt.security.risk.score` is mapped from the SonarQube provided severity level to static scores.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `dt.security.risk.level`) |
| --- | --- |
| BLOCKER/CRITICAL/HIGH  HIGH | 8.9 |
| MEDIUM/MAJOR  MEDIUM | 6.9 |
| MINOR/INFO/LOW  LOW | 3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest SonarQube vulnerability findings, metrics, and audit logs.](https://www.dynatrace.com/hub/detail/sonarqube)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")