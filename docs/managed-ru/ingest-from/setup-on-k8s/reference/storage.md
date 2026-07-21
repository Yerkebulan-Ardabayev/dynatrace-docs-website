---
title: Требования к хранилищу
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/storage
---


# Требования к хранилищу


# Требования к хранилищу


* 5 мин чтения
* Обновлено 2 января 2026 г.


В этом руководстве описано, как разные тома хранилища используются Dynatrace Operator.


## Обзор


В следующей таблице показаны требования к хранилищу для режимов развёртывания Dynatrace Operator.


| Тип развёртывания | CSI-драйвер отключён | CSI-драйвер включён |
| --- | --- | --- |
| `classicFullStack` | 2 ГБ для конфигурации и бинарных файлов OneAgent в корневой файловой системе узла | Н/Д |
| `hostMonitoring` | 2 ГБ для конфигурации и бинарных файлов OneAgent в корневой файловой системе узла | 2 ГБ для конфигурации и бинарных файлов OneAgent в корневом каталоге kubelet |
| `applicationMonitoring` | 1 ГБ на каждый отслеживаемый под из локального временного хранилища (например, корневой каталог kubelet) | 1 ГБ на арендатора и запущенную версию OneAgent в корневом каталоге kubelet  0,1 ГБ на каждый под с инъекцией из локального временного хранилища (например, корневой каталог kubelet) |
| `cloudNativeFullStack` | Комбинация `hostMonitoring` и `applicationMonitoring` | Комбинация `hostMonitoring` и `applicationMonitoring` |


## Тома CSI-драйвера


Корневой каталог `kubelet`, это центральное место хранения для всех каталогов, необходимых CSI-драйверу. Нужно выделить примерно 30 ГБ для каталога `kubelet`, чтобы покрыть все требования к хранилищу, связанные с Dynatrace.


Эти значения следует увеличивать для нестабильных сред и можно уменьшать для сред с мониторингом дискового пространства.


### Тома узла


В зависимости от настройки корневой каталог `kubelet` может находиться не в `/var/lib/kubelet`.


| **Имя тома** | **Путь на узле** | **Права доступа** | **Назначение** | **Рекомендация по размеру** |
| --- | --- | --- | --- | --- |
| `mountpoint-dir` | `/var/lib/kubelet/pods` | Требуется чтение-запись | Хранит информацию об узле | Н/Д |
| `registration-dir` | `/var/lib/kubelet/plugins_registry` | Требуется чтение-запись | Содержит сокет «регистрации» CSI-драйвера. Этот сокет позволяет регистратору использовать его для регистрации CSI-драйвера. | 10 МБ |
| `plugin-dir`, `data-dir` | `/var/lib/kubelet/plugins/csi.oneagent.dynatrace.com` | Требуется чтение-запись | Хранит все файлы, необходимые для работы CSI-драйвера. | См. [использование дискового пространства каталога плагина](#operator-csi-plugin-dir), где перечислены все факторы, влияющие на расход хранилища. |


#### Использование дискового пространства каталога плагина


Содержит компоненты CSI-драйвера и позволяет `kubelet` взаимодействовать с драйвером для таких операций, как проверки состояния.


Использование хранилища зависит от среды:


* Количество подов на узле
* Количество разных версий модулей кода
* Количество DynaKube


Если OneAgent отслеживает узел, расходуется дополнительное хранилище.


| Компонент | Использование диска | Примечания |
| --- | --- | --- |
| OneAgent | 5 ГБ | Необходимо для работы OneAgent. |
| Модули кода | см. таблицу ниже [1](#fn-1-1-def) |  |
| Логи времени выполнения | 0,1-1 ГБ на под | Логи и данные, создаваемые во время выполнения. |
| Конфигурация | 20 МБ на под |  |


1


Использование диска на версию зависит от архитектуры. Без CSI-драйвера указанный объём хранилища расходуется на каждый под.


| Архитектура | Использование диска |
| --- | --- |
| amd64 | 1,2 ГБ |
| arm64 | 800 МБ |
| s390x | 500 МБ |
| ppc64le | 500 МБ |


## Тома Extension Execution Controller


Позволяют Extension Execution Controller хранить конфигурацию, данные времени выполнения, логи и секреты, необходимые для выполнения расширений.


| **Имя тома** | **Тип тома** | **Путь монтирования** | **Назначение** |
| --- | --- | --- | --- |
| `agent-runtime` | `PersistentVolumeClaim` | `/var/lib/dynatrace/remotepluginmodule/agent/runtime` | Постоянный том для хранения данных и состояния времени выполнения расширений.  По умолчанию размер постоянного хранилища составляет 1 ГБ. Это значение можно настроить в поле `.spec.templates.extensionExecutionController.persistentVolumeClaim` ресурса Dynakube.  Дополнительную информацию см. в разделе [параметры Dynakube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extension-execution-controller-template "Список доступных параметров для настройки Dynatrace Operator на Kubernetes."). |
| `runtime-configuration` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/agent/conf` | Временный том, используемый для хранения конфигурации расширений. |
| `log` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/log` | Временный том для хранения логов расширений. |


## Тома SQL Extension Executor


Позволяют SQL Extension Executor хранить временные файлы (например, сертификаты).


| **Имя тома** | **Тип тома** | **Путь на узле** | **Назначение** |
| --- | --- | --- | --- |
| `tmp-data` | `emptyDir` | `/tmp` | Временный том, используемый для хранения данных приложения. |


## Тома OneAgent


Позволяют OneAgent сохранять свою конфигурацию.


| **Имя тома** | **Тип тома** | **Путь на узле** | **Назначение** |
| --- | --- | --- | --- |
| `volume-storage` | `hostPath` | `/var/opt/dynatrace` (по умолчанию) [1](#fn-2-1-def) | Без CSI-драйвера конфигурация записывается напрямую в файловую систему узла. |
| `volume-storage` | `csi` | `/var/lib/kubelet/plugins/plugins/csi.oneagent.dynatrace.com` | С CSI-драйвером конфигурация не записывается во временный том, вместо этого для сохранения конфигурации OneAgent используется [каталог плагина](#operator-csi-plugin-dir) на узле. |


1


Настраивается с помощью поля `storageHostPath` в Dynakube. Дополнительную информацию см. в разделе [параметры Dynakube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.").


## Тома подов приложений


Эти каталоги специфичны для Dynatrace. Они внедряются в рабочие нагрузки через [Webhook](#webhook) и не требуют управления или настройки со стороны пользователя.


| **Имя тома** | **Тип тома** | **Назначение** | **Рекомендация по размеру** |
| --- | --- | --- | --- |
| `oneagent-bin` | `emptyDir` | Хранит бинарный файл и логи OneAgent. | `emptyDir` используется, только если CSI-драйвер не установлен. [1](#fn-3-1-def)  Примечание: можно настроить лимит размера тома `emptyDir`, аннотировав рабочие нагрузки с помощью  `volume.dynatrace.com/oneagent-bin: 1500Mi`. |
| `oneagent-bin` | `csi` | Хранит бинарный файл и логи OneAgent. | Используется, если CSI-драйвер установлен. [1](#fn-3-1-def) |
| `dynatrace-config` | `emptyDir` | Хранит данные конфигурации и логи OneAgent, включая пользовательские CA. Хранит данные конфигурации для обогащения метаданными (`dt_metadata`). | Dynatrace Operator версии 1.7.0+  Можно настроить лимит размера тома `emptyDir`, аннотировав рабочие нагрузки с помощью  `volume.dynatrace.com/dynatrace-config: <size>` [2](#fn-3-2-def).  Operator помещает `~5Mb` (в основном зависит от количества сертификатов у пользователя) файлов конфигурации в `dynatrace-config`, остальным управляет CodeModule согласно [механизму устаревания файлов](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Узнайте, как OneAgent удаляет старые файлы для минимизации использования дискового пространства."). Все предоставленные сертификаты будут реплицированы для каждого контейнера, поэтому они будут присутствовать в `dynatrace-config` X раз (X, это количество контейнеров с инъекцией в поде). Пример: если есть под с 3 контейнерами, `<size>` будет равен 3Gi, потому что 3 ГБ (~2,8Gi) согласно документации по устареванию файлов и 3x5Mi=15Mi для сертификатов/конфигурации, с округлением до удобного числа. |


1


Такое же использование диска, как описано в разделе [использование дискового пространства каталога плагина](#operator-csi-plugin-dir). Можно сэкономить хранилище, настроив функцию [загрузки образа узла](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая временные тома, загрузку образа через CSI-драйвер и загрузку ZIP."). 


2


Более подробную информацию о формате `<size>` можно найти в [документации Kubernetes﻿](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).


## Временные тома


Обзор лимитов размера временных томов для компонентов Dynatrace Operator и переключателей Helm, которые можно использовать для их настройки.


### Лимиты размера временных томов


| Компонент | Контейнер(ы) | Имя тома | Точка монтирования | Значение Helm | Лимит размера по умолчанию |
| --- | --- | --- | --- | --- | --- |
| dynatrace-webhook | webhook | certs-dir | `/tmp/k8s-webhook-server/serving-certs` | `webhook.volumes.certsDir.sizeLimit` | 10 Mi |


### Лимиты временного хранилища


Для настройки ресурсов временного хранилища нет значений по умолчанию. Их можно настроить с помощью переключателей Helm, показанных в следующей таблице:


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

Переключатели Helm можно использовать в пользовательском файле [`values.yaml`﻿](https://dt-url.net/helm-values) для управления лимитами во время установки Operator с помощью чарта Helm.