---
title: Settings API - Ownership teams schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ownership-teams
scraped: 2026-05-12T11:44:41.584561
---

# Settings API - Ownership teams schema table

# Settings API - Ownership teams schema table

* Published Dec 05, 2023

### Ownership teams (`builtin:ownership.teams)`

Set up teams and assign responsibilities to them. Link teams to monitored entities in Dynatrace by referencing the team identifier in entity metadata. [See documentationï»¿](https://dt-url.net/ownership)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ownership.teams` | * `group:ownership` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.teams` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ownership.teams` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.teams` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Team name `name` | text | - | Required |
| Description `description` | text | - | Optional |
| Team identifier `identifier` | text | The team identifier is used to reference the team from any entity in Dynatrace. If you are using Kubernetes labels, keep in mind the 63 character limit that they enforce. | Required |
| Supplementary identifiers `supplementaryIdentifiers` | Set<[SupplementaryIdentifier](#SupplementaryIdentifier)> | The supplementary team identifiers can be optionally used in addition to the main team identifier to reference this team from any entity in Dynatrace. Up to 3 supplementary identifiers are supported. | Required |
| Responsibilities `responsibilities` | [Responsibilities](#Responsibilities) | Turn on all responsibility assignments that apply to this team. | Required |
| Contact details `contactDetails` | [ContactDetails](#ContactDetails)[] | Define options for messaging integration or other means of contacting this team. | Required |
| Links `links` | [Link](#Link)[] | Include links to online resources where information relevant to this teamâs responsibilities can be found. | Required |
| Additional information `additionalInformation` | [AdditionalInformation](#AdditionalInformation)[] | Define key/value pairs that further describe this team â for example, cost center, solution type, or business unit assignments. | Required |
| External ID `externalId` | text | This field should only be used for the automation purpose when importing team information. | Optional |

##### The `SupplementaryIdentifier` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Supplementary Identifier `supplementaryIdentifier` | text | - | Required |

##### The `Responsibilities` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Development `development` | boolean | Responsible for developing and maintaining high quality software. Development teams are responsible for making code changes to address performance regressions, errors, or security vulnerabilities. | Required |
| Security `security` | boolean | Responsible for the security posture of the organization. Teams with security responsibility must understand the impact, priority, and team responsible for addressing security vulnerabilities. | Required |
| Operations `operations` | boolean | Responsible for deploying and managing software, with a focus on high availability and performance. Teams with operations responsibilities needs to understand the impact, priority, and team responsible for addressing problems detected by Dynatrace. | Required |
| Infrastructure `infrastructure` | boolean | Responsible for the administration, management, and support of the IT infrastructure including physical servers, virtualization, and cloud. Teams with infrastructure responsibility are responsible for addressing hardware issues, resource limits, and operating system vulnerabilities. | Required |
| Line of Business `lineOfBusiness` | boolean | Responsible for ensuring that applications in development align with business needs and meet the usability requirements of users, stakeholders, customers, and external partners. Teams with line of business responsibility are responsible for understanding the customer experience and how it affects business goals. | Required |

##### The `ContactDetails` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Integration type `integrationType` | enum | The element has these enums * `JIRA` * `EMAIL` * `MS_TEAMS` * `SLACK` | Required |
| Email `email` | text | - | Required |
| Team `msTeams` | text | - | Required |
| Jira `jira` | [JiraConnection](#JiraConnection) | - | Required |
| Channel `slackChannel` | text | - | Required |
| URL `url` | text | - | Optional |

##### The `Link` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Type `linkType` | enum | The element has these enums * `DOCUMENTATION` * `RUNBOOK` * `WIKI` * `DASHBOARD` * `HEALTH_APP` * `URL` * `REPOSITORY` | Required |
| URL `url` | text | - | Required |

##### The `AdditionalInformation` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `key` | text | - | Required |
| Value `value` | text | - | Required |
| URL `url` | text | - | Optional |

##### The `JiraConnection` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Project `project` | text | - | Required |
| Default Assignee `defaultAssignee` | text | - | Required |