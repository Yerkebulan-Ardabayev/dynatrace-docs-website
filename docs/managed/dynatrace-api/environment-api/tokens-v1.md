---
title: Tokens API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1
---

# Tokens API v1

# Tokens API v1

* Reference
* Updated on May 17, 2022

This API is deprecated. Use the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.") instead.

The **Tokens** API enables you to manage the Dynatrace API authentication tokens of your environment.

### List all tokens

[Get an overview](/managed/dynatrace-api/environment-api/tokens-v1/get-all-tokens "Learn how to use the Dynatrace API to get a list of all Dynatrace API authentication tokens.") of all tokens available in your environment.

### View a token

Get metadata of a token, either by [its ID](/managed/dynatrace-api/environment-api/tokens-v1/get-token-metadata "Learn how use the Dynatrace API to get metadata for a Dynatrace API authentication token.") or by the [token itself](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.").

### Create a token

[Create a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Learn how to use the Dynatrace API to create a new Dynatrace API authentication token.") with a defined scope and validity period.

### Edit a token

[Update](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Learn how to use the Dynatrace API to update a Dynatrace API authentication token.") an existing token. You can revoke a token or change its scope.

### Delete a token

[Delete tokens](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Learn how to delete a Dynatrace API authentication token using the Dynatrace API.") your environment doesn't need anymore.

---

### Implement token rotation

[Set up](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation "Learn how to use the Dynatrace API to regularly rotate Dynatrace API authentication tokens in your environment.") regular renewal of tokens.

### Search and delete an exposed token

[Find and remove](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token "Learn how to find and replace an exposed Dynatrace API authentication token using the Dynatrace API.") a compromised token.