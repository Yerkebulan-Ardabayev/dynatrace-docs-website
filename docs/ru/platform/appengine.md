---
title: AppEngine
source: https://www.dynatrace.com/docs/platform/appengine
scraped: 2026-02-20T21:08:51.079108
---

# AppEngine

# AppEngine

* Latest Dynatrace
* 2-min read
* Updated on Jan 28, 2026

With the introduction of the Dynatrace AppEngine, you can now build custom apps on top of all the observability data collected by Dynatrace.

Compared to other Dynatrace platform functionality, Dynatrace apps are smaller, self-contained, and focused on specific use cases. But a Dynatrace app is not an isolated application: the Dynatrace platform implements an [intent conceptï»¿](https://developer.dynatrace.com/develop/intents/) that allows interoperability between Dynatrace apps.

## Why AppEngine?

The following areas make AppEngine unique:

* **Logic to data:** With AppEngine, you bring logic to data. Writing apps on the Dynatrace platform allows you to utilize the capabilities like Smartscape on Grail and Dynatrace Intelligence to solve your custom use cases close to where the data is stored.
* **Secure and scalable app runtime:** AppEngine adds security to your data by ensuring logic and data stay within the security boundaries and everything runs within a defined scope. Furthermore, AppEngine makes sure your app scales up to your needs.
* **Integrates your environment:** AppEngine enables you to create any integration to third-party systems to solve all your custom use cases.

Dynatrace apps are self-contained and focus on specific use cases. However, a Dynatrace app isn't an isolated application. It interacts with the capabilities of the Dynatrace platform via APIs, with other apps via [intentsï»¿](https://developer.dynatrace.com/develop/intents/), or with publicly available third-party systems. Dynatrace apps can also interact with your on-premises systems via EdgeConnect, which you can run in your corporate network.

![AppEngine architecture](https://dt-cdn.net/images/architecture-diagram-2056-09a196c931.webp)

## Building blocks

The user interface of a Dynatrace app is written as a React single-page application and uses TypeScript to enhance the developer experience. The Dynatrace platform provides an extensive toolchain to make the life of an app developer as easy as possible:

* The [**Strato design system**ï»¿](https://developer.dynatrace.com/reference/design-system/) and design tokens provide fundamental and customizable UI components.
* [**TypeScript SDKs**ï»¿](https://developer.dynatrace.com/reference/sdks/) allow apps to interact with the [Dynatrace platform servicesï»¿](https://developer.dynatrace.com/platform-services/) (querying data, document service, state service, etc.).
* [**app functions**ï»¿](https://developer.dynatrace.com/develop/functions/) as the backend for your app, written in TypeScript and run within the [Dynatrace JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/).
* The [**Dynatrace app Toolkit**ï»¿](https://developer.dynatrace.com/reference/app-toolkit/) allows you to easily create, build, and deploy apps and their functions.

## Learn more

For tutorials, how-to guides, and technical references for Dynatrace app developers, head over to [Dynatrace Developerï»¿](https://dt-url.net/developers). There's something for every skill level.

## Related topics

* [AppEngine empowers organizations to create custom apps for better data insightsï»¿](https://www.dynatrace.com/news/blog/appengine-custom-apps-for-data-insights/)