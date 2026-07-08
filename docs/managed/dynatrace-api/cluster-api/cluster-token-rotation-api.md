---
title: Rotating cluster tokens via API
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-token-rotation-api
---

# Rotating cluster tokens via API

# Rotating cluster tokens via API

* Published Feb 28, 2020

Regularly changing your Dynatrace API authentication tokens is a good security practice. You can use Dynatrace Cluster API to rotate cluster management tokens. With the Tokens API, you can also automate the rotation.

To access the Dynatrace Cluster API

1. Open the Cluster Management Console.
2. Go to the User menu in the upper-right corner.
3. Select **Cluster API**.

## Token rotation

To rotate cluster management tokens using Tokens API

1. Get the ID of an old token.

   You need the ID so you can revoke and then delete it. If you only know the token itself, you need to get the token's ID to revoke and subsequently delete it. To do so, issue a [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.") request with the token to be deleted as the payload. The request returns the metadata of the token, including its ID, which you will need later.
2. Create a new token.

   To create a new token that will replace the outdated one, execute a [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Learn how to use the Dynatrace API to create a new Dynatrace API authentication token.") request. Since you create a token with same parameters on a regular basis, you might consider storing its configuration in a version control system.
3. Revoke the old token. (Don't delete it before you revoke it.)

   To revoke the old token, execute [PUT an existing token](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Learn how to use the Dynatrace API to update a Dynatrace API authentication token."). You will need the token **ID** value you obtained in step 1.  
   A revoked token can't be used for authentication, but it still exists in your environment. We recommend that you wait a week before deleting a revoked token, in case there is an emergency need for it. Check your organization's security policies for the exact delay.  
   If you want to rotate the token you're currently using for authentication of API calls, replace it with the new token you created in step 2.
4. Delete the old token.

   After the waiting period, with the old token disabled (revoked), delete it. To do so, execute [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Learn how to delete a Dynatrace API authentication token using the Dynatrace API."). You will need the **ID** of the token you obtained in step 1.

## Example of rotating a token

For this example, let's assume you want to rotate a token with the following parameters:

* The name of the token is `ClusterTokenManager`.
* The scope of the token includes `Cluster token management` permissions.
* The current token is `0987654321jihgfedcba`.

With the Tokens API, you can automate the rotation.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get the ID of an old token**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-1 "Find out how to rotate cluster management tokens using Cluster API.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create a new token**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-2 "Find out how to rotate cluster management tokens using Cluster API.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Revoke the old token**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-3 "Find out how to rotate cluster management tokens using Cluster API.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Delete the old token**](/managed/dynatrace-api/cluster-api/cluster-token-rotation-api#step-4 "Find out how to rotate cluster management tokens using Cluster API.")

### Step 1 Get the ID of an old token

You will need the ID so you can revoke and then delete it.

Send a `POST` request to `https://<your-domain>/api/cluster/v1/tokens/lookup`  
Include this `application/json` payload, where `0987654321jihgfedcba` is the token value:

```
{



"token": "0987654321jihgfedcba"



}
```

The request returns the metadata of the token in the `application/json` payload:

```
{



"id": "3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5",



"name": "ClusterTokenManager",



"userId": "admin@mycluster.com",



"revoked": false,



"created": 1578902397474,



"lastUse": 1582130541813,



"scopes": [



"ClusterTokenManagement"



]



}
```

Save the token's **ID** value (`3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`).  
You will need it later to revoke and delete this token.

### Step 2 Create a new token

Send a `POST` request to `https://<your-domain>/api/cluster/v1/tokens`  
Include this `application/json` payload:

```
{



"name": "ClusterTokenManager",



"scopes": [



"ClusterTokenManagement"



],



"expiresIn": {



"value": 30,



"unit": "DAYS"



}



}
```

The request returns the new token in the `application/json` payload:

```
{



"token": "jihgfedcba0987654321"



}
```

### Step 3 Revoke the old token (3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5)

Saved ID (step 1) of the token to be revoked and then deleted is: `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`

Send a `PUT` request with the token to be revoked to `https://<your-domain>/api/cluster/v1/tokens/3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`  
Include this `application/json` payload:

```
{



"revoked": true



}
```

A successful request is indicated by the `204` response code. The response doesn't return any content.  
The token with ID `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5` is now revoked.

### Step 4 Delete the old token (3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5)

To delete the `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5` token, send the `DELETE` request with the revoked token ID to `https://<your-domain>/api/cluster/v1/tokens/3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5`

A successful request is indicated by the `204` response code. The response doesn't return any content.  
The token with ID `3cf7c26f-ab12-abc123-ab1a-9340a6cce9a5` is now deleted.