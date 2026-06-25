---
title: Settings API - Real User Monitoring for process group schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-processgroup
scraped: 2026-05-12T11:40:42.325833
---

# Settings API - Real User Monitoring for process group schema table

# Settings API - Real User Monitoring for process group schema table

* Published Dec 05, 2023

### Real User Monitoring для process group (`builtin:rum.processgroup)`

Когда включён [Real User Monitoring](https://dt-url.net/1n2b0prq), Dynatrace собирает данные о времени загрузки и поведении страниц, которые видят клиенты при работе с приложением. Мониторятся только приложения с внедрёнными JavaScript-тегами.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.processgroup` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `PROCESS_GROUP` - Process Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.processgroup` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.processgroup` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.processgroup` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Real User Monitoring `enable` | boolean | Позволяет OneAgent:  * автоматически внедрять RUM JavaScript-тег в каждую страницу, отдаваемую этой process group * предоставлять информацию для корреляции RUM-данных с серверными PurePath'ами * пересылать beacon'ы в кластер * доставлять код мониторинга  Если эта настройка не включена, RUM-данные могут не коррелироваться с серверными PurePath'ами, что станет проблемой, когда корень серверного PurePath захватывается на этой process group. Например, Apache HTTP-сервер как proxy и Java app-сервер как backend. Отключение этой настройки для process group Apache HTTP-сервера сломает RUM-корреляцию, даже если Dynatrace внедряет RUM JavaScript-тег в process group Java-backend. Чтобы RUM-данные коррелировались с серверными PurePath'ами, RUM должен быть включён на OneAgent, инструментирующем точку входа приложения (Apache HTTP-сервер в этом примере). | Required |