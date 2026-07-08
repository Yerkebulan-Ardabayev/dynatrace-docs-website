---
title: Implement token rotation
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/token-rotation
---

# Implement token rotation

# Implement token rotation

* Reference
* Updated on May 17, 2022

Regularly changing your password is a good security practice. Same goes for Dynatrace API authentication tokens.

With the Tokens API, you can automate the rotation.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get the ID of an old token**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#get-old "Learn how to use the Dynatrace API to regularly rotate Dynatrace API authentication tokens in your environment.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create a new token**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#create-new "Learn how to use the Dynatrace API to regularly rotate Dynatrace API authentication tokens in your environment.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Revoke the old token**  
Don't delete it before you revoke it.](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#revoke-old "Learn how to use the Dynatrace API to regularly rotate Dynatrace API authentication tokens in your environment.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Delete the old token**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#delete-old "Learn how to use the Dynatrace API to regularly rotate Dynatrace API authentication tokens in your environment.")

For a workflow example, let's assume you want to rotate a token with following parameters:

* The name of the token is **RW config token**.
* The scope of the token includes **ReadConfig** and **WriteConfig** scopes.
* The validity period of the token is 30 days (**2,592,000** seconds).
* The current token is **0987654321jihgfedcba**.
* The current token has been created on **March 6th, 2019** and expires on **April 5th, 2019**.

## Step 1 Get the ID of an old token

If you only know the token itself, you need to obtain its ID to revoke and subsequently delete it. To do so, issue a [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.") request with the token to be deleted as the payload.

The request returns the metadata of the token, including its ID, which you will need later.

#### Request

Send a POST request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/lookup
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/lookup

Include this `application/json` payload, where `0987654321jihgfedcba` is the token value:

```
{



"token": "0987654321jihgfedcba"



}
```

#### Response

The request returns the metadata of the token in the `application/json` payload:

```
{



"id": "a6e91657-1fa7-4742-af40-39469b92bd65",



"name": "RW config token",



"userId": "admin@mysampleenv.com",



"created": "2019-03-06T09:15:49Z",



"expires": "2019-04-05T09:15:49Z",



"scopes": [



"ReadConfig",



"WriteConfig"



]



}
```

You need to retrieve token's **id** value, which you will need to retire (revoke and delete) this token.

## Step 2 Create a new token

To create a new token that will replace the outdated one, execute a [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Learn how to use the Dynatrace API to create a new Dynatrace API authentication token.") request. Since you create a token with same parameters on a regular basis, you might consider storing its configuration in a version control system.

#### Request

Send a POST request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens

Include this `application/json` payload:

```
{



"name": "RW config token",



"scopes": [



"WriteConfig",



"ReadConfig"



],



"expiresIn": {



"value": 30,



"unit": "DAYS"



}



}
```

#### Response

The request returns the new token in the `application/json` payload:

```
{



"token": "jihgfedcba0987654321"



}
```

## Step 3 Revoke the old token

To revoke the old token, execute [PUT an existing token](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Learn how to use the Dynatrace API to update a Dynatrace API authentication token."). You will need the token **id** value you obtained in [step 1](#get-old).

A revoked token cannot be used for authentication, but it still exists in your environment. We recommend that you wait a week before deleting a revoked token, in case there is an emergency need for it. Check your organization's security policies for the exact delay.

If you want to rotate the token you're currently using for authentication of API calls, replace it with the new token you've just created in the [step 2](#create-new).

In our example, the ID of the token to be revoked is **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Request

Send a PUT request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

Include this `application/json` payload:

```
{



"revoked": true



}
```

#### Response

A successful request is indicated by the **204** response code. It doesn't return any content.

## Step 4 Delete the old token

After the waiting period, with the old token disabled (revoked), delete it. To do so, execute [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Learn how to delete a Dynatrace API authentication token using the Dynatrace API."). You will need the **ID** of the token you obtained in [step 1](#get-old).

In our example, the ID of the token to be deleted is **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Request

Send the DELETE request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

#### Response

A successful request is indicated by the **204** response code. It doesn't return any content.