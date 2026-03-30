---
title: Безопасность Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/security
scraped: 2026-03-02T21:18:55.414129
---

Наблюдаемость Kubernetes основана на компонентах с различными назначениями, конфигурациями по умолчанию и разрешениями. Этим компонентам необходимы разрешения для выполнения и поддержания работоспособности Dynatrace в вашем кластере.

Хотя разрешения Dynatrace соответствуют принципу минимальных привилегий, обязательно защитите пространство имён `dynatrace` и ограничьте доступ закрытой группой администраторов и операторов.

## Список разрешений

### Dynatrace Operator

**Назначение:** Управляет жизненным циклом компонентов Dynatrace. Заменяет OneAgent Operator.

**Конфигурация по умолчанию:** `1-replica-per-cluster`

**Объекты RBAC**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/Update/Delete/List | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
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

### Сервер вебхуков Dynatrace Operator

**Назначение**:

* Модифицирует определения подов для включения модулей кода Dynatrace для наблюдаемости приложений
* Валидирует пользовательские ресурсы DynaKube
* Обрабатывает конвертацию DynaKube между версиями

**Конфигурация по умолчанию**: `1-replica-per-cluster`, может масштабироваться

**Объекты RBAC**:

* Service Account `dynatrace-webhook`
* Cluster-Role `dynatrace-webhook`
* Role `dynatrace-webhook`

#### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/List/Watch/Update | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `replicationcontrollers` | `""` | Get |  |
| `replicasets` | `apps` | Get |  |
| `statefulsets` | `apps` | Get |  |
| `daemonsets` | `apps` | Get |  |
| `deployments` | `apps` | Get |  |
| `jobs` | `batch` | Get |  |
| `cronjobs` | `batch` | Get |  |
| `deploymentconfigs` | `apps.openshift.io` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `events` | `""` | Create/Patch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |

### CSI-драйвер Dynatrace Operator

**Назначение**:

* Для конфигураций `applicationMonitoring` предоставляет необходимый бинарный файл OneAgent для мониторинга приложений подам на каждом узле.
* Для конфигураций `hostMonitoring` предоставляет доступную для записи папку для конфигураций OneAgent при использовании файловой системы хоста в режиме «только чтение».
* Для `cloudNativeFullStack` предоставляет оба вышеперечисленных варианта.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-oneagent-csi-driver`
* Cluster-Role `dynatrace-oneagent-csi-driver`
* Role `dynatrace-oneagent-csi-driver`

#### Разрешение на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get/List/Create/Delete/Watch |  |
| `events` | `""` | Create/Patch |  |

### ActiveGate

#### Мониторинг платформы Kubernetes

**Назначение**: собирает метрики кластера и рабочих нагрузок, события и статус из Kubernetes API.

**Конфигурация по умолчанию**: `1-replica-per-cluster`, может масштабироваться

**Объекты RBAC**:

* Service Account: `dynatrace-kubernetes`
* Cluster-Roles:

  + `dynatrace-kubernetes-monitoring`

    - Используется для агрегации всех ClusterRoles с меткой `rbac.dynatrace.com/aggregate-to-monitoring: "true"`
  + `dynatrace-kubernetes-monitoring-default`

    - Агрегируется через `dynatrace-kubernetes-monitoring`, подробности см. в документации по агрегации ClusterRole

##### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
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
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Назначение**: Kubernetes Security Posture Management обнаруживает, анализирует и непрерывно отслеживает ошибки конфигурации, рекомендации по усилению безопасности и потенциальные нарушения соответствия в Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-node-config-collector`
* Cluster-Role `dynatrace-kubernetes-monitoring-kspm`

  + Агрегируется через ClusterRole `dynatrace-kubernetes-monitoring`, подробности см. в документации по агрегации ClusterRole

##### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
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

**Назначение**:

* Собирает метрики хоста с узлов Kubernetes.
* Обнаруживает новые контейнеры и внедряет модули кода Dynatrace в поды приложений с использованием классической инъекции полного стека. Необязательно
* Собирает логи контейнеров с узлов Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-logmonitoring`

**Настройки политики**: Разрешает **HostNetwork**, **HostPID**, использование любых типов томов.

**Необходимые capabilities**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, `FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, `SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`

#### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes/proxy` | `""` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Модуль логов Dynatrace

**Назначение**:

* Собирает логи контейнеров с узлов Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-logmonitoring`
* Cluster-Role `dynatrace-logmonitoring`

#### Разрешения на уровне кластера

Мониторинг логов требует [те же разрешения на уровне кластера, что и OneAgent](#oneagent-permissions).

### Приём телеметрии Dynatrace

**Назначение**:

* Включение эндпоинтов телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере

  + Приём данных через эндпоинты [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger](https://www.jaegertracing.io/), [StatsD](https://github.com/statsd/statsd) или [Zipkin](https://zipkin.io/)
* Анализ контекстно-обогащённых данных с помощью встроенных приложений, DQL, Notebooks и Dashboards

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | Get/Watch/List |  |
| `namespaces` | `""` | Get/Watch/List |  |
| `nodes` | `""` | Get/Watch/List |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Расширения

**Назначение**:

* Расширения расширяют аналитические возможности Dynatrace, принимая данные из различных источников, таких как сторонние приложения, сервисы и пользовательские метрики. Подробнее см. Расширения.

**Конфигурация по умолчанию**:

Следующие компоненты необходимы независимо от используемых расширений:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**Объекты RBAC**:

В зависимости от используемого расширения требуются следующие объекты RBAC.

* Service Accounts

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Разрешения пространства имён `dynatrace`

*Расширение Prometheus*

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Расширение базы данных*

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Расширение Prometheus

**Назначение**:

* Собирает метрики с эндпоинтов Prometheus в вашем кластере.

**Конфигурация по умолчанию**:

* Источник данных Prometheus: `replicas-set-in-dynakube` (значение по умолчанию отсутствует, реплики задаются в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-extensions-prometheus`

##### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
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

#### Расширение базы данных

**Назначение**:

* Собирает метрики с эндпоинтов баз данных в вашем кластере.

**Конфигурация по умолчанию**:

* SQL Extension Executor: `replicas-set-in-dynakube` (значение по умолчанию отсутствует, реплики задаются в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-sql-ext-exec`
* Roles

  + `dynatrace-sql-ext-exec`

##### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Поддерживаемость Dynatrace Operator

**Назначение**:

* Позволяет Dynatrace Operator выполнять команду support-archive. Необходимо для устранения неполадок, связанных с Operator.

**Объекты RBAC**:

* Role `dynatrace-operator-supportability`

**Отключение**:

* Вы можете отключить эту функцию, установив значение `rbac.supportability` в Helm-чарте Dynatrace Operator в `false`.

Отключение этой функции затруднит предоставление необходимой информации при открытии обращений в службу поддержки по вопросам Dynatrace Operator.

#### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get/List |  |

### Поддержка обновления API Dynatrace Operator

**Назначение**:

* Запуск задания `dynatrace-operator-crd-storage-migration` для автоматической очистки удалённых версий API Dynakube в хуке Helm `pre-upgrade`.

**Объекты RBAC**:

* ClusterRole `dynatrace-crd-storage-migration`
* Role `dynatrace-crd-storage-migration`
* ServiceAccount `dynatrace-crd-storage-migration`

**Включение**:

* Вы можете отключить эту функцию, установив значение `crdStorageMigrationJob` в Helm-чарте Dynatrace Operator в `false`.

#### Разрешения на уровне кластера

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Разрешения пространства имён `dynatrace`

| Доступные ресурсы | Группа API | Используемые API | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |

## Средства контроля безопасности компонентов Dynatrace Operator

В следующей таблице представлен подробный анализ средств контроля безопасности для компонентов Kubernetes: Dynatrace Operator, вебхук Dynatrace Operator и CSI-драйвер Dynatrace Operator. Этот отчёт основан на:

* [CIS Benchmark](https://dt-url.net/zd0368p) — всемирно признанном стандарте для обеспечения безопасности развёртываний Kubernetes.
* [Политиках POD Security Standard](https://dt-url.net/mp0345l).
* Лучших практиках.

| Средство контроля безопасности | Стандарт (\*) | Operator | Webhook | CSI driver | OneAgent | Extensions Controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Запрет привилегированных контейнеров | CIS [1](#fn-1-1-def) 5.2.2 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Запрет повышения привилегий | CIS [1](#fn-1-1-def) 5.2.6 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [11](#fn-1-11-def) | Satisfied | Required [16](#fn-1-16-def) | Satisfied | Satisfied | Satisfied |
| Запрет запуска контейнеров от имени root | CIS [1](#fn-1-1-def) 5.2.7 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [6](#fn-1-6-def) | Required [10](#fn-1-10-def) | Satisfied | Required [16](#fn-1-16-def) | Required [18](#fn-1-18-def) | Satisfied | Required [19](#fn-1-19-def) |
| Запрет использования избыточных или небезопасных capabilities | CIS [1](#fn-1-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [12](#fn-1-12-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Satisfied | Required [24](#fn-1-24-def) |
| Ограничение доступа к секретам (RBAC) | CIS [1](#fn-1-1-def) 5.1.4 | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Запрет использования томов HostPath | CIS [1](#fn-1-1-def) 5.2.12 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [7](#fn-1-7-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [20](#fn-1-20-def) |
| Запрет использования HostPorts | CIS [1](#fn-1-1-def) 5.2.13 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Запрет доступа к сети хоста | CIS [1](#fn-1-1-def) 5.2.5 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [13](#fn-1-13-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Запрет использования host PID | CIS [1](#fn-1-1-def) 5.2.3 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [14](#fn-1-14-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [23](#fn-1-23-def) |
| Запрет использования host IPC | CIS [1](#fn-1-1-def) 5.2.4 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Требование readOnlyRootFilesystem | Лучшая практика | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Требование лимитов ресурсов | Лучшая практика | Satisfied | Satisfied | Satisfied [9](#fn-1-9-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Требование использования seccomp (минимум default/runtime) | CIS [1](#fn-1-1-def) 5.7.2 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [15](#fn-1-15-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Required [21](#fn-1-21-def) | Required [19](#fn-1-19-def) |
| Запрет секретов, монтированных как переменные окружения | CIS [1](#fn-1-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Planned improvement [17](#fn-1-17-def) | Satisfied | Satisfied | Satisfied |
| Ограничение sysctls | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Ограничение AppArmor | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Запрет SELinux | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [8](#fn-1-8-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Ограничение автомонтирования токена сервисного аккаунта | CIS [1](#fn-1-1-def) 5.1.6 | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) |
| Тип монтирования /proc | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |

**Стандарт**:

1

[Center for Internet Security (CIS) Kubernetes benchmark](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profile](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profile](https://dt-url.net/ut4387d).

**Общее**:

4

Компоненту необходимо взаимодействовать с Kubernetes API.

**CSI**:

5

CSI-драйверу требуются повышенные разрешения для создания и управления монтированиями на хост-системе. Подробнее см. Привилегии CSI-драйвера.

6

CSI-драйвер взаимодействует с kubelet через сокет на хосте; для доступа к этому сокету CSI-драйвер должен запускаться от имени root.

7

CSI-драйвер сохраняет/кеширует бинарные файлы OneAgent в файловой системе хоста; для этого ему необходимо монтирование hostVolume.

8

CSI-драйверу необходим уровень seLinux s0, чтобы поды приложений могли видеть файлы из тома, созданного CSI-драйвером.

9

Провизионер CSI-драйвера не имеет лимитов ресурсов по умолчанию для обеспечения наилучшей производительности при провизионировании; лимиты могут быть установлены через значения Helm-чарта.

**OneAgent**:

10

DaemonSet OneAgent запускается с привилегиями уровня хоста для полной видимости (сеть, процессы, файловая система).

11

Требуется для init-контейнеров, которые инструментируют процессы перед запуском.

12

Требуются ограниченные Linux capabilities (например, NET\_RAW) для наблюдаемости сети.

13

Использует пространство имён сети хоста для мониторинга сетевого трафика.

14

Использует пространство имён PID хоста для корреляции метрик процессов.

15

Использует профиль seccomp среды выполнения по умолчанию; явная настройка запланирована.

**Extension Execution Controller / Dynatrace Collector**:

16

Dynatrace Collector и контроллер расширений могут требовать привилегии root или повышенные привилегии для сбора метрик и операций sidecar.

17

Dynatrace Collector в настоящее время использует переменные окружения для токенов; миграция на файлы секретов запланирована.

**ActiveGate / EdgeConnect / KSPM**:

18

ActiveGate запускается с минимальными повышенными привилегиями для управления входящими подключениями.

19

KSPM монтирует корневую файловую систему хоста `/` для выполнения сканирования конфигурации и безопасности; оценка ограничения hostPath запланирована.

20

KSPM монтирует всю файловую систему хоста для сканирования на уровне узла; рассматривается улучшение для ограничения монтируемых путей.

21

EdgeConnect в настоящее время не имеет явного профиля seccomp; его добавление запланировано в будущих выпусках. Этот контроль рассматривается в предстоящих выпусках.

22

Роли на уровне пространства имён для Operator, Webhook и CSI-драйвера в настоящее время разрешают доступ ко всем секретам в их пространстве имён. Запланировано улучшение для ограничения этих ролей конкретными именами секретов, в соответствии с конфигурацией ClusterRole.

23

KSPM требуется доступ к пространству имён host PID для сборщика узлов, чтобы собирать данные на уровне процессов. Это требование будет задокументировано.

24

KSPM требуются определённые Linux capabilities для сканирования и сбора данных конфигурации и безопасности системы; это сделано намеренно и не может быть удалено.

## Средства контроля безопасности компонентов, управляемых Dynatrace Operator

В следующей таблице представлен подробный анализ средств контроля безопасности для компонентов Kubernetes, управляемых Dynatrace Operator: ActiveGate, OneAgent (CloudNative), LogAgent. Этот отчёт основан на:

* [CIS Benchmark](https://dt-url.net/zd0368p) — всемирно признанном стандарте для обеспечения безопасности развёртываний Kubernetes.
* [Политиках POD Security Standard](https://dt-url.net/mp0345l).
* Лучших практиках.

| Средство контроля безопасности | Стандарт (\*) | ActiveGate | OneAgent CloudNative | Модуль логов OneAgent |
| --- | --- | --- | --- | --- |
| Запрет привилегированных контейнеров | CIS [1](#fn-2-1-def) 5.2.2 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Required [15](#fn-2-15-def) |
| Запрет повышения привилегий | CIS [1](#fn-2-1-def) 5.2.6 / PSSR [3](#fn-2-3-def) | Satisfied | Required [6](#fn-2-6-def) | Required [16](#fn-2-16-def) |
| Запрет запуска контейнеров от имени root | CIS [1](#fn-2-1-def) 5.2.7 / PSSR [3](#fn-2-3-def) | Satisfied | Satisfied | Satisfied |
| Запрет использования избыточных или небезопасных capabilities | CIS [1](#fn-2-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-2-3-def) | Satisfied | Required [7](#fn-2-7-def) | Required [17](#fn-2-17-def) |
| Запрет использования томов HostPath | CIS [1](#fn-2-1-def) 5.2.12 / PSSB [2](#fn-2-2-def) | Satisfied | Required [8](#fn-2-8-def) | Required [18](#fn-2-18-def) |
| Запрет использования HostPorts | CIS [1](#fn-2-1-def) 5.2.13 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Запрет доступа к сети хоста | CIS [1](#fn-2-1-def) 5.2.5 / PSSB [2](#fn-2-2-def) | Satisfied | Required [9](#fn-2-9-def) | Satisfied |
| Запрет использования host PID | CIS [1](#fn-2-1-def) 5.2.3 / PSSB [2](#fn-2-2-def) | Satisfied | Required [10](#fn-2-10-def) | Satisfied |
| Запрет использования host IPC | CIS [1](#fn-2-1-def) 5.2.4 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Требование readOnlyRootFilesystem | Лучшая практика | Satisfied | Satisfied | Satisfied |
| Требование лимитов ресурсов | Лучшая практика | Configurable [5](#fn-2-5-def) | Configurable [11](#fn-2-11-def) | Configurable [19](#fn-2-19-def) |
| Требование использования seccomp (минимум default/runtime) | CIS [1](#fn-2-1-def) 5.7.2 / PSSR [3](#fn-2-3-def) | Satisfied | Required [12](#fn-2-12-def) | Required [20](#fn-2-20-def) |
| Запрет секретов, монтированных как переменные окружения | CIS [1](#fn-2-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied |
| Ограничение sysctls | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Ограничение AppArmor | PSSB [2](#fn-2-2-def) | Satisfied | Required [13](#fn-2-13-def) | Satisfied |
| Запрет SELinux | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Ограничение автомонтирования токена сервисного аккаунта | CIS [1](#fn-2-1-def) 5.1.6 | Required [4](#fn-2-4-def) | Configurable [14](#fn-2-14-def) | Required [4](#fn-2-4-def) |
| Тип монтирования /proc | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |

**Стандарт**:

1

[Center for Internet Security (CIS) Kubernetes benchmark](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profile](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profile](https://dt-url.net/ut4387d).

**Общее**:

4

Компоненту необходимо взаимодействовать с Kubernetes API.

**ActiveGate**

5

Лимиты в значительной степени зависят от объёма обрабатываемых данных. Могут быть установлены через DynaKube.

**OneAgent**

6

Повышение привилегий необходимо для процессов внутри контейнера OneAgent для получения Linux capabilities.

7

[Действия мониторинга](../../dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux.md#operation "Узнайте о безопасности Dynatrace OneAgent и изменениях в вашей Linux-системе"), выполняемые процессами OneAgent, требуют следующих [capabilities](../../dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged.md#linux-system-capabilities "Узнайте, когда Dynatrace OneAgent требует привилегий root в Linux.").

8

Смонтированная корневая файловая система хоста используется всеми модулями OneAgent и обеспечивает доступ к файлам логов, метрикам диска и другим возможностям мониторинга хоста и процессов.

9

OneAgent требуется доступ к пространству имён сети хоста для обеспечения мониторинга сетевого состояния на уровне хоста и процессов.

10

OneAgent требуется доступ к таблице процессов хоста для сбора метрик производительности всех процессов, запущенных на хосте.

11

Лимиты в значительной степени зависят от объёма обрабатываемых данных. Могут быть установлены через DynaKube.

12

OneAgent требуется доступ к системным вызовам ядра за пределами набора RuntimeDefault для целей мониторинга.

13

OneAgent требуется доступ к команде mount, которая заблокирована профилем AppArmor по умолчанию.

14

Компоненту OneAgent необходимо взаимодействовать с эндпоинтом kubelet `/pods`. Токен K8s не монтируется в под, если LogMonitoring отключён через значения Helm.

**Модуль логов OneAgent**:

15

LogAgent должен запускаться как привилегированный контейнер в кластере OCP для доступа к его постоянному хранилищу. [Постоянное хранилище OCP с использованием hostPath](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

16

AllowPrivilegeEscalation всегда имеет значение true, когда контейнер запускается как привилегированный. [Настройка контекста безопасности для пода или контейнера](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

17

LogAgent требуется дополнительный capability для доступа ко всем отслеживаемым файлам логов.

18

Требуется доступ к файлам логов в файловой системе хоста.

19

Лимиты в значительной степени зависят от объёма обрабатываемых данных. Могут быть установлены через DynaKube.

20

Профиль seccomp может быть задан через DynaKube для запуска в режиме безопасных вычислений.

## Политики безопасности подов

Ранее эти разрешения управлялись с помощью **PodSecurityPolicy** (PSP), но [в Kubernetes версии 1.25 PSP будут удалены](https://dt-url.net/2403pxy) из следующих компонентов:

* [Dynatrace Operator](https://dt-url.net/d7034gj) версии 0.2.2
* **УСТАРЕВШИЙ** [Dynatrace OneAgent Operator](https://dt-url.net/3023pvs) версии 0.11.0
* [Соответствующие Helm-чарты](https://dt-url.net/rp43pl1)

**Dynatrace Operator версии 0.2.1** — последняя версия, в которой PSP применяются по умолчанию, поэтому обеспечение соблюдения этих правил зависит от вас. В качестве альтернатив PSP вы можете использовать другие инструменты принудительного применения политик, такие как:

* [k-rail](https://dt-url.net/qx63p3n)
* [Kyverno](https://dt-url.net/6m83ppk)
* [Gatekeeper](https://dt-url.net/aha3ps4)

Если вы решите использовать альтернативу PSP, убедитесь, что компонентам Dynatrace предоставлены необходимые разрешения.

## Безопасность Dynatrace Operator context constraints

Dynatrace Operator версии 0.12.0+

Начиная с Dynatrace Operator версии 0.12.0, встроенное создание пользовательских ограничений контекста безопасности (SCC) было удалено для Dynatrace Operator и компонентов, управляемых Dynatrace Operator. Это изменение было сделано для уменьшения сложностей, вызванных пользовательскими SCC в уникальных конфигурациях OpenShift.

Несмотря на это обновление, компоненты сохраняют те же разрешения и требования безопасности, что и раньше.

В следующих таблицах показаны SCC, используемые в различных версиях Dynatrace Operator и OpenShift.

| Доступные ресурсы | Пользовательский SCC в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift ранее 4.11 |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |
| Сервер вебхуков Dynatrace Operator | `dynatrace-webhook` | `privileged`[1](#fn-3-1-def) |
| CSI-драйвер Dynatrace Operator | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

| Доступные ресурсы | Пользовательский SCC в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift 4.11+ |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |
| Сервер вебхуков Dynatrace Operator | `dynatrace-webhook` | `nonroot-v2` |
| CSI-драйвер Dynatrace Operator | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

1

Этот SCC является единственным встроенным SCC OpenShift, который разрешает использование seccomp (что установлено по умолчанию для наших компонентов), а также использование томов CSI.

Вы по-прежнему можете создавать собственные более разрешительные или ограничительные SCC с учётом вашей конкретной конфигурации. Старые SCC, созданные предыдущей версией Dynatrace Operator, можно безопасно удалить.

Для удаления старых SCC используйте следующую команду:

```
oc delete scc <scc-name>
```
