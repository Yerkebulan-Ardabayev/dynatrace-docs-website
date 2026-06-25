---
title: Включение AppArmor для повышения безопасности
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor
scraped: 2026-05-12T12:14:30.813706
---

# Включение AppArmor для повышения безопасности

# Включение AppArmor для повышения безопасности

* Чтение: 2 мин
* Обновлено 9 марта 2026 г.

Сделать Dynatrace Operator более безопасным можно, включив [AppArmor](https://dt-url.net/3403y6b).

## Включение AppArmor для Dynatrace Operator, Webhook и CSI driver

В зависимости от того, развернули ли вы Dynatrace Operator с помощью **Helm** или путём прямого применения **манифестов YAML**.

Helm

Manifest

Изменения настройки AppArmor в Kubernetes 1.31+

Начиная с версии Kubernetes 1.31 профили AppArmor настраиваются с помощью `securityContext.appArmorProfile` вместо аннотаций подов. Прежние значения Helm `operator.apparmor`, `webhook.apparmor` и `csidriver.apparmor` устарели. Вместо них используйте значения `appArmorProfile`, показанные ниже. Устаревшие значения поддерживаются, пока Kubernetes 1.30 и OpenShift 4.17 не достигнут окончания поддержки (июль 2027 г.).

Добавьте поле `appArmorProfile` в `podSecurityContext` в вашем `values.yaml`, чтобы включить AppArmor для Dynatrace Operator и Webhook:

```
operator:



podSecurityContext:



appArmorProfile:



type: RuntimeDefault



webhook:



podSecurityContext:



appArmorProfile:



type: RuntimeDefault
```

Для **CSI driver** задайте `appArmorProfile` в `securityContext` каждого контейнера по отдельности:

```
csidriver:



csiInit:



securityContext:



appArmorProfile:



type: RuntimeDefault



server:



securityContext:



appArmorProfile:



type: RuntimeDefault



provisioner:



securityContext:



appArmorProfile:



type: RuntimeDefault



registrar:



securityContext:



appArmorProfile:



type: RuntimeDefault



livenessprobe:



securityContext:



appArmorProfile:



type: RuntimeDefault
```

В Kubernetes версии 1.31+ профили AppArmor настраиваются с помощью `securityContext.appArmorProfile` вместо аннотаций подов.

Прекращение поддержки аннотации подов AppArmor

В Kubernetes версии 1.30 и более ранних AppArmor настраивался с помощью аннотации подов `container.apparmor.security.beta.kubernetes.io/<container-name>: runtime/default`. Этот подход устарел. Вместо него используйте `securityContext.appArmorProfile`, который изначально поддерживается в Kubernetes версии 1.31+.

* **Dynatrace Operator и Webhook** требуют обновления `securityContext` в YAML развёртывания:

  ```
  kind: Deployment



  metadata:



  name: dynatrace-webhook



  spec:



  template:



  spec:



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  kind: Deployment



  metadata:



  name: dynatrace-operator



  spec:



  template:



  spec:



  securityContext:



  appArmorProfile:



  type: RuntimeDefault
  ```
* **CSI driver** требует задания `appArmorProfile` в `securityContext` каждого контейнера в DaemonSet:

  ```
  kind: DaemonSet



  metadata:



  name: dynatrace-oneagent-csi-driver



  spec:



  template:



  spec:



  initContainers:



  - name: csi-init



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  containers:



  - name: server



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: provisioner



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: registrar



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: liveness-probe



  securityContext:



  appArmorProfile:



  type: RuntimeDefault
  ```

## Включение AppArmor для компонентов, развёрнутых оператором

Чтобы включить AppArmor для компонентов, которые Dynatrace Operator развёртывает в отслеживаемые кластеры, необходимо подключить его для каждого компонента отдельно.

### ActiveGate

В Kubernetes 1.31+ AppArmor настраивается через `securityContext`. На более старых кластерах вместо этого используется аннотация. Оператор автоматически выбирает подходящий метод в зависимости от версии кластера. Чтобы подключить его, добавьте в ваш DynaKube следующую аннотацию:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/activegate-apparmor: true
```

### OneAgent

В Kubernetes 1.31+ оператор автоматически применяет AppArmor через `securityContext`, действий со стороны пользователя не требуется. В Kubernetes 1.30 и более ранних AppArmor для OneAgent не применяется автоматически. Чтобы использовать пользовательский профиль AppArmor на более старых кластерах, см. [Включение пользовательского профиля AppArmor для OneAgent](#custom-apparmor).

### EdgeConnect

Чтобы включить AppArmor для EdgeConnect, добавьте аннотацию AppArmor через поле DynaKube `spec.edgeConnect.annotations`:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



edgeConnect:



annotations:



container.apparmor.security.beta.kubernetes.io/edge-connect: runtime/default
```

Аннотация `container.apparmor.security.beta.kubernetes.io` устарела в Kubernetes 1.30 и удалена в Kubernetes 1.31. В Kubernetes 1.31+ эта аннотация не действует для EdgeConnect. Настройка AppArmor для EdgeConnect на основе `securityContext` пока не поддерживается.

### Включение пользовательского профиля AppArmor для OneAgent

Доступ OneAgent можно ограничить нужным набором функций. Ниже описано, как включить пользовательский профиль AppArmor и применить его к подам OneAgent.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание пользовательского профиля AppArmor для OneAgent**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#create-profile "Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Установка профиля на все рабочие узлы**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#install-profile "Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Принудительное применение профиля ко всем подам OneAgent**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#enforce-profile "Применение профилей AppArmor к компонентам Dynatrace для повышения безопасности.")

#### Шаг 1. Создание пользовательского профиля AppArmor для OneAgent

Подробнее о том, как создать пользовательский профиль AppArmor, см. [Запуск OneAgent как контейнера Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#with-apparmor "Установка и обновление Dynatrace OneAgent как контейнера Docker.").

#### Шаг 2. Установка профиля на все рабочие узлы

OneAgent по умолчанию развёртывается как daemonset, что означает, что поды, использующие профиль AppArmor, будут задействованы на каждом узле. Поэтому профиль AppArmor для OneAgent необходимо установить **на всех узлах**.

В зависимости от окружения это можно сделать несколькими способами, например с помощью [kube-apparmor-manager](https://dt-url.net/5g034s7) или [security-profiles-operator](https://dt-url.net/uz23475). О том, как применять эти инструменты в вашем кластере, см. их официальную документацию.

#### Шаг 3. Принудительное применение профиля ко всем подам OneAgent

Чтобы включить AppArmor для всех подов OneAgent, добавьте аннотацию `container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent` в одно из следующих полей в зависимости от вашего развёртывания:

* `oneAgent.classicFullStack.annotations`
* `oneAgent.cloudNativeFullStack.annotations`
* `oneAgent.hostMonitoring.annotations`

Пример для развёртывания `cloudNativeFullStack`:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack:



annotations:



container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent
```