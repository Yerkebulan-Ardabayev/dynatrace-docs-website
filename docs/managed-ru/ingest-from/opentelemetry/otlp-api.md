---
title: Эндпоинты Dynatrace OTLP API
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api
scraped: 2026-05-12T11:13:55.308011
---

# Эндпоинты Dynatrace OTLP API

# Эндпоинты Dynatrace OTLP API

* Пояснение
* Чтение: 8 мин
* Обновлено 09 января 2026 г.

Протокол [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) является основным сетевым протоколом для обмена данными телеметрии между сервисами и приложениями на базе OpenTelemetry.

Dynatrace предоставляет нативные OTLP-эндпоинты для следующих сервисов:

* Платформа Dynatrace Managed.
* Экземпляры ActiveGate.

Кроме того, можно развернуть [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") в качестве промежуточного сервисного приложения для группировки запросов и повышения производительности сети или для преобразования запросов перед их пересылкой в Dynatrace (например, [маскирование конфиденциальных данных](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")).

## Пути приёма данных по умолчанию

Пути приёма данных, используемые Dynatrace для отдельных типов сигналов, соответствуют [стандартным путям OpenTelemetry](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).

| Тип сигнала | Путь |
| --- | --- |
| Трассировки | `/v1/traces` |
| Метрики | `/v1/metrics` |
| Логи | `/v1/logs` |

В зависимости от конфигурации может потребоваться добавить эти пути отдельно к базовым URL следующих эндпоинтов сервисов при указании URL экспорта. Это может происходить либо в коде при использовании [ручного инструментирования](/managed/ingest-from/opentelemetry/walkthroughs "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."), либо с помощью стандартных [переменных окружения](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).

## Экспорт в Dynatrace

### Базовые URL

Следующие адреса предоставляют базовые URL для настройки приёма OTLP. Используйте URL, подходящий для вашего типа среды, и замените соответствующую часть на ваш [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Понять принцип работы со средами мониторинга и научиться с ними работать.").
Базовый URL также используется при определении переменной окружения `OTEL_EXPORTER_OTLP_ENDPOINT`, см. раздел [Переменные окружения](#environment-variables).

| Тип API | Базовый URL |
| --- | --- |
| Dynatrace Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |
| Containerized Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |

1

Environment ActiveGate по умолчанию прослушивают порт `9999`. Если этот порт был изменён, скорректируйте порт в URL соответствующим образом.

2

Для этой настройки требуется [PVC](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Настройте постоянное хранилище для контейнеризованного ActiveGate для использования в качестве временного хранилища принятых данных.").

### Примеры URL

Следующие примеры URL иллюстрируют комбинации базовых URL и путей для типов сигналов.

#### Cluster ActiveGate

| Тип сигнала | URL |
| --- | --- |
| Трассировки | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/traces` |
| Метрики | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/metrics` |
| Логи | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |

#### Environment ActiveGate

| Тип сигнала | URL |
| --- | --- |
| Трассировки | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces` |
| Метрики | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics` |
| Логи | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |

Обогащение информацией

Для стандартных экспортов OTLP в ActiveGate требуется ручное обогащение информацией о хосте Dynatrace для получения корректных данных топологии.

Для этого убедитесь, что в ваших трассировках заданы корректные атрибуты ресурса сопоставления. Список применимых атрибутов можно найти в [файлах обогащения](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") (или импортировать оттуда).

### Ограничения API

Вызовы к эндпоинтам Dynatrace API имеют следующие ограничения.

* gRPC не поддерживается.
  Вызовы API должны использовать HTTP.
  Для преобразования запроса gRPC OTLP в его аналог по HTTP можно использовать Collector, см. [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP.").
* JSON не поддерживается для Protocol Buffers.
  Необходимо использовать двоичный формат.

### Переменные окружения

При настройке приложения для экспорта в Dynatrace можно задать определённые переменные окружения, как описано ниже.

```
OTEL_EXPORTER_OTLP_ENDPOINT=[YOUR_BASE_URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [YOUR_TOKEN]"



OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

Дополнительные сведения о конфигурации для конкретных языков см. в разделе [Инструментирование вашего приложения](/managed/ingest-from/opentelemetry/walkthroughs "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

### Аутентификация и токены доступа

Для экспортов в ActiveGate аутентификация осуществляется с помощью API-токена доступа и HTTP-заголовка `Authorization`.
Дополнительные сведения о токенах доступа см. в разделе [Dynatrace API: токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для работы с Dynatrace API.").

Для создания токена доступа в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
Используйте соответствующие области доступа для сигналов, которые требуется экспортировать.
Области доступа можно объединять в одном токене, а также добавлять их к существующему токену.

* Трассировки: `openTelemetryTrace.ingest`
* Метрики: `metrics.ingest`
* Логи: `logs.ingest`

### Сетевые требования

Убедитесь, что выполняются следующие условия:

* TCP-порт не заблокирован

  Поскольку OTLP-взаимодействие с ActiveGate осуществляется через порты 443 (для SaaS и Managed) или 9999 (для Environment ActiveGate), убедитесь, что соответствующий TCP-порт не заблокирован межсетевым экраном или другим применяемым решением для управления сетью.
* Хранилище доверенных сертификатов системы актуально

  Чтобы избежать возможных проблем с SSL-сертификатами из-за просроченных или отсутствующих корневых сертификатов по умолчанию, убедитесь, что хранилище доверенных сертификатов вашей системы актуально.

## Экспорт в OTel Collector

Использование OTel Collector в качестве промежуточного шлюза позволяет централизованно оптимизировать данные телеметрии и запросы. Дополнительные сведения и примеры конфигураций для популярных сценариев использования Collector см. в разделе [Сценарии использования OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases "Настройте экземпляр OpenTelemetry Collector для различных сценариев использования.").

Дополнительные сведения о настройке экземпляра Collector см. в разделе [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.").

Преобразование gRPC

Поскольку Dynatrace в настоящее время требует экспорта OTLP по HTTP, можно использовать OTel Collector для преобразования экспортов gRPC в HTTP.

Дополнительные сведения см. в разделе [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP.").

### Аутентификация и TLS

Необходимость использования TLS и аутентификации запросов к OTel Collector зависит от конкретной настройки и конфигурации Collector. По умолчанию [receiver OTLP](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.151.0/receiver/otlpreceiver/README.md) настроен для работы по HTTP без шифрования и не требует аутентификации.

Исходящее соединение из OTel Collector в Dynatrace всегда требует аутентификации и TLS.

### Сетевые требования

Убедитесь, что выполняются следующие условия:

* Сетевые порты не заблокированы

  Убедитесь, что сетевые порты, необходимые для настроенных экземпляров receiver, не заблокированы межсетевым экраном или другим решением для управления сетью, используемым в вашей инфраструктуре.

## Связанные темы

* [API приёма OpenTelemetry Protocol (OTLP)](/managed/dynatrace-api/environment-api/opentelemetry "Используйте Dynatrace API в качестве цели для экспортёров OpenTelemetry для приёма метрик, логов и трассировок OpenTelemetry.")