---
title: Settings API - Security Posture Management- Kubernetes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-kubernetes-security-posture-management
scraped: 2026-05-12T11:48:07.489074
---

# Settings API - Security Posture Management- Kubernetes schema table

# Settings API - Security Posture Management- Kubernetes schema table

* Published Mar 17, 2025

### Security Posture Management: Kubernetes (`builtin:kubernetes.security-posture-management)`

[Kubernetes Security Posture Management (KSPM)ï»¿](https://dt-url.net/b303utv) helps you assess and ensure the security and compliance of a Kubernetes environment by adhering to security best practices and regulatory standards.

Note: You can [enable Kubernetes Security Posture Managementï»¿](https://dt-url.net/o003ue9) per environment or cluster.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:kubernetes.security-posture-management` | * `group:appsec.security-posture-management` * `group:appsec` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Security Posture Management `configurationDatasetPipelineEnabled` | boolean | Follow the [installation instructionsï»¿](https://dt-url.net/4x23ut5) to deploy the Security Posture Management components. | Required |