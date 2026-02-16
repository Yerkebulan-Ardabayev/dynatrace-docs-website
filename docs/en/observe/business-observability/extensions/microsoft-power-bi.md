---
title: Microsoft Power BI
source: https://www.dynatrace.com/docs/observe/business-observability/extensions/microsoft-power-bi
scraped: 2026-02-16T09:25:31.806545
---

# Microsoft Power BI

# Microsoft Power BI

* Latest Dynatrace
* Overview
* 2-min read
* Published Mar 17, 2025
* Preview

Preview

The Microsoft Power BI extension brings data from Grail directly into your Microsoft Power BI reports and dashboards by providing DQL queries.

The cost of executing DQL queries within Microsoft Power BI is equivalent to [the Dynatrace UI](/docs/license/subscription-and-license/subscription-and-license-dps "View license and subscription usage and consumption history Dynatrace Platform subscription licenses that were signed prior to April, 2023.").

## Limitations

* Import mode only
* Maximum result for DQL queries: 1,000,000 rows
* Maximum result for default tables (BizEvents, Events, Logs, Spans): 1,000 rows

## Setup

You need to have [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") to execute queries and to view
certain tables in Grail.

Example for a policy statement to read Business Events:

```
ALLOW storage:buckets:read WHERE storage:table-name = "bizevents";



ALLOW storage:bizevents:read;
```

### Connect to Dynatrace Grail from Microsoft Power BI Desktop

To connect to a Dynatrace SaaS instance from Power Query Desktop, take the following steps.

1. Select **Dynatrace Grail DQL** in the **Get Data** experience. For more information, see [Where to get data | Power Queryï»¿](https://dt-url.net/x203wmh).
2. Enter your Dynatrace environment. This environment needs to be the latest Dynatrace version with Grail enabled. The DQL query is optional at this point, but should be used for more complex queries outside of the default built-in queries.
3. Sign into your environment to authenticate your permissions.
4. Enter your credentials into the pop-up window.
5. Once you authenticate, you'll see the message that you're signed in. Select **Connect**.
6. The **Navigator** page shows the record types available to select from Dynatrace Grail.
7. Select one of them, **Logs** for example, and run a fetch logs DQL query with a default 1,000 row limit. You require permissions on the Dynatrace environment in order to run this query successfully.
8. The **Advanced Editor** shows the M code the connector is using.
9. You can go back now to the optional DQL query from step 2 and type in a DQL query.
10. Import the results into Microsoft Power BI.

## Related topics

* [Microsoft Power BI extensionï»¿](https://dt-url.net/go03wp3)