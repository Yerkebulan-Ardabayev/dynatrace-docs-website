---
title: Трассировка Azure Functions на Node.js
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs
---

# Трассировка Azure Functions на Node.js

# Трассировка Azure Functions на Node.js

* Практическое руководство
* 6 мин чтения
* Обновлено 04 ноя 2025

Модуль [`@dynatrace/opentelemetry-azure-functions`﻿](https://dt-url.net/9603x96) предоставляет API для трассировки Node.js в Azure Functions.

## Предварительные требования

Нужно выполнить шаги **начальной настройки**, описанные в [Настройка мониторинга OpenTelemetry для Azure Functions на Consumption Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace."), прежде чем использовать пакеты ниже.

* @dynatrace/opentelemetry-azure-functions версии 1.243+

## Установка

Чтобы настроить интеграцию OpenTelemetry Node.js в Azure Functions, выполните следующую команду.

```
npm install --save @dynatrace/opentelemetry-azure-functions
```

## Экспорт трасс

Azure Functions можно разрабатывать с использованием одной из двух различных [моделей программирования﻿](https://dt-url.net/9p03lmb): v3 и v4. Чтобы учесть различия между двумя моделями, Dynatrace предоставляет два способа экспорта трасс:

* Для модели программирования v3 обработчик Azure Functions оборачивается (с помощью API `wrapHandler`) для генерации и экспорта трасс.
* Для модели программирования v4 для этой же цели используются [Azure Functions Hooks﻿](https://dt-url.net/v323l3e). Обратите внимание: hooks доступны только для модели программирования v4.

Подробности см. ниже.

### Модель программирования v3

Чтобы экспортировать трассы в Dynatrace из Azure Functions, разработанных с [моделью программирования v3﻿](https://dt-url.net/n443lxw):

1. Выберите один из двух способов инициализации трассировки.

   * `NodeTracerProvider`, более лёгкий вариант по сравнению с `NodeSDK`
   * `NodeSDK`, как правило используется, если нужны дополнительные сигналы OpenTelemetry, например метрики

   Несколько Azure Functions можно объединить в одно Azure Function app. Поэтому важно инициализировать трассировку только один раз на Azure Function app, а не один раз на функцию. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве для JavaScript-разработчиков Azure Functions﻿](https://dt-url.net/t223xf2), и подключить его в начале всех функций.

   Код настройки трассировки должен инициализировать трассировку только один раз, до подключения любых других сторонних модулей.

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

### Programming model v4

Есть два способа экспортировать трассы в Dynatrace из Azure Functions, разработанных с использованием [programming model v4﻿](https://dt-url.net/7t03lem).

* Использовать API `initDynatrace`.
* Инициализировать трассировку, зарегистрировав хуки Azure Function вручную.

Независимо от выбранного подхода к инструментированию, код настройки трассировки нужно реализовывать таким образом, чтобы трассировка инициализировалась только один раз, до подключения любых сторонних модулей.

#### Использование API `initDynatrace`

API `initDynatrace` регистрирует хуки Azure Function, необходимые для трассировки, и при необходимости регистрирует требуемые компоненты трассировки.

Это можно сделать как с настройкой OpenTelemetry, так и без неё:

* initDynatrace с настройкой OpenTelemetry (рекомендуется)

  Передайте `true` первым аргументом в `initDynatrace`, чтобы настроить трассировку и получить зарегистрированный NodeTracerProvider. Атрибуты ресурса для провайдера можно передать вторым необязательным аргументом.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // initialize instrumentation with tracing setup



  const provider = initDynatrace(true, {



  "my.resource.attribute": "My Resource"



  });



  // azure functions registration goes here
  ```
* initDynatrace без настройки OpenTelemetry

  Вызовите `initDynatrace` без параметров, чтобы зарегистрировать только необходимые хуки Azure Function и настроить трассировку вручную. Это удобно, когда в настройке трассировки нужны дополнительные кастомизации.

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

  Обратите внимание, что код настройки трассировки совпадает с кодом для programming model v3, и пример с NodeSDK (из model v3 выше) также будет работать здесь. Для удобства предусмотрен API `configureDynatrace`, который делает то же самое, что и код выше.

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

#### Инициализация трассировки через ручную регистрацию хуков Azure Function

В случаях, когда нужно зарегистрировать дополнительные хуки Azure Functions, API `initDynatrace` может не подойти.

Поскольку хуки Azure Function выполняются в том порядке, в котором они зарегистрированы, важно соблюдать следующее:

* Регистрировать хук Dynatrace Trace Start как первый pre-invocation хук
* Регистрировать хук Dynatrace Trace End как последний post-invocation хук

Время выполнения хуков включается в общее время выполнения функции. Если порядок зарегистрированных хуков нарушен, время выполнения функции, которое сообщает наша инструментация, также будет неточным.

Подробнее о хуках Azure Function см. в [руководстве разработчика Azure Functions Node.js﻿](https://dt-url.net/uo23lv1).

Чтобы упорядочить хуки нужным образом, можно использовать APIs `registerTraceStartHook` и `registerTraceEndHook`, как показано ниже.

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

## Compatibility

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
| 1.337+ | 1.x.y | 1.0.x - 2.6.x |
| 1.343+ | 1.x.y | 1.0.x - 2.7.x |

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-azure-functions` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 (вместо V1), нужно переопределить версию модуля `@dynatrace/opentelemetry-core` (требуемого `@dynatrace/opentelemetry-azure-functions`) на версию, поддерживающую OpenTelemetry SDK V2.

1. В таблице выше выберите версию с поддержкой OpenTelemetry SDK V2.
2. В файле `package.json` добавьте секцию `overrides` и укажите одну из версий модуля `@dynatrace/opentelemetry-core` для принудительного применения.
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

После того как `@dynatrace/opentelemetry-azure-functions` по умолчанию перейдёт на использование OpenTelemetry SDK V2, это переопределение больше не потребуется.

Поддерживаемые версии [среды выполнения Azure Functions﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):

* 4.x

Поддерживаемые версии [модели программирования Azure Functions﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):

* 3.x
* 4.x @dynatrace/opentelemetry-azure-functions версии 1.289+

## Limitations

* Поддерживаются только обработчики функций с типом `async`.

  + Это следует рекомендации Azure использовать [`async` и `await`﻿](https://dt-url.net/be03x31).
  + `wrapHandler` возвращает любую не-`async` функцию без обёртки, поэтому функция продолжит работать, но спан создан не будет.
  + Обратите внимание, что async-функции появились в ECMAScript 2017. Если используется более ранняя версия ECMAScript, спан создан не будет. При использовании TypeScript убедитесь, что [цель компиляции﻿](https://dt-url.net/df02zbc) установлена на ECMAScript 2017 или выше.
* Пакет поддерживает только [план Consumption﻿](https://dt-url.net/ck022yx). На других планах он может работать, однако совместимость и производительность не гарантируются.
* Сигнализирование о завершении функции через устаревшие вызовы [`context.done()`﻿](https://dt-url.net/0l23xfy) или [`context.res.send()`﻿](https://dt-url.net/dj43xgq) не поддерживается. Нужно либо использовать привязку `$return` и возвращать результат из обработчика функции, либо использовать именованную привязку `out` и задавать `context.binding.<name>`. Для HTTP-триггеров также поддерживается установка `context.res`.

## Related topics

* [Настройка Dynatrace на Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")