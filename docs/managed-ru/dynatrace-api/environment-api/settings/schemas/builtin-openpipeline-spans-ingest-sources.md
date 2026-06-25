---
title: Settings API - Ingest sources configuration (spans) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-ingest-sources
scraped: 2026-05-12T11:47:27.361772
---

# Settings API - Ingest sources configuration (spans) schema table

# Settings API - Ingest sources configuration (spans) schema table

* Опубликовано 25 августа 2025 г.

### Конфигурация ingest sources (spans) (`builtin:openpipeline.spans.ingest-sources)`

Содержит конфигурацию ingest sources

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:openpipeline.spans.ingest-sources` | * `group:openpipeline.all.ingest-sources` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.spans.ingest-sources` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.spans.ingest-sources` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.spans.ingest-sources` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Список metadata для ingest source `metadataList` | [MetadataEntry](#MetadataEntry)[] | - | Required |
| Display name endpoint `displayName` | text | - | Required |
| Тип source `sourceType` | enum | Возможные значения: * `http` * `extension` | Required |
| Source `source` | text | - | Required |
| Сегмент endpoint `pathSegment` | text | - | Required |
| Bucket по умолчанию `defaultBucket` | text | - | Optional |
| Включено `enabled` | boolean | - | Required |
| Static routing для endpoint `staticRouting` | [StaticRouting](#StaticRouting) | - | Optional |
| Processing stage `processing` | [Stage](#Stage) | - | Optional |

##### Объект `MetadataEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ записи metadata `entryKey` | text | - | Required |
| Значение записи metadata `entryValue` | text | - | Optional |

##### Объект `StaticRouting`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Pipeline Type `pipelineType` | enum | Возможные значения: * `custom` * `builtin` | Required |
| Pipeline ID `pipelineId` | setting | - | Required |
| Builtin Pipeline ID `builtinPipelineId` | text | - | Required |

##### Объект `Stage`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Processors stage `processors` | [Processor](#Processor)[] | - | Required |

##### Объект `Processor`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Идентификатор processor `id` | text | - | Required |
| Тип `type` | enum | Тип processor Возможные значения: * `fieldsAdd` * `fieldsRemove` * `fieldsRename` * `dql` * `technology` * `drop` * `bucketAssignment` * `noStorage` * `securityContext` * `counterMetric` * `samplingAwareCounterMetric` * `valueMetric` * `histogramMetric` * `samplingAwareValueMetric` * `samplingAwareHistogramMetric` * `davis` * `bizevent` * `sdlcEvent` * `azureLogForwarding` * `securityEvent` * `costAllocation` * `productAllocation` * `smartscapeNode` * `smartscapeEdge` | Required |
| Matcher (DQL) `matcher` | text | [См. документацию](https://dt-url.net/bp234rv) | Required |
| Описание `description` | text | - | Required |
| Sample data `sampleData` | text | - | Optional |
| Включено `enabled` | boolean | - | Required |
| Атрибуты DQL processor `dql` | [DqlAttributes](#DqlAttributes) | - | Required |
| Атрибуты processor добавления полей `fieldsAdd` | [FieldsAddAttributes](#FieldsAddAttributes) | - | Required |
| Атрибуты processor переименования полей `fieldsRename` | [FieldsRenameAttributes](#FieldsRenameAttributes) | - | Required |
| Атрибуты processor удаления полей `fieldsRemove` | [FieldsRemoveAttributes](#FieldsRemoveAttributes) | - | Required |
| Атрибуты technology processor `technology` | [TechnologyAttributes](#TechnologyAttributes) | - | Required |
| Атрибуты processor назначения bucket `bucketAssignment` | [BucketAssignmentAttributes](#BucketAssignmentAttributes) | - | Required |
| Атрибуты processor security context `securityContext` | [SecurityContextAttributes](#SecurityContextAttributes) | - | Required |
| Атрибуты processor counter metric `counterMetric` | [CounterMetricAttributes](#CounterMetricAttributes) | - | Required |
| Атрибуты processor sampling-aware counter metric `samplingAwareCounterMetric` | [SamplingAwareCounterMetricAttributes](#SamplingAwareCounterMetricAttributes) | - | Required |
| Атрибуты processor value metric `valueMetric` | [ValueMetricAttributes](#ValueMetricAttributes) | - | Required |
| Атрибуты processor histogram metric `histogramMetric` | [HistogramMetricAttributes](#HistogramMetricAttributes) | - | Required |
| Атрибуты processor sampling-aware value metric `samplingAwareValueMetric` | [SamplingAwareValueMetricAttributes](#SamplingAwareValueMetricAttributes) | - | Required |
| Атрибуты processor sampling-aware histogram metric `samplingAwareHistogramMetric` | [SamplingAwareHistogramMetricAttributes](#SamplingAwareHistogramMetricAttributes) | - | Required |
| Атрибуты processor извлечения Davis event `davis` | [DavisAttributes](#DavisAttributes) | - | Required |
| Атрибуты processor извлечения bizevent `bizevent` | [BizeventAttributes](#BizeventAttributes) | - | Required |
| Атрибуты processor извлечения SdlcEvent `sdlcEvent` | [SdlcEventAttributes](#SdlcEventAttributes) | - | Required |
| Атрибуты processor извлечения Smartscape node `smartscapeNode` | [SmartscapeNodeAttributes](#SmartscapeNodeAttributes) | - | Required |
| Атрибуты processor извлечения Smartscape edge `smartscapeEdge` | [SmartscapeEdgeAttributes](#SmartscapeEdgeAttributes) | - | Required |
| Атрибуты processor Azure log forwarding `azureLogForwarding` | [AzureLogForwardingAttributes](#AzureLogForwardingAttributes) | - | Required |
| Атрибуты processor извлечения security event `securityEvent` | [SecurityEventAttributes](#SecurityEventAttributes) | - | Required |
| Атрибуты processor cost allocation `costAllocation` | [CostAllocationAttributes](#CostAllocationAttributes) | - | Required |
| Атрибуты processor product allocation `productAllocation` | [ProductAllocationAttributes](#ProductAllocationAttributes) | - | Required |

##### Объект `DqlAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Скрипт DQL `script` | text | - | Required |

##### Объект `FieldsAddAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Поля для добавления `fields` | [FieldsAddAttributesEntry](#FieldsAddAttributesEntry)[] | - | Required |

##### Объект `FieldsRenameAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Поля для переименования `fields` | [FieldsRenameAttributesEntry](#FieldsRenameAttributesEntry)[] | - | Required |

##### Объект `FieldsRemoveAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Поля для удаления `fields` | set | - | Required |

##### Объект `TechnologyAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Custom matcher `customMatcher` | text | Custom-условие сопоставления, которое используется вместо technology matcher. | Optional |
| Technology ID `technologyId` | text | - | Required |

##### Объект `BucketAssignmentAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя bucket `bucketName` | text | - | Required |

##### Объект `SecurityContextAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Назначение значения security context `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### Объект `CounterMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### Объект `SamplingAwareCounterMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | Возможные значения: * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | Возможные значения: * `disabled` * `enabled` | Optional |

##### Объект `ValueMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Поле со значением метрики `field` | text | - | Required |
| Значение по умолчанию для значения метрики `defaultValue` | text | - | Optional |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### Объект `HistogramMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Поле со значением метрики `field` | text | - | Required |
| Значение по умолчанию для значения метрики `defaultValue` | text | - | Optional |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |

##### Объект `SamplingAwareValueMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Поле со значением метрики `field` | text | - | Required |
| Значение по умолчанию для значения метрики `defaultValue` | text | - | Optional |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | Возможные значения: * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | Возможные значения: * `disabled` * `enabled` | Optional |
| Measurement `measurement` | enum | Возможные значения: * `field` * `duration` | Required |

##### Объект `SamplingAwareHistogramMetricAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ метрики `metricKey` | text | - | Required |
| Поле со значением метрики `field` | text | - | Required |
| Значение по умолчанию для значения метрики `defaultValue` | text | - | Optional |
| Список dimensions `dimensions` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Sampling `sampling` | enum | Возможные значения: * `disabled` * `enabled` | Optional |
| Aggregation `aggregation` | enum | Возможные значения: * `disabled` * `enabled` | Optional |
| Measurement `measurement` | enum | Возможные значения: * `field` * `duration` | Required |

##### Объект `DavisAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойства `properties` | [DavisEventProperty](#DavisEventProperty)[] | - | Required |

##### Объект `BizeventAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип события `eventType` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Провайдер события `eventProvider` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Извлечение поля `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### Объект `SdlcEventAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип события `eventType` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Провайдер события `eventProvider` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Категория события `eventCategory` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Статус события `eventStatus` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Извлечение поля `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### Объект `SmartscapeNodeAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип node `nodeType` | text | - | Required |
| Имя поля ID node `nodeIdFieldName` | text | - | Required |
| Компоненты ID `idComponents` | [SmartscapeIdComponentsEntry](#SmartscapeIdComponentsEntry)[] | - | Required |
| Извлекать node `extractNode` | boolean | - | Required |
| Имя node `nodeName` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |
| Поля для извлечения `fieldsToExtract` | [SmartscapeFieldExtractionEntry](#SmartscapeFieldExtractionEntry)[] | - | Required |
| Static edges для извлечения `staticEdgesToExtract` | [SmartscapeStaticEdgeExtractionEntry](#SmartscapeStaticEdgeExtractionEntry)[] | - | Required |

##### Объект `SmartscapeEdgeAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип source `sourceType` | text | - | Required |
| Имя поля ID source `sourceIdFieldName` | text | - | Required |
| Тип edge `edgeType` | text | - | Required |
| Тип target `targetType` | text | - | Required |
| Имя поля ID target `targetIdFieldName` | text | - | Required |

##### Объект `AzureLogForwardingAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ForwarderConfigId `forwarderConfigId` | text | - | Required |
| Извлечение поля `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### Объект `SecurityEventAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Извлечение поля `fieldExtraction` | [FieldExtraction](#FieldExtraction) | - | Required |

##### Объект `CostAllocationAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Стратегия задания поля cost allocation `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### Объект `ProductAllocationAttributes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Стратегия задания поля product allocation `value` | [GenericValueAssignment](#GenericValueAssignment) | - | Required |

##### Объект `FieldsAddAttributesEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя поля `name` | text | - | Required |
| Значение поля `value` | text | - | Required |

##### Объект `FieldsRenameAttributesEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя поля `fromName` | text | - | Required |
| Новое имя поля `toName` | text | - | Required |

##### Объект `GenericValueAssignment`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип назначения значения `type` | enum | Возможные значения: * `constant` * `multiValueConstant` * `field` | Required |
| Константное значение `constant` | text | - | Required |
| Константное multi-value `multiValueConstant` | list | - | Required |
| Значение из поля `field` | [ValueAssignmentFromFieldEntry](#ValueAssignmentFromFieldEntry) | - | Required |

##### Объект `FieldExtractionEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Стратегия извлечения поля `strategy` | enum | Возможные значения: * `equals` * `startsWith` | Optional |
| Тип извлечения значения поля `extractionType` | enum | Возможные значения: * `constant` * `field` | Required |
| Имя поля-источника `sourceFieldName` | text | - | Required |
| Имя поля-приёмника `destinationFieldName` | text | - | Optional |
| Значение по умолчанию `defaultValue` | text | - | Optional |
| Имя поля-приёмника `constantFieldName` | text | - | Required |
| Константное значение для назначения полю `constantValue` | text | - | Required |

##### Объект `DavisEventProperty`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Стратегия извлечения поля `strategy` | enum | Возможные значения: * `equals` * `startsWith` | Optional |
| Ключ `key` | text | - | Required |
| Значение `value` | text | - | Required |

##### Объект `FieldExtraction`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип извлечения полей `type` | enum | Возможные значения: * `include` * `exclude` * `includeAll` | Required |
| Поля `include` | Set<[FieldExtractionEntry](#FieldExtractionEntry)> | - | Required |
| Поля `exclude` | set | - | Required |

##### Объект `SmartscapeIdComponentsEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Компонент ID `idComponent` | text | - | Required |
| Имя ссылающегося поля `referencedFieldName` | text | - | Required |

##### Объект `SmartscapeFieldExtractionEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Стратегия извлечения поля `strategy` | enum | Возможные значения: * `equals` * `startsWith` | Optional |
| Имя поля `fieldName` | text | - | Required |
| Имя ссылающегося поля `referencedFieldName` | text | - | Required |

##### Объект `SmartscapeStaticEdgeExtractionEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип edge `edgeType` | text | - | Required |
| Тип target `targetType` | text | - | Required |
| Имя поля ID target `targetIdFieldName` | text | - | Required |

##### Объект `ValueAssignmentFromFieldEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя поля-источника `sourceFieldName` | text | - | Required |
| Значение по умолчанию `defaultValue` | text | - | Optional |