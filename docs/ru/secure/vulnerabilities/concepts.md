---
title: Vulnerabilities concepts
source: https://www.dynatrace.com/docs/secure/vulnerabilities/concepts
scraped: 2026-02-18T21:35:58.241010
---

# Vulnerabilities concepts

# Vulnerabilities concepts

* Latest Dynatrace
* Explanation
* Updated on Dec 18, 2025

Understand essential concepts and key terms for ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**.

## How Dynatrace uses CVSS

Third-party vulnerabilities

Dynatrace uses the [Common Vulnerability Scoring System (CVSS)ï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System) to assess and contextualize vulnerabilities. CVSS provides a standardized framework for describing the severity, exploitability, and impact of vulnerabilities using structured vector strings and numerical scores.
This scoring system forms the foundation for the Dynatrace Security Score (DSS), which adds environmental context to help prioritize remediation.

### CVSS data source

CVSS vector data is sourced from the Snyk vulnerability feed, which includes both CVSS v3 and CVSS v4 vectors when available.

### Scoring logic

Dynatrace supports both CVSS v3 and CVSS v4 for vulnerability scoring. CVSS vector data is sourced from both the Snyk vulnerability feed and the National Vulnerability Database (NVD). When CVSS v4 vectors are available in the Snyk feed, they are used to calculate the [Dynatrace Security Score (DSS)](#dss). If CVSS v4 is not available, CVSS v3 vectors are used as a fallback.

CVSS v4 is currently supported only for vulnerabilities sourced from Snyk, not from NVD.

Scoring is based on the official [CVSS v4 calculatorï»¿](https://github.com/FIRSTdotorg/cvss-v4-calculator/blob/main/cvss_score.js) provided by [FIRST.orgï»¿](https://www.first.org/).

### CVSS vectors

In ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, each vulnerability displays two types of CVSS vectors:

* **CVSS Base Vector**: Describes the vulnerability's inherent characteristics, such as its attack vector, required privileges, user interaction, and impact on confidentiality, integrity, and availability. These traits are static and don't change across environments.
* **CVSS Modified Vector**: Adjusts the base metrics to reflect your specific environment. This includes factors like asset exposure and reachability. Modified vectors provide a more accurate reflection of risk in your context.

  + For **CVSS v3**, modified impact metrics are labeled as `MC` (Confidentiality), `MI` (Integrity), and `MA` (Availability).
  + For **CVSS v4**, these are updated to `MVC`, `MVI`, and `MVA`, where the "V" stands for **Vulnerable System Impact Metrics**, reflecting the impact on the vulnerable system itself.

Both vectors are visible on the **Prioritization** page:

* In the vulnerabilities table (go to the [column settings](/docs/secure/vulnerabilities/manage-results#format "Filter, format, and sort to find relevant vulnerability information.") ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") and select **CVSS Base Vector** and **CVSS Modified Vector**).
* In the details of a vulnerability (in the side panel that opens when you select a vulnerability, go to **Overview** and look for **Dynatrace Security Score calculation**).

This visibility helps you understand how the CVSS score was derived and compare raw versus contextualized risk.

Dynatrace supports filtering by CVSS vector components for advanced triage. For practical examples and usage, see [Filter by CVSS vectors](/docs/secure/vulnerabilities/manage-results#cvss-filter "Filter, format, and sort to find relevant vulnerability information.").

## Dynatrace Security Score

Dynatrace calculates the severity of a vulnerability based on Dynatrace Security Score (DSS), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact.

DSS
:   An enhanced risk-calculation score based on the industry-standard [Common Vulnerability Scoring System (CVSS)ï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System). Dynatrace Security Score is designed to provide a more precise risk-assessment score by considering additional parameters such as public internet exposure and whether or not data assets are reachable from an affected entity.

**Risk-averse**: Virtually all security products use the CVSS Base Score to set the severity of security vulnerabilities. CVSS was designed to be risk-averse, which means that, for any given vulnerability, the assigned score assumes the worst-case scenario. The CVSS specification does allow for some modifications based on environmental influences, but this is usually not factored into the risk score calculation, which leads to many high or critical vulnerability scores that the user needs to handle.

**Accurate**: Dynatrace Security Score doesn't assume the worst-case scenario. Instead, it adapts the characteristics of the vulnerability to your particular environment, taking into consideration its structure and topology, and advises you as to which elements are at risk and how to handle security issues. With Dynatrace Security Score, you can find out if the affected entity is reachable from the internet and if there is any data storage in reach of an affected entity.

**Efficient**: By including additional parameters in its analysis, Dynatrace Security Score is designed to leverage data to more precisely calculate the security score and predict the potential risk of a vulnerability to your environment. By reducing the score of vulnerabilities that are considered less relevant for your environment, you gain time to focus on the most critical issues and fix them faster.

### Vulnerability score calculation

Third-party vulnerabilities

Code-level vulnerabilities

Dynatrace determines the Dynatrace Security Score for third-party vulnerabilities through a combination of CVSS data and environmental context:

1. Gather CVSS vector data

Vectors are pulled from both the Snyk vulnerability feed and the National Vulnerability Database (NVD).

* CVSS v4 is currently supported *only* for vulnerabilities from Snyk.
* CVSS v2 is [deprecatedï»¿](https://dt-url.net/f6k3wfz). For vulnerabilities relying on this data, Dynatrace Security Score can't be assessed. For the supported CVSS versions, see [How Dynatrace uses CVSS](#cvss).

2. Determine applicable CVSS version

If CVSS v4 vectors are available, theyâre used to calculate DSS. Otherwise, Dynatrace falls back to CVSS v3.

3. Incorporate environmental context

DSS adjusts the CVSS Base Score using modifiers that reflect your environment:

* **For CVSS v3**:

  + `MC` â Modified Confidentiality
  + `MI` â Modified Integrity
* **For CVSS v4**:

  + `MVC` â Modified Vulnerable Confidentiality
  + `MVI` â Modified Vulnerable Integrity

    These belong to the **Vulnerable System Impact Metrics** group in CVSS v4.

4. Calculate DSS for each affected entity

DSS is calculated individually for each affected entity. If multiple entities are impacted, the highest DSS score is used.

DSS never exceeds the original CVSS Base Score; environmental modifiers can only reduce or maintain the score.

The score of a code-level vulnerability is always `10` and the risk always `Critical` because it's considered to be exploitable at any time.

For example, on a login page where the password hasn't been sanitized before sending it to the database, thus allowing an SQL injection, it's only a matter of time until an attacker finds this vulnerability and exploits it.

### Dynatrace Risk Levels

The DSS scale ranges between 0.1 (lowest risk) and 10.0 (most critical risk):

| **Dynatrace Risk Level** | **Vulnerability score range** |
| --- | --- |
| Low risk Low | Vulnerabilities ranging between 0.1 and 3.9 |
| Medium risk Medium | Vulnerabilities ranging between 4.0 and 6.9 |
| High risk High | Vulnerabilities ranging between 7.0 and 8.9 |
| Critical risk Critical | Vulnerabilities ranging between 9.0 and 10.0 |

### Calculation differences



The Dynatrace Security Score (DSS) calculation differs between ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** and ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.

| **App** | **DSS assessment** |
| --- | --- |
| Third Party Vulnerabilities **Third-Party Vulnerabilities** | DSS is assessed based on aggregating the scores of affected entities within the selected management zone. |
| Vulnerabilities **Vulnerabilities** | DSS is assessed based on the DSS of the affected entities within the selected segment. |

Thus, the DSS (score and risk level) for vulnerabilities in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** can be lower than in ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.

#### Example

A vulnerability with `Critical` severity affects two processes, `Process_1` and `Process_2`.

1. Evaluation of risk assessment

* `Process_1` is exposed to the public internet but has no reachable data assets => DSS lowers the severity to `High`.
* `Process_2` isn't exposed to the public internet but has reachable data assets => DSS lowers the severity to `High`.

2. Final score

* In ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, DSS aggregates the risk factors of the affected entities (the vulnerability is both exposed to the public internet and has reachable data assets), thus the severity remains `Critical`.
* In ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, the score is determined by the affected entity with the highest DSS score. So if both affected entities have `High` severity, the severity is lowered from the initial `Critical` to `High`.

How to use: You can [prioritize vulnerabilities based on DSS](/docs/secure/vulnerabilities/prioritize#dss "Prioritize third-party, code-level, and runtime vulnerabilities.").

## Coverage

Coverage refers to the extent to which your environment's processes are monitored by Runtime Vulnerability Analytics (RVA). This processâlevel information is aggregated to the host level. Coverage determines whether vulnerabilities can be detected and reported for the monitored processes and their corresponding hosts.

Coverage:

* Highlights monitoring gaps where vulnerabilities may go undetected.
* Identifies the most affected processes with the corresponding hosts.
* Provides trends in findings and scans over time.

For practical guidance on how to visualize coverage, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

## Security Advisor

Security Advisor recommends the fixes that would most improve the overall security of your environment.

### Basis for calculation

To calculate recommended fixes, Security Advisor takes into consideration all third-party vulnerabilities that are currently open and not muted; resolved or muted vulnerabilities aren't taken into account. Fixes are tailored to your environment and ranked based on how much they improve the overall security of your environment.

### Grouping

Security Advisor groups specific libraries that trigger vulnerabilities to simplify remediation efforts.
When calculating the advice, Security Advisor ignores the specific version of the library. All shown libraries contain known vulnerabilities and should be updated to the latest version.

### Advice ranking

Advice is ranked based on the severity of the third-party vulnerabilities. Advice regarding a critical vulnerability, for example, is ranked higher than advice for a high-severity vulnerability.

The severity of a vulnerability is calculated based on [Dynatrace Security Score (DSS)](#dss), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact.

## Dynatrace Assessment

Understand the risk factors and assessment modes considered when assessing a vulnerability.

* [Public internet exposure](#internet-exposure)
* [Reachable data assets](#data-assets)
* [Vulnerable functions](#vulnerable-functions) Third-party vulnerabilities
* [Public exploit](#public-exploit) Third-party vulnerabilities
* [Assessment mode](#assessment-mode)

### Public internet exposure

Public internet exposure
:   One of the risk factors taken into consideration when determining the [Dynatrace Security Score](#dss). If there is public internet exposure, it means that vulnerabilities affect at least one process that is exposed to the internet.

#### States

| **State** | **Description** |
| --- | --- |
| Public network | There is public internet exposure. |
| Not detected | No public internet exposure was found. |
| Not available | Data isn't available, because the related hosts aren't running in Full-Stack Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Public internet exposure`.

Further reading: [How is public internet exposure determined?](/docs/secure/faq#internet-exposure "Frequently asked questions about Dynatrace Application Security.")

### Reachable data assets

Reachable data assets
:   One of the risk factors taken to consideration when determining the [Dynatrace Security Score](#dss). If there are any reachable data assets affected it means that vulnerabilities affect at least one process that has database access (runs a database service).

#### States

| **State** | **Description** |
| --- | --- |
| Within range | There are reachable data assets affected. |
| None within range | There are no reachable data assets within range. |
| Not available | Data isn't available, because the related hosts aren't running in Full-Stack Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Reachable data assets`.

### Vulnerable functions

Third-party vulnerabilities

Vulnerable function
:   One of the risk factors to consider when evaluating a vulnerability (yet they are not considered for the DSS calculation). If there are any vulnerable functions in use, there is at least one process using a vulnerable function (this might indicate a higher exploitation risk).

Class
:   The class that contains the vulnerable function related to the vulnerability.

    * Example: `org.apache.http.client.utils.URIUtils`

Function usage
:   Shows whether the vulnerable function is being used by your application. Based on whether your application uses the vulnerable function, you can assess the impact on your environment. The usage of a vulnerable function is calculated on the process level and is aggregated to the process group level, which results in a count of affected process groups per function.

    * Examples: `In use`, `Not in use`, `Not available`

#### States

| **State** | **Description** |
| --- | --- |
| In use | There are vulnerable functions in use. |
| Not in use | No vulnerable functions in use were found. |
| Not available | Data isn't available. For details, see [FAQ: Why is there no data available for vulnerable function?](/docs/secure/faq#vuln-funct-no-info-available "Frequently asked questions about Dynatrace Application Security."). |

How to use: You can

* [Filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Vulnerable functions in use`
* [Prioritize vulnerabilities based on vulnerable functions](/docs/secure/vulnerabilities/prioritize#details-functions "Prioritize third-party, code-level, and runtime vulnerabilities.")

Further reading:

* [How are vulnerable functions determined?](/docs/secure/faq#vuln-function-calculation "Frequently asked questions about Dynatrace Application Security.")
* [Why is there no information on vulnerable functions?](/docs/secure/faq#vuln-function-no-info-available "Frequently asked questions about Dynatrace Application Security.")
* [Why is there no data available for vulnerable functions?](/docs/secure/faq#vuln-function-no-data-available "Frequently asked questions about Dynatrace Application Security.")

### Public exploit

Third-party vulnerabilities

Public exploit
:   One of the risk factors to be considered when assessing a vulnerability. If there is any public exploit published, it means that malicious code to exploit this vulnerability is available on the internet.

#### States

| **State** | **Description** |
| --- | --- |
| Public exploit published | A publicly known exploit for this vulnerability is available. |
| No public exploit published | No publicly known exploit for this vulnerability is available. |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Public exploit published`.

### Assessment mode



Assessment mode
:   Determines whether detailed analysis is possible based on your monitoring mode.

#### States

| **State** | **Description** |
| --- | --- |
| Full | All process group instances are monitored in [Full-stack monitoring mode](/docs/secure/application-security#fullstack "Access the Dynatrace Application Security functionalities."). |
| Reduced | Detailed assessment isn't possible because at least one process group instance isn't monitored in Full-stack monitoring mode. |
| Not available | The vulnerability is resolved. |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Assessment mode`.

#### How reduced accuracy affects the DSS calculation

The context of internet exposure or reachable data assets cannot be examined due to the lack of information, thus the DSS score can't be lowered.

## Affected and related entities

Learn about the entities affected by and related to vulnerabilities in your environment.

### Affected entities

Affected entities
:   Entities (process groups, processes, and Kubernetes nodes) for which a vulnerability was detected, and are therefore directly affected by the vulnerability.

Affected process
:   A process that contains a vulnerable library or runtime.

How to use: You can [prioritize vulnerabilities by affected entities](/docs/secure/vulnerabilities/prioritize#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.").

### Related entities

Related entities
:   Entities that are connected to one of the affected entities and, thus, indirectly affected by the vulnerability.

Related application
:   An application associated with the affected processes.

Related service
:   A service that runs directly on a vulnerable process group instance.

Related host
:   A host on which the vulnerable process runs.

Related database
:   A database that is accessed by the vulnerable process or reachable from it. It can be reached via multiple hops.

Related Kubernetes workload/cluster
:   In Kubernetes environments, the workload or cluster to which the vulnerable process belongs.

Related container image
:   In Kubernetes environments, the container image used by the affected processes.

How to use: You can [prioritize vulnerabilities by related entities](/docs/secure/vulnerabilities/prioritize#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.").

## Vulnerability source

Drill down into the source of vulnerabilities for the [vulnerable component](#vulnerable-component), [entry point](#entry-points), and [code location](#code-location).

### Vulnerable component

Third-party vulnerabilities

Vulnerable component
:   A software component (library) or runtime component (for example, a Kubernetes package) that has a vulnerable function causing a vulnerability:

    * For Snyk-based vulnerabilities, the package name (example: `org.apache.tomcat:tomcat-coyote`)

    * For NVD-based vulnerabilities, the runtime technology (examples: `Java runtime`, `Node.js runtime`)

How to use: You can [drill down and explore vulnerable components](/docs/secure/vulnerabilities/address-remediation#vulnerable-component "Address remediation and optimize remediation activities.").

Further reading: [Why is a fixed vulnerability still showing as open?](/docs/secure/faq#open "Frequently asked questions about Dynatrace Application Security.")

### Entry point

Code-level vulnerabilities

Entry point
:   A point in the code where an attacker could enter the application, for example, by passing user input fields to the application (such as a login form or search bar).

URL path
:   The path used in the HTTP request to reach and potentially exploit the vulnerability.

    * Example: `/user/1218/bio`

Untrusted input
:   The input that is passed to the vulnerable function.

Payloads
:   The user-controlled inputs that could be used to exploit the vulnerability. This may be the part of the SQL statement (for SQL injection), the command (for command injection), the JNDI lookup name (for improper input validation), or the request URL (for SSRF).
    The userâcontrolled input is highlighted. If the payload has an associated key (for example, an HTTP parameter name or an HTTP header name), it's shown after a colon.

    * Example: `HTTP parameter value: bioText`

How to use: You can [drill down and explore entry points](/docs/secure/vulnerabilities/address-remediation#entry-points "Address remediation and optimize remediation activities.").

### Code location

Code-level vulnerabilities

Code location
:   Shows where the actual vulnerability is in the code (the location where the vulnerable function is called from).

    * Example: `SQL injection at DatabaseManager.updateBio():82`

How to use: You can [drill down and explore code location](/docs/secure/vulnerabilities/address-remediation#code-location "Address remediation and optimize remediation activities.").

## Vulnerability status

Learn about the resolution and mute status of a vulnerability or [affected entity](#affected).

### States for vulnerabilities

| **State** | **Description** |
| --- | --- |
| Open | The vulnerability is active. |
| Resolved | The vulnerability was closed automatically because the root cause is no longer present. For details, see [Vulnerability evaluation: Resolution](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |
| Muted (Open) | The vulnerability is active but all its affected entities were muted by request. |

How to use: On the **Prioritization** page, you can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.")

* By **Status** to see `Open` and `Resolved` vulnerabilities
* By **Mute: Status** to see `Muted (Open)` vulnerabilities

  Resolved vulnerabilities are displayed only once (at the resolution time). Extend the timeframe to include more results. For details, see [Timeframe filter](/docs/secure/vulnerabilities/manage-results#timeframe "Filter, format, and sort to find relevant vulnerability information.").

### States for affected entities

| **State** | **Description** |
| --- | --- |
| Affected | The entity is affected by the vulnerability. |
| Resolved | The entity was closed automatically because the root cause is no longer present. |
| Muted (Affected) | The entity is affected by the vulnerability but was silenced by request. |
| Muted (Resolved) | The silenced vulnerability was closed automatically because the root cause is no longer present. |

A muted entity that was closed automatically doesn't change its status to `Resolved`, but to `Muted (Resolved)`.

How to use: On the overview page of affected process groups or Kubernetes nodes, you can

* [Filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.")

  + By **Status** to see the affected entities that are `Affected` or `Resolved`
  + By **Mute** > **Mute: Status** to see affected entities that are `Muted (Affected)` or `Muted (Resolved)`
* [Format](/docs/secure/vulnerabilities/manage-results#format "Filter, format, and sort to find relevant vulnerability information.") affected entities table by **Status**
* [Change the mute status of affected entities](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.")

Further reference: [Can a vulnerability be resolved while there are still affected entities?](/docs/secure/faq#resolution-affected-entities "Frequently asked questions about Dynatrace Application Security.")

## Third-party library events



Third-party libraries

Prerequisite: [Enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

To help you monitor and analyze **third-party libraries** in your applications, Dynatrace provides detailed event data that captures how external libraries are assessed for security risks.

This data is represented through two types of security events:

* `VULNERABILITY_FINDING`: Represents a single vulnerability identified in a specific process at a given time.

  + For details, see [Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
* `VULNERABILITY_SCAN`: Represents the analysis of detected packages within a specific process at a given time.

  + For details, see [Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.").

Both types are stored in the `security.events` table and can be queried using [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

As Dynatrace analyzes the libraries used by your application, it continuously generates vulnerability findings. These raw events reflect the same underlying vulnerability data shown in [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), but in a more granular form.

The table below highlights the core differences between the granular finding events and the aggregated view in the app and entity events:

| **Granular view (DQL)** | **Aggregated view (Vulnerabilities **Vulnerabilities**)** |
| --- | --- |
| Continuously generated by Dynatrace during library analysis | Aggregated from entity state events |
| Unaggregated event data: `VULNERABILITY_FINDING` and `VULNERABILITY_SCAN` | Vulnerability-based view with comprehensive summaries |
| Not influenced by user actions | Includes [states](#status) (open/resolved) and user-controlled input like [mute states](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.") and [tracking links](/docs/secure/vulnerabilities/address-remediation#remediation-tracking "Address remediation and optimize remediation activities.") |
| Queried using DQL | Accessed via the app interface or via DQL by querying entity state events |
| Offers deeper investigative context for custom analysis | Designed for high-level overview and vulnerability management |

Both views reflect the same underlying data and are complementaryâuse DQL for deep dives and ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** for concise overviews and comprehensive risk analysis.

Here's an example DQL query to retrieve vulnerability findings and scans:

```
fetch security.events



| filter event.provider == "Dynatrace"



| filter event.type == "VULNERABILITY_FINDING" OR event.type == "VULNERABILITY_SCAN"
```

## Ingested vulnerability findings

In addition to findings generated by Dynatrace through [thirdâparty library detection](#tpv-events) and code-level vulnerability detection, vulnerability findings can also be ingested from external security tools. These originate outside Dynatrace and are brought in via [security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail."). For details, see [Vulnerability findings](/docs/secure/threat-observability/concepts#vuln-findings "Basic concepts related to Threat Observability").

Ingested findings represent individual vulnerabilities reported by thirdâparty products. They are stored in the `security.events` table and available in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** on the [**Findings** page](/docs/secure/vulnerabilities/explore-findings "View, filter, and analyze vulnerability findings from Dynatrace and external security tools."), where you can filter, sort, remove duplicates, and analyze them alongside Dynatraceâgenerated findings.

### Severity normalization mapping

To ensure consistency across sources, severity and risk scores from external tools are normalized to the Dynatrace unified risk scale.

Severity normalization follows this mapping:

| Reported severity | Normalized score |
| --- | --- |
| Critical | 10.0 |
| High | 8.9 |
| Medium | 6.9 |
| Low | 3.9 |
| Other/unknown | 0.0 |

For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").