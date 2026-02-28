---
title: Web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications
scraped: 2026-02-28T21:12:15.035590
---

# Web applications

# Web applications

* Overview
* 1-min read
* Updated on Apr 03, 2024

All HTML pagesâlike static webpages or single-page applications running in a browserâare regarded as web applications.

We ended support for Internet Explorer 11 starting with RUM JavaScript version 1.293. For more information, see [RUM JavaScript for Internet Explorer](/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

### Initial setup

* [Define applications for Real User Monitoring](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")
* [Configure automatic injection](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications")
* [Set up agentless Real User Monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.")
* [Select a snippet format](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [Configure Real User Monitoring to capture XHR actions](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")
* [Pages and page groups](/docs/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.")
* [Create custom user action names for web applications](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.")
* [Firewall constraints for RUM](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall.")
* [Link cross-origin XHR user actions and their distributed traces](/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.")
* [Use Subresource Integrity (SRI) for Real User Monitoring code](/docs/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.")
* [Check your application health](/docs/observe/digital-experience/web-applications/initial-setup/app-health-check "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")
* [Roll out RUM selectively for your applications](/docs/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Additional configuration



* [Control the RUM JavaScript version](/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version "Control the RUM JavaScript version used to monitor your applications")
* [Configure cost and traffic control for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.")
* [Configure data privacy settings for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")
* [Configure key user actions for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications.")
* [Capture additional interaction types for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types "Choose which interaction types RUM should detect for your web applications.")
* [Adjust Apdex settings for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web "Configure the user-satisfaction performance thresholds for your web application and its key user actions.")
* [Change user experience score thresholds for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web "Adjust the user experience score thresholds to meet the specific requirements of your web application.")
* [Create calculated metrics for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")
* [Create USQL custom metrics for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications.")
* [Define user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.")
* [Customize Real User Monitoring with the JavaScript API for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.")
* [Configure error detection for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")
* [Tag specific users for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.")
* [Customize IP address detection for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications.")
* [Map internal IP addresses to locations for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Configure first-party, third-party, and CDN resource detection for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Configure the RUM cookie domain for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain "Learn when and how to configure the cookie domain.")
* [Configure beacon origin allowlist for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.")
* [Configure beacon endpoint for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.")
* [Configure the Real User Monitoring code source](/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.")
* [Exclude IP addresses, browsers, bots, and spiders from monitoring for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.")
* [Configure your caching servers](/docs/observe/digital-experience/web-applications/additional-configuration/configure-your-caching-servers "Learn how to configure your caching server correctly to avoid cache-related problems.")
* [Check application detection rules](/docs/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Configure XHR for older versions of Internet Explorer](/docs/observe/digital-experience/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie "Learn how to make Dynatrace JavaScript work with outdated versions of Internet Explorer.")
* [Real User Monitoring for process groups](/docs/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring for process groups.")
* [Modify Content Security Policy for RUM](/docs/observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum "Learn how to enable and modify CSP for your RUM-monitored applications.")
* [Delete a web application](/docs/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.")

### Analyze and use RUM data



* [Introduction to application overview page](/docs/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.")
* [Performance analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.")
* [User behavior analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Understand the user behavior analysis options that are provided by Dynatrace.")
* [Multidimensional analysis for web applications](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Waterfall analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.")
* [World map view](/docs/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.")
* [Work with key performance metrics](/docs/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.")
* [Analyze individual user actions](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions "Understand how you can access user action detail pages and analyze user actions.")
* [Leverage user action and user session properties for web applications](/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Define conversion goals](/docs/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones.")
* [Use 'Visually complete' and 'Speed index' metrics](/docs/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.")
* [Visually complete top findings](/docs/observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings "Lean how to leverage Visually complete top findings provided in the waterfall analysis.")
* [Application analysis with Hyperlyzer](/docs/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions.")
* [Service flows for applications and user actions](/docs/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Learn how to access service flows for applications and user actions.")
* [Source map support for JavaScript error analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors.")

### Troubleshooting

[Troubleshooting RUM for web applications](/docs/observe/digital-experience/web-applications/troubleshooting "Learn how to troubleshoot issues when you use Real User Monitoring for your web applications.")