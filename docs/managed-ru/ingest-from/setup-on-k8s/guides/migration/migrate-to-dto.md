---
title: Миграция с OneAgent Operator на Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto
scraped: 2026-05-12T12:08:58.025839
---

# Миграция с OneAgent Operator на Dynatrace Operator

# Миграция с OneAgent Operator на Dynatrace Operator

* Чтение: 5 мин
* Опубликовано 1 апреля 2021 г.

## Описание и настройка пользовательского ресурса DynaKube

Пользовательский ресурс DynaKube (CR) заменяет пользовательский ресурс OneAgent. Ресурс DynaKube CR следует принципу "don't repeat yourself" (DRY) для развёртывания ряда различных компонентов в вашем кластере Kubernetes.

Каждый раздел содержит иллюстрацию различий между двумя пользовательскими ресурсами: что меняется при переходе от старого пользовательского ресурса к новому (отмечено зелёным) и что остаётся неизменным в обоих пользовательских ресурсах (отмечено синим).

Смена операторов изменит вычисление идентификаторов хостов для отслеживаемых хостов, что приведёт к аномалиям мониторинга в интерфейсе Dynatrace.

### Миграция классического full-stack

Следуйте приведённым ниже инструкциям, чтобы выполнить миграцию с OneAgent Operator на Dynatrace Operator для классического внедрения full-stack.

![Migration of properties](https://dt-cdn.net/images/classicfullstackmigration-600-fb8529d001.png)

Миграция свойств

Что остаётся неизменным

Что меняется

**Глобальные параметры (`spec`)**  
Следующие настройки являются глобальными, общими для всех компонентов и находятся в `spec`.

* `apiUrl`
* `tokens`[1](#fn-1-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Токены должны указывать на существующий секрет.**

**Параметры ClassicFullStack (`.spec.oneAgent.classicFullStack`)**  
Новый раздел для full-stack OneAgent находится в `.spec.oneAgent.classicFullStack`:

* `image`
* ~~`autoUpdate`~~[1](#fn-2-1-def)
* `version`[2](#fn-2-2-def)

1

Ранее это был `disableAgentUpdate` в OneAgent CR.  
Поле `autoUpdate` было удалено. [Закрепите версию OneAgent в вашем тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").  
Автообновление отключается, если задано поле `version` или `image`.

2

Это был `agentVersion` в OneAgent CR.

Все остальные параметры OneAgent (такие как tolerations, аргументы, DNS и настройки ресурсов) также находятся в разделе `.spec.oneAgent.classicFullStack` и уникальны для установки full-stack.

### Миграция только приложений

Следуйте приведённым ниже инструкциям, чтобы выполнить миграцию с OneAgent Operator на Dynatrace Operator для автоматического внедрения только в приложения.

![Cloud native app only](https://dt-cdn.net/images/cloudnativeappo-600-de0c984048.png)

Только приложения (cloud-native)

Что остаётся неизменным

Что меняется

**Глобальные параметры (`spec`)**  
Следующие настройки являются глобальными, общими для всех компонентов и находятся в `spec`.

* `apiUrl`
* `tokens`[1](#fn-3-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Токены должны указывать на существующий секрет.**

**Параметры ApplicationMonitoring (`.spec.oneAgent.applicationMonitoring`)**  
Новый раздел для full-stack OneAgent находится в `.spec.oneAgent.applicationMonitoring`:

* `version`[1](#fn-4-1-def)
* `useCSIDriver`[2](#fn-4-2-def)

1

Это был `agentVersion` в OneAgent CR.

2

Этот новый параметр будет автоматически доставлять двоичные файлы в поды и устранит требования к хранилищу на подах. Доступен только в режиме предварительного просмотра, по умолчанию `false`.

Параметр `image` больше недоступен. Эта функциональность будет восстановлена в будущем. На данный момент все поды загружаются из API URL.

## Миграция с OneAgent Operator на Dynatrace Operator

Можно выполнить миграцию с устаревшего OneAgent Operator на новый Dynatrace Operator, который управляет жизненным циклом нескольких компонентов Dynatrace, таких как OneAgent, маршрутизация и Kubernetes API Monitor. По мере появления новых возможностей наблюдаемости будут добавляться дополнительные компоненты.

Выберите **один из следующих вариантов** в зависимости от методов развёртывания.

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Миграция манифестов

Kubernetes

OpenShift

1. Удалите OneAgent Operator и пространство имён/проект `dynatrace`.

   ```
   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/kubernetes.yaml



   kubectl delete namespace dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").

1. Удалите OneAgent Operator и пространство имён/проект `dynatrace`.

   ```
   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/openshift.yaml



   oc delete project dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").

### Миграция с помощью Helm

Kubernetes

OpenShift

1. Удалите OneAgent Operator, репозиторий Helm и пространство имён/проект `dynatrace`.

   ```
   helm uninstall dynatrace-oneagent-operator



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   kubectl delete namespace dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").

1. Удалите OneAgent Operator, репозиторий Helm и пространство имён/проект `dynatrace`.

   ```
   helm uninstall dynatrace-oneagent-operator



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   oc delete project dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").