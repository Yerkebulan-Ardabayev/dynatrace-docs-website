---
title: Resolve incidents faster with Investigations templates
source: https://www.dynatrace.com/docs/secure/use-cases/resolve-incidents-faster-with-templates
scraped: 2026-02-19T21:34:49.289259
---

# Resolve incidents faster with Investigations templates

# Resolve incidents faster with Investigations templates

* Latest Dynatrace
* Tutorial
* Published Feb 11, 2025

To kick off new investigations faster and save yourself from repetitive manual work, you can use templates in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."). Templates provide a boilerplate for investigations, creating initial DQL queries ready to be executed and the required artifacts about your environment available as evidence lists. This saves time when creating manual queries or copying the queries from incident response playbooks.

In the following, you'll learn how to speed up log-related endeavors in ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** using templates.

## Target audience

This article is intended for security engineers, site reliability engineers, DevOps engineers, and others who regularly perform investigations and log analysis on Grail data using ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

## Scenario

When Dynatrace notifies you of an issue in a production environment, you typically start an investigation with the same basic queries. For example, in a Kubernetes environment, you want to determine:

* Is the error present in only one cluster or across all of them?
* Does the error appear in only one cluster node or several?
* Which pods and containers are currently running in your environment?
* What was logged in the specific Kubernetes log?
* What was logged by the pod?
* What was logged by the container?

The queries you create to answer such questions are often scattered across previous investigations, DQL query repositories, and incident response playbooks.

To streamline your process, you want to create a template to prepare these queries in advance for future incidents. Fortunately, you have already conducted an investigation that includes these queries, allowing you to create a template from an existing investigation.

## Start a template

In ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**, select one of the three ways to start a template:

* **Create it from an investigation**: You can make a template from an existing investigation, for example, if you want to use the queries from a previous investigation. For instructions, see [Save investigations as templates](/docs/secure/investigations/manage-templates#create-template-from-case "Reuse common queries and workflows in Investigations.").
* **Upload it**: You can upload a template downloaded from a blog post or provided by the community. For instructions, see [Download and upload templates](/docs/secure/investigations/manage-templates#download-upload-template "Reuse common queries and workflows in Investigations.").
* **Duplicate it**: You can copy a template that you own or clone and edit a template that has been shared with you. For instructions, see [Duplicate templates](/docs/secure/investigations/manage-templates#duplicate-template "Reuse common queries and workflows in Investigations.").

## Work with your template

Once you created a template, the following options are available.

1. Modify the template

You can modify your template if, for example, you want to remove some queries and add production cluster names to the evidence list in the template for faster access. For instructions, see [Edit templates](/docs/secure/investigations/manage-templates#edit-template "Reuse common queries and workflows in Investigations.").

2. Create a case from the template

You can start a new investigation based on the initial input from your template. For instructions, see [Create cases from templates](/docs/secure/investigations/manage-templates#create-case-from-template "Reuse common queries and workflows in Investigations.").

3. Duplicate the template

You can create another similar template for yourself based on your template. For instructions, see [Duplicate templates](/docs/secure/investigations/manage-templates#duplicate-template "Reuse common queries and workflows in Investigations.").

4. Share the template with others

You can share your template with others to increase productivity and empower collaboration between within you, your team, and your organization. This enables your team members to save time when kicking off an investigation. Templates can be shared in a similar way with cases. For instructions, see [Duplicate templates](/docs/secure/investigations/manage-templates#share-template "Reuse common queries and workflows in Investigations.").

## Related topics

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")