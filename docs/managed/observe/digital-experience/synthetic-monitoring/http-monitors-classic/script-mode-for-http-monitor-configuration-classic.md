---
title: Script mode for HTTP monitor configuration in Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic
---

# Script mode for HTTP monitor configuration in Classic

# Script mode for HTTP monitor configuration in Classic

* How-to guide
* 1-min read
* Published Jul 17, 2019

In addition to the configuration in the UI (**Visual mode**), you can use **Script mode** to configure your [HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site."). In this mode, you can access the underlying JSON script of your monitor. If you're a Synthetic Monitoring Classic power user, this will make your life a lot easier and allow you to speed up monitor creation and management. Use the script editor to quickly find specific events (steps) or adapt locators across the entire script.

You aren't limited to just one mode—you can switch between the UI and script modes by selecting the **Visual mode**/**Script mode**.

## Access the script

To edit your HTTP monitor in script mode:

1. Go to **Synthetic Classic** and opt to view your monitors in list mode.
2. Select the check box next to the monitor that you want to edit > select **Edit** in the lower-left corner.
3. Select the **HTTP Requests** tab of Monitor settings on the left.
4. Select **Script mode** at the top.

## Edit the script

You can download the script (**Download script as .json**) or just copy it from the editor and edit it in a text editor of your choice. However, you can also edit the script directly in the browser. This provides the following benefits:

* Autocomplete—just press **Ctrl+Spacebar** to see a list of suggestions.
* Syntax highlighting makes it easier for you to write script code.
* Instant error validation—the editor instantly shows a warning for any error in the script. Hover over the error to see what's wrong and a suggestion for how to fix it. You cannot save changes until the code is error free.

Note that you need to escape all special characters and break lines with a backslash (for example, a new line is `\n`, double quotes is `\"`, and tab is `\t`).

## Script structure

Script parameters

Script model

#### Main script object

Contains the monitor script.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `version` | string | Script version—use the `1.0` value here. | Required |
| `requests` | Array of:  [request](#request) | A list of HTTP requests to be performed by the monitor  The requests are executed in the order in which they appear in the script. | Required |

#### The `request` object

Contains the parameters of an HTTP request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `description` | string | A short description of the event to appear in the web UI | Optional |
| `url` | string | The URL to check | Required |
| `method` | string | The HTTP method of the request | Required |
| `requestBody` | string | The body of the HTTP request—you need to escape all JSON characters.  Is set to null if the request method is GET, HEAD, or OPTIONS. | Optional |
| `validation` | [requestValidation](#validation) | The validation configuration of the request  Validation helps you verify that your HTTP monitor loads the expected content. | Optional |
| `configuration` | [requestConfiguration](#configuration) | The [setup](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#setup "Learn about configuring HTTP monitors.") of the monitor | Optional |
| `preProcessingScript` | string | The [script](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") executed before the request  You must escape all JSON characters and break lines with `/n`. | Optional |
| `postProcessingScript` | string | The [script](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests") executed after the request  You must escape all JSON characters and break lines with `/n`. | Optional |

#### The `requestValidation` object

Contains the validation configuration for the request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `rules` | Array of:  [validationRule](#validation-rule) | A list of validation rules | Optional |

The following types of rules (see [validationRule](#validation-rule)) are evaluated for HTTP monitor validation:

* Response status code validation
* Text validation, where the response body is checked for a string of text or a regular expression
* SSL certificate expiry validation

This means that the monitor will **fail** if at least one of these rules with `passIfFound` = `false` is met or at least one rule with `passIfFound` = `true` is not met.

The monitor will **succeed** if all rules with `passIfFound` = `false` are not met and all rules with `passIfFound` = `true` are met.

#### The `validationRule` object

Contains a validation rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `type` | string | The type of rule—possible values are:  * `patternConstraint`—performs a simple content match. * `regexConstraint`—interprets the content match as a [regular expression](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace."). * `httpStatusesList`—validates a list of HTTP status codes. * `certificateExpiryDateConstraint`—checks if certificate expiry is within a specified number of days. | Required |
| `passIfFound` | boolean | The validation condition:  * `true`—validation **succeeds** if the specified content/element is found. * `false`—validation **fails** if the specified content/element is found.  Always specify `false` for `certificateExpiryDateConstraint` to fail the monitor if SSL certificate expiry is within the specified number of days. | Required |
| `value` | string | The content to look for | Required |

#### The `requestConfiguration` object

Contains the [setup](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#setup "Learn about configuring HTTP monitors.") of the monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `userAgent` | string | The [**User agent**﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) of the request | Optional |
| `acceptAnyCertificate` | boolean | Accept any (`true`) or only a trusted (`false`) SSL certificate.  If set to `false`, then the monitor fails with invalid SSL certificates.  If not set, the `false` option is used. | Optional |
| `followRedirects` | boolean | Follow (`true`) or don't follow (`false`) redirects.  If set to `false`, redirects are reported as successful requests with response code `3xx`.  If not set, the `false` option is used. | Optional |
| `requestHeaders` | Array of:  [requestHeader](#header) | A list of additional headers for the request  By default, only the **User-Agent** header is set.  You can't set or modify this header here. Use the `userAgent` field for that. | Optional |

#### The `requestHeader` object

Contains an HTTP header of the request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| `name` | string | The key of the header | Required |
| `value` | string | The value of the header | Required |

This is a model of the script JSON, showing all the possible elements. It has to be adjusted to be used as an actual script. To see an example script of a real monitor, you can check any existing HTTP monitor in script mode.

```
{



"version": "1.0",



"requests": [



{



"description": "string",



"url": "string",



"method": "POST",



"requestBody": "{\n\"customParameter1\": \"customValue1\",\n\"customParameter2\": true,\n\"customParameter3\": 452\n}",



"validation": {



"rules": [



{



"type": "patternConstraint",



"passIfFound": true,



"value": "string"



},



{



"type": "regexConstraint",



"passIfFound": true,



"value": "string"



}



],



"rulesChaining": "or"



},



"configuration": {



"userAgent": "string",



"acceptAnyCertificate": false,



"followRedirects": true,



"requestHeaders": [



{



"name": "string",



"value": "string"



}



]



},



"preProcessingScript": "string",



"postProcessingScript": "string"



}



]



}
```