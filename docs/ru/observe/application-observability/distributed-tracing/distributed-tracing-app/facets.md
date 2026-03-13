---
title: Manage facets
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/distributed-tracing-app/facets
scraped: 2026-03-06T21:22:48.617165
---

# Управление фасетами

# Управление фасетами

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 23, 2025

Эта статья содержит информацию о том, как управлять фасетами, чтобы они соответствовали предпочтительному способу фильтрации в приложении Distributed Tracing.

## Прежде чем начать

Предварительные требования

* [Настройте разрешения Grail для Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.").

## Управление всеми фасетами

Чтобы управлять тем, какие фасеты вашей среды отображаются:

1. Перейдите в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Выберите **Show facets**.
3. Установите или снимите флажки с элементов в предварительно определённых категориях.

   * Установите флажок категории, чтобы выбрать или снять выбор со всех фасетов категории.
   * Выберите, чтобы просмотреть фасеты в категории и выбрать или снять их выбор.
4. Выберите **Save**.

## Возврат к настройкам по умолчанию

Если вы ранее изменяли фасеты и хотите вернуться к настройкам по умолчанию:

1. Перейдите в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Выберите **Show facets**.
3. Выберите **Reset facet to default**.
4. Выберите **Confirm reset?**

## Редактирование фасета

1. Перейдите в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Разверните категорию фасетов и выберите фасет, который хотите отредактировать.
3. Выберите рядом с названием фасета, затем **Edit facet**.
4. Внесите необходимые изменения и выберите **Save**.

## Скрытие фасета

Чтобы скрыть фасет из списка:

1. Перейдите в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Разверните категорию фасетов и выберите фасет, который хотите скрыть.
3. Выберите рядом с названием фасета, затем **Hide facet**.

## Группировка фасетов

Чтобы сгруппировать записи по атрибутам:

1. Перейдите в ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** > **Explorer**.
2. Разверните категорию фасетов и выберите фасет, который хотите использовать для группировки.
3. Выберите рядом с названием фасета, затем **Group by**.

Таблица обновится с учётом выбранных атрибутов. Чтобы изменить выбор фильтра, выберите поле **Group by:** и добавьте или удалите любой атрибут из списка. Если убрать все атрибуты, таблица вернётся к стандартному виду.
