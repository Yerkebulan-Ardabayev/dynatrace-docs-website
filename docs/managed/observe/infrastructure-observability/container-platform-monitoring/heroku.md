---
title: Heroku monitoring
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/heroku
---

# Heroku monitoring

# Heroku monitoring

* Reference
* 2-min read
* Published May 22, 2019

With Dynatrace cloud-native monitoring enabled for your Heroku applications, you get

* Deep application monitoring and code-level details for Java, PHP, Node.js and more – with just a single, language-independent buildpack
* [Automatic root cause analysis](/managed/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") of your Heroku web applications
* Insights into how your Heroku applications use [Databases Services](/managed/observe/infrastructure-observability/databases "Learn how to automatically detect database services, how to analyze database services, and more."),—including detailed metrics for each database statement
* [Real User Monitoring](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.") data on customers’ web browser and mobile device behavior
* Automated external and third-party service monitoring (for example, calls to external REST APIs)

## Prerequisites

[Set up and configure Dynatrace integration on Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## View monitoring results

After linking your Dynatrace account with your Heroku application, you’ll receive the full range of application and service monitoring visibility that Dynatrace provides (for example, **Smartscape** and service-level insights with **Service flow**). Dynatrace automatically detects that your application is running on Heroku as well as services related to you Heroku application.

![Heroku monitoring](https://dt-cdn.net/images/heroku1-2874-778cc74486.png)

Heroku monitoring

Dynatrace automatically initiates deep application monitoring for your Heroku applications and provides code-level visibility into your applications’ services. Dynatrace **Service flow** allows you to track how requests to services provided by your Heroku application are propagated through a system. Service tracing also helps to identify performance bottlenecks and failed requests in the service-to-service communication chain. With Dynatrace, it’s never been easier to pinpoint the root cause of poor performance in heterogeneous microservices stacks.

![Heroku monitoring](https://dt-cdn.net/images/heroku2-2884-8bad582082.png)

Heroku monitoring

## Tag your Heroku applications

You can use the Dynatrace powerful [tagging mechanism](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to automatically organize and filter all monitored Heroku application components. Dynatrace allows you to apply tags to processes and hosts based on environment variables.

`heroku config:set DT_TAGS=owner=team-easytravel`

## Related topics

* [Set up Dynatrace on Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")