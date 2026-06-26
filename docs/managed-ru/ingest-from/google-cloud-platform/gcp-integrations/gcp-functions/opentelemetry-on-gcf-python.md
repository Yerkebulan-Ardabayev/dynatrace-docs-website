---
title: Интеграция на Google Cloud Functions Python
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python
scraped: 2026-05-12T11:51:58.800080
---

# Интеграция на Google Cloud Functions Python

# Интеграция на Google Cloud Functions Python

* Практическое руководство
* Чтение: 3 мин
* Обновлено 16 июня 2023 г.

Пакет `dynatrace-opentelemetry-gcf` [package](https://pypi.org/project/dynatrace-opentelemetry-gcf) предоставляет API для трассировки Python Google Cloud Functions (GCF).

## Предварительные требования

Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной конфигурации**, описанные в разделе [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.").

* dynatrace-opentelemetry-gcf версии 1.247+
* Версия продукта Cloud Functions: 1st gen, 2nd gen

## Установка

Чтобы настроить интеграцию OpenTelemetry для Python на Google Cloud Functions, добавьте следующую строку в файл `requirements.txt` функции:

```
dynatrace-opentelemetry-gcf
```

Это добавляет последнюю версию пакета `dynatrace-opentelemetry-gcf` как зависимость функции. Подробнее об управлении зависимостями см. [GCF documentation for Python](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).

## Экспорт трассировок

Для экспорта трассировок в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать функцию-обработчик](#instrument).

### Инициализация трассировки

Выберите один из следующих способов инициализации трассировки:

* Функция `configure_dynatrace`: рекомендуемый вариант, если не требуется ручная настройка компонентов трассировки.

  Пример с `configure_dynatrace` (рекомендуется)

  ```
  from opentelemetry.sdk.resources import Resource



  from opentelemetry.semconv.resource import ResourceAttributes



  from dynatrace.opentelemetry.tracing.api import configure_dynatrace



  tracer_provider = configure_dynatrace(



  resource=Resource.create({"my.resource.attribute": "My Resource"})



  )
  ```
* Ручная настройка трассировки: позволяет более детально настроить компоненты трассировки.

  Пример с ручной настройкой трассировки

  ```
  from opentelemetry.propagate import set_global_textmap



  from opentelemetry.sdk.resources import Resource



  from opentelemetry.sdk.trace import TracerProvider



  from opentelemetry.semconv.resource import ResourceAttributes



  from opentelemetry.trace import set_tracer_provider



  from dynatrace.opentelemetry.tracing.api import (



  DtSampler,



  DtSpanProcessor,



  DtTextMapPropagator,



  )



  span_processor = DtSpanProcessor()



  tracer_provider = TracerProvider(



  sampler=DtSampler(),



  resource=Resource.create({"my.resource.attribute": "My Resource"}),



  )



  tracer_provider.add_span_processor(span_processor)



  set_global_textmap(DtTextMapPropagator())



  set_tracer_provider(tracer_provider)
  ```

Код настройки трассировки должен инициализировать трассировку только один раз, до импорта любых сторонних модулей. Если для сортировки импортов используется `isort`, рекомендуется [отключить его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в следующем примере:

```
# isort: off



import setup_tracing  # import the module containing your setup code



# isort: on



# import other modules
```

### Инструментирование функции-обработчика

Используйте декоратор `wrap_handler` для инструментирования функции-обработчика, как показано в следующем примере:

```
import flask



from dynatrace.opentelemetry.gcf import wrap_handler



@wrap_handler



def handler(request: flask.Request) -> flask.Response:



# From here the created span is available in the OpenTelemetry context as the current span.



# do something ...



return flask.Response("Hello World", 200)
```

## Холодный старт

При первом вызове обёрнутого обработчика после [холодного старта](https://cloud.google.com/functions/docs/concepts/exec#cold_starts) декоратор выполняет дополнительные HTTP-запросы для получения метаданных из [среды Google Cloud](https://cloud.google.com/compute/docs/metadata/overview). Эти метаданные используются для задания необходимых атрибутов, по которым Dynatrace обрабатывает спан.

## Сброс спанов

По умолчанию декоратор `wrap_handler` автоматически выполняет операцию сброса при завершении декорированной функции, чтобы гарантировать корректный экспорт спанов. Однако сброс спанов увеличивает время выполнения, так как эта операция становится частью логики функции.

Передав декоратору дополнительный параметр `@wrap_handler(flush_on_exit=False)`, можно отключить сброс после каждого вызова. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.

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

## Ограничения

* `DtSpanProcessor` работает только совместно с `DtSampler`. При ручной настройке трассировки обязательно задайте `DtSampler` в качестве сэмплера, иначе спаны могут не экспортироваться.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с Dynatrace.")
* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)