---
title: Поддержка Terraform API и обработка разрешений доступа
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling
scraped: 2026-03-05T21:37:34.807717
---

* Последнее Dynatrace
* Справка
* 3-минутное чтение

Dynatrace предлагает различные варианты аутентификации вызовов API. Поставщик Terraform Dynatrace поддерживает следующие варианты аутентификации.

* Токены платформы
* Клиенты OAuth
* Токены доступа (классические)

Для получения более подробной информации об управлении идентификацией и доступом (IAM), включая токены платформы, клиенты OAuth и токены API/токены доступа классического типа, см. Токены и клиенты OAuth.

## Создание токенов платформы

Токены платформы можно использовать для аутентификации вызовов API против Dynatrace.
Эти токены платформы являются долгосрочными токенами доступа.
Для полного списка поддерживаемых сервисов токенов платформы см. [Доступные сервисы для токенов платформы](../../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md#available-services "Создайте персонализированные токены платформы для доступа к сервисам Dynatrace через API в вашем контексте пользователя.").

Следующие блоки кода показывают, как определить переменные среды для URL-адреса вашей среды и токена платформы для Windows и Linux.

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

## Создание клиента OAuth

Чтобы создать клиента OAuth, следуйте шагам, описанным в Клиентах OAuth.

Чтобы убедиться, что клиент OAuth работает как ожидается, проверьте, что группы сервисного пользователя предоставляют те же области, что и клиент OAuth, который вы создали для всех сред, с которыми вы хотите использовать его.
Для получения более подробной информации о контроле разрешений см. Работа с политиками.

Поставщик Terraform Dynatrace запрашивает токены доступа OAuth с помощью ваших учетных данных клиента для аутентификации вызовов API.

Следующие блоки кода показывают, как определить переменные среды для URL-адреса вашей среды, клиента аутентификации и секрета для Windows и Linux.

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

## Создание токена доступа API

Используйте токены доступа для аутентификации вызовов API классического типа Dynatrace.
Для получения более подробной информации о том, как использовать токен Dynatrace API, см. Dynatrace API - Токены и аутентификация.

Следующие блоки кода показывают, как определить переменные среды для URL-адреса вашей среды и токена API для Windows и Linux.

Windows Classic Dynatrace

Linux Classic Dynatrace

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com


set DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com


export DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

## Покрытие API

Поставщик Terraform Dynatrace содержит большинство Dynatrace API.
Все поддерживаемые ресурсы перечислены в документации поставщика Terraform Dynatrace в [Реестре Terraform](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs).

Всегда учитывайте правильные области разрешений, необходимые для выбранных ресурсов API.
Информацию можно найти в Справке по политикам IAM и [репозитории Git Hub поставщика Terraform Dynatrace](https://github.com/dynatrace-oss/terraform-provider-dynatrace/blob/main/documentation/supported-resources.md).