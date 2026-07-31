---
title: .NET
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/dotnet
---

# .NET

# .NET

* Справочник
* 3 мин чтения
* Обновлено 14 июля 2026 г.

Dynatrace OneAgent инструментирует .NET-приложения, расставляя трассировочные операторы в ключевых точках кода для трассировки кода, сбора метрик производительности, обнаружения ошибок, отслеживания зависимостей и прочего.

Не каждое обнаруженное .NET-приложение инструментируется по умолчанию. Dynatrace поддерживает набор правил для инструментирования конкретных процессов (например, пулов приложений IIS, которые можно расширить собственными правилами). Основы настройки мониторинга группы процессов (автоматический глубокий мониторинг, пользовательские правила мониторинга, встроенные правила мониторинга) описаны в разделе [Настройка мониторинга группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Способы настройки мониторинга группы процессов").

## Возможности

Dynatrace предоставляет широкие возможности мониторинга .NET:

* [Поддержка OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-dotnet) для захвата трасс и приёма метрик.  
  Подробнее: [Инструментирование .NET-приложения с помощью OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/dotnet "Узнайте, как инструментировать .NET-приложение с помощью OpenTelemetry и Dynatrace.")
* Сквозная трассировка транзакций для запросов к веб-сервисам, сервисам удалённого взаимодействия, очередям и базам данных. [Подробнее о сервисах](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать сервисы, определять и использовать атрибуты запросов и многое другое.")
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет инструментировать приложение вручную для расширения сквозной видимости в фреймворках и технологиях, для которых кодовый модуль ещё недоступен.") для пользовательской трассировки
* Сборка мусора, метрики процессов и многое другое
* [Непрерывное профилирование CPU уровня production 24x7﻿](https://www.dynatrace.com/news/blog/analyze-cpu-consumption-background-threads/)

Перечень поддерживаемых фреймворков: [матрица поддерживаемых технологий](/managed/ingest-from/technology-support#net "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Поддерживаемые версии .NET

| Версия | Дата выпуска вендором | Конец поддержки вендором | Первая поддерживаемая версия Dynatrace OneAgent | Последняя поддерживаемая версия Dynatrace OneAgent | Поддержка Dynatrace до | [Уровень поддержки Dynatrace](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 2025-11-11 | - | 1.325 | - | - | Supported |
| 9 | 2024-11-12 | - | 1.305 | - | - | Supported |
| 8 | 2023-11-14 | - | 1.277 | - | - | Supported |
| 7 | 2022-11-08 | - | 1.263 | - | - | Supported |
| 6 | 2021-11-08 | - | 1.229 | - | - | Supported |
| 5 | 2020-11-10 | - | 1.203 | - | - | Supported |
| Core 3.1 | 2019-12-03 | - | 1.183 | - | - | Supported |
| Core 3.0 | 2019-09-23 | - | 1.177 | - | - | Supported |
| Core 2.2 | - | 2019-12-23 | - | - | - | Supported |
| Core 2.1 | - | - | - | - | - | Supported |
| Core 2.0 | - | 2018-10-01 | - | 1.297 | 2024-08-31 | Limited[1](#fn-net-and-net-core-1-def) |
| Core 1.1 | - | 2019-06-27 | - | 1.177 | 2019-12-01 | Not supported |
| Core 1.0 | - | 2019-06-27 | - | 1.177 | 2019-12-01 | Not supported |

1

Ограниченная поддержка: Dynatrace может решать только те проблемы, которые воспроизводятся на поддерживаемых версиях.

## Поддерживаемые версии .NET Framework

| Версия | Дата выпуска вендором | Конец поддержки вендором | Первая поддерживаемая версия Dynatrace OneAgent | Последняя поддерживаемая версия Dynatrace OneAgent | Поддержка Dynatrace до | [Уровень поддержки Dynatrace](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 4.5.2 - 4.8 | - | - | - | - | - | Supported |
| 4.5.1 | - | 2016-01-12 | - | - | - | Limited[1](#fn-net-framework-1-def) |
| 4.5 | - | 2016-01-12 | - | - | - | Limited[1](#fn-net-framework-1-def) |
| 4 | - | 2016-01-12 | - | - | - | Limited[1](#fn-net-framework-1-def) |
| 3.5 SP1 | - | - | - | - | - | Supported |

1

Ограниченная поддержка: Dynatrace может решать только те проблемы, которые воспроизводятся на поддерживаемых версиях.

## Жизненный цикл поддержки

Dynatrace поддерживает каждую версию в течение её официального срока поддержки:

* См. [жизненный цикл поддержки Microsoft для .NET и .NET Core﻿](https://docs.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core).
* См. [жизненный цикл поддержки Microsoft для .NET Framework﻿](https://docs.microsoft.com/en-us/lifecycle/products/microsoft-net-framework).

## Ограничения

### Хотспоты методов в Linux

Кодовый модуль .NET использует сигналы POSIX для захвата стектрейсов в функции хотспотов методов.

Поскольку эти сигналы могут прерывать приложение в произвольные моменты, некоторые приложения и библиотеки (в особенности .NET-библиотеки с нативными зависимостями) могут работать некорректно при включённых функциях хотспотов методов.

Затронутое приложение может проявлять следующие симптомы:

* Проблемы с подключением
* Повреждённые текстовые данные
* Kubernetes readiness и liveness probes завершаются с ошибкой

Единственное текущее решение, отключить соответствующие функции OneAgent для затронутой группы процессов:

* Capture method hotspot information in PurePaths
* Capture background CPU method hotspot information
* .NET Async Method Hotspots

Хотспоты методов могут некорректно захватывать стектрейсы в операционных системах на базе musl-libc, например Alpine. Это связано с тем, что библиотека musl-libc удаляет часть отладочной информации. Переход на операционную систему на базе glibc (Debian/Ubuntu) позволяет устранить эту конкретную проблему.

* Хотспоты методов .NET недоступны для Linux на ARM64 (AArch64).

### Trimming

Опциональная функция .NET [trimmed self-contained deployments and executables﻿](https://docs.microsoft.com/en-us/dotnet/core/deploying/trim-self-contained) была введена для оптимизации размера упакованных приложений.
Начиная с версии OneAgent 1.337+, trimmed self-contained deployments поддерживаются при наличии ссылки на пакет NuGet [Dynatrace.OneAgent.Trimming﻿](https://www.nuget.org/packages/Dynatrace.OneAgent.Trimming) в приложении. Настоятельно рекомендуется использовать последнюю версию пакета, чтобы иметь доступ к актуальным функциям.

### Однофайловые приложения

.NET SDK поддерживает сборку приложения в виде [единого файла﻿](https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/overview?tabs=cli), объединяющего все зависимости в один платформозависимый исполняемый файл.

В зависимости от того, используется ли [framework-dependent deployment﻿](https://learn.microsoft.com/en-us/dotnet/core/deploying/#publish-framework-dependent) или [self-contained applications﻿](https://learn.microsoft.com/en-us/dotnet/core/deploying/#publish-self-contained), среда выполнения также может быть включена в исполняемый файл.

Такие приложения поддерживаются начиная с версии OneAgent 1.343+ при использовании функции "Instrument .NET Single-File Self-Contained applications", которая также требует включения функции "Advanced .NET Instrumentation Mode".
В Linux и Alpine Dynatrace не поддерживает версии среды выполнения .NET 10 от 10.0.0 до 10.0.8 для Single-File Self-Contained приложений.