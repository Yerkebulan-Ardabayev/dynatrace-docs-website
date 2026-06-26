# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/google-cloud-platform/gcp-integrations/gcp-functions"

TRANS = {
    "title: Integrate on Google Cloud Functions Python": "title: Интеграция на Google Cloud Functions Python",
    "# Integrate on Google Cloud Functions Python": "# Интеграция на Google Cloud Functions Python",
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Jun 16, 2023": "* Обновлено 16 июня 2023 г.",
    "The `dynatrace-opentelemetry-gcf` [package](https://pypi.org/project/dynatrace-opentelemetry-gcf) provides APIs for tracing Python Google Cloud Functions (GCF).": "Пакет `dynatrace-opentelemetry-gcf` [package](https://pypi.org/project/dynatrace-opentelemetry-gcf) предоставляет API для трассировки Python Google Cloud Functions (GCF).",
    "## Prerequisites": "## Предварительные требования",
    "Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf \"Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.\") before using the packages below.": "Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной конфигурации**, описанные в разделе [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf \"Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.\").",
    "* dynatrace-opentelemetry-gcf version 1.247+": "* dynatrace-opentelemetry-gcf версии 1.247+",
    "* Cloud Functions product version: 1st gen, 2nd gen": "* Версия продукта Cloud Functions: 1st gen, 2nd gen",
    "## Installation": "## Установка",
    "To set up OpenTelemetry Python integration on Google Cloud Functions, add the following line to the `requirements.txt` file of your function:": "Чтобы настроить интеграцию OpenTelemetry для Python на Google Cloud Functions, добавьте следующую строку в файл `requirements.txt` функции:",
    "This adds the latest version of the `dynatrace-opentelemetry-gcf` package as a dependency to your function. For more information about managing dependencies, consult the [GCF documentation for Python](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).": "Это добавляет последнюю версию пакета `dynatrace-opentelemetry-gcf` как зависимость функции. Подробнее об управлении зависимостями см. [GCF documentation for Python](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).",
    "## Trace export": "## Экспорт трассировок",
    "To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler function](#instrument).": "Для экспорта трассировок в Dynatrace необходимо [инициализировать трассировку](#initialize), а затем [инструментировать функцию-обработчик](#instrument).",
    "### Initialize tracing": "### Инициализация трассировки",
    "Select one of the following ways to initialize tracing:": "Выберите один из следующих способов инициализации трассировки:",
    "* `configure_dynatrace` function—This is the recommended option unless you need to manually set up tracing components.": "* Функция `configure_dynatrace`: рекомендуемый вариант, если не требуется ручная настройка компонентов трассировки.",
    "Example with `configure_dynatrace` (recommended)": "Пример с `configure_dynatrace` (рекомендуется)",
    "* Manual tracing setup—This allows for a more fine-grained setup of tracing components.": "* Ручная настройка трассировки: позволяет более детально настроить компоненты трассировки.",
    "Example with manual tracing setup": "Пример с ручной настройкой трассировки",
    "The tracing setup code should be implemented to set up tracing only once before any other third-party module is imported. If you use `isort` to sort your imports, we suggest that you [deactivate it](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) while importing the tracing setup module, as shown in the following example:": "Код настройки трассировки должен инициализировать трассировку только один раз, до импорта любых сторонних модулей. Если для сортировки импортов используется `isort`, рекомендуется [отключить его](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) при импорте модуля настройки трассировки, как показано в следующем примере:",
    "### Instrument a handler function": "### Инструментирование функции-обработчика",
    "Use the `wrap_handler` decorator to instrument your handler function as shown in the following example:": "Используйте декоратор `wrap_handler` для инструментирования функции-обработчика, как показано в следующем примере:",
    "## Cold start": "## Холодный старт",
    "When the wrapped handler is invoked for the first time after [cold start](https://cloud.google.com/functions/docs/concepts/exec#cold_starts), the decorator will make additional HTTP requests to fetch metadata from your [Google Cloud environment](https://cloud.google.com/compute/docs/metadata/overview). This metadata is used to set the required attributes for Dynatrace to process the span.": "При первом вызове обёрнутого обработчика после [холодного старта](https://cloud.google.com/functions/docs/concepts/exec#cold_starts) декоратор выполняет дополнительные HTTP-запросы для получения метаданных из [среды Google Cloud](https://cloud.google.com/compute/docs/metadata/overview). Эти метаданные используются для задания необходимых атрибутов, по которым Dynatrace обрабатывает спан.",
    "## Span flush": "## Сброс спанов",
    "By default, the `wrap_handler` decorator automatically performs a flush operation when the decorated function exits to ensure that spans are exported properly. However, flushing spans results in longer execution time, because this operation becomes part of the function's execution logic.": "По умолчанию декоратор `wrap_handler` автоматически выполняет операцию сброса при завершении декорированной функции, чтобы гарантировать корректный экспорт спанов. Однако сброс спанов увеличивает время выполнения, так как эта операция становится частью логики функции.",
    "By providing an additional parameter to the decorator, `@wrap_handler(flush_on_exit=False)`, you can disable the flushing after every invocation. Spans will still be periodically exported in the background.": "Передав декоратору дополнительный параметр `@wrap_handler(flush_on_exit=False)`, можно отключить сброс после каждого вызова. Спаны по-прежнему будут периодически экспортироваться в фоновом режиме.",
    "Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.": "Поскольку код, выполняемый вне контекста функции, может быть завершён в любой момент, Google Cloud Functions не рекомендует такой подход.",
    "* Google Cloud Functions 1st gen": "* Google Cloud Functions 1st gen",
    "Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.": "Выполнение фоновых задач после вызова функции без сброса спанов не гарантировано и может привести к потере спанов. Практика показывает, что в большинстве случаев спаны корректно экспортируются даже без явного сброса.",
    "* Google Cloud Functions 2nd gen": "* Google Cloud Functions 2nd gen",
    "Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.": "Google Cloud Functions 2nd gen поддерживает обработку нескольких одновременных запросов в рамках одного экземпляра функции. Операция сброса одного вызова может увеличить время выполнения другого.",
    "Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycle](https://cloud.google.com/run/docs/container-contract#lifecycle-services).": "Так как экземпляры функции обычно должны оставаться в режиме ожидания для обработки параллельных запросов, можно отключить сброс спанов для повышения производительности. Подробнее см. [Instance lifecycle](https://cloud.google.com/run/docs/container-contract#lifecycle-services).",
    "Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocation](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.": "Обратите внимание: простаивающим экземплярам функции не гарантируется выделение CPU, если режим [CPU allocation](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в `CPU always allocated`.",
    "For details, see [Function execution timeline](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).": "Подробнее см. [Function execution timeline](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).",
    "## Dynatrace overhead": "## Накладные расходы Dynatrace",
    "* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.": "* Экспорт спанов и получение метаданных при холодных стартах занимают время, увеличивая продолжительность выполнения функции и соответственно затраты.",
    "* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.": "* Обратите особое внимание на редко вызываемые функции (как правило, с холодными стартами): они могут требовать больше времени на TCP-рукопожатие при экспорте спанов.",
    "* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.": "* Любые сетевые проблемы между экспортером и бэкендом Dynatrace также могут привести к неожиданно высоким накладным расходам.",
    "## Limitations": "## Ограничения",
    "* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.": "* `DtSpanProcessor` работает только совместно с `DtSampler`. При ручной настройке трассировки обязательно задайте `DtSampler` в качестве сэмплера, иначе спаны могут не экспортироваться.",
    "## Related topics": "## Связанные темы",
    "* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform \"Monitor Google Cloud with Dynatrace.\")": "* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform \"Мониторинг Google Cloud с Dynatrace.\")",
    "* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)": "* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)",
}

PASS = set()

build_one(REL, "opentelemetry-on-gcf-python.md", TRANS, PASS)
qa_one(REL, "opentelemetry-on-gcf-python.md")
