# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans"

TT_HUB = "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace."
TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."

TRANS = {
    "title: Trace Azure Functions written in Node.js": "title: Трассировка Azure Functions на Node.js",
    "# Trace Azure Functions written in Node.js": "# Трассировка Azure Functions на Node.js",
    "* How-to guide": "* Практическое руководство",
    "* 6-min read": "* Чтение: 6 мин",
    "* Updated on Nov 04, 2025": "* Обновлено 4 ноября 2025 г.",
    "The [`@dynatrace/opentelemetry-azure-functions` module](https://dt-url.net/9603x96) provides APIs for tracing Node.js on Azure Functions.": "Модуль [`@dynatrace/opentelemetry-azure-functions`](https://dt-url.net/9603x96) предоставляет API для трассировки Node.js на Azure Functions.",
    "## Prerequisites": "## Предварительные требования",
    f'Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.': f'Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "{TT_HUB}").',
    "* @dynatrace/opentelemetry-azure-functions version 1.243+": "* @dynatrace/opentelemetry-azure-functions версии 1.243+",
    "## Installation": "## Установка",
    "To set up OpenTelemetry Node.js integration on Azure Functions, run the following command.": "Чтобы настроить интеграцию OpenTelemetry для Node.js на Azure Functions, выполните следующую команду.",
    "## Trace export": "## Экспорт трассировки",
    "Azure Functions can be developed by using either of two different [programming models](https://dt-url.net/9p03lmb), v3 and v4. To accommodate differences between the two models, Dynatrace provides two different ways of trace export:": "Azure Functions можно разрабатывать с использованием одной из двух [моделей программирования](https://dt-url.net/9p03lmb): v3 и v4. Для учёта различий между ними Dynatrace предоставляет два способа экспорта трассировки:",
    "* For programming model v3, the Azure Functions handler is wrapped (with the `wrapHandler` API) to generate and export traces.": "* Для модели программирования v3 обработчик Azure Functions оборачивается (с помощью API `wrapHandler`) для генерации и экспорта трассировок.",
    "* For programming model v4, [Azure Functions Hooks](https://dt-url.net/v323l3e) are used to achieve the same. Note that hooks are available only for the programming model v4.": "* Для модели программирования v4 для той же цели используются [Azure Functions Hooks](https://dt-url.net/v323l3e). Обратите внимание, что хуки доступны только для модели программирования v4.",
    "For details, see below.": "Подробнее см. ниже.",
    "### Programming model v3": "### Модель программирования v3",
    "To export traces to Dynatrace from Azure Functions developed with [programming model v3](https://dt-url.net/n443lxw)": "Для экспорта трассировок в Dynatrace из Azure Functions, разработанных с использованием [модели программирования v3](https://dt-url.net/n443lxw):",
    "1. Select one of the two ways below to initialize tracing.": "1. Выберите один из двух способов инициализации трассировки.",
    "* `NodeTracerProvider`—more lightweight than `NodeSDK`": "* `NodeTracerProvider`: более лёгкий вариант по сравнению с `NodeSDK`",
    "* `NodeSDK`—typically used if you're interested in additional OpenTelemetry signals such as metrics": "* `NodeSDK`: как правило, используется при необходимости работы с дополнительными сигналами OpenTelemetry, например с метриками",
    "It is possible to bundle several Azure Functions into a single Azure Function app. It's therefore important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put a tracing setup code into a shared file as described in the [Azure Functions JavaScript developer guide](https://dt-url.net/t223xf2) and require it at the top of all functions.": "Несколько Azure Functions можно объединить в одно приложение Azure Function app. Поэтому важно инициализировать трассировку один раз на уровне приложения, а не отдельно для каждой функции. Проще всего поместить код настройки трассировки в общий файл, как описано в [руководстве разработчика Azure Functions для JavaScript](https://dt-url.net/t223xf2), и подключить его в начале всех функций.",
    "The tracing setup code should be implemented to set up tracing only once before any other third-party module is required.": "Код настройки трассировки должен выполняться ровно один раз до подключения любых сторонних модулей.",
    "NodeTracerProvider example (recommended)": "Пример с NodeTracerProvider (рекомендуется)",
    "NodeSDK example": "Пример с NodeSDK",
    "2. Wrap your function handler as below and export the wrapped handler.": "2. Оберните обработчик функции, как показано ниже, и экспортируйте обёрнутый обработчик.",
    "### Programming model v4": "### Модель программирования v4",
    "There are two ways to export traces to Dynatrace from Azure Functions developed with [programming model v4](https://dt-url.net/7t03lem).": "Существует два способа экспорта трассировок в Dynatrace из Azure Functions, разработанных с использованием [модели программирования v4](https://dt-url.net/7t03lem).",
    "* Use the `initDynatrace` API.": "* Использование API `initDynatrace`.",
    "* Initialize tracing by registering Azure Function hooks manually.": "* Инициализация трассировки путём регистрации хуков Azure Function вручную.",
    "Regardless of the instrumentation approach you choose, always implement the tracing setup code to set up tracing only once before any other third-party module is required.": "Независимо от выбранного подхода к инструментированию, код настройки трассировки всегда должен выполняться ровно один раз до подключения любых сторонних модулей.",
    "#### Use the `initDynatrace` API": "#### Использование API `initDynatrace`",
    "The `initDynatrace` API registers Azure Function hooks required for tracing and optionally registers required tracing components.": "API `initDynatrace` регистрирует хуки Azure Function, необходимые для трассировки, и при необходимости регистрирует требуемые компоненты трассировки.",
    "You can do this either with or without the OpenTelemetry setup:": "Это можно сделать как с настройкой OpenTelemetry, так и без неё:",
    "* initDynatrace with OpenTelemetry setup (recommended)": "* initDynatrace с настройкой OpenTelemetry (рекомендуется)",
    "Pass `true` as the first argument to the `initDynatrace` to set up tracing and return the registered NodeTracerProvider. Resource attributes for the provider can be passed as the second optional argument.": "Передайте `true` в качестве первого аргумента `initDynatrace`, чтобы настроить трассировку и получить зарегистрированный NodeTracerProvider. Атрибуты ресурса для provider можно передать в качестве второго необязательного аргумента.",
    "* initDynatrace without OpenTelemetry setup": "* initDynatrace без настройки OpenTelemetry",
    "Call `initDynatrace` without parameters to register required Azure Function hooks only and set up tracing manually. This is convenient if customizations are required in the tracing setup.": "Вызовите `initDynatrace` без параметров, чтобы зарегистрировать только необходимые хуки Azure Function и настроить трассировку вручную. Это удобно, если для настройки трассировки требуются дополнительные параметры.",
    "Note that the tracing setup code is the same as for programming model v3 and the example with NodeSDK (from the model v3 above) would work here as well. To make it more convenient, there is the `configureDynatrace` API, which does the same as the above.": "Обратите внимание, что код настройки трассировки аналогичен коду для модели программирования v3, и пример с NodeSDK (из раздела v3 выше) также применим здесь. Для удобства предусмотрен API `configureDynatrace`, выполняющий те же действия.",
    "#### Initializing tracing by registering Azure Function hooks manually.": "#### Инициализация трассировки путём регистрации хуков Azure Function вручную",
    "In cases where you need to register additional Azure Functions hooks, the `initDynatrace` API might not be suitable.": "В случаях, когда требуется зарегистрировать дополнительные хуки Azure Functions, API `initDynatrace` может не подойти.",
    "Because Azure Function hooks are executed in the same order they are registered, it's important to:": "Поскольку хуки Azure Function выполняются в том порядке, в котором они были зарегистрированы, важно:",
    "* Register the Dynatrace Trace Start hook as the first pre-invocation hook": "* Зарегистрировать хук Dynatrace Trace Start первым среди хуков предварительного вызова",
    "* Register the Dynatrace Trace End hook as the last post-invocation hook": "* Зарегистрировать хук Dynatrace Trace End последним среди хуков завершения вызова",
    "Hook execution times are included in the total function execution time. If the order of the registered hooks is incorrect, the function execution time reported by our instrumentation won't be accurate either.": "Время выполнения хуков включается в общее время выполнения функции. Если порядок зарегистрированных хуков нарушен, сообщаемое инструментированием время выполнения функции также будет неточным.",
    "To find out more about Azure Function hooks, see the [Azure Functions Node.js developer guide](https://dt-url.net/uo23lv1).": "Подробнее о хуках Azure Function см. в [руководстве разработчика Azure Functions для Node.js](https://dt-url.net/uo23lv1).",
    "To order hooks as needed, you can use the `registerTraceStartHook` and `registerTraceEndHook` APIs as shown below.": "Для управления порядком хуков используйте API `registerTraceStartHook` и `registerTraceEndHook`, как показано ниже.",
    "## Compatibility": "## Совместимость",
    "| OneAgent version | OpenTelemetry API | OpenTelemetry SDK |": "| Версия OneAgent | OpenTelemetry API | OpenTelemetry SDK |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| 1.243 - 1.255 | 1.x.y | 1.0.x |": "| 1.243 - 1.255 | 1.x.y | 1.0.x |",
    "| 1.257+ | 1.x.y | 1.0.x - 1.7.x |": "| 1.257+ | 1.x.y | 1.0.x - 1.7.x |",
    "| 1.259+ | 1.x.y | 1.0.x - 1.8.x |": "| 1.259+ | 1.x.y | 1.0.x - 1.8.x |",
    "| 1.261+ | 1.x.y | 1.0.x - 1.9.x |": "| 1.261+ | 1.x.y | 1.0.x - 1.9.x |",
    "| 1.265+ | 1.x.y | 1.0.x - 1.10.x |": "| 1.265+ | 1.x.y | 1.0.x - 1.10.x |",
    "| 1.273+ | 1.x.y | 1.0.x - 1.15.x |": "| 1.273+ | 1.x.y | 1.0.x - 1.15.x |",
    "| 1.279+ | 1.x.y | 1.0.x - 1.17.x |": "| 1.279+ | 1.x.y | 1.0.x - 1.17.x |",
    "| 1.283+ | 1.x.y | 1.0.x - 1.18.x |": "| 1.283+ | 1.x.y | 1.0.x - 1.18.x |",
    "| 1.285+ | 1.x.y | 1.0.x - 1.20.x |": "| 1.285+ | 1.x.y | 1.0.x - 1.20.x |",
    "| 1.289+ | 1.x.y | 1.0.x - 1.22.x |": "| 1.289+ | 1.x.y | 1.0.x - 1.22.x |",
    "| 1.293+ | 1.x.y | 1.0.x - 1.24.x |": "| 1.293+ | 1.x.y | 1.0.x - 1.24.x |",
    "| 1.297+ | 1.x.y | 1.0.x - 1.25.x |": "| 1.297+ | 1.x.y | 1.0.x - 1.25.x |",
    "| 1.303+ | 1.x.y | 1.0.x - 1.26.x |": "| 1.303+ | 1.x.y | 1.0.x - 1.26.x |",
    "| 1.307+ | 1.x.y | 1.0.x - 1.29.x |": "| 1.307+ | 1.x.y | 1.0.x - 1.29.x |",
    "| 1.313+ | 1.x.y | 1.0.x - 1.30.x |": "| 1.313+ | 1.x.y | 1.0.x - 1.30.x |",
    "| 1.327+ | 1.x.y | 1.0.x - 2.0.x |": "| 1.327+ | 1.x.y | 1.0.x - 2.0.x |",
    "| 1.331+ | 1.x.y | 1.0.x - 2.2.x |": "| 1.331+ | 1.x.y | 1.0.x - 2.2.x |",
    "| 1.335+ | 1.x.y | 1.0.x - 2.5.x |": "| 1.335+ | 1.x.y | 1.0.x - 2.5.x |",
    "Dynatrace version 1.327+ The `@dynatrace/opentelemetry-azure-functions` module supports OpenTelemetry SDK V2. To use V2 (instead of V1), override the version of `@dynatrace/opentelemetry-core` module (required by `@dynatrace/opentelemetry-azure-functions`) with a version that supports OpenTelemetry SDK V2.": "Dynatrace версии 1.327+ Модуль `@dynatrace/opentelemetry-azure-functions` поддерживает OpenTelemetry SDK V2. Чтобы использовать V2 вместо V1, переопределите версию модуля `@dynatrace/opentelemetry-core` (требуется для `@dynatrace/opentelemetry-azure-functions`), указав версию с поддержкой OpenTelemetry SDK V2.",
    "1. From the table above, choose a version that supports OpenTelemetry SDK V2.": "1. Выберите из таблицы выше версию с поддержкой OpenTelemetry SDK V2.",
    "2. In your `package.json` file, add the `overrides` section and specify one of the versions of the `@dynatrace/opentelemetry-core` module to enforce.": "2. В файле `package.json` добавьте раздел `overrides` и укажите одну из версий модуля `@dynatrace/opentelemetry-core` для принудительного использования.",
    "3. Run `npm install` to apply the changes.": "3. Выполните `npm install`, чтобы применить изменения.",
    "Example:": "Пример:",
    "Once `@dynatrace/opentelemetry-azure-functions` is changed to use OpenTelemetry SDK V2 by default, this override won't be needed anymore.": "Как только `@dynatrace/opentelemetry-azure-functions` будет переведён на использование OpenTelemetry SDK V2 по умолчанию, это переопределение больше не потребуется.",
    "Supported [Azure Functions runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):": "Поддерживаемые версии [Azure Functions runtime](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):",
    "* 4.x": "* 4.x",
    "Supported [Azure Functions programming model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):": "Поддерживаемые [модели программирования Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):",
    "* 3.x": "* 3.x",
    "* 4.x @dynatrace/opentelemetry-azure-functions version 1.289+": "* 4.x @dynatrace/opentelemetry-azure-functions версии 1.289+",
    "## Limitations": "## Ограничения",
    "* Only `async` function handlers are supported.": "* Поддерживаются только обработчики функций типа `async`.",
    "+ This follows the Azure recommendation to use [`async` and `await`](https://dt-url.net/be03x31).": "+ Это соответствует рекомендации Azure использовать [`async` и `await`](https://dt-url.net/be03x31).",
    "+ `wrapHandler` returns any non-`async` function unwrapped, so the function itself will work but no span will be created.": "+ `wrapHandler` возвращает любую функцию без `async` в необёрнутом виде: функция будет работать, но спан создан не будет.",
    "+ Note that async functions were introduced in ECMAScript 2017. No span will be created if an earlier version of ECMAScript is used. In case TypeScript is used, make sure [compilation target](https://dt-url.net/df02zbc) is set to ECMAScript 2017 or higher.": "+ Обратите внимание, что асинхронные функции появились в ECMAScript 2017. Если используется более ранняя версия ECMAScript, спаны создаваться не будут. При использовании TypeScript убедитесь, что [цель компиляции](https://dt-url.net/df02zbc) установлена на ECMAScript 2017 или выше.",
    "* The package supports only the [Consumption plan](https://dt-url.net/ck022yx). While it may work on other plans, we cannot guarantee compatibility or performance.": "* Пакет поддерживает только [план Consumption](https://dt-url.net/ck022yx). На других планах он может работать, однако совместимость и производительность не гарантируются.",
    "* Signaling function completion using the deprecated [`context.done()`](https://dt-url.net/0l23xfy) or [`context.res.send()`](https://dt-url.net/dj43xgq) calls is not supported. Either use a `$return` binding and return the result from the function handler, or use a named `out` binding and set `context.binding.<name>`. For HTTP triggers, setting `context.res` is also supported.": "* Сигнализация о завершении функции с помощью устаревших вызовов [`context.done()`](https://dt-url.net/0l23xfy) или [`context.res.send()`](https://dt-url.net/dj43xgq) не поддерживается. Используйте привязку `$return` и возвращайте результат из обработчика функции, либо используйте именованную привязку `out` и задавайте `context.binding.<name>`. Для HTTP-триггеров также поддерживается установка `context.res`.",
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "opentelemetry-on-azure-functions-nodejs.md", TRANS, PASS)
    qa_one(REL, "opentelemetry-on-azure-functions-nodejs.md")
