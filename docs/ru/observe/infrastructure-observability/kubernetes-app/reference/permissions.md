---
title: Permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/reference/permissions
scraped: 2026-03-06T21:11:58.626956
---

# Разрешения

# Разрешения

* Latest Dynatrace
* Reference
* 1-min read
* Published Jan 19, 2024

Это руководство описывает необходимые разрешения для ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и объясняет, как адаптировать их под конкретные роли и требования.

## Пользовательские разрешения

Для полноценного использования всех сценариев применения ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** требуется определённый набор разрешений. Полный список этих разрешений можно найти через Dynatrace Hub.

В Dynatrace Hub выберите **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") для просмотра необходимых разрешений.

Для управления разрешениями в ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** можно назначать политики по умолчанию различным ролям, присвоенным группам пользователей (например, **AppEngine User**, **Storage All Grail Data Read**).

## Настройка разрешений и политик

Dynatrace IAM позволяет детально и гибко определять и назначать разрешения. Эти разрешения можно группировать в политики и затем назначать пользователям или группам. Кроме того, разрешения можно ограничивать конкретными подмножествами объектов Kubernetes с помощью условий, например для определённых кластеров и/или пространств имён.

Для получения дополнительной информации см. [Identity and access management (IAM)](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Пример политики

```
ALLOW hub:catalog:read;



ALLOW storage:buckets:read, storage:entities:read, storage:events:read, storage:logs:read, storage:metrics:read;



ALLOW environment-api:api-tokens:write, environment-api:entities:read, environment-api:entities:write, environment-api:metrics:read, environment-api:security-problems:read, environment-api:slo:read;



ALLOW settings:objects:read, settings:objects:write, state:user-app-states:read, state:user-app-states:write;



ALLOW davis:analyzers:execute, unified-analysis:screen-definition:read;
```
