---
title: View surrounding logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs
scraped: 2026-02-06T16:00:10.985968
---

# View surrounding logs

# View surrounding logs

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 02, 2025

View the surrounding logs for every log record to better understand the context for the data.

![Surrounding logs of a log error based on trace ID correlation](https://dt-cdn.net/images/surroundinglogs-1907-40995092b7.png)

To view surrounding logs

1. In ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, find a relevant log line in the result table and open its details.
2. Select **Show surrounding logs**.

The surrounding logs are shown for the context provided by the log record.

* If `trace_id` parameter is present, you should see other records with the same trace ID.

  For more information about automated correlation, see [Connect log data to traces](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.").
* Alternatively, you can examine the surrounding logs for the same topology entity, for example, a host.

  Select **Run query for 15 logs before** or **Run query for 15 logs after** to expand the context by loading more data before or after the timestamp of the original.