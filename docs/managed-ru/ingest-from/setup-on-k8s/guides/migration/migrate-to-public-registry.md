---
title: Переход на публичный реестр
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-public-registry
---

# Переход на публичный реестр

# Переход на публичный реестр

* Практическое руководство
* Чтение за 3 минуты
* Опубликовано 01 июля 2026 г.

Чтобы перевести существующую установку Dynatrace Operator на автоматическое разрешение образов из публичного реестра, см. [Автоматическое разрешение образов с Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

## Предварительные требования

* Dynatrace Operator версии 1.10.0 или новее
* Доступ к [поддерживаемому публичному реестру](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* Dynatrace SaaS версии 1.343 или новее

Dynatrace Operator может автоматически разрешать актуальные URI публичных образов для управляемых компонентов из среды Dynatrace, без ручной настройки поля `image`.

Когда эта функция активна, Dynatrace Operator периодически синхронизирует ссылки на образы для каждого компонента из среды Dynatrace и применяет их автоматически.

### Включение автоматического разрешения образов

1. Удалить поля `image` и `codeModulesImage` из DynaKube, если они заданы: их значения имеют приоритет над автоматически разрешёнными образами для соответствующего компонента.
2. Установить аннотацию `feature.dynatrace.com/use-public-registry` в DynaKube:

   ```
   apiVersion: dynatrace.com/v1beta6



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/use-public-registry: "true"



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   ...
   ```

Включение автоматически с platform token

Если DynaKube использует platform token, Dynatrace Operator включает разрешение из публичного реестра автоматически. Аннотация не требуется. Можно задать `spec.publicRegistryOverride`, чтобы использовать конкретный поддерживаемый публичный реестр.

Переопределение хоста реестра

Чтобы запрашивать образы из конкретного поддерживаемого публичного реестра, нужно задать `spec.publicRegistryOverride` одним из хостов реестра, перечисленных в разделе [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.»), например `public.ecr.aws` для Amazon ECR Public или `registry-1.docker.io» для Docker Hub. Dynatrace Operator передаёт хост в среду Dynatrace при разрешении URI образов.

### Что меняется при включении функции

* **Образы компонентов**: Dynatrace Operator разрешает ссылки на образы из среды Dynatrace для OneAgent, ActiveGate и CodeModules. Компоненты без источника образа по умолчанию (Extension Execution Controller, Standalone Log Module, SQL Extension Executor) всегда требуют указания пользовательского образа в соответствующем поле `spec.templates`.
* **Перезапуски подов**: при первом включении функции перезапускаются все поды управляемых компонентов.
* **Внедрение в приложения**: образ init-контейнера, внедряемый в поды приложений, меняется при следующем перезапуске пода, если не используется CSI driver или если используется [загрузка образа на узел через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). В обоих случаях webhook переключается с режима ZIP-download на режим самораспаковки с использованием образа CodeModules.

### Проверка

После включения нужно убедиться, что Dynatrace Operator разрешает образы из публичного реестра:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

Значение `public-registry` подтверждает, что образ ActiveGate был разрешён из публичного реестра. Аналогично можно проверить `status.oneAgent.source` и `status.codeModules.source` для OneAgent и CodeModules.

## Похожие темы

* [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* [Настройка автообновления для управляемых компонентов Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator")