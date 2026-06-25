---
title: Customize IP address detection for mobile applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile
scraped: 2026-05-12T11:20:17.930536
---

# Customize IP address detection for mobile applications

# Customize IP address detection for mobile applications

* How-to guide
* 1-min read
* Updated on Mar 21, 2024

When web requests and RUM beacons are directly sent to an instrumented server, Dynatrace identifies the IP addresses of your end users' devices via the socket connections.

When you use uninstrumented components such as load balancers, CDNs, or proxies, the remote IP address is different from the original IP address. For such cases, Dynatrace also watches certain HTTP headers. These headers are most frequently used to identify the originating IP address when a client connects to a web server through an HTTP proxy, a CDN, or a load balancer.

You can view the list of headers that Dynatrace uses to determine client IP addresses for your applications. To do that, go to **Settings** > **Web and mobile monitoring** > **IP determination**. Dynatrace processes these headers in a specific order, but you can change the processing order and add your own headers.

## Manage default headers

You can update header names, delete headers you don't need, and change the order in which Dynatrace processes the headers.

1. Go to **Settings** > **Web and mobile monitoring** > **IP determination**.
2. Manage the headers:

   * To rename a header, select **Expand row** ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row"), and then enter a new header name.
   * To delete a header, select **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove").
   * To change a header's priority, select and hold **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") next to the header name, and move the header up or down.

## Add your custom client IP headers

If your client IP addresses are located in a different header, create a custom rule so that Dynatrace can correctly identify the IP addresses.

To add a custom client IP header

1. Go to **Settings** > **Web and mobile monitoring** > **IP determination**.
2. Select **Create custom client IP header**.
3. Provide the name of your header.

You can create up to 10 custom client IP headers per environment.

Adding a custom client IP header might be required in one of the following cases.

* When the header that contains your client IP addresses is not in our list of headers under **Settings** > **Web and mobile monitoring** > **IP determination**.
* When the client IP addresses for your applications are stored in a proprietary header.
* When the client IP addresses are not detected correctly, for instance, when the IP addresses of your load balancers are shown in Dynatrace.

## Reasons for incorrect client IP addresses

There might be several reasons why you don't see the correct client IP addresses for your application. Check the sections above for detailed instructions.

| Issue | Possible solution |
| --- | --- |
| The client IP addresses for your applications are located in a header that is not in our list. | Add a custom client IP header. |
| You have provided the incorrect custom client IP header. | Update the header name. |
| The custom client IP header that you provided does not actually contain IP addresses. | Specify another custom client IP header. |
| The order of the headers is not correct. | Change the processing order of the headers. |
| Your infrastructure isn't configured to add a header that propagates the client IP addresses. | Reconfigure your infrastructure. |
| The header that contains the client IP addresses is not part of the beacon requests.[1](#fn-1-1-def) | Reconfigure your infrastructure. |

1

The IP detection headers in regular requests of the application are irrelevant for the IP detection of captured RUM data, even when they are captured as traces and those traces are correlated to user actions.

## Related topics

* [Detection of IP addresses, geolocations, and user agents](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")