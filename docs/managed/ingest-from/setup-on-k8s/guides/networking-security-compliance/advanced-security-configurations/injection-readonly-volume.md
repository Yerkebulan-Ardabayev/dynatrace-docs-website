---
title: Configure read-only CSI volumes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume
scraped: 2026-05-12T12:04:35.978215
---

# Configure read-only CSI volumes

# Configure read-only CSI volumes

* 1-min read
* Updated on Nov 20, 2025
* Deprecated

Dynatrace Operator version 0.12.0+ and <1.7.0

This is only relevant for Operator version after 0.12.0 and before 1.7.0.

After Operator version 1.7.0, all the CSI volumes injected by the Operator are readonly.

### Prerequisites Deprecated

* The Dynatrace Operator CSI driver installed on the Kubernetes cluster.
* DynaKube configured to use the CSI driver. For example, ensure that `applicationMonitoring` is enabled with `useCSIDriver: true`.

  `cloudNativeFullStack` is not supported on [BottleRocketï»¿](https://dt-url.net/4c0365f).

### Enable feature flag Deprecated

When using this feature flag, our CSI driver's resilience feature will not work. Use Operator version 1.7+ in case resilient read-only CSI volumes are required.

* CSI driver's resilience feature: In case our CSI driver can't successfully provide a mount to an injected container for several minutes, it will back off, so the user application can start but without monitoring.

To enable the injection of read-only CSI volumes, set the `feature.dynatrace.com/injection-readonly-volume` feature flag to `true`. When the feature flag is enabled, the injected CSI volume becomes read-only.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/injection-readonly-volume: "true"
```

This enables usage of the CSI driver even on [BottleRocketï»¿](https://dt-url.net/4c0365f) platforms where host monitoring OneAgents don't work. To accommodate this feature, extra ephemeral storage is added to allow the injected OneAgent to store logs and additional configurations.

A drawback to this approach is that if your pods terminate unexpectedly or are otherwise deleted, any logs stored in ephemeral storage will be lost.