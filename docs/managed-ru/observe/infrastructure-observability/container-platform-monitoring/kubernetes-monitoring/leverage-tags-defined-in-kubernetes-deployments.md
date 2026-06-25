---
title: Организация развёртываний Kubernetes/OpenShift с помощью тегов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments
scraped: 2026-05-12T11:11:34.364716
---

# Organize Kubernetes/OpenShift deployments by tags

# Организация развёртываний Kubernetes/OpenShift с помощью тегов

* How-to guide
* 6-min read
* Updated on Nov 09, 2023

Dynatrace автоматически формирует теги из меток Kubernetes/OpenShift. Это позволяет автоматически организовывать и фильтровать все отслеживаемые компоненты приложений Kubernetes/OpenShift.

## Рекомендации

Рекомендуется определять дополнительные метаданные на уровне развёртываемой системы. Для приложений на основе Kubernetes можно использовать [аннотации Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/). Dynatrace автоматически обнаруживает и получает все аннотации Kubernetes и OpenShift для подов, отслеживаемых с помощью кодового модуля OneAgent. Это позволяет использовать [правила автоматической расстановки тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") на основе существующих или пользовательских метаданных для определения наборов фильтров для диаграмм, оповещений и других задач. Эти теги и правила можно изменять и адаптировать в любое время — они применяются практически мгновенно без каких-либо изменений в отслеживаемой среде или приложениях.

В Dynatrace можно указать [владельцев сущностей](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") для различных объектов Kubernetes, таких как Deployments, Pods, Services или пространства имён. Рекомендуется предоставлять информацию о владельцах с помощью меток или аннотаций Kubernetes (для прикрепления метаданных к объектам Kubernetes можно использовать как метки, так и аннотации). Это обеспечивает надлежащее покрытие владельцев для объектов Kubernetes, что особенно важно для недолговечных сущностей, таких как Pods. Подробнее о правильном формате и примерах предоставления информации о владельцах в виде пар «ключ-значение» в файле спецификации развёртывания см. в разделе [Назначение команд-владельцев отслеживаемым сущностям](/managed/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.").

Рекомендуется определять владельцев для Deployment и всех других объектов, для которых требуется покрытие владельцев. См. также [Рекомендации по управлению владельцами сущностей](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage"). Одному объекту Kubernetes можно назначить более одной команды, при условии что ключи в парах «ключ-значение» уникальны.

Теги (ручные, автоматизированные и через API) также можно использовать для предоставления информации о владельцах объектов Kubernetes, однако этот подход имеет ограничения — подробнее в разделе [Рекомендации по управлению владельцами сущностей](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

## Автоматическое обнаружение свойств и аннотаций Kubernetes

Dynatrace обнаруживает свойства и аннотации Kubernetes. Такие [свойства и аннотации](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") можно использовать при задании [автоматизированных тегов на основе правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

Кроме того, Dynatrace обнаруживает следующие свойства, которые можно использовать для [автоматизированных тегов на основе правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") и [правил обнаружения групп процессов на основе свойств](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection#detection-rules "Ways to customize process-group detection").

* Kubernetes base pod name: имя пода, предоставленное пользователем, которому принадлежит контейнер.
* Kubernetes container: имя контейнера, в котором работает процесс.
* Kubernetes full pod name: полное имя пода, которому принадлежит контейнер.
* Kubernetes namespace: пространство имён, которому назначен контейнеризированный процесс.
* Kubernetes pod UID: уникальный идентификатор связанного пода.

## Использование меток Kubernetes в Dynatrace

Теги на основе Kubernetes доступны для поиска через поиск Dynatrace. Это позволяет легко находить и анализировать результаты мониторинга связанных процессов, работающих в среде Kubernetes или OpenShift. Теги Kubernetes также можно использовать для настройки детальных [профилей оповещений о проблемах](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles."). Теги Kubernetes также легко интегрируются с [фильтрами Dynatrace](/managed/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").

## Импорт меток и аннотаций

Требования

Чтобы OneAgent обнаруживал аннотации и свойства Kubernetes, убедитесь, что:

* Поды отслеживаются с помощью кодового модуля.
* В спецификации (`spec`) пода не задано `automountServiceAccountToken: false`.

Kubernetes

OpenShift

[Метки Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) можно указывать в [определении развёртывания](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment) вашего приложения или обновлять метки ресурсов Kubernetes с помощью команды `kubectl label`.

[Метки OpenShift](https://docs.openshift.com/enterprise/3.0/architecture/core_concepts/pods_and_services.html#labels) можно указывать в [определении объекта Pod](https://docs.openshift.com/container-platform/3.10/architecture/core_concepts/pods_and_services.html) вашего приложения или обновлять метки ресурсов OpenShift с помощью команды [oc label](https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html#application-modification-cli-operations).

Dynatrace автоматически обнаруживает все метки, прикреплённые к подам при развёртывании приложения. Достаточно предоставить подам достаточные привилегии для чтения метаданных из конечной точки Kubernetes REST API. Таким образом, кодовые модули OneAgent могут читать эти метки непосредственно из пода.

### Предоставление роли просмотра учётным записям сервисов

Kubernetes

OpenShift

В Kubernetes каждый под связан с учётной записью сервиса, используемой для аутентификации запросов пода к Kubernetes API. Если не указано иное, под использует учётную запись сервиса `default` своего пространства имён.

У каждого пространства имён есть собственный набор учётных записей сервисов, а также собственная учётная запись `default` уровня пространства имён. Метки всех подов, для которых у учётной записи сервиса есть права просмотра, будут автоматически импортированы в Dynatrace.

Следующие шаги показывают, как добавить права просмотра учётной записи `default` в пространстве имён `namespace1`. Эти шаги необходимо повторить для всех учётных записей сервисов и пространств имён, которые нужно включить для Dynatrace.

Создайте следующие `Role` и `RoleBinding`, которые разрешают учётной записи `default` просматривать необходимые метаданные о пространстве имён `namespace1` через Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: namespace1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]



---



kind: RoleBinding



apiVersion: rbac.authorization.k8s.io/v1



metadata:



name: dynatrace-oneagent-metadata-viewer-binding



namespace: namespace1



subjects:



- kind: ServiceAccount



name: default



apiGroup: ""



roleRef:



kind: Role



name: dynatrace-oneagent-metadata-viewer



apiGroup: ""
```

```
kubectl -n namespace1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

В OpenShift каждый под связан с учётной записью сервиса, используемой для аутентификации запросов пода к Kubernetes API. Если не указано иное, под использует учётную запись `default` своего проекта OpenShift.

У каждого проекта OpenShift есть собственный набор учётных записей сервисов, а также собственная учётная запись `default` уровня проекта. Метки всех подов, для которых у учётной записи сервиса есть права просмотра, будут автоматически импортированы в Dynatrace.

Следующие шаги показывают, как добавить права просмотра учётной записи `default` в проекте `project1`. Эти шаги необходимо повторить для всех учётных записей сервисов и проектов, которые нужно включить для Dynatrace.

Создайте следующую `Role`, которая разрешит учётной записи сервиса просматривать необходимые метаданные о пространстве имён `project1` через Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: project1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]
```

```
oc -n project1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

Привяжите `Role` к учётной записи `default`, чтобы она вступила в силу:

```
oc -n project1 policy add-role-to-user dynatrace-oneagent-metadata-viewer --role-namespace="project1" -z default
```

Кроме того, OpenShift позволяет привязать `Role` ко всем учётным записям сервисов в проекте.

```
oc -n project1 policy add-role-to-group dynatrace-oneagent-metadata-viewer --role-namespace="project1" system:serviceaccounts:project1
```

В результате [процессы](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") Kubernetes, отслеживаемые в вашей среде Dynatrace, будут иметь метки Kubernetes в качестве тегов. Для пространств имён, подов и нагрузок теги Kubernetes не оцениваются.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Назначение команд-владельцев отслеживаемым сущностям](/managed/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")