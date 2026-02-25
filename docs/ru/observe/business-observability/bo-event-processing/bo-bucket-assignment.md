---
title: Business event bucket assignment via classic pipeline
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing/bo-bucket-assignment
scraped: 2026-02-25T21:17:59.451230
---

# Business event bucket assignment via classic pipeline

# Business event bucket assignment via classic pipeline

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Nov 28, 2025

Business events can be stored in buckets that can have different retention periods. You create rules with matcher-specific [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries to assign matching business events to a bucket. The default retention period for a built-in business events bucket (`default_bizevents`) is 35 days. You can also create [custom buckets](/docs/platform/grail/organize-data/assign-permissions-in-grail#custom-grail-buckets "Find out how to assign permissions to buckets and tables in Grail.") with a specific retention period.

For custom buckets, the possible retention period ranges from 1 day to 10 years, with an additional week.

Business events can be stored in different buckets that determine the retention time and access permissions. You can create rules with matcher-specific DQL queries to assign matching business events to a bucket. By default, every incoming business event is stored in the default bucket with a 35-day retention period. Longer and shorter periods can also be set.

## Choose the retention period

1. Go to **Settings** > **Business Observability** > **Ingest Pipeline** > **Bucket assignment**.
2. In the **Business event bucket assignment**, select **Add rule** and name your rule.
3. Select the **Bucket**.
4. Add a **Matcher** to your rule by typing or pasting your [matcher-specific DQL query](/docs/analyze-explore-automate/logs/lma-classic-log-processing#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation."). Events that match your rule will be assigned to your selected bucket. If no rules match, events will be assigned to the default bucket.
5. Select **Save changes**.

## Matcher examples

* If you needed to add only one event type (for example, `com.easytrade.buy-assets`), the matcher would be:

```
matchesValue(event.type, "com.easytrade.buy-assets")
```

* For two event types within the same event provider, the matcher would be:

```
matchesValue(event.type, "com.easytrade.buy-assets") or matchesValue(event.type, "com.  easytrade.sell-assets")
```

* In this use case, however, you need to take all event types under the EasyTrade event provider, so it is sufficient just to use:

```
matchesValue(event.provider, "www.easytrade.com")
```