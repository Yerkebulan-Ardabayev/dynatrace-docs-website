---
title: Application Security FAQ
source: https://www.dynatrace.com/docs/secure/faq
scraped: 2026-02-28T21:13:06.420345
---

# Application Security FAQ

# Application Security FAQ

* Latest Dynatrace
* Troubleshooting
* Updated on Feb 23, 2026

See below for answers to some of the most frequently asked questions about Dynatrace Application Security, grouped by topics.

For troubleshooting articles related to Application Security, visit [Dynatrace Communityï»¿](https://dt-url.net/dy122xtf).

## Detection and monitoring

### How can I detect security risks in my applications?

Latest Dynatrace

You can detect, analyze, and understand security risks in your applications using several Dynatrace security apps:

* Identify, prioritize, and monitor vulnerabilities in thirdâparty libraries, application runtimes, and custom code across production and preâproduction environments with [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.").
* Investigate, triage, and take action on realâtime detection findings and alerts affecting your applications with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").
* Explore securityârelated data, run DQL queries, extract fields, and perform deeper investigations across logs, metrics, and traces with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

deprecated

* To detect and monitor third-party vulnerabilities, [enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), then go to [![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.").
* For a unified view of third-party and code-level vulnerabilities and information about host coverage, [enable Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), then go to [![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview**](/docs/secure/application-security/vulnerability-analytics/application-security-overview "Get an overview of the security issues of your third-party libraries.").

### What's the difference between the classic monitoring rules and the new monitoring rules?

The [new monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#new "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") let you include or exclude processes, Kubernetes nodes, and hosts based on resource attributes and Kubernetes labels. This approach is more flexible and precise, works well in dynamic and cloudânative environments, and supports previews so you can verify which entities match before enabling the rules. These rules are recommended and are the default for newer environments.

The [classic monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#classic "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") rely on process group tags, host tags, and management zones. They offer less granularity, depend on correct tagging, and don't provide the same level of preview or control. Classic rules still work but are scheduled for deprecation and can't be used at the same time as the new rules.

### How do RVA and RAP work?

* To learn about the Runtime Vulnerability Analytics (RVA) mechanism, see [How RVA works](/docs/secure/application-security/vulnerability-analytics#mechanism "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* To learn more about the Runtime Application Protection (RAP) mechanism, see [How RAP works](/docs/secure/application-security/application-protection#mechanism "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

### What's the impact of enabling Application Security?

***What should I consider before enabling Application Security? Can it impact anything?***

When you enable Application Security (Runtime Vulnerability Analytics or Runtime Application Protection), keep the following in mind:

* **Consumption**:  
  **Runtime Vulnerability Analytics and Runtime Application Protection** consume [GiB-hours](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.") if you're using the [Dynatrace Platform Subscription (DPS) licensing model](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), or [Application Security units (ASUs)](/docs/license/monitoring-consumption-classic/application-security-units "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") if you're using the [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").
* **Network bandwidth usage**:

  + **Codeâlevel vulnerability detection and attack detection**: Expect a slight increase in network usage, depending on the number of monitored applications. In most cases, this overhead is negligible.
  + **Thirdâparty vulnerability detection**: No additional process overhead is introduced.

### How can I disable security monitoring?

* To disable Runtime Vulnerability Analytics

  1. Go to **Settings** > **Analyze and alert** > **General settings**.
  2. Under **Third-party Vulnerability Analytics**, turn off **Enable Third-party Vulnerability Analytics**.
  3. Under **Code-level Vulnerability Analytics**, turn off **Enable Code-level Vulnerability Analytics**.
* To disable Runtime Application Protection

  1. Go to **Settings** > **Analyze and alert** > **Application security** > **Application protection (New)**.
  2. Turn off Runtime Application Protection.

### Can I manually start a security scan?

***Does Application Security perform a scheduled job? What's the scheduled time interval? Can I manually start a security scan after deploying our changes in the environment?***

There are no scheduled scans. Once you enable any Dynatrace Application Security functionality, your environment is automatically monitored for the selected functionality continuously and in real time.

## Restrict permissions

### How can I give someone view-only access to vulnerabilities?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, which is deprecated.

To restrict specific users to view-only access, so they can view but not manage vulnerabilities, see [Customize access](/docs/secure/application-security/vulnerability-analytics#restrict-permissions "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

## Resolution

### Does Dynatrace remediate vulnerabilities?

***Will Dynatrace fix vulnerabilities or do I need to take any action to fix them?***

Dynatrace does not remediate vulnerabilities. It identifies and monitors vulnerabilities in applications in your production and pre-production environments, and it helps you determine the root cause by providing rich context and information that helps you take the appropriate actions. For more information about capabilities, see

* [Runtime Vulnerability Analytics: Capabilities](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Latest Dynatrace [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.")

Once the root cause is gone, the vulnerability is automatically resolved. For more information about vulnerability resolution, see:

* [Third-party vulnerabilities: Resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")
* [Code-level vulnerabilities: Resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#clv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")

### How do I fix detected vulnerabilities?

The rich and precise context and details provided on the vulnerabilities pages help you identify and understand vulnerabilities, prioritize them by risk, and automatically monitor and alert on newly discovered vulnerabilities. Based on this information, you can determine what actions are needed to fix the vulnerabilities.

For example:

Latest Dynatrace

In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), you can:

* [Apply fix recommendations from Snyk](/docs/secure/vulnerabilities/address-remediation#snyk "Address remediation and optimize remediation activities.")
* [Apply DSA fixes](/docs/secure/vulnerabilities/address-remediation#dsa "Address remediation and optimize remediation activities.")
* [Connect affected entities to your ticketing system and track the remediation progress](/docs/secure/vulnerabilities/address-remediation#remediation-tracking "Address remediation and optimize remediation activities.")
* [Drill down into the source of vulnerabilities](/docs/secure/vulnerabilities/address-remediation#source "Address remediation and optimize remediation activities.")
* [Change the mute status of affected entities](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.")

deprecated

In [![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries."), you can:

* Use the recommended [DSA fixes](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.") to upgrade to a non-vulnerable version of the vulnerable component
* [Set up tracking links for affected entities and follow up with their remediation progress](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")

### When is a vulnerability marked as resolved?

***I removed the vulnerable component, but the vulnerability still shows as open. When does it get resolved?***

A vulnerability is marked as `Resolved` under the following conditions:

* No process group or Kubernetes node has reported any vulnerable components for more than two hours.
* The root cause of the vulnerability is no longer present; for example, the vulnerable component has been removed or the affected process has been terminated.

  This condition applies regardless of how much time has passed since the last report.

### Why is my vulnerability still open if there's no affected process group anymore?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

A vulnerability is still reported if it's still present in other management zones. To see the affected process groups, select `All` in the management zone filter.

### Can a vulnerability be resolved while there are still affected entities?

No. A vulnerability is resolved if there are no longer any affected entities.

### Why are some vulnerabilities resolved without any mitigation?

***After enabling Runtime Vulnerability Analytics, 19 critical vulnerabilities were found. Now they are down to three without any mitigation from our side. Why are some vulnerabilities resolved without any mitigation?***

A vulnerability is resolved automatically if the root cause is no longer present. To learn more, see

* [Third-party vulnerability resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")
* [Code-level vulnerability resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#clv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")

### Why do some vulnerabilities keep being resolved and reopened?

A vulnerability keeps being resolved and reopened when a process using the vulnerable library isn't running all the time:

* When the process is terminated, the vulnerability is resolved.
* When the process is restarted, the vulnerability is reopened.

For details about the reasons why vulnerabilities are resolved and reopened, see [Resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

To determine which processes are affected, see:

* Latest Dynatrace [What is at risk (affected and related entities)](/docs/secure/vulnerabilities/prioritize#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.")
* deprecated [Remediation tracking for processes](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#process "Track the remediation progress of vulnerabilities.").

### Why do resolved vulnerabilities show up in every management zone?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

Management zone information is not directly attached to a vulnerability. It derives from the vulnerable entities that are affected by the respective vulnerability: a process in a management zone that uses a vulnerable library causes a third-party vulnerability in the respective management zone.

A vulnerability is resolved if there are no vulnerable entities anymore. In the vulnerability list, all resolved vulnerabilities displayed are not filterable by management zone anymore, as that information is not attached to them.

### Why am I getting zero resolved process groups for resolved vulnerabilities in my management zone?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

***For resolved vulnerabilities, I would like to examine resolved process groups to understand which entities were previously affected, but there are zero resolved process groups in my management zone. Why?***

On the Vulnerabilities pages, in the **Process group overview** section, if there are zero resolved process groups displayed for a resolved vulnerability in your management zone, it means that none of the entities that were previously affected and resolved are in that management zone. To find the respective entities, switch the management zone filter to `All`.

## Restart required

### Is restart required after enabling or disabling an Application Security feature or functionality?

See below the restart requirements by functionality.

* **Third-party vulnerabilities**: An application process restart is required in the following case:

  + In [**Discovery mode**](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent."), after you [enable code-module injection](/docs/platform/oneagent/monitoring-modes/monitoring-modes#code-module-injection "Find out more about the available monitoring modes when using OneAgent.")
* **Code-level vulnerabilities**: An application process restart is required in the following cases:

  + After each step in [Enable code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."):

    - Enable Code-level Vulnerability Analytics
    - Configure the global code-level vulnerability detection control per technology
    - Enable OneAgent monitoring
  + After you enable a [monitoring rule](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups")
* **Attacks**: An application process restart is required in the following cases:

  + After each step in [Get started with Runtime Application Protection](/docs/secure/application-security/application-protection#start "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities."):

    - Enable Runtime Application Protection
    - Define the global attack control per technology
    - Enable OneAgent monitoring
  + After you enable a [monitoring rule](/docs/secure/application-security/application-protection/application-protection-rules "Create, modify, and delete rules for specific attacks.")

### Why is there a "Restart required" notification on some Application Security pages?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

OneAgent version 1.279+

See [How can I know if information about vulnerable functions is outdated and what can I do about it?](#outdated-vulnerable-functions).

## Notifications and reporting

### How can I get notifications for vulnerabilities?

Latest Dynatrace

You can [set up a workflow](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.") to configure Dynatrace to send notifications for [vulnerabilities and vulnerability findings](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") through your preferred [channels](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems."). The configuration options give you fineâgrained control over when and how the notifications are triggered.

* For examples of how to configure a workflow, see [Workflows use cases](/docs/analyze-explore-automate/workflows/use-cases "Explore common Workflows use cases in Dynatrace deployments.").

deprecated

You can [set up notifications](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva "Integrate security notifications for vulnerabilities with Dynatrace.") through your preferred channels.

* For example, you can trigger alerts

  + When a vulnerability is reopened (**Vulnerability (re)opened**)
  + When a new process group in a management zone becomes affected by a vulnerability (**New Management zone affected**)

### How can I get notifications for attacks?

Latest Dynatrace

You can [set up a workflow](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.") to configure Dynatrace to send notifications for [detection findings](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.") through your preferred [channels](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems."). The configuration options give you fineâgrained control over when and how the notifications are triggered.

* For examples of how to configure a workflow, see [Workflows use cases](/docs/analyze-explore-automate/workflows/use-cases "Explore common Workflows use cases in Dynatrace deployments.").

### How can I create reports and share them with others?

Latest Dynatrace

* In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), you can:

  + [Download the vulnerability data as a CSV file](/docs/secure/vulnerabilities/collaborate-with-apps#dwld "Navigate between Dynatrace apps, share vulnerability data externally, and automate remediation workflows.")
  + [Download the vulnerability finding data as a CSV file](/docs/secure/vulnerabilities/explore-findings#collaborate "View, filter, and analyze vulnerability findings from Dynatrace and external security tools.")
* In [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts."), you can [download the detection finding data as a CSV file](/docs/secure/threats-and-exploits/collaborate-with-apps#download "Interact with other apps for further insights and share results with stakeholders.").
* In [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."), you can generate reports for [security events](/docs/secure/threat-observability/concepts#security-events "Basic concepts related to Threat Observability") with [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."), and then create [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") based on the results.

  + For commonly used queries, see [DQL examples for security data](/docs/secure/threat-observability/dql-examples#vulnerabilities-per-application "DQL examples for security data powered by Grail.").
  + For a complete list of queryable fields, including descriptions and examples, see [Dynatrace Semantic Dictionary: Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.").

deprecated

* With the Dynatrace API, you can chart [Application Security metrics](/docs/secure/application-security/vulnerability-analytics/app-sec-metrics "View available Application Security metrics for Dynatrace Runtime Vulnerability Analytics.") and [pin them to your dashboard](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#pin "Browse metrics with the Dynatrace metrics browser."). For example, you can retrieve [all security problems detected in your applications](/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerabilities "View the list of vulnerabilities via Dynatrace API.") or the [vulnerable functions of a security problem](/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions "View the vulnerable functions of a vulnerability via Dynatrace API.").
* With [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), you can [share your metric results](/docs/analyze-explore-automate/explorer#share "Query for metrics and transform results to gain desired insights.") and [export them to a CSV file](/docs/analyze-explore-automate/explorer#csv "Query for metrics and transform results to gain desired insights.").

### How can I stop receiving notifications for an irrelevant vulnerability or entity?

If you think a vulnerability or an entity isn't relevant or is a false positive, you can:

Latest Dynatrace

Mute (silence) all its affected entities. This sets the vulnerability status to `Muted`. For instructions, see [Change the affected entity status](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.").

deprecated

* Mute (silence) the vulnerability. For details, see [Change the third-party vulnerability status](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#mute "Organize third-party vulnerabilities for easy management and to prioritize issues.").
* Mute (silence) the entity. For details, see [Change vulnerability status of process groups](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#status-pg "Track the remediation progress of vulnerabilities.") and [Change vulnerability status of nodes](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#status-node "Track the remediation progress of vulnerabilities.").

### Why do we keep receiving notifications for the same vulnerability?

***Every day we receive notifications for the same vulnerability ID, with the same process group, entity name, and entity link. We have other vulnerabilities detected, but no extra notifications are sent. Why do we keep receiving notifications for the same vulnerability?***

A process that does not run all the time might be using a vulnerable library. For details, see [Why do some vulnerabilities keep being resolved and reopened?](#reopen).
To stop receiving notifications for this vulnerability, you can:

* Exclude the respective process from Application Security monitoring by setting up a [third-party monitoring rule](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")/[code-level monitoring rule](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups").
* Latest Dynatrace Mute (silence) all the vulnerability's affected entities. This sets the vulnerability status to `Muted`. For instructions, see [Change the affected entity status](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.").
* deprecated Mute (silence) the vulnerability. For details, see [Change the third-party vulnerability status](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#mute "Organize third-party vulnerabilities for easy management and to prioritize issues.").

### How can I fetch fix recommendation information for vulnerabilities?

* Latest Dynatrace To retrieve remediation guidance for vulnerabilities, use [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to run a [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query that includes the `vulnerability.remediation.description` field. Example:

  ```
  fetch security.events



  | filter event.type == "VULNERABILITY_STATE_REPORT_EVENT"



  | filter event.level == "ENTITY"



  | fields vulnerability.risk.level, vulnerability.title, vulnerability.remediation.description
  ```

  For a complete list of queryable fields, including descriptions and examples, see [Dynatrace Semantic Dictionary: Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.").
* deprecated To retrieve remediation guidance for a specific vulnerability, call the Dynatrace API endpoint for an individual vulnerability. Provide the vulnerability ID and request the `recommendationDescription` property in response.

  For details, see [Vulnerabilities API - GET vulnerability details](/docs/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerability-details "View details of a vulnerability via Dynatrace API.").

## Coverage

### How can I gain insights into my environment's Runtime Vulnerability Analytics coverage?

* Latest Dynatrace Evaluate your environment's Runtime Vulnerability Analytics process and host coverage with the ready-made [**Vulnerability coverage** dashboard](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").
* deprecated Go to ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview**. In the **Host coverage** section, select **Monitored hosts** to go to the **Hosts** page filtered by monitored hosts. For details, see [Application Security overview: Host coverage](/docs/secure/application-security/vulnerability-analytics/application-security-overview#host-coverage "Get an overview of the security issues of your third-party libraries.").

### Why do I see a vulnerability on one host but not on another?

Vulnerability detection depends on the data Dynatrace receives from each host. If a host is missing required instrumentation or configuration, Dynatrace may not be able to detect or confirm a vulnerability on that host. Common causes include missing OneAgent injection, autoâinjection disabled, outdated OneAgent versions, or unsupported runtimes.

Latest Dynatrace To identify hosts with missing or disabled autoâinjection, you can run a DQL query in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."), for example:

```
fetch dt.entity.host



| fieldsAdd autoInjection



| fieldsAdd entity.name
```

## Limit monitoring

### How can I exclude specific entities from being monitored by Runtime Vulnerability Analytics?

You can:

* [Create monitoring rules for third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")
* [Create monitoring rules for code-level vulnerabilities](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups")

Your custom rules override the global third-party vulnerability detection control setting. Any entity that doesn't match one of your rules will follow the global thirdâparty vulnerability detection setting.

### Where can I find examples of monitoring rule configurations?

If you need guidance for setting up monitoring rules in common scenarios such as monitoring only specific hosts, processes, Kubernetes namespaces, Kubernetes nodes, or excluding certain processes, you can refer to [Use cases for new monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#usecases "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."). It provides practical examples that show how to configure rules for a variety of environments and requirements.

### How can I limit Runtime Vulnerability Analytics monitoring to a specific management zone?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

[Create a monitoring rule](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") that says `Do not monitor` if the management zone does not equal `<your-management-zone>`. After you add, edit, or remove a rule, allow up to 15 minutes for your changes to take effect.

### How can I enable Runtime Vulnerability Analytics only for specific hosts or Kubernetes namespaces?

To enable Runtime Vulnerability Analytics only for selected parts of your environment, create monitoring rules that apply to the specific hosts or Kubernetes namespaces you want to monitor.

You can follow these example use cases:

* [Monitor only the processes on specific hosts](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#monitor-processes-specific-host "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")
* [Monitor only processes running in a specific Kubernetes namespace](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#processes-specific-namespace "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")

These examples show how to disable global monitoring and then create resourceâattribute monitoring rules that selectively enable monitoring for the entities you choose.

## Change status

### If a vulnerability is muted, are the affected entities muted as well?

No. The `MUTE` state does not automatically transfer to its affected entities; there is no interdependence between the two when assessing this state.

Latest Dynatrace In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), a vulnerability is only muted if all its affected entities are muted. For details, see [Change the mute status of affected entities](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.").

## Status updates

### What does "last update" on vulnerabilities list pages refer to?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

***On the third-party vulnerabilities list page, does "Last update" refer to the last time when Dynatrace provided an update? How can I request an update for a vulnerability which was last updated two days ago?***

**Last update** refers to the last time when a vulnerability had a status change. It does not refer to the last time when Dynatrace provided an update. For details, see [FAQ: Can I manually start a security scan?](#start-scan).

#### What are status changes

* For third-party vulnerabilities, a status change can be when:

  + The vulnerability is resolved or reopened
  + The vulnerability is muted or unmuted
  + The number of affected process groups has decreased or increased
  + The risk assessment has changed
  + The Dynatrace Security Score has changed
  + A new software component is detected
* For code-level vulnerabilities, a status change can be when:

  + The vulnerability is resolved or reopened
  + The vulnerability is muted or unmuted
  + The risk assessment has changed
  + New attacks on the vulnerability have been detected

## Different values

### Why are there different values on the vulnerabilities page versus Data Explorer?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

***In ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, on the **Third-party vulnerabilities** list page, when I filter for resolved vulnerabilities over the last seven days, I get `3` vulnerabilities. When I use the metric query (`builtin:security.securityProblem.resolved.new.global`) in Data Explorer, I get `25`. Why are there different values on the vulnerabilities page versus Data Explorer?***

The vulnerability list shows the current state (the total count of vulnerabilities that are currently resolved), while using the metric query in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") shows the change over time.

For example, if two vulnerabilities are open and resolved several times over a period of time, the Data Explorer chart shows only one spike (which is the maximum over the given timeframe) while the vulnerabilities page shows two (because there are currently two resolved vulnerabilities).

To find out how many vulnerabilities were resolved in the given timeframe using the metric query

1. In Data Explorer, set the visualization type to `Single value`.
2. Expand **Settings** and set **Fold transformation** to `Value`.

   This shows how many times the vulnerabilities were resolved during the selected timeframe.

![example Data Explorer fold transformation setting](https://dt-cdn.net/images/2023-06-15-09-41-13-1626-bcb5aa24fb.png)

### Why are there different values on the Third-party vulnerabilities and vulnerability details pages?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

There can be two reasons why values on these pages don't match:

* [Different number of affected entities](#different-affected-entities)
* [Different risk factors](#different-risk-factors)

#### Different number of affected entities

In ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, the number of affected entities (process groups or hosts) on the **Third-party vulnerabilities** page (in the **Affected entities** column for a specific vulnerability) may differ from the number of affected entities on the vulnerability details page for the following reasons:

* On the **Third-party vulnerabilities** page:

  + Affected entities aren't filtered by management zone.
  + Calculations take place every 15 minutes.
* On the vulnerability details page:

  + Affected entities are filtered by management zone.
  + Current data is considered.

#### Different risk factors

In ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, the assessment of risk factors (`Public exploit`, `Public internet exposure`, `Reachable data assets`, `Vulnerable functions in use`) in the infographic on the vulnerability details page and the **Davis Security Score** column on the **Third-party vulnerabilities** page may be different from the assessment of risk factors on the vulnerability details page (in the **Vulnerability details** section) for the following reason:

For the infographic on the vulnerability details page and the **Davis Security Score** column on the **Third-party vulnerabilities** page, calculations take place every 15 minutes
For the **Vulnerability details** section on the vulnerability details page, current data is considered.

### Why does my vulnerability have a different risk assessment and DSS than its affected entities?

A vulnerability is an aggregation of all its affected entities in your environment; therefore, it can have different values (risk assessment and DSS) than its affected entities. For example, the risk score of an affected entity might be `8.0`, while the score of the aggregated vulnerability is `9.0`. At the same time, if at least one affected entity is exposed to the internet, the aggregated vulnerability is also exposed to the internet.

Latest Dynatrace In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), the DSS score is the maximum DSS score of the affected entities. For details, see [Calculation differences](/docs/secure/vulnerabilities/concepts#differences "Concepts that are specific to the Dynatrace Vulnerabilities app.").

### Why am I seeing different vulnerabilities in production vs non-production environment?

You have the same vulnerabilities in two environments only if all of the following are the same in both environments:

* Deployment (including the OneAgent version)
* Settings
* Application usage
* Traffic

### Why does the number of vulnerabilities differ between the classic apps and the Vulnerabilities app?

The total number of vulnerabilities shown in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** may differ slightly from the counts in the classic **Third-party vulnerabilities** app. This difference stems from several backend-related factors:

* **Timing**: State report exports can take up to 15 minutes. As a result, vulnerabilities may appear or disappear with a delay in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**.
* **Muting**: Muted vulnerabilities are excluded from the reported **vulnerabilities detected** count in the classic apps. To view them, you need to apply a filter for muted vulnerabilities or refer to the summary panel.
* **Timeframe**: The default timeframe for ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** is 30 minutes, whereas the classic apps use a 2-hour default timeframe.

We recommend using ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** as your primary interface for managing vulnerabilities. It reflects the latest detection logic, is actively maintained, and continues to evolve. The classic views are planned to be phased out for SaaS customers in the coming years.

## Public internet exposure

### How is public internet exposure determined?

On Linux hosts, if there's no information, which can happen in different monitoring modes or because something went wrong, public internet exposure is detected via eBPF. Potential states are `Public network` and `Not detected`.

Full-Stack Monitoring mode

Infrastructure Monitoring mode and Discovery mode

To determine public internet exposure, Dynatrace:

1. Evaluates all the IP addresses detected in the last hour.
2. Discards the private IP ranges.
3. Groups the remaining IPs by subnet.

As soon as the respective subnets reach a certain (low) threshold, public internet exposure is triggered.

Public internet exposure can't be evaluated on operating systems other than Linux, and the state is `Not available`.

## Vulnerable libraries

### Does Dynatrace detect vulnerable libraries that aren't in use?

Runtime Vulnerability Analytics focuses on the runtime aspect, aiming to provide a prioritized list of vulnerabilities that are relevant to your running environments. For this purpose, Dynatrace only reports libraries that are actively used.

### Where can I see the origin of a vulnerable library?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

On the remediation tracking pages for process groups and processes affected by a vulnerability, you can see where the software component has been loaded from.

This feature is displayed for vulnerable Java, .NET, Node.js, Python, and Go software components.

Note that to display the origin of .NET software components, the minimum OneAgent version required is OneAgent version 1.301+.

Example:

![load-origins-pg](https://dt-cdn.net/images/2023-08-21-15-09-46-1812-3f3a0b8200.png)

For information on how to navigate there, see [Remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.").

## Vulnerable functions

### How are vulnerable functions determined?

* If the Snyk feed provides information about the vulnerable function, and OneAgent monitoring for Java vulnerable functions is enabled, OneAgent determines whether the vulnerable function is in use.
* If the Snyk feed provides information about the vulnerable function, but the OneAgent feature is disabled, the number of vulnerable functions is displayed as **Not available**.

### Why is there no information on vulnerable functions?

There are two cases when information about vulnerable functions is not available:

* If no vulnerable function information is provided by Snyk or the Dynatrace security research team.
* For runtime vulnerabilities, which are based on the NVD feed.

### Why is there no data available for vulnerable functions?

* Once you [enable Third-party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), it will take some time (one hour at the most) until data about vulnerable functions is displayed.
* OneAgent monitoring for Java vulnerable functions is disabled. To enable it, see [Enable OneAgent monitoring for Java vulnerable functions](/docs/secure/application-security/vulnerability-analytics#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

  The OneAgent feature must be enabled for all processes affected by the vulnerability. For instructions on how to enable OneAgent monitoring, see [Enable OneAgent monitoring for Java vulnerable functions](/docs/secure/application-security/vulnerability-analytics#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* No vulnerable functions of the vulnerability are contained in the release version of the third-party libraries (software components) in use.
* No vulnerable functions are provided by the Snyk feed.
* deprecated You need to restart the processes affected by the vulnerability for updated information. For details, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

#### How do I know which processes to restart?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

If you see the **Restart required** notification on the details page of a vulnerability, follow the steps below to determine which processes you need to restart:

1. On the [**Process group overview**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#pg "Monitor the security issues of your third-party libraries.") card, select **View all process groups**.
2. Filter by `Vulnerable functions: Restart required`.
3. For each of the resulting process groups, select **Details**, then select the link provided in the **Restart required** notification to navigate to the list of processes that require a restart.

![Select the processes that need to be restarted](https://dt-cdn.net/images/2023-12-18-13-43-19-539-175d9b3394.png)

Example result:

![Filter by Vulnerable functions: Restart required](https://dt-cdn.net/images/2023-12-18-13-07-00-1594-7f9f9381c3.png)

After a process restart, it takes about a minute for the updated information to be displayed.

This feature only works if [OneAgent monitoring for Java vulnerable functions is enabled](/docs/secure/application-security/vulnerability-analytics#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

#### Why does my process still need to be restarted after I already restarted it?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

If you followed the [instructions](#which-process-to-restart) to identify the process and restarted it, and the process still requires a restart (the same **Restart required** notification shows up, and the information about vulnerable functions is unchanged), this can happen in Kubernetes deployments if there's no persistent storage.

To fix this issue, add persistent storage by mounting file storage that isn't deleted when restarting your pods.

### How can I know if information about vulnerable functions is outdated and what can I do about it?

Content below refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated.

OneAgent version 1.279+

If new information about a vulnerability's vulnerable functions is available, a process restart is required so that OneAgent can pick up and use the new data.
In this case, a **Restart required** notification or symbol is displayed on

* A vulnerability's details page (in [**Vulnerability details**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#vulnerability-details "Monitor the security issues of your third-party libraries.") > **Vulnerable functions**)

  ![Restart required on a vulnerability details page](https://dt-cdn.net/images/2023-12-18-12-45-12-776-d39b330fe4.png)
* The [process groups overview related to a vulnerability](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#pg "Track the remediation progress of vulnerabilities.") (in [**Details**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#details "Track the remediation progress of vulnerabilities.") > **Risk assessment**)

  ![Restart required on the process groups overview related to a vulnerability](https://dt-cdn.net/images/2023-12-18-12-41-00-1597-34af91fcf3.png)
* The [process list related to a vulnerability](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#process "Track the remediation progress of vulnerabilities.") (in **Vulnerable functions** and **Details**).

  ![Restart required on the process list related to a vulnerability](https://dt-cdn.net/images/2023-12-18-12-37-41-1570-47da22adc2.png)

## Snyk feed

### Why is the Snyk link missing for some vulnerabilities?

***Why don't some vulnerabilities contain a link to Snyk, even though I can find the same CVE in Snyk?***

To fetch data about vulnerabilities, Dynatrace Application Security uses either [Snykï»¿](https://snyk.io) or [NVDï»¿](https://nvd.nist.gov/vuln), depending on the vulnerable component.

A vulnerability with a CVE that is listed in Snyk but that doesn't have any Snyk-related information in Dynatrace is using the NVD feed. For more information, see [Third-party vulnerability feeds](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#vulnerability-feeds "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

## Attack blocking mechanism

### How does Dynatrace actually block attacks?

Selecting `Block attack` for an attack doesn't automatically block the respective attack; it takes you to the Settings page where you can create a monitoring rule to block that attack in the future. Dynatrace is configured to block future exploit situations, not the current ones.
The request (thread) with the exploit throws an exception in the running code. All other users who aren't attacking are unaffected.  
Dynatrace detects when a user-supplied attack payload finds its way to a line of code that uses an insecure way of

* Talking to the database (SQL injection)
* Talking to the operating system (command injection)
* Doing a JNDI lookup (JNDI injection, such as Log4Shell)
* Doing a HTTP request (SSRF)

The vulnerability is identified with or without an attack. If the data sent by the client includes characteristics of an attack that reaches this line of code, it's deemed an exploit, and Dynatrace alerts or blocks it.

To learn more about the Runtime Application Protection mechanism, see [How it works](/docs/secure/application-security/application-protection#mechanism "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

### How is an attacker's IP determined?

In Runtime Application Protection, to determine an attacker's IP, Dynatrace verifies

* Specific HTTP headers, such as `X-Client-IP` or `X-Forwarded-For`.

* The client IP of the socket connection (if the HTTP headers mentioned above aren't available).

  For details, see [Client IP address detection](/docs/secure/threats-and-exploits#client-ip-address "Understand, triage, and investigate detection findings and alerts.").

## Data retention

### What's the data retention period for vulnerabilities, events, and attacks?

For information about how security-related data is stored in Dynatrace, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").

## Consumption

### How can I check how much my hosts consume?

* If you're using [Dynatrace Platform Subscription](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), see:

  + [Calculate your consumption of Runtime Vulnerability Analytics](/docs/license/capabilities/application-security/runtime-vulnerability-analytics "Learn how your consumption of the Dynatrace Runtime Vulnerability Analytics (RVA) DPS capability is billed and charged.")
  + [Calculate your consumption of Runtime Application Protection](/docs/license/capabilities/application-security/runtime-application-protection "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.")
  + [Calculate your consumption of Security Posture Management](/docs/license/capabilities/application-security/security-posture-management "Learn how your consumption of the Dynatrace Security Posture Management (SPM) DPS capability is billed and charged.")
* If you're using [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."), see [How capabilities affect monitoring consumption](/docs/license/monitoring-consumption-classic/application-security-units#how-capabilities-affect-monitoring-consumption "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.").

deprecated To see which hosts consume DPS/ASUs, in ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview**, go to the **Host coverage** section for third-party and code-level vulnerabilities and select **Monitored hosts**. The resulting list of hosts are the hosts in your environment which consume DPS/ASUs.
For more information, see [Host coverage](/docs/secure/application-security/vulnerability-analytics/application-security-overview#host-coverage "Get an overview of the security issues of your third-party libraries.").

### Why is Application Security still showing usage even though I disabled RVA?

***I disabled Thirdâparty and Codeâlevel Vulnerability Analytics. My host shows 'Not analyzed', yet usage is still appearing in my subscription. Why?***

This behavior applies to both [Dynatrace classic licensing (ASU)](/docs/license/monitoring-consumption-classic/application-security-units#how-capabilities-affect-monitoring-consumption "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") and [Dynatrace Platform Subscription (DPS)](/docs/license/capabilities/application-security/runtime-application-protection "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.").

Check whether Runtime Application Protection (RAP) is enabled. RAP depends on Runtime Vulnerability Assessment (RVA) to determine which vulnerability an attack attempts to exploit. Because RAP cannot operate without RVA, any host with RAP enabled will always consume ASUs/DPS for both RAP and RVAâeven if the global switches for thirdâparty or codeâlevel vulnerability detection are turned off.