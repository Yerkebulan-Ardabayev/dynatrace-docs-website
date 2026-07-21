---
title: Мутации подов Dynatrace для приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/workload-mutation
---

# Мутации подов Dynatrace для приложений

# Мутации подов Dynatrace для приложений

* Чтение 3 мин
* Обновлено 04 дек 2025

Когда включается обогащение метаданными или OneAgent для подов приложений, Operator Dynatrace использует webhook, чтобы перехватывать события создания workload и применять мутации к получившимся подам. Эти мутации изменяют спецификацию пода для включения возможностей мониторинга.

## Общие компоненты

Начиная с Operator v1.7, механизмы внедрения были унифицированы для повышения эффективности за счёт сокращения volume mount'ов и отказа от переменных окружения в пользу улучшенного подхода на основе init-контейнера.

### `annotations`

Эти `annotations` актуальны для всех типов внедрений webhook Dynatrace.

| Имя | Пример значений | Описание |
| --- | --- | --- |
| `dynakube.dynatrace.com/injected` | `true` | Указывает, что webhook обработал под и либо внедрил в него изменения, либо пропустил внедрение |
| `dynakube.dynatrace.com/reason` | `"NoBootstrapperConfig"` | Присутствует только при `dynakube.dynatrace.com/injected: false`, содержит дополнительную информацию о причине пропуска внедрения |

Возможные значения для `dynakube.dynatrace.com/reason`:

* `NoBootstrapperConfig`: Operator Dynatrace должен предоставлять конфигурацию каждому отслеживаемому namespace через секреты `dynatrace-bootstrapper-config` и `dynatrace-bootstrapper-certs`. Если приложение запланировано до создания этих секретов, webhook должен пропустить внедрение.
* `NoMutationNeeded`: [есть несколько способов исключить под из внедрения в otherwise отслеживаемом namespace.](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") Для таких подов это значение устанавливается как `reason` отсутствия внедрения.

### `volumes`

Эти `volumes` актуальны для всех типов внедрений Webhook Dynatrace.

| `name` | `type` |
| --- | --- |
| `dynatrace-input` | `projected` с `dynatrace-bootstrapper-config` (обязательный `Secret`) и `dynatrace-bootstrapper-certs` (опциональный `Secret`) |
| `dynatrace-config` | `emptyDir` |

Том `dynatrace-input` используется исключительно внедрённым init-контейнером и содержит:

* конфигурацию, необходимую для внедрения, в секрете `dynatrace-bootstrapper-config`;
* необходимые сертификаты в секрете `dynatrace-bootstrapper-certs`.

  + Точное содержимое секретов зависит от того, что настроено в `DynaKube`.
  + Том `projected` используется, чтобы не упереться в ограничение размера секретов, когда пользователи указывают большое количество сертификатов.

Том `dynatrace-config` содержит всю необходимую конфигурацию для внедрения после настройки init-контейнером.

### `volumeMounts`

Каждый пользовательский контейнер, независимо от типа внедрения, будет иметь этот volume mount.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace` | `dynatrace-config` | `<container-name>` |

Том `dynatrace-config` после настройки init-контейнером содержит все необходимые файловые конфигурации для включения возможностей мониторинга. OneAgent также использует этот том для хранения данных.

#### `volumeMounts` в режиме `split-mounts`

Начиная с Operator версии 1.8.0, к поду можно применить опциональную аннотацию `dynatrace.com/split-mounts`, чтобы включить режим `split-mounts`.

| Имя | Пример значений | Описание |
| --- | --- | --- |
| `dynatrace.com/split-mounts` | `true` | позволяет внедрять в workload'ы Dynatrace (такие как ActiveGate) |

При включённом режиме `split-mounts` вместо `/var/lib/dynatrace` используется четыре пути монтирования. Это предотвращает конфликты между образами приложений Dynatrace и внедрённым volumeMount `/var/lib/dynatrace`.

В случае ActiveGate подкаталог `/var/lib/dynatrace/gateway/config_template` становится недоступным при использовании пути монтирования `/var/lib/dynatrace`.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace/oneagent` | `dynatrace-config` | `<container-name>/oneagent` |
| `/var/lib/dynatrace/enrichment/dt_metadata.json` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.json` |
| `/var/lib/dynatrace/enrichment/dt_metadata.properties` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.properties` |
| `/var/lib/dynatrace/enrichment/endpoint` | `dynatrace-config` | `<container-name>/enrichment/endpoint` |

Режим `split-mounts` всегда включён для ActiveGate, управляемых Operator Dynatrace.

### `initContainers`

Добавляется init-контейнер с именем `dynatrace-operator`, чтобы обогатить контейнер метаданными и/или внедрить OneAgent.

* Использует конфигурацию пода и кластера (включая имя пода, UID и ID кластера) как часть своей конфигурации.
* Использует контекст безопасности по умолчанию либо копирует securityContext пода.
* Использует ограничения ресурсов в зависимости от типа внедрения:

  + (standalone) Метаданные: устанавливаются значения по умолчанию.
  + OneAgent: можно настроить в `DynaKube`, иначе

    - без CSI: значений по умолчанию нет;
    - с CSI: устанавливаются значения по умолчанию.

Пример YAML

Этот пример показывает одновременно включённые внедрение OneAgent и обогащение метаданными:

```
initContainers:



- args:



- bootstrap



- --config-directory=/mnt/config



- --input-directory=/mnt/input



- --source=/opt/dynatrace/oneagent



- --target=/mnt/bin



- --install-path=/opt/dynatrace/oneagent-paas



- --technology=php



- --attribute=k8s.workload.kind=deployment



- --attribute=k8s.workload.name=csi-scenario



- --attribute=k8s.namespace.annotation.operator-demo=example



- --attribute=prop=example



- --metadata-enrichment



- --attribute-container={"container_image.registry":"docker.io","container_image.repository":"php","container_image.tags":"fpm-stretch","k8s.container.name":"app"}



- --attribute=k8s.pod.uid=$(K8S_PODUID)



- --attribute=k8s.node.name=$(K8S_NODE_NAME)



- --attribute=k8s.namespace.name=demo



- --attribute=k8s.cluster.uid=84793b4d-9046-45f9-99da-cf3595cc4440



- --attribute=k8s.cluster.name=zib50933zib50933zib50933zib50933zib5093



- --attribute=dt.entity.kubernetes_cluster=KUBERNETES_CLUSTER-D3946527FEB7CAAF



- --attribute=k8s.pod.name=$(K8S_PODNAME)



env:



- name: K8S_PODNAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_PODUID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



image: public.ecr.aws/dynatrace/dynatrace-operator:v1.7.2



imagePullPolicy: IfNotPresent



name: dynatrace-operator



resources: {}



securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- ALL



privileged: false



readOnlyRootFilesystem: true



runAsGroup: 1001



runAsNonRoot: true



runAsUser: 1001



terminationMessagePath: /dev/termination-log



terminationMessagePolicy: File



volumeMounts:



- mountPath: /mnt/bin



name: oneagent-bin



readOnly: true



- mountPath: /mnt/config



name: dynatrace-config



- mountPath: /mnt/input



name: dynatrace-input



readOnly: true



- mountPath: /var/run/secrets/kubernetes.io/serviceaccount



name: kube-api-access-jtkxm



readOnly: true
```

## Мутация workload в режиме внедрения OneAgent

В режиме внедрения OneAgent мутации сосредоточены на включении возможностей full-stack мониторинга. Этот режим внедряет OneAgent в поды приложений, чтобы обеспечить всесторонний мониторинг приложений и глубокую видимость.

Аргументы init-контейнера, специфичные для внедрения OneAgent

* `--source=/opt/dynatrace/oneagent`: (актуально только для [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")) путь источника для копирования бинарных файлов OneAgent
* `--target=/mnt/bin`: путь назначения для копирования бинарных файлов OneAgent
* `--install-path=/opt/dynatrace/oneagent-paas`: путь установки, куда бинарные файлы OneAgent будут смонтированы в пользовательском контейнере (используется для настройки файла `ld.so.preload`)
* `--technology=...`: (актуально только для [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") или когда init-контейнер скачивает OneAgent) указывает тип OneAgent для скачивания/копирования, чтобы уменьшить размер бинарных файлов (настраивается через аннотации пода или DynaKube)
* `--flavor=...`: (актуально только когда init-контейнер скачивает OneAgent) указывает flavor OneAgent для скачивания/копирования, чтобы уменьшить размер бинарных файлов (настраивается через аннотации пода)

### `annotations`

| Имя | Пример значений |
| --- | --- |
| `oneagent.dynatrace.com/injected` | `true` |

### `env`

| Имя | Пример значений | Описание |
| --- | --- | --- |
| `DT_DEPLOYMENT_METADATA` | `orchestration_tech=Operator-cloud_native_fullstack;script_version=snapshot;orchestrator_id=b9c38fb3-6c0f-45f6-8c25-9eb3b4b5af2a` | Содержит метаданные развёртывания для OneAgent |
| `LD_PRELOAD` | `/opt/dynatrace/oneagent-paas/agent/lib64/liboneagentproc.so` | Предзагружает библиотеку OneAgent для мониторинга |

### `volumes`

Эти `volumes` актуальны для внедрения OneAgent.

| `name` | `type` | Описание |
| --- | --- | --- |
| `oneagent-bin` | `csi` или `emptyDir` | Содержит бинарные файлы OneAgent |

Монтирование `csi` использует драйвер `csi.oneagent.dynatrace.com` и всегда доступно только для чтения.

### `volumeMounts`

Эти `volumeMounts` относятся к внедрению OneAgent.

| `mountPath` | `name` | `subPath` | `readOnly` | Описание |
| --- | --- | --- | --- | --- |
| `/opt/dynatrace/oneagent-paas` | `oneagent-bin` |  | `true` | Каталог установки OneAgent |
| `/etc/ld.so.preload` | `dynatrace-config` | `oneagent/ld.so.preload` | `false` | Конфигурация предзагрузки библиотек |

## Мутация Pod для обогащения метаданных

Начиная с версии 1.9.0 Dynatrace Operator, функция `metadataEnrichment` автоматически включается для namespace'ов с внедрением OneAgent, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

Поэтому эти специфичные для обогащения метаданных мутации применяются к pod'ам в namespace'ах с внедрением OneAgent даже без явного включения `metadataEnrichment` в `DynaKube`. Явное отключение обогащения метаданных на уровне pod через аннотацию `metadata-enrichment.dynatrace.com/inject: false` также не даст эффекта.

В режиме обогащения метаданных Dynatrace Operator дополняет pod'ы дополнительными метаданными.

Специфичные для обогащения метаданных аргументы для init-контейнера

* `--metadata-enrichment`: указывает init-контейнеру выполнить обогащение метаданных
* `--attribute=k8s.workload.kind=...`: webhook определяет это, следуя `OwnerReferences` pod'а
* `--attribute=k8s.workload.name=...`: webhook определяет это, следуя `OwnerReferences` pod'а
* `--attribute=...`: метаданные, распространяемые из аннотаций namespace pod'а, появляются как атрибуты

### `annotations`

| Имя | Пример значений |
| --- | --- |
| `metadata.dynatrace.com/k8s.workload.kind` | `deployment` |
| `metadata.dynatrace.com/k8s.workload.name` | `example-app` |
| `metadata-enrichment.dynatrace.com/injected` | `true` |

## Мутация Pod для внедрения OneAgent с node-image-pull

В режиме внедрения OneAgent с [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), Dynatrace Operator сочетает полный мониторинг стека (full-stack monitoring) с возможностями обогащения метаданных.

### `initContainers`

Ключевое отличие от других режимов внедрения в том, что `image` init-контейнера **не** совпадает с `image` Operator/Webhook. Вместо этого используется `codeModulesImage`, определённый в `DynaKube`.

Пример YAML

Поскольку `image` Operator/Webhook не используется, аргумент `bootstrap` в init-контейнере отсутствует, так как в нём нет необходимости.

```
initContainers:



- args:



- --config-directory=/mnt/config



- --input-directory=/mnt/input



- --suppress-error



- --attribute-container={"container_image.registry":"registry.k8s.io","container_image.repository":"ingress-nginx/controller","container_image.tags":"v1.12.1","container_image.digest":"sha256:d2fbc4ec70d8aa2050dd91a91506e998765



e86c96f32cffb56c503c9c34eed5b","k8s.container.name":"controller"}



- --source=/opt/dynatrace/oneagent



- --target=/mnt/bin



- --install-path=/opt/dynatrace/oneagent-paas



- --fullstack



- --tenant=zib50933



- --technology=nginx



- --attribute=k8s.pod.uid=$(K8S_PODUID)



- --attribute=k8s.workload.name=ingress-nginx-controller



- --attribute=k8s.cluster.uid=84793b4d-9046-45f9-99da-cf3595cc4440



- --attribute=k8s.cluster.name=example



- --attribute=dt.entity.kubernetes_cluster=KUBERNETES_CLUSTER-D3946527FEB7CAAF



- --attribute=k8s.pod.name=$(K8S_PODNAME)



- --attribute=k8s.node.name=$(K8S_NODE_NAME)



- --attribute=k8s.namespace.name=ingress-nginx



- --attribute=k8s.workload.kind=deployment



env:



- name: K8S_PODNAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_PODUID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



image: public.ecr.aws/dynatrace/dynatrace-codemodules:1.315.62.20250613-075406



imagePullPolicy: IfNotPresent



name: dynatrace-operator



resources: {}



securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- ALL



privileged: false



readOnlyRootFilesystem: true



runAsGroup: 1001



runAsNonRoot: true



runAsUser: 1001



terminationMessagePath: /dev/termination-log



terminationMessagePolicy: File



volumeMounts:



- mountPath: /mnt/bin



name: oneagent-bin



- mountPath: /mnt/config



name: dynatrace-config



- mountPath: /mnt/input



name: dynatrace-input



readOnly: true



- mountPath: /var/run/secrets/kubernetes.io/serviceaccount



name: kube-api-access-p5css



readOnly: true
```