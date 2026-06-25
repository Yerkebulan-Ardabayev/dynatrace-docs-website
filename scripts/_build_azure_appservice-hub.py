# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_APPSERVICE = "Мониторинг Azure App Service"
TT_WINEXT = "Установка, настройка, обновление, удаление и устранение неполадок OneAgent для мониторинга Azure App Service на Windows через Azure site extension."
TT_CONTAINERS = "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux."
TT_MONITOR_APP = "Мониторинг Azure App Service (App Service Plan, Web App Deployment Slot) и просмотр доступных метрик."
TT_LOG_FORWARDER = "Использование Azure log forwarding для приёма логов Azure."
TT_SERVERLESS = "Бессерверная наблюдаемость с Dynatrace"

TRANS = {
    "title: Monitor Azure App Service": "title: Мониторинг Azure App Service",
    "# Monitor Azure App Service": "# Мониторинг Azure App Service",
    "* Overview": "* Обзор",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Jan 16, 2023": "* Опубликовано 16 января 2023 г.",
    "Azure App Service provides many different hosting options for Windows, Linux, and containers with shared infrastructure ([App Service plan](https://dt-url.net/f4031wl)), or fully isolated and dedicated infrastructure ([Azure App Service Environment](https://dt-url.net/u0231c3)).": "Azure App Service предоставляет множество вариантов размещения для Windows, Linux и контейнеров с общей инфраструктурой ([App Service Plan](https://dt-url.net/f4031wl)) или полностью изолированной и выделенной инфраструктурой ([Azure App Service Environment](https://dt-url.net/u0231c3)).",
    "## Capabilities": "## Возможности",
    "The App Service integration with Dynatrace provides the following capabilities:": "Интеграция App Service с Dynatrace предоставляет следующие возможности:",
    f'* [Integration for OneAgent on Windows via an extension for easy deployment](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service#install "Install, configure, update, uninstall, and troubleshoot OneAgent for monitoring Azure App Service on Windows using an Azure site extension.")': f'* [Интеграция OneAgent на Windows через расширение для простого развёртывания](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service#install "{TT_WINEXT}")',
    f'* [Integration for OneAgent on Linux and containers](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")': f'* [Интеграция OneAgent на Linux и в контейнерах](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "{TT_CONTAINERS}")',
    "* Automatic distributed tracing and monitoring for .NET/.NET Core, Java, Node.js, PHP, and IIS": "* Автоматическая распределённая трассировка и мониторинг для .NET/.NET Core, Java, Node.js, PHP и IIS",
    "* Enhanced capturing of Azure App Service metadata, such as SKU or Website-Name": "* Расширенный сбор метаданных Azure App Service, таких как SKU или Website-Name",
    f'* Capturing of platform-level metrics and [additional insights into your App-Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Monitor Azure App Service (App Service Plan, Web App Deployment Slot) and view available metrics.") via the [Azure Monitor integration](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* Сбор метрик уровня платформы и [дополнительная аналитика по App Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "{TT_MONITOR_APP}") через [интеграцию с Azure Monitor](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    f'* Capturing of logs via [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")': f'* Сбор логов через [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "{TT_LOG_FORWARDER}")',
    "## Related topics": "## Связанные темы",
    f'* [Serverless monitoring](/managed/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")': f'* [Бессерверный мониторинг](/managed/discover-dynatrace/get-started/serverless-monitoring "{TT_SERVERLESS}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-appservice.md", TRANS, PASS)
    qa_one(REL, "azure-appservice.md")
