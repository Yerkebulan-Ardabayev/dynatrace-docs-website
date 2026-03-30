---
title: Передача журналов в Dynatrace с помощью Fluent Bit (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit
scraped: 2026-03-05T21:32:29.846836
---

* Учебник
* 3-минутное чтение

Мониторинг журналов Classic

Для самой новой версии Dynatrace см. Передача журналов в Dynatrace с помощью Fluent Bit.

Вы можете отправлять журналы в Dynatrace с помощью Fluent Bit. Настройте Fluent Bit для отправки журналов в универсальный приемник журналов API.

## Возможности

* Fluent Bit — это многофункциональный процессор и передатчик журналов, который позволяет собирать данные/журналы из различных источников, объединять и отправлять их в несколько мест назначения. Он совместим с окружением Docker и Kubernetes.
* Dynatrace можно настроить в качестве целевой среды управления журналами и аналитики для ваших данных благодаря настраиваемому `http output`.
* Вы можете использовать любой из плагинов ввода Fluent Bit, чтобы получить журналы и события из вашего приложения в Dynatrace.

## Настройка

Плагин `http output` Fluent Bit позволяет передавать ваши журналы в конечную точку приемки журналов Dynatrace.

1. Получите токен Dynatrace API с областью `logs.ingest` (Прием журналов).
2. [Разверните Fluent Bit](https://dt-url.net/zd034je).
3. Чтобы отправить журналы в конечную точку приемки журналов Dynatrace, настройте плагин [http output](https://dt-url.net/0z034x4) через файл конфигурации.
4. В вашем основном файле конфигурации Fluent Bit добавьте раздел вывода с следующими параметрами:

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

Вы можете разместить ваш токен API в заголовке или как переменную `GET` в URI (см. пример ниже).

* Для Dynatrace SaaS конечная точка приемки журналов доступна в вашей среде.

* Если [Environment ActiveGate](../../../ingest-from/dynatrace-activegate.md#agtypes "Поймите основные понятия, связанные с ActiveGate.") является вашим выбором для конечной точки в локальной среде, установите экземпляр ActiveGate.

  В Dynatrace Hub выберите **ActiveGate** > **Настройка**.
* Прием журналов API v2 автоматически включен на ActiveGate.

## Пример

Fluent Bit — это рекомендуемое решение, когда снижение потребления ресурсов имеет решающее значение.
В примере ниже вам необходимо принять журналы AWS Fargate. FireLens позволяет настроить Fluent Bit для этого приема.

### Прием журналов AWS Fargate с помощью Fluent Bit

При создании нового определения задачи с помощью консоли управления AWS раздел интеграции FireLens упрощает добавление контейнера маршрутизатора журналов. Следуйте шагам ниже, чтобы выполнить прием:

1. В консоли управления AWS перейдите в раздел интеграции FireLens.

![Окончательная страница интеграции журналов в консоли управления AWS](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Выберите встроенный образ Fluent Bit.

3. Отредактируйте контейнер, в котором выполняется ваше приложение, генерирующее журналы.

4. В разделе **Хранилище и журналирование** выберите **awsfirelens** в качестве драйвера журнала.

![Установите AWS FireLens в качестве драйвера журнала](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

Настройки драйвера журнала должны указывать на токен приемки журналов вашего арендатора SaaS. Вам необходимо предоставить два заголовка для Fluent Bit: тип содержимого и токен авторизации. Поскольку FireLens поддерживает только один заголовок, вы можете передать токен как часть URL. Ваша конфигурация для AWS FireLens должна иметь следующий вид:

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

Чтобы избежать публикации токена в открытом виде, следуйте инструкциям из [AWS Secrets Manager](https://dt-url.net/r5234z4).
Как только ваше приложение начнет публиковать журналы, вы сможете просмотреть их в интерфейсе Dynatrace.

См. [репозиторий примеров AWS](https://dt-url.net/3j0348v) для определения задачи с конфигурацией Dynatrace.

Для получения дополнительных сведений о конфигурации см. [Руководство по разработке Amazon ECS](https://dt-url.net/cf4349a).

## Устранение неполадок

Посетите сообщество Dynatrace для руководств по устранению неполадок, а также см. Устранение неполадок мониторинга журналов (Logs Classic).

* [Устранение неполадок журналов, принятых через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)