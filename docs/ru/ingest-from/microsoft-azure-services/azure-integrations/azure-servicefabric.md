---
title: Мониторинг Azure Service Fabric
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric
scraped: 2026-03-06T21:18:10.162845
---

# Мониторинг Azure Service Fabric


* Последняя версия Dynatrace
* Практическое руководство
* 1 минута чтения
* Опубликовано 19 июля 2017 г.

## Возможности

* Полностековый мониторинг на базе OneAgent
* [Расширения для удобного развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](../../microsoft-azure-services.md "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных виртуальных машин Azure: регионы Azure, масштабируемые наборы и другое
* Автоматическая инструментация, включая контейнеризированные приложения

Обратите внимание, что готовой инструментации (OOTB) для модели программирования Azure Service Fabric (Reliable Services и Actors) не предусмотрено. Вместо этого используйте пользовательскую инструментацию с помощью OpenTelemetry.

## Установка

Чтобы развернуть OneAgent на Azure Service Fabric, следуйте той же процедуре, что и для [масштабируемых наборов виртуальных машин Azure](azure-vmss.md "Узнайте, как установить, настроить и устранить неполадки OneAgent для мониторинга масштабируемых наборов виртуальных машин Azure с помощью расширения виртуальной машины.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../microsoft-azure-services.md "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
