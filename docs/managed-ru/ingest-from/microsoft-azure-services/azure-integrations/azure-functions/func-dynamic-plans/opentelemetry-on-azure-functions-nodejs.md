---
title: Трассировка Azure Functions на Node.js
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs
scraped: 2026-05-12T12:07:43.833171
---

# Трассировка Azure Functions на Node.js

# Трассировка Azure Functions на Node.js

* Практическое руководство
* Чтение: 6 мин
* Обновлено 4 ноября 2025 г.

Модуль [`@dynatrace/opentelemetry-azure-functions`](https://dt-url.net/9603x96) предоставляет API для трассировки Node.js на Azure Functions.

## Предварительные требования

Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.").

* @dynatrace/opentelemetry-azure-functions версии 1.243+

## Установка

Чтобы настроить интеграцию OpenTelemetry для Node.js на Azure Functions, выполните следующую команду.

```
npm install --save @dynatrace/opentelemetry-azure-functions
```

## Экспорт трассировки

Azure Functions можно разрабатывать с использованием одной из двух [моделей программирования](https://dt-url.net/9p03lmb): v3 и v4. Для учёта различий между ними Dynatrace предоставляет два способа экспорта трассировки:

* Для модели программирования v3 обработчик Azure Functions оборачивается (с помощью API `wrapHandler`) для генерации и экспорта трассировок.
* Для модели программирования v4 для той же цели используются [Azure Functions Hooks](https://dt-url.net/v323l3e). Обратите внимание, что хуки доступны только для модели программирования v4.

Подробнее см. ниже.

### Модель программирования v3

Для экспорта трассировок в Dynatrace из Azure Functions, разработанных с использованием [модели программирования v3](https://dt-url.net/n443lxw):

1. Выберите один из двух способов инициализации трассировки.

   * `NodeTracerProvider`: более лёгкий вариант по сравнению с `NodeSDK`
   * `NodeSDK`: как правило, используется при необходимости работы с дополнительными сигналами OpenTelemetry, например с метриками

   Несколько Azure Functions можно объединить в одно приложение Azure Function app. Поэтому важно инициализировать трассировку один раз на уровне приложения, а не отдельно для каждой функции. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions для JavaScript](https://dt-url.net/t223xf2), и подключить его в начале всех функций.

   Код настройки трассировки должен выполняться ровно один раз до подключения любых сторонних модулей.

   Пример с NodeTracerProvider (рекомендуется)

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

   Пример с NodeSDK

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

Существует два способа экспорта трассировок в Dynatrace из Azure Functions, разработанных с использованием [модели программирования v4](https://dt-url.net/7t03lem).

* Использование API `initDynatrace`.
* Инициализация трассировки путём регистрации хуков Azure Function вручную.

Независимо от выбранного подхода к инструментированию, код настройки трассировки всегда должен выполняться ровно один раз до подключения любых сторонних модулей.

#### Использование API `initDynatrace`

API `initDynatrace` регистрирует хуки Azure Function, необходимые для трассировки, и при необходимости регистрирует требуемые компоненты трассировки.

Это можно сделать как с настройкой OpenTelemetry, так и без неё:

* initDynatrace с настройкой OpenTelemetry (рекомендуется)

  Передайте `true` в качестве первого аргумента `initDynatrace`, чтобы настроить трассировку и получить зарегистрированный NodeTracerProvider. Атрибуты ресурса для provider можно передать в качестве второго необязательного аргумента.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // initialize instrumentation with tracing setup



  const provider = initDynatrace(true, {



  "my.resource.attribute": "My Resource"



  });



  // azure functions registration goes here
  ```
* initDynatrace без настройки OpenTelemetry

  Вызовите `initDynatrace` без параметров, чтобы зарегистрировать только необходимые хуки Azure Function и настроить трассировку вручную. Это удобно, если для настройки трассировки требуются дополнительные параметры.

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

  Обратите внимание, что код настройки трассировки аналогичен коду для модели программирования v3, и пример с NodeSDK (из раздела v3 выше) также применим здесь. Для удобства предусмотрен API `configureDynatrace`, выполняющий те же действия.

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

#### Инициализация трассировки путём регистрации хуков Azure Function вручную

В случаях, когда требуется зарегистрировать дополнительные хуки Azure Functions, API `initDynatrace` может не подойти.

Поскольку хуки Azure Function выполняются в том порядке, в котором они были зарегистрированы, важно:

* Зарегистрировать хук Dynatrace Trace Start первым среди хуков предварительного вызова
* Зарегистрировать хук Dynatrace Trace End последним среди хуков завершения вызова

Время выполнения хуков включается в общее время выполнения функции. Если порядок зарегистрированных хуков нарушен, сообщаемое инструментированием время выполнения функции также будет неточным.

Подробнее о хуках Azure Function см. в [руководстве разработчика Azure Functions для Node.js](https://dt-url.net/uo23lv1).

Для управления порядком хуков используйте API `registerTraceStartHook` и `registerTraceEndHook`, как показано ниже.

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
| 1.335+ | 1.x.y | 1.0.x - 2.5.x |

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-azure-functions` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 вместо V1, переопределите версию модуля `@dynatrace/opentelemetry-core` (требуется для `@dynatrace/opentelemetry-azure-functions`), указав версию с поддержкой OpenTelemetry SDK V2.

1. Выберите из таблицы выше версию с поддержкой OpenTelemetry SDK V2.
2. В файле `package.json` добавьте раздел `overrides` и укажите одну из версий модуля `@dynatrace/opentelemetry-core` для принудительного использования.
3. Выполните `npm install`, чтобы применить изменения.

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

Как только `@dynatrace/opentelemetry-azure-functions` будет переведён на использование OpenTelemetry SDK V2 по умолчанию, это переопределение больше не потребуется.

Поддерживаемые версии [Azure Functions runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):

* 4.x

Поддерживаемые [модели программирования Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):

* 3.x
* 4.x @dynatrace/opentelemetry-azure-functions версии 1.289+

## Ограничения

* Поддерживаются только обработчики функций типа `async`.

  + Это соответствует рекомендации Azure использовать [`async` и `await`](https://dt-url.net/be03x31).
  + `wrapHandler` возвращает любую функцию без `async` в необёрнутом виде: функция будет работать, но спан создан не будет.
  + Обратите внимание, что асинхронные функции появились в ECMAScript 2017. Если используется более ранняя версия ECMAScript, спаны создаваться не будут. При использовании TypeScript убедитесь, что [цель компиляции](https://dt-url.net/df02zbc) установлена на ECMAScript 2017 или выше.
* Пакет поддерживает только [план Consumption](https://dt-url.net/ck022yx). На других планах он может работать, однако совместимость и производительность не гарантируются.
* Сигнализация о завершении функции с помощью устаревших вызовов [`context.done()`](https://dt-url.net/0l23xfy) или [`context.res.send()`](https://dt-url.net/dj43xgq) не поддерживается. Используйте привязку `$return` и возвращайте результат из обработчика функции, либо используйте именованную привязку `out` и задавайте `context.binding.<name>`. Для HTTP-триггеров также поддерживается установка `context.res`.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")