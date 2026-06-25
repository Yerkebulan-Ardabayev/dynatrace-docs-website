---
title: Update log events per cluster for Log Monitoring
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring
scraped: 2026-05-12T11:06:15.941819
---

# Update log events per cluster for Log Monitoring

# Update log events per cluster for Log Monitoring

* Published Oct 14, 2021

Этот API-вызов обновляет общий лимит log events на кластер на основе размера ресурсов кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/logMonitoring/refreshLogEventsLimit`

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LogEventsLimitDto](#openapi-definition-LogEventsLimitDto) | Операция выполнена успешно. Возвращает новый лимит log events |
| **500** | - | Обновление лимита log events невозможно из-за отсутствия статистики хранилища |

### Объекты тела ответа

#### Объект `LogEventsLimitDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| limit | integer | - |

### JSON-модели тела ответа

```
{



"limit": 1



}
```

## Пример

В этом примере лимит ingest log events увеличивается до `54236` log events в минуту на кластер.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/logMonitoring/refreshLogEventsLimit"



-H "accept: application/json; charset=utf-8"



-H "Authorization: Api-Token abc"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/logMonitoring/refreshLogEventsLimit
```

#### Тело ответа

```
{



"limit": 54236



}
```

#### Код ответа

`200`