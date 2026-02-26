---
title: Capture request attributes based on web request data
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data
scraped: 2026-02-26T21:16:59.564628
---

# Capture request attributes based on web request data

# Capture request attributes based on web request data

* Latest Dynatrace
* 4-min read
* Updated on Jul 06, 2023

To define a request attribute based on web request data:

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select the **Create new request attribute** button.
3. Provide a unique **Request attribute name**. You can rename an attribute at any point in the future.
4. Indicate **Data type**.  
   You can't change **Data type** following request attribute setup.
5. If multiple values exist in a single request, specify what should be stored in the request attribute for every request, and choose how to normalize the text.
6. Check whether this rule should access unmasked data, and whether the request attribute contains [confidential data](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#restrict-view-access "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

   This will potentially access personal data.
7. Add a data source. You can define one or more rules to specify how your attribute should be fetched.  
   Each rule needs a source. Dynatrace needs to know where it can collect the request attribute. You can define the rule by first selecting where the rule should be applied (based on process group, host group, service technology, or group tag), and then indicating where the actual parameter can be found (**Request attribute source**).
8. Once you have added all the data sources, select **Save** to save your request attribute rule.

## Request attribute rules

Have a look at the example request attribute rule below. Note that the request attribute `destination` can obtain its value from two different sources, either an `HTTP Post` parameter (`iceform:destination`) or an `HTTP GET` parameter (`destination`). Rules are executed in order. If a request meets the criteria for both rules, its value will be taken from the first rule.

Each rule needs a source. In the example below, the request attribute source is a web request `HTTP GET` parameter (`destination`).

![Example of request attributes rule definition](https://dt-cdn.net/images/get-2018-10-30-14-26-29-1373-3d3ff74f1c.png)

This `GET` parameter will be captured on all monitored processes that support code-level insight and it will be reported on all requests that are monitored by Dynatrace.

While this is convenient, itâs not always whatâs needed. This is why you can restrict rules to a subset of process groups and services. To do this, select process group and service names from the four drop-lists above to reduce the number of process groups and services that the rule applies to.

You may not be interested in capturing every value. In other cases, a value may contain a prefix that you want to check against. To do this, specify that the designated parameter should only be used if its value matches a certain value. You can also opt to not use an entire value, but instead extract a portion of a value. The example below is set up to only consider `iceform:destination` `HTTP POST` parameters that begin with the string `Journey :`. This approach will extract everything that follows the string `Journey:` and store it in the request attribute.

![Example of request attributes POST rule definition](https://dt-cdn.net/images/post-2018-10-30-14-15-35-1379-6f82cbbf7c.png)

Requests can have as many attributes as you want.

## Request attribute sources for web requests

Request attribute data sources for web requests include

* Technology-independent sources, such as:

  + HTTP POST parameters
  + [Client IP addresses](/docs/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#ip-addresses "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")  
    The value of the first matching header is reported.
  + HTTP request and response headers
  + Web request URL or one of its constituents, like the path or a query parameter

  In the last two cases, you can also choose the side of the web request on which to capture and store the attribute.

  OneAgent is always required at capture.

  1

  Full-service call: request that is fully monitored by Dynatrace.

  2

  External service call: request that goes to external resources.
* Technology-specific sources.

  + The application can hold a complex object in an attribute, while OneAgent converts it to a string upon capture (for example, in [Java servlet session attributeï»¿](https://dt-url.net/q503soq) and [ASP.NET session-state variableï»¿](https://dt-url.net/qf23stx)). This might have side effects, so be careful with what you capture.
  + ASP.NET When multiple parameters have the same name, you will see only the first captured value.
  + Java servlet Java servlet request attributes and session attributes are captured only after the servlet or filter is entered.

## Post processing

In most cases, a captured value will contain what it is youâre looking for. However, you may not want an entire value, or even every value. With post processing you can manipulate the captured value.

Expand the **Optionally restrict or process the captured parameter(s) further** option to see the processing steps. The steps are executed in the presented orderâeach step is applied to the result of the previous step.

You don't have to apply all the steps. Each step becomes active once you provide a value for it or select the option box.

![Post processing options for defining request attribute rule](https://dt-cdn.net/images/post5steps-1353-6e753964a1.png)

Step 1 enables you to extract something from the resulting string based on delimited characters.

Step 2 can split the captured value into several values based on a delimited character.

Step 3 removes whitespaces.

Step 4 enables you to filter out captured values that don't fit the provided criterion.

Step 5 enables you to extract something from the resulting string based a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").