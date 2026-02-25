---
title: Custom API definitions
source: https://www.dynatrace.com/docs/observe/application-observability/services/customize-api-definitions
scraped: 2026-02-25T21:26:50.524124
---

# Custom API definitions

# Custom API definitions

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Nov 22, 2018

For some languages, like Node.js and Go, Dynatrace provides detection based on modules and packages. It uses a basic set of predefined APIs for Java and .NET. However, for others, Dynatrace allows you to create custom API definitions for the various frameworks in your environment. Custom API definitions are used to further segment the API breakdown and make it easier to quickly see which frameworks contain hotspots.

For example, by using a custom-created API definition called `easyTravel`, Dynatrace is able to identify all easyTravel-related method calls as part of the easyTravel-specific code.

To add a user-defined API detection rule:

1. Go to **Settings** > **Server-side service monitoring** > **API detection rules**.
2. Select **Create API detection rule**.
3. Type the name of the API.  
   The API name in this example is **easyTravel**.
4. Select **Add new condition**.
   The pattern to be used for identifying the API in this example is `com.dynatrace.easytravel`.
5. Select **Confirm** to save the new API detection rule.

![Add API detection rule](https://dt-cdn.net/images/add-api-detection-rule-1316-08acb766e6.png)

The user-defined **easyTravel** API is now included in the code-level analysis.

## Related topics

* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")