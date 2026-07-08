---
title: Adjust the sensitivity of anomaly detection for applications
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-applications
---

# Adjust the sensitivity of anomaly detection for applications

# Adjust the sensitivity of anomaly detection for applications

* How-to guide
* 5-min read
* Published Sep 06, 2021

Dynatrace detects four types of anomalies for applications: **key performance metric degradations**, **traffic drops**, **traffic spikes**, and **increases in failure rate**. Each anomaly type is detected independently and triggers its own problems and alerts.

To adjust global configuration of anomaly detection for applications

1. Go to **Settings** > **Anomaly detection** and select **Web applications**, **Mobile apps**, or **Custom apps**.

## Key performance metric degradation

This type of anomaly detection observes [key performance metrics](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics#kpm "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") and triggers an alert if a metric violates the specified threshold. Dynatrace can detect degradation based on automatic baselining or fixed thresholds.

Dynatrace evaluates degradation for two categories—all actions and the slowest 10%—and triggers an alert if **any** metric violates the threshold.

To configure key performance metric degradation detection

Automated baselining

Fixed thresholds

1. Turn on **Detect key performance metric time degradations** and select **automatically** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which an application should be considered a low-traffic application. Applications with lower traffic rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long an application must stay in abnormal state to trigger an alert.

1. Turn on **Detect key performance metric time degradations** and select **using fixed thresholds** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which an application should be considered a low-traffic application. Applications with lower traffic rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long an application must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Traffic drops

This type of anomaly detection learns the normal behavior of your application's traffic over a period of 7 days and triggers an alert if the traffic drops significantly.

To configure traffic drops detection

1. Turn on **Detect traffic drops**.
2. Specify the observed traffic threshold to receive alerts in case of traffic drops.

## Traffic spikes

This type of anomaly detection learns the normal behavior of your application's traffic over a period of 7 days and triggers an alert if the traffic rises significantly.

To configure traffic spikes detection

1. Turn on **Detect traffic spikes**.
2. Specify the observed traffic threshold to receive alerts in case of traffic spikes.

## Failure rate increase

This type of anomaly detection observes the failure rate of your applications and triggers an alert if the rate exceeds the specified thresholds. Dynatrace can detect failure rate increase based on automatic baselining or fixed thresholds.

To configure the increased failure rate detection

Automated baselining

Fixed thresholds

1. Turn on **Detect increase in failure rate** and select **automatically** from the list.
2. Specify the **relative %** and **absolute %** values above which alerts should be sent out. **Both** thresholds must be violated to trigger an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which an application should be considered a low-traffic application. Applications with lower traffic rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long an application must stay in abnormal state to trigger an alert.

1. Turn on **Detect increase in failure rate** and select **using fixed thresholds** from the list.
2. Specify the **absolute %** value above which alerts should be sent out.
3. Optional To avoid over-alerting, define an **actions/min** rate below which an application should be considered a low-traffic application. Applications with lower traffic rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long an application must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Reference period

Davis automatically generates baselines during a recent reference period. The default reference period is the past **7 days**.

If monitoring data detected during the reference period is no longer valid—for example, if you've deployed a new version of your application that includes major changes, and you're now receiving a high number of alerts—select **Reset** to establish a new baseline. Davis will purge the previous reference period and immediately begin collecting data for a new reference period.

## Thresholds for a specific application

As an alternative to defining thresholds globally across your entire environment, you can provide fine-tuned thresholds for individual applications. Application-level thresholds override global thresholds for the application, while global settings still apply to other applications. You can revert to globally defined thresholds at any time.

To change threshold settings for a specific application

1. Go to **Web**, **Mobile**, **Frontend**, or **Custom Applications**, depending on the application type.
2. Select the application you want to configure.
3. In the browse menu (**…**), select **Edit**.
4. Select **Anomaly detection**.
5. Turn off **Use global anomaly detection settings**.
6. Set the application-level thresholds in the same manner as described above for global settings.

## Related topics

* [Anomaly detection API - Applications](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Learn what the Dynatrace Anomaly detection API for applications offers.")
* [Work with key performance metrics in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.")