---
title: Settings API - Monitoring settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring
scraped: 2026-05-12T11:44:03.867350
---

# Settings API - Monitoring settings schema table

# Settings API - Monitoring settings schema table

* Published Dec 05, 2023

### Параметры мониторинга (`builtin:cloud.kubernetes.monitoring)`

Настройте функции мониторинга для Kubernetes или OpenShift. Подробнее об этих функциях см. в [documentation](https://dt-url.net/2ma0vhp).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.kubernetes.monitoring` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes.monitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить namespace, сервисы, workload и pod в Kubernetes `cloudApplicationPipelineEnabled` | boolean | - | Required |
| Мониторить аннотированные Prometheus-экспортёры `openMetricsPipelineEnabled` | boolean | Руководство по аннотациям см. в [documentation](https://dt-url.net/g42i0ppw).  Метрики Prometheus в Kubernetes-окружениях подпадают под лицензирование.  Если у вас DPS-лицензирование, подробности см. в [licensing documentation](https://dt-url.net/nd0348b).  Если у вас не-DPS-лицензирование, подробности см. в [Monitoring consumption](https://dt-url.net/k8smpm). | Required |
| Мониторить метрики ресурсов workload и узла `openMetricsBuiltinEnabled` | boolean | Метрики ресурсов workload и узла основаны на подмножестве cAdvisor-метрик. В зависимости от размера Kubernetes-кластера это может увеличить потребление CPU/памяти ActiveGate. Для метрик ресурсов узла требуется ActiveGate 1.271+ | Required |
| Мониторить события `eventProcessingActive` | boolean | Все события мониторятся, если не заданы фильтры событий. Все принятые события по умолчанию подпадают под лицензирование.  Если у вас DPS-лицензия, подробности см. в [licensing documentation](https://dt-url.net/cee34zj).  Если у вас не-DPS-лицензия, подробности см. в [DDUs for events](https://dt-url.net/5n03vcu). | Required |
| Фильтровать события `filterEvents` | boolean | Включать только события, заданные через Events Field Selectors | Required |
| Включать важные события `includeAllFdiEvents` | boolean | Список включённых событий см. в [documentation](https://dt-url.net/l61d02no).  Автоматически включать все события, релевантные для Davis | Required |
| Селекторы полей событий `eventPatterns` | [EventComplexType](#EventComplexType)[] | Задайте фильтры событий Kubernetes для ingest событий в окружение. Подробнее см. в [documentation](https://dt-url.net/2201p0u). | Required |

##### Объект `EventComplexType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя селектора поля `label` | text | - | Required |
| Выражение селектора поля `pattern` | text | Набор допустимых символов для этого поля расширен в ActiveGate версии 1.259. Подробнее см. в [documentation](https://dt-url.net/7h23wuk#set-up-event-field-selectors). | Required |
| Активировать `active` | boolean | - | Required |