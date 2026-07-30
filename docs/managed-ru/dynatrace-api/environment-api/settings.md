---
title: Settings API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings
---

# Settings API

# Settings API

* Справочник
* Обновлено 09 июля 2026

[### Ключевые концепции

Перед началом работы нужно понять ключевые концепции Settings API: области, схемы, внешние идентификаторы, пагинацию и управление параллелизмом.](/managed/dynatrace-api/environment-api/settings/key-concepts "Изучить ключевые концепции Settings API: области, схемы, внешние идентификаторы, пагинацию и управление параллелизмом.")

## Schemas

[### Список схем

Получить обзор всех схем настроек в окружении.](/managed/dynatrace-api/environment-api/settings/schemas/get-all "Просмотр всех схем настроек среды мониторинга через Dynatrace API.")[### Просмотр схемы

Получить параметры схемы.](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.")

## Objects

[### Список объектов

Получить обзор объектов настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API.")[### Просмотр объекта

Получить параметры объекта настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-object "Просмотр объекта настроек через Dynatrace API.")

[### Создание объекта

Создать новый объект настроек или валидировать объект, над которым ведётся работа.](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация объекта настроек через Dynatrace API.")[### Редактирование объекта

Обновить существующий объект настроек.](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование объекта настроек через Dynatrace API.")[### Удаление объекта

Удалить объект настроек, который больше не нужен.](/managed/dynatrace-api/environment-api/settings/objects/del-object "Удаление объекта настроек через Dynatrace API.")[### Просмотр значений

Проверить фактическую конфигурацию объекта настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "Просмотр фактической конфигурации схемы настроек через Dynatrace API.")

## Permissions

[### Список разрешений объекта

Получить все разрешения, установленные на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-permissions "Просмотр всех разрешений объекта настроек через Dynatrace API.")[### Добавление разрешения объекта

Добавить разрешения для одного аксессора на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/post-permission "Добавление разрешений для одного аксессора на объекте настроек через Dynatrace API.")

[### Просмотр разрешения all-users

Получить разрешения аксессора all-users на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-permission-all-users "Просмотр разрешений аксессора all-users на объекте настроек через Dynatrace API.")[### Обновление разрешения all-users

Обновить разрешения аксессора all-users на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/put-permission-all-users "Обновление разрешений аксессора all-users на объекте настроек через Dynatrace API.")[### Удаление разрешения all-users

Удалить разрешения аксессора all-users с объекта настроек.](/managed/dynatrace-api/environment-api/settings/objects/del-permission-all-users "Удаление разрешений аксессора all-users с объекта настроек через Dynatrace API.")

[### Просмотр разрешения аксессора

Получить разрешения конкретного аксессора на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/get-permission "Просмотр разрешений аксессора на объекте настроек через Dynatrace API.")[### Обновление разрешения аксессора

Обновить разрешения конкретного аксессора на объекте настроек.](/managed/dynatrace-api/environment-api/settings/objects/put-permission "Обновление разрешений аксессора на объекте настроек через Dynatrace API.")[### Удаление разрешения аксессора

Удалить разрешения конкретного аксессора с объекта настроек.](/managed/dynatrace-api/environment-api/settings/objects/del-permission "Удаление разрешений аксессора с объекта настроек через Dynatrace API.")

[### Передача владения

Передать владение объектом настроек другому пользователю.](/managed/dynatrace-api/environment-api/settings/objects/post-transfer-ownership "Передача владения объектом настроек через Dynatrace API.")

## Связанные темы

* [Dynatrace settings framework](/managed/manage/settings/settings-20 "Введение в фреймворк Settings 2.0")