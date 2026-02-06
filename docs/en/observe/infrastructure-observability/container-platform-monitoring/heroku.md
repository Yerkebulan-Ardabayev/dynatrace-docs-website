---
title: Heroku monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/heroku
scraped: 2026-02-06T16:28:55.999404
---

# Heroku monitoring

# Heroku monitoring

* Reference
* 2-min read
* Published May 22, 2019

With Dynatrace cloud-native monitoring enabled for your Heroku applications, you get

* Deep application monitoring and code-level details for Java, PHP, Node.js and more â with just a single, language-independent buildpack
* [Automatic root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") of your Heroku web applications
* Insights into how your Heroku applications use [databases](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.")âincluding detailed metrics for each database statement
* [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") data on customersâ web browser and mobile device behavior
* Automated external and third-party service monitoring (for example, calls to external REST APIs)

## Prerequisites

[Set up and configure Dynatrace integration on Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## View monitoring results

After linking your Dynatrace account with your Heroku application, youâll receive the full range of application and service monitoring visibility that Dynatrace provides (for example, **Smartscape** and service-level insights with **Service flow**). Dynatrace automatically detects that your application is running on Heroku as well as services related to you Heroku application.

![Heroku monitoring](https://dt-cdn.net/images/heroku1-2874-778cc74486.png)

Dynatrace automatically initiates deep application monitoring for your Heroku applications and provides code-level visibility into your applicationsâ services. Dynatrace **Service flow** allows you to track how requests to services provided by your Heroku application are propagated through a system. Service tracing also helps to identify performance bottlenecks and failed requests in the service-to-service communication chain. With Dynatrace, itâs never been easier to pinpoint the root cause of poor performance in heterogeneous microservices stacks.

![Heroku monitoring](https://dt-cdn.net/images/heroku2-2884-8bad582082.png)

## Tag your Heroku applications

You can use the Dynatrace powerful [tagging mechanism](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to automatically organize and filter all monitored Heroku application components. Dynatrace allows you to apply tags to processes and hosts based on environment variables.

`heroku config:set DT_TAGS=owner=team-easytravel`

## Related topics

* [Set up Dynatrace on Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")