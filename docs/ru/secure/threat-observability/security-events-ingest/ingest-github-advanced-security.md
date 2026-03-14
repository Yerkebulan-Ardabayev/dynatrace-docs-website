---
title: Прием событий безопасности и журналов аудита GitHub Advanced Security
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security
scraped: 2026-03-06T21:24:04.309763
---

# Приём событий безопасности и журналов аудита GitHub Advanced Security

# Приём событий безопасности и журналов аудита GitHub Advanced Security

* Latest Dynatrace
* Расширение
* Обновлено 7 октября 2025 г.

Эта страница обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список изменений и необходимых действий для завершения миграции см. в [руководстве по миграции таблиц безопасности Grail](../migration.md "Узнайте об изменениях в новой таблице безопасности Grail и о том, как выполнить миграцию.").

Загружайте журналы аудита и события безопасности GitHub Advanced Security в Dynatrace в качестве событий безопасности.

## Начало работы

### Обзор

Интеграция Dynatrace с [GitHub Advanced Security](https://github.com/security/advanced-security) (GHAS) позволяет пользователям объединять и контекстуализировать результаты анализа уязвимостей из различных инструментов и продуктов DevSecOps, обеспечивая централизованную приоритизацию, визуализацию и автоматизацию результатов безопасности.

[GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) включает [Code Security](https://github.com/security/advanced-security/code-security) и [Secret Protection](https://github.com/security/advanced-security/secret-protection), которые генерируют результаты анализа уязвимостей для артефактов разработки, таких как код и контейнеры. Dynatrace наблюдает за сущностями времени выполнения, связанными с этими артефактами. Приём и обогащение результатов анализа уязвимостей помогает пользователям сфокусироваться на высокоприоритетных рисках, влияющих на рабочие приложения.

Первая версия этой интеграции загружает и контекстуализирует [оповещения Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts), которые бесплатны для публичных репозиториев и являются частью премиального предложения Code Security.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии, такие как:

* [Визуализация и анализ результатов безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Визуализируйте, приоритизируйте и анализируйте загруженные результаты безопасности.")
* [Автоматизация и оркестрация результатов безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Регулярно проверяйте критические результаты безопасности и получайте автоматические тикеты Jira или оповещения Slack.")
* [Обнаружение пробелов в покрытии безопасности](../../use-cases/discover-coverage-gaps-in-security-scans.md "Выявите слепые зоны в вашем жизненном цикле разработки ПО (SDLC).")

### Требования

Ниже описаны требования для [GitHub](#github) и [Dynatrace](#dt).

#### Требования GitHub

Для сбора данных безопасности расширению необходимы учётные данные аутентификации с соответствующими разрешениями. Доступны два варианта, описанных ниже.

Аутентификация на основе GitHub-приложения

Аутентификация на основе PAT

Рекомендуется

[Аутентификация на основе GitHub-приложения](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-token-generated-by-an-app)

* Обеспечивает гранулярный контроль разрешений
* Позволяет собирать журналы аудита на уровне организации
* Имеет более высокие лимиты API-запросов

Для регистрации и установки GitHub-приложения выполните следующие шаги.

1. Зарегистрируйте GitHub-приложение

1. Следуйте инструкциям в [Регистрация GitHub-приложения](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) со следующими значениями:

* Для **GitHub App Name** введите `DynatraceAppSec-<Your Company>`, заменив `<Your Company>` на ваше значение.
* Для **Homepage URL** введите `https://dynatrace.com`.
* Снимите флажок **Webhook > Active**.
* Включите следующие разрешения:

  + Разрешения репозитория:

    - **Contents**: `Read-only`
    - **Dependabot alerts**: `Read-only`
    - **Code scanning alerts**: `Read-only` (необходимо при приёме событий сканирования кода)
    - **Secret scanning alerts**: `Read-only` (необходимо при приёме событий сканирования секретов)
  + Разрешения организации

    - **Administration**: `Read-only` (необходимо для журналов аудита)
* Для указания места установки приложения выберите один из вариантов:

  + `Any account` (позволяет установить приложение в нескольких организациях и даже в учётных записях пользователей, что упростит конфигурации мониторинга)
  + `Only this account` (приложение устанавливается в текущей учётной записи; это означает, что вам потребуется несколько приложений и конфигураций мониторинга для покрытия нескольких организаций в рамках предприятия)

2. Сгенерируйте закрытый ключ для приложения

1. Выберите вкладку **General** и перейдите к настройкам зарегистрированного приложения.
2. Скопируйте идентификатор клиента (он потребуется при настройке конфигурации мониторинга).
3. В разделе **Private keys** сгенерируйте закрытый ключ (он потребуется при настройке конфигурации мониторинга)

   Закрытый ключ позволяет выполнять аутентифицированные запросы от расширения; обеспечьте его безопасное хранение.

3. Установите приложение

[Установите GitHub-приложение](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app) на все учётные записи (пользователей или организаций), которые вы хотите отслеживать.

[Аутентификация на основе Personal Access Token (PAT)](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-personal-access-token)

* Обеспечивает более быструю настройку
* Подходит для быстрой валидации интеграции
* Позволяет собирать журналы аудита

  Для [журналов аудита предприятия](https://docs.github.com/en/enterprise-cloud@latest/rest/enterprise-admin/audit-log?apiVersion=2022-11-28) аутентифицированный пользователь должен быть администратором предприятия для использования этого эндпоинта.

Для генерации Personal Access Token следуйте инструкциям в [Управление персональными токенами доступа](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), указав следующие значения:

* Токен должен быть **Classic Personal Access Token**.
* **Expiration**: если вы устанавливаете срок действия токена, вы несёте ответственность за его обновление.
* **Scopes**:

  + **repo**: полный контроль
  + **audit\_log**: `read:audit_log`

#### Требования Dynatrace

* ActiveGate версии 1.310+, который должен:

  + Поддерживать платформу Extensions 2.0
  + Иметь доступ к URL-адресам API GitHub
* Разрешения:

  + Для запуска ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**: Перейдите в **Hub**, выберите ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** и откройте **Technical information**.
  + Для запросов загруженных данных: `storage:security.events:read`.
* Сгенерируйте токен доступа с областью `openpipeline.events_security` и сохраните его. Подробнее см. [API Dynatrace — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования API Dynatrace.").

## Активация и настройка

1. В Dynatrace найдите **GitHub Advanced Security** и выберите **Install**.
2. Следуйте инструкциям на экране для настройки расширения.
3. Проверьте конфигурацию, выполнив следующие запросы в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитикой ваших данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве."):

   * Для журналов аудита:

     ```
     fetch logs



     | filter log.source=="GitHub Advanced Security"
     ```
   * Для событий обнаружения:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="GitHub Advanced Security"



     AND event.type=="VULNERABILITY_FINDING"
     ```
   * Для событий сканирования:

     ```
     fetch security.events



     | filter dt.system.bucket == "default_securityevents"



     | filter event.provider=="GitHub Advanced Security"



     AND event.type=="VULNERABILITY_SCAN"
     ```
4. После установки и настройки расширения вы можете получить доступ к нему и управлять им в Dynatrace через ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**. Подробнее см. [О расширениях](../../../ingest-from/extensions/concepts.md "Узнайте больше о концепции расширений Dynatrace.").

## Подробности

### Как это работает

![how it works](https://dt-cdn.net/images/diagram-2560-ac2977ae34.png)

1. События и логи собираются из продуктов GHAS

Интеграция Dynatrace GHAS — это расширение, развёрнутое в [Dynatrace ActiveGate](../../../ingest-from/dynatrace-activegate.md "Основные концепции ActiveGate."), которое периодически собирает результаты анализа безопасности и журналы аудита с помощью [GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28).

2. Результаты безопасности и логи загружаются в Dynatrace

Результаты безопасности загружаются в платформу Dynatrace через выделенный эндпоинт приёма безопасности [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью OpenPipeline.").

3. Результаты безопасности и логи обрабатываются и сохраняются в Grail

Эндпоинт приёма OpenPipeline обрабатывает и сопоставляет результаты безопасности в соответствии с [конвенциями Semantic Dictionary](https://dt-url.net/3q03pb0).

Они сохраняются в бакете `default_securityevents` (подробнее см. [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Организация данных в модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

Опционально собранные журналы аудита загружаются через выделенный [конвейер приёма логов расширений](../../../analyze-explore-automate/logs/lma-log-ingestion.md#ingest-extensions "Потоковая передача данных логов в Dynatrace.") и сохраняются в соответствующем [семантическом формате](../../../semantic-dictionary/model/log.md "Модели Semantic Dictionary, связанные с аналитикой логов.").

### Лицензирование и стоимость

Информацию о тарификации см. в [События на платформе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на платформе Grail в рамках модели подписки Dynatrace Platform.").

## Наборы функций

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) вы можете ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собрать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. При создании конфигурации мониторинга вы можете выбрать набор функций и соответствующую группу ActiveGate, которая может подключиться к определённому сегменту.

Все метрики, не отнесённые к какому-либо набору функций, считаются набором по умолчанию и всегда передаются.

Метрика наследует набор функций подгруппы, которая в свою очередь наследует набор функций группы. Набор функций, определённый на уровне метрики, переопределяет набор, определённый на уровне подгруппы, который в свою очередь переопределяет набор, определённый на уровне группы.

## Часто задаваемые вопросы

### Какая модель данных используется для логов безопасности и событий из интеграции GHAS?

* [**События обнаружения уязвимостей**](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Модели Semantic Dictionary, связанные с событиями безопасности.") хранят отдельные результаты обнаружения уязвимостей, сообщённые различными продуктами GHAS для затронутых артефактов и компонентов.
* [**События сканирования уязвимостей**](../../../semantic-dictionary/model/security-events.md#vulnerability-scan-events "Модели Semantic Dictionary, связанные с событиями безопасности.") указывают на покрытие сканирования для отдельных артефактов.
* [**Журналы аудита**](../../../semantic-dictionary/model/log.md#audit-logs "Модели Semantic Dictionary, связанные с аналитикой логов.") представляют журналы активности пользователей в продуктах GHAS.

### Какие результаты безопасности GHAS импортируются в Dynatrace?

* Если расширение настроено на приём данных с интервалом `n` часов, то при каждом запуске все события безопасности (оповещения Dependabot, сканирования кода и сканирования секретов), обновлённые за последние `n` часов, будут загружены.
* При первом приёме учитываются оповещения, обновлённые за последние `m` часов, где `m` — интервал первого приёма, настроенный в конфигурации мониторинга.
* Если сканирование не проводилось, результаты не будут загружены, даже если в проекте есть открытые проблемы. Обратитесь к документации GitHub по [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts#detection-of-insecure-dependencies), [сканированию кода](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql) и [сканированию секретов](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning), чтобы узнать, когда запускается сканирование.

### Какие поля расширения добавляются к основным полям событий, загруженных из GHAS?

Пространство имён `github` добавляется для извлечения нескольких атрибутов, специфичных для GHAS, для удобства пользователей поверх исходного JSON, который хранится в поле `event.original_content`.

**Примеры**:

* `github.dependency.relationship`
* `github.dependency.scope`
* `github.epss.percentage`
* `github.epss.percentile`
* `github.ecosystem`

### Какие типы активов GHAS поддерживаются Dynatrace для контекстуализации времени выполнения?

`CODE_ARTIFACT`: Все результаты из продуктов GitHub Advanced Security, полученные в результате оценки артефактов кода, сопоставляются со значением `CODE_ARTIFACT` в поле `object.type`, и добавляются пространства имён `artifact` и `component` с соответствующими полями:

* `artifact.repository.name` представляет имя репозитория, содержащего артефакт.
* `artifact.path` — полный путь к файлу, представляющему артефакт кода.
* `component.name` представляет имя уязвимой библиотеки внутри артефакта кода.
* `component.version` включает версию уязвимого компонента.

  GitHub предоставляет только предельные значения, а не точную версию, например, `<1.4`. Это ограничивает возможность сопоставления компонентов времени выполнения, поскольку версия в этом случае не совпадает.

### Как нормализуется оценка риска для результатов GHAS?

Dynatrace нормализует уровни серьёзности и оценки риска для всех результатов, загруженных через текущую интеграцию. Это помогает приоритизировать результаты единообразно, независимо от их источника.
Подробнее о нормализации см. [Нормализация серьёзности и оценок](../concepts.md#normalization "Основные концепции наблюдаемости угроз").

Уровни и оценки риска Dynatrace сопоставляются с исходными [уровнями серьёзности и оценками GHAS](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).

* `dt.security.risk.level` — берётся из уровня серьёзности GHAS и сопоставляется из исходных значений в `finding.severity`.
* `dt.security.risk.score` — берётся из уровня серьёзности GHAS и сопоставляется со статическими оценками. Оценка CVSS, сообщённая GHAS, доступна в `finding.score`; однако она может не всегда совпадать с указанной серьёзностью.

| `dt.security.risk.level` (сопоставлено из `finding.severity`) | `dt.security.risk.score` (сопоставлено из `dt.security.risk.level`) |
| --- | --- |
| critical -> CRITICAL | 10.0 |
| high/error -> HIGH | 8.9 |
| medium/warning -> MEDIUM | 6.9 |
| low/note -> LOW | 3.9 |

Оповещениям сканирования секретов по умолчанию присваивается уровень риска HIGH. Вы можете настроить эту настройку в **Advanced options** при конфигурации расширения.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

Загрузка событий безопасности и журналов аудита GitHub Advanced Security (GHAS).](https://www.dynatrace.com/hub/detail/github-advanced-security/)

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Модели Semantic Dictionary, связанные с событиями безопасности.")