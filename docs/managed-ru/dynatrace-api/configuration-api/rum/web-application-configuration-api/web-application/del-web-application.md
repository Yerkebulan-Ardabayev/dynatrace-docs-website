---
title: Web application configuration API - DELETE a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application
scraped: 2026-05-12T11:16:51.645643
---

# Web application configuration API - DELETE a web application

# Web application configuration API - DELETE a web application

* Reference
* Published Sep 03, 2019

Удаляет указанное веб-приложение.

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений смотрите [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого веб-приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Приложение удалено. Ответ без тела. |

## Связанные темы

* [Удаление веб-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Удаление веб-приложений через веб-интерфейс Dynatrace или API.")