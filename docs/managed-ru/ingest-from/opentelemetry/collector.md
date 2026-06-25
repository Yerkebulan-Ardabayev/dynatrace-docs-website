---
title: OTel Collector для приёма телеметрии в Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector
scraped: 2026-05-12T12:00:51.847493
---

# OTel Collector для приёма телеметрии в Dynatrace

# OTel Collector для приёма телеметрии в Dynatrace

* Обзор
* Чтение: 5 мин
* Обновлено 28 апреля 2026 г.

OTel Collector (или просто "Collector"), сетевое сервисное приложение, позволяет группировать и преобразовывать данные телеметрии. Оно работает как прокси: принимает запросы OTLP, а также данные из других источников, преобразует их по заданным правилам и пересылает в бэкенд.

На следующей схеме показаны различные компоненты, которые Collector может использовать для приёма, обработки и экспорта данных телеметрии в Dynatrace.

![The OTel Collector can receive, process, and export telemetry data to Dynatrace](https://cdn.bfldr.com/B686QPH3/as/5b86f3jgqb7frz6rtb85hjc/OpenTelemetry_-_Dynatrace_Collector_-_Light_Mode?auto=webp&format=png&position=1)

Конвейер OTel Collector

## Преимущества использования Collector

В целом использование Collector совместно с сервисом может быть выгодно, поскольку позволяет сервису быстро выгружать данные, а Collector берёт на себя дополнительную обработку (повторные попытки, группирование, шифрование, фильтрацию конфиденциальных данных). Общие задачи обработки централизуются, а не дублируются в каждом приложении.

Collector следует использовать, если:

* Нужно собирать данные из различных источников в разных форматах и требуется простой способ доставить их все в бэкенд, который иначе был бы несовместим.
* Необходима общая обработка атрибутов данных телеметрии.

Collector, относительно лёгкий компонент, позволяет командам развёртывать собственные экземпляры, не используя одну общую конфигурацию.

Collector настраивается в одном YAML-файле. Это устраняет необходимость просматривать несколько файлов и упрощает обслуживание. Дополнительные сведения о настройке см. в разделе [Настройка OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.").

## Дистрибутивы

Collector поставляется в нескольких вариантах дистрибутива с различными параметрами установки и развёртывания.

| Тип | Когда использовать? |
| --- | --- |
| Dynatrace OTel Collector Recommended | Предпочтительный выбор для большинства сценариев использования. Поставляется с набором проверенных и стабильных компонентов Collector, типично применяемых в конфигурациях Dynatrace. |
| Core | Когда нужно в первую очередь выполнять преобразование между протоколами OTLP (например, конвертацию между HTTP и gRPC, см. [Преобразование OTLP gRPC в HTTP с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Настройте OpenTelemetry Collector для преобразования запроса gRPC OTLP в HTTP.")), применять ограничения использования памяти или группировать запросы. |
| Contrib | Идеально подходит для тестовых конфигураций, поскольку содержит все сторонние компоненты и не требует пользовательской сборки. Как правило, не рекомендуется для производственных систем, так как обычно потребляет больше ресурсов и может быть менее стабильным, чем оптимизированный экземпляр Builder. |
| Collector Builder | Когда нужно полностью настроить экземпляр Collector и запускать только компоненты, необходимые для вашего сценария использования. |

### Dynatrace OTel Collector

Дистрибутив Dynatrace для OpenTelemetry (OTel) Collector представляет собой специализированную сборку Collector, предоставляемую Dynatrace. Он адаптирован для типичных сценариев использования в контексте Dynatrace и поставляется с оптимизированным и проверенным набором компонентов Collector.

#### Преимущества Dynatrace OTel Collector

Dynatrace OTel Collector предлагает следующие преимущества по сравнению с другими дистрибутивами Collector.

* Поддерживается командой Dynatrace, см. [Поддержка Dynatrace OTel Collector](#support).
* Компоненты Collector проверены Dynatrace.
* Патчи безопасности выпускаются независимо от релизов OTel Collector.

Dynatrace OTel Collector сохраняет стандартную модель конфигурации и семантику компонентов.
Отказавшись от проприетарных абстракций и скрытых значений по умолчанию, он позволяет как людям, так и ИИ-агентам надёжно повторно использовать стандартные справочные материалы и примеры OpenTelemetry с меньшим числом ошибок.

#### Поддержка Dynatrace OTel Collector

Сборки x86-64 и ARM64 дистрибутива Dynatrace OTel Collector поддерживаются командой Dynatrace Support в соответствии с [политикой поддержки Dynatrace](https://support.dynatrace.com/).

Для получения полной поддержки обращайтесь в Dynatrace через официальные каналы поддержки.
Проблемы, сообщённые через GitHub, обрабатываются по принципу "наилучших усилий"; контракты поддержки и SLA не применяются.

Каждая минорная версия поддерживается в течение трёх месяцев.
Исправления предоставляются либо в виде патч-релиза для последней поддерживаемой минорной версии, либо в составе последующего минорного релиза.

#### Компоненты Dynatrace OTel Collector

Полный список предоставляемых компонентов см. на странице [Components](https://github.com/Dynatrace/dynatrace-otel-collector#components).

#### Сценарии использования Dynatrace OTel Collector

Конкретные примеры сценариев использования и конфигурации для отдельных компонентов см. в разделе [Сценарии использования OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases "Настройте экземпляр OpenTelemetry Collector для различных сценариев использования.").

#### Развёртывание Dynatrace OTel Collector

Чтобы развернуть Dynatrace OTel Collector, следуйте шагам, описанным в разделе [Развёртывание Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OpenTelemetry Collector.").

Dynatrace OTel Collector поставляется со специальными компонентами, описанными в [репозитории GitHub Dynatrace OTel Collector](https://github.com/Dynatrace/dynatrace-otel-collector/).

### Дистрибутивы OpenTelemetry

Dynatrace обеспечивает ограниченную поддержку конфигураций Core, Contrib и Builder.
Эта поддержка распространяется только на компоненты и их версии, включённые в Dynatrace OTel Collector.

Полностью поддерживаемый дистрибутив Collector см. в разделе [Dynatrace OTel Collector](#dt-collector-dist).

#### Collector Core

Дистрибутив [Core](https://github.com/open-telemetry/opentelemetry-collector) содержит базовый прокси-сервис и несколько фундаментальных сервисных компонентов.
В их числе:

* receiver для данных протокола OpenTelemetry (OTLP) через HTTP и gRPC.
* processor для группирования запросов и соблюдения ограничений использования памяти.
* exporter для вывода в консоль и OTLP через HTTP и gRPC.

#### Collector Contrib

Дистрибутив [Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) построен поверх Core и расширяет его функциональность за счёт большого числа дополнительных receiver, processor и exporter, предоставленных третьими сторонами.

Поскольку дистрибутив Contrib является комплексным пакетом и поставляется со всеми сервисными компонентами в предварительно скомпилированном виде, он может потреблять больше системных ресурсов (дисковое пространство и память), чем оптимизированная сборка Collector.

Dynatrace рекомендует использовать дистрибутив Contrib только в целях тестирования.
Его не следует применять в производственных средах.

#### Collector Builder

Помимо двух дистрибутивов, OpenTelemetry предлагает [OpenTelemetry Collector Builder (OCB)](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/cmd/builder), инструмент командной строки для создания собственной настроенной версии Collector.

## Компоненты

### Receiver

receiver: компонент, позволяющий данным поступать в Collector. Он может принимать данные из нескольких источников. Многие receiver поставляются с настройками по умолчанию и не требуют значительной конфигурации.

Список доступных receiver и их базовую конфигурацию см. в официальной [документации OpenTelemetry по receiver](https://opentelemetry.io/docs/collector/configuration/#receivers).

### Processor Optional

processor: необязательный компонент, который преобразует, фильтрует или обогащает данные перед экспортом.

Список доступных processor и их базовую конфигурацию см. в официальной [документации OpenTelemetry по processor](https://opentelemetry.io/docs/collector/configuration/#processors). В OpenTelemetry есть список [рекомендуемых processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor#recommended-processors), однако они необязательны.

### Exporter

exporter: компонент, отправляющий обработанные данные в один или несколько бэкендов. exporter может поддерживать более одного источника данных.

Поскольку многие exporter требуют дополнительной настройки (например, эндпоинта), обязательно ознакомьтесь с официальной [документацией OpenTelemetry по exporter](https://opentelemetry.io/docs/collector/configuration/#exporters) для просмотра списка доступных exporter и их конфигураций.

### Services

Services определяют конвейеры, направляющие данные через Collector. Они задают, какие компоненты работают совместно для обработки данных OpenTelemetry.