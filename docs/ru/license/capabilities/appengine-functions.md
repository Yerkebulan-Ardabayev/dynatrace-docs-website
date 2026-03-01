---
title: AppEngine Functions (Serverless Functions) overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/appengine-functions
scraped: 2026-03-01T21:19:12.190772
---

# AppEngine Functions (Serverless Functions) overview (DPS)

# AppEngine Functions (Serverless Functions) overview (DPS)

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on May 22, 2025

AppEngine Functions are the backend for your app.
They are written in TypeScript and run within the [Dynatrace JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/).

There are three types of AppEngine Functions:

* App functions:
  These functions represent the backend of an app and are built, bundled, and deployed together with your custom app.
* Ad-hoc functions:
  Custom code that accomplishes a specific use case is referred to as an ad-hoc function.
  These functions can be invoked from within ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, or directly via API.
* Custom actions:
  A specific type of app function that, together with a UI component, can be declared as a custom workflow action to extend ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
  Custom actions can then be selected as a task within ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and can be executed within a workflow.

All AppEngine Functions are deployed in an environment with 256 MiB RAM.

AppEngine Functions work out-of-the-box: no external hosting is required, and there is no need to worry about maintaining a runtime environment to execute logic or code.

## Related topics

* [AppEngine](/docs/platform/appengine "Develop feature-rich Dynatrace apps for you and the world!")
* [App functionsï»¿](https://developer.dynatrace.com/develop/functions/ "Basic concepts of app functions, which represent an app backend")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)