---
title: Synthetic monitors API v2 - GET определение монитора Synthetic
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-monitor-definition
scraped: 2026-05-12T12:15:46.525963
---

# Synthetic monitors API v2 - GET определение монитора Synthetic

# Synthetic monitors API v2 - GET определение монитора Synthetic

* Справочник
* Updated on May 05, 2026

Возвращает определение монитора Synthetic для заданного ID монитора.

Метод доступен только для браузерных и NAM-мониторов.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `settings.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| monitorId | string | Идентификатор монитора. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticMultiProtocolMonitorResponse](#openapi-definition-SyntheticMultiProtocolMonitorResponse) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticMultiProtocolMonitorResponse`

Монитор Network Availability.

| Поле | Тип | Описание |
| --- | --- | --- |
| description | string | Описание монитора |
| enabled | boolean | Если true, монитор включён. |
| entityId | string | Entity id монитора. |
| frequencyMin | integer | Частота монитора, в минутах. |
| locations | string[] | Локации, которым назначен монитор. |
| modificationTimestamp | integer | Метка времени последнего изменения |
| name | string | Имя монитора. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация порогов производительности. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto[]](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto) | Первичные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS и не для Managed. |
| steps | [SyntheticMultiProtocolMonitorStepDto[]](#openapi-definition-SyntheticMultiProtocolMonitorStepDto) | Шаги монитора. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки недоступности. |
| tags | [SyntheticTagWithSourceDto[]](#openapi-definition-SyntheticTagWithSourceDto) | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. |
| type | string | Тип монитора. Поле может принимать значения: * `MULTI_PROTOCOL` * `BROWSER` |

#### Объект `SyntheticMonitorPerformanceThresholdsDto`

Конфигурация порогов производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Порог производительности включён (`true`) или отключён (`false`). |
| thresholds | [SyntheticMonitorPerformanceThresholdDto[]](#openapi-definition-SyntheticMonitorPerformanceThresholdDto) | Список правил порогов производительности. |

#### Объект `SyntheticMonitorPerformanceThresholdDto`

Правило порога производительности.

| Поле | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации Поле может принимать значения: * `AVG` * `MAX` * `MIN` |
| dealertingSamples | integer | Количество самых свежих не нарушающих выполнений запроса, которое закрывает проблему. |
| samples | integer | Количество выполнений запроса в анализируемом скользящем окне (размер скользящего окна). |
| stepIndex | integer | Укажите индекс шага, к которому применяется порог. Если порог монитор-уровня, индекс не нужен. |
| threshold | number | Уведомлять, если запрос монитора выполняется дольше *X* единиц времени. Для мониторов Network Availability единица времени, это миллисекунды, для браузерных мониторов, секунды. |
| type | string | Тип порога производительности. Поле может принимать значения: * `MONITOR` * `STEP` |
| violatingSamples | integer | Количество нарушающих выполнений запроса в анализируемом скользящем окне. |

#### Объект `SyntheticMonitorPrimaryGrailTagDto`

Пара ключ-значение первичного grail-тега.

| Поле | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ тега. |
| value | string | Значение тега. |

#### Объект `SyntheticMultiProtocolMonitorStepDto`

Шаг монитора доступности сети.

| Поле | Тип | Описание |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Список ограничений, которые применяются ко всем запросам в шаге. |
| name | string | Имя шага. |
| properties | object | Свойства, которые применяются ко всем запросам в шаге. |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto[]](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto) | Конфигурации запросов. |
| requestType | string | Тип запроса. Поле может принимать значения: * `ICMP` * `TCP` * `DNS` |
| targetFilter | string | Фильтр целей. |
| targetList | string[] | Список целей. |

#### Объект `SyntheticMonitorConstraintDto`

Ограничение синтетического монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| properties | object | Свойства ограничения. |
| type | string | Тип ограничения. |

#### Объект `SyntheticMultiProtocolRequestConfigurationDto`

Конфигурация запроса монитора доступности сети.

| Поле | Тип | Описание |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Ограничения запроса. |

#### Объект `SyntheticMonitorOutageHandlingSettingsDto`

Конфигурация обработки недоступности.

| Поле | Тип | Описание |
| --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев для всех локаций. |
| globalOutages | boolean | Создать проблему и отправить алерт, когда монитор недоступен на всех настроенных локациях. |
| localConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев. |
| localLocationOutageCountThreshold | integer | Количество отказавших локаций. |
| localOutages | boolean | Создать проблему и отправить алерт, когда монитор недоступен в течение одного или нескольких последовательных запусков на любой локации. |
| origin | string | Указывает происхождение этих настроек. Поле может принимать значения: * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |
| retryOnError | boolean | Свойство только для Browser Monitor. Если задано true, повтор выполнения произойдёт в случае сбоя монитора. |

#### Объект `SyntheticTagWithSourceDto`

Тег с источником отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO. Поле может принимать значения: * `AUTO` * `RULE_BASED` * `USER` |
| value | string | Значение тега. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "My network availability monitor description",



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F19"



],



"name": "My network availability monitor",



"performanceThresholds": {



"enabled": "true",



"thresholds": [



{



"aggregation": "AVG",



"dealertingSamples": "5",



"samples": "5",



"stepIndex": "0",



"threshold": "200",



"violatingSamples": "3"



}



]



},



"primaryGrailTags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "another sample key",



"value": "another sample value"



}



],



"steps": [



{



"constraints": [



{



"properties": {



"operator": ">=",



"value": "95"



},



"type": "SUCCESS_RATE_PERCENT"



}



],



"name": "Step 1",



"properties": {



"ICMP_IP_VERSION": "4",



"ICMP_NUMBER_OF_PACKETS": "8",



"ICMP_TIMEOUT_FOR_REPLY": "PT1S"



},



"requestConfigurations": [



{



"constraints": [



{



"properties": {



"operator": "=",



"value": "100"



},



"type": "ICMP_SUCCESS_RATE_PERCENT"



}



]



}



],



"requestType": "ICMP",



"targetFilter": "ipMask == 127.0.0.1/24",



"targetList": [



"127.0.0.1",



"127.0.0.2"



]



}



],



"syntheticMonitorOutageHandlingSettings": {



"globalConsecutiveOutageCountThreshold": "1",



"globalOutages": "true",



"localConsecutiveOutageCountThreshold": "3",



"localLocationOutageCountThreshold": "3",



"localOutages": "true"



},



"tags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "sample key"



}



],



"type": "MULTI_PROTOCOL"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")