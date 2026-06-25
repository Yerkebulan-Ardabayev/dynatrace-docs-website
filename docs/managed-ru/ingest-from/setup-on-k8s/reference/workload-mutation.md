---
title: Мутации подов Dynatrace для прикладных рабочих нагрузок
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/workload-mutation
scraped: 2026-05-12T11:53:43.772625
---

# Мутации подов Dynatrace для прикладных рабочих нагрузок

# Мутации подов Dynatrace для прикладных рабочих нагрузок

* Чтение: 3 мин
* Обновлено 4 декабря 2025 г.

Когда вы включаете обогащение метаданными или OneAgent для прикладных подов, Dynatrace Operator использует вебхук для перехвата событий создания рабочих нагрузок и применяет мутации к создаваемым подам. Эти мутации изменяют спецификацию пода, чтобы включить возможности мониторинга.

## Общие компоненты

Начиная с Operator v1.7, механизмы внедрения были унифицированы для повышения эффективности за счёт сокращения монтирований томов и отказа от переменных окружения в пользу улучшенного подхода с init-контейнером.

### `annotations`

Эти `annotations` относятся ко всем типам внедрений через вебхук Dynatrace.

| Имя | Примеры значений | Описание |
| --- | --- | --- |
| `dynakube.dynatrace.com/injected` | `true` | Указывает, что вебхук обработал под и либо внедрил его, либо пропустил внедрение |
| `dynakube.dynatrace.com/reason` | `"NoBootstrapperConfig"` | Присутствует только при `dynakube.dynatrace.com/injected: false`, предоставляет дополнительную информацию о том, почему внедрение было пропущено |

Возможные значения для `dynakube.dynatrace.com/reason`:

* `NoBootstrapperConfig`: Dynatrace Operator должен предоставлять конфигурацию каждому отслеживаемому пространству имён через секреты с именами `dynatrace-bootstrapper-config` и `dynatrace-bootstrapper-certs`. Если приложение планируется до создания этих секретов, вебхук должен пропустить внедрение.
* `NoMutationNeeded`: [Существует несколько способов исключить под из внедрения в пространстве имён, которое в остальном отслеживается.](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройте мониторинг для пространств имён и подов") Для таких подов это значение задаётся как `reason` для отсутствия внедрения.

### `volumes`

Эти `volumes` относятся ко всем типам внедрений через вебхук Dynatrace.

| `name` | `type` |
| --- | --- |
| `dynatrace-input` | `projected` с `dynatrace-bootstrapper-config`(обязательный `Secret`) и `dynatrace-bootstrapper-certs`(необязательный `Secret`) |
| `dynatrace-config` | `emptyDir` |

Том `dynatrace-input` используется исключительно внедрённым init-контейнером и содержит:

* Конфигурацию, необходимую для внедрения, в секрете `dynatrace-bootstrapper-config`
* Необходимые сертификаты в секрете `dynatrace-bootstrapper-certs`

  + Точное содержимое секретов зависит от того, что настроено в `DynaKube`
  + Том `projected` используется, чтобы не превысить ограничение на размер секретов, когда пользователи предоставляют большое количество сертификатов

Том `dynatrace-config` содержит всю необходимую конфигурацию для внедрения после настройки init-контейнером.

### `volumeMounts`

Каждый пользовательский контейнер, независимо от типа внедрения, будет иметь это монтирование тома.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace` | `dynatrace-config` | `<container-name>` |

Том `dynatrace-config` после настройки init-контейнером содержит все необходимые файловые конфигурации для включения возможностей мониторинга. OneAgent также использует этот том для хранения.

#### `volumeMounts` в режиме `split-mounts`

Начиная с Operator версии 1.8.0, к поду можно применить необязательную аннотацию `dynatrace.com/split-mounts`, чтобы включить режим `split-mounts`.

| Имя | Примеры значений | Описание |
| --- | --- | --- |
| `dynatrace.com/split-mounts` | `true` | позволяет выполнять внедрение в рабочие нагрузки Dynatrace (например, ActiveGate) |

При включённом режиме `split-mounts` вместо `/var/lib/dynatrace` используются четыре пути монтирования. Это предотвращает конфликты между образами приложений Dynatrace и внедрённым монтированием тома `/var/lib/dynatrace`.

В случае ActiveGate подкаталог `/var/lib/dynatrace/gateway/config_template` становится недоступным при использовании пути монтирования `/var/lib/dynatrace`.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace/oneagent` | `dynatrace-config` | `<container-name>/oneagent` |
| `/var/lib/dynatrace/enrichment/dt_metadata.json` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.json` |
| `/var/lib/dynatrace/enrichment/dt_metadata.properties` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.properties` |
| `/var/lib/dynatrace/enrichment/endpoint` | `dynatrace-config` | `<container-name>/enrichment/endpoint` |

Режим `split-mounts` всегда включён для ActiveGate, которыми управляет Dynatrace Operator.

### `initContainers`

Init-контейнер с именем `dynatrace-operator` добавляется для обогащения контейнера метаданными и/или внедрения OneAgent.

* Использует конфигурацию пода и кластера (включая имя пода, UID и идентификатор кластера) как часть своей конфигурации.
* Использует контекст безопасности по умолчанию или копирует securityContext пода.
* Использует лимиты ресурсов в зависимости от типа внедрения:

  + (автономное) Метаданные: задаются значения по умолчанию
  + OneAgent: можно настроить в `DynaKube`, иначе

    - без CSI: значения по умолчанию не заданы
    - с CSI: задаются значения по умолчанию

Пример YAML

В этом примере включены и внедрение OneAgent, и обогащение метаданными:

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

## Мутация рабочей нагрузки в режиме внедрения OneAgent

В режиме внедрения OneAgent мутации направлены на включение возможностей full-stack мониторинга. Этот режим внедряет OneAgent в ваши прикладные поды, чтобы обеспечить комплексный мониторинг приложений и глубокую видимость.

Аргументы init-контейнера, специфичные для внедрения OneAgent

* `--source=/opt/dynatrace/oneagent`: (Относится только к [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройте загрузку образа на узле")) Исходный путь для копирования двоичных файлов OneAgent
* `--target=/mnt/bin`: Путь назначения для копирования двоичных файлов OneAgent
* `--install-path=/opt/dynatrace/oneagent-paas`: Путь установки, по которому двоичные файлы OneAgent будут смонтированы в пользовательском контейнере (используется для настройки файла `ld.so.preload`)
* `--technology=...`: (Относится только к [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройте загрузку образа на узле") или когда init-контейнер загружает OneAgent) Указывает тип OneAgent для загрузки/копирования с целью уменьшения размера двоичного файла (настраивается через аннотации пода или DynaKube)
* `--flavor=...`: (Относится только к случаю, когда init-контейнер загружает OneAgent) Указывает разновидность OneAgent для загрузки/копирования с целью уменьшения размера двоичного файла (настраивается через аннотации пода)

### `annotations`

| Имя | Примеры значений |
| --- | --- |
| `oneagent.dynatrace.com/injected` | `true` |

### `env`

| Имя | Примеры значений | Описание |
| --- | --- | --- |
| `DT_DEPLOYMENT_METADATA` | `orchestration_tech=Operator-cloud_native_fullstack;script_version=snapshot;orchestrator_id=b9c38fb3-6c0f-45f6-8c25-9eb3b4b5af2a` | Содержит метаданные развёртывания для OneAgent |
| `LD_PRELOAD` | `/opt/dynatrace/oneagent-paas/agent/lib64/liboneagentproc.so` | Предварительно загружает библиотеку OneAgent для мониторинга |

### `volumes`

Эти `volumes` относятся к внедрению OneAgent.

| `name` | `type` | Описание |
| --- | --- | --- |
| `oneagent-bin` | `csi` или `emptyDir` | Содержит двоичные файлы OneAgent |

Монтирование `csi` использует драйвер `csi.oneagent.dynatrace.com` и всегда доступно только для чтения.

### `volumeMounts`

Эти `volumeMounts` относятся к внедрению OneAgent.

| `mountPath` | `name` | `subPath` | `readOnly` | Описание |
| --- | --- | --- | --- | --- |
| `/opt/dynatrace/oneagent-paas` | `oneagent-bin` |  | `true` | Каталог установки OneAgent |
| `/etc/ld.so.preload` | `dynatrace-config` | `oneagent/ld.so.preload` | `false` | Конфигурация предварительной загрузки библиотеки |

## Мутация пода для обогащения метаданными

Начиная с Dynatrace Operator версии 1.9.0, функция `metadataEnrichment` автоматически включается для пространств имён с внедрением OneAgent, даже если параметр `enabled` в `.spec.metadataEnrichment` имеет значение `false`.

Поэтому эти специфичные для обогащения метаданными мутации применяются к подам в пространствах имён с внедрением OneAgent, даже без явного включения `metadataEnrichment` в `DynaKube`. Явное отключение обогащения метаданными на уровне пода через аннотацию `metadata-enrichment.dynatrace.com/inject: false` также не будет иметь эффекта.

В режиме обогащения метаданными Dynatrace Operator дополняет поды дополнительными метаданными.

Аргументы init-контейнера, специфичные для обогащения метаданными

* `--metadata-enrichment`: Указывает init-контейнеру выполнить обогащение метаданными
* `--attribute=k8s.workload.kind=...`: Вебхук определяет это, следуя `OwnerReferences` пода
* `--attribute=k8s.workload.name=...`: Вебхук определяет это, следуя `OwnerReferences` пода
* `--attribute=...`: Метаданные, распространённые из аннотаций пространства имён пода, появляются как атрибуты

### `annotations`

| Имя | Примеры значений |
| --- | --- |
| `metadata.dynatrace.com/k8s.workload.kind` | `deployment` |
| `metadata.dynatrace.com/k8s.workload.name` | `example-app` |
| `metadata-enrichment.dynatrace.com/injected` | `true` |

## Мутация пода для внедрения OneAgent с node-image-pull

В режиме внедрения OneAgent с [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройте загрузку образа на узле") Dynatrace Operator сочетает full-stack мониторинг с возможностями обогащения метаданными.

### `initContainers`

Ключевое отличие от других режимов внедрения в том, что `image` init-контейнера **не** совпадает с `image` Operator/Webhook. Вместо этого используется `codeModulesImage`, определённый в `DynaKube`.

Пример YAML

Поскольку `image` Operator/Webhook не используется, аргумент `bootstrap` отсутствует в init-контейнере, так как он не нужен.

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