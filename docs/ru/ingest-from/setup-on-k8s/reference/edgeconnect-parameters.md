---
title: Параметры EdgeConnect для Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters
scraped: 2026-03-04T21:30:01.817464
---

# Параметры EdgeConnect для Dynatrace Operator


* Latest Dynatrace
* 7-min read
* Updated on Dec 22, 2025

[EdgeConnect](../../edgeconnect.md "Use EdgeConnect to control how your apps and workflows interact with your internal systems.") позволяет приложениям и рабочим процессам Dynatrace безопасно взаимодействовать с вашими системами. EdgeConnect доступен в виде контейнера Docker и может работать в любой среде выполнения контейнеров. В этом справочном руководстве представлена подробная информация о настройке [пользовательского ресурса](https://dt-url.net/b60397m) EdgeConnect в вашей среде Kubernetes.

В следующей таблице перечислены минимально необходимые версии Dynatrace Operator для каждой версии API EdgeConnect.

| Версия API DynaKube | Минимальная версия Dynatrace Operator |
| --- | --- |
| `v1alpha2` | 1.3.0+ |
| `v1alpha1` | Все версии |

v1alpha1

v1alpha2

## `.spec`

* Параметры `apiServer` и `oauth` являются обязательными.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiServer` | Расположение имени хоста API Dynatrace для подключения, включая уникальный UUID вашей среды. Пример: `ENVIRONMENT_ID.live.dynatrace.com` | Не применимо | string |
| `annotations` | Добавляет аннотации к Pod-ам EdgeConnect. | Не применимо | map[string] string |
| `autoUpdate` | Включает автоматический перезапуск Pod-ов EdgeConnect при появлении новой версии. | `true` | boolean |
| `customPullSecret` | Секрет для загрузки образов из вашего частного реестра. | Не применимо | string |
| `env` | Добавляет переменные окружения к Pod-ам EdgeConnect. | Не применимо | []EnvVar |
| `hostRestrictions` | Ограничивает исходящие HTTP-запросы от ваших внутренних ресурсов указанными хостами. Список через запятую. | Не применимо | string |
| `imageRef` | Переопределяет образ по умолчанию. | Не применимо | Object |
| `labels` | Добавляет метки к Pod-ам EdgeConnect. | Не применимо | map[string]string |
| `nodeSelector` | Селектор узлов для управления выбором узлов для Pod-ов EdgeConnect. | Не применимо | map[string]string |
| `oauth` | EdgeConnect использует OAuth-клиент для аутентификации на платформе Dynatrace. | Не применимо | Object |
| `replicas` | Количество реплик для вашего EdgeConnect. | 1 | int |
| `resources` | Определяет запросы ресурсов и ограничения для отдельных Pod-ов. | Не применимо | ResourceRequirements |
| `tolerations` | Указывает допуски для вашего EdgeConnect. | Не применимо | []Toleration |
| `topologySpreadConstraints` | Устанавливает ограничения распределения по топологии для Pod-ов EdgeConnect. | Не применимо | []TopologySpreadConstraint |
| `hostPatterns` | Указывает список шаблонов хостов для запросов, управляемых экземпляром EdgeConnect. Это поле является обязательным и используется только при `.spec.oauth.provisioner` = `true`. | empty | []string |
| `caCertsRef` | Добавляет пользовательский корневой сертификат из ConfigMap. Убедитесь, что сертификат находится в каталоге `certs` внутри вашего ConfigMap. | empty | string |

## `.spec.oauth`

* Параметры `resource`, `endpoint`, `clientSecret` являются обязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `clientSecret` | Имя секрета, содержащего ID/секрет OAuth-клиента. | Не применимо | string |
| `endpoint` | URL конечной точки токена Dynatrace SSO. | Не применимо | string |
| `resource` | URN, идентифицирующий вашу учётную запись. URN предоставляется при создании OAuth-клиента. | Не применимо | string |
| `provisioner` | Включает автоматическое предоставление EdgeConnect. Для этого требуется настройка поля `.spec.hostPatterns`. | `false` | bool |

## `.spec.imageRef`

* Все параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `repository` | Пользовательский репозиторий образов EdgeConnect. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Указывает версию образа EdgeConnect. | `latest` | string |

## `.spec.proxy`

* Все параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `authRef` | Имя секрета, содержащего имя пользователя и пароль для аутентификации на прокси-сервере с использованием базовой схемы HTTP-аутентификации. | empty | string |
| `host` | Адрес сервера (имя хоста или IP-адрес) прокси-сервера. | empty | string |
| `noProxy` | Представляет переменную окружения `NO_PROXY` или `no_proxy`. Указывает строку со значениями через запятую, определяющими хосты, которые должны быть исключены из проксирования. | empty | string |
| `port` | Порт прокси-сервера. | empty | integer |

## `.spec`

* Параметры `apiServer` и `oauth` являются обязательными.
* Все остальные параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `apiServer` | Расположение имени хоста API Dynatrace для подключения, включая уникальный UUID вашей среды. Пример: `ENVIRONMENT_ID.live.dynatrace.com` | Не применимо | string |
| `annotations` | Добавляет аннотации к Pod-ам EdgeConnect. | Не применимо | map[string] string |
| `autoUpdate` | Включает автоматический перезапуск Pod-ов EdgeConnect при появлении новой версии. | `true` | boolean |
| `customPullSecret` | Секрет для загрузки образов из вашего частного реестра. | Не применимо | string |
| `env` | Добавляет переменные окружения к Pod-ам EdgeConnect. | Не применимо | []EnvVar |
| `hostRestrictions` | Ограничивает исходящие HTTP-запросы от ваших внутренних ресурсов указанными хостами. | Не применимо | []string |
| `imageRef` | Переопределяет образ по умолчанию. | Не применимо | Object |
| `labels` | Добавляет метки к Pod-ам EdgeConnect. | Не применимо | map[string]string |
| `nodeSelector` | Селектор узлов для управления выбором узлов для Pod-ов EdgeConnect. | Не применимо | map[string]string |
| `oauth` | EdgeConnect использует OAuth-клиент для аутентификации на платформе Dynatrace. | Не применимо | Object |
| `replicas` | Количество реплик для вашего EdgeConnect. | 1 | int |
| `resources` | Определяет запросы ресурсов и ограничения для отдельных Pod-ов. | Не применимо | ResourceRequirements |
| `tolerations` | Указывает допуски для вашего EdgeConnect. | Не применимо | []Toleration |
| `topologySpreadConstraints` | Устанавливает ограничения распределения по топологии для Pod-ов EdgeConnect. | Не применимо | []TopologySpreadConstraint |
| `hostPatterns` | Указывает список шаблонов хостов для запросов, управляемых экземпляром EdgeConnect. Это поле является обязательным и используется только при `.spec.oauth.provisioner` = `true`. | empty | []string |
| `caCertsRef` | Добавляет пользовательский корневой сертификат из ConfigMap. Убедитесь, что сертификат находится в каталоге `certs` внутри вашего ConfigMap. | empty | string |
| `serviceAccountName` | Имя Kubernetes `ServiceAccount`, позволяющего EdgeConnect получить доступ к API Kubernetes. | `dynatrace-edgeconnect` | string |
| `kubernetesAutomation` | Настраивает Kubernetes Automation. | Не применимо | Object |

## `.spec.oauth`

* Параметры `resource`, `endpoint`, `clientSecret` являются обязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `clientSecret` | Имя секрета, содержащего ID/секрет OAuth-клиента. | Не применимо | string |
| `endpoint` | URL конечной точки токена Dynatrace SSO. | Не применимо | string |
| `resource` | URN, идентифицирующий вашу учётную запись. URN предоставляется при создании OAuth-клиента. | Не применимо | string |
| `provisioner` | Включает автоматическое предоставление EdgeConnect. Для этого требуется настройка поля `.spec.hostPatterns`. | `false` | bool |

## `.spec.imageRef`

* Все параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `repository` | Пользовательский репозиторий образов EdgeConnect. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Указывает версию образа EdgeConnect. | `latest` | string |

## `.spec.proxy`

* Все параметры являются необязательными.

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `authRef` | Имя секрета, содержащего имя пользователя и пароль для аутентификации на прокси-сервере с использованием базовой схемы HTTP-аутентификации. | empty | string |
| `host` | Адрес сервера (имя хоста или IP-адрес) прокси-сервера. | empty | string |
| `noProxy` | Представляет переменную окружения `NO_PROXY` или `no_proxy`. Указывает строку со значениями через запятую, определяющими хосты, которые должны быть исключены из проксирования. | empty | string |
| `port` | Порт прокси-сервера. | empty | integer |

## `.spec.kubernetesApiAutomation`

| **Параметр** | **Описание** | **Значение по умолчанию** | **Тип данных** |
| --- | --- | --- | --- |
| `enabled` | Включает Kubernetes Automation. | `false` | bool |
