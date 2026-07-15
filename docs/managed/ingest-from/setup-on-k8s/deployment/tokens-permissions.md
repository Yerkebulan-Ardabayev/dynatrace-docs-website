---
title: Tokens and permissions
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions
---

# Tokens and permissions

# Tokens and permissions

* How-to guide
* 4-min read
* Updated on Jul 15, 2026

Tokens authenticate and authorize API calls, ensuring that only authorized services can interact with your Dynatrace environment. In the context of [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator "Components of Dynatrace Operator") for Kubernetes, two tokens are used:

* **Operator token**  
  The Operator token (former API token) enables the Dynatrace Operator to manage settings and the lifecycle of all Dynatrace components in the Kubernetes cluster.
* **Data Ingest token**  
  The data ingest token enriches and sends additional observability signals (for example, custom metrics) from your Kubernetes cluster to Dynatrace.

Latest Dynatrace

Dynatrace Classic

Latest Dynatrace

For each Kubernetes cluster, Dynatrace Operator uses two platform tokens associated with a dedicated service user:

* **Operator token** — assigned the **Kubernetes Operator** policy. Manages the lifecycle of all Dynatrace components in the cluster.
* **Data Ingest token** — assigned the **Kubernetes Ingest** policy. Ingests observability signals (metrics, logs, traces) from the cluster.

Token scopes

**Operator token**

| Scope | Usage |
| --- | --- |
| `fleet-management:activegate.connection-info:read` | Collect information for ActiveGate lifecycle |
| `fleet-management:activegate.tokens:create` | Create an authentication token for your ActiveGate to connect to the Dynatrace Cluster |
| `fleet-management:container-images:read` | Read image information for managed components |
| `fleet-management:oneagent.connection-info:read` | Collect information for OneAgent lifecycle |
| `fleet-management:oneagents:download` | Manage OneAgent lifecycle |
| `settings:objects:read` | Read settings for Kubernetes API monitoring, [KSPM](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), and [log monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") |
| `settings:objects:write` | Manage settings for Kubernetes API monitoring, [KSPM](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), and [log monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") |

**Data Ingest token**

| Scope | Usage |
| --- | --- |
| `openpipeline:logs:ingest` | Ingest logs |
| `openpipeline:metrics:ingest` | Ingest metrics |
| `openpipeline:traces:ingest` | Ingest traces |
| `storage:metrics:write` | Write metrics to Dynatrace |

For background on the required concepts, see:

* [Local groups, policies](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Manage service users](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Platform tokens for service users](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")

Platform tokens are created automatically as part of the [Kubernetes Onboarding](/managed/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes") flow — you don't need to create them manually unless you prefer to. To use the onboarding flow, an account administrator must first [grant Kubernetes Onboarding permissions](#grant-privileges) to your user.

## Create tokens

### Create a service user

1. Go to [**Account Management**﻿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Service users**.
3. On the **Service users** page, select  **Add service user**.
4. On the **Create service user** page, enter the following service user details.

   * **Name**
   * Optional **Description**

   Make sure they're both meaningful for environment admins so that they understand the purpose of the service user.
5. In the **Assign permissions** section, select to assign the following permissions **Directly**:

   * Kubernetes Operator
   * Kubernetes Ingest
6. Select **Create**.

### Create platform tokens

Repeat the following steps for both the Operator and Data Ingest tokens.

1. Go to [My platform tokens﻿](https://myaccount.dynatrace.com/platformTokens).
2. Select  **Platform token** and specify:

   * A meaningful **Token Name**
   * **Expiration date**
   * **Account**
   * **Environments** to restrict the token's scope to specific Dynatrace environments
3. Select token scopes in the table.

   * For the Operator token, enable the scopes listed in [Operator token](#operatorToken).
   * For the Data Ingest token, enable the scopes listed in [Data Ingest token](#dataIngestToken).
4. Assign each token to the service user.
5. Select **Generate** to create the token.
6. Copy the token and store it in a secure place. The token is only shown once.
7. Select **Finish and exit**.

## Grant Kubernetes Onboarding permissions to users

Only a Dynatrace account administrator can complete the following steps.

1. Go to [**Account Management**﻿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Group management**.
3. On the **Group management** page, select  **Create group**.
4. On the **New group** page, enter the following group details.

   * **Name**
   * Optional **Description**

   Make sure they're both meaningful for environment admins so that they understand the purpose of the group.
5. In the **Permissions** tab, select  **Add permission**.

   * Select **Kubernetes Onboarding** from the **Permissions** drop down, then choose a **Scope** and **Boundaries** to assign to this group.
6. In the **Members** tab, select  **Add members**.

   * Select members in the **Add members to this group** dialog, then select **Add**.
7. Select **Create**.

## Create token

Repeat the following steps for both the Operator and Data Ingest tokens.

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Provide a meaningful name for the token.
4. Enable the required permissions for the token.

   1. For the Operator token, select the template in **Template** > **Kubernetes: Dynatrace Operator**. This will automatically add the required scopes (see [Operator token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#classic-operatorToken "Configure tokens and permissions to monitor your Kubernetes cluster"))
   2. For the Data Ingest token, select the template in **Template** > **Kubernetes: Data Ingest**. This will automatically add the required scopes (see [Data Ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#classic-dataIngestToken "Configure tokens and permissions to monitor your Kubernetes cluster"))
5. Select **Generate token** to create the token.
6. Copy the token and store it in a secure place.

## View token scopes

### Operator token

The Operator token requires the following scopes:

| Scope | Usage | Dynatrace Operator version |
| --- | --- | --- |
| PaaS - Installer (`Installer download`) | Manages OneAgent and ActiveGate lifecycle. | Any version |
| Access problem and event feed, metrics, and topology (API v1 - `DataExport`) | Notifies the Dynatrace Cluster of graceful shutdown. Starting with OneAgent version 1.301, graceful host shutdown is detected without Dynatrace Operator. | <1.6.0 |
| Read settings (API v2 - `settings.read`) | Manage the ActiveGate object for Kubernetes API monitoring. [2](#fn-1-2-def) | 0.4.0+ |
| Write settings (API v2 - `settings.write`) | Manage the ActiveGate object for Kubernetes API monitoring. [2](#fn-1-2-def) | 0.4.0+ |
| Read entities (API v2 - `entities.read`) | Checks if the ActiveGate object exists for Kubernetes API monitoring. [3](#fn-1-3-def) | 0.4.0 - <1.7.0 |
| Create ActiveGate token (API v2 - `activeGateTokenManagement.create`) | Creates an authentication token for your ActiveGate to connect to the Dynatrace Cluster.[1](#fn-1-1-def) | 0.9.0+ |

1

The token is rotated by Dynatrace Operator every 30 days. When an authentication token is rotated, the affected ActiveGate is automatically deleted and redeployed.

2

Optional since Dynatrace Operator version v1.7.0+.

3

No longer required with Dynatrace Operator version v1.7.0+

### Data Ingest token

Recommended token scopes:

| Scope | Usage | Minimum DTO version |
| --- | --- | --- |
| Ingest metrics (API v2 - `metrics.ingest`) | Enables metadata enrichment for custom metrics. | 0.4.0+ |
| Ingest logs (API v2 - `logs.ingest`) | Send logs through Log Monitoring API v2. | 0.4.0+ |
| Ingest OpenTelemetry traces (API v2 - `openTelemetryTrace.ingest`) | Send OpenTelemetry traces to Dynatrace | 0.4.0+ |