---
title: Configure high availability for Dynatrace Operator webhook
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/high-availability
scraped: 2026-05-12T12:09:29.945714
---

# Configure high availability for Dynatrace Operator webhook

# Configure high availability for Dynatrace Operator webhook

* 1-min read
* Updated on Feb 27, 2026

## Configure high availability

Dynatrace Operator version 1.9.0+

You can customize the `replicas`, `topologySpreadConstraints`, and `podDisruptionBudget` values independently:

The examples below use Helm values. If you deploy using manifests, you can achieve the same by adjusting the corresponding sections in your deployment manifest directly.

```
webhook:



# highAvailability: true # Deprecated, use the following values instead



replicas: 2



topologySpreadConstraints:



- maxSkew: 1



topologyKey: "topology.kubernetes.io/zone"



whenUnsatisfiable: ScheduleAnyway



labelSelector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook



- maxSkew: 1



topologyKey: "kubernetes.io/hostname"



whenUnsatisfiable: ScheduleAnyway



nodeTaintsPolicy: Honor



labelSelector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook



podDisruptionBudget:



minAvailable: 1



selector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook
```

You must keep `highAvailability` set to `true` (the default value) for the `replicas`, `topologySpreadConstraints`, and `podDisruptionBudget` values to take effect. If you set `highAvailability` to `false`, these fields are ignored. This ensures backward compatibility for users who previously disabled the high availability mode.

### Changes to topology spread constraints

The default `topologySpreadConstraints` is now `whenUnsatisfiable: ScheduleAnyway` instead of the previous `whenUnsatisfiable: DoNotSchedule`. This change makes scheduling less aggressive, so the webhook pods can still be scheduled in environments where only a few nodes (one or two) are available. Previously, `DoNotSchedule` could prevent pods from being scheduled if the topology constraints couldn't be fully satisfied.

## Legacy `highAvailability` Helm value (**deprecated**)

Dynatrace Operator version 0.6.0+

Starting with Operator version 1.9.0, the `highAvailability` value is deprecated in favor of the `replicas`, `topologySpreadConstraints`, and `podDisruptionBudget` values. See [Configure high availability](#configure-high-availability) for the recommended approach.

The legacy `highAvailability` Helm value offered the following capabilities:

* Increases replicas to two replicas for webhook deployment.
* Adds [pod topology spread constraintsï»¿](https://dt-url.net/xc03ysw):

  + Pods are spread across different nodes, with the nodes in different zones where possible.
  + Multiple pods are allowed in the same zone.
* Adds [pod disruption budgetï»¿](https://dt-url.net/m303yfk):

  + It restricts graceful shutdowns of the webhook pod if it's the last remaining pod.