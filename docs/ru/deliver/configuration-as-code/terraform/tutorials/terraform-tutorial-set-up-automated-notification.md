---
title: Настройка автоматических уведомлений с помощью Terraform и Configuration as Code
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/tutorials/terraform-tutorial-set-up-automated-notification
scraped: 2026-03-06T21:28:19.838321
---

* Последняя Dynatrace
* 2 мин. чтения

В этом руководстве объясняется, как настроить уведомление о событиях с помощью последней версии Dynatrace.

Уведомление состоит из:

* Конфигурации пользовательского оповещения, которое создаёт событие оповещения при выполнении определённого условия.
* Простого рабочего процесса, который автоматически отправляет email при активации события оповещения.

## Предварительные требования

* Terraform CLI с установленным провайдером Dynatrace, доступным в PATH.
  Подробнее см. Установка Terraform CLI и настройка Configuration as Code через Terraform.
* OAuth-клиент или платформенный токен со следующими разрешениями.
  Подробнее см. [Создание токена доступа API](../terraform-api-support-access-permission-handling.md#terraform-api-setup "Описание различных вариантов аутентификации API-вызовов Dynatrace провайдером Terraform.").

  + Просмотр объектов настроек для схемы (`settings:objects:read`)
  + Создание объектов настроек для схемы (`settings:objects:write`)
  + Просмотр рабочих процессов (`automation:workflows:read`)
  + Создание и редактирование рабочих процессов (`automation:workflows:write`)

  Пользователь Terraform должен иметь все необходимые разрешения для запуска автоматизированных конфигураций, таких как пользовательские оповещения или рабочие процессы.
  Отсутствующие или неправильные разрешения могут привести к непредвиденному поведению.

## Что вы узнаете

Вы узнаете, как настроить пользовательское оповещение и рабочий процесс с действием отправки email.

## Шаги

### Создание конфигурации Terraform

Для создания конфигурации, описывающей событие и простой рабочий процесс для отправки email при возникновении события:

1. В вашей рабочей директории создайте файл `main.tf` с содержимым для выбранных ресурсов.

   Показать код для создания пользовательского оповещения и рабочего процесса

   ```
   locals {


   event_name = "Authentication Service: High Response Time"


   }


   resource "dynatrace_davis_anomaly_detectors" "Authentication_Service_High_Response_Time" {


   enabled     = true


   source      = "Anomaly Detection"


   title       = "Authentication Service: High Response Time"


   description = "Raises an event if my service response time performance decreases"


   analyzer {


   name = "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer"


   input {


   analyzer_input_field {


   key   = "query"


   value =<<-EOT


   timeseries avg(dt.service.request.response_time), by:{dt.entity.service}


   | fieldsAdd name=entityName(dt.entity.service)


   | filter in(name, "AuthenticationService")


   EOT


   }


   analyzer_input_field {


   key   = "threshold"


   value = "3000000"


   }


   analyzer_input_field {


   key   = "alertCondition"


   value = "ABOVE"


   }


   analyzer_input_field {


   key   = "alertOnMissingData"


   value = "false"


   }


   analyzer_input_field {


   key   = "violatingSamples"


   value = "3"


   }


   analyzer_input_field {


   key   = "slidingWindow"


   value = "30"


   }


   analyzer_input_field {


   key   = "dealertingSamples"


   value = "15"


   }


   }


   }


   event_template {


   properties {


   property {


   key   = "dt.source_entity"


   value = "{dims:dt.entity.service}"


   }


   property {


   key   = "event.type"


   value = "PERFORMANCE_EVENT"


   }


   property {


   key   = "event.description"


   value =<<-EOT


   **Alert description** An anomaly was detected:


   An anomaly was detected on {metricname}. Within the sliding window, {violating_samples} violation samples were detected that were {alert_condition} the threshold of {threshold}.


   EOT


   }


   property {


   key   = "event.name"


   value = local.event_name


   }


   property {


   key   = "dt.owner"


   value = "myTeam"


   }


   }


   }


   execution_settings {


   }


   }


   resource "dynatrace_automation_workflow" "Authentication_Service_Email_Notification" {


   type          = "SIMPLE"


   private       = false


   title         = "Authentication Service: Email Notification"


   tasks {


   task {


   name        = "send_email"


   description = "Send email"


   action      = "dynatrace.email:send-email"


   input       = jsonencode({


   "bcc": [],


   "cc": [


   "otherteam@mycompany.com"


   ],


   "content": "{{event()[\"event.description\"]}}\nAn alert has been raised, impacting the service: \n\nDetails:\nStatus:             {{event()[\"event.status\"]}}\nId:                 {{event()[\"event.id\"]}}\nTime:               {{event()[\"timestamp\"]}}\nCategory:           {{event()[\"event.category\"]}}\nImpacted service:   {{event()[\"dt.entity.service.name\"]}}\nResponsible team:   {{event()[\"dt.owner\"]}},\n",


   "environmentUrl": "{{ environment().url }}",


   "executionId": "{{ execution().id }}",


   "subject": "Dynatrace Alert",


   "taskId": "{{ task().id }}",


   "to": [


   "myteam@mycompany.com"


   ]


   })


   position {


   x = 0


   y = 1


   }


   }


   }


   trigger {


   event {


   active = true


   config {


   davis_event {


   entity_tags_match = "all"


   names {


   name {


   name = local.event_name


   match = "equals"


   }


   }


   }


   }


   }


   }


   }
   ```

   Этот файл содержит конфигурацию Terraform — набор блоков ресурсов, определяющих конфигурацию.

   Если вы хотите попробовать другие ресурсы, рассмотрите использование утилиты экспорта для экспорта существующих конфигураций из вашей выбранной среды.
2. Откройте терминал и установите переменные среды для URL вашей среды и учётных данных аутентификации.
   Переменная среды определяет, на какой тенант вы будете отправлять конфигурации.
   Подробнее см. Обработка поддержки API и разрешений доступа Terraform.
3. В вашей рабочей директории выполните `terraform plan` для генерации плана выполнения, предоставляющего предварительный просмотр планируемых Terraform изменений.

   Показать пример предварительного просмотра

   ```
   Terraform used the selected providers to generate the following execution


   plan. Resource actions are indicated with the following symbols:


   + create


   Terraform will perform the following actions:


   # dynatrace_automation_workflow.Authentication_Service_Email_Notification will be created


   + resource "dynatrace_automation_workflow" "Authentication_Service_Email_Notification" {


   + id      = (known after apply)


   + private = false


   + title   = "Authentication Service: Email Notification"


   + type    = "SIMPLE"


   + tasks {


   + task {


   + action      = "dynatrace.email:send-email"


   + active      = true


   + description = "Send email"


   + input       = jsonencode(


   {


   + bcc            = []


   + cc             = [


   + "otherteam@mycompany.com",


   ]


   + content        = <<-EOT


   {{event()["event.description"]}}


   An alert has been raised, impacting the service:


   Details:


   Status:             {{event()["event.status"]}}


   Id:                 {{event()["event.id"]}}


   Time:               {{event()["timestamp"]}}


   Category:           {{event()["event.category"]}}


   Impacted service:   {{event()["dt.entity.service.name"]}}


   Responsible team:   {{event()["dt.owner"]}},


   EOT


   + environmentUrl = "{{ environment().url }}"


   + executionId    = "{{ execution().id }}"


   + subject        = "Dynatrace Alert"


   + taskId         = "{{ task().id }}"


   + to             = [


   + "myteam@mycompany.com",


   ]


   }


   )


   + name        = "send_email"


   # (4 unchanged attributes hidden)


   + position {


   + x = 0


   + y = 1


   }


   }


   }


   + trigger {


   + event {


   + active = true


   + config {


   + davis_event {


   + entity_tags_match = "all"


   + on_problem_close  = false


   + names {


   + name {


   + match = "equals"


   + name  = "Authentication Service: High Response Time"


   }


   }


   }


   }


   }


   }


   }


   # dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time will be created


   + resource "dynatrace_davis_anomaly_detectors" "Authentication_Service_High_Response_Time" {


   + description = "Raises an event if my service response time performance decreases"


   + enabled     = true


   + id          = (known after apply)


   + source      = "Anomaly Detection"


   + title       = "Authentication Service: High Response Time"


   + analyzer {


   + name = "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer"


   + input {


   + analyzer_input_field {


   + key   = "alertCondition"


   + value = "ABOVE"


   }


   + analyzer_input_field {


   + key   = "alertOnMissingData"


   + value = "false"


   }


   + analyzer_input_field {


   + key   = "dealertingSamples"


   + value = "15"


   }


   + analyzer_input_field {


   + key   = "query"


   + value = <<-EOT


   timeseries avg(dt.service.request.response_time), by:{dt.entity.service}


   | fieldsAdd name=entityName(dt.entity.service)


   | filter in(name, "AuthenticationService")


   EOT


   }


   + analyzer_input_field {


   + key   = "slidingWindow"


   + value = "30"


   }


   + analyzer_input_field {


   + key   = "threshold"


   + value = "3000000"


   }


   + analyzer_input_field {


   + key   = "violatingSamples"


   + value = "3"


   }


   }


   }


   + event_template {


   + properties {


   + property {


   + key   = "dt.source_entity"


   + value = "{dims:dt.entity.service}"


   }


   + property {


   + key   = "event.type"


   + value = "PERFORMANCE_EVENT"


   }


   + property {


   + key   = "event.description"


   + value = <<-EOT


   **Alert description** An anomaly was detected:


   An anomaly was detected on {metricname}. Within the sliding window, {violating_samples} violation samples were detected that were {alert_condition} the threshold of {threshold}.


   EOT


   }


   + property {


   + key   = "event.name"


   + value = "Authentication Service: High Response Time"


   }


   + property {


   + key   = "dt.owner"


   + value = "myTeam"


   }


   }


   }


   + execution_settings {}


   }


   Plan: 2 to add, 0 to change, 0 to destroy.
   ```
4. После проверки плана выполните `terraform apply` для реализации предложенных изменений.

   Показать пример завершения

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creating...


   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creating...


   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creation complete after 2s [id=************]


   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creation complete after 5s [id=************]


   Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
   ```

   Файл состояния Terraform `terraform.tfstate` генерируется автоматически. Он отслеживает ресурсы, которыми управляет Terraform.
   Он критически важен для последующих операций Terraform.

### Изменение конфигурации Terraform

Для изменения конфигурации Terraform

1. Выполните `terraform plan`, который должен указать, что изменения не требуются.

   Показать лог выполнения

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]


   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]


   No changes. Your infrastructure matches the configuration.


   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. Для внесения изменений отредактируйте файл `main.tf`. Например, вы можете изменить получателя email-уведомления, изменив атрибут `to` в ресурсе `dynatrace_davis_anomaly_detectors`.
3. После внесения изменений выполните `terraform apply`, который обновит конфигурацию в Dynatrace и соответственно скорректирует файл состояния Terraform.

   Показать пример предварительного просмотра

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifying... [id=************]


   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifications complete after 3s [id=************]


   Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
   ```

### Удаление конфигурации

1. Для удаления конфигурации выполните `terraform plan`, чтобы убедиться в отсутствии ожидающих изменений.

   Показать лог выполнения

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]


   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]


   No changes. Your infrastructure matches the configuration.


   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. Для окончательного удаления выбранной конфигурации выполните `terraform destroy`.

   Показать лог выполнения

   ```
   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destroying... [id= ************]


   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destroying... [id= ************]


   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destruction complete after 0s


   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destruction complete after 1s


   Destroy complete! Resources: 2 destroyed.
   ```

   Ранее созданные конфигурации в среде Dynatrace были удалены. Убедитесь, что ваш файл состояния `terraform.tfstate` пуст.