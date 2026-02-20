---
title: Remote environment data
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/remote-environment-data
scraped: 2026-02-20T21:19:30.565911
---

# Remote environment data

# Remote environment data

* Latest Dynatrace
* How-to guide
* 9-min read
* Updated on Dec 02, 2024

With [code tiles](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.") (in Dashboards) and [code sections](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") (in Notebooks), you can consolidate data from multiple Dynatrace environments.

There are two authentication mechanisms available for fetching data from remote environments:

* **Platform token authentication**: Intended for personal use. Use when you need rapid testing and quick data fetching from remote environments.
* **OAuth Client Authentication**: Intended for sharing. Use to ensure consistent data visibility for all users.

New! Start with a snippet in Dashboards or Notebooks

Dashboards version 1.310+ Notebooks version 1.310+

You can now start with a snippet when creating a dashboard or notebook that uses data from a remote Dynatrace environment.

* > **Fetch external data**
* > **Remote environment data via Platform token**
* > **Remote environment data via OAuth**

## Platform token authentication

Fetching data from remote environments via a platform token is intended for personal use. This method is ideal when you need to rapidly test and quickly fetch data from remote environments first before sharing it with others.

The example JavaScript code described below uses the credential vault for secure token storage, and a platform token for authentication, to offer a robust and secure way to fetch data from a remote Dynatrace environment.

### Prerequisites

Before you create the code for your dashboard tile or notebook section:

* Create a Dynatrace platform token on the environment you want to fetch the data from. For details, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
* Create a Dynatrace credential vault entry on the primary environment to store the platform token that is later used in the code tile or section for authentication. For details, see [Credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
* Allow external requests

  External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Select  **New host pattern**.
  3. Add the domain names.
  4. Select **Add**.

  This way you can granularly control the web services your functions can connect to.

  For example, you could add `myenv8132.apps.dynatrace.com` to allow just that environment, or use a wildcard like `*.apps.dynatrace.com` to allow all your Dynatrace environments at once.

For more about allowlisting, see [Allow IP ranges that can access your environment](/docs/manage/account-management/settings/ip-allowlist "Allow IP ranges that can access your environment using the CIDR notation.")

### Code

Before you start coding, review how the functions are used.

1. `async function()`

   This is the main function. It calls `fetchFromDynatrace` (see above) with the necessary parameters.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   To fetch data from Dynatrace, this function:

   1. Retrieves the credentials from the credential vault entry on the primary tenant based on the given credentialId.
   2. Makes the API call on the APIs of the secondary/remote tenant based on the credentials as well as the `url` and `query` parameter provided by the main function.

Now that you have completed the [prerequisites](#prerequisites) and reviewed the functions, you're ready to code.

* Base your code on the example below.
* Read the comments in the code example for code details.
* Replace `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` with your own credential ID.
* Replace `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` with your own URL.
* Customize the `"fetch logs | limit 1"` query according to your needs.
* Run your code in a [code tile](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.") (Dashboards) or [code section](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") (Notebooks).

  If you encounter errors when you run your code, they will be caught and logged with the prefixes `[DynatraceAuthError]`, `[CredentialVaultError]`, or `[ExecutionError]` for easier debugging.

Start with a snippet

You can start with a snippet (**Remote environment data via Platform token**) when creating a dashboard or notebook that uses data from a remote Dynatrace environment.

```
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";



/**



* Execute a query against a Dynatrace API with token retrieval inlined.



* @param {string} credentialId - The ID of the credential vault entry.



* @param {string} url - The API endpoint URL.



* @param {string} query - The query to execute.



* @returns {Promise<any>} - The API response data.



* @throws Will throw an error if any step fails.



*/



async function fetchFromDynatrace(credentialId, url, query) {



if (!credentialId || !url || !query) {



throw new Error("[ValidationError] Missing required parameters: credentialId, url, or query.");



}



try {



// Retrieve the platform token from the credential vault.



const { token } = await credentialVaultClient.getCredentialsDetails({



id: credentialId,



}).catch((error) => {



console.error(`[CredentialVaultError] Failed to retrieve token: ${error.message}`);



throw new Error("Unable to fetch platform token.");



});



if (!token) {



throw new Error("[CredentialVaultError] Token is undefined or empty.");



}



// Perform the API request.



const response = await fetch(url, {



method: "POST",



headers: {



"Content-Type": "application/json",



Accept: "application/json",



Authorization: `Bearer ${token}`,



},



body: JSON.stringify({



query,



requestTimeoutMilliseconds: 60000,



enablePreview: true,



}),



});



if (!response.ok) {



throw new Error(`[HTTPError] API call failed with status ${response.status}: ${response.statusText}`);



}



return await response.json();



} catch (error) {



console.error(`[FetchError] Query execution failed: ${error.message}`);



throw new Error("Unable to execute query.");



}



}



/**



* Main function to fetch and return results from Dynatrace.



* @returns {Promise<any>} - The query result.



*/



export default async function() {



const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Replace with your credential vault ID.



const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Replace with API URL.



const query = "fetch logs | limit 1"; // Replace with your query.



try {



const { result } = await fetchFromDynatrace(credentialId, url, query);



return result;



} catch (error) {



console.error(`[MainFunctionError] ${error.message}`);



return null; // Or handle as needed.



}



}
```

## OAuth client authentication

Fetching data from remote environments via OAuth is intended for sharing. This method ensures consistent data visibility for all users.

The example JavaScript code described below uses the credential vault for secure token storage, and OAuth for authentication, to offer a robust and secure way to fetch data from a remote Dynatrace environment.

### Prerequisites

Before you create the code for your dashboard tile or notebook section:

* Create an OAuth client. For details, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").
* Create a Dynatrace credential vault entry on the primary environment to store the OAuth token that is later used in the code tile or section for authentication. For details, see [Credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
* Allow external requests

  External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Select  **New host pattern**.
  3. Add the domain names.
  4. Select **Add**.

  This way you can granularly control the web services your functions can connect to.

  For example, you could add `myenv8132.apps.dynatrace.com` to allow just that environment, or use a wildcard like `*.apps.dynatrace.com` to allow all your Dynatrace environments at once.

For more about allowlisting, see [Allow IP ranges that can access your environment](/docs/manage/account-management/settings/ip-allowlist "Allow IP ranges that can access your environment using the CIDR notation.")

### Code

Before you start coding, review how the functions are used.

1. `async function()`

   This is the main function. It calls `fetchFromDynatrace` (see above) with the necessary parameters.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   To fetch data from Dynatrace, this function:

   1. Retrieves the credentials from the credential vault entry on the primary tenant based on the given credentialId.
   2. Gets an access token for the secondary tenant via SSO by calling the authenticateToDynatrace function.
   3. Makes the API call on the APIs of the secondary/remote tenant based on the previously received `accessToken` value as well as the `url` and `query` parameter provided by the main function.
3. `authenticateToDynatrace(clientId = '', clientSecret = '')`

   To authenticate against SSO, this function:

   1. Takes two parameters: `clientId` and `clientSecret`.
   2. Requests an access token based on the initial function parameters provided and the set of scopes defined within the function.
   3. On success, it returns the received access token from the Dynatrace SSO endpoint.

Now that you have completed the [prerequisites](#prerequisites) and reviewed the functions, you're ready to code.

* Base your code on the example below.
* Read the comments in the code example for code details.
* Replace `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` with your own credential ID.
* Replace `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` with your own URL.
* Customize the `"fetch logs | limit 1"` query according to your needs.
* Run your code in a [code tile](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.") (Dashboards) or [code section](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") (Notebooks).

  If you encounter errors when you run your code, they will be caught and logged with the prefixes `[DynatraceAuthError]`, `[CredentialVaultError]`, or `[ExecutionError]` for easier debugging.

Start with a snippet

You can start with a snippet (**Remote environment data via OAuth**) when creating a dashboard or notebook that uses data from a remote Dynatrace environment.

```
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";



/**



* Authenticate to Dynatrace SSO using client credentials.



* @param {string} clientId - The client ID for authentication.



* @param {string} clientSecret - The client secret for authentication.



* @returns {Promise<string>} - The access token.



* @throws Will throw an error if authentication fails.



*/



async function authenticateToDynatrace(clientId, clientSecret) {



if (!clientId || !clientSecret) {



throw new Error("[ValidationError] Missing clientId or clientSecret for SSO authentication.");



}



const scopes = [



"environment-api",



"storage:buckets:read",



"storage:bizevents:read",



"storage:logs:read",



"storage:metrics:read",



"storage:entities:read",



].join(" ");



try {



const response = await fetch("https://sso.dynatrace.com/sso/oauth2/token", {



method: "POST",



headers: { "Content-Type": "application/x-www-form-urlencoded" },



body: `grant_type=client_credentials&client_id=${clientId}&client_secret=${clientSecret}&scopes=${scopes}`,



});



if (!response.ok) {



throw new Error(`[HTTPError] SSO authentication failed with status ${response.status}: ${response.statusText}`);



}



const { access_token: accessToken } = await response.json();



if (!accessToken) {



throw new Error("[SSOError] Access token not received.");



}



return accessToken;



} catch (error) {



console.error(`[DynatraceAuthError] ${error.message}`);



throw error;



}



}



/**



* Fetch data from Dynatrace using a query.



* @param {string} credentialId - The credential vault ID.



* @param {string} url - The API endpoint URL.



* @param {string} query - The query to execute.



* @returns {Promise<any>} - The API response data.



* @throws Will throw an error if any step fails.



*/



async function fetchFromDynatrace(credentialId, url, query) {



if (!credentialId || !url || !query) {



throw new Error("[ValidationError] Missing one or more required parameters: credentialId, url, or query.");



}



try {



// Retrieve credentials from the credential vault.



const { username: clientId, password: clientSecret } = await credentialVaultClient.getCredentialsDetails({



id: credentialId,



}).catch(error => {



console.error(`[CredentialVaultError] Failed to retrieve credentials: ${error.message}`);



throw new Error("Unable to fetch credentials from the vault.");



});



if (!clientId || !clientSecret) {



throw new Error("[CredentialVaultError] Missing clientId or clientSecret from the retrieved credentials.");



}



// Authenticate and get an access token.



const accessToken = await authenticateToDynatrace(clientId, clientSecret);



// Perform the API request.



const response = await fetch(url, {



method: "POST",



headers: {



"Content-Type": "application/json",



Accept: "application/json",



Authorization: `Bearer ${accessToken}`,



},



body: JSON.stringify({



query,



requestTimeoutMilliseconds: 60000,



enablePreview: true,



}),



});



if (!response.ok) {



throw new Error(`[HTTPError] API call failed with status ${response.status}: ${response.statusText}`);



}



return await response.json();



} catch (error) {



console.error(`[FetchError] ${error.message}`);



throw error;



}



}



/**



* Main function to execute a query and return results from Dynatrace.



* @returns {Promise<any>} - The query result.



*/



export default async function fetchDynatraceData() {



const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Replace with your credential vault ID.



const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Replace with API URL.



const query = "fetch logs | limit 1"; // Replace with your query.



try {



const { result } = await fetchFromDynatrace(credentialId, url, query);



return result;



} catch (error) {



console.error(`[MainFunctionError] ${error.message}`);



return null; // Return null or handle gracefully.



}



}
```