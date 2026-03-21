---
title: API метрик OneAgent
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api
scraped: 2026-03-06T21:16:38.345678
---

* Latest Dynatrace

Вы можете использовать локальную конечную точку API `http://localhost:<port>/metrics/ingest` для отправки локально полученных метрик в Dynatrace через защищённый и аутентифицированный канал. Эта конечная точка доступна только для локальных клиентов и не может быть достигнута с удалённых хостов.

Если вы не можете отправлять метрики через локальную конечную точку API, вы также можете использовать публичную конечную точку [Metric API v2](#api).

## Включение API метрик OneAgent

ActiveGate версии 1.243+

OneAgent версии 1.243+

API метрик OneAgent поставляется с OneAgent версии 1.201 по умолчанию. Вам нужно только включить API метрик OneAgent на уровне среды или хоста. Обратите внимание, что конфигурация на уровне хоста переопределяет конфигурацию среды.

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

   Список хостов теперь отфильтрован по выбранной группе хостов. У каждого хоста в списке есть ссылка **Host group:** `<имя группы>`, где `<имя группы>` -- это имя группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни к одной группе хостов.
4. Выберите имя группы хостов в любой строке.

   Поскольку вы отфильтровали по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

Если вы хотите изменить лимиты потребления ресурсов EEC, см. [Профиль производительности](../../../extensions/concepts.md#performance-profile "Learn more about the concept of Dynatrace Extensions.").

## Осведомлённость о топологии

При использовании локальной конечной точки API идентификатор хоста и контекст имени хоста автоматически добавляются к каждой метрике в качестве измерений. Узнайте, как [обогатить ваши метрики другими специфическими для Dynatrace измерениями](../../extend-data.md "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") и применять детали причинно-следственного анализа Dynatrace-AI к загруженным данным.

## Формат метрик

Предоставляемые точки данных должны соответствовать [протоколу загрузки метрик](../reference/metric-ingestion-protocol.md "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Запрос принимает полезную нагрузку `text/plain` с набором символов `charset=utf-8`. Полезная нагрузка ограничена `1 000` строками.

## Пример

С помощью этой команды `curl` вы загрузите метрику `cpu.temperature`, привязанную к измерению `cpu=1`. Метрика будет автоматически привязана к соответствующему идентификатору хоста и имени хоста.

```
curl --data "cpu.temperature,cpu=1 55" http://localhost:14499/metrics/ingest \


-H "Content-Type: text/plain; charset=utf-8"
```

Успешный ответ:

```
{


"error": null,


"linesValid": 1,


"linesInvalid": 0


}
```

## Порт связи

Начиная с OneAgent версии 1.267+, системы AIX также поддерживают загрузку метрик.

Порт загрузки метрик по умолчанию -- `14499`. При необходимости вы можете использовать команду [oneagentctl](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для проверки или изменения порта. Изменение порта загрузки метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](../../../dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") к команде для автоматического перезапуска OneAgent.

### Проверка порта загрузки

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта загрузки (по умолчанию `14499`).

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

Настройте прокси вашего хоста, чтобы разрешить трафик localhost к порту загрузки метрик (по умолчанию `14499`).

Обратите внимание, что изменение порта для API метрик OneAgent также влияет на интеграцию со скриптами и Telegraf.

## Metrics API v2

В отличие от локального интерфейса загрузки, который добавляет контекст топологии автоматически (каждая метрика привязывается к соответствующему хосту), метрики, отправленные через публичный [Metrics API](../../../../dynatrace-api/environment-api/metric-v2.md "Retrieve metric information via Metrics v2 API.") v2, по умолчанию не привязаны к топологии. Это особенно полезно для бизнес-метрик, которые не имеют связи с сущностями топологии в вашей среде.

Однако, чтобы генерировать события для выбранного хоста и позволить Dynatrace Intelligence выполнять причинно-следственный анализ на основе ваших метрик, вы можете настроить ваше приложение для добавления измерения `dt.entity.host`. Для автоматического обогащения идентификатором группы процессов укажите измерение `dt.process.pid`. Для получения дополнительной информации см. [Metrics API - POST ingest data points](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.").

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
