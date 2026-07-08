---
title: Pre- and post-execution scripts for HTTP monitors in Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic
---

# Pre- and post-execution scripts for HTTP monitors in Classic

# Pre- and post-execution scripts for HTTP monitors in Classic

* Explanation
* 9-min read
* Updated on Apr 13, 2022

When executing a complex API monitor, pre- and post-execution scripts enable you to add logic before/after the HTTP monitor requests (for example, to skip a request under certain conditions, add a header, modify body content, or modify a URL). The scripts are based on custom JavaScript code that runs before and/or after each HTTP request is executed. You can also set values in your scripts and pass them as variables between requests.

## Define pre- and post-execution scripts

In edit mode, enable pre- or post-script execution in the request to display the code editor. As you type, the editor displays inline help with short descriptions of the available methods after you type the objects `api`, `request` (for pre-execution scripts), or `response` (for post-execution scripts).

You can also add scripts using [script mode](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.")—simply add the script as the value of the `preProcessingScript` or `postProcessingScript` keys. However, with this approach, you will not be able to use the inline method helper and will need to escape all special characters and break lines with a backslash (for example, a new line is `\n`, double quotes is `\"`, and tab is `\t`).

The `api` object can be used in pre- or post-execution scripts to store and retrieve variables, perform cryptographic functions, log data, skip other requests, and many other functions. Pre-execution scripts use the `request` object to add or modify the current HTTP request's parameters (for example, the URL, header values, and request body). Post-execution scripts use the `response` object to access the response body, headers, and status code of the current HTTP request after a response is received.

Pre- and post-execution scripts have direct access only to the data retrieved as the result of the current request. In other words, the response details are available only within the same request’s post-execution script. To pass the information to a different request within the same monitor, use a [variable](#variables) instead.

## Passing variables

Variables can be passed only in the context of a single execution of an HTTP monitor. You also need to make sure that when you refer to a variable, the data behind it is logically available to the monitor. For example, if you set a variable based on data from the response body of a request, you cannot retrieve the value in the pre-execution script for that request, because at this point, the content does not exist yet.

After you set a global variable using the `api.setValue()` method, you can apply its value using the `{variable_name}` convention with `api.getValue()` or `api.getValues()` in subsequent pre- or post-execution scripts. [See the example below](#variables-example) on how to set a variable and retrieve it using `api.setValue()` and `api.getValue()`.

You can also apply the value of a variable previously set using `api.setValue()` in subsequent HTTP monitor configuration fields using the `{variable_name}` convention. The UI informs you whenever this is possible.

Variable and key names have a 100-character limit. Global variable values have a 5000-character limit.

![Passing variables](https://dt-cdn.net/images/httpmonitorsvariables-973-778f630782.png)

Passing variables

### Example monitor

In this example, we perform an OAuth 2.0 authorization using pre- and post-execution scripts that retrieve and apply the access token.

The HTTP monitor is composed of two requests. The first request retrieves the access token, and a post-execution script saves it in the `bearerToken` variable. We then run the second request where a pre-execution script adds the value of the `bearerToken` variable to the request authorization header.

#### Request 1

**Request URL**: `https://somesite.com/sso/oauth2/access_token?realm=/somename`
**HTTP method**: POST
**Post-execution script**:

```
if (response.getStatusCode() != 200) {



api.fail("HTTP error: " + response.getStatusCode());



}



var responseBody = response.getResponseBody();



var jsonData = JSON.parse(responseBody);



api.setValue("bearerToken", jsonData.access_token);



api.info(jsonData.access_token);
```

#### Request 2

**Request URL**: `https://account.somesite.com/rest/user/user%40somesite%2Ecom?`
**HTTP method**: GET
**Pre-execution script**:

```
request.addHeader("Authorization", "Bearer " + api.getValue("bearerToken"));
```

#### Full monitor script

```
{



"version": "1.0",



"requests": [



{



"description": "GET access_token",



"url": "https://somesite.com/sso/oauth2/access_token?realm=/somename",



"method": "POST",



"requestBody": "scope=openid%20read&client_secret=somesecret&grant_type=password&username=user%40somesite%2Ecom&password=password123&client_id=clientid",



"configuration": {



"requestHeaders": [



{



"name": "Content-Type",



"value": "application/x-www-form-urlencoded"



}



],



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": "if (response.getStatusCode() != 200) {\n    api.fail(\"HTTP error: \" + response.getStatusCode());\n}\nvar responseBody = response.getResponseBody();\nvar jsonData = JSON.parse(responseBody);\napi.setValue(\"bearerToken\", jsonData.access_token);\napi.info(jsonData.access_token);"



},



{



"description": "GET tenants",



"url": "https://account.somesite.com/rest/user/user%40somesite%2Ecom?",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "request.addHeader(\"Authorization\", \"Bearer \" + api.getValue(\"bearerToken\"));",



"postProcessingScript": ""



}



]



}
```

## Method reference

When writing pre- and post-execution scripts, you can use the following methods in your JavaScript code. The script editor has a built-in, type-ahead syntax guide and syntax check.

### Store and retrieve values across HTTP requests

* `api.setValue(key, value)`—Sets a `value` for the `key`. Use a separate instance of `api.setValue()` for each key-value pair you wish to specify.
* `api.getValue(key)`—Gets the value of the `key` previously set by `api.setValue()`.
* `api.getValues()`—Returns an object holding the key-value pairs that were previously set by `api.setValue()`.

Variable and key names have a 100-character limit. Global variable values have a 5000-character limit.

### Mark requests as failed or finished

* `api.fail(message)`—Marks the request as failed, providing the `message` as the reason, and marks the monitor execution as failed. The `message` parameter has a 1,000-character limit. `message` appears as the **Failure message** in the **Events** card on the [HTTP monitor details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors."). Custom log messages also appear in the `customLogs` attribute in [HTTP monitor execution details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Learn about the Synthetic details page for HTTP monitors.").
* `api.finish()`—Finishes the request so that the next request is executed.

### Skip HTTP requests

These methods skip HTTP requests after completion of the current request.

* `api.skipNextRequest()`—Skips execution of the next request.
* `api.skipNextRequests(n)`—Skips execution of the next `n` consecutive requests.
* `api.skipRequest(requestIndex)`—Skips execution of the request with the index `requestIndex`. Request index numbers start at `1` and match the request numbers displayed in the web UI.
* `api.skipRequests(requestIndexes)`—Skips execution of multiple requests; the Int32Array of `requestIndexes` specifies the requests to skip, for example, `api.skipRequests(new Int32Array([2,4]))`. You can also define an array first and then refer to it, for example, `api.skipRequests(x)`, where `x=new Int32Array([2,4])` has already been defined.

### Basic logging

* `api.info(message)`—Logs a `message` using the `info` log level.
* `api.warn(message)`—Logs a `message` using the `warning` log level.
* `api.error(message)`—Logs a `message` using the `error` log level.

The `message` parameter has a 1,000-character limit. Messages are logged in the `vuc-http-custom.log` file saved in the [ActiveGate log directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), which is accessible for [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."). Custom log messages also appear in the `customLogs` attribute in [HTTP monitor execution details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Learn about the Synthetic details page for HTTP monitors.").

### Basic encoding

* `api.urlEncode(url)`—Converts a `url` string to the `application/x-www-form-urlencoded` MIME format.
* `api.base64UrlEncode(urlToEncode)`—Encodes input (`urlToEncode`) using Base64URL encoding.
* `api base64UrlDecode(encodedUrl)`—Decodes Base64URL input (`encodedUrl`).

* `api.HMACSHA256(message, secret)`—Creates a Base64 hash using HMAC-SHA256 where `message` is the text that you want to encode; `secret` is secret key.
* `api.btoa(value)`—Creates a Base64-encoded ASCII string from a string (`value`) of binary data.
* `api.atob(value)`—Decodes a Base64-encoded ASCII string (`value`) into a binary string. The input string must be a Base64 representation of a valid UTF-8 string. For more general-purpose Base64 decoding, use the `api.base64decode()` function. The `value` parameter has a 10,000-character limit.

### Generate random values

* `api.randomNextInt()`—Returns a pseudorandom, uniformly distributed `int` value.
* `api.randomNextIntWithBound(value)`—Returns a pseudorandom, uniformly distributed `int` value between 0 (inclusive) and the specified `value` (exclusive).
* `api.randomNextFloat()`—Returns a pseudorandom, uniformly distributed float value.
* `api.randomNextLong()`—Returns a pseudorandom, uniformly distributed long value.
* `api.randomString(numberOfChars, supportedChars)`—Creates a random string whose length is the number of characters (`numberOfChars`); the characters are chosen from the set of characters specified as a string (`supportedChars`). Both parameters have a 5000-character limit.

### Date formatting

* `api.dateToFormat(timestamp, format)`—Returns the input `timestamp` in the specified `format` based on the [Java SimpleDateFormat﻿](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html) class. `timestamp` must be in UNIX Epoch time.
* `api.date()`—Returns the current date as a raw millisecond UNIX Epoch-based value.

Example:

```
api.setValue("dateToFormat", api.dateToFormat("1346524199000", "dd/MM/yy"));



api.setValue("dateToFormatCurrentDate", api.dateToFormat(api.date(), "dd/MM/yy"));
```

### Retrieve data

* `api.UUID()`—Returns a universally unique identifier.

* `api.getContext().location.name`—Returns the name of the private or public location from where the monitor is executed. This is helpful when applying conditional logic based on the execution location (for example, using different login information per location) or for writing to logs, as shown in the example below.

  Example:

  ```
  var loc = api.getContext().location.name;



  api.info("Location Name is: " + loc);
  ```
* `api.getCredential(id, type)`—Retrieves a credential value, given the credential ID (`id`) and (`type`), which can be `username`, `password`, or `token`. You need to provide the exact value of one of the autocomplete suggestions for the credential ID; using dynamic identifiers like variables is not supported. The list consists of only those [credentials to which you have access](/managed/manage/credential-vault#owner-shared-public "Store and manage credentials in the credential vault.").

  Requires ActiveGate version 1.212+ for [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

  As a security best practice, we recommend that you use only dedicated test credentials for synthetic monitors.

  Example:

  ```
  var userName = api.getCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", "username");



  api.setValue("un", userName + "1");
  ```

### Write data

* `api.saveCredential(id, username, password)`—Overwrites a username-password credential, given the credential `id`, the new value for the username (`username`), and the new value for the password (`password`). The `username` and `password` parameters may be strings or variables.

  Example with username and password strings:

  ```
  api.saveCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", "newusername", "newpassword");
  ```

  Example with variables containing the values of the username and password:

  ```
  api.saveCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", myusernamevariable, mypasswordvariable);
  ```
* `api.saveToken(id, token)`—Overwrites a token credential, given the credential `id` and the new value for the token (`token`). The `token` parameter may be a string or a variable.

### Pre-execution script methods

These methods are request specific, so you can only use them for pre-execution scripts.

* `request.addHeader(key, value)`—Adds a request header where `key` is the header name and `value` is the header value.
* `request.setUrl(URL)`—Sets the request `URL`.
* `request.setBody(requestBody)`—Sets the request body (`requestBody`).

### Post-execution script methods

These methods are response specific, so you can only use them for post-execution scripts.

* `response.getResponseBody()`—Returns the first 50 KB of the response body as a string. To parse the JSON-formatted response into an object, use, for example:

  ```
  var responseBody = response.getResponseBody();



  var jsonData = JSON.parse(responseBody);
  ```
* `response.getHeaders()`—Returns an object holding all response HTTP headers.

  Use `response.getHeaders().get(<header-name>)` to get the value of a specific response header as a string.
* `response.getStatusCode()`—Returns the response status code as a number.