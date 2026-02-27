---
title: Filter with facets
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/facets
scraped: 2026-02-27T21:11:29.404795
---

# Filter with facets

# Filter with facets

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jun 15, 2025

Facets are quick filters for log data.
They correspond to log attribute key-value pairs detected in your environment and are grouped by facet categories.
The most important DQL field IDs are grouped by default in predefined categories.
Facets also help you estimate the amount of log data corresponding to each attribute.

## Filter data with facets

To query logs in your environment with facets

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Expand facet groups like âCoreâ or âLog sourceâ.
3. Expand the facet relevant for your query, like âStatusâ.
4. Select values relevant for your query, like âErrorâ and âWarningâ.
5. Observe how the filters are generated in the Filter Field.
6. Select as many facets as needed for your query.

   Within a single facet, selected values are combined using the `OR` operator. This means logs matching any of the selected values for that facet will be included.
   Between different facets, values are combined using the `AND` operator. This means logs must match at least one value from each selected facet to be included.
7. Press **Run query** to see logs from your environment based on your filter.

## Estimate amount of data with facets

To get a sense of how many logs with specific attributes there are in your environment

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Expand facet groups and facets relevant for your query.
3. Look at the approximate values for each value.

The numbers displayed for each facet value represent the approximate number of logs based on your last query filters. If you see the '~' symbol, it indicates that Dynatrace is using sampling when reading log data to improve responsiveness.

Example:

* You query error logs from Kubernetes namespace âastroshopâ with following filters: `k8s.namespace.name = "astroshop"` `status = "Error"`
* After executing query, look at the facet `k8s.container.name`
* You will only see container names for logs coming from Kubernetes namespace âastroshopâ with the status âErrorâ
* Number displayed next to each container name shows the approximate number of logs with Kubernetes namespace âastroshopâ, status âErrorâ and respective container name

## Manage all facets

To manage which facets of your environment are displayed

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Select  **Facets edit icon** next to the facets search bar.
3. Select or deselect items from the predefined categories.

   * Check the category box to select or deselect all facets in the category.
   * Select  to view the facets in a category and select or deselect them.
4. Select **Save**.

## Revert to default settings

If you have previously modified the facets, to revert to the default settings for facets in your environment

1. Go to ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.
2. Select  **Facets edit icon** next to the facets search bar.
3. Select **Reset to default**.
4. Select **Save**.