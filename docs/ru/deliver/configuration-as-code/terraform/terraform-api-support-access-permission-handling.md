---
title: Terraform API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling
scraped: 2026-02-27T21:29:37.206809
---

# Terraform API support and access permission handling

# Terraform API support and access permission handling

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Nov 20, 2025

Dynatrace offers different options to authenticate API calls. The Dynatrace Terraform Provider supports the following authentication options.

* Platform tokens
* OAuth clients
* Access tokens (classic)

For more information about Identity and Access Management (IAM), including platform tokens, OAuth clients, and API tokens / access tokens classic, see [Tokens and OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Create platform tokens

[Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") can be used to authenticate API calls against Dynatrace.
These platform tokens are long-lived access tokens.
For the full list of supported platform token services, see [Available services for platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#available-services "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

The following code blocks show you how to define environment variables for your environment URL and platform token for Windows and Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

## Create OAuth client

To create an OAuth client, follow the steps described in [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-oauth-client "Manage authentication and user permissions using OAuth clients.").

To ensure the OAuth client works as intended, verify that the service user's groups grant the same scopes as the OAuth client you have created for all environments you want to use it with.
For more details on controlling permissions, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

The Dynatrace Terraform Provider requests OAuth access tokens using your client credentials to make authenticated API calls.

The following code blocks show you how to define environment variables for your environment URL, authentication client, and secret for Windows and Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



set DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



export DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

## Create API access token

Use access tokens to authenticate Dynatrace Classic API calls.
For more information on how to use a Dynatrace API token, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

The following code blocks show you how to define environment variables for your environment URL and API token for Windows and Linux.

Windows SaaS Classic Dynatrace

Linux SaaS Classic Dynatrace

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

## API coverage

The Dynatrace Terraform Provider contains most Dynatrace APIs. All supported resources are listed in the Dynatrace Terraform Provider documentation in the [Terraform Registryï»¿](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs).

Always consider the correct permission scopes that are needed for the selected API resources.
Information can be found at [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") and [the Dynatrace Terraform provider GitHub repositoryï»¿](https://github.com/dynatrace-oss/terraform-provider-dynatrace/blob/main/documentation/supported-resources.md).