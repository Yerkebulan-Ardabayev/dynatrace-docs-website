---
title: API приёма журналов OneAgent
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api
scraped: 2026-03-05T21:32:31.516583
---

# API загрузки логов OneAgent

# API загрузки логов OneAgent

* Latest Dynatrace
* 2-min read
* Updated on Jul 01, 2025

Вы можете использовать локальную конечную точку API `http://localhost:<port>/v2/logs/ingest` для отправки локально полученных логов в Dynatrace по безопасному и аутентифицированному каналу. Эта конечная точка доступна только для локальных клиентов и недоступна с удалённых хостов.

Конечная точка загрузки логов OneAgent повторяет поведение публичной конечной точки [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.").

## Включение API загрузки логов

Вам необходимо включить API загрузки логов OneAgent на уровне среды или хоста. Обратите внимание, что конфигурация на уровне хоста переопределяет конфигурацию среды.

Включение на уровне среды

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для отдельного хоста

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите ваш хост для отображения страницы обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

Включение для группы хостов

1. Перейдите в ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, а затем выберите группу хостов, которую хотите настроить, из выпадающего списка.

   Список хостов теперь отфильтрован по выбранной группе хостов. У каждого хоста в списке есть ссылка **Host group:** `<имя группы>`, где `<имя группы>` — это название группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни к одной группе хостов.
4. Выберите название группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты принадлежат к одной группе хостов.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

## Формат событий лога

Запрос принимает полезную нагрузку `application/json` с набором символов `charset=utf-8`. Для получения дополнительной информации о формате см. [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.").

## Ограничения

События логов, отправляемые в Dynatrace с использованием API загрузки логов OneAgent, подчиняются тем же ограничениям, что и для публичного [Log Monitoring API v2 - POST ingest logs](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md#request-body-objects "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.").

## Пример

С помощью этой команды `curl` вы загрузите событие `Exception: Custom error log sent via OneAgent log ingest` с уровнем серьёзности `error` и пользовательским атрибутом со значением `attribute value`. Поскольку временная метка не указана, событие автоматически получает временную метку времени чтения события. Вы сможете получить доступ к событию в [Log viewer (Logs Classic)](../../../analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer.md "Узнайте, как использовать средство просмотра логов Dynatrace для анализа данных логов.").

```
curl -i -X POST "http://127.0.0.1:14499/v2/logs/ingest" -H "Content-Type: application/json; charset=utf-8" -d "{\"content\":\"Exception: Custom error log sent via Generic Log Ingest\",\"custom.attribute\":\"attribute value\",\"severity\": \"error\"}"
```

Успешный ответ возвращает код `204`.

```
HTTP/1.1 204 No Content



Content-Type: application/json



Server: EEC



Content-Length: 116
```

## Порт связи

Начиная с версии OneAgent 1.267+, системы AIX также поддерживают загрузку метрик.

Порт загрузки метрик по умолчанию — `14499`. При необходимости вы можете использовать команду [oneagentctl](../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#metrics "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.") для проверки или изменения порта. Изменение порта загрузки метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#oneagent-restart "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.") к команде для автоматического перезапуска OneAgent.

### Проверка порта загрузки

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта загрузки, по умолчанию `14499`.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Установка пользовательского порта загрузки

Используйте параметр `--set-extensions-ingest-port=<arg>` для установки пользовательского локального порта загрузки.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Настройка прокси

Настройте прокси вашего хоста, чтобы разрешить трафик localhost, направляемый на порт загрузки метрик, по умолчанию `14499`.

Обратите внимание, что изменение порта для API загрузки логов OneAgent также влияет на [OneAgent metric API](../extend-metrics/ingestion-methods/oneagent-metric-api.md "Используйте Dynatrace API для получения метрик отслеживаемых объектов."), [Metric scripting integration](../extend-metrics/ingestion-methods/oneagent-pipe.md "Узнайте, как загружать метрики с помощью локальной интеграции скриптов.") и [Telegraf metrics integration](../extend-metrics/ingestion-methods/telegraf.md "Загружайте метрики Telegraf в Dynatrace.").