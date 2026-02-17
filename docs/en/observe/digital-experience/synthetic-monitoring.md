---
title: Synthetic Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring
scraped: 2026-02-17T04:50:01.950528
---

# Synthetic Monitoring

# Synthetic Monitoring

* Overview
* 1-min read
* Published Sep 25, 2018

Just because your web application is accessible from your office and runs great on your laptop doesn't mean that your customers around the world are also having a great experience with it. Therefore, it's imperative to ensure constant availability and performance of your application from your users' point of view.

Dynatrace Synthetic Monitoring makes it easy for you to monitor the availability and performance of your applications as experienced by your customers around the world and around the clock. Availability is the success rate at a given instant or time period that indicates if your application is fully functional and available to users. Performance measures whether your web page or recorded interaction experiences significant slowdowns compared to a threshold.

The availability and performance of your internal resources are equally important. With the ability to execute monitors from private locations, you can bring the testing capabilities available in public locations right to your own infrastructure.

Dynatrace offers the following types of synthetic monitors: single-URL browser monitors, browser clickpaths, HTTP monitors and NAM monitors. Check out the links below to learn more. Licensing is based on the [consumption of Synthetic actions and requests](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

### General information

* [Types of synthetic monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.")
* [Synthetic calculations](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.")
* [Supported authentication methods in Synthetic Monitoring](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.")
* [On-demand synthetic monitor executions for CI/CD](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations")
* [External vault integration](/docs/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Synchronize Synthetic Monitoring credentials with external vaults.")
* [Public Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.")
* [Synthetic architecture and communication](/docs/observe/digital-experience/synthetic-monitoring/general-information/architecture-communication "Detailed description of the architecture and communication infrastructure for Synthetic app")

### HTTP monitors

* [Create an HTTP monitor](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.")
* [Configure HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")
* [Script mode for HTTP monitor configuration](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Create or edit your HTTP monitors in JSON format.")
* [Pre- and post-execution scripts for HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Learn how to apply pre and post scripts to your requests")
* [HTTP monitor metrics](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic "Learn about the performance metrics collected for HTTP monitors.")

### Analysis and alerting

* [Synthetic alerting overview](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview "Learn about synthetic alerting concepts and workflow.")
* [Synthetic details for browser monitors](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.")
* [Multidimensional analysis for browser monitors](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Learn how to analyze browser-monitor data points.")
* [Waterfall graphs](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "How to analyze page resource downloads for browser monitors.")
* [HTTP monitors reporting results](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.")

### Browser monitors

* [Create a single-URL browser monitor](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.")
* [Record a browser clickpath](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.")
* [Configure browser monitors](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Browser clickpath events](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Learn about the event types created when recording a browser clickpath.")
* [Script mode for browser monitor configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.")
* [Number of actions consumed by browser clickpaths](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Find out how many actions are consumed by a browser clickpath and how they differ from events.")

### Private Synthetic locations

* [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")
* [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")
* [Set up a proxy for private synthetic monitoring](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")
* [Containerized, auto-scalable private Synthetic locations on Kubernetes](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.")
* [Manage private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations.")

### API

* [Synthetic API v1](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.")
* [Synthetic API v2](/docs/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers.")
* [Credential vault API](/docs/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers.")
* [Calculated metrics API - Synthetic](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Manage calculated synthetic metrics via the Dynatrace configuration API.")

## Related topics

* [Synthetic Monitoringï»¿](https://www.dynatrace.com/platform/synthetic-monitoring/)