---
title: Types of synthetic monitors in Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors
---

# Types of synthetic monitors in Classic

# Types of synthetic monitors in Classic

* Explanation
* 3-min read
* Published Oct 06, 2017

Synthetic Monitoring Classic is about proactively simulating user visits, regardless of whether or not real users are currently visiting your site. Dynatrace Synthetic Monitoring Classic provides you with 24x7 global visibility into your applications. An HTTP monitor uses simple HTTP requests. A browser monitor involves much more—it drives real web browser sessions with full HTML5/AJAX support.

Dynatrace offers these types of synthetic monitors: single-URL browser monitors, browser clickpaths, HTTP monitors and NAM monitors.

## Single-URL browser monitors

A [single-URL browser monitor](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.") is the equivalent of a simulated user visiting your application using a modern, updated web browser. Browser monitors can be configured to run from any of our [global public](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring Classic locations.") or [private locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") at frequencies of up to every five minutes. Browser monitors alert you when your application becomes inaccessible or when baseline performance degrades significantly.

## Browser clickpaths

[Browser clickpaths](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") are simulated user visits that monitor your application’s business-critical workflows. You can use the Dynatrace recorder (or you can use [script mode](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.")) to capture an exact sequence of clicks and user input that you're interested in monitoring for availability and performance. Once you’ve captured the mouse clicks and additional user actions that you want your browser clickpath to include, you can schedule the browser clickpath to run automatically at regular intervals from our global public or private locations to test your site’s availability and performance.

## HTTP monitors

[HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") comprise simple HTTP requests. You can use them to monitor the availability of your API endpoints or perform simple HTTP checks for single-resource availability. You can also set up performance thresholds for HTTP monitors. As with browser monitors, HTTP monitors run automatically at regular intervals from our global public or private locations.

HTTP monitors executed by an [ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") from a private Synthetic location can be used to check the availability of your internal resources that are inaccessible from outside your network. Note that on private locations, capacity usage is tracked separately for a subtype, [**high-resource HTTP monitors**](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations."). These monitors have special resource-intensive features such as pre- or post-execution scripts, OAuth2 authorization, or Kerberos authentication.

## Network availability monitoring

[Network availability monitoring](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/nam-for-managed) (NAM) allows you to monitor the availability of remote hosts or services over the network when an HTTP/HTTPS endpoint isn't available.

NAM enables you to create synthetic network availability monitors of the following types:

* ICMP—Sends pings with a configurable number of packets or size to validate if there's a network connection to the host or device. It also checks the quality of that connection.
* TCP—Establishes a TCP connection to a particular port. It validates if a port is open and if it accepts TCP connections. It also checks if a host is available through the network.
* DNS—Validates if a hostname can be resolved to an IP address.

NAM monitors only work with private locations. To learn more about private locations, see [Private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations "Learn about private locations in Synthetic Classic.").

## Supported browsers

The supported browser for the Dynatrace Synthetic Recorder is Google Chrome (latest version, backwards compatible).

The browser used for executing browser monitors from public locations is listed on the Frequency and locations page when you create or edit a browser monitor.

See [Browser monitors in private locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for browser versions you should install on a Synthetic-enabled ActiveGate running private browser monitors.

## Synthetic monitor security

To enhance synthetic monitor security, Dynatrace blocks monitors from sending requests to a local host (for example, `localhost` or `127.0.0.1`).

Additionally, you can read about [credential vault security architecture](/managed/manage/credential-vault#security "Store and manage credentials in the credential vault.") for synthetic monitoring credentials.