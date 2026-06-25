---
title: Заметки о выпуске Dynatrace Operator версии 1.9.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-9-0
scraped: 2026-05-12T12:14:23.050606
---

# Заметки о выпуске Dynatrace Operator версии 1.9.0

# Заметки о выпуске Dynatrace Operator версии 1.9.0

* Заметки о выпуске
* Published Mar 19, 2026

Дата выпуска: April 13, 2026

На этой странице представлен обзор нового и улучшенного в Dynatrace Operator версии 1.9.0.

## Новые функции и улучшения

* Обогащение метаданными для кодовых модулей OneAgent:  
  При использовании `applicationMonitoring` или `cloudNativeFullstack` функция `metadataEnrichment` включается автоматически и не требует явного добавления. Это обеспечивает автоматическое добавление метаданных Kubernetes ко всем сигналам, предоставляя полный контекст наблюдаемости без дополнительной настройки.

* SecurityContext для контейнеров Dynatrace OpenTelemetry Collector, EdgeConnect, NodeConfigCollector и CSI-драйвера обновлены в соответствии с актуальными требованиями [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes) и [Pod Security Standards (PSS)](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

* При первом включении мониторинга Kubernetes (например, при подключении нового кластера) настройки KSPM конфигурируются автоматически. Новые кластеры больше не требуют ручной настройки. Существующие кластеры и их конфигурации не затрагиваются. Подробнее см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

* Устаревшие атрибуты обогащения метаданными `dt.kubernetes.*` полностью заменены атрибутами `k8s.*`. Для обратной совместимости устаревшие атрибуты по-прежнему выводятся по умолчанию. Если вы перенесли дашборды, оповещения и запросы на использование `k8s.*`, устаревшие атрибуты можно отключить, установив `feature.dynatrace.com/enable-attributes-dt.kubernetes="false"` в DynaKube. Полный список флагов функций см. в разделе [Флаги функций DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.").

  + Затронутые атрибуты (с заменой из [семантического словаря](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")):

    - `dt.kubernetes.cluster.id` (заменяется на `k8s.cluster.uid`)
    - `dt.kubernetes.workload.kind` (заменяется на `k8s.workload.kind`)
    - `dt.kubernetes.workload.name` (заменяется на `k8s.workload.name`)

* Для ускорения запуска политика получения образов теперь следует значению по умолчанию Kubernetes (`IfNotPresent` для образов с тегами, `Always` для `:latest` или образов без тегов) вместо явной установки `Always`. Политику получения образов можно настроить в DynaKube для компонентов, управляемых Operator, или в Helm-чарте для самого Operator.

* В соответствии с изменениями в Kubernetes 1.31+, профили AppArmor теперь настраиваются непосредственно в `securityContext` пода или контейнера вместо использования аннотаций. Никаких действий не требуется — Dynatrace Operator автоматически применяет правильный метод в зависимости от версии кластера.

* Теперь можно управлять поведением поэтапного обновления (rolling update) непосредственно в DynaKube индивидуально для OneAgent, ActiveGate и LogMonitoring, используя новое поле `rollingUpdate`. Подробнее см. в разделе [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* Архив поддержки теперь включает файл `kubernetes-version.txt` с версией сервера Kubernetes кластера.

## Исправленные ошибки

* Исправлена проблема, при которой Dynatrace Operator сбрасывал количество реплик ActiveGate, EdgeConnect, OpenTelemetry Collector и согласователей расширений базы данных до значений по умолчанию при каждом согласовании, что мешало горизонтальному автомасштабированию подов (HPA). Operator больше не записывает поле `replicas`, если оно явно не указано в DynaKube.

* Исправлена проблема, при которой сбой создания секрета для внедрения Dynatrace в одном пространстве имён прерывал создание секретов для всех остальных пространств имён.

* Значение Helm `customPullSecret` теперь применяется ко всем компонентам, развёртываемым в пространстве имён Dynatrace.

* Поведение внедрения, управляемое `dynatrace.com/inject`, `otlp-exporter-configuration.dynatrace.com/inject` и флагом DynaKube `feature.dynatrace.com/automatic-injection`, теперь согласовано с механизмами внедрения OneAgent и обогащения метаданными.

* Валидация пространств имён теперь охватывает и автонастройку OTLP-экспортёра. Применение DynaKube завершается с ошибкой, если его `namespaceSelector` для внедрения OneAgent, обогащения метаданными или настройки OTLP-экспортёра пересекается с другим DynaKube.

* Исправлена проблема, при которой тома CSI могли прекращать работу после перезапуска узла из-за ошибочной логики отступа (backoff). Теперь доступность монтирования проверяется перед отступом.

* Исправлена проблема, при которой секрет TLS ActiveGate не очищался корректно из-за неверного имени при удалении. Теперь используется правильное имя `<dynakube>-activegate-tls`.

* Исправлена проблема соединения между внутрикластерным ActiveGate и агентами CodeModules. Секреты TLS-сертификатов в отслеживаемых пространствах имён теперь корректно удаляются, когда они больше не нужны.

* Метка `app.kubernetes.io/version` на развёртываемых подах Extension Execution Controller (EEC) теперь отражает версию, указанную в DynaKube.

* Исправлена проблема с заданием получения образов узлов (node-image-pull), в котором использовалось имя узла вместо селектора узла, что приводило к неоптимальному взаимодействию с планировщиком Kubernetes.

* Исправлена проблема, при которой удаление DynaKube и его пересоздание с другим именем приводило к перезаписи параметров подключения кластера Kubernetes в Dynatrace, изменяя имя кластера в пользовательском интерфейсе Dynatrace.

* Исправлена проблема, при которой ActiveGate входил в начальную фазу `Error` при развёртывании, прежде чем успешно завершить согласование.

* Агрегированные ClusterRoles больше не используются. Это решает известную несовместимость с OperatorHub и соответствует принципам наименьших привилегий.

## Уведомления об удалении и прекращении поддержки (deprecation)

* Helm-репозиторий по адресу `dynatrace/helm-charts` объявлен устаревшим и прекратит получать обновления в будущем выпуске. Обновите URL следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Значения Helm `operator.apparmor`, `webhook.apparmor` и `csidriver.apparmor` объявлены устаревшими. В Kubernetes версии 1.31+ задавайте AppArmor через `appArmorProfile` в `podSecurityContext`.

* Флаг `feature.dynatrace.com/oneagent-max-unavailable` объявлен устаревшим. Вместо него используйте поле `rollingUpdate` в DynaKube.

## Обновление с Dynatrace Operator версии 1.8

В Dynatrace Operator версии 1.9 версия API DynaKube `v1beta3` удалена из CRD. Применение ресурсов DynaKube с использованием этой версии завершится с ошибкой. Кроме того, `v1beta4` объявлена устаревшей. Обновите манифесты DynaKube до `v1beta6` перед обновлением Dynatrace Operator. Подробнее см. в [Руководстве по миграции версий API DynaKube](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

Поды, внедрённые через `applicationMonitoring` или `cloudNativeFullStack`, теперь автоматически получают обогащение метаданными. Если `metadataEnrichment` в DynaKube был включён только для поддержки внедрения OneAgent, его можно удалить.

Флаг функции `feature.dynatrace.com/init-container-seccomp-profile` теперь включён по умолчанию. Если вы полагались на неуказанный профиль seccomp для внедрённых init-контейнеров, установите флаг в значение `false` в вашем DynaKube.