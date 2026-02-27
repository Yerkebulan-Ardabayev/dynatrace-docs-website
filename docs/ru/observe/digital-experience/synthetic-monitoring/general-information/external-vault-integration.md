---
title: External vault integration
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration
scraped: 2026-02-27T21:27:58.336661
---

# External vault integration

# External vault integration

* How-to guide
* 22-min read
* Updated on Jan 17, 2024

Synthetic Monitoring [username-password](/docs/manage/credential-vault#uid-password "Store and manage credentials in the credential vault.") and [token](/docs/manage/credential-vault#token "Store and manage credentials in the credential vault.") credentials in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") can be synchronized with an external vaultâ[Azure Key Vault](#azure-key-vault), [HashiCorp Vault](#hashicorp), or [CyberArk Vault](#cyberark) (username-password credentials only). Synchronized credentials contain the keys of external key-value pairs that hold the required values.

When you set up synchronized credentials in the credential vault, Dynatrace automatically creates [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") specifically for the purpose of synchronization. You can also use the `api.saveCredential()` or `api.saveToken()` methods in [pre-and post-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") to create your own synchronization monitors.

Autocreated synchronization monitors are named with the credential ID of the synchronized credential and are executed hourly by default from the Amazon US East (N. Virginia) [public Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations."). Note that the request and response bodies and headers of synchronization monitors are automatically hidden from execution details (**Analyze execution details**).

Other synthetic monitors can call and use these synchronized credentials for testing API endpoints and websites. The monitors that call these credentials use the synchronized values obtained from the external vaults. Synchronization frequency determines how often these credentials are rotated within the synthetic monitors that call them.

Synchronization process reads the credentials from external vault and saves a copy within the Dynatrace vault.

## Azure Key Vault

Username-password or token credentials for use in synthetic monitors can be synchronized with Azure Key Vault key-value pairs containing the username, password, or token value.

### Prerequisites

Before setting up credentials synchronized with Azure Key Vault, you need to define the required **client (application) ID** and **client secret** as [token credentials](/docs/manage/credential-vault#token "Store and manage credentials in the credential vault.") stored in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."). We recommend naming such prerequisite tokens so that they're easily identifiable as companion credentials for synchronization. If your vault doesn't contain any tokens that you have access to, you'll see a warning.

### Set up synchronized credentials

1. In the credential vault, create a **User and password** or **Token** credential. You can also overwrite an existing credential.
2. For **Credential scope**, select **Synthetic**.
3. Turn on **Synchronization with external vault**.
4. Select **Azure Key Vault** (default) as the **Credential source**.
5. We recommend editing the default **Credential name** to easily identify your new credential.
6. Enter the URL to access the vault (**Vault URL**) and the **Tenant (directory) ID**.
7. Select the [companion tokens](#azure-prereqs) created earlier for the **Client (application) ID** and **Client secret**.
8. Enter the name of the Azure Key Vault key.

   Username-password credentials

   Token credentials

   * In **Secret name for username**, enter the name of the Azure Key Vault key mapped to the username value; do not enter an actual username.
   * In **Secret name for password**, enter the name of the Azure Key Vault key mapped to the password value; do not enter an actual password.

   * In **Secret name for token**, enter the name of the Azure Key Vault key mapped to the token value; do not enter an actual token value.
9. Select a **Location for synchronization**âyou can select any public or private Synthetic location for [synchronization monitor](#azure-monitor) execution. You can search for a location by entering the location name in the field.
10. Optional Provide a **Description** for the credential.
11. Credentials are set to **Owner access only** by default. (Read more about [credential ownership](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.").)
12. **Save** your credential.

See also [Best practices](#best-practices) and what happens when you [edit or delete synchronized and companion credentials](#edit-delete-credential).

![Set up Azure synchronization - token](https://dt-cdn.net/images/cv-azure-token-1113-f0f69b54d9.webp)

### Azure Key Vault synchronization monitors



When you have [set up your synchronized username-password or token credential](#azure-set-up), Dynatrace automatically creates and executes an [HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") that synchronizes the credential with Azure Key Vault. This monitor is automatically associated with the synchronized username-password or token credential.

See also [Best practices](#best-practices) and what happens when you [edit or delete synchronization credentials](#edit-delete-credential).

Username-password credentials

Token credentials

The synchronization monitor contains three requests. Azure Key Vault requires splitting the retrieval of the username and password into two separate requests.

1. The first request (POST) fetches an access token.
   Request configuration details

   * The request URL references the tenant ID as an attribute of the [synchronized credential](#azure-set-up) defined above; the tenant ID is not displayed.

     ![Azure KV request 1 URL](https://dt-cdn.net/images/cvazurerequest1url-1446-eed3251a4d.png)
   * The client ID and client secret, referenced as attributes of the synchronized credential, are passed as key-value pairs in the [request body](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Learn about configuring HTTP monitors."); the client ID and client secret are not displayed.

     ![Azure KV request 1 request body](https://dt-cdn.net/images/cvazurerequest1requestbody-984-7631f538d2.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![Azure KV request 1 post script](https://dt-cdn.net/images/cvazurerequest1postscript-962-26b361836f.png)
2. The second request (GET) fetches the username value.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#azure-set-up) defined above; the vault URL is not displayed. The request URL also references the key mapped to the username value in Azure Key Vault.

     ![Azure KV request 2 URL](https://dt-cdn.net/images/cvazurerequest2url-1775-b114ec0406.png)
   * The [Authorization header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the access token retrieved in the first request.

     ![Azure KV request 2 request header](https://dt-cdn.net/images/cvazurerequest2authheader-964-9fb3850f7d.png)
   * The username value is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the value in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![Azure KV request 2 post script](https://dt-cdn.net/images/cvazurerequest2postscript-962-8bccc9e09c.png)
3. The third request (GET) fetches the password value. It also uses `api.saveCredential()` in a post-execution script to write the fetched values to the [synchronized username-password credential](#azure-set-up) defined above.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#azure-set-up); the vault URL is not displayed. The request URL also references the key mapped to the password value in Azure Key Vault.

     ![Azure KV request 3 URL](https://dt-cdn.net/images/cvazurerequest3url-1777-8a113269d0.png)
   * The [Authorization header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the access token retrieved in the first request.
   * The password value is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the value in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveCredential()` to write the retrieved values to the synchronized username-password credential.

     ![Azure KV request 3 post script](https://dt-cdn.net/images/cvazurerequest3postscript-962-b44c6bda2a.png)

The synchronization monitor contains two requests.

1. The first request (POST) fetches an access token.
   Request configuration details

   * The request URL references the tenant ID, which is stored as an attribute of the [synchronized credential](#azure-set-up) defined above; the tenant ID is not displayed.

     ![Azure KV request 1 URL](https://dt-cdn.net/images/cv-azure-token-request1-url-1446-9fd964d06c.png)
   * The client ID and client secret, referenced as attributes of the synchronized credential, are passed as key-value pairs in the [request body](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Learn about configuring HTTP monitors."); the client ID and client secret are not displayed.

     ![Azure KV request 1 request body](https://dt-cdn.net/images/cvazurerequest1requestbody-984-7631f538d2.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![Azure KV request 1 post script](https://dt-cdn.net/images/cvazurerequest1postscript-962-26b361836f.png)
2. The second request (GET) fetches the token value.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#azure-set-up) defined above; the vault URL is not displayed. The request URL also references the key mapped to the token value in Azure Key Vault.

     ![Azure KV request 2 URL](https://dt-cdn.net/images/cv-azure-token-request2-url-1770-f949f51173.png)
   * The [Authorization header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the access token retrieved in the first request.

     ![Azure KV request 2 request header](https://dt-cdn.net/images/cvazurerequest2authheader-964-9fb3850f7d.png)
   * The token value is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the value in a variable. It also uses `api.saveToken()` in a post-execution script to write the retrieved value to the synchronized token credential.

     ![Azure KV request 2 post script](https://dt-cdn.net/images/cv-azure-token-request2-post-script-961-337899fa61.png)

## HashiCorp Vault

[Username-password or token credentials](#hashicorp-set-up) for use in synthetic monitors can be synchronized with HashiCorp Vault key-value pairs containing the username, password, or token value. You can use either **[AppRole-based](#app-role) or [certificate authentication](#certificate)**.

### Prerequisites

* Before using [AppRole-based authentication](#app-role), you need to define the required **secret ID** as a [token credential](/docs/manage/credential-vault#token "Store and manage credentials in the credential vault.") stored in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."); do not reuse other tokens as the secret ID. If your vault doesn't contain any tokens you have access to, you'll see a warning.
* Before using [certificate authentication](#certificate), you need to store the required **TLS [certificate](/docs/manage/credential-vault#certificate "Store and manage credentials in the credential vault.")** in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."). If your vault doesn't contain any certificates you have access to, you'll see a warning.

We recommend naming such prerequisite tokens and certificates so that they're easily identifiable as companion credentials for synchronization.

### Set up synchronized credentials



1. In the credential vault, create a **User and password** or **Token** credential. You can also overwrite an existing credential.
2. For **Credential scope**, select **Synthetic**.
3. Turn on **Synchronization with external vault**.
4. Select **HashiCorp Vault** as the **Credential source**.
5. We recommend editing the default **Credential name** to easily identify your new credential.
6. Enter the URL to access the vault (**Vault URL**) and the **Path to credentials** (folders must be separated by a forward slash).

   The HashiCorp **Vault URL** for certificate authentication might be different from that used for AppRole-based authentication.
7. Enter the name of the HashiCorp Vault key.

   Username-password credentials

   Token credentials

   * In **Secret name for username**, enter the name of the HashiCorp Vault key mapped to the username value; do not enter an actual username.
   * In **Secret name for password**, enter the name of the HashiCorp Vault key mapped to the password value; do not enter an actual password.

   * In **Secret name for token**, enter the name of the HashiCorp Vault key mapped to the token value; do not enter an actual token value.
8. Perform steps related to **Authentication method**.

   AppRole

   Certificate

   1. Select **AppRole** for the **Authentication method**.
   2. Enter the string provided by HashiCorp in **Role ID**.
   3. Select the [companion token](#hashicorp-prereqs) created earlier for the **Secret ID**.
   4. Enter the **Vault namespace**.

   ![Set up HashiCorp AppRole synchronization - token](https://dt-cdn.net/images/cv-hashicorp-approle-token-1113-2263da2bbc.webp)

   5. Select **Certificate** for the **Authentication method**.
   6. For **Certificate**, select the [companion TLS certificate](#hashicorp-prereqs) created earlier.

   ![Set up HashiCorp certificate synchronization - UID](https://dt-cdn.net/images/cv-hashicorp-certificate-uid-1113-8b177811b5.webp)
9. Select a **Location for synchronization**âyou can select any public or private Synthetic location for synchronization monitor execution. You can search for a location by entering the location name in the field.
10. Optional Provide a **Description**.
11. Credentials are set to **Owner access only** by default. (Read more about [credential ownership](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.").)
12. **Save** your credential.

See also [Best practices](#best-practices) and what happens when you [edit or delete synchronized and companion credentials](#edit-delete-credential).

When you have set up your synchronized credential, Dynatrace automatically creates and executes an [HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") that synchronizes the credential with HashiCorp Vault.

### HashiCorp Vault AppRole synchronization monitors



The autocreated HTTP monitor contains two requests and is automatically associated with the [synchronized credential](#hashicorp-set-up) defined above.

Username-password credentials

Token credentials

1. The first request (POST) fetches a client token.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#hashicorp-set-up); the vault URL is not displayed. The request URL also contains the authentication method `approle`.

     ![HashiCorp AppRole request 1 URL](https://dt-cdn.net/images/cvhashiapprolerequest1url-1447-20b5ca2512.png)
   * The vault namespace, referenced as an attribute of the synchronized credential, is passed as a [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors."); the vault namespace is not displayed.

     ![HashiCorp AppRole request 1 header](https://dt-cdn.net/images/cvhashiapprolerequest1requestheader-964-7efd88a7af.png)
   * The role ID and secret ID, referenced as attributes of the synchronized credential, are passed as key-value pairs in the [request body](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Learn about configuring HTTP monitors."); the role ID and secret ID are not displayed.

     ![HashiCorp AppRole request 1 body](https://dt-cdn.net/images/cvhashiapprolerequest1requestbody-966-5eb6ad4427.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![HashiCorp AppRole request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)
2. The second request (GET) fetches the username and password values. It also uses `api.saveCredential()` in s post-execution script to write the fetched values to the [synchronized username-password credential](#hashicorp-set-up) defined above.
   Request configuration details

   * The request URL references the vault URL and the path to credentials as attributes of the synchronized credential; the vault URL and path to credentials are not displayed.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)
   * A [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the client token retrieved in the first request. The vault namespace (not displayed, but referenced as an attribute of the synchronized credential) is also passed as a request header.

     ![HashiCorp AppRole request 2 headers](https://dt-cdn.net/images/cvhashiapprolerequest2requestheader-964-739c560649.png)
   * The username and password values are returned in the JSON response. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the values in [global variables](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveCredential()` to write the retrieved values to the synchronized username-password credential.

     ![HashiCorp AppRole request 2 post script](https://dt-cdn.net/images/cvhashiapprolerequest2postscript-964-828da84802.png)

1. The first request (POST) fetches a client token.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#hashicorp-set-up); the vault URL is not displayed. The request URL also contains the authentication method `approle`.

     ![HashiCorp AppRole request 1 URL](https://dt-cdn.net/images/cvhashiapprolerequest1url-1447-20b5ca2512.png)
   * The vault namespace, referenced as an attribute of the synchronized credential, is passed as a [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors."); the vault namespace is not displayed.

     ![HashiCorp AppRole request 1 header](https://dt-cdn.net/images/cvhashiapprolerequest1requestheader-964-7efd88a7af.png)
   * The role ID and secret ID, referenced as attributes of the synchronized credential, are passed as key-value pairs in the [request body](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Learn about configuring HTTP monitors."); the role ID and secret ID are not displayed.

     ![HashiCorp AppRole request 1 body](https://dt-cdn.net/images/cvhashiapprolerequest1requestbody-966-5eb6ad4427.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![HashiCorp AppRole request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)
2. The second request (GET) fetches the token value. It also uses `api.saveToken()` in a post-execution script to write the fetched values to the [synchronized token credential](#hashicorp-set-up) defined above.
   Request configuration details

   * The request URL references the vault URL and the path to the credentials as attributes of the synchronized credential; the vault URL and path to credentials are not displayed.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)
   * A [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the client token retrieved in the first request. The vault namespace (not displayed, but referenced as an attribute of the synchronized credential) is also passed as a request header.

     ![HashiCorp AppRole request 2 headers](https://dt-cdn.net/images/cvhashiapprolerequest2requestheader-964-739c560649.png)
   * The token value is returned in the JSON response. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the value in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveToken()` to write the retrieved value to the synchronized token credential.

     ![HashiCorp AppRole request 2 post-script to save token](https://dt-cdn.net/images/cv-hashi-approle-request2-postscript-savetoken-936-a139146cec.png)

### HashiCorp Vault TLS certificate synchronization monitors



The autocreated HTTP monitor contains two requests and is automatically associated with the [synchronized credential](#hashicorp-set-up) defined above.

Username-password credentials

Token credentials

1. The first request (POST) fetches a client token.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#hashicorp-set-up); the vault URL is not displayed. The request URL also contains the authentication method `cert`.

     ![HashiCorp certificate request 1 URL](https://dt-cdn.net/images/cvhashicertificaterequest1url-1448-630ba53192.png)
   * The request uses the TLS certificate for authentication.

     ![HashiCorp certificate request 1 certificate](https://dt-cdn.net/images/cvhashicertificaterequest1cert-964-996d51d92a.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![HashiCorp certificate request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)
2. The second request (GET) fetches the username and password values. It also uses `api.saveCredential()` in a post-execution script to write the fetched values to the [synchronized username-password credential](#hashicorp-set-up) defined above.
   Request configuration details

   * The request URL references the vault URL and the path to credentials as attributes of the synchronized credential; the vault URL and path to credentials are not displayed.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)
   * A [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the client token retrieved in the first request.

     ![HashiCorp certificate request 2 header](https://dt-cdn.net/images/cvhashicertificaterequest2requestheader-964-230e35242e.png)
   * The username and password values are returned in the JSON response. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the values in [global variables](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveCredential()` to write the retrieved values to the synchronized username-password credential.

     ![HashiCorp certificate request 2 post script](https://dt-cdn.net/images/cvhashiapprolerequest2postscript-964-828da84802.png)

1. The first request (POST) fetches a client token.
   Request configuration details

   * The request URL references the vault URL as an attribute of the [synchronized credential](#hashicorp-set-up); the vault URL is not displayed. The request URL also contains the authentication method `cert`.

     ![HashiCorp certificate request 1 URL](https://dt-cdn.net/images/cvhashicertificaterequest1url-1448-630ba53192.png)
   * The request uses the TLS certificate for authentication.

     ![HashiCorp certificate request 1 certificate](https://dt-cdn.net/images/cvhashicertificaterequest1cert-964-996d51d92a.png)
   * A client token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![HashiCorp certificate request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)
2. The second request (GET) fetches the token value. It also uses `api.saveToken()` in a post-execution script to write the fetched value to the [synchronized token credential](#hashicorp-set-up) defined above.
   Request configuration details

   * The request URL references the vault URL and the path to the credentials as attributes of the synchronized credential; the vault URL and path to credentials are not displayed.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)
   * A [request header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.") contains the client token retrieved in the first request.

     ![HashiCorp certificate request 2 header](https://dt-cdn.net/images/cvhashicertificaterequest2requestheader-964-230e35242e.png)
   * The token value is returned in the JSON response. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the value in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveToken()` to write the retrieved value to the synchronized token credential.

     ![HashiCorp certificate request 2 post-script to save token](https://dt-cdn.net/images/cv-hashi-approle-request2-postscript-savetoken-936-a139146cec.png)

## CyberArk Vault

Username-password credentials for use in synthetic monitors can be synchronized with CyberArk Vault key-value pairs containing the username or password. You can use either [username and password](#cyberark-monitor-uid-authentication) or [host-based authentication](#cyberark-monitor-allowed-machines) to CyberArk Vault. Host-based authentication allows you to predefine hosts (**Allowed Machines**) in CyberArk Vault that are allowed to access credentials. These hosts are the [public or private Synthetic locations you select](#cyberark-set-up) for synchronization monitor execution and are defined by hostname or IP address. Host-based authentication enables synchronization monitors to bypass fetching an access token from CyberArk Vault.

### Prerequisites

* Before using [username and password authentication](#cyberark-monitor-uid-authentication), you need to define authentication credentials for CyberArk Vaultâa [username-password pair](/docs/manage/credential-vault#uid-password "Store and manage credentials in the credential vault.") and, optionally, a [certificate credential](/docs/manage/credential-vault#certificate "Store and manage credentials in the credential vault.") stored in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."). We recommend naming such prerequisite credentials so that they're easily identifiable as companion credentials for synchronization.
* Before using [host-based authentication](#cyberark-monitor-allowed-machines), you need to define **Allowed Machines** by hostname or IP address in CyberArk Vault Application Details. These are the hosts that are allowed to access the synchronized credentials in CyberArk Vault and are the public or private Synthetic locations you select for synchronization monitor execution. Note that when defining allowed machines in CyberArk Vault, the application ID must be the same as provided when [you set up a synchronized credential in Dynatrace](#cyberak-set-up). Optionally, you can also define a [certificate credential](/docs/manage/credential-vault#certificate "Store and manage credentials in the credential vault.") stored in the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") for authentication to CyberArk Vault. If your vault doesn't contain any certificates you have access to, you'll see a warning.

We recommend naming any prerequisite credentials so that they're easily identifiable as companion credentials for synchronization.

### Set up synchronized credentials



1. In the credential vault, create a **User and password** credential. You can also overwrite an existing credential.
2. For **Credential scope**, select **Synthetic**.
3. Turn on **Synchronization with external vault**.
4. Select **CyberArk Vault** as the **Credential source**.
5. We recommend editing the default **Credential name** to easily identify your new credential.
6. Enter the **Central Credential Provider URL** (HTTPS) to access the vault.
7. Perform steps related to **Authentication method**.

   Username and password

   Allowed machines

   1. Select **Username and password** for the **Authentication method**.
   2. Select the [companion username-password](#cyberark-prereqs) created earlier for CyberArk authentication from the **Username and password for Central Credential Provider** list.

   ![Set up CyberArk synchronization - UID](https://dt-cdn.net/images/cyberark-credential-vault-uid-1145-62675d95c7.webp)

   1. Select **Allowed machines (location)** for the **Authentication method**.

      You should already have registered the hostname or IP address of your selected **Location for synchronization** in the CyberArk Allowed Machines listâsee [Prerequisites](#cyberark-prereqs) above.

   ![Set up CyberArk synchronization - allowed machines](https://dt-cdn.net/images/cyberark-credential-vault-allowed-machines-1154-a9d5d09098.webp)
8. Recommended Select a **Certificate used for authentication to CyberArk application** from the list provided.
9. Enter additional fields for identifying the CyberArk Vault key-value pair.

   * **Application ID**âThis must be the same as the application ID when defining allowed machines in CyberArk Vaultâsee [Prerequisites](#cyberark-prereqs) above.
   * **Safe name**
   * **Account name**âThe name of the object that stores the username and password to retrieve and synchronize with the Dynatrace credential vault; this is not the name of the account logged into CyberArk Central Credential Provider.
   * **Folder name** OptionalâThe name of the folder where the credentials are stored in CyberArk Vault; the default folder name is `Root`.
10. Select a **Location for synchronization**âyou can select any public or private Synthetic location for synchronization monitor execution. You can search for a location by entering the location name in the field.
11. Optional Provide a **Description** for the credential.
12. Credentials are set to **Owner access only** by default. (Read more about [credential ownership](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.").)
13. **Save** your credential.

See also [Best practices](#best-practices) and what happens when you [edit or delete synchronized and companion credentials](#edit-delete-credential).

When you have set up your synchronized credential, Dynatrace automatically creates and executes an [HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") that synchronizes the credential with CyberArk Vault.

### CyberArk Vault synchronization monitors (username-password authentication)

The autocreated HTTP monitor contains two requests and is automatically associated with the [synchronized credential](#cyberark-set-up) defined above.

1. The first request (POST) fetches an access token.
   Request configuration details

   * The request URL references the **Central Credential Provider URL** as an attribute of the [synchronized credential](#cyberark-set-up) defined above; the central credential provider URL is not displayed.

     ![CyberArk Vault request 1 URL](https://dt-cdn.net/images/cv-cyberark-request1-url-1445-f352bc0566.png)
   * The [request body](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Learn about configuring HTTP monitors.") references the username-password credential selected for CyberArk Vault authentication (**Username and password for Central Credential Provider**); the authentication username and password are not displayed.

     ![CyberArk Vault request 1 request body](https://dt-cdn.net/images/cv-cyberark-request1-request-body-1409-efb85f9433.png)
   * Additionally, the first request contains any authentication certificate specified in **Certificate used for authentication to CyberArk**.

     ![CyberArk Vault request 1 certificate](https://dt-cdn.net/images/cv-cyberark-request1-certificate-962-8b7934f165.png)
   * A token is returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the token in a [global variable](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests").

     ![CyberArk Vault request 1 post script](https://dt-cdn.net/images/cv-cyberark-request1-post-script-962-04c94bf083.png)
2. The second request (GET) fetches the username and password values from CyberArk Vault. It also uses `api.saveCredential()` in a post-execution script to write the fetched values to the [synchronized username-password credential](#cyberark-set-up) defined above.
   Request configuration details

   * The request URL references the **Central Credential Provider URL** as an attribute of the synchronized credential; the central credential provider URL is not displayed. The request URL also references (but doesn't display) the **Application ID**, **Safe name**, **Account name**, and **Folder name**.

     ![CyberArk Vault request 2 URL](https://dt-cdn.net/images/cv-cyberark-request2-url-1879-7911c0b652.png)
   * The second request also contains any authentication certificate and the access token retrieved in the first request in the [Authorization header](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Learn about configuring HTTP monitors.").

     ![CyberArk Vault request 2 token and certificate](https://dt-cdn.net/images/cv-cyberark-request2-certificate-auth-header-1269-b10aa9737b.png)
   * The username and password values are returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the values in [global variables](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveCredential()` to write the retrieved values to the synchronized username-password credential.

     ![CyberArk Vault request 2 post script](https://dt-cdn.net/images/cv-cyberark-request2-post-script-999-5b4607154b.png)

### CyberArk Vault synchronization monitors (host-based authentication)

Because the autocreated HTTP monitor can bypass fetching an access token, it contains a single GET request to fetch the username and password values from CyberArk Vault. It also uses `api.saveCredential()` in a post-execution script to write the fetched values to the [synchronized username-password credential](#cyberark-set-up) defined above. The synchronization monitor is automatically associated with the synchronized credential.

Request configuration details

* The request URL references the **Central Credential Provider URL** as an attribute of the synchronized credential; the central credential provider URL is not displayed. The request URL also references (but doesn't display) the **Application ID**, **Safe name**, **Account name**, and **Folder name**.

![CyberArk Vault allowed machines request URL](https://dt-cdn.net/images/cv-cyberark-allowed-machines-url-1881-1ea05be669.jpg)

* The request also contains any authentication certificate specified during credential setup.

![CyberArk Vault allowed machines authentication certificate](https://dt-cdn.net/images/cv-cyberark-allowed-machines-certificate-1415-568a21181f.jpg)

* The username and password values are returned in the response body. A [post-execution script](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") saves the values in [global variables](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Learn how to apply pre and post scripts to your requests"). It also uses `api.saveCredential()` to write the retrieved values to the synchronized username-password credential.

![CyberArk Vault allowed machines post script](https://dt-cdn.net/images/cv-cyberark-allowed-machines-post-script-1415-5e3ea56704.jpg)

## Best practices and caveats



If creating a synchronization monitor manually, be sure to select **Do not store and display request and response bodies and header values in execution details** in any requests that fetch client tokens or credential values from external vaults. Failing to do so will expose the sensitive information when you **Analyze execution details** in [HTTP monitor details](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.").

* Automatically created synchronization monitors may be edited. To edit an autocreated synchronization monitor, you must have [access to the credentials](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.") referenced in the monitor. You might need to make edits if the external vault vendor makes changes. For example, you might need to edit request URLs if Microsoft changes the API version for fetching client tokens from Azure Key Vault.

  + In general, however, we recommend that you limit your changes to execution frequency or locations.
  + When changing location, be careful not to pick [private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") that don't have external network access.
  + When changing location to a private Synthetic location, ensure that the proxy configuration isn't blocking access to required resources.
* We recommend editing the default names of synchronized credentials, companion credentials (for example, TLS certificates for HashiCorp Vault), and synchronization monitors for easy identification.
* We do not recommend reusing companion credentials (for example, for the HashiCorp secret ID token) required for synchronization monitors in other synthetic monitors for testing purposes.

### Edit or delete synchronized and companion credentials

* Once created, synchronized credentials are no longer editable by anyone; they can only be [overwritten](/docs/manage/credential-vault#overwrite-credential "Store and manage credentials in the credential vault."). In order to overwrite a synchronized credential, you need to provide new synchronization details; do not provide actual username, password, or token values.

  + When you overwrite a synchronized credential, Dynatrace-created synchronization monitors are automatically updated.
* Be sure to maintain the same [ownership](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.") for all credentials within a synchronization monitor (that is, the synchronized credential and companion credentials).
* You cannot delete companion credentials referenced by a synchronization monitor unless you disable or delete the synchronization monitor.
* If you delete a synchronized credential, its autocreated synchronization monitor is deleted as well.

  + If there's more than one synchronization monitor, you need to delete or disable such monitors before you can delete a synchronized credential.
  + Any synthetic monitor that uses the (deleted) synchronized credential for testing is disabled.