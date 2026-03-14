---
title: Settings API - таблица схем приложения Kubernetes
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes
scraped: 2026-03-06T21:22:29.540143
---

# Settings API — таблица схемы приложения Kubernetes

# Settings API — таблица схемы приложения Kubernetes

* Опубликовано 26 февраля 2024 г.

### Приложение Kubernetes (`builtin:app-transition.kubernetes`)

Откройте для себя улучшенный опыт работы с новым приложением Kubernetes.

| Идентификатор схемы | Группы схем | Область действия |
| --- | --- | --- |
| `builtin:app-transition.kubernetes` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` — кластер Kubernetes  `environment` |

Получение схемы через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-transition.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-transition.kubernetes` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия **Чтение настроек** (`settings.read`). Чтобы узнать, как получить и использовать токен, см. раздел [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| `kubernetesAppOptions` | [KubernetesAppOptions](#KubernetesAppOptions) | - | Обязательно |

##### Объект `KubernetesAppOptions`

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Новый интерфейс Kubernetes `enableKubernetesApp` | boolean | - | Обязательно |
