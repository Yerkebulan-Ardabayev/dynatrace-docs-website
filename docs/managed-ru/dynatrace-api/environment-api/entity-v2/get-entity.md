---
title: API отслеживаемых сущностей - GET сущность
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/entity-v2/get-entity
scraped: 2026-05-12T11:54:07.138149
---

# API отслеживаемых сущностей - GET сущность

# API отслеживаемых сущностей - GET сущность

* Справочник
* Опубликовано 28 мая 2020 г.

Возвращает полный список свойств указанной сущности. Фактический набор зависит от типа сущности.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/entities/{entityId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/entities/{entityId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `entities.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| entityId | string | ID требуемой сущности. | path | Обязательный |
| from | string | Начало запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется относительный интервал в три дня (`now-3d`). | query | Необязательный |
| to | string | Конец запрашиваемого временного интервала. Можно использовать один из форматов: * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе. Можно указать относительный интервал и без выравнивания: `now-NU`. Поддерживаемые единицы времени для относительного интервала: + `m`: минуты + `h`: часы + `d`: дни + `w`: недели + `M`: месяцы + `y`: годы Если не задан, используется текущая метка времени. | query | Необязательный |
| fields | string | Определяет список свойств сущности, включаемых в ответ. ID и имя сущности **всегда** включаются в ответ. Чтобы добавить свойства, перечислите их с ведущим плюсом `+`. Можно указать несколько свойств через запятую (например `fields=+lastSeenTms,+properties.BITNESS`). Чтобы получить список доступных свойств для вашего типа сущности, используйте запрос [GET entity type](https://dt-url.net/2ka3ivt). Поля из объекта **properties** должны указываться в формате `properties.FIELD` (например, `properties.BITNESS`). При запросе большого количества полей-связей возможно троттлинг (ограничение скорости). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Entity](#openapi-definition-Entity) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Entity`

Свойства отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| displayName | string | Имя сущности, отображаемое в UI. |
| entityId | string | ID сущности. |
| firstSeenTms | integer | Метка времени, когда сущность была впервые увидена, в UTC миллисекундах. |
| fromRelationships | object | Список связей, в которых сущность занимает позицию FROM. |
| icon | [EntityIcon](#openapi-definition-EntityIcon) | Иконка отслеживаемой сущности. |
| lastSeenTms | integer | Метка времени последнего наблюдения сущности, в UTC миллисекундах. |
| managementZones | [EnrichedManagementZoneDto[]](#openapi-definition-EnrichedManagementZoneDto) | Набор зон управления, к которым относится сущность. |
| properties | object | Список дополнительных свойств сущности. |
| tags | [EnrichedTagDto[]](#openapi-definition-EnrichedTagDto) | Набор тегов, присвоенных сущности. |
| toRelationships | object | Список связей, в которых сущность занимает позицию TO. |
| type | string | Тип сущности. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `EntityIcon`

Иконка отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| customIconPath | string | Пользовательская иконка сущности. Укажите [barista](https://dt-url.net/u403suy) ID иконки или URL вашей собственной иконки. |
| primaryIconType | string | Основная иконка сущности. Указывается [barista](https://dt-url.net/u403suy) ID иконки. |
| secondaryIconType | string | Вторичная иконка сущности. Указывается [barista](https://dt-url.net/u403suy) ID иконки. |

#### Объект `EnrichedManagementZoneDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |
| sourceSetting | string | Путь к объекту настроек в Settings API. |

#### Объект `EnrichedTagDto`

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| source | string | Источник, откуда пришёл тег. Возможные значения: * Auto tags * Environment tags * User provided tags |
| sourceSetting | string | Путь к объекту настроек в Settings API. Доступно только для тегов с источником Auto tags. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"displayName": "my host",



"entityId": "HOST-06F288EE2A930951",



"firstSeenTms": 1574697667547,



"fromRelationships": {



"isInstanceOf": [



{



"id": "HOST_GROUP-0E489369D663A4BF",



"type": "HOST_GROUP"



}



]



},



"icon": {



"customIconPath": "host",



"primaryIconType": "linux",



"secondaryIconType": "microsoft-azure-signet"



},



"lastSeenTms": 1588242361417,



"managementZones": [



{



"id": "6239538939987181652",



"name": "main app"



}



],



"properties": {



"bitness": 64,



"cpuCores": 8,



"monitoringMode": "FULL_STACK",



"networkZoneId": "aws.us.east01",



"osArchitecture": "X86",



"osType": "LINUX"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "architecture",



"stringRepresentation": "architecture:x86",



"value": "x86"



},



{



"context": "ENVIRONMENT",



"key": "Infrastructure",



"stringRepresentation": "[ENVIRONMENT]Infrastructure:Linux",



"value": "Linux"



}



],



"toRelationships": {



"isDiskOf": [



{



"id": "DISK-0393340DCA3853B0",



"type": "DISK"



}



]



},



"type": "HOST"



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

В этом примере запрос выводит свойства сервиса **dotNetBackend\_easyTravel\_x64** с ID **SERVICE-1125C375A187D27A**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/entities/SERVICE-1125C375A187D27A' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/entities/SERVICE-1125C375A187D27A
```

#### Тело ответа

```
{



"entityId": "SERVICE-1125C375A187D27A",



"displayName": "dotNetBackend_easyTravel_x64",



"firstSeenTms": 1424310498896,



"lastSeenTms": 1590609632865,



"properties": {



"serviceType": "WEB_REQUEST_SERVICE",



"internalName": "dotNetBackend_easyTravel_x64",



"webServerName": "dotNetBackend_easyTravel_x64",



"softwareTechnologies": [



{



"edition": "FullCLR",



"version": "2.0.50727"



},



{



"type": "DOTNET",



"edition": ".NET Framework",



"version": "3.5.1.0"



},



{



"type": "ADO_NET",



"edition": "System.Data",



"version": "2.0.50727.8751"



},



{



"type": "ASP_DOTNET",



"version": "3.5.1.0"



},



{



"type": "IIS_APP_POOL",



"version": "10.0.14393.0"



},



{



"type": "DOTNET_REMOTING",



"version": "2.0.50727.8771"



}



],



"serviceTechnologyTypes": [



"IIS app pool",



"ASP.NET",



"DotNet"



],



"mainServiceSoftwareTech": {



"type": "ASP_DOTNET"



},



"contextRoot": "/",



"agentTechnologyType": "DOTNET"



},



"tags": [



{



"context": "CONTEXTLESS",



"key": "customService",



"stringRepresentation": "customService"



},



{



"context": "CONTEXTLESS",



"key": "easytravel",



"value": "backend",



"stringRepresentation": "easytravel:backend",



"source": "Auto tags",



"sourceSetting": "api/v2/settings/objects/vu9U3hXa3q0AAAABABlidWlsdGluOnRhZ3MuYXV0by10YWdnaW5nAAZ0ZW5hbnQABnRlbmFudAAkNGQ5YTFhMTUtZmY1ZS0zNDE5LWE2MDUtOTlmOWJkZTFhODNmvu9U3hXa3q0"



}



],



"mangementZones": [



{



"id": "2827032493241090264",



"name": "allServices"



},



{



"id": "9130632296508575249",



"name": "Easytravel",



"sourceSetting": "api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOm1hbmFnZW1lbnQtem9uZXMABnRlbmFudAAGdGVuYW50ACQ1MTNkNWNkMC0zZjEyLTNiOTUtODZlMi05YjU4ODk0ODM4MWO-71TeFdrerQ"



}



],



"fromRelationships": {



"calls": [



{



"id": "SERVICE-775060208AAA1058",



"type": "SERVICE"



},



{



"id": "SERVICE-6737CDED8F9BF969",



"type": "SERVICE"



}



],



"runsOn": [



{



"id": "PROCESS_GROUP-0A9A52EA262BC039",



"type": "PROCESS_GROUP"



}



],



"runsOnHost": [



{



"id": "HOST-B64B6B9CB11E2244",



"type": "HOST"



},



{



"id": "HOST-CF61BC45E6282234",



"type": "HOST"



}



],



"runsOnProcessGroupInstance": [



{



"id": "PROCESS_GROUP_INSTANCE-DE765F657721AF59",



"type": "PROCESS_GROUP_INSTANCE"



}



]



},



"toRelationships": {



"calls": [



{



"id": "SERVICE-D20E300A0A6814EF",



"type": "SERVICE"



},



{



"id": "SERVICE-7675DAA7464128F8",



"type": "SERVICE"



}



]



}



}
```

#### Код ответа

200

## Связанные темы

* [API пользовательских тегов](/managed/dynatrace-api/environment-api/custom-tags "Управляйте пользовательскими тегами отслеживаемых сущностей через Dynatrace API.")