---
title: Enable Go monitoring
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring
---

# Enable Go monitoring

# Enable Go monitoring

* 2-min read
* Updated on Oct 23, 2025

Dynatrace OneAgent for Go can monitor your Golang applications as well as any third-party Go-based applications that your own applications may rely on. This monitoring technology allows you to capture data that is well beyond the capabilities of traditional monitoring solutions. Dynatrace extracts internal Go runtime information that is inaccessible with public Go runtime APIs.

Go monitoring is enabled by default for all new environments. However, only applications that are listed as allowed in the pre-deployed process monitoring rules will be monitored. To enable monitoring of additional processes, you'll need to define your own monitoring rules.

## Enable Go monitoring

To activate Go monitoring

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Find **Go** in the list of supported technologies, and select **Edit** (pencil icon).
3. Turn on **Monitor Go on every host**.

   ![Enable Go monitoring](https://dt-cdn.net/images/enable-go-monitoring-1839-e2e67e5563.png)

   Enable Go monitoring
4. [Create a process monitoring rule](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring") to enable deep monitoring of the selected processes.

## Enable Go static monitoring

Support for the monitoring of statically linked Go applications is available starting with Dynatrace OneAgent version 1.203.

Unless there are dependencies on packages using [cgo﻿](https://blog.golang.org/cgo), the Go toolchain produces statically linked Go executables by default. These applications don't allow loading of additional code dynamically, so it is impossible for most monitoring agents to auto-inject themselves into such applications.

With Dynatrace, you do not need to force your application to be dynamically linked or change the source code if you want to monitor statically linked Go applications. There are [several limitations for this solution](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Learn the limitations for Go support and their workarounds."), though.

To activate Go static application monitoring

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Find **Go** in the list of supported technologies, and select **Edit** (pencil icon).
3. Ensure that **Monitor Go on every host** is turned on.
4. Turn on **Enable Go static application monitoring on every host**.

   ![Enable Go static monitoring](https://dt-cdn.net/images/enable-go-static-monitoring-1838-33cac1f1b9.png)

   Enable Go static monitoring
5. [Create a process monitoring rule](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring") to enable deep monitoring of each statically linked Go executable.

## Built-in process monitoring rules

OneAgent has a set of built-in process monitoring rules that define which processes OneAgent monitors. To check the current process monitoring rules, go to **Settings** > **Processes and containers** > **Built-in process monitoring rules**.

By default, OneAgent monitors a predefined list of Go applications (for example, Gorouter and InfluxDB) and dynamically linked Go applications started in a container.
To monitor an arbitrary Go application, [define a custom process monitoring rule](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").