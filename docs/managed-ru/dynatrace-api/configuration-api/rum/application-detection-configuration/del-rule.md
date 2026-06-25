---
title: Applications detection rules API - DELETE a rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/del-rule
scraped: 2026-05-12T11:16:07.633423
---

# Applications detection rules API - DELETE a rule

# Applications detection rules API - DELETE a rule

* Reference
* Published Aug 30, 2019

Удаляет указанное правило обнаружения приложений.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого правила обнаружения приложений. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Пример

В этом примере запрос удаляет правило обнаружения приложений из примера [POST request](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/post-rule#example "Создание правила обнаружения приложений через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/applicationDetectionRules/9568a82b-73d8-4b18-be1a-4289433e2619
```

#### Код ответа

204

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Легко разберитесь в правилах обнаружения вашего RUM-приложения.")
* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")