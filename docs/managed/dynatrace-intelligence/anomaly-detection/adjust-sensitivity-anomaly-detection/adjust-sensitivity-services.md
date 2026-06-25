---
title: Adjust the sensitivity of anomaly detection for services
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services
scraped: 2026-05-12T11:20:49.401762
---

# Adjust the sensitivity of anomaly detection for services

# Adjust the sensitivity of anomaly detection for services

* How-to guide
* 6-min read
* Updated on Jan 28, 2026

Dynatrace detects four types of anomalies for services: **response time degradations**, **increases in failure rate**, **service load drops**, and **service load spikes**. Each anomaly type is detected independently and triggers its own problems and alerts.

To adjust global configuration of anomaly detection for services

1. Go to **Settings**.
2. Select **Anomaly detection** > **Services**. Here you can configure detection for each anomaly type.

## Response time degradation

This type of anomaly detection observes the response time of your services and triggers an alert if a metric violates the specified thresholds. Dynatrace can detect degradation based on automatic baselining (relative threshold) or fixed thresholds (absolute threshold).

Dynatrace evaluates degradation for two categories:

* All responses: alert is raised if the median response time of all requests degrades beyond both the absolute and relative thresholds.
* Slowest 10% responses: alert is raised if response time of the slowest 10% of requests degrades beyond both the absolute and relative thresholds.

To configure response time degradation detection

Automated baselining

Fixed thresholds

1. Turn on **Detect response time degradation** and select **automatically** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a service should be considered a low load. Services with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.

1. Turn on **Detect response time degradation** and select **using fixed thresholds** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a service should be considered a low-load service. Services with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Failure rate increase

This type of anomaly detection observes the failure rate of your services and triggers an alert if the rate exceeds the specified thresholds. Dynatrace can detect failure rate increase based on automatic baselining or fixed thresholds.

To configure the increased failure rate detection

Automated baselining

Fixed thresholds

1. Turn on **Detect increase in failure rate** and select **automatically** from the list.
2. Specify the **relative %** and **absolute %** values above which alerts should be sent out. **Both** thresholds must be violated to trigger an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a service should be considered a low-load service. Services with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.

1. Turn on **Detect increase in failure rate** and select **using fixed thresholds** from the list.
2. Specify the **absolute %** value above which alerts should be sent out.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a service should be considered a low-load service. Services with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Service load drops

This type of anomaly detection learns the normal behavior of your service load over a period of 7 days and triggers an alert if the load drops significantly.

To configure service drops detection

1. Turn on **Detect service load drops**.
2. Specify the observed load threshold to receive alerts in case of load drops.
3. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.

## Service load spikes

This type of anomaly detection learns the normal behavior of your service load over a period of 7 days and triggers an alert if the load increases significantly.

To configure service spikes detection

1. Turn on **Detect service load spikes**.
2. Specify the observed load threshold to receive alerts in case of load spikes.
3. Optional To avoid accidental alerts, define how long a service must stay in abnormal state to trigger an alert.

## Reference period

Davis automatically generates baselines during a recent reference period. The default reference period is the past **7 days**.

If monitoring data detected during the reference period is no longer validâfor example, if you've deployed a new version of your application that includes major changes, and you're now receiving a high number of alertsâselect **Reset** to establish a new baseline. Davis will purge the previous reference period and immediately begin collecting data for a new reference period.

## Thresholds for a specific service

As an alternative to defining thresholds globally across your entire environment, you can provide fine-tuned thresholds for individual services. Service-level thresholds override global thresholds for the service, while global settings still apply to other services. You can revert to globally defined thresholds at any time.

To change threshold settings for a specific service

1. Go to **Services**.
2. Select the service you want to configure.
3. In the browse menu (**â¦**), select **Settings**.
4. Select **Anomaly detection**.
5. Turn off **Use global anomaly detection settings**.
6. Set the service-level thresholds in the same manner as described above for global settings.

## Thresholds for a specific web request

By understanding the baseline performance of individual service requests, Davis can intelligently analyze highly divergent response times of multiple requests within the same service. For example, while the service request `orange.jsf` might have a median response time of `200 ms`, the request `orange-booking-payment.jsf` within the same service might be faster, with a median response time of `25 ms`. Davis understands such differences and raises an alert if either request begins to respond more slowly than these established baselines.

There are, however, use cases for which parameterization of automatic baselining algorithms might be beneficial at the request level. These include:

* To set lower response-time thresholds for specific, business-critical service requests.
* To set higher response-time thresholds for volatile service requests that are non-business critical.
* To set a fixed threshold rather than a relative threshold for requests that have a defined SLA.
* To set a fixed threshold rather than a relative threshold for requests that have a defined timeout point.
* To disable alerting for specific, non-business critical requests.

Each of these use cases can now also be achieved by setting request-level thresholds for a [key web request](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business."). To configure threshold for a key request

1. Go to **Services**.
2. Select the service you want to configure.
3. In the browse menu (**â¦**), select **Settings**.
4. Select **Anomaly detection**.
5. Scroll down to the **Set thresholds on key requests** section and expand the menu of the required key request.
6. Turn off **Use service or global settings**.
7. Set the request-level thresholds in the same manner as described above for global settings.

## Related topics

* [Anomaly detection API - Services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Learn what the Dynatrace Anomaly detection API for services offers.")