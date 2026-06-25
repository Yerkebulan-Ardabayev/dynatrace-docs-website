---
title: Требования к хранилищу
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/storage
scraped: 2026-05-12T11:53:45.304380
---

# Требования к хранилищу

# Требования к хранилищу

* Чтение: 5 мин
* Обновлено 02 января 2026 г.

В этом руководстве описано, как различные тома хранилища используются Dynatrace Operator.

## Обзор

В следующей таблице показаны требования к хранилищу для режимов развёртывания Dynatrace Operator.

| Тип развёртывания | CSI driver отключён | CSI driver включён |
| --- | --- | --- |
| `classicFullStack` | 2 GB для конфигурации и двоичных файлов OneAgent в корневой файловой системе узла | N/A |
| `hostMonitoring` | 2 GB для конфигурации и двоичных файлов OneAgent в корневой файловой системе узла | 2 GB для конфигурации и двоичных файлов OneAgent в корневом каталоге kubelet |
| `applicationMonitoring` | 1 GB на отслеживаемый под из локального эфемерного хранилища (например, корневой каталог kubelet) | 1 GB на тенант и запущенную версию OneAgent в корневом каталоге kubelet  0.1 GB на под с внедрением из локального эфемерного хранилища (например, корневой каталог kubelet) |
| `cloudNativeFullStack` | Сочетание `hostMonitoring` и `applicationMonitoring` | Сочетание `hostMonitoring` и `applicationMonitoring` |

## Тома CSI driver

Корневой каталог `kubelet`, это центральное место хранения для всех каталогов, необходимых CSI driver. Выделите примерно 30 GB для каталога `kubelet`, чтобы покрыть все требования к хранилищу, связанные с Dynatrace.

Эти значения следует увеличить для нестабильных окружений и можно уменьшить для окружений с мониторингом дискового пространства.

### Тома узла

В зависимости от вашей конфигурации корневой каталог `kubelet` может находиться не в `/var/lib/kubelet`.

| **Имя тома** | **Путь на узле** | **Разрешения** | **Назначение** | **Рекомендация по размеру** |
| --- | --- | --- | --- | --- |
| `mountpoint-dir` | `/var/lib/kubelet/pods` | Необходим доступ на чтение и запись | Хранит информацию об узле | N/A |
| `registration-dir` | `/var/lib/kubelet/plugins_registry` | Необходим доступ на чтение и запись | Содержит сокет "registration" для CSI driver. Этот сокет позволяет регистратору использовать его для регистрации CSI driver. | 10 MB |
| `plugin-dir`, `data-dir` | `/var/lib/kubelet/plugins/csi.oneagent.dynatrace.com` | Необходим доступ на чтение и запись | Хранит все файлы, необходимые для работы CSI driver. | См. [использование диска каталогом плагина](#operator-csi-plugin-dir), где перечислены все факторы, влияющие на потребление хранилища. |

#### Использование диска каталогом плагина

Содержит компоненты CSI driver и позволяет `kubelet` взаимодействовать с драйвером для таких операций, как проверки работоспособности.

Использование хранилища зависит от вашего окружения:

* Количество подов на узле
* Количество различных версий модулей кода
* Количество DynaKube

Если OneAgent отслеживает узел, потребляется дополнительное хранилище.

| Компонент | Использование диска | Примечания |
| --- | --- | --- |
| OneAgent | 5 GB | Необходимо для работы OneAgent. |
| Code Modules | см. таблицу ниже [1](#fn-1-1-def) |  |
| Runtime logs | 0.1-1 GB на под | Логи и данные, генерируемые во время выполнения. |
| Configuration | 20 MB на под |  |

1

Использование диска на версию зависит от архитектуры. Без CSI driver указанный объём хранилища потребляется на каждый под.

| Архитектура | Использование диска |
| --- | --- |
| amd64 | 1.2 GB |
| arm64 | 800 MB |
| s390x | 500 MB |
| ppc64le | 500 MB |

## Тома Extension Execution Controller

Позволяет Extension Execution Controller хранить конфигурацию, данные выполнения, логи и секреты, необходимые для выполнения расширений.

| **Имя тома** | **Тип тома** | **Путь монтирования** | **Назначение** |
| --- | --- | --- | --- |
| `agent-runtime` | `PersistentVolumeClaim` | `/var/lib/dynatrace/remotepluginmodule/agent/runtime` | Постоянный том для хранения данных выполнения и состояния расширений.  По умолчанию размер постоянного хранилища составляет 1 GB. Это значение можно настроить в поле `.spec.templates.extensionExecutionController.persistentVolumeClaim` вашего ресурса Dynakube.  Подробнее см. [параметры Dynakube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extension-execution-controller-template "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). |
| `runtime-configuration` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/agent/conf` | Эфемерный том, используемый для хранения конфигурации расширений. |
| `log` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/log` | Эфемерный том для хранения логов расширений. |

## Тома SQL Extension Executor

Позволяет SQL Extension Executor хранить временные файлы (например, сертификаты).

| **Имя тома** | **Тип тома** | **Путь на узле** | **Назначение** |
| --- | --- | --- | --- |
| `tmp-data` | `emptyDir` | `/tmp` | Эфемерный том, используемый для хранения данных приложения. |

## Тома OneAgent

Позволяет OneAgent сохранять свою конфигурацию.

| **Имя тома** | **Тип тома** | **Путь на узле** | **Назначение** |
| --- | --- | --- | --- |
| `volume-storage` | `hostPath` | `/var/opt/dynatrace` (по умолчанию) [1](#fn-2-1-def) | Без CSI driver конфигурация записывается напрямую в файловую систему узла. |
| `volume-storage` | `csi` | `/var/lib/kubelet/plugins/plugins/csi.oneagent.dynatrace.com` | С CSI driver конфигурация не записывается в эфемерный том, вместо этого для сохранения конфигурации OneAgent используется [каталог плагина](#operator-csi-plugin-dir) на узле. |

1

Настраивается с помощью поля `storageHostPath` в Dynakube. Подробнее см. [параметры Dynakube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

## Тома пода приложения

Эти каталоги специфичны для Dynatrace. Они внедряются в рабочие нагрузки [Webhook](#webhook) и не требуют управления или настройки со стороны пользователя.

| **Имя тома** | **Тип тома** | **Назначение** | **Рекомендация по размеру** |
| --- | --- | --- | --- |
| `oneagent-bin` | `emptyDir` | Хранит двоичный файл и логи OneAgent. | `emptyDir` используется, только если CSI driver не установлен. [1](#fn-3-1-def)  Примечание: ограничение размера тома `emptyDir` можно настроить, добавив к рабочим нагрузкам аннотацию  `volume.dynatrace.com/oneagent-bin: 1500Mi`. |
| `oneagent-bin` | `csi` | Хранит двоичный файл и логи OneAgent. | Используется, если CSI driver установлен. [1](#fn-3-1-def) |
| `dynatrace-config` | `emptyDir` | Хранит данные конфигурации и логи OneAgent, включая пользовательские CA. Хранит данные конфигурации для обогащения метаданными (`dt_metadata`). | Dynatrace Operator version 1.7.0+  Ограничение размера тома `emptyDir` можно настроить, добавив к рабочим нагрузкам аннотацию  `volume.dynatrace.com/dynatrace-config: <size>` [2](#fn-3-2-def).  Operator помещает `~5Mb` файлов конфигурации в `dynatrace-config` (в основном зависит от того, сколько сертификатов у пользователя), остальное управляется CodeModule согласно [механизму устаревания файлов](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Узнайте, как OneAgent удаляет старые файлы для минимизации использования дискового пространства."). Все предоставленные сертификаты будут реплицированы для каждого контейнера, поэтому они будут присутствовать в `dynatrace-config` X раз. (X, это количество контейнеров с внедрением в поде). Пример: если у нас есть Pod с 3 контейнерами, `<size>` составит 3Gi, потому что 3GB (~2.8Gi) согласно документации об устаревании файлов и 3x5Mi=15Mi для сертификатов/конфигурации с округлением до удобного числа. |

1

Такое же использование диска, как описано в разделе [использование диска каталогом плагина](#operator-csi-plugin-dir). Сэкономить хранилище можно, настроив функцию [загрузки образа на узел](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройте загрузку образа на узел").

2

Подробнее о формате `<size>` см. в [документации Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).

## Эфемерные тома

Обзор ограничений размера для эфемерных томов компонентов Dynatrace Operator и того, какие переключатели Helm можно использовать для их настройки.

### Ограничения размера эфемерных томов

| Компонент | Контейнер(ы) | Имя тома | Точка монтирования | Значение Helm | Ограничение размера по умолчанию |
| --- | --- | --- | --- | --- | --- |
| dynatrace-webhook | webhook | certs-dir | `/tmp/k8s-webhook-server/serving-certs` | `webhook.volumes.certsDir.sizeLimit` | 10 Mi |

### Ограничения эфемерного хранилища

Для настройки ресурсов эфемерного хранилища нет значений по умолчанию. Их можно настроить с помощью переключателей Helm, показанных в следующей таблице:

| Компонент | Контейнер(ы) | Значение Helm |
| --- | --- | --- |
| dynatrace-operator | operator | `operator.requests.ephemeral-storage`  `operator.limits.ephemeral-storage` |
| dynatrace-webhook | webhook | `webhook.requests.ephemeral-storage`  `webhook.limits.ephemeral-storage` |
| dynatrace-csi-driver | init | `csidriver.csiInit.resources.requests.ephemeral-storage`  `csidriver.csiInit.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | provisioner | `csidriver.provisioner.resources.requests.ephemeral-storage`  `csidriver.provisioner.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | server | `csidriver.server.resources.requests.ephemeral-storage`  `csidriver.server.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | registrar | `csidriver.registrar.resources.requests.ephemeral-storage`  `csidriver.registrar.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | livenessprobe | `csidriver.livenessprobe.resources.requests.ephemeral-storage`  `csidriver.livenessprobe.resources.limits.ephemeral-storage` |
| codemodule-download-<hash> | codemodule-download | `csidriver.job.resources.requests.ephemeral-storage`  `csidriver.job.resources.limits.ephemeral-storage` |

Переключатели Helm можно использовать в пользовательском файле [`values.yaml`](https://dt-url.net/helm-values) для управления ограничениями во время установки Operator с помощью чарта Helm.