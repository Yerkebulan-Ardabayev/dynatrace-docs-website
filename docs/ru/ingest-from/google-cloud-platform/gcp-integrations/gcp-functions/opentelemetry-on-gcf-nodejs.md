---
title: Integrate on Google Cloud Functions Node.js
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs
scraped: 2026-03-05T21:29:51.504437
---

# Интеграция OpenTelemetry с Google Cloud Functions на Node.js

# Интеграция OpenTelemetry с Google Cloud Functions на Node.js

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Sep 26, 2025

Модуль [`@dynatrace/opentelemetry-gcf`](https://dt-url.net/zm03ye8) предоставляет API для трассировки Node.js в Google Cloud Functions (GCF).

## Предварительные требования

Убедитесь, что вы выполнили инструкции по [интеграции OpenTelemetry с Google Cloud Functions](opentelemetry-on-gcf.md "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").

* На данный момент поддерживаются только [HTTP-триггеры](https://dt-url.net/os23yfz).
* Версия продукта Cloud Function: 1-е поколение, 2-е поколение

## Установка

Для настройки интеграции OpenTelemetry Node.js с Google Cloud Functions выполните приведённую ниже команду в корневом каталоге вашего проекта Google Cloud Function.

```
npm install --save @dynatrace/opentelemetry-gcf
```

Эта команда установит последнюю версию модуля [`@dynatrace/opentelemetry-gcf`](https://dt-url.net/zm03ye8) из NPM. Обратите внимание, что сама по себе эта библиотека не достаточна для начала трассировки ваших Google Cloud Functions.
См. раздел [Использование](#usage) ниже для описания оставшихся необходимых шагов.

## Использование

Для экспорта трейсов в Dynatrace:

1. Выберите один из двух способов инициализации трассировки, описанных ниже.

   * `NodeTracerProvider`, используемый для инициализации трассировки, более легковесен, чем `NodeSDK`.
   * `NodeSDK` обычно используется, если вас интересуют дополнительные сигналы OpenTelemetry, такие как метрики.

   Использование NodeTracerProvider (рекомендуется)

   Использование NodeSDK

   Установите необходимые пакеты OpenTelemetry с помощью приведённой ниже команды.

   ```
   npm install --save @opentelemetry/sdk-trace-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку, используя следующий фрагмент кода в качестве примера.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



   const processor = new DtSpanProcessor(new DtSpanExporter());



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource",



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

   Установите необходимые пакеты OpenTelemetry с помощью приведённой ниже команды.

   ```
   npm install --save @opentelemetry/sdk-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку, используя следующий фрагмент кода в качестве примера.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeSDK } = require('@opentelemetry/sdk-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



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
2. Запустите корневой спан сервера Google Cloud Function, используя один из двух общих подходов OpenTelemetry, описанных ниже.

   Запуск активного спана (рекомендуется)

   Запуск спана с последующей активацией

   Пример запуска и немедленной активации спана внутри Google Cloud Function:

   ```
   const { startActiveHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   await startActiveHttpSpan(req, async (span) => {



   let error;



   try {



   // do something



   } catch (e) {



   error = e;



   }



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   });



   }
   ```

   Пример запуска спана внутри Google Cloud Function с последующей активацией в той же функции.

   ```
   const { context, trace, ROOT_CONTEXT } = require('@opentelemetry/api');



   const { startHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   const span = await startHttpSpan(req);



   let error;



   await context.with(trace.setSpan(ROOT_CONTEXT, span), async () => {



   try {



   // do something



   } catch (e) {



   error = e;



   }



   });



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   }
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

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-gcf` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 (вместо V1), переопределите версию модуля `@dynatrace/opentelemetry-core` (требуемого `@dynatrace/opentelemetry-gcf`) на версию, поддерживающую OpenTelemetry SDK V2.

1. Из приведённой выше таблицы выберите версию, поддерживающую OpenTelemetry SDK V2.
2. В файле `package.json` добавьте раздел `overrides` и укажите одну из версий модуля `@dynatrace/opentelemetry-core` для принудительного использования.
3. Выполните `npm install` для применения изменений.

Пример:

```
{



"dependencies": {



"@dynatrace/opentelemetry-gcf": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Когда `@dynatrace/opentelemetry-gcf` будет по умолчанию использовать OpenTelemetry SDK V2, это переопределение больше не потребуется.

## Холодный старт

Запуск спана Google Cloud Function во время [холодного старта](https://dt-url.net/j543yr9) приводит к дополнительным HTTP-запросам для получения метаданных из вашей [среды Google Cloud](https://dt-url.net/jc83y1m) и установки атрибутов, необходимых Dynatrace для обработки спанов.

## Отправка спанов

Для корректного экспорта спанов необходимо выполнить их отправку (flush) до того, как ответ функции будет отправлен клиенту. Подробнее об этом ограничении см. [Signalling function termination](https://dt-url.net/5ta3ywp).

Вы можете использовать `endHttpSpan()` и `flushSpans()` раздельно вместо `endHttpSpanAndFlush()`, когда это необходимо.

Отправка спанов в коде функции приводит к увеличению времени выполнения, так как эта операция становится частью логики выполнения функции. Чтобы избежать этого, вы можете пропустить операцию отправки. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.

Поскольку выполнение кода за пределами вызова функции может быть прервано в любой момент, Google Cloud Functions не рекомендует этот подход.

* Google Cloud Functions 1-го поколения

  Выполнение фоновых задач после вызова функции не гарантируется без отправки спанов и может привести к их потере. На практике примеры показывают, что отсутствие явной отправки спанов обычно по-прежнему приводит к корректному экспорту спанов.
* Google Cloud Functions 2-го поколения

  Google Cloud Functions 2-го поколения может обрабатывать несколько параллельных запросов в одном экземпляре функции. Операция отправки одного вызова может увеличить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно должны оставаться в режиме ожидания некоторое время для обработки нескольких параллельных запросов, вы можете отключить отправку спанов для повышения производительности. Подробнее см. [Instance lifecycle](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание, что для простаивающих экземпляров функций выделение CPU не гарантируется, если режим [выделения CPU](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в значение `CPU always allocated`.

  Подробнее см. [Function execution timeline](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Особые случаи

Необходимо уделять особое внимание таким случаям, как необработанные исключения или превышение времени ожидания функции. При неправильной обработке они могут привести к незавершённому, а следовательно, неэкспортированному спану.

## Накладные расходы Dynatrace

* Поскольку экспорт спанов и получение метаданных занимают время при холодном старте, они увеличивают длительность выполнения функции и, соответственно, расходы.
* Обратите внимание на редко вызываемые функции (обычно с холодным стартом), которым может потребоваться больше времени на установление TCP-соединения при экспорте спанов.
* Любые сетевые проблемы между экспортёром и бэкендом Dynatrace также могут привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](../../../google-cloud-platform.md "Monitor Google Cloud with Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)