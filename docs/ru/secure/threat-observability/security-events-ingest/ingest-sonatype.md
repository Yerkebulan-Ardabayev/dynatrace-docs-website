---
title: Прием событий безопасности и журналов аудита Sonatype Lifecycle
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-sonatype
scraped: 2026-03-06T21:24:09.563425
---

# Загрузка событий безопасности и журналов аудита Sonatype Lifecycle


* Latest Dynatrace
* Extension

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, описан в [руководстве по миграции таблиц безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

Загружайте события безопасности и журналы аудита Sonatype Lifecycle в Dynatrace в качестве событий безопасности.

## Начало работы

### Обзор

Интеграция Dynatrace с [Sonatype Lifecycle](https://www.sonatype.com/products/open-source-security-dependency-management) позволяет пользователям объединять и контекстуализировать результаты анализа уязвимостей из различных инструментов и продуктов DevSecOps, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию обработки результатов безопасности.

Sonatype предлагает ряд продуктов, помогающих разработчикам повысить продуктивность. Продукт [Sonatype Lifecycle](https://help.sonatype.com/en/sonatype-lifecycle.html) выявляет уязвимости в артефактах разработки, таких как код и контейнеры. Платформа Dynatrace наблюдает за соответствующими сущностями времени выполнения, связанными с этими артефактами. Загрузка и обогащение результатов анализа уязвимостей помогает пользователям лучше сосредоточиться на основных рисках, влияющих на их продуктивные приложения.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии использования, например:

* [Визуализация и анализ результатов безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Визуализируйте, приоритизируйте и анализируйте загруженные результаты безопасности.")
* [Обнаружение пробелов в покрытии результатов безопасности](../../use-cases/discover-coverage-gaps-in-security-scans.md "Выявляйте слепые зоны в жизненном цикле разработки программного обеспечения (SDLC).")
* [Автоматизация и оркестрация результатов безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Регулярно проверяйте критические результаты безопасности и получайте автоматические тикеты Jira или оповещения Slack.")

### Требования

Ниже приведены требования для [Sonatype Lifecycle](#sonatype) и [Dynatrace](#dt).

#### Требования Sonatype Lifecycle

Для того чтобы расширение могло собирать данные безопасности из Sonatype Lifecycle, необходимы учётные данные аутентификации с соответствующими разрешениями. Есть два варианта предоставления учётных данных:

* **Вариант 1**: [Пользовательский токен](https://help.sonatype.com/en/iq-server-user-tokens.html) Рекомендуется

  + Рекомендуется для сервисных пользователей.
  + Состоит из кода пользователя и пароля.
  + Это одноразовые учётные данные, которые можно отозвать в любое время без влияния на связанную учётную запись пользователя.
* **Вариант 2**: Имя пользователя и пароль

  + Используются стандартные учётные данные для входа в вашу учётную запись.

**Необходимые разрешения**:

Для успешного сбора данных аутентифицированный пользователь должен иметь следующие разрешения в Sonatype Lifecycle:

* `View IQ Elements`
* `Access Audit Log` (требуется только при настроенной загрузке журнала аудита)

#### Требования Dynatrace

* ActiveGate версии 1.313+, который должен иметь возможность

  + Запускать фреймворк Extensions 2.0
  + Обращаться к конечным точкам API Sonatype
* Разрешения: список необходимых разрешений можно найти, перейдя в **Hub**, выбрав ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** и открыв **Technical information**.
* Сгенерируйте токен доступа с областью действия `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробнее см. [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Активация и настройка

1. В Dynatrace найдите **Sonatype Lifecycle** и выберите **Install**.
2. Следуйте инструкциям на экране для настройки расширения.
3. Проверьте конфигурацию, выполнив следующие запросы в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитикой из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве."):

   * Для журналов аудита:

     ```
     fetch logs


     | filter log.source=="Sonatype Lifecycle"
     ```
   * Для событий обнаружения:

     ```
     fetch security.events


     | filter dt.system.bucket == "default_securityevents"


     | filter event.provider=="Sonatype Lifecycle"


     AND event.type=="VULNERABILITY_FINDING"
     ```
   * Для событий сканирования:

     ```
     fetch security.events


     | filter dt.system.bucket == "default_securityevents"


     | filter event.provider=="Sonatype Lifecycle"


     AND event.type=="VULNERABILITY_SCAN"
     ```
4. После установки и запуска расширения вы можете управлять им в Dynatrace через ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. Подробнее см. [О расширениях](../../../ingest-from/extensions/concepts.md "Узнайте больше о концепции расширений Dynatrace.").

## Подробности

### Как это работает

![как это работает - sonatype](https://dt-cdn.net/images/architechture-diagram-2560-277696e6e1.png)

Интеграция Dynatrace с Sonatype Lifecycle — это [расширение](../../../ingest-from/extensions.md "Узнайте, как создавать и управлять расширениями Dynatrace."), работающее на Dynatrace ActiveGate. После включения и настройки расширения Dynatrace Sonatype Lifecycle

1. Оно периодически собирает результаты безопасности и журналы аудита с помощью [Sonatype REST API](https://help.sonatype.com/en/rest-apis.html).
2. Полученные данные загружаются в Dynatrace и сопоставляются с [семантическим словарём Dynatrace](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.").
3. Данные хранятся в корзине (bucket) с именем `default_securityevents` (подробнее см. [Встроенные корзины Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из корзин, таблиц и представлений.")).

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [События на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в модели подписки на платформу Dynatrace.").

## Часто задаваемые вопросы

### Какая модель данных используется для журналов безопасности и событий, поступающих из Sonatype Lifecycle?

* [События обнаружения уязвимостей](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.") хранят отдельные результаты обнаружения уязвимостей, сообщённые Sonatype Lifecycle для затронутых артефактов и компонентов.
* [**События сканирования уязвимостей**](../../../semantic-dictionary/model/security-events.md#vulnerability-scan-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.") указывают на покрытие сканирования для отдельных артефактов.
* [**Журналы аудита**](../../../semantic-dictionary/model/log.md#audit-logs "Ознакомьтесь с моделями семантического словаря, связанными с Log Analytics.") представляют собой журналы активности пользователей в Sonatype Lifecycle.

### Какие результаты безопасности Sonatype Lifecycle импортируются в Dynatrace?

* При первой загрузке учитываются результаты, обновлённые за последние `m` часов, где `m` — интервал первой загрузки, настроенный в конфигурации мониторинга.
* Если расширение настроено на загрузку данных с интервалом `n` часов, то при каждом запуске расширения будут загружены все результаты обнаружения уязвимостей, обновлённые за последние `n` часов.
* Если новых или обновлённых результатов не обнаружено, загрузка результатов не производится.

### Какие поля расширения добавляются к основным полям событий, загруженных из Sonatype Lifecycle?

Пространство имён `sonatype` добавляется для извлечения нескольких специфичных для Sonatype атрибутов для удобства пользователей поверх исходного JSON, который хранится в поле `event.original_content`.

**Примеры**:

* `sonatype.application_public_id` представляет понятное имя оцениваемого приложения.
* `sonatype.application_internal_id` представляет идентификатор оцениваемого приложения.
* `sonatype.commit_hash` представляет хеш коммита кода, к которому относится оценка.
* `sonatype.stage` представляет стадию приложения, на которой была выполнена оценка.

### Какие типы активов Sonatype Lifecycle поддерживаются Dynatrace для контекстуализации во время выполнения?

`CODE_ARTIFACT`: Все результаты из Sonatype Lifecycle, полученные при оценке артефактов кода, помечаются значением `CODE_ARTIFACT` в поле `object.type`, и добавляется пространство имён `software_component` с соответствующими полями:

* `software_component.purl` представляет URL пакета уязвимого программного компонента.
* `software_component.ecosystem` представляет экосистему компонента, такую как maven, npm и другие.
* `software_component.type` представляет тип уязвимого программного компонента.
* `software_component.name` представляет имя уязвимой библиотеки в артефакте кода.
* `software_component.version` представляет версию уязвимого компонента.

### Как нормализуется оценка риска для результатов Sonatype Lifecycle?

Dynatrace нормализует уровни серьёзности и оценки риска для всех результатов, загруженных через текущую интеграцию. Это помогает вам последовательно приоритизировать результаты, независимо от их источника.
Подробнее о работе нормализации см. [Нормализация серьёзности и оценки](../concepts.md#normalization "Основные концепции, связанные с Threat Observability").

Уровни и оценки риска Dynatrace сопоставляются с исходными оценками Sonatype Lifecycle.

* `dt.security.risk.score` — сопоставляется из оценки серьёзности, предоставленной Sonatype Lifecycle, в статические оценки.
* `dt.security.risk.level` — сопоставляется из оценки серьёзности Sonatype Lifecycle и преобразуется из исходных значений в `finding.score`.

| `dt.security.risk.score` (сопоставлено из `finding.score`) | `dt.security.risk.level` (сопоставлено из `dt.security.risk.score`) |
| --- | --- |
| 9.0-10.0 | CRITICAL |
| 7.0-8.9 | HIGH |
| 4.0-6.9 | MEDIUM |
| 0.1-3.9 | LOW |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Загружайте результаты обнаружения уязвимостей Sonatype, сканирования и журналы аудита.](https://www.dynatrace.com/hub/detail/sonatype-lifecycle)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.")