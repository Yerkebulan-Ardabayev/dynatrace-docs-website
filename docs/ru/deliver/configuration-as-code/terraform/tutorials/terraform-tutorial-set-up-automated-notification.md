---
title: Настройка автоматических уведомлений с помощью Terraform и Configuration as Code
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/tutorials/terraform-tutorial-set-up-automated-notification
scraped: 2026-02-16T21:27:45.110164
---

# Настройка автоматических уведомлений с помощью Terraform и Configuration as Code

* Latest Dynatrace
* Урок
* 2-минутное чтение
* Обновлено 05 ноября 2025 г.

Этот урок объясняет, как настроить уведомление о событии с помощью последней версии Dynatrace.

Уведомление состоит из

* Настройки [пользовательского оповещения](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.") , которое вызывает событие оповещения, если выполнено определенное условие.
* Простого рабочего процесса, который автоматически отправляет электронное письмо, когда событие оповещения активно.

## Предварительные условия

* Terraform CLI с установленным провайдером Dynatrace и доступным по пути.
  Для получения дополнительной информации см. [Установка Terraform CLI и настройка Configuration as Code через Terraform](/docs/deliver/configuration-as-code/terraform/terraform-cli "Установите Terraform CLI и настройте Configuration as Code Dynatrace через Terraform.").
* Клиент OAuth или платформенный токен с следующими разрешениями.
  Для получения дополнительной информации см. [Создание токена доступа к API](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling#terraform-api-setup "Описывает различные варианты, которые провайдер Terraform может использовать для аутентификации вызовов API Dynatrace.").

  + Просмотр объектов настроек для схемы (`settings:objects:read`)
  + Создание объектов настроек для схемы (`settings:objects:write`)
  + Просмотр рабочих процессов (`automation:workflows:read`)
  + Создание и редактирование рабочих процессов (`automation:workflows:write`)

  Пользователь Terraform должен иметь все необходимые разрешения для запуска автоматических конфигураций, таких как пользовательские оповещения или рабочие процессы.
  Отсутствие или неправильное разрешение может привести к непредвиденному поведению.

## Что вы узнаете

Вы узнаете, как настроить [пользовательское оповещение](/docs/dynatrace-intelligence/anomaly-detection "Как Dynatrace обнаруживает аномалии в вашей среде.") и [рабочий процесс](/docs/analyze-explore-automate/workflows "Автоматизируйте процессы ИТ с помощью рабочих процессов Dynatrace — реагируйте на события, планируйте задачи и подключайте службы.") с действием электронной почты.

## Шаги

### Создание конфигурации Terraform

To build a configuration for raising an event and a simple workflow for sending an email in case of a raised event

1. Inside your working directory, create a `main.tf` file with the content for selected resources.

   Show me the code to build a custom alert configuration and a workflow

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

   This file contains the Terraform configurationâa set of resource blocks that define the configuration.

   If you want to try other resources, consider using the export utility to export existing configurations from your selected environment.
2. Open a terminal and set the environment variables for your environment URL and authentication credentials.
   The environment variable identifies which tenant you'll be pushing configurations to.
   For more information, see [Terraform API support and access permission handling](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").
3. In your working directory, run the `terraform plan` to generate an execution plan that provides a preview of the changes Terraform intends to make.

   Show me preview example

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
4. After verifying the plan, execute `terraform apply` to implement the proposed changes.

   Show me an example of completion

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creating...



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creating...



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creation complete after 2s [id=************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creation complete after 5s [id=************]



   Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
   ```

   A Terraform `terraform.tfstate` state file is automatically generated. It keeps track of the resources that Terraform manages.
   It's crucial for subsequent Terraform operations.



### Modify Terraform configuration

To modify the Terraform configuration

1. Execute the `terraform plan`, which should indicate that no changes are needed.

   Show me the execution log

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To make a change, edit the `main.tf file`. For instance, you can modify the email notification recipient by modifying the `to` attribute in the `dynatrace_davis_anomaly_detectors` resource.
3. After making your changes, execute terraform apply that will update the management zone configuration in Dynatrace and adjust the Terraform state file accordingly.

   Show me preview example

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifying... [id=************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifications complete after 3s [id=************]



   Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
   ```

### Delete your configuration

1. To remove a configuration, run `terraform plan` to confirm no pending changes.

   Show me the execution log

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To permanently delete the selected configuration, execute `terraform destroy`.

   Show me the execution log

   ```
   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destroying... [id= ************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destroying... [id= ************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destruction complete after 0s



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destruction complete after 1s



   Destroy complete! Resources: 2 destroyed.
   ```

   The previously created configurations in the Dynatrace environment have been destroyed. Confirm that your Terraform state `terraform.tfstate` file is empty.