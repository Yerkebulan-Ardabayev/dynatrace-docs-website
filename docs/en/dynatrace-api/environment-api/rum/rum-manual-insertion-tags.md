---
title: RUM manual insertion tags API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags
scraped: 2026-03-06T21:32:36.491296
---

# RUM manual insertion tags API


* Reference

The **RUM manual insertion tags API** allows you to retrieve the RUM JavaScript for two different manual insertion scenarios:

* Agentless monitoring and
* [Manual insertion for pages of an auto-injected application](../../../observe/digital-experience/web-applications/initial-setup/rum-injection.md#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").

Different snippet formats are available, and supported tag attributes can be controlled via API parameters. By integrating this API into your build scripts, you can automate the insertion of the RUM JavaScript and ensure that your application always uses the current configuration.

To retrieve the snippet format [code snippet](../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), use the Real User Monitoring JavaScript API.

### Get JavaScript tag

Retrieve the most recent JavaScript tag for manual insertion.### Get OneAgent JavaScript tag

Retrieve the most recent OneAgent JavaScript tag for manual insertion.### Get OneAgent JavaScript tag with SRI

Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.### Get inline code

Retrieve the most recent inline code for manual insertion.