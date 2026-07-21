---
title: Конечные точки Dynatrace OTLP API
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api
---

# Конечные точки Dynatrace OTLP API

# Конечные точки Dynatrace OTLP API

* Пояснение
* Чтение займёт 8 минут
* Обновлено 09 января 2026 г.

[OpenTelemetry Protocol (OTLP)﻿](https://opentelemetry.io/docs/specs/otlp/) это основной сетевой протокол для обмена данными телеметрии между сервисами и приложениями на базе OpenTelemetry.

Dynatrace предоставляет нативные конечные точки OTLP со следующими сервисами:

* Платформа Dynatrace Managed.
* Экземпляры ActiveGate.

Также можно развернуть [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") как промежуточное сервисное приложение для пакетирования запросов и повышения производительности сети, или для преобразования запросов перед их пересылкой в Dynatrace (например, [маскирования конфиденциальных данных](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед пересылкой в Dynatrace.")).

## Пути приёма по умолчанию

Пути приёма, которые Dynatrace использует для отдельных типов сигналов, соответствуют [стандартным путям OpenTelemetry﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).

| Тип сигнала | Путь |
| --- | --- |
| Трассировки | `/v1/traces` |
| Метрики | `/v1/metrics` |
| Логи | `/v1/logs` |

В зависимости от конфигурации может потребоваться добавлять эти пути по отдельности к базовым URL следующих сервисных конечных точек при указании URL экспорта. Это может происходить либо в коде, при использовании [ручной инструментации](/managed/ingest-from/opentelemetry/walkthroughs "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."), либо с помощью стандартных [переменных окружения﻿](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).

## Экспорт в Dynatrace

### Базовые URL

Следующие адреса представляют собой базовые URL для конфигурации приёма OTLP. Используйте URL, применимый к вашему типу среды, и замените соответствующую часть на [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор своей среды и как настроить и подключить несколько сред.").
Базовый URL также используется при определении переменной окружения `OTEL_EXPORTER_OTLP_ENDPOINT`, см. [Переменные Environment](#environment-variables).

| Тип API | Базовый URL |
| --- | --- |
| Dynatrace Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |
| Контейнеризованный Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |

1

Environment ActiveGate по умолчанию прослушивает порт `9999`. Если этот порт изменён, соответствующим образом скорректируйте порт в URL.

2

Для этой настройки требуется [PVC](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Настройте постоянное хранилище для контейнеризованного ActiveGate, используемое как временное хранилище для принятых данных.").

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

Обогащение информации

Экспорт OTLP «в чистом виде» в ActiveGate требует ручного обогащения информации об узле Dynatrace, чтобы получить корректную топологическую информацию.

Для этого убедитесь, что в трассировках заданы корректные атрибуты ресурса для сопоставления. Список применимых атрибутов можно найти (или импортировать) в [файлах обогащения](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

### Ограничения API

Вызовы конечных точек Dynatrace API имеют следующие ограничения.

* gRPC не поддерживается.
  Вызовы API должны использовать HTTP.
  Для преобразования gRPC-запроса OTLP в его HTTP-аналог можно использовать Collector, см. [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования gRPC-запроса OTLP в HTTP.").
* JSON не поддерживается для Protocol Buffers.
  Должен использоваться бинарный формат.

### Переменные Environment

При настройке приложения для экспорта в Dynatrace один из способов, настроить определённые переменные окружения, как описано ниже.

```
OTEL_EXPORTER_OTLP_ENDPOINT=[YOUR_BASE_URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [YOUR_TOKEN]"



OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

Дополнительную информацию о конфигурации для конкретных языков см. в разделе [Инструментирование приложения](/managed/ingest-from/opentelemetry/walkthroughs "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

### Аутентификация и токены доступа

Для экспорта в ActiveGate аутентификация выполняется с помощью токена доступа API и HTTP-заголовка `Authorization`.
Дополнительную информацию о токенах доступа см. в разделе [Dynatrace API: токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Чтобы создать токен доступа, в Dynatrace перейдите в раздел ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
Используйте соответствующие области доступа для сигналов, которые нужно экспортировать.
Области можно объединять в одном токене, а также добавлять области к существующему токену.

* Трассировки: `openTelemetryTrace.ingest`
* Метрики: `metrics.ingest`
* Логи: `logs.ingest`

### Сетевые требования

Убедитесь, что выполняются следующие условия:

* TCP-порт не заблокирован

  Поскольку обмен данными OTLP с ActiveGate происходит через порты 443 (для SaaS и Managed) или 9999 (для Environment ActiveGate), убедитесь, что соответствующий TCP-порт не заблокирован брандмауэром или другим используемым решением для управления сетью.
* Хранилище доверенных сертификатов системы актуально

  Чтобы избежать возможных проблем с SSL-сертификатами из-за истёкших или отсутствующих корневых сертификатов по умолчанию, убедитесь, что хранилище доверенных сертификатов системы актуально.

## Экспорт в OTel Collector

Использование OTel Collector в качестве промежуточного шлюза позволяет централизованно упорядочивать и оптимизировать данные телеметрии и запросы. Дополнительную информацию и примеры конфигураций для популярных сценариев использования Collector см. в разделе [Сценарии использования OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases "Настройте экземпляр OpenTelemetry Collector для различных сценариев использования.").

Подробнее о настройке экземпляра Collector см. в разделе [OTel Collector для приёма телеметрии в Dynatrace](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.").

Преобразование gRPC

Поскольку Dynatrace в настоящее время требует экспорта OTLP по HTTP, можно использовать OTel Collector для преобразования экспорта gRPC в HTTP.

Подробнее см. в разделе [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования gRPC-запроса OTLP в HTTP.").

### Аутентификация и TLS

Необходимость использования TLS и аутентификации запросов к OTel Collector зависит от конкретной настройки/конфигурации Collector. По умолчанию [приёмник OTLP﻿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.156.0/receiver/otlpreceiver/README.md) настроен на использование обычного текстового HTTP и не требует аутентификации.

Итоговое исходящее соединение от OTel Collector к Dynatrace всегда требует аутентификации и TLS.

### Сетевые требования

Убедитесь, что выполняются следующие условия:

* Сетевые порты не заблокированы

  Убедитесь, что сетевые порты, необходимые для настроенных экземпляров приёмников, не заблокированы брандмауэром или другим решением для управления сетью, используемым в вашей инфраструктуре.

## Похожие темы

* [Конечная точка приёма API OpenTelemetry Protocol (OTLP)](/managed/dynatrace-api/environment-api/opentelemetry "Используйте Dynatrace API в качестве целевой точки для экспортёров OpenTelemetry для приёма метрик, логов и трассировок OpenTelemetry.")