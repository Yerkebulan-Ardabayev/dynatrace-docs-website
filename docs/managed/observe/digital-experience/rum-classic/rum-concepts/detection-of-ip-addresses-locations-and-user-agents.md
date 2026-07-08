---
title: Detection of IP addresses, geolocations, and user agents in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents
---

# Detection of IP addresses, geolocations, and user agents in RUM Classic

# Detection of IP addresses, geolocations, and user agents in RUM Classic

* Explanation
* 3-min read
* Updated on Mar 21, 2024

Dynatrace automatically detects IP addresses and geolocations as well as browsers, devices, and operating systems.

## IP addresses

When web requests and RUM beacons are directly sent to an instrumented server, Dynatrace identifies the IP addresses of your end users' devices via the socket connections.

When you use uninstrumented components such as load balancers, CDNs, or proxies, the remote IP address is different from the original IP address. For such cases, Dynatrace also watches certain HTTP headers. These headers are most frequently used to identify the originating IP address when a client connects to a web server through an HTTP proxy, a CDN, or a load balancer.

You can view the list of headers that Dynatrace uses to determine client IP addresses for your applications. To do that, go to **Settings** > **Web and mobile monitoring** > **IP determination**. Dynatrace processes these headers in a specific order, but you can change the processing order and add your own headers for your [web](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications."), [mobile](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Change the way Dynatrace determines client IP addresses for your mobile applications."), and [custom applications](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.").

Keep in mind that Dynatrace [masks the last part of end-user IP addresses](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") by default.

## Geolocations

Dynatrace Real User Monitoring Classic tries to assign every [user session](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") a geolocation (city, region, and country) to group user sessions and [user actions](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") per location and show them on the world map for your [web](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), [mobile](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your mobile application."), and [custom applications](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your custom application.").

For web applications, Dynatrace uses the [MaxMind Geo2 database﻿](https://www.maxmind.com) to map and resolve IP addresses to geographical locations.

For mobile apps, the IP address mapping depends on whether the mobile app has permission to access the geolocation information.

* **With permission**. Dynatrace uses the device coordinates (GPS or Wi-Fi) and calculates the city that is closest to the reported GPS location.
* **No permission**. Dynatrace uses the IP address and the [MaxMind Geo2 database﻿](https://www.maxmind.com) to determine the geolocation.

Dynatrace automatically updates the MaxMind Geo2 database in your environment with the release of each new version of Dynatrace.

Request updates to the MaxMind database when IP addresses don't resolve correctly

If you discover an error in MaxMind mapping, you can [request that MaxMind update their database﻿](https://www.maxmind.com/en/geoip-data-correction-request). After MaxMind changes an IP address mapping, the mapping in your Dynatrace environment is updated with the Dynatrace version following the change.

You can check your IP address against the MaxMind database at any time via the [GeoIP2 Databases Demo﻿](https://www.maxmind.com/en/geoip-demo) form.

For custom locations that have internal or private IP addresses, like your different offices, you can define custom IP mappings. You can even overwrite the default IP address mappings via custom IP address mapping rules for your [web](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are."), [mobile](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are."), and [custom applications](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.").

Dynatrace also [masks the GPS coordinates](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") by default.

## Browsers, devices, and operating systems

For web applications, Dynatrace uses the [user agent string﻿](https://developer.mozilla.org/docs/Web/HTTP/Headers/User-Agent) sent by the browser to distinguish user sessions of real users from synthetic and robots (user types: **Bot**, **Real**, and **Synthetic**). It also leverages this string to identify operating systems and device types like desktop, tablet, or mobile. For browser classification, Dynatrace uses the [udger.com﻿](https://udger.com) user agent database.

For Android apps, device names are provided by [Google Play Store﻿](https://support.google.com/googleplay/answer/1727131?hl=en-GB). For iOS apps, Dynatrace maintains a cross-reference list that maps Apple device IDs to Apple device names. The operating system—Android or iOS—is provided by Dynatrace OneAgent for Mobile.

Internet service providers (ISPs) are detected based on their IP addresses against the MaxMind database.