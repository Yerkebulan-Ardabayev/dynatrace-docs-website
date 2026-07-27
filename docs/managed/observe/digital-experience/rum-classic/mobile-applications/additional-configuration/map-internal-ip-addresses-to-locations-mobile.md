---
title: Map internal IP addresses to locations for mobile applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile
---

# Map internal IP addresses to locations for mobile applications in RUM Classic

# Map internal IP addresses to locations for mobile applications in RUM Classic

* How-to guide
* 1-min read
* Updated on Jul 21, 2026

Dynatrace Real User Monitoring Classic groups [user sessions and user actions per location](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") and shows them on the [world map](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your mobile application.").

If you don't see data for some of your application's users on the world map, it might be because those users have private IP addresses. You can map such internal IP addresses to real geographic locations. The granularity of regional performance analysis increases as the number of detected user requests goes up in a specific region (continent, country, state, or city). You can even override auto-detected IP addresses if necessary to improve mapping accuracy.

To add an IP address mapping rule

1. Go to **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. Under **IP address mapping rules**, select **Add item**.
3. Specify the IP address or IP range, and then set the **Country**, **Region**, and **City**.

If you have numerous custom IP addresses to import, it's more convenient to use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), specifically the [Map IP addresses to locations schema](/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings "View builtin:rum.ip-mappings settings schema table of your monitoring environment via the Dynatrace API.").

## Related topics

* [Settings API - Map IP addresses to locations schema table](/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings "View builtin:rum.ip-mappings settings schema table of your monitoring environment via the Dynatrace API.")