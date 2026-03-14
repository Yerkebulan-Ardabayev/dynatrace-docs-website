---
title: API топологии и Smartscape
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-03-06T21:12:56.066698
---

# API топологии и Smartscape


* Справочник
* Обновлено 22 марта 2023 г.
* Устарело

Этот API устарел. Вместо него используйте [API отслеживаемых сущностей](entity-v2.md "Узнайте об API отслеживаемых сущностей Dynatrace."). Дополнительную информацию о переходе на новый API можно найти в [руководстве по миграции](../basics/deprecation-migration-guides/topology-v1-to-entity-v2.md "Перенесите автоматизацию на API отслеживаемых сущностей.").

**API топологии и Smartscape** предоставляет сведения о приложениях, сервисах, группах процессов и инфраструктурных сущностях, которые Dynatrace автоматически обнаруживает и отслеживает в данной среде.

Возвращаемая информация содержит важные атрибуты отслеживаемых сущностей, а также исходящие и входящие отношения. Это семейство эндпоинтов организовано по пяти основным уровням среды: приложения, хосты, процессы, группы процессов и сервисы.

### Приложения

* [Получить список](topology-and-smartscape/applications-api/get-all.md "Список всех отслеживаемых приложений через API Dynatrace.")
* [Получить детали](topology-and-smartscape/applications-api/get-an-app.md "Просмотр отслеживаемого приложения через API Dynatrace.")
* [Назначить теги](topology-and-smartscape/applications-api/post-tags.md "Назначение тегов отслеживаемому приложению через API Dynatrace.")
* [Получить базовые данные](topology-and-smartscape/applications-api/get-baseline.md "Просмотр базовых данных отслеживаемого приложения через API Dynatrace.")

### Хосты

* [Получить список](topology-and-smartscape/hosts-api/get-all.md "Список всех отслеживаемых хостов через API Dynatrace.")
* [Получить детали](topology-and-smartscape/hosts-api/get-a-host.md "Просмотр отслеживаемого хоста через API Dynatrace.")
* [Назначить теги](topology-and-smartscape/hosts-api/post-tags.md "Назначение тегов отслеживаемому хосту через API Dynatrace.")

### Процессы

* [Получить список](topology-and-smartscape/processes-api/get-all.md "Список всех отслеживаемых процессов через API Dynatrace.")
* [Получить детали](topology-and-smartscape/processes-api/get-a-process.md "Просмотр отслеживаемого процесса через API Dynatrace.")

### Группы процессов

* [Получить список](topology-and-smartscape/process-groups-api/get-all.md "Список всех отслеживаемых групп процессов через API Dynatrace.")
* [Получить детали](topology-and-smartscape/process-groups-api/get-a-process-group.md "Просмотр отслеживаемой группы процессов через API Dynatrace.")
* [Назначить теги](topology-and-smartscape/process-groups-api/post-tags.md "Назначение тегов отслеживаемой группе процессов через API Dynatrace.")

### Сервисы

* [Получить список](topology-and-smartscape/services-api/get-all.md "Список всех отслеживаемых сервисов через API Dynatrace.")
* [Получить детали](topology-and-smartscape/services-api/get-a-service.md "Просмотр отслеживаемого сервиса через API Dynatrace.")
* [Назначить теги](topology-and-smartscape/services-api/post-tags.md "Назначение тегов сервису через API Dynatrace.")
* [Получить базовые данные](topology-and-smartscape/services-api/get-baseline.md "Просмотр базовых данных отслеживаемого сервиса через API Dynatrace.")

### Создание пользовательского устройства

[Создайте пользовательское устройство](topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api.md "Узнайте, как использовать API Dynatrace для создания пользовательского устройства.") с точными параметрами, которые вам нужны.

### Отправка данных на пользовательское устройство

[Отправьте метрику пользовательского устройства](topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api.md "Узнайте, как использовать API Dynatrace для отправки данных метрики на пользовательское устройство.").

## Связанные темы

* [Визуализация вашей среды через Smartscape Classic](../../analyze-explore-automate/smartscape-classic.md "Узнайте, как Smartscape Classic визуализирует все сущности и зависимости в вашей среде.")
