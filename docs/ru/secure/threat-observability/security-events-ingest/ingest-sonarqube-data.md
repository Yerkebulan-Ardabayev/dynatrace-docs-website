---
title: Прием событий безопасности и качества, метрик и журналов аудита SonarQube
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data
scraped: 2026-03-06T21:23:52.074280
---

# Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube


* Расширение

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, описан в [руководстве по миграции таблицы безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Загрузка событий безопасности и качества, метрик и журналов аудита SonarQube в Dynatrace в качестве событий безопасности.

## Начало работы

### Обзор

Интеграция Dynatrace с [SonarQube](https://www.sonarsource.com/) позволяет объединять и контекстуализировать результаты поиска уязвимостей из инструментов и продуктов DevSecOps, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию результатов безопасности.

SonarQube генерирует результаты поиска уязвимостей в артефактах разработки, таких как код и конфигурационные файлы. Платформа Dynatrace наблюдает за соответствующими сущностями среды выполнения, связанными с этими артефактами. Загрузка и обогащение результатов поиска уязвимостей помогает пользователям лучше сосредоточиться на наиболее значимых рисках, влияющих на их рабочие приложения.

В рамках этой интеграции, помимо журналов аудита и событий безопасности, Dynatrace загружает различные метрики качества SonarQube и генерирует события жизненного цикла разработки ПО (SDLC) для представления оценок артефактов, выполненных в конвейере SDLC. Это позволяет командам разработки получить более полное представление о качестве своих приложений и сервисов. Это также позволяет SRE-инженерам иметь лучшую видимость и контроль над качеством развёрнутых артефактов с различных точек зрения.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии использования, такие как

* [Визуализация и анализ результатов безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Визуализация, приоритизация и анализ загруженных результатов безопасности.")
* [Обнаружение пробелов в покрытии безопасности](../../use-cases/discover-coverage-gaps-in-security-scans.md "Выявите слепые зоны в вашем жизненном цикле разработки ПО (SDLC).")
* [Автоматизация и оркестрация результатов безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Регулярная проверка критических результатов безопасности и автоматическое создание тикетов Jira или уведомлений Slack.")

### Требования

[SonarQube Server Web API v1](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/)

#### Требования SonarQube

* [Сгенерируйте API-токен](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/managing-tokens/#generating-a-token) с разрешениями системного администратора и `Browse` для проектов, которые необходимо мониторить.

#### Требования Dynatrace

* ActiveGate версии 1.313+, который должен иметь возможность

  + Запускать фреймворк Extensions 2.0
  + Подключаться к URL-адресу API SonarQube
* Разрешения: Для получения списка необходимых разрешений перейдите в **Hub**, выберите ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** и откройте **Technical information**.
* Сгенерируйте токен доступа с областями действия `openpipeline.events_security` и `openpipeline.events_sdlc` и сохраните его. Подробнее см. [Dynatrace API — токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace найдите **SonarQube** и выберите **Install**.
2. Следуйте инструкциям на экране для настройки расширения.
3. Проверьте конфигурацию, выполнив следующие запросы в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости в едином настраиваемом рабочем пространстве."):

   * Для журналов аудита:

     ```
     fetch logs


     | filter log.source=="SonarQube"
     ```
   * Для событий обнаружения уязвимостей:

     ```
     fetch security.events


     | filter dt.system.bucket == "default_securityevents"


     | filter event.provider=="SonarQube"


     AND event.type=="VULNERABILITY_FINDING"
     ```
   * Для событий сканирования безопасности:

     ```
     fetch security.events


     | filter dt.system.bucket == "default_securityevents"


     | filter event.provider=="SonarQube"


     AND event.type=="VULNERABILITY_SCAN"
     ```
   * Для событий SDLC:

     ```
     fetch events


     | filter event.kind == "SDLC_EVENT"


     AND event.type == "control"


     | filter event.provider=="SonarQube"
     ```
   * Для метрик:

     ```
     timeseries {


     Vulnerabilities = sum(sonarqube.code.vulnerabilities),


     Hotspots = sum(sonarqube.security.hotspots),


     `Hotspots reviewed` = sum(sonarqube.security.hotspots.reviewed),


     Bugs = sum(sonarqube.bugs),


     Coverage = sum(sonarqube.code.coverage),


     `Duplicated lines` = sum(sonarqube.code.duplication),


     `Code smells` = sum(sonarqube.code.smells)


     }, interval:3h
     ```
4. После установки и запуска расширения вы можете получить к нему доступ и управлять им в Dynatrace через ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. Подробнее см. [О расширениях](../../../ingest-from/extensions/concepts.md "Узнайте больше о концепции расширений Dynatrace.").

## Подробности

### Как это работает

![механизм sonarqube](https://dt-cdn.net/images/architecture-diagram-1-2560-7fb217b566.png)

Интеграция Dynatrace с SonarQube представляет собой [расширение](../../../ingest-from/extensions.md "Узнайте, как создавать и управлять расширениями Dynatrace."), работающее на Dynatrace ActiveGate. После включения и настройки расширения Dynatrace SonarQube

1. Оно периодически собирает результаты безопасности и журналы аудита с помощью [SonarQube Web API v1](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/).
2. Полученные данные загружаются в Dynatrace и сопоставляются с [семантическим словарём Dynatrace](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.").
3. Данные хранятся в корзине `default_securityevents` (подробнее см. [Встроенные корзины Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из корзин, таблиц и представлений.")).

### Лицензирование и стоимость

Информацию о биллинге см. в разделе [События на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в модели подписки Dynatrace Platform.").

## Часто задаваемые вопросы

### Какая модель данных используется для журналов безопасности и событий, поступающих из SonarQube?

* [**События обнаружения уязвимостей**](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.") хранят отдельные результаты обнаружения уязвимостей, сообщённые SonarQube, для затронутых артефактов и компонентов.
* [**События сканирования уязвимостей**](../../../semantic-dictionary/model/security-events.md#vulnerability-scan-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.") отражают покрытие сканирования для отдельных артефактов.
* [**Журналы аудита**](../../../semantic-dictionary/model/log.md#audit-logs "Ознакомьтесь с моделями семантического словаря, связанными с Log Analytics.") представляют журналы активности пользователей в SonarQube.
* **События управления SDLC** указывают на запуск проверки управления.

### Какие результаты безопасности SonarQube импортируются в Dynatrace?

* Если расширение настроено на загрузку данных с интервалом `n` часов, при каждом запуске расширения все результаты безопасности, сгенерированные за последние `n` часов, будут загружены.
* При первой загрузке учитываются все результаты, обновлённые за последние `m` часов, где `m` — интервал первой загрузки, настроенный в конфигурации мониторинга.
* Если сканирования не проводились, результаты не загружаются, даже если в проекте есть открытые проблемы.

### Какие поля расширения добавлены поверх основных полей событий, загружаемых из SonarQube?

Пространство имён `sonarqube` добавлено для извлечения нескольких специфических для SonarQube атрибутов для удобства пользователя поверх исходного JSON проблемы, который хранится в поле `dt.raw_data`.

Примеры полей:

* `sonarqube.project.name`
* `sonarqube.project.id`
* `sonarqube.revision`
* `sonarqube.revision.author`
* `sonarqube.tags`
* `sonarqube.component`

### Какие типы ресурсов SonarQube поддерживаются Dynatrace для контекстуализации среды выполнения?

`CODE_ARTIFACT`: все результаты из SonarQube генерируются оценками уязвимостей артефактов кода, для которых в поле `object.type` установлено значение `CODE_ARTIFACT`. Пространства имён `artifact` и `code` добавлены с соответствующими полями:

* `artifact.repository.name`: имя репозитория, содержащего артефакт.
* `artifact.path`: полный путь к файлу, представляющему артефакт кода.
* `code.filepath`: включает версию уязвимого компонента.
* `code.line.number`: номер строки, где обнаружена проблема.
* `code.line.offset.start`: номер первого символа в строке с проблемой.
* `code.line.offset.end`: номер последнего символа в строке с проблемой.
* `code.line.start`: номер строки, где начинается проблема. Совпадает с `code.line.number`.
* `code.line.end`: номер строки, где заканчивается проблема.

### Как нормализуется оценка риска для результатов SonarQube?

Dynatrace нормализует уровни серьёзности и оценки рисков для всех результатов, загруженных через текущую интеграцию. Это помогает вам последовательно приоритизировать результаты независимо от их источника.
Подробнее о нормализации см. [Нормализация серьёзности и оценки](../concepts.md#normalization "Основные концепции, связанные с Threat Observability").

Уровни и оценки рисков Dynatrace сопоставлены с исходными [уровнями серьёзности SonarQube](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience#se-severity).

* `dt.security.risk.level` берётся из уровня серьёзности SonarQube и сопоставляется с исходными значениями в `finding.severity`.
* `dt.security.risk.score` сопоставляется из предоставленного SonarQube уровня серьёзности со статическими оценками.

| `dt.security.risk.level` (сопоставлен из `finding.severity`) | `dt.security.risk.score` (сопоставлен из `dt.security.risk.level`) |
| --- | --- |
| BLOCKER  CRITICAL | 10.0 |
| CRITICAL/HIGH  HIGH | 8.9 |
| MEDIUM/MAJOR  MEDIUM | 6.9 |
| MINOR/INFO/LOW  LOW | 3.9 |
| INFO  NONE | 0.0 |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Откройте в Dynatrace Hub

Загрузка результатов обнаружения уязвимостей, метрик и журналов аудита SonarQube.](https://www.dynatrace.com/hub/detail/sonarqube)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.")
