---
title: Use Subresource Integrity (SRI) in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity
scraped: 2026-02-16T09:31:02.420793
---

# Use Subresource Integrity (SRI) in the New RUM Experience

# Use Subresource Integrity (SRI) in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

Integrating third-party resources into web pages, such as those from a content delivery network (CDN), poses the risk that an attacker could potentially gain control of the third-party host and manipulate these resources. The [Subresource Integrity (SRI)ï»¿](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) browser feature mitigates this risk by ensuring that only unaltered resources are used. It does this by including a cryptographic hash that the fetched resource must match.

Dynatrace RUM supports SRI through a dedicated snippet format, [OneAgent JavaScript tag with SRI](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#oneagent-js-tag-sri "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). This contains a cryptographic hash for the RUM monitoring code. If the cryptographic hash doesn't match the monitoring code received by the browser, the code won't be executed.

If Session Replay Classic is enabled, the Session Replay Classic monitoring code is injected into your page by the RUM JavaScript as an external resource, resulting in a separate request. When you use the OneAgent JavaScript tag with SRI, the RUM JavaScript injects both the Session Replay monitoring code and a cryptographic hash to ensure its integrity.

SRI is not supported for the snippet format JavaScript tag due to its incompatibility with the dynamic update mechanism inherent to this format.

## Auto-injected frontend Configure an auto-injected frontend to use SRI

Note that all connected ActiveGates must be on ActiveGate version 1.310+ for at least 30 days before this feature becomes available.

For auto-injected frontends, the Real User Monitoring code is, by default, delivered by OneAgent. To use SRI, you need to [configure your frontend to request the monitoring code from the Dynatrace CDN](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source in the New RUM Experience to meet your specific requirements."), which will allow you to select the necessary snippet format.

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. Under **Real User Monitoring code source**, select **CDN**.
6. Under **Snippet format**, select **OneAgent JavaScript Tag with SRI**.
7. Select **Save**.

## Agentless frontend Configure an agentless frontend to use SRI

The optimal approach to using SRI for an agentless frontend is to integrate the insertion of the OneAgent JavaScript tag with SRI into your build process via the [API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion."). This ensures that your frontend consistently operates with the latest configuration.

To get the OneAgent JavaScript tag with SRI from the web UI

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to instrument.
4. On the **Settings** tab, select **Manual insertion**.
5. Scroll to the **OneAgent JavaScript Tag with SRI** section and select  to copy the RUM JavaScript to the clipboard.

We don't recommend using the OneAgent JavaScript tag with SRI from the web UI unless timely configuration updates are not critical.

## Related topics

* [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")
* [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.")
* [Set up agentless RUM in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")