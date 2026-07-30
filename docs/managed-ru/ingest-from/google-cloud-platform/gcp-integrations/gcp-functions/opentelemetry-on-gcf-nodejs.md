---
title: Интеграция в Google Cloud Functions Node.js
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs
---

# Интеграция в Google Cloud Functions Node.js

# Интеграция в Google Cloud Functions Node.js

* Практическое руководство
* Чтение: 4 мин
* Обновлено 26 сентября 2025 г.

Модуль [`@dynatrace/opentelemetry-gcf`﻿](https://dt-url.net/zm03ye8) предоставляет API для трассировки Node.js на Google Cloud Functions (GCF).

## Предварительные требования

Нужно выполнить инструкции по [интеграции OpenTelemetry на Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").

* На данный момент поддерживаются только [HTTP-триггеры﻿](https://dt-url.net/os23yfz).
* Версия продукта Cloud Function: 1st gen, 2nd gen

## Установка

Чтобы настроить интеграцию OpenTelemetry Node.js на Google Cloud Functions, выполните следующую команду в корневом каталоге проекта Google Cloud Function.

```
npm install --save @dynatrace/opentelemetry-gcf
```

Это установит последнюю версию модуля [`@dynatrace/opentelemetry-gcf`﻿](https://dt-url.net/zm03ye8) из NPM. Обратите внимание, что одной этой библиотеки недостаточно для начала трассировки Google Cloud Functions.
Остальные необходимые шаги описаны в разделе [Usage](#usage) ниже.

## Usage

Чтобы экспортировать трассы в Dynatrace:

1. Выберите один из двух способов инициализации трассировки ниже.

   * `NodeTracerProvider`, используемый для инициализации трассировки, более легковесен, чем `NodeSDK`.
   * `NodeSDK` обычно применяется, если нужны дополнительные сигналы OpenTelemetry, такие как метрики.

   Using NodeTracerProvider (recommended)

   Using NodeSDK

   Установите необходимые пакеты OpenTelemetry с помощью команды ниже.

   ```
   npm install --save @opentelemetry/sdk-trace-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку, используя следующий фрагмент в качестве примера.

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

   Установите необходимые пакеты OpenTelemetry с помощью команды ниже.

   ```
   npm install --save @opentelemetry/sdk-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку, используя следующий фрагмент в качестве примера.

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
2. Запустите корневой span сервера Google Cloud Function, используя один из двух общих паттернов OpenTelemetry ниже.

   Start an active span (recommended)

   Start the span and activate it later

   Пример запуска с немедленной активацией span внутри Google Cloud Function:

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

   Пример запуска span внутри Google Cloud Function с последующей активацией в рамках той же функции.

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
| 1.335+ | 1.x.y | 1.0.x - 2.5.x |
| 1.337+ | 1.x.y | 1.0.x - 2.6.x |
| 1.343+ | 1.x.y | 1.0.x - 2.7.x |

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-gcf` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 вместо V1, нужно переопределить версию модуля `@dynatrace/opentelemetry-core` (который требуется `@dynatrace/opentelemetry-gcf`) на версию с поддержкой OpenTelemetry SDK V2.

1. Выберите из таблицы выше версию с поддержкой OpenTelemetry SDK V2.
2. В файле `package.json` добавьте раздел `overrides` и укажите нужную версию модуля `@dynatrace/opentelemetry-core` для принудительного использования.
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

После того как `@dynatrace/opentelemetry-gcf` по умолчанию перейдёт на OpenTelemetry SDK V2, это переопределение больше не потребуется.

## Cold start

Запуск span Google Cloud Function во время [cold starts﻿](https://dt-url.net/j543yr9) порождает дополнительные HTTP-запросы для получения метаданных из [среды Google Cloud﻿](https://dt-url.net/jc83y1m) и установки атрибутов, необходимых Dynatrace для обработки span.

## Сброс span

Чтобы span корректно экспортировались, их нужно сбросить до отправки ответа функцией клиенту. Подробнее об этом ограничении см. в [Signalling function termination﻿](https://dt-url.net/5ta3ywp).

При необходимости можно вызывать `endHttpSpan()` и `flushSpans()` раздельно вместо `endHttpSpanAndFlush()`.

Сброс span в коде функции увеличивает время её выполнения, поскольку эта операция становится частью логики выполнения функции. Чтобы этого избежать, операцию сброса можно пропустить. Span всё равно будут периодически экспортироваться в фоновом режиме.

Поскольку код, выполняющийся за пределами функции, может быть прерван в любой момент, Google Cloud Functions не рекомендует этот подход.

* Google Cloud Functions 1st gen

  Выполнение фоновых задач после вызова функции не гарантируется без сброса span, что может привести к потере span. На практике опыт показывает, что отсутствие явного сброса span обычно всё же приводит к корректному экспорту span.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen может обрабатывать несколько одновременных запросов в одном экземпляре функции. Операция сброса одного вызова может увеличить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно некоторое время остаются в режиме ожидания для обработки нескольких одновременных запросов, можно отключить сброс span для повышения производительности. Подробнее см. в [Instance lifecycle﻿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание, что простаивающим экземплярам функций не гарантируется выделение CPU, если режим [CPU allocation﻿](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в `CPU always allocated`.

  Подробнее см. в [Function execution timeline﻿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Предостережения

Нужно уделять особое внимание случаям вроде необработанных исключений или таймаутов функций. Если не обработать их должным образом, span может остаться незавершённым и, следовательно, не будет экспортирован.

## Накладные расходы Dynatrace

* Поскольку экспорт span'ов и получение метаданных занимают некоторое время при холодном запуске, это увеличивает длительность выполнения функции и, соответственно, затраты.
* Нужно обращать внимание на редко вызываемые функции (как правило, с холодным запуском): им может потребоваться больше времени на TCP-рукопожатие при экспорте span'ов.
* Любая сетевая проблема между экспортером и бэкендом Dynatrace также может привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoring﻿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)