---
title: Атрибуты ресурсов
source: https://docs.dynatrace.com/managed/platform/oneagent/resource-attributes
scraped: 2026-05-12T12:10:28.674801
---

# Атрибуты ресурсов

# Атрибуты ресурсов

* Reference
* 6-min read
* Updated on Jul 23, 2025

## Атрибуты ресурсов на уровне хоста

Все артефакты мониторинга, исходящие с данного хоста — то есть имеющие хост в качестве ресурса — обогащаются атрибутами ресурсов на уровне хоста.

Атрибуты ресурсов на уровне хоста — это атрибуты ресурсов отслеживаемых хостов. Все события, генерируемые компонентами OneAgent, работающими на данном хосте, и измерения, поступающие от них, обогащаются этими атрибутами. Затем вы можете использовать их в запросах для структурирования и фильтрации данных мониторинга.

Вы также можете использовать некоторые атрибуты для создания политик управления доступом к данным. См. [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") и найдите поля с тегом Permission.

Если у вас есть доступ к хосту с установленным OneAgent, вы можете проверить файлы `dt_host_metadata.json` и `dt_host_metadata.properties` для просмотра области обогащения атрибутами ресурсов, предоставляемой OneAgent. Подробнее см. в разделе [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### Пользовательские атрибуты на уровне хоста

Вы можете создавать собственные атрибуты, настраивая пары «ключ–значение» для тегов и свойств через [oneagentctl](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") или через [Удалённое управление конфигурацией OneAgents и ActiveGates](/managed/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API."). Пользовательские теги и свойства, определённые таким образом, передаются как плоские атрибуты ресурсов первого уровня.

Теги-ключи без значения игнорируются.

Теги, назначенные через [автоматические правила](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), [переменные среды](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") и [Topology and Smartscape API](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API."), не включаются.

### Общие атрибуты на уровне хоста

| Атрибут | Описание |
| --- | --- |
| Custom host tags | См. [Пользовательские атрибуты](#custom) |
| `dt.host_group.id` | Обратите внимание на разницу между `dt.entity.host_group` и `dt.host_group.id`: `dt.host_group.id` — это имя [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Это удобочитаемый идентификатор группы хостов, например `MyHostGroup`. `dt.entity.host_group` — это идентификатор сущности группы хостов в модели Dynatrace. Идентификатор сущности не совпадает с удобочитаемым идентификатором группы хостов. Он создаётся автоматически и имеет формат, например, `HOST_GROUP-008786529C8EE446`. Подробнее см. в разделе [Организация среды с помощью групп хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). |
| `dt.entity.host` | Идентификатор сущности типа HOST. |
| `dt.entity.host_group` | Идентификатор сущности типа `HOST_GROUP`. |
| `host.name` | Имя хоста, определяемое в зависимости от источника данных (например, OneAgent, Extensions или OpenTelemetry). Имя хоста может быть изменено на основе правил именования. Обратите внимание, что это не идентификатор сущности типа `HOST` (`dt.entity.host`). |

#### AWS

| Атрибут | Описание |
| --- | --- |
| `dt.entity.ec2_instance` | Идентификатор сущности типа `EC2_INSTANCE`. |
| `dt.entity.aws_availability_zone` | Идентификатор сущности типа `AWS_AVAILABILITY_ZONE`. |
| `aws.availability_zone` | Конкретная зона доступности в заданном регионе AWS. Например, `us-east-1a`. |
| `aws.region` | Конкретное географическое расположение облака AWS. Например, `us-east-1`. |
| `aws.resource.id` | Уникальный идентификатор ресурса. |

#### Azure

| Атрибут | Описание |
| --- | --- |
| `dt.entity.azure_vm` | Идентификатор сущности типа `AZURE_VM`, извлечённый из поля `instanceId` метаданных экземпляра Azure. |
| `dt.entity.azure_region` | Идентификатор сущности типа `AZURE_REGION`. |
| `azure.location` | Конкретное географическое расположение ресурса Azure, извлечённое из поля `location` метаданных экземпляра Azure. |
| `azure.vmid` | Уникальный 128-битный идентификатор виртуальной машины Azure. |

#### Google Cloud

| Атрибут | Описание |
| --- | --- |
| `gcp.instance.id` | Постоянный идентификатор, уникальный в рамках вашего проекта Google Cloud. |
| `gcp.project.id` | Идентификатор проекта GCP, связанного с этим ресурсом. |
| `dt.entity.gcp_zone` | Идентификатор сущности типа `GCP_ZONE`. |
| `gcp.zone` | Зона — это часть региона. Каждый регион содержит три или более зоны. Например, `europe-west3-c`. |
| `gcp.region` | Регион — это конкретное географическое расположение для размещения ресурсов. Например, `europe-west3`. |

#### OpenStack

| Атрибут | Описание |
| --- | --- |
| `openstack.availability_zone` | Конкретная зона доступности в заданном регионе OpenStack. Например, `us-east-1a`. |
| `openstack.instance_uuid` | UUID экземпляра OpenStack. |

#### Kubernetes

| Атрибут | Описание |
| --- | --- |
| `k8s.cluster.uid` | Поскольку имя кластера Kubernetes не всегда доступно, Dynatrace идентифицирует кластер по UID пространства имён kube-system. Доступно только в развёртываниях Dynatrace Operator. |
| `k8s.node.name` | Имя узла Kubernetes. Доступно только в развёртываниях Dynatrace Operator. |

#### BOSH

| Атрибут | Описание |
| --- | --- |
| `bosh.instance_id` | Уникальный идентификатор, присваиваемый каждому развёрнутому экземпляру BOSH. |
| `bosh.availability_zone` | Конкретное географическое расположение BOSH. Например, `us-east-1a`. |
| `bosh.name` | Уникальный идентификатор развёртывания или экземпляра. |

### Нормализация атрибутов ресурсов

Для обеспечения согласованного и надёжного приёма метрик нормализация атрибутов ресурсов применяется ко всем соответствующим внутренним ключам и значениям метрик. Этот процесс помогает предотвратить отброс метрик из-за недействительных или некорректных измерений.

#### Правила для ключей измерений

| Описание правила | Подробности |
| --- | --- |
| **Недопустимые символы** | Недопустимый символ или серия недопустимых символов заменяется одним символом подчёркивания `_`. Например, `zaó$%ą` заменяется на `za_`. |
| **Пустые ключи** | Измерения без допустимых символов пропускаются |
| **Ограничение длины ключа** | OneAgent версии 1.317+ Макс. 350 символов (ранее макс. 100 символов) |

#### Правила для значений измерений

| Описание правила | Подробности |
| --- | --- |
| **Допустимые символы** | Все непечатаемые символы (ASCII и Unicode) |
| **Управляющие символы** | Не допускаются. Управляющий символ или серия таких символов заменяется одним символом подчёркивания `_`. |
| **Ограничение длины значения** | OneAgent версии 1.313+ Макс. 2048 символов (ранее макс. 255 символов) |
| **Значения в кавычках** | Если значение начинается и заканчивается символом `"`, оно экранируется |

#### Ограничения на количество измерений

Для соответствия текущей спецификации используется определённая иерархия измерений с заданными ограничениями, чтобы предотвратить предупреждения и отброс метрик из-за превышения этих ограничений.

По умолчанию глобальный лимит измерений равен `100`, а пользовательский лимит составляет 40% от глобального лимита.