---
title: Detect threats in cloud-native environments using workflows
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-cloud-native-workflows
scraped: 2026-02-27T21:19:01.980100
---

# Detect threats in cloud-native environments using workflows

# Detect threats in cloud-native environments using workflows

* Latest Dynatrace
* Tutorial
* Updated on Sep 10, 2025

In this tutorial, you'll learn how to

* Continuously detect and respond to active threats within your cloud-native environment
* Find attackers trying to exploit your applications before they can negatively affect your business
* Easily and flexibly search through huge amounts of data to find signs of suspicious behavior

## Target audience

This article is intended for

* DevOps, CloudOps, and SREs responsible for protecting workloads
* Security analysts responsible for cloud-native environments

## Prerequisites

* Set up ingestion of Kubernetes audit logs, for example, through [Amazon Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput."). Firehose can be used to ship logs from Amazon Elastic Kubernetes Service (EKS), but the provided template is compatible with any Kubernetes distribution.
* Generate an access token with the `openpipeline.events_security` scope to allow us to ingest detection findings. To later access the token securely from within a workflow, store the token in the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."). For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Get started

After setting up log ingestion, you can start detecting threats.

1. Set up scheduled DQL queries

Use ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** to execute DQL queries regularly and look for suspicious behavior in your data.

1. Import our [workflow templateï»¿](https://dt-url.net/s9030m9).
2. For the **execute\_query** step, adapt the DQL query to your needs.

   The template query aims to find possibly compromised service accounts within our Kubernetes cluster.

   * You can tune it, adjust its logic or modify it completely to detect other potential threats.
   * You can find additional examples in the [Dynatrace blogï»¿](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/).
3. For the **ingest\_findings** step, go to **Input** > **Authentication** and select the token previously stored in the credential vault.

2. Test the workflow

To trigger a detection finding based on the query provided, execute the following commands in a Dynatrace-monitored Kubernetes cluster:

1. Create a test service account:

   ```
   kubectl create serviceaccount test-sa -n default
   ```
2. Attempt unauthorized access (should trigger detection):

   ```
   kubectl --as=system:serviceaccount:default:test-sa get secret -A
   ```

3. Tune detection

You can define exceptions to the rule by adding allowlisting criteria to the **apply\_allowlist** step in the workflow.

A detection finding event will not be created if all attributes of an entry match those of any single allowlisted entry.

* Attribute comparison follows `AND` logic within an entry.
* Allowlist evaluation uses `OR` logic across entries.

4. Triage and investigate

Use [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.") to examine and prioritize the detection findings created. The rich observability context provided in the detection finding enables fast analysis and confident assessment of the situation.

**Sample result**

![sample result in threats and exploits app](https://dt-cdn.net/images/image-58-1667-0a98717d9c.png)

## Sample workflows for threat response

Dynatrace provides ready-to-use workflow templates that automatically trigger on new Kubernetes threat detection findings and send notifications via [Slack](/docs/analyze-explore-automate/workflows/actions/slack#workflow "Send messages to Slack Workspaces"), [Microsoft Teams](/docs/analyze-explore-automate/workflows/actions/microsoft-teams#use "Send messages to Microsoft Teams"), or [Email](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
Use these as starting points to build your own automated response workflows:

* [Instant notification for critical Kubernetes detection findingsï»¿](https://dt-url.net/l9430ds): Triggers on high or critical findings and alerts the responsible team.
* [Threat detection notification senderï»¿](https://dt-url.net/hs2301e): A reusable sub-workflow for centralized notification delivery.

These templates show how to enrich findings with [ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") context and integrate real-time alerting into your response workflows.

## Conclusion

Workflows enable precise threat detection and response aligned with your environmentâs context. Features like flexible scheduling, DQL-based filtering, allowlisting, ownership tagging, and notification integration allow for rapid, low-noise detection. The included blueprint offers a modular starting point that can be fine-tuned or extended to meet specific operational needs.