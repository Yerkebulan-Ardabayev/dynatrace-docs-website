---
title: Initial setup for web frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup
scraped: 2026-02-19T21:32:41.269206
---

# Initial setup for web frontends

# Initial setup for web frontends

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Feb 03, 2026

Start your journey with the New RUM Experience using the foundational guides in this section, designed to help you achieve a working setup.

## Already using RUM Classic for your web frontends?

Upgrading to the New RUM Experience is straightforward and unlocks enhanced monitoring capabilities.

[Learn more](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps)

## Instrument new frontends

To get started monitoring your web frontends with the New RUM Experience, follow the instructions below.

1. Find the suitable instrumentation approach

The New RUM Experience offers two approaches for instrumenting your web frontends: Automatic injection and agentless RUM.

#### Automatic injection

Automatic injection is the most convenient way to instrument your web frontends. To use it, the following prerequisites must be met:

* You can access your web server and install [OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.").
* At least one of the application tiers involved in delivering the HTML must be instrumented by a OneAgent code module that supports automatic RUM injection. For a list of supported technologies, see [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

If these conditions are met, we recommend using automatic injection.

If the conditions are met but you prefer to insert the RUM JavaScript manually, create an auto-injected frontend and then follow the instructions in [Use manual insertion for pages of an auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.").

#### Agentless RUM

If automatic injection isnât feasible, use agentless RUM. This approach only requires access to the applicationâs code, not to the web server. To set up agentless RUM, you need to manually insert the RUM JavaScript into each page of your application.

2. Set up your frontend

Once youâve chosen your instrumentation approach, follow the corresponding guide below to set up your frontend.

[**Set up an auto-injected frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[**Set up agentless RUM**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")

3. Finalize your initial setup

Open [![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**](/docs/observe/digital-experience/new-rum-experience/experience-vitals "The Experience Vitals app provides an entry point for monitoring web and mobile frontends.") and navigate to the frontend you created. If your frontend is receiving traffic, the charts should begin displaying data within ten minutes. If they donât, your environment may require further configuration steps. The guides below will walk you through verifying and completing your setup.

[**Finalize the initial setup for your auto-injected frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-auto-injection "Verify and complete the initial setup for your auto-injected frontend.")[**Finalize the initial setup for your agentless frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-agentless "Verify and complete the initial setup for your agentless frontend.")

## Roll out RUM selectively

After deploying OneAgent in full-stack monitoring mode on a host, web applications running on that host are, by default, automatically monitored using RUM. If you prefer to roll out RUM in a more phased manner after deploying OneAgent, follow the instructions in [Roll out RUM selectively for your frontends in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.").

## Explore all initial setup guides

* [Enable the New RUM Experience for your RUM Classic web applications](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps "Learn how to enable the New RUM Experience for your RUM Classic web applications")
* [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")
* [Set up agentless RUM in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")
* [Finalize the initial setup for your auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-auto-injection "Verify and complete the initial setup for your auto-injected frontend.")
* [Finalize the initial setup for your agentless frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-agentless "Verify and complete the initial setup for your agentless frontend.")
* [Set up host name determination in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-host-name-determination "Learn how to set up host name determination in the New RUM Experience.")
* [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")
* [Use Subresource Integrity (SRI) in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature in the New RUM Experience to ensure the integrity of Real User Monitoring code.")
* [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.")
* [Adapt CSP rules for the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules "Learn how to adapt your CSP rules for the New RUM Experience.")
* [Configure the Real User Monitoring code source in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source "Configure the Real User Monitoring code source in the New RUM Experience to meet your specific requirements.")
* [Configure the beacon endpoint for web frontends in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements.")
* [Roll out RUM selectively for your frontends in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")