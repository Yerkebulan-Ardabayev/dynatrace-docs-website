---
title: Руководство по миграции версий API для DynaKube
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/dynakube
---

# Руководство по миграции версий API для DynaKube

# Руководство по миграции версий API для DynaKube

* Справка
* Чтение 10 мин
* Обновлено 17 апр. 2026 г.

## Обзор

В зависимости от версии Dynatrace Operator поддерживаются разные `apiVersion` для `DynaKube`. На этой странице собраны руководства по миграции для каждой `apiVersion` с учётом версии Operator.

Начиная с версии Dynatrace Operator 1.8.0+, Dynatrace Operator выдаёт предупреждающее событие Kubernetes, если установленная версия DynaKube CRD не соответствует версии, ожидаемой этим релизом Operator.

### Обзор версий API

| Версия API DynaKube | Введена | Устарела | Не обслуживается [1](#fn-1-1-def) | Удалена | Руководства по миграции |
| --- | --- | --- | --- | --- | --- |
| v1beta6 | 1.8.0 |  |  |  |  |
| v1beta5 | 1.6.0 | 1.10.0 |  |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Migrate your v1beta5 DynaKube CR to the v1beta6 apiVersions.") |
| v1beta4 | 1.5.0 | 1.9.0 | 1.10.0 |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Migrate your v1beta4 DynaKube CR to the v1beta6 apiVersions."), [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |
| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.8.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.8.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |

1

Указанная версия Dynatrace Operator больше не обслуживает эту версию API. С её помощью нельзя применять новые ресурсы. Схема сохраняется в CRD только для автоматического преобразования и будет удалена в одном из последующих релизов. Подробнее см. [Процесс удаления](#deprecation).

## Стратегии преобразования

### Автоматическое преобразование

Каждая версия Dynatrace Operator преобразует развёрнутые `DynaKubes` со старой `apiVersion` в последнюю `apiVersion`, поддерживаемую этой версией Dynatrace Operator.

* Пример: Dynatrace Operator v1.6.x всегда преобразует `DynaKubes` в `v1beta5`.

Поэтому при проверке через `kubectl`, какая `apiVersion` используется, всегда будет видна последняя `apiVersion`, поддерживаемая этой версией Dynatrace Operator. Этот механизм можно использовать вместо ручного преобразования.

1. Загрузить преобразованную версию DynaKube. Следующая команда выдаст DynaKube, преобразованную в последнюю поддерживаемую `apiVersion`:

   ```
   kubectl get dynakubes -n <namespace> <dynakube-name> -o yaml
   ```
2. Очистить загруженную DynaKube, оставив только следующие разделы

   * относящиеся к делу части раздела `.metadata`
   * полный раздел `.spec`

### Ручное преобразование

1. Сначала проверить версию Operator, развёрнутую в данный момент. Если неизвестно, какая версия используется, есть несколько способов это узнать.

   С помощью Helm:

   * Использовать команду `helm list`: поле `APP VERSION` показывает версию установленного Dynatrace Operator.

     + Пример:

   ```
   > helm list -n dynatrace -o json | jq -r '.[].app_version'`



   1.6.2
   ```

   С помощью `kubectl`:

   * На Deployment Dynatrace Operator есть метка `app.kubernetes.io/version`, показывающая используемую версию.

     + Пример:

   ```
   > kubectl get deployment dynatrace-operator -n dynatrace -o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'



   1.6.2
   ```
2. Затем проверить `apiVersion` используемой `DynaKube` и следовать соответствующему руководству по миграции в [обзоре выше](#overview).

## Процесс удаления

Dynatrace Operator следует структурированному процессу устаревания, соответствующему [официальным рекомендациям Kubernetes﻿](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning), чтобы обеспечить плавный переход между версиями API DynaKube и предоставить достаточно времени для миграции.

### Этап 1: объявление об устаревании

**Предварительное уведомление об устаревании**: объявление публикуется в примечаниях к выпуску как минимум за один релиз Dynatrace Operator до вступления устаревания в силу.

**Отметка устаревания**: версия API официально помечается как устаревшая в следующем релизе, но остаётся полностью функциональной и поддерживаемой.

### Этап 2: период поддержки устаревшей версии

**Продолжение поддержки**: устаревшая версия API продолжает полностью поддерживаться и оставаться функциональной в течение периода устаревания.

**Рекомендация к миграции**: пользователям настоятельно рекомендуется в этот период выполнить миграцию на более новую версию API, используя предоставленные руководства по миграции.

**Автоматическое преобразование**: Operator автоматически преобразует устаревшие версии API в последнюю поддерживаемую версию в фоновом режиме, обеспечивая совместимость.

### Этап 3: подготовка к удалению

**Отключение обслуживания API**: по окончании периода поддержки устаревшая версия API помечается в Custom Resource Definition (CRD) как `served: false`.

**Режим только для преобразования**: схема версии API сохраняется в CRD исключительно для целей преобразования, что позволяет читать и преобразовывать существующие ресурсы.

**Крайний срок миграции**: пользователям необходимо завершить миграцию на более новую версию API до начала этого этапа, чтобы обеспечить дальнейшую работоспособность своих ресурсов DynaKube.

### Этап 4: полное удаление

**Удаление схемы**: схема устаревшей версии API полностью удаляется из CRD в одном из будущих релизов Operator.

**Отсутствие поддержки преобразования**: после удаления никакая поддержка преобразования или совместимости для устаревшей версии API недоступна.

### Рекомендации по срокам миграции

* **Немедленные действия**: планировать миграцию сразу после объявления об устаревании
* **Период тестирования**: использовать период устаревания для тестирования миграции в непроизводственных средах
* **Миграция в продуктивной среде**: завершить миграцию в продуктивной среде задолго до отключения обслуживания API
* **Проверка**: после миграции убедиться, что все ресурсы DynaKube используют текущую версию API