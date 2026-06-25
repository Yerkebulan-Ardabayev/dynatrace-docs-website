---
title: Conditional naming API - POST a new naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/conditional-naming/post-rule
scraped: 2026-05-12T11:17:17.217697
---

# Conditional naming API - POST a new naming rule

# Conditional naming API - POST a new naming rule

* Reference
* Published Apr 23, 2020

Создаёт новое правило условного именования.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все JSON-модели, зависящие от **типа** модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/conditional-naming/json-models "Узнайте, что предлагает Dynatrace conditional naming API.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Тип правила, определяемый типом сущностей Dynatrace, к которым применяется правило. Элемент может принимать значения * `processGroup` * `host` * `service` | path | Required |
| body | [ConditionalNamingRule](#openapi-definition-ConditionalNamingRule) | JSON-тело запроса. Содержит параметры нового правила именования.  Не указывайте **id** правила.  Значение поля **type** должно совпадать с path-параметром **type**. | body | Optional |

### Объекты тела запроса

#### Объект `ConditionalNamingRule`

Правило условного именования.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| displayName | string | Имя правила. | Required |
| enabled | boolean | Правило включено (`true`) или выключено (`false`). | Required |
| id | string | ID правила именования. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки. | Optional |
| nameFormat | string | Имя, которое будет присвоено совпадающим сущностям. Здесь можно использовать следующие плейсхолдеры:  * `{AwsAutoScalingGroup:Name}` * `{AwsAvailabilityZone:Name}` * `{AwsElasticLoadBalancer:Name}` * `{AwsRelationalDatabaseService:DBName}` * `{AwsRelationalDatabaseService:Endpoint}` * `{AwsRelationalDatabaseService:Engine}` * `{AwsRelationalDatabaseService:InstanceClass}` * `{AwsRelationalDatabaseService:Name}` * `{AwsRelationalDatabaseService:Port}` * `{AzureRegion:Name}` * `{AzureScaleSet:Name}` * `{AzureVm:Name}` * `{CloudFoundryOrganization:Name}` * `{CustomDevice:DetectedName}` * `{CustomDevice:DnsName}` * `{CustomDevice:IpAddress}` * `{CustomDevice:Port}` * `{DockerContainerGroupInstance:ContainerName}` * `{DockerContainerGroupInstance:FullImageName}` * `{DockerContainerGroupInstance:ImageVersion}` * `{ESXIHost:HardwareModel}` * `{ESXIHost:HardwareVendor}` * `{ESXIHost:Name}` * `{ESXIHost:ProductName}` * `{ESXIHost:ProductVersion}` * `{Ec2Instance:AmiId}` * `{Ec2Instance:BeanstalkEnvironmentName}` * `{Ec2Instance:InstanceId}` * `{Ec2Instance:InstanceType}` * `{Ec2Instance:LocalHostName}` * `{Ec2Instance:Name}` * `{Ec2Instance:PublicHostName}` * `{Ec2Instance:SecurityGroup}` * `{GoogleComputeInstance:Id}` * `{GoogleComputeInstance:IpAddresses}` * `{GoogleComputeInstance:MachineType}` * `{GoogleComputeInstance:Name}` * `{GoogleComputeInstance:ProjectId}` * `{GoogleComputeInstance:Project}` * `{Host:AWSNameTag}` * `{Host:AixLogicalCpuCount}` * `{Host:AzureHostName}` * `{Host:AzureSiteName}` * `{Host:BoshDeploymentId}` * `{Host:BoshInstanceId}` * `{Host:BoshInstanceName}` * `{Host:BoshName}` * `{Host:BoshStemcellVersion}` * `{Host:CpuCores}` * `{Host:DetectedName}` * `{Host:Environment:AppName}` * `{Host:Environment:BoshReleaseVersion}` * `{Host:Environment:Environment}` * `{Host:Environment:Link}` * `{Host:Environment:Organization}` * `{Host:Environment:Owner}` * `{Host:Environment:Support}` * `{Host:IpAddress}` * `{Host:LogicalCpuCores}` * `{Host:OneAgentCustomHostName}` * `{Host:OperatingSystemVersion}` * `{Host:PaasMemoryLimit}` * `{HostGroup:Name}` * `{KubernetesCluster:Name}` * `{KubernetesNode:DetectedName}` * `{OpenstackAvailabilityZone:Name}` * `{OpenstackZone:Name}` * `{OpenstackComputeNode:Name}` * `{OpenstackProject:Name}` * `{OpenstackVm:InstanceType}` * `{OpenstackVm:Name}` * `{OpenstackVm:SecurityGroup}` * `{ProcessGroup:AmazonECRImageAccountId}` * `{ProcessGroup:AmazonECRImageRegion}` * `{ProcessGroup:AmazonECSCluster}` * `{ProcessGroup:AmazonECSContainerName}` * `{ProcessGroup:AmazonECSFamily}` * `{ProcessGroup:AmazonECSRevision}` * `{ProcessGroup:AmazonLambdaFunctionName}` * `{ProcessGroup:AmazonRegion}` * `{ProcessGroup:ApacheConfigPath}` * `{ProcessGroup:ApacheSparkMasterIpAddress}` * `{ProcessGroup:AspDotNetCoreApplicationPath}` * `{ProcessGroup:AspDotNetCoreApplicationPath}` * `{ProcessGroup:AzureHostName}` * `{ProcessGroup:AzureSiteName}` * `{ProcessGroup:CassandraClusterName}` * `{ProcessGroup:CatalinaBase}` * `{ProcessGroup:CatalinaHome}` * `{ProcessGroup:CloudFoundryAppId}` * `{ProcessGroup:CloudFoundryAppName}` * `{ProcessGroup:CloudFoundryInstanceIndex}` * `{ProcessGroup:CloudFoundrySpaceId}` * `{ProcessGroup:CloudFoundrySpaceName}` * `{ProcessGroup:ColdFusionJvmConfigFile}` * `{ProcessGroup:ColdFusionServiceName}` * `{ProcessGroup:CommandLineArgs}` * `{ProcessGroup:DetectedName}` * `{ProcessGroup:DotNetCommandPath}` * `{ProcessGroup:DotNetCommand}` * `{ProcessGroup:DotNetClusterId}` * `{ProcessGroup:DotNetNodeId}` * `{ProcessGroup:ElasticsearchClusterName}` * `{ProcessGroup:ElasticsearchNodeName}` * `{ProcessGroup:EquinoxConfigPath}` * `{ProcessGroup:ExeName}` * `{ProcessGroup:ExePath}` * `{ProcessGroup:GlassFishDomainName}` * `{ProcessGroup:GlassFishInstanceName}` * `{ProcessGroup:GoogleAppEngineInstance}` * `{ProcessGroup:GoogleAppEngineService}` * `{ProcessGroup:GoogleCloudProject}` * `{ProcessGroup:HybrisBinDirectory}` * `{ProcessGroup:HybrisConfigDirectory}` * `{ProcessGroup:HybrisConfigDirectory}` * `{ProcessGroup:HybrisDataDirectory}` * `{ProcessGroup:IBMCicsRegion}` * `{ProcessGroup:IBMCicsTransactionGateway}` * `{ProcessGroup:IBMImsConnectRegion}` * `{ProcessGroup:IBMImsControlRegion}` * `{ProcessGroup:IBMImsMessageProcessingRegion}` * `{ProcessGroup:IBMImsSoapGwName}` * `{ProcessGroup:IBMIntegrationNodeName}` * `{ProcessGroup:IBMIntegrationServerName}` * `{ProcessGroup:IISAppPool}` * `{ProcessGroup:IISRoleName}` * `{ProcessGroup:JbossHome}` * `{ProcessGroup:JbossMode}` * `{ProcessGroup:JbossServerName}` * `{ProcessGroup:JavaJarFile}` * `{ProcessGroup:JavaJarPath}` * `{ProcessGroup:JavaMainCLass}` * `{ProcessGroup:KubernetesBasePodName}` * `{ProcessGroup:KubernetesContainerName}` * `{ProcessGroup:KubernetesFullPodName}` * `{ProcessGroup:KubernetesNamespace}` * `{ProcessGroup:KubernetesPodUid}` * `{ProcessGroup:MssqlInstanceName}` * `{ProcessGroup:NodeJsAppBaseDirectory}` * `{ProcessGroup:NodeJsAppName}` * `{ProcessGroup:NodeJsScriptName}` * `{ProcessGroup:OracleSid}` * `{ProcessGroup:PHPScriptPath}` * `{ProcessGroup:PHPWorkingDirectory}` * `{ProcessGroup:Ports}` * `{ProcessGroup:RubyAppRootPath}` * `{ProcessGroup:RubyScriptPath}` * `{ProcessGroup:SoftwareAGInstallRoot}` * `{ProcessGroup:SoftwareAGProductPropertyName}` * `{ProcessGroup:SpringBootAppName}` * `{ProcessGroup:SpringBootProfileName}` * `{ProcessGroup:SpringBootStartupClass}` * `{ProcessGroup:TIBCOBusinessWorksAppNodeName}` * `{ProcessGroup:TIBCOBusinessWorksAppSpaceName}` * `{ProcessGroup:TIBCOBusinessWorksCeAppName}` * `{ProcessGroup:TIBCOBusinessWorksCeVersion}` * `{ProcessGroup:TIBCOBusinessWorksDomainName}` * `{ProcessGroup:TIBCOBusinessWorksEnginePropertyFilePath}` * `{ProcessGroup:TIBCOBusinessWorksEnginePropertyFile}` * `{ProcessGroup:TIBCOBusinessWorksHome}` * `{ProcessGroup:VarnishInstanceName}` * `{ProcessGroup:WebLogicClusterName}` * `{ProcessGroup:WebLogicDomainName}` * `{ProcessGroup:WebLogicHome}` * `{ProcessGroup:WebLogicName}` * `{ProcessGroup:WebSphereCellName}` * `{ProcessGroup:WebSphereClusterName}` * `{ProcessGroup:WebSphereNodeName}` * `{ProcessGroup:WebSphereServerName}` * `{ProcessGroup:ActorSystem}` * `{Service:STGServerName}` * `{Service:DatabaseHostName}` * `{Service:DatabaseName}` * `{Service:DatabaseVendor}` * `{Service:DetectedName}` * `{Service:EndpointPath}` * `{Service:EndpointPathGatewayUrl}` * `{Service:IIBApplicationName}` * `{Service:MessageListenerClassName}` * `{Service:Port}` * `{Service:PublicDomainName}` * `{Service:RemoteEndpoint}` * `{Service:RemoteName}` * `{Service:WebApplicationId}` * `{Service:WebContextRoot}` * `{Service:WebServerName}` * `{Service:WebServiceNamespace}` * `{Service:WebServiceName}` * `{VmwareDatacenter:Name}` * `{VmwareVm:Name}` | Required |
| rules | [EntityRuleEngineCondition[]](#openapi-definition-EntityRuleEngineCondition) | Список условий сопоставления правила.  Правило применяется только если выполнены **все** условия. | Required |
| type | string | Тип сущностей Dynatrace, к которым применяется правило. Элемент может принимать значения * `HOST` * `PROCESS_GROUP` * `SERVICE` | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `EntityRuleEngineCondition`

Условие определяет, как выполняется логика сопоставления для сущности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| comparisonInfo | [ComparisonBasic](#openapi-definition-ComparisonBasic) | Определяет, как фактически выполняется сопоставление: что и как мы сравниваем.  Фактический набор полей и возможные значения поля **operator** зависят от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [JSON models](https://dt-url.net/0b83s6z). | Required |
| key | [ConditionKey](#openapi-definition-ConditionKey) | Ключ для идентификации сопоставляемых данных.  Фактический набор полей и возможные значения зависят от типа ключа. Список фактических объектов см. в описании поля **type** или см. [JSON models](https://dt-url.net/0b83s6z). | Required |

#### Объект `ComparisonBasic`

Определяет, как фактически выполняется сопоставление: что и как мы сравниваем.

Фактический набор полей и возможные значения поля **operator** зависят от типа сравнения. Список фактических объектов см. в описании поля **type** или см. [JSON models](https://dt-url.net/0b83s6z).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| negate | boolean | Инвертирует **operator** сравнения. Например, превращает **begins with** в **does not begin with**. | Required |
| operator | string | Оператор сравнения. Можно инвертировать, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Список фактических моделей см. в описании поля **type** и проверьте описание нужной модели. | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING` -> StringComparison * `INDEXED_NAME` -> IndexedNameComparison * `INDEXED_STRING` -> IndexedStringComparison * `INTEGER` -> IntegerComparison * `SERVICE_TYPE` -> ServiceTypeComparison * `PAAS_TYPE` -> PaasTypeComparison * `CLOUD_TYPE` -> CloudTypeComparison * `AZURE_SKU` -> AzureSkuComparision * `AZURE_COMPUTE_MODE` -> AzureComputeModeComparison * `ENTITY_ID` -> EntityIdComparison * `SIMPLE_TECH` -> SimpleTechComparison * `SIMPLE_HOST_TECH` -> SimpleHostTechComparison * `SERVICE_TOPOLOGY` -> ServiceTopologyComparison * `DATABASE_TOPOLOGY` -> DatabaseTopologyComparison * `OS_TYPE` -> OsTypeComparison * `HYPERVISOR_TYPE` -> HypervisorTypeComparision * `IP_ADDRESS` -> IpAddressComparison * `OS_ARCHITECTURE` -> OsArchitectureComparison * `BITNESS` -> BitnessComparision * `APPLICATION_TYPE` -> ApplicationTypeComparison * `MOBILE_PLATFORM` -> MobilePlatformComparison * `CUSTOM_APPLICATION_TYPE` -> CustomApplicationTypeComparison * `DCRUM_DECODER_TYPE` -> DcrumDecoderComparison * `SYNTHETIC_ENGINE_TYPE` -> SyntheticEngineTypeComparison * `TAG` -> TagComparison * `INDEXED_TAG` -> IndexedTagComparison Элемент может принимать значения * `APPLICATION_TYPE` * `AZURE_COMPUTE_MODE` * `AZURE_SKU` * `BITNESS` * `CLOUD_TYPE` * `CUSTOM_APPLICATION_TYPE` * `DATABASE_TOPOLOGY` * `DCRUM_DECODER_TYPE` * `ENTITY_ID` * `HYPERVISOR_TYPE` * `INDEXED_NAME` * `INDEXED_STRING` * `INDEXED_TAG` * `INTEGER` * `IP_ADDRESS` * `MOBILE_PLATFORM` * `OS_ARCHITECTURE` * `OS_TYPE` * `PAAS_TYPE` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SIMPLE_HOST_TECH` * `SIMPLE_TECH` * `STRING` * `SYNTHETIC_ENGINE_TYPE` * `TAG` | Required |
| value | string | Значение для сравнения. | Optional |

#### Объект `AnyValue`

Схема, представляющая значение произвольного типа.

#### Объект `ConditionKey`

Ключ для идентификации сопоставляемых данных.

Фактический набор полей и возможные значения зависят от типа ключа. Список фактических объектов см. в описании поля **type** или см. [JSON models](https://dt-url.net/0b83s6z).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attribute | string | Атрибут, используемый для сравнения. Элемент может принимать значения * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `AWS_AVAILABILITY_ZONE_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AZURE_ENTITY_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_MGMT_GROUP_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_TENANT_NAME` * `AZURE_TENANT_UUID` * `AZURE_VM_NAME` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `CUSTOM_DEVICE_DETECTED_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_TECHNOLOGY` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `DOCKER_STRIPPED_IMAGE_NAME` * `EC2_INSTANCE_AMI_ID` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `EC2_INSTANCE_TAGS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_NAME` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `ESXI_HOST_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `GEOLOCATION_SITE_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `HOST_ARCHITECTURE` * `HOST_AWS_NAME_TAG` * `HOST_AZURE_COMPUTE_MODE` * `HOST_AZURE_SKU` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BITNESS` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `HOST_CLOUD_TYPE` * `HOST_CPU_CORES` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_HYPERVISOR_TYPE` * `HOST_IP_ADDRESS` * `HOST_KUBERNETES_LABELS` * `HOST_LOGICAL_CPU_CORES` * `HOST_NAME` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `HOST_TAGS` * `HOST_TECHNOLOGY` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `KUBERNETES_CLUSTER_NAME` * `KUBERNETES_NODE_NAME` * `KUBERNETES_SERVICE_NAME` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `NAME_OF_COMPUTE_NODE` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_REGION_NAME` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_VM_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `QUEUE_NAME` * `QUEUE_TECHNOLOGY` * `QUEUE_VENDOR` * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_IIB_APPLICATION_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_TAGS` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` | Required |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `PROCESS_CUSTOM_METADATA_KEY` -> CustomProcessMetadataConditionKey * `HOST_CUSTOM_METADATA_KEY` -> CustomHostMetadataConditionKey * `PROCESS_PREDEFINED_METADATA_KEY` -> ProcessMetadataConditionKey * `STRING` -> StringConditionKey * `STATIC` -> StaticConditionKey Элемент может принимать значения * `HOST_CUSTOM_METADATA_KEY` * `PROCESS_CUSTOM_METADATA_KEY` * `PROCESS_PREDEFINED_METADATA_KEY` * `STATIC` * `STRING` | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"displayName": "TestRule",



"enabled": true,



"id": "4e88530c-edec-4e31-9cb4-3f2c63abc2b7",



"nameFormat": "TestNameFormat",



"rules": [



{



"comparisonInfo": {



"negate": "false",



"operator": "EQUALS",



"type": "SIMPLE_TECH",



"value": {



"type": "JAVA"



}



},



"key": {



"attribute": "PROCESS_GROUP_TECHNOLOGY"



}



},



{



"comparisonInfo": {



"caseSensitive": true,



"negate": "false",



"operator": "CONTAINS",



"type": "STRING",



"value": "test"



},



"key": {



"attribute": "PROCESS_GROUP_PREDEFINED_METADATA",



"dynamicKey": "EXE_NAME",



"type": "PROCESS_PREDEFINED_METADATA_KEY"



}



}



],



"type": "PROCESS_GROUP"



}
```

## Ответ

Запрос возвращает краткое представление вновь созданного правила.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Правило именования создано. Ответ содержит ID нового правила. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

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
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Валидация payload

Рекомендуется проверять payload перед отправкой реального запроса. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Валидация пройдена. Отправленная конфигурация корректна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

## Связанные темы

* [Process group naming](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Способы настройки именования process group.")