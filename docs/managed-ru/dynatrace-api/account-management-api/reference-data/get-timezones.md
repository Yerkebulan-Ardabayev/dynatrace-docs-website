---
title: Reference data API - GET time zones
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/reference-data/get-timezones
scraped: 2026-05-12T11:24:40.979212
---

# Reference data API - GET time zones

# Reference data API - GET time zones

* Reference
* Published Jul 25, 2022

Возвращает все часовые пояса, которые использует ваш аккаунт.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/ref/v1/time-zones` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for environment resources** (`account-env-read`). О том, как его получить и использовать.

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TimeZoneDto[]](#openapi-definition-TimeZoneDto) | Успех. Тело ответа содержит список часовых поясов. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `TimeZoneDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Имя часового пояса в формате UTC. |
| name | string | Стандартное имя часового пояса. |

### JSON-модели тела ответа

```
[



{



"displayName": "string",



"name": "string"



}



]
```

## Пример

В этом примере запрос возвращает все часовые пояса аккаунта с UUID **9ad20784-76c6-4167-bfba-9b0d8d72a71d**. Результат обрезан до трёх записей.

#### Curl

```
curl --request GET \



--url https://api.dynatrace.com/ref/v1/time-zones \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/ref/v1/time-zones
```

#### Тело ответа

```
[



{



"displayName": "UTC+00:00 Universal Time Coordinated",



"name": "UTC"



},



{



"displayName": "UTC-07:00 Arizona",



"name": "America/Arizona"



},



{



"displayName": "UTC+01:00 Central European Time",



"name": "Europe/Berlin"



}



]
```

#### Код ответа

200