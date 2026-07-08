---
title: Use Subresource Integrity (SRI) for Real User Monitoring Classic code
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/subresource-integrity
---

# Use Subresource Integrity (SRI) for Real User Monitoring Classic code

# Use Subresource Integrity (SRI) for Real User Monitoring Classic code

* How-to guide
* 2-min read
* Published Mar 04, 2025

Integrating third-party resources into web pages, such as those from a Content Delivery Network (CDN), poses the risk that an attacker could potentially gain control of the third-party host and manipulate these resources. The [Subresource Integrity (SRI)﻿](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) browser feature mitigates this risk by ensuring that only unaltered resources are used. It does this by including a cryptographic hash that the fetched resource must match.

Dynatrace RUM supports SRI through a dedicated snippet format [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case"). It contains a hash for the RUM monitoring code. If the hash doesn't match the monitoring code received by the browser, the code won't be executed.

When Session Replay is enabled, the Session Replay monitoring code is injected into your page by the RUM JavaScript as an external resource, resulting in a separate request. Starting with RUM JavaScript version 1.309, if you use the OneAgent JavaScript tag with SRI, the RUM JavaScript will inject both the Session Replay monitoring code and a cryptographic hash to ensure its integrity.

SRI is not supported for the snippet formats JavaScript tag and code snippet due to its incompatibility with the dynamic update mechanisms inherent to these formats.

## Auto-injected app Configure an auto-injected application to use SRI

Note that all connected ActiveGates must be on ActiveGate version 1.310+ for at least 30 days before this feature becomes available.

For auto-injected applications, the Real User monitoring code is, by default, delivered by OneAgent. To use SRI, you need to configure your application to request the monitoring code from your CDN or Cluster ActiveGate as described in
[Configure the Real User Monitoring Classic code source](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring Classic code source for your specific requirements."). This will allow you to select the necessary snippet format.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Injection** > **Automatic injection**.
5. In the **Real User Monitoring code source** dropdown list, select **CDN**.
6. In the **Snippet format** dropdown list, select **OneAgent JavaScript Tag with SRI**.

## Agentless app Configure an agentless application to use SRI

The optimal approach to using SRI for an agentless application is to integrate the insertion of the OneAgent JavaScript tag with SRI into your build process via the [API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion."). This ensures that your application consistently operates with the latest configuration.

To get the OneAgent JavaScript tag with SRI from the web UI

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Injection** > **Manual insertion**.
5. In the **OneAgent JavaScript Tag with SRI** section, select **Copy** to copy the tag to the clipboard.

We don't recommend using the OneAgent JavaScript tag with SRI from the web UI unless timely configuration updates are not critical.