---
title: "Delete user sessions of a given user"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/delete-cluster-user-session
updated: 2026-02-09
---

Этот API-вызов позволяет завершить все сессии конкретного пользователя.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/userSessions`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| userId | string | ID пользователя (обязательный) | query | Optional |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успех |
| **400** | Bad request. User id должен быть заполнен. |
| **404** | Сессии пользователя не найдены |
| **500** | Операция не выполнена |
| **510** | Не удалось инвалидировать сессии |

## Пример

В этом примере запрос удаляет все сессии пользователя с user ID `user.name`. Код ответа `200` означает успешное удаление.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name" -H  "accept: */*"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name
```

#### Код ответа

`200`
