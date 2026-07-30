---
title: Settings API - Service Detection v2 for OneAgent schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-v2-for-oneagent
---

# Settings API - Service Detection v2 for OneAgent schema table

# Settings API - Service Detection v2 for OneAgent schema table

* Опубликовано 25 сен. 2025

### Service Detection v2 for OneAgent (`builtin:service-detection-v2-for-oneagent)`

При включении SDv2 для OneAgent используются те же правила на основе атрибутов, что и для OpenTelemetry, при обнаружении сервисов, эндпоинтов и сбоев. Подробности в [документации SDv2﻿](https://dt-url.net/5e0309z).

**Важно**

Сервисы, соответствующие заданным условиям, получат новые ключи метрик, что нарушит работу существующих запросов API, дашбордов и имён сервисов. Custom, opaque, third party, database и message queue сервисы обнаруживаются в SDv2 иначе. Представления анализа для операций сервис-база данных и сервис-очередь сообщений будут объявлены в ближайших релизах.

| ID схемы | Группы схем | Область действия |
| --- | --- | --- |
| `builtin:service-detection-v2-for-oneagent` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - пространство имён Kubernetes  `KUBERNETES_CLUSTER` - кластер Kubernetes  `HOST_GROUP` - Host Group  `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью **Read settings** (`settings.read`). Как получить и использовать токен, описано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Enable Service detection v2 for Kubernetes workloads `enableSDV2ForKubernetesWorkloads` | boolean | - | Обязательный |
| Matching condition for Kubernetes workloads `condition` | text | Сужает область действия опции фильтрацией по условиям [DQL matcher﻿](https://dt-url.net/l603wby) для выбранного набора атрибутов.  Service detection v2 применяется только при выполнении этого условия. Допустимые атрибуты: ресурсные атрибуты и пользовательские атрибуты. Если поле пустое, условие считается всегда выполненным. | Обязательный |
| Enable Service detection v2 for FaaS `enableSDV2ForFaaS` | boolean | - | Необязательный |
| Matching condition for FaaS `conditionForFaaS` | text | Сужает область действия опции фильтрацией по условиям [DQL matcher﻿](https://dt-url.net/l603wby) для выбранного набора атрибутов.  Service detection v2 применяется только при выполнении этого условия. Допустимые атрибуты: ресурсные атрибуты и пользовательские атрибуты. Если поле пустое, условие считается всегда выполненным. | Обязательный |
| Enable Service detection v2 for generic workloads `enableSDV2ForAnyWorkload` | boolean | Убедитесь, что правила обнаружения сервисов (`<your-dynatrace-url>/builtin:service-detection-rules`) и правила разделения (`<your-dynatrace-url>/builtin:service-splitting-rules`) актуальны для этих рабочих нагрузок. | Необязательный |
| Matching condition for generic workloads `conditionForAnyWorkload` | text | Сужает область действия опции фильтрацией по условиям [DQL matcher﻿](https://dt-url.net/l603wby) для выбранного набора атрибутов. Ресурсные атрибуты должны присутствовать.  Service detection v2 применяется только при выполнении этого условия. Допустимые атрибуты: ресурсные атрибуты и пользовательские атрибуты. Если поле пустое, условие считается всегда выполненным. Если набор ресурсных атрибутов отсутствует или пуст, условие считается не выполненным. | Обязательный |