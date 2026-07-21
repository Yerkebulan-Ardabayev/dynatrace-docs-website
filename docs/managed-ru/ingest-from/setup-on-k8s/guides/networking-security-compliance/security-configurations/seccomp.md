---
title: Профили seccomp
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp
---

# Профили seccomp

# Профили seccomp

* Пояснение
* Чтение 5 мин
* Опубликовано 24 марта 2026 г.

## Что такое seccomp?

Seccomp (secure computing mode), это функция безопасности ядра Linux, которая ограничивает системные вызовы, которые может выполнять процесс. Применяя профиль seccomp к контейнеру, ограничивается набор операций на уровне ядра, которые он может выполнять, что уменьшает поверхность атаки рабочих нагрузок. Kubernetes поддерживает настройку профилей seccomp как на уровне пода, так и на уровне контейнера через поле `securityContext`, что делает эту функцию ключевым механизмом для соответствия стандартам безопасности, таким как Kubernetes [Pod Security Standards﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

В Kubernetes есть три типа профилей seccomp:

* **RuntimeDefault**, встроенный профиль контейнерного runtime по умолчанию. Он разрешает определённый набор распространённых системных вызовов, блокируя потенциально опасные.
* **Localhost**, пользовательский профиль, загружаемый из файла JSON в файловой системе узла.
* **Unconfined**, фильтрация seccomp не применяется, разрешены все системные вызовы.

Все инфраструктурные компоненты Dynatrace Operator (operator, webhook и CSI driver), а также компоненты, развёрнутые оператором (ActiveGate, EdgeConnect), используют профиль seccomp `RuntimeDefault`. Исключение составляет OneAgent, для которого профиль unconfined (профиль seccomp не задан). Профиль `RuntimeDefault` подходит для большинства рабочих нагрузок и удовлетворяет стандарту Pod Security Standard уровня **restricted**.

Использование seccomp в OpenShift

Если Dynatrace Operator внедряет профиль seccomp в под приложения в OpenShift, [SecurityContextConstraints (SCC)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies), которые запрещают использование профиля seccomp, такие как `anyuid`, `restricted` или `nonroot`, перестанут применяться. Вместо этого система переключится на другой SCC (например, `restricted-v2`), что может сделать поды непланируемыми или привести к деградации рабочей нагрузки.

## Профиль seccomp для OneAgent

По умолчанию OneAgent работает без профиля seccomp (unconfined). Это значение по умолчанию выбрано для обеспечения совместимости с максимально широким набором платформ и контейнерных runtime, поскольку OneAgent требует доступа к более широкому набору системных вызовов для глубокого мониторинга на уровне хоста.

### Настройка пользовательского профиля seccomp для OneAgent

Dynatrace Operator версии 1.2.0+

Если политики безопасности требуют наличия профиля seccomp для OneAgent, его можно настроить с помощью поля `secCompProfile` в соответствующем режиме OneAgent в пользовательском ресурсе DynaKube.

**Ограничение:** профиль seccomp для OneAgent всегда применяется с типом `Localhost`. Это значит, что нужно предоставить пользовательский файл профиля seccomp JSON на каждом узле, задать тип `RuntimeDefault` или `Unconfined` через это поле нельзя.

Cloud-native full stack

Classic full stack

Host monitoring

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullStack:



secCompProfile: "my-seccomp-profile.json"
```

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: "my-seccomp-profile.json"
```

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: "my-seccomp-profile.json"
```

Тип `Localhost` требует, чтобы файл профиля seccomp JSON присутствовал в локальной файловой системе узла, в корневом каталоге профилей seccomp, настроенном для kubelet (по умолчанию `/var/lib/kubelet/seccomp/`). Для приведённых выше примеров файл профиля должен находиться по пути `/var/lib/kubelet/seccomp/my-seccomp-profile.json` на каждом узле, где запланирован OneAgent.

Чтобы узнать, как создавать профили seccomp `Localhost` и управлять ими, обратитесь к документации Kubernetes:

* [Restrict a Container's Syscalls with seccomp﻿](https://kubernetes.io/docs/tutorials/security/seccomp/)
* [Set the seccomp profile for a Container﻿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-seccomp-profile-for-a-container)

## Настройка seccomp для init-контейнера Dynatrace

Dynatrace Operator версии 0.11.2+

Профиль seccomp для init-контейнера Dynatrace (используемого для внедрения модуля кода) управляется флагом функции `feature.dynatrace.com/init-container-seccomp-profile`.

Начиная с Dynatrace Operator версии 1.9.0, значение этого флага функции по умолчанию изменилось с `"false"` на `"true"`. Это означает, что теперь для init-контейнера по умолчанию применяется профиль seccomp `RuntimeDefault`, что помогает соответствовать требованиям стандарта Pod Security Standard уровня **restricted** для отслеживаемых рабочих нагрузок Kubernetes.

Если используется Dynatrace Operator версии от 0.11.2 до 1.8.x, для применения профиля `RuntimeDefault` нужно явно включить этот флаг функции:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "true"
```

Чтобы отключить профиль seccomp для init-контейнера (в любой версии), установите флаг функции в `"false"`:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "false"
```

При значении `"false"` для init-контейнера профиль seccomp задан не будет, вместо этого будет использоваться поведение контейнерного runtime по умолчанию.