---
title: Отправка метрик Telegraf в Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf
scraped: 2026-03-06T21:16:32.145427
---

* Актуальная версия Dynatrace

[Telegraf](https://github.com/influxdata/telegraf) — это плагин-ориентированный серверный агент для сбора, обработки, агрегации и записи метрик. Telegraf поставляется с плагином вывода Dynatrace Output Plugin, который позволяет легко отправлять метрики Telegraf в Dynatrace.

## Включение приёма метрик Telegraf

Приём метрик Telegraf доступен начиная с OneAgent версии 1.201+. Самый простой сценарий конфигурации — установить Telegraf и OneAgent на одном хосте. В этом случае вам нужно только включить Dynatrace Output Plugin в конфигурации Telegraf (Telegraf версии 1.16+) и включить приём метрик Telegraf на уровне среды или хоста в конфигурации Dynatrace. Обратите внимание, что конфигурация на уровне хоста переопределяет конфигурацию на уровне среды.

Включение Dynatrace Output Plugin в конфигурации Telegraf

### Telegraf и OneAgent на одном хосте

1. Отредактируйте `telegraf.conf` — [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.16/administration/configuration/).
2. Раскомментируйте строку `[[outputs.dynatrace]]`.
3. Необязательно Раскомментируйте строку `prefix = "telegraf."` и установите префикс для удобного поиска метрик, принятых через Telegraf. Префикс также будет отображаться в ключе метрики Dynatrace.
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

Если вы не можете установить OneAgent на хосте, мониторируемом Telegraf, вы можете настроить Dynatrace Output Plugin для отправки метрик напрямую в вашу среду Dynatrace через Metrics API v2.

#### Предварительные требования

* API-токен с областью действия **Ingest metrics data points**.
* Ваш идентификатор среды.

1. Отредактируйте `telegraf.conf` — [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Раскомментируйте строку `# [[outputs.dynatrace]]`.
3. Необязательно Раскомментируйте строку `# prefix = "telegraf."` и установите префикс для удобного поиска метрик, принятых через Telegraf. Префикс также будет отображаться в ключе метрики Dynatrace.
4. Раскомментируйте строку `# api_token = ""` и добавьте ваш API-токен, например `api_token = "abcdefjhij1234567890"`
5. Раскомментируйте строку `# url = ""` и добавьте конечную точку Dynatrace для метрик. Например,

   * Dynatrace SaaS `url = "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"`
   * Dynatrace Managed `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest`
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

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите ваш хост для отображения страницы обзора хоста.
3. В правом верхнем углу страницы обзора хоста нажмите **More** (**...**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

Включение для группы хостов

1. Перейдите в ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, затем выберите группу хостов, которую хотите настроить, из выпадающего списка.

   Список хостов теперь отфильтрован по выбранной группе хостов. Каждый перечисленный хост имеет ссылку **Host group:** `<group name>`, где `<group name>` — имя группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни к одной группе хостов.
4. Нажмите на имя группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

## Осведомлённость о топологии

Когда OneAgent и Telegraf установлены на одном хосте, идентификатор хоста и имя хоста автоматически добавляются к каждой метрике в качестве измерений. Узнайте, как обогатить ваши метрики другими специфичными для Dynatrace измерениями и применить детали причинно-следственного анализа Dynatrace-AI к принятым данным.

## Формат метрик

Предоставленные точки данных должны соответствовать протоколу приёма метрик.

## Порт связи

Плагин Telegraf Dynatrace Output Plugin отправляет метрики на конечную точку OneAgent metric API.

Порт приёма метрик по умолчанию — `14499`. При необходимости вы можете использовать команду oneagentctl для проверки или изменения порта. Изменение порта приёма метрик требует перезапуска OneAgent. Добавьте `--restart-service` к команде для автоматического перезапуска OneAgent.

### Проверка порта приёма

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта приёма (по умолчанию `14499`).

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

Настройте прокси вашего хоста для разрешения трафика localhost, идущего на порт приёма метрик (по умолчанию `14499`).

Если вы изменяете порт связи OneAgent по умолчанию, убедитесь, что вы также обновили конфигурацию Telegraf.

1. Отредактируйте `telegraf.conf` — [файл конфигурации Telegraf](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Установите свойство `url` в значение `url = "http://127.0.0.1:<your-custom-port>/metrics/ingest"`.
3. Сохраните файл.

Обратите внимание, что изменение порта для метрик, принятых через Telegraf, также влияет на OneAgent REST API и интеграцию со скриптами.
