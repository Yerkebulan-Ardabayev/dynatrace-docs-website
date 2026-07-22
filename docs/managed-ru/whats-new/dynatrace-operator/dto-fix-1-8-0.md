---
title: Dynatrace Operator, примечания к выпуску версии 1.8.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-8-0
---

# Dynatrace Operator, примечания к выпуску версии 1.8.0

# Dynatrace Operator, примечания к выпуску версии 1.8.0

* Примечания к выпуску
* Обновлено 23 апр. 2026 г.

Дата выпуска: 27 января 2026 г.

Обновление до 1.8.1

Если используется Dynatrace Operator версии 1.8, рекомендуется обновиться до версии 1.8.1, чтобы получить последние важные исправления.

## Анонсы

Версия 1.8.0 Dynatrace Operator требует дополнительных прав развёртывания по сравнению с предыдущими и будущими версиями. Появление [агрегации ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Понимание того, как Dynatrace Operator использует агрегацию ClusterRole для управления правами мониторинга Kubernetes.") для мониторинга Kubernetes означает, что тому, кто выполняет развёртывание, нужны права на создание агрегированных ClusterRole. Это особенно затрагивает такие инструменты, как ArgoCD, которые управляют нагрузками без прав `cluster-admin`. Полный список необходимых прав развёртывания смотри в разделе [Права развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых им прав").

Версия 1.8 Dynatrace Operator вводит новую версию DynaKube CRD `v1beta6` в качестве версии по умолчанию и рекомендуемой. Рекомендуется обновить существующие ресурсы DynaKube до этой последней версии, чтобы воспользоваться новыми функциями и улучшениями.

### Автоматическая настройка OTLP-экспортёра для приложений, инструментированных с помощью OpenTelemetry

Dynatrace Operator теперь умеет автоматически настраивать приложения, инструментированные с помощью OpenTelemetry, для экспорта трасс, метрик и логов в Dynatrace через функцию автонастройки OTLP-экспортёра. Это упрощает управление конфигурацией и помогает обеспечить единообразный приём телеметрии во всех окружениях.

Подробности настройки и примеры смотри в [руководстве по автонастройке OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматическая настройка OTLP-экспортёра в приложениях, инструментированных с помощью OpenTelemetry SDKs, с использованием Dynatrace Operator.").

## Новые функции и улучшения

* Внесены улучшения в [модель RBAC, используемую для мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/reference/security#kubernetes-monitoring "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых им прав") через ActiveGate.

  + ServiceAccount `dynatrace-kubernetes-monitoring` удалён и заменён на ServiceAccount `dynatrace-activegate`.
  + Можно использовать [агрегацию ClusterRole в Kubernetes﻿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) для назначения ServiceAccount `dynatrace-activegate` дополнительных прав мониторинга во время установки Operator. Подробности смотри в [документации по агрегации ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Понимание того, как Dynatrace Operator использует агрегацию ClusterRole для управления правами мониторинга Kubernetes.").
  + ClusterRole `dynatrace-kubernetes-monitoring` использует [агрегацию ClusterRole в Kubernetes﻿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) для назначения ServiceAccount необходимых прав во время установки Operator.
  + Токен ServiceAccount монтируется в statefulset ActiveGate только при необходимости. ActiveGate, которым токен больше не нужен (например, ActiveGate, выполняющие только маршрутизацию), перезапускаются после обновления Operator, чтобы гарантировать отсутствие смонтированного токена ServiceAccount.
  + Установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Перед обновлением обязательно скорректируй значения Helm, если применимо.**

* Dynatrace Operator теперь генерирует предупреждающее событие Kubernetes, если версия CRD DynaKube или EdgeConnect не является последней, поддерживаемой этим выпуском Operator. Это упрощает выявление устаревших версий CRD DynaKube.

  + Права RBAC Dynatrace Operator обновлены и теперь включают право `events.patch` для пространства имён `dynatrace`.

* Dynatrace Operator теперь использует сертификаты CA, предоставленные через `.spec.caCertsRef`, в запросах к API Dynatrace при развёртывании EdgeConnect.

* Задания, которые CSI-драйвер создаёт для [функции подтягивания образов на узле](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, подтягивание образов через CSI-драйвер и загрузку ZIP."), теперь используют тот же PriorityClass, что и CSI-драйвер, чтобы обеспечить быстрое планирование и допустить вытеснение на перегруженных узлах. Приоритет настраивается через значение Helm `csidriver.priorityClassValue`. Рекомендации смотри в разделе [Использование priorityClass для критически важных компонентов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Использование priorityClass для критически важных компонентов Dynatrace").

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь обязательно при включённом [приёме телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.").

* Используй новую аннотацию пода `dynatrace.com/split-mounts`, чтобы избежать конфликтов с образами приложений, которые уже содержат каталог `/var/lib/dynatrace`. Эта аннотация в основном предназначена для того, чтобы разрешить внедрение модулей кода в поды ActiveGate для глубокого мониторинга. Она включена по умолчанию для ActiveGate, управляемых Dynatrace Operator.

* Компоненты Dynatrace Operator теперь узнают об ограничениях памяти пода через установку переменной окружения [`GOMEMLIMIT`﻿](https://pkg.go.dev/runtime#hdr-Environment_Variables). Это сделает их более устойчивыми к OOM-килам, поскольку оптимизирует поведение сборщика мусора Go. Ограничения памяти устанавливаются на уровне 90% от лимитов, настроенных для компонентов Operator через Helm (например, `csidriver.provisioner.resources.limts.memory`, `webhook.limits.memory`). Значения можно указывать с суффиксами IEC (например, 123Mi).

* Пространства имён, выбранные для мониторинга (соответствующие настроенным `namespaceSelectors` у `metadataEnrichment` или `oneAgent`), записываются в условия DynaKube и в лог оператора. Это упрощает проверку и диагностику настроенных селекторов.

* Метаданные кластера и узла Kubernetes (такие как имя кластера, UID кластера и имя узла) теперь автоматически добавляются (через initContainer с именем `dynatrace-operator`) к атрибутам ресурса OneAgent, чтобы улучшить топологическую картину и обеспечить единообразный набор атрибутов ресурса для всех сигналов независимо от их источника.

* Подробные причины сбоев внедрения в поды теперь записываются в аннотации `oneagent.dynatrace.com/reason`, `metadata-enrichment.dynatrace.com/reason` и `otlp-exporter-configuration.dynatrace.com/reason` на затронутых подах. Это делает диагностику проблем внедрения в поды быстрее и прозрачнее.

* ActiveGate, управляемые Dynatrace Operator, теперь используют liveness probe для улучшения обнаружения неисправных состояний.

* Требования к ресурсам по умолчанию для заданий, создаваемых CSI-драйвером для [функции подтягивания образов на узле](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, подтягивание образов через CSI-драйвер и загрузку ZIP."), были снижены. Рекомендации смотри в разделе [Установка ограничений на ресурсы для компонентов Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "Установка ограничений на ресурсы для компонентов Dynatrace Operator.")

## Устранённые проблемы

* Обработка удалённых версий API при обновлении Dyntrace Operator

  Kubernetes фиксирует версии CRD в `.status.storedVersions`, но не удаляет записи при удалении версий, поэтому старые версии накапливаются и могут блокировать обновления.

  В Dynatrace Operator 1.8.0 версии API `v1beta1` и `v1beta2` удалены из Dynakube CRD. Если ранее использовался Dynatrace operator версии < 1.4.0, эти версии хранятся в CRD в `.status.storedVersions` и требуют очистки, иначе обновление до новой версии API `v1beta6` завершится ошибкой. Начиная с Dynatrace Operator версии 1.7.3 внедрено двухшаговое решение для обеспечения плавного обновления.

  1. Хук Helm для очистки CRD

     Перед непосредственным обновлением хук Helm запускает Job Kubernetes, который удаляет устаревшие версии API из поля `status.storedVersions` DynaKube CRD. Job оставляет только последнюю версию API, доступную в версии Dynatrace Operator, установленной **перед** обновлением. Этот шаг обеспечивает плавное обновление до нового CRD в процессе обновления Helm. Информацию о необходимых разрешениях см. в разделе [Безопасность Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/security#upgrade-support "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и разрешений, которые им требуются").
  2. Миграция при запуске Dynatrace Operator

     **После** успешного обновления и запуска новой версии Dynatrace Operator 1.8.0 он мигрирует все существующие DynaKube на последнюю поддерживаемую версию API `v1beta6`. После миграции DynaKube поле `status.storedVersions` в DynaKube CRD обновляется, чтобы хранить только последнюю версию API `v1beta6`, для обеспечения согласованности.

  Важное уведомление для кластеров, на которых ранее работал Dynatrace Operator версии < 1.4.0

  + **Если ранее использовалась версия Dynatrace Operator <= 1.2, обновление до Dynatrace Operator версии 1.7.3 обязательно как промежуточный шаг перед обновлением до более поздних версий, чтобы обеспечить плавный и надёжный переход.** В общем случае пропуск версий не рекомендуется.
  + Установка на основе Helm

    При **использовании Helm** для установки или обновления с версии Dynatrace Operator >=1.3.0 никаких дополнительных действий не требуется. Необходимые корректировки будут автоматически выполнены хуком pre-upgrade Helm в процессе обновления.
  + Альтернативные методы установки

    **Если используется один из перечисленных ниже альтернативных методов развёртывания, обновление до Dynatrace Operator версии 1.7.3 обязательно как промежуточный шаг перед обновлением до более поздних версий, чтобы обеспечить плавный и надёжный переход.**

    - Red Hat OpenShift OperatorHub
    - OperatorHub.io
    - Google Marketplace
    - Обычные манифесты Kubernetes
  + Ручной способ

    Вместо обновления до версии 1.7.3 можно вручную выполнить необходимые корректировки CRD

    1. Выполнить следующую команду, чтобы вывести список хранимых версий в CRD кластера.

       ```
       kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
       ```
    2. Продолжить процедуру, если `v1beta1` или `v1beta2` присутствуют в списке хранимых версий CRD в кластере.
    3. Определить текущую активную версию:

       ```
       storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
       ```
    4. Преобразовать все DynaKube к активной версии:

       ```
       kubectl get dynakube -n dynatrace -o yaml | kubectl apply -f -
       ```
    5. Удалить все предыдущие версии, оставив активную версию:

       ```
       kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
       ```

  Обеспечение надлежащей очистки поля `.status.storedVersions` CRD критично, чтобы избежать проблем при будущих обновлениях.

  ArgoCD может отображать ресурсы, всё ещё использующие старую версию API, как «out-of-sync».

* Больше нельзя задать `codeModulesImage`, если CSI driver Dyntrace Operator отключён и не используется ни `applicationMonitoring`, ни `cloudNativeFullStack`. При попытке сделать это будет вызвана ошибка валидации при развёртывании или обновлении DynaKube.

* Поле `spec.templates.kspmNodeConfigurationCollector.nodeAffinity` теперь корректно применяется к DaemonSet KSPM Node Configuration Collector.

* KSPM DaemonSet теперь использует встроенный SCC `privileged` на OpenShift, что устраняет необходимость в дополнительной настройке SCC.

* [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.") теперь настроен так, чтобы не использовать прокси для подключения к ActiveGate внутри кластера или к Kubernetes API.

* Имя кластера, используемое для атрибута `k8s.cluster.name` при приёме телеметрии, теперь учитывает пользовательские имена кластеров, а не только имя DynaKube.

* `subPath` больше не используется для томов `hostPath`, чтобы повысить совместимость с различными дистрибутивами Kubernetes (включая RKE):

  + Базовая структура host path остаётся неизменной. Прежнее значение `subPath` теперь добавляется в конец `hostPath`.

* Была проблема с архитектурой образов code modules на узлах ARM. Образы code modules по умолчанию теперь корректно загружаются.

* Если включено, CSI driver теперь корректно устанавливается при развёртывании Dynatrace Operator из Google Marketplace.

* Обработка отсутствующего объекта настроек тенанта `builtin:app-transition.kubernetes` для поддержки более новых тенантов, у которых этого объекта уже нет.

* Уменьшена максимальная длина имени DynaKube в зависимости от включённых функций, чтобы предотвратить проблемы при развёртывании компонентов. Теперь применяются следующие ограничения длины имени:

  + 32 символа, если включён `spec.extensions`
  + 35 символов, если включён `spec.kspm`
  + 38 символов, если включён `spec.telemetryIngest`.
  + Существующие ресурсы, нарушающие эти новые правила валидации, продолжат работать как раньше, но потребуют исправления при желании внести изменение или обновление.

* Исправлена проблема совместимости, связанная с `metadataEnrichment` и `classicFullstack`. Теперь `metadataEnrichment` будет работать с `classicFullstack`. Подробнее см. [Поддержка Dynatrace Operator и известные проблемы](/managed/ingest-from/technology-support/support-model-and-issues#classic-full-stack-with-metadata-enrichment "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, и известные проблемы").

* Исправлена проблема с подключением в Dynatrace Operator v1.7, возникавшая между OTLP-экспортёром или CodeModules, внедрёнными в поды приложений, и ActiveGate внутри кластера, когда флаг функции [`automatic-tls-certificate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "Список флагов функций для настройки Dynatrace Operator на Kubernetes.") переключался с `true` на `false`. Начиная с Operator v1.8.0, TLS-сертификат, ранее созданный для ActiveGate внутри кластера, автоматически удаляется из внедрённых пространств имён при отключении `automatic-tls-certificate`.

* Изменена точка монтирования пользовательских CA-сертификатов EdgeConnect, чтобы предотвратить перезапись известных доверенных CA. Предыдущие версии operator требуют включения CA-сертификатов для публичных эндпойнтов Dynatrace в ConfigMap, если задан `.spec.caCertsRef` EdgeConnect.

## Известные проблемы

* Dynatrace Operator 1.8.0 не может установить мониторинг Kubernetes при установке через OLM (Operator Lifecycle Manager) через OperatorHub. Operator полагается на агрегированные ClusterRole и соответствующие им ClusterRoleBinding для настройки необходимых разрешений для мониторинга Kubernetes. Поскольку агрегированные ClusterRole пусты на этапе сборки (их правила заполняются во время выполнения через aggregationRules), OLM неверно распознаёт их как пустые и удаляет манифесты как ClusterRole, так и ClusterRoleBinding во время установки. В результате необходимые разрешения так и не предоставляются, и мониторинг Kubernetes не может быть установлен. Эта проблема исправлена в [Dynatrace Operator 1.8.1](/managed/whats-new/dynatrace-operator/dto-fix-1-8-1 "Примечания к выпуску Dynatrace Operator, версия 1.8.1"), настоятельно рекомендуется обновиться.
* RBAC для мониторинга Kubernetes требует повышенных разрешений для развёртывания агрегированного ClusterRole. Это затрагивает инструменты, такие как ArgoCD, которые управляют рабочими нагрузками без разрешений cluster-admin.

## Уведомления об удалении и устаревании

* [Поддержка Kubernetes 1.27](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") завершилась в июле 2025 года. В результате Dynatrace Operator 1.8.0+ больше не будет поддерживать эту версию.
* ServiceAccount `dynatrace-kubernetes-monitoring` больше не будет существовать. Вместо него теперь используется агрегированная ClusterRole, привязанная к ServiceAccount `dynatrace-activegate`, которая с этой версии применяется для прав мониторинга Kubernetes. Подробнее см. в [документации по агрегации ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
* Если использовался [Preview расширенной видимости объектов Kubernetes](/managed/whats-new/preview-releases#k8s-object-visibility "Learn about our Preview releases and how you can participate in them.") и также был разблокирован мониторинг чувствительных объектов Kubernetes ConfigMaps и Secrets, рекомендуется выполнить следующий шаг очистки после обновления до Operator 1.8.0:

  ```
  kubectl delete ClusterRoleBinding/dynatrace-kubernetes-monitoring-sensitive
  ```

  Подробности: Dynatrace Operator 1.8.0 использует `aggregationRules` для объединения прав из разных ClusterRole. Это делает ClusterRoleBinding `dynatrace-kubernetes-monitoring-sensitive` устаревшим, его можно безопасно удалить после обновления до Operator 1.8.0.

* Репозиторий Helm, расположенный в `dynatrace/helm-charts`, устарел и в одном из будущих релизов перестанет получать обновления! Если он ещё используется,
  нужно обновить URL на `dynatrace/dynatrace-operator` или перейти на подход на основе OCI registry. URL репозитория Helm обновляется следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Чтобы избежать возможных сбоев, настоятельно рекомендуется поддерживать версию API DynaKube актуальной. Как только версия помечается устаревшей и удаляется, обновление может стать значительно сложнее и более чувствительным по срокам.

  + Подробнее о процессе устаревания версий API DynaKube см. в [руководстве по миграции](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* Бинарные файлы CSI sidecar, расположенные в `/usr/local/bin/csi-node-driver-registrar` и `/usr/local/bin/livenessprobe`, а также флаги чарта Helm `csidriver.registrar.builtIn` и `csidriver.livenessprobe.builtIn` были удалены (устарели в v1.7.0). Поды CSI driver теперь всегда будут использовать встроенные реализации livenessprobe и CSI node driver registrar. У клиентов, ранее установивших эти флаги в значение `false`, может наблюдаться изменение поведения. Цель этого изменения, минимизировать уязвимости в Dynatrace Operator за счёт своевременного обновления этих компонентов.

* Поле `autoUpdate` OneAgent было удалено. Автоматические обновления теперь следуют настроенной целевой версии тенанта. Чтобы отключить автоматические обновления, нужно задать поле `version` или `image` в DynaKube CR.

* Событие «Mark for Termination» устарело и будет удалено в одной из будущих версий Operator. Эта функциональность теперь избыточна, так как её заменили события доступности хоста при выключении и перезагрузке хоста, введённые в OneAgent версии 1.301.

## Обновление с версии Dynatrace Operator 1.7

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь обязательно, если включён [приём телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.").
* Устаревшие версии API DynaKube `v1beta1` и `v1beta2` были удалены из схемы DynaKube CRD.
* Версия API DynaKube `v1beta3` больше не обслуживается и будет удалена в одном из будущих релизов Dynatrace Operator. См.: [Руководство по миграции для версий API DynaKube](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")
* Обновление Dynatrace Operator может привести к перезапуску ActiveGate, DaemonSet OneAgent (host agent) и DaemonSet Log Monitoring.
* При мониторинге Kubernetes через публичный API Kubernetes изнутри ActiveGate внутри кластера, нужно пересоздать bearer-токен, поскольку имя используемого ServiceAccount изменилось с `dynatrace-kubernetes-monitoring` на `dynatrace-activegate`. Следуйте инструкциям в разделе [Подключение к публичному API Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* Из-за вышеупомянутых изменений в объектах RBAC ActiveGate установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Обязательно скорректируйте значения Helm, если применимо, перед обновлением.**