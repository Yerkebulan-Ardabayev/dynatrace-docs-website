---
title: Access tokens classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
scraped: 2026-02-27T21:31:10.631421
---

# Access tokens classic

# Access tokens classic

* Reference
* 2-min read
* Updated on Oct 25, 2023

This article discusses access tokens used in previous Dynatrace to authenticate to classic Configuration and Environment APIs. For the latest Dynatrace access, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") and [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

All external access to your Dynatrace monitoring environment relies on two pieces of information: the [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") and an *access token*.

Dynatrace uses several types of tokens:

* Access tokens and personal access tokens grant access to:

  + [Dynatrace API](/docs/dynatrace-api "Find out what you need to use the Dynatrace API.")
  + Download of OneAgent and ActiveGate installers
* [Personal access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.") grant access to some endpoints of Dynatrace API
* [Tenant tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") allow OneAgent to report data to Dynatrace

## Token format

Dynatrace uses a unique token format consisting of three components separated by dots (`.`).

### Token example

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Token components

### Token prefixes

This predictable format offers you several capabilities:

* Use Git pre-commit hooks to avoid pushing tokens to source code repositories (for example, using tools like [git-secretsï»¿](https://github.com/awslabs/git-secrets))
* Define masking rules to obfuscate the secret portions of tokens when writing log files
* Detect tokens in internal files or communications
* Enable the [GitHub secret scanning serviceï»¿](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) to identify any token pushed to a public GitHub repository

Use this regular expression to look for tokens:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

With the rollout of Dynatrace version 1.210, this format is enabled by default (all newly generated tokens will use the new format).

All existing tokens of the old format remain valid.

### Disable the new format

For a limited time, you can opt out of using the new token format:

1. Go to **Settings > Integration > Token settings**.
2. Turn off **Create Dynatrace API tokens in the new format**.

## Generate an access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

## Token scopes

Access tokens have fine-grained scopes to limit access to specific product functionality for security reasons.

### OpenPipeline

### API v2

### API v1

### PaaS

### Other

## Related topics

* [Tokens API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")