---
title: Trace Azure Functions written in Node.js
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs
scraped: 2026-03-06T21:37:47.614506
---

# Трассировка Azure Functions, написанных на Node.js

# Трассировка Azure Functions, написанных на Node.js

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 6 мин
* Обновлено 4 ноября 2025

Модуль [`@dynatrace/opentelemetry-azure-functions`](https://dt-url.net/9603x96) предоставляет API для трассировки Node.js в Azure Functions.

## Предварительные требования

Убедитесь, что вы выполнили шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions на плане потребления](opentelemetry-on-azure-functions.md "Мониторинг Azure Functions на плане потребления с помощью OpenTelemetry и Dynatrace."), прежде чем использовать указанные ниже пакеты.

* @dynatrace/opentelemetry-azure-functions версии 1.243+

## Установка

Для настройки интеграции OpenTelemetry Node.js в Azure Functions выполните следующую команду.

```
npm install --save @dynatrace/opentelemetry-azure-functions
```

## Экспорт трассировок

Azure Functions можно разрабатывать с использованием двух различных [моделей программирования](https://dt-url.net/9p03lmb), v3 и v4. Для учёта различий между двумя моделями Dynatrace предоставляет два способа экспорта трассировок:

* Для модели программирования v3 обработчик Azure Functions оборачивается (с помощью API `wrapHandler`) для генерации и экспорта трассировок.
* Для модели программирования v4 используются [хуки Azure Functions](https://dt-url.net/v323l3e) для достижения того же результата. Обратите внимание, что хуки доступны только для модели программирования v4.

Подробности см. ниже.

### Модель программирования v3

Для экспорта трассировок в Dynatrace из Azure Functions, разработанных с [моделью программирования v3](https://dt-url.net/n443lxw):

1. Выберите один из двух способов инициализации трассировки ниже.

   * `NodeTracerProvider` -- более легковесный, чем `NodeSDK`
   * `NodeSDK` -- обычно используется, если вас интересуют дополнительные сигналы OpenTelemetry, такие как метрики

   Можно объединить несколько Azure Functions в одном приложении Azure Function. Поэтому важно инициализировать трассировку только один раз для каждого приложения Azure Function, а не для каждой функции. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions JavaScript](https://dt-url.net/t223xf2), и подключать его в начале всех функций.

   Код настройки трассировки должен выполнять настройку только один раз, до подключения любых сторонних модулей.

   Пример NodeTracerProvider (рекомендуется)

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



   // tracing setup



   const exporter = new DtSpanExporter();



   const processor = new DtSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



   spanProcessors: [processor]



   // ...other configurations



   });



   provider.register({



   propagator: new DtTextMapPropagator(),



   // ...other configurations



   });
   ```

   Пример NodeSDK

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeSDK } from "@opentelemetry/sdk-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



   const sdk = new NodeSDK({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   spanProcessor: new DtSpanProcessor(new DtSpanExporter()),



   textMapPropagator: new DtTextMapPropagator(),



   // ...other configurations



   });



   sdk.start().then(() => {



   // Resources have been detected and SDK is started



   });
   ```
2. Оберните обработчик функции, как показано ниже, и экспортируйте обёрнутый обработчик.

   ```
   import type { AzureFunction, Context, HttpRequest } from "@azure/functions"



   // Import the wrapHandler function.



   import { wrapHandler } from "@dynatrace/opentelemetry-azure-functions";



   const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {



   // The created span is set as active by the OpenTelemetry ContextManager here



   context.log("HTTP trigger function processed a request.");



   const name = (req.query.name || (req.body && req.body.name));



   const responseMessage = name



   ? "Hello, " + name + ". This HTTP triggered function executed successfully."



   : "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.";



   context.res = {



   status: 200,



   body: responseMessage



   };



   };



   // Export the wrapped handler function.



   export default wrapHandler(httpTrigger);
   ```

### Модель программирования v4

Существует два способа экспорта трассировок в Dynatrace из Azure Functions, разработанных с [моделью программирования v4](https://dt-url.net/7t03lem).

* Использовать API `initDynatrace`.
* Инициализировать трассировку путём ручной регистрации хуков Azure Function.

Независимо от выбранного подхода инструментирования, всегда реализуйте код настройки трассировки так, чтобы он выполнялся только один раз, до подключения любых сторонних модулей.

#### Использование API `initDynatrace`

API `initDynatrace` регистрирует хуки Azure Function, необходимые для трассировки, и при необходимости регистрирует необходимые компоненты трассировки.

Это можно сделать с настройкой OpenTelemetry или без неё:

* initDynatrace с настройкой OpenTelemetry (рекомендуется)

  Передайте `true` в качестве первого аргумента `initDynatrace` для настройки трассировки и получения зарегистрированного NodeTracerProvider. Атрибуты ресурсов для провайдера можно передать вторым необязательным аргументом.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // initialize instrumentation with tracing setup



  const provider = initDynatrace(true, {



  "my.resource.attribute": "My Resource"



  });



  // azure functions registration goes here
  ```
* initDynatrace без настройки OpenTelemetry

  Вызовите `initDynatrace` без параметров для регистрации только необходимых хуков Azure Function и настройте трассировку вручную. Это удобно, если требуется кастомизация настройки трассировки.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  import { Resource } from "@opentelemetry/resources";



  import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



  import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const exporter = new DtSpanExporter();



  const processor = new DtSpanProcessor(exporter);



  const provider = new NodeTracerProvider({



  resource: new Resource({



  "my.resource.attribute": "My Resource"



  }),



  sampler: new DtSampler(),



  // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



  spanProcessors: [processor]



  // ...other configurations



  });



  provider.register({



  propagator: new DtTextMapPropagator(),



  // ...other configurations



  });



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

  Обратите внимание, что код настройки трассировки аналогичен модели программирования v3, и пример с NodeSDK (из модели v3 выше) также будет работать здесь. Для удобства существует API `configureDynatrace`, который делает то же самое, что и код выше.

  ```
  import { configureDynatrace, initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const provider = configureDynatrace({



  "my.resource.attribute": "My Resource"



  });



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

#### Инициализация трассировки путём ручной регистрации хуков Azure Function

В случаях, когда необходимо зарегистрировать дополнительные хуки Azure Functions, API `initDynatrace` может не подойти.

Поскольку хуки Azure Function выполняются в том же порядке, в котором они зарегистрированы, важно:

* Зарегистрировать хук Dynatrace Trace Start как первый хук pre-invocation
* Зарегистрировать хук Dynatrace Trace End как последний хук post-invocation

Время выполнения хуков включается в общее время выполнения функции. Если порядок зарегистрированных хуков неверный, время выполнения функции, отчитываемое нашим инструментированием, также будет неточным.

Подробнее о хуках Azure Function см. в [руководстве разработчика Azure Functions Node.js](https://dt-url.net/uo23lv1).

Чтобы упорядочить хуки по необходимости, можно использовать API `registerTraceStartHook` и `registerTraceEndHook`, как показано ниже.

```
import { app, PreInvocationContext, PostInvocationContext } from "@azure/functions";



import { configureDynatrace, registerTraceStartHook, registerTraceEndHook } from "@dynatrace/opentelemetry-azure-functions";



// setup tracing with configureDynatrace or manually



const provider = configureDynatrace();



// register Dynatrace Trace Start hook



registerTraceStartHook();



// register other user's pre-invocation hooks



app.hook.preInvocation(async (context: PreInvocationContext) => {



// hook code



});



// register other user's post-invocation hooks



app.hook.postInvocation(async (context: PostInvocationContext) => {



// hook code



});



// register Dynatrace Trace End hook



registerTraceEndHook();



// azure functions registration goes here
```

## Совместимость

| Версия OneAgent | OpenTelemetry API | OpenTelemetry SDK |
| --- | --- | --- |
| 1.243 - 1.255 | 1.x.y | 1.0.x |
| 1.257+ | 1.x.y | 1.0.x - 1.7.x |
| 1.259+ | 1.x.y | 1.0.x - 1.8.x |
| 1.261+ | 1.x.y | 1.0.x - 1.9.x |
| 1.265+ | 1.x.y | 1.0.x - 1.10.x |
| 1.273+ | 1.x.y | 1.0.x - 1.15.x |
| 1.279+ | 1.x.y | 1.0.x - 1.17.x |
| 1.283+ | 1.x.y | 1.0.x - 1.18.x |
| 1.285+ | 1.x.y | 1.0.x - 1.20.x |
| 1.289+ | 1.x.y | 1.0.x - 1.22.x |
| 1.293+ | 1.x.y | 1.0.x - 1.24.x |
| 1.297+ | 1.x.y | 1.0.x - 1.25.x |
| 1.303+ | 1.x.y | 1.0.x - 1.26.x |
| 1.307+ | 1.x.y | 1.0.x - 1.29.x |
| 1.313+ | 1.x.y | 1.0.x - 1.30.x |
| 1.327+ | 1.x.y | 1.0.x - 2.0.x |
| 1.331+ | 1.x.y | 1.0.x - 2.2.x |

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-azure-functions` поддерживает OpenTelemetry SDK V2. Для использования V2 (вместо V1) переопределите версию модуля `@dynatrace/opentelemetry-core` (требуемого `@dynatrace/opentelemetry-azure-functions`) на версию, поддерживающую OpenTelemetry SDK V2.

1. В таблице выше выберите версию, поддерживающую OpenTelemetry SDK V2.
2. В файле `package.json` добавьте раздел `overrides` и укажите одну из версий модуля `@dynatrace/opentelemetry-core` для принудительного применения.
3. Выполните `npm install` для применения изменений.

Пример:

```
{



"dependencies": {



"@dynatrace/opentelemetry-azure-functions": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Когда `@dynatrace/opentelemetry-azure-functions` будет изменён для использования OpenTelemetry SDK V2 по умолчанию, это переопределение больше не потребуется.

Поддерживаемая [среда выполнения Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):

* 4.x

Поддерживаемая [модель программирования Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):

* 3.x
* 4.x @dynatrace/opentelemetry-azure-functions версии 1.289+

## Ограничения

* Поддерживаются только обработчики функций `async`.

  + Это соответствует рекомендации Azure по использованию [`async` и `await`](https://dt-url.net/be03x31).
  + `wrapHandler` возвращает любую функцию без `async` без обёртки, поэтому сама функция будет работать, но спан не будет создан.
  + Обратите внимание, что асинхронные функции были введены в ECMAScript 2017. Спан не будет создан, если используется более ранняя версия ECMAScript. При использовании TypeScript убедитесь, что [целевая компиляция](https://dt-url.net/df02zbc) установлена на ECMAScript 2017 или выше.
* Пакет поддерживает только [план потребления](https://dt-url.net/ck022yx). Хотя он может работать на других планах, мы не можем гарантировать совместимость или производительность.
* Сигнализация о завершении функции с помощью устаревших вызовов [`context.done()`](https://dt-url.net/0l23xfy) или [`context.res.send()`](https://dt-url.net/dj43xgq) не поддерживается. Используйте привязку `$return` и возвращайте результат из обработчика функции, либо используйте именованную привязку `out` и установите `context.binding.<name>`. Для HTTP-триггеров также поддерживается установка `context.res`.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
