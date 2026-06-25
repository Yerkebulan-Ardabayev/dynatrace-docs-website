---
title: Поддерживаемые дистрибутивы
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/supported-technologies
scraped: 2026-05-12T11:23:15.589141
---

# Поддерживаемые дистрибутивы

# Поддерживаемые дистрибутивы

* Чтение: 6 мин
* Обновлено 19 февраля 2026 г.

На этой странице приведён обзор и описаны различные конфигурации для всех основных дистрибутивов Kubernetes.

Полный жизненный цикл поддержки Dynatrace для Kubernetes и Red Hat OpenShift, включая текущие поддерживаемые версии, см. в разделе [Жизненный цикл поддержки Dynatrace для full stack мониторинга Kubernetes и Red Hat OpenShift](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы").

## AWS Elastic Kubernetes Service (EKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для EKS специальная конфигурация не требуется.

Dynatrace поддерживает множество различных разновидностей AWS EKS. Для EKS на EC2 или bare metal можно установить Dynatrace с [любым доступным вариантом развёртывания](#installation-k8s) без каких-либо дополнительных изменений конфигурации. Для EKS на Fargate можно [установить Dynatrace for App Observability](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.").

### AWS Bottlerocket OS

applicationMonitoring

Для AWS Bottlerocket OS на узлах EKS требуется дополнительная настройка.
Можно развернуть Dynatrace for Application Observability и настроить Platform Observability через ActiveGate (Kubernetes API Monitoring). Platform Observability через Dynatrace OneAgent не поддерживается. Начиная с версии Dynatrace Operator 0.12.0 и до версии Dynatrace Operator 1.7.0 CSI driver поддерживается и должен быть настроен в [режиме только для чтения для Bottlerocket OS](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume "Настройте тома CSI только для чтения для инъекции OneAgent, чтобы повысить безопасность данных."):

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

Для AKS специальная конфигурация не требуется.

## Google Kubernetes Engine (GKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для GKE специальная конфигурация не требуется.

### GKE Standard & Anthos

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Если вы развёртываете Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI driver Dynatrace Operator, требуется дополнительная настройка. Включите хранение на томе для OneAgent, задав переменную окружения `ONEAGENT_ENABLE_VOLUME_STORAGE`:

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

Для GKE Autopilot можно [установить Dynatrace for App Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Разверните Dynatrace Operator в режиме application monitoring в Kubernetes"). CSI driver Dynatrace Operator поддерживается для всех кластеров GKE Autopilot с версией Kubernetes 1.26+. Кроме того, поддерживаются только образы из следующих репозиториев, и они должны быть указаны во время установки:

* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`
* `docker.io/dynatrace/dynatrace-operator`
* `public.ecr.aws/dynatrace/dynatrace-operator`

Standalone LogMonitoring на GKE Autopilot полностью поддерживается начиная с версии Dynatrace Operator 1.4.2 со следующей поддержкой источников-репозиториев:

* `docker.io/dynatrace/dynatrace-logmodule`
* `public.ecr.aws/dynatrace/dynatrace-logmodule`

#### Добавление нагрузок Dynatrace в список разрешённых

CSI driver Standalone LogMonitoring

Начиная с версии GKE Autopilot 1.32.1-gke.1376000, `WorkloadAllowlist` явно разрешает исключения безопасности (например, позволяя CSI driver Dynatrace Operator запускать привилегированные нагрузки).
Dynatrace работает с Google над своевременным развёртыванием этих `WorkloadAllowlists` для каждого выпуска.

Дополнительные сведения о процессе можно найти в официальной [документации Google Cloud](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

Развёртывание и управление AllowlistSynchronizer будет автоматизировано в версии Dynatrace Operator 1.5.0+. Для версий 1.4.1 - 1.4.X такой манифест придётся применять самостоятельно.

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

v1.3.2 и более ранние версии

CSI driver

В зависимости от варианта развёртывания образ можно задать разными способами.

#### Helm

Задайте значение `image` в вашем helm `values.yaml` равным одному из поддерживаемых репозиториев во время установки.

```
--set image=gcr.io/dynatrace-marketplace-prod/dynatrace-operator:v1.3.2
```

```
--set image=docker.io/dynatrace/dynatrace-operator:v1.3.2
```

#### Манифесты

1. Вместо применения манифеста манифесты (`kubernetes-csi.yaml`) нужно загрузить со [страницы выпусков](https://github.com/Dynatrace/dynatrace-operator/releases).
2. Замените значение `public.ecr.aws/dynatrace/dynatrace-operator` в полях image на `docker.io/dynatrace/dynatrace-operator`.
3. Примените изменённый манифест. Используйте подходящий в зависимости от того, нужен CSI driver или нет.

   ```
   kubectl apply -f kubernetes-csi.yaml
   ```

## Red Hat OpenShift

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Classic full-stack поддерживается только на узлах Kubernetes, использующих Red Hat Enterprise Linux (RHEL) в качестве операционной системы.

Для OpenShift необходимо [настроить Security Context Constraints (SCC)](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.") для всех развёртываний, использующих CSI driver Dynatrace Operator (`cloudNativeFullStack`, `applicationMonitoring`/`hostMonitoring` с CSI). Кроме того, начиная с Openshift 4.13, необходимо [настроить плагин CSI Inline Ephemeral Volume Admission](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Настройка Dynatrace Operator в окружениях OpenShift.").

Для управляемых реализаций OpenShift, таких как AWS ROSA и Azure Red Hat OpenShift (ARO), Dynatrace поддерживает те же функции, что и для выделенного OpenShift.

Для OpenShift Dedicated необходима [роль cluster-admin](https://dt-url.net/a2038v8).

## Rancher Kubernetes Engine 2 (RKE2)

applicationMonitoring

При использовании режима `applicationMonitoring` для RKE2 специальная конфигурация не требуется. Из-за политик SELinux на производных Red Hat Enterprise Linux режимы `hostMonitoring`, `cloudNativeFullStack` и `classicFullStack` не поддерживаются.

## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для TKGI требуются дополнительные настройки окружения для всех режимов развёртывания, кроме `applicationMonitoring` без CSI driver Dynatrace Operator.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI driver) и `hostMonitoring`

В `values.yaml` для этих режимов требуется дополнительная настройка для конфигурации CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/vcap/data/kubelet"
```

### `classicFullStack`

Требует образов из встроенного реестра Dynatrace, а не из публичного реестра. Используйте следующую конфигурацию:

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

Для IKS требуются дополнительные настройки окружения для всех режимов развёртывания, кроме `applicationMonitoring` без CSI driver.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI driver) и `hostMonitoring`

Для этих режимов требуется дополнительная настройка для конфигурации CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/data/kubelet"
```

### `classicFullStack`

Требует образов из встроенного реестра Dynatrace, а не из публичного реестра. Используйте следующую конфигурацию:

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

Если вы развёртываете Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI driver, обязательно настройте хранение на томе для OneAgent:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack: # change to `hostMonitoring` if needed



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