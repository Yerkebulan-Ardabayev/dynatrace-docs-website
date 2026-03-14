---
title: Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/default-monitoring-settings
scraped: 2026-03-06T21:21:49.803705
---

# Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift

# Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift

* Classic
* 2-min read
* Updated on Jun 15, 2023

Dynatrace версии 1.270+

Вы можете настроить параметры мониторинга по умолчанию для кластеров Kubernetes/OpenShift. Эти значения по умолчанию используются для всех новых кластеров, если только параметры мониторинга не заданы при их создании.

## Настройка через веб-интерфейс

Параметры мониторинга можно настроить как для отдельного кластера, так и для всей среды.

### Настройка параметров на уровне среды

Для настройки параметров по умолчанию для всей среды

1. Перейдите в **Settings** и выберите **Cloud and virtualization** > **Kubernetes**.
2. На странице **Monitoring settings** измените параметры по необходимости.
3. Выберите **Save changes**.

![Kubernetes monitoring settings on tenant](https://dt-cdn.net/images/tenant-monitoring-settings-1425-ab644e8cd0.png)

Эти параметры на уровне среды будут использоваться в качестве значений по умолчанию для всех кластеров, которые явно не переопределяют их.

### Список переопределяющих кластеров

Чтобы увидеть, какие кластеры в данный момент переопределяют эти параметры

1. На странице **Monitoring settings** уровня среды выберите **More** (**...**) > **Hierarchy and overrides** в правом верхнем углу.
2. Просмотрите таблицу **Hierarchy and overrides**.

Подробнее об иерархии параметров см. в [документации по Settings](../../../../manage/settings/settings-20.md#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework").

![Kubernetes monitoring settings overrides](https://dt-cdn.net/images/tenant-monitoring-settings-overrides-2058-db713cf077.png)

### Удаление переопределений на уровне кластера

Если вы хотите удалить переопределение для конкретного кластера

1. В таблице **Hierarchy and overrides** выберите имя кластера.

   Откроется страница **Monitoring settings** для выбранного кластера. Отображается сообщение "These settings are overriding Environment settings".
2. В поле сообщения выберите **Remove override**. Если переопределение не установлено, будут использоваться значения, заданные на уровне среды.

![Kubernetes monitoring settings on cluster](https://dt-cdn.net/images/cluster-monitoring-settings-override-929-a45970ae1e.png)

## Настройка через API

Вы также можете настроить параметры мониторинга через [Settings API](../../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers."), используя [схему параметров мониторинга](../../../../dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring.md "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.").

Чтобы изменить значения по умолчанию для среды, установите свойство `scope` в запросе равным `environment`.

Чтобы использовать настройки по умолчанию при подключении кластера, [схема параметров подключения](../../../../dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes.md "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") должна иметь версию `3.0.0` или выше. Использование более старых версий автоматически переопределит настройки мониторинга по умолчанию для этого кластера.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](../../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
