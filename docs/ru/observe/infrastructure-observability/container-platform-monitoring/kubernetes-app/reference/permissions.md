---
title: Permissions
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/reference/permissions
scraped: 2026-02-06T16:19:43.850239
---

# Разрешения

# Разрешения

* Последняя версия Dynatrace
* Ссылка
* 1 минута чтения
* Опубликовано 19 января 2024 г.

В этом руководстве описаны необходимые разрешения для ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и описано, как настроить их в соответствии с конкретными ролями и требованиями.

## Разрешения пользователя

Чтобы в полной мере использовать все варианты использования ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, требуется определенный набор разрешений. Полный список этих разрешений можно найти через Dynatrace Hub.

В Dynatrace Hub выберите **Kubernetes** ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)"), чтобы просмотреть необходимые разрешения.

Чтобы управлять разрешениями в ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, вы можете назначить политики по умолчанию различным ролям, назначенным группам пользователей (например, **Пользователь AppEngine**, **Хранение всех данных Grail для чтения**).

## Настройка разрешений/политик

Dynatrace IAM позволяет очень подробно и гибко определять и назначать разрешения.Эти разрешения можно сгруппировать в политики, а затем назначить пользователям или группам.Кроме того, разрешения могут быть нацелены на определенные подмножества объектов Kubernetes с помощью условий, например, для определенных кластеров и/или пространств имен.

Для получения дополнительной информации см. [Управление идентификацией и доступом (IAM)](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Пример политики

```
ALLOW hub:catalog:read;



ALLOW storage:buckets:read, storage:entities:read, storage:events:read, storage:logs:read, storage:metrics:read;



ALLOW environment-api:api-tokens:write, environment-api:entities:read, environment-api:entities:write, environment-api:metrics:read, environment-api:security-problems:read, environment-api:slo:read;



ALLOW settings:objects:read, settings:objects:write, state:user-app-states:read, state:user-app-states:write;



ALLOW davis:analyzers:execute, unified-analysis:screen-definition:read;
```