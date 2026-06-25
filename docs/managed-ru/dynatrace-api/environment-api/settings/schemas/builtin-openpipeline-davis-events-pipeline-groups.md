---
title: Settings API - Pipeline Groups configuration (davis.events) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-pipeline-groups
scraped: 2026-05-12T11:42:21.952062
---

# Settings API - Pipeline Groups configuration (davis.events) schema table

# Settings API - Pipeline Groups configuration (davis.events) schema table

* Published Sep 25, 2025

### Конфигурация Pipeline Groups (davis.events) (`builtin:openpipeline.davis.events.pipeline-groups)`

Содержит конфигурацию pipeline group

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:openpipeline.davis.events.pipeline-groups` | * `group:openpipeline.all.pipeline-groups` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.davis.events.pipeline-groups` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.davis.events.pipeline-groups` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.davis.events.pipeline-groups` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отображаемое имя `displayName` | text | - | Required |
| Pipeline'ы, обёрнутые этой группой `memberPipelines` | set | - | Required |
| Конфигурация stage для pipeline'ов-членов `memberStages` | [StageConfig](#StageConfig) | - | Required |
| Композиция `composition` | [PipelineGroupComposition](#PipelineGroupComposition)[] | - | Required |

##### Объект `StageConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип конфигурации stage `type` | enum | Возможные значения: * `include` * `exclude` * `includeAll` | Required |
| Включаемые stage `include` | Set<[StageType](#StageType)> | Возможные значения: * `processing` * `securityContext` * `costAllocation` * `productAllocation` * `storage` * `smartscapeNodeExtraction` * `smartscapeEdgeExtraction` * `metricExtraction` * `davis` * `dataExtraction` | Required |
| Исключаемые stage `exclude` | Set<[StageType](#StageType)> | Возможные значения: * `processing` * `securityContext` * `costAllocation` * `productAllocation` * `storage` * `smartscapeNodeExtraction` * `smartscapeEdgeExtraction` * `metricExtraction` * `davis` * `dataExtraction` | Required |

##### Объект `PipelineGroupComposition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Placeholder для обёрнутого pipeline `isPipelinePlaceholder` | boolean | - | Required |
| ID pipeline `pipelineId` | setting | - | Required |
| Конфигурация stage для этих pipeline'ов `stages` | [StageConfig](#StageConfig) | - | Required |