---
title: Get cluster user sessions configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions-configuration
scraped: 2026-05-12T11:05:49.127124
---

# Get cluster user sessions configuration

# Get cluster user sessions configuration

* Published Apr 02, 2020

Этот API-вызов возвращает конфигурацию пользовательских сессий кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterConfig/userSessions`

## Параметры

Параметры для этого API-вызова не нужны.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UserSessionsConfig](#openapi-definition-UserSessionsConfig) | Успешно |

### Объекты тела ответа

#### Объект `UserSessionsConfig`

Конфигурация пользовательских сессий: политика одновременных сессий и автоматического logout.

| Элемент | Тип | Описание |
| --- | --- | --- |
| automaticLogoutDto | [AutomaticLogoutConfiguration](#openapi-definition-AutomaticLogoutConfiguration) | Конфигурация автоматического logout. |
| concurrentSessionPolicyDto | [ConcurrentSessionPolicy](#openapi-definition-ConcurrentSessionPolicy) | Конфигурация политики одновременных сессий. Установите '0', чтобы отключить ограничение сессий. |

#### Объект `AutomaticLogoutConfiguration`

Конфигурация автоматического logout.

| Элемент | Тип | Описание |
| --- | --- | --- |
| logoutInactiveUsersEnabled | boolean | True, если автоматический logout включён |
| userInactivityTimeout | integer | Таймаут неактивности пользователя |

#### Объект `ConcurrentSessionPolicy`

Конфигурация политики одновременных сессий. Установите '0', чтобы отключить ограничение сессий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| adminLimit | integer | Лимит сессий для admin-пользователей (0 = без лимита) |
| userLimit | integer | Лимит сессий для обычных пользователей (0 = без лимита) |

### JSON-модели тела ответа

```
{



"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



},



"concurrentSessionPolicyDto": {



"adminLimit": 1,



"userLimit": 1



}



}
```

## Пример

В этом примере запрос получает текущую конфигурацию пользовательских сессий кластера. В ответ кластер возвращает информацию о текущей политике одновременных входов и неактивности пользователей. Ответ показывает, что лимит одновременных входов для пользователей `2`. Для аккаунтов cluster admins лимит `5`. Также активна политика logout по неактивности с таймаутом `900` секунд.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions
```

#### Тело ответа

```
{



"concurrentSessionPolicyDto": {



"userLimit": 2,



"adminLimit": 5



},



"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



}



}
```

#### Код ответа

`204`