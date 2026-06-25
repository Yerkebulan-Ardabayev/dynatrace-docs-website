---
title: Maintenance windows API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api
scraped: 2026-05-12T11:36:43.198871
---

# Maintenance windows API

# Maintenance windows API

* Reference
* Updated on Apr 28, 2020

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema instead.

Dynatrace uses [maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.") to ensure accurate monitoring data during planned maintenance of your systems.

The **Maintenance windows** configuration API enables you to use 3rd party tools to manage maintenance windows and downtimes within a monitored environment.

### List all maintenance windows

[Get an overview](/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-all "View all maintenance windows of your environment via the Dynatrace API.") of all maintenance windows available in your Dynatrace environment.

### View a maintenance window

[Get parameters of a maintenance window](/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-mw "View a maintenance window via the Dynatrace API.") by its ID.

### Create a maintenance window

[Create a new maintenance window](/managed/dynatrace-api/configuration-api/maintenance-windows-api/post-mw "Create a maintenance window via the Dynatrace API.") with the exact parameters you need.

### Edit a maintenance window

[Update the existing configuration](/managed/dynatrace-api/configuration-api/maintenance-windows-api/put-mw "Edit a maintenance window via the Dynatrace API.") of a maintenance window.

### Delete a maintenance window

[Delete maintenance windows](/managed/dynatrace-api/configuration-api/maintenance-windows-api/delete-mw "Delete a maintenance window via the Dynatrace API.") you no longer need.

## Related topics

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.")