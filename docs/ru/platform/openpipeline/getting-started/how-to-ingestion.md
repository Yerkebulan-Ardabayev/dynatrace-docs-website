---
title: Как принимать данные (события)
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/how-to-ingestion
scraped: 2026-03-06T21:15:55.878660
---

В этом руководстве показано, как принять событие в Grail через эндпоинт `platform/ingest/v1/events` и проверить, что оно сохранено.

Событие, которое мы будем принимать:

```
{


"name": "My first ingested event"


}
```

## Для кого это руководство

Эта статья предназначена для команд разработчиков, управляющих приёмом данных.

## Перед началом работы

Предварительные требования

* Среда Dynatrace на основе Grail и AppEngine.
* Лицензия Dynatrace — модели лицензирования для всех возможностей Dynatrace."), включающая обзор Events на основе Grail (DPS).

## Шаги

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Аутентификация**](how-to-ingestion.md#authenticate "Как принимать данные для области конфигурации в OpenPipeline.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Скопировать путь эндпоинта**](how-to-ingestion.md#path "Как принимать данные для области конфигурации в OpenPipeline.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Отправить событие**](how-to-ingestion.md#send "Как принимать данные для области конфигурации в OpenPipeline.")[![Шаг 4, необязательный](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4, необязательный")

**Проверить приём**](how-to-ingestion.md#verify "Как принимать данные для области конфигурации в OpenPipeline.")

### Шаг 1. Аутентификация

Эндпоинт `platform/ingest/v1/events` использует аутентификацию по токену доступа. Для генерации токена доступа:

1. Перейдите в раздел **Access Tokens**.
2. Выберите **Generate new token** (Создать новый токен).
3. Введите имя токена.
4. Найдите и выберите область **OpenPipeline — Ingest Events** (`openpipeline.events`).
5. Нажмите **Generate token** (Создать токен).
6. Нажмите **Copy** (Копировать), затем сохраните токен в надёжном месте. Это длинная строка, которую потребуется скопировать и вставить обратно в Dynatrace позже.

### Шаг 2. Копирование пути эндпоинта

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Events** > **Ingest sources**.
2. Найдите интересующий вас источник приёма.
3. В столбце **Endpoints path** выберите имя эндпоинта > ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy** (Копировать).

### Шаг 3. Отправка события

Выполните следующую команду-пример, чтобы отправить событие на эндпоинт вашей среды `platform/ingest/v1/events` через запрос `POST`.

Пример команды указывает тип содержимого JSON и передаёт данные события в формате JSON через параметр `-d`. Обязательно замените:

* `<your-endpoint-URL>` — URL скопированного эндпоинта. Он выглядит как `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events`.
* `<your-API-token>` — созданный вами токен.
* `My first ingested event` — именем вашего события.

```
curl -i -X POST "<your-endpoint-URL>" \


-H "Content-Type: application/json" \


-H "Authorization: Api-Token <your-API-token>" \


-d "{\"name\":\"My first ingested event\"}"
```

Запрос успешен, если в выводе содержится код ответа 202, например:

```
HTTP/2 202
```

### Шаг 4 (необязательный). Проверка приёма

Чтобы убедиться, что событие успешно принято, выполните запрос через DQL, например в разделе **Notebooks**.

1. Перейдите в **Notebooks**.
2. Выберите или создайте блокнот.
3. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL**, чтобы добавить новый раздел с полем ввода DQL-запроса.
4. Введите следующий DQL-запрос.

   Обязательно замените `My first ingested event` на имя вашего события.

   ```
   fetch events


   | filter name == "My first ingested event"
   ```

Запрос успешен, если в выводе содержится запись с временной меткой, источником приёма и именем, например:

![Проверка приёма события в Notebooks](https://dt-cdn.net/images/verify-event-ingest-1200-05f1ad9526.webp)

## Узнайте больше

OpenPipeline — это унифицированный компонент приёма данных для Dynatrace Platform. Через API можно принимать различные области конфигурации. Для приёма записей для области конфигурации через API необходимо:

1. Выполнить аутентификацию.
2. Скопировать путь эндпоинта.
3. Отправить запись.
4. Проверить приём.

Обзор доступных эндпоинтов см. в разделе Источники приёма в OpenPipeline.

## Связанные темы

* Поток данных в OpenPipeline
* Источники приёма в OpenPipeline
