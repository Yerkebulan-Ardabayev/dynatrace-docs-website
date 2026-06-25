---
title: Миграция конфигураций
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/guides/migration
scraped: 2026-05-12T12:11:52.236013
---

# Migration

# Migration

* How-to guide
* 3-min read
* Updated on Jul 01, 2024

Это руководство описывает как пакетный, так и итеративный методы миграции конфигураций между окружениями Dynatrace с помощью Dynatrace Configuration as Code через Terraform.

Убедитесь, что коммуникация OneAgent перенастроена через `oneagentctl` для выполнения миграции. Прямая миграция OneAgent может сформировать новые идентификаторы сущностей, что потенциально приведёт к потере конфигурации.

**Некорректная миграция может вызвать серьёзные проблемы в окружении**.

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

## Задание переменных окружения

Утилиту экспорта и последующее выполнение Terraform можно запустить двумя способами.

Отдельные переменные для исходного и целевого окружения

Общие переменные для обоих окружений

Раздельное задание переменных для исходного и целевого окружений удобно при итеративном методе, когда в рамках одного сеанса командной строки может выполняться несколько операций экспорта и запусков Terraform.

1. Задайте переменные окружения `DYNATRACE_SOURCE_ENV_URL` и `DYNATRACE_SOURCE_API_TOKEN` как URL и токен API исходного окружения Dynatrace.
2. Задайте переменные окружения `DYNATRACE_ENV_URL` и `DYNATRACE_API_TOKEN` как URL и токен API целевого окружения Dynatrace.

Например (Managed в SaaS на Windows):

```
set DYNATRACE_SOURCE_ENV_URL=https://<dynatrace-host>/e/########



set DYNATRACE_SOURCE_API_TOKEN=dt0c01.########.########



set DYNATRACE_ENV_URL=https://########.live.dynatrace.com



set DYNATRACE_API_TOKEN=dt0c01.########.########
```

При данном методе одни и те же переменные используются для обоих окружений.

Задайте переменные окружения `DYNATRACE_ENV_URL` и `DYNATRACE_API_TOKEN` как URL и токен API — одни и те же переменные используются для исходного и целевого окружений Dynatrace. Изменяйте значения между запуском утилиты экспорта и выполнением Terraform.

При необходимости задайте переменную окружения `DYNATRACE_TARGET_FOLDER` для указания выходной директории. Если переменная не задана, используется директория по умолчанию `./configuration`.

## Методы миграции

Существует два основных подхода к миграции:

* [Пакетный](#bulk) — перенос всех конфигураций из исходного в новое целевое окружение.
* [Итеративный](#iterative) — перенос конфигураций по группам ресурсов. Подходит для целевых окружений с уже существующими конфигурациями.

  Для итеративной миграции используйте таблицу [Terraform Migration Helper](https://dt-url.net/m5i37ar). Она помогает отслеживать порядок и завершённость миграции.

### Пакетная миграция

Убедитесь, что в целевом окружении отсутствуют какие-либо конфигурации.

Используйте флаг `-migrate`. Это создаст все необходимые файлы с зависимостями ресурсов и хардкоднутыми идентификаторами сущностей.

**Windows**: `terraform-provider-dynatrace.exe -export -migrate`

**Linux**: `terraform-provider-dynatrace -export -migrate`

Чтобы просмотреть ресурсы, исключённые из экспорта по умолчанию, запустите провайдер с флагом `-list-exclusions`. Для экспорта исключённых ресурсов см. [Примеры использования](/managed/deliver/configuration-as-code/terraform/guides/export-utility#usage-examples "Export existing Dynatrace configurations using Dynatrace Configuration as Code via Terraform.").

### Итеративная миграция

Итеративный подход подходит для миграции конкретных групп ресурсов или в окружения с существующими конфигурациями.

Задайте переменные окружения для обработки дублирующихся конфигураций:

* `DYNATRACE_DUPLICATE_REJECT=ALL`: запрещает перезапись существующих конфигураций.
* `DYNATRACE_DUPLICATE_HIJACK=ALL`: разрешает перезапись существующих конфигураций.

Используйте флаг `-migrate -datasources`. Это создаст все необходимые файлы с зависимостями через источники данных и хардкоднутыми идентификаторами сущностей.

**Windows**: `terraform-provider-dynatrace.exe -export -migrate -datasources <resourcename>`

**Linux**: `terraform-provider-dynatrace -export -migrate -datasources <resourcename>`

### Устранение неполадок

В процессе миграции некоторые ресурсы могут завершиться с ошибкой. Типичные причины:

* Часть API-эндпоинтов может отклонять устаревшие конфигурации. Например, вычисляемые метрики сервисов теперь требуют указания зоны управления или условия, помеченного свойством сервиса.
* Некоторые API-эндпоинты проверяют существование идентификаторов сущностей в конфигурации. Если они отсутствуют в целевом окружении, повторно примените конфигурацию после появления нужных сущностей.

При возникновении других ошибок создайте [задачу на GitHub](https://dt-url.net/4bg37q8).