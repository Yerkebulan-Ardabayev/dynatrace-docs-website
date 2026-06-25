---
title: Disk events anomaly detection API - DELETE an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/del-event
scraped: 2026-05-12T11:20:22.293650
---

# Disk events anomaly detection API - DELETE an event

# Disk events anomaly detection API - DELETE an event

* Reference
* Published Aug 29, 2019

Удаляет указанное правило disk event.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого правила disk event. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Правило disk event удалено. Ответ без тела. |

## Пример

В этом примере запрос удаляет правило **very slow disk**, созданное в примере [POST request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event#example "Создание правила disk event через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/fdd83212-9c08-44ba-a0cf-dbb471cd819a \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents/fdd83212-9c08-44ba-a0cf-dbb471cd819a
```

#### Код ответа

204

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")