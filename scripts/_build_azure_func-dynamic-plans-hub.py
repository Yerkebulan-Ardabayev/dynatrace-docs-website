# -*- coding: utf-8 -*-
"""L4-IF.73 -- ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans.md"""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions"

TT_AZURE_RU = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_OA_MATRIX_RU = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."
TT_SERVERLESS_RU = "Узнайте, как рассчитывается потребление при бессерверном мониторинге."
TT_DOTNET_RU = "Мониторинг Azure Functions с помощью OpenTelemetry для .NET и Dynatrace."
TT_NODEJS_RU = "Мониторинг Azure Functions с помощью OpenTelemetry для Node.js и Dynatrace."
TT_PYTHON_RU = "Мониторинг Azure Functions с помощью OpenTelemetry для Python и Dynatrace."
TT_OTEL_HUB_RU = "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace."

TRANS = {
    "title: Monitor Azure Functions on Consumption Plans": "title: Мониторинг Azure Functions на планах Consumption",
    "# Monitor Azure Functions on Consumption Plans": "# Мониторинг Azure Functions на планах Consumption",
    "* Overview": "* Обзор",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Apr 20, 2022": "* Опубликовано 20 апреля 2022 г.",
    "Azure Functions let you run code without provisioning or managing servers.": "Azure Functions позволяет запускать код без выделения серверов и управления ими.",
    'This deployment model is sometimes referred to as "serverless" or "Function as a Service" (FaaS).': 'Эта модель развёртывания иногда называется "бессерверной" или "Function as a Service" (FaaS).',
    "* An Azure Function runs in an application on a container managed by Azure. This lets you focus on writing code without worrying about the underlying application or infrastructure.": "* Azure Function выполняется в приложении в контейнере под управлением Azure. Это позволяет сосредоточиться на написании кода, не беспокоясь о базовом приложении или инфраструктуре.",
    "* Azure Functions are ephemeral. This means that the underlying container can be suspended or recycled when there’s no request pending.": "* Azure Functions являются эфемерными. Это означает, что базовый контейнер может быть приостановлен или переработан при отсутствии ожидающих запросов.",
    "## Integration": "## Интеграция",
    '[Trace Azure Functions written in .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")': f'[Трассировка Azure Functions на .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "{TT_DOTNET_RU}")',
    '[Trace Azure Functions written in Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")': f'[Трассировка Azure Functions на Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "{TT_NODEJS_RU}")',
    '[Trace Azure Functions written in Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")': f'[Трассировка Azure Functions на Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "{TT_PYTHON_RU}")',
    "## Monitoring Consumption": "## Мониторинг потребления",
    'For Azure Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.': f'Для Azure Functions мониторинг потребления основан на единицах данных Davis. Подробнее см. в разделе [Бессерверный мониторинг](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "{TT_SERVERLESS_RU}").',
    "## Related topics": "## Связанные темы",
    '* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE_RU}")',
    '* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_OA_MATRIX_RU}")',
    '* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")': f'* [Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "{TT_OTEL_HUB_RU}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "func-dynamic-plans.md", TRANS, PASS)
    qa_one(REL, "func-dynamic-plans.md")
