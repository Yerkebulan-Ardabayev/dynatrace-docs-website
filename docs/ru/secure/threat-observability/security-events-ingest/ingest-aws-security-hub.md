---
title: Ingest AWS Security Hub security findings
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub
scraped: 2026-03-06T21:23:41.794802
---

# Загрузка результатов безопасности AWS Security Hub

# Загрузка результатов безопасности AWS Security Hub

* Latest Dynatrace
* How-to guide
* Обновлено 25 авг. 2025

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, описан в [руководстве по миграции таблиц безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Загружайте результаты безопасности AWS Security Hub и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Далее вы узнаете, как загрузить результаты безопасности из [AWS Security Hub](https://dt-url.net/wv03w0h) в [Grail](../../../platform/grail.md "Информация о том, что и как можно запрашивать из данных Dynatrace.") и анализировать их на платформе Dynatrace, чтобы получать аналитику Dynatrace для результатов безопасности AWS Security Hub и единообразно визуализировать, анализировать и автоматизировать результаты безопасности на платформе Dynatrace.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии использования, например:

* [Загрузка и обогащение результатов AWS Security Hub с помощью Dynatrace](https://dt-url.net/t703wux)
* [Визуализация и анализ результатов безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Визуализируйте, приоритизируйте и анализируйте загруженные результаты безопасности.")
* [Автоматизация и оркестрация результатов безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Регулярно проверяйте критические результаты безопасности и получайте автоматические тикеты Jira или оповещения Slack.")

### Требования

Ниже приведены требования для [AWS Security Hub](#aws) и [Dynatrace](#dt).

#### Требования AWS Security Hub

* Установите и настройте [последнюю версию AWS CLI](https://dt-url.net/uf03pcx).
* Выберите регион AWS, в котором вы хотите создать средство пересылки событий AWS Security Hub.

  Покажите мне как

  1. В терминале выполните:

     ```
     aws configure
     ```
  2. Установите регион по умолчанию (например, `us-east-1`).

#### Требования Dynatrace

* Разрешения:

  + Вам нужен пользователь с правами администратора, чтобы определить пользовательскую политику с [разрешением `app-engine:apps:install`](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#app-engine-apps-install "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") для установки приложения. Подробнее см. [Доступ к Dynatrace](../../../manage/identity-access-management/permission-management/default-policies.md#access "Справочник политик по умолчанию Dynatrace").
  + Для запросов к загруженным данным: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью действия `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробнее см. [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace откройте [**Hub**](../../../manage/hub.md "Информация о Dynatrace Hub.").
2. Найдите **AWS Security Hub** и выберите **Install**.
3. Выберите **Set up**, затем выберите **Configure new connection**.
4. Следуйте инструкциям на экране для настройки загрузки.

## Подробности

### Как это работает

![как это работает](https://dt-cdn.net/images/2025-01-15-09-02-44-1355-c1a2ad92c9.png)

1. События загружаются в Dynatrace

События результатов безопасности из AWS Security Hub загружаются в Dynatrace через выделенную конечную точку загрузки безопасности [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.") с использованием пересылки событий [Amazon EventBridge](https://dt-url.net/qi03wtk), настроенной с помощью шаблона [AWS CloudFormation](https://dt-url.net/e603poa).

2. Результаты безопасности обрабатываются и сохраняются в Grail

Конечная точка загрузки OpenPipeline обрабатывает и сопоставляет результаты безопасности в соответствии с [соглашениями семантического словаря](https://dt-url.net/3q03pb0).

Они хранятся в корзине (bucket) с именем `default_securityevents` (подробнее см. [Встроенные корзины Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из корзин, таблиц и представлений.")).

### Мониторинг данных

После загрузки данных AWS Security Hub в Grail вы можете отслеживать свои данные в приложении (в Dynatrace перейдите в **Settings**, затем найдите и выберите **AWS Security Hub**).

![security hub](https://dt-cdn.net/images/2025-03-25-11-46-26-1920-ffd9b3b4d1.png)

Вы можете просмотреть

* График загруженных данных из всех существующих подключений с течением времени

  + Доступные действия: [Запрос загруженных данных](#query)
* Таблицу с информацией о ваших подключениях

  + Доступные действия: [Удаление подключения](#remove)

### Визуализация и анализ результатов

Вы можете создавать собственные [дашборды](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") или использовать наши шаблоны для визуализации и анализа результатов уязвимостей контейнеров.

1. В **Settings** откройте **AWS Security Hub**.
2. В разделе **Try our templates** выберите нужный шаблон дашборда.

### Автоматизация и оркестрация результатов

Вы можете создавать собственные [рабочие процессы](../../../analyze-explore-automate/workflows.md "Автоматизируйте IT-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.") или использовать наши шаблоны для автоматизации и оркестрации результатов уязвимостей контейнеров.

1. В **Settings** откройте **AWS Security Hub**.
2. В разделе **Try our templates** выберите нужный шаблон рабочего процесса.

### Запрос загруженных данных

Вы можете запрашивать загруженные данные в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитикой из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") или [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../investigations.md "Объединяйте функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и охоту за угрозами."), используя формат данных из [семантического словаря](https://dt-url.net/3q03pb0).

1. В **Settings** откройте **AWS Security Hub**.
2. Выберите **Open with**.
3. Выберите **Investigations** или **Notebooks**.

### Оценка, приоритизация и расследование результатов обнаружения

Вы можете оценивать, приоритизировать и расследовать результаты обнаружения с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../../threats-and-exploits.md "Понимайте, приоритизируйте и расследуйте результаты обнаружения и оповещения.").

1. Откройте ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**.
2. Отфильтруйте по **Provider** > **AWS Security Hub**.

### Поддержка и сопоставление

Для AWS Dynatrace поддерживает следующие типы событий безопасности:

* Vulnerability (уязвимости)
* Detection (обнаружения)
* Compliance experimental (соответствие, экспериментально)

#### Список событий AWS, сопоставленных с Dynatrace

| Тип события AWS | Сопоставление с Dynatrace |
| --- | --- |
| Software and Configuration Checks/Vulnerabilities/\* | Результаты обнаружения уязвимостей |
| TTPs/\* | Результаты обнаружения |
| Effects/\* | Результаты обнаружения |
| Unusual Behaviors/\* | Результаты обнаружения |
| Software and Configuration Checks/Industry and Regulatory Standards/\* | Результаты соответствия |

Все остальные события загружаются, но не сопоставляются.

#### Как обрабатываются обнаружения

* Когда имеется несколько ресурсов AWS, обнаружения разделяются по каждому связанному ресурсу в событии для генерации отдельных событий на ресурс.
* Поле `types` из AWS Security Hub, которое обычно является массивом с одним значением, сопоставляется с `detection.type`. Когда указано несколько типов, сопоставляется первое значение массива.

### Ограничение загрузки

По умолчанию, после настройки интеграции Dynatrace все типы событий AWS загружаются в Dynatrace.

Чтобы ограничить загрузку определённым типом события, необходимо настроить [фильтры](https://dt-url.net/z803wpf) для Lambda-функции пересылки событий Dynatrace AWS Security Hub в [EventBridge](https://dt-url.net/qi03wtk).

1. Как настроить фильтры

1. В консоли AWS перейдите в **Lambda** > **Functions** и выберите функцию пересылки событий Dynatrace AWS Security Hub.
2. В **Configuration** отредактируйте шаблон события для триггера.

Примеры фильтров:

Загрузка только результатов уязвимостей

Загрузка только результатов обнаружения

Загрузка только результатов соответствия

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": ["Software and Configuration Checks/Vulnerabilities/CVE"]



}



}



}
```

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": [{



"wildcard": "TTPs*"



}, {



"wildcard": "Effects*"



}, {



"wildcard": "Unusual Behaviors*"



}]



}



}



}
```

experimental

```
{



"source": ["aws.securityhub"],



"detail-type": ["Security Hub Findings - Imported"],



"detail": {



"findings": {



"Types": [{



"wildcard": "Software and Configuration Checks/Industry and Regulatory Standards*"



}]



}



}



}
```

### Удаление подключений

Чтобы прекратить отправку событий в Dynatrace

1. В **Settings** откройте **AWS Security Hub**.
2. Для подключения, которое вы хотите удалить, выберите **Delete**.
3. Следуйте инструкциям на экране для удаления ресурсов. Если вы использовали значения, отличные от указанных в диалоге настройки, скорректируйте их соответственно.

Это удалит ресурсы Dynatrace, созданные для данной интеграции.

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [События на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в модели подписки на платформу Dynatrace.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Загружайте уязвимости, обнаружения и результаты соответствия AWS Security Hub.](https://www.dynatrace.com/hub/detail/aws-security-hub)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.")