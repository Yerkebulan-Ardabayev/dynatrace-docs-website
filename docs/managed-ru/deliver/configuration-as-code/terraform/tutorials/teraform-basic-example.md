---
title: Базовый пример Terraform
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example
scraped: 2026-05-12T11:21:29.936798
---

# Terraform basic example

# Terraform basic example

* Tutorial
* 4-min read
* Updated on Jul 01, 2024

Для знакомства с управлением конфигурациями этот раздел проведёт вас через простой пример создания зоны управления с помощью Dynatrace Configuration as Code через Terraform. Вы научитесь создавать, обновлять и удалять конфигурацию.

## Предварительные условия

* [Terraform CLI с установленным провайдером Dynatrace](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform."), доступный в `PATH`.
* [Токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") как минимум со следующими разрешениями:

  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)

  Для создания токена, работающего со всеми конфигурациями, также включите следующие разрешения.

  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Создание конфигурации

Создайте зону управления для веб-приложения с помощью Terraform.

1. В рабочей директории создайте файл `main.tf` со следующим содержимым.

   Этот файл содержит конфигурацию Terraform — набор блоков ресурсов, определяющих конфигурацию. Подробнее о ресурсе зоны управления см. в документации [Terraform Registry](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs/resources/management_zone_v2).

   Рассмотрите использование утилиты экспорта для экспорта существующих конфигураций из окружения.

   ```
   resource "dynatrace_management_zone_v2" "TerraformExample" {



   name = "Terraform Example"



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type = "WEB_APPLICATION"



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "WEB_APPLICATION_NAME"



   operator       = "EQUALS"



   string_value   = "easyTravel"



   }



   }



   }



   }



   }



   }
   ```
2. Откройте терминал и задайте переменные окружения для URL вашего окружения и токена API. Это определяет тенант, в который будут отправляться конфигурации.

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
3. В рабочей директории выполните `terraform plan` для формирования плана выполнения, отображающего предварительный просмотр изменений, которые Terraform намеревается внести.

   ```
   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:



   + create



   Terraform will perform the following actions:



   # dynatrace_management_zone_v2.TerraformExample will be created



   + resource "dynatrace_management_zone_v2" "TerraformExample" {



   + id        = (known after apply)



   + legacy_id = (known after apply)



   + name      = "Terraform Example"



   + rules {



   + rule {



   + enabled = true



   + type    = "ME"



   + attribute_rule {



   + entity_type = "WEB_APPLICATION"



   + attribute_conditions {



   + condition {



   + case_sensitive = true



   + key            = "WEB_APPLICATION_NAME"



   + operator       = "EQUALS"



   + string_value   = "easyTravel"



   }



   }



   }



   }



   }



   }



   Plan: 1 to add, 0 to change, 0 to destroy.
   ```
4. После проверки плана выполните `terraform apply` для применения предложенных изменений (в данном случае — отправки конфигурации зоны управления в окружение).

   ```
   dynatrace_management_zone_v2.TerraformExample: Creating...



   dynatrace_management_zone_v2.TerraformExample: Creation complete after 1s [id=*************)]



   Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
   ```

   После выполнения команды `apply` появится файл `terraform.tfstate`. Это файл состояния Terraform, генерируемый автоматически для отслеживания ресурсов, которыми в данный момент управляет Terraform. Он необходим для последующих операций Terraform.

## Изменение конфигурации

1. Выполните `terraform plan` — должно отобразиться, что изменения не требуются.

   ```
   dynatrace_management_zone_v2.easyTravel: Refreshing state... [id=*************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. Для внесения изменения отредактируйте файл `main.tf`. Например, измените значение `string_value` с `"easyTravel"` на `"Terraform"`.

   ```
   resource "dynatrace_management_zone_v2" "TerraformExample" {



   name = "Terraform Example"



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type = "WEB_APPLICATION"



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "WEB_APPLICATION_NAME"



   operator       = "EQUALS"



   string_value   = "Terraform"



   }



   }



   }



   }



   }



   }
   ```
3. После внесения изменений выполните `terraform apply` для обновления конфигурации зоны управления в Dynatrace и соответствующего обновления файла состояния Terraform.

   ```
   dynatrace_management_zone_v2.easyTravel: Modifying... [id=*************]



   dynatrace_management_zone_v2.easyTravel: Modifications complete after 0s [id=*************]



   Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
   ```

## Удаление конфигурации

1. Для удаления конфигурации выполните `terraform plan`, чтобы убедиться в отсутствии ожидающих изменений.

   ```
   dynatrace_management_zone_v2.easyTravel: Refreshing state... [id=*************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. Для удаления зоны управления выполните `terraform destroy`.

   ```
   dynatrace_management_zone_v2.easyTravel: Destroying... [id=*************]



   dynatrace_management_zone_v2.easyTravel: Destruction complete after 0s



   Destroy complete! Resources: 1 destroyed.
   ```

Конфигурация зоны управления в окружении Dynatrace удалена, и файл состояния Terraform теперь пуст.

**Следующий шаг**: [Расширенный пример Terraform](/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example "Advanced example of creating a management zone with Dynatrace Configuration as Code via Terraform.")