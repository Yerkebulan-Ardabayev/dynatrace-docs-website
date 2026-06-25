---
title: Reference data API - GET geographical regions
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/reference-data/get-regions
scraped: 2026-05-12T11:24:42.135733
---

# Reference data API - GET geographical regions

# Reference data API - GET geographical regions

* Reference
* Published Jul 25, 2022

Возвращает все географические регионы, которые использует ваш аккаунт.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/ref/v1/regions` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for environment resources** (`account-env-read`). О том, как его получить и использовать.

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RegionDto[]](#openapi-definition-RegionDto) | Успех. Тело ответа содержит список регионов. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `RegionDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя региона. |

### JSON-модели тела ответа

```
[



{



"name": "string"



}



]
```

## Пример

В этом примере запрос возвращает все регионы аккаунта с UUID **9ad20784-76c6-4167-bfba-9b0d8d72a71d**. Результат обрезан до двух записей.

#### Curl

```
curl --request GET \



--url https://api.dynatrace.com/ref/v1/regions \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/ref/v1/regions
```

#### Тело ответа

```
[



{



"name": "US East Virginia"



},



{



"name": "US West Oregon"



}



]
```

#### Код ответа

200