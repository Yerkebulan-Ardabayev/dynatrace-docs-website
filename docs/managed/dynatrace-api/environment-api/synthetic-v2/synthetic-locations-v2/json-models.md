---
title: Synthetic locations API v2 - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models
---

# Synthetic locations API v2 - JSON models

# Synthetic locations API v2 - JSON models

* Reference
* Published Jul 13, 2020

Some JSON models of the **Synthetic locations** API vary depending on its **type**. Here you can find JSON models for each variation.

## Variations of the `SyntheticLocation` object

The `SyntheticLocation` object is the base for synthetic locations. The actual set of fields depends on the **type** of the location.

### CLUSTER and PRIVATE

PrivateSyntheticLocation

Parameters

JSON model

#### The `PrivateSyntheticLocation` object

Configuration of a private synthetic location.

Some fields are inherited from the base *SyntheticLocation* object.

| Element | Type | Description |
| --- | --- | --- |
| autoUpdateChromium | boolean | Non-containerized location property. Auto upgrade of Chromium is enabled (`true`) or disabled (`false`). |
| availabilityLocationOutage | boolean | Alerting for location outage is enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. |
| availabilityNodeOutage | boolean | Alerting for node outage is enabled (`true`) or disabled (`false`). \n\n If enabled, the outage of *any* node in the location triggers an alert. Supported only for private Synthetic locations. |
| availabilityNotificationsEnabled | boolean | Notifications for location and node outage are enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. |
| browserExecutionSupported | boolean | Containerized location property. Boolean value describes if browser monitors will be executed on this location:  * `false`: Browser monitor executions disabled. * `true`: Browser monitor executions enabled. |
| city | string | The city of the location. |
| countryCode | string | The country code of the location.  To fetch the list of available country codes, use the [GET all countries﻿](https://dt-url.net/37030go?dt=m) request. |
| countryName | string | The country name of the location. |
| deploymentType | string | The deployment type of the location:  * `STANDARD`: The location is deployed on Windows or Linux. * `KUBERNETES`: The location is deployed on Kubernetes. The element can hold these values * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | The Dynatrace entity ID of the location. |
| fipsMode | string | Containerized location property indicating whether FIPS mode is enabled on this location:  * `DISABLED`: FIPS is not enabled on the location. * `ENABLED`: FIPS is enabled on the location. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS with corporate proxy is enabled on this location.   Default: DISABLED The element can hold these values * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| geoLocationId | string | The Dynatrace GeoLocation ID of the location. |
| latitude | number | The latitude of the location in `DDD.dddd` format. |
| locationNodeOutageDelayInMinutes | integer | Alert if location or node outage lasts longer than *X* minutes. \n\n Only applicable when `availabilityLocationOutage` or `availabilityNodeOutage` is set to `true`. Supported only for private Synthetic locations. |
| longitude | number | The longitude of the location in `DDD.dddd` format. |
| namExecutionSupported | boolean | Containerized location property. Boolean value describes if icmp monitors will be executed on this location:  * `false`: Icmp monitor executions disabled. * `true`: Icmp monitor executions enabled. |
| name | string | The name of the location. |
| nodeNames | object | A mapping id to name of the nodes belonging to the location. |
| nodes | string[] | A list of synthetic nodes belonging to the location.  You can retrieve the list of available nodes with the [GET all nodes﻿](https://dt-url.net/miy3rpl?dt=m) call. |
| regionCode | string | The region code of the location.  To fetch the list of available region codes, use the [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m) request. |
| regionName | string | The region name of the location. |
| status | string | The status of the location:  * `ENABLED`: The location is displayed as active in the UI. You can assign monitors to the location. * `DISABLED`: The location is displayed as inactive in the UI. You can't assign monitors to the location. Monitors already assigned to the location will stay there and will be executed from the location. * `HIDDEN`: The location is not displayed in the UI. You can't assign monitors to the location. You can only set location as `HIDDEN` when no monitor is assigned to it. The element can hold these values * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | -The element can hold these values * `CLUSTER` * `PRIVATE` * `PUBLIC` |
| useNewKubernetesVersion | boolean | Containerized location property. Boolean value describes which kubernetes version will be used:  * `false`: Version 1.23+ that is older than 1.26 * `true`: Version 1.26+. |

```
{



"entityId": "SYNTHETIC_LOCATION-F23EE93163E76BE2",



"type": "PRIVATE",



"status": "ENABLED",



"name": "Sample synthetic location",



"countryCode": "PL",



"regionCode": "82",



"city": "Gdańsk",



"latitude": 54.389,



"longitude": 18.6255,



"nodes": [



"2131628184"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000,



"geoLocationId": "GEOLOCATION-AA22893EF461842C"



}
```

### PUBLIC

PublicSyntheticLocation

Parameters

JSON model

#### The `PublicSyntheticLocation` object

Configuration of a public synthetic location.

| Element | Type | Description |
| --- | --- | --- |
| browserType | string | The type of the browser the location is using to execute browser monitors. |
| browserVersion | string | The version of the browser the location is using to execute browser monitors. |
| capabilities | string[] | A list of location capabilities. |
| cloudPlatform | string | The cloud provider where the location is hosted. The element can hold these values * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| ips | string[] | The list of IP addresses assigned to the location. |
| stage | string | The stage of the location. The element can hold these values * `BETA` * `COMING_SOON` * `DELETED` * `GA` |

```
{



"name": "US Central",



"entityId": "SYNTHETIC_LOCATION-00000000000001A5",



"type": "PUBLIC",



"cloudPlatform": "GOOGLE_CLOUD",



"ips": [



"210.6.226.150",



"185.77.153.103",



"153.242.5.43"



],



"stage": "BETA",



"status": "ENABLED",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-AA22893EF461842C"



}
```

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")