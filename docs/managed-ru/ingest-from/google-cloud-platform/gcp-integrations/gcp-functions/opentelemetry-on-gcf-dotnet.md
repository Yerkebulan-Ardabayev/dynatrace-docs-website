---
title: Интеграция на Google Cloud Functions .NET
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet
scraped: 2026-05-12T11:51:54.147702
---

# Интеграция на Google Cloud Functions .NET

# Интеграция на Google Cloud Functions .NET

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 25 июля 2023 г.

Пакет NuGet `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` предоставляет API для трассировки серверных вызовов .NET Google Cloud Function (GCF).

## Предварительные требования

* [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.").
* Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions версии 1.273+
* Версии продукта Cloud Functions: 1st gen, 2nd gen

## Установка

Чтобы настроить интеграцию OpenTelemetry для .NET на Google Cloud Functions, выполните следующую команду в корневой директории проекта Google Cloud Function.

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions
```

Это добавляет последнюю версию пакета NuGet `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` как зависимость проекта.

## Экспорт трассировок

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Инициализация трассировки**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#initialize "Мониторинг Google Cloud Functions с OpenTelemetry для .NET и Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Инструментирование функции-обработчика**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#instrument "Мониторинг Google Cloud Functions с OpenTelemetry для .NET и Dynatrace.")

## Шаг 1 Инициализация трассировки

Код инициализации трассировки GCF в файле `Function.cs` может выглядеть следующим образом (где `Function` является настроенным классом-обработчиком GCF):

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

## Шаг 2 Инструментирование функции-обработчика

Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions версии 1.273 Поддерживается только трассировка входящих вызовов для HTTP-функций.

Для инструментирования HTTP-функции с целью трассировки входящих вызовов, в дополнение к [коду инициализации выше](#initialization), оберните метод-обработчик функции GCF с помощью `GoogleCloudFunctionsWrapper.Trace` или `GoogleCloudFunctionsWrapper.TraceAsync`, как показано в следующем примере.

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

При первом вызове обработчика функции после [холодного старта](https://cloud.google.com/functions/docs/concepts/exec#cold_starts) метод инициализации инструментирования `AddGoogleCloudFunctionsInstrumentation`
выполняет дополнительные HTTP-запросы для получения метаданных из [среды Google Cloud](https://cloud.google.com/compute/docs/metadata/overview). Эти метаданные используются для задания необходимых атрибутов, по которым Dynatrace обрабатывает
спан ("Activity" в терминологии .NET).

### Ограничения

Дополнительные HTTP-запросы метода `AddGoogleCloudFunctionsInstrumentation` могут вызвать необработанные исключения на этапе инициализации (например, `HttpRequestException` при нарушении сетевого соединения). Если в коде предусмотрено отключение мониторинга при сбое запуска, исключения всё равно будут перехвачены.

## Сброс спанов

По умолчанию все оборачивающие методы `Trace/TraceAsync` автоматически выполняют операцию сброса перед завершением вызова функции для корректного экспорта всех спанов. Поскольку сброс спанов становится частью логики выполнения функции, это может увеличить время выполнения.

Чтобы отключить сброс после каждого вызова, передайте параметр конфигурации с флагом `ForceFlushAfterEachInvocation`, равным `false`, в метод `AddGoogleCloudFunctionsInstrumentation`. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.

```
TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



// Setting ForceFlushAfterEachInvocation to false disables the flushing after every function invocation.



.AddGoogleCloudFunctionsInstrumentation(c => c.ForceFlushAfterEachInvocation = false)



.Build();
```

Поскольку код, выполняемый вне контекста функции, может быть завершён в любой момент, Google Cloud Functions не рекомендует такой подход.

* Google Cloud Functions 1st gen

  Выполнение фоновых задач после вызова функции без сброса спанов не гарантировано и может привести к потере спанов. Практика показывает, что в большинстве случаев спаны корректно экспортируются даже без явного сброса.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen поддерживает обработку нескольких одновременных запросов в рамках одного экземпляра функции. Операция сброса одного вызова может увеличить время выполнения другого.
  Так как экземпляры функции обычно должны оставаться в режиме ожидания для обработки параллельных запросов, можно отключить сброс спанов для повышения производительности. Подробнее см. [Instance lifecycle](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание: простаивающим экземплярам функции не гарантируется выделение CPU, если режим [CPU allocation](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в `CPU always allocated`.

  Подробнее см. [Function execution timeline](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Накладные расходы Dynatrace

* Экспорт спанов и получение метаданных при холодных стартах занимают время, увеличивая продолжительность выполнения функции и соответственно затраты.
* Обратите особое внимание на редко вызываемые функции (как правило, с холодными стартами): они могут требовать больше времени на TCP-рукопожатие при экспорте спанов.
* Любые сетевые проблемы между экспортером и бэкендом Dynatrace также могут привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с Dynatrace.")
* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)