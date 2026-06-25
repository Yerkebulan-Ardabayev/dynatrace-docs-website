---
title: Settings API - Cookie schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-injection-cookie
scraped: 2026-05-12T11:45:33.953669
---

# Settings API - Cookie schema table

# Settings API - Cookie schema table

* Published Feb 26, 2024

### Cookie (`builtin:rum.web.injection.cookie)`

Dynatrace RUM использует cookie для корреляции пользовательских действий с backend-метриками производительности. Здесь можно изменить настройки cookie. Подробнее о RUM cookies см. в [documentation](https://dt-url.net/wmq1pti).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.injection.cookie` | * `group:rum-injection` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.injection.cookie` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Использовать атрибут Secure для cookie, устанавливаемых Dynatrace `useSecureCookieAttribute` | boolean | Если приложение доступно только по SSL, можно добавить атрибут Secure ко всем cookie, устанавливаемым Dynatrace. Это предотвращает отображение предупреждений от сканеров безопасности PCI-compliance. Учтите: при включении этой настройки корреляция пользовательских действий с серверными web-запросами возможна только через SSL-соединения. | Required |
| Атрибут cookie SameSite `sameSiteCookieAttribute` | enum | Определите, должен ли cookie быть ограничен first-party или same-site контекстом. Подробнее см. [SameSite cookies and available values](https://dt-url.net/yds1p8u). Возможные значения: * `NOTSET` * `NONE` * `LAX` * `STRICT` | Required |
| Домен для размещения cookie `cookiePlacementDomain` | text | Укажите альтернативный домен для cookie, устанавливаемых Dynatrace. Учтите: браузер может не разрешать размещение cookie на определённых доменах (например, top-level доменах). Перед вводом доменного имени убедитесь, что домен принимает cookie от вашего браузера. Подробнее см. список [forbidden top-level domains](https://dt-url.net/9n6b0pfz). | Optional |