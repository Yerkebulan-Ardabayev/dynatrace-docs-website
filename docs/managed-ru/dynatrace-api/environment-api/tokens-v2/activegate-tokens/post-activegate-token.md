---
title: ActiveGate tokens API - POST токена
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token
scraped: 2026-05-12T12:09:53.794174
---

# ActiveGate tokens API - POST токена

# ActiveGate tokens API - POST токена

* Reference
* Published Dec 02, 2021

Создаёт новый ActiveGate-токен.

Владельцем токена становится пользователь, которому принадлежит токен, использованный для аутентификации вызова.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGateTokens` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGateTokens` |

## Аутентификация

Для выполнения запроса необходим access token с одним из следующих scope:

* `activeGateTokenManagement.create`
* `activeGateTokenManagement.write`

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [ActiveGateTokenCreate](#openapi-definition-ActiveGateTokenCreate) | JSON-тело запроса. Содержит параметры нового ActiveGate-токена. | body | Обязательный |

### Объекты тела запроса

#### Объект `ActiveGateTokenCreate`

Параметры нового ActiveGate-токена.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| activeGateType | string | Тип ActiveGate, для которого действителен токен. Элемент может принимать значения * `ENVIRONMENT` * `CLUSTER` | Обязательный |
| expirationDate | string | Дата истечения срока действия токена.  Можно использовать один из следующих форматов:  * Временная метка в UTC-миллисекундах. * Человеко-читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный временной интервал, отсчитываемый назад от текущего момента. Формат: `now-NU/A`, где `N` это объём времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад, выравненный по неделе.   Относительный интервал можно задавать и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, токен не истекает.  Убедитесь, что значение не задано в прошлом и не превышает `2 года` с момента создания." | Опциональный |
| name | string | Имя токена. | Обязательный |
| seedToken | boolean | Токен является seed-токеном (`true`) или индивидуальным токеном (`false`).  Рекомендуется использовать вариант индивидуального токена (false). | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
{



"activeGateType": "ENVIRONMENT",



"expirationDate": "now+6M",



"name": "myToken",



"seedToken": false



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [ActiveGateTokenCreated](#openapi-definition-ActiveGateTokenCreated) | Успех. Токен создан. Тело ответа содержит секрет токена. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateTokenCreated`

Только что созданный ActiveGate-токен.

| Элемент | Тип | Описание |
| --- | --- | --- |
| expirationDate | string | Дата истечения срока действия токена в формате ISO 8601 (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| id | string | Идентификатор ActiveGate-токена, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg?dt=m) токена. |
| token | string | Секрет токена. |

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



"expirationDate": "2020-11-24T08:15:30.144Z",



"id": "dt0g02.4KWZO5EF",



"token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E"



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

В этом примере запрос создаёт новый ActiveGate-токен для environment ActiveGate. Токен действителен в течение двух недель (14 дней) с момента создания.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "REST test",



"expirationDate": "now+14d",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com//api/v2/activeGateTokens
```

#### Тело запроса

```
{



"name": "REST test",



"expirationDate": "now+14d",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}
```

#### Тело ответа

```
{



"id": "dt0g02.xyz789",



"token": "dt0g02.xyz789.987654321zyxwvutsrq",



"expirationDate": "2021-12-14T13:42:31.148Z"



}
```

#### Код ответа

201

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные понятия, связанные с ActiveGate.")