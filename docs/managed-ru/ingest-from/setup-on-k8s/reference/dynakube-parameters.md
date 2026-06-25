---
title: Параметры DynaKube для Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters
scraped: 2026-05-12T11:22:33.891596
---

# Параметры DynaKube для Dynatrace Operator

# Параметры DynaKube для Dynatrace Operator

* Чтение: 57 мин
* Обновлено 16 марта 2026 г.

Эта страница поможет понять и настроить DynaKube [Kubernetes Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), что позволит оптимизировать настройку Dynatrace Operator в соответствии с вашими конкретными требованиями.

В таблице ниже указаны необходимые версии Dynatrace Operator, соответствующие каждой версии API DynaKube.

| Версия API DynaKube | Минимальная версия Dynatrace Operator | Максимальная версия Dynatrace Operator [1](#fn-1-1-def) |
| --- | --- | --- |
| `v1beta6` | 1.8 |  |
| `v1beta5` | 1.6 |  |
| `v1beta4` | 1.5 |  |
| `v1beta3` | 1.4 | 1.7 |
| `v1beta2` | 1.2 | 1.6 |
| `v1beta1` | Все версии | 1.6 |

1

Соответствующие версии API DynaKube будут удалены из Dynatrace Operator в следующем минорном или мажорном выпуске.

См. примеры YAML для DynaKube на [GitHub](https://github.com/Dynatrace/dynatrace-operator/tree/v1.9.0/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Dynatrace Operator version 1.8.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate.Отключено по умолчанию. | Нет значения по умолчанию (необязательно) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязательно) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap.Ключом к данным должен быть `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. |  |  |
| Нет значения по умолчанию (необязательно) | string |  |  |
| `codeModulesImagePullPolicy` | Определяет политику загрузки образа для образа CodeModules. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `imagePullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `rollingUpdate` | Определите настройки rollingUpdate для UpdateStrategy OneAgent DaemonSet.Подробнее см. [DaemonSet specification](https://dt-url.net/v0038c5). | Нет значения по умолчанию (необязательно) | RollingUpdateDaemonSet |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `imagePullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `rollingUpdate` | Определите настройки rollingUpdate для UpdateStrategy OneAgent DaemonSet.Подробнее см. [DaemonSet specification](https://dt-url.net/v0038c5). | Нет значения по умолчанию (необязательно) | RollingUpdateDaemonSet |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. | Нет значения по умолчанию (необязательно) | string |
| `codeModulesImagePullPolicy` | Определяет политику загрузки образа для образа CodeModules. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `imagePullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `imagePullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `rollingUpdate` | Определите настройки rollingUpdate для UpdateStrategy OneAgent DaemonSet.Подробнее см. [DaemonSet specification](https://dt-url.net/v0038c5). | Нет значения по умолчанию (необязательно) | RollingUpdateDaemonSet |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-2-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-2-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `imagePullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `rollingUpdate` | Определите настройки rollingUpdate для UpdateStrategy ActiveGate StatefulSet. Подробнее см. [StatefulSet Specification](https://dt-url.net/ql238m1).  UpdateStrategy для StatefulSet требует Kubernetes 1.35 и выше. На более ранних версиях настройка игнорируется, и Operator предупреждает об игнорируемых настройках, если они были указаны. | Нет значения по умолчанию (необязательно) | RollingUpdateStatefulSetStrategy |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | Нет значения по умолчанию (необязательно) | int |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и допускает Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `prometheus` | Включает расширение prometheus. | Нет значения по умолчанию (необязательно) |  |
| `databases` | Список расширений баз данных. | Нет значения по умолчанию (необязательно) | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.extensions.databases`

Доступно в будущей версии Dynatrace.

* Все параметры, кроме `id`, необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `id` | Уникальное имя объекта Kubernetes. | Нет значения по умолчанию (обязательно) | string |
| `replicas` | Количество реплик SQL Extension Executor. | 1 | int32 |
| `volumes` | Тома для аутентификации на основе файлов. | Нет значения по умолчанию (необязательно) | []Volume |
| `volumeMounts` | Монтирования томов для аутентификации на основе файлов. | Нет значения по умолчанию (необязательно) | []VolumeMount |
| `serviceAccountName` | ServiceAccount для аутентификации на основе IAM. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Метки SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Label |
| `annotations` | Аннотации SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Annotation |
| `affinity` | Affinity для SQL Extension Executor. | Нет значения по умолчанию (необязательно) | []Affinity |
| `resources` | Ресурсы SQL Extension Executor. | Нет значения по умолчанию (необязательно) | ResourcesSpec |
| `nodeSelector` | Селектор узлов SQL Extension Executor. | Нет значения по умолчанию (необязательно) | NodeSelectorSpec |
| `topologySpreadConstraints` | Topology spread constraints для SQL Extension Executor. | Нет значения по умолчанию (необязательно) | TopologySpreadConstraints |

В OpenShift использование томов типа `hostPath` запрещено политикой SCC по умолчанию и приведёт к сбоям. Если `hostPath` необходим, создайте роль с достаточными привилегиями и привяжите её к соответствующему service account. В этом примере созданная роль привязывается к service account с именем `custom-sql-extension-executor-sa`:

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

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Чтобы использовать KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.
* Все параметры в `.spec.kspm` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Указывает пути на хосте, которые монтируются в контейнер NCC. | Нет значения по умолчанию (необязательно) | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Указывает правила и условия для сопоставления атрибутов приёма. | Нет значения по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Указывает имя атрибута для сопоставления правил приёма. | Нет значения по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма применилось. | Нет значения по умолчанию (необязательно) | []string |

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

Dynatrace Operator version 1.6.0+

Включите дополнительные [конечные точки приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для приёма данных локально в кластере.") в Kubernetes для приёма данных локально в кластере с использованием сторонних протоколов. Добавление этого раздела разворачивает рабочую нагрузку Dynatrace Collector в кластере.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Указывает протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Указывает имя используемого сервиса. Если не указано, serviceName устанавливается в значение по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый telemetryIngest. | Нет значения по умолчанию (необязательно) | string |

## `.spec.otlpExporterConfiguration`

Dynatrace Operator version 1.8.0+

Включите автоматическую [настройку экспортёра OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматически настраивайте экспортёр OTLP в приложениях, инструментированных с помощью OpenTelemetry SDK, средствами Dynatrace Operator.") для подов приложений, которые уже инструментированы с помощью OpenTelemetry SDK.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `signals` | Сигналы OpenTelemetry, которые будут автоматически приниматься в Dynatrace. | Нет значения по умолчанию (необязательно) | [signalConfiguration](#otlp-exporter-signals) |
| `namespaceSelector` | Пространства имён, в которые будет внедряться конфигурация экспортёра OTLP. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides#annotate "Подробное описание вариантов установки и настройки для конкретных сценариев использования") | Нет значения по умолчанию (необязательно) | LabelSelector |
| `overrideEnvVars` | Включает переопределение существующих переменных окружения конфигурации экспортёра OTLP. | false | boolean |

## `.spec.otlpExporterConfiguration.signals`

Dynatrace Operator version 1.8.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `logs` | Включает автоматическую настройку экспортёра OTLP для логов. См. [endpoint urls for otlphttp](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | Нет значения по умолчанию (необязательно) | object |
| `metrics` | Включает автоматическую настройку экспортёра OTLP для метрик. См. [endpoint urls for otlphttp](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | Нет значения по умолчанию (необязательно) | object |
| `traces` | Включает автоматическую настройку экспортёра OTLP для трассировок. См. [endpoint urls for otlphttp](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp) | Нет значения по умолчанию (необязательно) | object |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определите updateStrategy для daemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | DaemonSetUpdateStrategy |
| `labels` | Добавьте пользовательские метки к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Добавьте пользовательские аннотации к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (необязательно) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, определяет приоритет пода. Имя должно быть задано путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определите nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задайте tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |
| `env` | Задайте дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `repository` | URL образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Добавьте пользовательские метки к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задайте политику DNS для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначьте класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима защищённых вычислений для подов LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `rollingUpdate` | Определите настройки rollingUpdate для UpdateStrategy LogMonitoring DaemonSet.Подробнее см. [DaemonSet specification](https://dt-url.net/v0038c5). | Нет значения по умолчанию (необязательно) | RollingUpdateDaemonSet |
| `tolerations` | Задайте tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.extensionExecutionController`

Доступно в будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указано, используется PVC по умолчанию. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат для связи между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `customExtensionCertificates` | Секрет, содержащий сертификаты, использованные для подписи пользовательских расширений. Необходим для проверки подписи расширений в Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (необязательно) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый Dynatrace Collector для проверки соединений с конечными точками других компонентов. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `pullPolicy` | Определяет политику загрузки образа. Если не задано, применяется значение по умолчанию Kubernetes. | Нет значения по умолчанию (необязательно) | string |
| `repository` | URL образа Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.sqlExtensionExecutor`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для SQL Extension Executor. | Нет значения по умолчанию (необязательно) | [imageRef](#extensions-sql-extension-executor-image-ref) |
| `tolerations` | Tolerations для подов SQL Extension Executor.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |

## `.spec.templates.sqlExtensionExecutor.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа SQL Extension Executor. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа SQL Extension Executor. | Нет значения по умолчанию (необязательно) | string |

Dynatrace Operator version 1.6.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate.Отключено по умолчанию. | Нет значения по умолчанию (необязательно) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязательно) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap.Ключом к данным должен быть `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-3-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-3-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | Нет значения по умолчанию (необязательно) | int |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |
| `volumeClaimTemplate` | Описывает общие атрибуты устройств хранения и допускает Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator version 1.9.0+

Когда для пространства имён настроено внедрение OneAgent, обогащение метаданными неявно включается для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Чтобы использовать расширения

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Чтобы использовать KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.
* Все параметры в `.spec.kspm` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Указывает пути на хосте, которые монтируются в контейнер NCC. | Нет значения по умолчанию (необязательно) | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Указывает правила и условия для сопоставления атрибутов приёма. | Нет значения по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Указывает имя атрибута для сопоставления правил приёма. | Нет значения по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма применилось. | Нет значения по умолчанию (необязательно) | []string |

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

Dynatrace Operator version 1.6.0+

Включите [конечные точки телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для приёма данных локально в кластере.") Dynatrace в Kubernetes для приёма данных локально в кластере. Добавление этого раздела разворачивает Dynatrace Collector силами Dynatrace Operator.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Указывает протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Указывает имя используемого сервиса. Если не указано, serviceName устанавливается в значение по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый telemetryIngest. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определите updateStrategy для daemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | DaemonSetUpdateStrategy |
| `labels` | Добавьте пользовательские метки к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Добавьте пользовательские аннотации к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (необязательно) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, определяет приоритет пода. Имя должно быть задано путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определите nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задайте tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |
| `env` | Задайте дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Добавьте пользовательские метки к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задайте политику DNS для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначьте класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима защищённых вычислений для подов LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Задайте tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.extensionExecutionController`

Доступно в будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указано, используется PVC по умолчанию. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат для связи между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `customExtensionCertificates` | Секрет, содержащий сертификаты, использованные для подписи пользовательских расширений. Необходим для проверки подписи расширений в Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (необязательно) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый Dynatrace Collector для проверки соединений с конечными точками других компонентов. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator version 1.5.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate.Отключено по умолчанию. | Нет значения по умолчанию (необязательно) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязательно) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap.Ключом к данным должен быть `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://github.com/Dynatrace/dynatrace-operator/tree/v1.9.0/assets/samples/dynakube).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для внедрения в поды приложений. Обновления применяются только при изменении ссылки на образ. Если используется плавающий тег (например, `latest`), новые образы, опубликованные под тем же тегом, не подхватываются автоматически на существующих узлах. Рекомендуется использовать уникальный тег для каждой версии образа OneAgent CodeModule. | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `storageHostPath` | Доступный для записи каталог в файловой системе хоста, где будут храниться конфигурации OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-4-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-4-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `terminationGracePeriodSeconds` | Настраивает параметр terminationGracePeriodSeconds пода ActiveGate. Применяются значения по умолчанию и правила Kubernetes. | Нет значения по умолчанию (необязательно) | int |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |
| `persistentVolumeClaim` | Описывает общие атрибуты устройств хранения и допускает Source для атрибутов, специфичных для провайдера. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaimSpec |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator version 1.9.0+

Когда для пространства имён настроено внедрение OneAgent, обогащение метаданными неявно включается для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Чтобы использовать расширения

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Чтобы использовать KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Указывает правила и условия для сопоставления атрибутов приёма. | Нет значения по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Указывает имя атрибута для сопоставления правил приёма. | Нет значения по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма применилось. | Нет значения по умолчанию (необязательно) | []string |

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

Dynatrace Operator version 1.6.0+

Добавление этого раздела разворачивает Dynatrace Collector силами Operator.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `protocols` | Указывает протоколы, которые будет принимать Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Указывает имя используемого сервиса. Если не указано, serviceName устанавливается в значение по умолчанию. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый telemetryIngest. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `updateStrategy` | Определите updateStrategy для daemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | DaemonSetUpdateStrategy |
| `labels` | Добавьте пользовательские метки к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Добавьте пользовательские аннотации к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (необязательно) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, определяет приоритет пода. Имя должно быть задано путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определите nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задайте tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |
| `env` | Задайте дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Добавьте пользовательские метки к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задайте политику DNS для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначьте класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима защищённых вычислений для подов LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Задайте tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.logMonitoring.imageRef`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.extensionExecutionController`

Доступно в будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указано, используется PVC по умолчанию. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат для связи между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `customExtensionCertificates` | Секрет, содержащий сертификаты, использованные для подписи пользовательских расширений. Необходим для проверки подписи расширений в Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |
| `useEphemeralVolume` | Указывает, использовать ли эфемерный том для хранения. | Нет значения по умолчанию (необязательно) | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (необязательно) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый Dynatrace Collector для проверки соединений с конечными точками других компонентов. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator version 1.4.0+

## `.spec`

* Параметр `apiUrl` обязателен и неизменяем. После установки его нельзя изменить в существующем DynaKube.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate.Отключено по умолчанию. | Нет значения по умолчанию (необязательно) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязательно) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap.Ключом к данным должен быть `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-5-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-5-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

### Неявное обогащение метаданными

Dynatrace Operator version 1.9.0+

Когда для пространства имён настроено внедрение OneAgent, обогащение метаданными неявно включается для этого пространства имён, даже если параметр `enabled` в `.spec.metadataEnrichment` установлен в `false`.

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

Добавление этого раздела включает поддержку расширений в Kubernetes. Чтобы использовать расширения

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.kspm`

Добавление этого раздела включает [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Чтобы использовать KSPM

* `kubernetes-monitoring` обязателен и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, а также
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.

## `.spec.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

Для Log Monitoring требуется включённая [возможность ActiveGate](#active-gate) `kubernetes-monitoring`, но её не обязательно настраивать в том же DynaKube. Если `kubernetes-monitoring` отсутствует или флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` установлен в `false`, Operator выдаёт предупреждение, но Log Monitoring всё равно разворачивается.

* Все параметры в `.spec.logMonitoring` необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Указывает правила и условия для сопоставления атрибутов приёма. | Нет значения по умолчанию (необязательно) | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

Это поле неизменяемо. После установки оно больше не обновляется.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `attribute` | Указывает имя атрибута для сопоставления правил приёма. | Нет значения по умолчанию (необязательно) | string |
| `values` | Перечисляет значения, которым должен соответствовать `attribute`, чтобы правило приёма применилось. | Нет значения по умолчанию (необязательно) | []string |

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
| `updateStrategy` | Определите updateStrategy для daemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | DaemonSetUpdateStrategy |
| `labels` | Добавьте пользовательские метки к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Добавьте пользовательские аннотации к подам Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды Node Configuration Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию. | Нет значения по умолчанию (необязательно) | [imageRef](#kspm-image-ref) |
| `priorityClassName` | Если указано, определяет приоритет пода. Имя должно быть задано путём создания объекта PriorityClass с этим именем. Если не указано, настройка будет удалена из DaemonSet. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для подов Node Configuration Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определите nodeAffinity для DaemonSet Node Configuration Collector | Нет значения по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задайте tolerations для подов Node Configuration Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |
| `env` | Задайте дополнительные переменные окружения для основного контейнера Node Configuration Collector. | Нет значения по умолчанию (необязательно) | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| repository | URL образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |
| tag | Тег образа Node Configuration Collector. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.logMonitoring`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

* Параметр `imageRef` обязателен.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Добавьте пользовательские метки к подам LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будут развёрнуты поды LogMonitoring. | Нет значения по умолчанию (необязательно) | map[string]string |
| `imageRef` | Переопределяет образ по умолчанию для подов LogMonitoring. | Нет значения по умолчанию (обязательно) | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Задайте политику DNS для подов LogMonitoring. | `ClusterFirst` | string |
| `priorityClassName` | Назначьте класс приоритета подам LogMonitoring. По умолчанию класс не задан. | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Настраивает профиль SecComp для включения режима защищённых вычислений для подов LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Определите запросы и лимиты ресурсов для основного и init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `nodeAffinity` | Определите nodeAffinity для DaemonSet NodeConfigurationCollector | Нет значения по умолчанию (необязательно) | NodeAffinity |
| `tolerations` | Задайте tolerations для подов LogMonitoring.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `args` | Задайте дополнительные аргументы для init-контейнера LogMonitoring. | Нет значения по умолчанию (необязательно) | []string |
| `updateStrategy` | Определите updateStrategy для daemonSet NodeConfigurationCollector. | Нет значения по умолчанию (необязательно) | DaemonSetUpdateStrategy |

## `.spec.templates.logMonitoring.imageRef`

Доступно с версии Dynatrace 1.306 и OneAgent 1.305

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа LogMonitoring. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.extensionExecutionController`

Доступно в будущей версии Dynatrace.

* Параметр `imageRef` обязателен.
* Все остальные параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Extension Execution Controller. Это поле обязательно. | Нет значения по умолчанию (обязательно) | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC для Extension Execution Controller. Если не указано, используется PVC по умолчанию. | Нет значения по умолчанию (необязательно) | PersistentVolumeClaim |
| `labels` | Метки, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Extension Execution Controller. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат для связи между Extension Execution Controller и Dynatrace Collector. | Нет значения по умолчанию (необязательно) | string |
| `customConfig` | ConfigMap, содержащий пользовательскую конфигурацию Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `customExtensionCertificates` | Секрет, содержащий сертификаты, использованные для подписи пользовательских расширений. Необходим для проверки подписи расширений в Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Extension Execution Controller.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Extension Execution Controller. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

## `.spec.templates.extensionExecutionController.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |
| `tag` | Тег образа Extension Execution Controller. | Нет значения по умолчанию (необязательно) | string |

## `.spec.templates.otelCollector`

Доступно в будущей версии Dynatrace.

* Все параметры необязательны.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `imageRef` | Образ, используемый для Dynatrace Collector. | Нет значения по умолчанию (необязательно) | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Количество реплик Dynatrace Collector. | 1 | int32 |
| `labels` | Метки, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `annotations` | Аннотации, применяемые к поду Dynatrace Collector. | Нет значения по умолчанию (необязательно) | map[string]string |
| `tlsRefName` | Секрет, содержащий TLS-сертификат, используемый Dynatrace Collector для проверки соединений с конечными точками других компонентов. | Нет значения по умолчанию (необязательно) | string |
| `resources` | Настройки ресурсов для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `tolerations` | Tolerations для пода Dynatrace Collector.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints для пода Dynatrace Collector. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Доступно в будущей версии Dynatrace.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `repository` | URL образа Dynatrace Collector. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Тег образа Dynatrace Collector. | `latest` | string |

Dynatrace Operator version 1.2.0 - 1.6.0

Уведомление о прекращении поддержки

Версия API DynaKube `v1beta2` больше не доступна в Dynatrace Operator версии 1.7.0+.

## `.spec`

* Параметр `apiUrl` обязателен.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") | Нет значения по умолчанию (обязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `dynatraceApiRequestThreshold` | Минимальное число минут между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate.Отключено по умолчанию. | Нет значения по умолчанию (необязательно) | boolean |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | DynaKubeProxy |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | Нет значения по умолчанию (необязательно) | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap.Ключом к данным должен быть `certs`.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator.Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |
| `useCSIDriver` | Установите, если нужно использовать CSIDriver. Не включайте, если у вас нет доступа к узлам Kubernetes или недостаточно привилегий. | `false` | boolean |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `secCompProfile` | Профиль SecComp, который будет настроен для запуска в режиме защищённых вычислений. | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-6-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-6-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры необязательны.

Дополнительные сведения см. в разделе [Настройка каталога обогащения](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Обогащение метаданными в Dynatrace Operator добавляет контекст к подам Kubernetes, присоединяя релевантные метаданные к таким сущностям, как поды, хосты и процессы, для лучшей наблюдаемости.")

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `true`. | `true` | boolean |

Версия API DynaKube `v1beta1` больше не доступна в Dynatrace Operator версии 1.6.0+.
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

Dynatrace Operator version <=1.6.0

Уведомление о прекращении поддержки

Версия API DynaKube `v1beta1` больше не доступна в Dynatrace Operator версии 1.7.0+.

## `.spec`

* Параметр `apiUrl` обязателен.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце.- Для SaaS задайте `YOUR_ENVIRONMENT_ID` равным вашему ID окружения.- Для Managed измените адрес `apiUrl`.Инструкции по определению ID окружения и настройке адреса apiUrl см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга."). | Нет значения по умолчанию (обязательно) | string |
| `tokens` | Имя секрета, содержащего токены. | Имя пользовательского ресурса (`.metadata.name`), если не задано | string |
| `skipCertCheck` | Отключает проверку сертификата для соединения между Dynatrace Operator и Dynatrace Cluster.Установите `true`, если нужно пропустить проверки валидации сертификата. | `false` | boolean |
| `proxy` | Задаёт пользовательские настройки proxy напрямую или из секрета с полем `proxy`.Применяется к Dynatrace Operator, ActiveGate и OneAgent. | Нет значения по умолчанию (необязательно) | string |
| `trustedCAs` | Добавляет пользовательские RootCAs из configmap. Поместите сертификат под ключом `certs` в вашем configmap.Применяется к Dynatrace Operator, OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `networkZone` | Задаёт network zone для подов OneAgent и ActiveGate. | Нет значения по умолчанию (необязательно) | string |
| `customPullSecret` | Определяет пользовательский pull-секрет на случай использования приватного реестра при загрузке образов из окружения Dynatrace.Примечание: для [функции загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа узла") без CSI driver необходимо вручную обеспечить наличие pull-секретов во внедрённом поде. Подробнее см. [предварительные требования для загрузки образа узла](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образа узла").Чтобы определить пользовательский pull-секрет и узнать об ожидаемом поведении, см. [Настройка `customPullSecret`](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Использование приватного реестра"). | Нет значения по умолчанию (необязательно) | string |
| `enableIstio` | Когда включено и если Istio установлен в окружении Kubernetes, Dynatrace Operator создаёт соответствующие объекты VirtualService и ServiceEntry, чтобы разрешить доступ к Dynatrace Cluster от OneAgent или ActiveGate. Отключено по умолчанию. | `false` | boolean |
| `namespaceSelector` | Применимо только для типов конфигурации `applicationMonitoring` или `cloudNativeFullStack`. Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры необязательны.

Рекомендуется

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `version` | Версия OneAgent, используемая для OneAgent мониторинга хостов, работающих в выделенном поде. Эта настройка не влияет на версию OneAgent, используемую для мониторинга приложений. | По умолчанию используется последняя версия. | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

## `.spec.oneAgent.classicFullStack`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `image` | Используйте пользовательский образ Docker для OneAgent. По умолчанию используется образ из кластера Dynatrace. | Имя образа. | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |

## `.spec.oneAgent.applicationMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `codeModulesImage` | Образ OneAgent, используемый для внедрения в поды | Нет значения по умолчанию (необязательно) | string |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `useCSIDriver` | Установите, если нужно использовать CSI driver. Не включайте, если у вас нет доступа к узлам Kubernetes или недостаточно привилегий. | `false` | boolean |
| `initResources` | Определите запросы и лимиты ресурсов для initContainer. Подробнее см. [Managing resources for containers](https://dt-url.net/atc371q). | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `hostGroup` | Укажите имя группы, к которой нужно отнести хост. Этот способ предпочтительнее устаревшего аргумента `--set-host-group`. Если используются обе настройки, это поле имеет приоритет над аргументом `--set-host-group`. | Нет значения по умолчанию (необязательно) | string |
| `namespaceSelector` | Пространства имён, в которые должен внедряться Dynatrace Operator. Подробнее см. [Настройка мониторинга для пространств имён и подов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"). | Нет значения по умолчанию (необязательно) | LabelSelector |

## `.spec.oneAgent.hostMonitoring`

* Все параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `version` | Используемая версия OneAgent. | По умолчанию используется последняя версия. | string |
| `image` | Используйте пользовательский образ Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `priorityClassName` | Назначьте класс приоритета подам OneAgent. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `tolerations` | Tolerations, включаемые в OneAgent DaemonSet.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление OneAgent сильно зависит от отслеживаемой рабочей нагрузки. Можно использовать настройки по умолчанию в [CR](https://dt-url.net/dynakube-samples).`resource.requests` показывает значения, необходимые для запуска; `resource.limits` показывает максимальные лимиты для пода. | Нет значения по умолчанию (необязательно) | ResourceRequirements |
| `autoUpdate` (**устаревший**) | Устаревшее поле, будет удалено в одном из будущих выпусков. [Закрепите версию OneAgent на вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").Автообновление отключается, когда заданы поля `version` или `image`. | `true` | boolean |
| `dnsPolicy` | Задайте политику DNS для подов OneAgent.Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Добавьте пользовательские аннотации OneAgent. | Нет значения по умолчанию (необязательно) | map[string]string |
| `labels` | Заданные вами метки для подов OneAgent, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `env` | Задайте дополнительные переменные окружения для подов OneAgent. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `args` | Задайте дополнительные аргументы для установщика OneAgent.Доступные параметры см. в разделе [Пользовательская установка на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик для Linux с параметрами командной строки.").Список ограничений см. в разделе [Ограничения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как контейнера Docker."). | Нет значения по умолчанию (необязательно) | []string |

## `.spec.activeGate`

* Параметр `capabilities` обязателен.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры необязательны.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `capabilities` | Определяет возможности пода ActiveGate: какую функциональность следует включить.Возможные значения:- `routing` включает маршрутизацию OneAgent.- `kubernetes-monitoring` включает мониторинг Kubernetes API.- `metrics-ingest`[1](#fn-7-1-def) открывает конечную точку приёма метрик на ActiveGate DynaKube и перенаправляет на неё все поды.- `dynatrace-api`[1](#fn-7-1-def) включает вызов API Dynatrace через ActiveGate.- `debugging` включает [модуль Live Debugging](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований.") в ActiveGate. | Нет значения по умолчанию (обязательно) | string |
| `image` | Используйте пользовательский образ ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Нет значения по умолчанию (необязательно) | string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `tolerations` | Задайте tolerations для подов ActiveGate.Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Нет значения по умолчанию (необязательно) | []Toleration |
| `nodeSelector` | Укажите селектор узлов, который определяет, на каких узлах будет развёрнут ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ActiveGate сильно зависит от отслеживаемой рабочей нагрузки; корректируйте значения соответственно. | Нет значения по умолчанию (рекомендуется) | ResourceRequirements |
| `labels` | Заданные вами метки для подов ActiveGate, чтобы структурировать рабочие нагрузки по необходимости. | Нет значения по умолчанию (необязательно) | map[string]string |
| `env` | Задайте дополнительные переменные окружения для подов ActiveGate. | Нет значения по умолчанию (необязательно) | []EnvVar |
| `group` | Задайте группу активации для ActiveGate. Подробнее см. [Настройка свойств ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших нужд и требований."). | Нет значения по умолчанию (рекомендуется) | string |
| `customProperties` | Добавьте файл пользовательских свойств, указав его как значение или сославшись на него из секрета.При ссылке на файл пользовательских свойств из секрета убедитесь, что ключ называется `customProperties`. Подробнее см. [Как добавить файл пользовательских свойств](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств"). | Нет значения по умолчанию (необязательно) | string |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. Подробнее см. [Как добавить пользовательский сертификат для ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Настройка Dynatrace в окружениях с сетевыми ограничениями, сетевых параметров и конфигураций proxy."). | Нет значения по умолчанию (необязательно) | string |
| `dnsPolicy` | Задайте политику DNS для подов ActiveGate. | `ClusterFirstWithHostNet` | string |
| `priorityClassName` | Назначьте класс приоритета подам ActiveGate. По умолчанию класс не задан.Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Нет значения по умолчанию (необязательно) | string |
| `annotations` | Добавьте пользовательские аннотации ActiveGate. | Нет значения по умолчанию (необязательно) | map[string]string |
| `topologySpreadConstraints` | Добавляет [topology spread constraints](https://dt-url.net/xc03ysw) к подам ActiveGate. | Нет значения по умолчанию (необязательно) | []TopologySpreadConstraint |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.