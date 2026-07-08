---
title: Additional OpenShift configurations
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration
---

# Additional OpenShift configurations

# Additional OpenShift configurations

* 3-min read
* Updated on Feb 27, 2026

Integrating Dynatrace Operator into OpenShift environments requires understanding the specifics of both platforms. This guide depicts the necessary configurations, focusing on [Security Context Constraints (SCCs)﻿](https://dt-url.net/sl0340s) and the use of Dynatrace Operator CSI driver in various scenarios.

## Security Context Constraints (SCCs)

In OpenShift, SCCs provide control over pod permissions in a manner akin to the built-in Role-Based Access Control (RBAC) system of Kubernetes. SCCs specify the actions a pod can perform and define its levels of resource access.

To get an overview of all default and custom SCCs in an OpenShift cluster, execute the following command:

```
oc get scc
```

OpenShift provides [default SCCs﻿](https://dt-url.net/e5027ls) for a more standardized approach, while also supporting custom SCCs to cover more specific requirements.

### Dynatrace Operator

This section provides an overview of the SCCs used by Dynatrace Operator and serves as a reference.

| Component | SCC used |
| --- | --- |
| Operator | `nonroot-v2` |
| Webhook | `nonroot-v2` |
| CSI driver | `privileged` |
| OneAgent | `privileged` |
| ActiveGate | `nonroot-v2` |

### Code module injection for application monitoring

cloudNativeFullStack applicationMonitoring

For application monitoring, Dynatrace Operator's webhook adds volumes of different types to the monitored pods:

* `secret` volume for providing credentials and configuration data to the OneAgent.
* `projected` volume for aggregating multiple sources of data, such as secrets, into a single volume for easier access by the OneAgent.
* `emptyDir` volume for storing ephemeral data produced due to the injection.
* `csi` volume for injecting the OneAgent code module into the monitored pods.

  + This volume type is only used if the CSI driver is installed and used for code module injection.

The default `restricted-v2` SCC allows such volumes, and our injected init-container meets this SCC's security requirements if the injected container also adheres to the same constraints.

If you want to use a custom SCC for your application pods, ensure it allows `secret`, `projected`, `emptyDir`, and `csi` volumes.

## CSI Inline Ephemeral Volume Security

OpenShift version 4.13+

The CSI driver requires specific labeling for validation by the [CSI Volume Admission plugin﻿](https://dt-url.net/2l038e8).

[The necessary label is automatically added to the `csidriver` resource﻿](https://dt-url.net/ry238f0). It is required for enabling CSI volumes injected by Dynatrace Operator using Webhook-based injection modes.