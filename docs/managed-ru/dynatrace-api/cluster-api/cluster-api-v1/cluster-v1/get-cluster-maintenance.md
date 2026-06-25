---
title: Get details about the current cluster maintenance state
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-maintenance
scraped: 2026-05-12T12:12:41.958990
---

# Get details about the current cluster maintenance state

# Get details about the current cluster maintenance state

* Published Sep 29, 2025

Этот API-запрос возвращает информацию о текущем состоянии maintenance кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/cluster/maintenance`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [IPMigrationMaintenanceMode](#openapi-definition-IPMigrationMaintenanceMode) | Успех |

### Объекты тела ответа

#### Объект `IPMigrationMaintenanceMode`

Информация о cluster maintenance, инициированном IP migration.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ended | [TriggeredByResponseDto](#openapi-definition-TriggeredByResponseDto) | Данные о том, кто и когда завершил состояние maintenance. |
| jsonObjectForReasonMessage | string | - |
| metadata | [IpMigrationMetadataResponseDto](#openapi-definition-IpMigrationMetadataResponseDto) | Опциональные метаданные. |
| nodeId | integer | ID узла. |
| reason | string | Причина перехода в maintenance mode. Возможные значения: * `IP_MIGRATION` |
| started | [TriggeredByResponseDto](#openapi-definition-TriggeredByResponseDto) | Данные о том, кто и когда завершил состояние maintenance. |

#### Объект `TriggeredByResponseDto`

Данные о том, кто и когда завершил состояние maintenance.

| Элемент | Тип | Описание |
| --- | --- | --- |
| date | string | Дата триггера. |
| user | string | Кем инициировано. |

#### Объект `IpMigrationMetadataResponseDto`

Опциональные метаданные.

| Элемент | Тип | Описание |
| --- | --- | --- |
| newIp | string | - |
| oldIp | string | - |

### JSON-модели тела ответа

```
{



"ended": {



"date": "2025-07-09T08:38:08.690Z",



"user": "admin"



},



"metadata": {



"newIp": "172.31.101.10",



"oldIp": "172.31.101.9"



},



"nodeId": 1,



"reason": "IP_MIGRATION",



"started": {



"date": "2025-07-08T08:38:08.690Z",



"user": "admin"



}



}
```

#### Тело ответа

```
{



"ended": {



"date": "2025-07-09T08:38:08.690Z",



"user": "admin"



},



"metadata": {



"newIp": "172.31.101.10",



"oldIp": "172.31.101.9"



},



"nodeId": 1,



"reason": "IP_MIGRATION",



"started": {



"date": "2025-07-08T08:38:08.690Z",



"user": "admin"



}



}
```

#### Код ответа

200