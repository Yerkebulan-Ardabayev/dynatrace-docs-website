# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md

Anchor file for the Azure batch: validates the shared engine on Azure paths and
demonstrates the grounded glossary in a worked example.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."

TRANS = {
    "title: Monitor Azure Service Fabric": "title: Мониторинг Azure Service Fabric",
    "# Monitor Azure Service Fabric": "# Мониторинг Azure Service Fabric",
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Jul 19, 2017": "* Опубликовано 19 июля 2017 г.",
    "## Capabilities": "## Возможности",
    "* Full-stack monitoring powered by OneAgent": "* Мониторинг полного стека на базе OneAgent",
    "* [Extensions for easy deployment of OneAgent](#installation)": "* [Расширения для простого развёртывания OneAgent](#installation)",
    f'* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    "* Enhanced support for Azure VM Metadata such as Azure regions, scale sets and more": "* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое",
    "* Automatic instrumentation including containerized applications": "* Автоматическое инструментирование, включая контейнеризированные приложения",
    "Note that we don't have an OOTB instrumentation for the Azure Service Fabric Programming Model (Reliable Services and Actors). Instead, use a custom instrumentation using OpenTelemetry.": "Обратите внимание, что готового инструментирования для модели программирования Azure Service Fabric (Reliable Services и Actors) нет. Вместо этого используйте пользовательское инструментирование с помощью OpenTelemetry.",
    "## Installation": "## Установка",
    """To deploy OneAgent on Azure Service Fabric, follow the same procedure as for [Azure Virtual Machines Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.").""": """Чтобы развернуть OneAgent на Azure Service Fabric, выполните ту же процедуру, что и для [Azure Virtual Machines Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Узнайте, как установить, настроить и устранять неполадки OneAgent для мониторинга Azure VM Scale Set через VM extension.").""",
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    '* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': '* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-servicefabric.md", TRANS, PASS)
    qa_one(REL, "azure-servicefabric.md")
