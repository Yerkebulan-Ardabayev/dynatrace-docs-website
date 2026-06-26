---
title: Интеграция OpenTelemetry на Google Cloud Functions Node.js
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs
scraped: 2026-05-12T11:52:01.511048
---

# Интеграция OpenTelemetry на Google Cloud Functions Node.js

# Интеграция OpenTelemetry на Google Cloud Functions Node.js

* Практическое руководство
* Чтение: 4 мин
* Обновлено 26 сентября 2025 г.

Модуль [`@dynatrace/opentelemetry-gcf`](https://dt-url.net/zm03ye8) предоставляет API для трассировки Node.js на Google Cloud Functions (GCF).

## Предварительные требования

Убедитесь, что вы выполнили инструкции по [интеграции OpenTelemetry на Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с помощью OpenTelemetry и Dynatrace.").

* На данный момент поддерживаются только [триггеры HTTP](https://dt-url.net/os23yfz).
* Версия продукта Cloud Function: 1-го поколения, 2-го поколения

## Установка

Чтобы настроить интеграцию OpenTelemetry Node.js на Google Cloud Functions, выполните следующую команду в корневом каталоге вашего проекта Google Cloud Function.

```
npm install --save @dynatrace/opentelemetry-gcf
```

Будет установлена последняя версия модуля [`@dynatrace/opentelemetry-gcf`](https://dt-url.net/zm03ye8) из NPM. Обратите внимание: одной этой библиотеки недостаточно для начала трассировки Google Cloud Functions.
Оставшиеся необходимые шаги см. в разделе [Использование](#usage) ниже.

## Использование

Чтобы экспортировать трассировки в Dynatrace

1. Выберите один из двух способов инициализации трассировки.

   * `NodeTracerProvider` для инициализации трассировки легче, чем `NodeSDK`.
   * `NodeSDK` обычно используется, если требуются дополнительные сигналы OpenTelemetry, например метрики.

   Использование NodeTracerProvider (рекомендуется)

   Использование NodeSDK

   Установите необходимые пакеты OpenTelemetry следующей командой.

   ```
   npm install --save @opentelemetry/sdk-trace-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку с помощью следующего примера кода.

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

   Установите необходимые пакеты OpenTelemetry следующей командой.

   ```
   npm install --save @opentelemetry/sdk-node @opentelemetry/semantic-conventions
   ```

   После установки пакетов инициализируйте трассировку с помощью следующего примера кода.

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
2. Запустите корневой серверный спан Google Cloud Function, используя один из двух шаблонов OpenTelemetry.

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
| 1.335+ | 1.x.y | 1.0.x - 2.5.x |

Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-gcf` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 (вместо V1), переопределите версию модуля `@dynatrace/opentelemetry-core` (требуемого `@dynatrace/opentelemetry-gcf`) на версию с поддержкой OpenTelemetry SDK V2.

1. Из таблицы выше выберите версию с поддержкой OpenTelemetry SDK V2.
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

После того как `@dynatrace/opentelemetry-gcf` будет по умолчанию переключён на OpenTelemetry SDK V2, это переопределение больше не потребуется.

## Холодный старт

Запуск спана Google Cloud Function при [холодных стартах](https://dt-url.net/j543yr9) генерирует дополнительные HTTP-запросы для получения метаданных из [среды Google Cloud](https://dt-url.net/jc83y1m) и установки атрибутов, необходимых Dynatrace для обработки спанов.

## Сброс спанов

Чтобы спаны экспортировались корректно, необходимо выполнить их сброс до отправки ответа функции клиенту. Подробнее об этом ограничении см. [Сигнализация завершения функции](https://dt-url.net/5ta3ywp).

При необходимости можно использовать `endHttpSpan()` и `flushSpans()` раздельно вместо `endHttpSpanAndFlush()`.

Сброс спанов в коде функции увеличивает время выполнения, поскольку эта операция становится частью логики выполнения функции. Чтобы избежать этого, можно пропустить операцию сброса: спаны всё равно будут периодически экспортироваться в фоновом режиме.

Поскольку код, выполняющийся за пределами выполнения функции, может быть завершён в любой момент, Google Cloud Functions не рекомендует такой подход.

* Google Cloud Functions 1-го поколения

  Выполнение фоновых задач после вызова функции без сброса спанов не гарантировано и может привести к потере спанов. На практике примеры показали, что отсутствие явного сброса спанов, как правило, всё равно приводит к их корректному экспорту.
* Google Cloud Functions 2-го поколения

  Google Cloud Functions 2-го поколения может обрабатывать несколько одновременных запросов в одном экземпляре функции. Операция сброса одного вызова может увеличить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно должны некоторое время оставаться в режиме ожидания для обработки нескольких одновременных запросов, можно отключить сброс спанов для повышения производительности. Подробнее см. [Жизненный цикл экземпляра](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание: простаивающим экземплярам функций не гарантировано выделение CPU, если их режим [выделения CPU](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в `CPU always allocated`.

  Подробнее см. [Временная шкала выполнения функции](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Особые замечания

Необходимо уделять особое внимание случаям необработанных исключений или тайм-аутов функции. При ненадлежащей обработке они могут привести к незавершённому и, следовательно, неэкспортированному спану.

## Накладные расходы Dynatrace

* Поскольку экспорт спанов и получение метаданных занимают некоторое время при холодных стартах, они увеличивают продолжительность выполнения функции и, следовательно, повышают затраты.
* Обратите внимание на редко вызываемые функции (как правило, с холодными стартами): им может потребоваться больше времени для TCP-рукопожатия при экспорте спанов.
* Любые сетевые проблемы между экспортером и бэкендом Dynatrace могут также привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)