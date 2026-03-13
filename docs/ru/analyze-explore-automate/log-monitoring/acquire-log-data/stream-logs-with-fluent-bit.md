---
title: Stream logs to Dynatrace with Fluent Bit (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit
scraped: 2026-03-05T21:32:29.846836
---

# Потоковая передача логов в Dynatrace с помощью Fluent Bit (Logs Classic)

# Потоковая передача логов в Dynatrace с помощью Fluent Bit (Logs Classic)

* Classic
* Руководство
* Чтение: 3 мин.
* Обновлено 22 января 2026 г.

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Потоковая передача логов в Dynatrace с помощью Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Интеграция Fluent Bit для потоковой передачи логов в Dynatrace.").

Вы можете отправлять логи в Dynatrace с помощью Fluent Bit. Настройте Fluent Bit для отправки логов через универсальный API загрузки Dynatrace.

## Возможности

* Fluent Bit — это мультиплатформенный процессор и ретранслятор логов, который позволяет собирать данные/логи из различных источников, унифицировать и отправлять их в несколько назначений. Он совместим со средами Docker и Kubernetes.
* Dynatrace может быть настроен в качестве целевой среды управления и анализа логов для ваших данных благодаря настраиваемому `http output` Fluent Bit.
* Вы можете использовать любые входные плагины Fluent Bit для передачи логов и событий из вашего приложения в Dynatrace.

## Конфигурация

Выходной плагин Fluent Bit `http output` позволяет пересылать ваши логи в конечную точку загрузки логов Dynatrace.

1. Получите [токен API Dynatrace](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования API Dynatrace.") с областью `logs.ingest` (Загрузка логов).
2. [Разверните Fluent Bit](https://dt-url.net/zd034je).
3. Чтобы отправлять логи в конечную точку [загрузки логов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace загружает данные логов и какие возможные ограничения имеет такая загрузка.") Dynatrace, настройте [выходной плагин http](https://dt-url.net/0z034x4) через конфигурационный файл.
4. В вашем основном конфигурационном файле Fluent Bit добавьте раздел Output со следующими параметрами:

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

Вы можете разместить ваш токен API в заголовке или в качестве переменной `GET` в URI (см. пример ниже).

* Для Dynatrace SaaS конечная точка [загрузки логов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace загружает данные логов и какие возможные ограничения имеет такая загрузка.") доступна в вашей среде.

* Если [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate#agtypes "Основные концепции, связанные с ActiveGate.") является вашим выбором конечной точки в локальной среде, установите экземпляр ActiveGate.

  В Dynatrace Hub выберите **ActiveGate** > **Set up**.
* API загрузки логов v2 автоматически включён на ActiveGate.

## Пример

Fluent Bit является рекомендуемым решением, когда критично снижение потребления ресурсов.
В приведённом ниже примере вам необходимо загрузить логи AWS Fargate. FireLens позволяет настроить Fluent Bit для этой загрузки.

### Загрузка логов AWS Fargate с помощью Fluent Bit

При создании нового определения задачи с помощью AWS Management Console раздел интеграции FireLens упрощает добавление контейнера маршрутизатора логов. Выполните следующие шаги для загрузки:

1. В AWS Management Console перейдите в раздел интеграции Firelens.

![Final log integration page in AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Выберите встроенный образ Fluent Bit.

3. Отредактируйте контейнер, в котором работает ваше приложение, генерирующее логи.

4. В разделе **Storage and Logging** выберите **awsfirelens** в качестве драйвера логов.

![Set AWS Firelens as a log driver](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

Настройки драйвера логов должны указывать на API загрузки логов вашего SaaS-тенанта. Вам необходимо предоставить два заголовка для Fluent Bit: тип содержимого и токен авторизации. Поскольку FireLens поддерживает только один заголовок, вы можете передать токен как часть URL. Ваша конфигурация для AWS FireLens должна содержать следующее:

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
После того как ваше приложение начнёт публиковать логи, вы сможете просматривать их в пользовательском интерфейсе Dynatrace.

Обратитесь к [репозиторию примеров AWS](https://dt-url.net/3j0348v) для получения JSON определения задачи с конфигурацией Dynatrace.

Для получения дополнительных сведений о конфигурации см. [Руководство разработчика Amazon ECS](https://dt-url.net/cf4349a).

## Устранение неполадок

Посетите Dynatrace Community для получения руководств по устранению неполадок, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Решение проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.").

* [Устранение неполадок логов, загруженных через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
