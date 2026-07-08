---
title: Trigger manual cluster update
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/updates-v1/post-trigger-manual-cluster-update
---

# Trigger manual cluster update

# Trigger manual cluster update

* Published Jun 03, 2026

This API call triggers a manual cluster update.

## Authentication

To execute this request, you need one of the following API-Token scopes:

* `ControlManagement`
* `ServiceProviderAPI`
* `Nodekeeper`

## Endpoint

`/api/v1.0/upgradeManagement/triggerUpgrade`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Started successfully. |
| **412** | Triggering of update failed due to missing new version on all nodes. |
| **510** | Could not trigger update. Check logs for details... |
| **553** | Update suspended by Dynatrace Mission Control. Could not update cluster now. |
| **554** | Update is already running. |