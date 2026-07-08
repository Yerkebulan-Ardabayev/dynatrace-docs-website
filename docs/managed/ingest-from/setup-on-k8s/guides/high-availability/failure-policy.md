---
title: Configure failure policy
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/failure-policy
---

# Configure failure policy

# Configure failure policy

* 1-min read
* Published Jul 28, 2023

Dynatrace Operator version 0.11.0+

Ensure that the OneAgent CSI driver pods are up and running.

The failure policy determines what should happen when OneAgent injection fails for a particular pod in a Kubernetes cluster. By default, the failure policy is set to `silent`. You can override the failure policy for all injected pods that match the DynaKube by setting the `feature.dynatrace.com/injection-failure-policy` to one of the following values.

* `silent`—if OneAgent injection fails for a particular pod, the pod will continue to run without monitoring.
* `fail`—if OneAgent injection fails for a particular pod, the pod will not start, and the injection failure will be treated as an error.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/injection-failure-policy: [fail|silent]
```