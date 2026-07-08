---
title: Use journald to ingest systemd journal logs with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/journald
---

# Use journald to ingest systemd journal logs with the OTel Collector

# Use journald to ingest systemd journal logs with the OTel Collector

* How-to guide
* 4-min read
* Published Mar 12, 2026

The journald receiver reads log entries from the [systemd journal﻿](https://wiki.archlinux.org/title/Systemd/Journal) by invoking `journalctl` as a subprocess and streaming its output into the OTel Collector pipeline.

Each journal entry becomes an OTLP log record where journal fields are mapped to log attributes.
You can use [operators](#operators) to rename or transform these attributes to align with OpenTelemetry semantic conventions.

Use the journald receiver when:

* Your Linux-based services write logs to the systemd journal rather than to separate log files.
* You want to centralize host-level system service logs (for example, `ssh`, `kubelet`, or `docker`) in Dynatrace without managing additional log file paths.
* You need to filter ingestion by specific systemd units and priority levels to control data volume.

## Prerequisites

* One of the following Collector distributions with the [journald receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/journaldreceiver).

  + [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#collector-distro "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.

* Linux OS on the host or container where the Collector runs.
* The `journalctl` binary needs to be present on the host or in the container where the Collector runs.
  This is because the receiver relies on `journalctl` for all journal access.

  + For container deployments, use an image that includes `systemd` and mount the journal directory from the host.
  + For Kubernetes-specific requirements, see [Kubernetes deployment](#kubernetes-deployment).
* The Collector process needs permission to read the systemd journal via `journalctl`.

  + On a Linux OS host, add the user running the Collector to the `systemd-journal` group to grant read access to the journal.
    The Collector doesn't need to run as root.
  + For Kubernetes, the Collector must run as root because container isolation prevents group-based journal access.
    For more information, see [Kubernetes deployment](#kubernetes-deployment).

## Demo configuration

The following configuration example shows how to:

* Configure a Collector instance to read logs from specific systemd units.
* Map journald fields to OpenTelemetry semantic conventions.
* Send the entries to Dynatrace.

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



receivers:



journald:



directory: /var/log/journal



priority: info



start_at: end



operators:



# Move (rename) _PID to pid



- type: move



from: body._PID



to: body.pid



# Promote _EXE to a semantic convention attribute



- type: move



from: body._EXE



to: attributes["process.executable.name"]



# Rename MESSAGE to a consistently named body field



- type: move



from: body.MESSAGE



to: body.message



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions: [health_check]



pipelines:



logs:



receivers: [journald]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we configure the `journald` receiver with the following parameters.

#### Filtering by systemd unit

The `units` parameter restricts ingestion to entries belonging to the listed systemd units.
Remove it to collect logs from all units on the host.

For more granular filtering use the `matches` parameter instead.
For example, you can combine unit names with specific journal field values.

See the [journald receiver documentation﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/journaldreceiver#configuration) for a full parameter reference, filtering examples, and performance considerations for `start_at` and `priority`.

#### Operators

The `operators` parameter accepts an array of [stanza operators﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/pkg/stanza/docs/operators/README.md) applied to each log entry as it enters the pipeline.

In this configuration, we use [`move` operators﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/pkg/stanza/docs/operators/move.md) to rename specific journal fields and promote `_EXE` to a log attribute aligned with the [OpenTelemetry process semantic conventions﻿](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/).

* `body._PID` is renamed to `body.pid`.
* `body._EXE` is renamed to `attributes["process.executable.name"]`.
* `body.MESSAGE` is renamed to `body.message`.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporter﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.155.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).
* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

### Service pipelines

Under `service`, we assemble the receiver and exporter into a logs pipeline.
The pipeline reads journal entries, applies the operator-based field transformations, and ingests the results into Dynatrace.

## Considerations for Kubernetes deployments

When running the journald receiver in Kubernetes, deploy the Collector as a DaemonSet so that one Collector pod runs on every node.

A Deployment is unsuitable because each pod can only access the systemd journal of the node it is scheduled on.
Scaling a Deployment to multiple replicas can cause duplicate log ingestion when more than one replica lands on the same node.
A DaemonSet ensures complete cluster-wide log coverage and guarantees exactly one privileged, host-access pod per node.
This limits the security footprint of running the Collector as root.

### Image requirements

As said in [Prerequisites](#prerequisites), the Collector container must include `journalctl` to access the systemd journal.

For more information, see the [OTel upstream documentation﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.155.0/receiver/journaldreceiver/examples/container).

### Security context

Reading from the systemd journal requires specific Linux capabilities.

Apply the following `securityContext` (shown in the code block below) to the Collector container.
The table then describes the purpose of relevant attributes within the security context definition.

```
securityContext:



allowPrivilegeEscalation: false



readOnlyRootFilesystem: true



seccompProfile:



type: RuntimeDefault



runAsUser: 0



capabilities:



drop:



- ALL



add:



- DAC_READ_SEARCH



- SYS_PTRACE
```

| Setting | Reason |
| --- | --- |
| `allowPrivilegeEscalation: false` | Prevents the process from gaining additional privileges beyond the declared capabilities. |
| `readOnlyRootFilesystem: true` | Makes the container root filesystem read-only to reduce the attack surface. |
| `seccompProfile: RuntimeDefault` | Applies the default seccomp profile to restrict permitted system calls. |
| `runAsUser: 0` | The Collector process runs as root to access the journal socket.  When you run as root, you increase the risk of granting root-level access to the node. For more information, see [Run as root](#collector-root). |
| `DAC_READ_SEARCH` | Bypasses file-system permission checks when reading journal files. |
| `SYS_PTRACE` | Required for process introspection used by the journald receiver. |

### Run as root

The journald receiver does not require that you run as root, but it is the simplest way to obtain the necessary Linux capabilities in a containerized environment.

If your Collector runs as root, avoid co-locating network-exposed receivers (such as `otlp` bound to `0.0.0.0`) in the same instance.
A remotely exploitable vulnerability in a network receiver would grant root-level access to the node.

To reduce risk, use a dedicated Collector instance solely for journald log collection.
If you must include additional receivers in the same instance, bind them to `127.0.0.1` (loopback) rather than `0.0.0.0` to prevent external access.

### Volume mounts

Mount the host's journal directory into the container as read-only.

Set `directory: /run/log/journal` in the `journald` receiver configuration to match this mount path.

* On traditional (non-containerized) Linux systems the persistent journal is stored at `/var/log/journal`.
* In containerized Linux environments the journal is typically written to `/run/log/journal`.
  This is ephemeral, in-memory storage.

```
volumeMounts:



- name: run-journal



mountPath: /run/log/journal



readOnly: true



volumes:



- name: run-journal



hostPath:



path: /run/log/journal
```

## Limits and limitations

Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information, see [Ingest OpenTelemetry logs](/managed/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Related topics

* [Ingest logs from files with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")
* [Ingest syslog data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")
* [Ingest Kubernetes pod logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs "Configure the OpenTelemetry Collector to ingest Kubernetes pod log files into Dynatrace.")
* [Transform and filter data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")