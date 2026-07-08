---
title: Synthetic locations API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models
---

# Synthetic locations API - JSON models

# Synthetic locations API - JSON models

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

**countryCode**, **regionCode**, **city** parameters are optional as they can be retrieved based on **latitude** and **longitude** of location.

| Element | Type | Description |
| --- | --- | --- |
| autoUpdateChromium | boolean | Non-containerized location property. Auto upgrade of Chromium is enabled (`true`) or disabled (`false`). |
| availabilityLocationOutage | boolean | Alerting for location outage is enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. |
| availabilityNodeOutage | boolean | Alerting for node outage is enabled (`true`) or disabled (`false`). \n\n If enabled, the outage of *any* node in the location triggers an alert. Supported only for private Synthetic locations. |
| availabilityNotificationsEnabled | boolean | Notifications for location and node outage are enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. |
| browserExecutionSupported | boolean | Containerized location property. Boolean value describes if browser monitors will be executed on this location:  * `false`: Browser monitor executions disabled. * `true`: Browser monitor executions enabled. |
| deploymentType | string | The deployment type of the location:  * `STANDARD`: The location is deployed on Windows or Linux. * `KUBERNETES`: The location is deployed on Kubernetes. The element can hold these values * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| fipsMode | string | Containerized location property indicating whether FIPS mode is enabled on this location:  * `DISABLED`: FIPS is not enabled on the location. * `ENABLED`: FIPS is enabled on the location. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS with corporate proxy is enabled on this location.   Default: DISABLED The element can hold these values * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| locationNodeOutageDelayInMinutes | integer | Alert if location or node outage lasts longer than *X* minutes. \n\n Only applicable when `availabilityLocationOutage` or `availabilityNodeOutage` is set to `true`. Supported only for private Synthetic locations. |
| maxActiveGateCount | integer | Containerized location property. The maximum number of ActiveGates deployed for the location (required for a Kubernetes location). |
| minActiveGateCount | integer | Containerized location property. The minimum number of ActiveGates deployed for the location (required for a Kubernetes location). |
| namExecutionSupported | boolean | Containerized location property. Boolean value describes if icmp monitors will be executed on this location:  * `false`: Icmp monitor executions disabled. * `true`: Icmp monitor executions enabled. |
| nodeSize | string | Containerized location property. The size of a containerized node deployed for the location (required for a Kubernetes location). Accepted values:  * `XS`: extra small * `S`: small * `M`: medium   The node size `L` is not supported in containerized locations. The element can hold these values * `M` * `S` * `UNSUPPORTED` * `XS` |
| nodes | string[] | A list of synthetic nodes belonging to the location.  You can retrieve the list of available nodes with the [GET all nodes﻿](https://dt-url.net/miy3rpl) call. |
| useNewKubernetesVersion | boolean | Containerized location property. Boolean value describes which kubernetes version will be used:  * `false`: Version 1.23+ that is older than 1.26 * `true`: Version 1.26+. |

```
{



"entityId": "SYNTHETIC_LOCATION-F23EE93163E76BE2",



"type": "PRIVATE",



"name": "Sample synthetic location",



"countryCode": "PL",



"regionCode": "82",



"city": "Gdańsk",



"latitude": 54.389,



"longitude": 18.6255,



"status": "ENABLED",



"nodes": [



"2131628184"



]



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



"entityId": "GEOLOCATION-AA22893EF461842C",



"type": "PUBLIC",



"cloudPlatform": "GOOGLE_CLOUD",



"ips": [



"200.198.18.147",



"186.202.218.192",



"221.120.251.140"



],



"stage": "GA",



"status": "ENABLED"



}
```

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")