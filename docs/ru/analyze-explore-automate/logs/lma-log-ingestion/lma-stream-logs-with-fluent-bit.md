---
title: Stream logs to Dynatrace with Fluent Bit
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit
scraped: 2026-03-06T21:36:44.146131
---

# Потоковая передача журналов в Dynatrace с помощью Fluent Bit

# Потоковая передача журналов в Dynatrace с помощью Fluent Bit

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jan 22, 2026

Вы можете отправлять журналы в Dynatrace с помощью Fluent Bit. Настройте Fluent Bit для отправки журналов в универсальный API приёма данных Dynatrace.

## Возможности

* Fluent Bit — это многоплатформенный процессор и пересыльщик журналов, который позволяет собирать данные/журналы из различных источников, унифицировать их и отправлять в несколько назначений. Он совместим со средами Docker и Kubernetes.
* Dynatrace можно настроить в качестве целевой среды управления журналами и аналитики для ваших данных благодаря настраиваемому параметру Fluent Bit `http output`.
* Вы можете использовать любой из входных плагинов Fluent Bit для получения журналов и событий из вашего приложения в Dynatrace.

## Конфигурация

Плагин Fluent Bit `http output` позволяет передавать журналы в конечную точку универсального приёма журналов Dynatrace.

1. Получите [токен API Dynatrace](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования API Dynatrace.") с областью `logs.ingest` (Ingest Logs).
2. [Разверните Fluent Bit](https://dt-url.net/zd034je).
3. Для отправки журналов в конечную точку [универсального приёма журналов](../../log-monitoring/acquire-log-data/logs-classic-ingestion-api.md "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения такого приёма.") Dynatrace настройте [плагин http output](https://dt-url.net/0z034x4) через файл конфигурации.
4. В основном файле конфигурации Fluent Bit добавьте раздел Output со следующими параметрами:

```
[OUTPUT]



name  http



match *



header Content-Type application/json; charset=utf-8



header Authorization Api-Token {your-API-token-here}



allow_duplicated_headers false



host  {your-environment-id}.live.dynatrace.com



Port  443



URI   /api/v2/logs/ingest



Format json



json_date_format iso8601



json_date_key timestamp



tls On



tls.verify On
```

Вы можете разместить токен API в заголовке или в качестве переменной `GET` в URI (см. пример ниже).

* Для Dynatrace SaaS конечная точка [универсального приёма журналов](../../log-monitoring/acquire-log-data/logs-classic-ingestion-api.md "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения такого приёма.") доступна в вашей среде.
* Если [Environment ActiveGate](../../../ingest-from/dynatrace-activegate.md#agtypes "Понимание основных понятий, связанных с ActiveGate.") является вашим выбором для конечной точки в локальной среде, установите экземпляр ActiveGate.

  В Dynatrace Hub выберите **ActiveGate** > **Set up**.
* Универсальный API приёма журналов v2 автоматически включается на ActiveGate.

## Пример: приём журналов ECS Fargate с помощью Fluent Bit

Fluent Bit является рекомендуемым решением, когда критически важно снизить потребление ресурсов.
В примере ниже описывается, как можно настроить приём журналов AWS Fargate с помощью Fluent Bit.

При создании нового определения задачи с помощью консоли управления AWS раздел интеграции FireLens упрощает добавление контейнера маршрутизатора журналов. Следуйте приведённым ниже шагам для настройки приёма журналов:

1. В консоли управления AWS перейдите в раздел интеграции Firelens.

![Final log integration page in AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Выберите встроенный образ Fluent Bit.

3. Отредактируйте контейнер, в котором выполняются ваши приложения, генерирующие журналы.

4. В разделе **Storage and Logging** выберите **awsfirelens** в качестве драйвера журналов.

![Set AWS Firelens as a log driver](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

Параметры драйвера журналов должны указывать на API приёма журналов вашего SaaS-клиента. Для Fluent Bit необходимо предоставить два заголовка: тип контента и токен авторизации. Поскольку FireLens поддерживает только один заголовок, вы можете передать тип контента как часть URL. Ваша конфигурация для AWS FireLens должна содержать определённые пары ключ-значение, как показано в блоке кода ниже.

```
Name: http



TLS: on



Format: json



Header: Authorization Api-Token {your-API-token-here}



Host: {your-environment-id}.live.dynatrace.com



Port: 443



URI: /api/v2/logs/ingest?Content-Type=application/json



Allow_Duplicated_Headers": "false"



Json_Date_Format": "iso8601"



Json_Date_Key": "timestamp"
```

Чтобы избежать публикации токена в открытом виде, следуйте шагам в [AWS Secrets Manager](https://dt-url.net/r5234z4).
После того как ваше приложение начнёт публиковать журналы, вы сможете просматривать их в пользовательском интерфейсе Dynatrace.

Обратитесь к [примерному репозиторию AWS](https://dt-url.net/3j0348v) для получения JSON-файла определения задачи с конфигурацией Dynatrace.

Дополнительные сведения о конфигурации см. в [Руководстве разработчика Amazon ECS](https://dt-url.net/cf4349a).

## Устранение неполадок

Посетите Dynatrace Community для получения руководств по устранению неполадок, а также ознакомьтесь с разделом [Устранение неполадок Log Management and Analytics](../lma-troubleshooting.md "Устранение проблем, связанных с настройкой и конфигурацией Log Management and Analytics.").

* [Устранение неполадок с журналами, принятыми через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
