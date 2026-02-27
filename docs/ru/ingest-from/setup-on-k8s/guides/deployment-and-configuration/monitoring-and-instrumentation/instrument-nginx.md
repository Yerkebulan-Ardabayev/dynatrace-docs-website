---
title: Instrument ingress-nginx
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx
scraped: 2026-02-27T21:14:55.675904
---

# Instrument ingress-nginx

# Instrument ingress-nginx

* Latest Dynatrace
* 1-min read
* Published Sep 02, 2021

The instructions below are relevant only for the [official Kubernetes ingress controller implementation from Googleï»¿](https://dt-url.net/xr03xh3).

* Derivatives from the official project, such as the [Bitnami ingress controllerï»¿](https://dt-url.net/ns03xjt), are not supported. However, you may instrument them manually by using the [Manual runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") for NGINX.
* The [ingress controller implementation from F5 NGINXï»¿](https://dt-url.net/ph43xrd) can be instrumented automatically; no manual steps are required.

The NGINX process of the official Kubernetes ingress-nginx controller container image can't be instrumented automatically. To manually instrument ingress-nginx on Kubernetes, follow the instructions below.

## Prerequisites

ARM64 architecture is not supported.

* OneAgent version 1.227+
* The pod name must contain the substring `ingress-nginx-` to ensure proper instrumentation of the NGINX binary. We recommend to maintain the default pod name `ingress-nginx-controller`.

## Instrument Kubernetes ingress-nginx

To instrument ingress-nginx on Kubernetes, you need to load the NGINX module manually via a ConfigMap.

Ensure that OneAgent is running and capable of instrumenting the ingress-nginx containers when applying changes to the ingress-nginx ConfigMap. If these conditions are not met, NGINX will fail to start.

1. Edit the ConfigMap.

   ```
   kubectl edit configmap ingress-nginx-controller
   ```
2. Add the following value to the `main-snippet` key (below `data`).

   Example:

   ```
   data:



   main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

   For `cloudNativeFullStack` and `applicationMonitoring` deployments, the path becomes:

   ```
   data:



   main-snippet: load_module /opt/dynatrace/oneagent-paas/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

## Verify your configuration

If your pod isn't up and running, make sure that it hasn't exceeded either of the following:

* Its resource quota (especially for memory).
* The initial liveness/readiness probe timeouts. You might need to increase `initialDelaySeconds` for these probes.