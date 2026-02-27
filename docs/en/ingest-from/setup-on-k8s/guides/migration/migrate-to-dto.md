---
title: Migrate from OneAgent Operator to Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto
scraped: 2026-02-27T21:18:22.715137
---

# Migrate from OneAgent Operator to Dynatrace Operator

# Migrate from OneAgent Operator to Dynatrace Operator

* Latest Dynatrace
* 5-min read
* Published Apr 01, 2021

## Understand and configure the DynaKube custom resource

The DynaKube custom resource (CR) replaces the OneAgent custom resource. The DynaKube CR follows the "don't repeat yourself" (DRY) principle to deploy a number of different components to your Kubernetes cluster.

Each section includes an illustration of the differences between the two custom resources, what changes from the old custom resource to the new one (marked with green), and what stays the same in both custom resource (marked with blue).

Changing operators will change the host ID calculations for monitored hosts, which will lead to monitoring anomalies in the Dynatrace UI.

### Classic full-stack migration

Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for classic full-stack injection.

![Migration of properties](https://dt-cdn.net/images/classicfullstackmigration-600-fb8529d001.png)

What stays the same

What changes

**Global parameters (`spec`)**  
The following settings are global, shared by every component, and located under `spec`.

* `apiUrl`
* `tokens`[1](#fn-1-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Tokens must point to an existing secret.**

**ClassicFullStack parameters (`.spec.oneAgent.classicFullStack`)**  
A new section for the full-stack OneAgent is located at `.spec.oneAgent.classicFullStack`:

* `image`
* ~~`autoUpdate`~~[1](#fn-2-1-def)
* `version`[2](#fn-2-2-def)

1

Previously, this was `disableAgentUpdate` in the OneAgent CR.  
The `autoUpdate` field has been removed. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).").  
Auto-update is disabled when either the `version` or `image` fields are set.

2

This was `agentVersion` in the OneAgent CR.

All the other OneAgent parameters (such as tolerations, arguments, DNS, and resource settings) are also located in the `.spec.oneAgent.classicFullStack` section and are unique to the full-stack installation.

### Application-only migration

Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for automatic application-only injection.

![Cloud native app only](https://dt-cdn.net/images/cloudnativeappo-600-de0c984048.png)

What stays the same

What changes

**Global parameters (`spec`)**  
The following settings are global, shared by every component, and located under `spec`.

* `apiUrl`
* `tokens`[1](#fn-3-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Tokens must point to an existing secret.**

**ApplicationMonitoring parameters (`.spec.oneAgent.applicationMonitoring`)**  
A new section for the full-stack OneAgent is located at `.spec.oneAgent.applicationMonitoring`:

* `version`[1](#fn-4-1-def)
* `useCSIDriver`[2](#fn-4-2-def)

1

This was `agentVersion` in the OneAgent CR.

2

This new parameter will deliver binaries to pods automatically and eliminate storage requirements on pods. This is in preview only and defaults to `false`.

The `image` parameter is no longer available. The functionality will be reintroduced in future. For now, all pods download from the API URL.

## Migrate from OneAgent Operator to Dynatrace Operator

You can migrate from the deprecated OneAgent Operator to the new Dynatrace Operator that manages the lifecycle of several Dynatrace components such as OneAgent, routing, and Kubernetes API Monitor. Additional components will be added as new observability features become available.

Select **one of the following options**, depending on your deployment methods.

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Migrate manifests

Kubernetes

OpenShift

1. Delete OneAgent Operator and the `dynatrace` namespace/project.

   ```
   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/kubernetes.yaml



   kubectl delete namespace dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

1. Delete OneAgent Operator and the `dynatrace` namespace/project.

   ```
   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/openshift.yaml



   oc delete project dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

### Migrate with Helm

Kubernetes

OpenShift

1. Remove OneAgent Operator, the Helm repository, and the `dynatrace` namespace/project.

   ```
   helm uninstall dynatrace-oneagent-operator



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   kubectl delete namespace dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

1. Remove OneAgent Operator, the Helm repository, and the `dynatrace` namespace/project.

   ```
   helm uninstall dynatrace-oneagent-operator



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   oc delete project dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").