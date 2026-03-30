---
title: Передача журналов в Dynatrace с помощью Fluent Bit
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit
scraped: 2026-03-06T21:36:44.146131
---

* Последняя Dynatrace
* Учебник
* 3-минутное чтение

Вы можете отправлять журналы в Dynatrace с помощью Fluent Bit. Настройте Fluent Bit для отправки журналов в общий конечный пункт приема API Dynatrace.

## Возможности

* Fluent Bit — это многофункциональный процессор и передатчик журналов, который позволяет собирать данные/журналы из различных источников, объединять и отправлять их в несколько пунктов назначения. Он совместим с средами Docker и Kubernetes.
* Dynatrace можно настроить в качестве целевой среды управления журналами и аналитики для ваших данных благодаря настраиваемому выходу `http`.
* Вы можете использовать любой из входных плагинов Fluent Bit, чтобы получить журналы и события из вашего приложения в Dynatrace.

## Настройка

Плагин выхода `http` Fluent Bit позволяет передавать ваши журналы в общий конечный пункт приема журналов Dynatrace.

1. Получите токен API Dynatrace с областью `logs.ingest` (Прием журналов).
2. [Разверните Fluent Bit](https://dt-url.net/zd034je).
3. Чтобы отправить журналы в общий конечный пункт приема журналов Dynatrace, настройте [плагин выхода http](https://dt-url.net/0z034x4) через файл конфигурации.
4. В вашем основном файле конфигурации Fluent Bit добавьте раздел выхода с следующими параметрами:

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

* Для Dynatrace SaaS общий конечный пункт приема журналов доступен в вашей среде.
* Если [Environment ActiveGate](../../../ingest-from/dynatrace-activegate.md#agtypes "Поймите основные понятия, связанные с ActiveGate.") является вашим выбором для конечной точки в локальной среде, установите экземпляр ActiveGate.

  В Dynatrace Hub выберите **ActiveGate** > **Настройка**.
* Общий конечный пункт приема журналов API v2 автоматически включен на ActiveGate.

## Пример: Прием журналов ECS Fargate с помощью Fluent Bit

Fluent Bit — это рекомендуемое решение, когда важно уменьшить потребление ресурсов.
Пример ниже описывает, как вы можете настроить прием журналов AWS Fargate с помощью Fluent Bit.

При создании нового определения задачи с помощью консоли управления AWS раздел интеграции FireLens позволяет легко добавить контейнер маршрутизатора журналов. Следуйте шагам ниже, чтобы настроить прием журналов:

1. В консоли управления AWS перейдите в раздел интеграции Firelens.

![Окончательная страница интеграции журналов в консоли управления AWS](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Выберите встроенный образ Fluent Bit.

3. Отредактируйте контейнер, в котором запускаются ваши приложения, генерирующие журналы.

4. В разделе **Хранилище и журналирование** выберите **awsfirelens** в качестве драйвера журналов.

![Установка AWS Firelens в качестве драйвера журналов](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

Настройки драйвера журналов должны указывать на конечную точку приема журналов API вашего арендатора SaaS. Вам необходимо предоставить два заголовка для Fluent Bit: тип содержимого и токен авторизации. Поскольку FireLens поддерживает только один заголовок, вы можете передать тип содержимого как часть URL. Ваша конфигурация для AWS FireLens должна содержать определенные пары ключ-значение, как показано в блоке кода ниже.

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
Как только ваше приложение начнет публиковать журналы, вы можете просмотреть их в интерфейсе Dynatrace.

См. [репозиторий примеров AWS](https://dt-url.net/3j0348v) для определения задачи JSON с конфигурацией Dynatrace.

Для получения дополнительных сведений о конфигурации см. [Руководство разработчика Amazon ECS](https://dt-url.net/cf4349a).

## Устранение неполадок

Посетите сообщество Dynatrace для руководств по устранению неполадок, а также см. Устранение неполадок управления журналами и аналитики.

* [Устранение неполадок журналов, принятых через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)