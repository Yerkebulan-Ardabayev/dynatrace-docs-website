---
title: Script mode for browser monitor configuration
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration
scraped: 2026-05-12T11:32:27.220122
---

# Script mode for browser monitor configuration

# Script mode for browser monitor configuration

* How-to guide
* 2-min read
* Published Sep 19, 2018

In addition to the usual configuration in the UI, you can use **Script** mode to configure your [clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") or [single-URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.") monitors. In this mode, you can access the underlying JSON script of your monitor. If you're a synthetic power user, this will make your life a lot easier and allow you to speed up clickpath creation and management. Use the script editor to quickly find specific events (steps), adapt locators across the whole script, or edit parts of the clickpath without rerecording.

You aren't limited to just one modeâyou can switch back and forth between the UI and script modes by clicking the **Clickpath**/**Script** switch.

## Access the clickpath script

To edit your clickpath browser monitor in script mode:

1. Go to **Synthetic Classic**.
2. Select the clickpath monitor you want to edit.
3. Click the **Browse** button (**â¦**) and select **Edit**.
4. Click the **Recorded clickpath** tab in the Monitor settings menu on the left.
5. Click **Script** at the top.

## Access the single-URL script

To edit your single-URL browser monitor in the script mode:

1. Go to **Synthetic Classic**.
2. Select the single-URL monitor you want to edit.
3. Click the **Browse** button (**â¦**) and select **Edit**.
4. Click the **Monitor script** tab in the in the Monitor settings menu on the left.

## Edit the script

You can download the script (**Download script as .json**) or just copy it from the editor and edit it in a text editor of your choice. However, you can also edit the script directly in the browser. This provides the following benefits:

* Autocompleteâjust press **Ctrl+Spacebar** to see a list of suggestions.
* Syntax highlighting makes it easier for you to write script code.
* Instant error validationâthe editor instantly shows a warning for any error in the script. Hover over the error to see what's wrong and a suggestion for how to fix it. You cannot save changes until the code is error free.

Note that you need to escape all special characters and break lines with a backslash (for example, a new line is `\n`, double quotes is `\"`, and tab is `\t`).

You can play your changes back for clickpath scripts without saving themâjust click **Play back clickpath**.

## Script structure

Script parameters

Script model

#### Main script object

Contains the monitor script.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configuration | [ScriptConfig](#script-config) | The [setup](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of the monitor | Optional |
| type | string | The type of monitor  Possible values are:  * `clickpath` for clickpath monitors * `availability` for single-URL browser monitors    These monitors are only allowed to have one event of the `navigate` type. | Required |
| version | string | Script versionâuse the `1.0` value here. | Required |
| events | Array of:  [navigateEvent](#navigate-event)  [interactionEvent](#interaction-event)  [javaScriptEvent](#javascript-event)  [selectOptionEvent](#select-option-event)  [cookieEvent](#cookie-event)  [keystrokesEvent](#keystrokes-event) | Steps of the clickpathâthe first step must always be of the `navigate` type.  Note that an event is not the same thing as an actionâonly events that trigger web requests are called actions, so your script might not have as many actions as events. Synthetic actions (similar to user actions for real user monitoring) hold the performance data collected during the playback of clickpath events.  The actual JSON object of the event depends on its type:  * `navigateEvent`âcontains a **Navigate** event. * `interactionEvent`âcontains a **Click** or **Tap** event. * `javaScriptEvent`âcontains a **JavaScript** event. * `selectOptionEvent`âcontains a **Select option** event. * `cookieEvent`âcontains a **Cookie** event. * `keystrokesEvent`âcontains a **Keystroke** event. | Required |

#### The `ScriptConfig` object

Contains the [setup](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") of the monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| userAgent | string | The [user agentï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) of the request | Optional |
| device | [customDevice](#custom-device)  or  [predefinedDevice](#predefined-device) | The emulated device of the monitorâholds either the parameters of the custom device or the name and orientation of the preconfigured device.  If not set, then the `Desktop` preconfigured device is used. | Optional |
| bandwidth | [bandwidthOptions](#bandwidth-options)  or  [predefinedBandwidth](#predefined-bandwidth) | The emulated network conditions of the monitor  If not set, then the full available bandwidth is used. | Optional |
| requestHeaders | [requestHeader[]](#request-header) | The list of HTTP headers to be sent with requests of the monitor | Optional |
| cookies | [requestCookie[]](#request-cookie) | List of cookies to be created for the monitor  These cookies are added before execution of the first step. | Optional |

#### The `customDevice` object

Contains the emulated device of the monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| mobile | boolean | The flag of the mobile device  Set to `true` for mobile devices or `false` for a desktop or laptop. | Required |
| touchEnabled | boolean | The flag of the touchscreen  Set to `true` if the device uses touchscreen. In that case, use can set interaction event as `tap`. | Required |
| width | integer | The width of the screen in pixels  The maximum allowed width is `1920`. | Required |
| height | integer | The height of the screen in pixels  The maximum allowed height is `1080`. | Required |
| scaleFactor | integer | The pixel ratio of the device | Optional |

#### The `predefinedDevice` object

Contains one of the preconfigured device emulations.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| deviceName | string | The name of the preconfigured deviceâwhen editing in the browser, press `Crtl`+`Spacebar` to see the list of available devices. | Required |
| orientation | string | The orientation of the deviceâ`portrait` or `landscape`  Desktop and laptop devices are not allowed to use the `portrait` orientation. | Required |

#### The `bandwidthOptions` object

Contains the emulated network conditions of the monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| latency | integer | The latency of the network, in milliseconds | Required |
| download | integer | The download speed of the network, in bytes per second | Required |
| upload | integer | The upload speed of the network, in bytes per second | Required |

#### The `predefinedBandwidth` object

Contains the pre-configured network emulations.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| networkType | string | The type of the preconfigured networkâwhen editing in the browser, press `Crtl`+`Spacebar` to see the list of available networks. | Required |

#### The `requestHeader` object

Contains the list of HTTP headers to be sent with requests of the monitor.

The following headers are not allowed:

* user-agent
* cookie

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The name of the HTTP header | Required |
| value | string | The value of the HTTP header | Required |

#### The `requestCookie` object

Contains the list of cookies to be created for the monitor.

Every cookie must be unique within the list. However, you can use the same cookie again in other event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The name of the cookie  The following cookie names are not allowed:  * `dtCookie` * `dtLatC` * `dtPC` * `rxVisitor` * `rxlatency` * `rxpc` * `rxsession` * `rxvt` | Required |
| value | string | The value of the cookieâthe following symbols are not allowed: `;,\"`. | Required |
| domain | string | The domain of the cookie | Required |
| path | string | The path to the cookie | Optional |

#### The `navigateEvent` object

Contains a **Navigate** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of synthetic event  In this case, the event type is `navigate`. | Required |
| url | string | The URL to navigate to | Required |
| description | string | A short description of the event to appear in the UI | Required |
| wait | [waitCondition](#wait-condition) | The wait condition for the eventâdefines how long Dynatrace should wait before the next action is executed. | Optional |
| validate | [validationType[]](#validation-type) | The validation rule for the eventâhelps you verify that your browser monitor loads the expected page content or page element. | Optional |
| target | [targetType](#target-type) | The tab on which the page should open | Optional |
| authentication | [plainAuthenticationType](#plain-authentication-type) or [secureAuthenticationType](#secure-authentication-type) | The login credentials to bypass the browser login mask | Optional |

#### The `interactionEvent` object

Contains a **Click** or a **Tap** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of synthetic event  In this case, `click` or `tap` | Required |
| description | string | A short description of the event to appear in the UI | Required |
| button | integer | The mouse button to be used for the click | Required |
| wait | [waitCondition](#wait-condition) | The wait condition for the eventâdefines how long Dynatrace should wait before the next action is executed. | Optional |
| validate | [validationType[]](#validation-type) | The validation rule for the eventâhelps you verify that your browser monitor loads the expected page content or page element. | Optional |
| target | [targetType](#target-type) | The element to click/tap on | Optional |

#### The `javaScriptEvent` object

Contains a **JavaScript** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of synthetic event  In this case, `javascript` | Required |
| description | string | A short description of the event to appear in the UI | Required |
| javaScript | string | The JavaScript code to be executed in this event | Required |
| wait | [waitCondition](#wait-condition) | The wait condition for the eventâdefines how long Dynatrace should wait before the next action is executed. | Optional |
| target | [targetType](#target-type) | The tab where the JavaScript code is executed | Optional |

#### The `selectOptionEvent` object

Contains a **Select option** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of synthetic event  In this case, `selectOption` | Required |
| description | string | A short description of the event to appear in the UI | Required |
| selections | [listOptions[]](#list-options) | The options to be selected | Required |
| wait | [waitCondition](#wait-condition) | The wait condition for the eventâdefines how long Dynatrace should wait before the next action is executed. | Optional |
| validate | [validationType[]](#validation-type) | The validation rule for the eventâhelps you to verify that your browser monitor loads the expected page content or page element. | Optional |
| target | [targetType](#target-type) | The selection tag of the dropdown list | Optional |

#### The `cookieEvent` object

Contains a **Cookie** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | `cookie` | Required |
| description | string | A short description of the event to appear in the UI | Required |
| cookies | [requestCookie[]](#request-cookie) | The list of cookies to be created during the event  Every cookie must be unique within the list. However, you can use the same cookie again in other event. | Required |

#### The `keystrokesEvent` object

Contains a **Keystroke** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | `keystrokes` | Required |
| description | string | A short description of the event to appear in the UI | Required |
| textValue | string | The text to enter | Required |
| masked | boolean | Indicates whether the **textValue** is encrypted (`true`) or not (`false`). | Required |
| simulateBlurEvent | boolean | Defines whether to blur the text field when it loses focus.  Set to `true` to trigger the blur the `textValue`. | Required |
| wait | [waitCondition](#wait-condition) | The wait condition for the eventâdefines how long Dynatrace should wait before the next action is executed. | Optional |
| validate | [validationType[]](#validation-type) | The validation rule for the eventâhelps you to verify that your browser monitor loads the expected page content or page element. | Optional |
| target | [targetType](#target-type) | The object to enter the text to | Optional |

#### The `waitCondition` object

Contains the wait condition for an event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| waitFor | string | The time to wait before the next event is triggered  Possible values are:  * `page_complete`âwait for the page to load completely. * `network`âwait for background network activity to complete. * `next_action`âwait for the next action. * `time`âwait for specific period of time. * `validation`âwait for a specific element to appear. | Required |
| milliseconds | integer | The time to wait, in milliseconds  The maximum allowed value is `60000`. | Required for the `time` type  Not applicable otherwise |
| timeoutInMilliseconds | integer | The maximum amount of time to wait for a certain element to appear, in millisecondsâif exceeded, the action is marked as failed.  The maximum allowed value is `60000`. | Required for the `validation` type  Not applicable otherwise |
| validation | [validationType[]](#validation-type) | The element to wait for | Required for the `validation` type  Not applicable otherwise |

#### The `validationType` object

Contains the validation rule for an event or waiting rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The goal of the validation:  * `content_match`âcheck page for the specific content. Not allowed for validation inside of wait condition. * `element_match`âcheck page for the specific element. | Required |
| match | string | The content to look for on the page  Regular expressions are allowed. In that case set **isRegex** as `true`. | Required for `content_match`  Optional for `element_match` |
| isRegex | boolean | Defines whether **match** is a plain text (`false`) or regular expression (`true`). | Optional |
| failIfFound | boolean | The condition of the validation:  * `false`âvalidation *succeeds* if the specified content/element is found. * `true`âvalidation *fails* if the specified content/element is found. | Required |
| target | [targetType](#target-type) | The element to look for on the page | Required for `element_match`  Optional for `content_match` |

#### The `plainAuthenticationType` object

Plain login credentials to bypass the browser login mask during a **Navigate** event

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of authenticationâ`http_authentication` or `webform`.  `webform` authentication type is not allowed in clickpath monitors. | Optional |
| username | string | The username to log in with. | Required |
| password | string | The password to log in with.  It contains not the actual password, but a unique ID of it, and the password itself is stored in Dynatrace and found by the ID. If you change the ID, the stored password becomes unavailable.  To change the password, set the **masked** property as `false` and type in the new password. | Required |
| masked | boolean | The flag of the masked password  `true` means that the password is encrypted and stored, and the **password** field shows the ID of the password to encrypt the password.  Set `false` to type in a new password. | Optional |

#### The `secureAuthenticationType` object

The login credentials to bypass the browser login mask during a **Navigate** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | The type of authenticationâ`http_authentication`, `webform`, or `kerberos`.  `webform` authentication type is not allowed in clickpath monitors. | Optional |
| credential | [credentialType](#credential-type) | The credential object that contains the username and password. | Required |
| domain | string | Kerberos domain. | Required for `kerberos` |
| authServerAllowlist | string | List of allowed servers for kerberos authentication. Wildcards can be used. Exact details are provided in the [Chrome Enterprise documentationï»¿](https://dt-url.net/p803wkm). | Required for `kerberos` |

#### The `credentialType` object

The credentials from the credential vault.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| id | string | The ID of the credentials in the credential vault. | Required |
| credentialField | string | The type of authenticationâ`username` or `password`. | Optional |

#### The `listOptions` object

Contains the options to be selected in the **Select option** event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| index | integer | The index of the option to be selected | Required |
| value | string | The value of the option to be selected | Required |

#### The `targetType` object

Contains the target tab or element of the event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| window | string | The tab of the target | Optional |
| locators | [locatorType[]](#locator-type) | The list of locators identifying the desired element | Optional |

#### The `locatorType` object

Contains an element of a page to look for.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines where to look for the element:  * `css`âin CSS selector * `dom`âin JavaScript code | Required |
| value | string | The name of the element to be found | Required |

This is a model of the script JSON, showing all the possible elements. It has to be adjusted to be used as an actual script. To get an example of a real monitor, you can check the script of an existing monitor.

```
{



"configuration": {



"userAgent": "string",



"device": {



"mobile": true,



"touchEnabled": true,



"width": 375,



"height": 667,



"scaleFactor": 2,



"deviceName": "string",



"orientation": "portrait"



},



"bandwidth": {



"latency": 1,



"download": 1,



"upload": 1,



"networkType": "WiFi"



},



"requestHeaders": {



"addHeaders": [



{



"name": "string",



"value": "string"



}



],



"toRequests": ["string"]



},



"cookies": [



{



"name": "string",



"value": "string",



"domain": "string",



"path": "string"



}



]



},



"version": "1.0",



"type": "clickpath",



"events": [



{



"type": "navigate",



"url": "string",



"description": "string",



"wait": {



"waitFor": "page_complete"



},



"authentication": {



"type": "basic",



"masked": true,



"username": "string",



"password": "string"



},



"validate": [



{



"type": "content_match",



"failIfFound": true,



"isRegex": false,



"match": "string"



}



],



"target": {



"window": "string"



}



},



{



"type": "click",



"description": "string",



"button": 0,



"wait": {



"waitFor": "network"



},



"target": {



"locators": [



{



"type": "css",



"value": "string"



},



{



"type": "dom",



"value": "string"



}



]



},



"validate": [



{



"type": "element_match",



"failIfFound": false,



"target": {



"locators": [



{



"type": "css",



"value": "string"



}



]



}



}



]



},



{



"type": "javascript",



"description": "string",



"javaScript": "string",



"wait": {



"waitFor": "time",



"milliseconds": 2000



},



"target": {



"window": "string"



}



},



{



"type": "selectOption",



"description": "string",



"selections": [



{



"index": 1,



"value": "string"



}



],



"wait": {



"waitFor": "validation",



"validation": {



"type": "element_match",



"failIfFound": false,



"match": "string",



"target": {



"locators": [



{



"type": "dom",



"value": "string"



}



]



}



},



"timeoutInMilliseconds": 60000



}



},



{



"type": "cookie",



"description": "string",



"cookies": [



{



"name": "string",



"value": "string",



"domain": "string",



"path": "string"



}



]



},



{



"type": "keystrokes",



"description": "string",



"textValue": "string",



"masked": false,



"simulateBlurEvent": true,



"wait": {



"waitFor": "next_action"



}



}



]



}
```