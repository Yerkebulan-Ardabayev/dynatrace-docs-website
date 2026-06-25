---
title: Settings API - Container monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-monitoring-rule
scraped: 2026-05-12T11:43:56.451284
---

# Settings API - Container monitoring rules schema table

# Settings API - Container monitoring rules schema table

* Published Dec 05, 2023

### Правила мониторинга контейнеров (`builtin:container.monitoring-rule)`

В контейнерных окружениях OneAgent автоматически внедряет модули кода в контейнеризованные процессы, обеспечивая полную full-stack видимость приложений, работающих в контейнерах. Dynatrace даёт полный контроль над автоматическим внедрением модулей кода в контейнерные технологии.

В Kubernetes правила мониторинга контейнеров вычисляются только в режиме внедрения `classicFullStack`. В режимах `cloudNativeFullStack` или `applicationMonitoring` правила игнорируются.

Используйте вариант конфигурации на основе аннотаций, как описано [here](https://dt-url.net/k8sdtoconfig).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.monitoring-rule` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.monitoring-rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Режим `mode` | enum | Возможные значения: * `MONITORING_OFF` * `MONITORING_ON` | Required |
| Свойство контейнера `property` | enum | Возможные значения: * `CONTAINER_NAME` * `IMAGE_NAME` * `KUBERNETES_NAMESPACE` * `KUBERNETES_CONTAINERNAME` * `KUBERNETES_BASEPODNAME` * `KUBERNETES_FULLPODNAME` * `KUBERNETES_PODUID` | Required |
| Условный оператор `operator` | enum | Возможные значения: * `STARTS` * `NOT_STARTS` * `ENDS` * `NOT_ENDS` * `CONTAINS` * `NOT_CONTAINS` * `EQUALS` * `NOT_EQUALS` * `EXISTS` * `NOT_EXISTS` | Required |
| Значение условия `value` | text | - | Required |