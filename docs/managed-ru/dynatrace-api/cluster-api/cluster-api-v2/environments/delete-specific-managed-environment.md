---
title: Delete specific environment
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/delete-specific-managed-environment
scraped: 2026-05-12T11:05:58.749801
---

# Delete specific environment

# Delete specific environment

* Published Mar 09, 2021

Этот API-вызов удаляет указанное окружение. Перед удалением окружение нужно отключить.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID окружения, которое нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |
| **400** | Сбой. Например, если окружение не отключено. |

## Пример

Удаляет окружение `19a963a7-b19f-4382-964a-4df674c8eb8e`.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e" -H "accept: */*" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e
```

#### Тело ответа

Ответ без тела.

#### Код ответа

`204`