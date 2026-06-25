---
title: Миграция конфигурации с Monaco 1.x на 2.x
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2
scraped: 2026-05-12T12:02:54.560771
---

# Migrate configuration from Monaco 1.x to 2.x

# Migrate configuration from Monaco 1.x to 2.x

* How-to guide
* 9-min read
* Updated on May 08, 2023

Последняя версия Monaco, поддерживающая команду `convert`, — Monaco версии `2.19.0`.
Для преобразования проекта по инструкциям на этой странице загрузите и используйте эту версию.

Если вы используете Dynatrace Configuration as Code через Monaco (Dynatrace Monaco CLI) версии 1.x, данный раздел поможет мигрировать на версию 2.x.

## Предварительные условия

* Dynatrace Monaco CLI версии 2.0.0 – Monaco CLI 2.19.0, установленная (см. [Установка Dynatrace Configuration as Code через Monaco](/managed/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.")) и доступная в вашем `PATH`.
* Существующий проект Dynatrace Monaco CLI версии 1.x.
* Окружение Dynatrace и разрешение на создание токенов доступа.
* Существующий или новый токен доступа Dynatrace с необходимыми правами для конфигурации Dynatrace Monaco CLI 1.x.
  Подробнее о создании токенов доступа см. [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
* Если ваш проект Dynatrace Monaco CLI 1.x ещё использует устаревшие типы конфигурации, мигрируйте их до преобразования: [Миграция устаревших типов конфигурации](/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration "Migrate deprecated 1.x configuration types.")

### Образец проекта

Данное руководство поможет преобразовать ваши существующие проекты.

Для иллюстрации команд используется проект из образцов в [репозитории GitHub](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples).

Для точного выполнения команд руководства клонируйте или загрузите репозиторий и перейдите в папку `observability_clinic_sample`.

## Преобразование проекта

Миграция существующих проектов Monaco 1.x выполняется простым запуском команды `convert`.

В данном примере предполагается, что существующая конфигурация находится в папке `existing_v1_config`.

Содержимое этой папки выглядит следующим образом:

```
existing_v1_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



├── synthetic-monitor/



└── environments.yaml
```

Напомним, как это работает в Monaco 1.x: папка содержит:

* Папку проекта `project`
* Папка `project` содержит папки конфигурации для `application-web`, `auto-tag`, `slo` и `synthetic-monitor`.

  + Каждая из этих папок конфигурации содержит YAML-файл конфигурации и один или несколько JSON-шаблонов.
* Файл `environments.yaml` определяет окружения, в которые развёртывается данный проект конфигурации.

Linux/macOS

Windows

1. Откройте предпочитаемый терминал.
2. Перейдите в директорию выше папки конфигурации `/existing_v1_config`.
3. Выполните `monaco convert`, указав `environments.yaml` и папку `existing_v1_config`.

   ```
   monaco convert existing_v1_config/environments.yaml existing_v1_config -o converted_config
   ```

   Флаг `-o` позволяет задать имя папки с преобразованным результатом.
4. Изучите `converted_config`, созданную Monaco.

   ```
   ls existing_v1_config-v2
   ```

   Она должна выглядеть следующим образом:

   ```
   converted_config/



   ├── project/



   ├── application-web/



   ├── auto-tag/



   ├── slo/



   ├── synthetic-monitor/



   └── manifest.yaml
   ```

1. Откройте Windows PowerShell.
2. Перейдите в директорию выше папки конфигурации `/existing_v1_config`.
3. Выполните `monaco convert`, указав `environments.yaml` и папку `existing_v1_config`.

   ```
   monaco convert existing_v1_config/environments.yaml existing_v1_config -o converted_config
   ```

   Флаг `-o` позволяет задать имя папки с преобразованным результатом.
4. Изучите `converted_config`, созданную Monaco.

   ```
   dir existing_v1_config-v2
   ```

   Она должна выглядеть следующим образом:

   ```
   converted_config/



   ├── project/



   ├── application-web/



   ├── auto-tag/



   ├── slo/



   ├── synthetic-monitor/



   └── manifest.yaml
   ```

## Различия между версиями 1.x и 2.x

Основные видимые различия между версиями 1.x и 2.x — введение структурированной конфигурации.

Рассмотрим, как изменился проект, подробнее.

### Папка проекта

На уровне папок файл `environments.yaml` заменяется на `manifest.yaml`.

Версия 1.x

Версия 2.x

```
existing_v1_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



├── synthetic-monitor/



└── environments.yaml
```

```
converted_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



├── synthetic-monitor/



└── manifest.yaml
```

### От `environments.yaml` к `manifest.yaml`

* В версии 1.x проекты определялись как папки в директории, где выполняется CLI; версия 2.x вводит файлы манифеста, которые определяют проекты (*что* развёртывается) и окружения, ранее задававшиеся в файлах окружений (*куда* развёртываются конфигурации).
* Для указания того, что URL загружается из переменной окружения:

  + В версии 1.x используется специальный префикс шаблонизации `.Env.`
  + В версии 2.x используется явный `type`

Подробнее о файлах манифеста см. [Обзор конфигурации Monaco](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").

Версия 1.x

Версия 2.x

```
environment1:



- name: "Sample Environment"



- env-url: {{ .Env.DEMO_ENV_URL }}



- env-token-name: "DEMO_ENV_ACCESS_TOKEN"
```

```
manifestVersion: "1.0"



projects:



- name: project



environmentGroups:



- name: default



environments:



- name: environment1



url:



type: environment



value: DEMO_ENV_URL



auth:



token:



name: DEMO_ENV_ACCESS_TOKEN
```

### Конфигурация

* YAML-файлы конфигурации в версии 2.x существенно изменились по сравнению с простыми списками ключ-значение версии 1.x.
* JSON-шаблоны полезной нагрузки не изменились между версиями 1.x и 2.x.

Версия 1.x

Версия 2.x

```
config:



- slo: "slo.json"



slo:



- name: "My App's Availability SLO"



- metricName: "my_app_synthetic_availability"



- syntheticId: "/project/synthetic-monitor/AppAvailabilityMonitor.id"



- thresholdTarget: "99.98"



- thresholdWarning: "99.99"
```

Обратите внимание, что поле `syntheticId` определяет ссылку на ID synthetic-monitor в строковом формате версии 1.x.

```
configs:



- id: slo



config:



name: My App's Availability SLO



parameters:



metricName: my_app_synthetic_availability



syntheticId:



configId: AppAvailabilityMonitor



configType: synthetic-monitor



property: id



type: reference



thresholdTarget: "99.98"



thresholdWarning: "99.99"



template: slo.json



skip: false



type:



api: slo
```

Как видно, конфигурация `slo` существенно изменилась.

* Теперь есть объект config с ID `slo`, который определяет все параметры и файл JSON-шаблона — вместо исходной пары ID-шаблон `slo:slo.json`, за которой следовали пары ключ-значение с параметрами конфигурации.
* Наиболее значимо то, что поле `syntheticId` теперь является структурированным полем типа `reference`, явно определяющим ID, тип и свойство, на которое оно ссылается.

Обратите внимание, что при преобразовании `project` удалён из ссылки, поскольку он избыточен для ссылок внутри одного проекта.

Преобразование может включать небольшие улучшения входной конфигурации.

Наконец, конфигурация теперь имеет явный `type`. В версии 2.x типы определяются этим значением в YAML-конфигурации и больше не основаны на названии папки файла.

#### Переопределения окружений

Аналогично другим изменениям в конфигурации, версия 2.x делает определение переопределений окружений более явным.

Версия 1.x

Версия 2.x

```
config:



- slo: "slo.json"



slo:



- name: "My App's Availability SLO"



- thresholdTarget: "99"



slo.dev-env:



- name: "My App's Availability SLO - on DEV stage"



- thresholdTarget: "99.999"
```

```
configs:



- id: slo



type:



api: slo



config:



name: My App's Availability SLO



parameters:



thresholdTarget: "99"



template: slo.json



environmentOverrides:



- environment: dev-env



override:



name: My App's Availability SLO - on DEV stage



parameters:



thresholdTarget: "99.999"
```

## Развёртывание преобразованного проекта

Теперь развернём новый преобразованный проект в то же окружение, которым уже управляет Dynatrace Monaco CLI.

Linux/macOS

Windows

1. Экспортируйте токен доступа Dynatrace в окружение.
   Убедитесь, что токен доступа имеет необходимые права для вашей конфигурации (в данном примере — **Write configuration** (`WriteConfig`)).

   ```
   export DEMO_ENV_ACCESS_TOKEN=YourAccessTokenValue
   ```

   Имя переменной окружения совпадает с именем в `environments.yaml` версии 1.x (для данного образца — `DEMO_ENV_ACCESS_TOKEN`).
2. Запустите `monaco deploy --dry-run`, чтобы убедиться в синтаксической корректности и согласованности конфигурации.

   ```
   monaco  deploy --dry-run converted_config/manifest.yaml
   ```
3. При успешном пробном запуске Dynatrace Monaco CLI выводит сообщение следующего вида:

   ```
   2023/02/09 16:57:13 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 16:57:13 INFO  Projects to be deployed:



   2023/02/09 16:57:13 INFO    - project



   2023/02/09 16:57:13 INFO  Environments to deploy to:



   2023/02/09 16:57:13 INFO    - environment1



   2023/02/09 16:57:13 INFO  Validating configurations for environment `environment1`...



   2023/02/09 16:57:13 INFO    Validating config project:application-web:myApp



   2023/02/09 16:57:13 INFO    Validating config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 16:57:13 INFO    Validating config project:slo:slo



   2023/02/09 16:57:13 INFO    Validating config project:auto-tag:application-tagging



   2023/02/09 16:57:13 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 16:57:13 INFO  Validation finished without errors
   ```
4. Используйте `monaco deploy` для развёртывания преобразованной конфигурации.

   ```
   monaco  deploy converted_config/manifest.yaml
   ```
5. При успешном развёртывании Dynatrace Monaco CLI выводит сообщение следующего вида:

   ```
   2023/02/09 17:05:28 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 17:05:28 INFO  Projects to be deployed:



   2023/02/09 17:05:28 INFO    - project



   2023/02/09 17:05:28 INFO  Environments to deploy to:



   2023/02/09 17:05:28 INFO    - environment1



   2023/02/09 17:05:28 INFO  Deploying configurations to environment `environment1`...



   2023/02/09 17:05:28 INFO    Deploying config project:application-web:myApp



   2023/02/09 17:05:29 INFO    Deploying config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 17:05:30 INFO    Deploying config project:slo:slo



   2023/02/09 17:05:30 INFO    Deploying config project:auto-tag:application-tagging



   2023/02/09 17:05:30 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 17:05:31 INFO  Deployment finished without errors
   ```
6. Открыв окружение Dynatrace в браузере, вы найдёте конфигурацию в прежнем виде.

Вы готовы расширять существующие конфигурации с помощью Dynatrace Configuration as Code через Monaco 2.x.

1. Экспортируйте токен доступа Dynatrace в окружение.
   Убедитесь, что токен доступа имеет необходимые права для вашей конфигурации (в данном примере — **Write configuration** (`WriteConfig`)).

   ```
   $env:DEMO_ENV_ACCESS_TOKEN="YourTokenValue"
   ```

   Имя переменной окружения совпадает с именем в `environments.yaml` версии 1.x (для данного образца — `DEMO_ENV_ACCESS_TOKEN`).
2. Запустите `monaco deploy --dry-run`, чтобы убедиться в синтаксической корректности и согласованности конфигурации.

   ```
   monaco  deploy --dry-run converted_config/manifest.yaml
   ```
3. При успешном пробном запуске Dynatrace Monaco CLI выводит сообщение следующего вида:

   ```
   2023/02/09 16:57:13 INFO  Dynatrace Configuration as Code v2.0.0



   ...



   2023/02/09 16:57:13 INFO  Validation finished without errors
   ```
4. Используйте `monaco deploy` для развёртывания преобразованной конфигурации.

   ```
   monaco  deploy converted_config/manifest.yaml
   ```
5. При успешном развёртывании Dynatrace Monaco CLI выводит сообщение следующего вида:

   ```
   2023/02/09 17:05:28 INFO  Dynatrace Configuration as Code v2.0.0



   ...



   2023/02/09 17:05:31 INFO  Deployment finished without errors
   ```
6. Открыв окружение Dynatrace в браузере, вы найдёте конфигурацию в прежнем виде.

Вы готовы расширять существующие конфигурации с помощью Dynatrace Monaco CLI 2.x.

## Связанные темы

* [Миграция устаревших типов конфигурации](/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration "Migrate deprecated 1.x configuration types.")