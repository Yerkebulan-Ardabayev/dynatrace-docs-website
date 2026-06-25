---
title: Maintenance windows API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api
scraped: 2026-05-12T11:36:43.198871
---

# Maintenance windows API

# Maintenance windows API

* Reference
* Updated on Apr 28, 2020

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Maintenance windows** (`builtin:alerting.maintenance-window`).

Dynatrace использует [maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. Прочитайте о поддерживаемых типах maintenance window.") для обеспечения точности данных мониторинга во время планового обслуживания ваших систем.

API конфигурации **Maintenance windows** позволяет использовать сторонние инструменты для управления maintenance windows и downtime в отслеживаемом окружении.

### Список всех maintenance windows

[Получить обзор](/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-all "Просмотр всех maintenance windows вашего окружения через Dynatrace API.") всех maintenance windows, доступных в вашем Dynatrace-окружении.

### Просмотр maintenance window

[Получить параметры maintenance window](/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-mw "Просмотр maintenance window через Dynatrace API.") по его ID.

### Создание maintenance window

[Создать новое maintenance window](/managed/dynatrace-api/configuration-api/maintenance-windows-api/post-mw "Создание maintenance window через Dynatrace API.") с нужными параметрами.

### Редактирование maintenance window

[Обновить существующую конфигурацию](/managed/dynatrace-api/configuration-api/maintenance-windows-api/put-mw "Редактирование maintenance window через Dynatrace API.") maintenance window.

### Удаление maintenance window

[Удалить maintenance windows](/managed/dynatrace-api/configuration-api/maintenance-windows-api/delete-mw "Удаление maintenance window через Dynatrace API."), которые больше не нужны.

## Связанные темы

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать maintenance window. Прочитайте о поддерживаемых типах maintenance window.")