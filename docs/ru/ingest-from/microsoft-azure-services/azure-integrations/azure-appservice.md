---
title: Мониторинг Azure App Service
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice
scraped: 2026-03-06T21:18:06.853367
---

# Мониторинг Azure App Service

# Мониторинг Azure App Service

* Последняя Dynatrace
* Обзор
* 1 мин. чтения
* Опубликовано 16 января 2023 г.

Azure App Service предоставляет множество различных вариантов размещения для Windows, Linux и контейнеров с общей инфраструктурой ([App Service plan](https://dt-url.net/f4031wl)) или полностью изолированной и выделенной инфраструктурой ([Azure App Service Environment](https://dt-url.net/u0231c3)).

## Возможности

Интеграция App Service с Dynatrace предоставляет следующие возможности:

* [Интеграция OneAgent в Windows с помощью расширения для удобного развёртывания](azure-appservice/integrate-oneagent-on-azure-app-service.md#install "Установка, настройка, обновление, удаление и устранение неполадок OneAgent для мониторинга Azure App Service на Windows через расширение сайта Azure.")
* [Интеграция OneAgent в Linux и контейнерах](azure-appservice/integrate-oneagent-on-web-app-for-containers.md "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнерных приложениях на Linux.")
* Автоматическая распределённая трассировка и мониторинг для .NET/.NET Core, Java, Node.js, PHP и IIS
* Расширенный сбор метаданных Azure App Service, таких как SKU или Website-Name
* Сбор метрик уровня платформы и [дополнительная информация о вашем App Service Plan](azure-appservice/monitor-app-service.md "Мониторинг Azure App Service (App Service Plan, Web App Deployment Slot) и просмотр доступных метрик.") через [интеграцию Azure Monitor](../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
* Сбор журналов с помощью [пересылки логов](set-up-log-forwarder-azure.md "Использование пересылки логов Azure для приёма логов Azure.")

## Связанные темы

* [Мониторинг бессерверных приложений](../../../discover-dynatrace/get-started/serverless-monitoring.md "Наблюдаемость бессерверных приложений с помощью Dynatrace")
