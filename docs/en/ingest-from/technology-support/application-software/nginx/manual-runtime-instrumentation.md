---
title: Runtime instrumentation
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation
scraped: 2026-02-16T09:20:28.971206
---

# Runtime instrumentation

# Runtime instrumentation

* Latest Dynatrace
* 2-min read
* Updated on Oct 26, 2022

The NGINX code module relies on ahead-of-time assumptions about the internal NGINX data structure declarations and their layout in the memory during its automatic instrumentation. If the underlying data structure declarations are patched (meaning the source code defining these structures has been modified) and hence the ahead-of-time assumptions are invalid, the automatic instrumentation done by the code module may cause problems on NGINX due to reading from, or writing to, wrong parts of the memory.

To avoid such a scenario, the NGINX code module tries to detect patched NGINX data structure declarations. If a patched declaration is detected, the code module disables its automatic instrumentation and shows the following note on the process page in the web UI:

Notification

* Incompatible NGINX modules were detected in this process. Automatic instrumentation was disabled. To force instrumenting NGINX, see [Runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.").

## Instrument a patched NGINX

NGNIX Code Module can instrument a patched NGINX for [supported versions](/docs/ingest-from/technology-support/application-software/nginx#nginx-versions "Learn the details of Dynatrace support for NGINX.") by inspecting internal NGINX data structure declarations on startup (during runtime), instead of relying on ahead-of-time assumptions.

An example of a patched NGINX is the NGINX binary distributed with the Kong Gateway.

As patches can significantly alter the internal workings of NGINX, there is no guarantee that NGINX instrumented with runtime instrumentation will work as expected. Consider the following limitations.

Runtime instrumentation limitations

* The runtime instrumentation depends on debug symbols being available for the NGINX binary, which is not always the case.
* The runtime instrumentation adds a notable startup delay (10 seconds or more) to NGINX.
* The runtime instrumentation on Linux ARM64 requires OneAgent version 1.313+.

  My NGINX or Kong Pod in Kubernetes is not starting up due to a timeout

  In cloud deployments, adjust your Pod or container startup timeouts to prevent NGINX from running into a timeout when starting up.

  If an NGINX or Kong pod in Kubernetes is not starting up, look for a mention of failing liveness or readiness probes in the logs, and adjust the initial delay, timeout, and failure threshold values of these probes to high enough values. The exact configuration depends on the deployment.
* The runtime instrumentation requires more memory during the startup of NGINX. This higher peak memory consumption can lead to Pods being killed by Kubernetes (or other container runtimes) in case of strict memory limits. Please adjust your memory limits to accommodate runtime instrumentation.

To force instrumenting a patched NGINX during runtime

1. Add the environment variable `DT_NGINX_FORCE_RUNTIME_INSTRUMENTATION` to your NGINX:

```
DT_NGINX_FORCE_RUNTIME_INSTRUMENTATION=on
```

2. Restart your NGINX to pick up the environment variable.