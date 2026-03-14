---
title: Поддерживаемые дистрибутивы
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/supported-technologies
scraped: 2026-03-05T21:26:22.993785
---

# Поддерживаемые дистрибутивы

# Поддерживаемые дистрибутивы

* Последняя версия Dynatrace
* Чтение: 6 мин
* Обновлено 7 сентября 2023 г.

На этой странице представлен обзор и описаны различные конфигурации для всех основных дистрибутивов Kubernetes.

Общую информацию о жизненном цикле поддержки Dynatrace для Kubernetes и Red Hat OpenShift, включая текущие поддерживаемые версии, см. в разделе [Жизненный цикл поддержки Dynatrace для Kubernetes и Red Hat OpenShift full stack Monitoring](../../technology-support/support-model-and-issues.md "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы").

## AWS Elastic Kubernetes Service (EKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для EKS не требуется специальная конфигурация.

Dynatrace поддерживает различные варианты AWS EKS. Для EKS на EC2 или bare metal вы можете установить Dynatrace в [любом доступном варианте развёртывания](#installation-k8s) без дополнительных изменений конфигурации. Для EKS на Fargate вы можете [установить Dynatrace для наблюдаемости приложений](../../amazon-web-services/integrate-into-aws/aws-fargate.md "Установка OneAgent на AWS Fargate.").

### AWS Bottlerocket OS

applicationMonitoring

Для AWS Bottlerocket OS на узлах EKS требуется дополнительная конфигурация.
Вы можете развернуть Dynatrace для наблюдаемости приложений и настроить наблюдаемость платформы через ActiveGate (мониторинг API Kubernetes). Наблюдаемость платформы через Dynatrace OneAgent не поддерживается. Начиная с версии Dynatrace Operator 0.12.0 и до версии Dynatrace Operator 1.7.0 поддерживается CSI-драйвер, который необходимо настроить в [режиме только для чтения для Bottlerocket OS](../guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume.md "Настройка томов CSI только для чтения для инъекции OneAgent с целью повышения безопасности данных."):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



feature.dynatrace.com/injection-readonly-volume: "true"



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- kubernetes-monitoring



- dynatrace-api



...
```

## Azure Kubernetes Service (AKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для AKS не требуется специальная конфигурация.

## Google Kubernetes Engine (GKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для GKE не требуется специальная конфигурация.

### GKE Standard и Anthos

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Если вы развёртываете Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI-драйвера Dynatrace Operator, требуется дополнительная конфигурация. Включите хранилище томов для OneAgent, установив переменную среды `ONEAGENT_ENABLE_VOLUME_STORAGE`:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



...
```

### GKE Autopilot

applicationMonitoring

Для GKE Autopilot вы можете [установить Dynatrace для наблюдаемости приложений](application-observability.md "Развёртывание Dynatrace Operator в режиме мониторинга приложений в Kubernetes"). CSI-драйвер Dynatrace Operator поддерживается для всех кластеров GKE Autopilot с Kubernetes версии 1.26+. Кроме того, поддерживаются только образы из следующих репозиториев, которые необходимо указать при установке:

* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`
* `docker.io/dynatrace/dynatrace-operator`
* `public.ecr.aws/dynatrace/dynatrace-operator`

Standalone LogMonitoring на GKE Autopilot полностью поддерживается начиная с версии Dynatrace Operator 1.4.2 со следующими поддерживаемыми источниками репозиториев:

* `docker.io/dynatrace/dynatrace-logmodule`
* `public.ecr.aws/dynatrace/dynatrace-logmodule`

#### Разрешение рабочих нагрузок Dynatrace

CSI driver Standalone LogMonitoring

Начиная с версии GKE Autopilot 1.32.1-gke.1376000 ресурс `WorkloadAllowlist` явно разрешает исключения безопасности (например, позволяет CSI-драйверу Dynatrace Operator запускать привилегированные рабочие нагрузки).
Dynatrace работает совместно с Google для своевременного выпуска этих `WorkloadAllowlist` для каждого релиза.

Дополнительные сведения о процессе можно найти в официальной [документации Google Cloud](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

Развёртывание и управление AllowlistSynchronizer будет автоматизировано в Dynatrace Operator версии 1.5.0+. Для версий 1.4.1 - 1.4.X вам потребуется применить такой манифест самостоятельно.

##### AllowlistSynchronizer для версии 1.4.2:

```
apiVersion: auto.gke.io/v1



kind: AllowlistSynchronizer



metadata:



name: allowlist-synchronizer-dynatrace



spec:



allowlistPaths:



- Dynatrace/csidriver/1.4.2/*



- Dynatrace/logmonitoring/1.4.2/*
```

Примените `AllowlistSynchronizer`:

```
kubectl apply -f allowlist-synchronizer-dynatrace.yaml
```

Версии v1.3.2 и более ранние

CSI driver

В зависимости от варианта развёртывания образ может быть указан различными способами.

#### Helm

Установите значение `image` в вашем `values.yaml` для Helm, указав один из поддерживаемых репозиториев при установке.

```
--set image=gcr.io/dynatrace-marketplace-prod/dynatrace-operator:v1.3.2
```

```
--set image=docker.io/dynatrace/dynatrace-operator:v1.3.2
```

#### Манифесты

1. Вместо применения манифеста необходимо загрузить манифесты (`kubernetes-csi.yaml`) со [страницы релизов](https://github.com/Dynatrace/dynatrace-operator/releases).
2. Замените значение `public.ecr.aws/dynatrace/dynatrace-operator` в полях image на `docker.io/dynatrace/dynatrace-operator`.
3. Примените изменённый манифест. Используйте соответствующий файл в зависимости от того, хотите ли вы использовать CSI-драйвер.

   ```
   kubectl apply -f kubernetes-csi.yaml
   ```

## Red Hat OpenShift

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Classic full-stack поддерживается только на узлах Kubernetes, использующих Red Hat Enterprise Linux (RHEL) в качестве операционной системы.

Для OpenShift необходимо [настроить Security Context Constraints (SCC)](../guides/networking-security-compliance/security-configurations/openshift-configuration.md "Настройка Dynatrace Operator в средах OpenShift.") для всех развёртываний, использующих CSI-драйвер Dynatrace Operator (`cloudNativeFullStack`, `applicationMonitoring`/`hostMonitoring` с CSI). Кроме того, начиная с OpenShift 4.13, необходимо [настроить плагин допуска CSI Inline Ephemeral Volume](../guides/networking-security-compliance/security-configurations/openshift-configuration.md "Настройка Dynatrace Operator в средах OpenShift.").

Для управляемых реализаций OpenShift, таких как AWS ROSA и Azure Red Hat OpenShift (ARO), Dynatrace поддерживает те же функции, что и для выделенного OpenShift.

Для OpenShift Dedicated требуется [роль cluster-admin](https://dt-url.net/a2038v8).

## Rancher Kubernetes Engine 1 (RKE1)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для RKE1 не требуется специальная конфигурация.

## Rancher Kubernetes Engine 2 (RKE2)

applicationMonitoring

Для RKE2 не требуется специальная конфигурация при использовании режима `applicationMonitoring`. Из-за политик SELinux на производных Red Hat Enterprise Linux режимы `hostMonitoring`, `cloudNativeFullStack` и `classicFullStack` не поддерживаются.

## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для TKGI требуются дополнительные конфигурации среды для всех режимов развёртывания, кроме `applicationMonitoring` без CSI-драйвера Dynatrace Operator.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI-драйвером) и `hostMonitoring`

В `values.yaml` для этих режимов требуется дополнительная конфигурация CSI-драйвера:

```
csidriver:



enabled: true



kubeletPath: "/var/vcap/data/kubelet"
```

### `classicFullStack`

Требуются образы из встроенного реестра Dynatrace, а не из публичного реестра. Используйте следующую конфигурацию:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /var/vcap/store
```

## IBM Kubernetes Service (IKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для IKS требуются дополнительные конфигурации среды для всех режимов развёртывания, кроме `applicationMonitoring` без CSI-драйвера.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI-драйвером) и `hostMonitoring`

Для этих режимов требуется дополнительная конфигурация CSI-драйвера:

```
csidriver:



enabled: true



kubeletPath: "/var/data/kubelet"
```

### `classicFullStack`

Требуются образы из встроенного реестра Dynatrace, а не из публичного реестра. Используйте следующую конфигурацию:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /opt
```

## SUSE Container as a Service (CaaS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Если вы развёртываете Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI-драйвера, обязательно настройте хранилище томов для OneAgent:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack: # измените на `hostMonitoring` при необходимости



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"
```

## Nutanix Kubernetes Platform (NKP, ранее D2iQ Konvoy)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная конфигурация не требуется.

## Oracle Kubernetes Engine (OKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная конфигурация не требуется.

## Mirantis Kubernetes Engine

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная конфигурация не требуется.