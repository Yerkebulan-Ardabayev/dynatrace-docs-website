---
title: Мониторинг базы данных Microsoft SQL
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql
scraped: 2026-03-03T21:22:02.020530
---

# Мониторинг базы данных Microsoft SQL

# Мониторинг базы данных Microsoft SQL

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

В Dynatrace поддерживаются три расширения Microsoft SQL:

* [Microsoft SQL Server](../../extensions/microsoft-sql-server-2.md#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует современную архитектуру расширений с возможностями AIOps для упрощения мониторинга баз данных и улучшения межкомандного взаимодействия. Это расширение предоставляет автоматические аналитические данные о метриках производительности базы данных и бизнес-KPI в реальном времени.
* [Microsoft SQL Server (local)](../../extensions/microsoft-sql-server-local.md#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует WMI-запросы для сбора ключевых метрик производительности и работоспособности экземпляра SQL Server, работающего на хосте, расширяя вашу видимость.
* [Microsoft SQL Server local counters](../../extensions/microsoft-sql-server-local-counters.md#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует счётчики производительности Windows для сбора ключевых метрик производительности и работоспособности всех экземпляров SQL Server на хосте.

В зависимости от вашего конкретного сценария использования, такого как ограничения доступа среды, требования к производительности и цели мониторинга, вы можете выбрать одно или оба расширения для обеспечения полной видимости.

## Предварительные требования

Убедитесь, что ваша система соответствует требованиям и имеет необходимую информацию о совместимости для полной поддержки функций.

* Для Microsoft SQL Server ознакомьтесь с [требованиями](../../extensions/microsoft-sql-server-2.md#requirements "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.") и [информацией о совместимости](../../extensions/microsoft-sql-server-2.md#compatibility-information "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server (local) ознакомьтесь с [информацией о совместимости](../../extensions/microsoft-sql-server-local.md#compatibility-information "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server local counters ознакомьтесь с [требованиями и совместимостью](../../extensions/microsoft-sql-server-local-counters.md#requirements "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Настройка расширения Microsoft SQL для мониторинга

Для настройки и активации расширения:

* Для Microsoft SQL Server ознакомьтесь с разделом [Активация и настройка Microsoft SQL Server](../../extensions/microsoft-sql-server-2.md#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server (local) и Microsoft SQL Server local counters выполните следующие шаги.

  1. Установите OneAgent на хост SQL Server.
  2. Включите мониторинг логов.
  3. Активируйте расширение из Hub.

  Подробнее см. [Шаги активации Microsoft SQL Server (local)](../../extensions/microsoft-sql-server-local.md#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.") и [Шаги активации Microsoft SQL Server local counters](../../extensions/microsoft-sql-server-local-counters.md#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Наборы функций

Наборы функций определяют, какие метрики собираются при активации расширения.
Ознакомьтесь с разделами ниже, чтобы узнать больше о каждом наборе функций.

* Наборы функций [Microsoft SQL Server](../../extensions/microsoft-sql-server-2.md#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Наборы функций [Microsoft SQL Server (local)](../../extensions/microsoft-sql-server-local.md#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Наборы функций [Microsoft SQL Server local counters](../../extensions/microsoft-sql-server-local-counters.md#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Сценарии использования

Ознакомьтесь с этими сценариями использования для получения подробной информации.

* Сценарии использования [Microsoft SQL Server](../../extensions/microsoft-sql-server-2.md#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Сценарии использования [Microsoft SQL Server (local)](../../extensions/microsoft-sql-server-local.md#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Сценарии использования [Microsoft SQL Server local counters](../../extensions/microsoft-sql-server-local-counters.md#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Связанные темы

* [Расширение Microsoft SQL Server](../../extensions/microsoft-sql-server-2.md "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")
* [Расширение Microsoft SQL Server local counters](../../extensions/microsoft-sql-server-local-counters.md "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")
* [Расширение Microsoft SQL Server (local)](../../extensions/microsoft-sql-server-local.md "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")