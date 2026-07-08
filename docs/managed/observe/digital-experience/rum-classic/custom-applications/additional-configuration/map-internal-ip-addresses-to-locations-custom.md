---
title: Map internal IP addresses to locations for custom applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom
---

# Map internal IP addresses to locations for custom applications in RUM Classic

# Map internal IP addresses to locations for custom applications in RUM Classic

* How-to guide
* 1-min read
* Published Jan 30, 2023

Dynatrace Real User Monitoring Classic groups [user sessions and user actions per location](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") and shows them on the [world map](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your custom application.").

If you don't see data for some of your application's users on the world map, it might be because those users have private IP addresses. You can map such internal IP addresses to real geographic locations. The granularity of regional performance analysis increases as the number of detected user requests goes up in a specific region (continent, country, state, or city). You can even override auto-detected IP addresses if necessary to improve mapping accuracy.

To add an IP address mapping rule

1. Go to **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. Under **IP address mapping rules**, select **Add item**.
3. Specify the IP address or IP range, and then set the **Country**, **Region**, and **City**.

If you have numerous custom IP addresses to import, it's more convenient to use the Dynatrace API, specifically the [IP address mapping rules - PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Update the configuration of IP address mapping via the Dynatrace API.") method.

## Related topics

* [Geographic regions - IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Learn what the Dynatrace configuration API for IP address mapping rules offers.")