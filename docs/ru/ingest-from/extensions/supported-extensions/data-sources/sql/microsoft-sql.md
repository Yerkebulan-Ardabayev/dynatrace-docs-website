---
title: Manage Microsoft SQL Server extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql
scraped: 2026-03-06T21:16:10.453218
---

# Управление расширениями Microsoft SQL Server

# Управление расширениями Microsoft SQL Server

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 05, 2022

Dynatrace предоставляет фреймворк, который позволяет расширить наблюдаемость вашего приложения до данных, получаемых непосредственно с уровня Microsoft SQL Database, чтобы вы могли отслеживать влияние задач сервера баз данных на ваше приложение.

Начните с проверки [Dynatrace Hub](https://www.dynatrace.com/hub/?query=microsoft+sql), чтобы убедиться, что расширение Microsoft SQL Server, предоставляемое Dynatrace, удовлетворяет вашим требованиям. Если вам нужно что-то другое, вы можете создать собственное [расширение Microsoft SQL Server](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Узнайте, как создать расширение на основе источника данных SQL с помощью фреймворка Extensions.").

## Перед началом работы

Назначьте одну или несколько групп ActiveGate, которые будут удалённо подключаться к вашему серверу Microsoft SQL Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключиться к вашему серверу Microsoft SQL Database.

## Управление расширениями Microsoft SQL

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Менеджер расширений

Latest Dynatrace

Теперь для управления расширениями можно использовать специальное приложение Extensions. Оно предоставляет аналогичный рабочий процесс активации и настройки, что и Dynatrace Hub в предыдущей версии Dynatrace. Кроме того, оно даёт прямой доступ к мониторингу работоспособности расширений.

* Чтобы воспользоваться приложением:

  + В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") выберите и установите приложение.
  + В листинге Hub содержится информация о разрешениях, необходимых для работы с приложением (вкладка **Техническая информация**).

Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими, обеспечивающих загрузку данных Microsoft SQL Server в вашу среду Dynatrace.

Необходимое разрешение: **Change monitoring settings**

1. В Dynatrace Hub выберите и установите расширение **Microsoft SQL Server**. Это включит расширение в вашей среде.
2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Определите конечные точки](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, получаемых от Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Выберите ActiveGates](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, получаемых от Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Активируйте расширение](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, получаемых от Microsoft SQL Server.")

### Шаг 1. Определение конечных точек

1. Выберите **Add Sql Server endpoint**, чтобы определить серверы, с которых требуется получать данные. Можно задать до 100 конечных точек. Укажите следующие данные подключения:

   * Хост
   * Необязательный порт
   * Необязательное имя экземпляра
   * Необязательное имя базы данных
   * Схема аутентификации. Можно выбрать одну из следующих [схем аутентификации](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Расширения Microsoft SQL в фреймворке Extensions."):

     + Базовая аутентификация
     + Аутентификация Kerberos
     + Аутентификация NTLM
   * Вы можете [включить SSL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Расширения Microsoft SQL в фреймворке Extensions."), чтобы установить защищённое соединение для вашей конфигурации.
   * Вы можете [использовать хранилище учётных данных](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Расширения Microsoft SQL в фреймворке Extensions.") для более безопасного хранения и управления учётными данными пользователей.
2. Выберите **Next step**.

### Шаг 2. Выбор ActiveGates

1. Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение.
2. Выберите **Next step**.

### Шаг 3. Активация расширения

1. Задайте отличительную метку для вашей конфигурации мониторинга в поле **Description**.
2. Выберите **Activate**.

## Конфигурация мониторинга в формате JSON

Мастер активации расширений содержит динамически обновляемую JSON-нагрузку с вашей конфигурацией мониторинга. Чтобы узнать, как использовать её для активации расширения через Dynatrace API, см. раздел [Управление расширениями](/docs/ingest-from/extensions/manage-extensions "Узнайте, как управлять расширениями.").

## Связанные темы

* [Устранение неполадок с расширениями](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")
