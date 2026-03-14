---
title: Интеграция в Google Cloud Functions .NET
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet
scraped: 2026-03-05T21:29:29.015445
---

# Интеграция с Google Cloud Functions .NET

# Интеграция с Google Cloud Functions .NET

* Последняя версия Dynatrace
* Практическое руководство
* 3 мин. чтения
* Опубликовано 25 июля 2023 г.

NuGet-пакет `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` предоставляет API для трассировки серверных вызовов .NET Google Cloud Function (GCF).

## Предварительные условия

* [Настройте мониторинг Google Cloud Functions с помощью OpenTelemetry](opentelemetry-on-gcf.md "Мониторинг Google Cloud Functions с помощью OpenTelemetry и Dynatrace.").
* Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions версии 1.273+
* Версии Cloud Functions: 1-е поколение, 2-е поколение

## Установка

Для настройки интеграции OpenTelemetry .NET с Google Cloud Functions выполните приведённую ниже команду в корневом каталоге вашего проекта Google Cloud Function.

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions
```

Эта команда добавляет последнюю версию NuGet-пакета `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` в качестве зависимости вашего проекта.

## Экспорт трассировок

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Инициализация трассировки**](opentelemetry-on-gcf-dotnet.md#initialize "Мониторинг Google Cloud Functions с помощью OpenTelemetry для .NET и Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Инструментирование функции-обработчика**](opentelemetry-on-gcf-dotnet.md#instrument "Мониторинг Google Cloud Functions с помощью OpenTelemetry для .NET и Dynatrace.")

## Шаг 1. Инициализация трассировки

Код инициализации трассировки GCF в файле `Function.cs` может выглядеть следующим образом (где `Function` — настроенный класс-обработчик GCF):

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions;



using Google.Cloud.Functions.Framework;



using Microsoft.AspNetCore.Http;



using OpenTelemetry;



using OpenTelemetry.Trace;



namespace Examples.GcfFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



static Function()



{



DynatraceSetup.InitializeLogging();



TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



.AddGoogleCloudFunctionsInstrumentation()



.Build();



}



}



}
```

## Шаг 2. Инструментирование функции-обработчика

Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions версии 1.273. Поддерживается только трассировка входящих вызовов для HTTP-функций.

Чтобы инструментировать HTTP-функцию для трассировки входящих вызовов, помимо [приведённого выше кода инициализации](#initialization), оберните метод-обработчик GCF с помощью `GoogleCloudFunctionsWrapper.Trace` или `GoogleCloudFunctionsWrapper.TraceAsync`, как показано в следующем примере.

```
public Task HandleAsync(HttpContext context)



{



return GoogleCloudFunctionsWrapper.TraceAsync(



TracerProvider,



() => HandleInternalAsync(context), context);



}



private Task HandleInternalAsync(HttpContext context)



{



// This is just an example of function handler and should be replaced by actual code.



return Task.CompletedTask;



}
```

## Холодный старт

При первом вызове обработчика функции после [холодного старта](https://cloud.google.com/functions/docs/concepts/exec#cold_starts) метод инициализации инструментирования `AddGoogleCloudFunctionsInstrumentation` выполняет дополнительные HTTP-запросы для получения метаданных из вашей [среды Google Cloud](https://cloud.google.com/compute/docs/metadata/overview). Эти метаданные используются для установки необходимых атрибутов, чтобы Dynatrace мог обработать спан ("Activity" в терминологии .NET).

### Ограничения

Дополнительные HTTP-запросы метода `AddGoogleCloudFunctionsInstrumentation` могут вызвать необработанные исключения на этапе инициализации (например, `HttpRequestException` в случае разрыва сетевого соединения). Если ваш код настроен на отключение мониторинга при сбое запуска, исключения всё равно будут перехвачены.

## Отправка спанов

По умолчанию все методы-обёртки `Trace/TraceAsync` автоматически выполняют операцию сброса перед завершением вызова функции, чтобы гарантировать правильный экспорт всех спанов. Поскольку сброс спанов становится частью логики выполнения функции, это может привести к увеличению времени выполнения.

Чтобы отключить сброс после каждого вызова, вы можете передать параметр конфигурации с флагом `ForceFlushAfterEachInvocation`, установленным в `false`, в методе `AddGoogleCloudFunctionsInstrumentation`. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.

```
TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



// Setting ForceFlushAfterEachInvocation to false disables the flushing after every function invocation.



.AddGoogleCloudFunctionsInstrumentation(c => c.ForceFlushAfterEachInvocation = false)



.Build();
```

Поскольку выполнение кода за пределами функции может быть прервано в любой момент, Google Cloud Functions не рекомендует такой подход.

* Google Cloud Functions 1-го поколения

  Выполнение фоновых задач после вызова функции не гарантируется без сброса спанов и может привести к потере спанов. На практике примеры показывают, что без явного сброса спаны обычно всё равно экспортируются корректно.
* Google Cloud Functions 2-го поколения

  Google Cloud Functions 2-го поколения может обрабатывать несколько одновременных запросов в одном экземпляре функции. Операция сброса одного вызова может продлить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно должны оставаться в режиме ожидания для обработки нескольких одновременных запросов, вы можете отключить сброс спанов для повышения производительности. Подробнее см. [Жизненный цикл экземпляра](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание, что выделение CPU для экземпляров функций в режиме ожидания не гарантируется, если режим [выделения CPU](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в значение `CPU always allocated`.

  Подробнее см. [Временная шкала выполнения функции](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Накладные расходы Dynatrace

* Поскольку экспорт спанов и получение метаданных требуют времени при холодном старте, они увеличивают длительность выполнения функции и, следовательно, расходы.
* Обратите внимание на редко вызываемые функции (обычно с холодным стартом), которым может потребоваться больше времени для установления TCP-соединения при экспорте спанов.
* Любые сетевые проблемы между экспортёром и бэкендом Dynatrace также могут привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](../../../google-cloud-platform.md "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)