---
title: Трассировка Azure Functions, написанных на Python
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python
scraped: 2026-03-05T21:29:47.819803
---

Пакет [`dynatrace-opentelemetry-azure-functions`](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) предоставляет API для трассировки Python Azure Functions.

## Предварительные требования

Убедитесь, что вы выполнили шаги **начальной конфигурации**, описанные в разделе Настройка мониторинга OpenTelemetry для Azure Functions на плане потребления, прежде чем использовать описанные ниже пакеты.

* dynatrace-opentelemetry-azure-functions версии 1.245+

## Установка

Чтобы настроить интеграцию OpenTelemetry Python для Azure Functions, добавьте следующую строку в файл `requirements.txt` вашего приложения-функции:

```
dynatrace-opentelemetry-azure-functions
```

Это добавит последнюю версию пакета `dynatrace-opentelemetry-azure-functions` в качестве зависимости вашего приложения-функции. Подробнее об управлении зависимостями см. в [руководстве разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).

## Экспорт трейсов

Для экспорта трейсов в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать ваши функции-обработчики](#instrument).

### Инициализация трассировки

Выберите один из двух описанных ниже способов инициализации трассировки.

* Функция `configure_dynatrace` — это рекомендуемый вариант, если вам не нужна ручная настройка компонентов трассировки.
* Ручная настройка трассировки — позволяет более детально настроить компоненты трассировки.

Поскольку в одном приложении Azure Function можно объединить несколько Azure Functions, важно инициализировать трассировку только один раз на каждое приложение Azure Function, а не один раз на каждую функцию. Самый простой способ сделать это — поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure), и импортировать его в начале файлов, определяющих функцию.

Пример с `configure_dynatrace` (рекомендуется)

```
from opentelemetry.sdk.resources import Resource


from opentelemetry.semconv.resource import ResourceAttributes


from dynatrace.opentelemetry.tracing.api import configure_dynatrace


tracer_provider = configure_dynatrace(


resource=Resource.create({"my.resource.attribute": "My Resource"})


)
```

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

Код настройки трассировки должен быть реализован таким образом, чтобы трассировка настраивалась только один раз, перед импортом любых сторонних модулей. Если вы используете `isort` для сортировки импортов, мы рекомендуем [деактивировать его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в следующем примере:

```
# isort: off


import setup_tracing  # import the module containing your setup code


# isort: on


# import other modules
```

### Инструментирование функции-обработчика

#### Модель программирования v1

Используйте декоратор `wrap_handler` для инструментирования вашей функции-обработчика, как показано в примере ниже:

```
from azure import functions as func


# import the wrap_handler decorator


from dynatrace.opentelemetry.azure.functions import wrap_handler


@wrap_handler


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:


# From here the created span is available in the OpenTelemetry context as the current span.


# do something ...


return  func.HttpResponse(f"Hello world.", status_code=200)
```

Параметр [context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) является необязательным и может быть опущен в сигнатуре обработчика.

Если ваша HTTP-функция-обработчик не возвращает явный результат и использует несколько привязок `Out`, вы должны указать имя привязки ответа в качестве подсказки для декоратора, чтобы атрибуты результата могли быть правильно установлены в span.

Пример:

```
from azure import functions as func


# import the wrap_handler decorator


from dynatrace.opentelemetry.azure.functions import wrap_handler


@wrap_handler(http_result_param_name="res")


def main(req: func.HttpRequest, other: func.Out[str], res: func.Out[func.HttpResponse]):


# do something ...


res.set(func.HttpResponse(f"Hello world.", status_code=200))
```

#### Модель программирования v2

Функции, реализованные с использованием [модели программирования v2](https://dt-url.net/ix03806), также можно инструментировать с помощью декоратора `wrap_handler`.

Поскольку фреймворк Azure Functions для модели программирования V2 использует декораторы для обозначения функций-обработчиков, порядок применения декоратора `wrap_handler` и декораторов Azure имеет значение.
Фрагмент ниже показывает правильный порядок: обработчик должен быть декорирован `wrap_handler` перед декоратором `app.route`.

```
import azure.functions as func


# import the wrap_handler decorator


from dynatrace.opentelemetry.azure.functions import wrap_handler


app = func.FunctionApp()


@app.function_name("MyHttpFunc")


@app.route(route="hello")


@wrap_handler # Note: wrap_handler must be located after the app.route decorator, so it's executed first.


def main(req: func.HttpRequest) -> func.HttpResponse:


# do something ...


return func.HttpResponse("Hello world", status_code=200)
```

## Ограничения

* Среда выполнения Azure динамически передаёт аргумент [контекста вызова](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) в вашу функцию-обработчик, если сигнатура обработчика содержит параметр с именем `context`. Однако, если в вашем файле `function.json` также есть привязка с именем `context`, контекст вызова игнорируется привязкой, и вместо него передаётся привязка. Декоратор `wrap_handler` не будет работать в этом случае, поскольку ему требуется контекст вызова для извлечения определённых атрибутов span. Не используйте имя `context` для какой-либо привязки в вашем файле `function.json`.
* HTTP-функции-обработчики с несколькими привязками `Out` и без явного возвращаемого результата должны указывать имя привязки выходного ответа в декораторе функции, чтобы атрибуты результата span были правильно установлены.
* `DtSpanProcessor` работает только совместно с `DtSampler`. Обязательно установите `DtSampler` в качестве сэмплера при ручной настройке трассировки; в противном случае span-ы могут не экспортироваться.
* Инструментирование веб-фреймворков [WSGI и ASGI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) в настоящее время не поддерживается для модели программирования v2 из-за отличающейся сигнатуры обработчика.

## Связанные темы

* Настройка Dynatrace в Microsoft Azure
* [Мониторинг Azure](https://www.dynatrace.com/technologies/azure-monitoring/)
