---
title: Потоковая передача журналов в Dynatrace с помощью Fluent Bit (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit
scraped: 2026-05-12T12:09:43.487287
---

# Потоковая передача журналов в Dynatrace с помощью Fluent Bit (Logs Classic)

# Потоковая передача журналов в Dynatrace с помощью Fluent Bit (Logs Classic)

* Учебное руководство
* Чтение: 3 мин
* Обновлено 22 января 2026 г.

Log Monitoring Classic

Журналы можно отправлять в Dynatrace с помощью Fluent Bit. Настройте Fluent Bit для отправки журналов в универсальный API приёма Dynatrace.

## Возможности

* Fluent Bit — многоплатформенный процессор и отправщик журналов, позволяющий собирать данные/журналы из различных источников, унифицировать их и отправлять в несколько назначений. Совместим со средами Docker и Kubernetes.
* Dynatrace можно настроить как целевую среду управления журналами и аналитики благодаря настраиваемому `http output` Fluent Bit.
* Можно использовать любые входные плагины Fluent Bit для получения журналов и событий из приложения в Dynatrace.

## Конфигурация

Плагин `http output` Fluent Bit позволяет перенаправлять журналы на эндпоинт приёма журналов Dynatrace.

1. Получите [API-токен Dynatrace](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") со скоупом `logs.ingest` (Ingest Logs).
2. [Разверните Fluent Bit](https://dt-url.net/zd034je).
3. Для отправки журналов в эндпоинт [приёма журналов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов и о возможных ограничениях.") Dynatrace настройте [плагин http output](https://dt-url.net/0z034x4) через конфигурационный файл.
4. В основном конфигурационном файле Fluent Bit добавьте раздел Output со следующими параметрами:

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

API-токен можно поместить в заголовок или передать как переменную `GET` в URI (см. пример ниже).

* Если [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate#agtypes "Общие понятия, связанные с ActiveGate.") выбран в качестве эндпоинта в локальной среде или для Dynatrace Managed, установите экземпляр ActiveGate.

  Перейдите в **Deploy Dynatrace**, затем выберите **Install ActiveGate**.
* Log ingestion API v2 автоматически включается на ActiveGate.

## Пример

Fluent Bit является рекомендуемым решением, когда критично снижение потребления ресурсов.
В примере ниже необходимо принять журналы AWS Fargate. FireLens позволяет настроить Fluent Bit для этого приёма.

### Приём журналов AWS Fargate с помощью Fluent Bit

При создании нового определения задачи с помощью AWS Management Console раздел интеграции FireLens упрощает добавление контейнера маршрутизатора журналов. Выполните следующие шаги:

1. В AWS Management Console перейдите в раздел интеграции Firelens.

![Страница финальной интеграции журналов в AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

Страница финальной интеграции журналов в AWS Management Console

2. Выберите встроенный образ Fluent Bit.

3. Отредактируйте контейнер, в котором работает генерирующее журналы приложение.

4. В разделе **Storage and Logging** выберите **awsfirelens** в качестве драйвера журналирования.

![Установка AWS Firelens в качестве драйвера журналирования](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

Установка AWS Firelens в качестве драйвера журналирования

Настройки драйвера журналирования должны указывать на API приёма журналов вашего SaaS-тенанта. Для Fluent Bit нужно предоставить два заголовка: тип содержимого и токен авторизации. Поскольку FireLens поддерживает только один заголовок, токен можно передать как часть URL. Конфигурация для AWS FireLens:

```
Name: http



TLS: on



Format: json



Header: Content-Type application/json; charset=utf-8



Host: {your-environment-id}.live.dynatrace.com



Port: 443



URI: /api/v2/logs/ingest?api-token={your-API-token-here}



Allow_Duplicated_Headers": "false"



Json_Date_Format": "iso8601"



Json_Date_Key": "timestamp"
```

Чтобы избежать публикации токена в открытом виде, следуйте инструкциям [AWS Secrets Manager](https://dt-url.net/r5234z4).
После того как приложение начнёт публиковать журналы, их можно просматривать в UI Dynatrace.

Обратитесь к [AWS sample repository](https://dt-url.net/3j0348v) для ознакомления с JSON определения задачи с конфигурацией Dynatrace.

Дополнительные сведения о конфигурации: [Amazon ECS Developer Guide](https://dt-url.net/cf4349a).

## Устранение неполадок

Посетите сообщество Dynatrace, а также ознакомьтесь с разделом [Устранение неполадок Log Monitoring (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Устраните проблемы, связанные с настройкой и конфигурацией Log Monitoring Classic.").

* [Troubleshooting logs ingested via Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)