---
title: Settings API - Container monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-technology
scraped: 2026-05-12T11:47:42.869431
---

# Settings API - Container monitoring schema table

# Settings API - Container monitoring schema table

* Published Dec 05, 2023

### Container monitoring (`builtin:container.technology)`

Enable/disable automatic injection of code modules into specific containers.

Dynatrace OneAgent automatically monitors all processes that are running on your monitored hosts. Within container environments (for example, Kubernetes, OpenShift, Cloud Foundry, or Docker), OneAgent automatically injects code modules into containerized processes to provide out of the box full-stack visibility into applications running within containers. Enabling auto-injection provides deep monitoring for all processes within containers, at both the request- and PurePath levels. If disabled, OneAgent will not inject into a container of a specific type at all. Dynatrace provides complete control over automatic injection of code modules into the container technologies listed below. For full details see [Supported container versionsï»¿](https://dt-url.net/lmy0p0j "Visit Dynatrace support center").

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.technology` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.technology` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.technology` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.technology` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| BOSH Process Manager (BPM) containers `boshProcessManager` | boolean | Platform: Cloud Foundry  Status: Released  Operating system: Linux  Min agent version: 1.159 | Required |
| Containerd containers `containerd` | boolean | Platform: Kubernetes  Status: Released  Operating system: Linux  Min agent version: 1.169 | Required |
| CRI-O containers `crio` | boolean | Platform: Kubernetes  Status: Released  Operating system: Linux  Min agent version: 1.163 | Required |
| Docker containers `docker` | boolean | Platform: Docker and Kubernetes  Status: Released  Operating system: Linux | Required |
| Docker for Windows Server containers `dockerWindows` | boolean | Platform: Docker  Status: Early adopter  Operating system: Windows  Min agent version: 1.149 | Required |
| Garden containers `garden` | boolean | Platform: Cloud Foundry  Status: Released  Operating system: Linux  Min agent version: 1.133 | Required |
| Winc for Windows Server containers `winc` | boolean | Platform: Cloud Foundry  Status: Early adopter  Operating system: Windows  Min agent version: 1.175 | Required |
| Podman containers `podman` | boolean | Platform: Podman  Status: Released  Operating system: Linux  Min agent version: 1.267 | Required |