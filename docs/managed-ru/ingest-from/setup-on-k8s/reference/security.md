---
title: Безопасность Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/security
---

# Безопасность Dynatrace Operator

# Безопасность Dynatrace Operator

* Справка
* Чтение: 16 мин
* Обновлено 20 мая 2026 г.

Наблюдаемость Kubernetes опирается на компоненты с разными назначениями, конфигурациями по умолчанию и правами доступа. Этим компонентам нужны права для выполнения и поддержания рабочих функций Dynatrace в кластере.

Хотя права Dynatrace соответствуют принципу минимально необходимых привилегий, нужно защитить пространство имён `dynatrace` и ограничить доступ к нему закрытой группой администраторов и операторов.

## Права на развёртывание

Установка и обновление Dynatrace Operator требуют административных привилегий. Если не используется кластерная роль `cluster-admin`, нужно убедиться, что у субъекта, выполняющего развёртывание, есть права, перечисленные в этом разделе. Требуемые права также включают `patch` для поддержки `helm upgrade` и права на управление пользовательскими ресурсами `DynaKube` и `EdgeConnect`.

Эти права требуются только для развёртывания (установки) Operator. Права, необходимые во время выполнения, см. в разделе [Список прав](#permission-list).

### Ресурсы уровня кластера

Пользователь или сервисный аккаунт, выполняющий развёртывание, должен иметь возможность **создавать, обновлять, применять патчи и удалять** следующие типы ресурсов уровня кластера:

| Тип ресурса | Группа API | Глаголы | Имена ресурсов | Примечания |
| --- | --- | --- | --- | --- |
| `CustomResourceDefinition` | `apiextensions.k8s.io` | `create`, `update`, `patch`, `delete` | `dynakubes.dynatrace.com`, `edgeconnects.dynatrace.com` | Требуется для установки CRD Dynatrace |
| `ClusterRole` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete`, `escalate`, `bind` |  | **Важно:** требуются права `escalate` или эквивалентные. См. [Глаголы RBAC для развёртывания](#deployment-rbac-verbs). |
| `ClusterRoleBinding` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |  |  |
| `MutatingWebhookConfiguration` | `admissionregistration.k8s.io` | `create`, `update`, `patch`, `delete` | `dynatrace-webhook` |  |
| `ValidatingWebhookConfiguration` | `admissionregistration.k8s.io` | `create`, `update`, `patch`, `delete` | `dynatrace-webhook` |  |
| `CSIDriver` | `storage.k8s.io` | `create`, `update`, `patch`, `delete` |  | Требуется для CSI-драйвера |
| `PriorityClass` | `scheduling.k8s.io` | `create`, `update`, `patch`, `delete` |  | Требуется для CSI-драйвера |
| `Namespace` | `""` | `create` |  | Требуется для `helm install --create-namespace` |

### Ресурсы уровня пространства имён

Пользователь или сервисный аккаунт, выполняющий развёртывание, должен иметь возможность **создавать, обновлять, применять патчи и удалять** следующие типы ресурсов в пространстве имён оператора:

| Тип ресурса | Группа API | Глаголы |
| --- | --- | --- |
| `ServiceAccount` | `""` | `create`, `update`, `patch`, `delete` |
| `Role` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |
| `RoleBinding` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |
| `Deployment` | `apps` | `create`, `update`, `patch`, `delete` |
| `DaemonSet` | `apps` | `create`, `update`, `patch`, `delete` |
| `Service` | `""` | `create`, `update`, `patch`, `delete` |
| `Secret` | `""` | `create`, `update`, `patch`, `delete` |
| `ConfigMap` | `""` | `create`, `update`, `patch`, `delete` |
| `PodDisruptionBudget` | `policy` | `create`, `update`, `patch`, `delete` |
| `DynaKube` | `dynatrace.com` | `create`, `update`, `patch`, `delete` |
| `EdgeConnect` | `dynatrace.com` | `create`, `update`, `patch`, `delete` |
| `Job` | `batch` | `create`, `update`, `patch`, `delete` |

Ссылки на манифесты ClusterRole для развёртывания Dynatrace Operator см. в разделе [Глаголы RBAC для развёртывания](#deployment-rbac-verbs).

### Специфичные для платформы ресурсы

В зависимости от целевой платформы, чарт Helm создаёт дополнительные ресурсы, для которых требуются дополнительные права у пользователя, выполняющего развёртывание.

#### GKE Autopilot

В кластерах GKE Autopilot чарт Helm автоматически обнаруживает группу API `auto.gke.io/v1/AllowlistSynchronizer` и создаёт ресурс `AllowlistSynchronizer` в качестве pre-install хука Helm. Это добавляет в allowlist CSI-драйвер, мониторинг логов и рабочие нагрузки CSI-задач, необходимые оператору.

Пользователю или сервисному аккаунту, выполняющему развёртывание, требуется следующее дополнительное право:

| Группа API | Ресурс | Глаголы |
| --- | --- | --- |
| `auto.gke.io` | `allowlistsynchronizers` | `create`, `get`, `update`, `patch`, `delete`, `list` |

#### OpenShift

В кластерах OpenShift (обнаруживаются по группе API `security.openshift.io/v1` или по параметру `--set platform=openshift`) чарт Helm создаёт дополнительные ClusterRole, предоставляющие доступ `use` к SecurityContextConstraints (`privileged`, `nonroot`, `nonroot-v2`). Если используется рекомендуемый подход `escalate`, описанный в разделе [Глаголы RBAC для развёртывания](#deployment-rbac-verbs), дополнительные права у пользователя, выполняющего развёртывание, не требуются.

### Глаголы RBAC для развёртывания: `bind` и `escalate`

Kubernetes применяет [предотвращение эскалации привилегий﻿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping): нельзя создать ClusterRole, предоставляющую права, которых у пользователя ещё нет, и нельзя создать ClusterRoleBinding, ссылающийся на ClusterRole с правами, которых у пользователя нет.

Чарт Helm Dynatrace Operator создаёт несколько ClusterRole (например, для чтения узлов, подов и метрик). Аккаунту, выполняющему развёртывание, нужна возможность создавать эти ClusterRole и их привязки. Есть два подхода:

Приведённые ниже примеры манифестов ClusterRole для аккаунта развёртывания включают права на управление пользовательскими ресурсами `DynaKube` и `EdgeConnect`. Предполагается, что тот же сервисный аккаунт, который используется для развёртывания Operator, используется и для развёртывания пользовательских ресурсов, настраивающих его. В примеры также включены специфичные для платформы ресурсы для GKE Autopilot и OpenShift.

Эти примеры манифестов соответствуют правам для **текущей** версии Operator. При обновлении до новой версии Operator нужно использовать манифесты из соответствующего [тега релиза﻿](https://github.com/Dynatrace/dynatrace-operator/tags).

#### Вариант A: использование `escalate` и `bind`

Предоставить аккаунту развёртывания глаголы `escalate` и `bind` на ресурсах RBAC. Это подход с низкими затратами на обслуживание, так как права аккаунта развёртывания не нужно обновлять при изменении ClusterRole Operator между версиями.

* **`escalate`** для `clusterroles` разрешает создавать или обновлять объекты ClusterRole, содержащие права, которых нет у аккаунта развёртывания. Это **не** предоставляет эти права самому аккаунту развёртывания, а лишь разрешает управлять ресурсами ClusterRole.
* **`bind`** для `clusterroles` и `clusterrolebindings` разрешает создавать ClusterRoleBinding, ссылающиеся на ClusterRole с правами, которых нет у аккаунта развёртывания.

Предоставление `escalate` и `bind` отключает для аккаунта развёртывания предотвращение эскалации привилегий Kubernetes, то есть он сможет создавать ClusterRole с любыми правами и привязывать их к любому субъекту. Эти риски можно снизить, используя политики допуска (admission control), ограничивающие, какие ClusterRole и ClusterRoleBinding может создавать аккаунт развёртывания.

Пример манифеста ClusterRole для аккаунта развёртывания (включает права для CSI-драйвера, GKE Autopilot и OpenShift):

[С CSI-драйвером﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/assets/samples/deployer/deployer-clusterrole-with-csi.yaml)

Если CSI-драйвер не развёртывается, нужно использовать вариант [Без CSI-драйвера﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/assets/samples/deployer/deployer-clusterrole-no-csi.yaml), он не содержит прав `CSIDriver` и `PriorityClass`.

#### Вариант B: расширенные права, если `escalate` или `bind` запрещены

Если политики безопасности запрещают глаголы `escalate` или `bind`, аккаунт развёртывания должен уже обладать всеми правами, которые предоставляют ClusterRole Operator во время выполнения. Это означает перечисление всех прав Dynatrace Operator в ClusterRole аккаунта развёртывания, чтобы предотвращение эскалации Kubernetes никогда не срабатывало.

ClusterRole без escalate напрямую предоставляет все права времени выполнения: чтение и запись секретов, pods/exec, изменение webhook, управление DaemonSet и другие. Из-за этого сам аккаунт развёртывания становится субъектом с высокими привилегиями и широким доступом к кластеру. Всё равно рекомендуется использовать политики допуска, ограничивающие, какие ресурсы RBAC может создавать аккаунт развёртывания.

Пример манифеста ClusterRole для аккаунта развёртывания (без escalate, включает права для CSI-драйвера, GKE Autopilot и OpenShift):

[С CSI-драйвером﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/assets/samples/deployer/deployer-clusterrole-no-escalate-with-csi.yaml)

Если CSI-драйвер не развёртывается, нужно использовать вариант [Без CSI-драйвера﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.0/assets/samples/deployer/deployer-clusterrole-no-escalate-no-csi.yaml), он не содержит прав `CSIDriver` и `PriorityClass`.

## Список прав

### Dynatrace Operator

**Назначение:** поддерживает жизненный цикл компонентов Dynatrace. Заменяет OneAgent Operator.

**Конфигурация по умолчанию:** `1-replica-per-cluster`

**Объекты RBAC**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Разрешения на уровне кластера

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes` | `""` | Get, List, Watch |  |
| `namespaces` | `""` | Get, List, Watch, Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get, Update, Delete, List | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get, Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get, Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Разрешения в пространстве имён `dynatrace`

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch, Update |  |
| `edgeconnects` | `dynatrace.com` | Get, List, Watch, Update |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |
| `dynakubes/status` | `dynatrace.com` | Update |  |
| `edgeconnects/status` | `dynatrace.com` | Update |  |
| `statefulsets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `daemonsets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `replicasets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `deployments` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `deployments/finalizers` | `apps` | Update |  |
| `configmaps` | `""` | Get, List, Watch, Create, Update, Delete |  |
| `pods` | `""` | Get, List, Watch |  |
| `secrets` | `""` | Get, List, Watch, Create, Update, Delete |  |
| `events` | `""` | Create, Get, List, Patch |  |
| `services` | `""` | Create, Update, Delete, Get, List, Watch |  |
| `serviceentries` | `networking.istio.io` | Get, List, Create, Update, Delete |  |
| `virtualservices` | `networking.istio.io` | Get, List, Create, Update, Delete |  |
| `leases` | `coordination.k8s.io` | Get, Update, Create |  |

### Dynatrace Operator Webhook Server

**Назначение**:

* изменяет определения подов, добавляя в них модули кода Dynatrace для application observability;
* проверяет пользовательские ресурсы DynaKube;
* обрабатывает преобразование DynaKube между версиями.

**Конфигурация по умолчанию**: `1-replica-per-cluster`, можно масштабировать

**Объекты RBAC**:

* Service Account `dynatrace-webhook`
* Cluster-Role `dynatrace-webhook`
* Role `dynatrace-webhook`

#### Разрешения на уровне кластера

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get, List, Watch, Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get, List, Watch, Update | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
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

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `events` | `""` | Create, Patch |  |
| `secrets` | `""` | Get, List, Watch |  |
| `configmaps` | `""` | Get, List, Watch |  |
| `dynakubes` | `dynatrace.com` | Get, List, Watch |  |

### Dynatrace Operator CSI driver

**Назначение**:

* для конфигураций `applicationMonitoring` предоставляет подам на каждом узле необходимый бинарный файл OneAgent для application monitoring;
* для конфигураций `hostMonitoring` предоставляет доступную для записи папку для конфигураций OneAgent, когда используется файловая система хоста, доступная только для чтения;
* для `cloudNativeFullStack` предоставляет оба варианта из перечисленных выше.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-oneagent-csi-driver`
* Cluster-Role `dynatrace-oneagent-csi-driver`
* Role `dynatrace-oneagent-csi-driver`

#### Разрешение на уровне кластера

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Разрешения в пространстве имён `dynatrace`

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch |  |
| `secrets` | `""` | Get, List, Watch |  |
| `configmaps` | `""` | Get, List, Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get, List, Create, Delete, Watch |  |
| `events` | `""` | Create, Patch |  |

### ActiveGate

#### Kubernetes Platform Monitoring

**Назначение**: сбор метрик, событий и статуса кластера и рабочих нагрузок из API Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-cluster`, можно масштабировать

**Объекты RBAC**:

* Service Account: `dynatrace-kubernetes`
* ClusterRole: `dynatrace-kubernetes-monitoring`

В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring` был агрегированной ClusterRole. Подробности см. в [ClusterRole aggregation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

##### Разрешения на уровне кластера

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `nodes` | `""` | List, Watch, Get |  |
| `pods` | `""` | List, Watch, Get |  |
| `namespaces` | `""` | List, Watch, Get |  |
| `replicationcontrollers` | `""` | List, Watch, Get |  |
| `events` | `""` | List, Watch, Get |  |
| `resourcequotas` | `""` | List, Watch, Get |  |
| `pods/proxy` | `""` | List, Watch, Get |  |
| `nodes/proxy` | `""` | List, Watch, Get |  |
| `nodes/metrics` | `""` | List, Watch, Get |  |
| `services` | `""` | List, Watch, Get |  |
| `persistentvolumeclaims` | `""` | List, Watch, Get |  |
| `persistentvolumes` | `""` | List, Watch, Get |  |
| `jobs` | `batch` | List, Watch, Get |  |
| `cronjobs` | `batch` | List, Watch, Get |  |
| `deployments` | `apps` | List, Watch, Get |  |
| `replicasets` | `apps` | List, Watch, Get |  |
| `statefulsets` | `apps` | List, Watch, Get |  |
| `daemonsets` | `apps` | List, Watch, Get |  |
| `deploymentconfigs` | `apps.openshift.io` | List, Watch, Get |  |
| `clusterversions` | `config.openshift.io` | List, Watch, Get |  |
| `dynakubes` | `dynatrace.com` | List, Watch, Get |  |
| `edgeconnects` | `dynatrace.com` | List, Watch, Get |  |
| `customresourcedefinitions` | `apiextensions.k8s.io` | List, Watch, Get |  |
| `ingresses` | `networking.k8s.io` | List, Watch, Get |  |
| `networkpolicies` | `networking.k8s.io` | List, Watch, Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Назначение**: [Kubernetes Security Posture Management](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") обнаруживает, анализирует и непрерывно отслеживает
неправильные конфигурации, рекомендации по усилению безопасности и потенциальные нарушения комплаенса в Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-node-config-collector`
* ClusterRole: `dynatrace-kubernetes-monitoring-kspm`

В Dynatrace Operator версии 1.8 `dynatrace-kubernetes-monitoring-kspm` агрегировался ClusterRole `dynatrace-kubernetes-monitoring`. Подробности см. в [ClusterRole aggregation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

##### Разрешения на уровне кластера

| Ресурсы | Группа API | Действия | Имена ресурсов |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get, List, Watch |  |
| `nodes` | `""` | Get, List, Watch |  |
| `pods` | `""` | Get, List, Watch |  |
| `replicationcontrollers` | `""` | Get, List, Watch |  |
| `serviceaccounts` | `""` | Get, List, Watch |  |
| `services` | `""` | Get, List, Watch |  |
| `cronjobs` | `batch` | Get, List, Watch |  |
| `jobs` | `batch` | Get, List, Watch |  |
| `daemonsets` | `apps` | Get, List, Watch |  |
| `deployments` | `apps` | Get, List, Watch |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `statefulsets` | `apps` | Get, List, Watch |  |
| `networkpolicies` | `networking.k8s.io` | Get, List, Watch |  |
| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `clusterroles` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `rolebindings` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `roles` | `rbac.authorization.k8s.io` | Get, List, Watch |  |

### OneAgent

**Назначение**:

* Собирает метрики хостов с узлов Kubernetes.
* Обнаруживает новые контейнеры и внедряет модули кода Dynatrace в поды приложений с помощью classic full-stack injection. Опционально.
* Собирает логи контейнеров с узлов Kubernetes.

**Конфигурация по умолчанию**: `1-replica-per-node` (развёртывается через DaemonSet)

**Объекты RBAC**:

* Service Account `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-logmonitoring`

**Настройки политики**: разрешает **HostNetwork**, **HostPID**, использование любых типов томов.

**Необходимые capabilities**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, `FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, `SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`

#### Права на уровне кластера

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
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

#### Права на уровне кластера

Log monitoring требует [те же права на уровне кластера, что и OneAgent](#oneagent-permissions).

### Dynatrace telemetry ingest

**Назначение**:

* Включить [эндпоинты приёма телеметрии Dynatrace](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") в Kubernetes для приёма данных локально в кластере

  + Приём данных через эндпоинты [OTLP﻿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger﻿](https://www.jaegertracing.io/), [StatsD﻿](https://github.com/statsd/statsd) или [Zipkin﻿](https://zipkin.io/)
* Анализ насыщенных контекстом данных с помощью встроенных приложений, DQL, Notebooks и Dashboards

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Права на уровне кластера

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | Get, Watch, List |  |
| `namespaces` | `""` | Get, Watch, List |  |
| `nodes` | `""` | Get, Watch, List |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Extensions

**Назначение**:

* Extensions расширяют аналитические возможности Dynatrace, принимая данные из различных источников, таких как сторонние приложения, сервисы и пользовательские метрики. Подробнее см. [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

**Конфигурация по умолчанию**:

Следующие компоненты необходимы независимо от того, какие extensions используются:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**Объекты RBAC**:

В зависимости от используемого extension требуются следующие объекты RBAC.

* Service Accounts

  + `dynatrace-extension-controller`
* ClusterRoles

  + `dynatrace-extension-controller`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Права на уровне кластера

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List, Watch |  |
| `services` | `""` | List, Watch |  |

##### Права в пространстве имён `dynatrace`

*Prometheus extension*

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Database extension*

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Prometheus extension

**Назначение**:

* Собирает метрики с эндпоинтов Prometheus в кластере.

**Конфигурация по умолчанию**:

* Prometheus datasource: `replicas-set-in-dynakube` (значения по умолчанию нет, число реплик задаётся в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-extensions-prometheus`

##### Права на уровне кластера

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | Get, List, Watch |  |
| `namespaces` | `""` | Get, List, Watch |  |
| `endpoints` | `""` | Get, List, Watch |  |
| `services` | `""` | Get, List, Watch |  |
| `nodes` | `""` | Get, List, Watch |  |
| `nodes/metrics` | `""` | Get, List, Watch |  |
| `deployments` | `apps` | Get, List, Watch |  |
| `daemonsets` | `apps` | Get, List, Watch |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `statefulsets` | `apps` | Get, List, Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Database extension

**Назначение**:

* Собирает метрики с эндпоинтов баз данных в кластере.

**Конфигурация по умолчанию**:

* SQL Extension Executor: `replicas-set-in-dynakube` (значения по умолчанию нет, число реплик задаётся в DynaKube)

**Объекты RBAC**:

* Service Accounts

  + `dynatrace-sql-ext-exec`
* Roles

  + `dynatrace-sql-ext-exec`

##### Права в пространстве имён `dynatrace`

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Поддерживаемость Dynatrace Operator

**Назначение**:

* Позволяет Dynatrace Operator выполнять [команду support-archive](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components."). Необходимо для устранения неполадок, связанных с Operator.

**Объекты RBAC**:

* Role `dynatrace-operator-supportability`

**Отказ от функции**:

* Эту функцию можно отключить, задав значению `rbac.supportability` Helm chart Dynatrace Operator значение `false`.

Отключение этой функции затруднит предоставление необходимой информации при открытии обращений в поддержку по вопросам Dynatrace Operator.

#### Права в пространстве имён `dynatrace`

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get, List |  |

### Поддержка обновления API Dynatrace Operator

**Назначение**:

* Запуск Job `dynatrace-operator-crd-storage-migration` для автоматической очистки удалённых версий API Dynakube в хуке `pre-upgrade` Helm.

**Объекты RBAC**:

* ClusterRole `dynatrace-crd-storage-migration`
* Role `dynatrace-crd-storage-migration`
* ServiceAccount `dynatrace-crd-storage-migration`

**Подключение функции**:

* Эту функцию можно отключить, задав значению `crdStorageMigrationJob` Helm chart Dynatrace Operator значение `false`.

#### Права на уровне кластера

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Права в пространстве имён `dynatrace`

| Ресурсы, к которым выполняется доступ | Группа API | Глаголы | Имена ресурсов |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch, Update |  |
| `edgeconnects` | `dynatrace.com` | Get, List, Watch, Update |  |

## Контроль безопасности компонентов Dynatrace Operator

В следующей таблице представлен подробный анализ элементов контроля безопасности для компонентов Kubernetes: Dynatrace Operator, вебхук Dynatrace Operator и CSI driver Dynatrace Operator. Отчёт основан на:

* [CIS Benchmark﻿](https://dt-url.net/zd0368p), общепризнанном мировом стандарте обеспечения безопасности развёртываний Kubernetes.
* [Политиках POD Security Standard﻿](https://dt-url.net/mp0345l).
* Лучших практиках.

**Стандарты и сокращения**:

* **CIS**: [Center for Internet Security (CIS) Kubernetes Benchmark﻿](https://dt-url.net/zd0368p).
* **PSSB**: [Pod Security Standards – Baseline profile﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).
* **PSSR**: [Pod Security Standards – Restricted profile﻿](https://dt-url.net/ut4387d).

Столбец **Standard** ссылается на эти сокращения.

### Dynatrace Operator components

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Соответствует  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Исключение (см. развёрнутое описание ниже)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Планируемое улучшение (см. развёрнутое описание ниже)

| Мера безопасности | Стандарт | Operator | Webhook | CSI driver |
| --- | --- | --- | --- | --- |
| Запрет привилегированных контейнеров[1](#fn-1-1-def) | CIS 5.2.2 / PSS Baseline | Соответствует | Соответствует | Исключение |
| Запрет повышения привилегий[1](#fn-1-1-def) | CIS 5.2.6 / PSS Restricted | Соответствует | Соответствует | Исключение |
| Запрет запуска контейнеров от имени root[2](#fn-1-2-def) | CIS 5.2.7 / PSS Restricted | Соответствует | Соответствует | Исключение |
| Ограничение доступа к секретам (RBAC) | CIS 5.1.4 | Планируемое улучшение | Планируемое улучшение | Планируемое улучшение |
| Запрет использования томов HostPath[3](#fn-1-3-def) | CIS 5.2.12 / PSS Baseline | Соответствует | Соответствует | Исключение |
| Ограничение автомонтирования токена сервисного аккаунта[4](#fn-1-4-def) | CIS 5.1.6 | Исключение | Исключение | Исключение |
| Запрет использования избыточного числа или небезопасных capabilities | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSS Restricted | Соответствует | Соответствует | Соответствует |
| Запрет использования HostPorts | CIS 5.2.13 / PSS Baseline | Соответствует | Соответствует | Соответствует |
| Запрет доступа к сети хоста | CIS 5.2.5 / PSS Baseline | Соответствует | Соответствует | Соответствует |
| Запрет использования host PID | CIS 5.2.3 / PSS Baseline | Соответствует | Соответствует | Соответствует |
| Запрет использования host IPC | CIS 5.2.4 / PSS Baseline | Соответствует | Соответствует | Соответствует |
| Требование readOnlyRootFilesystem | Рекомендуемая практика | Соответствует | Соответствует | Соответствует |
| Требование ограничений ресурсов[5](#fn-1-5-def) | Рекомендуемая практика | Соответствует | Соответствует | Соответствует |
| Требование seccomp (минимум default/runtime) | CIS 5.7.2 / PSS Restricted | Соответствует | Соответствует | Соответствует |
| Запрет монтирования секретов как переменных окружения | CIS 5.4.1 | Соответствует | Соответствует | Соответствует |
| Ограничение sysctls | PSS Baseline | Соответствует | Соответствует | Соответствует |
| Ограничение AppArmor | PSS Baseline | Соответствует | Соответствует | Соответствует |
| Запрет SELinux[6](#fn-1-6-def) | PSS Baseline | Соответствует | Соответствует | Исключение |
| Тип монтирования /proc | PSS Baseline | Соответствует | Соответствует | Соответствует |

1

CSI driver требует повышенных прав для создания и управления точками монтирования на хост-системе. Подробнее см. [Привилегии CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Компоненты Dynatrace Operator").

2

CSI driver взаимодействует с kubelet через сокет на хосте, для доступа к этому сокету CSI driver должен работать от имени root.

3

CSI driver хранит и кэширует бинарные файлы OneAgent в файловой системе хоста, для этого требуется монтирование hostVolume.

4

Компонентам Dynatrace Operator, Webhook и CSI driver нужно взаимодействовать с Kubernetes API.

5

По умолчанию у provisioner CSI driver нет ограничений ресурсов, это обеспечивает наилучшую [производительность при provisioning](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "Настройка ограничений ресурсов для компонентов Dynatrace Operator"); ограничения можно задать через значения чарта Helm.

6

CSI driver требует уровень seLinux s0, чтобы поды приложений могли видеть файлы из тома, созданного CSI driver.

**Планируемое улучшение**:  
Роли (Role) с областью действия namespace для Operator, Webhook и CSI driver в текущей реализации дают доступ ко всем секретам в своём namespace. Планируется улучшение, ограничивающее эти роли конкретными именами секретов, аналогично конфигурации ClusterRole.

### Managed компоненты

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Соответствует  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Исключение (см. раскрытие ниже)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Планируемое улучшение (см. раскрытие ниже)

| Элемент управления безопасностью | Стандарт | OneAgent | Extensions controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM | OneAgent Log Module |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Запрет привилегированных контейнеров[1](#fn-2-1-def) | CIS 5.2.2 / PSSB | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Исключение |
| Запрет эскалации привилегий[2](#fn-2-2-def) | CIS 5.2.6 / PSSR | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Исключение |
| Запрет запуска контейнеров от имени root[3](#fn-2-3-def) | CIS 5.2.7 / PSSR | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Исключение | Соответствует |
| Запрет использования слишком большого числа или небезопасных capabilities[4](#fn-2-4-def) | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSSR | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Исключение | Исключение |
| Ограничение доступа к secrets (RBAC) | CIS 5.1.4 | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Запрет использования томов HostPath[5](#fn-2-5-def) | CIS 5.2.12 / PSSB | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Исключение | Исключение |
| Запрет использования HostPorts | CIS 5.2.13 / PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Запрет доступа к сети хоста[6](#fn-2-6-def) | CIS 5.2.5 / PSSB | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Запрет использования host PID[7](#fn-2-7-def) | CIS 5.2.3 / PSSB | Исключение | Соответствует | Соответствует | Соответствует | Соответствует | Исключение | Соответствует |
| Запрет использования host IPC | CIS 5.2.4 / PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Требование readOnlyRootFilesystem | Лучшая практика | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Требование лимитов ресурсов[10](#fn-2-10-def) | Лучшая практика | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Планируемое улучшение |
| Требование использования seccomp (как минимум default/runtime)[8](#fn-2-8-def) | CIS 5.7.2 / PSSR | Исключение | Соответствует | Соответствует | Исключение | Исключение | Исключение | Исключение |
| Запрет монтирования Secrets как переменной окружения | CIS 5.4.1 | Соответствует | Соответствует | Планируемое улучшение | Соответствует | Соответствует | Соответствует | Соответствует |
| Ограничение sysctls | PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Ограничение AppArmor | PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Запрет SELinux | PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |
| Ограничение автомонтирования токена service account[9](#fn-2-9-def) | CIS 5.1.6 | Исключение | Исключение | Исключение | Исключение | Исключение | Исключение | Исключение |
| Тип монтирования /proc | PSSB | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует | Соответствует |

1

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
OneAgent Log Module: LogAgent должен работать как привилегированный контейнер в кластере OCP для доступа к своему постоянному хранилищу. [OCP persistent storage using hostPath﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

2

OneAgent: Требуется для init-контейнеров, которые инструментируют процессы до запуска.  
OneAgent Log Module: `AllowPrivilegeEscalation` всегда true, когда контейнер запущен как привилегированный. [Configure a Security Context for a Pod or Container﻿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

3

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для выполнения сканирований конфигурации и безопасности; оценка ограничения hostPath запланирована.

4

OneAgent: Требует ограниченного набора Linux capabilities (например, NET\_RAW) для сетевой наблюдаемости.  
KSPM: KSPM требует определённых Linux capabilities для сканирования и сбора данных о конфигурации и безопасности системы; это заложено архитектурно и не может быть убрано.  
OneAgent Log Module: LogAgent нужна дополнительная capability для получения доступа ко всем отслеживаемым лог-файлам.

5

OneAgent: DaemonSet OneAgent работает с привилегиями уровня хоста для полной видимости стека (сеть, процессы, файловая система).  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для сканирования на уровне узла; улучшение по ограничению монтируемых путей рассматривается.  
OneAgent Log Module: Требуется доступ к лог-файлам в файловой системе хоста.

6

OneAgent: Использует пространство имён сети хоста для мониторинга сетевого трафика.

7

OneAgent: Использует пространство имён host PID для сопоставления метрик процессов.  
KSPM: KSPM требует доступа к пространству имён host PID для сбора коллектором узла данных на уровне процессов. Это требование будет задокументировано.

8

OneAgent: Использует профиль seccomp по умолчанию (runtime); явная настройка запланирована.  
ActiveGate: ActiveGate работает с минимальным набором повышенных привилегий для управления входящими соединениями.  
EdgeConnect: В EdgeConnect в настоящее время отсутствует явный профиль seccomp; его добавление запланировано в будущих релизах. Этот элемент управления прорабатывается в предстоящих релизах.  
KSPM: KSPM монтирует корневую файловую систему хоста `/` для выполнения сканирований конфигурации и безопасности; оценка ограничения hostPath запланирована.  
OneAgent Log Module: Профиль seccomp можно задать через DynaKube для запуска в режиме secure computing.

9

OneAgent, Extensions Controller, Dynatrace Collector, ActiveGate, EdgeConnect и компоненты KSPM должны взаимодействовать с Kubernetes API.

10

OneAgent Log Module: Лимиты сильно зависят от объёма обрабатываемых данных. Можно задать через DynaKube.

**Планируемое улучшение**:  
Запрет монтирования Secrets как переменной окружения: Dynatrace Collector в настоящее время использует переменные окружения для токенов; запланирован переход на файлы secrets.

## Политики безопасности подов

Эти разрешения раньше управлялись с помощью **PodSecurityPolicy** (PSP), но [в Kubernetes версии 1.25 PSP будут удалены﻿](https://dt-url.net/2403pxy) из следующих компонентов:

* [Dynatrace Operator﻿](https://dt-url.net/d7034gj) версии 0.2.2
* **УСТАРЕВШИЙ** [Dynatrace OneAgent Operator﻿](https://dt-url.net/3023pvs) версии 0.11.0
* [Соответствующие чарты Helm﻿](https://dt-url.net/rp43pl1)

**Dynatrace Operator версии 0.2.1**, это последняя версия, в которой PSP применяются по умолчанию, поэтому обеспечивать соблюдение этих правил нужно самостоятельно. В качестве альтернатив PSP можно использовать другие инструменты обеспечения соблюдения политик, такие как:

* [k-rail﻿](https://dt-url.net/qx63p3n)
* [Kyverno﻿](https://dt-url.net/6m83ppk)
* [Gatekeeper﻿](https://dt-url.net/aha3ps4)

При использовании альтернативы PSP нужно обязательно предоставить необходимые разрешения компонентам Dynatrace.

## Security context constraints Dynatrace Operator

Dynatrace Operator версии 0.12.0+

Начиная с Dynatrace Operator версии 0.12.0, встроенное создание пользовательских security context constraints (SCC) для Dynatrace Operator и компонентов, управляемых Dynatrace Operator, было убрано. Это изменение сделано для уменьшения сложностей, вызываемых пользовательскими SCC в уникальных настройках OpenShift.

Несмотря на это обновление, компоненты сохраняют те же разрешения и требования безопасности, что и раньше.

В следующих таблицах показаны SCC, используемые в разных версиях Dynatrace Operator и OpenShift.

| Ресурсы, к которым предоставляется доступ | Пользовательский SCC, используемый в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift ранее 4.11 |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

| Ресурсы, к которым предоставляется доступ | Пользовательский SCC, используемый в версиях Dynatrace Operator ранее 0.12.0 | SCC в Dynatrace Operator версии 0.12.0+ и OpenShift 4.11+ |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

1

Этот SCC, единственный встроенный SCC OpenShift, который допускает использование seccomp (заданного у наших компонентов по умолчанию), а также использование томов CSI.

По-прежнему можно создавать собственные, более разрешительные или более строгие SCC с учётом особенностей конкретной инфраструктуры. Старые SCC, созданные предыдущей версией Dynatrace Operator, можно безопасно удалить.

Для удаления старых SCC используйте следующую команду:

```
oc delete scc <scc-name>
```