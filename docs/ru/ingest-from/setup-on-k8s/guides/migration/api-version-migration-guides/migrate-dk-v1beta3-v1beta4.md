---
title: Миграция DynaKube v1beta3 на v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4
scraped: 2026-03-05T21:31:57.056358
---

# Миграция DynaKube с v1beta3 на v1beta4


* Latest Dynatrace
* 10-min read

Это руководство покажет, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta3` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta3

**Введено в**: Dynatrace Operator версии 1.3.0

**Устарело в**: Dynatrace Operator версии 1.6.0

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также любые другие поля, которые были изменены

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` устарело.") в `v1beta5` и не должно использоваться.

Рекомендуется следующее:

* Если требуется `autoUpdate: true`, не устанавливайте `image`, `codeModulesImage` или `version`.

  ```
  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack: {} # same as autoUpdate: true


  # ...
  ```
* Если требуется `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`

  ```
  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack:


  image: ... # same effect as autoUpdate: false


  codeModulesImage: # same effect as autoUpdate: false


  # ...


  ---


  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack:


  version: ... # replaces autoUpdate: false


  # ...
  ```
