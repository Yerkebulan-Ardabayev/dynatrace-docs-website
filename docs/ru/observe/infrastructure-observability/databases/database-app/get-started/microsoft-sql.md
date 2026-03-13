---
title: Monitor Microsoft SQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql
scraped: 2026-03-03T21:22:02.020530
---

# Мониторинг базы данных Microsoft SQL

# Мониторинг базы данных Microsoft SQL

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

В Dynatrace поддерживаются три расширения Microsoft SQL:

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует современную архитектуру расширений с возможностями AIOps для упрощения мониторинга баз данных и улучшения межкомандного взаимодействия. Это расширение предоставляет автоматические аналитические данные о метриках производительности базы данных и бизнес-KPI в реальном времени.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует WMI-запросы для сбора ключевых метрик производительности и работоспособности экземпляра SQL Server, работающего на хосте, расширяя вашу видимость.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#overview "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL."): Использует счётчики производительности Windows для сбора ключевых метрик производительности и работоспособности всех экземпляров SQL Server на хосте.

В зависимости от вашего конкретного сценария использования, такого как ограничения доступа среды, требования к производительности и цели мониторинга, вы можете выбрать одно или оба расширения для обеспечения полной видимости.

## Предварительные требования

Убедитесь, что ваша система соответствует требованиям и имеет необходимую информацию о совместимости для полной поддержки функций.

* Для Microsoft SQL Server ознакомьтесь с [требованиями](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#requirements "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.") и [информацией о совместимости](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#compatibility-information "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server (local) ознакомьтесь с [информацией о совместимости](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#compatibility-information "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server local counters ознакомьтесь с [требованиями и совместимостью](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#requirements "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Настройка расширения Microsoft SQL для мониторинга

Для настройки и активации расширения:

* Для Microsoft SQL Server ознакомьтесь с разделом [Активация и настройка Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Для Microsoft SQL Server (local) и Microsoft SQL Server local counters выполните следующие шаги.

  1. Установите OneAgent на хост SQL Server.
  2. Включите мониторинг логов.
  3. Активируйте расширение из Hub.

  Подробнее см. [Шаги активации Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.") и [Шаги активации Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#activation-and-setup "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Наборы функций

Наборы функций определяют, какие метрики собираются при активации расширения.
Ознакомьтесь с разделами ниже, чтобы узнать больше о каждом наборе функций.

* Наборы функций [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Наборы функций [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Наборы функций [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#feature-sets "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Сценарии использования

Ознакомьтесь с этими сценариями использования для получения подробной информации.

* Сценарии использования [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Сценарии использования [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").
* Сценарии использования [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#use-cases "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.").

## Связанные темы

* [Расширение Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2 "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")
* [Расширение Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")
* [Расширение Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local "Улучшите мониторинг работоспособности и производительности серверов Microsoft SQL.")