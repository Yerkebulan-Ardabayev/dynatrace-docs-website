---
title: Установка Terraform CLI и настройка Configuration as Code через Terraform
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/terraform-cli
scraped: 2026-05-12T11:21:31.157280
---

# Install Terraform CLI and set up Configuration as Code via Terraform

# Install Terraform CLI and set up Configuration as Code via Terraform

* How-to guide
* 2-min read
* Updated on Jul 01, 2024

Это руководство описывает установку Terraform CLI и настройку Dynatrace Terraform Provider.

## Установка Terraform CLI

Начните с установки Terraform в вашей системе, следуя [документации Terraform](https://dt-url.net/hd037k2).

1. Скачайте бинарный файл для вашей операционной системы.
2. Добавьте путь в `PATH`, чтобы бинарный файл Terraform был доступен в масштабе всей системы.
3. Проверьте установку, открыв новый сеанс терминала и выполнив следующую команду:

   ```
   terraform version
   ```

## Настройка Dynatrace Terraform Provider

Dynatrace Provider доступен в Terraform Registry и может быть получен автоматически в процессе выполнения `terraform init`.

1. Создайте рабочую директорию для файлов конфигурации Terraform.
2. В этой директории создайте файл `providers.tf`. Используйте приведённый ниже блок конфигурации.

   ```
   terraform {



   required_providers {



   dynatrace = {



   version = "~> 1.0"



   source = "dynatrace-oss/dynatrace"



   }



   }



   }
   ```
3. Перейдите в рабочую директорию в терминале и выполните следующую команду.

   ```
   terraform init
   ```

   Ожидаемый вывод будет выглядеть следующим образом:

   ```
   Initializing the backend...



   Initializing provider plugins...



   - Finding dynatrace-oss/dynatrace versions matching "x.y.z"...



   - Installing dynatrace-oss/dynatrace x.y.z...



   - Installed dynatrace-oss/dynatrace x.y.z (signed by a HashiCorp partner, key ID *************)



   ...



   Terraform has been successfully initialized!
   ```

**Следующий шаг**: [Базовый пример Terraform](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.")