---
title: Параметры DynaKube для Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters
---

# Параметры DynaKube для Dynatrace Operator

# Параметры DynaKube для Dynatrace Operator

* Чтение: 57 мин
* Обновлено 10 июля 2026 г.

Эта страница поможет разобраться в настройке [Kubernetes Custom Resource﻿](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) DynaKube и оптимизировать установку Dynatrace Operator под конкретные требования.

В таблице ниже указаны требуемые версии Dynatrace Operator, соответствующие каждой версии API DynaKube.

| Версия API DynaKube | Минимальная версия Dynatrace Operator | Максимальная версия Dynatrace Operator [1](#fn-1-1-def) |
| --- | --- | --- |
| `v1beta6` | 1.8 |  |
| `v1beta5` | 1.6 |  |
| `v1beta4` | 1.5 |  |
| `v1beta3` | 1.4 | 1.7 |
| `v1beta2` | 1.2 | 1.6 |
| `v1beta1` | Все версии | 1.6 |

1

Соответствующие версии API DynaKube будут удалены из Dynatrace Operator в следующем минорном или мажорном релизе.

Примеры YAML DynaKube см. на [GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.10.1/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Dynatrace Operator версии 1.8.0+

## `.spec`

* Параметр `apiUrl` является обязательным и неизменяемым. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS: установите `YOUR_ENVIRONMENT_ID` равным идентификатору среды.- Для Managed: измените адрес `apiUrl`.Инструкции по определению идентификатора среды и настройке адреса apiUrl см. в разделе [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор среды и как настроить несколько сред.") | Нет (обязательный) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет для приватного реестра. Выполняет аутентификацию только для компонентов, управляемых оператором, в пространстве имён `dynatrace`, и не распространяется на инжектируемые поды приложений. Подробнее: [Create a pull secret](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра") и [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Использование приватного реестра"). | Нет (необязательный) | string |
| `dynatraceApiRequestThreshold` | Минимальный интервал в минутах между запросами API Dynatrace. | 15 | integer |
| `enableIstio` | При включении, если Istio установлен в среде Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry для обеспечения доступа к кластеру Dynatrace из OneAgent или ActiveGate. По умолчанию отключено. | Нет (необязательный) | boolean |
| `networkZone` | Задаёт сетевую зону для подов OneAgent и ActiveGate. | Нет (необязательный) | string |
| `proxy` | Настройка пользовательского прокси: напрямую или через секрет с полем `proxy`. Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет (необязательный) | DynaKubeProxy |
| `publicRegistryOverride` | Переопределяет хост публичного реестра по умолчанию, используемый для получения образов компонентов мониторинга. Dynatrace Operator передаёт указанный хост реестра в среду Dynatrace. Допустимые значения: `public.ecr.aws` (Amazon ECR Public) или `registry-1.docker.io` (Docker Hub). Подробнее: [Resolve public registry images automatically](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator для использования образов публичного реестра. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace."). | Нет (необязательный) | string |
| `resourceAttributes` | Атрибуты ресурса, которые Dynatrace Operator применяет ко всем сигналам телеметрии. Доступно начиная с Dynatrace Operator версии 1.10.0. | Нет (необязательный) | map[string]string |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и кластером Dynatrace. Установите в `true`, чтобы пропустить проверку сертификата. | Нет (необязательный) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет (необязательный) | string |
| `trustedCAs` | Добавляет пользовательские корневые сертификаты (RootCAs) из configmap. Ключ данных должен быть `certs`. Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет (необязательный) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, в которую нужно включить хост. Этот метод предпочтительнее устаревшего аргумента `--set-host-group`. Если используются оба параметра, это поле имеет приоритет над аргументом `--set-host-group`. | Нет (необязательный) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры являются необязательными.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `additionalResourceAttributes` | Дополнительные атрибуты ресурса для телеметрии OneAgent, объединяются с `.spec.resourceAttributes`. Доступно начиная с Dynatrace Operator 1.10.0. | Нет (необязательный) | map[string]string |
| `annotations` | Добавляет пользовательские аннотации для подов OneAgent. | Нет (необязательный) | map[string]string |
| `args` | Задаёт дополнительные аргументы для установщика OneAgent. Доступные параметры: [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки."). Список ограничений: [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет (необязательный) | []string |
| `codeModulesImage` | Ссылка на образ контейнера для code modules. Следует избегать изменяемых тегов, например `latest`, и использовать digest или неизменяемый тег для воспроизводимых развёртываний. | Нет (необязательный) | string |
| `codeModulesImagePullPolicy` | Определяет политику извлечения образа для CodeModules. При пустом значении применяется политика Kubernetes по умолчанию. | Нет (необязательный) | string |
| `dnsPolicy` | Задаёт политику DNS для подов OneAgent. Подробнее: [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные среды для подов OneAgent. | Нет (необязательный) | []EnvVar |
| `image` | Использует пользовательский образ Docker для OneAgent. При указании переопределяет образ, автоматически разрешаемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator для использования образов публичного реестра. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace."). | Образ из кластера Dynatrace. | string |
| `imagePullPolicy` | Определяет политику извлечения образа. При пустом значении применяется политика Kubernetes по умолчанию. | Нет (необязательный) | string |
| `initResources` | Определяет запросы ресурсов и лимиты для initContainer. Подробнее: [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет (необязательный) | ResourceRequirements |
| `labels` | Пользовательские метки для подов OneAgent для структурирования рабочих нагрузок. | Нет (необязательный) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инжекцию. Подробнее: [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет (необязательный) | LabelSelector |
| `nodeSelector` | Задаёт node selector, управляющий тем, на каких узлах будет развёрнут OneAgent. | Нет (необязательный) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление ресурсов OneAgent существенно зависит от отслеживаемой нагрузки. Можно использовать значения по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples). `resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет (необязательный) | ResourceRequirements |
| `priorityClassName` | Назначает класс приоритета подам OneAgent. По умолчанию класс не задан. Подробнее: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет (необязательный) | string |
| `rollingUpdate` | Определяет параметры rollingUpdate для UpdateStrategy DaemonSet OneAgent. Подробнее: [DaemonSet specification﻿](https://dt-url.net/v0038c5). | Нет (необязательный) | RollingUpdateDaemonSet |
| `secCompProfile` | Профиль SecComp, настраиваемый для запуска в режиме защищённых вычислений. | Нет (необязательный) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где хранятся конфигурации OneAgent. | Нет (необязательный) | string |
| `tolerations` | Tolerations для DaemonSet OneAgent. Подробнее: [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет (необязательный) | []Toleration |
| `version` | Версия OneAgent для хостового мониторинга OneAgent в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

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
* Параметры `resources` и `group` рекомендованы.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские ActiveGate аннотации. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет capabilities подов ActiveGate: какую функциональность нужно включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-2-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет к нему все поды.- `dynatrace-api`[1](#fn-2-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавить файл пользовательских свойств, передав его как значение или указав ссылку на него из secret.При ссылке на файл пользовательских свойств из secret нужно убедиться, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Добавить файл пользовательских свойств к ActiveGate, запущенному в Kubernetes, для определения настроек конфигурации при настройке мониторинга кластера."). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задать DNS policy для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задать activation group для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задано, переопределяет образ, автоматически разрешаемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настроить Dynatrace Operator на использование образов из public registry для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace."). | Нет значения по умолчанию (необязательно) | string |
| `imagePullPolicy` | Определяет image pull policy. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Пользовательские labels для подов ActiveGate для структурирования рабочих нагрузок по желанию. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначить priority class подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `rollingUpdate` | Определить настройки rollingUpdate для UpdateStrategy StatefulSet ActiveGate. Подробнее см. [StatefulSet Specification﻿](https://dt-url.net/ql238m1).  UpdateStrategy для StatefulSet требует Kubernetes 1.35 и выше. На более ранних версиях настройка игнорируется, а Operator предупреждает об игнорируемых настройках, если они были указаны. | Нет значения по умолчанию (необязательно) | RollingUpdateStatefulSetStrategy |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ресурсов ActiveGate сильно зависит от отслеживаемой нагрузки; скорректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | Нет значения по умолчанию (необязательно) | int |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в средах с ограниченным сетевым доступом, сетевые настройки и конфигурации прокси."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задать tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли ephemeral volume для хранилища. | Нет значения по умолчанию (необязательно) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и предоставляет Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaimSpec |

1

Для этой capability требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `initResources` | Определить resource requests и limits для init-контейнера, используемого для автономного обогащения метаданными. Учитывается только при отсутствии инжектируемого OneAgent. Подробнее см. [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые нужно выполнить инжект Dynatrace Operator. Подробнее см. [Настройка мониторинга для namespaces и Pod'ов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для namespaces и pod'ов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `prometheus` | Включает расширение prometheus. | Нет значения по умолчанию (необязательно) |  |
| `databases` | Список расширений баз данных. | Нет значения по умолчанию (необязательно) | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список capabilities ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.extensions.databases`

Доступно в будущей версии Dynatrace.

* Все параметры, кроме `id`, необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `id` | Уникальное имя объекта Kubernetes. | Нет значения по умолчанию (обязательно) | string |
| `replicas` | Количество реплик SQL Extension Executor. | 1 | int32 |
| `volumes` | Volumes для файловой аутентификации. | Нет значения по умолчанию (необязательно) | []Volume |
| `volumeMounts` | Volume mounts для файловой аутентификации. | Нет значения по умолчанию (необязательно) | []VolumeMount |
| `serviceAccountName` | ServiceAccount для аутентификации на основе IAM. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Labels SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Label |
| `annotations` | Annotations SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Annotation |
| `affinity` | Affinities SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Affinity |
| `resources` | Ресурсы SQL Extension Executor. | Нет значения по умолчанию (необязательно) | ResourcesSpec |
| `nodeSelector` | Node selector SQL Extension Executor. | Нет значения по умолчанию (необязательно) | NodeSelectorSpec |
| `topologySpreadConstraints` | Topology spread constraints SQL Extension Executor. | Нет значения по умолчанию (необязательно) | TopologySpreadConstraints |

На OpenShift использование volumes типа `hostPath` запрещено стандартным SCC и приведёт к сбоям. Если `hostPath` необходим, нужно создать role с достаточными привилегиями и привязать её к соответствующему service account. В этом примере созданная role привязывается к service account с именем `custom-sql-extension-executor-sa`:

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

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские OneAgent аннотации. | По умолчанию не задано (необязательно) | map[string]string |
| `args` | Задать дополнительные аргументы установщику OneAgent.Доступные параметры описаны в разделе [Пользовательская установка Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Описание использования Linux-установщика с параметрами командной строки.").Список ограничений: [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent в виде контейнера Docker."). | По умолчанию не задано (необязательно) | []string |
| `autoUpdate` (**deprecated**) | Устаревшее поле, которое будет удалено в будущем релизе. [Закрепите версию OneAgent в тенанте для настройки авто-обновления](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка авто-обновления для всех компонентов, управляемых Dynatrace Operator").Авто-обновление отключается при установке полей `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробнее: [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | По умолчанию не задано (необязательно) | []EnvVar |
| `image` | Использовать пользовательский образ OneAgent Docker. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator для использования образов из публичного реестра для себя и управляемых компонентов. Можно настроить вручную или через автоматическое определение из вашей среды Dynatrace."). | Образ из кластера Dynatrace. | string |
| `labels` | Пользовательские метки для подов OneAgent, позволяющие структурировать нагрузки. | По умолчанию не задано (необязательно) | map[string]string |
| `nodeSelector` | Указать node selector, управляющий тем, на каких узлах будет развёрнут OneAgent. | По умолчанию не задано (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent существенно зависит от контролируемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты пода. | По умолчанию не задано (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначить класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | По умолчанию не задано (необязательно) | string |
| `secCompProfile` | SecComp Profile, настраиваемый для запуска в режиме безопасных вычислений. | По умолчанию не задано (необязательно) | string |
| `storageHostPath` | Директория с правом записи в файловой системе хоста, где будут храниться конфигурации OneAgent. | По умолчанию не задано (необязательно) | string |
| `tolerations` | Tolerations для DaemonSet OneAgent.Подробнее: [Taints and Tolerations﻿](https://dt-url.net/od03765). | По умолчанию не задано (необязательно) | []Toleration |
| `version` | Версия OneAgent для использования. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские ActiveGate аннотации. | По умолчанию не задано (необязательно) | map[string]string |
| `capabilities` | Определяет возможности подов ActiveGate: какую функциональность нужно включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-3-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет все поды к нему.- `dynatrace-api`[1](#fn-3-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей.") в ActiveGate. | По умолчанию не задано (обязательно) | string |
| `customProperties` | Добавить файл пользовательских свойств, указав его значение напрямую или сославшись на секрет.При ссылке на файл пользовательских свойств из секрета ключ должен называться `customProperties`. Подробнее: [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Добавление файла пользовательских свойств к ActiveGate, работающему в Kubernetes, для настройки параметров мониторинга кластера."). | По умолчанию не задано (необязательно) | string |
| `dnsPolicy` | Задать DNS policy для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов ActiveGate. | По умолчанию не задано (необязательно) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробнее: [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей."). | По умолчанию не задано (рекомендуется) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator для использования образов из публичного реестра для себя и управляемых компонентов. Можно настроить вручную или через автоматическое определение из вашей среды Dynatrace."). | По умолчанию не задано (необязательно) | string |
| `labels` | Пользовательские метки для подов ActiveGate, позволяющие структурировать нагрузки. | По умолчанию не задано (необязательно) | map[string]string |
| `nodeSelector` | Указать node selector, управляющий тем, на каких узлах будет развёрнут ActiveGate. | По умолчанию не задано (необязательно) | map[string]string |
| `priorityClassName` | Назначить класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | По умолчанию не задано (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate существенно зависит от контролируемой нагрузки; значения нужно скорректировать соответственно. | По умолчанию не задано (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | По умолчанию не задано (необязательно) | int |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее: [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в сетях с ограниченным доступом, сетевые параметры и конфигурации прокси."). | По умолчанию не задано (необязательно) | string |
| `tolerations` | Задать tolerations для подов ActiveGate.Подробнее: [Taints and Tolerations﻿](https://dt-url.net/od03765). | По умолчанию не задано (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | По умолчанию не задано (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | По умолчанию не задано (необязательно) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и предоставляет Source для атрибутов, специфичных для провайдера. | По умолчанию не задано (необязательно) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее: параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инъекцию с помощью Dynatrace Operator. Подробнее: [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | По умолчанию не задано (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator версии 1.9.0+

Когда для пространства имён настроена инъекция OneAgent, обогащение метаданными неявно включается для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Для использования расширений

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

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

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет (необязателен) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Labels, применяемые к поду Dynatrace Collector. | Нет (необязателен) | map[string]string |
| `annotations` | Annotations, применяемые к поду Dynatrace Collector. | Нет (необязателен) | map[string]string |
| `tlsRefName` | Secret с TLS-сертификатом, используемым Dynatrace Collector для проверки подключений к эндпоинтам других компонентов. | Нет (необязателен) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет (необязателен) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет (необязателен) | []Toleration |
| `topologySpreadConstraints` | Ограничения распределения топологии для пода Dynatrace Collector. | Нет (необязателен) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator версии 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator версии 1.5.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным идентификатору своего окружения.- Для Managed измените адрес `apiUrl`. Инструкции по определению идентификатора окружения и настройке адреса apiUrl см. в [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") | Нет (обязателен) | string |
| `customPullSecret` | Задаёт пользовательский pull secret, если для образов, определённых в DynaKube, используется приватный реестр. Примечание: при [node image pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") нужно убедиться, что pull secrets доступны на инжектируемом поде. Подробнее см. [prerequisites](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#prerequisites "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). Чтобы задать пользовательский pull secret и узнать об ожидаемом поведении, см. [Configure `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | Нет (необязателен) | string |
| `dynatraceApiRequestThreshold` | Минимальный интервал в минутах между запросами Dynatrace API. | 15 | integer |
| `enableIstio` | При включении, если в окружении Kubernetes установлен Istio, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, открывающие доступ к кластеру Dynatrace из OneAgent или ActiveGate. Отключено по умолчанию. | Нет (необязателен) | boolean |
| `networkZone` | Задаёт сетевую зону для подов OneAgent и ActiveGate. | Нет (необязателен) | string |
| `proxy` | Задаёт пользовательские настройки прокси напрямую или из secret с полем `proxy`. Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет (необязателен) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для подключения между Dynatrace Operator и кластером Dynatrace. Установите `true`, чтобы пропустить проверку сертификата. | Нет (необязателен) | boolean |
| `tokens` | Имя secret, содержащего токены для подключения к Dynatrace. | Нет (необязателен) | string |
| `trustedCAs` | Добавляет пользовательские корневые CA из configmap. Ключ данных должен быть `certs`. Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет (необязателен) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Указывает имя группы, к которой нужно привязать хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются оба параметра, данное поле имеет приоритет над аргументом `--set-host-group`. | Нет (необязателен) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавляет пользовательские annotations для OneAgent. | Нет (необязателен) | map[string]string |
| `args` | Задаёт дополнительные аргументы установщику OneAgent. Доступные параметры см. в [Linux custom installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). Список ограничений см. в [Limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Нет (необязателен) | []string |
| `autoUpdate` (**deprecated**) | Устаревшее поле, которое будет удалено в одном из будущих релизов. [Pin the OneAgent version on your tenant to configure auto-update](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for all components managed by Dynatrace Operator"). Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Ссылка на образ контейнера с code modules. Избегайте изменяемых тегов вроде `latest`: используйте digest или неизменяемый тег для воспроизводимых развёртываний. | Нет (необязателен) | string |
| `dnsPolicy` | Задаёт DNS Policy для подов OneAgent. Подробнее см. [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задаёт дополнительные переменные окружения для подов OneAgent. | Нет (необязателен) | []EnvVar |
| `image` | Использует пользовательский образ OneAgent Docker. Если задано, переопределяет образ, автоматически определяемый через [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Образ из кластера Dynatrace. | string |
| `initResources` | Задаёт запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers﻿](https://dt-url.net/atc371q). | Нет (необязателен) | ResourceRequirements |
| `labels` | Пользовательские labels для подов OneAgent, позволяющие структурировать нагрузки по своему усмотрению. | Нет (необязателен) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инжекцию. Подробнее см. [Configure monitoring for namespaces and Pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет (необязателен) | LabelSelector |
| `nodeSelector` | Указывает node selector, определяющий узлы, на которых будет развёрнут OneAgent. | Нет (необязателен) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление ресурсов OneAgent существенно зависит от отслеживаемой нагрузки. Значения по умолчанию можно взять из примеров DynaKube на [GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.10.1/assets/samples/dynakube). `resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет (необязателен) | ResourceRequirements |
| `priorityClassName` | Назначает priority class подам OneAgent. По умолчанию класс не задан. Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет (необязателен) | string |
| `secCompProfile` | SecComp Profile, настраиваемый для работы в режиме безопасных вычислений. | Нет (необязателен) | string |
| `storageHostPath` | Доступный для записи каталог на файловой системе хоста, в котором будут храниться конфигурации OneAgent. | Нет (необязателен) | string |
| `tolerations` | Tolerations для DaemonSet OneAgent. Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет (необязателен) | []Toleration |
| `version` | Версия OneAgent, используемая для хостового мониторинга OneAgent, запущенных в выделенном поде. Этот параметр не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

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

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности подов ActiveGate: какой функциональности нужно быть включённой.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-4-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет на него все поды.- `dynatrace-api`[1](#fn-4-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавить файл пользовательских свойств, указав его как значение или сославшись на него из secret'а.При ссылке на файл пользовательских свойств из secret'а убедитесь, что ключ назван `customProperties`. Подробности: [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Add a custom properties file to ActiveGate running in Kubernetes to define configuration settings for your cluster monitoring setup."). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задать политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробности: [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задан, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). | Нет значения по умолчанию (необязательно) | string |
| `labels` | Пользовательские метки для подов ActiveGate для организации нагрузок по своему усмотрению. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Указать селектор узлов, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначить класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробности: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ресурсов ActiveGate сильно зависит от контролируемой нагрузки; значения нужно подбирать соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения и правила Kubernetes по умолчанию. | Нет значения по умолчанию (необязательно) | int |
| `tlsSecretName` | Имя secret'а, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробности: [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задать tolerations для подов ActiveGate.Подробности: [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранилища. | Нет значения по умолчанию (необязательно) | boolean |
| `persistentVolumeClaim` | Описывает общие атрибуты устройств хранилища и предоставляет Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробности: параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые нужно инжектировать Dynatrace Operator. Подробности: [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Нет значения по умолчанию (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator версии 1.9.0+

Когда для пространства имён настроена инжекция OneAgent, обогащение метаданными неявно включается для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Для использования расширений

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). Для использования KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно в версии Dynatrace 1.306 и OneAgent 1.305

Log Monitoring требует, чтобы была включена [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия для сопоставления атрибутов приёма. | Нет значения по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма. | Нет значения по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы применялось правило приёма. | Нет значения по умолчанию (необязательно) | []string |

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

Добавление этого раздела разворачивает Dynatrace Collector через Operator.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Задаёт протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Задаёт имя используемого сервиса. Если не указано, serviceName устанавливается по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret, содержащий TLS-сертификат, используемый telemetryIngest. | Нет значения по умолчанию (необязательно) | string |

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
* Параметры `resources` и `group` рекомендованы.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские ActiveGate аннотации. | Нет по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какие функции должны быть включены. Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-5-1-def) открывает эндпоинт приёма метрик на DynaKube ActiveGate и перенаправляет все поды к нему.- `dynatrace-api`[1](#fn-5-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.") в ActiveGate. | Нет по умолчанию (обязательно) | string |
| `customProperties` | Добавить файл пользовательских свойств, указав его как значение или сославшись на него из секрета. При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее: [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Добавьте файл пользовательских свойств в ActiveGate, работающий в Kubernetes, чтобы задать параметры конфигурации для настройки мониторинга кластера."). | Нет по умолчанию (необязательно) | string |
| `dnsPolicy` | Задать DNS-политику для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов ActiveGate. | Нет по умолчанию (необязательно) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробнее: [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями."). | Нет по умолчанию (рекомендуется) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задано, переопределяет образ, автоматически разрешённый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator для использования образов публичного реестра для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое разрешение из вашей среды Dynatrace."). | Нет по умолчанию (необязательно) | string |
| `labels` | Пользовательские метки для подов ActiveGate, позволяющие структурировать рабочие нагрузки по своему усмотрению. | Нет по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Указать селектор узлов, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначить класс приоритета подам ActiveGate. По умолчанию класс не задан. Подробнее: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ресурсов ActiveGate во многом зависит от мониторируемой нагрузки; значения нужно корректировать соответственно. | Нет по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее: [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройте Dynatrace в средах с ограниченным сетевым доступом, сетевые параметры и конфигурации прокси."). | Нет по умолчанию (необязательно) | string |
| `tolerations` | Задать tolerations для подов ActiveGate. Подробнее: [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет по умолчанию (необязательно) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробнее: параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые нужно выполнять инжекцию Dynatrace Operator. Подробнее: [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет по умолчанию (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator версии 1.9.0+

Если для пространства имён настроена инжекция OneAgent, обогащение метаданными включается неявно для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Чтобы использовать расширения:

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`; и
* флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Чтобы использовать KSPM:

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`; и
* флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно в Dynatrace версии 1.306 и OneAgent 1.305

Log Monitoring требует включения [возможности ActiveGate](#active-gate) `kubernetes-monitoring`, но её не нужно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Задаёт правила и условия сопоставления атрибутов приёма данных. | Нет по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Задаёт имя атрибута для сопоставления правил приёма данных. | Нет по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма данных применялось. | Нет по умолчанию (необязательно) | []string |

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
| `updateStrategy` | Определить стратегию обновления daemonSet для Node Configuration Collector. | Нет по умолчанию (необязательно) | DaemonSetUpdateStrategy |
| `labels` | Добавить пользовательские метки к подам Node Configuration Collector. | Нет по умолчанию (необязательно) | map[string]string |
| `annotations` | Добавить пользовательские аннотации к подам Node Configuration Collector. | Нет по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Указать селектор узлов, определяющий, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет по умолчанию (необязательно) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если задано, указывает приоритет пода. Имя должно быть определено путём создания объекта PriorityClass с этим именем. Если не задано, настройка удаляется из DaemonSet. | Нет по умолчанию (необязательно) | string |
| `resources` | Определить запросы ресурсов и лимиты для подов Node Configuration Collector. | Нет по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определить nodeAffinity для DaemonSet Node Configuration Collector. | Нет по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задать tolerations для подов Node Configuration Collector. Подробнее: [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет по умолчанию (необязательно) | []Toleration |
| `args` | Задать дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет по умолчанию (необязательно) | []string |
| `env` | Задать дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет по умолчанию (необязательно) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| repository | URL образа Node Configuration Collector. | Нет по умолчанию (необязательно) | string |
| tag | Тег образа Node Configuration Collector. | Нет по умолчанию (необязательно) | string |

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

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательный) | map[string]string |
| `args` | Задать дополнительные аргументы для установщика OneAgent.Доступные параметры описаны в разделе [Кастомная установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").Список ограничений приведён в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательный) | []string |
| `autoUpdate` (**устарело**) | Устаревшее поле, которое будет удалено в будущей версии. [Закрепите версию OneAgent на тенанте для настройки автообновления](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройте автообновления для всех компонентов, управляемых Dynatrace Operator").Автообновление отключается, если заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задать DNS Policy для подов OneAgent.Подробнее см. [Pods DNS Policy﻿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательный) | []EnvVar |
| `image` | Использовать кастомный образ OneAgent Docker. Если задано, переопределяет образ, автоматически определённый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного реестра для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Образ из кластера Dynatrace. | string |
| `labels` | Пользовательские метки для подов OneAgent для структурирования рабочих нагрузок по необходимости. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательный) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой нагрузки. Можно использовать настройки по умолчанию из [CR﻿](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для работы; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательный) | ResourceRequirements |
| `priorityClassName` | Назначить priority class для подов OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательный) | string |
| `secCompProfile` | SecComp Profile, который будет настроен для работы в режиме безопасных вычислений. | Нет значения по умолчанию (необязательный) | string |
| `tolerations` | Tolerations для DaemonSet OneAgent.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `version` | Версия OneAgent для использования. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавить пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательный) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность нужно включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-6-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет все поды к нему.- `dynatrace-api`[1](#fn-6-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [Live Debugging module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательный) | string |
| `customProperties` | Добавить файл пользовательских свойств, передав его как значение или указав ссылку на secret.При ссылке на файл пользовательских свойств из secret убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Добавьте файл пользовательских свойств в ActiveGate, запущенный в Kubernetes, для определения параметров конфигурации настройки мониторинга кластера."). | Нет значения по умолчанию (необязательный) | string |
| `dnsPolicy` | Задать DNS policy для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задать дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательный) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Использовать кастомный образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задано, переопределяет образ, автоматически определённый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного реестра для себя и управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Нет значения по умолчанию (необязательный) | string |
| `labels` | Пользовательские метки для подов ActiveGate для структурирования рабочих нагрузок по необходимости. | Нет значения по умолчанию (необязательный) | map[string]string |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательный) | map[string]string |
| `priorityClassName` | Назначить priority class для подов ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательный) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой нагрузки; при необходимости скорректируйте значения. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат ActiveGate, ключ и пароль. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить кастомный сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройте Dynatrace в сетях с ограниченным доступом, сетевые параметры и конфигурации прокси."). | Нет значения по умолчанию (необязательный) | string |
| `tolerations` | Задать tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations﻿](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательный) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательный) | []TopologySpreadConstraint |

1

Для этой возможности требуется кастомный сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

Дополнительные сведения приведены в разделе [Настройка каталога обогащения](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Настройте обогащение метаданными в Dynatrace Operator для добавления метаданных Kubernetes к сигналам телеметрии с помощью OneAgent, OTLP exporter или автономного обогащения.")

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `true`. | `true` | boolean |

DynaKube API версия `v1beta1` недоступна начиная с версии Dynatrace Operator 1.6.0+.
| `namespaceSelector` | Пространства имён, в которые нужно внедрять Dynatrace Operator. Подробнее см. [Настройка мониторинга пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга пространств имён и подов"). | Нет значения по умолчанию (необязательный) | LabelSelector |

Dynatrace Operator версии <=1.6.0

Уведомление об устаревании

DynaKube API версия `v1beta1` недоступна начиная с версии Dynatrace Operator 1.7.0+.

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

* Параметр `capabilities` является обязательным.
* Параметры `resources` и `group` являются рекомендуемыми.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `capabilities` | Определяет возможности pod ActiveGate: какая функциональность должна быть включена.Возможные значения:- `routing` включает OneAgent routing.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-7-1-def) открывает endpoint приёма метрик на DynaKube ActiveGate и перенаправляет все pod к нему.- `dynatrace-api`[1](#fn-7-1-def) включает вызов Dynatrace API через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований.") в ActiveGate. | Значения по умолчанию нет (обязательный) | string |
| `image` | Использовать пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. Если задано, переопределяет образ, автоматически определяемый через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройте Dynatrace Operator на использование образов из публичного реестра для себя и своих управляемых компонентов. Это можно сделать вручную или через автоматическое определение из среды Dynatrace."). | Значения по умолчанию нет (необязательный) | string |
| `replicas` | Количество реплик pod ActiveGate. | 1 | int |
| `tolerations` | Задать tolerations для pod ActiveGate. Подробности: [Taints and Tolerations﻿](https://dt-url.net/od03765). | Значения по умолчанию нет (необязательный) | []Toleration |
| `nodeSelector` | Указать node selector, определяющий, на каких узлах будет развёрнут ActiveGate. | Значения по умолчанию нет (необязательный) | map[string]string |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой нагрузки; значения нужно корректировать соответственно. | Значения по умолчанию нет (рекомендуемый) | ResourceRequirements |
| `labels` | Пользовательские labels для pod ActiveGate, позволяющие структурировать рабочие нагрузки по необходимости. | Значения по умолчанию нет (необязательный) | map[string]string |
| `env` | Задать дополнительные переменные окружения для pod ActiveGate. | Значения по умолчанию нет (необязательный) | []EnvVar |
| `group` | Задать группу активации для ActiveGate. Подробности: [Customize ActiveGate properties](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований."). | Значения по умолчанию нет (рекомендуемый) | string |
| `customProperties` | Добавить файл пользовательских свойств, указав его как значение или сославшись на secret. При ссылке на файл пользовательских свойств из secret убедиться, что ключ называется `customProperties`. Подробности: [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file "Добавьте файл пользовательских свойств в ActiveGate, запущенный в Kubernetes, для определения параметров конфигурации мониторинга кластера."). | Значения по умолчанию нет (необязательный) | string |
| `tlsSecretName` | Имя secret, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробности: [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройте Dynatrace в сетях с ограниченным доступом, сетевые параметры и конфигурации прокси."). | Значения по умолчанию нет (необязательный) | string |
| `dnsPolicy` | Задать DNS-политику для pod ActiveGate. | `ClusterFirstWithHostNet` | string |
| `priorityClassName` | Назначить приоритетный класс pod ActiveGate. По умолчанию класс не задан. Подробности: [Pod Priority and Preemption﻿](https://dt-url.net/n8437bl). | Значения по умолчанию нет (необязательный) | string |
| `annotations` | Добавить пользовательские annotations для ActiveGate. | Значения по умолчанию нет (необязательный) | map[string]string |
| `topologySpreadConstraints` | Добавляет [topology spread constraints﻿](https://dt-url.net/xc03ysw) к pod ActiveGate. | Значения по умолчанию нет (необязательный) | []TopologySpreadConstraint |

1

Для данной возможности требуется пользовательский сертификат. Подробности: параметр `tlsSecretName`.