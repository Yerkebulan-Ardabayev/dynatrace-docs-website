---
title: Azure SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure
scraped: 2026-02-27T21:27:40.354754
---

# Azure SCIM configuration for Dynatrace

# Azure SCIM configuration for Dynatrace

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Aug 06, 2024

This page describes the IdP (**Azure**) end of your **SCIM** SSO configuration, not the Dynatrace end. Use it as part of the entire [SCIM configuration procedure](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM") for Dynatrace SaaS if you're using Azure.

While we do our best to provide you with current information, Dynatrace has no control over changes that may be made by third-party providers. Always refer to official third-party documentation from your IdP as your primary source of information for third-party products.

To set up SCIM for your domain

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create SCIM application in Azure**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#create-scim-app "Learn how to configure Dynatrace SCIM in Azure.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure provisioning**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#provisioning "Learn how to configure Dynatrace SCIM in Azure.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Configure group mappings**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#configure-group-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Configure user mappings**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#configure-user-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Assign users and groups**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#assign-users-and-groups "Learn how to configure Dynatrace SCIM in Azure.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Enable SCIM**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#enable-scim "Learn how to configure Dynatrace SCIM in Azure.")

## Step 1 Create SCIM application in Azure

In **Microsoft Entra ID**

1. From the leftmost menu, select **Manage** > **Enterprise applications**.
2. Select **New application** > **Create your own application**.
3. In the pop-up window on the right, enter an **Input name** for your app.

   Make sure that you have selected **Integrate any other application you don't find in the gallery (Non-gallery)**.
4. Select **Create**.

## Step 2 Configure provisioning

To configure provisioning in Azure, you need the Dynatrace SCIM base URL and a secret token you got in the [Get Dynatrace SCIM endpoint and create secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

In **Microsoft Entra ID** with your application selected

1. If you're already on the application **Overview** page, select **3. Provision User Accounts** in the **Getting Started** section.

   Alternatively, from the leftmost menu, select **Manage** > **Provisioning**.
2. If you're doing this for the first time, select **Get started**.
3. In **Provisioning Mode**, select **Automatic**.
4. Expand **Admin Credentials**.
5. Enter your admin credentials:

   * **Tenant URL**  
     Example: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**  
     You got this token from Dynatrace.
6. Select **Test Connection** to validate the endpoint and credentials.
7. If the test succeeds, select **Save** in the upper-left corner of the page to generate mappings.

   If the test fails, verify your settings:

   * **Tenant URL**  
     Example: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**  
     You created this earlier in the [Get a secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

## Step 3 optional Configure group mappings Optional

Do this if you need to provision only certain groups in Dynatrace.

In **Microsoft Entra ID** with your application selected

1. On the **Provisioning** page, expand **Mappings**.
2. Select **Synchronize Azure Active Directory Groups to customappsso**.

   Make sure that the **Enabled** toggle is set to **Yes**.
3. In **Source Object Scope**, select **All records**.
4. Select **Add new filter group**.
5. Fill in the fields.
6. Select **Apply** in the lower-left corner.
7. You can leave all **Target Object Actions** selected.  
   Dynatrace SCIM supports all of these actions.
8. Set **Attribute Mappings** as follows:
9. Select **Save** on the **Attribute Mapping** page.

## Step 4 Configure user mappings

You need to limit the scope of users that are provisioned by SCIM to those with matching email domains to prevent your SCIM requests from being rejected.

To create a filtering rule for users

1. On the **Provisioning** page, expand **Mappings**.
2. Select **Synchronize Azure Active Directory Users to customappsso**.
3. Select your **Source Object Scope**.
4. Select **Add new filter group**.
5. On **Add Scoping Filter**, fill in the fields as follows:

   * Source Attribute: `mail`
   * Operator: `ENDS_WITH`
   * Clause value: `@<YOUR_DOMAIN>` (for example, `@example.com`)

   Keep in mind that subdomains should be verified for the account separately. Therefore, the `@` in the domain string is required and will guarantee that your requests won't be rejected due to an invalid user domain.
6. Select **Apply** in the lower-left corner.
7. You can leave all **Target Object Actions** selected.  
   Dynatrace SCIM supports all of these actions.
8. Limit **Attribute Mappings** to the following:
9. Select **Show advanced options** in **Attribute Mappings**, and select **Edit attribute list for customappsso**.
10. Make sure the following checkboxes are selected.

    * For **id**âselect **Primary Key?** and **Required?**
    * For **userName**âselect **Required?**
11. Select **Save** on the **Edit Attribute List** page.
12. Select **Save** on the **Attribute Mapping** page.

## Step 5 Assign users and groups

To assign users or groups to your application and send them via SCIM to Dynatrace, in **Microsoft Entra ID**

1. If you're already on the application **Overview** page, select **1. Assign users and groups** in the **Getting Started** section.

   Alternatively, from the leftmost menu, select **Manage** > **Users**.
2. Select **Add user/group**.
3. Select the **Users and groups** you want to sync.
4. Select **Assign**.

## Step 6 Enable SCIM

To enable SCIM provisioning

1. Go to the **Provisioning** page and expand **Settings**.
2. In **Scope** list, select **Sync only assigned users and groups**.
3. Turn **Provisioning Status** on.

In Azure, the initial sync takes longer than subsequent syncs, which occur approximately every 40 minutes as long as the service is running.

## Troubleshooting

I have accidentally deleted a SCIM synchronized user in Dynatrace my account. Is it possible to re-synchronize the user via SCIM in Azure?

Yes, you can restart SCIM synchronization. To do this, go to the SCIM application's **Overview** tab and select **Restart provisioning**.