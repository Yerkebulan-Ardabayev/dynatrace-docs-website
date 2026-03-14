---
title: Отправка метрик Telegraf в Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf
scraped: 2026-02-06T16:28:34.508791
---

# Отправка метрик Telegraf в Dynatrace


* Latest Dynatrace
* Чтение: 2 мин.
* Опубликовано 15 октября 2020 г.

[Telegraf](https://github.com/influxdata/telegraf) — это серверный агент на основе плагинов для сбора, обработки, агрегации и записи метрик. Telegraf поставляется с плагином Dynatrace Output Plugin, который позволяет легко отправлять метрики Telegraf в Dynatrace.

## Включение приёма метрик Telegraf

Приём метрик Telegraf доступен начиная с OneAgent версии 1.201+. Самый простой сценарий настройки — установить Telegraf и OneAgent на одном хосте. В этом случае вам нужно только включить Dynatrace Output Plugin в конфигурации Telegraf (Telegraf версии 1.16+) и включить приём метрик Telegraf на уровне среды или хоста в настройках Dynatrace. Обратите внимание, что настройка на уровне хоста переопределяет настройку на уровне среды.

Включите Dynatrace Output Plugin в конфигурации Telegraf

### Telegraf и OneAgent на одном хосте

1. Отредактируйте `telegraf.conf`, [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.16/administration/configuration/).
2. Раскомментируйте строку `[[outputs.dynatrace]]`.
3. Необязательно: раскомментируйте строку `prefix = "telegraf."` и задайте префикс для удобного поиска метрик, принятых через Telegraf. Префикс также будет отображаться в ключе метрики Dynatrace.
4. Сохраните файл.

```
# # Send telegraf metrics to a Dynatrace environment


[[outputs.dynatrace]]


#   ## For usage with the Dynatrace OneAgent you can omit any configuration,


#   ## the only requirement is that the OneAgent is running on the same host.


#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.


#   ##


#   ## Your Dynatrace environment URL.


#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)


#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"


#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"


#   url = ""


#


#   ## Your Dynatrace API token.


#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API


#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.


#   api_token = ""


#


#   ## Optional prefix for metric names (e.g.: "telegraf.")


prefix = "telegraf."


#


#   ## Optional TLS Config


#   # tls_ca = "/etc/telegraf/ca.pem"


#   # tls_cert = "/etc/telegraf/cert.pem"


#   # tls_key = "/etc/telegraf/key.pem"


#


#   ## Optional flag for ignoring tls certificate check


#   # insecure_skip_verify = false


#


#


#   ## Connection timeout, defaults to "5s" if not set.


#   timeout = "5s"
```

### Без OneAgent на хосте

Если вы не можете установить OneAgent на хосте, мониторинг которого осуществляется Telegraf, вы можете настроить Dynatrace Output Plugin для отправки метрик напрямую в вашу среду Dynatrace через [Metrics API v2](../../../../dynatrace-api/environment-api/metric-v2.md "Получение информации о метриках через Metrics v2 API.").

#### Предварительные требования

* [Токен API](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") с областью действия **Ingest metrics data points**.
* Ваш [идентификатор среды](../../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.").

1. Отредактируйте `telegraf.conf`, [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Раскомментируйте строку `# [[outputs.dynatrace]]`.
3. Необязательно: раскомментируйте строку `# prefix = "telegraf."` и задайте префикс для удобного поиска метрик, принятых через Telegraf. Префикс также будет отображаться в ключе метрики Dynatrace.
4. Раскомментируйте строку `# api_token = ""` и добавьте ваш токен API, например `api_token = "abcdefjhij1234567890"`.
5. Раскомментируйте строку `# url = ""` и добавьте конечную точку API метрик Dynatrace. Например:

   * Dynatrace SaaS: `url = "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"`
   * Dynatrace Managed: `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest`
6. Сохраните файл.

```
# # Send telegraf metrics to a Dynatrace environment


[[outputs.dynatrace]]


#   ## For usage with the Dynatrace OneAgent you can omit any configuration,


#   ## the only requirement is that the OneAgent is running on the same host.


#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.


#   ##


#   ## Your Dynatrace environment URL.


#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)


#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"


#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"


#   url = "https://abd12345.live.dynatrace.com/api/v2/metrics/ingest"


#


#   ## Your Dynatrace API token.


#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API


#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.


api_token = "abcdefjhij1234567890"


#


#   ## Optional prefix for metric names (e.g.: "telegraf.")


prefix = "telegraf."


#


#   ## Optional TLS Config


#   # tls_ca = "/etc/telegraf/ca.pem"


#   # tls_cert = "/etc/telegraf/cert.pem"


#   # tls_key = "/etc/telegraf/key.pem"


#


#   ## Optional flag for ignoring tls certificate check


#   # insecure_skip_verify = false


#


#


#   ## Connection timeout, defaults to "5s" if not set.


#   timeout = "5s"
```

Включение на уровне среды

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для отдельного хоста

1. Перейдите в **Hosts** (предыдущий Dynatrace) или ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите ваш хост, чтобы отобразить страницу обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

Включение для группы хостов

1. Перейдите в ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, а затем выберите группу хостов, которую вы хотите настроить, из выпадающего списка.

   Список хостов теперь отфильтрован по выбранной группе хостов. Каждый перечисленный хост имеет ссылку **Host group:** `<group name>`, где `<group name>` — имя группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни одной группе хостов.
4. Выберите имя группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты принадлежат к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

## Осведомлённость о топологии

Когда OneAgent и Telegraf установлены на одном хосте, идентификатор хоста и имя хоста автоматически добавляются к каждой метрике в качестве измерений. Узнайте, как [обогатить ваши метрики дополнительными измерениями, специфичными для Dynatrace](../../extend-data.md "Узнайте, как автоматически обогащать телеметрические данные измерениями, специфичными для Dynatrace."), и применить детали причинно-следственного анализа Dynatrace AI к вашим принятым данным.

## Формат метрик

Предоставляемые точки данных должны соответствовать [протоколу приёма метрик](../reference/metric-ingestion-protocol.md "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

## Порт связи

Плагин Telegraf Dynatrace Output Plugin отправляет метрики на конечную точку [OneAgent metric API](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Приём пользовательских метрик в Dynatrace через Metrics v2 API.").

Порт приёма метрик по умолчанию — `14499`. При необходимости вы можете использовать команду [oneagentctl](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#metrics "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") для проверки или изменения порта. Изменение порта приёма метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#oneagent-restart "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") к команде для автоматического перезапуска OneAgent.

### Проверка порта приёма

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта приёма, по умолчанию `14499`.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Установка пользовательского порта приёма

Используйте параметр `--set-extensions-ingest-port=<arg>` для установки пользовательского локального порта приёма.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Настройка прокси

Настройте прокси вашего хоста, чтобы разрешить трафик localhost на порт приёма метрик, по умолчанию `14499`.

Если вы изменили порт связи OneAgent по умолчанию, убедитесь, что вы также обновили конфигурацию Telegraf.

1. Отредактируйте `telegraf.conf`, [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Установите свойство `url` в значение `url = "http://127.0.0.1:<your-custom-port>/metrics/ingest"`.
3. Сохраните файл.

Обратите внимание, что изменение порта для метрик, принятых через Telegraf, также влияет на OneAgent REST API и интеграцию со скриптами.