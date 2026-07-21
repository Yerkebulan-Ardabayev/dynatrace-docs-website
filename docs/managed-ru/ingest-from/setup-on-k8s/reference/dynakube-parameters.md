---
title: Параметры DynaKube для оператора Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters
---

# Параметры DynaKube для оператора Dynatrace

# Параметры DynaKube для оператора Dynatrace

* 57 минут на чтение
* Обновлено 10 июля 2026

Эта страница поможет разобраться и настроить пользовательский ресурс DynaKube [Kubernetes Custom Resource﻿](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), что позволяет оптимизировать настройку оператора Dynatrace под конкретные требования.

В таблице ниже указаны требуемые версии оператора Dynatrace, соответствующие каждой версии DynaKube API.

| Версия DynaKube API | Минимальная версия оператора Dynatrace | Максимальная версия оператора Dynatrace [1](#fn-1-1-def) |
| --- | --- | --- |
| `v1beta6` | 1.8 |  |
| `v1beta5` | 1.6 |  |
| `v1beta4` | 1.5 |  |
| `v1beta3` | 1.4 | 1.7 |
| `v1beta2` | 1.2 | 1.6 |
| `v1beta1` | Все версии | 1.6 |

1

Соответствующие версии DynaKube API будут удалены из оператора Dynatrace в следующем минорном или мажорном релизе.

Примеры YAML DynaKube смотри на [GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.10.0/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Версия оператора Dynatrace 1.8.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующей DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS укажи в `YOUR_ENVIRONMENT_ID` идентификатор своей среды.- Для Managed измени адрес `apiUrl`.Инструкции по определению идентификатора среды и настройке адреса apiUrl смотри в разделе [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") | Нет значения по умолчанию (обязателен) | string |
| `customPullSecret` | Определяет пользовательский pull secret для приватного реестра. Он аутентифицирует только компоненты, управляемые оператором, в пространстве имён `dynatrace`, и не распространяется на инжектируемые поды приложений. Подробности см. в разделах [Create a pull secret](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry") и [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry"). | Нет значения по умолчанию (необязателен) | string |
| `dynatraceApiRequestThreshold` | Минимальное количество минут между запросами API Dynatrace. | 15 | integer |
| `enableIstio` | При включении, если в среде Kubernetes установлен Istio, оператор Dynatrace создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster из OneAgent или ActiveGate.По умолчанию отключено. | Нет значения по умолчанию (необязателен) | boolean |
| `networkZone` | Задаёт сетевую зону для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязателен) | string |
| `proxy` | Задай пользовательские настройки прокси напрямую либо из secret с полем `proxy`.Применяется к оператору Dynatrace, ActiveGate и OneAgent.| Нет значения по умолчанию (необязателен) | DynaKubeProxy |
| `publicRegistryOverride` | Переопределяет реестр по умолчанию, используемый для разрешения образов компонентов мониторинга. Оператор Dynatrace передаёт указанный хост реестра в среду Dynatrace. Поддерживаемые значения: `public.ecr.aws` (Amazon ECR Public) или `registry-1.docker.io` (Docker Hub). Подробнее см. в разделе [Resolve public registry images automatically](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (необязателен) | string |
| `resourceAttributes` | Атрибуты ресурса, которые оператор Dynatrace применяет ко всем сигналам телеметрии. Доступно начиная с версии оператора Dynatrace 1.10.0. | Нет значения по умолчанию (необязателен) | map[string]string |
| `skipCertCheck` | Отключает проверку сертификата для соединения между оператором Dynatrace и Dynatrace Cluster.Установи `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязателен) | boolean |
| `tokens` | Имя secret, содержащего токены, используемые для подключения к Dynatrace. | Нет значения по умолчанию (необязателен) | string |
| `trustedCAs` | Добавляет пользовательские RootCA из configmap.Ключ данных должен называться `certs`.Применяется к оператору Dynatrace, OneAgent и ActiveGate. | Нет значения по умолчанию (необязателен) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажи имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются оба варианта, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязателен) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OneAgent, объединяются с `.spec.resourceAttributes`. Доступно начиная с оператора Dynatrace 1.10.0. | Нет значения по умолчанию (необязателен) | map[string]string |
| `annotations` | Добавь пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязателен) | map[string]string |
| `args` | Задай дополнительные аргументы для установщика OneAgent.Доступные варианты см. в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (необязателен) | []string |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Избегай изменяемых тегов вроде `latest`, используй digest или неизменяемый тег для воспроизводимых развёртываний. | Нет значения по умолчанию (необязателен) | string |
| `codeModulesImagePullPolicy` | Определяет политику pull для образа CodeModules. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязателен) | string |
| `dnsPolicy` | Задай политику DNS для подов OneAgent.Подробности см. в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задай дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязателен) | []EnvVar |
| `image` | Используй пользовательский образ Docker для OneAgent. Если задано, переопределяет образ, автоматически разрешаемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `imagePullPolicy` | Определяет политику pull для образа. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязателен) | string |
| `initResources` | Задай запросы и лимиты ресурсов для initContainer. Подробности см. в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязателен) | ResourceRequirements |
| `labels` | Заданные метки для подов OneAgent, чтобы структурировать нагрузки нужным образом. | Нет значения по умолчанию (необязателен) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые нужно инжектировать оператору Dynatrace.Подробнее см. в разделе [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (необязателен) | LabelSelector |
| `nodeSelector` | Укажи селектор узлов, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязателен) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию в [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, нужные для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязателен) | ResourceRequirements |
| `priorityClassName` | Присвой класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности см. в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязателен) | string |
| `rollingUpdate` | Задай настройки rollingUpdate для UpdateStrategy DaemonSet OneAgent.Подробности см. в разделе [DaemonSet specification﻿](https://dt-url.net/v0038c5). | Нет значения по умолчанию (необязателен) | RollingUpdateDaemonSet |
| `secCompProfile` | Профиль SecComp, который будет настроен для работы в режиме безопасных вычислений. | Нет значения по умолчанию (необязателен) | string |
| `storageHostPath` | Доступная для записи директория в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязателен) | string |
| `tolerations` | Toleration'ы, включаемые в DaemonSet OneAgent.Подробности см. в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязателен) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

Classic Full-Stack mode не поддерживается при использовании [platform token](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), а также в средах Latest Dynatrace.

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OneAgent, объединяются с `.spec.resourceAttributes`. Доступно начиная с Dynatrace Operator 1.10.0. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опционально) | []string |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опционально) | []EnvVar |
| `image` | Использует пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `imagePullPolicy` | Определяет image pull policy. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `labels` | Пользовательские метки (labels) для подов OneAgent с целью структурирования нагрузок по своему усмотрению. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление ресурсов OneAgent сильно зависит от нагрузки, которая мониторится. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для пода. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `priorityClassName` | Назначает priority class для подов OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `rollingUpdate` | Задаёт настройки rollingUpdate для UpdateStrategy DaemonSet OneAgent.Подробности см. в [DaemonSet specification﻿](https://dt-url.net/v0038c5). | Нет значения по умолчанию (опционально) | RollingUpdateDaemonSet |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (опционально) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OneAgent, объединяются с `.spec.resourceAttributes`. Доступно начиная с Dynatrace Operator 1.10.0. | Нет значения по умолчанию (опционально) | map[string]string |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Следует избегать изменяемых тегов, таких как `latest`, и использовать digest или неизменяемый тег для воспроизводимых развёртываний. | Нет значения по умолчанию (опционально) | string |
| `codeModulesImagePullPolicy` | Определяет image pull policy для образа CodeModules. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `imagePullPolicy` | Определяет image pull policy. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `initResources` | Задаёт запросы и ограничения ресурсов для initContainer. Подробности см. в [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно внедрять Dynatrace Operator.Подробнее см. в [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (опционально) | LabelSelector |
| `version` | Версия OneAgent, которая будет использоваться. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OneAgent, объединяются с `.spec.resourceAttributes`. Доступно начиная с Dynatrace Operator 1.10.0. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опционально) | []string |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опционально) | []EnvVar |
| `image` | Использует пользовательский образ Docker для OneAgent. Если задано, переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `imagePullPolicy` | Определяет image pull policy. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `labels` | Пользовательские метки (labels) для подов OneAgent с целью структурирования нагрузок по своему усмотрению. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление ресурсов OneAgent сильно зависит от нагрузки, которая мониторится. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для пода. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `priorityClassName` | Назначает priority class для подов OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `rollingUpdate` | Задаёт настройки rollingUpdate для UpdateStrategy DaemonSet OneAgent.Подробности см. в [DaemonSet specification﻿](https://dt-url.net/v0038c5). | Нет значения по умолчанию (опционально) | RollingUpdateDaemonSet |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (опционально) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские ActiveGate аннотации. | Нет значения по умолчанию (необязательный) | map[string]string |
| `capabilities` | Определяет ActiveGate pod capabilities: какая функциональность должна быть включена.Возможные значения:- `routing` включает OneAgent routing.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-2-1-def) открывает metrics ingest endpoint на ActiveGate ActiveGate и перенаправляет на него все pod'ы.- `dynatrace-api`[1](#fn-2-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательный) | string |
| `customProperties` | Добавляет файл пользовательских свойств, передав его как значение или сославшись на него из secret.При ссылке на файл пользовательских свойств из secret ключ должен называться `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств") | Нет значения по умолчанию (необязательный) | string |
| `dnsPolicy` | Задаёт DNS policy для ActiveGate pod'ов. | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для ActiveGate pod'ов. | Нет значения по умолчанию (необязательный) | []EnvVar |
| `group` | Задаёт группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использует пользовательский ActiveGate image. По умолчанию используется последний ActiveGate image из кластера Dynatrace. Если задан, переопределяет image, автоматически определяемый через [публичный registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator для использования публичных registry-образов для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Нет значения по умолчанию (необязательный) | string |
| `imagePullPolicy` | Определяет image pull policy. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательный) | string |
| `labels` | Заданные метки для ActiveGate pod'ов для структурирования нагрузок нужным образом. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательный) | map[string]string |
| `priorityClassName` | Назначает класс приоритета для ActiveGate pod'ов. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательный) | string |
| `replicas` | Количество реплик ActiveGate pod'ов. | 1 | int |
| `rollingUpdate` | Задаёт настройки rollingUpdate для UpdateStrategy ActiveGate StatefulSet. Подробнее см. [StatefulSet Specification﻿](https://dt-url.net/ql238m1).  UpdateStrategy для StatefulSet требует Kubernetes версии 1.35 и выше. На более низких версиях настройка игнорируется, и Operator предупреждает о проигнорированных настройках, если они были заданы. | Нет значения по умолчанию (необязательный) | RollingUpdateStatefulSetStrategy |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от нагрузки, за которой ведётся наблюдение; значения нужно корректировать соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds pod'а ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | Нет значения по умолчанию (необязательный) | int |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в средах с сетевыми ограничениями, настройки, связанные с сетью, и конфигурации прокси."). | Нет значения по умолчанию (необязательный) | string |
| `tolerations` | Задаёт tolerations для ActiveGate pod'ов.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к ActiveGate pod'ам. | Нет значения по умолчанию (необязательный) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли ephemeral volume для хранения. | Нет значения по умолчанию (необязательный) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и позволяет задать Source для атрибутов конкретного провайдера. | Нет значения по умолчанию (необязательный) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `initResources` | Задаёт запросы и лимиты ресурсов для init-контейнера, используемого для отдельного (standalone) обогащения метаданных. Учитывается только когда не внедрён OneAgent. Подробнее см. [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `namespaceSelector` | Namespace'ы, в которые нужно выполнять внедрение Dynatrace Operator. Подробнее см. [Настройка мониторинга для namespace'ов и Pod'ов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для namespace'ов и pod'ов"). | Нет значения по умолчанию (необязательный) | LabelSelector |

## `.spec.extensions`

Доступно в одной из будущих версий Dynatrace.

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `prometheus` | Включает расширение prometheus. | Нет значения по умолчанию (необязательный) |  |
| `databases` | Список расширений баз данных. | Нет значения по умолчанию (необязательный) | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.extensions.databases`

Доступно в одной из будущих версий Dynatrace.

* Все параметры, кроме `id`, необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `id` | Уникальное имя объекта Kubernetes. | Нет значения по умолчанию (обязательный) | string |
| `replicas` | Количество реплик SQL Extension Executor. | 1 | int32 |
| `volumes` | Volume'ы для файловой аутентификации. | Нет значения по умолчанию (необязательный) | []Volume |
| `volumeMounts` | Volume mount'ы для файловой аутентификации. | Нет значения по умолчанию (необязательный) | []VolumeMount |
| `serviceAccountName` | ServiceAccount для IAM-аутентификации. | Нет значения по умолчанию (необязательный) | string |
| `labels` | Метки SQL Extension Executor. | Нет значения по умолчанию (необязательный) | []Label |
| `annotations` | Аннотации SQL Extension Executor. | Нет значения по умолчанию (необязательный) | []Annotation |
| `affinity` | Affinity SQL Extension Executor. | Нет значения по умолчанию (необязательный) | []Affinity |
| `resources` | Ресурсы SQL Extension Executor. | Нет значения по умолчанию (необязательный) | ResourcesSpec |
| `nodeSelector` | Node selector SQL Extension Executor. | Нет значения по умолчанию (необязательный) | NodeSelectorSpec |
| `topologySpreadConstraints` | Topology spread constraints SQL Extension Executor. | Нет значения по умолчанию (необязательный) | TopologySpreadConstraints |

На OpenShift использование volume'ов типа `hostPath` запрещено стандартным SCC и приведёт к сбоям. Если `hostPath` необходим, создайте роль с достаточными привилегиями и привяжите её к соответствующему service account. В этом примере созданная роль привязана к service account с именем `custom-sql-extension-executor-sa`:

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: Role



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-role



namespace: dynatrace



rules:



- apiGroups:



- ""



resources:



- pods



verbs:



- list



- apiGroups:



- security.openshift.io



resourceNames:



- nonroot-v2



resources:



- securitycontextconstraints



verbs:



- use



---



kind: RoleBinding



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-rolebinding



namespace: dynatrace



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: Role



name: custom-sql-extension-executor-role



subjects:



- kind: ServiceAccount



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



kind: Dynakube



spec:



extensions:



databases:



- id: my-sql-db



serviceAccountName: custom-sql-extension-executor-sa
```

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Для использования KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Указывает пути хоста, которые монтируются в контейнер NCC. | Значения по умолчанию нет, рекомендуемое значение:  - /boot  - /etc  - /proc/sys/kernel  - /sys/fs  - /sys/kernel/security/apparmor  - /usr/lib/systemd/system  - /var/lib | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Доступно с Dynatrace версии 1.306 и OneAgent 1.305

Log Monitoring требует включения [возможности ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно развёртывается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия для сопоставления атрибутов приёма данных. | Нет значения по умолчанию (опционально) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемое. После установки оно больше не будет обновляться.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма данных. | Нет значения по умолчанию (опционально) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма данных применялось. | Нет значения по умолчанию (опционально) | []string |

#### Пример:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator версии 1.6.0+

Включает дополнительные [конечные точки приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.") в Kubernetes для приёма данных внутри кластера с использованием сторонних протоколов. Добавление этого раздела разворачивает в кластере рабочую нагрузку Dynatrace Collector.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Задаёт протоколы, данные которых будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Задаёт имя используемого сервиса. Если не указано, serviceName устанавливается по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, используемый telemetryIngest. | Нет значения по умолчанию (опционально) | string |

## `.spec.otlpExporterConfiguration`

Dynatrace Operator версии 1.8.0+

Включает автоматическую [настройку экспортёра OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматическая настройка экспортёра OTLP в приложениях, инструментированных SDK OpenTelemetry, с помощью Dynatrace Operator.") для подов приложений, уже инструментированных SDK OpenTelemetry.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OTLP, объединяемые с `.spec.resourceAttributes` и внедряемые в `OTEL_RESOURCE_ATTRIBUTES`. Доступно начиная с Dynatrace Operator 1.10.0. | Нет значения по умолчанию (опционально) | map[string]string |
| `signals` | Сигналы OpenTelemetry, которые будут автоматически приниматься в Dynatrace. | Нет значения по умолчанию (опционально) | [signalConfiguration](#otlp-exporter-signals) |
| `namespaceSelector` | Пространства имён, в которые будет внедряться конфигурация экспортёра OTLP. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides#annotate "Подробное описание вариантов установки и настройки для конкретных случаев использования") | Нет значения по умолчанию (опционально) | LabelSelector |
| `overrideEnvVars` | Включает переопределение существующих переменных окружения конфигурации экспортёра OTLP. | false | boolean |

## `.spec.otlpExporterConfiguration.signals`

Dynatrace Operator версии 1.8.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `logs` | Включает автоматическую настройку экспортёра OTLP для логов. См. [endpoint urls for otlphttp﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | Нет значения по умолчанию (опционально) | object |
| `metrics` | Включает автоматическую настройку экспортёра OTLP для метрик. См. [endpoint urls for otlphttp﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | Нет значения по умолчанию (опционально) | object |
| `traces` | Включает автоматическую настройку экспортёра OTLP для трейсов. См. [endpoint urls for otlphttp﻿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp) | Нет значения по умолчанию (опционально) | object |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определяет updateStrategy для daemonSet Node Configuration Collector | Нет значения по умолчанию (опционально) | DaemonSetUpdateStrategy |
| `labels` | Добавляет пользовательские labels к подам Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Добавляет пользовательские annotations к подам Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт nodeSelector, определяющий, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (опционально) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, определяет приоритет Pod'а. Имя должно быть определено путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (опционально) | string |
| `resources` | Определяет запросы и ограничения ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `nodeAffinity` | Определяет nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (опционально) | NodeAffinity |
| `tolerations` | Задаёт tolerations для подов Node Configuration Collector. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `args` | Задаёт дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (опционально) | []string |
| `env` | Задаёт дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (опционально) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику pull образа. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `repository` | URL образа Node Configuration Collector. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа Node Configuration Collector. | Нет значения по умолчанию (опционально) | string |
| `digest` | Закрепляет образ по адресуемому по содержимому digest в формате `<algorithm>:<hex>` (например, `sha256:…`). При установке `tag` игнорируется. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.logMonitoring`

Доступно с Dynatrace версии 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские annotations к подам LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `labels` | Добавляет пользовательские labels к подам LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт nodeSelector, определяющий, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задаёт DNS-политику для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначает класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (опционально) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима безопасных вычислений для подов LogMonitoring. | Нет значения по умолчанию (опционально) | string |
| `resources` | Определяет запросы и ограничения ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `rollingUpdate` | Определяет настройки rollingUpdate для UpdateStrategy DaemonSet LogMonitoring. Подробнее см. [DaemonSet specification﻿](https://dt-url.net/v0038c5). | Нет значения по умолчанию (опционально) | RollingUpdateDaemonSet |
| `tolerations` | Задаёт tolerations для подов LogMonitoring. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `args` | Задаёт дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (опционально) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно с Dynatrace версии 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (опционально) | string |
| `digest` | Закрепляет образ по content-addressable digest в формате `<algorithm>:<hex>` (например, `sha256:…`). Если задано, `tag` игнорируется. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.extensionExecutionController`

Доступно в одной из будущих версий Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указано, используется PVC по умолчанию. | Нет значения по умолчанию (опционально) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (опционально) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат для взаимодействия между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (опционально) | string |
| `customConfig` | ConfigMap с пользовательской конфигурацией Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `customExtensionCertificates` | Secret с сертификатами, использованными для подписи пользовательских расширений. Нужен для проверки подписи расширений компонентом Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения по топологии для пода Extension Execution Controller. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения данных. | Нет значения по умолчанию (опционально) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в одной из будущих версий Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `digest` | Закрепляет образ по content-addressable digest в формате `<algorithm>:<hex>` (например, `sha256:…`). Если задано, `tag` игнорируется. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator версии 1.6.0+

* Все параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (опционально) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Число реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, который Dynatrace Collector использует для проверки соединений с эндпоинтами других компонентов. | Нет значения по умолчанию (опционально) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения по топологии для пода Dynatrace Collector. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator версии 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если пусто, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | string |
| `repository` | URL образа Dynatrace Collector. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа Dynatrace Collector. | Нет значения по умолчанию (опционально) | string |
| `digest` | Закрепляет образ по content-addressable digest в формате `<algorithm>:<hex>` (например, `sha256:…`). Если задано, `tag` игнорируется. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.sqlExtensionExecutor`

Доступно в одной из будущих версий Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для SQL Extension Executor. | Нет значения по умолчанию (опционально) | [imageRef](#extensions-sql-extension-executor-image-ref) |
| `tolerations` | Tolerations для подов SQL Extension Executor. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |

## `.spec.templates.sqlExtensionExecutor.imageRef`

Доступно в одной из будущих версий Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа SQL Extension Executor. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа SQL Extension Executor. | Нет значения по умолчанию (опционально) | string |
| `digest` | Закрепляет образ по content-addressable digest в формате `<algorithm>:<hex>` (например, `sha256:…`). Если задано, `tag` игнорируется. | Нет значения по умолчанию (опционально) | string |

Dynatrace Operator версии 1.6.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS укажите `YOUR_ENVIRONMENT_ID` как идентификатор своей среды.- Для Managed измените адрес `apiUrl`.Инструкции по определению идентификатора среды и настройке адреса apiUrl см. в разделе [ID Environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull secret для приватного реестра. Аутентифицирует только компоненты, управляемые оператором, в пространстве имён `dynatrace`, и не распространяется на поды приложений, в которые выполнена инъекция. Подробнее см. [Create a pull secret](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry") и [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry"). | Нет значения по умолчанию (опционально) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами API Dynatrace. | 15 | integer |
| `enableIstio` | Если включено и в среде Kubernetes установлен Istio, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster из OneAgent или ActiveGate.По умолчанию отключено. | Нет значения по умолчанию (опционально) | boolean |
| `networkZone` | Задаёт сетевую зону для подов OneAgent и ActiveGate. | Нет значения по умолчанию (опционально) | string |
| `proxy` | Настройка пользовательского прокси напрямую либо из secret с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent'ам. | Нет значения по умолчанию (опционально) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (опционально) | boolean |
| `tokens` | Имя secret, содержащего токены, используемые для подключения к Dynatrace. | Нет значения по умолчанию (опционально) | string |
| `trustedCAs` | Добавляет пользовательские RootCA из configmap.Ключ данных должен называться `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (опционально) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее, чем ныне устаревший аргумент `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (опционально) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задать дополнительные аргументы для установщика OneAgent.Доступные параметры описаны в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепить версию OneAgent на тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Не использовать изменяемые теги вроде `latest`, а использовать digest или неизменяемый тег для воспроизводимых развёртываний. | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задать DNS-политику для подов OneAgent.Подробности в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Использовать пользовательский образ OneAgent Docker. При указании переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `initResources` | Определить запросы и лимиты ресурсов для initContainer. Подробности в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные пользователем метки для подов OneAgent для структурирования workloads нужным образом. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator.Подробнее в разделе [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Указать node selector, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемого workload'а. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступная для записи директория в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations для включения в DaemonSet OneAgent.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для host monitoring OneAgent, работающего в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для application monitoring. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задать дополнительные аргументы для установщика OneAgent.Доступные параметры описаны в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепить версию OneAgent на тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS-политику для подов OneAgent.Подробности в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Использовать пользовательский образ OneAgent Docker. По умолчанию используется образ из кластера Dynatrace. | Название образа. | string |
| `labels` | Заданные пользователем метки для подов OneAgent для структурирования workloads нужным образом. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Указать node selector, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемого workload'а. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступная для записи директория в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations для включения в DaemonSet OneAgent.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Не использовать изменяемые теги вроде `latest`, а использовать digest или неизменяемый тег для воспроизводимых развёртываний. | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определить запросы и лимиты ресурсов для initContainer. Подробности в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator.Подробнее в разделе [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательные.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательный) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (необязательный) | []string |
| `autoUpdate` (**устарел**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent.Подробности в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательный) | []EnvVar |
| `image` | Использует пользовательский образ OneAgent Docker. Если задан, переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `labels` | Заданные пользователем метки для подов OneAgent для структурирования нагрузок нужным образом. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательный) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать значения по умолчанию в [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательный) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для работы в режиме безопасных вычислений. | Нет значения по умолчанию (необязательный) | string |
| `storageHostPath` | Каталог с правом записи в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательный) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязательный.
* Параметры `resources` и `group` рекомендуемые.
* Все остальные параметры необязательные.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательный) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какой функционал должен быть включён.Возможные значения:- `routing` включает роутинг OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-3-1-def) открывает эндпоинт для приёма метрик на DynaKube ActiveGate и перенаправляет на него все поды.- `dynatrace-api`[1](#fn-3-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает модуль [Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") в ActiveGate. | Нет значения по умолчанию (обязательный) | string |
| `customProperties` | Добавляет файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробности в [How to add a custom properties file](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file"). | Нет значения по умолчанию (необязательный) | string |
| `dnsPolicy` | Задаёт DNS policy для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательный) | []EnvVar |
| `group` | Задаёт группу активации для ActiveGate. Подробности в [Customize ActiveGate properties](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements."). | Нет значения по умолчанию (рекомендуемый) | string |
| `image` | Использует пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задан, переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (необязательный) | string |
| `labels` | Заданные пользователем метки для подов ActiveGate для структурирования нагрузок нужным образом. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательный) | map[string]string |
| `priorityClassName` | Назначает класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробности в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательный) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой нагрузки, значения нужно подбирать соответственно. | Нет значения по умолчанию (рекомендуемый) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются правила и значения по умолчанию Kubernetes. | Нет значения по умолчанию (необязательный) | int |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задан, используется самоподписанный сертификат. Подробности в [How to add a custom certificate for ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Нет значения по умолчанию (необязательный) | string |
| `tolerations` | Задаёт tolerations для подов ActiveGate.Подробности в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательный) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательный) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и позволяет задать Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательный) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробности в параметре `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательные.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator. Подробнее в [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (необязательный) | LabelSelector |

### Неявное обогащение метаданных

Dynatrace Operator версии 1.9.0+

Когда для пространства имён настроена инъекция OneAgent, обогащение метаданных для этого пространства имён включается неявно, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в одной из будущих версий Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Для использования расширений

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Для использования KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.
* Все параметры в `.spec.kspm` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Задаёт пути хоста, монтируемые в контейнер NCC. | Значения по умолчанию нет (необязательный) | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выводит предупреждение, но Log Monitoring всё равно развёртывается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия для сопоставления атрибутов приёма (ingest). | Значения по умолчанию нет (необязательный) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемое. После установки оно больше не будет обновляться.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма. | Значения по умолчанию нет (необязательный) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма применялось. | Значения по умолчанию нет (необязательный) | []string |

#### Пример:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator версии 1.6.0+

Включает [конечные точки телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включить конечные точки приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.") Dynatrace в Kubernetes для приёма данных внутри кластера. Добавление этого раздела приводит к развёртыванию Dynatrace Collector силами Dynatrace Operator.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Задаёт протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Задаёт имя используемого сервиса. Если не указано, serviceName устанавливается по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, используемый telemetryIngest. | Значения по умолчанию нет (необязательный) | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определяет updateStrategy daemonSet Node Configuration Collector | Значения по умолчанию нет (необязательный) | DaemonSetUpdateStrategy |
| `labels` | Добавляет пользовательские метки к подам Node Configuration Collector. | Значения по умолчанию нет (необязательный) | map[string]string |
| `annotations` | Добавляет пользовательские аннотации к подам Node Configuration Collector. | Значения по умолчанию нет (необязательный) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будут развёрнуты поды Node Configuration Collector. | Значения по умолчанию нет (необязательный) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Значения по умолчанию нет (необязательный) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, задаёт приоритет Pod'а. Имя должно быть определено путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Значения по умолчанию нет (необязательный) | string |
| `resources` | Определяет запросы и лимиты ресурсов для подов Node Configuration Collector. | Значения по умолчанию нет (необязательный) | ResourceRequirements |
| `nodeAffinity` | Определяет nodeAffinity для DaemonSet Node Configuration Collector | Значения по умолчанию нет (необязательный) | NodeAffinity |
| `tolerations` | Задаёт tolerations для подов Node Configuration Collector. Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (необязательный) | []Toleration |
| `args` | Задаёт дополнительные аргументы для основного контейнера Node Configuration Collector. | Значения по умолчанию нет (необязательный) | []string |
| `env` | Задаёт дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Значения по умолчанию нет (необязательный) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Node Configuration Collector. | Значения по умолчанию нет (необязательный) | string |
| `tag` | Тег образа Node Configuration Collector. | Значения по умолчанию нет (необязательный) | string |

## `.spec.templates.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации к подам LogMonitoring. | Значения по умолчанию нет (необязательный) | map[string]string |
| `labels` | Добавляет пользовательские метки к подам LogMonitoring. | Значения по умолчанию нет (необязательный) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будут развёрнуты поды LogMonitoring. | Значения по умолчанию нет (необязательный) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Значения по умолчанию нет (обязательный) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задаёт DNS-политику для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначает класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Значения по умолчанию нет (необязательный) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима безопасных вычислений для подов LogMonitoring. | Значения по умолчанию нет (необязательный) | string |
| `resources` | Определяет запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Значения по умолчанию нет (необязательный) | ResourceRequirements |
| `tolerations` | Задаёт tolerations для подов LogMonitoring. Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (необязательный) | []Toleration |
| `args` | Задаёт дополнительные аргументы для init-контейнера LogMonitoring. | Значения по умолчанию нет (необязательный) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Значения по умолчанию нет (необязательный) | string |
| `tag` | Тег образа LogMonitoring. | Значения по умолчанию нет (необязательный) | string |

## `.spec.templates.extensionExecutionController`

Доступно в одной из будущих версий Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Значения по умолчанию нет (обязательный) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указан, используется PVC по умолчанию. | Значения по умолчанию нет (необязательный) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Значения по умолчанию нет (необязательный) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Значения по умолчанию нет (необязательный) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат для взаимодействия между Extension Execution Controller и Dynatrace Collector. | Значения по умолчанию нет (необязательный) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Значения по умолчанию нет (необязательный) | string |
| `customExtensionCertificates` | Secret, содержащий сертификаты, использованные для подписи пользовательских extensions. Необходим для проверки подписи extensions со стороны Extension Execution Controller. | Значения по умолчанию нет (необязательный) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Значения по умолчанию нет (необязательный) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller. Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (необязательный) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения по топологии (topology spread constraints) для пода Extension Execution Controller. | Значения по умолчанию нет (необязательный) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли для хранения эфемерный том (ephemeral volume). | Значения по умолчанию нет (необязательный) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в одной из будущих версий Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Значения по умолчанию нет (необязательный) | string |
| `tag` | Тег образа Extension Execution Controller. | Значения по умолчанию нет (необязательный) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator версии 1.6.0+

* Все параметры не обязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, который используется для Dynatrace Collector. | Нет значения по умолчанию (не обязательно) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (не обязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (не обязательно) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, который Dynatrace Collector использует для проверки подключений к конечным точкам других компонентов. | Нет значения по умолчанию (не обязательно) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (не обязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (не обязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Dynatrace Collector. | Нет значения по умолчанию (не обязательно) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator версии 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator версии 1.5.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры не обязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS укажите в `YOUR_ENVIRONMENT_ID` идентификатор среды.- Для Managed измените адрес `apiUrl`.Инструкции по определению идентификатора среды и настройке адреса apiUrl см. в [ID Environment](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор своей среды и как настроить и подключить несколько сред.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull secret на случай, если для образов, заданных в DynaKube, используется приватный реестр. Примечание: для [загрузки образа узла через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, загрузку образа через CSI-драйвер и ZIP-загрузку.") нужно убедиться, что pull secret доступны в инжектированном поде. Подробнее см. [предварительные требования](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#prerequisites "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, загрузку образа через CSI-драйвер и ZIP-загрузку."). Чтобы задать пользовательский pull secret и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (не обязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальный интервал в минутах между запросами API Dynatrace. | 15 | integer |
| `enableIstio` | При включении, если в среде Kubernetes установлен Istio, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster из OneAgent или ActiveGate. По умолчанию отключено. | Нет значения по умолчанию (не обязательно) | boolean |
| `networkZone` | Задаёт зону сети для подов OneAgent и ActiveGate. | Нет значения по умолчанию (не обязательно) | string |
| `proxy` | Задаёт пользовательские настройки прокси либо напрямую, либо из secret с полем `proxy`. Применяется к Dynatrace Operator, ActiveGate и OneAgent'ам. | Нет значения по умолчанию (не обязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster. Установите значение `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (не обязательно) | boolean |
| `tokens` | Имя secret, хранящего токены, используемые для подключения к Dynatrace. | Нет значения по умолчанию (не обязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCA из configmap. Ключ данных должен называться `certs`. Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (не обязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее теперь устаревшего аргумента `--set-host-group`. Если используются оба параметра, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (не обязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры не обязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | Нет значения по умолчанию (не обязательно) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent. Доступные параметры см. в [Пользовательская установка для Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки."). Список ограничений см. в [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker."). | Нет значения по умолчанию (не обязательно) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в своём тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для всех компонентов, управляемых Dynatrace Operator"). Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Ссылка на образ контейнера для модулей кода. Избегайте изменяемых тегов, например `latest`, и используйте digest или неизменяемый тег для воспроизводимых развёртываний. | Нет значения по умолчанию (не обязательно) | string |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent. Подробнее см. [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (не обязательно) | []EnvVar |
| `image` | Использовать пользовательский образ Docker для OneAgent. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного реестра для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Образ из кластера Dynatrace. | string |
| `initResources` | Задаёт запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (не обязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать нагрузки нужным образом. | Нет значения по умолчанию (не обязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инжектирование. Подробнее см. [Настройка мониторинга для namespace и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для namespace и подов"). | Нет значения по умолчанию (не обязательно) | LabelSelector |
| `nodeSelector` | Укажите node selector, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (не обязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от нагрузки, за которой нужно наблюдать. Можно использовать настройки по умолчанию из примеров DynaKube на [GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.10.0/assets/samples/dynakube). `resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (не обязательно) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета подам OneAgent. По умолчанию класс не задан. Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (не обязательно) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (не обязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе узла, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (не обязательно) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (не обязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent'ов мониторинга хоста, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры опциональны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | No default (optional) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | No default (optional) | []string |
| `autoUpdate` (**deprecated**) | Устаревшее поле, которое будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для Pod'ов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для Pod'ов OneAgent. | No default (optional) | []EnvVar |
| `image` | Использовать пользовательский образ Docker OneAgent. По умолчанию используется образ из кластера Dynatrace. | Name of the image. | string |
| `labels` | Заданные пользователем метки для Pod'ов OneAgent, позволяющие структурировать нагрузки нужным образом. | No default (optional) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будет развёрнут OneAgent. | No default (optional) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для Pod'а. | No default (optional) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета для Pod'ов OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | No default (optional) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | No default (optional) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | No default (optional) | string |
| `tolerations` | Tolerations, которые нужно включить в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | No default (optional) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры опциональны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Избегайте изменяемых тегов, таких как `latest`, и используйте digest или неизменяемый тег для воспроизводимых развёртываний. | No default (optional) | string |
| `initResources` | Задаёт requests и limits ресурсов для initContainer. Подробности см. в [Managing resources for containers﻿](https://dt-url.net/atc371q). | No default (optional) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инъекцию.Подробнее см. в [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | No default (optional) | LabelSelector |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры опциональны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | No default (optional) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | No default (optional) | []string |
| `autoUpdate` (**deprecated**) | Устаревшее поле, которое будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для Pod'ов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для Pod'ов OneAgent. | No default (optional) | []EnvVar |
| `image` | Использовать пользовательский образ Docker OneAgent. Если задано, переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | The image from the Dynatrace cluster. | string |
| `labels` | Заданные пользователем метки для Pod'ов OneAgent, позволяющие структурировать нагрузки нужным образом. | No default (optional) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будет развёрнут OneAgent. | No default (optional) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для Pod'а. | No default (optional) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета для Pod'ов OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | No default (optional) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | No default (optional) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | No default (optional) | string |
| `tolerations` | Tolerations, которые нужно включить в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | No default (optional) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязательный.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность нужно включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-4-1-def) открывает endpoint приёма метрик на ActiveGate DynaKube и перенаправляет на него все поды.- `dynatrace-api`[1](#fn-4-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить исходя из своих потребностей и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавляет файл пользовательских свойств, указав его как значение или через ссылку на secret.При ссылке на файл пользовательских свойств из secret нужно убедиться, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавить файл пользовательских свойств"). | Нет значения по умолчанию (опционально) | string |
| `dnsPolicy` | Устанавливает DNS-политику для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (опционально) | []EnvVar |
| `group` | Устанавливает группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить исходя из своих потребностей и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использует пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задан, переопределяет образ, автоматически определённый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Operator Dynatrace на использование образов из публичного реестра для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Нет значения по умолчанию (опционально) | string |
| `labels` | Заданные метки для подов ActiveGate для структурирования рабочих нагрузок нужным образом. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `priorityClassName` | Назначает класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой нагрузки, значения нужно подбирать соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются правила и значения по умолчанию Kubernetes. | Нет значения по умолчанию (опционально) | int |
| `tlsSecretName` | Имя secret, содержащего сертификат TLS, ключ и пароль ActiveGate. Если не задан, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройте Dynatrace в средах с ограничениями сети, сетевые параметры и конфигурации proxy."). | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Задаёт tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) для подов ActiveGate. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный volume для хранения. | Нет значения по умолчанию (опционально) | boolean |
| `persistentVolumeClaim` | Описывает общие атрибуты устройств хранения и позволяет задать Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (опционально) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые нужно внедрение Operator Dynatrace. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (опционально) | LabelSelector |

### Неявное обогащение метаданных

Operator Dynatrace версии 1.9.0+

Когда для пространства имён настроено внедрение OneAgent, обогащение метаданных для этого пространства имён включается неявно, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку extensions в Kubernetes. Для использования extensions

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* Feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed."). Для использования KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* Feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно в Dynatrace версии 1.306 и OneAgent 1.305

Log Monitoring требует включения [возможности ActiveGate](#active-gate) `kubernetes-monitoring`, но она не обязательно должна быть настроена в том же DynaKube. Если `kubernetes-monitoring` отсутствует или feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно развёртывается.

* Все параметры в `.spec.logMonitoring` опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия для сопоставления атрибутов приёма данных. | Нет значения по умолчанию (опционально) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемое. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма данных. | Нет значения по умолчанию (опционально) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма данных применилось. | Нет значения по умолчанию (опционально) | []string |

#### Пример:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Operator Dynatrace версии 1.6.0+

Добавление этого раздела приводит к развёртыванию Dynatrace Collector Operator'ом.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Задаёт протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Задаёт имя используемого сервиса. Если не указано, serviceName устанавливается по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret, содержащий сертификат TLS, используемый telemetryIngest. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Задаёт updateStrategy daemonSet Node Configuration Collector | Нет значения по умолчанию (необязательный) | DaemonSetUpdateStrategy |
| `labels` | Добавляет пользовательские labels к подам Node Configuration Collector. | Нет значения по умолчанию (необязательный) | map[string]string |
| `annotations` | Добавляет пользовательские annotations к подам Node Configuration Collector. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (необязательный) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (необязательный) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указан, определяет приоритет пода. Имя должно быть задано созданием объекта PriorityClass с этим именем. Если не указан, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (необязательный) | string |
| `resources` | Задаёт запросы и лимиты ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `nodeAffinity` | Задаёт nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (необязательный) | NodeAffinity |
| `tolerations` | Задаёт tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `args` | Задаёт дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательный) | []string |
| `env` | Задаёт дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательный) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Node Configuration Collector. | Нет значения по умолчанию (необязательный) | string |
| `tag` | Тег образа Node Configuration Collector. | Нет значения по умолчанию (необязательный) | string |

## `.spec.templates.logMonitoring`

Доступно начиная с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские annotations к подам LogMonitoring. | Нет значения по умолчанию (необязательный) | map[string]string |
| `labels` | Добавляет пользовательские labels к подам LogMonitoring. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (необязательный) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательный) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задаёт DNS policy для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначает класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (необязательный) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима безопасных вычислений для подов LogMonitoring. | Нет значения по умолчанию (необязательный) | string |
| `resources` | Задаёт запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `tolerations` | Задаёт tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `args` | Задаёт дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательный) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно начиная с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (необязательный) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (необязательный) | string |

## `.spec.templates.extensionExecutionController`

Доступно с будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательный) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указан, используется PVC по умолчанию. | Нет значения по умолчанию (необязательный) | PersistentVolumeClaim |
| `labels` | Labels, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательный) | map[string]string |
| `annotations` | Annotations, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательный) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат для взаимодействия между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (необязательный) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (необязательный) | string |
| `customExtensionCertificates` | Secret, содержащий сертификаты, использованные для подписи пользовательских расширений. Требуется для проверки подписи расширений Extension Execution Controller. | Нет значения по умолчанию (необязательный) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения топологии для пода Extension Execution Controller. | Нет значения по умолчанию (необязательный) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли ephemeral volume для хранения. | Нет значения по умолчанию (необязательный) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно с будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (необязательный) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (необязательный) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator версии 1.6.0+

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (необязательный) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Labels, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательный) | map[string]string |
| `annotations` | Annotations, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательный) | map[string]string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, используемый Dynatrace Collector для проверки соединений с эндпоинтами других компонентов. | Нет значения по умолчанию (необязательный) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения топологии для пода Dynatrace Collector. | Нет значения по умолчанию (необязательный) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator версии 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator версии 1.4.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, включая путь `/api` в конце.- Для SaaS укажи `YOUR_ENVIRONMENT_ID` как идентификатор своей среды.- Для Managed измени адрес `apiUrl`.Инструкции по определению идентификатора среды и настройке адреса apiUrl см. в [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") | Нет значения по умолчанию (обязательный) | string |
| `customPullSecret` | Задаёт кастомный pull secret на случай использования приватного реестра для образов, определённых в DynaKube. Примечание: для [загрузки образа на узел через ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") нужно убедиться, что pull secrets доступны для инжектируемого пода. Подробности см. в [требованиях](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#prerequisites "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). О настройке кастомного pull secret и ожидаемом поведении см. [Configure `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | Нет значения по умолчанию (опциональный) | string |
| `dynatraceApiRequestThreshold` | Минимальный интервал в минутах между запросами Dynatrace API. | 15 | integer |
| `enableIstio` | Если включено и на среде Kubernetes установлен Istio, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster из OneAgent или ActiveGate.По умолчанию отключено. | Нет значения по умолчанию (опциональный) | boolean |
| `networkZone` | Задаёт сетевую зону для подов OneAgent и ActiveGate. | Нет значения по умолчанию (опциональный) | string |
| `proxy` | Задаёт кастомные настройки прокси напрямую или из secret с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent'ам. | Нет значения по умолчанию (опциональный) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установи `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (опциональный) | boolean |
| `tokens` | Имя secret, хранящего токены для подключения к Dynatrace. | Нет значения по умолчанию (опциональный) | string |
| `trustedCAs` | Добавляет кастомные RootCA из configmap.Ключ данных должен называться `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (опциональный) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажи имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются оба варианта, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (опциональный) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры опциональны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет кастомные аннотации OneAgent. | Нет значения по умолчанию (опциональный) | map[string]string |
| `args` | Задаёт дополнительные аргументы для инсталлятора OneAgent.Доступные опции см. в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опциональный) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, которое будет удалено в одном из будущих релизов. [Закрепи версию OneAgent на своём тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Образ OneAgent, используемый для инжекции в поды. Если задан, переопределяет образ CodeModules, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (опциональный) | string |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опциональный) | []EnvVar |
| `image` | Использует кастомный образ Docker OneAgent. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `initResources` | Определяет запросы и лимиты ресурсов для initContainer. Подробности см. в [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (опциональный) | ResourceRequirements |
| `labels` | Заданные метки для подов OneAgent, чтобы структурировать рабочие нагрузки нужным образом. | Нет значения по умолчанию (опциональный) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые нужно, чтобы Dynatrace Operator выполнял инжекцию.Подробнее см. [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (опциональный) | LabelSelector |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опциональный) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от контролируемой нагрузки. Можно использовать настройки по умолчанию в [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (опциональный) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опциональный) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме безопасных вычислений. | Нет значения по умолчанию (опциональный) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опциональный) | []Toleration |
| `version` | Версия OneAgent, используемая для мониторинга хостов OneAgent'ами, работающими в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | No default (optional) | map[string]string |
| `args` | Задаёт дополнительные аргументы для инсталлятора OneAgent.Доступные опции описаны в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | No default (optional) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для Pod'ов OneAgent.Подробности см. в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для Pod'ов OneAgent. | No default (optional) | []EnvVar |
| `image` | Используется для указания пользовательского образа Docker OneAgent. По умолчанию используется образ из кластера Dynatrace. | Name of the image. | string |
| `labels` | Определённые пользователем метки для Pod'ов OneAgent для структурирования workload'ов нужным образом. | No default (optional) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий, на каких узлах будет развёрнут OneAgent. | No default (optional) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для Pod'а. | No default (optional) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета Pod'ам OneAgent. По умолчанию класс не задан.Подробности см. в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | No default (optional) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | No default (optional) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | No default (optional) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для инъекции в Pod'ы. Если задан, переопределяет образ CodeModules, автоматически разрешаемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | No default (optional) | string |
| `initResources` | Определяет запросы и лимиты ресурсов для initContainer. Подробности см. в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | No default (optional) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator.Дополнительную информацию см. в разделе [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | No default (optional) | LabelSelector |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | No default (optional) | map[string]string |
| `args` | Задаёт дополнительные аргументы для инсталлятора OneAgent.Доступные опции описаны в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | No default (optional) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для Pod'ов OneAgent.Подробности см. в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для Pod'ов OneAgent. | No default (optional) | []EnvVar |
| `image` | Используется для указания пользовательского образа Docker OneAgent. Если задан, переопределяет образ, автоматически разрешаемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | The image from the Dynatrace cluster. | string |
| `labels` | Определённые пользователем метки для Pod'ов OneAgent для структурирования workload'ов нужным образом. | No default (optional) | map[string]string |
| `nodeSelector` | Задаёт node selector, определяющий, на каких узлах будет развёрнут OneAgent. | No default (optional) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для Pod'а. | No default (optional) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета Pod'ам OneAgent. По умолчанию класс не задан.Подробности см. в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | No default (optional) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | No default (optional) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | No default (optional) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | The latest version is used by default. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавление пользовательских аннотаций ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `capabilities` | Определяет capabilities пода ActiveGate: какую функциональность нужно включить.Возможные значения:- `routing` включает routing OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-5-1-def) открывает endpoint приёма метрик на ActiveGate DynaKube и перенаправляет на него все поды.- `dynatrace-api`[1](#fn-5-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить исходя из своих потребностей и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавление файла с пользовательскими свойствами: передать его как значение или сослаться на него из secret.При ссылке на файл с пользовательскими свойствами из secret ключ должен называться `customProperties`. Подробнее см. [Как добавить файл с пользовательскими свойствами](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла с пользовательскими свойствами"). | Нет значения по умолчанию (опционально) | string |
| `dnsPolicy` | Установка DNS-политики для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Установка дополнительных переменных окружения для подов ActiveGate. | Нет значения по умолчанию (опционально) | []EnvVar |
| `group` | Установка группы активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить исходя из своих потребностей и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использование пользовательского образа ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задано, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator на использование образов из публичного реестра для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Нет значения по умолчанию (опционально) | string |
| `labels` | Заданные пользователем метки для подов ActiveGate для структурирования workload'ов нужным образом. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Указание node selector, определяющего, на каких нодах будет развёрнут ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `priorityClassName` | Назначение класса приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемого workload'а, значения нужно корректировать соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в средах с сетевыми ограничениями, сетевых параметров и конфигураций прокси."). | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Установка tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |

1

Для этой capability требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Namespace'ы, в которые нужно выполнять инъекцию Dynatrace Operator. Подробнее см. [Настройка мониторинга для namespace'ов и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для namespace'ов и подов"). | Нет значения по умолчанию (опционально) | LabelSelector |

### Неявное обогащение метаданных

Dynatrace Operator версии 1.9.0+

Когда для namespace'а настроена инъекция OneAgent, обогащение метаданных для этого namespace'а включается неявно, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку extensions в Kubernetes. Для использования extensions

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список capabilities ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Для использования KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список capabilities ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно с Dynatrace версии 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая capability `kubernetes-monitoring` [ActiveGate](#active-gate), но она не обязательно должна быть настроена в том же DynaKube. Если `kubernetes-monitoring` отсутствует или feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выводит предупреждение, но Log Monitoring всё равно развёртывается.

* Все параметры в `.spec.logMonitoring` опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия для сопоставления атрибутов приёма данных. | Нет значения по умолчанию (опционально) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемое. После установки оно больше не будет обновляться.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма данных. | Нет значения по умолчанию (опционально) | string |
| `values` | Список значений, которым должен соответствовать `attribute`, чтобы правило приёма данных применялось. | Нет значения по умолчанию (опционально) | []string |

#### Пример:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определяет updateStrategy daemonSet'а Node Configuration Collector | Нет значения по умолчанию (опционально) | DaemonSetUpdateStrategy |
| `labels` | Добавление пользовательских меток к подам Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Добавление пользовательских аннотаций к подам Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Указание node selector, определяющего, на каких нодах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (опционально) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (опционально) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, задаёт приоритет пода. Имя должно быть определено путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (опционально) | string |
| `resources` | Определяет requests и limits ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `nodeAffinity` | Определяет nodeAffinity для DaemonSet'а Node Configuration Collector | Нет значения по умолчанию (опционально) | NodeAffinity |
| `tolerations` | Установка tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `args` | Установка дополнительных аргументов для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (опционально) | []string |
| `env` | Установка дополнительных переменных окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (опционально) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| repository | URL образа Node Configuration Collector. | Нет значения по умолчанию (опционально) | string |
| tag | Тег образа Node Configuration Collector. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.logMonitoring`

Доступно начиная с Dynatrace версии 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации к подам LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `labels` | Добавляет пользовательские метки к подам LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, определяющий, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (опционально) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задаёт политику DNS для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначает класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (опционально) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима безопасных вычислений для подов LogMonitoring. | Нет значения по умолчанию (опционально) | string |
| `resources` | Определяет запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `nodeAffinity` | Определяет nodeAffinity для DaemonSet NodeConfigurationCollector | Нет значения по умолчанию (опционально) | NodeAffinity |
| `tolerations` | Задаёт tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `args` | Задаёт дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (опционально) | []string |
| `updateStrategy` | Определяет updateStrategy для daemonSet NodeConfigurationCollector. | Нет значения по умолчанию (опционально) | DaemonSetUpdateStrategy |

## `.spec.templates.logMonitoring.imageRef`

Доступно начиная с Dynatrace версии 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.extensionExecutionController`

Доступно начиная с будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указан, используется PVC по умолчанию. | Нет значения по умолчанию (опционально) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (опционально) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат для связи между Extension Execution Controller и коллектором Dynatrace. | Нет значения по умолчанию (опционально) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `customExtensionCertificates` | Секрет, содержащий сертификаты, использованные для подписи пользовательских расширений. Требуется для проверки подписи расширений через Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения топологии (topology spread constraints) для пода Extension Execution Controller. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно начиная с будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (опционально) | string |

## `.spec.templates.otelCollector`

Доступно начиная с будущей версии Dynatrace.

* Все параметры опциональны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для коллектора Dynatrace. | Нет значения по умолчанию (опционально) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Число реплик коллектора Dynatrace. | 1 | int32 |
| `labels` | Метки, применяемые к поду коллектора Dynatrace. | Нет значения по умолчанию (опционально) | map[string]string |
| `annotations` | Аннотации, применяемые к поду коллектора Dynatrace. | Нет значения по умолчанию (опционально) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый коллектором Dynatrace для проверки соединений с эндпоинтами других компонентов. | Нет значения по умолчанию (опционально) | string |
| `resources` | Настройки ресурсов для пода коллектора Dynatrace. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `tolerations` | Tolerations для пода коллектора Dynatrace.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения топологии (topology spread constraints) для пода коллектора Dynatrace. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Доступно начиная с будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа коллектора Dynatrace. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа коллектора Dynatrace. | `latest` | string |

Dynatrace Operator версии 1.2.0, 1.6.0

Уведомление об устаревании

DynaKube API версии `v1beta2` больше не доступна начиная с Dynatrace Operator версии 1.7.0+.

## `.spec`

* Параметр `apiUrl` обязателен.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.Для SaaS задать `YOUR_ENVIRONMENT_ID` равным идентификатору окружения.Для Managed изменить адрес `apiUrl`.Инструкции по определению идентификатора окружения и настройке адреса apiUrl см. в [ID Environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Задаёт пользовательский pull secret на случай использования приватного реестра для образов, указанных в DynaKube.Примечание: для [загрузки образа узла через ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") нужно убедиться, что pull secrets доступны для инжектируемого пода. Подробнее см. [предварительные требования](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#prerequisites "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.").О том, как задать пользовательский pull secret и об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | Нет значения по умолчанию (опционально) | string |
| `dynatraceApiRequestThreshold` | Минимальное количество минут между запросами API Dynatrace. | 15 | integer |
| `enableIstio` | Если включено и Istio установлен в окружении Kubernetes, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к кластеру Dynatrace из OneAgent или ActiveGate.По умолчанию отключено. | Нет значения по умолчанию (опционально) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (опционально) | string |
| `proxy` | Задаёт пользовательские настройки прокси напрямую либо из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent.| Нет значения по умолчанию (опционально) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и кластером Dynatrace.Установить в `true`, чтобы пропустить проверки валидации сертификата. | Нет значения по умолчанию (опционально) | boolean |
| `tokens` | Имя секрета, содержащего токены, используемые для подключения к Dynatrace. | Нет значения по умолчанию (опционально) | string |
| `trustedCAs` | Добавляет пользовательские RootCA из configmap.Ключ данных должен называться `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (опционально) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Указывает имя группы, к которой нужно присвоить хост. Этот способ предпочтительнее устаревшего теперь аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (опционально) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры опциональны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `args` | Задать дополнительные аргументы для установщика OneAgent.Доступные параметры описаны в разделе [Кастомная установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опционально) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из будущих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Образ OneAgent, используемый для инъекции в поды. Если задан, переопределяет образ CodeModules, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (опционально) | string |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробности в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опционально) | []EnvVar |
| `image` | Использовать пользовательский образ Docker для OneAgent. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `initResources` | Определить requests и limits ресурсов для initContainer. Подробности в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `labels` | Заданные метки для подов OneAgent, чтобы структурировать рабочие нагрузки нужным образом. | Нет значения по умолчанию (опционально) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator.Подробнее в разделе [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (опционально) | LabelSelector |
| `nodeSelector` | Указать селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от нагрузки, которую нужно мониторить. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для пода. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Tolerations, которые нужно включить в DaemonSet OneAgent.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться для OneAgent мониторинга хостов, запущенных в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `args` | Задать дополнительные аргументы для установщика OneAgent.Доступные параметры описаны в разделе [Кастомная установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опционально) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из будущих релизов. [Закрепите версию OneAgent в тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробности в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опционально) | []EnvVar |
| `image` | Использовать пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `labels` | Заданные метки для подов OneAgent, чтобы структурировать рабочие нагрузки нужным образом. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Указать селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от нагрузки, которую нужно мониторить. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для пода. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме secure computing. | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Tolerations, которые нужно включить в DaemonSet OneAgent.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `version` | Версия OneAgent, которая будет использоваться. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для инъекции в поды. Если задан, переопределяет образ CodeModules, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (опционально) | string |
| `initResources` | Определить requests и limits ресурсов для initContainer. Подробности в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator.Подробнее в разделе [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (опционально) | LabelSelector |
| `useCSIDriver` | Задать, если нужно использовать CSIDriver. Не включать эту опцию, если нет доступа к узлам Kubernetes или недостаточно прав. | `false` | boolean |
| `version` | Версия OneAgent, которая будет использоваться. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent.Доступные опции описаны в разделе [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений приведён в разделе [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет значения по умолчанию (опционально) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из следующих релизов. [Закрепить версию OneAgent в тенанте для настройки автообновления](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent.Подробности в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (опционально) | []EnvVar |
| `image` | Использовать пользовательский образ Docker для OneAgent. При установке переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `labels` | Пользовательские метки для подов OneAgent для нужной структуризации рабочих нагрузок. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (опционально) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (опционально) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме secure computing. | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Tolerations для включения в DaemonSet OneAgent.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские аннотации ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какой функционал должен быть включён.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-6-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет на него все поды.- `dynatrace-api`[1](#fn-6-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавляет файл пользовательских свойств, передавая его как значение или через ссылку на секрет.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробности в разделе [How to add a custom properties file](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file"). | Нет значения по умолчанию (опционально) | string |
| `dnsPolicy` | Задаёт DNS policy для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (опционально) | []EnvVar |
| `group` | Задаёт activation group для ActiveGate. Подробности в разделе [Customize ActiveGate properties](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. При установке переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (опционально) | string |
| `labels` | Пользовательские метки для подов ActiveGate для нужной структуризации рабочих нагрузок. | Нет значения по умолчанию (опционально) | map[string]string |
| `nodeSelector` | Задаёт селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (опционально) | map[string]string |
| `priorityClassName` | Назначает класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробности в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционально) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки, значения нужно подбирать соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробности в разделе [How to add a custom certificate for ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Нет значения по умолчанию (опционально) | string |
| `tolerations` | Задаёт tolerations для подов ActiveGate.Подробности в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционально) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) для подов ActiveGate. | Нет значения по умолчанию (опционально) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробности в описании параметра `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры опциональны.

Дополнительная информация приведена в разделе [Configure enrichment directory](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.")

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `true`. | `true` | boolean |

Версия API DynaKube `v1beta1` больше недоступна начиная с версии Dynatrace Operator 1.6.0+.
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию Dynatrace Operator. Подробнее в разделе [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (опционально) | LabelSelector |

Версия Dynatrace Operator <=1.6.0

Уведомление об устаревании

Версия API DynaKube `v1beta1` больше недоступна начиная с версии Dynatrace Operator 1.7.0+.

## `.spec`

* Параметр `apiUrl` обязателен.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, включая путь `/api` в конце.- Для SaaS указать `YOUR_ENVIRONMENT_ID` в качестве ID окружения.- Для Managed изменить адрес `apiUrl`.Инструкции о том, как определить ID окружения и как настроить адрес apiUrl, см. в разделе [ID Environment](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти ID своего окружения и как настроить и подключить несколько окружений."). | Нет значения по умолчанию (обязателен) | string |
| `tokens` | Имя секрета, содержащего токены. | Имя пользовательского ресурса (`.metadata.name`), если не задано | string |
| `skipCertCheck` | Отключить проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установить значение `true`, если нужно пропустить проверки валидации сертификата. | `false` | boolean |
| `proxy` | Задать пользовательские настройки прокси напрямую либо из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgents. | Нет значения по умолчанию (необязателен) | string |
| `trustedCAs` | Добавляет пользовательские RootCA из configmap. Сертификат нужно поместить под `certs` внутри configmap.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязателен) | string |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязателен) | string |
| `customPullSecret` | Определяет пользовательский pull secret на случай, если для образов, заданных в DynaKube, используется приватный registry. Примечание: для [загрузки образа узла через ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая ephemeral volumes, загрузку образа через CSI driver и загрузку ZIP.") нужно убедиться, что pull secrets доступны в внедряемом поде. Подробности см. в разделе [предварительные условия](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#prerequisites "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая ephemeral volumes, загрузку образа через CSI driver и загрузку ZIP."). Чтобы задать пользовательский pull secret и узнать про ожидаемое поведение, см. раздел [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного registry"). | Нет значения по умолчанию (необязателен) | string |
| `enableIstio` | При включении, если в окружении Kubernetes установлен Istio, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster из OneAgent или ActiveGate. По умолчанию отключено. | `false` | boolean |
| `namespaceSelector` | Применимо только для типов конфигурации `applicationMonitoring` или `cloudNativeFullStack`. Пространства имён, в которые нужно выполнять внедрение через Dynatrace Operator. Подробнее см. в разделе [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов."). | Нет значения по умолчанию (необязателен) | LabelSelector |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Указать имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязателен) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `image` | Использовать пользовательский образ OneAgent Docker. Если задан, переопределяет образ, автоматически определяемый через [публичный registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного registry для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из вашего окружения Dynatrace."). | Образ из кластера Dynatrace. | string |
| `codeModulesImage` | Образ OneAgent, который используется для внедрения в поды. Если задан, переопределяет образ CodeModules, автоматически определяемый через [публичный registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного registry для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из вашего окружения Dynatrace."). | Нет значения по умолчанию (необязателен) | string |
| `version` | Версия OneAgent, которая используется для мониторинга хоста OneAgents, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |
| `tolerations` | Tolerations, которые нужно включить в DaemonSet OneAgent.Подробности см. в разделе [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязателен) | []Toleration |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязателен) | map[string]string |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробности см. в разделе [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязателен) | string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от нагрузки, которую нужно мониторить. Можно использовать настройки по умолчанию в [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные ограничения для пода. | Нет значения по умолчанию (необязателен) | ResourceRequirements |
| `autoUpdate` (**устарело**) | Устаревшее поле, которое будет удалено в одном из будущих релизов. [Закрепите версию OneAgent на своём тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для всех компонентов, управляемых Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробности см. в разделе [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязателен) | map[string]string |
| `labels` | Определённые вами метки для подов OneAgent, чтобы структурировать нагрузки нужным образом. | Нет значения по умолчанию (необязателен) | map[string]string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязателен) | []EnvVar |
| `args` | Задать дополнительные аргументы для инсталлятора OneAgent.Доступные варианты см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязателен) | []string |
| `initResources` | Задать запросы и ограничения ресурсов для initContainer. Подробности см. в разделе [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязателен) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять внедрение через Dynatrace Operator. Подробнее см. в разделе [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов."). | Нет значения по умолчанию (необязателен) | LabelSelector |

## `.spec.oneAgent.classicFullStack`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `image` | Использовать кастомный образ Docker OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (опционально) | []Toleration |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из будущих релизов. [Закрепить версию OneAgent на тенанте для настройки автообновления](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавить кастомные аннотации OneAgent. | Значения по умолчанию нет (опционально) | map[string]string |
| `labels` | Определённые пользователем метки для подов OneAgent для структурирования workload по своему усмотрению. | Значения по умолчанию нет (опционально) | map[string]string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Значения по умолчанию нет (опционально) | []EnvVar |
| `args` | Задать дополнительные аргументы для инсталлятора OneAgent.Доступные опции см. в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Значения по умолчанию нет (опционально) | []string |
| `nodeSelector` | Указать node selector, определяющий, на каких нодах будет развёрнут OneAgent. | Значения по умолчанию нет (опционально) | map[string]string |
| `priorityClassName` | Назначить приоритетный класс подам OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Значения по умолчанию нет (опционально) | string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемого workload. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Значения по умолчанию нет (опционально) | ResourceRequirements |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для инъекции в поды. При задании переопределяет образ CodeModules, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Значения по умолчанию нет (опционально) | string |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `useCSIDriver` | Указать, если нужно использовать CSI driver. Не включать, если нет доступа к нодам Kubernetes или недостаточно привилегий. | `false` | boolean |
| `initResources` | Определить запросы и лимиты ресурсов для initContainer. Подробности см. в [Managing resources for containers﻿](https://dt-url.net/atc371q). | Значения по умолчанию нет (опционально) | ResourceRequirements |
| `hostGroup` | Указать имя группы, к которой нужно отнести хост. Этот способ предпочтительнее, чем ныне устаревший аргумент `--set-host-group`. Если используются оба варианта, это поле имеет приоритет над аргументом `--set-host-group`. | Значения по умолчанию нет (опционально) | string |
| `namespaceSelector` | Namespace, в которые Operator Dynatrace должен производить инъекцию. Подробнее см. в [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Значения по умолчанию нет (опционально) | LabelSelector |

## `.spec.oneAgent.hostMonitoring`

* Все параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `image` | Использовать кастомный образ Docker OneAgent. При задании переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `nodeSelector` | Указать node selector, определяющий, на каких нодах будет развёрнут OneAgent. | Значения по умолчанию нет (опционально) | map[string]string |
| `priorityClassName` | Назначить приоритетный класс подам OneAgent. По умолчанию класс не задан.Подробности см. в [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Значения по умолчанию нет (опционально) | string |
| `tolerations` | Tolerations, включаемые в DaemonSet OneAgent.Подробности см. в [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (опционально) | []Toleration |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемого workload. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Значения по умолчанию нет (опционально) | ResourceRequirements |
| `autoUpdate` (**устарело**) | Устаревшее поле, будет удалено в одном из будущих релизов. [Закрепить версию OneAgent на тенанте для настройки автообновления](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробности см. в [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавить кастомные аннотации OneAgent. | Значения по умолчанию нет (опционально) | map[string]string |
| `labels` | Определённые пользователем метки для подов OneAgent для структурирования workload по своему усмотрению. | Значения по умолчанию нет (опционально) | map[string]string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Значения по умолчанию нет (опционально) | []EnvVar |
| `args` | Задать дополнительные аргументы для инсталлятора OneAgent.Доступные опции см. в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Значения по умолчанию нет (опционально) | []string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры опциональны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `capabilities` | Определяет возможности ActiveGate pod: какой функционал должен быть включён.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-7-1-def) открывает endpoint приёма метрик на ActiveGate DynaKube и перенаправляет на него все pod'ы.- `dynatrace-api`[1](#fn-7-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") в ActiveGate. | Нет значения по умолчанию (обязателен) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. При установке переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (опционален) | string |
| `replicas` | Количество реплик pod'ов ActiveGate. | 1 | int |
| `tolerations` | Задать tolerations для pod'ов ActiveGate.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (опционален) | []Toleration |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (опционален) | map[string]string |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой нагрузки, значения нужно корректировать соответствующим образом. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `labels` | Заданные пользователем метки для pod'ов ActiveGate для структурирования нагрузок нужным образом. | Нет значения по умолчанию (опционален) | map[string]string |
| `env` | Задать дополнительные переменные окружения для pod'ов ActiveGate. | Нет значения по умолчанию (опционален) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements."). | Нет значения по умолчанию (рекомендуется) | string |
| `customProperties` | Добавить файл пользовательских свойств, указав его как значение или сославшись на него из secret.При ссылке на файл пользовательских свойств из secret ключ должен называться `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file"). | Нет значения по умолчанию (опционален) | string |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Нет значения по умолчанию (опционален) | string |
| `dnsPolicy` | Задать DNS-политику для pod'ов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `priorityClassName` | Назначить класс приоритета pod'ам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (опционален) | string |
| `annotations` | Добавить пользовательские аннотации ActiveGate. | Нет значения по умолчанию (опционален) | map[string]string |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к pod'ам ActiveGate. | Нет значения по умолчанию (опционален) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.