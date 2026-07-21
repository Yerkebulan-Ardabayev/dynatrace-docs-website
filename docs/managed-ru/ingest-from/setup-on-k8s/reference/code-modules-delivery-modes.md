---
title: Способы доставки code modules
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes
---

# Способы доставки code modules

# Способы доставки code modules

* Справка
* Чтение за 7 мин
* Обновлено 10 июля 2026 г.

cloudNativeFullStack applicationMonitoring

Dynatrace Operator может доставлять code modules OneAgent в поды приложений несколькими способами. Какой из них применяется, зависит от того, включён ли CSI driver, от версии Dynatrace Operator и от того, как настроен DynaKube.

Основные сценарии использования:

* Cloud-native full-stack monitoring работает независимо от CSI driver.
* Cloud-native full-stack monitoring можно развернуть через OpenShift OperatorHub.
* Внедрение code modules без CSI и через CSI можно комбинировать, подробности см. в разделе [Enforce ephemeral-volume injection on mixed clusters](#mixed-mode).

| Способ доставки | CSI driver включён | Затраты на хранение | Когда применяется | Примечания |
| --- | --- | --- | --- | --- |
| [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) | Нет, ephemeral volume | Расход хранилища на под | Настроен образ code modules. По умолчанию начиная с Operator v1.10 | Использует учётные данные узла. Образ кэшируется на каждом узле. |
| [CSI driver image pull](#csi-image-pull) | Да, CSI volume | Кэш на уровне узла | Настроен образ code modules, и включён CSI driver | Для приватных registry требуется `customPullSecret` |
| [Node Image Pull via CSI volume](#csi-node-image-pull) | Да, CSI volume | Кэш на уровне узла | Настроен образ code modules, и включён CSI driver. Включается через `feature.dynatrace.com/node-image-pull: "true"` | Использует учётные данные узла наряду с `customPullSecret` для приватных registry.[1](#fn-1-1-def) |
| [CSI driver ZIP download](#csi-zip) | Да, CSI volume | Кэш на уровне узла | Образ code modules не настроен | Не поддерживается в средах Latest Dynatrace. Вместо этого использовать [CSI driver image pull](#csi-image-pull). |
| [ZIP download](#zip-download) | Нет, ephemeral volume | Расход хранилища на под | Образ code modules не настроен | Добавляет задержку при каждом запуске пода. ZIP скачивается и распаковывается в ephemeral volume каждого пода. Не поддерживается в средах Latest Dynatrace. Вместо этого использовать [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull). |

1

Поскольку образы загружает узел Kubernetes с использованием собственных учётных данных, `customPullSecret` для приватных registry не требуется, если узлы уже настроены на аутентификацию в registry. Подробности см. в разделе [Prerequisites](#csi-node-image-pull-prerequisites).

## Типы volume

Способ доставки зависит от того, какой тип volume используется для предоставления бинарных файлов code modules поду приложения.

|  | Ephemeral volume | CSI volume |
| --- | --- | --- |
| **Требуется CSI driver** | Нет | Да |
| **Хранение** | На под (у каждого пода своя копия) | Кэш на уровне узла (общий для подов на одном узле) |
| **Учётные данные для приватных registry** | Учётные данные узла или `imagePullSecrets` на уровне пода | `customPullSecret` (либо учётные данные узла для Node Image Pull через CSI) |
| **Когда использовать** | CSI driver недоступен, или для отдельных workload предпочтительно ephemeral-внедрение | CSI driver доступен и предпочтительно кэширование на уровне узла |

## Ephemeral volume

Когда CSI driver не включён, code modules копируются в ephemeral volume пода приложения.

### Node Image Pull via Ephemeral Volume

При Node Image Pull через ephemeral volume внедряемый init container использует образ code modules вместо образа Operator. Узел Kubernetes загружает его напрямую, а init container копирует бинарные файлы OneAgent в ephemeral volume пода приложения.

Начиная с версии Dynatrace Operator 1.10, Node Image Pull в ephemeral volume используется, когда настроен образ code modules.
В предыдущих версиях это поведение управляется флагом функции `feature.dynatrace.com/node-image-pull: "true"`.

Настройка

#### Предварительные требования

* Dynatrace OneAgent версии 1.317+
* Образ code modules Dynatrace, полученный из [поддерживаемого публичного registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного registry для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace.") или [приватного registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование приватного registry").

При этом способе узел Kubernetes загружает образ code modules для внедряемых подов приложений. При использовании приватного registry `customPullSecret` из DynaKube **не** применяется к этим подам: Dynatrace Operator не реплицирует pull secret в пространства имён приложений и не добавляет их в поды за пределами пространства имён `dynatrace`.

Убедиться, что все узлы аутентифицированы в registry, либо распространить pull secret на пространства имён приложений, узлы или поды. Подробности см. в разделе [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Использование приватного registry").

#### Настройка DynaKube

Включить автоматическое определение образа через аннотацию `feature.dynatrace.com/use-public-registry` либо задать поле `codeModulesImage` напрямую. Об источниках образов и формате тегов см. [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного registry для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace.") или [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование приватного registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

### ZIP download

Внедряемый init container загружает и распаковывает ZIP-архив code module из Environment Dynatrace в ephemeral volume при запуске пода.

Этот способ доставки используется, когда образ code modules не настроен или не может быть определён автоматически, а CSI driver не включён.

Недостатки:

* Каждый под загружает ZIP code modules из Environment Dynatrace, что добавляет задержку и нагрузку.
* Init container должен иметь сетевой доступ к API Environment во время запуска пода.
* Отсутствует нативная интеграция с supply chain Kubernetes: бинарные файлы не доставляются как OCI-образ, поэтому политики подписи образов и admission-политики не применяются.

По этим причинам, когда это возможно, вместо ZIP download рекомендуется доставка через node image pull в ephemeral volume.

Настройка

#### Предварительные требования

* CSI driver не включён в кластере.
* Образ code modules не настроен.
* Внедряемые поды должны иметь сетевой доступ к API Environment Dynatrace при запуске.

#### Настройка DynaKube

Dynatrace Operator использует этот способ автоматически, когда образ code modules не задан, а CSI driver не включён. Убедиться, что `codeModulesImage` отсутствует в DynaKube, и что [автоматическое определение](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator для использования образов из публичного registry для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace.") не применяется:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack: {}
```

### Оптимизация хранения

OneAgent версии 1.315+

При доставке модулей кода через ephemeral volumes каждый инжектированный под получает собственную копию бинарных файлов модуля кода. Чтобы снизить потребление хранилища, можно ограничить инъекцию конкретными технологиями приложений (например, Java), избегая копирования ненужных бинарных файлов.

Если оптимизация хранилища не настроена (то есть отсутствует аннотация `oneagent.dynatrace.com/technologies`), потребление хранилища соответствует рекомендациям, описанным в [требованиях к хранилищу](/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments").

Указанные технологии копируются в общий том, потребляя ephemeral-хранилище.

#### Идентификаторы технологий

Для каждой технологии доступны следующие идентификаторы:

| Технология | Идентификатор |
| --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | `java` |
| [.NET, .NET Core и .NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | `dotnet` |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | `nodejs` |
| [Python](/managed/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.") | `python` |
| [PHP](/managed/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.") | `php` |
| [Go](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") | `go` |
| Apache, IBM HTTP Server | `apache` |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.") | `nginx` |

#### Аннотирование пода приложения

Чтобы уменьшить объём данных, копируемых в поды приложений, можно указать, какие технологии OneAgent актуальны для приложения. Аннотируйте поды приложений, как показано в примере ниже:

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"
```

При указании списка идентификаторов технологий через запятую следите за тем, чтобы в значении аннотации не было пробельных символов.

Значения аннотации должны использовать точные идентификаторы технологий, перечисленные в таблице выше.

Если аннотация `oneagent.dynatrace.com/technologies` не задана, в поды приложений копируются все технологии.

Если в кластере используется только одна технология или нужно задать технологию по умолчанию для инъекции модулей кода Dynatrace, это можно настроить на уровне DynaKube, чтобы применить настройку ко всем инжектированным подам приложений.

Настройка на уровне DynaKube

Измените конфигурацию DynaKube, ограничив инъекцию модулей кода одной технологией или набором нескольких технологий:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



oneagent.dynatrace.com/technologies: "java"



spec:



...
```

При указании списка идентификаторов технологий через запятую следите за тем, чтобы в значении аннотации не было пробельных символов.

## Том CSI

При доставке модулей кода с помощью CSI-драйвера бинарные файлы модулей кода становятся общими для подов, что позволяет избежать копирования на каждый под.

### Загрузка образа CSI-драйвером

CSI-драйвер загружает образ модулей кода и предоставляет бинарные файлы модулей кода в файловой системе хоста, где каждый инжектированный под приложения монтирует их через том CSI.

Конфигурация

#### Предварительные условия

* Образ модулей кода Dynatrace, полученный из [поддерживаемого публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), собственного [приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry") или [определённый автоматически](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

  + Для приватных реестров настройте `customPullSecret`. Подробности см. в разделе [Использование приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").
* CSI-драйвер включён в кластере.

#### Конфигурация DynaKube

Включите автоматическое определение образа с помощью аннотации `feature.dynatrace.com/use-public-registry` или задайте поле `codeModulesImage` напрямую. Об источниках образов и формате тега см. [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") или [Использование приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

### Загрузка образа на узел через том CSI

Dynatrace Operator версии 1.5

CSI-драйвер планирует задачу загрузки на каждом узле, где среда выполнения контейнеров загружает образ модулей кода напрямую. Затем бинарные файлы модулей кода предоставляются в файловой системе хоста, где каждый инжектированный под приложения монтирует их через том CSI.

Такой подход упрощает нативную интеграцию с Kubernetes с инструментами безопасности цепочки поставок и снижает необходимость в `customPullSecret` при получении образов из приватных реестров.[2](#fn-2-2-def) Поскольку образ загружается узлом, убедитесь, что узел аутентифицирован в приватном реестре. Подробности см. в разделе [Предоставление pull-секретов для инжектированных рабочих нагрузок](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").

Начиная с Dynatrace Operator версии 1.10, флаг функции `node-image-pull` влияет только на CSI-драйвер. Для развёртываний с ephemeral volume по умолчанию используется [Загрузка образа на узел через Ephemeral Volume](#ephemeral-node-image-pull).

2

Начиная с [Dynatrace Operator версии 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0"), задачи загрузки наследуют тот же `PriorityClass`, что и CSI-драйвер, обеспечивая быстрое планирование и вытеснение на перегруженных кластерах. Значение можно настроить через `csidriver.priorityClassValue` в файле значений Helm. Рекомендации см. в разделе [Использование priorityClass для критичных компонентов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Use priorityClass for critical Dynatrace components").

Конфигурация

#### Предварительные условия

* Dynatrace OneAgent версии 1.317+
* Образ модулей кода Dynatrace, полученный из [поддерживаемого публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") или собственного [приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").
* CSI-драйвер включён в кластере.

#### Конфигурация DynaKube

Включите флаг функции `node-image-pull` и аннотацию `use-public-registry` для автоматического определения образа, либо задайте поле `codeModulesImage` напрямую. Об источниках образов и формате тега см. [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") или [Использование приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

#### Ограничения

GKE Autopilot динамически выделяет узлы и их размеры на основе совокупных запросов ресурсов подов. Это делает GKE Autopilot непригодным для функции загрузки образа на узел в сочетании с CSI-драйвером. Dynatrace рекомендует либо отключить загрузку образа на узел на GKE Autopilot с CSI-драйвером, либо использовать вместо этого доставку через ephemeral volume, см. [Загрузка образа на узел через Ephemeral Volume](#ephemeral-node-image-pull).

### Загрузка ZIP-архива CSI-драйвером

CSI-драйвер скачивает, распаковывает и предоставляет ZIP-архив с модулями кода на файловой системе хоста, откуда каждый инъецируемый под приложения монтирует их через CSI volume.

Configuration

#### Prerequisites

* CSI driver enabled on the cluster.
* No code modules image configured.

#### DynaKube configuration

Оператор Dynatrace использует этот режим автоматически, когда CSI driver включён и образ code modules не задан. Нужно убедиться, что `codeModulesImage` отсутствует в DynaKube и что [автоматическое разрешение](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") не применяется:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack: {}
```

## Enforce ephemeral-volume injection on mixed clusters

applicationMonitoring cloudNativeFullStack OneAgent version 1.315+

Можно выборочно настроить инъекцию code module Dynatrace на использование ephemeral volumes, даже когда CSI driver доступен на ноде. В этом случае инъекция code module работает так, как описано в разделах [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) и [Storage optimization](#storage-optimization).

Для этого нужно использовать аннотацию `oneagent.dynatrace.com/volume-type: "ephemeral"` на Pod, как показано в блоке кода ниже. Аннотация `oneagent.dynatrace.com/technologies` это дополнительная оптимизация, см. [Annotate the application pod](#technologies).

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "ephemeral" # no CSI driver involved



oneagent.dynatrace.com/technologies: "nginx"    # minimize storage consumption
```

Такой подход сочетает оптимизацию хранилища, которую даёт CSI driver, с приростом производительности и повышенной отказоустойчивостью инъекции через ephemeral volume для выбранных подов и приложений.

Example scenarios:

* [NGINX instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") и prior injection рекомендуются с ephemeral volume для более высокой отказоустойчивости, в то время как остальные workloads можно инъецировать через CSI driver, что устраняет необходимость в каких-либо vendor-специфичных аннотациях.
* Смешанные конфигурации с доступом к ноде и без него, например AWS Elastic Kubernetes Service (EKS) с EC2-нодами и Fargate. Нужно убедиться, что CSI driver доступен на всех нодах, где может происходить инъекция code module на основе CSI.