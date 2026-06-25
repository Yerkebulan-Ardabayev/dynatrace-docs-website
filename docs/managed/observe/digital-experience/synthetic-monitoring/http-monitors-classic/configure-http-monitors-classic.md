---
title: Configure HTTP monitors
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic
scraped: 2026-05-12T11:31:48.513342
---

# Configure HTTP monitors

# Configure HTTP monitors

* How-to guide
* 16-min read
* Updated on Apr 01, 2026

Dynatrace allows you to easily configure your HTTP monitors when first setting them up and at any time thereafter.

During HTTP monitor creation, configuration settings appear after you've selected **Create an HTTP monitor**. These settings are a subset of the full set available in edit mode (described below) after the monitor has been deployed. If you're creating a new HTTP monitor, see [Create an HTTP monitor](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.").

HTTP monitors can be run from our global [public](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") or [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."), or from cluster-wide locations in Dynatrace Managed. See [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for details on using ActiveGate for Synthetic Monitoring. See [Requirements for private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for more information on supported Windows and Linux versions.

## Configure an existing HTTP monitor

To configure an existing HTTP monitor

1. Go to **Synthetic Classic**.
2. Select the HTTP monitor you want to configure (this takes you to the [details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.")).
3. Select **Edit** from the quick links in the upper-left corner to go to monitor settings.

   Alternatively, you can go to **Synthetic Classic** in list view, select the check box next the monitor you want to edit > **Edit** in the lower-left corner.
4. Browse through the **Monitor settings** tabs on the left to configure settings (detailed explanations belowâa subset of these settings are available when you first create an HTTP monitor).

   * [General](#setup)
   * [HTTP requests](#http-requests)
   * [Frequency and locations](#frequency-locations)
   * [Outage handling](#outage-handling)
   * [Performance thresholds](#performance-thresholds)
5. When you make changes, the **Discard changes** and **Save changes** buttons are displayed in the lower-left corner. Be sure to save your changes when you're done editing your monitor.

Who can edit a monitor that has associated credentials?

* If a monitor is associated with a public credential, anyone on your team can switch on/off, delete, or edit the monitor.

* If an HTTP monitor is associated with restricted credential (owner only or shared with a few users), any user can make changes to certain fields, even if they don't have access to the credential used. You can edit monitor name, locations, validation, thresholds, and, of course, change a certificate or a UID/password pair. You can edit and change the credentials in a URL, header value, or request body. You can create a credential within monitor settings in edit mode. You'll need to change all credentials in the monitor to ones that you have access to. Note that replacing another user's credential with one you have access to is irreversible.

  Controls that you cannot edit such as the request URL, HTTP method, pre-execution script, post-execution script, HTTP headers, request body, the follow redirects option, and adding/deleting HTTP requests are grayed out or display an error message when you attempt to save changes, whether in script or UI mode.

* You can enable/disable or delete a synthetic monitor that's secured by another user's owner-only credentials.

Read more about credential permissions in [Credential vault for synthetic monitors](/managed/manage/credential-vault "Store and manage credentials in the credential vault.").

## General

In the **General** tabs, you can:

* Review and change the **Monitor name** (up to 500 characters). This name should generally describe all the requests in this HTTP monitor.
* Set **Cookies** to store state information or instruct the server not to send certain kinds of information. Cookies are added to headers, and values are set before the first HTTP request is executed. This setting is available in edit mode only.

  In edit mode, enable **Set cookies**, then provide a **Name** and cookie **Value**. Every cookie must be unique within the list.

  The following symbols are not allowed in the cookie value: `;,\"`. Provide the **Domain** of the cookie, and optionally, the **Path** to the cookie. **Save** your cookie.

  Select **Add cookie** to define additional cookies.

  Any cookie values remain on the client until the server sends a `Set-Cookie` header, you change the cookie value in a [pre-execution script](#pre-execution), or until the end of monitor execution.

### Assigned applications

This setting is available in edit mode only.

If this synthetic monitor is associated with one of your monitored applications, you can assign the monitor to the application so you can track application availability and performance. Detected problems are then automatically associated with your application. If the monitor is unavailable, the associated application is also considered to be unavailable.

Select **Assign to application** and choose an application from the list. You can assign a monitor to multiple applications, and an application can have several assigned monitors.

You can assign an HTTP monitor to a web, mobile, or custom application.

Note that you cannot block Synthetic Monitoring traffic for RUM applications by [excluding bots, spiders, or the IP addresses of Synthetic locations](/managed/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.").

## HTTP requests

You can edit and add HTTP requests that the monitor sends to your server.

In **Visual mode**:

* Select **Add HTTP request** to add another HTTP request to the HTTP monitor.
* Select an existing HTTP request to display and edit configuration options for that request.
* If necessary, you can delete requests from your monitor by selecting **x** under **Delete** for the respective request.
* Use the **Move up/down** arrows ![Move up](https://dt-cdn.net/images/sorter-move-up-6275b6459e.svg "Move up") ![Move down](https://dt-cdn.net/images/sorter-move-down-710c5d6229.svg "Move down") to reorder requests.

You aren't limited to just one mode to view and edit your HTTP requestsâyou can switch back and forth between the UI and script modes by selecting **Visual mode** or **Script mode**. For details on editing your HTTP monitor in JSON format, see [Script mode for HTTP monitor configuration](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

### Basic request settings

These settings are available for [OAuth2 authorization requests](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#oauth2 "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.") as well as all [HTTP methods](#http-methods) in HTTP requests:

* **HTTP request URL**

  To enhance synthetic monitor security, Dynatrace blocks monitors from sending requests to a local host (for example, `localhost` or `127.0.0.1`).

  You can add [token credentials](/managed/manage/credential-vault#token "Store and manage credentials in the credential vault.") to the **HTTP request URL**âbegin by typing `{cr` to view a list of autocomplete credential suggestions. This list only has credentials that you have permission to use, that is, public credentials or owner-only credentials that you created.

  + In fields where you can manually insert a reference to a credential (as in the request URL) by copying the credential ID from the vault, use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, as appropriate for the type of credential you're inserting. You can only copy and paste credentials to which you have access.
  + Who can edit a monitor that has associated credentials?

    - If a monitor is associated with a public credential, anyone on your team can switch on/off, delete, or edit the monitor.

    - If an HTTP monitor is associated with restricted credential (owner only or shared with a few users), any user can make changes to certain fields, even if they don't have access to the credential used. You can edit monitor name, locations, validation, thresholds, and, of course, change a certificate or a UID/password pair. You can edit and change the credentials in a URL, header value, or request body. You can create a credential within monitor settings in edit mode. You'll need to change all credentials in the monitor to ones that you have access to. Note that replacing another user's credential with one you have access to is irreversible.

      Controls that you cannot edit such as the request URL, HTTP method, pre-execution script, post-execution script, HTTP headers, request body, the follow redirects option, and adding/deleting HTTP requests are grayed out or display an error message when you attempt to save changes, whether in script or UI mode.

    - You enable/disable or delete a synthetic monitor that's secured by another user's owner-only credentials.

    Read more about credential permissions in [Credential vault for synthetic monitors](/managed/manage/credential-vault "Store and manage credentials in the credential vault.").
* **Add authorization data to**

  This field is only available in the **OAuth2 authorization request** typeâsee [Supported authentication methods in Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#oauth2 "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").

* **HTTP method**

  For each request you create or edit, start with the **HTTP method**, because the available request settings depend on this selection. Supported HTTP methods are:

  + GET
  + POST
  + PUT
  + DELETE
  + HEAD
  + PATCH
  + OPTIONS
* Optional [**User agent**ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

  The default user agent is in the format `DynatraceSynthetic/{version}`, where `{version}` is the current version of the Synthetic engine executing the monitor. Even if you define a custom user agent, Dynatrace automatically appends `DynatraceSynthetic/{version}` to the user agent to make sure that synthetic monitoring traffic can be identified. **Do not** use `DynatraceSynthetic/` in your custom user agent; this is reserved for Dynatrace use.
* **Response status code verification**

  Opt to **Fail**/**Pass** your monitor based on the returned HTTP status code for the request.

  You can specify an exact status code, inequality symbol (`<`, `<=`, `>`, `>=`, `!=`), range, or status class mask (`xx` only). Use the Minus sign (`-`) with no spaces for a range; use `!=` for the not-equal-to operator. (Note that `=>` and `=<` are not supported.) Use commas to separate multiple values, for example, `3xx, 404, 406-410, >=500`. The default setting, when enabled, is to fail the monitor when the returned status code is `>=400`.

  HTTP monitor validation

  The following types of rules are evaluated for HTTP monitor validation in the `validation.rules` section in [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

  + Response status code validation
  + Text validation, where the first 50 KB of the response body is checked for a string of text or a regular expression
  + SSL certificate expiry validation (ActiveGate version 1.235+)

  In a monitor containing multiple validations, all rules are evaluated. However, a single execution status is returned based on priority: HTTP status code validation is the most important, followed by text and regular expression validation, and finally by SSL certificate expiry validation.

### Additional options

Adjust the **Additional options** as needed.

#### Enable pre-execution script

[Pre- and post-execution scripts](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") enable you to add custom logic between HTTP monitor requests to do things like parsing the response, modifying the request URL, or skipping requests under certain conditions.

If you enable this, an edit box is displayed for you to enter a script that is executed just before the request is triggered. Pre-execution scripts are based on custom JavaScript code and can be used to build your HTTP request or to add logic that you cannot or do not want to implement in the UI.

For more information and a method reference, see [Pre- and post-execution scripts for HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#methods "Learn how to apply pre and post scripts to your requests"). Note that some methods are only available for use in [pre-execution scripts](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#pre-execution "Learn how to apply pre and post scripts to your requests") or [post-execution scripts](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#post-execution "Learn how to apply pre and post scripts to your requests").

#### Enable post-execution script

If you enable this, an edit box is displayed for you to enter a script that is executed after the request is completed. Post-execution scripts are based on custom JavaScript code and can be used process responses to the request.

The [`api.fail()` method](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#end "Learn how to apply pre and post scripts to your requests") can be used to define a custom **Failure message** that appears in the Events card on the [HTTP monitor details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.").

![Custom failure message](https://dt-cdn.net/images/httpdetailseventsfailuremsg-1102-2317af2250.png)

Custom failure message

For more information and a method reference, see [Pre- and post-execution scripts for HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests"). Note that some methods are only available for use in [pre-execution scripts](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#pre-execution "Learn how to apply pre and post scripts to your requests") or [post-execution scripts](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#post-execution "Learn how to apply pre and post scripts to your requests").

#### Set authentication/authorization

Note that this setting is called **Set token request authentication** in the **OAuth2 authorization request** type.

Enable this and provide a username/password pair to automate the login process for password-protected sites via **Basic**, **NTLM**, or **Kerberos** authentication. Dynatrace automatically generates the required `Authorization` header with the information you've provided. (Read more about [Supported authentication methods in Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").)

Kerberos authentication isn't supported for monitors assigned to private Synthetic locations, where the ActiveGates handling monitor executions use a proxy to connect to the tested resources.

Dynatrace stores and manages all Synthetic Monitoring credentials in a credential vault. Credentials are access controlled and can be designated as owner only or public.

You can choose an existing credential (**Select credentials**). You can only see credentials that you have access to in this list, that is, public credentials or owner-access credentials created by you.

You can **Create new credentials** by entering a **Username** and **Password**. Provide a **Credential name** and **Save to vault**.

The `<domain>\<username>` format is not supported for the username in HTTP monitors; simply provide the `<username>`.

![Create a credential in an HTTP monitor](https://dt-cdn.net/images/httpmonitorcreatecredentialscv1-533-2baa3b4622.png)

Create a credential in an HTTP monitor

The credentials you create this way are automatically set to owner-only permissions and can only be used by you. Note that you can create credentials this way in a new or existing HTTP monitor even if you don't have permissions to access credential management in the [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault.").

#### Add client certificate

Use this option to enable client-side certificate authentication. (Read more about [Supported authentication methods in Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").)

Dynatrace stores and manages all Synthetic Monitoring credentials in a credential vault. Credentials are access controlled and can be designated as owner only or public.

You can choose an existing credential (**Select credentials**). You can only see the credentials that you have access to in this list, that is, public credentials or owner-only credentials created by you.

You can **Create new credentials**âsimply upload a **Certificate file** (in PFX, P12, or PEM format) and enter a **Certificate password**. Provide a **Credential name** and **Save to vault**. The credentials you create this way are automatically set to owner-only permissions and can only be used by you. Note that you can create credentials this way in a new or existing HTTP monitor even if you don't have permissions to access credential management in the [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault.").

![Upload a certificate via an HTTP monitor](https://dt-cdn.net/images/httpmonitoruploadcertificatecv-849-c7d1436e3b.png)

Upload a certificate via an HTTP monitor

To guarantee full mutual authentication, ensure [**Accept any SSL certificate**](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#ssl-accept "Learn about configuring HTTP monitors.") is turned off when using the certificate authentication.

#### Set additional HTTP headers

The monitor is created with a bare minimum set of headers required by the protocol. Enable this option to create custom/additional headers:

1. Select **Add header**.
2. Enter a **Header** name and **Value**.
3. **Add another header** as needed.

Use HTTP headers to implement bearer or token authenticationâread more in [Supported authentication methods in Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#bearer-token "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").)

You can add token credentials to the header **Value**âbegin by typing `{cr` to view a list of autocomplete credential suggestions. You can only see the credentials that you have access to in this list, that is, public credentials or owner-only credentials created by you.

* In fields where you can manually insert a reference to a credential (as in the header value) by copying the credential ID from the vault, use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, as appropriate for the type of credential you're inserting. You can only copy and paste credentials to which you have access.
* Default HTTP headers

  These are the default headers Dynatrace creates per request.

  | Name | Value |
  | --- | --- |
  | `Accept` | `*/*` |
  | `Connection` | `close` |
  | `Host` | `<hostname>` |
  | `User-Agent` | `DynatraceSynthetic/{version}`[1](#fn-1-1-def) |

  1

  `{version}` is the current version of the Synthetic engine executing the monitor. Even if you [define a custom user agent](#basic-settings), Dynatrace always automatically adds `DynatraceSynthetic/{version}` to the user agent to make sure that synthetic monitoring traffic can be identified.

  Dynatrace also creates the `x-Dynatrace-Tenant`, and `x-Dynatrace-Test` headers for internal administrative purposes.

#### Request body

You can send a payload with your **POST**, **PUT**, **DELETE**, and **PATCH** requests. You can add token credentials to the request bodyâbegin by typing `{cr` to view a list of autocomplete credential suggestions. You can only see the credentials that you have access to in this list, that is, public credentials or owner-only credentials created by you. If this field contains an [owner-only token](/managed/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault."), it cannot be edited by other users.

Specify the request body format and contents:

* **x-www-form-urlencoded**âSelect **Add property** and enter one or more pairs of property keys and values.
* **raw**âEnter the request body in the edit box.

In fields where you can manually insert a reference to a credential (as in the **Value** of a key-value pair in the request body) by copying the credential ID from the vault, use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, as appropriate for the type of credential you're inserting. You can only copy and paste credentials to which you have access.

#### Set rule for response validation

This option is not available in the **OAuth2 authorization request** type.

Response validation enables you to pass/fail your monitor based on expected content in the first 50 KB of the response body.

* **Pass if** or **Fail if** determines the basic test.
* **Text contains** specifies the text to look for in the response. This string is case sensitive. If your string contains non-ASCII characters, escape them in [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").
* **Interpret content match as regular expression** treats the specified text as a [regular expression](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

You can set up multiple such text-validation rules in [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

HTTP monitor validation

The following types of rules are evaluated for HTTP monitor validation in the `validation.rules` section in [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

* Response status code validation
* Text validation, where the first 50 KB of the response body is checked for a string of text or a regular expression
* SSL certificate expiry validation (ActiveGate version 1.235+)

In a monitor containing multiple validations, all rules are evaluated. However, a single execution status is returned based on priority: HTTP status code validation is the most important, followed by text and regular expression validation, and finally by SSL certificate expiry validation.

#### Follow redirects

By default, an HTTP monitor follows up to 10 redirects from an original request until it reaches the final destination. Turn this option off to monitor only the first response of the redirect chain, for example, to check redirect response status codes.

#### Accept any SSL certificate

By default, HTTP monitors fail when SSL certificates are invalid. Turn on the **Accept any SSL certificate** option to make the monitor accept any SSL certificates, regardless of whether they're valid.

Reasons for SSL certificate invalidity

Depending on your setting, your HTTP monitor can fail or succeed when an SSL certificate is invalid for any of these reasons, among others:

* Certificate is self signed
* Certificate has expired
* Certificate is inactive
* Certificate lifetime is greater than 398 days
* Missing hostname
* Invalid/incomplete certificate chain
* Untrusted certificate authority
* Insecure signature algorithm

See also [SSL certificate expiration date verification](#certificate-expiry) below.

#### SSL certificate expiration date verification

Turn on this option to generate an **SSL certificate expiration problem** when an SSL certificate is missing, expired, or will expire within the specified number of days (must be 100 or less). Note that this problem is generated without failing the monitor or affecting monitor availability.

SSL certificate expiration problems have the **Custom** severity level and display the number of days remaining until certificate expiry. This value is updated with each execution of the affected monitor.

![SSL certificate expiration problem](https://dt-cdn.net/images/sslcertexpirationproblem-1009-680712510b.png)

SSL certificate expiration problem

This setting requires ActiveGate version 1.235+ for private locations.

For private locations with ActiveGate versions lower than 1.235

When you turn on **SSL certificate expiration date verification** on private locations with ActiveGate versions lower than 1.235:

* The HTTP monitor will fail, generating an outage problem with an error, when SSL certificate expiry is within the specified number of days.
* The following SSL certificate expiration statuses are reported in outage problem details and in the **Events** and **Failed requests** cards in [HTTP monitor details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors."):

  + `SSL certificate expired` if the certificate has expired
  + `SSL certificate expires within N days`, where `N` = `10`, `30`, `50`, or `100`

  So, if you specify that certificate expiry must not be within 20 days, and the certificate is valid for 15 days, the HTTP request will fail with the status message `SSL certificate expires within 30 days`.

The following examples show how to apply the **SSL certificate expiration date verification** and [**Accept any SSL certificate**](#ssl-accept) settings.

* If you want to configure a monitor that accepts a self-signed certificate while triggering an alert for certificate expiry, you would:

  + Turn on **Accept any SSL certificate**.
  + Turn on **SSL certificate expiration date verification** and set a threshold for problem generation.
* If you choose not to accept any SSL certificate, and the SSL certificate has expired, the HTTP monitor will fail and trigger an outage problem with an `SSL certificate expired` message in problem details and in the **Events** and **Failed requests** cards in [HTTP monitor details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.").
* If you turn on both these options, and the SSL certificate has expired, the HTTP monitor will trigger an SSL certificate expiration problem. The **Events** card will display a custom alert for SSL certificate expiration.
* If you turn on both these options and specify a threshold of `n` days for SSL certificate expiry, and the SSL certificate expires within `n` days, the HTTP monitor will trigger an SSL certificate expiration problem. The **Events** card will display a custom alert for SSL certificate expiration.

HTTP monitor validation

The following types of rules are evaluated for HTTP monitor validation in the `validation.rules` section in [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

* Response status code validation
* Text validation, where the first 50 KB of the response body is checked for a string of text or a regular expression
* SSL certificate expiry validation (ActiveGate version 1.235+)

In a monitor containing multiple validations, all rules are evaluated. However, a single execution status is returned based on priority: HTTP status code validation is the most important, followed by text and regular expression validation, and finally by SSL certificate expiry validation.

#### Do not store and display request and response bodies, header values, and peer certificate details in execution details

Turn on this option to hide potentially sensitive information (contained in, say, the response body) in [execution details (**Analyze last execution**)](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Learn about the Synthetic details page for HTTP monitors.").

You need to do this for each request you wish to limit the display of. Request and response bodies, values of request and response headers, and peer certificate details are then replaced by placeholder text.

This option is automatically turned on for OAuth 2.0 requests and [external vault synchronization monitors](/managed/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults."). Users with access to any credentials contained in the monitor may disable it.

#### Adapt request timeout

Enable this option to edit the request timeout. Note that the default request timeout is 10 seconds, even if you do not enable this option. If the request time exceeds the specified/default timeout, the monitor will fail. Note that monitor execution time is the sum of the execution times of individual requests, and monitor timeout is 60 seconds.

## Frequency and locations

Two factors make up your monitoring schedule:

* **Frequency**âselect how frequently your HTTP monitor is executed from each location: every `1`, `2`, `5`, `10`, `15`, `30`, or `60` minutes. You can also set up your monitor to be executed [**On demand only**](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations").
* **Location** selections specify the locations from which the monitor is executed.

  HTTP monitors can be executed from our global [public](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") or [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."), or from cluster-wide locations in Dynatrace Managed.

Together, these factors determine the number of HTTP monitor executions per hour. For example, running a monitor from 3 locations every 15 minutes results in 12 executions per hour (4 times per hour from each of the 3 locations). Monitor executions are evenly spaced within the selected interval. That is, for a monitor running from 3 locations every 15 minutes, executions are triggered at 5-minute intervals.

Note that all public Synthetic locations are set to Coordinated Universal Time, or UTC. If your monitor script requires the local time or time zone, you can use the [`api.getContext()` method](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#retrieve-data "Learn how to apply pre and post scripts to your requests") and the system clock to implement conditional logic.

## Outage handling

Outage handling settings determine what to do in the event of monitor failures (availability outages). Default outage handling behavior can be defined at the environment level for all browser monitors or all HTTP monitorsâgo to **Settings** > **Web and mobile monitoring** and select the respective **Outage handling** tab. You can opt to use Dynatrace-provided defaults (**Use defaults**) to define environment-level outage handling. When enabled, these defaults apply for all browser or HTTP monitors that do not override them with monitor-level outage handling settings.

At the monitor level, this setting is available in edit mode only. The outage handling options available at the environment or the monitor level are the same. You can override the default, environment-wide settings at the monitor level. You can also restore environment-level defaults (**Remove override**).

You can disable problem generation for global and local outages if you're testing a volatile site or have scheduled downtime that you don't want to be alerted on.

* **Generate a problem and send an alert when this monitor is unavailable at all configured locations**

  This setting is enabled by default for newly created monitors. It alerts you of global availability outages, that is, when all locations experience a failure simultaneously.

  By default, a global outage problem is generated when all locations fail one time. However, you can specify the number of consecutive failures (from 1 to 5) for a global outage problem, that is, how many times all locations need to fail consecutively in order to generate a global outage problem.
* **Generate a problem and send an alert when this monitor is unavailable for one or more consecutive runs at any location**

  This allows you to raise a problem when there are consecutive failures at one or more locations. At the environment level, you can choose the number of failures. At the monitor level, you can also determine the number of monitor locations that need to fail in order to generate a local outage problem.

  In the example below, a monitor is configured for `4` locations, and a problem will be generated if `3` of those `4` locations are unable to access your site during `2` or more consecutive executions.

![Outage handling](https://dt-cdn.net/images/outagehttp-914-2e08ea40f8.png)

Outage handling

An outage problem is resolved when there are as many consecutive successful executions as the configured number of failed executions for generating the problem. The successful executions must occur on the number of locations that = the total number of locationsâthe number of locations required for the problem+1.

Note that when a global outage problem is resolved, you might still have one or more locations experiencing monitor failure. Set up local outage rules to be alerted on these.

See [Synthetic calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.") for more information on:

* The difference between [outage resolution and timeouts](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#availability-problems "Understand Synthetic Monitoring metric calculations.").
* [Excluding synthetic monitor executions during maintenance windows from availability calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring metric calculations.").

Retry on error is not available for HTTP monitors.

## Performance thresholds

Performance thresholds enable you to be proactive about site latency.

1. Turn on **Performance thresholds enabled**.
2. Select **Add new performance threshold**.
3. Select one of the requests in your monitor or **Sum of all requests**.
4. Set **Threshold value** to the threshold time in seconds. You can see the 24-hour average performance up until that point to help you set a threshold. Then select **Add threshold**.

   You can set multiple performance thresholdsâfor the monitor as a whole as well as for individual requests. Performance thresholds are defined as the **Response time** of the monitor or of individual requests.

Dynatrace generates a performance problem if a monitor at a given location violates **any** of the defined performance thresholds in 3 of the 5 most recent executions, unless there is an open maintenance window for the monitor. That is, the violations must occur at the same location. Multiple locations can have such violations and be included in a problem.

The problem is closed if the performance thresholds are not violated in the 5 most recent executions at each of the previously affected locations.

See [Synthetic calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#performance-problems "Understand Synthetic Monitoring metric calculations.") for more information.

## Related topics

* [Synthetic Monitors API](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")