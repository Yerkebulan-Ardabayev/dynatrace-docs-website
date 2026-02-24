---
title: Merged services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services
scraped: 2026-02-24T21:30:45.077180
---

# Merged services

# Merged services

* How-to guide
* 3-min read
* Updated on Oct 04, 2022

**Settings** > **Merged service monitoring** is deprecated.

* If merged services exist in your environment, you can still access the page to view and edit them.
* You can't create new merged services from this setting page. To create or edit the equivalent of a merged service via rule-based detection, see [Create a rule to aggregate services](#create-merged-service) below.

A merged service is a service that aggregates multiple [web-request services](/docs/observe/application-observability/services/service-detection/service-detection-v1#web-request-service "Find out how Dynatrace Service Detection v1 detects and names different types of services.") of the same process group that perform identical functions across separate cluster nodes. These web-request services are effectively identical from a performance-monitoring perspective. A merged service appears in Dynatrace as a single service that contains all the data of all aggregated services.

Say you have an Apache web server with several virtual host definitions (for example, `dynatrace.com`, `dynatrace.at`, and `dynatrace.pl`). From the Apache perspective, these are independent virtual hosts. Dynatrace therefore detects them as separate services. For your monitoring purposes however, you might want to view these services as a single merged service called `Dynatrace web page`.

Dynatrace automatically identifies mergeable services for you and displays them on the **Merged service monitoring** page (**Settings** > **Server-side service monitoring** > **Merged service monitoring**). Only services included in this list can be merged.

## Characteristics of existing merged services

* Once merged, the data of individual merged services can no longer be distinguishedâmonitoring data is available only in aggregate form for all the merged services.
* The original services of a merged service are no longer updated as data sources. While historical data remains available (for example, for charting), no new data is tracked for the original services. The aggregated data is assigned to and associated with the merged service.
* Merged services are of the same type. For example, they belong to the same process group, share the same underlying technology, or follow the same naming pattern. Multiple virtual hosts, context roots, or listen ports that represent the same logical entity can be part of a service merging.
* Only near-identical, standalone web-request services of the same process group are mergedâmerged services are not merged into other merged services.

## Split merged services

When you split a service from a merged service ("unmerge" the service), the historic data will be available only for the merged service. All newly captured data will be associated with the new standalone service.

To split a service from a merged service

1. Go to **Settings** > **Server-side service monitoring** > **Merged service monitoring**.
2. Select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in the row of the merged service you want to split.
3. Select **Remove** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the row of the service you want to remove.
4. Select **Update**.

## Delete merged service

If you delete a merged service, all individual merged services will be split and once again treated as standalone services.

To delete a merged service:

1. Go to **Settings** > **Server-side service monitoring** > **Merged service monitoring**.
2. Select **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the row of the merged service you want to delete.

## Create a rule to aggregate services

To carry out the equivalent task of creating a merged service, but via rule-based service detection

1. Go to **Settings** > **Service Detection**.

   * Select **Full web request rules** if the web requests are fully monitored by Dynatrace.
   * Select **External web request rules** for web requests going to external resources.
2. Select **Add item** and add a name for your new rule.
3. Turn on at least one service identifier contributor from the following: **Application identifier**, **URL context root**, and **Server name**.
4. Optional You can modify your rule by:

   * Setting a management zone
   * Adding specific conditions
   * Disabling the port
5. Select **Save changes**.

To learn more about how to create, edit, or delete service detection rules, see [Manage rule-based service detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection#manage "Use detection rules to customize and enhance the automated detection of your services.").

## Related topics

* [Service detection rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.")