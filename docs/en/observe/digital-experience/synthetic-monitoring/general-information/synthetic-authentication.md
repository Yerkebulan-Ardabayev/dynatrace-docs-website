---
title: Supported authentication methods in Synthetic Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication
scraped: 2026-02-25T21:33:18.329590
---

# Supported authentication methods in Synthetic Monitoring

# Supported authentication methods in Synthetic Monitoring

* How-to guide
* 9-min read
* Updated on Aug 19, 2025

Dynatrace Synthetic Monitoring offers various methods for monitoring web applications or API endpoints that require authentication. Read on for an overview of the most common scenarios and the appropriate methods to use.

## Browser monitors

The [**HTTP authentication**](#http-bm) and [**certificate authentication**](#certificate-bm) methods are supported for both [single-URL browser monitors](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.") and [browser clickpaths](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.").

The [**web form** (**HTML-based**)](#web-form-bm) is supported only for browser clickpaths.

### Web form (HTML-based) authentication for web applications

The most common scenario is a webpage with web form (HTML-based) authentication, which requires you to enter a username and password.

![Web application with HTML-based authentication](https://dt-cdn.net/images/htmlbasedauthentication-2048-c9fcf36a82.png)

You can monitor a transaction in a [browser clickpath](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") by recording credentials in a web form.

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Specify the monitor name, starting URL, and other options before selecting **Record clickpath** at the bottom of the page.
3. While recording, manually enter the username and password for authentication; Dynatrace automatically captures the credentials.
4. After recording, you have the option of storing the credentials to the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
5. [Complete the configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of your clickpath.

#### Single-URL monitors with web form authentication

Deprecated

Web form authentication is no longer supported for the single-URL browser monitors. You can instead create [browser clickpath](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") monitors for the test scenarios that require web form login. Your previously configured single-URL monitors will run as before, but we recommend to re-record them as clickpaths to clearly separate each step of the login process.

Re-recording is required if you want to modify any part of your monitor's configuration. You can no longer save changes in their current format.

Starting from Dynatrace version 1.324+, the single-URL monitors with the web form login will be automatically updated by adding a free JavaScript step to support the login process.

### Basic, digest, NTLM, or Negotiate (Kerberos) authentication for web applications

If you need to monitor a page with a browser-native dialog box (that's not part of the web application) to authenticate (as in the image below), it's likely that the basic, digest, NTLM, or Negotiate authentication methods are used in the background.

Negotiate (Kerberos) is supported for browser monitors executed in [private locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#kerberos-client-setup "Learn how to create a private location for synthetic monitoring.") on

* Windows
* ActiveGate version 1.311+ Linux
* ActiveGate version 1.311+ [Containerized](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations#kerberos "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.")

![Native browser login dialog box](https://dt-cdn.net/images/nativebrowserlogindialogbox-1837-c1502c0fdf.png)

Monitor a single page

Transaction in a recorded clickpath

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. In **Additional options**, turn on **Enable global login authentication**.
3. Select either:

   * **HTTP authentication** if the login happens via the native browser dialogue
   * **Kerberos authentication** if the login happens via Kerberos protocol. Fill additional required fields:

     + Domain: User's domain name
     + Auth server allow list: List of allowed servers for Kerberos authentication. Wildcards can be used. Exact details are provided in the [Chrome Enterprise documentationï»¿](https://dt-url.net/p803wkm)
4. Either use an existing credential from the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") (**Select credentials**) or **Create new credentials**.
5. [Complete the configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of your single-URL browser monitor.

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Specify the monitor name, starting URL, and other options before selecting **Record clickpath** at the bottom of the page.
3. While recording, manually enter the username and password in the browser-native dialog box.
4. When done recording, open the first [Navigate event](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Learn about the event types created when recording a browser clickpath.") of your clickpath and turn on **Enable HTTP authentication**.

   ![Navigate event HTTP authentication](https://dt-cdn.net/images/navigatehttpauthentication-652-d4048163be.png)
5. Either use an existing credential from the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") (**Select credentials**) or **Create new credentials**.

   Your clickpath will automatically use these credentials to authenticate via the browser-native login dialog.
6. To use Kerberos authentication, select **Kerberos authentication**. Authentication will be done by receiving Kerberos tickets for provided credentials from the Kerberos Key Distribution Center.

   ![Kerberos Authentication](https://dt-cdn.net/images/kerberosauth-608-429fe9ac73.png)

   * Domain: User's domain name
   * Auth server allow list: List of allowed servers for Kerberos authentication. Wildcards can be used. Exact details are provided in the [Chrome Enterprise documentationï»¿](https://dt-url.net/p803wkm)
7. [Complete the configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of your browser clickpath.

Supported username formats

* Browser monitors: `<username>` and `<domain>\<username>`
* HTTP monitors: `<username>`
* **NTLM authentication** in browser and HTTP monitors: `<username>`

### Client certificate authentication for web applications

Certificate authentication is available for browser monitors executed from any [public location](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") and on Linux-based [private locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."). Once you set up your browser monitor, you need to specify client certificate details in the **Advanced setup** tab of monitor settings in edit mode.

Monitor a single page

Transaction in a recorded clickpath

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Specify the monitor URL and name.

   You cannot specify a client certificate when initially setting up a single-URL browser monitor.
3. [Complete the configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of your single-URL browser monitor.

1. Before first recording a clickpath on a website that requires certificate authentication, ensure that you have installed the required certificate in Chrome.
2. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
3. Specify the monitor name, starting URL, and other options before selecting **Record clickpath** at the bottom of the page.
4. When you navigate to the website in the recording window, the native browser dialog simply selects the correct certificate that you've installed in Chrome. After you record the clickpath, you need to specify the certificate to use for monitor execution, as described below.

Next, in edit mode, add client certificates for browser monitor execution.

1. Select the **Advanced setup** tab in browser monitor settings.
2. Turn on **Use client certificates**.
3. Select **Add client certificate**.
4. Enter the **Domain** that the certificate is valid for.
5. Select a credential from the list of certificate credentials displayed. Alternatively, select **Create new credential** to upload and use a new client certificate. Any certificate credential you create is automatically designated as [owner only](/docs/manage/credential-vault#work-with-credentials "Store and manage credentials in the credential vault.") and stored in the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").

   You can specify and upload certificate files in PFX, P12, or PEM format.

   ![Certificate authentication setting for browser monitors](https://dt-cdn.net/images/bm-client-certificates-788-4347c846d7.png)
6. Select **Add entry**.
7. Repeat these steps to add multiple certificates for use in your clickpath. However, each certificate must be tied to a single domain.
8. **Save changes**.

## HTTP monitors

HTTP monitors support basic, NTLM, token, OAuth 2.0, or certificate-based authentication.

### Basic or NTLM authentication for endpoints

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor**.
2. Select **Add HTTP request** and choose the **HTTP request** type.
3. In the **Additional options** of the request, **Set authentication/authorization**.
4. Select **Basic authentication** or **NTLM**.
5. Either use an existing credential from the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") (**Select credentials**) or **Create new credentials**.

   Dynatrace automatically generates the required `Authorization` header with the information you've provided.

   Supported username formats

   * Browser monitors: `<username>` and `<domain>\<username>`
   * HTTP monitors: `<username>`
   * **NTLM authentication** in browser and HTTP monitors: `<username>`
6. Finish [configuring your HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.").

### Bearer or token authentication for endpoints

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor**.
2. Select **Add HTTP request** and choose the **HTTP request** type.
3. In the **Additional options** of the request, **Set additional HTTP headers**.
4. Select **Add header**.
5. Fill out the header, for example, set:

   **Header name** = `Authorization`

   **Header value** = `Bearer <your-token>`

   or

   **Header name** = `Authorization`

   **Header value** = `Api-Token <your-token>`
6. Finish [configuring your HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.").

### OAuth 2.0 authorization for endpoints

OAuth 2.0 authorization is available for HTTP monitors and is most commonly used when querying API endpoints. Dynatrace provides the **OAuth2 authorization request** type, which is a specialized HTTP request template for OAuth 2.0 authorization requests.

You first need to set up an OAuth 2.0 request for an access token, which you then use in all subsequent HTTP requests in your monitor that queries the API endpoint. The returned token is not stored to the credential vault, but it's easily accessible as an autocomplete option in your subsequent HTTP requests.

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor** and provide a **Name**.
2. Select **Add HTTP request** and choose the **OAth2 authorization request** type.
3. Enter the URL from which you're requesting an authorization token (**Access token URL**) and request **Name**.
4. Select **Add HTTP request** to view expanded request settings. Note that the OAuth 2.0 request is automatically created as a `POST` request.
5. Fill out or edit these important settings in the request details.

   1. Depending on how your authentication server is set up, opt to **Add authorization data to** the **Request body** or **Request URL**. Fill out the POST parameters (`grant_Type`, `scope`, `client_id`, `username`, and `password`) in the **Request body** or **Request URL**. You can add or modify parameters as needed.

      ![OAuth parameters in request body](https://dt-cdn.net/images/oauthparamsbody1-1171-5bbbc6be5d.png)

      ![OAuth parameters in request URL](https://dt-cdn.net/images/oauthparamsurl-1314-353802a4b5.png)
   2. A **post-execution script** is automatically enabled, where:

      * The request fails if the returned status code is not `200`.
      * The `api.fail()` method defines the **Failure message** that appears in case of failure in the **Events** card on the [HTTP monitor details page](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.") and in [execution details](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Learn about the Synthetic details page for HTTP monitors.").
      * If the request is successful, the response body, which is a JSON-formatted string, is stored in a JavaScript object (called `bearToken-2` in this example).
      * The `api.info()` method sends information to a log file, which is accessible on [private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

      Custom log messages also appear in the `customLogs` attribute in [HTTP monitor execution details](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Learn about the Synthetic details page for HTTP monitors.").

      ![Post-execution script](https://dt-cdn.net/images/oauthpostexecutionscript-812-911fe199bc.png)
   3. **Set token request authentication** enables you to specify additional authentication details (**Basic authentication**, **NTLM**, or **Kerberos**) for the server that the OAuth application sits behind.

For subsequent HTTP requests

1. Create an additional HTTP request for the endpoint you need to monitor (**Add HTTP request**).
2. In the **Additional options** of the second request:

   * Enable **Set authentication/authorization** and select the **OAuth2** method. Note that this option is only available if you've first created an OAuth 2.0 authorization request (described above).

     An autogenerated **pre-execution script** referencing the OAuth token received in the request created above is displayed.

     ![OAuth method in HTTP request](https://dt-cdn.net/images/oauthtokeninsert1-1129-0244726c35.png)
   * As an alternative, set an HTTP `Authorization` header with the JavaScript object containing the OAuth token as the **Header value**.

     ![OAuth method in HTTP request](https://dt-cdn.net/images/oauthtokeninsert2-1214-783de8da93.png)
3. Finish [configuring your HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.").

### Client certificate authentication for endpoints

1. Go to **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor** and provide a **Name**.
2. Select **Add HTTP request** and choose the **HTTP request** type.
3. In the **Additional options** of the request, **Add client certificate**.
4. Either use an existing certificate from the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") (**Select credentials**) or **Create new credentials**.
5. Finish [configuring your HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.").

To assure full mutual authentication, disable [**Accept any SSL certificate**](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#ssl-accept "Learn about configuring HTTP monitors.") when using certificate authentication.