---
title: Containerized ActiveGate volumes
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/ag-container-persistence
scraped: 2026-02-17T05:09:06.798345
---

# Containerized ActiveGate volumes

# Containerized ActiveGate volumes

* Latest Dynatrace
* 3-min read
* Published Sep 01, 2023

While running, the ActiveGate container writes data to certain directories within the root filesystem.

## Writeable directories

Purpose of directory

Default path

ActiveGate configuration

`/var/lib/dynatrace/gateway/config`

ActiveGate SSL directory

`/var/lib/dynatrace/gateway/ssl`

ActiveGate temporary files

`/var/tmp/dynatrace/gateway`

ActiveGate logs

`/var/log/dynatrace/gateway`

Environment data

`/var/lib/dynatrace/gateway/data`

Dump files uploaded to ActiveGate by OneAgent

`/var/lib/dynatrace/gateway/dump`

ActiveGate temporary files

`/var/lib/dynatrace/gateway/temp`

### Size requirements

See [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") for estimated size requirements for each directory.

## Hardened security

The ActiveGate [example deployment](/docs/ingest-from/dynatrace-activegate/activegate-in-container#deployment-example "Deploy a containerized ActiveGate.") has been hardened to minimize potential attacks: `securityContext.readOnlyRootFilesystem` is set to `true`.

This prevents the container from modifying any image content, so [directories](#directories) need to be set up using volumes.

### Security context

```
securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- all



privileged: false



readOnlyRootFilesystem: true



runAsNonRoot: true



seccompProfile:



type: RuntimeDefault
```

### Volumes

```
volumeMounts:



- name: server-certs-storage



mountPath: /var/lib/dynatrace/gateway/ssl



- name: ag-lib-gateway-config



mountPath: /var/lib/dynatrace/gateway/config



- name: ag-lib-gateway-temp



mountPath: /var/lib/dynatrace/gateway/temp



- name: ag-lib-gateway-data



mountPath: /var/lib/dynatrace/gateway/data



- name: ag-log-gateway



mountPath: /var/log/dynatrace/gateway



- name: ag-tmp-gateway



mountPath: /var/tmp/dynatrace/gateway
```

Refer to [ActiveGate storage requirements](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#space-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") for volume sizing.