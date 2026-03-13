---
title: Ingest Amazon GuardDuty security findings
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty
scraped: 2026-03-06T21:24:07.806532
---

# Загрузка результатов безопасности Amazon GuardDuty

# Загрузка результатов безопасности Amazon GuardDuty

* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 25 августа 2025 г.

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, см. в [руководстве по миграции таблицы безопасности Grail](/docs/secure/threat-observability/migration "Узнайте об изменениях в новой таблице безопасности Grail и о том, как выполнить миграцию.").

Загружайте результаты безопасности Amazon GuardDuty и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Интеграция Dynatrace с [Amazon GuardDuty](https://dt-url.net/2h03zvk) позволяет вам унифицировать и контекстуализировать результаты безопасности из различных инструментов и продуктов, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию.

GuardDuty обнаруживает подозрительную активность в ваших учётных записях AWS, рабочих нагрузках и данных. Платформа Dynatrace наблюдает за сущностями времени выполнения, связанными с этими ресурсами AWS. Загрузка результатов обнаружения из GuardDuty помогает анализировать их в контексте производственных приложений.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии, такие как

* [Визуализация и анализ результатов безопасности](/docs/secure/use-cases/visualize-and-analyze-security-findings "Визуализация, приоритизация и анализ загруженных результатов безопасности.")
* [Автоматизация и оркестрация результатов безопасности](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Регулярная проверка критических результатов безопасности и автоматическое создание заявок Jira или оповещений Slack.")

### Требования

Ниже приведены требования для [Amazon GuardDuty](#aws) и [Dynatrace](#dt).

#### Требования Amazon GuardDuty

* Установите и настройте [последнюю версию AWS CLI](https://dt-url.net/uf03pcx).
* Выберите регион AWS, в котором вы хотите создать перенаправление событий.

  Показать как

  1. В терминале выполните:

     ```
     aws configure
     ```
  2. Установите регион по умолчанию (например, `us-east-1`).

#### Требования Dynatrace

* Разрешения:

  + Для запроса загруженных данных: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью `openpipeline.events_security` и сохраните его. Подробности см. в [Dynatrace API - Токены и аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace откройте [**Hub**](/docs/manage/hub "Информация о Dynatrace Hub.").
2. Найдите **Amazon GuardDuty** и нажмите **Install**.
3. Нажмите **Set up**, затем выберите **Configure new connection**.
4. Следуйте инструкциям на экране для настройки загрузки.

## Подробности

### Как это работает

![guardduty](https://dt-cdn.net/images/image-20250327-102449-2454-96b81169b5.png)

1. События загружаются в Dynatrace

1. События Amazon GuardDuty отправляются в [Amazon EventBridge](https://dt-url.net/qi03wtk), который запускает функцию AWS Lambda.
2. Функция Lambda предварительно обрабатывает события и отправляет их в Dynatrace через выделенную конечную точку загрузки безопасности [OpenPipeline](/docs/platform/openpipeline "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.").

2. Результаты безопасности обрабатываются и сохраняются в Grail

1. Конечная точка загрузки OpenPipeline обрабатывает и сопоставляет данные в соответствии с [соглашениями Semantic Dictionary](https://dt-url.net/3q03pb0).
2. Данные сохраняются в бакете `default_securityevents` (подробности см. в [Встроенные бакеты Grail](/docs/platform/grail/organize-data#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

### Мониторинг данных

После загрузки данных Amazon GuardDuty в Grail вы можете отслеживать свои данные в приложении (в Dynatrace перейдите в **Settings**, затем найдите и выберите **Amazon GuardDuty**).

![guardduty](https://dt-cdn.net/images/2025-05-27-09-26-29-1431-96bb80a495.png)

Вы можете просматривать

* График загруженных данных со всех существующих подключений во времени

  + Доступные действия: [Запрос загруженных данных](#query)
* Таблицу с информацией о ваших подключениях

  + Доступные действия: [Удаление подключения](#remove)

### Визуализация и анализ результатов

Вы можете создавать собственные [дашборды](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") или использовать наши шаблоны для визуализации и анализа результатов уязвимостей контейнеров.

1. В **Settings** откройте **Amazon GuardDuty**.
2. В разделе **Try our templates** выберите нужный шаблон дашборда.

### Автоматизация и оркестрация результатов

Вы можете создавать собственные [рабочие процессы](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows -- реагируйте на события, планируйте задачи и подключайте сервисы.") или использовать наши шаблоны для автоматизации и оркестрации результатов уязвимостей контейнеров.

1. В **Settings** откройте **Amazon GuardDuty**.
2. В разделе **Try our templates** выберите нужный шаблон рабочего процесса.

### Запрос загруженных данных

Вы можете запрашивать загруженные данные в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости -- всё в одном совместном настраиваемом рабочем пространстве.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Сочетайте функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз."), используя формат данных из [Semantic Dictionary](https://dt-url.net/3q03pb0).

1. В **Settings** откройте **Amazon GuardDuty**.
2. Нажмите **Open with**.
3. Выберите **Investigations** или **Notebooks**.

### Оценка, сортировка и расследование результатов обнаружения

Вы можете оценивать, сортировать и расследовать результаты обнаружения с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Изучайте, сортируйте и расследуйте результаты обнаружения и оповещения.").

1. Откройте ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Отфильтруйте по **Provider** > **Amazon GuardDuty**.

### Удаление подключений

Чтобы прекратить отправку событий в Dynatrace

1. В **Settings** откройте **Amazon GuardDuty**.
2. Для подключения, которое вы хотите удалить, нажмите **Delete**.
3. Следуйте инструкциям на экране для удаления ресурсов. Если вы использовали значения, отличные от указанных в диалоге настройки, скорректируйте их соответствующим образом.

Это удалит ресурсы Dynatrace, созданные для данной интеграции.

### Лицензирование и стоимость

Информацию о биллинге см. в [События на базе Grail](/docs/license/capabilities/events "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в модели подписки Dynatrace Platform.").

## Часто задаваемые вопросы

### Какая модель данных используется для журналов безопасности и событий, поступающих из Amazon GuardDuty?

[События обнаружения](/docs/secure/threat-observability/concepts#detection "Основные концепции, связанные с наблюдаемостью угроз") хранят отдельные результаты обнаружения для каждого затронутого объекта, представленного ресурсом AWS.

### Какие дополнительные поля добавляются к событиям, загружаемым из Amazon GuardDuty?

Пространство имён `aws` добавляется для хранения информации, связанной с AWS, со следующими полями:

* `aws.account.id`
* `aws.region`
* `aws.availability_zone`
* `aws.resource.type`
* `aws.resource.name`

### Какие типы ресурсов Amazon GuardDuty поддерживаются Dynatrace для контекстуализации времени выполнения?

`CONTAINER`: Все результаты обнаружения с контейнером в качестве целевого ресурса классифицируются как `CONTAINER` в `object.type`, и пространство имён контейнера добавляется с соответствующими полями:

* `container.id`
* `container.name`
* `container.image.name`
* `container.image.version`

### Как нормализуется оценка риска для результатов Amazon GuardDuty?

Dynatrace нормализует уровни серьёзности и оценки риска для всех результатов, загруженных через текущую интеграцию. Это помогает вам приоритизировать результаты последовательно, независимо от их источника.
Подробности о том, как работает нормализация, см. в [Нормализация серьёзности и оценки](/docs/secure/threat-observability/concepts#normalization "Основные концепции, связанные с наблюдаемостью угроз").

* `dt.security.risk.level` сопоставляется на основе уровня серьёзности, определённого Amazon GuardDuty путём сопоставления оценки серьёзности (`detail.severity`).
* `dt.security.risk.score` сопоставляется напрямую из оценки серьёзности (`detail.severity`), установленной Amazon GuardDuty.

| `dt.security.risk.level` (сопоставляется из `finding.severity`) | `dt.security.risk.score` (сопоставляется из `finding.score`) |
| --- | --- |
| CRITICAL -> CRITICAL | 9.0-10.0 |
| HIGH -> HIGH | 7.00-8.9 |
| MEDIUM -> MEDIUM | 4.0-6.9 |
| LOW -> LOW | 1.0-3.9 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Загрузка результатов обнаружения Amazon GuardDuty.](https://www.dynatrace.com/hub/detail/amazon-guardduty)

## Связанные темы

* [OpenPipeline](/docs/platform/openpipeline "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [События безопасности](/docs/semantic-dictionary/model/security-events "Познакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.")
