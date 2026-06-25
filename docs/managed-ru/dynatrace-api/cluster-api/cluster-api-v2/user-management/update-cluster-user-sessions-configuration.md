---
title: Update cluster user sessions configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration
scraped: 2026-05-12T11:05:55.183707
---

# Update cluster user sessions configuration

# Update cluster user sessions configuration

* Published Feb 12, 2020

Этот API-вызов обновляет конфигурацию пользовательских сессий кластера. Можно изменить конфигурацию пользовательских сессий, задав новые лимиты одновременных пользовательских сессий для аккаунтов cluster admin и обычных пользователей. Установите лимиты в `0` для неограниченных одновременных сессий. Если задать любой лимит в `0`, лимит для другого типа аккаунта тоже должен быть `0`.

С помощью этого запроса можно обновить политику автоматического logout. По умолчанию пользователи на странице с auto-refresh не выходят автоматически. Используйте payload ниже, чтобы включить автоматический logout и задать таймаут сессии в `900` секунд (15 минут).

```
"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



}
```

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterConfig/userSessions`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [UserSessionsConfig](#openapi-definition-UserSessionsConfig) | Конфигурация пользовательских сессий: политика одновременных сессий и автоматического logout. | body | Optional |

### Объекты тела запроса

#### Объект `UserSessionsConfig`

Конфигурация пользовательских сессий: политика одновременных сессий и автоматического logout.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| automaticLogoutDto | [AutomaticLogoutConfiguration](#openapi-definition-AutomaticLogoutConfiguration) | Конфигурация автоматического logout. | Required |
| concurrentSessionPolicyDto | [ConcurrentSessionPolicy](#openapi-definition-ConcurrentSessionPolicy) | Конфигурация политики одновременных сессий. Установите '0', чтобы отключить ограничение сессий. | Required |

#### Объект `AutomaticLogoutConfiguration`

Конфигурация автоматического logout.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| logoutInactiveUsersEnabled | boolean | True, если автоматический logout включён | Required |
| userInactivityTimeout | integer | Таймаут неактивности пользователя | Required |

#### Объект `ConcurrentSessionPolicy`

Конфигурация политики одновременных сессий. Установите '0', чтобы отключить ограничение сессий.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| adminLimit | integer | Лимит сессий для admin-пользователей (0 = без лимита) | Required |
| userLimit | integer | Лимит сессий для обычных пользователей (0 = без лимита) | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успешно |
| **400** | Неверные параметры |
| **510** | Не удалось обновить конфигурацию |

## Пример

В этом примере запрос обновляет конфигурацию пользовательских сессий кластера. Кластер обновляет текущую политику одновременных входов и неактивности пользователей. Запрос задаёт лимит одновременных входов для пользователей в `3`. Лимит для аккаунтов cluster admin `5`. Также активна политика logout по неактивности с таймаутом `900` секунд.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions"



-H  "accept: */*"



-H  "Content-Type: */*"



-d "{\"concurrentSessionPolicyDto\":{\"userLimit\":0,\"adminLimit\":0},\"automaticLogoutDto\":{\"logoutInactiveUsersEnabled\":true,\"userInactivityTimeout\":900}}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions
```

#### Тело запроса

```
{



"concurrentSessionPolicyDto": {



"userLimit": 3,



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