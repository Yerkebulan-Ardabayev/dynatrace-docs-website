---
title: Account Management permissions
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/account-management-permissions
---

# Account Management permissions

# Account Management permissions

* Reference
* 5-min read
* Published Feb 01, 2022

Users need specific permissions to access Account Management. Capabilities are guarded in Account Management by the permissions shown in the following table.

## Permissions and capabilities

Each of the three account-level permissions:

* **View account**
* **View and manage account and billing information**
* **View and manage users and groups**

has a different set of capabilities in Account Management.

| **Capability** | **View account** | **View and manage account and billing information** | **View and manage users and groups** |
| --- | --- | --- | --- |
| Profile | Applicable | Applicable | Applicable |
| Lens account adoption | Applicable | Applicable | Not applicable |
| Lens environment information | Applicable | Applicable | Not applicable |
| Lens report | Applicable | Applicable | Not applicable |
| License and subscription management | Applicable | Applicable | Not applicable |
| View Dynatrace Platform Subscription consumption and usage | Applicable | Applicable | Not applicable |
| View subscription history | Applicable | Applicable | Not applicable |
| Cost Management | Not applicable | Applicable | Not applicable |
| Edit environment settings | Not applicable | Applicable | Not applicable |
| Split HU quota | Not applicable | Applicable | Not applicable |
| IAM | Not applicable | Not applicable | Applicable |
| IAM oAuth clients | Not applicable | Not applicable | Applicable |

## Manage permissions

Permissions are cumulative and are granted to the user using the appropriate Identity and Access Management interface.

Managed deployments manage permissions through the Cluster Management Console, which allows you to configure the account-level permissions needed to grant access to license and Lens capabilities.

A Dynatrace Managed user that needs access to the Account Management portal must have an active Dynatrace user account—which is used to access online Community and Support resources—and the correct permissions to access their account.

To provide a user with a Dynatrace user account, a **cluster administrator** must invite the user to support resources.

1. In Cluster Management Console, select **User authentication** > **User accounts**.
2. Select the user that needs access to Account Management.
3. Select **Invite to support resources** or **Resend invitation to support resources**.
4. The user will receive an email from Dynatrace (`notifications-noreply@dynatrace-managed.com`) with their username and instructions on how to set their password.

   Invitation expiration

   An emailed invitation expires after 24 hours.

Alternatively, your cluster administrator can enable a global setting to automatically invite new users to the Dynatrace Community. For details, see the [Dynatrace Community settings](/managed/managed-cluster/configuration/configure-cluster-preferences#dynatrace-community "Configure cluster preferences to manage proactive support reporting, remote access, data privacy, domain name, and community settings for your Managed Cluster.") page.

To provide access to Account Management, a **Cluster administrator** must add the user to a **group** with either the permission **Edit billing & account info** or **Access account**, which is referred to as the **View account** permission in the [permissions table](#permissions-table) above.

* A user only needs to be assigned to a group from within one cluster with the relevant account management permission.
* Cluster administrator is not a valid permission for Account Management. Additionally, the user that creates the first managed cluster can't be added to any other group and can't access Account Management.

## Access URLs

A user can be associated with one or more accounts. Account Management redirects to the correct location based on the following URLs:

* **URL:** `myaccount.dynatrace.com`

  Opens the home page of the user's account. If the user is a member of multiple accounts, they're directed to the **My accounts** page (`https://myaccount.dynatrace.com/accounts`) to select one.
* **URL:** `myaccount.dynatrace.com/accounts`

  Opens the **My accounts** page, which allows the user to select which account to open from the list of accounts to which the user has access.
* **URL:** `myaccount.dynatrace.com/account/home?account-uuid=<account_uuid>`

  Opens the home page of a specific account by `<account_uuid>`. Bookmark these URLs to access your accounts directly.

## FAQ

Why is the cluster administrator unable to access Account Management?

The permissions listed in the [permissions table](#permissions-table) above are account-level permissions and are visible to Account Management. The cluster administrator permission is visible only at the cluster level and does not provide the visibility that Account Management requires to provide access.

My user account is a member of a group with the required permissions. Why can't I access Account Management?

If the user is added to a group with **View account** or **View and manage account and billing information** permissions, it might take some time (up to 24 hours) for the cluster to synchronize with the Dynatrace identity management system. If user permissions are not synchronizing between your cluster and IDM, contact a Dynatrace product expert via live chat to let us know.

Can I limit visibility across environments or clusters in Account Management?

Account Management is an account-level tool to help organizations manage their subscription across environments and clusters. You can govern access using the permissions in the [permissions table](#permissions-table) above, but visibility is granted across clusters and environments.