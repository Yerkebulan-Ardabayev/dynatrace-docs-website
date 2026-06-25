---
title: Settings API - Configure ownership schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ownership-config
scraped: 2026-05-12T11:39:57.817239
---

# Settings API - Configure ownership schema table

# Settings API - Configure ownership schema table

* Published Dec 05, 2023

### Настройка владения (`builtin:ownership.config)`

Настройте ключи для метаданных владения и тегов. [See documentation](https://dt-url.net/ownership-custom-keys)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ownership.config` | * `group:ownership` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.config` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ownership.config` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.config` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключи для метаданных владения и тегов `ownershipIdentifiers` | [OwnershipIdentifier](#OwnershipIdentifier)[] | Теги и метаданные представляют собой пары ключ-значение. Задайте ключи для тегов и метаданных, которые учитываются при определении владения. Если тег или метаданные начинаются с ключа, определённого ниже, значение тега или метаданных считается идентификатором команды. | Required |

##### Объект `OwnershipIdentifier`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Ключ для метаданных владения и тегов `key` | text | - | Required |