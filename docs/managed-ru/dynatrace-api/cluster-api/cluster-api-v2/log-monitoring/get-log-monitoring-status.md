---
title: Get Log Monitoring status
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/get-log-monitoring-status
scraped: 2026-05-12T11:06:08.449485
---

# Get Log Monitoring status

# Get Log Monitoring status

* Published Oct 18, 2021

Этот API-вызов возвращает статус Log Monitoring для указанного окружения.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/logMonitoring/{environmentId}/status`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| environmentId | string | ID окружения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LogMonitoringStatus](#openapi-definition-LogMonitoringStatus) | Операция выполнена успешно. |
| **404** | - | Сбой. Запрошенный ресурс не существует. |

### Объекты тела ответа

#### Объект `LogMonitoringStatus`

Статус Log Monitoring

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Определяет, включён ли Log Monitoring |

### JSON-модели тела ответа

```
{



"enabled": "true"



}
```

## Пример

В этом примере запрашивается статус конфигурации Log Monitoring для окружения `19a963a7-b19f-4382-964a-4df674c8eb8e`. В ответ возвращается JSON, указывающий, что последняя версия Dynatrace Log Monitoring включена в этом окружении.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/logMonitoring/19a963a7-b19f-4382-964a-4df674c8eb8e/status"



-H  "accept: application/json; charset=utf-8"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/logMonitoring/19a963a7-b19f-4382-964a-4df674c8eb8e/status
```

#### Тело ответа

```
{



"enabled": "true"



}
```

#### Код ответа

`200`