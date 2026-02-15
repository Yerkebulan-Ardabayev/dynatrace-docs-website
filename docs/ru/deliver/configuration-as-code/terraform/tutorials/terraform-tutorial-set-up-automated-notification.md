---
title: Configure automated notifications using Terraform and Configuration as Code
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/tutorials/terraform-tutorial-set-up-automated-notification
scraped: 2026-02-15T09:07:31.529502
---

# Configure automated notifications using Terraform and Configuration as Code

# Configure automated notifications using Terraform and Configuration as Code

* Latest Dynatrace
* Tutorial
* 2-min read
* Updated on Nov 05, 2025

This tutorial explains how to configure an event notification with the latest Dynatrace.

The notification consists of

* A [custom alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") configuration, which raises an alerting event if a certain conditions is met.
* A simple workflow that automatically sends an email when the alerting event is active.

## Prerequisites

* Terraform CLI with the Dynatrace provider installed and available under PATH.
  For more information, see [Install Terraform CLI and set up Configuration as Code via Terraform](/docs/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.").
* OAuth client or platform token with the following permissions.
  For more information, see [Create API access token](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling#terraform-api-setup "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").

  + View settings objects for schema (`settings:objects:read`)
  + Create settings objects for schema (`settings:objects:write`)
  + View workflows (`automation:workflows:read`)
  + Create and edit workflows (`automation:workflows:write`)

  The Terraform user needs to have all required permissions to run the run automated configurations such as custom alerts or workflows.
  Missing or wrong permission can lead to an unexpected behavior.

## What will you learn

You'll learn how to configure a [custom alert](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.") and a [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") with an email action.

## Steps

### Build Terraform configuration

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

Файл состояния Terraform `terraform.tfstate` генерируется автоматически. Он отслеживает ресурсы, которыми управляет Terraform.
Он имеет решающее значение для последующих операций Terraform.

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