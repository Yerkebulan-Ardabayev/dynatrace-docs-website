---
title: Process logs with technology bundle parsers
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-technology-processor
scraped: 2026-03-06T21:13:36.221723
---

# Обработка логов с помощью парсеров технологических пакетов

# Обработка логов с помощью парсеров технологических пакетов

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Aug 06, 2025

OpenPipeline предлагает предустановленные технологические пакеты. Это библиотеки парсеров (правил обработки) для структурирования технологически специфичных логов в соответствии с Dynatrace Semantic Dictionary. Библиотека парсеров поддерживает широкий спектр технологий, включая общеизвестные форматы данных, популярные сторонние сервисы и облачных провайдеров, таких как AWS Lambda, Python, Cassandra и Apache Tomcat.

Парсеры помогают улучшить фильтрацию, устранение неполадок, метрики, оповещения и дашборды за счёт эффективного извлечения уровней логирования и релевантных атрибутов. Вы также можете использовать технологические пакеты для структурирования логов от технологий, которые не поддерживаются Dynatrace из коробки.

## Для кого предназначена эта статья

Эта статья предназначена для администраторов и пользователей приложений.

## Чему вы научитесь

В этой статье вы узнаете, как обрабатывать логи с помощью технологического пакета в OpenPipeline и анализировать их в Notebooks.

## Перед началом работы

Необходимые знания

* [Приём syslog-данных через ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Обработка в OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Предварительные требования

* Среда [Latest Dynatrace](/docs/platform "Dynatrace is an all-in-one platform that's purpose-built for a wide range of use cases.")
* Лицензия [Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") с возможностями [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

## Шаги

1. Создание конвейера для обработки

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. Чтобы создать новый конвейер, нажмите  **Pipeline** и введите имя, например `Syslog - Pipeline`.
3. Для настройки обработки перейдите в **Processing** >  **Processor** > **Technology bundle** и выберите нужный пакет. Например, пакет **Syslog**.

   Вы можете добавить несколько технологических пакетов в один конвейер, поэтому вам не нужно создавать отдельный конвейер и динамическую маршрутизацию каждый раз.
4. Скопируйте условие сопоставления технологии.

   Вы можете настроить условие сопоставления технологии под ваши нужды через OpenPipeline. См. [Настройка конвейера обработки](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
5. Нажмите **Save**.

Вы успешно настроили новый конвейер с процессором для структурирования syslog-логов в соответствии с предустановленными правилами, соответствующими Dynatrace Semantic Dictionary. Новый конвейер появился в списке конвейеров.

2. Маршрутизация данных в конвейер

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. Чтобы создать новый маршрут, нажмите  **Dynamic route** и введите:

   * Описательное имя, например `Syslog`
   * Скопированное условие сопоставления. Это условие сопоставления настраиваемо. Например, вы можете установить его как `true`, и все логи будут проходить через этот конвейер, если он правильно расположен в списке.
   * Конвейер, содержащий инструкции обработки (`Syslog - Pipeline`)
3. Нажмите **Add**.
4. Убедитесь, что новый маршрут расположен в правильной позиции в списке. Маршруты оцениваются сверху вниз. Данные динамически направляются в конвейер в соответствии с первым подходящим условием сопоставления. Направленные данные не оцениваются последующими условиями.
5. Нажмите **Save**.

Вы успешно настроили новый маршрут. Все syslog-логи направляются в конвейер для обработки. Новый маршрут появился в списке маршрутов.

Подробнее о динамической маршрутизации см. [Маршрутизация данных](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

3. Анализ структурированных логов

После обработки логов в соответствии с технологическим пакетом из содержимого логов извлекаются несколько атрибутов в новые поля, соответствующие Dynatrace Semantic Dictionary. Кроме того, технологические пакеты извлекают другие атрибуты из логов, что позволяет создавать собственные [пользовательские оповещения](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts "Learn more about custom alerts and the logic behind raising them."), [метрики](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.") и [дашборды](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

Обогащение логов

Использование парсеров помогает лучше структурировать и обогатить ваши логи. Сравните:

**Без парсинга**

```
{



"dt.openpipeline.source": "extension:syslog",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!"



}
```

**С парсингом**

```
{



"syslog.severity": 0,



"syslog.version": 1,



"syslog.priority": 24,



"syslog.facility": 3,



"syslog.message": "Critical system failure: Kernel panic detected, immediate attention required!",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!",



"syslog.proc_id": "9999",



"dt.openpipeline.source": "extension:syslog",



"loglevel": "EMERGENCY",



"syslog.message_id": "ID01",



"syslog.hostname": "core-router-01.example.com",



"syslog.appname": "kernel",



"timestamp": "2025-08-06T14:50:30.123000000Z",



"status": "ERROR"



}
```

Вы можете легко фильтровать логи по статусу, приложению или атрибутам, специфичным для технологии, как показано в примерах ниже.

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и откройте новый или существующий ноутбук.
2. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** и введите один из следующих запросов

   * Получение syslog-логов с уровнем warn

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog"



     | filter status == "WARN"



     | sort timestamp desc
     ```

     Результат:
   * Группировка syslog-логов по приложению

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize totalCount = count(), by: {syslog.appname}



     | sort totalCount desc
     ```

     Результат:

     ![Группировка syslog-логов по приложению](https://dt-cdn.net/images/syslog-byapp-1000-25aedf7940.png)
   * Сортировка приложений по проценту syslog-логов с ошибками

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize TotalCount = count(), Count = countIf(status == "ERROR"), by: {syslog.appname}



     | fieldsAdd Percentage = (Count * 100 / TotalCount)



     | sort Count desc



     | fieldsRemove TotalCount
     ```

     Результат:

     ![Сортировка приложений по проценту syslog-логов с ошибками](https://dt-cdn.net/images/syslog-error-995-e3d5fe605b.png)

Для просмотра результатов запросов необходимо, чтобы всё было правильно настроено.

## Заключение

Вы успешно структурировали syslog-логи в соответствии с предустановленными правилами обработки в OpenPipeline. Входящие записи, соответствующие условиям маршрутизации, направляются в конвейер syslog, где извлекаются новые атрибуты, специфичные для технологии syslog. Новые атрибуты соответствуют Dynatrace Semantic Dictionary, что обеспечивает удобный анализ. Вы можете фильтровать syslog-логи в Notebooks и максимально эффективно использовать структурированные логи.

## Связанные темы

* [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.")
* [Фильтрация логов](/docs/secure/investigations/filter-logs "Narrow down data to relevant entries in Investigations.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
