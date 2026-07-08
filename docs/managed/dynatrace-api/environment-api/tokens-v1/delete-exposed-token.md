---
title: Find and replace an exposed token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token
---

# Find and replace an exposed token

# Find and replace an exposed token

* Reference
* Updated on May 17, 2022

If any of your Dynatrace API authentication tokens is compromised (becomes exposed to the public) for any reason, immediately stop using it, remove it as soon as possible, and issue a replacement token as needed. The token API comes in handy for this task.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get the ID of an exposed token**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#get-old "Learn how to find and replace an exposed Dynatrace API authentication token using the Dynatrace API.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Delete the exposed token**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#delete-old "Learn how to find and replace an exposed Dynatrace API authentication token using the Dynatrace API.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create a new token to replace the compromised token**](/managed/dynatrace-api/environment-api/tokens-v1/delete-exposed-token#create-new "Learn how to find and replace an exposed Dynatrace API authentication token using the Dynatrace API.")

## Step 1 Get the ID of an exposed token

To delete a token, you need to obtain its ID. To do so, execute the [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.") request with the token to be deleted as a payload.

The request will return the metadata of the token. From the metadata, you will need:

* The **ID** of the token so you can delete it.
* The **userID** of the token owner so you can notify the user that the token is not usable anymore.
* The **scope** of the token so you can create a replacement token.

#### Request

Send a POST request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/lookup
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/lookup

Send it with an `application/json` payload like this, where `0987654321jihgfedcba` is the token:

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



"name": "John's token",



"userId": "john@mysampleenv.com",



"created": "2019-03-06T09:15:49Z",



"expires": "2019-04-05T09:15:49Z",



"scopes": [



"DataExport",



"ExternalSyntheticIntegration"



]



}
```

From this data, you need to retrieve the **id**, which you need to delete this token.

## Step 2 Delete the exposed token

Now delete the compromised token. To do so, execute [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Learn how to delete a Dynatrace API authentication token using the Dynatrace API."). You will need the **id** value you obtained in [step 1](#get-old).

In our example, the ID of the token to be deleted is **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Request

Send the DELETE request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

#### Response

A successful request is indicated by the **204** response code. It doesn't return any content.

## Step 3 Create a new token

To create a new token to replace the exposed one, execute the [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Learn how to use the Dynatrace API to create a new Dynatrace API authentication token.") request. Be sure to assign the same scope to it.

When the new token is created, give it to the user in accordance with the security policy of your organization.

#### Request

Send the POST request to this URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens

Include this `application/json` payload:

```
{



"name": "John's token",



"scopes": [



"DataExport",



"ExternalSyntheticIntegration"



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