---
title: Мониторинг Azure Cache for Redis
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis
scraped: 2026-03-06T21:35:52.648519
---

Для получения информации о различиях между классическими сервисами и другими сервисами см. Миграция с классических (ранее «встроенных») сервисов Azure на облачные сервисы.

Dynatrace получает метрики из Azure Metrics API для Azure Cache for Redis. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

Этот сервис мониторит часть Azure Cache for Redis (`Microsoft.Cache/redis`).

Пока этот сервис настроен, вы **не можете** включить сервис Azure Redis Cache (встроенный).

Сервис Enterprise Azure Cache for Redis (`Microsoft.Cache/redisEnterprise`) в настоящее время не может быть отслежен; для запроса этого типа мониторинга, пожалуйста, создайте RFE (Request for Enhancement).

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Технологии и процессы (классический вид)**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр, чтобы просмотреть **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если у сервиса есть предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса, содержащий все рекомендуемые метрики, на странице **Дашборды**. Вы можете искать конкретные дашборды, фильтруя по **Предустановленные**, а затем по **Имя**.

Для существующих отслеживаемых сервисов вам может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Настройки** > **Облако и виртуализация** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Сохранить**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**…**) и выберите **Клонировать**.
Чтобы удалить дашборд из списка дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**…**) и выберите **Скрыть**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендуемая |
| --- | --- | --- | --- | --- |
| Connected clients | Количество клиентских подключений к кешу. | Shard ID | Count | Применимо |
| Total operations | Общее количество команд, обработанных сервером кеша. | Shard ID | Count | Применимо |
| Cache hits | Количество успешных поисков ключей. | Shard ID | Count | Применимо |
| Cache misses | Количество неуспешных поисков ключей. | Shard ID | Count | Применимо |
| Cache miss rate | Процент запросов get, которые не нашли данные. | Shard ID | Percent | Применимо |
| Gets | Количество операций get из кеша. | Shard ID | Count |  |
| Sets | Количество операций set в кеше. | Shard ID | Count |  |
| Operations per second | Количество мгновенных операций в секунду, выполняемых в кеше. | Shard ID | Count |  |
| Evicted keys | Количество элементов, вытесненных из кеша. | Shard ID | Count |  |
| Total keys | Общее количество элементов в кеше. | Shard ID | Count |  |
| Expired keys | Количество элементов с истёкшим сроком действия в кеше. | Shard ID | Count |  |
| Used memory | Объём памяти кеша, используемой для пар ключ/значение, в МБ. | Shard ID | Byte |  |
| Used memory percentage | Процент памяти кеша, используемой для пар ключ/значение. | Shard ID | Percent | Применимо |
| Used memory RSS | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. | Shard ID | Byte |  |
| Server load | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. | Shard ID | Percent |  |
| Cache write | Объём данных, записываемых в кеш, в байтах в секунду. | Shard ID | BytePerSecond |  |
| Cache read | Объём данных, считываемых из кеша, в байтах в секунду. | Shard ID | BytePerSecond |  |
| Connections created per second (instance based) | Количество мгновенных подключений, создаваемых в секунду через порт 6379 или 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connections closed per second (instance based) | Количество мгновенных подключений, закрываемых в секунду через порт 6379 или 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connected clients (instance based) | Количество клиентских подключений к кешу. | Shard ID, Port, Primary | Count |  |
| Total operations (instance based) | Общее количество команд, обработанных сервером кеша. | Shard ID, Port, Primary | Count |  |
| Cache hits (instance based) | Количество успешных поисков ключей. | Shard ID, Port, Primary | Count |  |
| Cache misses (instance based) | Количество неуспешных поисков ключей. | Shard ID, Port, Primary | Count |  |
| Gets (instance based) | Количество операций get из кеша. | Shard ID, Port, Primary | Count |  |
| Sets (instance based) | Количество операций set в кеше. | Shard ID, Port, Primary | Count |  |
| Operations per second (instance based) | Количество мгновенных операций в секунду, выполняемых в кеше. | Shard ID, Port, Primary | Count |  |
| Evicted keys (instance based) | Количество элементов, вытесненных из кеша. | Shard ID, Port, Primary | Count |  |
| Total keys (instance based) | Общее количество элементов в кеше. | Shard ID, Port, Primary | Count |  |
| Expired keys (instance based) | Количество элементов с истёкшим сроком действия в кеше. | Shard ID, Port, Primary | Count |  |
| Used memory (instance based) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. | Shard ID, Port, Primary | Byte |  |
| Used memory percentage (instance based) | Процент памяти кеша, используемой для пар ключ/значение. | Shard ID, Port, Primary | Percent |  |
| Used memory RSS (instance based) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. | Shard ID, Port, Primary | Byte |  |
| Server load (instance based) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. | Shard ID, Port, Primary | Percent |  |
| Cache write (instance based) | Объём данных, записываемых в кеш, в байтах в секунду. | Shard ID, Port, Primary | BytePerSecond |  |
| Cache read (instance based) | Объём данных, считываемых из кеша, в байтах в секунду. | Shard ID, Port, Primary | BytePerSecond |  |
| CPU (instance based) | Использование CPU сервером Azure Redis Cache в процентах. | Shard ID, Port, Primary | Percent |  |
| CPU | Использование CPU сервером Azure Redis Cache в процентах. | Shard ID | Percent | Применимо |
| Cache latency microseconds (preview) | Задержка обращения к кешу в микросекундах. | Shard ID | Count |  |
| Errors | Количество ошибок, произошедших в кеше. | Shard ID, Error type | Count |  |
| Connected clients (shard 0) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 0) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 0) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 0) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 0) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 0) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 0) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 0) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 0) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 0) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 0) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 0) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 0) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 0) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 0) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 0) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 1) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 1) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 1) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 1) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 1) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 1) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 1) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 1) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 1) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 1) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 1) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 1) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 1) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 1) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 1) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 1) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 2) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 2) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 2) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 2) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 2) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 2) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 2) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 2) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 2) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 2) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 2) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 2) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 2) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 2) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 2) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 2) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 3) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 3) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 3) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 3) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 3) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 3) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 3) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 3) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 3) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 3) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 3) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 3) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 3) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 3) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 3) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 3) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 4) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 4) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 4) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 4) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 4) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 4) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 4) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 4) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 4) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 4) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 4) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 4) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 4) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 4) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 4) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 4) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 5) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 5) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 5) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 5) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 5) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 5) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 5) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 5) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 5) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 5) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 5) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 5) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 5) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 5) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 5) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 5) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 6) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 6) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 6) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 6) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 6) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 6) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 6) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 6) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 6) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 6) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 6) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 6) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 6) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 6) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 6) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 6) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 7) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 7) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 7) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 7) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 7) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 7) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 7) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 7) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 7) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 7) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 7) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 7) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 7) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 7) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 7) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 7) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 8) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 8) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 8) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 8) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 8) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 8) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 8) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 8) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 8) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 8) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 8) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 8) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 8) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 8) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 8) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 8) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Connected clients (shard 9) | Количество клиентских подключений к кешу. |  | Count |  |
| Total operations (shard 9) | Общее количество команд, обработанных сервером кеша. |  | Count |  |
| Cache hits (shard 9) | Количество успешных поисков ключей. |  | Count |  |
| Cache misses (shard 9) | Количество неуспешных поисков ключей. |  | Count |  |
| Gets (shard 9) | Количество операций get из кеша. |  | Count |  |
| Sets (shard 9) | Количество операций set в кеше. |  | Count |  |
| Operations per second (shard 9) | Количество мгновенных операций в секунду, выполняемых в кеше. |  | Count |  |
| Evicted keys (shard 9) | Количество элементов, вытесненных из кеша. |  | Count |  |
| Total keys (shard 9) | Общее количество элементов в кеше. |  | Count |  |
| Expired keys (shard 9) | Количество элементов с истёкшим сроком действия в кеше. |  | Count |  |
| Used memory (shard 9) | Объём памяти кеша, используемой для пар ключ/значение, в МБ. |  | Byte |  |
| Used memory RSS (shard 9) | Объём используемой памяти кеша в МБ, включая фрагментацию и метаданные. |  | Byte |  |
| Server load (shard 9) | Процент циклов, в которых сервер Redis занят обработкой и не ожидает в режиме простоя. |  | Percent |  |
| Cache write (shard 9) | Объём данных, записываемых в кеш, в байтах в секунду. |  | BytePerSecond |  |
| Cache read (shard 9) | Объём данных, считываемых из кеша, в байтах в секунду. |  | BytePerSecond |  |
| CPU (shard 9) | Использование CPU сервером Azure Redis Cache в процентах. |  | Percent |  |
| Geo - replication healthy | Состояние работоспособности канала гео-репликации. 1 — исправен, 0 — отключён или неисправен. | Shard ID | Count |  |
| Geo - replication data sync offset | Приблизительный объём данных в байтах, которые необходимо синхронизировать с гео-вторичным кешем. | Shard ID | Byte |  |
| Geo - replication connectivity lag | Время в секундах с момента последней успешной синхронизации данных с гео-первичным кешем. Значение продолжает увеличиваться, если канал связи отключён. | Shard ID | Second |  |
| Geo - replication full sync event started | Срабатывает при инициации события полной синхронизации между гео-реплицированными кешами. Эта метрика в основном показывает 0, поскольку гео-репликация использует частичную ресинхронизацию для любых новых данных, добавленных после начальной полной синхронизации. | Shard ID | Count |  |
| Geo - replication full sync event finished | Срабатывает при завершении события полной синхронизации между гео-реплицированными кешами. Эта метрика в основном показывает 0, поскольку гео-репликация использует частичную ресинхронизацию для любых новых данных, добавленных после начальной полной синхронизации. | Shard ID | Count |  |