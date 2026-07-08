---
title: Extending Dynatrace (Davis data units)
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units
---

# Extending Dynatrace (Davis data units)

# Extending Dynatrace (Davis data units)

* 8-min read
* Published Mar 30, 2020

Davis data units (DDU) provide a simple means of licensing certain capabilities (custom metrics, log monitoring, and custom events) on the Dynatrace platform. Think of DDUs as a kind of Dynatrace currency. In the same way that license consumption for Dynatrace RUM and Synthetic Monitoring relies on [Digital Experience Monitoring (DEM) units](/managed/license/classic-licensing/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), DDUs provide a seamless, shared consumption model across custom metrics, Log Monitoring, and custom events.

Because DDUs are consumption-based, you buy a certain volume and your available quota is consumed over time based on the amount of monitoring your environment consumes. This licensing approach makes it much easier for you to control and monitor your metric consumption (for example, in the case of misconfigured metrics) and to identify top consumers in your environment. To learn more about how metrics are licensed with DDUs, see [Metric cost calculation](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

For complete details about how your Dynatrace monitoring consumption is calculated, see [Calculate Dynatrace monitoring consumption](/managed/license/monitoring-consumption-classic "Understand how Dynatrace classic monitoring consumption is calculated, including host units, DDUs, DEM units, and Application Security units.").

## Davis data unit volumes

DDUs are purchased in volumes of 1 million units based on 1-3 year contract terms, with the full amount of licensed units renewing at the beginning of each year. For example, if you buy 100 million DDUs for a 3-year term, you can consume 100 million DDUs annually for 3 years.

You can purchase additional DDUs at any time if you run low. Reach out to your Dynatrace sales representative for details. To assist you in adjusting your monitoring consumption and avoiding cost overages, in-product notifications are displayed to alert your Dynatrace environment users when `90%` and `100%` of your licensed DDUs have been consumed.

### Davis data units - Free tier

Every new Dynatrace SaaS environment and each Dynatrace Managed license receives 200,000 DDUs free of charge. This translates into 381 metrics, captured at a 1-minute frequency. This free tier enables you to test out features and experience Dynatrace monitoring value before you pay. The free tier of 200,000 DDUs automatically renews annually at the beginning of each new license term for each account. This benefit is not available to Offline or consumption-based (pay-as-you-go) accounts.

## View DDU consumption details per environment

You need the **Manage monitoring settings** permission or an admin account to access this page. See [Account management permissions](/managed/manage/identity-access-management/permission-management/account-management-permissions "Dynatrace permissions required to access Account Management") for details.

To see how many DDUs your environment has consumed, go to [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**. There you can view your DDU consumption and identify the top contributors to DDU consumption.

This page offers an overview of DDU consumption per pool, as well as a detailed view per monitored entity (host, service, process group, application, or other). The second level navigation allows to further drill into detailed consumption per DDU pool (such as Metrics, Log Monitoring, Events).

### Get DDU consumption details via API

You can also [pull DDU consumption details via our API](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API."). The following metrics are available for retrieving DDU consumption details per pool via the API:

* `builtin:billing.ddu.metrics.total`
* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byMetric`
* `builtin:billing.ddu.log.total`
* `builtin:billing.ddu.log.byEntity`
* `builtin:billing.ddu.log.byDescription`
* `builtin:billing.ddu.serverless.total`
* `builtin:billing.ddu.serverless.byEntity`
* `builtin:billing.ddu.serverless.byDescription`
* `builtin:billing.ddu.events.total`
* `builtin:billing.ddu.events.byEntity`
* `builtin:billing.ddu.events.byDescription`
* `builtin:billing.ddu.traces.total`
* `builtin:billing.ddu.traces.byEntity`
* `builtin:billing.ddu.traces.byDescription`

### Get DDU consumption by management zone

The above mentioned metrics do not directly support filtering by management zone, however the API can be used to achieve this and thereby address cross-departmental charging requirements and create a consumption report of your monitored entities split by management zones.

See a sample management zone reporting script in the [Dynatrace snippets repository on GitHub﻿](https://github.com/Dynatrace/snippets/tree/master/api/ddu/management-zone-calculation)
The script accesses the `builtin:billing.ddu.metrics.byEntity` metric and allows you to query consumption of the Metrics DDU pool for all or one specific management zone in a defined timeframe.

## DDU pools

With DDU pools you can define monthly or yearly limits for DDU consumption on a per-environment basis. By default, pool limits are not enforced. To define limits for DDU consumption, go to **Settings** > **Consumption** > **Davis data unit pools**

![DDU pools](https://dt-cdn.net/images/davis-data-unit-pools-3356-11d216da22.png)

DDU pools

The following pools are available for limiting DDU consumption:

* Metrics
* Log Monitoring
* Serverless
* Events
* Traces

You need the **Manage monitoring settings** permission or an admin account to access the **Davis data unit pools** page.

Each pool can have a monthly or yearly defined limit for total DDU consumption. Similar to [DDU volume notifications](/managed/license/classic-licensing/davis-data-units#davis-data-unit-volumes "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."), all users of an environment will see banner notifications once 90% and 100% of the pool limit have been consumed.

Pool limits are evaluated per calendar month/year and are not associated with license renewal dates.

## FAQ

How will this impact my account and environments?

Dynatrace will automatically trigger the migration of your existing license quota for you. You'll receive a notification once the migration is complete and you can begin using the DDU approach.

Are DDU quotas tied to host unit consumption?

No, DDU consumption isn't tied to host unit consumption. DDUs are used to measure an environment's consumption of custom metrics, log lines, custom events, and third-party traces), not host monitoring.

Is there a free tier of DDUs available for each environment?

Yes, 200,000 DDUs are available for each environment (SaaS) or license (Managed/Offline). Same is true for our free trial customers. The free tier resets annually (this is not true for Offline customers).

Are there any differences between SaaS, Managed, and Offline deployments?

There is no difference between Dynatrace SaaS and Dynatrace Managed deployments. Offline deployments do not receive an annual reset of DDUs.

Where can I track/monitor my DDU consumption?

Go to [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

Which permission is required to see the DDU consumption overview?

You need the **Manage monitoring settings** permission or use an admin account to access the **DDU consumption overview** page. For more information on permissions, see [Manager user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Which permission is required to see the DDU consumption notifications?

You need the **Manage monitoring settings** permission or use an admin account to receive the DDU consumption notifications. For more information on permissions, see [Manager user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Can I get DDU consumption details via the API?

Yes, DDU consumption details can be pulled via the [Environment API v2](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

* `builtin:billing.ddu`
* `builtin:billing.ddu.metrics.byEntity`
* `builtin:billing.ddu.metrics.byMetric`

Is there any way to block/delay the DDU conversion?

No, because DDUs are designed for calculating your monitoring consumption of custom metrics, log lines, custom events, etc. You gain more precise consumption insights with immediate conversion to DDUs.

Are unused DDUs carried over to the next license term?

No. Your DDU quota is reset on each anniversary of the contract term, same as is done for DEM units.

Will we lose any functionality or flexibility?

No, you'll gain more flexibility, transparency, and other benefits with DDUs.

How many DDUs are in a licensing volume?

* One volume contains 1 million DDUs and translates to 1,903 metrics (at a 1-minute frequency)
* If a metric has multiple dimensions (for example, pool utilization per database pool name) then each dimension produces 1 metric data point per minute and subsequently deducts multiple DDUs per minute.

What is the minimum number of volumes I need to buy?

The minimum number of DDU volumes you can purchase is 1 (that is, 1 million DDUs). This equates to 1,903 metrics (at 1-minute frequency).

Can I enable overages for DDUs?

Yes, overages are available for DDUs.

How will the migration work if it takes place in the middle of a term?

All remaining custom metrics in your license will be converted to DDUs. Term duration is taken into consideration. For example, if you are six months into a one-year term (in other words, 50% of your term and custom metrics have been consumed), the remaining 50% of your custom metrics will be converted into an equivalent number of DDUs.

Can I split my DDUs across SaaS environments?

Eventually, yes. However this is currently not available.

Will I be notified once I've used up my quota of DDUs?

Yes, your Dynatrace environment users will see an in-product notification once you've used up `90%` and `100%` of your licensed DDUs.

Is there any support for the previous “non-host unit” license?

No, we can't support these older licenses. If you're still using one of these licenses, then the Dynatrace team should have already reached out to you. If they haven't, please contact us so that we can assist you with the conversion.

What is a “monitored entity”?

A monitored entity is anything in your environment that Dynatrace detects and monitors. This includes hosts, services, process groups, applications, and more.

What does “Not related to a monitored entity” mean?

The **Davis data units overview** sometimes displays the **Not related to a monitored entity** entry in the **Name** column of the **Monitored entities** table.

Depending on the pool, these are the potential sources of consumption booked on a **Not related to a monitored entity** entry:

| Pool | Entity-less sources |
| --- | --- |
| Metrics | See [Metrics section](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation#no-monitored-entity "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") |
| Log | [Generic log ingestion](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") |
| Serverless | None |
| Events | [Event API v2](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.") |
| Traces | Traces where `span:service` is missing in the generic entity config or span data doesn't have a `service.name` resource attribute. |

Can I split my consumption based on Azure subscription?

For consumption that is related to a monitored entity and where an `entitySelector` relation exists, use the [Metrics API](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") query:

```
builtin:billing.ddu.metrics.byEntity:filter(



and(in("dt.entity.monitored_entity",



entitySelector("type(AZURE_STORAGE_ACCOUNT), fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),



entityName.startsWith(~"myPrefix~"))"))



)



)



:splitBy():fold
```

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)