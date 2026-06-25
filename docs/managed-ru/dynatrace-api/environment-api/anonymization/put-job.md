---
title: Anonymization API - PUT anonymization job
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/anonymization/put-job
scraped: 2026-05-12T11:35:36.664786
---

# Anonymization API - PUT anonymization job

# Anonymization API - PUT anonymization job

* Reference
* Published Sep 10, 2019

Создаёт задачу анонимизации пользовательских сессий. Задача анонимизирует все пользовательские сессии в указанном таймфрейме, маскируя user ID (**userIds**) и IP-адрес (**ips**).

IP-адрес маскируется заменой последнего октета на `0`.

Чтобы идентифицировать сессии для анонимизации, можно указать user ID, IP-адрес, internal application ID или их комбинацию. Если задано несколько критериев, применяется логика **OR**.

* Каждая сессия указанных user ID анонимизируется независимо от IP-адреса, с которого она пришла.
* Каждая сессия с указанного IP-адреса анонимизируется, даже если она принадлежит user ID, не входящему в список.
* Каждая сессия, содержащая хотя бы одно user action, событие или ошибку с указанным internal application ID, анонимизируется независимо от user ID или IP-адреса.
  Можно указать несколько user ID и IP-адресов, но только один internal application ID.

Независимо от способа идентификации сессий маскируются и user ID, и IP-адрес. Отменить анонимизацию нельзя.

Запрос возвращает payload `application/json`. Тело ответа содержит `clusterRequestIds` в случае Premium High-Availability кластеров и `requestId` задачи анонимизации, который можно использовать для [проверки статуса задачи](/managed/dynatrace-api/environment-api/anonymization/get-job-status "Просмотр статуса задачи анонимизации через Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/anonymize/anonymizationJobs` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `UserSessionAnonymization`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| startTimestamp | integer | Стартовая временная метка анонимизируемой пользовательской сессии, в миллисекундах UTC.  Если не задано, используется самое раннее доступное время. | query | Optional |
| endTimestamp | integer | Конечная временная метка анонимизируемой пользовательской сессии, в миллисекундах UTC.  Если не задано, используется текущее время. | query | Optional |
| userIds | string[] | UserID пользователя для анонимизации.  Можно указать несколько ID в формате: `userIds=user1&userIds=user2`. | query | Optional |
| ips | string[] | IP-адрес пользователя для анонимизации. Все пользовательские сессии с этого IP будут анонимизированы.  Можно указать несколько IP в формате: `ips=ip1&ips=ip2`. | query | Optional |
| internalApplicationId | string | Internal application ID, используемый для идентификации сессий, подлежащих анонимизации.  Все пользовательские сессии, содержащие хотя бы одно user action, событие или ошибку с указанным application ID, будут анонимизированы.  Если вы задаёте дополнительные поля для анонимизации в user actions или событиях, анонимизированы будут только те user actions и события с соответствующим application ID. | query | Optional |
| additionalField | string[] | Список полей для анонимизации.  Можно указать несколько полей в формате: `additionalField=field1&additionalField=field2`. Элемент может принимать значения * `ip` * `content` * `country` * `region` * `city` * `userId` * `isp` * `stringProperties` * `longProperties` * `doubleProperties` * `dateProperties` * `carrier` * `userActions.name` * `userActions.domain` * `userActions.targetUrl` * `userActions.syntheticEvent` * `userActions.stringProperties` * `userActions.longProperties` * `userActions.doubleProperties` * `userActions.dateProperties` * `events.name` * `events.domain` * `events.page` * `events.pageGroup` * `events.pageReferrer` * `events.pageReferrerGroup` * `errors.name` * `errors.domain` | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AnonymizationIdResult](#openapi-definition-AnonymizationIdResult) | Успех. Тело ответа содержит ID задачи анонимизации. ID можно использовать для проверки статуса задачи. |
| **400** | - | Ошибка. Входные данные некорректны. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `AnonymizationIdResult`

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterRequestIds | [AnonymizationClusterRequestID[]](#openapi-definition-AnonymizationClusterRequestID) | Список пар request ID и имени кластера. |
| requestId | string | ID новой задачи анонимизации. При участии нескольких ЦОД возвращается список, разделённый символом "|". |

#### Объект `AnonymizationClusterRequestID`

Список пар request ID и имени кластера.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dcName | string | - |
| id | integer | - |

### JSON-модели тела ответа

```
{



"clusterRequestIds": [



{



"dcName": "string",



"id": 1



}



],



"requestId": "-4013759873546847071|7354684707140137598"



}
```

## Пример

В этом примере запрос запускает задачу анонимизации всех сессий пользователей **john.smith** и **mary.smith** в таймфрейме с 00:00 1 сентября 2018 г. до 23:59 10 сентября 2018 г. (соответствует таймстампам **1535752800000** и **1536616799000**).

API-токен передаётся в заголовке **Authorization**.

Ответ содержит ID задачи анонимизации, который можно использовать для проверки её статуса.

#### Curl

```
curl -X PUT \



'https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs?startTimestamp=1535752800000&endTimestamp=1536616799000&userIds=john.smith&userIds=mary.smith' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/anonymize/anonymizationJobs?startTimestamp=1535752800000&endTimestamp=1536616799000&userIds=john.smith&userIds=mary.smith
```

#### Содержимое ответа

```
{



"clusterRequestIds": [



{



"id": -7520440752290577000,



"dcName": ""



}



],



"requestId": "-7520440752290577781"



}
```

#### Код ответа

200