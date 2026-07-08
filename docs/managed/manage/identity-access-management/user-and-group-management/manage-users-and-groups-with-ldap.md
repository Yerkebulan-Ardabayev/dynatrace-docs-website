---
title: Manage users and groups via LDAP
source: https://docs.dynatrace.com/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap
---

# Manage users and groups via LDAP

# Manage users and groups via LDAP

* Published Jul 19, 2017

You can connect your Dynatrace Managed cluster to an LDAP directory for authentication, user management, and group management.

With LDAP integration, users from the external LDAP resource can access Dynatrace. You can then assign users to groups in Dynatrace, or groups can be assigned to users based on LDAP information.

## Get started

1. Go to **User authentication** > **User repository**.
2. Select **External LDAP server** from the list.  
   The **LDAP configuration** page is displayed.

   Example 'LDAP configuration' page

   ![LDAP configuration](https://dt-cdn.net/images/live-example-obfuscated-1218-f4bcd0eb01.png)

   LDAP configuration

   After you switch to LDAP authentication

   1. Local accounts (other than the administrator account) will stop working: it will be impossible to log in with a local account.
   2. The administrator account you created during installation will continue to work regardless of the selected authentication provider.
3. The **LDAP configuration** page displays a three-step process for configuration

   1. [Connection configuration](#connection-configuration)
   2. [Groups query configuration](#groups-query-configuration)
   3. [Users query configuration](#users-query-configuration)

   See below for configuration details.

## Connection configuration

Example 'Connection configuration' section

![Configuration connection settings](https://dt-cdn.net/images/1-connection-configuration-278-e88f7c30f4.png)

Configuration connection settings

1. Enter your LDAP **Host address**.

   * To enable encrypted communication with the LDAP server, select **Use SSL**. This will change **Port number** automatically, but you can then configure it to a different value as needed.
2. Adjust **Port number** as needed:

   * 389 is the default port number for a standard LDAP connection, but verify that your LDAP server actually uses it
   * 636 is the default port number for an LDAPS (LDAP over SSL) secure connection
3. Specify the **Bind DN** (Distinguished Name) for the LDAP user account, for example, in the format of:  
   `CN=UserName,OU=OU-name,DC=DomainName,DC=DomainExtension`  
   or any other valid LDAP string.

   **Bind DN** typically is a system user (not an actual person) used to connect to the LDAP server. From the LDAP server perspective, it's just a user that reads data and therefore does not need write access, but it needs read access to all the data that will be retrieved from LDAP by the Dynatrace server.
4. Enter the **Password** used by the LDAP user specified in the **Bind DN**.
5. Optional If you've configured referrals on your LDAP server, set **Maximum referral hops**.
6. Select **Test connection** to see if Dynatrace Managed is able to reach your LDAP server. During the connection test

   1. Dynatrace attempts to recognize the type of LDAP server you're using.
   2. Based on the previous step, Dynatrace provides you with the default settings for group and user queries.

When the connection is successful, you're ready to configure groups and users.

* Groups needs to be created manually by the admin.
* Users are created automatically, but only after a successful authentication attempt.

## Groups query configuration

Following a successful connection test, the **Groups query** step becomes active. If you want to use LDAP integration for authentication only (to manage groups and assign permissions in Dynatrace Managed), select the **Assign users to groups automatically based on LDAP query** check box and proceed to [Users query](#users-query-configuration) configuration. Otherwise, follow the steps below.

Example 'Groups query' section

![Groups query settings](https://dt-cdn.net/images/2-groups-query-278-94ee3c12f7.png)

Groups query settings

1. Type query strings into the appropriate fields to return the groups you want to integrate with Dynatrace.

   * The LDAP directory is organized in a tree structure. **Base DN** for the groups query is the entry that contains the subtree in which your groups exist. In the example image below, there are two subtrees containing user groups `OU=Groups,DC=dynatrace,DC=org` and `OU=Lab,DC=dynatrace,DC=org`:

   ![LDAP configuration example](https://dt-cdn.net/images/ldapexample1-275-b06a413d1e.png)

   LDAP configuration example

   If you want to assign users to groups in both subtrees, you should specify the Base DN for the groups query as `DC=dynatrace,DC=org` (the parent entry). To only assign users to groups of the `OU=Lab,DC=dynatrace,DC=org` subtree, specify this subtree as the Base DN.

   * You can type an LDAP **Filter** string to narrow down the number of returned groups. The filter should contain information about which object class the group entries have. For example, for Active Directory the default filter is:

     `(objectClass=group)`

     and for OpenLDAP the default filter is:

     `(objectClass=groupOfNames)`

     To narrow down the number of used groups, you can extend the filter with the group name restrictions. For example, the filter `(&(objectClass=group)(CN=PL_*))` narrows down the groups used by the system to groups that have `group` as an `objectClass` attribute and the `CN` attribute (common name) beginning with `PL_`. You can insert here any other valid LDAP query. Remember that LDAP is case-insensitive.
   * Configure the **Group Id attribute**. This attribute is used only in specific cases. To learn more, check the [Matching users and groups](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap#matching-users-and-groups "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.") section below. If not applicable, set this to the same value as **Group name attribute**.
   * Configure the **Group name attribute**. This is the attribute holding the name of a group, typically called `name` (for example, for Active Directory) or `cn` (for example, for OpenLDAP). The **Group name attribute** values in your LDAP directory should match LDAP group names on the **User groups** page. Remember that LDAP is case-insensitive.

     Example

     If the relevant group entry in your LDAP directory is:

     | Attribute | Value |
     | --- | --- |
     | `name` | `My_TestGroup1` |

     Then configure the following:

     + In Dynatrace, **User authentication** > **User repository** (the **LDAP configuration** page), in the **Groups query** step, set **Group name attribute** to `name` (the name of the attribute)
     + In Dynatrace, **User authentication** > **User groups**, edit or add the group and add `My_TestGroup1` (the value of the attribute) to **LDAP groups**

   LDAP group name on the **User groups** page is by default set to the group name you provide during group creation.

   * Configure the **Group members attribute**. This attribute is covered in detail in the [Matching users and groups](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap#matching-users-and-groups "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.") section below.
2. Select **Test query** to test your settings and verify that the query works.

## Users query configuration

After a successful connection test, the **Users query** step becomes active.

Example 'Users query' section

![Users query settings](https://dt-cdn.net/images/3-users-query-278-51fae6437d.png)

Users query settings

1. Type query strings into the appropriate fields to return the users you want to integrate with Dynatrace.

   * The LDAP directory is organized in a tree structure. **Base DN** for the users query is the entry that contains the subtree in which your users exist. For example, in the image below there are two subtrees holding users:

     `OU=Functional,OU=Accounts,DC=dynatrace,DC=org` and `OU=Primary,OU=Accounts,DC=dynatrace,DC=org`

   ![LDAP configuration example](https://dt-cdn.net/images/ldapexample2-286-fa119f53e5.png)

   LDAP configuration example

   Referring to the example tree above:

   * To authenticate users from both subtrees (`OU=Functional` and `OU=Primary`), set Base DN to the parent entry of those subtrees:  
     `OU=Accounts,DC=dynatrace,DC=org`
   * To authenticate users only from the `OU=Primary` subtree of `OU=Accounts`, set Base DN to:  
     `OU=Primary,OU=Accounts,DC=dynatrace,DC=org`
   * To further restrict system users to the `OU=EU` subtree of `OU=Primary`, set Base DN to:  
     `OU=EU,OU=Primary,OU=Accounts,DC=dynatrace,DC=org`
   * You can type an LDAP **Filter** string to narrow down the number of returned users. The filter should contain information about which object class the group entries have. For example, for Active Directory and OpenLDAP the default filter is:

     `(objectClass=person)`

     To narrow down the number of authenticated users, you can extend the filter with any valid LDAP query. For example, the filter  
     `(&(objectClass=user)(|(department=101)(department=102)(department=103)))`  
     narrows the authenticated users to those having `user` as `objectClass` attribute and `department` attribute set to one of specified values.  
     Remember that LDAP is case-insensitive.
   * Configure the **Login attribute**. This attribute is used to log in to the system.
   * Fine tune the **First name attribute**, **Last name attribute**, and **Email attribute** if the provided attributes don't work for you.
   * Configure the **Group membership attribute**. This attribute is covered in detail in [Matching users and groups](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap#matching-users-and-groups "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.") below.
2. Select **Test query** to test your settings and verify that the query works.

The test query options (for both groups and users) test only the correctness of Base DNs, filters, and mandatory attributes—group name attribute for groups and login attribute for users.

* Test queries don't raise errors when non-mandatory attributes are configured improperly.
* Test queries don't check if users are assigned to groups properly.

## Matching users and groups

There are several ways to match users with groups in LDAP directory servers. Review these examples to find the solution that works best for you.

### Matching example 1

If the **Group members attribute** (for example, `member` or `uniqueMember`) in an LDAP group entry contains the user's DN:

* Configuring **Group Id attribute** isn't necessary. You can configure **Group Id attribute** to the same value as **Group name attribute**.

### Matching example 2

If the **Group membership attribute** (for example, `memberOf` or `isMemberOf`) in a user entry contains the group's DN:

* Configuring the **Group Id attribute** also isn't necessary, because the group's DN is used for user-group matching. You can configure **Group Id attribute** to the same value as **Group name attribute**.

### Matching example 3

If the **Group membership attribute** (for example, `gid` or `group`) in a user entry contains the group's ID:

* **Group Id attribute** must be configured to the attribute that stores the referenced value.

**Example group entry in LDAP directory:**

| Attribute | Value |
| --- | --- |
| `gidNumber` | `6380` |

**Example user entry in LDAP directory:**

| Attribute | Value |
| --- | --- |
| `gid` | `6380` |

Then:

* **Group Id attribute** (in **Groups query**) should be configured to `gidNumber`
* **Group membership attribute** (in **Users query**) should be configured to `gid`

## Map Dynatrace Managed groups to LDAP groups

For information regarding the user group permissions that are available in Dynatrace Managed, see [User groups and permissions](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups.").

After you've successfully configured groups and users from LDAP, you need to assign monitoring environment roles to the groups from your user directory. By default, no monitoring environment permissions are granted to imported groups.

Users won't be able to access a monitoring environment until you perform this step.

1. Select **User authentication** > **User groups**.
2. From the list of groups imported from LDAP, select the group names you want to configure.
3. You can assign cluster administrator rights to any specific group by enabling **Grant global administrator permissions to this group**. All user accounts within this group will then have administrator rights.
4. In the **Permissions** section, manually set the permissions for each environment.

## Limitations

Dynatrace does not support multiple domains for LDAP user authentication.