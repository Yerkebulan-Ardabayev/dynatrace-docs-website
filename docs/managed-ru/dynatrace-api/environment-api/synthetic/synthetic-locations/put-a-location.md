---
title: Synthetic locations API - PUT локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/put-a-location
scraped: 2026-05-12T11:56:58.090740
---

# Synthetic locations API - PUT локация

# Synthetic locations API - PUT локация

* Справочник
* Опубликовано 26 июля 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Обновляет существующую **приватную** синтетическую локацию.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `ExternalSyntheticIntegration`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Узнайте о вариациях моделей в Synthetic locations v1 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID обновляемой синтетической локации. | path | Обязательный |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | JSON-тело запроса. Содержит обновлённые параметры приватной синтетической локации или статус локации. | body | Необязательный |

### Объекты тела запроса

#### Объект `SyntheticLocationUpdate`

Обновление синтетической локации. Точный объект зависит от **type** локации.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> PrivateSyntheticLocationUpdate Поле может принимать значения: * `PRIVATE` * `PUBLIC` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"latitude": 48.306351,



"longitude": 14.287399,



"name": "Linz Location",



"nodes": [



"93302281"



],



"status": "ENABLED",



"type": "PRIVATE"



}
```

## Ответ

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID обновляемой синтетической локации. | path | Обязательный |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | JSON-тело запроса. Содержит обновлённые параметры приватной синтетической локации или статус локации. | body | Необязательный |

### Объекты тела запроса

#### Объект `SyntheticLocationUpdate`

Обновление синтетической локации. Точный объект зависит от **type** локации.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> PrivateSyntheticLocationUpdate Поле может принимать значения: * `PRIVATE` * `PUBLIC` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"latitude": 48.306351,



"longitude": 14.287399,



"name": "Linz Location",



"nodes": [



"93302281"



],



"status": "ENABLED",



"type": "PRIVATE"



}
```

## Пример

В этом примере запрос обновляет приватную синтетическую локацию из [примера POST-запроса](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/post-a-location#example "Создание приватной синтетической локации через Synthetic v1 API."). Он меняет имя локации на **Linz** и добавляет синтетический узел с ID **353074222**.

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает, что обновление прошло успешно.

Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно замените список узлов на узлы, доступные в вашем окружении.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-8F419D1B53639A45 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"93302281",



"353074222"



]



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-8F419D1B53639A45
```

#### Тело запроса

```
{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["93302281", "353074222"]



}
```

#### Код ответа

204

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")