---
title: Services API - GET all services
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all
scraped: 2026-05-12T12:02:11.343542
---

# Services API - GET all services

# Services API - GET all services

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

Получает список всех сервисов в вашем окружении Dynatrace вместе с их параметрами и связями.

Полный список может быть длинным, поэтому его можно сузить, указав параметры фильтрации, например теги. Подробнее см. в разделе **Parameters**.

Дополнительно можно ограничить вывод с помощью постраничной разбивки:

1. Укажите количество результатов на странице в query-параметре **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в query-параметре **nextPageKey**, чтобы получить следующие страницы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/services` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Временной диапазон ограничен **максимальным периодом в 3 дня**.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется 72 часа назад от текущего момента. | query | Optional |
| endTimestamp | integer | Конечная метка времени запрашиваемого диапазона, в миллисекундах (UTC).  Если не задана, используется текущая метка времени.  Диапазон не должен превышать 3 дня. | query | Optional |
| relativeTime | string | Относительный диапазон, назад от текущего момента. Возможные значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Optional |
| tag | string[] | Фильтрует результирующий набор сервисов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Сервис должен соответствовать **всем** указанным тегам.  В случае тегов key-value, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов key-value опустите context: `tag=key:value`. | query | Optional |
| entity | string[] | Ограничивает результат только указанными сервисами.  Чтобы указать несколько сервисов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Optional |
| managementZone | integer | Возвращать только сервисы, входящие в указанную management zone. | query | Optional |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые у связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Optional |
| pageSize | integer | Количество сервисов на странице результатов.  Если не задано, постраничная разбивка не используется и результат содержит все сервисы, подходящие под указанные критерии фильтрации. | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  Если вы используете постраничную разбивку, первая страница всегда возвращается без этого курсора.  Чтобы получить следующие страницы, нужно сохранить все остальные query-параметры такими, как в первом запросе. | query | Optional |

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Оценочное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него снова вернётся первая страница. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Service[]](#openapi-definition-Service) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Service`

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentTechnologyType | string | -Возможные значения: * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | Сервисы системы акторов akka. |
| attributes | object | - |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | Пользовательское имя сущности |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace в том виде, как оно отображается в UI. |
| entityId | string | ID сущности Dynatrace для нужной сущности. |
| esbApplicationName | string | Имя ESB-приложения. |
| firstSeenTimestamp | integer | Метка времени, когда сущность была впервые обнаружена, в миллисекундах UTC |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | URL шлюза IBM CTG. |
| ibmCtgServerName | string | Имя IBM CICS Transaction Gateway. |
| iibApplicationName | string | Имя IIB-приложения. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | Метка времени, когда сущность была обнаружена в последний раз, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Management zone'ы, частью которых является сущность. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Публичное доменное имя. |
| remoteEndpoint | string | Endpoint удалённого сервиса. |
| remoteServiceName | string | Имя удалённого сервиса. |
| serviceDetectionAttributes | object | Атрибуты, повлиявшие на service id. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -Возможные значения: * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TechnologyInfo`

| Элемент | Тип | Описание |
| --- | --- | --- |
| edition | string | - |
| type | string | - |
| version | string | - |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
[



{



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



"attributes": {



"empty": true



},



"className": "string",



"contextRoot": "string",



"customizedName": "string",



"databaseHostNames": [



"string"



],



"databaseName": "string",



"databaseVendor": "string",



"discoveredName": "string",



"displayName": "string",



"entityId": "string",



"esbApplicationName": "string",



"firstSeenTimestamp": 1,



"fromRelationships": {



"calls": [



"string"



],



"runsOn": [



"string"



],



"runsOnProcessGroupInstance": [



"string"



]



},



"ibmCtgGatewayUrl": "string",



"ibmCtgServerName": "string",



"iibApplicationName": "string",



"ipAddresses": [



"string"



],



"isExternalService": true,



"lastSeenTimestamp": 1,



"managementZones": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"path": "string",



"port": 1,



"publicDomainName": {},



"remoteEndpoint": "string",



"remoteServiceName": "string",



"serviceDetectionAttributes": {},



"serviceTechnologyTypes": [



"string"



],



"serviceType": "Cics",



"softwareTechnologies": [



{



"edition": "string",



"type": "string",



"version": "string"



}



],



"tags": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"toRelationships": {



"calls": [



"string"



]



},



"webApplicationId": "string",



"webServerName": "string",



"webServiceName": "string",



"webServiceNamespace": "string"



}



]
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

В этом примере запрос выводит список всех сервисов окружения, обнаруженных **за последние 5 минут**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/entity/services?relativeTime=5mins' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/services?relativeTime=5mins
```

#### Тело ответа

```
[



{



"entityId": "SERVICE-72503CBDD2AEF066",



"displayName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"discoveredName": "PHP-FPM via domain socket /run/php7-fpm.sock",



"firstSeenTimestamp": 1505902015554,



"lastSeenTimestamp": 1544025169570,



"tags": [



{



"context": "CONTEXTLESS",



"key": "Sample tag"



}



],



"fromRelationships": {



"runsOnProcessGroupInstance": [



"PROCESS_GROUP_INSTANCE-165E2E1655782C30",



"PROCESS_GROUP_INSTANCE-2E41AD6095ACE67B",



"PROCESS_GROUP_INSTANCE-3E537F0F455E9757"



],



"runsOn": [



"PROCESS_GROUP-E5C3CC7EC1F80B5B"



]



},



"toRelationships": {



"calls": [



"SERVICE-5304CCF4AFBFF35E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest",



"softwareTechnologies": [



{



"type": "SQLITE",



"edition": null,



"version": null



},



{



"type": "PHP",



"edition": "FPM",



"version": "7.0.32"



},



{



"type": "PHP_FPM",



"edition": null,



"version": null



}



]



},



{



"entityId": "SERVICE-52AC624D70C377BC",



"displayName": "Requests to public networks",



"discoveredName": "Requests to public networks",



"firstSeenTimestamp": 1421376505750,



"lastSeenTimestamp": 1544025153570,



"tags": [],



"fromRelationships": {},



"toRelationships": {



"calls": [



"SERVICE-635F6C4CAD07BC56",



"SERVICE-74C7ACD74FA27688",



"SERVICE-C7790E5EDD1F895E"



]



},



"agentTechnologyType": "N/A",



"serviceType": "WebRequest"



}



]
```

#### Код ответа

200

## Связанные темы

* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")