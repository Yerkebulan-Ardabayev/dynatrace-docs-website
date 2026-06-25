---
title: Settings API - Security Posture Management- Kubernetes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-kubernetes-security-posture-management
scraped: 2026-05-12T11:48:07.489074
---

# Settings API - Security Posture Management- Kubernetes schema table

# Settings API - Security Posture Management- Kubernetes schema table

* Published Mar 17, 2025

### Security Posture Management: Kubernetes (`builtin:kubernetes.security-posture-management)`

[Kubernetes Security Posture Management (KSPM)](https://dt-url.net/b303utv) помогает оценить и обеспечить безопасность и соответствие требованиям Kubernetes-окружения, придерживаясь лучших практик безопасности и регуляторных стандартов.

Примечание: [enable Kubernetes Security Posture Management](https://dt-url.net/o003ue9) можно на уровне окружения или кластера.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:kubernetes.security-posture-management` | * `group:appsec.security-posture-management` * `group:appsec` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.security-posture-management` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Security Posture Management `configurationDatasetPipelineEnabled` | boolean | Следуйте [installation instructions](https://dt-url.net/4x23ut5), чтобы развернуть компоненты Security Posture Management. | Required |