---
title: Settings API - Management zones settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones
scraped: 2026-05-12T11:19:05.420553
---

# Settings API - Management zones settings schema table

# Settings API - Management zones settings schema table

* Опубликовано 5 декабря 2023 г.

### Настройки management zones (`builtin:management-zones)`

Management zones позволяют задавать точечные права доступа к частям environment. Management zone состоит из набора entities, таких как applications, hosts, process groups или services.

Для каждой Management zone можно определить, какие группы пользователей имеют к ней доступ. Так обеспечивается конфиденциальность отдельных частей environment с сохранением сквозного представления по всем компонентам для пользователей, которым оно нужно.

Для подсказки значений на основе данных entity и функции preview требуется environment-wide разрешение "Access environment".

Правила management zone периодически выполняются в фоне в течение ограниченного timeframe. Любая entity, удовлетворяющая правилу management zone, получит назначенную zone, при этом zones снимаются с entities, которые перестают подходить. Учтите: для любого условия, требующего связи между несколькими entities, все entities этого scope должны присутствовать в данном timeframe!

В зависимости от размера environment, количества правил (Management zones, а также tagging и naming rules) и их сложности, применение всех management zones может задерживаться!

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:management-zones` | * `group:management-zones` * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:management-zones` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:management-zones` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:management-zones` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя management zone `name` | text | **Будьте осторожны при переименовании**: если есть политики, ссылающиеся на эту Management zone, их потребуется адаптировать под новое имя! | Required |
| Описание `description` | text | - | Optional |
| Правила `rules` | Set<[Rule](#Rule)> | - | Required |

##### Объект `Rule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Тип правила `type` | enum | Возможные значения: * `ME` * `DIMENSION` * `SELECTOR` | Required |
| `attributeRule` | [ManagementZoneAttributeRule](#ManagementZoneAttributeRule) | - | Required |
| `dimensionRule` | [DimensionRule](#DimensionRule) | - | Required |
| Entity selector `entitySelector` | text | Подробнее об [Entity selector](https://dt-url.net/apientityselector). | Required |

##### Объект `ManagementZoneAttributeRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Правило применяется к `entityType` | enum | Возможные значения: * `SERVICE` * `PROCESS_GROUP` * `HOST` * `CUSTOM_DEVICE` * `ESXI_HOST` * `CUSTOM_DEVICE_GROUP` * `HOST_GROUP` * `DATA_CENTER_SERVICE` * `QUEUE` * `WEB_APPLICATION` * `ENTERPRISE_APPLICATION` * `MOBILE_APPLICATION` * `CUSTOM_APPLICATION` * `BROWSER_MONITOR` * `EXTERNAL_MONITOR` * `HTTP_MONITOR` * `NETWORK_AVAILABILITY_MONITOR` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AWS_ACCOUNT` * `AWS_CLASSIC_LOAD_BALANCER` * `AWS_RELATIONAL_DATABASE_SERVICE` * `AWS_AUTO_SCALING_GROUP` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_NETWORK_LOAD_BALANCER` * `OPENSTACK_ACCOUNT` * `KUBERNETES_CLUSTER` * `KUBERNETES_SERVICE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_APPLICATION` * `CLOUD_FOUNDRY_FOUNDATION` * `AZURE` | Required |
| Условия `conditions` | Set<[AttributeCondition](#AttributeCondition)> | - | Required |
| Применять к нижележащим hosts подходящих services `serviceToHostPropagation` | boolean | - | Required |
| Применять к нижележащим process groups подходящих services `serviceToPGPropagation` | boolean | - | Required |
| Применять к нижележащим hosts подходящих process groups `pgToHostPropagation` | boolean | - | Required |
| Применять ко всем services, предоставляемым process groups `pgToServicePropagation` | boolean | - | Required |
| Применять к процессам, работающим на подходящих hosts `hostToPGPropagation` | boolean | - | Required |
| Применять к custom devices в custom device group `customDeviceGroupToCustomDevicePropagation` | boolean | - | Required |
| Применять к services, предоставляемым подходящими Azure entities `azureToServicePropagation` | boolean | - | Required |
| Применять к process groups, связанным с подходящими Azure entities `azureToPGPropagation` | boolean | - | Required |

##### Объект `DimensionRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `appliesTo` | enum | Возможные значения: * `ANY` * `LOG` * `METRIC` | Required |
| Условия `conditions` | Set<[DimensionCondition](#DimensionCondition)> | - | Required |

##### Объект `AttributeCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойство `key` | enum | Возможные значения: * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_TAGS` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `EC2_INSTANCE_AMI_ID` * `AWS_AVAILABILITY_ZONE_NAME` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `HOST_AWS_NAME_TAG` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `HOST_ARCHITECTURE` * `HOST_AZURE_SKU` * `AZURE_VM_NAME` * `HOST_AZURE_COMPUTE_MODE` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `HOST_BITNESS` * `HOST_BOSH_NAME` * `HOST_CPU_CORES` * `HOST_CLOUD_TYPE` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_TAGS` * `OPENSTACK_REGION_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_IP_ADDRESS` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_NAME` * `HOST_TAGS` * `HOST_HYPERVISOR_TYPE` * `KUBERNETES_CLUSTER_NAME` * `HOST_LOGICAL_CPU_CORES` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `GEOLOCATION_SITE_NAME` * `OPENSTACK_VM_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `NAME_OF_COMPUTE_NODE` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `HOST_TECHNOLOGY` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_TECHNOLOGY` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_NAME` * `ESXI_HOST_TAGS` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `KUBERNETES_SERVICE_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_MGMT_GROUP_NAME` * `AZURE_ENTITY_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_TENANT_UUID` * `AZURE_TENANT_NAME` * `HOST_KUBERNETES_LABELS` * `KUBERNETES_NODE_NAME` * `QUEUE_NAME` * `QUEUE_VENDOR` * `QUEUE_TECHNOLOGY` | Required |
| Источник ключа `dynamicKeySource` | text | - | Required |
| Динамический ключ `dynamicKey` | text | - | Required |
| Оператор `operator` | enum | Возможные значения: * `EQUALS` * `NOT_EQUALS` * `EXISTS` * `NOT_EXISTS` * `BEGINS_WITH` * `NOT_BEGINS_WITH` * `CONTAINS` * `NOT_CONTAINS` * `ENDS_WITH` * `NOT_ENDS_WITH` * `GREATER_THAN` * `NOT_GREATER_THAN` * `GREATER_THAN_OR_EQUAL` * `NOT_GREATER_THAN_OR_EQUAL` * `LOWER_THAN` * `NOT_LOWER_THAN` * `LOWER_THAN_OR_EQUAL` * `NOT_LOWER_THAN_OR_EQUAL` * `TAG_KEY_EQUALS` * `NOT_TAG_KEY_EQUALS` * `IS_IP_IN_RANGE` * `NOT_IS_IP_IN_RANGE` * `REGEX_MATCHES` * `NOT_REGEX_MATCHES` | Required |
| Значение `enumValue` | text | - | Required |
| Значение `stringValue` | text | - | Required |
| С учётом регистра `caseSensitive` | boolean | - | Required |
| Значение `integerValue` | integer | - | Required |
| Значение `entityId` | text | - | Required |
| Тег `tag` | text | Формат: `[CONTEXT]tagKey:tagValue` | Required |

##### Объект `DimensionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `conditionType` | enum | Возможные значения: * `DIMENSION` * `LOG_FILE_NAME` * `METRIC_KEY` | Required |
| Ключ `key` | text | - | Required |
| Оператор `ruleMatcher` | enum | Возможные значения: * `BEGINS_WITH` * `EQUALS` | Required |
| Значение `value` | text | - | Required |