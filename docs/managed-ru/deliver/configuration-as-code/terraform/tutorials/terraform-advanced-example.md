---
title: Расширенный пример Terraform
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example
scraped: 2026-05-12T11:21:32.505428
---

# Terraform advanced example

# Terraform advanced example

* Tutorial
* 3-min read
* Updated on Jul 01, 2024

Этот раздел проведёт вас через расширенный пример создания шаблона конфигурации Dynatrace для нового развёртываемого приложения с помощью Dynatrace Configuration as Code через Terraform.

## Предварительные условия

* [Terraform CLI с установленным провайдером Dynatrace](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform."), доступный в `PATH`.
* [Токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") как минимум со следующими разрешениями:

  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)

  Для создания токена, работающего со всеми конфигурациями, также включите следующие разрешения.

  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Создание конфигурации

В этом примере используется JSON-файл с входными данными для автоматизации создания зоны управления, профиля оповещения и email-уведомления для каждого определённого приложения.

1. В рабочей директории создайте файл `main.tf` со следующим содержимым.

   В приведённой конфигурации используется блок `locals` для доступа к содержимому `data.json` внутри блоков `resource`.

   Подробнее о каждом ресурсе см. в документации [Terraform Registry](https://dt-url.net/1ta37uo).

   ```
   locals {



   app_data = jsondecode(file("data.json"))



   }



   resource "dynatrace_management_zone_v2" "mgmz_per_app" {



   for_each = local.app_data



   name = each.key



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type           = "HOST"



   host_to_pgpropagation = true



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "HOST_GROUP_NAME"



   operator       = "EQUALS"



   string_value   = each.value["host-group"]



   }



   }



   }



   }



   }



   }



   resource "dynatrace_alerting" "alerting_per_app" {



   for_each = dynatrace_management_zone_v2.mgmz_per_app



   name            = each.value.name



   management_zone = each.value.legacy_id



   rules {



   rule {



   delay_in_minutes = local.app_data[each.value.name]["delay-in-minutes"]



   include_mode     = "NONE"



   severity_level   = "MONITORING_UNAVAILABLE"



   }



   }



   }



   resource "dynatrace_email_notification" "email_notification_per_app" {



   for_each = dynatrace_alerting.alerting_per_app



   name                   = each.value.name



   subject                = "{State} Problem {ProblemID}: {ImpactedEntity}"



   to                     = local.app_data[each.value.name]["notify"]



   body                   = "{ProblemDetailsHTML}"



   profile                = each.value.id



   active                 = true



   notify_closed_problems = true



   }
   ```
2. Создайте файл `data.json` со следующим содержимым.

   ```
   {



   "App-A": {



   "host-group": "group-a",



   "delay-in-minutes": 20,



   "notify": ["app.a.owner@dynatrace.com"]



   },



   "App-B": {



   "host-group": "group-b",



   "delay-in-minutes": 30,



   "notify": ["app.b.owner@dynatrace.com"]



   }



   }
   ```

   В приведённой JSON-конфигурации определены два приложения: `"App-A"` и `"App-B"`. Эти имена будут использоваться при создании зоны управления, профиля оповещения и email-уведомления. Каждое приложение имеет следующие атрибуты:

   * `host-group`: ссылается на [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#assign-a-host-to-a-host-group "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."), связанную с приложением. Используется для правила зоны управления.
   * `delay-in-minutes`: указывает продолжительность (в минутах), в течение которой событие недоступности мониторинга остаётся открытым перед срабатыванием оповещения. Подробнее см. в разделе [профиль оповещения](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
   * `notify`: список получателей [email-уведомления](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.").
3. Откройте окно терминала и задайте переменные окружения для URL тенанта и токена API. Это тенант, в который будет отправлена конфигурация.

   SaaS

   Managed

   ```
   set DYNATRACE_ENV_URL=https://########.live.dynatrace.com



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

   ```
   set DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```
4. Выполните команду `terraform apply -auto-approve`, которая отображает план выполнения с описанием вносимых изменений.

   ```
   dynatrace_management_zone_v2.mgmz_per_app["App-A"]: Creating...



   dynatrace_management_zone_v2.mgmz_per_app["App-A"]: Creation complete after 1s [id=*************]



   dynatrace_management_zone_v2.mgmz_per_app["App-B"]: Creating...



   dynatrace_management_zone_v2.mgmz_per_app["App-B"]: Creation complete after 0s [id=*************]



   dynatrace_alerting.alerting_per_app["App-B"]: Creating...



   dynatrace_alerting.alerting_per_app["App-B"]: Creation complete after 1s [id=*************]



   dynatrace_alerting.alerting_per_app["App-A"]: Creating...



   dynatrace_alerting.alerting_per_app["App-A"]: Creation complete after 0s [id=*************]



   dynatrace_email_notification.email_notification_per_app["App-B"]: Creating...



   dynatrace_email_notification.email_notification_per_app["App-B"]: Creation complete after 1s [id=*************]



   dynatrace_email_notification.email_notification_per_app["App-A"]: Creating...



   dynatrace_email_notification.email_notification_per_app["App-A"]: Creation complete after 1s [id=*************]



   Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
   ```

После успешного выполнения конфигурации зоны управления, профиля оповещения и email-уведомления для `"App-A"` и `"App-B"` будут созданы в окружении Dynatrace.

Для изменения или удаления конфигурации обратитесь к примерам из раздела [Базовый пример Terraform](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.").

## Связанные темы

* [Утилита экспорта](/managed/deliver/configuration-as-code/terraform/guides/export-utility "Export existing Dynatrace configurations using Dynatrace Configuration as Code via Terraform.")