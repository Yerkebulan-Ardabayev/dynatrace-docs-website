---
title: Release validation
source: https://www.dynatrace.com/docs/deliver/quality-gates
scraped: 2026-03-06T21:30:00.295299
---

# Валидация релизов

# Валидация релизов

* Последняя версия Dynatrace
* Руководство
* Чтение: 6 мин
* Опубликовано 01 февраля 2024 г.

Критически важные для бизнеса сервисы требуют тщательной валидации перед развёртыванием в продакшен, поскольку потенциальные сбои негативно влияют на общую производительность.

Гибкость различных инструментов Dynatrace помогает оптимизировать процесс доставки. Основные компоненты:

* [Site Reliability Guardian](site-reliability-guardian.md "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") — приложение Dynatrace, которое автоматизирует валидацию релизов для проверки доступности, производительности, ёмкости и безопасности новой развёрнутой версии сервиса.
* [Workflows](../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") — приложение Dynatrace, в котором последовательность действий собирается в процессы в графическом представлении. Эти рабочие процессы могут автоматически запускаться событиями в Dynatrace — по расписанию или вручную.

## Введение

Ручная валидация релизов — это большая нагрузка, которая снижает пропускную способность вашей команды, замедляет циклы развёртывания и уменьшает потенциальную частоту развёртываний.

Это означает, что между коммитом и продакшеном могут проходить недели, а команды теряют возможность быстро внедрять инновации.

С помощью AutomationEngine и бизнес-событий в Grail вы можете автоматизировать валидацию процесса релиза, ускорить развёртывание и одновременно повысить качество. Поскольку сборка автоматизирована и выполняется только при успешном прохождении всех проверок, это автоматически повышает стандарты качества и помогает избежать исправления ошибок на этапе стабилизации.

## Сценарий

В тестовом пайплайне все тесты безопасности, сквозные и нагрузочные тесты отправляют бизнес-события (Business Events), которые фиксируют результаты тестирования. DQL-запросы выполняются во время продвижения для проверки того, что все необходимые тесты были успешно выполнены, а цели по производительности и безопасности достигнуты.

Кроме того, SLO используются для контроля того, что сервисы не деградируют со временем и по-прежнему соответствуют целевым показателям, установленным командой.

Предупреждение

В приведённых ниже шагах для реализации сценария валидации релизов используются бизнес-события. Этот подход актуален на данный момент, но мы планируем новый тип событий для событий, возникающих в течение жизненного цикла разработки программного компонента. Этот новый тип событий заменит бизнес-события в будущем.

## Шаги

1. Настройте инструмент CI/CD

   Ваш инструмент непрерывной интеграции (CI) или непрерывной доставки (CD), например Jenkins, может [отправлять бизнес-события в Dynatrace](../observe/business-observability/bo-api-ingest.md "Set up authentication for and ingest business events via API."). Эти события затем могут запускать валидации Site Reliability Guardian в рабочем процессе.

   Вы можете создать вспомогательную функцию, как в примере ниже, для вашего пайплайна, чтобы отправлять бизнес-события через API бизнес-событий.

   Показать код

   ```
   #!groovy



   /**



   * Sends biz_event to a given Dynatrace environment.



   * @param monitoringTenant url to monitoring environment



   * @param oauthClientId OAuth client id



   * @param oauthClientSecret OAuth client secret



   * @param payload biz_event payload



   * @return



   */



   def call(



   def monitoringTenant,



   def oauthClientId,



   def oauthClientSecret,



   def payload



   ) {



   // Get Access Token via OAuth - see https://developer.dynatrace.com/develop/access-platform-apis-from-outside/ for reference



   def ssoResponse = sh(script: """



   set +x



   curl --location --request POST 'https://sso.dynatrace.com/sso/oauth2/token' \\



   --header 'Content-Type: application/x-www-form-urlencoded' \\



   --data-urlencode 'grant_type=client_credentials' \\



   --data-urlencode 'client_id=${oauthClientId}' \\



   --data-urlencode 'client_secret=${oauthClientSecret}' \\



   --data-urlencode 'scope=storage:events:write'



   set -x



   """, returnStdout: true).trim()



   // Note: readJSON needs pipeline-utility-steps -> https://www.jenkins.io/doc/pipeline/steps/pipeline-utility-steps/#readjson-read-json-from-files-in-the-workspace



   def ssoResponseJSON = readJSON(text: ssoResponse)



   if (ssoResponseJSON.errorCode) {



   error(message: "Authentication failed: ${ssoResponse}")



   }



   def accessToken = ssoResponseJSON.access_token



   // Ingest BizEvent



   println("Sending BizEvent: ${payload}")



   sh(script: """



   set +x



   curl --location --request POST '${monitoringTenant}/platform/classic/environment-api/v2/bizevents/ingest' \\



   --header 'Content-Type: application/json' \\



   --header 'Authorization: Bearer ${accessToken}' \\



   --data-raw '${payload}'



   set -x



   """)



   }
   ```
2. Отправьте бизнес-событие в Dynatrace

   Если вы хотите фильтровать события валидации Site Reliability Guardian по триггеру-источнику, созданные бизнес-события должны содержать контекстную информацию о версии программного обеспечения, которую вы валидируете. Контекстная информация может передаваться через номер версии, номер сборки, Git-коммит или любой параметр, позволяющий идентифицировать валидируемое программное обеспечение.

   Для передачи контекста выполнения событие, запускающее выполнение рабочего процесса, должно содержать поле `execution_context`, как в примере ниже.

   ```
   {



   "timeframe.to": "2023-03-08T06:29:08.809Z",



   "timeframe.from": "2023-03-08T05:29:08.809Z",



   "event.id": "d08a70d8-f6de-4d0d-bd34-5d416a20ba6a",



   "timestamp": 1678256963078000000,



   "event.kind": "BIZ_EVENT",



   "event.type": "guardian.validation.triggered",



   "stage": "hardening",



   "event.provider": "Jenkins",



   "dt.system.bucket": "default_bizevents_short"



   "execution_context": {



   "buildId": "4711",



   "version": "0.1.0"



   }
   ```

   Контекст выполнения передаётся в бизнес-событие валидации guardian. События `guardian.validation.started`, `guardian.validation.finished` и `guardian.validation.objective` содержат переданное поле `execution_context`.
3. Создайте guardian

   После отправки бизнес-события в Dynatrace, Grail сохранит все связанные данные, и ваш guardian сможет запрашивать результаты, валидировать их по вашим целевым показателям и сохранять результат в Grail.

   Вот пример guardian с набором целевых показателей.

   ![Guardian example](https://dt-cdn.net/images/guardian-1077-6bdb4b505e.webp)

   Подробнее см. в разделе [Create a Site Reliability guardian](site-reliability-guardian/create-srg.md "Create a guardian manually or from a predefined template.").
4. Создайте рабочий процесс

   Теперь, когда все данные на месте, вы можете создать рабочий процесс, который будет валидировать результаты тестов с помощью [действия guardian в рабочем процессе](site-reliability-guardian.md#automation "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.").

   * Рабочий процесс запускается вашим пайплайном, отправляющим бизнес-событие. Для этого необходимо использовать [триггер по событию](../analyze-explore-automate/workflows/trigger.md#event-trigger "Introduction to workflow automation triggers for workflows."). Например, вы можете запустить рабочий процесс с помощью следующего фильтрующего запроса:

     ```
     ((event.type == "guardian.validation.triggered") and stage == "dev")
     ```
   * Создайте следующий шаг рабочего процесса, используя [действие guardian в рабочем процессе](site-reliability-guardian.md#automation "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision."). Действие должно указывать на guardian, созданный ранее. Действие выполнит guardian, и его результаты будут сохранены в Grail, что позволит вашему пайплайну запрашивать данные и решать, следует ли переходить к следующему шагу.

   Показать шаблон

   ```
   metadata:



   version: "1"



   dependencies:



   apps:



   - id: dynatrace.site.reliability.guardian



   version: ^1.8.1



   inputs:



   - type: connection



   schema: app:dynatrace.site.reliability.guardian:guardians



   targets:



   - tmy-object.objectId



   workflow:



   title: Pipeline validation



   tasks:



   trigger:



   name: validation-guardian



   description: Automation action to start a Site Reliability Guardian validation



   action: dynatrace.site.reliability.guardian:validate-guardian-action



   input:



   objectId: ""



   executionId: "{{ execution().id }}"



   expressionTo: '{{ event()["timeframe.to"] }}'



   expressionFrom: '{{ event()["timeframe.from"] }}'



   timeframeSelector:



   to: now



   from: now-2h



   timeframeInputType: expression



   position:



   x: 0



   y: 1



   predecessors: []



   description: ""



   trigger:



   eventTrigger:



   filterQuery: >



   ((event.type == "guardian.validation.triggered") and stage == "dev")



   isActive: true



   uniqueExpression: null



   triggerConfiguration:



   type: event



   value:



   query: >



   ((event.type == "guardian.validation.triggered") and stage == "dev")



   eventType: bizevents



   schemaVersion: 3
   ```
5. Проверьте результаты

   Ваш пайплайн отправил все необходимые данные в Grail и запустил рабочий процесс для выполнения guardian. Результаты guardian теперь готовы к получению и проверке того, готова ли ваша сборка к продвижению. Для этого снова извлекаются данные из бизнес-событий, созданных guardian. Например:

   ```
   query: fetch bizevents, from:now() - 5m, to:now()



   | filter event.type == "guardian.validation.finished"



   | filter event.provider == "dynatrace.site.reliability.guardian"



   | filter guardian.name == "validation-guardian"



   | filter matchesPhrase(execution_context, "1.286.0.0.20240129-160934")



   | sort timestamp desc



   limit 1 ,"timezone": "Europe/Warsaw", "enablePreview": true
   ```
6. Если ваш пайплайн завершился успешно, вы можете запустить ещё один рабочий процесс, отправляющий уведомление члену вашей команды, который может одобрить продвижение. Для этого вы можете использовать один из [коннекторов Workflows](../analyze-explore-automate/workflows/actions.md "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems."), например Slack, Microsoft Teams или Jira.

   Вот пример успешной сборки Jenkins, выполняющей описанные выше тесты.

   ![Jenkins CI](https://dt-cdn.net/images/jenkins-1046-4ceb87222d.png)
