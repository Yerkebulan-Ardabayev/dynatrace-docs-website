---
title: Event triggers for workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/trigger/event-trigger
scraped: 2026-03-05T21:32:26.413235
---

# Триггеры событий для рабочих процессов

# Триггеры событий для рабочих процессов

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 02, 2026

Триггеры событий -- это группа триггеров, которые можно настроить для сопоставления событий в конвейере приёма данных с целью запуска рабочего процесса.

Существует три типа триггеров событий:

* **Event trigger**
* **Davis problem trigger**
* **Davis event trigger**

## Event trigger

**Event trigger** позволяет задать пользовательский фильтр событий с помощью выражения [DQL matcher](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "Это DQL matcher для событий в классическом конвейере."), определяющего, какие события будут запускать выполнение рабочего процесса.

Для определения поведения триггера **Event trigger** доступны следующие параметры конфигурации.

* **Event type**

  + **events** -- создаются Dynatrace, а также вашей конфигурацией мониторинга и платформы.
  + **bizevents** -- бизнес-события. Внешнее приложение отправляет **bizevents**. Подробнее см. [эндпоинт `/bizevents/ingest`](/docs/observe/business-observability/bo-api-ingest "Настройте аутентификацию и приём бизнес-событий через API.").
  + **dt.system.events** -- генерируются системными сервисами Dynatrace. Не все системные события могут запускать рабочие процессы. Чтобы найти подходящие события, ищите те, у которых установлено свойство `dt.openpipeline.pipelines`, используя фильтр `isNotNull(dt.openpipeline.pipelines)` в notebook.
  + **security.events** -- генерируются Dynatrace Application Security, принимаются через [эндпоинт `v1/security.events`](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Приём событий безопасности через встроенные эндпоинты OpenPipeline Ingest API.") или через [пользовательские эндпоинты `custom/security.events/<custom-endpoint-name>`](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Настройка пользовательского эндпоинта для событий безопасности через OpenPipeline Ingest API."). Подробнее см. раздел [события безопасности](/docs/semantic-dictionary/model/security-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.") в семантическом словаре.
* В поле **Filter query** можно определить способ фильтрации событий. Фильтр задаётся в синтаксисе [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Рассмотрите конкретные функции DQL и логические операторы для обработки логов.").

Необязательно: выберите **Query past events**, чтобы оценить объём совпадающих событий в вашей среде.

Отдельные события

Все события оцениваются в конвейере приёма данных относительно выражения DQL matcher поштучно. Поэтому выражение DQL matcher не допускает использования агрегаций или запросов по набору событий.

## Davis problem trigger

Проблемы Davis создаются [Dynatrace Intelligence](/docs/dynatrace-intelligence/root-cause-analysis "Как Dynatrace анализирует проблемы для определения их первопричины.") на основе данных мониторинга. **Davis problem trigger** позволяет избирательно запускать рабочий процесс в ответ на них. Триггер срабатывает один раз, когда проблема Davis становится активной (при открытии и повторном открытии), и опционально один раз при закрытии проблемы.

Для определения поведения триггера **Davis problem trigger** доступны следующие параметры конфигурации.

* **Problem state**

  + **active** -- означает, что проблема Davis ещё не закрыта.
  + **active or closed** -- означает, что проблема Davis может быть как активной, так и закрытой.
* Определения **Event category** приведены в разделе [Категории событий](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, их уровнях серьёзности и логике их создания.").
* Выберите **Affected entities** на основе их тегов. Подробнее о тегах см. [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.").

  + **Include all entities**
  + **Include entities with all defined tags below**
  + **Include entities with any defined tag below**
* Определите **Additional custom filter query**, добавив любое выражение [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Рассмотрите конкретные функции DQL и логические операторы для обработки логов.") к приведённому выше определению.

## Davis event trigger

События Davis создаются [Dynatrace Intelligence](/docs/dynatrace-intelligence/root-cause-analysis "Как Dynatrace анализирует проблемы для определения их первопричины.") на основе данных мониторинга. **Davis event trigger** позволяет избирательно запускать рабочий процесс в ответ на них.

Для определения поведения триггера на события проблем Davis доступны следующие параметры конфигурации:

* **Problem state**

  + **active** -- означает, что событие Davis ещё не закрыто.
  + **active or closed** -- означает, что событие Davis может быть активным или закрытым.
* **Davis event name**

  + **equals** -- совпадение происходит, если имя события Davis точно соответствует строке имени события.
  + **contains** -- совпадение происходит, если имя события Davis содержит строку имени события.
* Выберите **Affected entities** на основе их тегов. Подробнее о тегах см. [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.").

  + **Include all entities**
  + **Include entities with all defined tags below**
  + **Include entities with any defined tag below**
* Определите **Additional custom filter query**, добавив любое выражение [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Рассмотрите конкретные функции DQL и логические операторы для обработки логов.") к приведённому выше определению.

## Разрешения

Актор рабочего процесса с триггером событий должен иметь доступ к событию, поэтому необходимо предоставить следующие разрешения.

* [storage:events:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-events-read "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") -- для общего триггера событий типа events, а также триггеров Davis problem и Davis event
* [storage:security.events:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-security-events-read "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") -- для триггера событий типа security.events
* [storage:bizevents:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-bizevents-read "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") -- для общего триггера событий типа bizevents
* [storage:system:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-system-read "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") -- для общего триггера событий типа dt.system.events
* [storage:buckets:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-buckets-read "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.") -- рекомендуется ограничить разрешение только бакетом, относящимся к данному событию

Эти разрешения должны быть предоставлены для любого типа пользователя, выбранного в качестве актора. В случае интерактивного пользователя (несистемного пользователя) убедитесь, что эти разрешения также выбраны в настройках авторизации этим пользователем. Подробнее см. (документацию по разрешениям для Workflows](workflows-security).

## Ограничения

Поскольку триггеры событий могут срабатывать часто, каждый рабочий процесс ограничен максимум 1 000 срабатываниями триггеров событий в час на один рабочий процесс.

* Если триггер событий превышает этот лимит, дальнейшие срабатывания триггеров событий для этого рабочего процесса не будут выполняться в течение часа.
* Если триггер событий достигает лимита три раза в течение семи дней, триггер событий отключается.

В обоих случаях превышение лимита отмечается в обзоре Workflows и доступно для фильтрации.

Для устранения этой ситуации рекомендуется скорректировать конфигурацию триггера событий и повторно включить триггер.

## Рекомендации по работе с рабочими процессами и триггерами событий

* Для доступа к полезной нагрузке события и параметризации задач в рабочем процессе используйте [выражение](/docs/analyze-explore-automate/workflows/reference#event "Ознакомьтесь с выражениями рабочих процессов") `event()`.
* Для триггера событий Workflows предложит контекст события последнего успешного выполнения при ручном запуске рабочего процесса. Prompt Workflows позволяет настроить контекст события для ручных запусков во время итераций разработки рабочего процесса.
* С помощью функции **Query past events** в определении триггера событий можно быстро увидеть, сколько совпадающих событий было зафиксировано в вашей среде ранее.
* Используйте [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь данными наблюдаемости в едином совместном настраиваемом рабочем пространстве.") для изучения событий в вашей среде и определения событий, которые вы хотите использовать.
* Учтите, что выражения фильтров событий поддерживают только синтаксис [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Рассмотрите конкретные функции DQL и логические операторы для обработки логов."), который является подмножеством DQL.
