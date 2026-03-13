---
title: Extend event observability
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-events
scraped: 2026-03-03T21:32:40.794084
---

# Расширение наблюдаемости событий

# Расширение наблюдаемости событий

* Последняя версия Dynatrace
* Чтение: 3 мин
* Опубликовано 4 апр. 2024

Dynatrace предоставляет специализированный REST API для загрузки и управления пользовательскими событиями. API доступен в двух основных точках:

* ActiveGate — для загрузки событий и запросов существующих событий
* OneAgent — только для загрузки событий

Полная документация по API доступна в разделе [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Узнайте, что можно сделать с помощью Dynatrace Events API v2.").

## Управление событиями через ActiveGate

Dynatrace поддерживает следующие конечные точки API для запросов и загрузки пользовательских событий:

| Тип ActiveGate | Базовый URL |
| --- | --- |
| Dynatrace SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/events` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events` |
| Контейнеризированный Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/events` |

1

Environment ActiveGate по умолчанию прослушивает порт `9999`. Если вы изменили этот порт, скорректируйте порт в URL соответствующим образом.

Обязательно укажите ваш [идентификатор среды](../../discover-dynatrace/get-started/monitoring-environment.md "Изучите и узнайте, как работать со средами мониторинга.") в правильном месте URL.

### Аутентификация

Аутентификация осуществляется с помощью токена доступа к API и HTTP-заголовка [`Authorization`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Authorization).

```
Authorization: Api-Token dt.....
```

Для получения токена доступа в Dynatrace перейдите в **Access Tokens**. В зависимости от того, хотите ли вы выполнять запросы или загружать события, вашему токену необходимы области `events.read` или `events.ingest` соответственно. Вы также можете комбинировать области.

Для получения дополнительной информации о токенах доступа см. [Dynatrace API — Токены и аутентификация](../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

### Сетевые требования

* **Незаблокированные сетевые порты**

  Убедитесь, что TCP-порты, используемые ActiveGate (443 или 9999), не заблокированы брандмауэром или любым другим решением для управления сетью.
* **Актуальное хранилище SSL-сертификатов**

  Чтобы избежать проблем с SSL-сертификатами из-за просроченных или отсутствующих корневых сертификатов, убедитесь, что хранилище сертификатов вашей системы актуально.

### Примеры команд curl

Полный список примеров ActiveGate для различных типов запросов см. в [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Узнайте, что можно сделать с помощью Dynatrace Events API v2.").

## Отправка событий в OneAgent

Помимо ActiveGate, OneAgent также предоставляет специализированную конечную точку HTTP (не HTTPS) для локальной загрузки событий. Применяются следующие ограничения:

* Это локальная конечная точка, доступная исключительно по адресу 127.0.0.1 (localhost)
* Поддерживается только загрузка событий (запрос `POST`)

Поддержка сжатия контента

OneAgent пока не поддерживает сжатие контента с использованием HTTP-заголовка Content-Encoding. Если вам необходимо использовать сжатие контента, выполняйте экспорт через ActiveGate.

Для отправки событий в OneAgent сначала необходимо включить Extension Execution Controller (EEC). Это можно сделать глобально для всей среды, для групп хостов или только для конкретных хостов.

Включение на уровне среды

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включение для группы хостов

1. Перейдите в ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** отключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group**, а затем выберите группу хостов, которую вы хотите настроить, из раскрывающегося списка.

   Список хостов теперь отфильтрован по выбранной группе хостов. У каждого хоста в списке есть ссылка **Host group:** `<group name>`, где `<group name>` — название группы хостов, которую вы хотите настроить.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни к одной группе хостов.
4. Выберите название группы хостов в любой строке.

   Поскольку вы выполнили фильтрацию по группе хостов, все отображаемые хосты относятся к одной группе.

5. В настройках группы хостов выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

Включение для отдельного хоста

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Найдите и выберите ваш хост, чтобы отобразить страницу обзора хоста.
3. В верхнем правом углу страницы обзора хоста выберите **More** (**…**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

После включения EEC установки OneAgent на соответствующих хостах начнут принимать запросы по URL `http://localhost:14499/v2/events/ingest`.

OneAgent по умолчанию использует TCP-порт 14499 для этой конечной точки. Вы можете изменить порт с помощью [`oneagentctl`](extend-metrics/ingestion-methods/oneagent-metric-api.md#communication-port "Используйте Dynatrace API для получения метрик отслеживаемых сущностей.").

EEC недоступен в контейнерных развёртываниях

Конечная точка загрузки EEC доступна только при развёртываниях Full-Stack и Infrastructure Monitoring. Она недоступна в контейнерных конфигурациях. Используйте ActiveGate в качестве конечной точки экспорта для контейнерных приложений.

### Аутентификация

Будучи локальной конечной точкой, OneAgent не требует аутентификации.

### Сетевые требования

* **Незаблокированные сетевые порты**

  Поскольку это локальная конечная точка, особой сетевой конфигурации не требуется, за исключением случаев, когда вы ограничили локальную сетевую связь. В этом случае убедитесь, что такие ограничения не распространяются на используемый TCP-порт (по умолчанию 14499).

### Пример команды curl

Следующая команда curl отправляет запрос `POST` на локальную конечную точку OneAgent по пути `/v2/events/ingest`, указывает тип контента JSON и предоставляет [данные события в формате JSON](../../dynatrace-api/environment-api/events-v2/post-event.md#request-body-objects "Загрузка события через Dynatrace API.") с помощью параметра `--data`.

```
curl --request POST --url http://localhost:14499/v2/events/ingest --header "Content-type: application/json" --data "{ \"eventType\": \"AVAILABILITY_EVENT\", \"title\": \"Demo title\" }"
```

## Связанные темы

* [Events API v2](../../dynatrace-api/environment-api/events-v2.md "Узнайте, что можно сделать с помощью Dynatrace Events API v2.")
