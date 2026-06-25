---
title: Заметки о выпуске Dynatrace Operator версии 1.8.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-8-0
scraped: 2026-05-12T12:05:26.349587
---

# Заметки о выпуске Dynatrace Operator версии 1.8.0

# Заметки о выпуске Dynatrace Operator версии 1.8.0

* Заметки о выпуске
* Updated on Mar 31, 2026

Дата выпуска: January 27th, 2026

Обновление до 1.8.1

Если вы используете Dynatrace Operator версии 1.8, рекомендуется обновиться до версии 1.8.1 для получения последних важных исправлений.

## Объявления

Dynatrace Operator версии 1.8 вводит новую рекомендуемую версию DynaKube CRD по умолчанию — `v1beta6`. Рекомендуется обновить существующие ресурсы DynaKube до этой последней версии для использования новых функций и улучшений.

### Автоматическая настройка OTLP-экспортёра для приложений, инструментированных с OpenTelemetry

Dynatrace Operator теперь может автоматически настраивать приложения, инструментированные с OpenTelemetry, для экспорта трейсов, метрик и логов в Dynatrace через функцию автонастройки OTLP-экспортёра. Это упрощает управление конфигурацией и обеспечивает согласованный приём телеметрии в различных средах.

Сведения о конфигурации и примеры см. в [руководстве по автонастройке OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

## Новые функции и улучшения

* Внесены улучшения в [модель RBAC для мониторинга Kubernetes](/managed/ingest-from/setup-on-k8s/reference/security#kubernetes-monitoring "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") через ActiveGate.

  + ServiceAccount `dynatrace-kubernetes-monitoring` удалён и заменён на ServiceAccount `dynatrace-activegate`.
  + Для назначения дополнительных разрешений на мониторинг ServiceAccount `dynatrace-activegate` во время установки Operator можно использовать [агрегирование ClusterRole Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles). Подробнее см. в [документации по агрегированию ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
  + ClusterRole `dynatrace-kubernetes-monitoring` использует [агрегирование ClusterRole Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) для назначения необходимых разрешений ServiceAccount во время установки Operator.
  + Токен ServiceAccount монтируется в StatefulSet ActiveGate только при необходимости. ActiveGate, которым токен больше не нужен (например, только маршрутизирующие ActiveGate), перезапускаются после обновления Operator, чтобы не оставалось смонтированных токенов.
  + Установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Перед обновлением обязательно скорректируйте значения Helm, если это применимо.**

* Dynatrace Operator теперь выдаёт предупреждающее событие Kubernetes, когда версия CRD DynaKube или EdgeConnect не является последней, поддерживаемой данным выпуском Operator. Это позволяет легче выявлять устаревшие версии DynaKube CRD.

  + Разрешения RBAC Dynatrace Operator обновлены: добавлено разрешение `events.patch` для пространства имён `dynatrace`.

* Dynatrace Operator теперь использует CA-сертификаты, указанные в `.spec.caCertsRef`, при запросах к Dynatrace API во время развёртывания EdgeConnect.

* Задания, создаваемые CSI-драйвером для [функции получения образов узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"), теперь используют тот же PriorityClass, что и CSI-драйвер, для обеспечения быстрого планирования и возможности вытеснения на перегруженных узлах. Приоритет настраивается через значение Helm `csidriver.priorityClassValue`. Инструкции см. в разделе [Использование priorityClass для критических компонентов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Use priorityClass for critical Dynatrace components").

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь обязательно при включённом [приёме телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.").

* Используйте новую аннотацию пода `dynatrace.com/split-mounts`, чтобы избежать конфликтов с образами приложений, которые уже содержат каталог `/var/lib/dynatrace`. Эта аннотация в первую очередь предназначена для внедрения кодовых модулей в поды ActiveGate для глубокого мониторинга. По умолчанию она включена на ActiveGate, управляемых Dynatrace Operator.

* Компоненты Dynatrace Operator теперь осведомлены об ограничениях памяти пода путём установки переменной среды [`GOMEMLIMIT`](https://pkg.go.dev/runtime#hdr-Environment_Variables). Это повысит их устойчивость к завершению по OOM, поскольку оптимизирует поведение сборщика мусора Go. Ограничения памяти задаются на уровне 90% от лимитов, настроенных для компонентов Operator через Helm. Значения можно указывать с суффиксами IEC (например, 123Mi).

* Пространства имён, выбранные для мониторинга (соответствующие настроенным `namespaceSelectors` для `metadataEnrichment` или `oneAgent`), записываются в условия DynaKube и в лог Operator. Это упрощает проверку и устранение неполадок с настроенными селекторами.

* Метаданные кластера и узлов Kubernetes (например, имя кластера, UID кластера и имя узла) теперь автоматически добавляются (через initContainer с именем `dynatrace-operator`) к атрибутам ресурсов OneAgent для улучшения топологических данных и обеспечения согласованного набора атрибутов ресурсов во всех сигналах.

* Подробные причины сбоев внедрения подов теперь записываются в аннотации `oneagent.dynatrace.com/reason`, `metadata-enrichment.dynatrace.com/reason` и `otlp-exporter-configuration.dynatrace.com/reason` на затронутых подах. Это ускоряет и делает более прозрачным устранение неполадок при внедрении подов.

* Управляемый Dynatrace Operator ActiveGate теперь использует пробу работоспособности (liveness probe) для улучшения обнаружения неисправных состояний.

* Снижены требования к ресурсам по умолчанию для заданий, создаваемых CSI-драйвером для [функции получения образов узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"). Инструкции см. в разделе [Задание ограничений ресурсов для компонентов Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "Set resource limits for Dynatrace Operator components.").

## Исправленные ошибки

* Обработка удалённых версий API при обновлении Dynatrace Operator

  Kubernetes записывает версии CRD в `.status.storedVersions`, но не удаляет записи при удалении версий, поэтому старые версии накапливаются и могут блокировать обновления.

  В Dynatrace Operator 1.8.0 версии API `v1beta1` и `v1beta2` удалены из CRD DynaKube. Если вы использовали Dynatrace Operator версии ниже 1.4.0, эти версии хранятся в CRD в `.status.storedVersions` и требуют очистки, иначе обновление до новой версии API `v1beta6` завершится с ошибкой. В Dynatrace Operator версии 1.7.3 реализовано двухэтапное решение для обеспечения плавного обновления.

  1. Helm-хук для очистки CRD

     Перед фактическим обновлением Helm-хук запускает задание Kubernetes, которое удаляет устаревшие версии API из поля `status.storedVersions` CRD DynaKube. Задание сохраняет только последнюю версию API, доступную в версии Dynatrace Operator, установленной **до** обновления. Этот шаг обеспечивает плавное обновление до нового CRD в процессе обновления Helm. Сведения о необходимых разрешениях см. в разделе [Безопасность Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/security#upgrade-support "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").
  2. Миграция при запуске Dynatrace Operator

     **После** успешного обновления и запуска новой версии Dynatrace Operator 1.8.0 все существующие DynaKube мигрируются на последнюю поддерживаемую версию API `v1beta6`. После миграции DynaKube поле `status.storedVersions` в CRD DynaKube обновляется для хранения только последней версии API `v1beta6`.

  Важное уведомление для кластеров, на которых ранее использовался Dynatrace Operator версии < 1.4.0

  + **Если вы использовали Dynatrace Operator версии <= 1.2, обновление до Dynatrace Operator версии 1.7.3 является обязательным промежуточным шагом перед обновлением до более поздних выпусков.** Пропуск версий не рекомендуется.
  + Установка на основе Helm

    При **использовании Helm** для установки или обновления с Dynatrace Operator версии >=1.3.0 никаких дополнительных действий с вашей стороны не требуется. Необходимые корректировки будут автоматически выполнены Helm-хуком перед обновлением.
  + Альтернативные методы установки

    **Если вы используете один из перечисленных ниже альтернативных методов развёртывания, обновление до Dynatrace Operator версии 1.7.3 является обязательным промежуточным шагом перед обновлением до более поздних выпусков.**

    - Red Hat OpenShift OperatorHub
    - OperatorHub.io
    - Google Marketplace
    - Простые манифесты Kubernetes
  + Ручной подход

    Вместо обновления до версии 1.7.3 можно вручную выполнить необходимые корректировки CRD:

    1. Выполните следующую команду для просмотра хранимых версий в CRD кластера.

       ```
       kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
       ```
    2. Продолжите процедуру, если в хранимых версиях CRD кластера указаны `v1beta1` или `v1beta2`.
    3. Определите текущую активную версию:

       ```
       storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
       ```
    4. Преобразуйте все DynaKube в активную версию:

       ```
       kubectl get dynakube -n dynatrace -o yaml | kubectl apply -f -
       ```
    5. Удалите все предыдущие версии, сохранив активную:

       ```
       kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
       ```

  Корректная очистка поля `.status.storedVersions` CRD критически важна для предотвращения проблем с будущими обновлениями.

  ArgoCD может отображать ресурсы, использующие старую версию API, как «out-of-sync».

* Установка `codeModulesImage` больше невозможна, если CSI-драйвер Dynatrace Operator отключён и не используется ни `applicationMonitoring`, ни `cloudNativeFullStack`. При попытке это сделать при развёртывании или обновлении DynaKube будет выдана ошибка валидации.

* Поле `spec.templates.kspmNodeConfigurationCollector.nodeAffinity` теперь корректно применяется к DaemonSet KSPM Node Configuration Collector.

* DaemonSet KSPM теперь использует встроенный SCC `privileged` на OpenShift, что исключает необходимость дополнительной настройки SCC.

* [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") теперь настроен на обход прокси при подключении к внутрикластерному ActiveGate или Kubernetes API.

* Имя кластера, используемое для атрибута `k8s.cluster.name` при приёме телеметрии, теперь учитывает пользовательские имена кластеров вместо только имени DynaKube.

* `subPath` больше не используется для томов `hostPath` для улучшения совместимости между дистрибутивами Kubernetes (включая RKE).

* Устранена проблема с архитектурой образов кодовых модулей на узлах ARM. Образы кодовых модулей по умолчанию теперь корректно загружаются.

* При включённом CSI-драйвере он теперь корректно устанавливается при развёртывании Dynatrace Operator из Google Marketplace.

* Обработка отсутствующего объекта настроек тенанта `builtin:app-transition.kubernetes` для поддержки новых тенантов, у которых этого объекта больше нет.

* Уменьшена максимальная длина имени DynaKube в зависимости от включённых функций для предотвращения проблем при развёртывании компонентов. Теперь применяются следующие ограничения длины имени:

  + 32 символа, если включён `spec.extensions`
  + 35 символов, если включён `spec.kspm`
  + 38 символов, если включён `spec.telemetryIngest`
  + Существующие ресурсы, нарушающие новые правила валидации, продолжат работать, однако для внесения изменений или обновлений их потребуется исправить.

## Известные ошибки

* Dynatrace Operator 1.8.0 не может установить мониторинг Kubernetes при установке через OLM (Operator Lifecycle Manager) через OperatorHub. Эта проблема исправлена в [Dynatrace Operator 1.8.1](/managed/whats-new/dynatrace-operator/dto-fix-1-8-1 "Release notes for Dynatrace Operator, version 1.8.1"), настоятельно рекомендуется выполнить обновление.
* RBAC для мониторинга Kubernetes требует повышенных разрешений для развёртывания агрегированного ClusterRole. Это затрагивает инструменты, например ArgoCD, управляющие рабочими нагрузками без разрешений cluster-admin.

## Уведомления об удалении и прекращении поддержки (deprecation)

* [Поддержка Kubernetes 1.27](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") завершилась в июле 2025 года. В результате Dynatrace Operator 1.8.0+ больше не поддерживает эту версию.
* ServiceAccount `dynatrace-kubernetes-monitoring` больше не существует. Вместо него агрегированный ClusterRole теперь привязан к ServiceAccount `dynatrace-activegate`, который с этой версии будет использоваться для разрешений мониторинга Kubernetes. Подробнее см. в [документации по агрегированию ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
* Helm-репозиторий по адресу `dynatrace/helm-charts` объявлен устаревшим и прекратит получать обновления в будущем выпуске. Обновите URL следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Событие «Mark for Termination» объявлено устаревшим и будет удалено в будущей версии Operator.

## Обновление с Dynatrace Operator версии 1.7

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь обязательно при включённом приёме телеметрии.
* Устаревшие версии API DynaKube `v1beta1` и `v1beta2` удалены из схемы CRD DynaKube.
* Версия API DynaKube `v1beta3` больше не обслуживается и будет удалена в будущем выпуске Dynatrace Operator. См.: [Руководство по миграции версий API DynaKube](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").
* Обновление Dynatrace Operator может привести к перезапуску ActiveGate, DaemonSet OneAgent (агент хоста) и DaemonSet Log Monitoring.
* Если вы отслеживаете Kubernetes через публичный Kubernetes API изнутри внутрикластерного ActiveGate, необходимо пересоздать токен-носитель (bearer token), так как имя используемого ServiceAccount изменилось с `dynatrace-kubernetes-monitoring` на `dynatrace-activegate`. Следуйте инструкциям в разделе [Подключение к публичному Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* В связи с вышеупомянутыми изменениями объектов RBAC ActiveGate установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Перед обновлением обязательно скорректируйте значения Helm, если это применимо.**