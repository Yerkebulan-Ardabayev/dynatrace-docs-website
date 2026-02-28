---
title: Ingest GitHub Advanced Security security events and audit logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security
scraped: 2026-02-28T21:19:24.368305
---

# Ingest GitHub Advanced Security security events and audit logs

# Ingest GitHub Advanced Security security events and audit logs

* Latest Dynatrace
* Extension
* Updated on Oct 07, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.

## Get started

### Overview

Dynatrace integration with [GitHub Advanced Securityï»¿](https://github.com/security/advanced-security) (GHAS) enables users to unify and contextualize vulnerability findings across DevSecOps tools and products, facilitating centralized prioritization, visualization, and automation of security findings.

[GitHub Advanced Securityï»¿](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) includes [Code Securityï»¿](https://github.com/security/advanced-security/code-security) and [Secret Protectionï»¿](https://github.com/security/advanced-security/secret-protection) which generate vulnerability findings for development artifacts, such as code and containers. Dynatrace observes the runtime entities associated with those artifacts. Ingesting and enriching vulnerability findings helps users focus on high-impact risks affecting production applications.

The first version of this integration ingests and contextualizes [Dependabot alertsï»¿](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts), which are free for public repositories and part of the Code Security premium offering.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")

### Requirements

See below for the [GitHub](#github) and [Dynatrace](#dt) requirements.

#### GitHub requirements

For the extension to collect security data, authentication credentials with proper permissions are required. You have two options, described below.

GitHub app-based authentication

PAT-based authentication

Recommended

The [GitHub app-based authenticationï»¿](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-token-generated-by-an-app)

* Allows granular permission control
* Can collect organization level audit logs
* Has higher API rate limits

To register and install a GitHub app, follow the steps below.

1. Register the GitHub app

1. Follow the steps in [Registering a GitHub appï»¿](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) with the following values:

* For **GitHub App Name**, enter `DynatraceAppSec-<Your Company>`, making sure to replace `<Your Company>` with your own value.
* For **Homepage URL**, enter `https://dynatrace.com`.
* Clear **Webhook > Active**.
* Enable the following permissions:

  + Repository permissions:

    - **Contents**: `Read-only`
    - **Dependabot alerts**: `Read-only`
    - **Code scanning alerts**: `Read-only` (required when code scanning events are ingested)
    - **Secret scanning alerts**: `Read-only` (required when secret scanning events are ingested)
  + Organization permissions

    - **Administration**: `Read-only` (required for audit logs)
* To set the location where the app will be installed, select one of the following:

  + `Any account` (allows you to install the app in multiple organizations and even user account, which will simplify your monitoring configurations)
  + `Only this account` (the app is installed in the current account; this means you'll need multiple apps and monitoring configurations to cover multiple organizations under an enterprise)

2. Generate a private key for the app

1. Select the **General** tab and go to the newly registered app settings.
2. Copy the client ID (you'll need it when setting up the monitoring configuration).
3. Under **Private keys**, generate a private key (you'll need it when setting up the monitoring configuration)

   The private key allows authenticated requests from the extension; make sure to secure it.

3. Install the app

[Install the GitHub appï»¿](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app) on any accounts (users or organizations) you want to monitor.

The [Personal Access Token (PAT)-based authenticationï»¿](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-personal-access-token)

* Allows a faster setup
* Is suitable for quick integration validation
* Allows audit log collection

  For the [enterprise audit logsï»¿](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28), the authenticated user must be an enterprise admin to use this endpoint.

To generate a Personal Access Token, follow the instructions at [Managing your personal access tokensï»¿](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), making sure to enter the following values:

* The token should be **Classic Personal Access Token**.
* **Expiration**: if you set the token to expire you are responsible for updating it.
* **Scopes**:

  + **repo**: full control
  + **audit\_log**: `read:audit_log`

#### Dynatrace requirements

* ActiveGate version 1.310+ that needs to be able to

  + Run Extensions 2.0 framework
  + Reach the GitHub API endpoint URLs
* Permissions:

  + To run ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Go to  **Hub**, select ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, and display **Technical information**.
  + To query ingested data: `storage:security.events:read`.
* Generate an access token with the `openpipeline.events_security` scope and save it for later. For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Activation and setup

1. In Dynatrace, search for **GitHub Advanced Security** and select **Install**.
2. Follow the on-screen instructions to configure the extension.
3. Verify configuration by running the following queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."):

   * For audit logs:

     ```
     fetch logs



     | filter log.source=="GitHub Advanced Security"
     ```
   * For finding events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="GitHub Advanced Security"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * For scan events:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="GitHub Advanced Security"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. Once the extension is installed and working, you can access and manage it in Dynatrace via ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. For details, see [About Extensions](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

## Details

### How it works

![how it works](https://dt-cdn.net/images/diagram-2560-ac2977ae34.png)

1. Events and logs are collected from GHAS products

The Dynatrace GHAS integration is an extension deployed in a [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") that periodically collects security findings and audit logs using the [GitHub REST APIï»¿](https://docs.github.com/en/rest?apiVersion=2022-11-28).

2. Security findings and logs are ingested into Dynatrace

Security findings are ingested into the Dynatrace platform via a dedicated [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") security ingest endpoint.

3. Security findings and logs are processed and stored in Grail

The OpenPipeline ingest endpoint processes and maps the security findings according to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

These are stored in a bucket called `default_securityevents` (for details, see: [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

Optionally, the collected audit logs are ingested via a dedicated [extensions log ingest pipeline](/docs/analyze-explore-automate/logs/lma-log-ingestion#ingest-extensions "Stream log data to Dynatrace.") and stored in the appropriate [semantic format](/docs/semantic-dictionary/model/log "Get to know the Semantic Dictionary models related to Log Analytics.").

### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

## FAQ

### Which data model is used for the security logs and events coming from GHAS integration?

* [**Vulnerability finding events**](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.") store the individual vulnerability findings reported by various GHAS products per affected artifacts and component.
* [**Vulnerability scan events**](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.") indicate coverage of scans for individual artifacts.
* [**Audit logs**](/docs/semantic-dictionary/model/log#audit-logs "Get to know the Semantic Dictionary models related to Log Analytics.") represent the user activity logs in the GHAS products.

### Which GHAS security findings are imported into Dynatrace?

* If the extension is configured to ingest data at an interval of `n` hours, then whenever the extension runs all security events (Dependabot, code scanning, and secret scanning alerts) updated in the last `n` hours will be ingested.
* On the first ingest, we consider alerts updated in the last `m` hours, where `m` is the first ingest interval configured in the monitoring configuration.
* If no scans occurred, no findings will be ingested, even if the project has open issues. Consult the GitHub documentation for [Dependabotï»¿](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts#detection-of-insecure-dependencies), [code scanningï»¿](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql), and [secret scanningï»¿](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) to see when a scan will occur.

### Which extension fields are added to the core fields of the events ingested from GHAS?

The `github` namespace is added for extracting several GHAS-specific attributes for user convenience on top of the original issue JSON, which is stored in the `event.original_content` field.

**Examples**:

* `github.dependency.relationship`
* `github.dependency.scope`
* `github.epss.percentage`
* `github.epss.percentile`
* `github.ecosystem`

### What GHAS asset types are supported by Dynatrace for runtime contextualization?

`CODE_ARTIFACT`: All the findings from GitHub Advanced Security products coming from the assessment of code artifacts are mapped set with `CODE_ARTIFACT` value in the `object.type` field, and the `artifact` and `component` namespaces are added with the corresponding fields:

* `artifact.repository.name` represents the repository name which hosts the artifact.
* `artifact.path` is the full path of the file representing the code artifact.
* `component.name` represents the name of the vulnerable library within a code artifact.
* `component.version` includes the version of the vulnerable component.

  GitHub only provides limit values and not the exact version, for example, `<1.4`. This limits the possibility of matching runtime components, as the version isn't matched in this case.

### How is the risk score for GHAS findings normalized?

Dynatrace normalizes severity and risk scores for all findings ingested through the current integration. This helps you to prioritize findings consistently, regardless of their source.  
For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").

The Dynatrace risk levels and scores are mapped from the original [GHAS severity and scoreï»¿](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).

* `dt.security.risk.level` - is taken from the GHAS severity level and mapped from the original values in `finding.severity`.
* `dt.security.risk.score` - is taken from the GHAS severity level and mapped to static scores. The CVSS score reported by GHAS is available in `finding.score`; however, this may not always match the reported severity.

| `dt.security.risk.level` (mapped from `finding.severity`) | `dt.security.risk.score` (mapped from `dt.security.risk.level`) |
| --- | --- |
| critical -> CRITICAL | 10.0 |
| high/error -> HIGH | 8.9 |
| medium/warning -> MEDIUM | 6.9 |
| low/note -> LOW | 3.9 |

Secret scanning alerts are assigned a default risk level of HIGH. You can customize this setting in **Advanced options** during the extension configuration.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Ingest GitHub Advanced Security (GHAS) security events and audit logs.](https://www.dynatrace.com/hub/detail/github-advanced-security/)

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")