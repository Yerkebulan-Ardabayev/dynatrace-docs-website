---
title: Заметки о выпуске Dynatrace Operator версии 1.9.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-9-0
---

# Заметки о выпуске Dynatrace Operator версии 1.9.0

# Заметки о выпуске Dynatrace Operator версии 1.9.0

* Заметки о выпуске
* Обновлено 16 июля 2026 г.

Дата выпуска: 13 апреля 2026 г.

На этой странице собран обзор нового и улучшенного в Dynatrace Operator версии 1.9.0.

## Новые функции и улучшения

* Обогащение метаданными для модулей кода OneAgent:
  При использовании `applicationMonitoring` или `cloudNativeFullstack` `metadataEnrichment` включается автоматически, добавлять его вручную не нужно. Это гарантирует, что метаданные Kubernetes автоматически добавляются ко всем сигналам, что даёт полный контекст наблюдаемости без дополнительной настройки.

* SecurityContexts контейнеров Dynatrace OpenTelemetry Collector, EdgeConnect, NodeConfigCollector и CSI driver обновлены в соответствии с последним [CIS Kubernetes Benchmark﻿](https://www.cisecurity.org/benchmark/kubernetes) и [Pod Security Standards (PSS)﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

* При первом включении мониторинга Kubernetes (например, при подключении нового кластера) настройки KSPM конфигурируются автоматически. Для новых кластеров ручная настройка больше не нужна. На существующие кластеры и их конфигурации это не влияет. Подробнее см. [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

* Устаревшие атрибуты обогащения метаданными `dt.kubernetes.*` полностью заменены атрибутами `k8s.*`. Для обратной совместимости устаревшие атрибуты по умолчанию по-прежнему передаются. Если дашборды, алерты и запросы уже перенесены на использование `k8s.*`, устаревшие атрибуты можно отключить, установив `feature.dynatrace.com/enable-attributes-dt.kubernetes="false"` в DynaKube. Полный список feature flag см. в [Feature flag DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.").

  + Затронутые атрибуты (с заменой из [Семантического словаря](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")):

    - `dt.kubernetes.cluster.id` (заменён на `k8s.cluster.uid`)
    - `dt.kubernetes.workload.kind` (заменён на `k8s.workload.kind`)
    - `dt.kubernetes.workload.name` (заменён на `k8s.workload.name`)

* Для ускорения запуска политика извлечения образов теперь следует поведению Kubernetes по умолчанию (`IfNotPresent` для образов с тегом, `Always` для `:latest` или образов без тега), а не устанавливается явно в `Always`. Политику извлечения образов можно настроить в DynaKube для компонентов, управляемых оператором, или в чарте Helm для самого оператора. Варианты настройки см. в [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* В соответствии с изменениями в Kubernetes 1.31+, профили AppArmor теперь настраиваются напрямую в `securityContext` пода или контейнера, а не через аннотации. Никаких действий не требуется, Dynatrace Operator автоматически применяет нужный метод в зависимости от версии кластера. Если используется Kubernetes 1.30 или более ранняя версия, существующая настройка AppArmor через чарт Helm продолжает работать, но считается устаревшей и будет удалена после окончания срока поддержки Kubernetes 1.30. Подробнее см. [Включение AppArmor для повышения безопасности](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.").

* Теперь поведение rolling update можно управлять напрямую в DynaKube отдельно для OneAgent, ActiveGate и LogMonitoring с помощью нового поля `rollingUpdate`. Подробнее см. [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* Архив поддержки теперь включает файл `kubernetes-version.txt` с версией сервера Kubernetes кластера.

## Устранённые проблемы

* Исправлена проблема, из-за которой Dynatrace Operator при каждом согласовании (reconciliation) сбрасывал количество реплик для ActiveGate, EdgeConnect, OpenTelemetry Collector и реконсилеров расширения баз данных до значений по умолчанию, что мешало горизонтальному автомасштабированию подов (HPA). Теперь Operator не записывает поле `replicas`, если оно явно не указано в DynaKube.

* Исправлена проблема, при которой сбой создания секрета для инъекции Dynatrace в одном namespace прерывал создание секретов для всех оставшихся namespace.

* Значение Helm `customPullSecret` теперь применяется ко всем компонентам, разворачиваемым в namespace Dynatrace.

* Поведение инъекции, управляемое `dynatrace.com/inject`, `otlp-exporter-configuration.dynatrace.com/inject` и feature flag DynaKube `feature.dynatrace.com/automatic-injection`, теперь приведено в соответствие с механизмами инъекции OneAgent и обогащения метаданными. Подробнее о доступных настройках для этих флагов см. в [Аннотации пода и контейнера](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config#annotations "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

* Валидация namespace теперь также охватывает автонастройку OTLP-exporter. Применение DynaKube завершается ошибкой, если её `namespaceSelector` для инъекции OneAgent, обогащения метаданными или настройки OTLP-exporter пересекается с другой DynaKube. Нужно следить, чтобы каждый namespace был назначен только одной DynaKube для инъекции.

* Устранена проблема, из-за которой тома CSI могли переставать работать после перезапуска узла из-за некорректной логики backoff. Теперь перед откатом (backing off) проверяется доступность точки монтирования.

* Исправлена проблема, при которой TLS-секрет ActiveGate очищался некорректно из-за неверного имени при удалении. Теперь используется правильное имя `<dynakube>-activegate-tls`.

* Исправлена проблема с подключением между ActiveGate внутри кластера и агентами CodeModules. TLS-секреты сертификатов в отслеживаемых namespace теперь корректно удаляются, когда они больше не нужны, например, при отключении пользователем feature flag `automatic-tls-certificate`. Ранее устаревшие секреты по-прежнему монтировались в поды приложений, что вызывало сбои подключения из-за истёкшего TLS-сертификата ActiveGate.

* Метка `app.kubernetes.io/version` на развёрнутых подах Extensions Execution Controller (EEC) теперь отражает версию, указанную в DynaKube. Ранее метка ошибочно содержала версию оператора или была пустой.

* Аннотация AppArmor для EdgeConnect, которую ранее устанавливал Operator, удалена, так как она никогда не применялась и не имела эффекта. Обратите внимание, что подход с аннотацией работает только на Kubernetes 1.30 и более ранних версиях, на Kubernetes 1.31+ настройка AppArmor через `securityContext` для EdgeConnect пока не поддерживается. Чтобы задать профиль AppArmor на Kubernetes 1.30 или более ранней версии, нужно использовать поле EdgeConnect `spec.annotations`. Подробнее см. [Включение AppArmor для повышения безопасности](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.").

* Исправлена проблема, при которой задание node-image-pull для загрузки модулей кода Dynatrace использовало имя узла вместо селектора узла, что приводило к неоптимальному взаимодействию с планировщиком Kubernetes.

* Исправлена проблема, при которой удаление DynaKube и повторное создание её под другим именем приводило к перезаписи настроек подключения кластера Kubernetes в Dynatrace, что меняло имя кластера, отображаемое в интерфейсе Dynatrace. Теперь Operator согласовывает сущность кластера Kubernetes перед изменением настроек, что сохраняет существующую конфигурацию.

* Исправлена проблема, при которой ActiveGate при развёртывании входил в начальную фазу `Error`, прежде чем успешно завершить согласование.

* Агрегированные ClusterRole больше не используются. Это устраняет известную несовместимость с OperatorHub и соответствует принципам минимальных привилегий, поскольку их использование требовало дополнительных прав при установке Dynatrace Operator. Развёртывание Dynatrace Operator теперь использует исключительно стандартные ClusterRole. Подробнее см. [Агрегация ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

## Известные проблемы

* Если Dynatrace Operator внедряет профиль seccomp в под приложения в OpenShift, [SecurityContextConstraints (SCC)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies), запрещающие использование профиля seccomp, такие как `anyuid`, `restricted` или `nonroot`, больше не будут применяться. Вместо этого система откатится к другому SCC (например, `restricted-v2`), что может сделать поды непланируемыми или вызвать деградацию рабочей нагрузки.

  [Отключите профиль seccomp для init-контейнеров Dynatrace](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Overview of seccomp profile configuration for Dynatrace components."), если это затрагивает вашу конфигурацию.

## Уведомления об удалении и устаревании

* Репозиторий Helm, расположенный в `dynatrace/helm-charts`, устарел и в одном из следующих релизов перестанет получать обновления! Если репозиторий всё ещё используется, нужно обновить URL на `dynatrace/dynatrace-operator` или перейти на подход на основе OCI registry. URL репозитория Helm обновляется следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Чтобы избежать возможных сбоев, настоятельно рекомендуется поддерживать версию API DynaKube в актуальном состоянии. После того как версия становится устаревшей и удаляется, обновление может значительно усложниться и стать более чувствительным ко времени.

  + Подробнее о процессе устаревания версий API DynaKube см. в [руководстве по миграции](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* Значения Helm `operator.apparmor`, `webhook.apparmor` и `csidriver.apparmor` устарели. Начиная с версии Kubernetes 1.31+, AppArmor нужно настраивать через `appArmorProfile` в `podSecurityContext`. Эти значения продолжат работать до тех пор, пока версия Kubernetes 1.30 не достигнет конца жизненного цикла (август 2026). Подробности см. в разделе [Включение AppArmor для повышения безопасности](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.").

* Флаг `feature.dynatrace.com/oneagent-max-unavailable` устарел. Вместо него нужно использовать поле `rollingUpdate` в DynaKube. Подробности см. в разделе [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

## Обновление с Dynatrace Operator версии 1.8

В Dynatrace Operator версии 1.9 версия API DynaKube `v1beta3` удалена из CRD. Применение ресурсов DynaKube с этой версией завершится ошибкой. Кроме того, `v1beta4` теперь устарела. Перед обновлением Dynatrace Operator нужно обновить манифесты DynaKube до `v1beta6`. Подробнее см. в разделе [Руководство по миграции версий API DynaKube](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

Поды, внедряемые через `applicationMonitoring` или `cloudNativeFullStack`, теперь автоматически получают обогащение метаданными. Если `metadataEnrichment` в DynaKube было включено только для поддержки внедрения OneAgent, его можно убрать.

[Флаг функции](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Overview of seccomp profile configuration for Dynatrace components.") `feature.dynatrace.com/init-container-seccomp-profile` теперь включён по умолчанию. Если ранее использовался неуказанный seccomp-профиль на внедрённых init-контейнерах, нужно установить этот флаг в `false` на DynaKube.