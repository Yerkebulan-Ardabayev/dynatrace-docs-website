---
title: Cluster API - Tokens and authentication
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-authentication
---

# Cluster API - Tokens and authentication

# Cluster API - Tokens and authentication

* Published Feb 28, 2020

Dynatrace Managed uses two types of API tokens:

* The environment token management token that is used to manage environment tokens based on the environment ID provided in the API call.
* The Cluster API token that is used to manage the cluster, even if that cluster contains more than one environment. This is the token most commonly used in Dynatrace Managed.

## Environment token management

The environment token management token is the token for authentication when using the [Create new Cluster token](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens "Learn how to create new Dynatrace Cluster token using API.") endpoint. It allows you to create a token with the `TokenManagement` scope for a specified environment. This token is helpful in automating token generation for many environments.

Short life

Because of its potential security impact on the cluster and all environments within the cluster, this token is valid for only 24 hours.

### Generate environment token management token

To generate a token for environment token management

1. Go to **Settings** > **API tokens**.
2. In the **Environment token management tokens** section, select **Generate token**.
3. Enter a name for your token.
4. Select **Save**.
5. Select **Copy** to copy the token and paste it to a secure location.

## Cluster configuration token

A cluster configuration token is a token that you use to interact with [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "Find out about API for managing environments, network zones, synthetic locations, nodes, and tokens.") or [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") endpoints. The following scopes are available:

* Cluster token management
* Service Provider API
* Read settings
* Write settings

To get authenticated to use the Cluster API, you need a valid API token. Access to the API is controlled by scope, meaning that you also need the proper permissions assigned to the token. See the description of each request to find out which permissions are required to use it.

### Generate a token for cluster configuration

To generate cluster API token

1. Go to **Settings** > **API tokens**.
2. In the **Cluster tokens** section, select **Generate token**.
3. Enter a name for your token.
4. Dynatrace provides the following permissions for API tokens. You can set them in the UI, as described above, or via Tokens API. You can assign multiple permissions to a single token, or you can generate several tokens, each with different access levels and use them accordingly—check with your organization's security policies for the best practice. We recommend to keep tokens with a dedicated single scope to limit potential damage in case of leakage.

   | Name | API value | Description |
   | --- | --- | --- |
   | Cluster token management | `ClusterTokenManagement` | Allows to access Tokens API and manage tokens. |
   | Service Provider API | `ServiceProviderAPI` | Allows access to Cluster Management API operations. |
   | Read settings | `settings.read` | Grants permission to read cluster settings (API v2). |
   | Write settings | `settings.write` | Grants permission to write cluster settings (API v2). |
5. Select **Save**.
6. Select **Copy** to copy the token and paste it to a secure location.

## Authenticate

Your API call can be authenticated in two ways: per call via an HTTP header or query parameter, or per login via the Cluster API screen.

### HTTP header

You can authenticate by attaching the token to the **Authorization** HTTP header preceding the **Api-Token** realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

The following example shows authentication via HTTP header.

```
curl --request GET \



--url https://myManaged.cluster.com/api/cluster/v1/tokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

### Query parameter

You can authenticate by adding the token as the value of the **api-token** query parameter.

```
curl --request GET \



--url 'https://myManaged.cluster.com/api/cluster/v1/tokens?limit=1000&user=Pete&permissions=ClusterTokenManagement&api-token=abcdefjhij1234567890' \
```

### Cluster API screen

1. In the upper-right corner, open the user menu and select **Cluster Management API**.
2. From the dropdown menu box in the top bar, select API definition: **Cluster Management API** or **Cluster API**.
3. In the API explorer, select **Authorize**.  
   **Available authorizations** is displayed.
4. Paste your token into the **Value** box and select **Authorize**.  
   Once completed, from the same dialog box you can select **Logout** to discontinue the authentication.