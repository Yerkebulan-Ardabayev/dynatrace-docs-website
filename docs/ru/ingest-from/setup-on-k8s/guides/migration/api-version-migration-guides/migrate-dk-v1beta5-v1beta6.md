---
title: Миграция DynaKube v1beta5 на v1beta6
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6
scraped: 2026-03-02T21:30:43.529124
---

# Миграция DynaKube с v1beta5 на v1beta6


* Последняя версия Dynatrace
* Справочник
* Чтение: 5 мин
* Опубликовано 20 января 2026 г.

Это руководство покажет, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta5` на `apiVersion: dynatrace.com/v1beta6` для DynaKube.

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

Поле `spec.extensions` было перемещено в `spec.extensions.prometheus`, чтобы освободить место для нового поля `spec.extensions.databases`. Функциональность осталась прежней.
