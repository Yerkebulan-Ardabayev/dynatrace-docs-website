---
title: Dynatrace API - Tokens and authentication
source: https://www.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication
scraped: 2026-02-24T21:23:14.182670
---

# Dynatrace API - Tokens and authentication

# Dynatrace API - Tokens and authentication

* Reference
* Published Aug 23, 2018

To be authenticated to use the Dynatrace API, you need a valid [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") or a valid [personal access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes."). Access to the API is fine-grained, meaning that you also need the proper scopes assigned to the token. See the description of each request to find out which scopes are required to use it.

For details on OAuth clients, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Token format

Dynatrace uses a unique token format consisting of three components separated by dots (`.`).

### Token example

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Token components

### Token prefixes

## Generate a token

Access token

Personal access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

To generate a personal access token

1. Go to **Personal Access Tokens** (accessible via the [user menu](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace") in the previous Dynatrace).
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

You can assign multiple scopes to a single token, or you can generate several tokens, each with different access levels and use them accordinglyâcheck your organization's security policies for the best practice.

To change the scope of an existing token, use the [PUT a token call](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token "Update an access token via Dynatrace API.") of the Access tokens API. Note that you need to submit the existing scopes if you want to keep them. Any existing scope missing in the payload is removed.

Alternatively, you can use the [POST a token](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Create an access token via Dynatrace API.") call to generate a token.

## Token scopes

Access token

Personal access token

### OpenPipeline

### API v2

### API v1

### PaaS

### Other

Dynatrace provides the following permissions for personal access tokens. You can set them in the web UI as described above or via the [**Access tokens** API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

## Authenticate

You have two options to pass your API token: in the **Authorization** HTTP header or in the **api-token** query parameter.

We recommend that you use the **Authorization** header, as URLs (along with tokens passed within them) might be logged in various locations. Users might also bookmark the URLs or share them in plain text. Therefore, placing authentication tokens into the URL increases the risk that they will be captured by an attacker.

HTTP header

Query parameter

You can authenticate by attaching the token to the **Authorization** HTTP header preceding the **Api-Token** realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

The following example shows authentication via HTTP header.

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

You can authenticate by adding the token as the value of the **api-token** query parameter.

```
curl --request GET \



--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

## Related topics

* [Access tokens classic](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")