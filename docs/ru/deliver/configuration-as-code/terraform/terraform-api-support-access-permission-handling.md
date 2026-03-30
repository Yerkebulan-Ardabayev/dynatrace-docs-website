---
title: Поддержка Terraform API и обработка разрешений доступа
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling
scraped: 2026-03-05T21:37:34.807717
---

Dynatrace Terraform Provider поддерживает аутентификацию через **токены платформы**, **OAuth-клиенты** и **токены доступа (классические)**. Подробности см. в разделе Токены и клиенты OAuth.

## Токены платформы

Долгосрочные токены доступа. Полный список поддерживаемых сервисов см. в [документации платформенных токенов](../../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md#available-services).

```
# Windows
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
set DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>

# Linux
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
export DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

## OAuth-клиент

Создайте по инструкции в документации OAuth-клиентов. Убедитесь, что группы сервисного пользователя предоставляют те же scopes, что и OAuth-клиент.

```
# Windows
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
set DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>
set DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>

# Linux
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
export DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>
export DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

## Токен доступа API (классический)

```
# Windows
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
set DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>

# Linux
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com
export DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

## Покрытие API

Все ресурсы перечислены в [Реестре Terraform](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs). Учитывайте необходимые scopes — см. Справку по политикам IAM и [репозиторий Terraform Provider](https://github.com/dynatrace-oss/terraform-provider-dynatrace/blob/main/documentation/supported-resources.md).
