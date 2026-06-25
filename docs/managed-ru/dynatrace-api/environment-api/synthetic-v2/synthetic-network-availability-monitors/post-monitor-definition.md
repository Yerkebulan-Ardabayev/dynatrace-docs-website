---
title: Synthetic monitors API v2 - Создание определения монитора Synthetic
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/post-monitor-definition
scraped: 2026-05-12T12:15:44.370255
---

# Synthetic monitors API v2 - Создание определения монитора Synthetic

# Synthetic monitors API v2 - Создание определения монитора Synthetic

* Справочник
* Updated on May 05, 2026

Создаёт новый монитор Synthetic.

* Метод доступен только для браузерных и NAM-мониторов. Подробнее о том, как создать браузерный или NAM-монитор в UI, смотрите [Браузерные мониторы](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors "Узнайте о браузерных мониторах.") и [Настройка NAM-монитора](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed "Узнайте, как настроить NAM-монитор и управлять им для проверки производительности и доступности вашего сайта.").
* HTTP-монитор можно создать только в UI. Подробнее смотрите [Создание HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности вашего сайта.").

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `settings.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Получение информации о синтетических узлах через Synthetic v2 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticMultiProtocolMonitorRequest](#openapi-definition-SyntheticMultiProtocolMonitorRequest) | JSON-тело запроса. Содержит параметры монитора. | body | Обязательный |

### Объекты тела запроса

#### Объект `SyntheticMultiProtocolMonitorRequest`

Монитор Network Availability.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Описание монитора | Необязательный |
| enabled | boolean | Если true, монитор включён. | Необязательный |
| frequencyMin | integer | Частота монитора, в минутах. Значение по умолчанию зависит от типа монитора (1 минута для MULTI\_PROTOCOL, 15 минут для BROWSER). | Необязательный |
| locations | string[] | Локации, которым назначен монитор. | Обязательный |
| name | string | Имя монитора. | Обязательный |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Конфигурация порогов производительности. | Необязательный |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto[]](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto) | Первичные теги Grail в виде списка пар ключ-значение. До 10 тегов. Эти поля доступны только для SaaS и не для Managed. | Необязательный |
| steps | [SyntheticMultiProtocolMonitorStepDto[]](#openapi-definition-SyntheticMultiProtocolMonitorStepDto) | Шаги монитора. | Обязательный |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Конфигурация обработки недоступности. | Необязательный |
| tags | [SyntheticTagWithSourceDto[]](#openapi-definition-SyntheticTagWithSourceDto) | Набор тегов, назначенных монитору.  Здесь можно указать только значение тега, контекст `CONTEXTLESS` и источник 'USER' будут добавлены автоматически. Но предпочтительный вариант, это использование модели SyntheticTagWithSourceDto. | Необязательный |
| type | string | Тип монитора. Поле может принимать значения: * `MULTI_PROTOCOL` * `BROWSER` | Обязательный |

#### Объект `SyntheticMonitorPerformanceThresholdsDto`

Конфигурация порогов производительности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Порог производительности включён (`true`) или отключён (`false`). | Обязательный |
| thresholds | [SyntheticMonitorPerformanceThresholdDto[]](#openapi-definition-SyntheticMonitorPerformanceThresholdDto) | Список правил порогов производительности. | Необязательный |

#### Объект `SyntheticMonitorPerformanceThresholdDto`

Правило порога производительности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации Поле может принимать значения: * `AVG` * `MAX` * `MIN` | Необязательный |
| dealertingSamples | integer | Количество самых свежих не нарушающих выполнений запроса, которое закрывает проблему. | Необязательный |
| samples | integer | Количество выполнений запроса в анализируемом скользящем окне (размер скользящего окна). | Необязательный |
| stepIndex | integer | Укажите индекс шага, к которому применяется порог. Если порог монитор-уровня, индекс не нужен. | Необязательный |
| threshold | number | Уведомлять, если запрос монитора выполняется дольше *X* единиц времени. Для мониторов Network Availability единица времени, это миллисекунды, для браузерных мониторов, секунды. | Обязательный |
| type | string | Тип порога производительности. Поле может принимать значения: * `MONITOR` * `STEP` | Необязательный |
| violatingSamples | integer | Количество нарушающих выполнений запроса в анализируемом скользящем окне. | Необязательный |

#### Объект `SyntheticMonitorPrimaryGrailTagDto`

Пара ключ-значение первичного grail-тега.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| key | string | Ключ тега. | Обязательный |
| value | string | Значение тега. | Обязательный |

#### Объект `SyntheticMultiProtocolMonitorStepDto`

Шаг монитора доступности сети.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Список ограничений, которые применяются ко всем запросам в шаге. | Обязательный |
| name | string | Имя шага. | Обязательный |
| properties | object | Свойства, которые применяются ко всем запросам в шаге. | Обязательный |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto[]](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto) | Конфигурации запросов. | Обязательный |
| requestType | string | Тип запроса. Поле может принимать значения: * `ICMP` * `TCP` * `DNS` | Обязательный |
| targetFilter | string | Фильтр целей. | Необязательный |
| targetList | string[] | Список целей. | Необязательный |

#### Объект `SyntheticMonitorConstraintDto`

Ограничение синтетического монитора.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| properties | object | Свойства ограничения. | Обязательный |
| type | string | Тип ограничения. | Обязательный |

#### Объект `SyntheticMultiProtocolRequestConfigurationDto`

Конфигурация запроса монитора доступности сети.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Ограничения запроса. | Обязательный |

#### Объект `SyntheticMonitorOutageHandlingSettingsDto`

Конфигурация обработки недоступности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев для всех локаций. | Необязательный |
| globalOutages | boolean | Создать проблему и отправить алерт, когда монитор недоступен на всех настроенных локациях. | Обязательный |
| localConsecutiveOutageCountThreshold | integer | Количество последовательных сбоев. | Необязательный |
| localLocationOutageCountThreshold | integer | Количество отказавших локаций. | Необязательный |
| localOutages | boolean | Создать проблему и отправить алерт, когда монитор недоступен в течение одного или нескольких последовательных запусков на любой локации. | Обязательный |
| origin | string | Указывает происхождение этих настроек. Поле может принимать значения: * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Необязательный |
| retryOnError | boolean | Свойство только для Browser Monitor. Если задано true, повтор выполнения произойдёт в случае сбоя монитора. | Необязательный |

#### Объект `SyntheticTagWithSourceDto`

Тег с источником отслеживаемой сущности.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. | Необязательный |
| key | string | Ключ тега. | Обязательный |
| source | string | Источник тега, например USER, RULE\_BASED или AUTO. Поле может принимать значения: * `AUTO` * `RULE_BASED` * `USER` | Необязательный |
| value | string | Значение тега. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"description": "My network availability monitor description",



"enabled": "true",



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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MonitorEntityIdDto](#openapi-definition-MonitorEntityIdDto) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MonitorEntityIdDto`

DTO для entity ID монитора.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Entity ID монитора. |

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



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1"



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