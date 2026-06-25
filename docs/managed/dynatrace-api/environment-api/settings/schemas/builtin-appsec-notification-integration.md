---
title: Settings API - Security notifications schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-appsec-notification-integration
scraped: 2026-05-12T11:43:50.526365
---

# Settings API - Security notifications schema table

# Settings API - Security notifications schema table

* Published Dec 05, 2023

### Security notifications (`builtin:appsec.notification-integration)`

Integrate security notifications with your existing incident-management system or team-collaboration channel. Within security integrations, use vulnerability and attack alerting profiles to filter the total number of alerts down to those relevant for your team.

To learn more, visit [Security notificationsï»¿](https://dt-url.net/ly039s4).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:appsec.notification-integration` | * `group:integration` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-integration` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:appsec.notification-integration` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:appsec.notification-integration` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Security alert type `trigger` | enum | The element has these enums * `SECURITY_PROBLEM` * `ATTACK_CANDIDATE` | Required |
| Notification type `type` | enum | The element has these enums * `WEBHOOK` * `JIRA` * `EMAIL` | Required |
| Display name `displayName` | text | - | Required |
| `webhookConfiguration` | [WebhookConfiguration](#WebhookConfiguration) | - | Required |
| `securityProblemBasedWebhookPayload` | [SecurityProblemBasedWebhookPayload](#SecurityProblemBasedWebhookPayload) | - | Required |
| `attackCandidateBasedWebhookPayload` | [AttackCandidateBasedWebhookPayload](#AttackCandidateBasedWebhookPayload) | - | Required |
| `jiraConfiguration` | [JiraConfiguration](#JiraConfiguration) | - | Required |
| `securityProblemBasedJiraPayload` | [SecurityProblemBasedJiraPayload](#SecurityProblemBasedJiraPayload) | - | Required |
| `attackCandidateBasedJiraPayload` | [AttackCandidateBasedJiraPayload](#AttackCandidateBasedJiraPayload) | - | Required |
| `emailConfiguration` | [EmailConfiguration](#EmailConfiguration) | - | Required |
| `securityProblemBasedEmailPayload` | [SecurityProblemBasedEmailPayload](#SecurityProblemBasedEmailPayload) | - | Required |
| `attackCandidateBasedEmailPayload` | [AttackCandidateBasedEmailPayload](#AttackCandidateBasedEmailPayload) | - | Required |
| Alerting profile `securityProblemBasedAlertingProfile` | setting | Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-alerting-profile`) to control the delivery of security notifications related to this integration. | Required |
| Alerting profile `attackCandidateBasedAlertingProfile` | setting | Select an alerting profile (`<your-dynatrace-url>//ui/settings/builtin:appsec.notification-attack-alerting-profile`) to control the delivery of security notifications related to this integration. | Required |

##### The `WebhookConfiguration` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Webhook endpoint URL `url` | text | - | Required |
| Accept any SSL certificate (including self-signed and invalid certificates) `acceptAnyCertificate` | boolean | - | Required |
| Additional HTTP headers `headers` | Set<[WebhookConfigurationHeader](#WebhookConfigurationHeader)> | Use additional HTTP headers to attach any additional information, for example, configuration, authorization, or metadata.  Note that JSON-based webhook endpoints require the addition of the **Content-Type: application/json** header to enable escaping of special characters and to avoid malformed JSON content. | Required |

##### The `SecurityProblemBasedWebhookPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Custom payload `payload` | text | This is the content your notification message will include when users view it.  In case a value of a security problem is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the custom payload might leak information to untrusted parties.  Available placeholders:  **{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".  **{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".  **{Description}**: A more detailed description of the vulnerability.  **{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty. **{DavisSecurityScore}**: [Davis Security Scoreï»¿](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".  **{Severity}**: The security problem severity, for example, "Critical" or "Medium".  **{SecurityProblemUrl}**: URL of the security problem in Dynatrace.  **{AffectedEntities}**: Details about the entities affected by the security problem in a json array.  **{ManagementZones}**: Comma-separated list of all management zones affected by the vulnerability at the time of detection.  **{Tags}**: Comma-separated list of tags that are defined for a vulnerability's affected entities. For example: "PROD, owner:John". Assign the tag's key in square brackets: **{Tags[key]}** to get all associated values. For example: "{Tags[owner]}" will be resolved as "John". Tags without an assigned value will be resolved as empty string.  **{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".  **{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".  **{ExploitAvailable}**: Describes whether there's an exploit available for the vulnerability. Can be "true" or "false". | Required |

##### The `AttackCandidateBasedWebhookPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Custom payload `payload` | text | This is the content your notification message will include when users view it.  In case a value of an attack is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the custom payload might leak information to untrusted parties.  Available placeholders:  **{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example: "A-1234".  **{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"  **{Type}**: The type of attack, for example: "SQL Injection".  **{AttackUrl}**: URL of the attack in Dynatrace.  **{ProcessGroupId}**: Details about the process group attacked.  **{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.  **{Status}**: The status of the attack, for example: "Exploited"  **{Timestamp}**: When the attack happened.  **{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty. | Required |

##### The `JiraConfiguration` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Jira endpoint URL `url` | text | The URL of the Jira API endpoint. | Required |
| Username `username` | text | The username of the Jira profile. | Required |
| API token `apiToken` | secret | The API token for the Jira profile. Using password authentication [was deprecated by Jiraï»¿](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-basic-auth-and-cookie-based-auth/) | Required |
| Project key `projectKey` | text | The project key of the Jira issue to be created by this notification. | Required |
| Issue type `issueType` | text | The type of the Jira issue to be created by this notification.  To find all available issue types or create your own, in Jira, go to Project settings > Issue types. | Required |

##### The `SecurityProblemBasedJiraPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Summary `summary` | text | The summary of the Jira issue to be created by this notification.  **Note:** The Jira summary field must contain less than 255 characters. Any content exceeding this limit after evaluating the placeholders will be discarded.  Available placeholders:  **{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".  **{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".  **{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty. **{DavisSecurityScore}**: [Davis Security Scoreï»¿](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".  **{Severity}**: The security problem severity, for example, "Critical" or "Medium".  **{SecurityProblemUrl}**: URL of the security problem in Dynatrace.  **{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".  **{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".  **{ExploitAvailable}**: Describes whether there's an exploit available for the vulnerability. Can be "true" or "false". | Required |
| Issue description `description` | text | The description of the Jira issue to be created by this notification.  In case a value of a security problem is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the description might leak information to untrusted parties.  Available placeholders:  **{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".  **{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".  **{Description}**: A more detailed description of the vulnerability.  **{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty. **{DavisSecurityScore}**: [Davis Security Scoreï»¿](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".  **{Severity}**: The security problem severity, for example, "Critical" or "Medium".  **{SecurityProblemUrl}**: URL of the security problem in Dynatrace.  **{AffectedEntities}**: Details about the entities affected by the security problem in a json array.  **{ManagementZones}**: Comma-separated list of all management zones affected by the vulnerability at the time of detection.  **{Tags}**: Comma-separated list of tags that are defined for a vulnerability's affected entities. For example: "PROD, owner:John". Assign the tag's key in square brackets: **{Tags[key]}** to get all associated values. For example: "{Tags[owner]}" will be resolved as "John". Tags without an assigned value will be resolved as empty string.  **{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".  **{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".  **{ExploitAvailable}**: Describes whether there's an exploit available for the vulnerability. Can be "true" or "false". | Required |

##### The `AttackCandidateBasedJiraPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Summary `summary` | text | The summary of the Jira issue to be created by this notification.  **Note:** The Jira summary field must contain less than 255 characters. Any content exceeding this limit after evaluating the placeholders will be discarded.  Available placeholders:  **{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example, "A-1234".  **{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"  **{Type}**: The type of attack, for example: "SQL Injection".  **{AttackUrl}**: URL of the attack in Dynatrace.  **{ProcessGroupId}**: Details about the process group attacked.  **{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.  **{Status}**: The status of the attack, for example: "Exploited"  **{Timestamp}**: When the attack happened.  **{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty. | Required |
| Issue description `description` | text | The description of the Jira issue to be created by this notification.  In case a value of an attack is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the description might leak information to untrusted parties.  Available placeholders:  **{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example: "A-1234".  **{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"  **{Type}**: The type of attack, for example: "SQL Injection".  **{AttackUrl}**: URL of the attack in Dynatrace.  **{ProcessGroupId}**: Details about the process group attacked.  **{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.  **{Status}**: The status of the attack, for example: "Exploited"  **{Timestamp}**: When the attack happened.  **{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty. | Required |

##### The `EmailConfiguration` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| To `recipients` | set | - | Required |
| CC `ccRecipients` | set | - | Required |
| BCC `bccRecipients` | set | - | Required |

##### The `SecurityProblemBasedEmailPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Subject `subject` | text | The subject of the email notifications.  Available placeholders:  **{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".  **{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".  **{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty. **{DavisSecurityScore}**: [Davis Security Scoreï»¿](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".  **{Severity}**: The security problem severity, for example, "Critical" or "Medium".  **{SecurityProblemUrl}**: URL of the security problem in Dynatrace.  **{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".  **{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".  **{ExploitAvailable}**: Describes whether there's an exploit available for the vulnerability. Can be "true" or "false". | Required |
| Body `body` | text | The template of the email notifications.  In case a value of a security problem is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the description might leak information to untrusted parties.  Available placeholders:  **{SecurityProblemId}**: The unique identifier assigned by Dynatrace, for example, "S-1234".  **{Title}**: A short summary of the type of vulnerability that was found, for example, "Remote Code Execution".  **{Description}**: A more detailed description of the vulnerability.  **{CvssScore}**: CVSS score of the identified vulnerability, for example, "10.0". Can be empty. **{DavisSecurityScore}**: [Davis Security Scoreï»¿](https://www.dynatrace.com/support/help/how-to-use-dynatrace/application-security/davis-security-score/) is an enhanced risk-calculation score based on the CVSS, for example, "10.0".  **{Severity}**: The security problem severity, for example, "Critical" or "Medium".  **{SecurityProblemUrl}**: URL of the security problem in Dynatrace.  **{AffectedEntities}**: Details about the entities affected by the security problem in a json array.  **{ManagementZones}**: Comma-separated list of all management zones affected by the vulnerability at the time of detection.  **{Tags}**: Comma-separated list of tags that are defined for a vulnerability's affected entities. For example: "PROD, owner:John". Assign the tag's key in square brackets: **{Tags[key]}** to get all associated values. For example: "{Tags[owner]}" will be resolved as "John". Tags without an assigned value will be resolved as empty string.  **{Exposed}**: Describes whether one or more affected process is exposed to the public Internet. Can be "true" or "false".  **{DataAssetsReachable}**: Describes whether one or more affected process can reach data assets. Can be "true" or "false".  **{ExploitAvailable}**: Describes whether there's an exploit available for the vulnerability. Can be "true" or "false". | Required |

##### The `AttackCandidateBasedEmailPayload` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Subject `subject` | text | The subject of the email notifications.  Available placeholders:  **{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example, "A-1234".  **{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"  **{Type}**: The type of attack, for example: "SQL Injection".  **{AttackUrl}**: URL of the attack in Dynatrace.  **{ProcessGroupId}**: Details about the process group attacked.  **{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.  **{Status}**: The status of the attack, for example: "Exploited"  **{Timestamp}**: When the attack happened.  **{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty. | Required |
| Body `body` | text | The template of the email notifications.  In case a value of a security problem is not set, the placeholder will be replaced by an empty string.  **Note:** Security notifications contain sensitive information. Excessive usage of placeholders in the body might leak information to untrusted parties.  Available placeholders:  **{AttackDisplayId}**: The unique identifier assigned by Dynatrace, for example: "A-1234".  **{Title}**: Location of the attack, for example: "com.dynatrace.Class.method():120"  **{Type}**: The type of attack, for example: "SQL Injection".  **{AttackUrl}**: URL of the attack in Dynatrace.  **{ProcessGroupId}**: Details about the process group attacked.  **{EntryPoint}**: The entry point of the attack into the process, for example: "/login". Can be empty.  **{Status}**: The status of the attack, for example: "Exploited"  **{Timestamp}**: When the attack happened.  **{VulnerabilityName}**: Name of the associated code-level vulnerability, for example: "InMemoryDatabaseCaller.getAccountInfo():51". Can be empty. | Required |

##### The `WebhookConfigurationHeader` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Secret HTTP header value `secret` | boolean | - | Required |
| Value `value` | text | The value of the HTTP header. May contain an empty value. | Required |
| Value `secretValue` | secret | The secret value of the HTTP header. May contain an empty value. | Required |