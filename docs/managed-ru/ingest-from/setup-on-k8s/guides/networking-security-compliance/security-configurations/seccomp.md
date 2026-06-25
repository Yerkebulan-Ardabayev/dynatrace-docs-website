---
title: Профили seccomp
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp
scraped: 2026-05-12T12:14:28.798329
---

# Профили seccomp

# Профили seccomp

* Пояснение
* Чтение: 5 мин
* Опубликовано 24 марта 2026 г.

## Что такое seccomp?

Seccomp (secure computing mode), это функция безопасности ядра Linux, которая ограничивает системные вызовы, которые разрешено выполнять процессу. Применяя профиль seccomp к контейнеру, вы ограничиваете, какие операции на уровне ядра он может выполнять, уменьшая поверхность атаки ваших рабочих нагрузок. Kubernetes поддерживает настройку профилей seccomp как на уровне пода, так и на уровне контейнера через поле `securityContext`, что делает её ключевым механизмом для соответствия стандартам безопасности, таким как Kubernetes [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

В Kubernetes есть три типа профилей seccomp:

* **RuntimeDefault**: встроенный профиль по умолчанию среды выполнения контейнеров. Он разрешает выверенный набор распространённых системных вызовов, блокируя потенциально опасные.
* **Localhost**: пользовательский профиль, загружаемый из JSON-файла в файловой системе узла.
* **Unconfined**: фильтрация seccomp не применяется, разрешены все системные вызовы.

Все инфраструктурные компоненты Dynatrace Operator (operator, webhook и CSI driver) и компоненты, развёртываемые оператором (ActiveGate, EdgeConnect), используют профиль seccomp `RuntimeDefault`. Исключением является OneAgent, который работает без ограничений (профиль seccomp не задан). Профиль `RuntimeDefault` подходит для большинства рабочих нагрузок и удовлетворяет стандарту **restricted** Pod Security Standard.

## Профиль seccomp для OneAgent

По умолчанию OneAgent работает без профиля seccomp (unconfined). Это значение по умолчанию было выбрано для обеспечения совместимости с самым широким набором платформ и сред выполнения контейнеров, поскольку OneAgent требует доступа к более широкому набору системных вызовов для глубокого мониторинга на уровне хоста.

### Настройка пользовательского профиля seccomp для OneAgent

Dynatrace Operator версии 1.2.0+

Если ваши политики безопасности требуют профиля seccomp для OneAgent, его можно настроить с помощью поля `secCompProfile` под соответствующим режимом OneAgent в вашем пользовательском ресурсе DynaKube.

**Ограничение:** профиль seccomp для OneAgent всегда применяется с типом `Localhost`. Это означает, что необходимо предоставить пользовательский JSON-файл профиля seccomp на каждом узле: задать тип `RuntimeDefault` или `Unconfined` через это поле нельзя.

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

Тип `Localhost` требует, чтобы JSON-файл профиля seccomp присутствовал в локальной файловой системе узла, в настроенном корневом каталоге профилей seccomp kubelet (по умолчанию `/var/lib/kubelet/seccomp/`). Для приведённых выше примеров файл профиля должен располагаться по пути `/var/lib/kubelet/seccomp/my-seccomp-profile.json` на каждом узле, где запланирован OneAgent.

О том, как создавать профили seccomp типа `Localhost` и управлять ими, см. документацию Kubernetes:

* [Restrict a Container's Syscalls with seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
* [Set the seccomp profile for a Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-seccomp-profile-for-a-container)

## Настройка seccomp для init-контейнера Dynatrace

Dynatrace Operator версии 0.11.2+

Профиль seccomp для init-контейнера Dynatrace (используемого для инъекции модуля кода) управляется флагом функции `feature.dynatrace.com/init-container-seccomp-profile`.

Начиная с версии Dynatrace Operator 1.9.0 значение этого флага функции по умолчанию изменилось с `"false"` на `"true"`. Это означает, что к init-контейнеру теперь по умолчанию применяется профиль seccomp `RuntimeDefault`, что помогает выполнить требования стандарта **restricted** Pod Security Standard для ваших отслеживаемых рабочих нагрузок Kubernetes.

Если вы используете Dynatrace Operator версий с 0.11.2 по 1.8.x, для применения профиля `RuntimeDefault` необходимо явно включить этот флаг функции:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "true"
```

Чтобы отключить профиль seccomp для init-контейнера (в любой версии), задайте для флага функции значение `"false"`:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "false"
```

При значении `"false"` для init-контейнера профиль seccomp не будет задан, и вместо этого будет использоваться поведение по умолчанию вашей среды выполнения контейнеров.