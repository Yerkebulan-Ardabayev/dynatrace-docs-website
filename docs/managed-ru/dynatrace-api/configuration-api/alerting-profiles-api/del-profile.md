---
title: Alerting profiles API - DELETE a profile
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/del-profile
scraped: 2026-05-12T12:06:36.130651
---

# Alerting profiles API - DELETE a profile

# Alerting profiles API - DELETE a profile

* Reference
* Published Aug 16, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Problem alerting profiles** (`builtin:alerting.profile`).

Удаляет указанный профиль оповещений. Удаление нельзя отменить. Профиль оповещений **Default** удалить нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого профиля оповещений. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Профиль оповещений удалён. Ответ без тела. |

## Пример

В этом примере запрос удаляет профиль оповещений, созданный в примере [POST request](/managed/dynatrace-api/configuration-api/alerting-profiles-api/post-profile#example "Создание профиля оповещений через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/19e50c27-8aed-408f-ad44-d6a1bf856f49 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/19e50c27-8aed-408f-ad44-d6a1bf856f49
```

#### Код ответа

204

## Связанные темы

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для работы с Dynatrace API.")