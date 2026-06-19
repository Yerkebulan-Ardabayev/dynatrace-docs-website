---
title: Руководство по миграции версий API DynaKube
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/dynakube
scraped: 2026-05-12T12:09:37.583978
---

# Руководство по миграции версий API DynaKube

# Руководство по миграции версий API DynaKube

* Справочник
* Чтение: 10 мин
* Обновлено 19 марта 2026 г.

## Обзор

В зависимости от версии Dynatrace Operator поддерживаются различные `apiVersion` ресурса `DynaKube`. На этой странице собраны руководства по миграции для каждой `apiVersion` с учётом версии Operator.

Начиная с версии Dynatrace Operator 1.8.0+, Dynatrace Operator создаёт предупреждающее событие Kubernetes, если установленная версия DynaKube CRD не соответствует версии, ожидаемой этим выпуском Operator.

### Обзор версий API

| Версия API DynaKube | Появилась | Устарела | Не обслуживается [1](#fn-1-1-def) | Удалена | Руководства по миграции |
| --- | --- | --- | --- | --- | --- |
| v1beta6 | 1.8.0 |  |  |  |  |
| v1beta5 | 1.6.0 |  |  |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Перенесите ваш ресурс v1beta5 DynaKube CR на apiVersion v1beta6.") |
| v1beta4 | 1.5.0 | 1.9.0 |  |  | [на v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Перенесите ваш ресурс v1beta4 DynaKube CR на apiVersion v1beta6."), [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Перенесите ваш ресурс v1beta4 DynaKube CR на apiVersion v1beta5.") |
| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Перенесите ваш ресурс v1beta3 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Перенесите ваш ресурс v1beta3 DynaKube CR на apiVersion v1beta4.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.7.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Перенесите ваш ресурс v1beta2 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Перенесите ваш ресурс v1beta2 DynaKube CR на apiVersion v1beta4.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.7.0 | [на v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Перенесите ваш ресурс v1beta1 DynaKube CR на apiVersion v1beta5."), [на v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Перенесите ваш ресурс v1beta1 DynaKube CR на apiVersion v1beta4.") |

1

Указанная версия Dynatrace Operator больше не обслуживает эту версию API. С её помощью нельзя применять новые ресурсы. Схема сохраняется в CRD только для автоматического преобразования и будет удалена в последующем выпуске. Подробнее см. [Процесс удаления](#deprecation).

## Стратегии преобразования

### Автоматическое преобразование

Каждая версия Dynatrace Operator преобразует развёрнутые `DynaKubes` с более старой `apiVersion` к новейшей `apiVersion`, поддерживаемой этой версией Dynatrace Operator.

* Пример: Dynatrace Operator v1.6.x всегда преобразует `DynaKubes` к `v1beta5`.

Поэтому при проверке с помощью `kubectl`, какая `apiVersion` используется, вы всегда будете видеть новейшую `apiVersion`, поддерживаемую этой версией Dynatrace Operator. Этот механизм можно использовать вместо ручного преобразования.

1. Загрузите преобразованную версию вашего DynaKube. Следующая команда выдаст DynaKube, преобразованный к новейшей поддерживаемой `apiVersion`:

   ```
   kubectl get dynakubes -n <namespace> <dynakube-name> -o yaml
   ```
2. Очистите загруженный DynaKube, оставьте только эти разделы

   * соответствующие части раздела `.metadata`
   * полный раздел `.spec`

### Ручное преобразование

1. Сначала проверьте версию Operator, которая развёрнута в настоящее время. Если вы не знаете, какая версия используется, ниже приведены несколько способов это выяснить.

   С помощью Helm:

   * Используйте команду `helm list`: поле `APP VERSION` показывает версию установленного Dynatrace Operator.

     + Пример:

   ```
   > helm list -n dynatrace -o json | jq -r '.[].app_version'`



   1.6.2
   ```

   С помощью `kubectl`:

   * На развёртывании Dynatrace Operator есть метка `app.kubernetes.io/version`, которая показывает используемую версию.

     + Пример:

   ```
   > kubectl get deployment dynatrace-operator -n dynatrace -o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'



   1.6.2
   ```
2. Затем проверьте `apiVersion` используемого `DynaKube` и следуйте соответствующему руководству по миграции в [обзоре выше](#overview).

## Процесс удаления

Dynatrace Operator придерживается структурированного процесса прекращения поддержки, который следует [официальным рекомендациям Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning) для обеспечения плавных переходов между версиями API DynaKube, предоставляя при этом достаточно времени для миграции.

### Этап 1: объявление о прекращении поддержки

**Предварительное уведомление об устаревании**: объявление делается в примечаниях к выпуску не менее чем за один выпуск Dynatrace Operator до того, как прекращение поддержки вступит в силу.

**Пометка об устаревании**: версия API официально помечается как устаревшая в следующем выпуске, но остаётся полностью функциональной и поддерживаемой.

### Этап 2: период поддержки после объявления об устаревании

**Продолжение поддержки**: устаревшая версия API продолжает полностью поддерживаться и оставаться функциональной в течение периода прекращения поддержки.

**Рекомендация по миграции**: пользователям настоятельно рекомендуется в это время перейти на более новую версию API с помощью предоставленных руководств по миграции.

**Автоматическое преобразование**: Operator автоматически преобразует устаревшие версии API к новейшей поддерживаемой версии в фоновом режиме, обеспечивая совместимость.

### Этап 3: подготовка к удалению

**Отключение обслуживания API**: после окончания периода поддержки устаревшая версия API помечается как `served: false` в Custom Resource Definition (CRD).

**Режим только преобразования**: схема версии API сохраняется в CRD только для целей преобразования, позволяя считывать и преобразовывать существующие ресурсы.

**Крайний срок миграции**: пользователи должны завершить миграцию на более новую версию API до этого этапа, чтобы обеспечить дальнейшую работоспособность своих ресурсов DynaKube.

### Этап 4: полное удаление

**Удаление схемы**: схема устаревшей версии API полностью удаляется из CRD в будущем выпуске Operator.

**Отсутствие поддержки преобразования**: после удаления для устаревшей версии API недоступна никакая поддержка преобразования или совместимости.

### Рекомендации по срокам миграции

* **Немедленные действия**: планируйте миграцию сразу после объявления уведомления об устаревании
* **Период тестирования**: используйте период прекращения поддержки для тестирования миграции в непроизводственных окружениях
* **Производственная миграция**: завершите производственную миграцию задолго до отключения обслуживания API
* **Проверка**: убедитесь, что после миграции все ресурсы DynaKube используют текущую версию API