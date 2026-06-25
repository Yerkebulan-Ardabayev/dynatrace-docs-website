---
title: Settings API - Attribute data masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-masking
scraped: 2026-05-12T11:49:36.526822
---

# Settings API - Attribute data masking schema table

# Settings API - Attribute data masking schema table

* Published Dec 05, 2023

### Маскирование данных атрибутов (`builtin:attribute-masking)`

Настройте видимость хранимых значений атрибутов в соответствии с требованиями приватности. Пользователи с правами **View sensitive request data** всегда видят значения. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-masking` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-masking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-masking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-masking` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если true, применяется маскирование указанного ключа. | Required |
| Ключ атрибута `key` | text | Ключ атрибута | Required |
| Маскирование `masking` | enum | Задайте стратегию маскирования, чтобы скрыть значение от пользователей.  Выберите **Mask entire value**, чтобы полностью скрыть значение этого атрибута от всех, у кого нет права 'View sensitive request data'. Такие атрибуты нельзя использовать для определения других конфигураций.  Выберите **Mask only confidential data**, чтобы применить автоматические стратегии маскирования. Стратегии охватывают, например, номера кредитных карт, IBAN, IP, email-адреса и т.п. Распознать все чувствительные данные может быть невозможно, поэтому всегда проверяйте, что чувствительные данные действительно замаскированы. Если чувствительные данные не распознаны, используйте **Mask entire value**. Пользователи с правом 'View sensitive request data' увидят значение целиком; остальные видят только нечувствительные части. Такие атрибуты нельзя использовать для определения других конфигураций. Возможные значения: * `MASK_ONLY_CONFIDENTIAL_DATA` * `MASK_ENTIRE_VALUE` | Required |