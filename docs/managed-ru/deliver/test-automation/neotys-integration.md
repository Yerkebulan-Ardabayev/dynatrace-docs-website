---
title: NeoLoad
source: https://docs.dynatrace.com/managed/deliver/test-automation/neotys-integration
scraped: 2026-05-12T11:38:37.449667
---

# NeoLoad

# NeoLoad

* Published Feb 08, 2022

NeoLoad — это платформа автоматизированного тестирования производительности, помогающая корпоративным организациям внедрять непрерывное тестирование и сквозное тестирование. NeoLoad имеет двунаправленную интеграцию с Dynatrace для точного анализа поведения всего приложения и его экосистемы под нагрузкой. Если вы являетесь пользователем как Dynatrace, так и NeoLoad, вы получаете KPI для анализа и принятия автоматизированных решений. NeoLoad поддерживает полный спектр мобильных, веб- и пакетных приложений.

По завершении каждого теста NeoLoad для каждого отслеживаемого сервиса создаётся событие Dynatrace. NeoLoad также отправляет глобальную статистику теста в Dynatrace, чтобы её можно было использовать в качестве пользовательских метрик на дашбордах Dynatrace.

## Предварительные условия Dynatrace

Прежде чем настраивать интеграцию со стороны NeoLoad, убедитесь, что выполнены следующие предварительные условия на стороне Dynatrace.

### Токен API

Для интеграции NeoLoad требуется [токен API Dynatrace](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") со следующими разрешениями:

| API v1 | API v2 |
| --- | --- |
| **Access problem and event feed, metrics and topology** | **Read metrics** |
| **Capture Request Data** | **Read entities** |
| **Read configuration** | **Write entities** |
| **Write configuration** |  |
| **Data ingest** |  |

### Тегирование

Каждый сервис, для которого нужно получать данные NeoLoad, должен быть [тегирован](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically."). Соответствующие теги добавляются при настройке интеграции со стороны NeoLoad.

## Настройка NeoLoad

Подробные инструкции по настройке интеграции в NeoLoad см. в разделе [Enable the integration of Dynatrace](https://documentation.tricentis.com/neoload/9.0/en/WebHelp/#5896_1.htm) документации NeoLoad.

## Анализ результатов в Dynatrace

Трафик, создаваемый NeoLoad, идентифицируется по добавляемому NeoLoad заголовку `X-Dynatrace-Test`, что позволяет легко изолировать трафик от NeoLoad. Метрики NeoLoad можно искать в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") с фильтрацией по `custom:neoload`.

## Связанные темы

* [Интеграция Dynatrace с инструментами нагрузочного тестирования](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Захват атрибутов запроса на основе данных веб-запроса](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Фильтрация данных мониторинга через атрибуты запроса](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")