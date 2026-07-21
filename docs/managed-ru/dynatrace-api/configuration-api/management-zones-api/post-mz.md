---
title: Management zones API - POST a management zone
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/management-zones-api/post-mz
---

# Management zones API - POST a management zone

# Management zones API - POST a management zone

* Справка
* Опубликовано 02 сент. 2019 г.

Устарело

Этот API устарел. Вместо него нужно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") со схемой [Management zones settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:management-zones`).

Создаёт новую management zone.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/managementZones` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/managementZones` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, рассказано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все модели JSON, которые зависят от типа модели, приведены в разделе [JSON models](/managed/dynatrace-api/configuration-api/management-zones-api/json-models "Learn the variations of models in the Management zones API.").

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ManagementZone](#openapi-definition-ManagementZone) | Тело JSON запроса. Содержит параметры новой management zone. | body | Опционально |

### Объекты тела запроса

#### Объект `ManagementZone`

Конфигурация management zone. Определяет, как применяется management zone.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| description | string | Описание management zone. | Опционально |
| dimensionalRules | [MzDimensionalRule](#openapi-definition-MzDimensionalRule)[] | Список правил размерных данных для использования management zone.  Если указано несколько правил, применяется логика **OR**. | Опционально |
| entitySelectorBasedRules | [EntitySelectorBasedMzRule](#openapi-definition-EntitySelectorBasedMzRule)[] | Список правил на основе entity selector для использования management zone.  Если указано несколько правил, применяется логика **OR**. | Опционально |
| id | string | ID management zone. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| name | string | Название management zone. | Обязательно |
| rules | [MzRule](#openapi-definition-MzRule)[] | Список правил для использования management zone.  Если указано несколько правил, применяется логика **OR**. | Опционально |

#### Объект `MzDimensionalRule`

Размерное правило использования management zone. Определяет, как применяется management zone.

Каждое правило оценивается независимо от всех остальных правил.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| appliesTo | string | Цель правила. Элемент может принимать следующие значения * `ANY` * `LOG` * `METRIC` | Обязательно |
| conditions | [MzDimensionalRuleCondition](#openapi-definition-MzDimensionalRuleCondition)[] | Список условий для management zone.  Management zone применяется, только если выполнены **все** условия. | Обязательно |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательно |

#### Объект `MzDimensionalRuleCondition`

Условие размерного правила management zone.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditionType | string | Тип условия. Элемент может принимать следующие значения * `DIMENSION` * `LOG_FILE_NAME` * `METRIC_KEY` | Обязательно |
| key | string | Эталонное значение для сравнения.  Для условий типа `DIMENSION` здесь указывается ключ. | Обязательно |
| ruleMatcher | string | Способ сравнения значений. Элемент может принимать следующие значения * `BEGINS_WITH` * `EQUALS` | Обязательно |
| value | string | Значение измерения.  Применимо, только если **conditionType** установлен в `DIMENSION`. | Опционально |

#### Объект `EntitySelectorBasedMzRule`

Правило использования management zone на основе entity selector. Позволяет добавлять сущности в management zone через entity selector.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Опционально |
| entitySelector | string | Строка entity selector, по которой выбираются сущности. | Обязательно |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `MzRule`

Правило использования management zone. Определяет, как применяется management zone.

Каждое правило оценивается независимо от всех остальных правил.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [EntityRuleEngineCondition](#openapi-definition-EntityRuleEngineCondition)[] | Список правил соответствия для management zone.  Management zone применяется, только если выполнены **все** условия. | Обязательно |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Обязательно |
| propagationTypes | string[] | Как применять management zone к нижележащим сущностям:  * `SERVICE_TO_HOST_LIKE`: применить к нижележащим хостам подходящих сервисов. * `SERVICE_TO_PROCESS_GROUP_LIKE`: применить к нижележащим группам процессов подходящих сервисов. * `PROCESS_GROUP_TO_HOST`: применить к нижележащим хостам подходящих групп процессов. * `PROCESS_GROUP_TO_SERVICE`: применить ко всем сервисам, предоставляемым подходящими группами процессов. * `HOST_TO_PROCESS_GROUP_INSTANCE`: применить к процессам, запущенным на подходящих хостах. * `CUSTOM_DEVICE_GROUP_TO_CUSTOM_DEVICE`: применить к пользовательским устройствам в подходящих группах пользовательских устройств. * `AZURE_TO_PG`: применить к группам процессов, связанным с подходящими сущностями Azure. * `AZURE_TO_SERVICE`: применить к сервисам, предоставляемым подходящими сущностями Azure. Элемент может принимать следующие значения * `AZURE_TO_PG` * `AZURE_TO_SERVICE` * `CUSTOM_DEVICE_GROUP_TO_CUSTOM_DEVICE` * `HOST_TO_PROCESS_GROUP_INSTANCE` * `PROCESS_GROUP_TO_HOST` * `PROCESS_GROUP_TO_SERVICE` * `SERVICE_TO_HOST_LIKE` * `SERVICE_TO_PROCESS_GROUP_LIKE` | Опционально |
| type | string | Тип сущностей Dynatrace, к которым может применяться management zone. Элемент может принимать следующие значения * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AWS_ACCOUNT` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AUTO_SCALING_GROUP` * `AWS_CLASSIC_LOAD_BALANCER` * `AWS_NETWORK_LOAD_BALANCER` * `AWS_RELATIONAL_DATABASE_SERVICE` * `AZURE` * `BROWSER_MONITOR` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_FOUNDRY_FOUNDATION` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DATA_CENTER_SERVICE` * `ENTERPRISE_APPLICATION` * `ESXI_HOST` * `EXTERNAL_MONITOR` * `HOST` * `HOST_GROUP` * `HTTP_MONITOR` * `KUBERNETES_CLUSTER` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `OPENSTACK_ACCOUNT` * `PROCESS_GROUP` * `QUEUE` * `SERVICE` * `WEB_APPLICATION` | Обязательно |

#### Объект `EntityRuleEngineCondition`

Условие определяет, как выполняется логика сопоставления для сущности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comparisonInfo | [ComparisonBasic](#openapi-definition-ComparisonBasic) | Определяет, как фактически выполняется сопоставление: что и как сравнивается.  Фактический набор полей и допустимые значения поля **operator** зависят от типа сравнения. Список фактических объектов см. в описании поля **type** или в [моделях JSON﻿](https://dt-url.net/0b83s6z?dt=m). | Обязательно |
| key | [ConditionKey](#openapi-definition-ConditionKey) | Ключ для идентификации данных, с которыми выполняется сопоставление.  Фактический набор полей и допустимые значения зависят от типа ключа. Список фактических объектов см. в описании поля **type** или в [моделях JSON﻿](https://dt-url.net/0b83s6z?dt=m). | Обязательно |

#### Объект `ComparisonBasic`

Определяет, как фактически выполняется сопоставление: что и как сравнивается.

Фактический набор полей и допустимые значения поля **operator** зависят от типа сравнения. Список фактических объектов см. в описании поля **type** или в [моделях JSON﻿](https://dt-url.net/0b83s6z?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| negate | boolean | Инвертирует **operator** сравнения. Например, превращает **begins with** в **does not begin with**. | Обязательно |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`.  Допустимые значения зависят от **type** сравнения. Список фактических моделей см. в описании поля **type** и проверьте описание нужной модели. | Обязательно |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING` -> StringComparison * `INDEXED_NAME` -> IndexedNameComparison * `INDEXED_STRING` -> IndexedStringComparison * `INTEGER` -> IntegerComparison * `SERVICE_TYPE` -> ServiceTypeComparison * `PAAS_TYPE` -> PaasTypeComparison * `CLOUD_TYPE` -> CloudTypeComparison * `AZURE_SKU` -> AzureSkuComparision * `AZURE_COMPUTE_MODE` -> AzureComputeModeComparison * `ENTITY_ID` -> EntityIdComparison * `SIMPLE_TECH` -> SimpleTechComparison * `SIMPLE_HOST_TECH` -> SimpleHostTechComparison * `SERVICE_TOPOLOGY` -> ServiceTopologyComparison * `DATABASE_TOPOLOGY` -> DatabaseTopologyComparison * `OS_TYPE` -> OsTypeComparison * `HYPERVISOR_TYPE` -> HypervisorTypeComparision * `IP_ADDRESS` -> IpAddressComparison * `OS_ARCHITECTURE` -> OsArchitectureComparison * `BITNESS` -> BitnessComparision * `APPLICATION_TYPE` -> ApplicationTypeComparison * `MOBILE_PLATFORM` -> MobilePlatformComparison * `CUSTOM_APPLICATION_TYPE` -> CustomApplicationTypeComparison * `DCRUM_DECODER_TYPE` -> DcrumDecoderComparison * `SYNTHETIC_ENGINE_TYPE` -> SyntheticEngineTypeComparison * `TAG` -> TagComparison * `INDEXED_TAG` -> IndexedTagComparison Элемент может принимать следующие значения * `APPLICATION_TYPE` * `AZURE_COMPUTE_MODE` * `AZURE_SKU` * `BITNESS` * `CLOUD_TYPE` * `CUSTOM_APPLICATION_TYPE` * `DATABASE_TOPOLOGY` * `DCRUM_DECODER_TYPE` * `ENTITY_ID` * `HYPERVISOR_TYPE` * `INDEXED_NAME` * `INDEXED_STRING` * `INDEXED_TAG` * `INTEGER` * `IP_ADDRESS` * `MOBILE_PLATFORM` * `OS_ARCHITECTURE` * `OS_TYPE` * `PAAS_TYPE` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SIMPLE_HOST_TECH` * `SIMPLE_TECH` * `STRING` * `SYNTHETIC_ENGINE_TYPE` * `TAG` | Обязательно |
| value | [AnyValue](#openapi-definition-AnyValue) | Значение для сравнения. | Опционально |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `ConditionKey`

Ключ для идентификации данных, с которыми выполняется сопоставление.

Фактический набор полей и допустимые значения зависят от типа ключа. Список фактических объектов см. в описании поля **type** или в [моделях JSON﻿](https://dt-url.net/0b83s6z?dt=m).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| attribute | string | Атрибут, используемый для сравнения. Элемент может принимать следующие значения * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `AWS_AVAILABILITY_ZONE_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AZURE_ENTITY_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_MGMT_GROUP_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_TENANT_NAME` * `AZURE_TENANT_UUID` * `AZURE_VM_NAME` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `CUSTOM_DEVICE_DETECTED_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_TECHNOLOGY` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `DOCKER_STRIPPED_IMAGE_NAME` * `EC2_INSTANCE_AMI_ID` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `EC2_INSTANCE_TAGS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_NAME` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `ESXI_HOST_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `GEOLOCATION_SITE_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `HOST_ARCHITECTURE` * `HOST_AWS_NAME_TAG` * `HOST_AZURE_COMPUTE_MODE` * `HOST_AZURE_SKU` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BITNESS` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `HOST_CLOUD_TYPE` * `HOST_CPU_CORES` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_HYPERVISOR_TYPE` * `HOST_IP_ADDRESS` * `HOST_KUBERNETES_LABELS` * `HOST_LOGICAL_CPU_CORES` * `HOST_NAME` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `HOST_TAGS` * `HOST_TECHNOLOGY` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `KUBERNETES_CLUSTER_NAME` * `KUBERNETES_NODE_NAME` * `KUBERNETES_SERVICE_NAME` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `NAME_OF_COMPUTE_NODE` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_REGION_NAME` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_VM_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `QUEUE_NAME` * `QUEUE_TECHNOLOGY` * `QUEUE_VENDOR` * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_IIB_APPLICATION_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_TAGS` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `PROCESS_CUSTOM_METADATA_KEY` -> CustomProcessMetadataConditionKey * `HOST_CUSTOM_METADATA_KEY` -> CustomHostMetadataConditionKey * `PROCESS_PREDEFINED_METADATA_KEY` -> ProcessMetadataConditionKey * `STRING` -> StringConditionKey * `STATIC` -> StaticConditionKey Элемент может принимать следующие значения * `HOST_CUSTOM_METADATA_KEY` * `PROCESS_CUSTOM_METADATA_KEY` * `PROCESS_PREDEFINED_METADATA_KEY` * `STATIC` * `STRING` | Optional |

### Модель тела запроса JSON

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"description": "sampleDescription",



"dimensionalRules": [



{



"appliesTo": "METRIC",



"conditions": [



{



"conditionType": "DIMENSION",



"key": "alwaysRequired",



"ruleMatcher": "EQUALS",



"value": "requiredForDimension_forbiddenForMetricKeyAndLogFileName"



}



],



"enabled": true



}



],



"entitySelectorBasedRules": [



{



"enabled": true,



"entitySelector": "type(HOST) AND cpuCores(4)"



}



],



"name": "sampleManagementZone",



"rules": [



{



"conditions": [



{



"comparisonInfo": {



"caseSensitive": false,



"negate": false,



"operator": "BEGINS_WITH",



"type": "STRING",



"value": "sample"



},



"key": {



"attribute": "SERVICE_DATABASE_NAME"



}



},



{



"comparisonInfo": {



"negate": false,



"operator": "EXISTS",



"type": "STRING"



},



"key": {



"attribute": "SERVICE_WEB_SERVER_NAME"



}



},



{



"comparisonInfo": {



"caseSensitive": false,



"negate": false,



"operator": "BEGINS_WITH",



"type": "STRING",



"value": "sample"



},



"key": {



"attribute": "PROCESS_GROUP_CUSTOM_METADATA",



"dynamicKey": {



"key": "kubernetes.io/limit-ranger",



"source": "KUBERNETES"



},



"type": "PROCESS_CUSTOM_METADATA_KEY"



}



}



],



"enabled": true,



"propagationTypes": [



"SERVICE_TO_HOST_LIKE"



],



"type": "SERVICE"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Management zone создана. Ответ содержит ID новой зоны. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Проверка полезной нагрузки

Рекомендуется проверить полезную нагрузку перед отправкой её в реальном запросе. Код ответа **204** означает, что полезная нагрузка действительна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/managementZones/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/managementZones/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация действительна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела ответа JSON

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

В этом примере запрос создаёт новую management zone с именем **Mainframe**. Она включает все **сервисы**, работающие на хостах с архитектурой **z/OS**, и **лежащие в основе группы процессов**.

Токен API передаётся в заголовке **Authorization**.

Тело запроса объёмное, поэтому в разделе **Curl** оно сокращено. Полное тело см. в разделе **Request body**. Пример тела запроса можно скачать или скопировать, чтобы попробовать самостоятельно.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{ <truncated - see the Request body section > }'
```

### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/managementZones
```

#### Тело запроса

```
{



"name": "Mainframe",



"rules": [



{



"type": "SERVICE",



"enabled": true,



"propagationTypes": ["SERVICE_TO_PROCESS_GROUP_LIKE"],



"conditions": [



{



"key": {



"attribute": "HOST_ARCHITECTURE"



},



"comparisonInfo": {



"type": "OS_ARCHITECTURE",



"operator": "EQUALS",



"value": "ZOS",



"negate": false



}



}



]



}



]



}
```

#### Тело ответа

```
{



"id": "2072664797514502900",



"name": "Mainframe"



}
```

#### Код ответа

201

#### Результат

Новая management zone в интерфейсе выглядит так:

![POST management zone](https://dt-cdn.net/images/post-mz-1345-ff7bd6a94e.png)

POST management zone

## Связанные темы

* [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")