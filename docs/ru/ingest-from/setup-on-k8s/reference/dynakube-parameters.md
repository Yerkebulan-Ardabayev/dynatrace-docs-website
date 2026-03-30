---
title: Параметры DynaKube для Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters
scraped: 2026-03-06T21:31:41.255882
---

Эта страница поможет вам понять и настроить пользовательский ресурс DynaKube [Kubernetes Custom Resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), что позволит оптимизировать настройку Dynatrace Operator в соответствии с вашими конкретными требованиями.

В таблице ниже указаны необходимые версии Dynatrace Operator для каждой версии API DynaKube.

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

См. примеры DynaKube YAML на [GitHub](https://github.com/Dynatrace/dynatrace-operator/tree/v1.8.1/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Dynatrace Operator версии 1.8.0+

## `.spec`

* Параметр `apiUrl` является обязательным и неизменяемым. После установки он не может быть изменён в существующем DynaKube.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiUrl` | `apiUrl` Dynatrace, включая путь `/api` в конце. - Для Dynatrace установите `YOUR_ENVIRONMENT_ID` как ID вашей среды. - Для Managed измените адрес `apiUrl`. Инструкции по определению ID среды и настройке адреса apiUrl см. в разделе ID среды | - | string |
| `customPullSecret` | Определяет пользовательский pull secret, если вы используете частный реестр при загрузке образов из среды Dynatrace. Примечание: для функции загрузки образов узлов без CSI-драйвера необходимо вручную обеспечить доступность pull secrets в инжектированном поде. | - | string |
| `dynatraceApiRequestThreshold` | Минимальный интервал в минутах между запросами к API Dynatrace. | 15 | integer |
| `enableIstio` | При включении, если Istio установлен в среде Kubernetes, Dynatrace Operator создаст соответствующие объекты VirtualService и ServiceEntry для обеспечения доступа к кластеру Dynatrace из OneAgent или ActiveGate. Отключено по умолчанию. | - | boolean |
| `networkZone` | Устанавливает сетевую зону для подов OneAgent и ActiveGate. | - | string |
| `proxy` | Настройка пользовательского прокси напрямую или из секрета с полем `proxy`. Применяется к Dynatrace Operator, ActiveGate и OneAgent. | - | DynaKubeProxy |
| `skipCertCheck` | Отключение проверки сертификата для подключения между Dynatrace Operator и кластером Dynatrace. Установите `true`, если хотите пропустить проверку сертификатов. | - | boolean |
| `tokens` | Имя секрета, содержащего токены для подключения к Dynatrace. | - | string |
| `trustedCAs` | Добавляет пользовательские корневые центры сертификации из configmap. Ключ данных должен быть `certs`. Применяется к Dynatrace Operator, OneAgent и ActiveGate. | - | string |

## `.spec.oneAgent`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `hostGroup` | Укажите имя группы, к которой вы хотите назначить хост. Этот метод предпочтительнее устаревшего аргумента `--set-host-group`. Если используются оба параметра, это поле имеет приоритет над аргументом `--set-host-group`. | Не применимо | string |

## `.spec.oneAgent.cloudNativeFullStack`

* Все параметры являются необязательными.

Рекомендуемый

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавление пользовательских аннотаций OneAgent. | Не применимо | map[string]string |
| `args` | Установка дополнительных аргументов для установщика OneAgent. Доступные параметры см. в Пользовательская установка Linux. | Не применимо | []string |
| `codeModulesImage` | Указывает образ OneAgent CodeModules, используемый для инжекции в поды приложений. Обновления применяются только при изменении ссылки на образ. | Не применимо | string |
| `dnsPolicy` | Установка политики DNS для подов OneAgent. Подробнее см. [Pods DNS Policy](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Установка дополнительных переменных окружения для подов OneAgent. | Не применимо | []EnvVar |
| `image` | Использование пользовательского образа Docker для OneAgent. | Образ из кластера Dynatrace. | string |
| `initResources` | Определение запросов и лимитов ресурсов для initContainer. Подробнее см. [Управление ресурсами контейнеров](https://dt-url.net/atc371q). | Не применимо | ResourceRequirements |
| `labels` | Пользовательские метки для подов OneAgent для структурирования рабочих нагрузок. | Не применимо | map[string]string |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инжекцию. Подробнее см. Настройка мониторинга для пространств имён и подов. | Не применимо | LabelSelector |
| `nodeSelector` | Указание селектора узлов, определяющего, на каких узлах будет развёрнут OneAgent. | Не применимо | map[string]string |
| `oneAgentResources` | Настройки ресурсов для контейнера OneAgent. Потребление ресурсов OneAgent сильно зависит от рабочей нагрузки для мониторинга. | Не применимо | ResourceRequirements |
| `priorityClassName` | Назначение класса приоритета подам OneAgent. По умолчанию класс не установлен. Подробнее см. [Pod Priority and Preemption](https://dt-url.net/n8437bl). | Не применимо | string |
| `tolerations` | Толерантности для DaemonSet OneAgent. Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Не применимо | []Toleration |
| `version` | Версия OneAgent для использования при мониторинге хостов в выделенном поде. Этот параметр не влияет на версию OneAgent для мониторинга приложений. | По умолчанию используется последняя версия. | string |

## `.spec.oneAgent.classicFullStack`

* Все параметры являются необязательными.

## `.spec.oneAgent.applicationMonitoring`

* Все параметры являются необязательными.

## `.spec.oneAgent.hostMonitoring`

* Все параметры являются необязательными.

## `.spec.activeGate`

* Параметр `capabilities` является обязательным.
* Параметры `resources` и `group` рекомендуются.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `annotations` | Добавление пользовательских аннотаций ActiveGate. | Не применимо | map[string]string |
| `capabilities` | Определяет возможности пода ActiveGate: какие функции должны быть включены. Возможные значения: - `routing` включает маршрутизацию OneAgent. - `kubernetes-monitoring` включает мониторинг Kubernetes API. - `metrics-ingest`[1](#fn-2-1-def) открывает конечную точку приёма метрик на DynaKube ActiveGate и перенаправляет все поды на неё. - `dynatrace-api`[1](#fn-2-1-def) включает вызов Dynatrace API через ActiveGate. - `debugging` включает модуль Live Debugging в ActiveGate. | Не применимо | string |
| `customProperties` | Добавление файла пользовательских свойств в виде значения или ссылки из секрета. При ссылке из секрета убедитесь, что ключ называется `customProperties`. | Не применимо | string |
| `env` | Установка дополнительных переменных окружения для подов ActiveGate. | Не применимо | []EnvVar |
| `group` | Установка группы активации для ActiveGate. | Не применимо | string |
| `image` | Использование пользовательского образа ActiveGate. По умолчанию используется последний образ ActiveGate из кластера Dynatrace. | Не применимо | string |
| `labels` | Пользовательские метки для подов ActiveGate. | Не применимо | map[string]string |
| `replicas` | Количество реплик подов ActiveGate. | 1 | int |
| `resources` | Настройки ресурсов для контейнера ActiveGate. Потребление ресурсов ActiveGate сильно зависит от рабочей нагрузки для мониторинга; корректируйте значения соответственно. | Не применимо | ResourceRequirements |
| `tlsSecretName` | Имя секрета, содержащего TLS-сертификат, ключ и пароль ActiveGate. Если не задано, используется самоподписанный сертификат. | Не применимо | string |
| `tolerations` | Установка толерантностей для подов ActiveGate. Подробнее см. [Taints and Tolerations](https://dt-url.net/od03765). | Не применимо | []Toleration |

1

Для этой возможности требуется пользовательский сертификат. Подробнее см. параметр `tlsSecretName`.

## `.spec.metadataEnrichment`

* Все параметры являются необязательными.

| Параметр | Описание | Значение по умолчанию | Тип данных |
| --- | --- | --- | --- |
| `enabled` | Включает MetadataEnrichment, по умолчанию `false`. | `false` | boolean |
| `namespaceSelector` | Пространства имён, в которые Dynatrace Operator должен выполнять инжекцию. Подробнее см. Настройка мониторинга для пространств имён и подов. | Не применимо | LabelSelector |

## `.spec.extensions`

Доступно в будущей версии Dynatrace.

* Все параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `prometheus` | Включает расширение Prometheus. | Не применимо |  |
| `databases` | Список расширений баз данных. | Не применимо | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` является обязательным и должен быть добавлен в [список возможностей ActiveGate](#active-gate) в `.spec.activeGate.capabilities`, и
* Флаг функции `feature.dynatrace.com/automatic-kubernetes-api-monitoring` не должен быть установлен в `false`.
