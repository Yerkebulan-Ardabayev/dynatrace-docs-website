---
title: Organize Kubernetes/OpenShift deployments by tags
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments
scraped: 2026-03-06T21:21:53.164758
---

# Организация развёртываний Kubernetes/OpenShift с помощью тегов

# Организация развёртываний Kubernetes/OpenShift с помощью тегов

* Classic
* Практическое руководство
* Чтение: 6 мин.
* Обновлено 9 ноября 2023 г.

Dynatrace автоматически извлекает теги из ваших меток Kubernetes/OpenShift. Это позволяет автоматически организовывать и фильтровать все отслеживаемые компоненты приложений Kubernetes/OpenShift.

## Рекомендации

Мы рекомендуем определять дополнительные метаданные на уровне развёрнутой системы. Для приложений на базе Kubernetes можно просто использовать [аннотации Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/). Dynatrace автоматически обнаруживает и извлекает все аннотации Kubernetes и OpenShift для подов, отслеживаемых с помощью модуля кода OneAgent. Это позволяет использовать [правила автоматического тегирования](../../../../manage/tags-and-metadata/setup/how-to-define-tags.md#automatic "Узнайте, как определять и применять теги вручную и автоматически.") на основе существующих или пользовательских метаданных для определения наборов фильтров для графиков, оповещений и многого другого. Эти теги и правила могут быть изменены и адаптированы в любое время и применяются практически мгновенно без каких-либо изменений в отслеживаемой среде или приложениях.

В Dynatrace вы можете указать [владельцев сущностей](../../../../deliver/ownership.md "Сопоставление владельцев команд с отслеживаемыми сущностями для улучшения совместной работы, назначения задач, реагирования на инциденты и уязвимости, а также управления уровнем сервиса.") для различных объектов Kubernetes, таких как Deployments, Pods, Services или пространства имён (namespaces). Мы рекомендуем предоставлять информацию о владельце через метки или аннотации Kubernetes (можно использовать как метки, так и аннотации для прикрепления метаданных к объектам Kubernetes). Это гарантирует, что объекты Kubernetes имеют адекватное покрытие владельцами, что особенно важно для кратковременных сущностей, таких как поды. Подробнее о правильном формате и примерах предоставления информации о владельце в парах ключ-значение в файле спецификации развёртывания см. в разделе [Назначение команд-владельцев для отслеживаемых сущностей](../../../../deliver/ownership/assign-ownership.md "Назначение владельцев сущностям с использованием метаданных сущностей: меток, переменных среды и тегов.").

Мы рекомендуем определять владельца для Deployment и всех остальных объектов, для которых вы хотите обеспечить покрытие владельцами. См. также [Лучшие практики для владения сущностями](../../../../deliver/ownership/best-practices.md "Советы и лучшие практики для обеспечения адекватного покрытия владельцами сущностей"). Вы можете назначить более одной команды для объекта Kubernetes, при условии, что ключи в парах ключ-значение уникальны.

Хотя вы также можете использовать теги (ручные, автоматические и через API) для добавления информации о владельце к объектам Kubernetes, этот подход имеет свои ограничения — подробнее в разделе [Лучшие практики для владения сущностями](../../../../deliver/ownership/best-practices.md "Советы и лучшие практики для обеспечения адекватного покрытия владельцами сущностей").

## Автоматическое обнаружение свойств и аннотаций Kubernetes

Dynatrace обнаруживает свойства и аннотации Kubernetes. Такие [свойства и аннотации](../../process-groups/configuration/define-your-own-process-group-metadata.md "Настройка собственных метаданных процессов на основе уникальных потребностей вашей организации или среды.") можно использовать при определении [автоматических тегов на основе правил](../../../../manage/tags-and-metadata/setup/how-to-define-tags.md "Узнайте, как определять и применять теги вручную и автоматически.").

Кроме того, Dynatrace обнаруживает следующие свойства, которые можно использовать для [автоматических тегов на основе правил](../../../../manage/tags-and-metadata/setup/how-to-define-tags.md "Узнайте, как определять и применять теги вручную и автоматически.") и [правил обнаружения групп процессов на основе свойств](../../process-groups/configuration/pg-detection.md#detection-rules "Способы настройки обнаружения групп процессов").

* Kubernetes base pod name: предоставленное пользователем имя пода, которому принадлежит контейнер.
* Kubernetes container: имя контейнера, в котором выполняется процесс.
* Kubernetes full pod name: полное имя пода, которому принадлежит контейнер.
* Kubernetes namespace: пространство имён, к которому назначен контейнеризированный процесс.
* Kubernetes pod UID: уникальный идентификатор связанного пода.

## Использование меток Kubernetes в Dynatrace

Теги на основе Kubernetes доступны через поиск Dynatrace. Это позволяет легко находить и проверять результаты мониторинга связанных процессов, выполняющихся в вашей среде Kubernetes или OpenShift. Вы также можете использовать теги Kubernetes для настройки детализированных [профилей оповещений о проблемах](../../../../analyze-explore-automate/notifications-and-alerting/alerting-profiles.md "Узнайте, как создавать и управлять профилями оповещений."). Теги Kubernetes также идеально интегрируются с [фильтрами Dynatrace](../../../application-observability/services-classic/service-flow/service-flow-filtering.md "Узнайте, как работает фильтрация сервисов и как её можно использовать.").

## Импорт меток и аннотаций

Требования

Для обнаружения OneAgent аннотаций и свойств Kubernetes убедитесь, что:

* Поды отслеживаются с помощью модуля кода
* В `spec` вашего пода не установлен параметр `automountServiceAccountToken: false`

Kubernetes

OpenShift

Вы можете указать [метки Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) в [определении развёртывания](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment) вашего приложения или обновить метки ваших ресурсов Kubernetes с помощью команды `kubectl label`.

Вы можете указать [метки OpenShift](https://docs.openshift.com/enterprise/3.0/architecture/core_concepts/pods_and_services.html#labels) в [определении объекта Pod](https://docs.openshift.com/container-platform/3.10/architecture/core_concepts/pods_and_services.html) вашего приложения или обновить метки ваших ресурсов OpenShift с помощью команды [oc label](https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html#application-modification-cli-operations).

Dynatrace автоматически обнаруживает все метки, прикреплённые к подам во время развёртывания приложения. Всё, что вам нужно сделать, — это предоставить подам достаточные привилегии для чтения метаданных из конечной точки REST API Kubernetes. Таким образом, модули кода OneAgent могут считывать эти метки непосредственно из пода.

### Предоставление роли просмотра учётным записям сервисов

Kubernetes

OpenShift

В Kubernetes каждый под связан с учётной записью сервиса, которая используется для аутентификации запросов пода к API Kubernetes. Если не указано иное, под использует учётную запись сервиса `default` своего пространства имён.

Каждое пространство имён имеет собственный набор учётных записей сервисов, а следовательно, и собственную учётную запись `default`, ограниченную данным пространством имён. Метки каждого пода, для которого учётная запись сервиса имеет права просмотра, будут автоматически импортированы в Dynatrace.

Следующие шаги показывают, как добавить привилегии просмотра для учётной записи сервиса `default` в пространстве имён `namespace1`. Вам необходимо повторить эти шаги для всех учётных записей сервисов и пространств имён, которые вы хотите активировать для Dynatrace.

Создайте следующие `Role` и `RoleBinding`, которые позволят учётной записи сервиса `default` просматривать необходимые метаданные вашего пространства имён `namespace1` через REST API Kubernetes:

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

В OpenShift каждый под связан с учётной записью сервиса, которая используется для аутентификации запросов пода к API Kubernetes. Если не указано иное, под использует учётную запись сервиса `default` своего проекта OpenShift.

Каждый проект OpenShift имеет собственный набор учётных записей сервисов, а следовательно, и собственную учётную запись `default`, ограниченную данным проектом. Метки каждого пода, для которого учётная запись сервиса имеет права просмотра, будут автоматически импортированы в Dynatrace.

Следующие шаги показывают, как добавить привилегии просмотра для учётной записи сервиса `default` в проекте `project1`. Вам необходимо повторить эти шаги для всех учётных записей сервисов и проектов, которые вы хотите активировать для Dynatrace.

Создайте следующую `Role`, которая позволит учётной записи сервиса просматривать необходимые метаданные вашего пространства имён `project1` через REST API Kubernetes:

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

Привяжите `Role` к учётной записи сервиса `default`, чтобы роль вступила в силу:

```
oc -n project1 policy add-role-to-user dynatrace-oneagent-metadata-viewer --role-namespace="project1" -z default
```

Кроме того, OpenShift позволяет привязать `Role` ко всем учётным записям сервисов в проекте.

```
oc -n project1 policy add-role-to-group dynatrace-oneagent-metadata-viewer --role-namespace="project1" system:serviceaccounts:project1
```

В результате [процессы](../../process-groups/configuration/define-your-own-process-group-metadata.md "Настройка собственных метаданных процессов на основе уникальных потребностей вашей организации или среды.") Kubernetes, отслеживаемые в вашей среде Dynatrace, будут иметь метки Kubernetes, прикреплённые в виде тегов Kubernetes. Для пространств имён, подов и рабочих нагрузок теги Kubernetes не вычисляются.

## Связанные темы

* [Настройка Dynatrace в Kubernetes](../../../../ingest-from/setup-on-k8s.md "Способы развёртывания и настройки Dynatrace в Kubernetes")
* [Назначение команд-владельцев для отслеживаемых сущностей](../../../../deliver/ownership/assign-ownership.md "Назначение владельцев сущностям с использованием метаданных сущностей: меток, переменных среды и тегов.")
