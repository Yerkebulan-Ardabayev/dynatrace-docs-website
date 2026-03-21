---
title: Настройка прав доступа для Live Debugging
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/setup
scraped: 2026-03-04T21:33:29.156035
---

# Настройка разрешений для Live Debugging


* Latest Dynatrace
* How-to guide
* 2-min read

## Разрешения пользователей

Все поддерживаемые значения для каждого разрешения IAM и условия перечислены ниже. Используйте их для определения политик доступа на основе детального набора разрешений и условий, которые могут применяться к каждому сервису отдельно. Дополнительную информацию см. в разделе [Работа с политиками](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Working with policies").

state:user-app-states:read

Разрешает запись необходимых пользовательских настроек

state:user-app-states:write

Разрешает запись необходимых пользовательских настроек

settings:objects:read

Разрешает чтение необходимых клиентских настроек

app-settings:objects:read

Разрешает чтение необходимых настроек, например серверов On-Prem Git

dev-obs:breakpoints:set

Просмотр агентов Observability for Developers и установка точек останова.

dev-obs:breakpoints:manage

Управление точками останова Observability for Developers.

## Установка точек останова

Предоставляет разрешение на установку точек останова Live Debugging на уровне пользователя.

**Условия**:

* `dev-obs:k8s.namespace.name` — имя пространства имён, в котором запущен под.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:k8s.cluster.name` — имя кластера, в котором запущен под.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.entity.process_group` — группа процессов, частью которой является ваше приложение.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:dt.process_group.detected_name` — обнаруженное имя группы процессов, частью которой является ваше приложение.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:host.group` — группа хостов, частью которой является ваше приложение.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `dev-obs:host.name` — имя хоста, частью которого является ваше приложение.

  операторы: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

**Примеры политик**:

* Разрешить установку точек останова для всех экземпляров:

  ```
  ALLOW dev-obs:breakpoints:set;
  ```
* Разрешить установку точек останова для определённой группы хостов:

  ```
  ALLOW dev-obs:breakpoints:set WHERE dev-obs:dt.process_group.detected_name = "my_process_group";
  ```

## Чтение снимков состояния

Предоставляет разрешение на чтение снимков состояния Live Debugging на уровне пользователя.

**Примеры политик**:

* Разрешить чтение снимков состояния:

  ```
  ALLOW storage:application.snapshots:read;


  ALLOW storage:buckets:read WHERE storage:table-name = "application.snapshots";
  ```
