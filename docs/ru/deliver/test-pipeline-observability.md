---
title: Наблюдаемость конвейера тестирования
source: https://www.dynatrace.com/docs/deliver/test-pipeline-observability
scraped: 2026-03-06T21:27:43.528580
---

# Наблюдаемость тестовых пайплайнов


* Latest Dynatrace
* Руководство
* Чтение: 9 мин
* Обновлено 7 октября 2024 г.

Это руководство описывает простой метод использования Dynatrace для эффективного наблюдения и анализа тестовых пайплайнов. Ориентированное как на технических, так и на нетехнических специалистов, руководство фокусируется на эффективном мониторинге тестовых процессов, позволяя командам сосредоточиться на критически важных аспектах процесса тестирования.

Благодаря инструментам наблюдаемости Dynatrace избыточные данные минимизируются, что позволяет сфокусироваться на релевантных и значимых тестовых событиях. Этот подход помогает упростить рабочий процесс тестирования, делая его более рациональным и целенаправленным. Узнайте, как Dynatrace может помочь вам получить более чёткое представление о ваших тестовых пайплайнах, повысив общую эффективность и продуктивность.

## Целевая аудитория

Эта статья в первую очередь предназначена для команд разработки, DevOps-инженеров и специалистов по обеспечению качества (QA), которые занимаются управлением и мониторингом тестовых пайплайнов.

Идеальные читатели — это те, кто знаком с базовыми процессами тестирования и имеет общее понимание практик разработки программного обеспечения. Глубокие знания Dynatrace не требуются, но базовое понимание инструментов наблюдаемости будет полезным.

Это руководство призвано помочь тем, кто отвечает за обеспечение эффективности и результативности процедур тестирования в своих организациях, особенно тем, кто стремится расширить свои возможности мониторинга и получить более содержательные данные из своих тестовых пайплайнов.

## Сценарий

В быстро развивающейся среде разработки программного обеспечения команда разработчиков и QA-инженеров сталкивается с проблемой эффективного управления и мониторинга тестовых пайплайнов. Их текущая настройка включает множество инструментов и фреймворков тестирования и пайплайнов, что приводит к фрагментации данных и затрудняет получение комплексного представления о жизненном цикле тестирования. Эта фрагментация препятствует быстрому выявлению и устранению проваленных тестов, что влияет на общую эффективность процесса разработки.

Команда ищет решение, которое позволит централизовать данные, связанные с тестированием, обеспечивая чёткий обзор всего тестового пайплайна. Они хотят получать уведомления только о значительных сбоях тестов или аномалиях, снижая информационный шум от рутинных результатов тестирования. Идеальное решение автоматически уведомляло бы ответственных членов команды о проваленных тестах, предлагая информацию о возможных причинах и рекомендуемых действиях по исправлению. Кроме того, они стремятся минимизировать ручной мониторинг тестовых пайплайнов, позволяя разработчикам и QA-инженерам больше сосредоточиться на устранении критических проблем, а не на просмотре тестовых данных.

Внедрив решение Test Pipeline Observability от Dynatrace, команда может достичь этих целей. Этот подход позволит получать данные и метаданные о выполнении тестов из различных инструментов на централизованной платформе. С помощью аналитики Dynatrace они могут настраивать дашборды для мониторинга в реальном времени и автоматизировать обнаружение аномалий в тестах. Решение обеспечит чёткую видимость результатов тестирования, тенденций и потенциальных проблем, повышая способность команды поддерживать высококачественные релизы программного обеспечения.

## Предварительные требования

Убедитесь, что все следующие условия выполнены, прежде чем начать:

### Доступ и разрешения

* У вас должны быть необходимые разрешения для настройки и доступа к инструментам мониторинга в Dynatrace.
* У вас должен быть доступ к данным выполнения тестов из различных инструментов тестирования для загрузки в Dynatrace.
* Вы можете интегрировать Dynatrace с различными инструментами и фреймворками тестирования, используемыми в вашем пайплайне.

### Знания

* Вы понимаете, как работает Dynatrace.
* Вы знаете, как настроить [дашборды Dynatrace](../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") и системы оповещения.
* Вы знаете, как загружать события и метаданные, связанные с тестированием, в Dynatrace, в частности используя Dynatrace API или аналогичные методы загрузки данных.
* Вы знаете, как настроить автоматизированные [рабочие процессы](../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflows—react to events, schedule tasks, and connect services.") в Dynatrace для автоматизации реагирования на события тестового пайплайна.
* Вы имеете базовое понимание процессов тестирования программного обеспечения и типичной структуры тестовых пайплайнов в среде разработки.
* Вы обладаете знаниями о сетевой безопасности и защите данных для обеспечения безопасной передачи и хранения данных в среде Dynatrace.

## Шаги

Предупреждение

Следующие шаги используют бизнес-события для реализации сценария наблюдаемости тестового пайплайна. Этот подход пока актуален, но мы планируем новый тип событий для событий, происходящих в жизненном цикле разработки программного компонента. Этот новый тип событий заменит бизнес-события в будущем.

1. Сбор и загрузка данных о выполнении тестов

   На основе ваших исходных инструментов и фреймворков тестовых пайплайнов соберите данные о выполнении тестов. Загрузите эти данные как бизнес-события в Dynatrace с помощью [Business events API](../observe/business-observability/bo-api-ingest.md "Set up authentication for and ingest business events via API."). Например, вы можете написать вспомогательные функции или отправлять запросы напрямую в Business events API.

   Показать пример кода

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

   Данные, отправляемые в событиях, зависят от вашей конкретной цели. Вы можете отправлять результаты каждого выполнения теста как бизнес-событие, добавляя критически важную информацию в полезную нагрузку. Таким образом, вы сможете запускать рабочие процессы, а Grail будет хранить все важные результаты выполнения тестов для запросов через DQL для ad-hoc анализа в Notebooks или в качестве входных данных для ваших дашбордов.
2. Создание [дашборда](../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")

   Используйте DQL для представления данных с помощью доступных визуализаций.
3. Настройка рабочего процесса

   Рабочий процесс может быть [запущен](../analyze-explore-automate/workflows/trigger.md "Introduction to workflow automation triggers for workflows.") при отправке бизнес-события после выполнения теста. Затем вы можете создавать последующие действия на основе загруженных данных тестирования. Например, вы можете определить владельцев неисправного ресурса с помощью действия [Ownership](ownership-app.md "It provides custom actions to define workflows integrating entity owners and their contact information."), а затем уведомить владельцев тестов о результатах через действие [Slack в рабочих процессах](../analyze-explore-automate/workflows/actions/slack.md "Send messages to Slack Workspaces").

   Вот пример простого рабочего процесса, отправляющего результаты выполнения тестов в канал Slack:

   1. Запуск выполнения по регулярному интервалу с помощью CRON
   2. Запрос данных, загруженных через бизнес-событие, которое вы настроили в начале руководства. Используйте встроенное действие **Execute DQL query**. Приведённый ниже DQL-запрос получает данные из событий `CS_TEST_EXECUTION_EVENT`, выполненных за последние 24 часа. Результаты фильтруются по тестам с тегом `data-quality-checks`.

      ```
      fetch bizevents, from:now() - 24h


      | filter event.type == "CS_TEST_EXECUTION_EVENT"


      | filter contains(test.tags, "data-quality-checks")
      ```
   3. Выполнение пользовательского JavaScript-кода для генерации сообщения, содержащего данные, полученные на предыдущем шаге.

      Показать код

      ```
      // optional import of sdk modules


      import { execution } from '@dynatrace-sdk/automation-utils';


      export default async function () {


      // your code goes here


      // e.g. get the current execution


      const ex = await execution();


      const res = await ex.result("query_biz_events");


      const records = res.records;


      var message = "EXECUTED TESTS:";


      records.forEach((record, index) => {


      if (record["test.execution.result"] == "Success") {


      message += "\n " + "[ Owner: " + record["test.owner.name"] + " ] [ Team: " + record["test.owner.team"] + " ] [ Departement: " + record["test.owner.capability"] + " ]"


      message += "\n * " + record["test.name"] + " [" + record["test.execution.stage"] + "]" + " - :green_heavy_check_mark: *Success*";


      message += "\n * " + "Pipeline URL: " + record["sdlc.pipeline.run.url"];


      }


      });


      return message;


      }
      ```

      Код сгенерирует сообщение, как в примере ниже

      ```
      EXECUTED TESTS:


      [ Owner: john.doe ] [ Team: my-team ] [ Departement: My departement ]


      * runtimeVulnerabilityAnalyticsTest [sprint] - :green_heavy_check_mark: *Success*


      * Pipeline URL: https://yourserver.org/build/52435771
      ```
   4. Используйте действие Slack для отправки сообщения владельцу теста.

      ![Slack action](https://dt-cdn.net/images/slack-736-cf40fdbb69.png)

      Показать шаблон рабочего процесса

      ```
      metadata:


      version: "1"


      dependencies:


      apps:


      - id: dynatrace.automations


      version: ^1.269.0


      - id: dynatrace.slack


      version: ^1.3.6


      inputs:


      - type: connection


      schema: app:dynatrace.slack:connection


      targets:


      - tasks.send_message.connection


      workflow:


      title: E2E Test slack notifications


      tasks:


      send_message:


      name: send_message


      description: Send a message to a Slack workspace


      action: dynatrace.slack:slack-send-message


      input:


      channel: C05UMMXSZ2R


      message: '{{ result("generate_message") }}'


      reaction: []


      connection: ""


      workflowID: "{{ execution().workflow.id }}"


      channelType: id


      executionID: "{{ execution().id }}"


      executionDate: "{{ execution().started_at }}"


      appendToThread: false


      selectedRequestType: 0


      attachmentToggleValue: none


      position:


      x: 0


      y: 3


      predecessors:


      - generate_message


      conditions:


      states:


      generate_message: OK


      generate_message:


      name: generate_message


      description: Build a custom task running js Code


      action: dynatrace.automations:run-javascript


      input:


      script: >-


      // optional import of sdk modules


      import { execution } from '@dynatrace-sdk/automation-utils';


      export default async function () {


      // your code goes here


      // e.g. get the current execution


      const ex = await execution();


      const res = await ex.result("query_biz_events");


      const records = res.records;


      var message = "EXECUTED TESTS:";


      records.forEach((record, index) => {


      if (record["test.execution.result"] == "Success") {


      message += "\n " + "[ Owner: " + record["test.owner.name"] + " ] [ Team: " + record["test.owner.team"] + " ] [ Departement: " + record["test.owner.capability"] + " ]"


      message += "\n * " + record["test.name"] + " [" + record["test.execution.stage"] + "]" + " - :green_heavy_check_mark: *Success*";


      message += "\n * " + "Pipeline URL: " + record["sdlc.pipeline.run.url"];


      }


      });


      return message;


      }


      position:


      x: 0


      y: 2


      predecessors:


      - query_biz_events


      conditions:


      states:


      query_biz_events: OK


      query_biz_events:


      name: query_biz_events


      description: Executes DQL query


      action: dynatrace.automations:execute-dql-query


      input:


      query: |-


      fetch bizevents, from:now() - 24h


      | filter event.type == "CS_TEST_EXECUTION_EVENT"


      | filter contains(test.tags, "data-quality-checks")


      position:


      x: 0


      y: 1


      predecessors: []


      description: ""


      trigger:


      schedule:


      rule: null


      trigger:


      type: cron


      cron: 0 9 * * *


      timezone: Europe/Vienna


      isActive: true


      isFaulty: false


      nextExecution: 2024-02-01T08:00:00.000Z


      filterParameters: {}


      inputs: {}


      schemaVersion: 3
      ```
4. Настройка обнаружения аномалий

   Вы также можете использовать действие [ИИ в рабочих процессах — Прогнозное обслуживание облачных дисков](../dynatrace-intelligence/use-cases/davis-for-workflows.md "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.") в вашем рабочем процессе для обнаружения аномалий в выполнении тестов/сборок, таких как необычно длительное время выполнения по сравнению с историческими данными. Эта информация помогает поддерживать и оптимизировать тестовые среды.
5. Проверка и оптимизация реализации

   После настройки проверьте рабочий процесс, запустив тестовые случаи и проверив дашборд на корректность представления данных. Оптимизируйте настройку на основе первоначальных наблюдений, обеспечивая согласованность и точность данных.
6. Мониторинг и корректировка

   Непрерывно контролируйте систему на предмет производительности и эффективности. Вносите корректировки по мере необходимости на основе обратной связи и меняющихся требований.

Следуя этим шагам, вы можете эффективно реализовать наблюдаемость тестовых пайплайнов Dynatrace для улучшения процессов тестирования, получения ценной информации и повышения общей эффективности.

## Заключение

Внедрение наблюдаемости тестовых пайплайнов с Dynatrace предоставляет практическое решение для улучшения мониторинга тестов. В этом руководстве описаны шаги по сбору и анализу тестовых данных, настройке дашбордов мониторинга и автоматизации реагирования на важные события тестирования. Эти действия помогают сократить ручные усилия при мониторинге тестов и позволяют командам сосредоточиться на критических проблемах, улучшая общий процесс тестирования.

Командам рекомендуется применять эти практики в своих тестовых средах и раскрыть весь потенциал инструментов наблюдаемости Dynatrace. Информация, полученная в результате этого внедрения, может привести к постоянным улучшениям в процессах разработки программного обеспечения. Продолжая использовать Dynatrace и его функции, команды могут обеспечить стабильное качество в своих усилиях по разработке программного обеспечения.