---
title: Monaco API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling
scraped: 2026-02-25T21:30:21.743290
---

# Monaco API support and access permission handling

# Monaco API support and access permission handling

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 27, 2025

Dynatrace offers different options to authenticate API calls. Dynatrace Monaco supports the following authentication options:

* Platform tokens
* OAuth clients

For details about Dynatrace Identity and Access Management (including platform tokens,API tokens, and OAuth clients), see [Tokens and OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Create a platform token for the Dynatrace Monaco CLI

To create a platform token, follow the steps described in [Create a platform token for the Dynatrace Monaco CLI](/docs/deliver/configuration-as-code/monaco/guides/create-platform-token "Create a platform token for Dynatrace Configuration as Code via Monaco.").
Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Create an OAuth client for the Dynatrace Monaco CLI

To create an OAuth client, follow the steps described in [Create an OAuth2 client](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-an-oauth2-client "Manage authentication and user permissions using OAuth clients.").

Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To use the `automation:workflows:admin` scope, you need to do the following before creating the OAuth client.

1. Create a custom policy granting that scope.
2. Bind a group to it.
3. Assign your user to that group.

For detailed information on managing policies, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To manage OpenPipeline configurations, ensure that the user belongs to a group with the policy **Data Processing and Storage** assigned to it.
Do this before creating the OAuth client.

In addition to the scopes available to the OAuth client, permissions can be further limited via policies applied to the user's groups.

When working with a service user, ensure the service user's permissions match the OAuth scopes for all environments.
For details on how permissions can be controlled, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

To use your OAuth client:

1. Follow the instructions for your operating system or CI/CD tool on how to make the client ID and secret available as environment variables.
2. Reference the environment variables you have created in the OAuth section of your manifest file
3. Dynatrace Monaco CLI will request OAuth access tokens using your client credentials to make authenticated API calls.

## API coverage

Dynatrace Monaco supports the following configuration types:

* Settings 2.0
* Configuration APIs
* Platform APIs

The specific configuration types are defined in the Monaco configuration YAML file.

### Settings 2.0

Settings 2.0 resources require a classic Dynatrace API access token or OAuth credentials.

The Dynatrace Monaco CLI provides general support for any Settings 2.0 schema available in your environment.
For information about schemas, see [Settings 2.0 - Available schemas](/docs/dynatrace-api/environment-api/settings/schemas "View the entire settings schemas table of your monitoring environment via the Dynatrace API.").

For latest Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings:objects:read`, `settings:objects:write` |
| View Settings 2.0 schemas | `settings:schemas:read` |

For classic Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings.read`, `settings.write` |

### Supported platform API types

The Dynatrace platform provides a collection of [platform servicesï»¿](https://developer.dynatrace.com/plan/platform-services/), each with a specific area of responsibility.
OAuth credentials are required to target platform APIs.

The Dynatrace Monaco CLI provides support for Dynatrace platform API types as described in the table below.

### Account Management permissions

To manage account resources, such as user management or policy handling, OAuth credentials require the following permissions:

* `account-idm-read`
* `account-idm-write`
* `account-env-read`
* `account-env-write`
* `iam-policies-management`
* `iam:policies:write`
* `iam:policies:read`
* `iam:bindings:write`
* `iam:bindings:read`
* `iam:boundaries:read`
* `iam:boundaries:write`

### Supported Configuration API types

Configuration via the [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.") requires an API access token.
Dynatrace Monaco CLI provides support for most Configuration APIs, as described in the table below.
This table provides:

* The supported configuration types.
* Their API endpoints.
* The access token permissions that are required to interact with any endpoint.

Note that most Configuration APIs are deprecated in favor of Settings 2.0, see [Settings 2.0](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

## Related topics

* [Monaco configuration YAML file - list of special configuration types](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas "This is a list of Monaco special configuration types.")