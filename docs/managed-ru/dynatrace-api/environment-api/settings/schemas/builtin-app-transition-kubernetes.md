---
title: Settings API - Kubernetes app schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes
scraped: 2026-05-12T11:39:17.440899
---

# Settings API - Kubernetes app schema table

# Settings API - Kubernetes app schema table

* Published Feb 26, 2024

### Приложение Kubernetes (`builtin:app-transition.kubernetes)`

Раскройте улучшенный опыт работы с новым приложением Kubernetes.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:app-transition.kubernetes` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `kubernetesAppOptions` | [KubernetesAppOptions](#KubernetesAppOptions) | - | Required |

##### The `KubernetesAppOptions` object

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Новый опыт Kubernetes `enableKubernetesApp` | boolean | - | Required |