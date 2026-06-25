---
title: Configure Real User Monitoring to capture XHR actions
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions
scraped: 2026-05-12T11:34:19.573016
---

# Configure Real User Monitoring to capture XHR actions

# Configure Real User Monitoring to capture XHR actions

* How-to guide
* 9-min read
* Updated on Apr 29, 2026

Modern web applications don't rely on page loads to change the UI after user input. Instead, each user interaction triggers one or more XHRs to get the necessary data, thus changing only parts of the UI. When you activate XHR-action support, you add visibility into each kind of user interaction, not just the regular page loads that are captured by default. This option significantly extends visibility in single-page application (SPA) environments built on top of various JavaScript frameworks.

## Supported JavaScript frameworks

We offer special support for [Angular 2â16](#enable-angular-12-16-support). For Angular 17+, [additional configuration is required](#enable-angular-17-support). If another JavaScript framework is used for your application, try [activating generic support](#enable-generic-js-frameworks).

End of special support for certain JavaScript frameworks

We stopped providing special support for the following JavaScript frameworks with the release of RUM JavaScript version 1.265 and Dynatrace version 1.266.

| JavaScript frameworks | Versions |
| --- | --- |
| AngularJS | 1.0 - 1.7 |
| Angular with SystemJS | 2 - 15 |
| Dojo | 1.6.1 - 1.13 |
| Ext JS | 3.4, 4, 5, 6 |
| ICEfaces | 1.8, 2, 3 |
| jQuery ( Backbone.js ) | 1.3 - 1.12, 2.0 - 2.2, 3.0 - 3.6 |
| MooTools | 1.4.5 - 1.6.0 |
| Prototype | 1.7 |
| Sencha Touch | 2.0 - 2.4 |

If you're using one of these frameworks, [activate the generic support](#enable-generic-js-frameworks).

Also, if you created your environment before Dynatrace version 1.266, you can use a version of the RUM JavaScript that offers special support for your framework.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **RUM JavaScript updates**.
5. Select the **Latest IE7-10 supported** option from the dropdown list.

## Activate support for Angular 2â16

If Angular 17+ is used for your application, follow the instructions in [Activate support for Angular 17+](#enable-angular-17-support) instead.

To enable support for Angular 2â16

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Async web requests and SPAs**.
5. Under **JavaScript framework support**, turn on the **Angular** toggle.
6. Angular 12+ Enter the Angular package name.

   What is an Angular package name?

   Starting with Angular version 12, you must specify your application's Angular package name in the Dynatrace settings. Otherwise, Real User Monitoring won't work.

   For Angular 12, the package name depends on the project name and is no longer static, while for Angular 11 and earlier, the package name is always `webpackjsonp`.

   To find the Angular package name for your application

   1. Open your browser's developer tools, and go to the **Console** tab.
   2. Start entering `webpackChunk`. The browser should display the package name for your Angular application. Copy that name.  
      For example, the package name on the screenshot below is `webpackChunklite`.

      ![Finding the Angular package name in the browser console](https://dt-cdn.net/images/find-angular-package-name-1918-f04cb24a1a.png)

      Finding the Angular package name in the browser console

      If you see multiple `webpackChunk` entries in the console, choose the one that matches your application's name. Also, try disabling your browser extensions to get a cleaner list.
      If there are no `webpackChunk` entries in the console, you're probably using Angular version 11 or earlier. In this case, you do not need to specify the Angular package name.
   3. Paste the name copied in step 2 to the **Angular package name** field in your application settings.

## Activate support for Angular 17+

As Angular 17 uses esbuild instead of Webpack by default, the RUM JavaScript can no longer automatically instrument Angular. For this reason, if Angular 17+ is used for your application, note that additional configuration is required.

To enable support for Angular 17+, perform the following actions.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Activate generic JavaScript framework support**](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-config-web-ui "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Implement exception capture**](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-exception-capture "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Set up page group detection**](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-page-group-detection "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")

### Step 1 Activate generic JavaScript framework support

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Async web requests and SPAs**.
5. Under **JavaScript framework support**, turn off the **Angular** toggle.
6. Under **Generic support**, turn on the required options.

   * Turn on **Capture fetch() requests** to capture user action data for requests based on the [Fetch API](/managed/observe/digital-experience/rum-concepts/user-actions#fetch-api "Learn what user actions are and how they help you understand what users do with your application.").
   * Turn on **Capture XmlHttpRequest (XHR)** to capture any interaction that leads to an XmlHttpRequest call as an XHR action.

### Step 2 Implement exception capture

Angular has a default exception handler ([`ErrorHandler`ï»¿](https://angular.io/api/core/ErrorHandler)) that catches exceptions and logs them to the `console` using `console.error`. However, a custom exception handler is sometimes used to intercept error handling.

#### Default exception handler

If the default exception handler is used, enable console error capture so that the RUM JavaScript can capture exceptions for your Angular 17+ applications.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Custom configuration properties**.
5. Select **Add a custom configuration property** and enter `cce=1`.

   `cce` stands for *capture console error*. When this option is enabled, the RUM JavaScript reports the first `Error` object or string that it can find in the arguments passed to the `console.error`.

#### Custom exception handler

If you have a custom exception handler and exceptions aren't logged to the `console`, you need to report exceptions manually.

```
export class CustomErrorHandler implements ErrorHandler {



handleError(error: any): void {



// Report the error



window.dtrum?.reportError(error);



// custom error handling



}



}



@NgModule({



...,



providers: [{provide: ErrorHandler, useClass: CustomErrorHandler}]



})
```

### Step 3 Set up page group detection

The default [page and page group detection](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.") is based on URLsânamely, on the paths and IDs that Dynatrace automatically detects. If the out-of-the-box page grouping is incorrect or you want to modify it, you can manually report page groups using the Angular Router. The sample code below can be used to retrieve the page group from the `routeConfig` where placeholder names are still available (for example, `/journey/:id` instead of `/journey/1235`).

```
@NgModule({



imports: [RouterModule.forRoot(routes)],



exports: [RouterModule]



})



export class AppRoutingModule {



constructor(private router: Router) {



window.dtrum?.enableManualPageDetection();



this.router.events.subscribe((value: Event) => {



if (value.type === EventType.ActivationEnd) {



const snapshot = value.snapshot;



if (snapshot.routeConfig) {



const group = snapshot.routeConfig.path;



const name = snapshot.url.join("/");



window.dtrum?.setPage({



name,



group



});



}



}



});



}



}
```

See also [Define your own page grouping](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups#configure-page-grouping "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.").

### `dT_.initAngularNg()`

Don't call `dT_.initAngularNg()`, as it no longer works with Angular 17. Doing it doesn't break anything, but it also has no effect.

For Angular 2â16, `dT_.initAngularNg` is used to pass HTTP and Headers objects to Dynatrace when using `HttpModule` from @angular/http or to pass the HTTP and HttpHeaders objects to Dynatrace when using `HttpClientModule` from @angular/common/http (Angular 5+).

## Activate generic JavaScript framework support

If your application uses a JavaScript framework other than Angular, enable generic support for XHR and fetch() web requests.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Async web requests and SPAs**.
5. Under **Generic support**, turn on the required options:

   * Turn on **Capture fetch() requests** to capture user action data for requests based on the [Fetch API](/managed/observe/digital-experience/rum-concepts/user-actions#fetch-api "Learn what user actions are and how they help you understand what users do with your application.").
   * Turn on **Capture XmlHttpRequest (XHR)** to capture any interaction that leads to an XmlHttpRequest call as an XHR action.

## Enable timed action support

Depending on the XHR (AJAX) framework or architecture of your application, you may additionally need to enable the timed action support setting. This setting is necessary when an application doesn't trigger XHR (AJAX) calls directly in event handlers of HTML elements but instead defers them via `SetTimeout` calls.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Content capture**.
5. Enable **Timed action support**.

## Exclude specific XHR calls from monitoring

When your application issues an XHR or Fetch request, it can be captured in one of the following ways:

* When no other user action is currently active and the XHR was triggered by a user interaction, a standalone XHR action is captured.
* When another user action is currently active and the XHR was not triggered by a user interaction, the active user action is extended to include the XHR's duration.

You can exclude specific XHR calls from monitoringâfor example, if your application sends frequent status-based XHR calls that you don't want to see in your user data. When you exclude these requests:

* No standalone XHR actions are captured.
* Excluded XHRs do not extend the duration of other user actions. However, they might still appear in the [waterfall analysis](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") if W3C resource timing support is active (application settings > **Capturing** > **Content capture** > **W3C resource timing support**).

### Configure XHR exclusion rules

To exclude XHR calls from monitoring

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Exclusions** > **XHR exclusions**.
5. Select **Add an XHR exclusion rule**, and specify a JavaScript regular expression that matches the URLs of the requests you want to exclude.

Avoid inefficient regular expressions

Inefficient regular expressions can cause performance issues in your application, including browser freezes lasting several seconds. For better performance, write expressions that match a URL substring rather than the entire URL. This is especially relevant for long URLs.

### How XHR exclusion rules are applied

The RUM JavaScript tests the regular expression against the URL using [`RegExp.prototype.test()`ï»¿](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test). The regular expression does not need to match the full URL, but only a substring of it. The URL can be relative or absolute, depending on what was passed to the XHR or Fetch call. Matching is case-insensitive, and forward slashes (`/`) do not need to be escaped.

Regex tester sites

When composing your regular expression using a site like [Regex101ï»¿](https://regex101.com/), select the following options:

* The flavor **ECMAScript (JavaScript)**
* The delimiter `"`
* The **Case insensitive match** flag

## Missing XHR actions when promises are used

When [promisesï»¿](https://web.dev/promises/) are used, Dynatrace does not always create user actions, so you might notice that some XHR actions are missing.

How Dynatrace usually creates user actions:

1. A user interaction with a pageâfor example, a click, keypress, or scroll eventâis registered.
2. If an XHR or fetch request starts during the next 30 milliseconds, a user action is created. If a request starts later than that, a user action is not created.

The 30-ms timeframe is extended indefinitely for an ongoing synchronous execution, for example, when a long calculation in the application code takes more than 30 ms and an XHR starts only after the calculation is completed. However, this only applies when the execution is done directly in the event handler and `setTimeout`, `setInterval`, or promises are not used.

Using promises, code can be executed asynchronously. When code execution is completed, the original caller is notified and can continue with its own code execution. Unfortunately, it's impossible to determine when code execution will be finished; it may or may not occur within the 30-ms window. For this reason, we recommend that you use the [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") to create actions in such cases.

To check if a user action uses promises

1. Open your browser's developer tools.
2. Perform an action in your web application.
3. Check the initiator of the request.

   ![Check if a user action uses promises in browser's developer tools](https://dt-cdn.net/images/promise-then-2446-542a8c167e.png)

   Check if a user action uses promises in browser's developer tools