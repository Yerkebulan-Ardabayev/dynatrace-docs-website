---
title: Automatically applied tags API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api
scraped: 2026-05-12T12:13:46.375595
---

# Automatically applied tags API

# Automatically applied tags API

* Reference
* Published Oct 22, 2018

Устарело

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "Просмотр таблицы schema builtin:tags.auto-tagging окружения мониторинга через Dynatrace API.") (`builtin:tags.auto-tagging`).

API **Automatically applied tags** позволяет управлять правилами автоматически применяемых тегов. Эти настройки находятся в UI Dynatrace в **Settings > Tags > Automatically applied tags**.

[### Список всех автоматически применяемых тегов

Получить обзор всех автоматически применяемых тегов, хранящихся в вашем окружении.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all "Просмотр всех автоматически применяемых тегов вашего окружения через Dynatrace API.")[### Просмотр автоматически применяемого тега

Получить конфигурацию автоматически применяемого тега по ID конфигурации.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-auto-tag "Просмотр автоматически применяемого тега через Dynatrace API.")

[### Создание автоматически применяемого тега

Создать новый автоматически применяемый тег именно с теми параметрами, которые вам нужны.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/post-auto-tag "Создание автоматически применяемого тега через Dynatrace API.")[### Редактирование автоматически применяемого тега

Обновить существующую конфигурацию автоматически применяемого тега. Также можно создать новый автоматически применяемый тег с указанным ID.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/put-auto-tag "Редактирование автоматически применяемого тега через Dynatrace API.")[### Удаление автоматически применяемого тега

Удалить автоматически применяемый тег, который больше не нужен.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/del-auto-tag "Удаление автоматически применяемого тега через Dynatrace API.")

## Связанные темы

* [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")
* [Теги и метаданные](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")