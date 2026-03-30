---
title: Управление конфигурациями с Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-getting-started
scraped: 2026-03-02T21:28:22.074262
---

# Управление конфигурациями с помощью Monaco

## Предварительные требования

* Установите Monaco и добавьте в `PATH`.
* Создайте платформенный токен или OAuth-клиент. Для примера с SLO нужны scopes: `slo:slos:read`, `slo:slos:write`, `slo:objective-templates:read`.

## Создание конфигурации

1. Создайте каталог проекта:

   ```
   mkdir -p monaco-getting-started/project-example/slo
   cd monaco-getting-started/project-example/slo
   ```

2. Создайте файлы `slo.json` и `slo.yaml`.

3. Содержимое `slo.json`:

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

4. Содержимое `slo.yaml`:

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

5. Создайте `manifest.yaml` в корне `monaco-getting-started/`:

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

6. Задайте переменные окружения:

   ```
   # Linux
   export DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"
   export PLATFORM_TOKEN="YourPlatformTokenValue"

   # Windows
   $env:DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"
   $env:PLATFORM_TOKEN="YourTokenValue"
   ```

7. Проверьте конфигурацию:

   ```
   monaco deploy --dry-run manifest.yaml
   ```

## Развёртывание

```
monaco deploy manifest.yaml
```

При ошибке проверьте синтаксис файлов и разрешения токена. После развёртывания найдите SLO в **Settings** > **Analyze and alert** > **Site reliability** > **SLOs**, поиск: `mySampleSLO`.

## Удаление конфигурации

1. Создайте `delete.yaml`:

   ```
   delete:
   - project: my-slo-project
   type: slo-v2
   id: my-sample-slo
   ```

2. Выполните удаление:

   ```
   monaco delete --manifest manifest.yaml --file delete.yaml -e development-environment
   ```

## Связанные темы

* Установка Dynatrace Configuration as Code via Monaco
* Поддержка API и управление правами доступа в Monaco
