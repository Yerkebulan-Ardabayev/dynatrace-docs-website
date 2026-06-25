---
title: Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings
scraped: 2026-05-12T12:07:41.616771
---

# Global default monitoring settings for Kubernetes/OpenShift

# Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift

* 2-min read
* Updated on Jun 15, 2023

Dynatrace version 1.270+

Вы можете настроить параметры мониторинга по умолчанию для кластеров Kubernetes/OpenShift. Эти значения по умолчанию используются для всех новых кластеров, если при их создании не заданы специальные настройки мониторинга.

## Настройка через веб-интерфейс

Параметры мониторинга можно настроить как для отдельного кластера, так и для всей среды.

### Настройка параметров на уровне среды

Чтобы настроить параметры по умолчанию для всей среды:

1. Перейдите в **Settings** и выберите **Cloud and virtualization** > **Kubernetes**.
2. На странице **Monitoring settings** измените параметры по необходимости.
3. Нажмите **Save changes**.

![Kubernetes monitoring settings on tenant](https://dt-cdn.net/images/tenant-monitoring-settings-1425-ab644e8cd0.png)

Настройки мониторинга Kubernetes на уровне тенанта

Эти параметры на уровне среды будут использоваться как значения по умолчанию для всех кластеров, которые явно не переопределяют их.

### Просмотр кластеров с переопределёнными настройками

Чтобы просмотреть, какие кластеры в настоящее время переопределяют эти настройки:

1. На странице **Monitoring settings** уровня среды выберите **More** (**…**) > **Hierarchy and overrides** в правом верхнем углу.
2. Просмотрите таблицу **Hierarchy and overrides**.

Подробнее об иерархии настроек см. в документации по [Settings](/managed/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

![Kubernetes monitoring settings overrides](https://dt-cdn.net/images/tenant-monitoring-settings-overrides-2058-db713cf077.png)

Переопределения настроек мониторинга Kubernetes

### Удаление переопределений на уровне кластера

Чтобы удалить переопределение для конкретного кластера:

1. В таблице **Hierarchy and overrides** выберите имя кластера.

   Откроется страница **Monitoring settings** для выбранного кластера с сообщением «These settings are overriding Environment settings».
2. В блоке сообщения нажмите **Remove override**. Если переопределение не задано, будут использоваться значения, установленные на уровне среды.

![Kubernetes monitoring settings on cluster](https://dt-cdn.net/images/cluster-monitoring-settings-override-929-a45970ae1e.png)

Настройки мониторинга Kubernetes на уровне кластера

## Настройка через API

Параметры мониторинга также можно настроить через [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") с использованием [схемы настроек мониторинга](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.").

Чтобы изменить значения по умолчанию для среды, задайте для свойства `scope` в запросе значение `environment`.

Чтобы при подключении кластера использовались настройки по умолчанию, [схема настроек подключения](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") должна быть версии `3.0.0` или выше. При использовании более старых версий настройки мониторинга по умолчанию для этого кластера будут переопределены автоматически.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")