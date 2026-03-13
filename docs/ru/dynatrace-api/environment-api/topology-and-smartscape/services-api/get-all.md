---
title: Services API - GET all services
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all
scraped: 2026-03-05T21:26:48.257759
---

# Services API - GET всех сервисов

# Services API - GET всех сервисов

* Справочник
* Обновлено 22 марта 2023
* Устарело

Этот API устарел. Используйте вместо него [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API."). Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Перенесите автоматизацию на Monitored entities API.").

Получает список всех сервисов в вашей среде Dynatrace вместе с их параметрами и связями.

Полный список может быть обширным, поэтому вы можете сузить его, указав параметры фильтрации, например теги. Подробности см. в разделе **Parameters**.

Вы также можете ограничить вывод, используя пагинацию:

1. Укажите количество результатов на страницу в параметре запроса **pageSize**.
2. Затем используйте курсор из заголовка ответа **Next-Page-Key** в параметре запроса **nextPageKey** для получения последующих страниц.

Запрос создаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services` |

## Аутентификация

Для выполнения этого запроса вам нужен токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Временной диапазон ограничен **максимальным периодом в 3 дня**.

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Начальная временная метка запрашиваемого временного диапазона в миллисекундах (UTC).  Если не задана, используется значение 72 часа назад от текущего момента. | query | Необязательный |
| endTimestamp | integer | Конечная временная метка запрашиваемого временного диапазона в миллисекундах (UTC).  Если не задана, используется текущая временная метка.  Временной диапазон не должен превышать 3 дня. | query | Необязательный |
| relativeTime | string | Относительный временной диапазон от текущего момента назад. Элемент может содержать следующие значения: * `min` * `5mins` * `10mins` * `15mins` * `30mins` * `hour` * `2hours` * `6hours` * `day` * `3days` | query | Необязательный |
| tag | string[] | Фильтрует результирующий набор сервисов по указанному тегу. Вы можете указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Сервис должен соответствовать **всем** указанным тегам.  Для тегов «ключ-значение», таких как импортированные теги AWS или CloudFoundry, используйте следующий формат: `tag=[context]key:value`. Для пользовательских тегов «ключ-значение» опустите контекст: `tag=key:value`. | query | Необязательный |
| entity | string[] | Фильтрует результат, оставляя только указанные сервисы.  Чтобы указать несколько сервисов, используйте следующий формат: `entity=ID1&entity=ID2`. | query | Необязательный |
| managementZone | integer | Возвращать только сервисы, входящие в указанную зону управления. | query | Необязательный |
| includeDetails | boolean | Включает (`true`) или исключает (`false`) детали, запрашиваемые из связанных сущностей.  Исключение деталей может ускорить запросы.  Если не задано, используется `true`. | query | Необязательный |
| pageSize | integer | Количество сервисов на страницу результатов.  Если не задано, пагинация не используется и результат содержит все сервисы, соответствующие указанным критериям фильтрации. | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в заголовке **Next-Page-Key** предыдущего ответа.  При использовании пагинации первая страница всегда возвращается без этого курсора.  Необходимо сохранять все остальные параметры запроса такими же, как в первом запросе, для получения последующих страниц. | query | Необязательный |

## Заголовки ответа

| Заголовок | Тип | Описание |
| --- | --- | --- |
| Total-Count | integer | Приблизительное количество результатов. |
| Next-Page-Key | string | Курсор для следующей страницы результатов. Без него вы получите первую страницу снова. |
| Page-Size | string | Максимальное количество результатов на странице. |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Service[]](#openapi-definition-Service) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Недопустимые входные данные. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Service`

| Элемент | Тип | Описание |
| --- | --- | --- |
| agentTechnologyType | string | -Элемент может содержать следующие значения: * `APACHE` * `DOTNET` * `DUMPPROC` * `GO` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `N/A` * `NET` * `NETTRACER` * `NGINX` * `NODEJS` * `OPENTRACINGNATIVE` * `OS` * `PHP` * `PLUGIN` * `PROCESS` * `PYTHON` * `REMOTE_PLUGIN` * `RUBY` * `SDK` * `UPDATER` * `VARNISH` * `WSMB` * `Z` |
| akkaActorSystem | string | Сервисы системы акторов akka. |
| className | string | - |
| contextRoot | string | - |
| customizedName | string | Пользовательское имя сущности |
| databaseHostNames | string[] | - |
| databaseName | string | - |
| databaseVendor | string | - |
| discoveredName | string | Обнаруженное имя сущности |
| displayName | string | Имя сущности Dynatrace, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace для требуемой сущности. |
| esbApplicationName | string | Имя приложения ESB. |
| firstSeenTimestamp | integer | Временная метка первого обнаружения сущности, в миллисекундах UTC |
| fromRelationships | object | - |
| ibmCtgGatewayUrl | string | URL шлюза IBM CTG. |
| ibmCtgServerName | string | Имя IBM CICS Transaction Gateway. |
| iibApplicationName | string | Имя приложения IIB. |
| ipAddresses | string[] | - |
| isExternalService | boolean | - |
| lastSeenTimestamp | integer | Временная метка последнего обнаружения сущности, в миллисекундах UTC |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Зоны управления, к которым относится сущность. |
| path | string | - |
| port | integer | - |
| publicDomainName | object | Публичное доменное имя. |
| remoteEndpoint | string | Конечная точка удалённого сервиса. |
| remoteServiceName | string | Имя удалённого сервиса. |
| serviceDetectionAttributes | object | Атрибуты, которые участвовали в определении идентификатора сервиса. |
| serviceTechnologyTypes | string[] | - |
| serviceType | string | -Элемент может содержать следующие значения: * `Cics` * `CicsInteraction` * `CustomApplication` * `Database` * `EnterpriseServiceBus` * `External` * `Ims` * `ImsInteraction` * `Messaging` * `Method` * `Mobile` * `Process` * `QueueInteraction` * `QueueListener` * `RemoteCall` * `Rmi` * `SaasVendor` * `Span` * `Unified` * `Unknown` * `WebRequest` * `WebService` * `WebSite` * `ZosConnect` |
| softwareTechnologies | [TechnologyInfo[]](#openapi-definition-TechnologyInfo) | - |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов сущности. |
| toRelationships | object | - |
| webApplicationId | string | - |
| webServerName | string | - |
| webServiceName | string | - |
| webServiceNamespace | string | - |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | Идентификатор сущности Dynatrace. |
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
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может содержать следующие значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  Для пользовательских тегов здесь содержится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
[



{



"agentTechnologyType": "APACHE",



"akkaActorSystem": "string",



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

В этом примере запрос выводит список всех сервисов среды, обнаруженных **за последние 5 минут**.

Токен API передаётся в заголовке **Authorization**.

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

* [Сервисы](/docs/observe/application-observability/services "Узнайте, как отслеживать и анализировать сервисы, определять и использовать атрибуты запросов и многое другое.")