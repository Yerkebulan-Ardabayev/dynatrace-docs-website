---
title: Управление расширениями Oracle Database
source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql
scraped: 2026-05-12T11:10:30.584363
---

# Управление расширениями Oracle Database

# Управление расширениями Oracle Database

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 11 апреля 2022 г.

Dynatrace предоставляет платформу для расширения наблюдаемости приложений за счёт данных, получаемых непосредственно с уровня Oracle Database, что позволяет отслеживать влияние задач сервера баз данных на приложение.

Для начала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=oracle+sql), соответствует ли предоставляемое Dynatrace расширение Oracle Database вашим требованиям. Если нет, создайте собственное [расширение Dynatrace Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions framework.").

## Перед началом работы

1. Определите, какой сервер Oracle Database нужно отслеживать. Расширение Oracle Database поддерживает Oracle Database версии 12.2+ со следующими конфигурациями:

   * Автономные серверы Oracle
   * Oracle Multitenant (CDB/PDB)
   * Oracle RAC
   * Oracle AWS RDS
2. Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу Oracle Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключаться к серверу Oracle Database.
3. Создайте выделенную учётную запись для мониторинга и предоставьте ей разрешения согласно описанию расширения [Oracle Database](https://dt-url.net/7f03qwp) в разделе **Get started with Oracle Database servers**.

## Управление расширениями Oracle SQL

Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных Oracle Database в среду Dynatrace.

Необходимое разрешение: **Change monitoring settings**

1. В Dynatrace Hub выберите и установите расширение **Oracle Database**. (Для фильтрации результатов поиска используйте "Oracle SQL".) Это включает расширение в среде.
2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.

Затем выполните следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Принятие лицензии на распространение драйвера Oracle JDBC**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-1 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Определение эндпоинтов**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-2 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Группа ActiveGate**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-3 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Активация расширения**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-4 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")

### Шаг 1. Принятие лицензии на распространение драйвера Oracle JDBC

Расширение Oracle Database требует принятия [лицензионного соглашения Dynatrace на распространение драйвера Oracle JDBC](https://dt-url.net/0s1n0pw9).

### Шаг 2. Определение эндпоинтов

Нажмите **Add Oracle endpoint**, чтобы определить серверы Oracle Database, с которых нужно получать данные. Можно определить до 100 эндпоинтов. Укажите следующие сведения для подключения:

* Хост
* Порт
* Идентификатор базы данных: **Service Name** или **SID**.
* Учётные данные аутентификации. Поддерживается только базовая аутентификация. Данные аутентификации, передаваемые в Dynatrace при активации конфигурации мониторинга, скрываются и не могут быть получены.

  + Для более безопасного хранения учётных данных пользователя и управления ими можно [использовать хранилище учётных данных](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#credential-vault "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.").

После этого нажмите **Next step**.

### Шаг 3. Группа ActiveGate

Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение. После этого нажмите **Next step**.

### Шаг 4. Активация расширения

Укажите финальные сведения о конфигурации.

* **Description**  
  Текст с описанием данной конфигурации мониторинга. При устранении неполадок он поможет вашей команде получить подробные сведения о конкретной конфигурации.
* **Feature sets**  
  В сильно сегментированных сетях наборы функций могут отражать сегменты среды. Их можно использовать для ограничения мониторинга определёнными сегментами. Наборы функций предопределены для каждого расширения.

После этого нажмите **Activate**.

## Конфигурация мониторинга в формате JSON

Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").

## Связанные разделы

* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")