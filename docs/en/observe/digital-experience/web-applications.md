---
title: Web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications
scraped: 2026-03-06T21:14:09.923490
---

# Web applications


* Classic
* Overview
* 1-min read
* Updated on Apr 03, 2024

All HTML pagesâlike static webpages or single-page applications running in a browserâare regarded as web applications.

We ended support for Internet Explorer 11 starting with RUM JavaScript version 1.293. For more information, see [RUM JavaScript for Internet Explorer](web-applications/additional-configuration/rum-javascript-version.md#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

### Initial setup

* [Define applications for Real User Monitoring](web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder.md "Learn how to define your applications following the suggested, manual, or application detection rules approach.")
* [Configure automatic injection](web-applications/initial-setup/rum-injection.md "Configure automatic injection of the RUM JavaScript into the pages of your applications")
* [Set up agentless Real User Monitoring](web-applications/initial-setup/set-up-agentless-real-user-monitoring.md "Set up agentless monitoring for your web applications.")
* [Select a snippet format](web-applications/initial-setup/snippet-formats.md "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [Configure Real User Monitoring to capture XHR actions](web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions.md "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")
* [Pages and page groups](web-applications/initial-setup/pages-and-pagegroups.md "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.")
* [Create custom user action names for web applications](web-applications/initial-setup/create-custom-names-for-user-actions.md "Customize automatically generated user action names for your web applications.")
* [Firewall constraints for RUM](web-applications/initial-setup/firewall-constraints-for-rum.md "Find out how to make sure that Real User Monitoring data passes through your firewall.")
* [Link cross-origin XHR user actions and their distributed traces](web-applications/initial-setup/link-cross-origin-xhrs.md "Enable the correlation between cross-origin XHR actions and distributed traces.")
* [Use Subresource Integrity (SRI) for Real User Monitoring code](web-applications/initial-setup/subresource-integrity.md "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.")
* [Check your application health](web-applications/initial-setup/app-health-check.md "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")
* [Roll out RUM selectively for your applications](web-applications/initial-setup/selective-rum-rollout.md "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Additional configuration

* [Control the RUM JavaScript version](web-applications/additional-configuration/rum-javascript-version.md "Control the RUM JavaScript version used to monitor your applications")
* [Configure cost and traffic control for web applications](web-applications/additional-configuration/configure-cost-and-traffic-control-web.md "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.")
* [Configure data privacy settings for web applications](web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr.md "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")
* [Configure key user actions for web applications](web-applications/additional-configuration/configure-key-user-actions-web.md "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications.")
* [Capture additional interaction types for web applications](web-applications/additional-configuration/capture-interaction-types.md "Choose which interaction types RUM should detect for your web applications.")
* [Adjust Apdex settings for web applications](web-applications/additional-configuration/configure-apdex-web.md "Configure the user-satisfaction performance thresholds for your web application and its key user actions.")
* [Change user experience score thresholds for web applications](web-applications/additional-configuration/configure-user-experience-score-web.md "Adjust the user experience score thresholds to meet the specific requirements of your web application.")
* [Create calculated metrics for web applications](web-applications/additional-configuration/rum-calculated-metrics-web.md "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")
* [Create USQL custom metrics for web applications](web-applications/additional-configuration/custom-metrics-from-user-sessions.md "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications.")
* [Define user action and user session properties for web applications](web-applications/additional-configuration/define-user-action-and-session-properties.md "Define custom string, numeric, and date properties for your monitored web applications.")
* [Customize Real User Monitoring with the JavaScript API for web applications](web-applications/additional-configuration/customize-rum.md "Find out how to customize Real User Monitoring using the JavaScript API.")
* [Configure error detection for web applications](web-applications/additional-configuration/configure-errors.md "Configure your application to capture or ignore request, custom, and JavaScript errors.")
* [Tag specific users for web applications](web-applications/additional-configuration/identify-individual-users-for-session-analysis.md "Tag individual users via the JavaScript API for session analysis.")
* [Customize IP address detection for web applications](web-applications/additional-configuration/customize-ip-address-detection-web.md "Change the way Dynatrace determines client IP addresses for your web applications.")
* [Map internal IP addresses to locations for web applications](web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web.md "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Configure first-party, third-party, and CDN resource detection for web applications](web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web.md "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Configure the RUM cookie domain for web applications](web-applications/additional-configuration/configure-the-cookie-domain.md "Learn when and how to configure the cookie domain.")
* [Configure beacon origin allowlist for web applications](web-applications/additional-configuration/configure-beacon-domain-allowlist.md "Specify the origins from which cross-origin RUM beacons should be accepted.")
* [Configure beacon endpoint for web applications](web-applications/additional-configuration/beacon-endpoint.md "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.")
* [Configure the Real User Monitoring code source](web-applications/additional-configuration/configure-monitoring-code-source.md "Configure the Real User Monitoring code source for your specific requirements.")
* [Exclude IP addresses, browsers, bots, and spiders from monitoring for web applications](web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring.md "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.")
* [Configure your caching servers](web-applications/additional-configuration/configure-your-caching-servers.md "Learn how to configure your caching server correctly to avoid cache-related problems.")
* [Check application detection rules](web-applications/additional-configuration/application-detection-rules.md "Easily understand the detection rules of your RUM application.")
* [Configure XHR for older versions of Internet Explorer](web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie.md "Learn how to make Dynatrace JavaScript work with outdated versions of Internet Explorer.")
* [Real User Monitoring for process groups](web-applications/additional-configuration/rum-for-process-groups.md "Learn how to configure Real User Monitoring for process groups.")
* [Modify Content Security Policy for RUM](web-applications/additional-configuration/modify-csp-for-rum.md "Learn how to enable and modify CSP for your RUM-monitored applications.")
* [Delete a web application](web-applications/additional-configuration/delete-application-web.md "Delete your web applications via the Dynatrace web UI or API.")

### Analyze and use RUM data

* [Introduction to application overview page](web-applications/analyze-and-use/introduction-to-application-overview.md "Read an overview of the analysis options offered on the application overview page.")
* [Performance analysis](web-applications/analyze-and-use/performance-analysis.md "Understand the available types of performance analysis that are provided by Dynatrace.")
* [User behavior analysis](web-applications/analyze-and-use/user-behavior-analysis.md "Understand the user behavior analysis options that are provided by Dynatrace.")
* [Multidimensional analysis for web applications](web-applications/analyze-and-use/multi-dimensional-analysis.md "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Waterfall analysis](web-applications/analyze-and-use/waterfall-analysis.md "Learn how to analyze all user action monitoring data through waterfall analysis.")
* [World map view](web-applications/analyze-and-use/world-map-view.md "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.")
* [Work with key performance metrics](web-applications/analyze-and-use/work-with-key-performance-metrics.md "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.")
* [Analyze individual user actions](web-applications/analyze-and-use/analyze-individual-user-actions.md "Understand how you can access user action detail pages and analyze user actions.")
* [Leverage user action and user session properties for web applications](web-applications/analyze-and-use/action-and-session-properties.md "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Define conversion goals](web-applications/analyze-and-use/define-conversion-goals.md "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones.")
* [Use 'Visually complete' and 'Speed index' metrics](web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics.md "Learn how to use 'Visually complete' and 'Speed index' metrics.")
* [Visually complete top findings](web-applications/analyze-and-use/visually-complete-top-findings.md "Lean how to leverage Visually complete top findings provided in the waterfall analysis.")
* [Application analysis with Hyperlyzer](web-applications/analyze-and-use/application-analysis-with-hyperlyzer.md "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions.")
* [Service flows for applications and user actions](web-applications/analyze-and-use/service-flows-for-applications-and-user-actions.md "Learn how to access service flows for applications and user actions.")
* [Source map support for JavaScript error analysis](web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis.md "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors.")

### Troubleshooting

[Troubleshooting RUM for web applications](web-applications/troubleshooting.md "Learn how to troubleshoot issues when you use Real User Monitoring for your web applications.")