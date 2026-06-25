---
title: Управление расширениями Microsoft SQL Server
source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql
scraped: 2026-05-12T11:10:29.358444
---

# Управление расширениями Microsoft SQL Server

# Управление расширениями Microsoft SQL Server

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 5 сентября 2022 г.

Dynatrace предоставляет платформу для расширения наблюдаемости приложений за счёт данных, получаемых непосредственно с уровня Microsoft SQL Database, что позволяет отслеживать влияние задач сервера баз данных на приложение.

Для начала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=microsoft+sql), соответствует ли предоставляемое Dynatrace расширение Microsoft SQL Server вашим требованиям. Если нет, создайте собственное [расширение Microsoft SQL Server](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions framework.").

## Перед началом работы

Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу Microsoft SQL Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключаться к серверу Microsoft SQL Database.

## Управление расширениями Microsoft SQL

Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных Microsoft SQL Server в среду Dynatrace.

Необходимое разрешение: **Change monitoring settings**

1. В Dynatrace Hub выберите и установите расширение **Microsoft SQL Server**. Это включает расширение в среде.
2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

Определение эндпоинтов](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

Выбор ActiveGates](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

Активация расширения](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")

### Шаг 1. Определение эндпоинтов

1. Нажмите **Add Sql Server endpoint**, чтобы определить серверы, с которых нужно получать данные. Можно определить до 100 эндпоинтов. Укажите следующие сведения для подключения:

   * Хост
   * Порт (необязательно)
   * Имя экземпляра (необязательно)
   * Имя базы данных (необязательно)
   * Схема аутентификации. Доступны следующие [схемы аутентификации](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Расширения Microsoft SQL в платформе Extensions framework."):

     + Базовая аутентификация
     + Аутентификация Kerberos
     + Аутентификация NTLM
   * Для установки защищённого соединения в конфигурации можно [включить SSL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Расширения Microsoft SQL в платформе Extensions framework.").
   * Для более безопасного хранения учётных данных пользователя и управления ими можно [использовать хранилище учётных данных](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Расширения Microsoft SQL в платформе Extensions framework.").
2. Нажмите **Next step**.

### Шаг 2. Выбор ActiveGates

1. Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение.
2. Нажмите **Next step**.

### Шаг 3. Активация расширения

1. Укажите отличительную метку конфигурации мониторинга в поле **Description**.
2. Нажмите **Activate**.

## Конфигурация мониторинга в формате JSON

Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").

## Связанные разделы

* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")