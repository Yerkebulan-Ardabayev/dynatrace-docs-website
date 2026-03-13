---
title: Create log metric
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric
scraped: 2026-03-06T21:23:16.645715
---

# Создание метрики журнала

# Создание метрики журнала

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Apr 24, 2023

Dynatrace Log Management and Analytics даёт возможность не только просматривать и анализировать журналы, но и создавать метрики на основе данных журналов и использовать их в Dynatrace так же, как любые другие метрики. Вы можете добавлять их на панели управления, включать в анализ и даже создавать пользовательские оповещения.

## Создание метрики отказанных подключений

Вам необходимо подсчитать количество отказанных подключений, зафиксированных в данных журналов. Для этого отфильтруйте нужные журналы и преобразуйте количество вхождений в метрику журнала. Отслеживая метрику, вы можете отслеживать возможные проблемы с межсетевым экраном, сетевым подключением или конфигурацией сервера.

### Построение DQL-запроса

Для построения и запуска запроса:

1. Перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. На странице **Logs and events** включите **Advanced mode**.
3. Нажмите ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **copy** для приведённого ниже примера кода.

   ```
   fetch logs



   | filter matchesPhrase(content, "Connection refused")



   | sort timestamp desc
   ```
4. Вставьте запрос в поле редактирования запроса и нажмите **Run query**.

Этот запрос выполняет следующие действия:

* Извлекает журналы с фразой `Connection refused`, найденной в содержимом журнала.
* Сортирует результат в порядке убывания по временной метке.

### Создание метрики

1. Перейдите в **Settings** > **Log Monitoring** > **Metrics extraction** и нажмите **Add log metric**.
2. В поле **Key** добавьте имя метрики к ключу метрики `log.`: `log.conn_refused_count`.
3. Добавьте **Matcher**.
   Используйте [функцию DQL](../lma-classic-log-processing/lma-log-processing-matcher.md#lp-dql-matchesPhrase "Ознакомьтесь с конкретными функциями DQL и логическими операторами для обработки журналов.") для сопоставления фраз, которая является частью [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesPhrase(content, "Connection refused")
   ```

   Это фильтрует данные журналов, содержащие фразу `Connection refused`.
4. Для параметра **Metric measurement** выберите **Occurrence of log records**.
   Метрика представляет количество вхождений записей журнала, содержащих фразу `Connection refused`.
5. Нажмите **Save changes** для создания метрики журнала.

### Просмотр метрики

Просмотр результата в Data Explorer

1. Перейдите в **Data Explorer**.
2. Выберите ключ журнала `log.conn_refused_count`.
3. Нажмите **Run query**.

## Создание метрики атрибута журнала

Вам необходимо отслеживать атрибут ваших журналов и следить за уровнями ошибок, сообщаемыми в журналах из вашего кластера K8s. Найдите нужные журналы из Grail и используйте фильтры для создания новой метрики. Добавьте статус журнала (error/warning/info) к вашей метрике, что упростит отслеживание с помощью метрик.

### Построение DQL-запроса

Для построения и запуска запроса

1. Перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. На странице **Logs and events** включите **Advanced mode**.
3. Нажмите ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy** для приведённого ниже примера кода.

   ```
   fetch logs



   | filter matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")



   | summarize count(), by:status
   ```
4. Вставьте запрос в поле редактирования запроса и нажмите **Run query**.

Этот запрос выполняет следующие действия:

* Извлекает записи журнала с атрибутом `dt.entity.kubernetes_cluster`, содержащим фразу `KUBERNETES_CLUSTER-92233333` в содержимом журнала.
* Подсчитывает количество таких записей журнала и упорядочивает их по атрибуту статуса.

### Создание метрики

1. Перейдите в **Settings** > **Log Monitoring** > **Metrics extraction** и нажмите **Add log metric**.
2. В поле **Key** добавьте имя метрики к ключу метрики `log.`: `K8-92233333`.
3. Добавьте **Matcher**.
   Используйте [функцию DQL](../lma-classic-log-processing/lma-log-processing-matcher.md#lp-dql-matchesPhrase "Ознакомьтесь с конкретными функциями DQL и логическими операторами для обработки журналов.") для сопоставления фраз, которая является частью [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")
   ```
4. Для параметра **Metric measurement** выберите **Occurrence of log records**.
   Метрика представляет количество вхождений записей журнала, содержащих фразу `KUBERNETES_CLUSTER-92233333`.
5. Добавьте измерение `status`.
6. Нажмите **Save changes** для создания метрики журнала.

### Просмотр метрики

Просмотр результата в Data Explorer

1. Перейдите в **Data Explorer**.
2. Выберите ключ журнала `log.K8-92233333` и в разделе **Split by** добавьте `status`.
3. Нажмите **Run query**.
