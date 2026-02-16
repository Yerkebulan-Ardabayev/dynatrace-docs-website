---
title: RUM manual insertion tags API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags
scraped: 2026-02-16T21:29:09.227504
---

# RUM manual insertion tags API

# RUM manual insertion tags API

* Reference

The **RUM manual insertion tags API** allows you to retrieve the RUM JavaScript for two different manual insertion scenarios:

* [Agentless monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") and
* [Manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").

Different [snippet formats](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") are available, and supported tag attributes can be controlled via API parameters. By integrating this API into your build scripts, you can automate the insertion of the RUM JavaScript and ensure that your application always uses the current configuration.

To retrieve the snippet format [code snippet](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), use the [Real User Monitoring JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

[### Get JavaScript tag

Retrieve the most recent JavaScript tag for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")[### Get OneAgent JavaScript tag

Retrieve the most recent OneAgent JavaScript tag for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")[### Get OneAgent JavaScript tag with SRI

Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.")[### Get inline code

Retrieve the most recent inline code for manual insertion.](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")