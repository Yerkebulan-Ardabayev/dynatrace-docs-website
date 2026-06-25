---
title: Manage users and groups with OpenID in Dynatrace Managed
source: https://docs.dynatrace.com/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid
scraped: 2026-05-12T11:24:25.249468
---

# Manage users and groups with OpenID in Dynatrace Managed

# Manage users and groups with OpenID in Dynatrace Managed

* Published Jul 17, 2018

Dynatrace Managed supports integration with [OpenIDï»¿](https://openid.net/what-is-openid/) as an SSO IdP (Single Sign-On Identity Provider) for the management of users and groups. We support standard claims (email, profile, address) as defined in the [OpenID Connect Core 1.0 specificationï»¿](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims).

## Configure redirect\_uri

The `redirect_uri` used for authentication is set to:

* `https://{dynatrace-server}/`  
  when you open Cluster Management Console.
  To check the value of 'Dynatrace Web UI URL'

  1. Select the User icon in the upper-right corner and select **Cluster Management**.
  2. Select **Settings > Public endpoints** and see **Dynatrace Web UI URL**.
* `https://{dynatrace-server}/e/{environment-uuid}`  
  when you open an environment.

You need to configure these URIs in your OpenID provider's client:

* Configure one URI for Cluster Management Console.
* Configure one URI per environment or use a wildcard (`https://{dynatrace-server}/e/*`) to match all environment URIs.

## Set up OpenID integration

1. In the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Navigate the Dynatrace Managed platform"), go to **Cluster Management**.
2. Select **User authentication** > **Single sign-on settings**.
3. In **Select single sign-on technology**, select **OpenID Connect**.
4. From **Select login page**, select the login options you want to offer users:

   * **Standard + SSO** displays the standard Dynatrace login page, where the user has the choice to sign in using a local user account (as configured through **User authentication > User accounts**) or to select the **Log in using SSO** link and use SSO authentication.
   * **SSO** skips the Dynatrace login page, so the user cannot sign in using a local user account, and redirects to the IdP login page for SSO authentication only.
5. Enter the **Client ID** and **Client Secret** of the client from the IdP that will be used for authentication.
6. To use an internet proxy to connect to your IdP, select **Use internet proxy for connection to IdP**.
7. To validate the ID token and UserInfo signature, select **Validate signature**.
8. In **Server discovery endpoint**, enter the OpenID configuration URL provided by the IdP and select **Import Configuration**.  
   If the import is successful, the **Save changes** button is enabled. Save the configuration.

## Group assignment configuration

Each Dynatrace Managed user must be assigned to at least one user group, with at least one associated [monitoring environment](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). Without such a mapping, the user can't sign in to Dynatrace Managed and will receive an error message stating that no environment has been found.

The **Assign users to groups based on UserInfo response attribute** switch determines how you manage user-group assignments:

* **Manually**: Turn the switch off if you want to make user-group assignments manually from within Dynatrace Managed. In this case, Dynatrace Managed ignores the list of groups sent in your IdP's authentication response.
* **Automatically**: Turn the switch on and enter the group name in the **User groups** attribute field if you want to handle user-group assignment automatically. In this case, any assignments made within Dynatrace Managed are overwritten by the list of groups sent in your IdP's authentication response. You can add a custom user groups separator to separate user groups.