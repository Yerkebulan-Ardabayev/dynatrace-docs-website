---
title: Миграция с оператора OneAgent на оператор Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto
---

# Миграция с оператора OneAgent на оператор Dynatrace

# Миграция с оператора OneAgent на оператор Dynatrace

* 5 мин чтения
* Обновлено 09 июня 2026 г.

## Понимание и настройка пользовательского ресурса DynaKube

Пользовательский ресурс (CR) DynaKube заменяет пользовательский ресурс OneAgent. CR DynaKube следует принципу «don't repeat yourself» (DRY), чтобы разворачивать ряд различных компонентов в кластере Kubernetes.

В каждом разделе приведена иллюстрация различий между двумя пользовательскими ресурсами: что меняется при переходе от старого пользовательского ресурса к новому (отмечено зелёным) и что остаётся одинаковым в обоих пользовательских ресурсах (отмечено синим).

Смена операторов изменит расчёт host ID для отслеживаемых хостов, что приведёт к аномалиям мониторинга в интерфейсе Dynatrace.

### Миграция классического full-stack

Следуй инструкциям ниже, чтобы перейти с оператора OneAgent на оператор Dynatrace для классического full-stack внедрения.

![Migration of properties](https://cdn.bfldr.com/B686QPH3/as/wn4ggjs69gk6km4wqt6q4h2j/Migrate_from_OneAgent_Operator_to_Dynatrace_Operator-Classic_full-stack_migration-Light_Mode?auto=webp&format=png&position=1)

Миграция свойств

Что остаётся неизменным

Что меняется

**Глобальные параметры (`spec`)**  
Следующие настройки являются глобальными, общими для каждого компонента, и находятся в `spec`.

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

Раньше это было `disableAgentUpdate` в CR OneAgent.  
Поле `autoUpdate` удалено. [Закрепи версию OneAgent в своём тенанте, чтобы настроить автообновление](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Настройка автообновлений для всех компонентов, управляемых оператором Dynatrace").  
Автообновление отключается, если задано поле `version` или `image`.

2

В CR OneAgent это было `agentVersion`.

Все остальные параметры OneAgent (такие как tolerations, аргументы, DNS и настройки ресурсов) также находятся в разделе `.spec.oneAgent.classicFullStack` и уникальны для full-stack установки.

### Миграция только приложений (application-only)

Следуй инструкциям ниже, чтобы перейти с оператора OneAgent на оператор Dynatrace для автоматического внедрения только в приложения.

![Cloud native app only](https://cdn.bfldr.com/B686QPH3/as/qk8rt6xnq7rhnjkgqvnpp7m/Migrate_from_OneAgent_Operator_to_Dynatrace_Operator-Application-only_migration-Light_Mode?auto=webp&format=png&position=1)

Только облачное приложение (cloud native)

Что остаётся неизменным

Что меняется

**Глобальные параметры (`spec`)**  
Следующие настройки являются глобальными, общими для каждого компонента, и находятся в `spec`.

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

В CR OneAgent это было `agentVersion`.

2

Этот новый параметр будет автоматически доставлять бинарные файлы в поды и устранит требования к хранилищу в подах. Пока это только в статусе preview и по умолчанию имеет значение `false`.

Параметр `image` больше недоступен. Эта функциональность будет возвращена в будущем. Пока все поды загружаются с URL API.

## Миграция с оператора OneAgent на оператор Dynatrace

С устаревшего оператора OneAgent можно перейти на новый оператор Dynatrace, который управляет жизненным циклом нескольких компонентов Dynatrace, таких как OneAgent, маршрутизация и монитор Kubernetes API. По мере появления новых функций observability будут добавляться дополнительные компоненты.

Выбери **один из следующих вариантов** в зависимости от способа развёртывания.

[**Манифест**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Миграция манифестов

Kubernetes

OpenShift

1. Удали оператор OneAgent и пространство имён/проект `dynatrace`.

   ```
   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/kubernetes.yaml



   kubectl delete namespace dynatrace
   ```
2. [Настрой мониторинг с оператором Dynatrace](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание оператора Dynatrace на Kubernetes").

1. Удали оператор OneAgent и пространство имён/проект `dynatrace`.

   ```
   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/openshift.yaml



   oc delete project dynatrace
   ```
2. [Настрой мониторинг с оператором Dynatrace](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание оператора Dynatrace на Kubernetes").

### Миграция с Helm

Kubernetes

OpenShift

1. Удали оператор OneAgent, репозиторий Helm и пространство имён/проект `dynatrace`.

   ```
   helm uninstall dynatrace-oneagent-operator



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   kubectl delete namespace dynatrace
   ```
2. [Настрой мониторинг с оператором Dynatrace](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание оператора Dynatrace на Kubernetes").

1. Удали оператор OneAgent, репозиторий Helm и пространство имён/проект `dynatrace`.

   ```
   helm uninstall dynatrace-oneagent-operator



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   oc delete project dynatrace
   ```
2. [Настрой мониторинг с оператором Dynatrace](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание оператора Dynatrace на Kubernetes").