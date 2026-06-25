---
title: Settings API - Built-in container monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-built-in-monitoring-rule
scraped: 2026-05-12T11:39:28.410825
---

# Settings API - Built-in container monitoring rules schema table

# Settings API - Built-in container monitoring rules schema table

* Published Dec 05, 2023

### Встроенные правила мониторинга контейнеров (`builtin:container.built-in-monitoring-rule)`

Dynatrace отключает мониторинг контейнеров, в которых не запущены приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.built-in-monitoring-rule` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Не мониторить контейнеры, у которых имя Kubernetes-контейнера равно 'POD' `ignoreKubernetesPauseContainer` | boolean | Отключить мониторинг внутренних pause-контейнеров платформы в Kubernetes и OpenShift. | Required |
| Не мониторить контейнеры, у которых stripped имя Docker-образа содержит 'pause-amd64' `ignoreDockerPauseContainer` | boolean | Отключить мониторинг внутренних pause-контейнеров платформы в Kubernetes и OpenShift. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-sdn' `ignoreOpenShiftSdnNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-sdn. | Required |
| Не мониторить контейнеры, у которых полное имя Kubernetes-pod заканчивается на '-build' `ignoreOpenShiftBuildPodName` | boolean | Отключить мониторинг промежуточных контейнеров, создаваемых при сборке образа. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-ovn-kubernetes' `ignoreOpenShiftOvnKubernetesNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-ovn-kubernetes. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-etcd' `ignoreOpenShiftEtcdNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-etcd. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-kube-apiserver' `ignoreOpenShiftKubeApiserverNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-kube-apiserver. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-monitoring' `ignoreOpenShiftMonitoringNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-monitoring. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-machine-config-operator' `ignoreOpenShiftMachineConfigOperatorNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-machine-config-operator. | Required |
| Не мониторить контейнеры, у которых Kubernetes-namespace равен 'openshift-ingress-canary' `ignoreOpenShiftIngressCanaryNamespace` | boolean | Отключить мониторинг внутренних контейнеров платформы в namespace openshift-ingress-canary. | Required |