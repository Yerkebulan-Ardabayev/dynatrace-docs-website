---
title: Топология и Smartscape API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
scraped: 2026-02-20T21:09:24.418977
---

# Топология и Smartscape API

# Топология и Smartscape API

* Справка
* Обновлено 22 марта 2023 г.
* Устаревшее

Этот API устарел. Вместо этого используйте [Сущности мониторинга API](/docs/dynatrace-api/environment-api/entity-v2 "Узнайте о сущностях мониторинга Dynatrace API.") . Более подробную информацию о переходе на новый API можно найти в [руководстве по миграции](/docs/dynatrace-api/basics/deprecation-migration-guides/topology-v1-to-entity-v2 "Перенесите свою автоматизацию на сущности мониторинга API.").

**Топология и Smartscape** API предоставляет подробную информацию о приложениях, сервисах, группах процессов и сущностях инфраструктуры, которые Dynatrace автоматически обнаруживает и отслеживает в заданной среде.

Возвращаемая информация содержит важные атрибуты о отслеживаемых сущностях, а также исходящие и входящие отношения. Эта семья конечных точек организована по пяти основным слоям среды: приложения, хосты, процессы, группы процессов и сервисы.

### Приложения

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-all "Список всех отслеживаемых приложений через Dynatrace API.") 
* [Получить подробную информацию](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-an-app "Просмотр отслеживаемого приложения через Dynatrace API.") 
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags "Назначить теги отслеживаемому приложению через Dynatrace API.") 
* [Получить базовые данные](/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline "Просмотр базовых данных отслеживаемого приложения через Dynatrace API.") 

### Хосты

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-all "Список всех отслеживаемых хостов через Dynatrace API.") 
* [Получить подробную информацию](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/get-a-host "Просмотр отслеживаемого хоста через Dynatrace API.") 
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags "Назначить теги отслеживаемому хосту через Dynatrace API.") 

### Процессы

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-all "Список всех отслеживаемых процессов через Dynatrace API.") 
* [Получить подробную информацию](/docs/dynatrace-api/environment-api/topology-and-smartscape/processes-api/get-a-process "Просмотр отслеживаемого процесса через Dynatrace API.") 

### Группы процессов

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-all "Список всех отслеживаемых групп процессов через Dynatrace API.") 
* [Получить подробную информацию](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/get-a-process-group "Просмотр отслеживаемой группы процессов через Dynatrace API.") 
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags "Назначить теги отслеживаемой группе процессов через Dynatrace API.") 

### Сервисы

* [Получить список](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-all "Список всех отслеживаемых сервисов через Dynatrace API.") 
* [Получить подробную информацию](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-a-service "Просмотр отслеживаемого сервиса через Dynatrace API.") 
* [Назначить теги](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/post-tags "Назначить теги сервису через Dynatrace API.") 
* [Получить базовые данные](/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline "Просмотр базовых данных отслеживаемого сервиса через Dynatrace API.") 

### Создать пользовательское устройство

[Создать пользовательское устройство](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api "Узнайте, как использовать Dynatrace API, чтобы создать пользовательское устройство.") с точными параметрами, которые вам нужны.

### Отправить данные на пользовательское устройство

[Отправить метрику пользовательского устройства](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API, чтобы отправить пользовательскую метрику на пользовательское устройство.").

## Связанные темы

* [Визуализация среды через Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape Classic визуализирует все сущности и зависимости в вашей среде.")