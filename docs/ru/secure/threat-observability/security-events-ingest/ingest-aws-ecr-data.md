---
title: Ingest Amazon ECR container vulnerability findings and scan events
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data
scraped: 2026-03-06T21:24:02.533373
---

# Приём данных об уязвимостях контейнеров Amazon ECR и событиях сканирования

# Приём данных об уязвимостях контейнеров Amazon ECR и событиях сканирования

* Latest Dynatrace
* How-to guide
* Updated on Aug 25, 2025

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, см. в [руководстве по миграции таблицы безопасности Grail](/docs/secure/threat-observability/migration "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Принимайте данные об уязвимостях образов контейнеров Amazon ECR и событиях сканирования и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Далее вы узнаете, как принимать данные об уязвимостях контейнеров и событиях сканирования из [AWS Elastic Container Registry (ECR)](https://dt-url.net/mu03pcw) в [Grail](/docs/platform/grail "Информация о том, что и как можно запрашивать в данных Dynatrace.") и анализировать их на платформе Dynatrace, чтобы получить представление об уязвимостях контейнеров Amazon ECR и удобно работать с вашими данными.

### Сценарии использования

С помощью принятых данных вы можете реализовать различные сценарии использования, такие как:

* [Визуализация и анализ результатов безопасности](/docs/secure/use-cases/visualize-and-analyze-security-findings "Визуализация, приоритизация и анализ принятых результатов безопасности.")
* [Автоматизация и оркестрация результатов безопасности](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Регулярная проверка критических результатов безопасности с автоматическим созданием тикетов Jira или оповещений Slack.")

### Требования

* Настройте нужный тип сканирования Amazon ECR. У вас есть два варианта:

  + [Настройка базового сканирования](https://dt-url.net/of23pfi)
  + [Настройка расширенного сканирования](https://dt-url.net/ay03qkl)

  Чтобы определить, какой тип сканирования выбрать, см. [Сканирование образов на наличие уязвимостей программного обеспечения в Amazon ECR](https://dt-url.net/8043q1w).
* Установите и настройте [последнюю версию AWS CLI](https://dt-url.net/uf03pcx).
* Выберите регион AWS, в котором вы хотите создать средство пересылки событий Amazon ECR.

  Покажите как

  1. В терминале выполните:

  ```
  aws configure
  ```

  2. Установите регион по умолчанию (например, `us-east-1`).
* **Разрешения**:

  + Для установки приложения вам нужен пользователь с правами администратора для определения пользовательской политики с [разрешением `app-engine:apps:install`](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#app-engine-apps-install "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."). Подробнее см. в разделе [Доступ к Dynatrace](/docs/manage/identity-access-management/permission-management/default-policies#access "Справочник стандартных политик Dynatrace").
  + Для запроса принятых данных: `storage:security.events:read`.
* **Токены**:

  + Сгенерируйте токен доступа со скоупом `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробнее см. в разделе [Dynatrace API - Токены и аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace откройте [**Hub**](/docs/manage/hub "Информация о Dynatrace Hub.").
2. Найдите **Amazon ECR** и выберите **Install**.
3. Выберите **Set up**, затем выберите **Configure new connection**.
4. Следуйте инструкциям на экране для настройки приёма данных.

## Подробности

### Как это работает

![how it works](https://dt-cdn.net/images/2025-01-15-09-03-31-1407-d2655c29b6.png)

1. Уязвимости образов контейнеров принимаются в Dynatrace

Уязвимости образов контейнеров, обнаруженные в Amazon ECR, принимаются в Dynatrace через выделенную конечную точку приёма событий безопасности [OpenPipeline](/docs/platform/openpipeline "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline."), используя пересылку событий [Amazon EventBridge](https://dt-url.net/qi03wtk), настроенную с помощью [шаблона AWS CloudFormation](https://dt-url.net/e603poa).

2. Результаты обнаружения уязвимостей обрабатываются и сохраняются в Grail

Конечная точка приёма OpenPipeline обрабатывает и сопоставляет результаты безопасности в соответствии с [соглашениями Semantic Dictionary](https://dt-url.net/3q03pb0).

Они сохраняются в бакете с именем `default_securityevents` (подробнее см.: [Встроенные бакеты Grail](/docs/platform/grail/organize-data#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

### Мониторинг данных

После приёма данных Amazon ECR в Grail вы можете мониторить свои данные в приложении (в Dynatrace перейдите в **Settings**, затем найдите и выберите **Amazon ECR**).

![amazon ecr](https://dt-cdn.net/images/2025-03-25-12-20-07-1920-c3fb043a87.png)

Вы можете просматривать:

* График принятых данных от всех существующих подключений с течением времени

  + Доступные действия: [Запрос принятых данных](#query)
* Таблицу с информацией о ваших подключениях

  + Доступные действия: [Удаление подключения](#remove)

### Визуализация и анализ результатов

Вы можете создавать собственные [дашборды](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") или использовать наши шаблоны для визуализации и анализа результатов обнаружения уязвимостей контейнеров.

Чтобы использовать шаблон дашборда

1. В **Settings** откройте **Amazon ECR**.
2. В разделе **Try our templates** выберите нужный шаблон дашборда.

### Автоматизация и оркестрация результатов

Вы можете создавать собственные [рабочие процессы](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows -- реагируйте на события, планируйте задачи и подключайте сервисы.") или использовать наши шаблоны для автоматизации и оркестрации результатов обнаружения уязвимостей контейнеров.

Чтобы использовать шаблон рабочего процесса

1. В **Settings** откройте **Amazon ECR**.
2. В разделе **Try our templates** выберите нужный шаблон рабочего процесса.

### Запрос принятых данных

Вы можете запрашивать принятые данные в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь выводами из ваших данных наблюдаемости -- в едином совместном настраиваемом рабочем пространстве.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе улик, включая разрешение инцидентов, анализ первопричин и поиск угроз."), используя формат данных из [Semantic Dictionary](https://dt-url.net/3q03pb0).

Чтобы запросить принятые данные

1. В **Settings** откройте **Amazon ECR**.
2. Выберите **Open with**.
3. Выберите **Investigations** или **Notebooks**.

### Удаление подключений

Чтобы прекратить отправку событий в Dynatrace

1. В **Settings** откройте **Amazon ECR**.
2. Для подключения, которое вы хотите удалить, выберите **Delete**.
3. Следуйте инструкциям на экране для удаления ресурсов. Если вы использовали значения, отличные от указанных в диалоговом окне настройки, скорректируйте их соответственно.

Это удалит ресурсы Dynatrace, созданные для данной интеграции.

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [Events powered by Grail](/docs/license/capabilities/events "Узнайте, как рассчитывается потребление Dynatrace Events powered by Grail в рамках модели подписки Dynatrace Platform Subscription.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Ознакомьтесь в Dynatrace Hub

Приём данных об уязвимостях Amazon Elastic Container Registry и событиях сканирования.](https://www.dynatrace.com/hub/detail/aws-ecr)

## Связанные темы

* [OpenPipeline](/docs/platform/openpipeline "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [События безопасности](/docs/semantic-dictionary/model/security-events "Ознакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.")
