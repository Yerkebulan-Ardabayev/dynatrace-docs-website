---
title: Instant Intrusion Response
source: https://www.dynatrace.com/docs/secure/use-cases/instant-intrusion-response
scraped: 2026-02-15T21:28:06.931389
---

# Instant Intrusion Response

# Instant Intrusion Response

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

Time is crucial when dealing with security incidents. This page shows how you can use Dynatrace to speed up your incident response in two phases:

* When an attack is detected, Dynatrace can automate the notification and analysis for you, so that the right teams are informed and receive actionable information to start working on the issue.
* When investigating an issue, each new discovery guides the next steps in the incident response. Through Grailâs schemaless queries, Dynatrace allows you to remain flexible in this time-critical process.

## Target audience

This page is intended for Security teams analyzing security incidents, such as the Incident Response team.

## Scenario

In the following, we address a scenario in which identifying an attack, researching the scope, determining the responsible entity owners, and remediating the attack takes hours, sometimes even days.

* Tools like AWS GuardDuty trigger events on suspicious activity independently.
* Handling the incoming load while increasing security strength is impossible.
* All correlation and collaboration are manual, resulting in frustration about the silos.
* Several internal integration tools, hard to manage, have been built; they are helpful, but aren't providing solid and safe automation.
* A typical suspicious incident takes days to escalate and qualify.

### Request

The team wants to quickly

* Identify when a possible attack is happening.
* Research the scope and determine what is affected: for example, whether the attack affects only a single isolated, non-production system or threatens a critical part of the environment.
* Determine the responsible entity owners.
* Remediate the attack.

### Goals

* **Efficiency**: The team should be able to respond much faster to attacks.
* **Flexibility**: The team should have more flexibility in their response to security incidents.

### Result

Combining the Dynatrace automation capabilities with insights into security-related data, our solution helps security teams react and respond faster to attacks. The team automatically scans all ingested logs for patterns that might indicate possible attacks. Because each attack is different, they make use of schemaless queries with instant responses to quickly identify the scope of an attack, thus reducing the required time from days to minutes.

## How it works

### Context

Logs from your [Dynatrace-monitored environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") are ingested into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") via [log ingestion](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace."). When an attack is detected, a Dynatrace problem is created.

### 1. Intrusion notification automation

A workflow is automatically triggered by this type of problem. The workflow collects, processes, and enriches the data with context, and converts the resulting information into notifications on your desired channels.

For an example of how you can set up an attack notification automation, see [Intrusion notification automation](#workflow).

### 2. Instant queries

Based on the information received, you can immediately respond to discoveries and perform further investigations by running a sequence of DQL queries in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** tailored to the attack type.

For details, see [Instant queries](#notebook).

## Prerequisites

* Dynatrace version 1.283+
* [Set up log ingestion](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") (ingests security incidents into Grail).
* [Set up ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") (allows the workflow to assign security incidents based on ownership of the affected entity).
* [Set up Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.") (allows the workflow to convert resulting findings into Jira tickets).
* [Set up Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces") (allows the workflow to send resulting findings to Slack channels).

  While the current scenario uses Slack and Jira as notification channels, other integrations are also available. For details, see [Workflows integrations](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").
* Basic knowledge of how to

  + [Use Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
  + [Create workflows](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.")
* Make sure the following permissions are enabled.

  + **Grail**: `storage:logs:read`. For instructions, see [Assign permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
  + ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**: Permissions to access, view, write, and execute workflows. For details, see [Authorization](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

    To access permissions, go to the **Settings** menu in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.

## 1. Intrusion notification automation

The following example illustrates how you can implement an attack notification automation using [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."). You can customize the workflow according to your needs.

1. Set the trigger

The automation needs to be triggered whenever an attack occurs.

In the **Select trigger** section, select and configure **Davis Problem trigger**. For details, see [Create workflows in Dynatrace Workflows: Trigger](/docs/analyze-explore-automate/workflows/building#trigger "Create and edit workflows in Dynatrace Workflows.").

Show me the relevant workflow task sequence

![Set the trigger](https://dt-cdn.net/images/trigger-1700-3001e4f912.png)

2. Determine ownership

Route notifications to the team responsible for the affected entities.

Select the **Get owners** action to create and configure this task. For details, see [Ownership app: **`get_owners`**](/docs/deliver/ownership-app#get-owners "It provides custom actions to define workflows integrating entity owners and their contact information.").

Show me the relevant workflow task sequence

![Set ownership](https://dt-cdn.net/images/set-owners-1700-f719d66bac.png)

3. Set up notification variables

Configure variables such as default values for Slack and Jira fields, that will be used in later steps in the notification process.

Select the **Run JavaScript** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequences

![Define notification channels](https://dt-cdn.net/images/channels-1700-83943a78ba.png)

4. Collect data and enrich with context

* Query third-party services. For example:

  + Perform a WHOIS lookup to find details about the attacker's IP address.
  + Verify the IP reputation using a third-party service such as AbuseIPDB.

  Select the **HTTP Request** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").
* Query Dynatrace. For example:

  + Determine whether there were any successful logins from the attacker's IP address.
  + Find out additional traffic information from the attacker's IP address.

  Select the **Execute DQL Query** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequences

![Collect and enrich data](https://dt-cdn.net/images/collect-data-1700-2cf1aad6c7.png)

5. Extract successful requests

Extract the successful requests from the total requests collected.

Select the **Run JavaScript** action to create and configure this task. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequence

![Extract successful requests](https://dt-cdn.net/images/extract-successful-1700-7d72549785.png)

6. Replay against target

Replay the successful requests against the target entity to look for indicators of compromise. Custom code steps allow you to automate complex logic that you want to run for each detected attack. Depending on the detected attack and the affected systems, you might want to replay the attacks for more detailed analysis.

Select the **Run JavaScript** action to create and configure this task. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequence

![Replay against target](https://dt-cdn.net/images/replay-against-target-1700-dca61b334e.png)

7. Send notifications

* Notify the responsible team on Slack.

  Select the **Send message** action to create and configure this task. For details, see [Use Workflows with Slack](/docs/analyze-explore-automate/workflows/actions/slack#workflow "Send messages to Slack Workspaces").
* Create a Jira ticket for the entity owner containing the collected information.

  Select the **Create issue** action to create and configure this task. For details, see [Create Jira issues with workflows](/docs/analyze-explore-automate/workflows/actions/jira#workflow "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.").

Show me the relevant workflow task sequences

![Send notifications](https://dt-cdn.net/images/send-notifications-1700-52548fa8bb.png)

## 2. Instant queries

After receiving the notification, the security team can immediately respond to discoveries and instantly run additional DQL queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") without knowing beforehand where the information they're looking for is. In an emergency situation, this is crucial, as a speedy response can ensure that the attack can be contained.

The following are some examples of how you can query Grail in case of a web attack.

### Logs from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP ADDRESS>>"



| sort timestamp desc
```

### Successful web requests from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP Address>>"



| filter http.status_code == "200"



| sort timestamp desc
```

### Status codes and response codes overview

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP Address>>"



| summarize requests=count(), by:{http.status_code, http.user_agent}



| sort http.status_code
```

### Payloads used by the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



// Successful requests only



| filter http.status_code == "200"



| filter net.peer.ip == "<<IP Address>>"



| summarize requests=count(), by:{http.target}



| sort requests DESC
```

### Successful requests from a given IP address sorted by response size

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| fields timestamp, net.peer.ip, http.target, http.status_code, http.response_content_length, http.user_agent



| filter http.status_code == "200"



// Filter for a specific IP address



| filter net.peer.ip == "<<IP Address>>"



| sort toLong(http.response_content_length) DESC
```

### Payloads in access logs (both successful and not successful)

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| fields payload = "<<PAYLOAD>>", timestamp, net.peer.ip, http.method, http.target, http.status_code, http.request.header.referrer, http.response_content_length, http.user_agent, content



| filter contains(content, payload)
```

### Successful SSO logins from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes: -1



// Search for logins



| filter log.source == "/var/log/sso.log"



// Search for successful logins from a given IP address



| filter contains(content, "user login successful") and contains(content, "<<IP address>>")



| sort timestamp desc
```

### Which environments the attacker has logged into

Query example:

```
fetch logs, scanLimitGBytes: -1



// Search for logins



| filter log.source == "/var/log/sso.log"



// Search for logins from a given account id



| filter contains(content, "<<Account ID>>") and contains(content, "tenant: ")



| sort timestamp desc
```

## Stay ahead of threats

You can use the above instructions as building blocks to automate common steps in your incidents process. These can help you respond faster to security incidents, thus reducing their impact.

## Further reading

[Log on Grail examples](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")

[Dynatrace Intelligence DQL examples](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")

[DQL examples for security-related data](/docs/secure/threat-observability/dql-examples "DQL examples for security data powered by Grail.")