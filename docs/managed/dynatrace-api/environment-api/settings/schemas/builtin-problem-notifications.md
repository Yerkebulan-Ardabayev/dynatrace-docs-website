---
title: Settings API - Problem notifications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-problem-notifications
---

# Settings API - Problem notifications schema table

# Settings API - Problem notifications schema table

* Published Dec 05, 2023

### Problem notifications (`builtin:problem.notifications)`

Integrate Dynatrace problem notifications with your organization's existing incident-management system or team-collaboration channel. Alerting profiles are used within problem integrations to filter the total number of alerts to a subset that is relevant for your team.

For details see [Third-party integrations﻿](https://dt-url.net/j803tgc).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:problem.notifications` | * `group:integration` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.notifications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:problem.notifications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.notifications` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Notification type `type` | enum | The element has these enums * `EMAIL` * `SLACK` * `JIRA` * `ANSIBLETOWER` * `OPS_GENIE` * `PAGER_DUTY` * `VICTOROPS` * `WEBHOOK` * `XMATTERS` * `TRELLO` * `SERVICE_NOW` | Required |
| Display name `displayName` | text | The name of the notification configuration. | Required |
| `emailNotification` | [EmailNotification](#EmailNotification) | - | Required |
| `slackNotification` | [SlackNotification](#SlackNotification) | - | Required |
| `jiraNotification` | [JiraNotification](#JiraNotification) | - | Required |
| `ansibleTowerNotification` | [AnsibleTowerNotification](#AnsibleTowerNotification) | - | Required |
| `opsGenieNotification` | [OpsGenieNotification](#OpsGenieNotification) | - | Required |
| `pagerDutyNotification` | [PagerDutyNotification](#PagerDutyNotification) | - | Required |
| `victorOpsNotification` | [VictorOpsNotification](#VictorOpsNotification) | - | Required |
| `webHookNotification` | [WebHookNotification](#WebHookNotification) | - | Required |
| `xMattersNotification` | [XMattersNotification](#XMattersNotification) | - | Required |
| `trelloNotification` | [TrelloNotification](#TrelloNotification) | - | Required |
| `serviceNowNotification` | [ServiceNowNotification](#ServiceNowNotification) | - | Required |
| Alerting profile `alertingProfile` | setting | Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:alerting.profile`) to control the delivery of problem notifications related to this integration. | Required |

##### The `EmailNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| To `recipients` | set | - | Required |
| CC `ccRecipients` | set | - | Required |
| BCC `bccRecipients` | set | - | Required |
| Subject `subject` | text | The subject of the email notifications. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |
| Send email if problem is closed `notifyClosedProblems` | boolean | - | Required |
| Body `body` | text | The template of the email notifications. Type '{' for placeholder suggestions.  **{ImpactedEntities}**: Details about the entities impacted by the problem in form of a json array.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsHTML}**: All problem event details including root cause as an HTML-formatted string.  **{ProblemDetailsJSONv2}**: Problem as json object following the structure from the [Dynatrace Problems V2 API﻿](https://dt-url.net/7a03ti2). The optional fields evidenceDetails and impactAnalysis are included, but recentComments is not.  **{ProblemDetailsJSON}**: Problem as json object following the structure from the [Dynatrace Problems V1 API﻿](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: All problem event details including root cause as a Markdown-formatted string.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `SlackNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| URL `url` | secret | Set up an incoming WebHook integration within your Slack account. Copy and paste the generated WebHook URL into the field above. | Required |
| Channel `channel` | text | The channel (for example, `#general`) or the user (for example, `@john.smith`) to send the message to. | Required |
| Message `message` | text | The content of the message. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `JiraNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Jira endpoint URL `url` | text | The URL of the Jira API endpoint. | Required |
| Username `username` | text | The username of the Jira profile. | Required |
| API token `apiToken` | secret | The API token for the Jira profile. Using password authentication [was deprecated by Jira﻿](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/) | Required |
| Project key `projectKey` | text | The project key of the Jira issue to be created by this notification. | Required |
| Issue type `issueType` | text | The type of the Jira issue to be created by this notification.  To find all available issue types, or to create your own issue type, within JIRA go to Options > Issues. | Required |
| Summary `summary` | text | The summary of the Jira issue to be created by this notification. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |
| Issue description `description` | text | The description of the Jira issue to be created by this notification. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `AnsibleTowerNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Job template URL `jobTemplateURL` | text | The URL of the target job template.  **Note:** Be sure to select the **Prompt on Launch** option in the Extra Variables section of your job template configuration. | Required |
| Accept any SSL certificate (including self-signed and invalid certificates) `acceptAnyCertificate` | boolean | - | Required |
| Username `username` | text | Account username. | Required |
| Password `password` | secret | Account password. | Required |
| Custom message (optional) `customMessage` | text | This message will be displayed in the Extra Variables **Message** field of your job template. Type '{' for placeholder suggestions.  **{ImpactedEntities}**: Details about the entities impacted by the problem in form of a json array.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `OpsGenieNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| OpsGenie API key `apiKey` | secret | The API key to access OpsGenie.  Go to OpsGenie-Integrations and create a new Dynatrace integration. Copy the newly created API key. | Required |
| OpsGenie region domain `domain` | text | The region domain of the OpsGenie.  For example, **api.opsgenie.com** for US or **api.eu.opsgenie.com** for EU. | Required |
| Message `message` | text | The content of the message. Type '{' for placeholder suggestions.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ImpactedEntityNames}**: The entity impacted by the problem (or multiple impacted entities). | Required |

##### The `PagerDutyNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Account `account` | text | The name of the PagerDuty account. | Required |
| Service name `serviceName` | text | The name of the service. | Required |
| Service key `serviceApiKey` | secret | The Events API key to access PagerDuty. | Required |

##### The `VictorOpsNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| API key `apiKey` | secret | The API key for the target Splunk On-Call account.  Receive your Splunk On-Call API key by navigating to: Settings -> Integrations -> Rest Endpoint -> Dynatrace. | Required |
| Routing key `routingKey` | text | The routing key, defining the group to be notified. | Required |
| Message `message` | text | The content of the message. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED. | Required |

##### The `WebHookNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Secret webhook URL `urlContainsSecret` | boolean | - | Optional |
| Webhook URL `url` | text | The URL of the webhook endpoint. | Required |
| Webhook URL `secretUrl` | secret | The secret URL of the webhook endpoint. | Required |
| Accept any SSL certificate (including self-signed and invalid certificates) `acceptAnyCertificate` | boolean | - | Required |
| Call webhook if new events merge into existing problems `notifyEventMergesEnabled` | boolean | - | Required |
| Call webhook if problem is closed `notifyClosedProblems` | boolean | - | Required |
| Use OAuth 2.0 for authentication `useOAuth2` | boolean | - | Optional |
| OAuth 2.0 credentials `oAuth2Credentials` | [OAuth2Credentials](#OAuth2Credentials) | To authenticate your integration, the OAuth 2.0 *Client Credentials* Flow (Grant Type) is used. For details see [Client Credentials Flow﻿](https://dt-url.net/ym22wsm)).  The obtained Access Token is subsequently provided in the *Authorization* header of the request carrying the notification payload. | Required |
| Timeout in Seconds `timeoutInSeconds` | integer | - | Optional |
| Additional HTTP headers `headers` | Set<[WebHookNotificationHeader](#WebHookNotificationHeader)> | A list of the additional HTTP headers. | Required |
| Custom payload `payload` | text | The content of the notification message. Type '{' for placeholder suggestions.  **{ImpactedEntities}**: Details about the entities impacted by the problem in form of a json array.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsHTML}**: All problem event details including root cause as an HTML-formatted string.  **{ProblemDetailsJSONv2}**: Problem as json object following the structure from the [Dynatrace Problems V2 API﻿](https://dt-url.net/7a03ti2). The optional fields evidenceDetails and impactAnalysis are included, but recentComments is not.  **{ProblemDetailsJSON}**: Problem as json object following the structure from the [Dynatrace Problems V1 API﻿](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: All problem event details including root cause as a Markdown-formatted string.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `XMattersNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| xMatters URL `url` | text | The URL of the xMatters webhook. | Required |
| Accept any SSL certificate (including self-signed and invalid certificates) `acceptAnyCertificate` | boolean | - | Required |
| Additional HTTP headers `headers` | Set<[WebHookNotificationHeader](#WebHookNotificationHeader)> | A list of the additional HTTP headers. | Required |
| Custom payload `payload` | text | The content of the notification message. Type '{' for placeholder suggestions.  **{ImpactedEntities}**: Details about the entities impacted by the problem in form of a json array.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsHTML}**: All problem event details including root cause as an HTML-formatted string.  **{ProblemDetailsJSONv2}**: Problem as json object following the structure from the [Dynatrace Problems V2 API﻿](https://dt-url.net/7a03ti2). The optional fields evidenceDetails and impactAnalysis are included, but recentComments is not.  **{ProblemDetailsJSON}**: Problem as json object following the structure from the [Dynatrace Problems V1 API﻿](https://dt-url.net/qn23tk2).  **{ProblemDetailsMarkdown}**: All problem event details including root cause as a Markdown-formatted string.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `TrelloNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Trello application key `applicationKey` | text | The application key for the Trello account.  You must be logged into Trello to have Trello automatically generate an application key for you. [Get application key﻿](https://trello.com/app-key) | Required |
| Trello authorization token `authorizationToken` | secret | The authorization token for the Trello account. | Required |
| Trello board ID problem cards should be assigned to `boardId` | text | - | Required |
| Trello list ID new problem cards should be assigned to `listId` | text | - | Required |
| Trello list ID resolved problem cards should be assigned to `resolvedListId` | text | - | Required |
| Card text `text` | text | The card text and problem placeholders to appear on new problem cards. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |
| Card description `description` | text | The description of the Trello card. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsMarkdown}**: All problem event details including root cause as a Markdown-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{ProblemURL}**: URL of the problem within Dynatrace.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |

##### The `ServiceNowNotification` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| ServiceNow instance identifier `instanceName` | text | The ServiceNow instance identifier. It refers to the first part of your own ServiceNow URL.  This field is mutually exclusive with the **url** field. You can only use one of them. | Required |
| OnPremise URL `url` | text | The URL of the on-premise ServiceNow installation.  This field is mutually exclusive with the **instanceName** field. You can only use one of them. | Optional |
| Username `username` | text | The username of the ServiceNow account.  Make sure that your user account has the `web_service_admin` and `x_dynat_ruxit.Integration` roles. | Required |
| Password `password` | secret | The password to the ServiceNow account. | Required |
| Description `message` | text | The content of the ServiceNow description. Type '{' for placeholder suggestions.  **{ImpactedEntity}**: A short description of the problem and impacted entity (or multiple impacted entities).  **{ImpactedEntityNames}**: The entity impacted by the problem.  **{NamesOfImpactedEntities}**: The names of all entities that are impacted by the problem.  **{PID}**: Unique system identifier of the reported problem.  **{ProblemDetailsHTML}**: All problem event details including root cause as an HTML-formatted string.  **{ProblemDetailsText}**: All problem event details including root cause as a text-formatted string.  **{ProblemID}**: Display number of the reported problem.  **{ProblemImpact}**: Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE.  **{ProblemSeverity}**: Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE\_CONTENTION, or CUSTOM\_ALERT.  **{ProblemTitle}**: Short description of the problem.  **{State}**: Problem state. Possible values are OPEN or RESOLVED.  **{Tags}**: Comma separated list of tags that are defined for all impacted entities. To refer to the value of a specific tag, specify the tag's key in square brackets: **{Tags[key]}**. If the tag does not have any assigned value, the placeholder will be replaced by an empty string. The placeholder will not be replaced if the tag key does not exist. | Required |
| Send incidents into ServiceNow ITSM. `sendIncidents` | boolean | - | Required |
| Send events into ServiceNow ITOM. `sendEvents` | boolean | - | Required |
| Use text format for problem details instead of HTML. `formatProblemDetailsAsText` | boolean | - | Optional |
| Timeout in Seconds `timeoutInSeconds` | integer | - | Optional |

##### The `OAuth2Credentials` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Access token URL `accessTokenUrl` | text | - | Required |
| Client ID `clientId` | text | - | Required |
| Client secret `clientSecret` | secret | - | Required |
| Scope `scope` | text | The scope of access you are requesting | Optional |
| Include the client credentials in the HTTP "Authorization" request header field with the HTTP "Basic" authentication scheme. `authenticateViaRequestHeader` | boolean | If false, the client credentials are included in the HTTP request body. | Optional |

##### The `WebHookNotificationHeader` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | The name of the HTTP header. | Required |
| Secret HTTP header value `secret` | boolean | - | Required |
| Value `value` | text | The value of the HTTP header. May contain an empty value. | Required |
| Value `secretValue` | secret | The secret value of the HTTP header. May contain an empty value. | Required |