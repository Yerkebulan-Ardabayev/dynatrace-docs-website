# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_SITEEXT = "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions через Azure site extension."
TT_OTLP = "Информация об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_DYNPLANS = "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions на бессерверных планах хостинга"
TT_BUILTIN = "Мониторинг Function Services Azure и просмотр доступных метрик."
TT_LOGS = "Использование log forwarding Azure для приёма логов Azure."
TT_SERVERLESS = "Бессерверная наблюдаемость с Dynatrace"

TRANS = {
    "title: Monitor Azure Functions using Azure App Service (built-in)": "title: Мониторинг Azure Functions через Azure App Service (встроенный)",
    "# Monitor Azure Functions using Azure App Service (built-in)": "# Мониторинг Azure Functions через Azure App Service (встроенный)",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Apr 20, 2022": "* Опубликовано 20 апреля 2022 г.",
    "Azure Functions offers a wide range of options to address various Azure Functions [scenarios and use-cases](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios):": "Azure Functions предлагает широкий спектр вариантов для различных [сценариев и случаев использования](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios) Azure Functions:",
    "* Use your preferred language": "* Использование предпочтительного языка программирования",
    "* Automate deployment": "* Автоматизация развёртывания",
    "* Take advantage of flexible [hosting](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)": "* Использование гибкого [хостинга](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)",
    "## Distributed Tracing": "## Распределённая трассировка",
    "With the different options for hosting your functions, Dynatrace provides you with the best options to enable distributed tracing.": "Для различных вариантов хостинга функций Dynatrace предоставляет оптимальные способы включения распределённой трассировки.",
    f'* Dynatrace offers an easy integration for **Azure Functions running on Appservice- (Dedicated) plan** using a [site extension](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.").': f'* Dynatrace предлагает простую интеграцию для **Azure Functions, работающих на плане Appservice- (Dedicated)**, с использованием [site extension](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "{TT_SITEEXT}").',
    "* Tracing Azure Functions on a **Consumption- or Premium-Plan** comes with additional restrictions by the nature of a serverless service, such as using instrumentation agents to fully automatically instrument your code at runtime.": "* Трассировка Azure Functions на плане **Consumption- или Premium-Plan** сопряжена с дополнительными ограничениями, обусловленными природой бессерверного сервиса, такими как использование агентов инструментирования для полностью автоматического инструментирования кода во время выполнения.",
    f'Dynatrace provides distributed tracing for these sandboxed environments based on [OpenTelemetry](https://opentelemetry.io/). If you already use OpenTelemetry to instrument your functions, you can ingest the trace data using [Dynatrace Trace Ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), but we recommend that you use the [Dynatrace exporter](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans"), which adds additional benefits to fully leverage the automatic AI-based analysis capabilities of Dynatrace.': f'Dynatrace обеспечивает распределённую трассировку для этих изолированных окружений на основе [OpenTelemetry](https://opentelemetry.io/). Если OpenTelemetry уже используется для инструментирования функций, данные трассировки можно принять через [Dynatrace Trace Ingest API](/managed/ingest-from/opentelemetry/otlp-api "{TT_OTLP}"), однако рекомендуется использовать [Dynatrace exporter](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "{TT_DYNPLANS}"), который предоставляет дополнительные преимущества для полноценного использования возможностей автоматического анализа на базе ИИ в Dynatrace.',
    f'To make using OpenTelemetry easier, Dynatrace provides [library packages for Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans") to reduce necessary OpenTelemetry boiler-plate code for trace-propagation, applying resource attributes and initialization code as well as aligning with semantic conventions.': f'Для упрощения работы с OpenTelemetry Dynatrace предоставляет [библиотечные пакеты для Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "{TT_DYNPLANS}"), которые сокращают необходимый шаблонный код OpenTelemetry для распространения трассировки, применения атрибутов ресурсов и кода инициализации, а также обеспечивают соответствие семантическим соглашениям.',
    "By using advanced concepts such as [aspect-oriented programming (AOP)](https://en.wikipedia.org/wiki/Aspect-oriented_programming), it is even possible to add fully automatic instrumentation without changing a single line of code, as demonstrated within this community github-project for [Azure Functions .NET](https://github.com/dtPaTh/Azure.Functions.Tracing).": "Используя такие продвинутые концепции, как [аспектно-ориентированное программирование (AOP)](https://en.wikipedia.org/wiki/Aspect-oriented_programming), можно реализовать полностью автоматическое инструментирование без изменения единой строки кода, что продемонстрировано в сообществном проекте на GitHub для [Azure Functions .NET](https://github.com/dtPaTh/Azure.Functions.Tracing).",
    "## Additional visibility using logs and platform metrics": "## Расширенная видимость с помощью логов и платформенных метрик",
    f'To enhance visibility for monitoring your Azure Functions health, we recommend that you [enable capturing service metrics from Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin "Monitor Azure Function Services and view available metrics.") as well as [ingesting logs](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.").': f'Для повышения видимости при мониторинге работоспособности Azure Functions рекомендуется [включить сбор метрик сервиса из Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin "{TT_BUILTIN}"), а также [настроить приём логов](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "{TT_LOGS}").',
    "![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)": "![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)",
    "Azure Function Service": "Azure Function Service",
    "## Related topics": "## Связанные темы",
    f'* [Serverless monitoring](/managed/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")': f'* [Бессерверный мониторинг](/managed/discover-dynatrace/get-started/serverless-monitoring "{TT_SERVERLESS}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-functions.md", TRANS, PASS)
    qa_one(REL, "azure-functions.md")
