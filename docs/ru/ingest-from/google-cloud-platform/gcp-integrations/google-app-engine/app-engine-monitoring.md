---
title: Мониторинг Google App Engine с метриками Operations suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring
scraped: 2026-03-06T21:34:13.395203
---

* 3 мин. чтения

Интеграция Dynatrace с Google Cloud использует данные, собранные из Google Operations API, для непрерывного мониторинга работоспособности и производительности сервисов Google Cloud. Помимо объединения всех релевантных данных в дашборды, она также обеспечивает оповещения и отслеживание событий.

## Предварительные требования

Настройка интеграции

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически начинает мониторинг ряда предустановленных сервисов Google Cloud и наборов функций (метрик). Помимо них, вы можете добавить дополнительные сервисы или наборы функций для мониторинга. Подробнее см. в разделе [Добавление и удаление сервисов](../gcp-guide/deploy-k8.md#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для данного сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции вы можете просматривать метрики отслеживаемых сервисов в браузере метрик, Data Explorer, а также в плитках дашбордов.

## Таблица метрик

Для Google App Engine доступны следующие наборы функций.

| Набор функций | Название | Единица | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| gae\_app/default\_metrics | Количество API-запросов агента мониторинга | Count | agent.googleapis.com/agent/api\_request\_count |
| gae\_app/default\_metrics | Количество записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_count |
| gae\_app/default\_metrics | Количество повторных записей лога агента логирования | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gae\_app/default\_metrics | Использование памяти агентом мониторинга | Byte | agent.googleapis.com/agent/memory\_usage |
| gae\_app/default\_metrics | Количество точек метрик агента мониторинга | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gae\_app/default\_metrics | Количество API-запросов агента логирования | Count | agent.googleapis.com/agent/request\_count |
| gae\_app/default\_metrics | Размер меток процессов агента мониторинга | Byte | agent.googleapis.com/agent/streamspace\_size |
| gae\_app/default\_metrics | Агент мониторинга ограничивает процессы | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gae\_app/default\_metrics | Время работы агента мониторинга/логирования | Second | agent.googleapis.com/agent/uptime |
| gae\_app/default\_metrics | Ёмкость утилизации метрик автомасштабирования | Count | appengine.googleapis.com/flex/autoscaler/capacity |
| gae\_app/default\_metrics | Текущая утилизация метрик автомасштабирования | Count | appengine.googleapis.com/flex/autoscaler/current\_utilization |
| gae\_app/default\_metrics | Подключения | Count | appengine.googleapis.com/flex/connections/current |
| gae\_app/default\_metrics | Зарезервированные ядра | Count | appengine.googleapis.com/flex/cpu/reserved\_cores |
| gae\_app/default\_metrics | Утилизация CPU | Percent | appengine.googleapis.com/flex/cpu/utilization |
| gae\_app/default\_metrics | Прочитано байт с диска | Byte | appengine.googleapis.com/flex/disk/read\_bytes\_count |
| gae\_app/default\_metrics | Записано байт на диск | Byte | appengine.googleapis.com/flex/disk/write\_bytes\_count |
| gae\_app/default\_metrics | Получено сетевых байт | Byte | appengine.googleapis.com/flex/network/received\_bytes\_count |
| gae\_app/default\_metrics | Отправлено сетевых байт | Byte | appengine.googleapis.com/flex/network/sent\_bytes\_count |
| gae\_app/default\_metrics | Количество перехватов | Count | appengine.googleapis.com/http/server/dos\_intercept\_count |
| gae\_app/default\_metrics | Количество отказов по квоте | Count | appengine.googleapis.com/http/server/quota\_denial\_count |
| gae\_app/default\_metrics | Количество ответов | Count | appengine.googleapis.com/http/server/response\_count |
| gae\_app/default\_metrics | Задержка ответов | MilliSecond | appengine.googleapis.com/http/server/response\_latencies |
| gae\_app/default\_metrics | Количество ответов по типу | Count | appengine.googleapis.com/http/server/response\_style\_count |
| gae\_app/default\_metrics | Утилизация Memcache | Count | appengine.googleapis.com/memcache/centi\_mcu\_count |
| gae\_app/default\_metrics | Коэффициент попаданий | Count | appengine.googleapis.com/memcache/hit\_ratio |
| gae\_app/default\_metrics | Операции Memcache | Count | appengine.googleapis.com/memcache/operation\_count |
| gae\_app/default\_metrics | Получено байт Memcache | Byte | appengine.googleapis.com/memcache/received\_bytes\_count |
| gae\_app/default\_metrics | Отправлено байт Memcache | Byte | appengine.googleapis.com/memcache/sent\_bytes\_count |
| gae\_app/default\_metrics | Используемый размер кэша | Byte | appengine.googleapis.com/memcache/used\_cache\_size |
| gae\_app/default\_metrics | Оценочное количество оплачиваемых экземпляров | Count | appengine.googleapis.com/system/billed\_instance\_estimate\_count |
| gae\_app/default\_metrics | Мегациклы CPU | Count | appengine.googleapis.com/system/cpu/usage |
| gae\_app/default\_metrics | Количество экземпляров | Count | appengine.googleapis.com/system/instance\_count |
| gae\_app/default\_metrics | Использование памяти | Byte | appengine.googleapis.com/system/memory/usage |
| gae\_app/default\_metrics | Полученные байты | Byte | appengine.googleapis.com/system/network/received\_bytes\_count |
| gae\_app/default\_metrics | Отправленные байты | Byte | appengine.googleapis.com/system/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Подключения | Count | appengine.googleapis.com/flex/instance/connections/current |
| gae\_instance/default\_metrics | Утилизация CPU | Percent | appengine.googleapis.com/flex/instance/cpu/utilization |
| gae\_instance/default\_metrics | Получено сетевых байт | Byte | appengine.googleapis.com/flex/instance/network/received\_bytes\_count |
| gae\_instance/default\_metrics | Отправлено сетевых байт | Byte | appengine.googleapis.com/flex/instance/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Средняя длительность Websocket | Second | appengine.googleapis.com/flex/instance/ws/avg\_duration |

## Связанные темы

* Интеграции Google Cloud
