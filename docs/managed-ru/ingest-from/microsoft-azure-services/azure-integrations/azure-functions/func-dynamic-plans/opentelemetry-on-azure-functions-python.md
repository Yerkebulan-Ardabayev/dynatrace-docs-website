---
title: Трассировка Azure Functions на Python
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python
scraped: 2026-05-12T12:07:46.021523
---

# Трассировка Azure Functions на Python

# Трассировка Azure Functions на Python

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 13 июля 2022 г.

Пакет [`dynatrace-opentelemetry-azure-functions`](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) предоставляет API для трассировки Python Azure Functions.

## Предварительные требования

Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.").

* dynatrace-opentelemetry-azure-functions версии 1.245+

## Установка

Чтобы настроить интеграцию OpenTelemetry для Python на Azure Functions, добавьте следующую строку в файл `requirements.txt` приложения функции:

```
dynatrace-opentelemetry-azure-functions
```

Это добавит последнюю версию пакета `dynatrace-opentelemetry-azure-functions` как зависимость приложения функции. Подробнее об управлении зависимостями см. [руководство разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).

## Экспорт трассировки

Для экспорта трассировок в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать функции-обработчики](#instrument).

### Инициализация трассировки

Выберите один из двух способов инициализации трассировки.

* Функция `configure_dynatrace`: рекомендуемый вариант, если не требуется вручную настраивать компоненты трассировки.
* Ручная настройка трассировки: обеспечивает более тонкую настройку компонентов трассировки.

Поскольку в одно приложение Azure Function app можно объединить несколько Azure Functions, важно инициализировать трассировку один раз на уровне приложения, а не отдельно для каждой функции. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure), и импортировать его в начале файлов с определениями функций.

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

Код настройки трассировки должен выполняться ровно один раз до импорта любых сторонних модулей. Если для сортировки импортов используется `isort`, рекомендуется [отключить его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в примере ниже:

```
# isort: off



import setup_tracing  # import the module containing your setup code



# isort: on



# import other modules
```

### Инструментирование функции-обработчика

#### Модель программирования v1

Используйте декоратор `wrap_handler` для инструментирования функции-обработчика, как показано в примере ниже:

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

Если HTTP-функция-обработчик не возвращает явного результата и использует несколько привязок `Out`, необходимо передать имя привязки ответа в декоратор в качестве подсказки, чтобы атрибуты результата были корректно установлены на спане.

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

Поскольку фреймворк Azure functions для модели программирования V2 использует декораторы для обозначения функций-обработчиков, важен порядок применения декораторов `wrap_handler` и Azure.
Фрагмент ниже демонстрирует правильный порядок: обработчик должен быть декорирован с помощью `wrap_handler` до применения декоратора `app.route`.

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

* Среда выполнения Azure динамически передаёт аргумент [invocation context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) в функцию-обработчик, если её сигнатура содержит параметр с именем `context`. Однако если в файле `function.json` также есть привязка с именем `context`, привязка перехватывает этот аргумент, и вместо него передаётся привязка. Декоратор `wrap_handler` в этом случае не будет работать, так как ему требуется контекст вызова для извлечения определённых атрибутов спана. Не используйте имя `context` ни для одной привязки в файле `function.json`.
* HTTP-функции-обработчики с несколькими привязками `Out` и без явного возвращаемого результата должны передавать имя привязки вывода ответа в декоратор функции, чтобы атрибуты результата спана устанавливались корректно.
* `DtSpanProcessor` работает только совместно с `DtSampler`. При ручной настройке трассировки обязательно задайте `DtSampler` в качестве sampler, иначе спаны могут не экспортироваться.
* Инструментирование веб-фреймворков [WSGI и ASGI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) в настоящее время не поддерживается для модели программирования v2 из-за отличающейся сигнатуры обработчика.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Мониторинг Azure](https://www.dynatrace.com/technologies/azure-monitoring/)