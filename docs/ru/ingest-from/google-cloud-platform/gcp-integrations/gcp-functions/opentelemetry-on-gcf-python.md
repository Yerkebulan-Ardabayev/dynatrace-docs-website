---
title: Integrate on Google Cloud Functions Python
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python
scraped: 2026-03-05T21:29:32.606351
---

# Интеграция с Google Cloud Functions на Python

# Интеграция с Google Cloud Functions на Python

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 16, 2023

[Пакет](https://pypi.org/project/dynatrace-opentelemetry-gcf) `dynatrace-opentelemetry-gcf` предоставляет API для трассировки функций Google Cloud Functions (GCF) на Python.

## Предварительные требования

Убедитесь, что вы выполнили шаги **начальной настройки**, описанные в [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с помощью OpenTelemetry и Dynatrace."), прежде чем использовать пакеты, описанные ниже.

* dynatrace-opentelemetry-gcf версии 1.247+
* Версия продукта Cloud Functions: 1-е поколение, 2-е поколение

## Установка

Чтобы настроить интеграцию OpenTelemetry Python с Google Cloud Functions, добавьте следующую строку в файл `requirements.txt` вашей функции:

```
dynatrace-opentelemetry-gcf
```

Это добавляет последнюю версию пакета `dynatrace-opentelemetry-gcf` в качестве зависимости вашей функции. Для получения дополнительной информации об управлении зависимостями обратитесь к [документации GCF для Python](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).

## Экспорт трассировок

Для экспорта трассировок в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать функцию-обработчик](#instrument).

### Инициализация трассировки

Выберите один из следующих способов инициализации трассировки:

* Функция `configure_dynatrace` -- это рекомендуемый вариант, если вам не требуется ручная настройка компонентов трассировки.

  Пример с `configure_dynatrace` (рекомендуется)

  ```
  from opentelemetry.sdk.resources import Resource



  from opentelemetry.semconv.resource import ResourceAttributes



  from dynatrace.opentelemetry.tracing.api import configure_dynatrace



  tracer_provider = configure_dynatrace(



  resource=Resource.create({"my.resource.attribute": "My Resource"})



  )
  ```
* Ручная настройка трассировки -- позволяет более детально настроить компоненты трассировки.

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

Код настройки трассировки должен быть реализован таким образом, чтобы трассировка настраивалась только один раз до импорта любого другого стороннего модуля. Если вы используете `isort` для сортировки импортов, мы рекомендуем [деактивировать его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в следующем примере:

```
# isort: off



import setup_tracing  # импортируйте модуль, содержащий ваш код настройки



# isort: on



# импортируйте другие модули
```

### Инструментация функции-обработчика

Используйте декоратор `wrap_handler` для инструментации функции-обработчика, как показано в следующем примере:

```
import flask



from dynatrace.opentelemetry.gcf import wrap_handler



@wrap_handler



def handler(request: flask.Request) -> flask.Response:



# Здесь созданный спан доступен в контексте OpenTelemetry как текущий спан.



# выполните какие-либо действия ...



return flask.Response("Hello World", 200)
```

## Холодный старт

При первом вызове обернутого обработчика после [холодного старта](https://cloud.google.com/functions/docs/concepts/exec#cold_starts) декоратор выполнит дополнительные HTTP-запросы для получения метаданных из вашей [среды Google Cloud](https://cloud.google.com/compute/docs/metadata/overview). Эти метаданные используются для установки необходимых атрибутов для обработки спана в Dynatrace.

## Сброс спанов

По умолчанию декоратор `wrap_handler` автоматически выполняет операцию сброса при завершении декорированной функции, чтобы обеспечить корректный экспорт спанов. Однако сброс спанов увеличивает время выполнения, поскольку эта операция становится частью логики выполнения функции.

Предоставив дополнительный параметр декоратору, `@wrap_handler(flush_on_exit=False)`, вы можете отключить сброс после каждого вызова. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.

Поскольку код, выполняющийся вне выполнения функции, может быть прерван в любой момент, Google Cloud Functions не рекомендует этот подход.

* Google Cloud Functions 1-го поколения

  Выполнение фоновых задач после вызова функции не гарантируется без сброса спанов и может привести к потере спанов. На практике примеры показали, что отсутствие явного сброса спанов обычно все равно приводит к корректному экспорту спанов.
* Google Cloud Functions 2-го поколения

  Google Cloud Functions 2-го поколения может обрабатывать несколько одновременных запросов в одном экземпляре функции. Операция сброса одного вызова может увеличить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно должны оставаться в режиме ожидания некоторое время для обработки нескольких одновременных запросов, вы можете отключить сброс спанов для повышения производительности. Подробнее см. [Жизненный цикл экземпляра](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание, что экземплярам функций в режиме ожидания не гарантируется выделение CPU, если их режим [выделения CPU](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в значение `CPU always allocated`.

  Подробнее см. [Временная шкала выполнения функции](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Накладные расходы Dynatrace

* Поскольку экспорт спанов и получение метаданных занимают некоторое время при холодных стартах, они увеличивают длительность функции и, соответственно, затраты.
* Обратите внимание на редко вызываемые функции (обычно с холодными стартами), которым может потребоваться больше времени для установления TCP-соединения при экспорте спанов.
* Любые сетевые проблемы между экспортером и бэкендом Dynatrace также могут привести к неожиданно высоким накладным расходам.

## Ограничения

* `DtSpanProcessor` работает только совместно с `DtSampler`. Убедитесь, что `DtSampler` установлен в качестве сэмплера при ручной настройке трассировки; в противном случае спаны могут не экспортироваться.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/docs/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)
