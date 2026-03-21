---
title: Конечные точки Dynatrace OTLP API
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api
scraped: 2026-03-06T21:23:20.064492
---

* Latest Dynatrace
* Объяснение

[OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) — это основной сетевой протокол для обмена телеметрическими данными между сервисами и приложениями, работающими на основе OpenTelemetry.

Dynatrace предоставляет нативные конечные точки OTLP через следующие сервисы:

* Платформа Dynatrace SaaS.
* Экземпляры ActiveGate.

В качестве альтернативы вы можете развернуть [Dynatrace Collector](collector.md "Узнайте о Dynatrace OTel Collector.") как промежуточный сервис для пакетирования запросов и повышения сетевой производительности или для преобразования запросов перед их отправкой в Dynatrace (например, [маскирование конфиденциальных данных](collector/use-cases/redact.md "Настройте OpenTelemetry Collector для маскирования конфиденциальных данных перед отправкой в Dynatrace.")).

## Стандартные пути приёма данных

Пути приёма данных, используемые Dynatrace для отдельных типов сигналов, соответствуют [стандартным путям OpenTelemetry](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).

| Тип сигнала | Путь |
| --- | --- |
| Трассировки | `/v1/traces` |
| Метрики | `/v1/metrics` |
| Логи | `/v1/logs` |

В зависимости от конфигурации вам может потребоваться добавить эти пути отдельно к базовым URL-адресам следующих конечных точек сервисов при указании URL-адресов экспорта. Это может происходить как в коде при использовании [ручного инструментирования](walkthroughs.md "Узнайте, как интегрировать и передавать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace."), так и с использованием стандартных [переменных окружения](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).

## Экспорт в Dynatrace

### Базовые URL-адреса

Следующие адреса предоставляют базовые URL-адреса для конфигурации приёма OTLP. Используйте URL-адрес, соответствующий типу вашей среды, и замените соответствующую часть вашим [идентификатором среды](../../discover-dynatrace/get-started/monitoring-environment.md "Узнайте, как работать со средами мониторинга.").
Базовый URL-адрес также используется при определении переменной окружения `OTEL_EXPORTER_OTLP_ENDPOINT`, см. [Переменные окружения](#environment-variables).

| Тип API | Базовый URL |
| --- | --- |
| Dynatrace SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |
| Контейнеризированный Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |

1

Environment ActiveGate по умолчанию прослушивает порт `9999`. Если вы изменили этот порт, скорректируйте порт в URL-адресе соответствующим образом.

2

Для этой конфигурации требуется [PVC](../setup-on-k8s/guides/deployment-and-configuration/activegate-pvc.md "Настройте постоянное хранилище для контейнеризированного ActiveGate, используемого в качестве временного хранилища для принимаемых данных.").

Если вы копируете идентификатор среды из адресной строки браузера, убедитесь, что вы удалили `.apps`.

* Неправильный базовый URL: `https://{your-environment-id}.live.apps.dynatrace.com/api/v2/otlp`
* Правильный базовый URL: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`

В противном случае вызовы API вернут ошибку следующего вида:

```
not retryable error: Permanent error: rpc error: code = Unimplemented desc = error exporting items, request to https://<environment>.live.apps.dynatracelabs.com/api/v2/otlp/v1/logs responded with HTTP Status Code 404
```

### Примеры URL-адресов

Следующие примеры URL-адресов иллюстрируют комбинации базовых URL-адресов и путей для типов сигналов.

#### Dynatrace SaaS

#### Environment ActiveGate

Обогащение информации

Стандартный экспорт OTLP в ActiveGate требует ручного обогащения информацией о хосте Dynatrace для получения корректной топологической информации.

Для этого убедитесь, что ваши трассировки имеют правильные атрибуты ресурсов для сопоставления. Список применимых атрибутов можно найти (или импортировать) в [файлах обогащения](../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать телеметрические данные специфичными для Dynatrace полями.").

### Ограничения API

Вызовы конечных точек Dynatrace API имеют следующие ограничения.

* gRPC не поддерживается.
  Вызовы API должны использовать HTTP.
  Вы можете использовать Collector для преобразования gRPC OTLP-запроса в его HTTP-аналог, см. [Преобразование OTLP gRPC в HTTP с помощью OpenTelemetry Collector](collector/use-cases/grpc.md "Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.").
* JSON не поддерживается для Protocol Buffers.
  Необходимо использовать бинарный формат.

### Переменные окружения

При настройке приложения для экспорта в Dynatrace один из способов — настроить определённые переменные окружения, как описано ниже.

```
OTEL_EXPORTER_OTLP_ENDPOINT=[YOUR_BASE_URL]


OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [YOUR_TOKEN]"


OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

Подробнее о конфигурации для конкретных языков см. [Инструментирование приложения](walkthroughs.md "Узнайте, как интегрировать и передавать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

### Аутентификация и токены доступа

Для экспорта в SaaS и ActiveGate аутентификация выполняется с помощью токена доступа API и HTTP-заголовка `Authorization`.
Подробнее о токенах доступа см. [Dynatrace API — токены и аутентификация](../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Чтобы создать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
Используйте соответствующие области доступа для сигналов, которые вы хотите экспортировать.
Вы можете объединить области в одном токене, а также добавить области к существующему токену.

* Трассировки: `openTelemetryTrace.ingest`
* Метрики: `metrics.ingest`
* Логи: `logs.ingest`

### Сетевые требования

Убедитесь, что выполнены следующие условия:

* TCP-порт не заблокирован

  Поскольку обмен данными OTLP с ActiveGate осуществляется через порты 443 (для SaaS и Managed) или 9999 (для Environment ActiveGate), убедитесь, что соответствующий TCP-порт не заблокирован брандмауэром или другими используемыми вами средствами управления сетью.
* Хранилище доверенных сертификатов вашей системы актуально

  Чтобы избежать возможных проблем с SSL-сертификатами из-за истёкших или отсутствующих корневых сертификатов по умолчанию, убедитесь, что хранилище доверенных сертификатов вашей системы актуально.

## Экспорт в Collector

Использование Collector в качестве промежуточного шлюза позволяет централизованно оптимизировать телеметрические данные и запросы. Подробнее см. [Сценарии использования OpenTelemetry Collector](collector/use-cases.md "Настройте экземпляр Collector для различных сценариев использования.") и примеры конфигураций для популярных сценариев использования Collector.

Подробнее о настройке экземпляра Collector см. [Dynatrace OTel Collector](collector.md "Узнайте о Dynatrace OTel Collector.").

Преобразование gRPC

Поскольку Dynatrace в настоящее время требует экспорт OTLP через HTTP, вы можете использовать Collector для преобразования экспорта gRPC в HTTP.

Подробнее см. [Преобразование OTLP gRPC в HTTP с помощью OpenTelemetry Collector](collector/use-cases/grpc.md "Настройте OpenTelemetry Collector для преобразования gRPC OTLP-запроса в HTTP.").

### Аутентификация и TLS

Необходимость использования TLS и аутентификации запросов к Collector зависит от конкретной настройки/конфигурации Collector. По умолчанию [OTLP receiver](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/receiver/otlpreceiver/README.md) настроен для незашифрованного HTTP и не требует аутентификации.

Исходящее соединение от Collector к Dynatrace всегда требует аутентификации и TLS.

### Сетевые требования

Убедитесь, что выполнены следующие условия:

* Сетевые порты не заблокированы

  Убедитесь, что сетевые порты, необходимые для настроенных экземпляров receiver, не заблокированы брандмауэром или другими средствами управления сетью, используемыми в вашей инфраструктуре.

## Связанные темы

* [OpenTelemetry Protocol (OTLP) ingest API](../../dynatrace-api/environment-api/opentelemetry.md "Используйте Dynatrace API в качестве целевой точки для экспортёров OpenTelemetry для приёма метрик, логов и трассировок OpenTelemetry.")
