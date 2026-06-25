# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions"

TT_ENABLE = "Включение мониторинга Azure в Dynatrace."
TT_TF = "Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)"
TT_DASH = "Узнайте, как создавать и редактировать дашборды Dynatrace."

TRANS = {
    "title: Monitor Function Service (built-in)": "title: Мониторинг Function Service (встроенный)",
    "# Monitor Function Service (built-in)": "# Мониторинг Function Service (встроенный)",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Feb 10, 2025": "* Обновлено 10 февраля 2025 г.",
    "Dynatrace ingests metrics from Azure Metrics API for **Azure Function App**. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.": "Dynatrace получает метрики из Azure Metrics API для **Azure Function App**. Для каждого экземпляра сервиса можно просматривать метрики, разбивать их по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.",
    "## Prerequisites": "## Предварительные требования",
    "* Environment ActiveGate": "* Environment ActiveGate",
    "* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.": "* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.",
    "## Enable monitoring": "## Включение мониторинга",
    f'To learn how to enable service monitoring, see [Enable service monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").': f'О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "{TT_ENABLE}").',
    "## View service metrics": "## Просмотр метрик сервиса",
    "You can view Azure service metrics in your Dynatrace environment on the Azure subscription page or on your own dashboard.": "Метрики сервисов Azure можно просматривать в окружении Dynatrace на странице подписки Azure или на собственном дашборде.",
    f"Values in the table depend upon the selected timeframe. For more details, see [Troubleshoot timeframe comparison for Azure monitoring setup)](https://dt-url.net/7j438f0).": f"Значения в таблице зависят от выбранного временного интервала. Подробнее см. в разделе [Устранение неполадок со сравнением временных интервалов при настройке мониторинга Azure)](https://dt-url.net/7j438f0).",
    "### View metrics on the Azure account page": "### Просмотр метрик на странице учётной записи Azure",
    "To access metrics on the Azure account page": "Чтобы получить доступ к метрикам на странице учётной записи Azure",
    "1. Go to **Azure**.": "1. Перейдите в **Azure**.",
    "2. Choose the Azure subscription.": "2. Выберите подписку Azure.",
    "3. Select the service whose metrics you want to check. Metrics for the selected service are visible under the infographic in the service section, similarly to the example below.": "3. Выберите сервис, метрики которого нужно проверить. Метрики выбранного сервиса отображаются под инфографикой в разделе сервиса, как в примере ниже.",
    "![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)": "![Azure service metrics](https://dt-cdn.net/images/azure-service-1109-9488bfa5e4.png)",
    "Azure service metrics": "Azure service metrics",
    "### View metrics on a dashboard": "### Просмотр метрик на дашборде",
    f'You can create your own dashboard for viewing Azure service metrics. For information on how to create dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").': f'Для просмотра метрик сервисов Azure можно создать собственный дашборд. О том, как создавать дашборды, см. в разделе [Создание и редактирование дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "{TT_DASH}").',
    "## Available metrics": "## Доступные метрики",
    "Metrics visibility depends on the type of application.": "Видимость метрик зависит от типа приложения.",
    "* builtin:cloud.azure.appService": "* builtin:cloud.azure.appService",
    "+ for WebApps (`Microsoft.Web/sites, kind = app`)": "+ для WebApps (`Microsoft.Web/sites, kind = app`)",
    "* builtin:cloud.azure.appService.functions": "* builtin:cloud.azure.appService.functions",
    "+ for FunctionApps (`Microsoft.Web/sites, kind = functionapp`)": "+ для FunctionApps (`Microsoft.Web/sites, kind = functionapp`)",
    '+ for Logic Apps created on the Standard Plan (`"type": "Microsoft.Web/sites", "kind": "functionapp,workflowapp"`)': '+ для Logic Apps, созданных на Standard Plan (`"type": "Microsoft.Web/sites", "kind": "functionapp,workflowapp"`)',
    "| Metric key | Name | Unit | Aggregations | Monitoring consumption |": "| Ключ метрики | Имя | Единица измерения | Агрегации | Потребление мониторинга |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin | DDUs |": "| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin | DDUs |",
    "| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |": "| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue | DDUs |",
    "| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue | DDUs |": "| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue | DDUs |",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "monitor-func-service-builtin.md", TRANS, PASS)
    qa_one(REL, "monitor-func-service-builtin.md")
