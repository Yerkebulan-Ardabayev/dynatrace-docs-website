---
title: Runtime Application Protection
source: https://www.dynatrace.com/docs/secure/application-security/application-protection
scraped: 2026-02-15T09:02:44.752186
---

# Runtime Application Protection

# Runtime Application Protection

* Latest Dynatrace
* How-to guide
* Updated on Nov 03, 2025

Dynatrace Runtime Application Protection leverages code-level insights and transaction analysis to detect and block exploitation attempts on your applications automatically and in real time.

## Capabilities

* Detection of SQL injection, JNDI injection, command injection, and SSRF attacks
* Code-level visibility provided by OneAgent
* Production-ready performance footprint
* Configurable automatic blocking of detected attacks
* Protection of web applications and APIs
* High alert precision with rich context to optimize your team's performance and make every minute count

## How it works

[Runtime Application Protection (RAP)](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") uses runtime instrumentation to detect and optionally block exploit attempts. When your application receives a web request, [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") tracks user input and analyzes how it interacts with sensitive code paths, such as SQL queries, OS commands, or JNDI lookups. If the behavior matches a known attack pattern, Dynatrace reports it as a security finding. If attack blocking is enabled, OneAgent throws an exception to stop the malicious request before it executes. RAP is lightweight and safe for use in production environments.

## Prerequisites

Before you begin, ensure your environment meets the necessary requirements:

* You're using a supported version of Dynatrace. Review the [release notes](/docs/whats-new "Read the product news and the release notes and find out which Documentation topics are new.") for currently supported versions.
* For Runtime Application Protection to work properly, make sure deep monitoring is enabled in **Settings** > **Processes and containers** > **Process group monitoring**.

  For .NET, Go, and Python technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Supported technologies

Dynatrace detects SQL injection, JNDI injection, command injection, and SSRF attacks in the following technologies.

| Technology | Minimum OneAgent version | SQL injection | Command injection | JNDI injection | SSRF |
| --- | --- | --- | --- | --- | --- |
| Java 8 or higher[1](#fn-1-1-def) | 1.241 |  |  |  |  |
| .NET[2](#fn-1-2-def)'[3](#fn-1-3-def) | 1.289 |  |  |  |  |
| Go[3](#fn-1-3-def) | 1.311 |  |  |  |  |

1

Only supported on Windows x86 and Linux x86 systems.

2

Only .NET Framework 4.5, .NET Core 3.0 or higher, and 64-bit processes are supported.

3

For .NET and Go technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Get started

To set up Runtime Application Protection, follow the instructions below.

To use preview features, please contact a Dynatrace product expert via live chat to **activate Runtime Application Protection** before continuing.

Enable Runtime Application Protection

To enable Runtime Application Protection globally on your environment

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New**).
2. Enable Runtime Application Protection.
3. Select **Enable**.
4. Restart your processes.

Define the global attack control

To define the global attack control for all process groups

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)** > **Monitoring rules** > **Default rules**.
2. Edit the attack control per technology:

* **Off; incoming attacks NOT detected or blocked.**âMonitoring is disabled; no attacks in the selected technology are reported.
* **Monitor; incoming attacks detected only.**âMonitoring is enabled; no attacks in the selected technology are blocked.
* **Block; incoming attacks detected and blocked.**âMonitoring is enabled; attacks in the selected technology are blocked at runtime.

If you define [custom monitoring rules](/docs/secure/application-security/application-protection/application-protection-rules#handling-rules "Create, modify, and delete rules for specific attacks.") based on certain process groups or vulnerability types, the custom rules override the global attack control for the selected technology, and Runtime Application Protection continues to monitor the attacks based on your rules.

3. Select **Save**.
4. Restart your processes.

Enable OneAgent monitoring

1. Go to **Settings (New)** and select **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Filter by `code-level attack evaluation` and enable the feature for the technologies you want to monitor.
3. Select **Save changes**.
4. Restart your processes.

OneAgent version 1.309 To detect SSRF attacks, you also need to enable SSRF attack evaluation. See below for instructions.

1. Go to **Settings (New)** and select **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Find and enable `Java SSRF code-level vulnerability and attack evaluation`.
3. Select **Save changes**.
4. Restart your processes.

## What's next

After you set up Runtime Application Protection, you can

* Evaluate, triage, and investigate findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").
* [Set up Runtime Application Protection monitoring rules](/docs/secure/application-security/application-protection/application-protection-rules "Create, modify, and delete rules for specific attacks.").

## Consumption

Runtime Application Protection is licensed based on the consumption of [GiB-hours](/docs/license/capabilities/application-security/runtime-application-protection "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.") if you're using the [Dynatrace Platform Subscription (DPS) licensing model](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), or [Application Security units (ASUs)](/docs/license/monitoring-consumption-classic/application-security-units "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") if you're using the [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")