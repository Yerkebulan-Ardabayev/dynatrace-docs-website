---
title: Tokens and permissions Classic
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions/tokens-permissions-classic
---

# Tokens and permissions Classic

# Tokens and permissions Classic

* How-to guide
* 4-min read
* Published Sep 11, 2026

Tokens authenticate and authorize API calls, ensuring that only authorized services can interact with your Dynatrace environment. In the context of [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator "Components of Dynatrace Operator") for Kubernetes, two tokens are used:

* **Operator token**  
  The Operator token (former API token) enables the Dynatrace Operator to manage settings and the lifecycle of all Dynatrace components in the Kubernetes cluster.
* **Data Ingest token**  
  The data ingest token enriches and sends additional observability signals (for example, custom metrics) from your Kubernetes cluster to Dynatrace.

## Create token

Repeat the following steps for both the Operator and Data Ingest tokens.

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Provide a meaningful name for the token.
4. Enable the required permissions for the token.

   1. For the Operator token, select the template in **Template** > **Kubernetes: Dynatrace Operator**. This will automatically add the required scopes (see [Operator token](#classic-operatorToken))
   2. For the Data Ingest token, select the template in **Template** > **Kubernetes: Data Ingest**. This will automatically add the required scopes (see [Data Ingest token](#classic-dataIngestToken))
5. Select **Generate token** to create the token.
6. Copy the token and store it in a secure place.

## View token scopes

### Operator token

The Operator token requires the following scopes:

| Scope | Usage | Dynatrace Operator version |
| --- | --- | --- |
| PaaS - Installer (`Installer download`) | Manages OneAgent and ActiveGate lifecycle. | Any version |
| Access problem and event feed, metrics, and topology (API v1 - `DataExport`) | Notifies the Dynatrace Cluster of graceful shutdown. Starting with OneAgent version 1.301, graceful host shutdown is detected without Dynatrace Operator. | <1.6.0 or ≥1.7.1 |
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