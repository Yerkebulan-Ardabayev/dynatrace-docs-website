---
title: Limits in Logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/limits
scraped: 2026-02-26T21:14:19.256670
---

# Limits in Logs

# Limits in Logs

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2026

This page describes the limits that apply when querying and viewing logs in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, as well as how to change the default limits.

## Query result rows (**Record limit**)

By default, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** displays a maximum of 1000 rows as a result of your query.

You can adjust the **Record limit** setting up to 50,000 rows to view more results in a single query.

## Scanned data per query (**Read data limit**)

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** reads a maximum of 500 GB of data per query. The query stops after reaching this limit.

You can adjust the **Read data limit** setting to your desired value to scan more data, but you cannot set it to unlimited.

## Result data size (**Result size limit**)

The result size of data returned by a query is limited to 100 MB by default.

You can reduce the **Result size limit** setting and choose a value between 1 and 100 MB based on your needs.

## Adjust limits

To adjust the limits for your queries in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. In the upper-right corner, next to **Run query**, select  (**Actions menu**) >  **App settings**.
3. In the **App settings** pane, adjust the desired limits.