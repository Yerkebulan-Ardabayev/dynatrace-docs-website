---
title: Platform tokens
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens
scraped: 2026-02-18T21:30:26.295024
---

# Platform tokens

# Platform tokens

* Latest Dynatrace
* Reference
* 8-min read
* Published Jul 23, 2024

Platform tokens are long-lived access tokens enabling programmatic access to Dynatrace platform services. They can be created by regular users and work within the bounds of the assigned user permissions.

Platform tokens are a user-friendly alternative to OAuth clients and are suited for processes and applications that integrate directly with the Dynatrace API. They can be assigned to the user creating them or to a service user that the creating user has access to.

Platform tokens can be set to expire after a period of time or never expire.

These properties make platform tokens a good candidate for all sorts of integrations with the Dynatrace platform, such as:

* Running a scheduled Grail query for data export and ETL
* Ingesting business metrics and events via the API
* A script that keeps Dashboards in sync across multiple environments

## How to use a platform token

Platform tokens are directly usable with the APIs offered by the Dynatrace platform services. To use a platform token please provide the token in the Authorization header:

`Authorization: Bearer <platformtoken>`

To get an overview of all the services supporting platform tokens, go to the Dynatrace API explorer. In Dynatrace, search for **Dynatrace API** and select the result.

You can also directly put the platform token into the Authorization field in the Dynatrace API explorer for quick experimentation and try-out.

## My platform tokens

This feature is available for regular users. Every user can create platform tokens in all the accounts of which they are a member.

The platform token management operations listed below are all performed using the **Account Management** pages.

1. Go to [My platform tokensï»¿](https://myaccount.dynatrace.com/platformTokens).

   This opens `https://myaccount.dynatrace.com/platformTokens`, which you can bookmark for easy access to platform tokens Management.
2. You are presented with a table that list all your platform tokens.

This page lists all of your platform tokens and enables you to create, delete, or disable your tokens.

### Create a new platform token

Every user is able to create up to 10 platform tokens in a given account.

1. Select  \*\*platform token \*\* and specify:

   * **Token Name**
   * **Expiration date**
   * **Account**
   * **Apply to account**
   * **Environments**.

     + If **apply to account** has been selected, this is not available.
2. Choose if the new token will be generated for you (default) or a service user you have access to.
3. Select token scopes in the table below

   * The table provides you with a list of scopes that map to the individual endpoints on the API.
   * Go to the Dynatrace API explorer, to see the mapping between token scopes and API endpoints.
   * **IMPORTANT**: A platform token will only work within the limits of the assigned user's permissions. This means that a selected scope is only granting access if that user has the respective permissions.
4. Select **Generate** to generate the platform token.
5. The created token will only be shown once, so make sure you copy it into a secure location.
6. After you have saved the token, select **Finish and exit** to return to the list of platform tokens.

### Disable a platform token

1. Find the platform token that you want to disable in the list overview.
2. In the **Actions** column, select  > **Disable**.
3. Select **Cancel** to cancel or **Disable** to confirm.

   * The dialog shows the ID of the token for confirmation.

A disabled token can not be used on the API but can later on be re-enabled to continue using it.
This is handy if you want to temporary block a token.

Disabling a platform token is immediate, but it may take up to five minutes for the change to propagate.

### Delete a platform token

1. Find the platform token that you want to delete in the list overview
2. In the **Actions** column, select  > **Delete**.
3. Select **Cancel** to cancel or **Disable** to confirm.

   * The dialog shows the ID of the token for confirmation.

### Duplicate a platform token

1. Find the platform token that you want to duplicate in the list overview.
2. In the **Actions** column, select  > **Duplicate**.
3. The creation process is triggered with an exact copy of the properties of the original token and the name "Duplicate of:" `<token-name>`.
4. Adjust the properties to your liking and select **Generate**.
5. After you duplicate the token, it's the only time you can preview it and copy to store for later use.
6. After you have stored the token, select **Finish and exit** to return to the list of platform tokens.

### Rotate a platform token

It's a security best practice to regularly rotate your tokens.

To rotate an active token

1. Find the platform token that you want to rotate in the list overview.
2. In the **Actions** column, select  > **Rotate**.
3. Choose when to expire the old token

   * You may choose to expire immediately or defer to a later time so that you allow some overlap between the two tokens.
4. Choose a name.

   * To differentiate the rotated token from the original, you can add the current date in the token name.  
     old: `K8s operator`  
     new: `K8s operator 10.09.2024`
5. Either accept the proposed expiry time or change it.
6. Select **Rotate**.

   * Do not forget to replace the old token with the new one, in all places you are using it.

### Expired tokens

Expired tokens will continue to show in the list overview until you or the account admin decides to delete them.

## Manage users tokens

Account admins can disable or delete platform tokens created by all users under their account. The Account Management UI management actions are performed in a similar way to the ones listed above for regular users.

### Disable platform token creation for an entire account

Account admins have the ability to enable or disable creation of new platform tokens for a given account.

1. In Account Management, go to **Identity & access management** > **Platform tokens**.
2. Turn off **Allow to manage platform tokens** and confirm the dialog with **Deny**.
3. Optional To disable existing platform tokens use, select specific or all tokens with the checkboxes on the left and select **Disable** at the top of the list.
4. Optional To delete existing platform tokens use, select specific or all tokens with the checkboxes on the left and select **Delete** at the top of the list.

To re-enable the creation of new platform tokens, turn on **Allow to manage platform tokens** and confirm the dialog with **Allow**.

### Allow users to generate platform tokens against service users

To allow users to generate platform tokens against existing service users, the account admin needs to assign `iam:service-users:use` permissions, and optionally conditionalize it with `iam:service-user-email` to one or more groups. An example policy could look like this:

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("abc@service.sso.dynatrace.com", "def@service.sso.dynatrace.com");
```

## Platform tokens requirements

* A maximum of 10 platform tokens can be generated by a user for a given account.
* A platform token is scoped to only one account and cannot be used to access other accounts.
* A platform token can be further reduced in scope to only target one or many environments within the account the token is being issued against.
* A platform token name can't exceed 255 characters.
* Using expired platform tokens to access Dynatrace will return an HTTP error 403 response.

## Available services for platform tokens

The following services are covered by platform tokens:

* `app-engine`
* `automation`
* `notification`
* `davis`
* `davis-copilot`
* `document`
* `email`
* `iam`
* `platform-management`
* `storage`
* `settings`
* `app-settings`
* `state`
* `state-management`