---
title: SCIM
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim
scraped: 2026-02-17T05:09:03.419970
---

# SCIM

# SCIM

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jun 30, 2025

System for Cross-domain Identity Management (SCIM) is an open standard for automating the exchange of user identity information between identity domains or IT systems. You can configure Dynatrace SaaS to be provided with user identity information automatically from your organization's identity provider (IdP) through SCIM.

## Benefits of using SCIM with Dynatrace SSO

* Users in your IdP will automatically be synchronized with Dynatrace, so there is no need to invite them manually

  + if a user is disabled or removed from the IdP, it will also disable the user in Dynatrace
* Groups in your IdP will automatically be synchronized with Dynatrace

  + All groups created by SCIM will be of type `SCIM` in Account Management
* Users will be assigned to groups in Dynatrace mirroring the relationship within the IdP

## SCIM notice and limitations

* SCIM synchronization is one-way from the IdP to Dynatrace. This is because technically the IdP is the owner of both the users and groups and changes in Dynatrace will never transpire to the IdP.
* Dynatrace will only accept users with domains, which were verified within the account
* Groups of type `SCIM` are managed by SCIM only and cannot be removed or modified through Account Management
* Permissions to SCIM groups still have to be assigned manually in Dynatrace

  + It is possible to use [Account Management API](/docs/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.") to manage the permissions programmatically
* If your SCIM client does not support dynamic external id changes, email/login change will cause SCIM integration to stop working for such users. Requests will be rejected due to invalid username (in SCIM it is email)
* The scope of users and groups synchronized into Dynatrace with SCIM can be narrowed within the SCIM application in your IdP
* Users in SCIM groups are not listed in the web UI for sharing a document (dashboard or notebook) to specific users or groups unless you add those users to local Dynatrace groups.
* A user cannot be assigned to an account if the account has already reached its [maximum number of assigned users](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS").
* A user cannot be added to a group if they have already reached the [maximum number of groups they can be assigned to](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS").

## SCIM requirements and supported features

* Dynatrace supports **SCIM 2.0** and **GET**, **POST**, **PATCH**, **PUT**, and **DELETE** operations for both **User** and **Group** resources.
* For authentication, SCIM requires **Bearer token** in **Authorization header**.
* SCIM is configured for the account and domain scopes. At least one domain ownership verification is required for the account.
* Only users whose email domains have been verified for ownership can be synchronized with Dynatrace via SCIM.
* Required and supported SCIM attributes:

  | SCIM Attribute | Type |
  | --- | --- |
  | userName | email format |
  | name.givenName | string |
  | name.familyName | string |
  | active | boolean |
* **userName** must be persistent. Dynatrace does not support user email change.

## Verify your ownership of the domain

Before you can proceed with SCIM configuration, you need to prove ownership of the domain. Verification is based on a DNS TXT Record check.

For the account, it is sufficient to verify the domain once. If a domain has been verified for SAML, it will be valid for SCIM as well.

To verify ownership of a domain

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Domain verification**.
3. In the **Add domain** section, enter the domain (for example, `mycompanyname.com`) for which you want to set up SCIM and select **Add** to add it to the **Pending domains** table.

   Multiple domains

   If users in your organization use more than one domain to sign in (for example, `@mycompanyname.com` and `@uk.mycompanyname.com`), you can add additional domains in additional rows and start verifying them all in parallel. Enter each domain in a different row.
4. For each domain you are verifying, in the **Pending domains** table, select **Copy** (in the **Value** column) and add the copied TXT resource record to your domainâs DNS configuration.
5. For each domain you are verifying, in the **Pending domains** table, select **Actions** > **Verify** so that Dynatrace can verify that the record was added to your domainâs DNS.

   Propagation time

   It typically takes a few minutes for a record to propagate through the DNS system and the value to become available for Dynatrace to verify. In some cases, it may take up to 24 hours.
6. Each verified domain is added to the **Verified domains** table.

## Get Dynatrace SCIM endpoint and create secret token

Use this procedure to get the Dynatrace SCIM Base URL for your account and create a secret token.

The token is revealed only once during generation time. Copy and paste it into a secure location. If you lose it, you have to generate a new one and replace it in your application.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **SCIM configuration**.
2. In the **Generate new token** section, optionally enter a token **Description** (or you can add a description for the token later).
3. Select **Generate token**
4. Next to **Token value**, select **Copy** to copy the token to your clipboard, and then paste it into a secure location for later use.

   Dynatrace SCIM supports Bearer Token Authentication only. Example:

   | Header | Value |
   | --- | --- |
   | Authorization | Bearer <DYNATRACE_TOKEN_PLACEHOLDER> |

The SCIM endpoint required for SCIM configuration in your application is added to the **List of tokens**.

## Example IdP-specific instructions

To continue integrating Dynatrace SCIM with your IdP, select the procedure appropriate for your IdP:

* [Azure](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure "Learn how to configure Dynatrace SCIM in Azure.")
* [Okta](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-okta "Learn how to configure Dynatrace SCIM in Okta.")

## FAQ

Is a change of email address supported?

No, an email address can't be changed by SCIM. Any requests to update an email address are ignored.

How many SCIM authentication tokens can I generate?

You can generate up to 10 SCIM authentication tokens. For security reasons, we strongly recommend that you delete all unused tokens.

Can I provision users from different email domains?

Yes, you can provision as many users from different email domains as you need, as long as all of their domains have been verified. You can verify multiple domains for a single account.

It is possible to create more than one group with the same name?

No, some IdPs, like Azure AD, allow multiple groups with the same name in a single account. For Dynatrace SSO, however, each group name in an account must be unique.

Is it possible to set group `description` during provisioning?

No, we're limited by the SCIM protocol specification, so additional fields, such as `description`, can't be set during provisioning.

### Azure

I have accidentally deleted a SCIM synchronized user in Dynatrace my account. Is it possible to re-synchronize the user via SCIM in Azure?

Yes, you can restart SCIM synchronization. To do this, go to the SCIM application's **Overview** tab and select **Restart provisioning**.