---
title: Mobile and custom app API - DELETE an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/apps/delete-app
scraped: 2026-05-12T11:15:27.684812
---

# Mobile and custom app API - DELETE an app

# Mobile and custom app API - DELETE an app

* Reference
* Published Nov 05, 2020

Удаляет указанное мобильное или пользовательское приложение.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Приложение удалено. Ответ без тела. |
| **404** | Сбой. Указанная сущность не существует. |

## Связанные темы

* [Удаление мобильного приложения](/managed/observe/digital-experience/mobile-applications/additional-configuration/delete-application-mobile "Удаление мобильных приложений через веб-интерфейс Dynatrace или API.")
* [Удаление пользовательского приложения](/managed/observe/digital-experience/custom-applications/additional-configuration/delete-application-custom "Удаление пользовательских приложений через веб-интерфейс Dynatrace или API.")