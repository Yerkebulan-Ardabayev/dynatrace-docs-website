---
title: Утилита экспорта
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/guides/export-utility
scraped: 2026-05-12T12:02:50.498896
---

# Export utility

# Export utility

* How-to guide
* 4-min read
* Updated on Jul 01, 2024

Помимо стандартной функциональности Terraform, провайдер может запускаться как автономный исполняемый файл для экспорта существующей конфигурации из окружения Dynatrace. Эта функция является альтернативой ручному созданию конфигурации Terraform и предоставляет простой способ создания шаблонов на основе существующей конфигурации.

## Предварительные условия

* [Terraform CLI с установленным провайдером Dynatrace](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform."), доступный в `PATH`.
* [Токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") как минимум со следующими разрешениями:

  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)
  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Руководство по экспорту

1. Определите URL окружения и токен API в окне терминала. Это идентифицирует тенант Dynatrace для получения конфигурации.

   Windows

   Linux

   ```
   set DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

   ```
   export DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   export DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

При необходимости задайте `DYNATRACE_TARGET_FOLDER` для указания выходной директории. Если не задана, используется директория по умолчанию `./configuration`.

1. В терминале перейдите к исполняемому файлу провайдера Dynatrace Terraform. Это не универсальный исполняемый файл типа `terraform.exe` или `./terraform`. Как правило, он находится в `.terraform/providers/registry.terraform.io/dynatrace-oss/dynatrace/{provider_version}/{os_version}/terraform-provider-dynatrace_x.y.z`.
2. Запустите исполняемый файл напрямую с нужными опциями. Поскольку экспорт — это дополнительная функциональность, прямой вызов плагина допустим; предупреждение можно безопасно игнорировать. Примеры см. в разделе [Примеры использования](#usage-examples) ниже.

   **Windows**: `terraform-provider-dynatrace.exe -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]`

   **Linux**: `./terraform-provider-dynatrace -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]`

### Опции

* `-ref`: включить ресурсы с источниками данных и зависимостями.
* `-migrate`: включить ресурсы с зависимостями, исключая источники данных. Подробнее см. в [Руководстве по миграции](/managed/deliver/configuration-as-code/terraform/guides/migration "Migrate configurations between Dynatrace environments using Dynatrace Configuration as Code via Terraform.").
* `-import-state`: инициализировать модули Terraform и импортировать ресурсы в состояние.
* `-id`: отображать закомментированный ID в файлах ресурсов.
* `-flat`: хранить все ресурсы непосредственно в целевой папке без структуры модулей.
* `-exclude`: исключить указанные ресурсы из экспорта.
* `-list-exclusions`: выводить обзор ресурсов, которые не будут экспортированы без явного указания.

По умолчанию дашборды (`dynatrace_json_dashboard`) и ряд других ресурсов исключаются из экспорта, если не указаны явно. Полный список исключённых ресурсов см. через опцию `-list-exclusions`.

### Примеры использования

Следующие примеры демонстрируют различные варианты использования утилиты экспорта.

* Экспорт всех конфигураций без источников данных/зависимостей:

  ```
  ./terraform-provider-dynatrace -export
  ```
* Экспорт всех конфигураций с источниками данных/зависимостями и закомментированными ID:

  ```
  ./terraform-provider-dynatrace -export -ref -id
  ```
* Экспорт всех конфигураций с зависимостями, включая ресурсы из списка исключений:

  ```
  ./terraform-provider-dynatrace -export -ref * dynatrace_json_dashboard dynatrace_document
  ```
* Экспорт конкретной конфигурации:

  ```
  ./terraform-provider-dynatrace -export dynatrace_json_dashboard dynatrace_document
  ```
* Экспорт конкретных конфигураций с их зависимостями:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_json_dashboard dynatrace_web_application
  ```
* Экспорт конкретных профилей оповещения по их ID:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_alerting=4f5942d4-3450-40a8-818f-c5faeb3563d0 dynatrace_alerting=9c4b75f1-9a64-4b44-a8e4-149154fd5325
  ```
* Экспорт нескольких ресурсов с зависимостями:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_calculated_service_metric dynatrace_alerting=4f5942d4-3450-40a8-818f-c5faeb3563d0
  ```
* Экспорт всех конфигураций с импортом в состояние:

  ```
  ./terraform-provider-dynatrace -export -import-state
  ```
* Экспорт конкретных веб-приложений с импортом в состояние:

  ```
  ./terraform-provider-dynatrace -export -import-state dynatrace_web_application
  ```
* Экспорт всех конфигураций кроме указанных ресурсов:

  ```
  ./terraform-provider-dynatrace -export -ref -exclude dynatrace_calculated_service_metric dynatrace_alerting
  ```

### Дополнительная информация

* Некоторые экспортированные конфигурации могут быть устаревшими или требовать изменений. Такие файлы перемещаются в директорию `.flawed` в выходной папке с комментариями в начале файла, объясняющими причины.
* В некоторых конфигурациях может отсутствовать необходимая информация для `terraform apply` из-за конфиденциальных данных или необходимости дополнительного внимания. Такие файлы перемещаются в `.requires_attention` с пояснениями в начале файла.

  Например, конфиденциальные строки `dynatrace_credentials` недоступны через API.