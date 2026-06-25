---
title: Adjust the sensitivity of anomaly detection for database services
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services-database
scraped: 2026-05-12T11:20:10.822612
---

# Adjust the sensitivity of anomaly detection for database services

# Adjust the sensitivity of anomaly detection for database services

* How-to guide
* 5-min read
* Updated on Jan 28, 2026

Dynatrace detects five types of anomalies for database services: **response time degradations**, **increases in failure rate**, **service load drops**, **service load spikes**, and **failed database connects**. Each anomaly type is detected independently and triggers its own problems and alerts.

To adjust global configuration of anomaly detection for database services

1. Go to **Settings**.
2. Select **Anomaly detection** > **Database services**. Here you can configure detection for each anomaly type.

## Response time degradation

This type of anomaly detection observes the response time of your databases and triggers an alert if a metric violates the specified thresholds. Dynatrace can detect degradation based on automatic baselining or fixed thresholds.

Dynatrace evaluates degradation for two categoriesâall responses and the slowest 10%âand triggers an alert if **any** response time violates the threshold.

To configure the response time degradation detection

Automated baselining

Fixed thresholds

1. Turn on **Detect response time degradation** and select **automatically** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a database should be considered a low load. Databases with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.

1. Turn on **Detect response time degradation** and select **using fixed thresholds** from the list.
2. Set degradation values in the remaining fields. Violation of **any** criterion triggers an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a database should be considered a low load. Databases with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Failure rate increase

This type of anomaly detection observes the failure rate of your database services and triggers an alert if the rate exceeds the specified thresholds. Dynatrace can detect failure rate increase based on automatic baselining or fixed thresholds.

To configure the increased failure rate detection

Automated baselining

Fixed thresholds

1. Turn on **Detect increase in failure rate** and select **automatically** from the list.
2. Specify the **relative %** and **absolute %** values above which alerts should be sent out. **Both** thresholds must be violated to trigger an alert.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a database should be considered a low-load database. Databases with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.

1. Turn on **Detect increase in failure rate** and select **using fixed thresholds** from the list.
2. Specify the **absolute %** value above which alerts should be sent out.
3. Optional To avoid over-alerting, define an **actions/min** rate below which a database should be considered a low-load database. Databases with lower load rates are excluded from evaluation.
4. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.
5. From the **Sensitivity** list, select the sensitivity of the threshold:

   * Low: High statistical confidence is used, so brief violations (for example, due to a surge in load) won't trigger alerts.
   * Medium: Reasonable statistical confidence is used to not alert on every single violation.
   * High: No statistical confidence is used. Each violation triggers an alert.

For fixed thresholds, the problem impact includes the fixed threshold and the amount by which the threshold was exceeded.

## Service load drops

This type of anomaly detection learns the normal behavior of your database service load over a period of 7 days and triggers an alert if the load drops significantly.

To configure the database service drops detection

1. Turn on **Detect service load drops**.
2. Specify the observed load threshold to receive alerts in case of load drops.
3. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.

## Service load spikes

This type of anomaly detection learns the normal behavior of your database service load over a period of 7 days and triggers an alert if the load increases significantly.

To configure the database service spikes detection

1. Turn on **Detect service load spikes**.
2. Specify the observed load threshold to receive alerts in case of load spikes.
3. Optional To avoid accidental alerts, define how long a database must stay in abnormal state to trigger an alert.

## Reference period

Davis automatically generates baselines during a recent reference period. The default reference period is the past **7 days**.

If monitoring data detected during the reference period is no longer validâfor example, if you've deployed a new version of your application that includes major changes, and you're now receiving a high number of alertsâselect **Reset** to establish a new baseline. Davis will purge the previous reference period and immediately begin collecting data for a new reference period.

## Thresholds for a specific database service

As an alternative to defining thresholds globally across your entire environment, you can provide fine-tuned thresholds for individual database services. Database-level thresholds override global thresholds for the database service, while global settings still apply to other databases. You can reverse to globally defined thresholds at any time.

To change threshold settings for a specific database service

1. Go to **Database Services**.
2. Select the database you want to configure.
3. In the browse menu (**â¦**), select **Edit**.
4. Select **Anomaly detection**.
5. Turn off **Use global anomaly detection settings**.
6. Set the database-level thresholds in the same manner as described above for global settings.

## Thresholds for a specific database statement

Davis can intelligently analyze highly divergent statements within the same database. Some statements, however, might require some special attention due to their importance to business-critical functionality. You can achieve that via key statements.

To configure threshold for a key statement

1. Go to **Database Services**.
2. Select the database you want to configure.
3. In the browse menu (**â¦**), select **Edit**.
4. Select **Anomaly detection**.
5. Scroll down to the **Set thresholds on key requests** section and expand the menu of the required key statement.
6. Turn off **Use service or global settings**.
7. Set the statement-level thresholds in the same manner as described above for global settings.

## Related topics

* [Anomaly detection API - Database services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Learn what the Dynatrace Anomaly detection API for database services offers.")