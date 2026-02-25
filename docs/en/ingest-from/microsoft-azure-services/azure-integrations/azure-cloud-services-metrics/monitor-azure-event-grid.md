---
title: Azure Event Grid (Domain Topics, Topics, System Topics) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid
scraped: 2026-02-25T21:27:07.177259
---

# Azure Event Grid (Domain Topics, Topics, System Topics) monitoring

# Azure Event Grid (Domain Topics, Topics, System Topics) monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Event Grid (Domain Topics, Topics, System Topics). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Eventgrid dash](https://dt-cdn.net/images/domain-dashboard-2831-82aa7e47f2.png)

![Topics](https://dt-cdn.net/images/topic-dashboard-1850-f3c283d392.png)

![System](https://dt-cdn.net/images/system-dashboard-1805-f6d8b147c2.png)

## Available metrics

### Azure Event Grid Domain Topics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, DeadLetterReason | Count |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, Error, ErrorType | Count | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | Topic, EventSubscriptionName, DomainEventSubscriptionName | MilliSecond | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, DropReason | Count | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Topic, ErrorType, Error | Count | Applicable |
| PublishSuccessCount | Total events published to this topic | Topic | Count | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds |  | MilliSecond | Applicable |

### Azure Event Grid Topics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Total events published to this topic | Count |  | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds | MilliSecond |  | Applicable |
| UnmatchedEventCount | Total events not matching any of the event subscriptions for this topic | Count |  | Applicable |

### Azure Event Grid System Topics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Total events published to this topic | Count |  | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds | MilliSecond |  | Applicable |
| UnmatchedEventCount | Total events not matching any of the event subscriptions for this topic | Count |  | Applicable |