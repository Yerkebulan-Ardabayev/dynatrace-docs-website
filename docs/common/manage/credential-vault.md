---
title: "Credential vault"
source: https://docs.dynatrace.com/docs/manage/credential-vault
updated: 2026-02-09
---

# Credential vault

# Credential vault

* Latest Dynatrace
* Tutorial
* 21-min read
* Updated on Sep 27, 2024

The credential vault is a centralized repository where you securely store and manage credentials (username-password pairs, certificates, or tokens) used by synthetic monitors ([browser](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") and [HTTP](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors#http-monitor "Learn about Dynatrace synthetic monitor types.")), [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."), and AppEngine apps.

To access the credential vault, go to **Credential Vault**.

## Credential security

Credentials are stored in Advanced Encryption Standardâencrypted form (AES-256) in the credential vault. Access to the data is encrypted using TLS 1.3. The contents of credentials in the vault are not visible to any user, including the creator; they are visible only to the synthetic monitors that reference them. Users with [access to the credential vault](#access-cv) can overwrite some or all credentialsâcheck [Who can edit or overwrite a credential](#overwrite-credential) for details on overwriting credentials.

Credential vault security architecture and communication

The **credential vault** is developed entirely by Dynatrace and resides on the Dynatrace Cluster. See the key Synthetic Monitoring components involved in credential vault security and communication below. All communication among key components is encrypted.

![Credential vault communication](https://dt-cdn.net/images/cvsecurityarch-476-4c11d31bd2.png)

* **Dynatrace Cluster**

  **Function**: The Dynatrace Cluster hosts the credential vault in the cluster database as part of your Dynatrace monitoring environment.

  **Credential access and security**: All credentials are created, changed, and deleted on the Dynatrace Cluster. The credential vault is environment-specific and is not shared across environments. Only the cluster has access to the credential vault and resolves credential IDs to actual values when preparing monitors for execution.

  **Communication**: All communication among key components is encrypted. If a monitor needs to be executed from a private Synthetic location, the cluster resolves and sends credentials as part of the monitor configuration to the Synthetic engine on creation and update (when monitors or referenced credentials are created or updated), not before every execution. In the same way, if a monitor needs to be executed from a public Synthetic location, the cluster resolves and sends credentials as part of the monitor configuration to the public Synthetic infrastructure on creation or update.
* **Synthetic engine**

  **Function**: The Synthetic engine executes synthetic monitors on both [private](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") and [public Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") and has access to monitor configurations and any resolved credentials in order to do so.

  **Communication**: The Synthetic engine does not communicate directly with the credential vault or see its contents. On private Synthetic locations, the Synthetic engine requests and retrieves the schedule of monitors to be executed and their configurations (with resolved credentials) from the Dynatrace Cluster on creation or update, that is, when monitors or referenced credentials are created or updated. On public Synthetic locations, this same communication takes place with the public Synthetic infrastructure. All communication among key components is encrypted.

  **Credential access and security**: The Synthetic engine has access only to those resolved credentials that are part of the monitors it needs to execute; it can't retrieve or view any other credentials. All monitor configurations are stored in Synthetic engine memory (with no persistence layers involved) for as long as the monitors need to be executed. If a monitor is turned off or deleted, its configuration is flushed from Synthetic engine memory.

  All credential data is exchanged via internal API secured with API token, and access is highly restricted at the network-protocol level. Each individual monitor execution is isolated; no memory or scripts are shared among executions.
* **Public Synthetic infrastructure**

  **Function**: This includes all infrastructure required to execute monitors from public locations. The public Synthetic infrastructure stores and communicates information to public Synthetic locations for the execution of synthetic monitors.

  **Communication**: If a monitor needs to be executed from a public Synthetic location, the Dynatrace Cluster sends the monitor configuration (with resolved credentials) to the public Synthetic infrastructure on creation or update (when monitors or referenced credentials are created or updated), not before every execution. The public Synthetic infrastructure then serves the same information to public Synthetic locations as the cluster does to private Synthetic locations. All communication among key components is encrypted.

  **Credential access and security**: Monitor configurations with resolved credentials are encrypted and persisted in the Synthetic database. Credentials aren't persisted directly as credentials but only as part of monitor configurations.

  Dynatrace manages and secures the entire public Synthetic infrastructure and public Synthetic locations. Access is only possible from within the Dynatrace corporate network and is secured by SSH key-based authentication. Access to private keys is limited to a small group of Dynatrace employees.

### Access to the credential vault

To view and write to the credential vault, a user requires the **View environment** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment level.

If you have only the **View environment** permission (and no other higher permission such as **Change monitoring settings**), you can:

* View the credential vault.
* View all "public" and any "owner only" credentials that you own.
* Create credentials within the credential vault. However, you are not allowed to use [external vault synchronization](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").
* Overwrite any credentials (public or owner only) that you own; you are not allowed to overwrite credentials owned by another user.
* Delete any credentials (public or owner only) that you own; you are not allowed to delete credentials owned by another user.

To overwrite and delete credentials owned by other users, you require the **Change monitoring settings** permission at the environment level.

Users with **View environment** or **Change monitoring settings** at the management-zone level can only view public credentials in the vault; they can't create credentials in the vault.

To create or edit synthetic monitors, you require the **Change monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment or management-zone level.

See [Credential vault API](#cv-api) below for the token scope required to access the credential vault via API.

### Owner-only, shared, and public credentials

Each credential has access levels. When a credential is initially created (in the vault or when creating or editing a synthetic monitor), it's designated as **Owner only**.

The owner of a credential may turn off the **Owner access only** toggle in the vault to change a credential's access level to **All**. The owner may also limit access to the credential to specified users by providing a comma-separated list of usernames (which can include email addresses set as usernames) in **Users with access**, for example, `username1, username2, userx@company.com`. The credential's access level is then set to **Shared**.

To give other users access to your credential, turn off **Owner access only**. If you turn off **Owner access only** and don't limit credential access to the usernames listed in **Users with access**, the credential is accessible to all users.

Other users can change a credential's access level by becoming the new owner of the credential and overwriting it with new authentication details.

Users with the **View environment** permission at the environment level can only overwrite credentials they own.

A credential's access level (**Owner only**, **Shared**, or **All**) determines who can use it in a synthetic monitor. An owner-only credential is one that only the credential owner can use, for example, to create or edit a synthetic monitor. A shared credential is available to the specified user list for use, for example, in synthetic monitors and apps. A public credential is available to all users.

Read more below in [Work with credentials](#work-with-credentials).

## Credential scopes

A credential scope represents the use case for a credential; you can select multiple scopes at once. The table below describes each scope and the credential types it applies to.

Scope

Credential types

Description

**Synthetic**

* User and password
* Certificate
* Token

For credentials to be used in synthetic monitors

**Extension authentication**

* User and password

Credentials used by extensions (data sources) to authenticate to a resource and retrieve data

**Extension validation**

* Public certificate

Used to sign extensions

**AppEngine**

* User and password
* Certificate
* Token
* Public certificate

To provide access to credentials from Dynatrace apps ([latest Dynatrace](/docs/discover-dynatrace/get-started/dynatrace-ui "Navigate the latest Dynatrace")) and ad hoc functions (without app context)

### AppEngine scope

Select the **AppEngine** scope to permit built-in apps from the latest Dynatrace to access a credential. This scope is available for all credential types.

When you first select the scope for a credential, the access defaults to **All applications** in **Dynatrace apps with access**.

![AppEngine scope default value](https://dt-cdn.net/images/cv-appengine-scope-default-801-8ce4bbdea2.webp)

To limit credential access to specific apps, place your cursor in the field to select from a list of available built-in apps in your environment. You can select multiple apps, one at a time. Credential access is now limited to the apps you select.

![AppEngine scope selected apps](https://dt-cdn.net/images/cv-appengine-scope-apps-871-24f162d410.webp)

Optionally, turn on **Allow access without app context**. This allows ad hoc functions, for example, from Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks"), to access your credential outside the context of an app.

App and user access interaction

For a credential to be accessible by a user within the context of an app, both the user and the app must have access to the credential separately. Both user and app access are validated, so if user X has access to the credential but app A does not, user X can't use the credentials from app A.

## View the credential vault

Go to **Credential Vault** to see all the credentials in your environment.

Users with the **View environment** permission at the environment level can only view public credentials and credentials they own.

The available credential types for synthetic monitoring are [username-password pairs](#uid-password), [certificates](#certificate), and [tokens](#token). Username-password pairs can be synchronized with external vault systemsâread more in [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").

Each credential is listed with an icon identifying the **Type**, **Name**, the monitors it's **Used by**, **Owner**, **Access** level, **Scope**, and controls to edit and **Delete** it.

You can filter the list by **Type**, **Name**, **Access**, **Owner**, or **Scope** (select **Synthetic**).

![Credential vault](https://dt-cdn.net/images/credential-vault-ui-1917-49ef8dcfb2.webp)

You can see the ID and properties of a credential, but credential content can't be viewed; it can only be overwritten. The contents of credentials are visible only to the synthetic monitors, apps, or ad hoc functions referencing them.

If you don't have access to a credential, you'll see a message about using or overwriting the credential. See [Who can edit or overwrite a credential](#overwrite-credential) below.

Select **HTTP** or **Browser** next to a credential to see the associated monitors on the **Synthetic** page. The list is automatically filtered by the credential name and owner.

![Credential associated monitors](https://dt-cdn.net/images/play-back-clickpath-credentials-2459-e8db1f6bbe.webp)

Optional **Turn on local playback of Synthetic browser monitors without entering credentials** so that your users can play back browser clickpaths locally without having to enter any associated tokens or username-password pairs that they have access to. If turned off, the user needs to enter associated credentials in order to play back browser clickpaths locally. Note that only users with access to the credentials in a browser clickpath can play it back.

![Play back clickpath with credentials](https://dt-cdn.net/images/playback-clickpath-credentials-1920-6aba6235d4.webp)

## Create credentials in the vault

You can create credentials directly in the vault or in the course of synthetic monitor creation and editing.

You can create the following types of credentials for synthetic monitoring.

* [Username and password pairs](#uid-password)
* [Certificate credentials](#certificate)
* [Token credentials](#token)

### Username and password pairs

Username and password pairs can be used for basic as well as web-form authentication, in [single-URL browser monitors](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site."), [browser clickpaths](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application."), and [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.").

Username-password pairs in the Dynatrace credential vault can be synchronized with an external vault (Azure Key Vault, HashiCorp Vault, or CyberArk Vault). Synthetic monitors containing these credentials use the synchronized values obtained from the external vaultsâread more in [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").

To create login credentials in the vault

1. Select **Add new credential** in the upper-right corner.
2. Select **User and password** as the **Credential type**.
3. Select **Synthetic** for **Credential scope**. Read more about other [Credential scopes](#credential-scopes), including the [AppEngine scope](#appengine-scope).
4. Edit the default **Credential name** to identify your new credential properly.
5. If synchronizing this username-password pair with an external vault (**Synchronization with external vault**), follow the instructions in [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").
6. Enter the **Username** and **Password**. The password is automatically masked as you type. Note that these fields don't appear for [synchronized credentials](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").

   Supported username formats

   * Browser monitors: `<username>` and `<domain>\<username>`
   * HTTP monitors: `<username>`
   * **NTLM authentication** in browser and HTTP monitors: `<username>`
7. Optional Provide a **Description**.
8. Credentials are set to **Owner access only** by default. Turn off this toggle to make the credential accessible to other users. Optionally, limit access to the credential to specified users by providing a comma-separated list of usernames in **Users with access**. Read more in [Owner-only, shared, and public credentials](#owner-shared-public) and [Work with credentials](#work-with-credentials).
9. **Save** your credential. Note that once created, the contents of credentials can only be overwritten.

![Create a username-password pair in the vault](https://dt-cdn.net/images/cv-create-uid-password-840-b7bc54f0b8.webp)

### Certificate credentials

Certificate credentials are used in HTTP monitorsâ[you can add a client certificate to an HTTP request](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#http-additional-options "Learn about configuring HTTP monitors.").

To create a certificate credential in the vault

1. Select **Add new credential** in the upper-right corner.
2. Select **Certificate** as the **Credential type**.
3. Select **Synthetic** for **Credential scope**. Read more about other [Credential scopes](#credential-scopes), including the [AppEngine scope](#appengine-scope).
4. **Upload** ![Upload](https://dt-cdn.net/images/uploadcertificateicon-32-1f39daa6ad.png "Upload") a **Certificate file**. Allowed file formats are PFX, P12, and PEM.

   If you run into issues with using a PEM certificate, see [Convert PEM certificates](#certificate-pem) below.
5. Enter the **Certificate password**.
6. Provide a **Credential name** and optional **Description**.
7. Credentials are set to **Owner access only** by default. Turn off this toggle to make the credential accessible to other users. Optionally, limit access to the credential to specified users by providing a comma-separated list of usernames in **Users with access**. Read more in [Owner-only, shared, and public credentials](#owner-shared-public) and [Work with credentials](#work-with-credentials).
8. **Save** your credential. Note that once created, the contents of credentials can only be overwritten.

#### Convert PEM certificates

If you run into issues when creating a credential using a PEM certificate, consider converting the certificate file to the P12 or PFX formats, which are endorsed for Java standards.

Use the `openssl` command-line utility to convert the certificate file. For example, the following command converts a PEM certificate to the P12 format.

```
openssl pkcs12 -export -in /path/to/certificate.pem -out /path/to/certificate.p12
```

### Token credentials

A token is a generic credential type with a single value. You can create tokens in the credential vault and insert references to them from [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.")âin request URLs, HTTP header values, and in the request body. In [clickpaths](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site."), you can insert a token ID in the [Keystroke event](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#keystroke "Learn about the event types created when recording a browser clickpath.").

Token credentials in the Dynatrace credential vault can be synchronized with an external vault (Azure Key Vault or HashiCorp Vault). Synthetic monitors containing these credentials use the synchronized values obtained from the external vaultsâread more in [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").

To create a token credential in the credential vault

1. Select **Add new credential** in the upper-right corner.
2. Select **Token** as the **Credential type**.
3. Select **Synthetic** for **Credential scope**. Read more about other [Credential scopes](#credential-scopes), including the [AppEngine scope](#appengine-scope).
4. If synchronizing this token with an external vault (**Synchronization with external vault**), follow the instructions in [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.").
5. Enter a **Token** value.
6. Provide a **Credential name** and optional **Description**.
7. Credentials are set to **Owner access only** by default. Turn off this toggle to make the credential accessible to other users. Optionally, limit access to the credential to specified users by providing a comma-separated list of usernames in **Users with access**. Read more in [Owner-only, shared, and public credentials](#owner-shared-public) and [Work with credentials](#work-with-credentials).
8. **Save** your credential. Note that once created, the contents of credentials can only be overwritten.

![Create a token credential in the vault](https://dt-cdn.net/images/cv-token-create-840-e34e842119.webp)

## Work with credentials

The access level of a credential ([owner only or public](#owner-shared-public)) determines who can use the credential to:

* [Create a new synthetic monitor or associate an existing monitor with the credential](#use-credential-in-monitor).
* [Edit a monitor that has an associated credential](#edit-monitor-with-credential).

Users can [delete/overwrite](#overwrite-credential) credentials and change credential access levels.

### Who can use a credential in a monitor

These operations require the **Change monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

When creating a monitor or editing an existing monitor that doesn't have associated credentials, you can:

* Use an existing credential stored in the vault in the monitorâyou can select public credentials or credentials that you own or are shared with you.
* Create a new credential as part of the monitor creation/editing workflow. The credential is automatically designated as owner only and stored in the vault. After you create a credential, note that another user may change a credential's access level by becoming the new owner and overwriting it with new authentication details.

* You can store passwords captured in recorded clickpaths to the vault (with a companion username or as a single-value token). These are stored as owner only. See how to use the [Keystroke event](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#keystroke "Learn about the event types created when recording a browser clickpath.").

  Alternatively, you can edit the recorded event to use an existing credential from the vault or create one of your own from within the clickpath.

### Who can edit a monitor that has an associated credential

These operations require the **Change monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

* If a monitor is associated with a public credential, anyone on your team can switch on/off, delete, or edit the monitor.

* You can turn on/turn off or delete a synthetic monitor secured by another user's owner-only or shared credentials.

* If a browser monitor (clickpath or single URL) is associated with a restricted credential (owner only or shared with a few users), any user can make changes to certain fields, even if they don't have access to the credential used. You can edit monitor name, device emulation settings, wait conditions, frequency, locations, outage alerting, performance thresholds, metrics, connected applications, validation, and HTTP status codes to be ignored. And, of course, you can change a token or user ID/password credential. You can create a credential within monitor settings in edit mode. You'll need to change all credentials in the monitor to ones that you have access to. Note that replacing another user's credential with one you have access to is irreversible.

  Controls that you cannot editâsuch as the URL, switching on/off HTTP authentication, adding or deleting clickpath events, data entry in Keystroke, and **Advanced setup** in monitor settingsâare grayed out or display an error message when you attempt to save changes, whether in script or UI mode.

* If an HTTP monitor is associated with restricted credential (owner only or shared with a few users), any user can make changes to certain fields, even if they don't have access to the credential used. You can edit monitor name, locations, validation, thresholds, and, of course, change a certificate or a UID/password pair. You can edit and change the credentials in a URL, header value, or request body. You can create a credential within monitor settings in edit mode. You'll need to change all credentials in the monitor to ones that you have access to. Note that replacing another user's credential with one you have access to is irreversible.

  Controls that you cannot edit such as the request URL, HTTP method, pre-execution script, post-execution script, HTTP headers, request body, the follow redirects option, and adding/deleting HTTP requests are grayed out or display an error message when you attempt to save changes, whether in script or UI mode.

If you're unable to edit a monitor that has an associated credential, you can [search for the credential owner](#owner-credential) to discuss changes or request access. You can also overwrite another user's credential.

### Who can edit or overwrite a credential

The contents of credentials are visible only to the synthetic monitors, apps, or ad hoc functions referencing them. You can see the ID and properties of a credential in the vault, but **the credential content can only be overwritten**.

Users with the **Change monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment level can overwrite another user's credential, and, thereby, take over ownership. In the course of overwriting (or anytime after), they can then also change the access level of the credential (whether shared, public, or owner only).

Users with the **View environment** permission at the environment level can only overwrite or delete credentials they own.

Select a credential and select **Overwrite credential** or **Overwrite certificate**.

In order to overwrite a credential, you need to provide the full set of authentication details. This means that you can only overwrite a credential (and take ownership) by providing a new username-password pair, a new certificate, or a new token. In the case of username-password pairs, if you leave the password blank, the old password value is not retained.

![Overwrite a credential](https://dt-cdn.net/images/cv-overwrite-credentials-2345-8f45446880.webp)

* Credential owners can change authentication details and/or access level of a credential.
* If you are not the owner of a credential:

  + You see a cautionary message about using or overwriting the credential.
  + You become the new owner of a credential if you overwrite it. You might want to notify the previous owner in this case.
  + You can change a credential's access level only by overwriting it completely with new authentication details and becoming the new owner.

Users with the **Change environment settings** permission at the environment level can delete another user's credentialsâif you delete a credential that's used in a monitor, that monitor becomes inactive.

![Delete a credential](https://dt-cdn.net/images/cv-delete-credential-1575-6c705c7d83.webp)

### How to search for the owner of a credential

The credential vault displays all credentials in your environment with owner name and access level. You can sort and filter credentials by **Owner** in the credential vault.

You can search for credential owners in **Synthetic Classic**. You can filter for monitors using a specific credential (**Associated credential**) and/or the credential owners (**Associated credential owner**). Note that these filters are only available when at least one credential from the vault is used in a monitor. The filters show you all the credentials (and their owners) currently used in monitors.

When you open a monitor using an owner-only or shared credential, the owner's name is highlighted.

![Credential owner in an HTTP monitor](https://dt-cdn.net/images/credential-owner-http-monitor-1749-b06ab2b529.webp)

## Credential vault API

You can access the [credential vault by API](/docs/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers."), which lends itself to a vast range of automation use cases.

* Reading the credential vault requires the **Read credential vault entries** API token scope. You can also use the broader **Read configuration** token scope.
* Writing to the credential vault requires the **Write credential vault entries** API token scope. You can also use the broader **Write configuration** token scope. Note that write scopes don't include read scopes, which must be granted separately (see above).
* Updating synthetic monitors via API requires the **Create and read synthetic monitors, locations, and nodes** API token scope.
* If you use the API to edit or update a monitor with a credential, the API token should be owned by someone who has access to the credentials assigned to the monitor.

Read more about token scopes in the [API authentication Documentation topic](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Best practices for credentials

* **We recommend that you use dedicated test credentials for synthetic monitors**.
* If many people need to [edit a synthetic monitor with credentials](#edit-monitor-with-credential), it's better to make the associated credential public.
* If the account of a credential owner no longer exists in your system, the execution of associated synthetic monitors is not affected; the monitors continue to be executed as before. However, we recommend that the credential be [overwritten](#overwrite-credential) by another user, making them the new owner. Without doing so, you will not be able to [use owner-only credentials in new monitors](#use-credential-in-monitor), or [edit existing monitors](#edit-monitor-with-credential) that have owner-only credentials.
* If you [overwrite](#overwrite-credential) a credential, notify the previous owner. If you delete a credential, notify the owner.
* If you use the [API](#cv-api) to edit or update a monitor with a credential, the API token should be owned by someone who has access to the credentials assigned to the monitor.
* Whenever possible, use the [narrow API token scopes](#cv-api) limiting read and write access to just the credential vault.

## Related topics

* [Sign extensions](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.")
* [WMI data source tutorial](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Learn about WMI extensions in the Extensions framework.")
