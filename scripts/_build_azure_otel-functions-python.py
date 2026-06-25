# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans"

TT_HUB = "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace."
TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."

TRANS = {
    "title: Trace Azure Functions written in Python": "title: Трассировка Azure Functions на Python",
    "# Trace Azure Functions written in Python": "# Трассировка Azure Functions на Python",
    "* How-to guide": "* Практическое руководство",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Jul 13, 2022": "* Опубликовано 13 июля 2022 г.",
    "The [`dynatrace-opentelemetry-azure-functions` package](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) provides APIs for tracing Python Azure Functions.": "Пакет [`dynatrace-opentelemetry-azure-functions`](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) предоставляет API для трассировки Python Azure Functions.",
    "## Prerequisites": "## Предварительные требования",
    f'Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.': f'Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "{TT_HUB}").',
    "* dynatrace-opentelemetry-azure-functions version 1.245+": "* dynatrace-opentelemetry-azure-functions версии 1.245+",
    "## Installation": "## Установка",
    "To set up OpenTelemetry Python integration on Azure Functions, add the following line to the `requirements.txt` file of your function app:": "Чтобы настроить интеграцию OpenTelemetry для Python на Azure Functions, добавьте следующую строку в файл `requirements.txt` приложения функции:",
    "This adds the latest version of the `dynatrace-opentelemetry-azure-functions` package as a dependency to your function app. For more information about managing dependencies, consult the [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).": "Это добавит последнюю версию пакета `dynatrace-opentelemetry-azure-functions` как зависимость приложения функции. Подробнее об управлении зависимостями см. [руководство разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).",
    "## Trace export": "## Экспорт трассировки",
    "To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler functions](#instrument).": "Для экспорта трассировок в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать функции-обработчики](#instrument).",
    "### Initialize tracing": "### Инициализация трассировки",
    "Select one of the two ways below to initialize tracing.": "Выберите один из двух способов инициализации трассировки.",
    "* `configure_dynatrace` function—This is the recommended option unless you need to manually set up the tracing components.": "* Функция `configure_dynatrace`: рекомендуемый вариант, если не требуется вручную настраивать компоненты трассировки.",
    "* Manual tracing setup—This allows for a more fine-grained setup of tracing components.": "* Ручная настройка трассировки: обеспечивает более тонкую настройку компонентов трассировки.",
    "Because it's possible to bundle several Azure Functions into a single Azure Function app, it's important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put the tracing setup code into a shared file as described in the [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure) and import it at the top of the files that define a function.": "Поскольку в одно приложение Azure Function app можно объединить несколько Azure Functions, важно инициализировать трассировку один раз на уровне приложения, а не отдельно для каждой функции. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions для Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure), и импортировать его в начале файлов с определениями функций.",
    "Example with `configure_dynatrace` (recommended)": "Пример с `configure_dynatrace` (рекомендуется)",
    "Example with manual tracing setup": "Пример с ручной настройкой трассировки",
    "The tracing setup code should be implemented to set up tracing only once before any other third-party module is imported. If you use `isort` to sort your imports, we suggest that you [deactivate it](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) while importing the tracing setup module, as shown in the following example:": "Код настройки трассировки должен выполняться ровно один раз до импорта любых сторонних модулей. Если для сортировки импортов используется `isort`, рекомендуется [отключить его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в примере ниже:",
    "### Instrument a handler function": "### Инструментирование функции-обработчика",
    "#### Programming model v1": "#### Модель программирования v1",
    "Use the `wrap_handler` decorator to instrument your handler function, as shown in the example below:": "Используйте декоратор `wrap_handler` для инструментирования функции-обработчика, как показано в примере ниже:",
    "The [context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) parameter is optional and can be omitted from the handler's signature.": "Параметр [context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) является необязательным и может быть опущен в сигнатуре обработчика.",
    "If your HTTP function handler doesn't return an explicit result and uses multiple `Out` bindings, you should provide the name of the response binding as a binding hint to the decorator, so that result attributes can be properly set on the span.": "Если HTTP-функция-обработчик не возвращает явного результата и использует несколько привязок `Out`, необходимо передать имя привязки ответа в декоратор в качестве подсказки, чтобы атрибуты результата были корректно установлены на спане.",
    "Example:": "Пример:",
    "#### Programming model v2": "#### Модель программирования v2",
    "Functions implemented using the [v2 programming model](https://dt-url.net/ix03806) can also be instrumented using the `wrap_handler` decorator.": "Функции, реализованные с использованием [модели программирования v2](https://dt-url.net/ix03806), также можно инструментировать с помощью декоратора `wrap_handler`.",
    "Because the Azure functions framework for programming model V2 uses decorators to mark handler functions, the order in which the `wrap_handler` and the Azure decorators are applied is important.": "Поскольку фреймворк Azure functions для модели программирования V2 использует декораторы для обозначения функций-обработчиков, важен порядок применения декораторов `wrap_handler` и Azure.",
    "The snippet below shows the correct order: the handler needs to be decorated with `wrap_handler` before the `app.route` decorator.": "Фрагмент ниже демонстрирует правильный порядок: обработчик должен быть декорирован с помощью `wrap_handler` до применения декоратора `app.route`.",
    "## Limitations": "## Ограничения",
    "* The Azure runtime dynamically passes the [invocation context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) argument to your handler function if the handler's signature contains a parameter with name `context`. However, if there's also a binding with the name `context` in your `function.json` file, the invocation context is ignored by the binding and the binding is passed instead. The `wrap_handler` decorator won't work in this case, since it requires the invocation context to extract certain span attributes. Be sure not to use the name `context` for any binding in your `function.json` file.": "* Среда выполнения Azure динамически передаёт аргумент [invocation context](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) в функцию-обработчик, если её сигнатура содержит параметр с именем `context`. Однако если в файле `function.json` также есть привязка с именем `context`, привязка перехватывает этот аргумент, и вместо него передаётся привязка. Декоратор `wrap_handler` в этом случае не будет работать, так как ему требуется контекст вызова для извлечения определённых атрибутов спана. Не используйте имя `context` ни для одной привязки в файле `function.json`.",
    "* HTTP handler functions with multiple `Out` bindings and no explicit return result should provide the name of the response output binding to the function decorator, so that result span attributes can be properly set.": "* HTTP-функции-обработчики с несколькими привязками `Out` и без явного возвращаемого результата должны передавать имя привязки вывода ответа в декоратор функции, чтобы атрибуты результата спана устанавливались корректно.",
    "* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.": "* `DtSpanProcessor` работает только совместно с `DtSampler`. При ручной настройке трассировки обязательно задайте `DtSampler` в качестве sampler, иначе спаны могут не экспортироваться.",
    "* Instrumentation of [WSGI and ASGI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) web frameworks is currently not supported for the v2 programming model because of the handler's different signature.": "* Инструментирование веб-фреймворков [WSGI и ASGI](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) в настоящее время не поддерживается для модели программирования v2 из-за отличающейся сигнатуры обработчика.",
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    "* [Azure monitoring](https://www.dynatrace.com/technologies/azure-monitoring/)": "* [Мониторинг Azure](https://www.dynatrace.com/technologies/azure-monitoring/)",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "opentelemetry-on-azure-functions-python.md", TRANS, PASS)
    qa_one(REL, "opentelemetry-on-azure-functions-python.md")
