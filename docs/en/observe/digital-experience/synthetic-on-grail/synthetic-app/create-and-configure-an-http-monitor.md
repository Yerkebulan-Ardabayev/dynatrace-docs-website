---
title: Create and configure an HTTP monitor
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor
scraped: 2026-02-22T21:20:24.700309
---

# Create and configure an HTTP monitor

# Create and configure an HTTP monitor

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Nov 06, 2025

You can create synthetic HTTP monitors to check the availability of your resourcesâwebsites or API endpoints. HTTP monitors can be run from our [global public](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") or [private](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") Synthetic locations.

## Create a new HTTP monitor

Go to ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** >  **Monitor** > **HTTP**.

### General

1. **Name this monitor**âenter a name (up to 500 characters) for the synthetic monitor. This name should generally describe all the requests in this HTTP monitor.
2. Select **Add tag** to manually apply tags to the monitor. After the monitor has been created, you can manage tags from the [HTTP monitor details page](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors#properties-tags "Learn about the Synthetic details page for HTTP monitors.").
3. Select **Assign frontends** to assign a monitor to a frontend application. You can assign the monitor to multiple applications, and an application can have several assigned monitors. It allows you to track application availability and performance. Detected problems are then automatically associated with your application. If the monitor is unavailable, the associated application is also considered to be unavailable.

   Note that you cannot block Synthetic Monitoring traffic for RUM applications by [excluding bots, spiders, or the IP addresses of Synthetic locations](/docs/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.").

### Requests

You can configure one or more requests in **Visual** or **Script** mode. In **Visual** mode the settings are shown in couple of groups:

* Basic configuration (request name and URL)
* Security (authentication and client certificateâfor both of them an existing credential saved in the credential vault can be selected or users can create a new one)

  + In **Security** section, turn on the **Set authentication/authorization** toggle to select the **Basic**, **NTLM** or **Kerberos** security method. For more details, see [synthetic authentication](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#basic-ntlm "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").
* SSL certificate (accept any SSL certificate and generate a problem if SSL certificate expires within the next `n` days)
* Execution attributes (HTTP method, user agent, additional HTTP headers and advanced attributes: follow redirects, ignore sensitive information, pre-/-post-execution script)
* Advanced attributes

  + **Ignore sensitive information** checkboxâexpand the **Advanced attributes** section and select this option to hide potentially sensitive information (contained in, say, the request headers, request body, sometimes URL).

    You need to do this for each request you wish to limit the display of. Request and response bodies, values of request and response headers, and peer certificate details are then replaced by placeholder text.

  Users with access to any credentials contained in the monitor may disable it.
* Constraints (response status code, response body pattern, response body regex)
* Performance thresholds alerting (threshold for this request)
* Basic configuration (request name)

  + **Name**âobligatory field which stands for a monitor step
* Target selection (URL)

  + **HTTP request URL**

    - To enhance synthetic monitor security, Dynatrace blocks monitors from sending requests to a local host (for example, `localhost` or `127.0.0.1`).
    - You can add a credential ID from the [vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") to the request URL. Use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, for example `https://example.com/api/random/{CREDENTIALS_VAULT-0000000000000000|token}` as appropriate for the type of credential you're inserting. You can only copy and paste credentials to which you have access.

      Who can edit a monitor that has associated credentials?

      * If a monitor is associated with a public credential, anyone on your team can switch on/off, delete, or edit the monitor.

      * If an HTTP monitor is associated with restricted credential (owner only or shared with a few users), any user can make changes to certain fields, even if they don't have access to the credential used. You can edit monitor name, locations, validation, thresholds, and, of course, change a certificate or a UID/password pair. You can edit and change the credentials in a URL, header value, or request body. You can create a credential within monitor settings in edit mode. You'll need to change all credentials in the monitor to ones that you have access to. Note that replacing another user's credential with one you have access to is irreversible.

        Controls that you cannot edit such as the request URL, HTTP method, pre-execution script, post-execution script, HTTP headers, request body, the follow redirects option, and adding/deleting HTTP requests are grayed out or display an error message when you attempt to save changes, whether in script or UI mode.

      * You can make active/inactive or delete a synthetic monitor that's secured by another user's owner-only credentials.

        Read more about credential permissions in [Credential vault for synthetic monitors](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
* Security (authentication and client certificateâfor both of them an existing credential saved in the credential vault can be selected or users can create a new one)

  + Turn on the **Set authentication/authorization** toggle to select the **Basic**, **NTLM** or **Kerberos** security method. For more details, see [synthetic authentication](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#basic-ntlm "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").

    Provide a username/password pair to automate the login process for password-protected sites via **Basic**, **NTLM**, or **Kerberos** authentication. Dynatrace automatically generates the required `Authorization` header with the information you've provided. (Read more about [Supported authentication methods in Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").)

    Dynatrace stores and manages all Synthetic Monitoring credentials in a credential vault. Credentials are access controlled and can be designated as owner only or public.

    You can choose an existing credential (**Select credentials**). You can only see the credentials that you have access to in this list, that is, public credentials or owner-only credentials created by you.

    You can create **New credential** by entering a **Username** and **Password**. Provide a **Credential name** and **Save to vault**.

    The `<domain>\<username>` format is not supported for the username in HTTP monitors; simply provide the `<username>`.

    The credentials you create this way are automatically set to owner-only permissions and can only be used by you. Note that you can create credentials this way in a new or existing HTTP monitor even if you don't have permissions to access credential management in the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
  + Turn on the **Add client certificate** toggle to switch on client-side certificate authentication. To learn more, see [Supported authentication methods in Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").

    Dynatrace stores and manages all Synthetic Monitoring credentials in a credential vault. Credentials are access controlled and can be designated as owner only or public.

    You can choose an existing credential (**Select credentials**). You can only see the credentials that you have access to in this list, that is, public credentials or owner-only credentials created by you.

    You can create a new credential:

    1. Select **+ New credential**.
    2. Upload a **Certificate file** (in PFX, P12, or PEM format).
    3. Enter a **Password**.
    4. Provide a **Credential name**.
    5. Select **Save to vault**.

    The credentials you create this way are automatically set to owner-only permissions and can only be used by you. Note that you can create credentials this way in a new or existing HTTP monitor even if you don't have permissions to access credential management in the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").

    To assure full mutual authentication, switch off **Accept any SSL certificate** when using certificate authentication.
* SSL certificate (accept any SSL certificate and generate a problem if SSL certificate expires within the next `n` days)

  + **Accept any SSL certificate**âby default, HTTP monitors fail when SSL certificates are invalid. Check the box to make the monitor accept any SSL certificates regardless of whether they're valid.

    Reasons for SSL certificate invalidity

    Depending on your settings, your HTTP monitor can fail or succeed when an SSL certificate is invalid for any of the following reasons:

    - Certificate is self signed
    - Certificate has expired
    - Certificate is inactive
    - Certificate lifetime is greater than 398 days
    - Missing hostname
    - Invalid/incomplete certificate chain
    - Untrusted certificate authority
    - Insecure signature algorithm

  + **Generate a problem if the SSL certificate expires within the next n days**âturn on this option to generate an **SSL certificate expiration problem** when an SSL certificate is missing, expired, or will expire within the specified number of days (must be 100 or less). Note that, this problem is generated without failing the monitor or affecting monitor availability.

    SSL certificate expiration problems have the custom severity level and display the number of days remaining until certificate expiry. This value is updated with each execution of the affected monitor.

    The following examples show how to apply the **SSL certificate expiration date verification** and **Accept any SSL certificate** settings.

    - If you want to configure a monitor that accepts a self-signed certificate while triggering an alert for certificate expiry, you would:

      * Turn on **Accept any SSL certificate**.
      * Turn on **SSL certificate expiration date verification** and set a threshold for problem generation.
    - If you choose not to accept any SSL certificate, and the SSL certificate has expired, the HTTP monitor will fail and trigger an outage problem with an `SSL certificate expired` message in problem details and in the **Events** and **Failed requests** cards in [HTTP monitor details](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.").
    - If you turn on both these options, and the SSL certificate has expired, the HTTP monitor will trigger an SSL certificate expiration problem. The **Events** card will display a custom alert for SSL certificate expiration.
    - If you turn on both these options and specify a threshold of `n` days for SSL certificate expiry, and the SSL certificate expires within `n` days, the HTTP monitor will trigger an SSL certificate expiration problem. The **Events** card will display a custom alert for SSL certificate expiration.

      HTTP monitor validation

      The following types of rules are evaluated for HTTP monitor validation in the `validation.rules` section in [script mode](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

      * Response status code validation
      * Text validation, where the first 50 KB of the response body is checked for a string of text or a regular expression
      * SSL certificate expiry validation (ActiveGate version 1.235+)

      In a monitor containing multiple validations, all rules are evaluated. However, a single execution status is returned based on priority: HTTP status code validation is the most important, followed by text and regular expression validation, and finally by SSL certificate expiry validation.
* Execution attributes (HTTP method, user agent, additional HTTP headers and advanced attributes: follow redirects, ignore sensitive information, pre-/-post-execution script)

  + **HTTP request method**

    For each request you create or edit, start with the **HTTP method**, because the available request settings depend on this selection. Supported HTTP methods are:

    - GET
    - POST
    - PUT
    - DELETE
    - HEAD
    - PATCH
    - OPTIONS
  + Optional [**User agent**ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

    The default user agent is in the format `DynatraceSynthetic/{version}`, where `{version}` is the current version of the Synthetic engine executing the monitor. Even if you define a custom user agent, Dynatrace automatically appends `DynatraceSynthetic/{version}` to the user agent to make sure that synthetic monitoring traffic can be identified. **Do not** use `DynatraceSynthetic/` in your custom user agent; this is reserved for Dynatrace use.

  + **Set additional HTTP headers**

    The monitor is created with a bare minimum set of headers required by the protocol. Choose this option to create custom/additional headers:

    1. Select **+ HTTP header**.
    2. Enter **Header name** and **Header value**.
    3. Add another header by clicking **+ HTTP header** as needed.

    Use HTTP headers to implement bearer or token authenticationâread more in [Supported authentication methods in Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#bearer-token "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.").

    You can add token credentials to the header value. Use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, for example `{CREDENTIALS_VAULT-0000000000000000|token}` as appropriate for the type of credential you're inserting. You can only copy and paste credentials to which you have access.

    Default HTTP headers

    These are the default headers Dynatrace creates per request.

    Name

    Value

    `Accept`

    `*/*`

    `Connection`

    `close`

    `Host`

    `<hostname>`

    `User-Agent`

    `DynatraceSynthetic/{version}`[1](#fn-1-1-def)

    1

    `{version}` is the current version of the Synthetic engine executing the monitor. Even if you [define a custom user agent](#basic-settings), Dynatrace always automatically adds `DynatraceSynthetic/{version}` to the user agent to make sure that synthetic monitoring traffic can be identified.

    Dynatrace also creates the `x-Dynatrace-Tenant`, and `x-Dynatrace-Test` headers for internal administrative purposes.
  + **Set request body**

    You can send a payload with your **POST**, **PUT**, **DELETE**, and **PATCH** requests. You can add token credentials to the request body. Use the format `{<credential ID>|token}`, `{<credential ID>|username}`, or `{<credential ID>|password}`, for example `{CREDENTIALS_VAULT-0000000000000000|token}` as appropriate for the type of credential you're inserting. You can only use credentials to which you have access, that is, public credentials or owner-only credentials created by you. If this field contains an [owner-only token](/docs/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault."), it cannot be edited by other users.
* Advanced attributes

  + **Follow redirects**âby default, an HTTP monitor follows up to 10 redirects from an original request until it reaches the final destination. Turn this option off to monitor only the first response of the redirect chain, for example, to check redirect response status codes.
  + **Set pre-execution script**â[pre- and post-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") allows you to add custom logic between HTTP monitor requests to do things like parsing the response, modifying the request URL, or skipping requests under certain conditions.

    If you choose this, an edit box is displayed for you to enter a script that is executed just before the request is triggered. Pre-execution scripts are based on custom JavaScript code and can be used to build your HTTP request or to add logic that you cannot or do not want to implement in the UI.

    For more information and a method reference, see [Pre- and post-execution scripts for HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#methods "Learn how to apply pre and post scripts to your requests"). Note that some methods are only available for use in [pre-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#pre-execution "Learn how to apply pre and post scripts to your requests") or [post-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#post-execution "Learn how to apply pre and post scripts to your requests").
  + **Set post-execution script**âif you choose this, an edit box is displayed for you to enter a script that is executed after the request is completed. Post-execution scripts are based on custom JavaScript code and can be used process responses to the request.

    The [`api.fail()` method](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#end "Learn how to apply pre and post scripts to your requests") can be used to define a custom **Failure message** that appears in the Events card on the [HTTP monitor details page](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.").

    For more information and a method reference, see [Pre- and post-execution scripts for HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests"). Note that some methods are only available for use in [pre-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#pre-execution "Learn how to apply pre and post scripts to your requests") or [post-execution scripts](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#post-execution "Learn how to apply pre and post scripts to your requests").
  + **Ignore sensitive information**âselect this option to hide potentially sensitive information (contained in, say, the request headers, request body, sometimes URL).
* Constraints (response status code, response body pattern, response body regex)

  Response validation allows you to pass/fail your monitor based on expected content in the first 50 KB of the response body.

  + **Pass if** or **Fail if** determines the basic test.
  + **Text contains** specifies the text to look for in the response. This string is case sensitive. If your string contains non-ASCII characters, escape them in [script mode](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").
  + **Interpret content match as regular expression** treats the specified text as a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

  You can add two or more constraints of the same type, for example, if your case requires finding two or more patterns within the response body.

  You can set up multiple such text-validation rules in [script mode](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

  HTTP monitor validation

  The following types of rules are evaluated for HTTP monitor validation in the `validation.rules` section in [script mode](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.").

  + Response status code validation
  + Text validation, where the first 50 KB of the response body is checked for a string of text or a regular expression
  + SSL certificate expiry validation (ActiveGate version 1.235+)

  In a monitor containing multiple validations, all rules are evaluated. However, a single execution status is returned based on priority: HTTP status code validation is the most important, followed by text and regular expression validation, and finally by SSL certificate expiry validation.
* Performance thresholds alerting (threshold for this request)

  You can use the **Generate a problem and send an alert on performance threshold violations** toggle to set up the timeout threshold for this particular request of the HTTP monitor. The problems triggering and alerting in case of violating performance threshold must be additionlly set when configuring [Outage and performance](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor#outage-and-performance "Learn how to set up and edit an HTTP monitor to check the performance and availability of your site.").

In **Visual** mode, you can also:

* Select  icon and drag it up or down to change the order of requests.
* Select  icon and delete the request.
* Select  icon and duplicate the request.

### Frequency and locations

Two factors make up your monitoring scheduleâhow frequently your browser monitor runs and the number of locations it's executed from.

Dynatrace offers a global network of [public Synthetic Monitoring locations](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") out-of-the-box. You can also [create private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") within your own network infrastructure. Both public and private locations appear on this settings page.

The frequency and number of locations determine the number of monitor executions per hour. For example, running a monitor from 3 locations every 15 minutes results in 12 executions per hour (4 times per hour from each of the 3 locations). Monitor executions are evenly spaced within the selected interval. That is, for a monitor running from 3 locations every 15 minutes, executions are triggered at 5-minute intervals.

You can choose a frequency of every **5**, **10**, **15**, or **30** minutes; or **1**, **2**, or **4** hours. You can also set up your monitor to be executed [**On demand only**](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations"). You can select multiple global locations from where your browser monitor is to be executed.

Note that all public Synthetic locations are set to Coordinated Universal Time, or UTC. If your monitor script requires the local time or time zone, you can use the [`api.getContext()` method](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#retrieve-data "Learn about the event types created when recording a browser clickpath.") and the system clock to implement conditional logic.

### Outage and performance

You can set global and local **Outage handling** and **Performance thresholds** for the sum of all requests.

* **Generate a problem and send an alert when this monitor is unavailable at all configured locations (global outage).**

  This setting is enabled by default for newly created monitors. It alerts you of global availability outages, that is, when all locations experience a failure simultaneously.

  By default, a global outage problem is generated when all locations fail one time. However, you can specify the number of consecutive failures (from 1 to 5) for a global outage problem, that is, how many times all locations need to fail consecutively in order to generate a global outage problem.
* **Generate a problem and send an alert when this monitor is unavailable for one or more consecutive runs at any location. Local outage problem generation is available only when at least two locations are assigned.**

  This allows you to raise a problem when there are consecutive failures at one or more locations. At the environment level, you can choose the number of failures. At the monitor level, you can also determine the number of monitor locations that need to fail in order to generate a local outage problem.

For **Performance thresholds**, you can turn on:

* **Generate a problem and send an alert on performance threshold violations.**

  This setting provides an option to set the **Threshold for the sum of all requests (in seconds)**. If the threshold exceeds the time you provided, you'll be notified.

### Summary

See the summary of all the steps and the estimated monthly number of requests.

See [HTTP monitors reporting results](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.") for monitoring analytics of each monitor.

## Related topics

* [HTTP monitors reporting results](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.")
* [Synthetic Monitors API](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")