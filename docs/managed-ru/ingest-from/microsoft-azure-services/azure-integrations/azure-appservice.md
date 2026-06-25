---
title: Мониторинг Azure App Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice
scraped: 2026-05-12T11:38:10.860760
---

# Мониторинг Azure App Service

# Мониторинг Azure App Service

* Обзор
* Чтение: 1 мин
* Опубликовано 16 января 2023 г.

Azure App Service предоставляет множество вариантов размещения для Windows, Linux и контейнеров с общей инфраструктурой ([App Service Plan](https://dt-url.net/f4031wl)) или полностью изолированной и выделенной инфраструктурой ([Azure App Service Environment](https://dt-url.net/u0231c3)).

## Возможности

Интеграция App Service с Dynatrace предоставляет следующие возможности:

* [Интеграция OneAgent на Windows через расширение для простого развёртывания](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service#install "Установка, настройка, обновление, удаление и устранение неполадок OneAgent для мониторинга Azure App Service на Windows через Azure site extension.")
* [Интеграция OneAgent на Linux и в контейнерах](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Узнайте, как установить, настроить, обновить и удалить OneAgent в контейнеризированных приложениях на Linux.")
* Автоматическая распределённая трассировка и мониторинг для .NET/.NET Core, Java, Node.js, PHP и IIS
* Расширенный сбор метаданных Azure App Service, таких как SKU или Website-Name
* Сбор метрик уровня платформы и [дополнительная аналитика по App Service Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Мониторинг Azure App Service (App Service Plan, Web App Deployment Slot) и просмотр доступных метрик.") через [интеграцию с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Сбор логов через [log forwarding](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Использование Azure log forwarding для приёма логов Azure.")

## Связанные темы

* [Бессерверный мониторинг](/managed/discover-dynatrace/get-started/serverless-monitoring "Бессерверная наблюдаемость с Dynatrace")