---
title: Управление конфигурациями с Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-getting-started
scraped: 2026-03-02T21:28:22.074262
---

# Управление конфигурациями с помощью Monaco


* Latest Dynatrace
* Explanation
* 6-min read

Чтобы помочь вам начать работу с управлением конфигурациями, в этом разделе приведён простой пример использования Monaco для создания, развёртывания и удаления конфигурации.

## Предварительные требования

* [Установите Monaco](installation.md "Download and install Dynatrace Configuration as Code via Monaco.") и сделайте исполняемый файл доступным в переменной окружения `PATH`.
* Создайте [платформенный токен или OAuth-клиент](monaco-api-support-and-access-handling.md "This is a list of the Monaco API support and access permission handling.") с соответствующими правами доступа.
  Необходимые права зависят от того, какие API вы используете.

  Для получения дополнительной информации см. документацию по API или [справочник по IAM-политикам](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

В этом примере мы будем использовать конфигурацию SLO, для которой необходимы следующие разрешения:

* `slo:slos:read`
* `slo:slos:write`
* `slo:objective-templates:read`

## Создание новой конфигурации с помощью Monaco

Чтобы создать новую конфигурацию Dynatrace, выполните приведённые ниже шаги.

1. Настройте каталог проекта.
   Выполните следующие команды.

   ```
   mkdir -p monaco-getting-started/project-example/slo


   cd monaco-getting-started/project-example/slo
   ```
2. Создайте два файла.
   Выполните следующие команды.

   ```
   # Linux


   touch slo.json slo.yaml


   # Windows


   New-Item slo.json


   New-Item slo.yaml
   ```
3. Заполните файл `slo.json`.
   Откройте JSON-файл конфигурации в текстовом редакторе и вставьте содержимое приведённого ниже блока кода.
   Сохраните файл.

   ```
   {


   "name": "{{ .name }}",


   "description": "Measures the proportion of successful service requests over time.",


   "tags": {{ .tags }},


   "criteria": [


   {


   "target": 95,


   "timeframeFrom": "now-7d",


   "timeframeTo": "now"


   }


   ],


   "customSli": {


   "filterSegments": [],


   "indicator": "timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }\n  , by: { dt.entity.service }\n  | fieldsAdd sli=(((total[]-failures[])/total[])*(100))\n | fieldsRemove total, failures"


   }


   }
   ```

   Имя и теги, используемые в этой конфигурации, задаются в виде переменных.
   Их значения будут указаны в YAML-файле конфигурации.
4. Заполните файл `slo.yaml`.
   Откройте YAML-файл конфигурации в текстовом редакторе и вставьте содержимое приведённого ниже блока кода.
   Сохраните файл.

   ```
   configs:


   - id: my-sample-slo


   config:


   name: mySampleSLO


   parameters:


   tags:


   type: list


   values: ["service:myService",


   "dt.owner:myTeam"]


   template: slo.json


   skip: false


   type: slo-v2
   ```

   Значения `name` и `tags` будут подставлены в соответствующие заполнители в файле `slo.json`.
5. Создайте манифест развёртывания в каталоге конфигурации.
   Выполните следующие команды.

   ```
   # Linux


   cd ../..


   touch manifest.yaml


   # Windows


   cd ../..


   New-Item manifest.yaml
   ```
6. Заполните файл `manifest.yaml`.
   Откройте YAML-файл конфигурации в текстовом редакторе и вставьте содержимое приведённого ниже блока кода.
   Сохраните файл.

   ```
   manifestVersion: 1.0


   projects:


   - name: my-slo-project


   path: project-example


   environmentGroups:


   - name: development


   environments:


   - name: development-environment


   url:


   type: environment


   value: DT_ENV_URL


   auth:


   platformToken:


   type: environment


   name: PLATFORM_TOKEN
   ```
7. Укажите следующие переменные окружения.
   Выполните приведённые ниже команды.

   ```
   # Linux


   export DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"


   export PLATFORM_TOKEN="YourPlatformTokenValue"


   # Windows


   $env:DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"


   $env:PLATFORM_TOKEN="YourTokenValue"
   ```
8. Запустите Monaco, чтобы проверить синтаксическую корректность и согласованность конфигурации.

   ```
   monaco deploy --dry-run manifest.yaml
   ```

   При успешном выполнении будет выведен результат, аналогичный показанному в блоке кода ниже.

   ```
   time=2025-09-01T09:06:23.506+02:00 level=INFO msg="Monaco version 2.24.0"


   time=2025-09-01T09:06:23.507+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"


   time=2025-09-01T09:06:23.535+02:00 level=INFO msg="Projects to be deployed (1):"


   time=2025-09-01T09:06:23.536+02:00 level=INFO msg="  - my-slo-project"


   time=2025-09-01T09:06:23.536+02:00 level=INFO msg="Environments to deploy to (1):"


   time=2025-09-01T09:06:23.537+02:00 level=INFO msg="  - development-environment"


   time=2025-09-01T09:06:23.537+02:00 level=INFO msg="Deploying configurations to environment \"development-environment\"..." environment.name=default environment.group=group


   time=2025-09-01T09:06:23.556+02:00 level=INFO msg="Deploying config" deploymentStatus=deploying environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0


   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Deployment successful" deploymentStatus=deployed environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0


   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Deployment successful for environment 'development-environment'" environment.group=group environment.name=development-environment environment.name=development-environment environment.group=group


   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Validation finished without errors"
   ```

Теперь вы создали корректные файлы конфигурации Dynatrace для использования с Dynatrace Monaco CLI.

## Развёртывание новой конфигурации с помощью Monaco

Теперь, когда вы создали конфигурацию, её необходимо развернуть в вашем окружении Dynatrace.

Примените вашу конфигурацию, указав имя файла развёртывания в качестве аргумента.
Выполните следующую команду.

```
monaco deploy manifest.yaml
```

При успешном развёртывании будет выведен результат, аналогичный показанному в блоке кода ниже.

```
time=2025-09-01T09:08:23.506+02:00 level=INFO msg="Monaco version 2.24.0"


time=2025-09-01T09:08:23.507+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"


time=2025-09-01T09:08:23.535+02:00 level=INFO msg="Projects to be deployed (1):"


time=2025-09-01T09:08:23.536+02:00 level=INFO msg="  - my-slo-project"


time=2025-09-01T09:08:23.536+02:00 level=INFO msg="Environments to deploy to (1):"


time=2025-09-01T09:08:23.537+02:00 level=INFO msg="  - development-environment"


time=2025-09-01T09:08:23.537+02:00 level=INFO msg="Deploying configurations to environment \"development-environment\"..." environment.name=default environment.group=group


time=2025-09-01T09:08:23.556+02:00 level=INFO msg="Deploying config" deploymentStatus=deploying environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0


time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment successful" deploymentStatus=deployed environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0


time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment successful for environment 'development-environment'" environment.group=group environment.name=development-environment environment.name=development-environment environment.group=group


time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment finished without errors"
```

Если развёртывание конфигурации завершилось с ошибкой, обратитесь к описанию ошибки в выводе.
В ваших файлах могут быть синтаксические ошибки, или платформенному токену могут потребоваться дополнительные разрешения.

Чтобы убедиться, что ваша конфигурация Dynatrace была создана в вашем окружении Dynatrace:

1. Войдите в ваше окружение Dynatrace.
2. Перейдите в **Settings** > **Analyze and alert** > **Site reliability** > **Service-level objectives (SLOs)**.
3. Выполните поиск по запросу `mySampleSLO`.

## Удаление конфигурации с помощью Monaco

Теперь, когда ваша конфигурация развёрнута, вы можете удалить её из локальной файловой системы.

1. Чтобы удалить ранее созданный SLO, создайте файл удаления.
   Выполните следующую команду.

   ```
   # Linux


   touch delete.yaml


   # Windows


   New-Item delete.yaml
   ```
2. Откройте файл в текстовом редакторе и вставьте следующую конфигурацию.
   Сохраните файл.

   ```
   delete:


   - project: my-slo-project


   type: slo-v2


   id: my-sample-slo
   ```
3. Запустите Monaco для удаления конфигурации, указав файл удаления и манифест.
   Это определяет, в каких окружениях конфигурация должна быть удалена.
   Выполните следующую команду.

   ```
   monaco delete --manifest manifest.yaml --file delete.yaml -e development-environment
   ```

   При успешном удалении будет выведен результат, аналогичный показанному в блоке кода ниже.

   ```
   time=2025-09-01T09:10:23.506+02:00 level=INFO msg="Monaco version 2.24.0"


   time=2025-09-01T09:10:23.751+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"


   time=2025-09-01T09:11:24.140+02:00 level=INFO msg="Deleting configs for environment \"development-environment\"..." environment.name=development-environment environment.group=group


   time=2025-09-01T09:11:24.140+02:00 level=INFO msg="Deleting 1 config(s) of type \"slo-v2\"..." type=slo-v2 environment.name=development-environment environment.group=group
   ```

Убедитесь, что ваша конфигурация Dynatrace была удалена из вашего окружения Dynatrace.

1. Войдите в ваше окружение Dynatrace.
2. Перейдите в **Settings** > **Analyze and alert** > **Site reliability** > **Service-level objectives (SLOs)**.
3. Выполните поиск по запросу `mySampleSLO`.

## Связанные темы

* [Установка Dynatrace Configuration as Code via Monaco](installation.md "Download and install Dynatrace Configuration as Code via Monaco.")
* [Поддержка API и управление правами доступа в Monaco](monaco-api-support-and-access-handling.md "This is a list of the Monaco API support and access permission handling.")
