---
title: Settings API - Span events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-event-attribute
scraped: 2026-05-12T11:47:00.793982
---

# Settings API - Span events schema table

# Settings API - Span events schema table

* Published Dec 05, 2023

### События span (`builtin:span-event-attribute)`

Эту настройку заменили на Allowed attributes (`<your-dynatrace-url>/builtin:attribute-allow-list`) и Attribute data masking (`<your-dynatrace-url>/builtin:attribute-masking`), данные перенесены. Эта настройка скоро будет удалена.

Изменения в этой настройке по-прежнему переносятся в новые, но учтите: некоторые изменения, например удаления атрибутов, перенести нельзя.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-event-attribute` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-event-attribute` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-event-attribute` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-event-attribute` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `key` | text | Ключ атрибута события span, который надо хранить | Required |
| Маскирование `masking` | enum | Если этот атрибут содержит конфиденциальные данные, включите маскирование, чтобы скрыть его значение от пользователей.  Внедрите более гранулярный контроль над видимостью значений атрибутов.  Выберите **Do not mask**, чтобы все пользователи видели реальное значение и могли использовать его в других конфигурациях.  Выберите **Mask entire value**, чтобы полностью скрыть значение этого атрибута от всех, у кого нет права 'View sensitive request data'. Такие атрибуты нельзя использовать для других конфигураций. Выберите **Mask only confidential data**, чтобы применить автоматические стратегии маскирования. Стратегии охватывают, например, номера кредитных карт, IBAN, IP, email-адреса и т.п. Распознать все чувствительные данные может быть невозможно, поэтому всегда проверяйте, что чувствительные данные действительно замаскированы. Если чувствительные данные не распознаны, используйте **Mask entire value**. Пользователи с правом 'View sensitive request data' увидят значение целиком; остальные только нечувствительные части. Такие атрибуты нельзя использовать для других конфигураций. Возможные значения: * `NOT_MASKED` * `MASK_ONLY_CONFIDENTIAL_DATA` * `MASK_ENTIRE_VALUE` | Required |