---
title: Events API v1 - POST событие
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/post-event
scraped: 2026-05-12T12:13:40.104293
---

# Events API v1 - POST событие

# Events API v1 - POST событие

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2.").

Отправляет пользовательские события из сторонних интеграций к одной или нескольким наблюдаемым сущностям.

Этот эндпоинт позволяет сторонним системам, таким как CI-платформы (Jenkins, Bamboo, Electric Cloud и т.д.), предоставлять дополнительные сведения для автоматического анализа первопричин Dynatrace.

Этот эндпоинт можно использовать для того, чтобы:

* Отправлять только информационные события из сторонних систем для предоставления дополнительной информации для автоматического анализа первопричин Dynatrace. Время закрытия события уже известно, и ID событий возвращаются мгновенно. Эти события можно отправлять с давностью до **30 дней** в прошлое. Типы только информационных событий:

  + `CUSTOM_ANNOTATION`
  + `CUSTOM_CONFIGURATION`
  + `CUSTOM_DEPLOYMENT`
  + `CUSTOM_INFO`
  + `MARKED_FOR_TERMINATION`
* Отправлять события, открывающие проблему (например, рост частоты ошибок), чтобы запустить движок автоматического анализа первопричин Dynatrace. Вместо ID событий возвращаются correlation ID. Эти события остаются открытыми, пока не истечёт указанный тайм-аут. Чтобы предотвратить истечение, эти события можно обновлять, отправляя тот же payload снова. Эти события можно отправлять с давностью до **60 минут** в прошлое. Типы событий, открывающих проблему (отсортированы от наивысшей к наименьшей критичности):

  + `AVAILABILITY_EVENT`
  + `ERROR_EVENT`
  + `PERFORMANCE_EVENT`
  + `RESOURCE_CONTENTION`

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/events` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Набор параметров зависит от типа события. Подробности смотрите в [**Сопоставление параметров**](#parameters-mapping) ниже.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [EventCreation](#openapi-definition-EventCreation) | JSON-тело запроса, содержащее параметры события. | body | Необязательный |

### Объекты тела запроса

#### Объект `EventCreation`

Конфигурация пользовательского события.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowDavisMerge | boolean | Разрешить Davis AI объединять это событие с существующими проблемами (true) или принудительно создавать новую проблему (false).  Применяется только к типам событий, открывающих проблему. | Необязательный |
| annotationDescription | string | Подробное описание пользовательской аннотации, например `DNS route has been changed to x.mydomain.com`. | Необязательный |
| annotationType | string | Тип пользовательской аннотации, например `DNS route has been changed`. | Необязательный |
| attachRules | [PushEventAttachRules](#openapi-definition-PushEventAttachRules) | Набор правил, определяющих сущности Dynatrace для связывания с событием.  Можно указать теги для динамического сопоставления сущностей Dynatrace или ID конкретных сущностей.  Требуется хотя бы один ID сущности или тег. | Обязательный |
| changed | string | Новое значение конфигурации, установленное событием. | Необязательный |
| ciBackLink | string | Ссылка на развёрнутый артефакт в сторонней системе. | Необязательный |
| configuration | string | ID или имя конфигурации, изменённой событием. | Необязательный |
| customProperties | object | Набор любых свойств, связанных с событием, в формате *"key" : "value"*. | Необязательный |
| deploymentName | string | ID запущенного развёртывания. | Необязательный |
| deploymentProject | string | Имя проекта развёрнутого пакета. | Необязательный |
| deploymentVersion | string | Версия запущенного развёртывания. | Необязательный |
| description | string | Текстовое описание изменения конфигурации. | Необязательный |
| end | integer | Конечная метка времени события, в миллисекундах UTC.  Если не задано, для только информационных событий используется текущее время.  Не применимо к событиям, открывающим проблему. Такое событие остаётся открытым, пока не истечёт тайм-аут в зависимости от параметра **timeoutMinutes**. | Необязательный |
| eventType | string | Тип события. Элемент может принимать значения * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION` | Обязательный |
| original | string | Предыдущее значение конфигурации. | Необязательный |
| remediationAction | string | Ссылка на действие по устранению, связанное с развёртыванием, во внешнем инструменте. | Необязательный |
| source | string | Имя или ID внешнего источника события. | Обязательный |
| start | integer | Начальная метка времени события, в миллисекундах UTC.  Если не задано, используется текущая метка времени.  Только информационные события можно сообщать с давностью до **30 дней** в прошлое.  События, открывающие проблему, можно сообщать с давностью до **60 минут** в прошлое. | Необязательный |
| timeoutMinutes | integer | Тайм-аут для событий, открывающих проблему, в минутах. Не применимо к только информационным событиям.  Если не задано, используется 15 минут. Максимально допустимое значение: 120 минут.  Событие можно обновить, отправив тот же payload снова. | Необязательный |
| timeseriesIds | string[] | Список ID временных рядов, связанных с событием. | Необязательный |
| title | string | Заголовок конфигурации, установленной событием. | Необязательный |

#### Объект `PushEventAttachRules`

Набор правил, определяющих сущности Dynatrace для связывания с событием.

Можно указать теги для динамического сопоставления сущностей Dynatrace или ID конкретных сущностей.

Требуется хотя бы один ID сущности или тег.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| entityIds | string[] | Список ID сущностей, к которым должно быть прикреплено событие. | Необязательный |
| tagRule | [TagMatchRule[]](#openapi-definition-TagMatchRule) | Набор правил сопоставления для динамического выбора сущностей на основе тегов.  Для правил сопоставления на основе тегов учитываются только сущности, наблюдавшиеся за последние **24 часа**. | Необязательный |

#### Объект `TagMatchRule`

Список тегов для сопоставления сущностей Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| meTypes | string[] | Список типов сущностей Dynatrace (например, хостов или сервисов), которые вы хотите выбрать сопоставлением. Элемент может принимать значения * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` | Обязательный |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов, которые вы хотите использовать для сопоставления. Требуется хотя бы один тег.  Можно использовать пользовательские теги из UI, импортированные теги и теги на основе переменных окружения. | Обязательный |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Обязательный |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. | Обязательный |
| value | string | Значение тега.  Не применимо к пользовательским тегам. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
{



"annotationDescription": "The coffee machine is broken",



"annotationType": "defect",



"attachRules": {



"entityIds": [



"CUSTOM_DEVICE-0000000000000007"



],



"tagRule": [



{



"meTypes": [



"HOST"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "customTag"



}



]



}



]



},



"end": 1521542929000,



"eventType": "CUSTOM_ANNOTATION",



"source": "OpsControl",



"start": 1521042929000



}
```

### Сопоставление параметров

|  | Событие доступности | Пользовательская аннотация | Пользовательская конфигурация | Пользовательское развёртывание | Пользовательская информация | Событие ошибки | Событие производительности | Конкуренция за ресурсы | Помечено на завершение |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| description | req | opt | req | n/a | req | req | req | req | req |
| title | req | n/a | n/a | n/a | opt | req | req | req | opt |
| source | req | req | req | req | req | req | req | req | req |
| annotationType | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| annotationDescription | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| deploymentName | n/a | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a |
| deploymentVersion | n/a | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a |
| deploymentProject | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a |
| ciBackLink | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | opt |
| remediationAction | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a |
| original | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a | n/a |
| configuration | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a |
| customProperties | opt | opt | opt | opt | opt | opt | opt | opt | opt |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventStoreResult](#openapi-definition-EventStoreResult) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventStoreResult`

Содержит ID всех пользовательских событий, созданных вызовом отправки события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| storedCorrelationIds | string[] | Список correlation ID для событий, открывающих проблему. |
| storedEventIds | integer[] | Список ID событий для только информационных событий.  Это поле предоставлено для совместимости. Вместо него следует использовать значения из поля **storedIds**. |
| storedIds | string[] | Список **закодированных** ID событий для только информационных событий. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"storedCorrelationIds": [



"string"



],



"storedEventIds": [



1



],



"storedIds": [



"string"



]



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

## Пример

В этом примере запрос отправляет событие **CUSTOM\_ANNOTATION**, которое применяется ко всем пользовательским устройствам с тегом **Coffee-2nd-floor**. Эта аннотация это уведомление о том, что эти кофемашины сломаны.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/events \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"eventType": "CUSTOM_ANNOTATION",



"timeoutMinutes": 0,



"attachRules": {



"tagRule": [



{



"meTypes": [



"CUSTOM_DEVICE"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "IG-test"



}



]



}



]



},



"source": "OpsControl",



"annotationType": "defect",



"annotationDescription": "coffee machine is defective"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/events
```

#### Тело запроса

```
{



"eventType": "CUSTOM_ANNOTATION",



"timeoutMinutes": 0,



"attachRules": {



"tagRule": [



{



"meTypes": ["CUSTOM_DEVICE"],



"tags": [



{



"context": "CONTEXTLESS",



"key": "IG-test"



}



]



}



]



},



"source": "OpsControl",



"annotationType": "defect",



"annotationDescription": "coffee machine is defective"



}
```

#### Тело ответа

```
{



"storedEventIds": [



-6153476110846051426



],



"storedIds": [



"-6153476110846051426_1533300519291"



],



"storedCorrelationIds": []



}
```

#### Код ответа

200

## Связанные темы

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий, поддерживаемых типах событий, уровнях критичности и логике их формирования.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Понимание секции Events на странице обзора хостов, процессов и сервисов.")
* [Creating a deployment event via the Dynatrace API](https://www.youtube.com/watch?v=LDAiUMdrtvA)