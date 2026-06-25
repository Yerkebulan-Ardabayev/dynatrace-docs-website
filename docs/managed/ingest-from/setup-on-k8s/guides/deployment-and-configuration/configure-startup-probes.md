---
title: Configure startup probes for Dynatrace Operator components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/configure-startup-probes
scraped: 2026-05-12T12:09:18.163544
---

# Configure startup probes for Dynatrace Operator components

# Configure startup probes for Dynatrace Operator components

* How-to guide
* 1-min read
* Published Mar 12, 2026

## Customize startup probes for Dynatrace Operator components

The default startup probe configuration is suitable for most environments, but you can customize the startup probes for Dynatrace Operator components to better align with your specific environment and operational requirements. Properly tuning these probes helps ensure that components are fully initialized and ready to operate before they begin handling requests.

Startup probe customization can easily be done via the Helm `values.yaml` for the Dynatrace Operator, Webhook, or CSI driver.

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