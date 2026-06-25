---
title: Мониторинг Azure Service Fabric
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric
scraped: 2026-05-12T11:22:55.403313
---

# Мониторинг Azure Service Fabric

# Мониторинг Azure Service Fabric

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 июля 2017 г.

## Возможности

* Мониторинг полного стека на базе OneAgent
* [Расширения для простого развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое
* Автоматическое инструментирование, включая контейнеризированные приложения

Обратите внимание, что готового инструментирования для модели программирования Azure Service Fabric (Reliable Services и Actors) нет. Вместо этого используйте пользовательское инструментирование с помощью OpenTelemetry.

## Установка

Чтобы развернуть OneAgent на Azure Service Fabric, выполните ту же процедуру, что и для [Azure Virtual Machines Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Узнайте, как установить, настроить и устранять неполадки OneAgent для мониторинга Azure VM Scale Set через VM extension.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")