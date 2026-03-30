---
title: Управление расширениями PostgreSQL
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/postgresql
scraped: 2026-03-04T21:32:21.031267
---

* Latest Dynatrace
* How-to guide
* 2-min read

Dynatrace предоставляет фреймворк, позволяющий расширить наблюдаемость вашего приложения за счёт данных, получаемых непосредственно со слоя сервера базы данных PostgreSQL, чтобы вы могли отслеживать влияние задач сервера базы данных на ваше приложение.

Начните с проверки [Dynatrace Hub](https://www.dynatrace.com/hub/?query=postgresql), чтобы убедиться, что предоставляемое Dynatrace расширение PostgreSQL Database Server удовлетворяет вашим требованиям.

## Прежде чем начать

Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу базы данных PostgreSQL для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключиться к серверу базы данных PostgreSQL.

## Управление расширениями PostgreSQL

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Теперь для управления расширениями можно использовать специальное приложение Extensions. Оно предоставляет аналогичный процесс активации и настройки, что и Dynatrace Hub в предыдущей версии Dynatrace. Кроме того, оно даёт прямой доступ к мониторингу работоспособности расширений.

* Для использования приложения:

  + В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") выберите и установите приложение.
  + В описании в Hub содержится информация о разрешениях, необходимых для использования приложения (вкладка **Technical information**).

Dynatrace Hub предоставляет унифицированный процесс для включения расширений и управления ими, обеспечивающих приём данных PostgreSQL Server в вашу среду Dynatrace.

Необходимое разрешение: **Change monitoring settings**

1. В Dynatrace Hub выберите и установите расширение **PostgresDB (remote monitoring)**. Это включает расширение в вашей среде мониторинга.
2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Определение конечных точек**](postgresql.md#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Выбор ActiveGate**](postgresql.md#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Активация расширения**](postgresql.md#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from PostgreSQL Database server.")

### Шаг 1. Определение конечных точек

1. Выберите **Add PostgreSQL endpoint**, чтобы определить серверы, с которых нужно получать данные. Можно определить до 20 000 конечных точек. Укажите следующие сведения о подключении:

* Host
* Port
* Database name
* Authentication credentials

  + Поддерживается только базовая аутентификация.
  + Данные аутентификации, переданные в Dynatrace при активации конфигурации мониторинга, скрываются, и их невозможно восстановить.
  + Для более безопасного хранения учётных данных и управления ими можно [использовать хранилище учётных данных](../../../develop-your-extensions/data-sources/sql/postgresql-monitoring.md#authentication "PostgreSQL extensions in the Extensions framework.").
* Выберите **Next step**.

### Шаг 2. Выбор ActiveGate

1. Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение.
2. Выберите **Next step**.

### Шаг 3. Активация расширения

1. Укажите окончательные сведения о конфигурации:

* **Description**
  Текст с пояснением деталей данной конкретной конфигурации мониторинга. При устранении неполадок мониторинга это может предоставить вашим командам важную информацию.
* **Feature sets**
  В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. Их можно использовать для ограничения мониторинга определёнными сегментами. Наборы функций предопределены для каждого расширения.
* Выберите **Activate**.

## Конфигурация мониторинга в формате JSON

Мастер активации расширения содержит динамически обновляемую полезную нагрузку JSON с вашей конфигурацией мониторинга. Чтобы узнать, как использовать её для активации расширения через Dynatrace API, см. Manage Extensions.

## Связанные темы

* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")
