---
title: Anonymization API - GET job status
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/anonymization/get-job-status
scraped: 2026-05-12T11:37:09.697708
---

# Anonymization API - GET job status

# Anonymization API - GET job status

* Reference
* Published Sep 10, 2019

Проверяет статус [задачи анонимизации](/managed/dynatrace-api/environment-api/anonymization/put-job "Запуск задачи анонимизации для удаления пользовательских данных через Dynatrace API."). Ответ содержит процент выполнения задачи.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs/{requestId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs/{requestId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `UserSessionAnonymization`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| requestId | string | ID запрашиваемой задачи анонимизации. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AnonymizationProgressResult](#openapi-definition-AnonymizationProgressResult) | Успех. Тело ответа содержит статус задачи анонимизации. |
| **400** | - | Ошибка. Входные данные некорректны. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `AnonymizationProgressResult`

| Элемент | Тип | Описание |
| --- | --- | --- |
| progress | integer | Прогресс задачи анонимизации в процентах.  -1, если задача ожидает выполнения. |

### JSON-модели тела ответа

```
{



"progress": 50



}
```

## Пример

В этом примере запрос проверяет статус задачи анонимизации с ID **7810238295331327902**.

API-токен передаётся в заголовке **Authorization**.

Ответ показывает, что задача завершена.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs/7810238295331327902 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs/7810238295331327902
```

#### Содержимое ответа

```
{



"progress": 100



}
```

#### Код ответа

200