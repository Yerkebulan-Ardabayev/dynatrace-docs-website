---
title: Compliance Assistant
source: https://www.dynatrace.com/docs/observe/business-observability/compliance-assistant
scraped: 2026-03-06T21:14:30.942740
---

# Compliance Assistant

# Compliance Assistant

* Latest Dynatrace
* App
* 3-min read
* Updated on Feb 04, 2026
* Preview

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** supports and helps you to:

* Track, manage, and automate compliance across your IT and business landscape.
* Gain real-time visibility into compliance risks with regulations and certifications out-of-the-box.
* Monitor compliance health across critical business processes to ensure continuous monitoring and automating incident classification.

Prerequisites

### Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

### Permissions

The following table describes the required permissions.

storage:buckets:read

Read buckets

storage:events:read

Read events

storage:entities:read

Read entities table

storage:metrics:read

Required for Istio discovery findings rule

storage:filter-segments:read

Read filter-segments

settings:objects:read

Required for reading Log ingest settings

settings:schemas:read

Read settings schemas

state:app-states:read

Required to read app state

hub:catalog:read

Required to read app version

storage:security.events:read

Required for fetching security events

### Set up sources and applications

To take full advantage of ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**, get started with [![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**](/docs/observe/business-observability/business-flow "Monitor and analyze critical business process flows. Track business key performance indicators (KPI), detect process anomalies, and prioritize optimization opportunities to improve business outcomes.") to monitor and analyze compliance-critical business processes.

To maximize the value of risk management insights, set up data sources for [security events](/docs/secure/threat-observability/concepts#security-data "Basic concepts related to Threat Observability") from your monitored environment or from third-party sources. Security-related data includes [vulnerability events](/docs/secure/threat-observability/concepts#vuln-events "Basic concepts related to Threat Observability"), [compliance events](/docs/secure/threat-observability/concepts#compliance "Basic concepts related to Threat Observability"), and [detection finding events](/docs/secure/threat-observability/concepts#detection "Basic concepts related to Threat Observability").

![Gain visibility into compliance health across your IT and business landscape](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/afdf37e4-9501-479f-803b-cf3cbecf62c1.png)![Map critical business processes and surface compliance gaps with framework-specific signals](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/81eb7b08-1a02-4d32-aa27-f7d5bb137496.png)![Automatically detect and classify incidents based on regulatory thresholds and impact criteria](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/a5d01e06-ec63-40bd-811e-d764651b8024.png)

1 of 3Gain visibility into compliance health across your IT and business landscape

## Get started

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** offers monitoring and automation capabilities streamlined to specific compliance frameworks. To start managing compliance, set up a [compliance framework](#compliance-framework) applicable to your organization.

### Set up a compliance framework

1. In Dynatrace, go to ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. Select **Set up framework**.
3. To choose the compliance framework you want to monitor, select the relevant framework. Currently, **DORA** is the only available framework in ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
4. Select **Next**.
5. To select critical or important functions (CIFs), select all compliance-critical business processes. If no CIFs are available, create a new [business process with configuration as an entity](/docs/observe/business-observability/business-flow/set-up-business-flow#set-a-business-flow-configuration-as-an-entity "Follow the instructions on how to successfully set up Business Flow.") in ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**.
6. Select **Next**.
7. To take full advantage of the ICT risk management capabilities, verify whether data sources for [security events](/docs/secure/threat-observability/concepts#security-data "Basic concepts related to Threat Observability") are properly configured in your environment.

#### If vulnerabilities aren't enabled

1. Select **Set up RVA** to go to **Vulnerability Analytics: General settings** and enable [Runtime Vulnerabilities Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."). There are two tabs: **Third-party Vulnerability Analytics** and **Code-level Vulnerability Analytics**. You can enable one or more options there.
2. To monitor third-party vulnerabilities, [enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
3. To monitor code-level vulnerabilities, [enable code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
4. To integrate external security data into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data."), you can ingest [vulnerability events](/docs/secure/threat-observability/concepts#vuln-events "Basic concepts related to Threat Observability") from third-party products. For a list of supported integrations, see [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
5. Select **Done**.

#### If security detection findings aren't enabled

1. Select **Set up RAP** to go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Application security** > **Application protection** and [enable Runtime Application Protection](/docs/secure/application-security/application-protection#start "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").
2. To integrate external security data into Grail, you can ingest [detection finding events](/docs/secure/threat-observability/concepts#detection "Basic concepts related to Threat Observability") from third-party products. For a list of supported integrations, see [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
3. Select **Done**.

#### If ICT asset configuration rules aren't enabled

1. Select **Set up KSPM** to go to **Security Posture Management: Kubernetes** and [enable Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management#enable "Configure and enable Security Posture Management in Kubernetes.").
2. To get started with Security Posture Management and configure the assessment scope, see [Get started with Security Posture Management](/docs/secure/xspm#get-started "Detect, manage, and take action on security and compliance findings."). To include DORA as a supported compliance standard in the assessment scope, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Application security** > **Security Posture Management** and enable DORA.
3. To integrate with external security data to ingest compliance findings, see [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
4. Select **Done**.

### Remove a compliance framework

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. Under the relevant compliance framework, such as **DORA**, select  **Remove framework**.
3. Select **Remove** to confirm. Be aware that removing a compliance framework impacts all ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** users.

### Manage compliance-critical business processes



![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** allows you to map compliance-relevant IT assets to end-to-end business processes. ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** integrates with [![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**](/docs/observe/business-observability/business-flow "Monitor and analyze critical business process flows. Track business key performance indicators (KPI), detect process anomalies, and prioritize optimization opportunities to improve business outcomes.") to identify compliance-critical [business process with configuration as an entity](/docs/observe/business-observability/business-flow/set-up-business-flow#set-a-business-flow-configuration-as-an-entity "Follow the instructions on how to successfully set up Business Flow.").

#### To add a critical or important function (CIF)

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. Under the compliance framework DORA, select  **Add CIFs**.
3. From the table, select business processes to add as CIFs.
4. Select **Save** to update the compliance framework.

#### To remove a critical or important function (CIF)

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. Under the compliance framework DORA, select the menu icon of the CIF to remove.
3. From the menu, select **Remove CIF**.
4. Select **Remove** to confirm. Be aware that removing a CIF impacts all ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** users.

#### To edit the estimated cost per minute of an incident

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. Under the compliance framework DORA, select the menu icon of the relevant CIF.
3. From the menu, select **Edit incident cost/min**.
4. Add the estimated incident cost per minute to be used to calculate the economic impact of incidents impacting specific CIF.
5. Select **Save**.

### Manage compliance incidents

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**

* Is designed to help you manage incidents in line with compliance requirements.
* Automatically classifies incidents based on regulatory impact thresholds and accelerates reporting of major incidents to align with regulatory deadlines.
* Streamlines the assessment of IT-detected incidents affecting business processes configured as CIFs into [unclassified problems](#unclassified-problems), [potential major incidents](#potential-major-incidents), and [classified major incidents](#classified-major-incidents).

#### To investigate and classify potential compliance incidents

1. Go to ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**.
2. See the **Incidents** section for tables of [potential major incidents](#potential-major-incidents) and [unclassified problems](#unclassified-problems).
3. Select the relevant incident to view the following details on any triggered classification threshold according to the EU DORA Regulation:

   * Critical or important functions (CIFs) affected by the incident.
   * Incident duration, calculated on the basis of the duration of the underlying problem in nanoseconds. The materiality threshold for the classification criterion is met when the duration of the incident is longer than 24 hours ([RTS on the classification of ICT-related incidents and cyber threatsï»¿](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772)).
   * The economic impact of the incident is calculated on the basis of the estimated incurred cost per minute of the affected CIFs and the duration of the underlying problem. To learn more about configuring the estimated cost value per minute, see [Edit the estimated cost per minute of an incident](#to-edit-the-estimated-cost-per-minute-of-an-incident). The materiality threshold for the classification criterion `Economic impact` is met where the costs and losses incurred by the financial entity due to the incident have exceeded or are likely to exceed â¬100,000 (RTS on the classification of ICT-related incidents and cyber threats).
4. To classify an incident as major in line with EU DORA, from the incident details view, select **Classify as major**.
5. Optional: Add a comment to document your decision. This comment is added to the incident classification business event.
6. Select **Confirm**.

   * Be aware that classification triggers ingestion of a business event with the details of the classified compliance incident and the process may take a few seconds.
   * The classified incident is now available in ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** > **Incidents** > **Classified incidents**.

## Concepts

### Compliance framework

A compliance framework is a structured set of requirements, guidelines, and best practices to support organizations in meeting regulatory and industry-specific standards.

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** consolidates insights and functionalities tailored to a specific compliance framework. ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** currently offers monitoring and automation capabilities supporting compliance with the [EU DORA Regulationï»¿](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng).

### Dynatrace score in compliance snapshot

A real-time, tiered score summarizing your current ICT risk posture across potential incidents, security detection findings, vulnerabilities, and misconfigurations. This score is an indicative metric based on current data and tier logic. This score is a high-level indicator based on real-time observability and automated systems. It does not replace comprehensive or formal compliance assessments.

### Critical or important functions (CIFs)

According to the [EU DORA Regulationï»¿](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng), financial entities must identify, classify, and document ICT-supported business functions and their supporting assets. CIFs are processeses that, if disrupted, could significantly impact financial performance or service continuity.

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** allows you to map compliance-relevant IT assets to end-to-end business processes. By integrating with ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**, you can identify compliance-critical business processes, leveraging Smartscape entities for enhanced visibility and context.

### Unclassified problems

[IT-detected incidents](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.") are affecting any of the business processes configured as CIFs that ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** is monitoring. Incidents are considered unclassified problems when less than one of the materiality thresholds for the classification of major incidents is breached. In line with the EU DORA Regulation, it must be assessed whether an incident affects or has affected ICT services or network and information systems that support CIFs [(RTS on the classification of ICT-related incidents and cyber threats)ï»¿](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772).

### Potential major incidents

[IT-detected incidents](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.") are affecting any of the business processes configured as CIFs that ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** is monitoring. Incidents are considered potential major incidents when two or more of the monitored materiality thresholds for the classification of major incidents are breached. In line with the EU DORA Regulation, an incident is considered major when two or more of the materiality thresholds are met ([RTS on the classification of ICT-related incidents and cyber threatsï»¿](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772)).

### Classified major incidents



[IT-detected incidents](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.") are affecting any of the business processes configured as CIFs that ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** is monitoring and have been manually classified as major in line with the EU DORA Regulation. Once an incident is classified as major, Dynatrace automatically generates a business event with a snapshot of the compliance incident. Learn more about [Compliance incident classification events](/docs/semantic-dictionary/model/business-analytics "Get to know the Semantic Dictionary models related to Business Observability.").

### Vulnerabilities

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** relies on [vulnerability findings](/docs/secure/threat-observability/concepts#vuln-events "Basic concepts related to Threat Observability") to proactively mitigate risks before they escalate into incidents. In line with the EU DORA Regulation, organizations are required to assess vulnerabilities on a continuous basis. A vulnerability finding is a security event that highlights a detected weakness in a system, software component, or environment.

### Security detection findings

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** relies on [detection finding events](/docs/secure/threat-observability/concepts#detection "Basic concepts related to Threat Observability") to support in prioritizing cyber risks. In line with the EU DORA Regulation, organizations are required to assess cyber threats on a continuous basis ([RTS on ICT risk management frameworkï»¿](https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj/eng)). A detection finding event is generated when suspicious activity is observed around an object.

### ICT asset configuration results

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** relies on [compliance events](/docs/secure/threat-observability/concepts#compliance "Basic concepts related to Threat Observability") to detect potential misconfigurations. In line with the EU DORA Regulation, organizations are required to identify a secure configuration baseline for ICT assets that minimizes exposure to cyber threats and regularly verify that those baselines are effectively deployed ([RTS on ICT risk management frameworkï»¿](https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj/eng)). Compliance events represent the assessment of a resource in the context of the rule specified in the compliance standard.

## Use cases

Compliance Assistant enables you to achieve and manage compliance across supported frameworks:

* Identify and map compliance-relevant IT assets by analyzing critical end-to-end business processes â promoting cross-functional alignment between IT, security, and business teams.
* Continuously track compliance status against a selected framework and detect risks using real-time data on vulnerabilities, detection findings, and misconfigurations.
* Detect, classify, and accelerate reporting of incidents that meet regulatory thresholds, automating the steps needed to comply with tight regulatory deadlines.

## FAQ

How can I improve the Dynatrace score in the compliance snapshot?

The Dynatrace score is a real-time indicator based on your current ICT risk posture and impacted by the severity of findings. To improve your score:

* Address potential major incidents and unclassified problems promptly.
* Remediate security detection findings and vulnerabilities. To review security detection findings and initiate deeper analysis, see [Gain insights](/docs/secure/threats-and-exploits/gain-insights "Drill into detection findings for detailed information."). To learn more on how to fix detected vulnerabilities, see [How do I fix detected vulnerabilities?](/docs/secure/faq#fix "Frequently asked questions about Dynatrace Application Security.").
* Fix ICT asset misconfigurations identified by Security Posture Management. For guidelines on how to fix findings, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").
* Ensure proper monitoring and real-time protection are enabled across your critical or important functions (CIFs).

How often are insights on critical or important functions (CIFs) updated in ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**?

Insights on conversions and errors KPIs on CIFs are updated on the basis of the configured generation frequency of the KPI monitoring in ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**. The evaluation timeframe for the monitored KPIs of critical or important functions (CIFs) is also defined in setting up a business configuration as an entity.

To ensure reliable KPI evaluation and avoid missing data from longârunning processes, set the evaluation timeframe to at least three to four times the process's average duration (for example, if the average duration of the CIF is 5 minutes, set the window to at least 15â20 minutes).

Why are the configured critical or important functions (CIFs) not updating?

If you have recently edited or added [business processes configured as entity](/docs/observe/business-observability/business-flow/set-up-business-flow#set-a-business-flow-configuration-as-an-entity "Follow the instructions on how to successfully set up Business Flow.") and selected any of those as a CIF in ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**, it may take up to the maximum defined frequency for the monitoring KPIs of those business processes to be updated in ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant**. You can adjust the monitoring frequency in the business flow configuration.

## Related topics

* [Business process monitoring](/docs/observe/business-observability/business-process-monitoring "Discover how to monitor business processes.")
* [Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
* [Security Posture Management](/docs/secure/application-security/spm "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.")
* [Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")