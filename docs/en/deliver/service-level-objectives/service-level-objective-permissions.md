---
title: Permissions for service-level objective (SLO) tiles in a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-permissions
scraped: 2026-02-21T21:26:58.982170
---

# Permissions for service-level objective (SLO) tiles in a dashboard

# Permissions for service-level objective (SLO) tiles in a dashboard

* Latest Dynatrace
* 1-min read
* Published Nov 24, 2024

You need the following permissions for service-level objective (SLO) tiles in a dashboard

For **Edit**

* `slo:slos:read` ârequired for reading all SLOs to show them in the dropdown selector
* `slo:slos:write` ârequired for showing the  **Service-level objective** button
* `slo:slos:write`, `slo:slos:read`, and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

For SLO tile evaluation

* `slo:slos:read` and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

For the SLO details view

* `slo:slos:read`, `slo:objective-templates:read`, and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").