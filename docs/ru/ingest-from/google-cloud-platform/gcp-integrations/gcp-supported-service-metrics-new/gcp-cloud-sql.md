---
title: Мониторинг Google Cloud SQL
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql
scraped: 2026-03-06T21:26:56.584086
---

# Мониторинг Google Cloud SQL

# Мониторинг Google Cloud SQL

* Последняя версия Dynatrace
* Практическое руководство
* 4 мин. чтения
* Опубликовано 17 янв. 2022 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

[Настройка интеграции](../gcp-guide/deploy-k8.md "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace."), [Data Explorer](../../../../analyze-explore-automate/explorer.md "Запрашивайте метрики и преобразуйте результаты для получения нужных данных."), а также в плитках дашбордов.

## Таблица метрик

Для Google Cloud SQL доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| cloudsql\_database/default\_metrics | Запросы на автоматическое переключение | Count | cloudsql.googleapis.com/database/auto\_failover\_request\_count |
| cloudsql\_database/default\_metrics | Доступность для переключения | Count | cloudsql.googleapis.com/database/available\_for\_failover |
| cloudsql\_database/default\_metrics | Зарезервированные ядра CPU | Count | cloudsql.googleapis.com/database/cpu/reserved\_cores |
| cloudsql\_database/default\_metrics | Использование CPU | Second | cloudsql.googleapis.com/database/cpu/usage\_time |
| cloudsql\_database/default\_metrics | Утилизация CPU | Percent | cloudsql.googleapis.com/database/cpu/utilization |
| cloudsql\_database/default\_metrics | Использовано байтов | Byte | cloudsql.googleapis.com/database/disk/bytes\_used |
| cloudsql\_database/default\_metrics | Квота диска | Byte | cloudsql.googleapis.com/database/disk/quota |
| cloudsql\_database/default\_metrics | Операции чтения диска | Count | cloudsql.googleapis.com/database/disk/read\_ops\_count |
| cloudsql\_database/default\_metrics | Утилизация диска | Count | cloudsql.googleapis.com/database/disk/utilization |
| cloudsql\_database/default\_metrics | Операции записи диска | Count | cloudsql.googleapis.com/database/disk/write\_ops\_count |
| cloudsql\_database/default\_metrics | Состояние экземпляра | Unspecified | cloudsql.googleapis.com/database/instance\_state |
| cloudsql\_database/default\_metrics | Квота памяти | Byte | cloudsql.googleapis.com/database/memory/quota |
| cloudsql\_database/default\_metrics | Общее использование памяти | Byte | cloudsql.googleapis.com/database/memory/total\_usage |
| cloudsql\_database/default\_metrics | Использование памяти | Byte | cloudsql.googleapis.com/database/memory/usage |
| cloudsql\_database/default\_metrics | Утилизация памяти | Count | cloudsql.googleapis.com/database/memory/utilization |
| cloudsql\_database/default\_metrics | Грязные страницы InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_dirty |
| cloudsql\_database/default\_metrics | Свободные страницы InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_free |
| cloudsql\_database/default\_metrics | Всего страниц InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_total |
| cloudsql\_database/default\_metrics | Вызовы fsync InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_data\_fsyncs |
| cloudsql\_database/default\_metrics | Вызовы fsync журнала InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_os\_log\_fsyncs |
| cloudsql\_database/default\_metrics | Прочитанные страницы InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_read |
| cloudsql\_database/default\_metrics | Записанные страницы InnoDB | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_written |
| cloudsql\_database/default\_metrics | Запросы | Count | cloudsql.googleapis.com/database/mysql/queries |
| cloudsql\_database/default\_metrics | Вопросы | Count | cloudsql.googleapis.com/database/mysql/questions |
| cloudsql\_database/default\_metrics | Полученные сетевые байты MySQL | Byte | cloudsql.googleapis.com/database/mysql/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Доступность для переключения (устаревшее) | Count | cloudsql.googleapis.com/database/mysql/replication/available\_for\_failover |
| cloudsql\_database/default\_metrics | Номер последней ошибки потока ввода-вывода | Count | cloudsql.googleapis.com/database/mysql/replication/last\_io\_errno |
| cloudsql\_database/default\_metrics | Номер последней ошибки SQL-потока | Count | cloudsql.googleapis.com/database/mysql/replication/last\_sql\_errno |
| cloudsql\_database/default\_metrics | Задержка реплики | Second | cloudsql.googleapis.com/database/mysql/replication/seconds\_behind\_master |
| cloudsql\_database/default\_metrics | Состояние потока ввода-вывода Slave | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_io\_running\_state |
| cloudsql\_database/default\_metrics | Состояние SQL-потока Slave | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_sql\_running\_state |
| cloudsql\_database/default\_metrics | Отправленные сетевые байты MySQL | Byte | cloudsql.googleapis.com/database/mysql/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Подключения Cloud SQL | Count | cloudsql.googleapis.com/database/network/connections |
| cloudsql\_database/default\_metrics | Полученные байты | Byte | cloudsql.googleapis.com/database/network/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Отправленные байты | Byte | cloudsql.googleapis.com/database/network/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Время выполнения | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/execution\_time |
| cloudsql\_database/default\_metrics | Время ввода-вывода | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/io\_time |
| cloudsql\_database/default\_metrics | Задержка | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/latencies |
| cloudsql\_database/default\_metrics | Агрегированное время блокировки | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/lock\_time |
| cloudsql\_database/default\_metrics | Затронутые строки | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/row\_count |
| cloudsql\_database/default\_metrics | Доступ к кэшу общих блоков | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Время выполнения по запросу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/execution\_time |
| cloudsql\_database/default\_metrics | Время ввода-вывода по запросу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/io\_time |
| cloudsql\_database/default\_metrics | Задержка по запросу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/latencies |
| cloudsql\_database/default\_metrics | Время блокировки по запросу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/lock\_time |
| cloudsql\_database/default\_metrics | Затронутые строки по запросу | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/row\_count |
| cloudsql\_database/default\_metrics | Доступ к кэшу общих блоков по запросу | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Время выполнения по тегу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/execution\_time |
| cloudsql\_database/default\_metrics | Время ввода-вывода по тегу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/io\_time |
| cloudsql\_database/default\_metrics | Задержка по тегу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/latencies |
| cloudsql\_database/default\_metrics | Время блокировки по тегу | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/lock\_time |
| cloudsql\_database/default\_metrics | Затронутые строки по тегу | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/row\_count |
| cloudsql\_database/default\_metrics | Доступ к кэшу общих блоков по тегу | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Подключения PostgreSQL | Count | cloudsql.googleapis.com/database/postgresql/num\_backends |
| cloudsql\_database/default\_metrics | Отставание в байтах | Byte | cloudsql.googleapis.com/database/postgresql/replication/replica\_byte\_lag |
| cloudsql\_database/default\_metrics | Количество транзакций | Count | cloudsql.googleapis.com/database/postgresql/transaction\_count |
| cloudsql\_database/default\_metrics | Задержка реплики | Second | cloudsql.googleapis.com/database/replication/replica\_lag |
| cloudsql\_database/default\_metrics | Сервер работает | Count | cloudsql.googleapis.com/database/up |
| cloudsql\_database/default\_metrics | Время работы | Second | cloudsql.googleapis.com/database/uptime |

## Связанные темы

* [Интеграции Google Cloud](../../gcp-integrations.md "Настройка и конфигурирование Dynatrace на Google Cloud.")
