---
title: Поддерживаемые дистрибутивы
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/supported-technologies
---

# Поддерживаемые дистрибутивы

# Поддерживаемые дистрибутивы

* 6 мин чтения
* Обновлено 24 июн 2026

Эта страница дает обзор и описывает различные конфигурации для всех основных дистрибутивов Kubernetes.

Общий жизненный цикл поддержки Dynatrace для Kubernetes и Red Hat OpenShift, включая текущие поддерживаемые версии, описан в разделе [Жизненный цикл поддержки Dynatrace для Kubernetes и Red Hat OpenShift full stack Monitoring](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

## AWS Elastic Kubernetes Service (EKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для EKS специальная конфигурация не требуется.

Dynatrace поддерживает разные варианты AWS EKS. Для EKS на EC2 или bare metal можно установить Dynatrace в [любом доступном варианте развертывания](#installation-k8s) без дополнительных изменений конфигурации. Для EKS на Fargate можно [установить Dynatrace для App Observability](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.").

### AWS Bottlerocket OS

applicationMonitoring

Для AWS Bottlerocket OS на узлах EKS требуется дополнительная конфигурация.
Можно развернуть Dynatrace для Application Observability и настроить Platform Observability через ActiveGate (Kubernetes API Monitoring). Platform Observability через Dynatrace OneAgent не поддерживается. Начиная с версии Dynatrace Operator 0.12.0 и до версии Dynatrace Operator 1.7.0, поддерживается CSI driver, который нужно настроить в [режиме только для чтения для Bottlerocket OS](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume "Configure read-only CSI volumes for OneAgent injection to enhance data security."):

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

### AKS admissions enforcer

applicationMonitoring cloudNativeFullStack

Внедрение code module пропускается в пространствах имен, управляемых AKS, потому что AKS admissions enforcer добавляет выражения `namespaceSelector` к каждому `MutatingWebhookConfiguration` и `ValidatingWebhookCOnfiguration`, которые явно исключают пространства имен с меткой `kubernetes.azure.com/managedby: aks`.

```
- key: control-plane



operator: NotIn



values: ["true"]



- key: kubernetes.azure.com/managedby



operator: NotIn



values: ["aks"]
```

Поскольку webhook Dynatrace Operator поставляется только с `dynakube.internal.dynatrace.com/instance: Exists` в своем namespace selector, любое пространство имен с меткой `kubernetes.azure.com/managedby: aks` исключается из внедрения после того, как enforcer изменяет конфигурацию webhook.

Чтобы проверить, изменил ли admissions enforcer конфигурацию webhook Dynatrace, выполнить:

```
kubectl get mutatingwebhookconfiguration dynatrace-webhook -o yaml
```

Если enforcer отработал, в выводе будут дополнительные записи в `namespaceSelector.matchExpressions` для `control-plane` и `kubernetes.azure.com/managedby`.

Если требуется внедрение в пространство имен с меткой `kubernetes.azure.com/managedby: aks`, нужно снабдить `MutatingWebhookConfiguration` аннотацией, чтобы вывести его из-под действия enforcer:

```
kubectl annotate mutatingwebhookconfiguration dynatrace-webhook \



admissions.enforcer/disabled=true
```

Аннотация не удаляет селекторы, которые enforcer уже добавил. Записи `control-plane` и `kubernetes.azure.com/managedby` нужно удалить из `namespaceSelector.matchExpressions` в `mutatingwebhookconfiguration` вручную.

Если Dynatrace Operator заново создает `MutatingWebhookConfiguration`, например после обновления оператора, аннотация `admissions.enforcer/disabled=true` теряется. При этом webhook Dynatrace никогда не блокирует планирование подов: если он недоступен, Kubernetes проигнорирует сбой и запланирует поды как обычно. Подробности см. в [AKS FAQ﻿](https://learn.microsoft.com/azure/aks/faq).

## Google Kubernetes Engine (GKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для GKE специальная конфигурация не требуется.

### GKE Standard & Anthos

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

При развертывании Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI driver Dynatrace Operator требуется дополнительная конфигурация. Нужно включить volume storage для OneAgent, задав переменную окружения `ONEAGENT_ENABLE_VOLUME_STORAGE`:

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

Для GKE Autopilot можно [установить Dynatrace для App Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"). CSI driver Dynatrace Operator поддерживается для всех кластеров GKE Autopilot с версией Kubernetes 1.26+. Кроме того, поддерживаются только образы из следующих репозиториев, которые нужно указать при установке:

* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`
* `docker.io/dynatrace/dynatrace-operator`
* `public.ecr.aws/dynatrace/dynatrace-operator`

**Code modules**: на GKE Autopilot с CSI driver Dynatrace Operator и включенной функцией [node image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") для Application observability параметр `codeModulesImage` в DynaKube должен ссылаться на один из следующих репозиториев:

* `docker.io/dynatrace/dynatrace-codemodules`
* `public.ecr.aws/dynatrace/dynatrace-codemodules`

**Standalone log monitoring**: полностью поддерживается на GKE Autopilot начиная с версии Dynatrace Operator 1.4.2, из следующих репозиториев:

* `docker.io/dynatrace/dynatrace-logmodule`
* `public.ecr.aws/dynatrace/dynatrace-logmodule`

#### Внесение рабочих нагрузок Dynatrace в allowlist

CSI driver Standalone LogMonitoring

Начиная с версии GKE Autopilot 1.32.1-gke.1376000, `WorkloadAllowlist` явно разрешает исключения безопасности (например, позволяет CSI driver Dynatrace Operator запускать привилегированные рабочие нагрузки).
Dynatrace совместно с Google своевременно раскатывает эти `WorkloadAllowlists` для каждого релиза.

Подробности процесса можно найти в официальной документации [Google Cloud﻿](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

Развертывание и управление AllowlistSynchronizer будет автоматизировано в версии Dynatrace Operator 1.5.0+. Для версий 1.4.1 - 1.4.X такой манифест нужно применять самостоятельно.

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

Применить `AllowlistSynchronizer`:

```
kubectl apply -f allowlist-synchronizer-dynatrace.yaml
```

Версия 1.3.2 и более ранние версии

CSI driver

В зависимости от варианта развертывания образ можно задать разными способами.

#### Helm

Во время установки задать значение `image` в файле `values.yaml` helm, указав один из поддерживаемых репозиториев.

```
--set image=gcr.io/dynatrace-marketplace-prod/dynatrace-operator:v1.3.2
```

```
--set image=docker.io/dynatrace/dynatrace-operator:v1.3.2
```

#### Манифесты

1. Вместо применения манифеста нужно скачать манифесты (`kubernetes-csi.yaml`) со [страницы релиза﻿](https://github.com/Dynatrace/dynatrace-operator/releases).
2. Заменить значение `public.ecr.aws/dynatrace/dynatrace-operator` в полях image на `docker.io/dynatrace/dynatrace-operator`.
3. Применить измененный манифест. Использовать подходящий вариант в зависимости от того, нужен CSI driver или нет.

   ```
   kubectl apply -f kubernetes-csi.yaml
   ```

## Red Hat OpenShift

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Classic full-stack поддерживается только на узлах Kubernetes, использующих Red Hat Enterprise Linux (RHEL) в качестве операционной системы.

Для OpenShift нужно [настроить Security Context Constraints (SCC)](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.") для всех развёртываний, использующих CSI-драйвер Dynatrace Operator (`cloudNativeFullStack`, `applicationMonitoring`/`hostMonitoring` с CSI). Кроме того, начиная с Openshift 4.13, нужно [настроить плагин CSI Inline Ephemeral Volume Admissing](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.").

Для управляемых реализаций OpenShift, таких как AWS ROSA и Azure Red Hat OpenShift (ARO), Dynatrace поддерживает те же функции, что и для выделенного OpenShift.

Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://dt-url.net/a2038v8).

## Rancher Kubernetes Engine 2 (RKE2)

applicationMonitoring

Для RKE2 при использовании режима `applicationMonitoring` специальная настройка не требуется. Из-за политик SELinux в производных Red Hat Enterprise Linux режимы `hostMonitoring`, `cloudNativeFullStack` и `classicFullStack` не поддерживаются.

## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Для TKGI дополнительная настройка окружения требуется для всех режимов развёртывания, кроме `applicationMonitoring` без CSI-драйвера Dynatrace Operator.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI-драйвером) и `hostMonitoring`

В `values.yaml` для этих режимов требуется дополнительная настройка для конфигурации CSI-драйвера:

```
csidriver:



enabled: true



kubeletPath: "/var/vcap/data/kubelet"
```

### `classicFullStack`

Требуются образы из встроенного реестра Dynatrace, а не из публичного реестра. Используй следующую конфигурацию:

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

Для IKS дополнительная настройка окружения требуется для всех режимов развёртывания, кроме `applicationMonitoring` без CSI-драйвера.

### `cloudNativeFullStack`, `applicationMonitoring` (с CSI-драйвером) и `hostMonitoring`

Для этих режимов требуется дополнительная настройка для конфигурации CSI-драйвера:

```
csidriver:



enabled: true



kubeletPath: "/var/data/kubelet"
```

### `classicFullStack`

Требуются образы из встроенного реестра Dynatrace, а не из публичного реестра. Используй следующую конфигурацию:

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

При развёртывании Dynatrace в режиме `classicFullStack` или `hostMonitoring` без CSI-драйвера обязательно настрой хранилище томов для OneAgent:

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

## Nutanix Kubernetes Platform (NKP, former D2iQ Konvoy)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная настройка не требуется.

## Oracle Kubernetes Engine (OKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная настройка не требуется.

## Mirantis Kubernetes Engine

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Специальная настройка не требуется.