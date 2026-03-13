---
title: API топологии и Smartscape
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-03-06T21:12:56.066698
---

# API топологии и Smartscape

# API топологии и Smartscape

* Справочник
* Обновлено 22 марта 2023 г.
* Устарело

Этот API устарел. Вместо него используйте [API отслеживаемых сущностей](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте об API отслеживаемых сущностей Dynatrace."). Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Перенесите автоматизацию на API отслеживаемых сущностей.").

**API топологии и Smartscape** предоставляет сведения о приложениях, сервисах, группах процессов и инфраструктурных сущностях, которые Dynatrace автоматически обнаруживает и отслеживает в данной среде.

Возвращаемая информация содержит важные атрибуты отслеживаемых сущностей, а также исходящие и входящие отношения. Это семейство эндпоинтов организовано по пяти основным уровням среды: приложения, хосты, процессы, группы процессов и сервисы.

### Приложения

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "Список всех отслеживаемых приложений через API Dynatrace.")
* [Получить детали](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "Просмотр отслеживаемого приложения через API Dynatrace.")
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Назначение тегов отслеживаемому приложению через API Dynatrace.")
* [Получить базовые данные](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "Просмотр базовых данных отслеживаемого приложения через API Dynatrace.")

### Хосты

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "Список всех отслеживаемых хостов через API Dynatrace.")
* [Получить детали](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "Просмотр отслеживаемого хоста через API Dynatrace.")
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Назначение тегов отслеживаемому хосту через API Dynatrace.")

### Процессы

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "Список всех отслеживаемых процессов через API Dynatrace.")
* [Получить детали](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "Просмотр отслеживаемого процесса через API Dynatrace.")

### Группы процессов

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "Список всех отслеживаемых групп процессов через API Dynatrace.")
* [Получить детали](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "Просмотр отслеживаемой группы процессов через API Dynatrace.")
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Назначение тегов отслеживаемой группе процессов через API Dynatrace.")

### Сервисы

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Список всех отслеживаемых сервисов через API Dynatrace.")
* [Получить детали](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "Просмотр отслеживаемого сервиса через API Dynatrace.")
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Назначение тегов сервису через API Dynatrace.")
* [Получить базовые данные](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "Просмотр базовых данных отслеживаемого сервиса через API Dynatrace.")

### Создание пользовательского устройства

[Создайте пользовательское устройство](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Узнайте, как использовать API Dynatrace для создания пользовательского устройства.") с точными параметрами, которые вам нужны.

### Отправка данных на пользовательское устройство

[Отправьте метрику пользовательского устройства](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать API Dynatrace для отправки данных метрики на пользовательское устройство.").

## Связанные темы

* [Визуализация вашей среды через Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape Classic визуализирует все сущности и зависимости в вашей среде.")
