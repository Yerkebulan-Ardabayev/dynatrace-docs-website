---
title: Configure startup probes for Dynatrace Operator components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/configure-startup-probes
---

# Configure startup probes for Dynatrace Operator components

# Configure startup probes for Dynatrace Operator components

* How-to guide
* 1-min read
* Updated on May 27, 2026

The startup probes of the Dynatrace Operator components perform a DNS lookup for `kubernetes.default.svc` to verify that cluster DNS is ready. This ensures the Operator only starts when DNS is available, preventing startup failures caused by unresolved Kubernetes API server addresses.

## Startup probe settings

The default startup probe configuration is suitable for most environments, but you can customize the startup probes for Dynatrace Operator components to better suit your environment. Tuning these probes ensures components are ready before handling requests.

You can customize startup probes in the Helm `values.yaml` for the Dynatrace Operator, Webhook, or CSI driver.

* **Dynatrace Operator**

  ```
  operator:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```
* **Webhook**

  ```
  webhook:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```
* **CSI driver**

  ```
  csidriver:



  provisioner:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```