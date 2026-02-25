---
title: CSPM Notification Automation
source: https://www.dynatrace.com/docs/secure/use-cases/notification-automation
scraped: 2026-02-25T21:18:31.859349
---

# CSPM Notification Automation

# CSPM Notification Automation

* Latest Dynatrace
* Tutorial
* Updated on Jan 31, 2024

Early Adopter

Hyperscalers provide offerings such as [AWS Security Hubï»¿](https://dt-url.net/5l239zz), through which security-related events give insights into potential threats. These events must be triaged, analyzed, and remediated by the owners of the affected resources, and reaching hundreds of thousands of such alerts is common.

* The volume of these events currently means that not all can get the attention they deserve.
* Because ownership of resources is distributed, significant coordination and administrative effort is required to ensure that all events are acted upon.

Dynatrace addresses these concerns and improves your cloud security posture management (CSPM) by introducing an automation workflow that filters security findings stored in Grail and triggers alerts only for the events that matter.

## Target audience

This page is intended for Security teams analyzing security findings.

## Scenario

In the following, we address a scenario in which 400,000 AWS alerts are issued daily.

Manually dealing with all of them is simply infeasible. The Security team therefore has to focus only on high-priority events and has built custom tooling to partially automate Jira ticket creation.

* Within a year, nearly 1,100 security tickets have been manually created from those events.
* Investigating those tickets has involved about 300 people gathering additional information to analyze the situation.

Effort is sometimes invested in vain, and alerts turn out to be irrelevant, but the resource owner must always cross-check the resolution with the Security team. Ensuring that all are followed up on requires a significant coordination effort, leaving less time for actual security work.

### Request

* The team wants to be able to explore all data but receive notifications (tickets) only for critical or high events and only for certain relevant AWS accounts.
* Notifications should include the alert type, full context, relevant details, and remediation advice to enable understanding, actionability, and operationalization.
* Only the account owner should be informed of the issue (tickets should be automatically assigned to him).
* The team doesn't want to be spammed with multiple notifications for the same issue, so there shouldn't be any duplicate tickets.

### Goal

**Efficiency**: The team should be able to act on everything that matters immediately.

### Result

**Dynatrace CSPM Notification Automation** is a tool designed to answer the Security team's pain and improve their efficiency significantly. It allows the team to continue monitoring events without being burdened with alerts; they can now focus only on what matters and requires their security expertise.

More concretely, from a total of 400,000 alerts per day, of which just 40,000 are relevant, with Dynatrace CSPM Notification Automation, only a couple of Jira tickets are now created daily, just for the relevant issues.

## How it works

Dynatrace CSPM Notification Automation consists of two stages.

1. (Prerequisite) AWS security findings from [AWS Security Hubï»¿](https://dt-url.net/5l239zz)
   are ingested into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") by means of [Dynatrace log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.").
2. (Actual automation) A predefined [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") orchestrates the processes of querying, filtering, and grouping data and converts the resulting findings into Jira tickets for remediation. See [Get started](#start) for the workflow steps.

![How CSPM automation works](https://dt-cdn.net/images/2024-01-31-15-04-14-470-834fcfc1a2.png)

## Prerequisites

See below for the [AWS](#aws) and [Dynatrace](#dt) requirements.

### AWS requirements

* [Set up AWS accountsï»¿](https://dt-url.net/ng439wv) for which you want to receive notifications.
* [Set up AWS Security Hubï»¿](https://dt-url.net/uh639rl) (collects AWS security findings).

### Dynatrace requirements

* Dynatrace version 1.276+
* [Set up log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") (ingests AWS security findings into Grail).
* [Set up Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira#setup "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.") (allows the workflow to convert resulting findings into Jira tickets).
* Make sure the following permissions are enabled.

  + **Grail**: `storage:logs:read`. For instructions, see [Assign permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
  + ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**: Permissions to access, view, write, and execute workflows. For details, see [Authorization](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

    To access permissions, go to the **Settings** menu in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.

## Get started

Once your AWS security findings are ingested into Grail (see [Prerequisites](#prerequisites)), you can set up the CSPM Notification Automation workflow.

The workflow consists of several steps you can adapt according to your needs. To configure it, you can start by importing a prefilled workflow into your environment.

1. Import workflow

1. Copy and save the JSON file below.

   ```
   {



   "id": "dcce961d-26a9-46e6-a9e4-14a0f7f2185c",



   "title": "CSPM Notification Automation",



   "description": "",



   "tasks": {



   "count_all_new_findings": {



   "name": "count_all_new_findings",



   "description": "Executes query to count all recently created AWS findings",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| fields timestamp\n| filter timestamp > now() - 24h                                                                        // Only filter created since last successful run         \n| summarize { count=count() }"



   },



   "position": {



   "x": -1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "log_new_findings_count": {



   "name": "log_new_findings_count",



   "description": "Logs total number of recently created AWS findings",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n\n  const ex = await execution(executionId);\n  const countResult = await ex.result(\"count_all_new_findings\");\n\n  console.log('======================================================================')\n  console.log('Total findings added since last run: ')\n  console.log(countResult.records[0].count)\n  console.log('')\n}"



   },



   "position": {



   "x": -1,



   "y": 3



   },



   "predecessors": [



   "count_all_new_findings"



   ],



   "conditions": {



   "states": {



   "count_all_new_findings": "OK"



   }



   }



   },



   "log_tickets_by_account": {



   "name": "log_tickets_by_account",



   "description": "Logs potentially created Jira issues for findings by account",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n  const ex = await execution(executionId);\n  const by_control_id = await ex.result(\"fetch_findings_by_account\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by accounts, ${by_control_id.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_control_id.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.controlId} - AWS account ${finding.awsAccountId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your account via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.awsAccountId}`)\n    console.log('')\n    console.log('Vulnerability:')\n    console.log(`${finding.controlId} - ${finding.title}`)\n    console.log(finding.severity)\n    console.log(finding.description)\n    console.log(finding.remediation[0].Recommendation.Url)\n    console.log('')\n    console.log('Affected resources:')\n    for(let resource of finding.resources) {\n      console.log(resource)\n    }\n    console.log('')          \n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_control_id.records;\n}"



   },



   "position": {



   "x": 0,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_account"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_account": "OK"



   }



   }



   },



   "workflow_config_params": {



   "name": "workflow_config_params",



   "description": "Sets configuration parameters for the workflow run",



   "action": "dynatrace.automations:run-javascript",



   "input": {



   "script": "// This step sets up some configurational parameters for the workflow run \n// (e.g. which accounts, which finding types we are filtering for)\nexport default async function () {\n\n  // AWS accounts to filter for\n  const awsAccountIds = [\n    // add your AWS account ids here, e.g.\n    // \"1234567890\"\n  ]\n\n  // Findings that should be grouped by AWS account\n  const securityControlIdsToGroupByAccount = [\n    // add you control IDs here, e.g.\n    // \"S3.1\" // S3 Block Public Access setting should be enabled\n  ]\n\n  // Findings that should be grouped by AWS Resource\n  const securityControlIdsToGroupByResource = [\n    // add you control IDs here, e.g.\n    // \"EC2.13\" // Security groups should not allow ingress from 0.0.0.0/0 to port 22\n  ]\n  \n  return { awsAccountIds, securityControlIdsToGroupByAccount, securityControlIdsToGroupByResource }\n}"



   },



   "position": {



   "x": 0,



   "y": 1



   },



   "predecessors": []



   },



   "log_tickets_by_resource": {



   "name": "log_tickets_by_resource",



   "description": "Logs potentially created Jira issues for findings by resource",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n  const ex = await execution(executionId);\n  const by_resource = await ex.result(\"fetch_findings_by_resource\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by resource, ${by_resource.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_resource.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.resource.resourceId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your resource via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.aws.accountId}`)\n    console.log('')\n    console.log('Resource details:')\n    console.log(finding.resource.resourceType)\n    console.log(finding.resource.resourceId)\n    console.log('')\n    console.log('Vulnerabilities:')\n    for(let vulnerability of finding.vulnerabilities) {\n      console.log(`${vulnerability.controlId} - ${vulnerability.title}`)\n      console.log(vulnerability.severity)\n      console.log(vulnerability.description)\n      console.log(vulnerability.remediation[0].Recommendation.Url)      \n    }\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_resource.records;\n}"



   },



   "position": {



   "x": 1,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_resource"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_resource": "OK"



   }



   }



   },



   "create_issue_for_account": {



   "name": "create_issue_for_account",



   "description": "Creates new Jira issue or the vulnerable AWS account",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 0,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_account": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_account\")}}"



   },



   "create_issue_for_resource": {



   "name": "create_issue_for_resource",



   "description": "Creates new issue for the vulnerable AWS resource",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 1,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_resource": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_resource\")}}"



   },



   "fetch_findings_by_account": {



   "name": "fetch_findings_by_account",



   "description": "Executes query to get relevant security findings grouped by AWS account",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resource = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByAccount | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus),\n              resources = collectDistinct(resource),\n              title = takeAny(title),\n              description = takeAny(description),\n              severity = takeAny(severity),\n              awsRegion = collectArray(awsRegion)\n            },\n            by:{\n              controlId, \n              awsAccountId\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields awsAccountId, entity.name\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n"



   },



   "position": {



   "x": 0,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "fetch_findings_by_resource": {



   "name": "fetch_findings_by_resource",



   "description": "Executes query to get relevant security findings grouped by AWS resource",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resourceId = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByResource | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus)\n            },\n            by:{\n              alertType, \n              resourceType, \n              controlId, \n              title,\n              description, \n              severity, \n              resourceId, \n              awsAccountId,\n              created,\n              awsRegion\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields id, awsAccountId, entity.name, tags, awsNameTag\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n| fields aws = record(\n            accountId = awsAccountId,\n            name = aws.account.entity.name,\n            entity = aws.account.id\n         ), \n         resource = record(\n           resourceId = resourceId,\n           resourceType = resourceType\n         ),\n         region = awsRegion,\n         alert = record(controlId = controlId, \n           severity = severity, \n           complianceStatus = complianceStatus,\n           title = title,\n           description = description,\n           remediation = remediation\n         )\n| summarize {\n        count=count(),\n        vulnerabilities = collectDistinct(alert)\n      },\n      by:{\n        aws,\n        resource,\n        region\n      }"



   },



   "position": {



   "x": 1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "prepare_tickets_by_account": {



   "name": "prepare_tickets_by_account",



   "description": "Prepares payload of Jira tickets for vulnerable AWS accounts",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n    const ex = await execution(executionId);\n    const records = await ex.result(\"log_tickets_by_account\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const resourcesList = finding.resources\n          .map( resource => `|${resource}|` )\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.controlId} - AWS Account ${finding.awsAccountId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.awsAccountId}|\\n\\n`\n              + '*Vulnerability*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + `|{noformat}${finding.controlId}{noformat}|{noformat}${finding.severity}{noformat}|${finding.title}|${finding.description}|[${finding.remediation[0].Recommendation.Url}]|\\n\\n`\n              + '*Affected Resources*:\\n'\n              + '||Resource Id||\\n'\n              + resourcesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 0,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_account": "OK"



   }



   }



   },



   "prepare_tickets_by_resource": {



   "name": "prepare_tickets_by_resource",



   "description": "Prepares payload of Jira tickets for vulnerable AWS resources",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n    const ex = await execution(executionId);\n    const records = await ex.result(\"log_tickets_by_resource\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const vulnerabilitiesList = finding.vulnerabilities\n          .map( vuln => \n            `|{noformat}${vuln.controlId}{noformat}|{noformat}${vuln.severity}{noformat}|${vuln.title}|${vuln.description}|[${vuln.remediation[0].Recommendation.Url}]|`)\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.resource.resourceId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.aws.accountId}|\\n\\n`\n              + '*Resource Details*:\\n'\n              + '||Resource Type||Resource Id||\\n'\n              + `|${finding.resource.resourceType}|${finding.resource.resourceId}|\\n\\n`\n              + '*Vulnerabilities*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + vulnerabilitiesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 1,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_resource": "OK"



   }



   }



   }



   },



   "ownerType": "USER",



   "isPrivate": false,



   "trigger": {



   "schedule": {



   "rule": null,



   "trigger": {



   "type": "time",



   "time": "09:00"



   },



   "timezone": "Europe/Berlin",



   "isActive": true,



   "isFaulty": false,



   "nextExecution": "2023-10-03T07:00:00.000Z",



   "filterParameters": {



   "earliestStart": "2023-09-25"



   },



   "inputs": {}



   }



   },



   "schemaVersion": 3



   }
   ```
2. In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, select **Upload** and upload the file.

2. Set the time

**Fixed time trigger**: Sets the time when you want the workflow to run (in the current case, the workflow runs every day at 9:00 AM). See [Schedule workflows](/docs/analyze-explore-automate/workflows/trigger/schedules "Guide to creating workflow automation schedule triggers in Dynatrace Workflows.") for more information on scheduling a workflow.

Show me the relevant workflow task

![Set the time in CSPM workflow ](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-79b6452375.png)

3. Define parameters

**Workflow config params**: Determines what findings you want to filter for. In the current scenario, the team wants to

* Receive notifications only about findings from important AWS accounts while discarding those from other accounts, such as environments that aren't in production.

  + Under `awsAccountIds`, select which AWS accounts you want to get findings for.
* Group findings for specific [security control IDsï»¿](https://dt-url.net/nx8393z) into one ticket per AWS account.

  + Under `securityControlIdsToGroupByAccount`, select which security control IDs you want to group by AWS account.
* Group findings for specific security control IDs into one ticket per AWS resource.

  + Under `securityControlIdsToGroupByResource`, select which security control IDs you want to group by AWS resource.

Show me the relevant workflow task

![Define parameters in CSMP workflow](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-711174cd7e.png)

4. Orchestrate findings

By AWS account

By AWS resource

The following task sequence orchestrates grouping and converting the resulting findings into one ticket per AWS account.

1. **Fetch findings by account**: Executes the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") that fetches the findings. Some of the information fetched for the current case, to be displayed in Jira, includes

   * Number of findings for the respective account
   * Issue title, including the security control IDs and the AWS account name
   * Short description of the vulnerabilities
   * Link to AWS for how to remediate the vulnerabilities
   * List of affected AWS resources
2. **Log tickets by account**: Shows a ticket's potential content before one is automatically created. This step ensures that your configuration is correct. For details, see [Plot statistics before creating tickets](#test).
3. **Prepare tickets by account**: Configures the payload for the Jira ticket.
4. **Create issues for account**: Integrates with your Jira connection. In **Input**, select your Jira connection created in [Prerequisites](#dt) and enter the desired parameters of the Jira ticket.

Show me the relevant workflow task sequence

![Group findings by AWS account](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e9069605d2.png)

The following task sequence orchestrates grouping and converting the resulting findings into one ticket per AWS resource.

1. **Fetch findings by resource**: Executes the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") that fetches the findings. Some of the information fetched for the current case, to be displayed in Jira, includes

   * Number of findings for the respective resource
   * Issue title, including the security control IDs and the AWS resource name
   * AWS account name of the respective resource
   * Resource details
   * Short description of the vulnerabilities
   * Link to AWS for how to remediate the vulnerabilities
2. **Log tickets by resource**: Shows a ticket's potential content before one is automatically created. This step ensures that your configuration is correct. For details, see [Plot statistics before creating tickets](#test).
3. **Prepare tickets by resource**: Configures the payload for the Jira ticket.
4. **Create issues for resource**: Integrates with your Jira connection. In **Input**, select your Jira connection created in [Prerequisites](#dt) and enter the desired parameters of the Jira ticket.

Show me the relevant workflow task sequence

![Group findings by AWS resource](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e30cc64df3.png)

5. Display statistics

The following task sequence displays a count of the new findings since the last workflow run.

1. **Count all new findings**: Executes the DQL query that fetches the number of findings created by AWS Security Hub in the last 24 hours.
2. **Log new findings count**: Displays the query result.

Show me the relevant workflow task sequence

![Display stats in CSPM workflow](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ac3fc24771.png)

Once you're done configuring the workflow, select **Save**.

### Plot statistics before creating tickets

To test your configuration before sending Jira tickets

1. Disable the **Prepare tickets by account/resource** and **Create issues for account/resource** tasks.

Show me the relevant workflow task sequences

![Disable tasks for creating notifications ](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ef757cb613.png)

For instructions on disabling a task, see [Disable or enable a task](/docs/analyze-explore-automate/workflows/building#disable-enable "Create and edit workflows in Dynatrace Workflows.").

2. Run the workflow or execute individual tasks for which you want to check the output. For instructions, see [Run and monitor workflows](/docs/analyze-explore-automate/workflows/running "Run and monitor workflows created in Dynatrace Workflows.").

## Smart security

Congratulations! Youâve now set up an automation that empowers your security team. With Dynatrace CSPM Notification Automation, critical events are streamlined, alert fatigue is minimized, and cloud security is enhanced. Efficiency unleashed!

## Further resources

The following is a tutorial by the internal customer of Dynatrace CSPM Notification Automation.

CSPM Notification Automation with Dynatrace

## Related topics

* [Alerting and notifications](/docs/analyze-explore-automate/alerting-and-notifications "Utilize anomaly detection, problem detection, and workflows for external notifications to ensure that critical problems never go unnoticed.")