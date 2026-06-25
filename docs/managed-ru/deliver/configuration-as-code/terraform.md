---
title: Обзор Configuration as Code через Terraform
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform
scraped: 2026-05-12T11:05:10.610759
---

# Configuration as Code via Terraform overview

# Configuration as Code via Terraform overview

* Explanation
* 2-min read
* Updated on Jul 01, 2024

Dynatrace предоставляет специализированный [провайдер Terraform](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest) для управления окружением мониторинга.

## Обзор Terraform

[Terraform](https://developer.hashicorp.com/terraform) от HashiCorp — широко применяемый инструмент Infrastructure-as-Code (IaC).

Провайдер Dynatrace Terraform — это библиотека, позволяющая использовать синтаксис и функциональность Terraform для создания пользовательских конфигураций (ресурсов), например дашборда Dynatrace, рабочего процесса или пользовательского оповещения.

Кроме того, он предоставляет источники данных, например ID сущности сервиса, обнаруженного Dynatrace.
Провайдер Dynatrace Terraform позволяет получать информацию из этих источников данных в Dynatrace.

## Преимущества использования провайдера Dynatrace Terraform

* Нет ручных правок в production.
* Масштабирование конфигураций по командам и стейджам.
* Синхронизация конфигураций или окружений.
* Воссоздание конфигураций (например, для аварийного восстановления).
* Расширенные возможности Terraform, например циклы.
* Группировка компонентов в модули для повторного использования.
* Подключение команд для создания новых приложений и шаблонизации.

## Шаги

* Для установки Terraform CLI см. [Установка Terraform CLI и настройка Configuration as Code через Terraform](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.").

* Изучите [базовый пример Terraform](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.").
* Изучите [расширенный пример Terraform](/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example "Advanced example of creating a management zone with Dynatrace Configuration as Code via Terraform.").

## Подробнее

Официальная документация Terraform:

* [Документация Terraform](https://developer.hashicorp.com/terraform/docs)
* [Руководства Terraform](https://developer.hashicorp.com/terraform/tutorials)

Дополнительная документация и материалы Dynatrace:

* [Репозиторий GitHub: `terraform-provider-dynatrace`](https://github.com/dynatrace-oss/terraform-provider-dynatrace)
* [Terraform Registry: Dynatrace Terraform Provider](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs)

Getting Started with Dynatrace Terraform