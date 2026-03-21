---
title: Миграция с OneAgent Operator на Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto
scraped: 2026-03-06T21:29:22.920771
---

* Latest Dynatrace
* 5-min read

## Понимание и настройка пользовательского ресурса DynaKube

Пользовательский ресурс (CR) DynaKube заменяет пользовательский ресурс OneAgent. CR DynaKube следует принципу «не повторяйся» (DRY) для развёртывания ряда различных компонентов в вашем кластере Kubernetes.

Каждый раздел включает иллюстрацию различий между двумя пользовательскими ресурсами, что меняется от старого пользовательского ресурса к новому (отмечено зелёным) и что остаётся одинаковым в обоих пользовательских ресурсах (отмечено синим).

Смена операторов изменит расчёт идентификаторов хостов для мониторируемых хостов, что приведёт к аномалиям мониторинга в интерфейсе Dynatrace.

### Миграция classic full-stack

Следуйте приведённым ниже инструкциям для миграции с OneAgent Operator на Dynatrace Operator для классической инъекции full-stack.

![Миграция свойств](https://dt-cdn.net/images/classicfullstackmigration-600-fb8529d001.png)

Что остаётся без изменений

Что меняется

**Глобальные параметры (`spec`)**
Следующие настройки являются глобальными, общими для каждого компонента, и расположены в разделе `spec`.

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
Новый раздел для full-stack OneAgent расположен в `.spec.oneAgent.classicFullStack`:

* `image`
* ~~`autoUpdate`~~[1](#fn-2-1-def)
* `version`[2](#fn-2-2-def)

1

Ранее это было `disableAgentUpdate` в CR OneAgent.
Поле `autoUpdate` было удалено. [Закрепите версию OneAgent на вашем тенанте для настройки автообновления](../deployment-and-configuration/updates-and-maintenance/auto-update-components.md#configure-oneagent-auto-update "Настройте автообновления для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).").
Автообновление отключается, если установлены поля `version` или `image`.

2

В CR OneAgent это было `agentVersion`.

Все остальные параметры OneAgent (такие как tolerations, аргументы, DNS и настройки ресурсов) также расположены в разделе `.spec.oneAgent.classicFullStack` и уникальны для установки full-stack.

### Миграция application-only

Следуйте приведённым ниже инструкциям для миграции с OneAgent Operator на Dynatrace Operator для автоматической инъекции application-only.

![Cloud native app only](https://dt-cdn.net/images/cloudnativeappo-600-de0c984048.png)

Что остаётся без изменений

Что меняется

**Глобальные параметры (`spec`)**
Следующие настройки являются глобальными, общими для каждого компонента, и расположены в разделе `spec`.

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
Новый раздел для full-stack OneAgent расположен в `.spec.oneAgent.applicationMonitoring`:

* `version`[1](#fn-4-1-def)
* `useCSIDriver`[2](#fn-4-2-def)

1

В CR OneAgent это было `agentVersion`.

2

Этот новый параметр будет автоматически доставлять бинарные файлы в поды и устранять требования к хранилищу на подах. Это доступно только в предварительной версии и по умолчанию установлено в `false`.

Параметр `image` больше недоступен. Функциональность будет повторно введена в будущем. На данный момент все поды загружаются с URL API.

## Миграция с OneAgent Operator на Dynatrace Operator

Вы можете мигрировать с устаревшего OneAgent Operator на новый Dynatrace Operator, который управляет жизненным циклом нескольких компонентов Dynatrace, таких как OneAgent, маршрутизация и Kubernetes API Monitor. Дополнительные компоненты будут добавляться по мере появления новых функций наблюдаемости.

Выберите **один из следующих вариантов** в зависимости от ваших методов развёртывания.

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
2. [Настройте мониторинг с помощью Dynatrace Operator](../../deployment.md "Разверните Dynatrace Operator в Kubernetes").

1. Удалите OneAgent Operator и пространство имён/проект `dynatrace`.

   ```
   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/openshift.yaml


   oc delete project dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](../../deployment.md "Разверните Dynatrace Operator в Kubernetes").

### Миграция с Helm

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
2. [Настройте мониторинг с помощью Dynatrace Operator](../../deployment.md "Разверните Dynatrace Operator в Kubernetes").

1. Удалите OneAgent Operator, репозиторий Helm и пространство имён/проект `dynatrace`.

   ```
   helm uninstall dynatrace-oneagent-operator


   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml


   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml


   helm repo remove dynatrace


   oc delete project dynatrace
   ```
2. [Настройте мониторинг с помощью Dynatrace Operator](../../deployment.md "Разверните Dynatrace Operator в Kubernetes").
