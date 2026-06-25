---
title: Topology and Smartscape API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-05-12T11:14:32.953086
---

# Topology and Smartscape API

# Topology and Smartscape API

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

API **Topology and Smartscape** возвращает детали о приложениях, сервисах, process groups и инфраструктурных сущностях, которые Dynatrace автоматически обнаруживает и отслеживает в указанном окружении.

Возвращаемая информация содержит важные атрибуты отслеживаемых сущностей, а также исходящие и входящие связи. Семейство endpoint'ов организовано по пяти основным слоям окружения: applications, hosts, processes, process groups и services.

### Applications

* [Получить список](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "Список всех отслеживаемых приложений через Dynatrace API.")
* [Получить детали](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "Просмотр отслеживаемого приложения через Dynatrace API.")
* [Назначить теги](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Назначение тегов отслеживаемому приложению через Dynatrace API.")
* [Получить baseline-данные](/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "Просмотр baseline-данных отслеживаемого приложения через Dynatrace API.")

### Hosts

* [Получить список](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "Список всех отслеживаемых хостов через Dynatrace API.")
* [Получить детали](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "Просмотр отслеживаемого хоста через Dynatrace API.")
* [Назначить теги](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Назначение тегов отслеживаемому хосту через Dynatrace API.")

### Processes

* [Получить список](/managed/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "Список всех отслеживаемых процессов через Dynatrace API.")
* [Получить детали](/managed/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "Просмотр отслеживаемого процесса через Dynatrace API.")

### Process groups

* [Получить список](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "Список всех отслеживаемых process groups через Dynatrace API.")
* [Получить детали](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "Просмотр отслеживаемой process group через Dynatrace API.")
* [Назначить теги](/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Назначение тегов отслеживаемой process group через Dynatrace API.")

### Services

* [Получить список](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Список всех отслеживаемых сервисов через Dynatrace API.")
* [Получить детали](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "Просмотр отслеживаемого сервиса через Dynatrace API.")
* [Назначить теги](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Назначение тегов сервису через Dynatrace API.")
* [Получить baseline-данные](/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "Просмотр baseline-данных отслеживаемого сервиса через Dynatrace API.")

### Создать custom device

[Создание custom device](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Узнайте, как использовать Dynatrace API для создания custom device.") с нужными параметрами.

### Отправка данных в custom device

[Отправка метрики custom device](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API для отправки точки данных пользовательской метрики в custom device.").

## Связанные темы

* [Visualize your environment through Smartscape](/managed/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape визуализирует все сущности и зависимости в вашем окружении.")