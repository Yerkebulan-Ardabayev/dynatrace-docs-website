---
title: Terraform API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling
scraped: 2026-03-05T21:37:34.807717
---

# Поддержка Terraform API и управление правами доступа

# Поддержка Terraform API и управление правами доступа

* Последняя версия Dynatrace
* Справочник
* Чтение: 3 мин
* Обновлено 20 ноября 2025 г.

Dynatrace предлагает различные варианты аутентификации вызовов API. Провайдер Dynatrace Terraform поддерживает следующие варианты аутентификации.

* Платформенные токены
* OAuth-клиенты
* Токены доступа (классические)

Дополнительную информацию об управлении идентификацией и доступом (IAM), включая платформенные токены, OAuth-клиенты и API-токены / классические токены доступа, см. в разделе [Токены и OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Создание платформенных токенов

[Платформенные токены](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") можно использовать для аутентификации вызовов API к Dynatrace.
Эти платформенные токены являются долгоживущими токенами доступа.
Полный список поддерживаемых сервисов платформенных токенов см. в разделе [Доступные сервисы для платформенных токенов](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#available-services "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

Следующие блоки кода показывают, как определить переменные окружения для URL вашей среды и платформенного токена для Windows и Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

## Создание OAuth-клиента

Чтобы создать OAuth-клиент, выполните шаги, описанные в разделе [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-oauth-client "Manage authentication and user permissions using OAuth clients.").

Чтобы убедиться, что OAuth-клиент работает должным образом, проверьте, что группы сервисного пользователя предоставляют те же области действия (scopes), что и созданный вами OAuth-клиент, для всех сред, в которых вы планируете его использовать.
Дополнительную информацию об управлении разрешениями см. в разделе [Работа с политиками](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Провайдер Dynatrace Terraform запрашивает токены доступа OAuth, используя ваши учетные данные клиента, для выполнения аутентифицированных вызовов API.

Следующие блоки кода показывают, как определить переменные окружения для URL вашей среды, клиента аутентификации и секрета для Windows и Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



set DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



export DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

## Создание токена доступа к API

Используйте токены доступа для аутентификации вызовов классического API Dynatrace.
Дополнительную информацию об использовании API-токена Dynatrace см. в разделе [Dynatrace API — токены и аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

Следующие блоки кода показывают, как определить переменные окружения для URL вашей среды и API-токена для Windows и Linux.

Windows SaaS Classic Dynatrace

Linux SaaS Classic Dynatrace

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

## Покрытие API

Провайдер Dynatrace Terraform содержит большинство API Dynatrace. Все поддерживаемые ресурсы перечислены в документации провайдера Dynatrace Terraform в [Terraform Registry](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs).

Всегда учитывайте правильные области разрешений (permission scopes), необходимые для выбранных ресурсов API.
Информацию можно найти в разделе [Справочник политик IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") и в [репозитории GitHub провайдера Dynatrace Terraform](https://github.com/dynatrace-oss/terraform-provider-dynatrace/blob/main/documentation/supported-resources.md).
