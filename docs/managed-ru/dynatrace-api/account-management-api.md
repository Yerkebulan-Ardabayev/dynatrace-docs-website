---
title: Account Management API
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api
scraped: 2026-05-12T11:03:10.106263
---

# Account Management API

# Account Management API

* Reference
* Updated on Feb 20, 2026

[### Управление окружениями (Environment management)

Просмотр окружений мониторинга вашего Dynatrace-аккаунта.](/managed/dynatrace-api/account-management-api/environment-management-api/environment-management-api "Просмотр окружений мониторинга Dynatrace-аккаунта через Environment management API.")[### Dynatrace Platform Subscription

Просмотр подписки Dynatrace Platform Subscription и её использования.](/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Запрос данных о Dynatrace Platform Subscription через Account Management API.")[### Справочные данные (Reference data)

Просмотр справочной информации об аккаунте.](/managed/dynatrace-api/account-management-api/reference-data "Просмотр справочной информации аккаунта через Reference data API.")

## API Explorer

Все endpoints Dynatrace API доступны через API Explorer.

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько аккаунтов, выберите нужный.
2. В верхней панели навигации перейдите в **Identity & access management** > **OAuth clients**.
3. В правом верхнем углу страницы нажмите **Account Management API**.

### Аутентификация в API Explorer

Нажмите иконку замка ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") рядом с любым endpoint, чтобы посмотреть информацию о токенах OAuth 2.0, защищающих этот endpoint. Каждому endpoint нужен определённый тип токена.

Также можно разблокировать все endpoints, нажав **Authorize**. В появившемся диалоге будут видны разрешения токена, нужные каждому API endpoint. Введя свой OAuth 2.0 токен в общем диалоге **Available authorizations**, вы разблокируете все связанные API endpoints.

### Попробовать API-вызов

После того как вы ввели OAuth 2.0 токен, API-вызовы можно выполнять прямо в API Explorer. Нажмите **Try it out**, чтобы открыть секцию параметров выбранного endpoint: там можно ввести дополнительные параметры и изменить payload запроса перед его выполнением через **Execute**.

## Связанные темы

* [Управление пользователями и группами](/managed/manage/identity-access-management/user-and-group-management "Управление пользователями и группами")