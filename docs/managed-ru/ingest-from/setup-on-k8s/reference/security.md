---
title: Безопасность Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/security
scraped: 2026-05-12T11:53:39.391593
---

# Безопасность Dynatrace Operator

# Безопасность Dynatrace Operator

* Чтение: 16 мин
* Обновлено 10 марта 2026 г.

Наблюдаемость Kubernetes опирается на компоненты с разными назначениями, конфигурациями по умолчанию и разрешениями. Этим компонентам нужны разрешения для выполнения и поддержания операционной работы Dynatrace в вашем кластере.

Хотя разрешения Dynatrace следуют принципу наименьших привилегий, обязательно защитите пространство имён `dynatrace` и ограничьте доступ закрытой группой администраторов и операторов.

## Список разрешений

### Dynatrace Operator

**Назначение:** поддерживает жизненный цикл компонентов Dynatrace. Заменяет OneAgent Operator.

**Конфигурация по умолчанию:** `1-replica-per-cluster`

**Объекты RBAC**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/Update/Delete/List | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |
| `dynakubes/status` | `dynatrace.com` | Update |  |
| `edgeconnects/status` | `dynatrace.com` | Update |  |
| `statefulsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `daemonsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `replicasets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments/finalizers` | `apps` | Update |  |
| `configmaps` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `pods` | `""` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `events` | `""` | Create/Get/List/Patch |  |
| `services` | `""` | Create/Update/Delete/Get/List/Watch |  |
| `serviceentries` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `virtualservices` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `leases` | `coordination.k8s.io` | Get/Update/Create |  |

### Dynatrace Operator Webhook Server

**Назначения**:

* Изменяет определения подов, чтобы включить модули кода Dynatrace для наблюдаемости приложений
* Проверяет пользовательские ресурсы DynaKube
* Обрабатывает преобразование DynaKube между версиями

**Конфигурация по умолчанию**: `1-replica-per-cluster`, можно масштабировать

**Объекты RBAC**:

* Service Account `dynatrace-webhook`
* Cluster-Role `dynatrace-webhook`
* Role `dynatrace-webhook`

#### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/List/Watch/Update | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
| `replicationcontrollers` | `""` | Get |  |
| `replicasets` | `apps` | Get |  |
| `statefulsets` | `apps` | Get |  |
| `daemonsets` | `apps` | Get |  |
| `deployments` | `apps` | Get |  |
| `jobs` | `batch` | Get |  |
| `cronjobs` | `batch` | Get |  |
| `deploymentconfigs` | `apps.openshift.io` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `events` | `""` | Create/Patch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |

### Dynatrace Operator CSI driver

**Назначение**:

* Для конфигураций `applicationMonitoring` он предоставляет подам на каждом узле необходимый исполняемый файл OneAgent для мониторинга приложений.
* Для конфигураций `hostMonitoring` он предоставляет папку с возможностью записи для конфигураций OneAgent, когда используется файловая система хоста только для чтения.
* Для `cloudNativeFullStack` он предоставляет оба указанных выше варианта.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-oneagent-csi-driver`
* Cluster-Role `dynatrace-oneagent-csi-driver`
* Role `dynatrace-oneagent-csi-driver`

#### Разрешение уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get/List/Create/Delete/Watch |  |
| `events` | `""` | Create/Patch |  |

### ActiveGate

#### Мониторинг платформы Kubernetes

**Назначение**: собирает метрики, события и статус кластера и рабочих нагрузок из Kubernetes API.

**Конфигурация по умолчанию**: `1-replica-per-cluster`, можно масштабировать

**Объекты RBAC**:

* Service Account: `dynatrace-kubernetes`
* ClusterRole: `dynatrace-kubernetes-monitoring`

В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring` был агрегированным ClusterRole. Подробнее см. [Агрегация ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Описание того, как Dynatrace Operator использует агрегацию ClusterRole для управления разрешениями для мониторинга Kubernetes.").

##### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes` | `""` | List/Watch/Get |  |
| `pods` | `""` | List/Watch/Get |  |
| `namespaces` | `""` | List/Watch/Get |  |
| `replicationcontrollers` | `""` | List/Watch/Get |  |
| `events` | `""` | List/Watch/Get |  |
| `resourcequotas` | `""` | List/Watch/Get |  |
| `pods/proxy` | `""` | List/Watch/Get |  |
| `nodes/proxy` | `""` | List/Watch/Get |  |
| `nodes/metrics` | `""` | List/Watch/Get |  |
| `services` | `""` | List/Watch/Get |  |
| `persistentvolumeclaims` | `""` | List/Watch/Get |  |
| `persistentvolumes` | `""` | List/Watch/Get |  |
| `jobs` | `batch` | List/Watch/Get |  |
| `cronjobs` | `batch` | List/Watch/Get |  |
| `deployments` | `apps` | List/Watch/Get |  |
| `replicasets` | `apps` | List/Watch/Get |  |
| `statefulsets` | `apps` | List/Watch/Get |  |
| `daemonsets` | `apps` | List/Watch/Get |  |
| `deploymentconfigs` | `apps.openshift.io` | List/Watch/Get |  |
| `clusterversions` | `config.openshift.io` | List/Watch/Get |  |
| `dynakubes` | `dynatrace.com` | List/Watch/Get |  |
| `edgeconnects` | `dynatrace.com` | List/Watch/Get |  |
| `customresourcedefinitions` | `apiextensions.k8s.io` | List/Watch/Get |  |
| `ingresses` | `networking.k8s.io` | List/Watch/Get |  |
| `networkpolicies` | `networking.k8s.io` | List/Watch/Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Назначения**: [Kubernetes Security Posture Management](/managed/upgrade/unavailable-in-managed "Выбранный вами элемент недоступен в Dynatrace Managed.") обнаруживает, анализирует и непрерывно отслеживает
ошибки конфигурации, рекомендации по усилению безопасности и потенциальные нарушения соответствия в Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-node-config-collector`
* ClusterRole: `dynatrace-kubernetes-monitoring-kspm`

В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring-kspm` был агрегирован ClusterRole `dynatrace-kubernetes-monitoring`. Подробнее см. [Агрегация ClusterRole](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Описание того, как Dynatrace Operator использует агрегацию ClusterRole для управления разрешениями для мониторинга Kubernetes.").

##### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `replicationcontrollers` | `""` | Get/List/Watch |  |
| `serviceaccounts` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `cronjobs` | `batch` | Get/List/Watch |  |
| `jobs` | `batch` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
| `networkpolicies` | `networking.k8s.io` | Get/List/Watch |  |
| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `clusterroles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `rolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `roles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |

### OneAgent

**Назначения**:

* Собирает метрики хостов с узлов Kubernetes.
* Обнаруживает новые контейнеры и внедряет модули кода Dynatrace в поды приложений с помощью инъекции Classic Full-Stack. Необязательно
* Собирает логи контейнеров с узлов Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-logmonitoring`

**Параметры политики**: разрешает **HostNetwork**, **HostPID**, использование любых типов томов.

**Необходимые возможности**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, `FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, `SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`

#### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes/proxy` | `""` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Dynatrace Log Module

**Назначения**:

* Собирает логи контейнеров с узлов Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-logmonitoring`
* Cluster-Role `dynatrace-logmonitoring`

#### Разрешения уровня кластера

Мониторинг логов требует [тех же разрешений уровня кластера, что и OneAgent](#oneagent-permissions).

### Прием телеметрии Dynatrace

**Назначения**:

* Включение [конечных точек телеметрии Dynatrace](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для локального для кластера приёма данных.") в Kubernetes для локального для кластера приёма данных

  + Приём данных через конечные точки [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger](https://www.jaegertracing.io/), [StatsD](https://github.com/statsd/statsd) или [Zipkin](https://zipkin.io/)
* Анализ насыщенных контекстом данных с помощью встроенных приложений, DQL, Notebooks и Dashboards

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | Get/Watch/List |  |
| `namespaces` | `""` | Get/Watch/List |  |
| `nodes` | `""` | Get/Watch/List |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Extensions

**Назначения**:

* Extensions расширяют аналитические возможности Dynatrace за счёт приёма данных из различных источников, таких как сторонние приложения, сервисы и пользовательские метрики. Подробнее см. [Extensions](/managed/ingest-from/extensions "Узнайте, как создавать Dynatrace Extensions и управлять ими.").

**Конфигурация по умолчанию**:

Следующие компоненты требуются независимо от того, какие расширения используются:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**Объекты RBAC**:

В зависимости от используемого расширения требуются следующие объекты RBAC.

* Service Accounts

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Разрешения в пространстве имён `dynatrace`

*Расширение Prometheus*

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Расширение Database*

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Расширение Prometheus

**Назначение**:

* Собирает метрики с конечных точек Prometheus в вашем кластере.

**Конфигурация по умолчанию**:

* Источник данных Prometheus: `replicas-set-in-dynakube` (без значения по умолчанию, число реплик задаётся в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-extensions-prometheus`

##### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch |  |
| `endpoints` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `nodes/metrics` | `""` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Расширение Database

**Назначение**:

* Собирает метрики с конечных точек баз данных в вашем кластере.

**Конфигурация по умолчанию**:

* SQL Extension Executor: `replicas-set-in-dynakube` (без значения по умолчанию, число реплик задаётся в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-sql-ext-exec`
* Roles

  + `dynatrace-sql-ext-exec`

##### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Поддерживаемость Dynatrace Operator

**Назначения**:

* Позволяет Dynatrace Operator выполнять [команду support-archive](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "Эта страница поможет вам справиться с любыми трудностями, которые могут возникнуть при работе с Dynatrace Operator и его различными компонентами."). Необходимо для устранения проблем, связанных с Operator.

**Объекты RBAC**:

* Role `dynatrace-operator-supportability`

**Отказ**:

* От этой функции можно отказаться, задав для значения Helm chart Dynatrace Operator `rbac.supportability` значение `false`.

Отключение этой функции затруднит предоставление необходимой информации при открытии обращений в поддержку по поводу Dynatrace Operator.

#### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get/List |  |

### Поддержка обновления API Dynatrace Operator

**Назначения**:

* Запускает Job `dynatrace-operator-crd-storage-migration` для автоматической очистки удалённых версий API Dynakube в хуке Helm `pre-upgrade`.

**Объекты RBAC**:

* ClusterRole `dynatrace-crd-storage-migration`
* Role `dynatrace-crd-storage-migration`
* ServiceAccount `dynatrace-crd-storage-migration`

**Подключение**:

* От этой функции можно отказаться, задав для значения Helm chart Dynatrace Operator `crdStorageMigrationJob` значение `false`.

#### Разрешения уровня кластера

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Разрешения в пространстве имён `dynatrace`

| Запрашиваемые ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |

## Меры безопасности компонентов Dynatrace Operator

В следующей таблице представлен подробный анализ мер безопасности для компонентов Kubernetes: Dynatrace Operator, вебхука Dynatrace Operator и CSI driver Dynatrace Operator. Этот отчёт основан на:

* [CIS Benchmark](https://dt-url.net/zd0368p), общепризнанном стандарте защиты развёртываний Kubernetes.
* [Политиках POD Security Standard](https://dt-url.net/mp0345l).
* Рекомендуемых практиках.

**Стандарты и сокращения**:

* **CIS**: [Center for Internet Security (CIS) Kubernetes Benchmark](https://dt-url.net/zd0368p).
* **PSSB**: [Pod Security Standards, профиль Baseline](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).
* **PSSR**: [Pod Security Standards, профиль Restricted](https://dt-url.net/ut4387d).

В столбце **Стандарт** используются эти сокращения.

### Компоненты Dynatrace Operator

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Соблюдается  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Исключение (см. раскрытие ниже)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Запланированное улучшение (см. раскрытие ниже)

| Мера безопасности | Стандарт | Operator | Webhook | CSI driver |
| --- | --- | --- | --- | --- |
| Запретить привилегированные контейнеры[1](#fn-1-1-def) | CIS 5.2.2 / PSS Baseline | Соблюдается | Соблюдается | Исключение |
| Запретить повышение привилегий[1](#fn-1-1-def) | CIS 5.2.6 / PSS Restricted | Соблюдается | Соблюдается | Исключение |
| Запретить контейнеры, работающие от root[2](#fn-1-2-def) | CIS 5.2.7 / PSS Restricted | Соблюдается | Соблюдается | Исключение |
| Ограничить доступ к секретам (RBAC) | CIS 5.1.4 | Запланированное улучшение | Запланированное улучшение | Запланированное улучшение |
| Запретить использование томов HostPath[3](#fn-1-3-def) | CIS 5.2.12 / PSS Baseline | Соблюдается | Соблюдается | Исключение |
| Ограничить автомонтирование токена service account[4](#fn-1-4-def) | CIS 5.1.6 | Исключение | Исключение | Исключение |
| Запретить использование слишком многих или небезопасных возможностей | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSS Restricted | Соблюдается | Соблюдается | Соблюдается |
| Запретить использование HostPorts | CIS 5.2.13 / PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Запретить доступ к сети хоста | CIS 5.2.5 / PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Запретить использование PID хоста | CIS 5.2.3 / PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Запретить использование IPC хоста | CIS 5.2.4 / PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Требовать readOnlyRootFilesystem | Рекомендуемая практика | Соблюдается | Соблюдается | Соблюдается |
| Требовать лимиты ресурсов[5](#fn-1-5-def) | Рекомендуемая практика | Соблюдается | Соблюдается | Соблюдается |
| Требовать seccomp (как минимум default/runtime) | CIS 5.7.2 / PSS Restricted | Соблюдается | Соблюдается | Соблюдается |
| Запретить монтирование секретов как переменной окружения | CIS 5.4.1 | Соблюдается | Соблюдается | Соблюдается |
| Ограничить sysctls | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Ограничить AppArmor | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |
| Запретить SELinux[6](#fn-1-6-def) | PSS Baseline | Соблюдается | Соблюдается | Исключение |
| Тип монтирования /proc | PSS Baseline | Соблюдается | Соблюдается | Соблюдается |

1

CSI driver требует повышенных разрешений для создания монтирований в хост-системе и управления ими. Подробнее см. [Привилегии CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Компоненты Dynatrace Operator").

2

CSI driver взаимодействует с kubelet через сокет на хосте, и для доступа к этому сокету CSI driver должен работать от root.

3

CSI driver хранит и кэширует исполняемые файлы OneAgent в файловой системе хоста, и для этого ему нужно монтирование hostVolume.

4

Компонентам Dynatrace Operator, Webhook и CSI driver необходимо взаимодействовать с Kubernetes API.

5

Provisioner CSI driver по умолчанию не имеет лимитов ресурсов, чтобы обеспечить наилучшую [производительность во время выделения ресурсов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "Задайте лимиты ресурсов для компонентов Dynatrace Operator."); лимиты можно задать через значения Helm chart.

6

CSI driver требует уровня seLinux s0, чтобы поды приложений видели файлы из тома, созданного CSI driver.

**Запланированное улучшение**:  
Role в области пространства имён для Operator, Webhook и CSI driver сейчас разрешают доступ ко всем секретам в их пространстве имён. Запланировано улучшение, ограничивающее эти Role конкретными именами секретов, в соответствии с конфигурацией ClusterRole.

### Управляемые компоненты

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Соблюдается  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Исключение (см. раскрытие ниже)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Запланированное улучшение (см. раскрытие ниже)

| Мера безопасности | Стандарт | OneAgent | Extensions controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM | OneAgent Log Module |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Запретить привилегированные контейнеры[1](#fn-2-1-def) | CIS 5.2.2 / PSSB | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение |
| Запретить повышение привилегий[2](#fn-2-2-def) | CIS 5.2.6 / PSSR | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение |
| Запретить контейнеры, работающие от root[3](#fn-2-3-def) | CIS 5.2.7 / PSSR | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | Соблюдается |
| Запретить использование слишком многих или небезопасных возможностей[4](#fn-2-4-def) | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSSR | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | Исключение |
| Ограничить доступ к секретам (RBAC) | CIS 5.1.4 | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Запретить использование томов HostPath[5](#fn-2-5-def) | CIS 5.2.12 / PSSB | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | Исключение |
| Запретить использование HostPorts | CIS 5.2.13 / PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Запретить доступ к сети хоста[6](#fn-2-6-def) | CIS 5.2.5 / PSSB | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Запретить использование PID хоста[7](#fn-2-7-def) | CIS 5.2.3 / PSSB | Исключение | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Исключение | Соблюдается |
| Запретить использование IPC хоста | CIS 5.2.4 / PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Требовать readOnlyRootFilesystem | Рекомендуемая практика | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Требовать лимиты ресурсов[10](#fn-2-10-def) | Рекомендуемая практика | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Запланированное улучшение |
| Требовать использования seccomp (как минимум default/runtime)[8](#fn-2-8-def) | CIS 5.7.2 / PSSR | Исключение | Соблюдается | Соблюдается | Исключение | Исключение | Исключение | Исключение |
| Запретить монтирование секретов как переменной окружения | CIS 5.4.1 | Соблюдается | Соблюдается | Запланированное улучшение | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Ограничить sysctls | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Ограничить AppArmor | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Запретить SELinux | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |
| Ограничить автомонтирование токена service account[9](#fn-2-9-def) | CIS 5.1.6 | Исключение | Исключение | Исключение | Исключение | Исключение | Исключение | Исключение |
| Тип монтирования /proc | PSSB | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается | Соблюдается |

1

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
OneAgent Log Module: LogAgent должен работать как привилегированный контейнер в кластере OCP, чтобы получить доступ к своему постоянному хранилищу. [Постоянное хранилище OCP с использованием hostPath](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

2

OneAgent: требуется для init-контейнеров, которые инструментируют процессы до запуска.  
OneAgent Log Module: `AllowPrivilegeEscalation` всегда имеет значение true, когда контейнер запущен как привилегированный. [Настройка Security Context для пода или контейнера](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

3

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для выполнения проверок конфигурации и безопасности; оценка ограничения hostPath запланирована.

4

OneAgent: требует ограниченных возможностей Linux (например, NET\_RAW) для наблюдаемости сети.  
KSPM: KSPM требует определённых возможностей Linux для сканирования и сбора данных о конфигурации системы и безопасности; это сделано намеренно и не может быть удалено.  
OneAgent Log Module: LogAgent нужна дополнительная возможность для получения доступа ко всем отслеживаемым файлам логов.

5

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для сканирования на уровне узла; рассматривается улучшение для ограничения монтируемых путей.  
OneAgent Log Module: нужен доступ к файлам логов в файловой системе хоста.

6

OneAgent: использует сетевое пространство имён хоста для мониторинга сетевого трафика.

7

OneAgent: использует пространство имён PID хоста для сопоставления метрик процессов.  
KSPM: KSPM требует доступа к пространству имён PID хоста, чтобы сборщик узла собирал данные на уровне процессов. Это требование будет задокументировано.

8

OneAgent: использует профиль seccomp среды выполнения по умолчанию; явная настройка запланирована.  
ActiveGate: ActiveGate работает с минимальными повышенными привилегиями для управления входящими подключениями.  
EdgeConnect: у EdgeConnect сейчас отсутствует явный профиль seccomp; его добавление запланировано в будущих выпусках. Эта мера будет реализована в ближайших выпусках.  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для выполнения проверок конфигурации и безопасности; оценка ограничения hostPath запланирована.  
OneAgent Log Module: профиль seccomp можно задать через DynaKube, чтобы работать в режиме secure computing.

9

Компонентам OneAgent, Extensions Controller, Dynatrace Collector, ActiveGate, EdgeConnect и KSPM необходимо взаимодействовать с Kubernetes API.

10

OneAgent Log Module: лимиты сильно зависят от объёма обрабатываемых данных. Можно задать через DynaKube.

**Запланированное улучшение**:  
Запретить монтирование секретов как переменной окружения: Dynatrace Collector сейчас использует переменные окружения для токенов; запланирован переход на файлы секретов.

## Политики Pod security

Раньше эти разрешения управлялись с помощью **PodSecurityPolicy** (PSP), но [в Kubernetes версии 1.25 PSP будут удалены](https://dt-url.net/2403pxy) из следующих компонентов:

* [Dynatrace Operator](https://dt-url.net/d7034gj) версии 0.2.2
* **LEGACY** [Dynatrace OneAgent Operator](https://dt-url.net/3023pvs) версии 0.11.0
* [Соответствующие Helm charts](https://dt-url.net/rp43pl1)

**Dynatrace Operator версии 0.2.1** является последней версией, в которой PSP применяются по умолчанию, поэтому применение этих правил остаётся за вами. В качестве альтернатив PSP можно использовать другие инструменты применения политик, такие как:

* [k-rail](https://dt-url.net/qx63p3n)
* [Kyverno](https://dt-url.net/6m83ppk)
* [Gatekeeper](https://dt-url.net/aha3ps4)

Если вы решите использовать альтернативу PSP, обязательно предоставьте необходимые разрешения компонентам Dynatrace.

## Dynatrace Operator security context constraints

Dynatrace Operator версии 0.12.0+

Начиная с Dynatrace Operator версии 0.12.0, встроенное создание пользовательских security context constraints (SCC) удалено для Dynatrace Operator и компонентов, управляемых Dynatrace Operator. Это изменение было сделано, чтобы уменьшить осложнения, вызываемые пользовательскими SCC в уникальных конфигурациях OpenShift.

Несмотря на это обновление, компоненты сохраняют те же разрешения и требования безопасности, что и раньше.

В следующих таблицах показаны SCC, используемые в разных версиях Dynatrace Operator и OpenShift.

| Запрашиваемые ресурсы | Пользовательский SCC, используемый в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift ранее 4.11 |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

| Запрашиваемые ресурсы | Пользовательский SCC, используемый в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift 4.11+ |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

1

Этот SCC является единственным встроенным SCC OpenShift, который разрешает использование seccomp, заданного нашими компонентами по умолчанию, а также использование томов CSI.

По-прежнему можно создавать собственные более или менее ограничительные SCC, учитывающие вашу конкретную конфигурацию. Старые SCC, созданные предыдущей версией Dynatrace Operator, можно безопасно удалить.

Чтобы удалить старые SCC, используйте следующую команду:

```
oc delete scc <scc-name>
```