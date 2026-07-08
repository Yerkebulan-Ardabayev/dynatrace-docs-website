---
title: Settings API - Git On-Premise Servers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-devobs-debugger-git-on-prem
---

# Settings API - Git On-Premise Servers schema table

# Settings API - Git On-Premise Servers schema table

* Published Mar 17, 2025

### Git On-Premise Servers (`app:dynatrace.devobs.debugger:git.on.prem)`

Specify your On-Premise Git servers to be able to fetch source code from them

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.devobs.debugger:git.on.prem` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.devobs.debugger:git.on.prem` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Git Provider `Provider` | enum | The git service provider for this server The element has these enums * `GithubOnPrem` * `GitlabOnPrem` * `BitbucketOnPrem` * `AzureOnPrem` | Required |
| Server URL `Url` | text | An HTTPS URL of your server (HTTP not supported) Provide only the base URL of the server, not a path to a specific project or repository (For instance, https://git.example.com) | Required |
| Include Credentials `IncludeCredentials` | boolean | If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`. | Required |