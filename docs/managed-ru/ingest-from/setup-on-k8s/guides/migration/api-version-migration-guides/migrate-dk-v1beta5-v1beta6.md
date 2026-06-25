---
title: Миграция DynaKube с v1beta5 на v1beta6
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6
scraped: 2026-05-12T12:14:38.501346
---

# Миграция DynaKube с v1beta5 на v1beta6

# Миграция DynaKube с v1beta5 на v1beta6

* Справочник
* Чтение: 5 мин
* Опубликовано 20 января 2026 г.

В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta5` на `apiVersion: dynatrace.com/v1beta6` для DynaKube.

## Жизненный цикл поддержки

### v1beta5

**Введено в**: Dynatrace Operator версии 1.6.0

### v1beta6

**Введено в**: Dynatrace Operator версии 1.8.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились.

### Перемещённые поля

#### `spec.extensions`

Поле `spec.extensions` было перемещено в `spec.extensions.prometheus` для поддержки нового поля `spec.extensions.databases`. Функциональность осталась прежней.