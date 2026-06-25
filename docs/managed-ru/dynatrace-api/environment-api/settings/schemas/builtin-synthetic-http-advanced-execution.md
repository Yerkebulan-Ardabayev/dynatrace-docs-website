---
title: Settings API - Advanced settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-advanced-execution
scraped: 2026-05-12T11:43:52.342639
---

# Settings API - Advanced settings schema table

# Settings API - Advanced settings schema table

* Published Sep 25, 2025
* Preview

### Дополнительные настройки (`builtin:synthetic.http.advanced-execution)`

Тонко настройте выполнение HTTP-монитора пользовательскими параметрами. Эти настройки переопределяют значения по умолчанию. Подробнее см. [Advanced settings for HTTP monitors](https://dt-url.net/wa034cl).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.advanced-execution` | * `group:synthetic.http` | `HTTP_CHECK` - HTTP monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.advanced-execution` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Таймаут запроса (мс) `requestTimeout` | integer | Поддерживаемые значения: от 1 000 до 60 000 мс | Optional |
| Таймаут подключения (мс) `connectTimeout` | integer | Поддерживаемые значения: от 1 000 до 60 000 мс | Optional |
| Максимальный размер заголовка (B) `maxHeaderSize` | integer | Поддерживаемые значения: от 10 240 до 61 440 байт | Optional |
| Таймаут выполнения монитора (мс) `monitorExecutionTimeout` | integer | Поддерживаемые значения: от 10 000 до 300 000 мс | Optional |
| Таймаут выполнения скрипта (мс) `scriptExecutionTimeout` | integer | Поддерживаемые значения: от 1 000 до 10 000 мс | Optional |
| Максимальный размер тела запроса (B) `maxRequestBodySize` | integer | Поддерживаемые значения: от 10 240 до 102 400 байт | Optional |
| Максимальный размер пользовательского скрипта (B) `maxCustomScriptSize` | integer | Поддерживаемые значения: от 10 240 до 102 400 байт | Optional |
| Максимальный размер тела ответа (B) `maxResponseBodySize` | integer | Поддерживаемые значения: от 51 200 до 20 971 520 байт | Optional |
| Максимальный размер тела ответа, читаемого пользовательским скриптом (B) `maxResponseBodyReadByScriptSize` | integer | Поддерживаемые значения: от 10 240 до 102 400 байт | Optional |
| Таймаут DNS-запроса (мс) `dnsQueryTimeout` | integer | Поддерживаемые значения: от 1 000 до 60 000 мс | Optional |