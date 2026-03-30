---
title: Поддержка API и управление правами доступа Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling
scraped: 2026-03-06T21:29:49.923198
---

Monaco поддерживает аутентификацию через **платформенные токены** и **OAuth-клиенты**. Подробности см. в разделе Токены и OAuth-клиенты.

## Создание платформенного токена

Следуйте шагам в документации «Создание платформенного токена для CLI Dynatrace Monaco». Каждый тип конфигурации требует определённых OAuth-scopes.

## Создание OAuth-клиента

Следуйте шагам в документации «Создание OAuth2-клиента».

Для области `automation:workflows:admin` предварительно создайте пользовательскую политику, привяжите группу и назначьте пользователя.

Для конфигураций OpenPipeline пользователь должен принадлежать к группе с политикой **Data Processing and Storage**.

Использование OAuth-клиента:
1. Задайте ID клиента и секрет как переменные окружения.
2. Укажите ссылки на них в разделе OAuth файла манифеста.
3. Monaco автоматически запрашивает токены доступа.

## Покрытие API

Поддерживаемые типы: **Settings 2.0**, **Configuration API**, **Platform API**.

### Settings 2.0

Требуемые OAuth-scopes (последняя версия):

| Назначение | Scope |
| --- | --- |
| Управление объектами Settings 2.0 | `settings:objects:read`, `settings:objects:write` |
| Просмотр схем | `settings:schemas:read` |

Для классического Dynatrace: `settings.read`, `settings.write`.

### Platform API

Требуются OAuth-учётные данные. Поддерживаемые типы описаны в документации Monaco.

### Разрешения управления аккаунтами

Необходимые scopes: `account-idm-read`, `account-idm-write`, `account-env-read`, `account-env-write`, `iam-policies-management`, `iam:policies:write`, `iam:policies:read`, `iam:bindings:write`, `iam:bindings:read`, `iam:boundaries:read`, `iam:boundaries:write`.

### Configuration API

Требует токена доступа к API. Большинство Configuration API устарели в пользу Settings 2.0.

## Связанные темы

* YAML-файл конфигурации Monaco — список специальных типов конфигурации
