---
title: "Navigate the Dynatrace Managed platform"
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/dynatrace-ui
updated: 2026-02-09
---

* Explanation
* 8-min read

## Dynatrace menu

Use the menu to navigate Dynatrace.

### Filter the menu

Use the filter box above the menu to find and select Dynatrace pages.

1. Enter a partial search string.

   ![Filter the menu](https://dt-cdn.net/images/filter-265-fc8901c349.png)
2. Select the best match.

   ![Select a menu item from the filter results](https://dt-cdn.net/images/filter-and-select-266-ac5a5c8210.png)

### Save your favorites

* To add a Dynatrace page to your favorites, hover over the page name and select the star.

  ![Add menu item to Favorites](https://dt-cdn.net/images/favorite-add-266-7262cf1304.png)
* To access a favorite, expand the **Favorites** section and select the page.

  ![Select a menu item from Favorites](https://dt-cdn.net/images/favorite-select-266-ca63c732de.png)
* To remove a page from your favorites, select the star again.

  ![Remove menu item from Favorites](https://dt-cdn.net/images/favorite-remove-264-6eb91e3ff5.png)

### Expand and collapse menu sections

* To show the contents of a menu section, select the expand button.

  ![Expand menu section](https://dt-cdn.net/images/section-expand-261-70573d8144.png)
* To hide the contents of a menu section, select the collapse button.

  ![Collapse menu section](https://dt-cdn.net/images/section-collapse-261-d51061df78.png)

### Hide or show the menu

* To hide the menu, select the arrow button above the menu.

  ![Hide menu](https://dt-cdn.net/images/menu-hide-2-271-588d75e5e9.png)
* To display the menu, select the menu button in the upper-left corner.

  ![Display the hidden menu](https://dt-cdn.net/images/menu-display-235-ba2b8a386f.png)

### User menu

![Display the user menu](https://dt-cdn.net/images/user-menu-86-9ab2cd2961.png)

The contents of this user menu depend on your permissions.

* Go to the user menu for your own account information, to sign out, to switch between environments, and to get the latest Dynatrace news.
* If you have administration permissions, select **Account settings** on the user menu to manage user, group, and account settings.

## Cluster Management Console (CMC)

### Home

**Home** displays the **Dynatrace Managed deployment overview** (the CMC default page), with a graphical representation of your deployment at a glance.

* [Environments](#environments)âDisplays the number of active environments. Links to [Environments](#environments).
* [ActiveGates](#deployment-status-activegates)âDisplays the number of Cluster ActiveGates and Environment ActiveGates. Links to [Deployment status](#deployment-status).
* [Cluster nodes](#deployment-status-cluster-nodes)âDisplays the number of Cluster nodes.
* Last backupâDisplays the date and storage location of the last backup.
* [Events](#events)âDisplays the number of log events.
* [Users](#user-authentication)âDisplays the number of users and user groups.
* Dynatrace Mission Control

### Deployment status

**Deployment status** displays:

#### Cluster nodes

* For details on a cluster node, expand its row.
* To install a cluster node, select **Install cluster node** in the upper-right corner.

#### ActiveGates

* For details on an ActiveGate, expand its row.
* To install a cluster ActiveGate, select **Install Cluster ActiveGate** in the upper-right corner.

#### Network zones

* For details on a network zone, select its name in the table.

### Environments

**Environments** displays a table of all Dynatrace environments you managed.

* To find an environment, use the filters on the left.
* To open an environment's details page, select the environment name.

  + To change an environment-specific setting, select  for that setting.  
    Sections include:

    - Capability settings
    - Storage settings
    - Cluster overload prevention settings
    - Assign environment permissions to user groups
  + To go to the selected Dynatrace environment, select  **Go to environment** in the upper-right corner.
  + To disable the selected Dynatrace environment, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Disable environment** in the upper-right corner.
  + To export the configuration of the selected Dynatrace environment, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Export configuration** in the upper-right corner.

### Events

**Events** lists log events by message and timestamp.

* Filter the table by:

  + Severity level
  + Timeframe
  + String search
* Page through the table with the controls under the table.

### User authentication

**User authentication** links to user-related settings.

* **User accounts**âLists user accounts. Select a user to view details and group assignments and permissions. For details, see User and group management.
* **User groups**âLists user groups. Select  for a group to configure the group name, permissions, and policies. For details, see User and group management.
* **Policy management**âLists policies. Select in the **Actions** column to view or edit a policy.
* **User sessions**âLists user sessions. For details, see Configure and manage user sessions.
* **Password policy**âFor details, see Password complexity rules.
* **User repository**âView and edit user repository settings. For details, see Manage users and groups via LDAP.
* **Single sign-on settings**âFor details, see Manage users and groups with SAML in Dynatrace Managed and Manage users and groups with OpenID in Dynatrace Managed.
* **Login screen**âFor details, see Sign-in page customization.

### Settings

**Settings** links to cluster-related settings.

* **Public endpoints**
* **Internet proxy**âFor details, see Configure internet proxy for cluster.
* **Emails**

  + **SMTP server**âConfigure how email notifications for the cluster are delivered. For details, see Configure an SMTP server connection.
  + **Email notifications**âConfigure email notification recipients.
* **Preferences**âFor details, see Cluster preferences settings.
* **Remote access permissions**âFor details, see Cluster remote access.
* **API tokens**âFor details, see Cluster API - Authentication.
* **Backup**âFor details, see Backup and restore a cluster.
* **Service Providers**
* **Automatic update**âFor details, see Update Dynatrace Managed.

### Licensing

**Licensing** displays account- and license-related information.

* **Account**
* **Contact email address**
* **Cluster identifier**
* **License name**
* **License type**
* **Expires**
* **Product version**
* **Premium High Availability**
* **Mainframe monitoring on IBM z/OS**
* **License status**
* **License key**

To verify your connection to Mission Control, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Check Mission Control connection** in the upper-right corner.

### Audit log

**Audit log** lists events triggered by the cluster and selected configuration changes for all environments.

This table shows only changes related to cluster-wide configuration, licensing, storage quota, and permissions. For all environment audit log entries, use the Audit Log REST API.
