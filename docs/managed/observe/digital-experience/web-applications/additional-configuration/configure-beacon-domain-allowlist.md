---
title: Configure beacon origin allowlist for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist
scraped: 2026-05-12T11:19:43.824004
---

# Configure beacon origin allowlist for web applications

# Configure beacon origin allowlist for web applications

* How-to guide
* 3-min read
* Updated on Jan 23, 2024

Use the beacon origin allowlist to specify the origins from which your [application beacon endpoints](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") should accept cross-origin RUM beacons.

## Same- and cross-origin beacons

The RUM JavaScript sends RUM beacons to report the captured data to Dynatrace. Depending on the injection method, there are two default setups:

* **Auto-injected applications > same-origin beacons**

  When the [RUM JavaScript is injected automatically](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), RUM beacons are sent back to the web or application server that hosts the auto-injected application; OneAgent provides a beacon endpoint.

  By default, the beacons of auto-injected applications are **same-origin beacons** since the protocol, host, and port of the beacon requests and the page where they're issued are identical.

  If you opted for one of the [alternative beacon endpoint setups](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.")âwhere the beacons of an auto-injected application are sent to a Cluster ActiveGate or an instrumented server on a different domainâRUM beacons are **cross-origin beacons**.
* **Agentless applications > cross-origin beacons**

  When [agentless monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") is used, RUM beacons are sent to a beacon endpoint that is part of a Cluster ActiveGate.

  For agentless applications, the RUM beacons are **cross-origin beacons** since they're sent to a different domain.

Browsers adhere to the same-origin policy that, by default, allows scripts to issue requests only to the same origin. To send cross-origin requests, Cross-Origin Resource Sharing (CORS) needs to be used, which allows servers to specify origins that are permitted to access the server. Therefore, cross-origin RUM beacons need to use CORS. In this case:

* The browser adds an `Origin` header to the cross-origin beacon.
* By default, the beacon endpoint adds an `Access-Control-Allow-Origin` header to each response that allows the origin provided in the `Origin` header.

Using the beacon origin allowlist, you can specify from which origins your beacon endpoints should accept RUM beacons.

## Specify beacon origins for CORS

Create a beacon origin rule to specify from which origins the OneAgent and Cluster ActiveGate should accept RUM beacons.

Right after you add the first beacon origin rule, applications that don't match that rule will stop collecting RUM data unless their beacons are sent to the same origin and handled by OneAgent.

To add a beacon origin rule

1. Go to **Settings** > **Web and mobile monitoring** > **Beacon origins for CORS**.
2. Select **Add item**.
3. Provide the correct pattern for the origin you want to specify.

   ![Add a beacon origin rule](https://dt-cdn.net/images/add-beacon-origin-rule-1912-783d3ea903.png)

   Add a beacon origin rule

You can add up to 20 beacon origin rules per environment.

## Application of beacon origin allowlist in different scenarios

![Beacon origin allowlist flowchart](https://dt-cdn.net/images/beacon-origin-allowlist-after-settings-conversion-716-6a55b387ba.png)

Beacon origin allowlist flowchart

This flowchart shows how Dynatrace applies the beacon origin allowlist in different scenarios. Use it to understand whether a specific beacon origin is allowed.

* If the beacon origin allowlist is empty, RUM beacons from any origin are accepted by all beacon endpoints.
* If an origin is on the allowlist, a RUM beacon from that origin is accepted. In the cross-origin case, the origin is copied to the `Access-Control-Allow-Origin` header of the response, and the beacon response returns the `200 OK` HTTP status code.
* If an origin is not on the allowlist, a cross-origin RUM beacon from that origin is rejected. The beacon fails with the `403 Forbidden` status code and a message such as `Value in Origin Header is not allowed`.
* OneAgent doesn't apply the beacon origin allowlist to same-origin beacons.