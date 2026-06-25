---
title: Fix probe timeouts due to OneAgent injection
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/probe-timeout
scraped: 2026-05-12T12:09:24.365725
---

# Fix probe timeouts due to OneAgent injection

# Fix probe timeouts due to OneAgent injection

* 1-min read
* Published May 28, 2024

This guide walks you through the process of fixing timeouts in readiness- or liveness-probes due to OneAgent injecting into the probe.

## Scenario

In some scenarios, a readiness- or liveness-probe is configured using an exec statement. This configuration causes OneAgent to attempt injection when the probe executable starts. This injection process introduces a slight delay in startup time, which can result in the probe timing out.

Consider the following example of a readiness probe:

```
readinessProbe:



exec:



command:



- /bin/sh



- -ec



- vault status -tls-skip-verify
```

In this example, Vault is the application we want to monitor, but we want to exclude the process used as the readiness-probe from being monitored.

## Resolution

To resolve this issue, you can configure an exception in the settings.

1. Go to **Settings** > **Processes and containers** > **Custom process monitoring rules**.
2. Select **Add custom rule**.
3. Add an exclusion to monitoring by supplying a part of the command line arguments used by the readiness probe. To resolve the timeout in our example, use the following settings:

   * **Mode**: `Do not monitor`
   * **Condition target**: `Command line args`
   * **Condition operator**: `contains`
   * **Condition value**: `vault status`
4. Save your changes (this might take up to 5 minutes).

Once the settings are applied to the cluster, the timeouts should be resolved.