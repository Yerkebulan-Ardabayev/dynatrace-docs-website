---
title: Azure Service Fabric
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-fabric
scraped: 2026-05-12T11:26:58.145105
---

# Azure Service Fabric

# Azure Service Fabric

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 28 марта 2024 г.

## Возможности

* Полный мониторинг стека на основе OneAgent
* [Расширения для удобного развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурация мониторинга Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM: регионы Azure, масштабируемые наборы и многое другое
* Автоматическая инструментация, включая контейнеризованные приложения

Обратите внимание, что готовой инструментации для модели программирования Azure Service Fabric (Reliable Services и Actors) не предусмотрено. Вместо этого используйте пользовательскую инструментацию с помощью OpenTelemetry.

## Установка

Чтобы развернуть OneAgent на Azure Service Fabric, следуйте той же процедуре, что и для [Azure Virtual Machines Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Узнайте, как установить, настроить и устранить неполадки OneAgent для мониторинга Azure VM Scale Set с использованием расширения VM.").