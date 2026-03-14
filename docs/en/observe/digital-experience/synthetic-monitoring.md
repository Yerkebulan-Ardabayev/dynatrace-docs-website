---
title: Synthetic Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring
scraped: 2026-03-06T21:14:11.591598
---

# Synthetic Monitoring


* Classic
* Overview
* 1-min read
* Published Sep 25, 2018

Just because your web application is accessible from your office and runs great on your laptop doesn't mean that your customers around the world are also having a great experience with it. Therefore, it's imperative to ensure constant availability and performance of your application from your users' point of view.

Dynatrace Synthetic Monitoring makes it easy for you to monitor the availability and performance of your applications as experienced by your customers around the world and around the clock. Availability is the success rate at a given instant or time period that indicates if your application is fully functional and available to users. Performance measures whether your web page or recorded interaction experiences significant slowdowns compared to a threshold.

The availability and performance of your internal resources are equally important. With the ability to execute monitors from private locations, you can bring the testing capabilities available in public locations right to your own infrastructure.

Dynatrace offers the following types of synthetic monitors: single-URL browser monitors, browser clickpaths, HTTP monitors and NAM monitors. Check out the links below to learn more. Licensing is based on the [consumption of Synthetic actions and requests](../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

### General information

* [Types of synthetic monitors](synthetic-monitoring/general-information/types-of-synthetic-monitors.md "Learn about Dynatrace synthetic monitor types.")
* [Synthetic calculations](synthetic-monitoring/general-information/synthetic-calculations.md "Understand Synthetic Monitoring metric calculations.")
* [Supported authentication methods in Synthetic Monitoring](synthetic-monitoring/general-information/synthetic-authentication.md "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.")
* [On-demand synthetic monitor executions for CI/CD](synthetic-monitoring/general-information/on-demand-executions.md "Execute synthetic monitors on demand from public or private locations")
* [External vault integration](synthetic-monitoring/general-information/external-vault-integration.md "Synchronize Synthetic Monitoring credentials with external vaults.")
* [Public Synthetic locations](synthetic-monitoring/general-information/public-synthetic-locations.md "Learn about all currently available public Synthetic Monitoring locations.")
* [Synthetic architecture and communication](synthetic-monitoring/general-information/architecture-communication.md "Detailed description of the architecture and communication infrastructure for Synthetic app")

### HTTP monitors

* [Create an HTTP monitor](synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic.md "Learn how to set up an HTTP monitor to check the performance and availability of your site.")
* [Configure HTTP monitors](synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic.md "Learn about configuring HTTP monitors.")
* [Script mode for HTTP monitor configuration](synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic.md "Create or edit your HTTP monitors in JSON format.")
* [Pre- and post-execution scripts for HTTP monitors](synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic.md "Learn how to apply pre and post scripts to your requests")
* [HTTP monitor metrics](synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic.md "Learn about the performance metrics collected for HTTP monitors.")

### Analysis and alerting

* [Synthetic alerting overview](synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview.md "Learn about synthetic alerting concepts and workflow.")
* [Synthetic details for browser monitors](synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors.md "Analyze browser monitor and clickpath results on the Synthetic details page.")
* [Multidimensional analysis for browser monitors](synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors.md "Learn how to analyze browser-monitor data points.")
* [Waterfall graphs](synthetic-monitoring/analysis-and-alerting/waterfall-graphs.md "How to analyze page resource downloads for browser monitors.")
* [HTTP monitors reporting results](synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic.md "Learn about the Synthetic details page for HTTP monitors.")

### Browser monitors

* [Create a single-URL browser monitor](synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor.md "Learn how to set up a single-URL browser monitor to check the availability of your site.")
* [Record a browser clickpath](synthetic-monitoring/browser-monitors/record-a-browser-clickpath.md "Learn how to record a browser clickpath to monitor the availability and performance of your application.")
* [Configure browser monitors](synthetic-monitoring/browser-monitors/configure-browser-monitors.md "Learn about configuring browser monitors and clickpaths.")
* [Browser clickpath events](synthetic-monitoring/browser-monitors/browser-clickpath-events.md "Learn about the event types created when recording a browser clickpath.")
* [Script mode for browser monitor configuration](synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration.md "Create or edit your browser monitors in JSON format.")
* [Number of actions consumed by browser clickpaths](synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths.md "Find out how many actions are consumed by a browser clickpath and how they differ from events.")

### Private Synthetic locations

* [Create a private Synthetic location](synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Learn how to create a private location for synthetic monitoring.")
* [Requirements for private Synthetic locations](synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")
* [Set up a proxy for private synthetic monitoring](synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic.md "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")
* [Containerized, auto-scalable private Synthetic locations on Kubernetes](synthetic-monitoring/private-synthetic-locations/containerized-locations.md "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.")
* [Manage private Synthetic locations](synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md "Analyze and manage capacity usage at your private Synthetic locations.")

### API

* [Synthetic API v1](../../dynatrace-api/environment-api/synthetic.md "Find out what the Dynatrace Synthetic v1 API offers.")
* [Synthetic API v2](../../dynatrace-api/environment-api/synthetic-v2.md "Find out what the Dynatrace Synthetic v2 API offers.")
* [Credential vault API](../../dynatrace-api/configuration-api/credential-vault.md "Learn what the Dynatrace configuration API for credentials offers.")
* [Calculated metrics API - Synthetic](../../dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics.md "Manage calculated synthetic metrics via the Dynatrace configuration API.")

## Related topics

* [Synthetic Monitoringï»¿](https://www.dynatrace.com/platform/synthetic-monitoring/)