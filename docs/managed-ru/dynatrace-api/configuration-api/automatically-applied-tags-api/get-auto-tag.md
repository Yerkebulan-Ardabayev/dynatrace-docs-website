---
title: Automatically applied tags API - GET an auto-tag
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-auto-tag
scraped: 2026-05-12T12:15:58.515712
---

# Automatically applied tags API - GET an auto-tag

# Automatically applied tags API - GET an auto-tag

* Reference
* Published Aug 09, 2019

Устарело

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "Просмотр таблицы schema builtin:tags.auto-tagging окружения мониторинга через Dynatrace API.") (`builtin:tags.auto-tagging`).

Возвращает параметры указанного автоматически применяемого тега.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/autoTags/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/autoTags/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного автоматически применяемого тега. | path | Required |
| includeProcessGroupReferences | boolean | Флаг для включения ссылок на группы процессов в ответ.  Ссылки на группы процессов несовместимы между окружениями.  Когда этот флаг установлен в `false`, условия со ссылками на группы процессов удаляются. Если в результате у правила не остаётся условий, всё правило удаляется. | query | Optional |

## Ответ

Смотрите [JSON models](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/models "Изучите вариации JSON-моделей в Dynatrace API автоматически применяемых тегов.") для всех JSON-моделей, которые зависят от **type** модели.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AutoTag](#openapi-definition-AutoTag) | Успех |

### Объекты тела ответа

#### Объект `AutoTag`

Конфигурация автоматически применяемого тега. Определяет условия применения тега и значение тега.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Описание автоматически применяемого тега. |
| entitySelectorBasedRules | [EntitySelectorBasedAutoTagRule[]](#openapi-definition-EntitySelectorBasedAutoTagRule) | Список правил на основе селектора сущностей для применения автотегирования.  Если указано несколько правил, применяется логика **OR**. |
| id | string | ID автоматически применяемого тега. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| name | string | Имя автоматически применяемого тега, которое применяется к сущностям.  Дополнительно вы можете указать **valueFormat** в правиле тега. В этом случае тег используется в формате `name:valueFormat`.  Например, вы можете расширить тег `Infrastructure` до `Infrastructure:Windows` и `Infrastructure:Linux`. |
| rules | [AutoTagRule[]](#openapi-definition-AutoTagRule) | Список правил применения тега.  При наличии нескольких правил применяется логика OR. |

#### Объект `EntitySelectorBasedAutoTagRule`

Правило на основе селектора сущностей для применения тега. Позволяет тегировать сущности через селектор сущностей.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| entitySelector | string | Строка селектора сущностей, по которой выбираются сущности. |
| normalization | string | Изменения, применяемые к значению после применения формата значения. По умолчанию LEAVE\_TEXT\_AS\_IS. Возможные значения: * `LEAVE_TEXT_AS_IS` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| valueFormat | string | Значение автоматически применяемого тега на основе селектора сущностей. Если указано, тег используется в формате `name:valueFormat`.  Например, вы можете расширить тег `Infrastructure` до `Infrastructure:Windows` и `Infrastructure:Linux`. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AutoTagRule`

Правило для автоматически применяемого тега.

Определяет условия применения тега.

| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [EntityRuleEngineCondition[]](#openapi-definition-EntityRuleEngineCondition) | Список правил сопоставления для автоматически применяемого тега.  Тег применяется только когда выполнены **все** условия. |
| enabled | boolean | Правило тега включено (`true`) или отключено (`false`). |
| normalization | string | Изменения, применяемые к значению после применения формата значения. По умолчанию LEAVE\_TEXT\_AS\_IS. Возможные значения: * `LEAVE_TEXT_AS_IS` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| propagationTypes | string[] | Как применять тег к нижележащим сущностям:  * `SERVICE_TO_PROCESS_GROUP_LIKE`: применить к нижележащим группам процессов подходящих сервисов. * `SERVICE_TO_HOST_LIKE`: применить к нижележащим хостам подходящих сервисов. * `PROCESS_GROUP_TO_HOST`: применить к нижележащим хостам подходящих групп процессов. * `PROCESS_GROUP_TO_SERVICE`: применить ко всем сервисам, предоставляемым группами процессов. * `HOST_TO_PROCESS_GROUP_INSTANCE`: применить к процессам, работающим на подходящих хостах. * `AZURE_TO_PG`: применить к группам процессов, связанным с подходящими сущностями Azure. * `AZURE_TO_SERVICE`: применить к сервисам, предоставляемым подходящими сущностями Azure. Возможные значения: * `AZURE_TO_PG` * `AZURE_TO_SERVICE` * `HOST_TO_PROCESS_GROUP_INSTANCE` * `PROCESS_GROUP_TO_HOST` * `PROCESS_GROUP_TO_SERVICE` * `SERVICE_TO_HOST_LIKE` * `SERVICE_TO_PROCESS_GROUP_LIKE` |
| type | string | Тип сущностей, к которым применяется правило. Возможные значения: * `APPLICATION` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_CLASSIC_LOAD_BALANCER` * `AWS_NETWORK_LOAD_BALANCER` * `AWS_RELATIONAL_DATABASE_SERVICE` * `AZURE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `DCRUM_APPLICATION` * `ESXI_HOST` * `EXTERNAL_SYNTHETIC_TEST` * `HOST` * `HTTP_CHECK` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `PROCESS_GROUP` * `SERVICE` * `SYNTHETIC_TEST` |
| valueFormat | string | Значение автоматически применяемого тега. Если указано, тег используется в формате `name:valueFormat`.  Например, вы можете расширить тег `Infrastructure` до `Infrastructure:Windows` и `Infrastructure:Linux`.  Здесь можно использовать следующие плейсхолдеры:  * `{AwsAutoScalingGroup:Name}` * `{AwsAvailabilityZone:Name}` * `{AwsElasticLoadBalancer:Name}` * `{AwsRelationalDatabaseService:DBName}` * `{AwsRelationalDatabaseService:Endpoint}` * `{AwsRelationalDatabaseService:Engine}` * `{AwsRelationalDatabaseService:InstanceClass}` * `{AwsRelationalDatabaseService:Name}` * `{AwsRelationalDatabaseService:Port}` * `{AzureRegion:Name}` * `{AzureScaleSet:Name}` * `{AzureVm:Name}` * `{CloudFoundryOrganization:Name}` * `{CustomDevice:DetectedName}` * `{CustomDevice:DnsName}` * `{CustomDevice:IpAddress}` * `{CustomDevice:Port}` * `{DockerContainerGroupInstance:ContainerName}` * `{DockerContainerGroupInstance:FullImageName}` * `{DockerContainerGroupInstance:ImageVersion}` * `{ESXIHost:HardwareModel}` * `{ESXIHost:HardwareVendor}` * `{ESXIHost:Name}` * `{ESXIHost:ProductName}` * `{ESXIHost:ProductVersion}` * `{Ec2Instance:AmiId}` * `{Ec2Instance:BeanstalkEnvironmentName}` * `{Ec2Instance:InstanceId}` * `{Ec2Instance:InstanceType}` * `{Ec2Instance:LocalHostName}` * `{Ec2Instance:Name}` * `{Ec2Instance:PublicHostName}` * `{Ec2Instance:SecurityGroup}` * `{GoogleComputeInstance:Id}` * `{GoogleComputeInstance:IpAddresses}` * `{GoogleComputeInstance:MachineType}` * `{GoogleComputeInstance:Name}` * `{GoogleComputeInstance:ProjectId}` * `{GoogleComputeInstance:Project}` * `{Host:AWSNameTag}` * `{Host:AixLogicalCpuCount}` * `{Host:AzureHostName}` * `{Host:AzureSiteName}` * `{Host:BoshDeploymentId}` * `{Host:BoshInstanceId}` * `{Host:BoshInstanceName}` * `{Host:BoshName}` * `{Host:BoshStemcellVersion}` * `{Host:CpuCores}` * `{Host:DetectedName}` * `{Host:Environment:AppName}` * `{Host:Environment:BoshReleaseVersion}` * `{Host:Environment:Environment}` * `{Host:Environment:Link}` * `{Host:Environment:Organization}` * `{Host:Environment:Owner}` * `{Host:Environment:Support}` * `{Host:IpAddress}` * `{Host:LogicalCpuCores}` * `{Host:OneAgentCustomHostName}` * `{Host:OperatingSystemVersion}` * `{Host:PaasMemoryLimit}` * `{HostGroup:Name}` * `{KubernetesCluster:Name}` * `{KubernetesNode:DetectedName}` * `{OpenstackAvailabilityZone:Name}` * `{OpenstackZone:Name}` * `{OpenstackComputeNode:Name}` * `{OpenstackProject:Name}` * `{OpenstackVm:UnstanceType}` * `{OpenstackVm:Name}` * `{OpenstackVm:SecurityGroup}` * `{ProcessGroup:AmazonECRImageAccountId}` * `{ProcessGroup:AmazonECRImageRegion}` * `{ProcessGroup:AmazonECSCluster}` * `{ProcessGroup:AmazonECSContainerName}` * `{ProcessGroup:AmazonECSFamily}` * `{ProcessGroup:AmazonECSRevision}` * `{ProcessGroup:AmazonLambdaFunctionName}` * `{ProcessGroup:AmazonRegion}` * `{ProcessGroup:ApacheConfigPath}` * `{ProcessGroup:ApacheSparkMasterIpAddress}` * `{ProcessGroup:AspDotNetCoreApplicationPath}` * `{ProcessGroup:AspDotNetCoreApplicationPath}` * `{ProcessGroup:AzureHostName}` * `{ProcessGroup:AzureSiteName}` * `{ProcessGroup:CassandraClusterName}` * `{ProcessGroup:CatalinaBase}` * `{ProcessGroup:CatalinaHome}` * `{ProcessGroup:CloudFoundryAppId}` * `{ProcessGroup:CloudFoundryAppName}` * `{ProcessGroup:CloudFoundryInstanceIndex}` * `{ProcessGroup:CloudFoundrySpaceId}` * `{ProcessGroup:CloudFoundrySpaceName}` * `{ProcessGroup:ColdFusionJvmConfigFile}` * `{ProcessGroup:ColdFusionServiceName}` * `{ProcessGroup:CommandLineArgs}` * `{ProcessGroup:DetectedName}` * `{ProcessGroup:DotNetCommandPath}` * `{ProcessGroup:DotNetCommand}` * `{ProcessGroup:DotNetClusterId}` * `{ProcessGroup:DotNetNodeId}` * `{ProcessGroup:ElasticsearchClusterName}` * `{ProcessGroup:ElasticsearchNodeName}` * `{ProcessGroup:EquinoxConfigPath}` * `{ProcessGroup:ExeName}` * `{ProcessGroup:ExePath}` * `{ProcessGroup:GlassFishDomainName}` * `{ProcessGroup:GlassFishInstanceName}` * `{ProcessGroup:GoogleAppEngineInstance}` * `{ProcessGroup:GoogleAppEngineService}` * `{ProcessGroup:GoogleCloudProject}` * `{ProcessGroup:HybrisBinDirectory}` * `{ProcessGroup:HybrisConfigDirectory}` * `{ProcessGroup:HybrisConfigDirectory}` * `{ProcessGroup:HybrisDataDirectory}` * `{ProcessGroup:IBMCicsRegion}` * `{ProcessGroup:IBMCicsTransactionGateway}` * `{ProcessGroup:IBMImsConnectRegion}` * `{ProcessGroup:IBMImsControlRegion}` * `{ProcessGroup:IBMImsMessageProcessingRegion}` * `{ProcessGroup:IBMImsSoapGwName}` * `{ProcessGroup:IBMIntegrationNodeName}` * `{ProcessGroup:IBMIntegrationServerName}` * `{ProcessGroup:IISAppPool}` * `{ProcessGroup:IISRoleName}` * `{ProcessGroup:JbossHome}` * `{ProcessGroup:JbossMode}` * `{ProcessGroup:JbossServerName}` * `{ProcessGroup:JavaJarFile}` * `{ProcessGroup:JavaJarPath}` * `{ProcessGroup:JavaMainCLass}` * `{ProcessGroup:KubernetesBasePodName}` * `{ProcessGroup:KubernetesContainerName}` * `{ProcessGroup:KubernetesFullPodName}` * `{ProcessGroup:KubernetesNamespace}` * `{ProcessGroup:KubernetesPodUid}` * `{ProcessGroup:MssqlInstanceName}` * `{ProcessGroup:NodeJsAppBaseDirectory}` * `{ProcessGroup:NodeJsAppName}` * `{ProcessGroup:NodeJsScriptName}` * `{ProcessGroup:OracleSid}` * `{ProcessGroup:PHPScriptPath}` * `{ProcessGroup:PHPWorkingDirectory}` * `{ProcessGroup:Ports}` * `{ProcessGroup:RubyAppRootPath}` * `{ProcessGroup:RubyScriptPath}` * `{ProcessGroup:SoftwareAGInstallRoot}` * `{ProcessGroup:SoftwareAGProductPropertyName}` * `{ProcessGroup:SpringBootAppName}` * `{ProcessGroup:SpringBootProfileName}` * `{ProcessGroup:SpringBootStartupClass}` * `{ProcessGroup:TIBCOBusinessWorksAppNodeName}` * `{ProcessGroup:TIBCOBusinessWorksAppSpaceName}` * `{ProcessGroup:TIBCOBusinessWorksCeAppName}` * `{ProcessGroup:TIBCOBusinessWorksCeVersion}` * `{ProcessGroup:TIBCOBusinessWorksDomainName}` * `{ProcessGroup:TIBCOBusinessWorksEnginePropertyFilePath}` * `{ProcessGroup:TIBCOBusinessWorksEnginePropertyFile}` * `{ProcessGroup:TIBCOBusinessWorksHome}` * `{ProcessGroup:VarnishInstanceName}` * `{ProcessGroup:WebLogicClusterName}` * `{ProcessGroup:WebLogicDomainName}` * `{ProcessGroup:WebLogicHome}` * `{ProcessGroup:WebLogicName}` * `{ProcessGroup:WebSphereCellName}` * `{ProcessGroup:WebSphereClusterName}` * `{ProcessGroup:WebSphereNodeName}` * `{ProcessGroup:WebSphereServerName}` * `{ProcessGroup:ActorSystem}` * `{Service:STGServerName}` * `{Service:DatabaseHostName}` * `{Service:DatabaseName}` * `{Service:DatabaseVendor}` * `{Service:DetectedName}` * `{Service:EndpointPath}` * `{Service:EndpointPathGatewayUrl}` * `{Service:IIBApplicationName}` * `{Service:MessageListenerClassName}` * `{Service:Port}` * `{Service:PublicDomainName}` * `{Service:RemoteEndpoint}` * `{Service:RemoteName}` * `{Service:WebApplicationId}` * `{Service:WebContextRoot}` * `{Service:WebServerName}` * `{Service:WebServiceNamespace}` * `{Service:WebServiceName}` * `{VmwareDatacenter:Name}` * `{VmwareVm:Name}` |

#### Объект `EntityRuleEngineCondition`

Условие определяет, как выполнять логику сопоставления для сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| comparisonInfo | [ComparisonBasic](#openapi-definition-ComparisonBasic) | Определяет, как именно выполняется сопоставление: что и как мы сравниваем.  Фактический набор полей и возможные значения поля **operator** зависят от типа сравнения. Найдите список фактических объектов в описании поля **type** или смотрите [JSON models](https://dt-url.net/0b83s6z). |
| key | [ConditionKey](#openapi-definition-ConditionKey) | Ключ для идентификации сопоставляемых данных.  Фактический набор полей и возможные значения зависят от типа ключа. Найдите список фактических объектов в описании поля **type** или смотрите [JSON models](https://dt-url.net/0b83s6z). |

#### Объект `ComparisonBasic`

Определяет, как именно выполняется сопоставление: что и как мы сравниваем.

Фактический набор полей и возможные значения поля **operator** зависят от типа сравнения. Найдите список фактических объектов в описании поля **type** или смотрите [JSON models](https://dt-url.net/0b83s6z).

| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертирует **operator** сравнения. Например, превращает **begins with** в **does not begin with**. |
| operator | string | Оператор сравнения. Вы можете инвертировать его, установив **negate** в `true`.  Возможные значения зависят от **type** сравнения. Найдите список фактических моделей в описании поля **type** и проверьте описание нужной вам модели. |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING` -> StringComparison * `INDEXED_NAME` -> IndexedNameComparison * `INDEXED_STRING` -> IndexedStringComparison * `INTEGER` -> IntegerComparison * `SERVICE_TYPE` -> ServiceTypeComparison * `PAAS_TYPE` -> PaasTypeComparison * `CLOUD_TYPE` -> CloudTypeComparison * `AZURE_SKU` -> AzureSkuComparision * `AZURE_COMPUTE_MODE` -> AzureComputeModeComparison * `ENTITY_ID` -> EntityIdComparison * `SIMPLE_TECH` -> SimpleTechComparison * `SIMPLE_HOST_TECH` -> SimpleHostTechComparison * `SERVICE_TOPOLOGY` -> ServiceTopologyComparison * `DATABASE_TOPOLOGY` -> DatabaseTopologyComparison * `OS_TYPE` -> OsTypeComparison * `HYPERVISOR_TYPE` -> HypervisorTypeComparision * `IP_ADDRESS` -> IpAddressComparison * `OS_ARCHITECTURE` -> OsArchitectureComparison * `BITNESS` -> BitnessComparision * `APPLICATION_TYPE` -> ApplicationTypeComparison * `MOBILE_PLATFORM` -> MobilePlatformComparison * `CUSTOM_APPLICATION_TYPE` -> CustomApplicationTypeComparison * `DCRUM_DECODER_TYPE` -> DcrumDecoderComparison * `SYNTHETIC_ENGINE_TYPE` -> SyntheticEngineTypeComparison * `TAG` -> TagComparison * `INDEXED_TAG` -> IndexedTagComparison Возможные значения: * `APPLICATION_TYPE` * `AZURE_COMPUTE_MODE` * `AZURE_SKU` * `BITNESS` * `CLOUD_TYPE` * `CUSTOM_APPLICATION_TYPE` * `DATABASE_TOPOLOGY` * `DCRUM_DECODER_TYPE` * `ENTITY_ID` * `HYPERVISOR_TYPE` * `INDEXED_NAME` * `INDEXED_STRING` * `INDEXED_TAG` * `INTEGER` * `IP_ADDRESS` * `MOBILE_PLATFORM` * `OS_ARCHITECTURE` * `OS_TYPE` * `PAAS_TYPE` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SIMPLE_HOST_TECH` * `SIMPLE_TECH` * `STRING` * `SYNTHETIC_ENGINE_TYPE` * `TAG` |
| value | string | Значение для сравнения. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `ConditionKey`

Ключ для идентификации сопоставляемых данных.

Фактический набор полей и возможные значения зависят от типа ключа. Найдите список фактических объектов в описании поля **type** или смотрите [JSON models](https://dt-url.net/0b83s6z).

| Элемент | Тип | Описание |
| --- | --- | --- |
| attribute | string | Атрибут, используемый для сравнения. Возможные значения: * `APPMON_SERVER_NAME` * `APPMON_SYSTEM_PROFILE_NAME` * `AWS_ACCOUNT_ID` * `AWS_ACCOUNT_NAME` * `AWS_APPLICATION_LOAD_BALANCER_NAME` * `AWS_APPLICATION_LOAD_BALANCER_TAGS` * `AWS_AUTO_SCALING_GROUP_NAME` * `AWS_AUTO_SCALING_GROUP_TAGS` * `AWS_AVAILABILITY_ZONE_NAME` * `AWS_CLASSIC_LOAD_BALANCER_FRONTEND_PORTS` * `AWS_CLASSIC_LOAD_BALANCER_NAME` * `AWS_CLASSIC_LOAD_BALANCER_TAGS` * `AWS_NETWORK_LOAD_BALANCER_NAME` * `AWS_NETWORK_LOAD_BALANCER_TAGS` * `AWS_RELATIONAL_DATABASE_SERVICE_DB_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_ENDPOINT` * `AWS_RELATIONAL_DATABASE_SERVICE_ENGINE` * `AWS_RELATIONAL_DATABASE_SERVICE_INSTANCE_CLASS` * `AWS_RELATIONAL_DATABASE_SERVICE_NAME` * `AWS_RELATIONAL_DATABASE_SERVICE_PORT` * `AWS_RELATIONAL_DATABASE_SERVICE_TAGS` * `AZURE_ENTITY_NAME` * `AZURE_ENTITY_TAGS` * `AZURE_MGMT_GROUP_NAME` * `AZURE_MGMT_GROUP_UUID` * `AZURE_REGION_NAME` * `AZURE_SCALE_SET_NAME` * `AZURE_SUBSCRIPTION_NAME` * `AZURE_SUBSCRIPTION_UUID` * `AZURE_TENANT_NAME` * `AZURE_TENANT_UUID` * `AZURE_VM_NAME` * `BROWSER_MONITOR_NAME` * `BROWSER_MONITOR_TAGS` * `CLOUD_APPLICATION_LABELS` * `CLOUD_APPLICATION_NAME` * `CLOUD_APPLICATION_NAMESPACE_LABELS` * `CLOUD_APPLICATION_NAMESPACE_NAME` * `CLOUD_FOUNDRY_FOUNDATION_NAME` * `CLOUD_FOUNDRY_ORG_NAME` * `CUSTOM_APPLICATION_NAME` * `CUSTOM_APPLICATION_PLATFORM` * `CUSTOM_APPLICATION_TAGS` * `CUSTOM_APPLICATION_TYPE` * `CUSTOM_DEVICE_DETECTED_NAME` * `CUSTOM_DEVICE_DNS_ADDRESS` * `CUSTOM_DEVICE_GROUP_NAME` * `CUSTOM_DEVICE_GROUP_TAGS` * `CUSTOM_DEVICE_IP_ADDRESS` * `CUSTOM_DEVICE_METADATA` * `CUSTOM_DEVICE_NAME` * `CUSTOM_DEVICE_PORT` * `CUSTOM_DEVICE_TAGS` * `CUSTOM_DEVICE_TECHNOLOGY` * `DATA_CENTER_SERVICE_DECODER_TYPE` * `DATA_CENTER_SERVICE_IP_ADDRESS` * `DATA_CENTER_SERVICE_METADATA` * `DATA_CENTER_SERVICE_NAME` * `DATA_CENTER_SERVICE_PORT` * `DATA_CENTER_SERVICE_TAGS` * `DOCKER_CONTAINER_NAME` * `DOCKER_FULL_IMAGE_NAME` * `DOCKER_IMAGE_VERSION` * `DOCKER_STRIPPED_IMAGE_NAME` * `EC2_INSTANCE_AMI_ID` * `EC2_INSTANCE_AWS_INSTANCE_TYPE` * `EC2_INSTANCE_AWS_SECURITY_GROUP` * `EC2_INSTANCE_BEANSTALK_ENV_NAME` * `EC2_INSTANCE_ID` * `EC2_INSTANCE_NAME` * `EC2_INSTANCE_PRIVATE_HOST_NAME` * `EC2_INSTANCE_PUBLIC_HOST_NAME` * `EC2_INSTANCE_TAGS` * `ENTERPRISE_APPLICATION_DECODER_TYPE` * `ENTERPRISE_APPLICATION_IP_ADDRESS` * `ENTERPRISE_APPLICATION_METADATA` * `ENTERPRISE_APPLICATION_NAME` * `ENTERPRISE_APPLICATION_PORT` * `ENTERPRISE_APPLICATION_TAGS` * `ESXI_HOST_CLUSTER_NAME` * `ESXI_HOST_HARDWARE_MODEL` * `ESXI_HOST_HARDWARE_VENDOR` * `ESXI_HOST_NAME` * `ESXI_HOST_PRODUCT_NAME` * `ESXI_HOST_PRODUCT_VERSION` * `ESXI_HOST_TAGS` * `EXTERNAL_MONITOR_ENGINE_DESCRIPTION` * `EXTERNAL_MONITOR_ENGINE_NAME` * `EXTERNAL_MONITOR_ENGINE_TYPE` * `EXTERNAL_MONITOR_NAME` * `EXTERNAL_MONITOR_TAGS` * `GEOLOCATION_SITE_NAME` * `GOOGLE_CLOUD_PLATFORM_ZONE_NAME` * `GOOGLE_COMPUTE_INSTANCE_ID` * `GOOGLE_COMPUTE_INSTANCE_MACHINE_TYPE` * `GOOGLE_COMPUTE_INSTANCE_NAME` * `GOOGLE_COMPUTE_INSTANCE_PROJECT` * `GOOGLE_COMPUTE_INSTANCE_PROJECT_ID` * `GOOGLE_COMPUTE_INSTANCE_PUBLIC_IP_ADDRESSES` * `HOST_AIX_LOGICAL_CPU_COUNT` * `HOST_AIX_SIMULTANEOUS_THREADS` * `HOST_AIX_VIRTUAL_CPU_COUNT` * `HOST_ARCHITECTURE` * `HOST_AWS_NAME_TAG` * `HOST_AZURE_COMPUTE_MODE` * `HOST_AZURE_SKU` * `HOST_AZURE_WEB_APPLICATION_HOST_NAMES` * `HOST_AZURE_WEB_APPLICATION_SITE_NAMES` * `HOST_BITNESS` * `HOST_BOSH_AVAILABILITY_ZONE` * `HOST_BOSH_DEPLOYMENT_ID` * `HOST_BOSH_INSTANCE_ID` * `HOST_BOSH_INSTANCE_NAME` * `HOST_BOSH_NAME` * `HOST_BOSH_STEMCELL_VERSION` * `HOST_CLOUD_TYPE` * `HOST_CPU_CORES` * `HOST_CUSTOM_METADATA` * `HOST_DETECTED_NAME` * `HOST_GROUP_ID` * `HOST_GROUP_NAME` * `HOST_HYPERVISOR_TYPE` * `HOST_IP_ADDRESS` * `HOST_KUBERNETES_LABELS` * `HOST_LOGICAL_CPU_CORES` * `HOST_NAME` * `HOST_ONEAGENT_CUSTOM_HOST_NAME` * `HOST_OS_TYPE` * `HOST_OS_VERSION` * `HOST_PAAS_MEMORY_LIMIT` * `HOST_PAAS_TYPE` * `HOST_TAGS` * `HOST_TECHNOLOGY` * `HTTP_MONITOR_NAME` * `HTTP_MONITOR_TAGS` * `KUBERNETES_CLUSTER_NAME` * `KUBERNETES_NODE_NAME` * `KUBERNETES_SERVICE_NAME` * `MOBILE_APPLICATION_NAME` * `MOBILE_APPLICATION_PLATFORM` * `MOBILE_APPLICATION_TAGS` * `NAME_OF_COMPUTE_NODE` * `NETWORK_AVAILABILITY_MONITOR_NAME` * `NETWORK_AVAILABILITY_MONITOR_TAGS` * `OPENSTACK_ACCOUNT_NAME` * `OPENSTACK_ACCOUNT_PROJECT_NAME` * `OPENSTACK_AVAILABILITY_ZONE_NAME` * `OPENSTACK_PROJECT_NAME` * `OPENSTACK_REGION_NAME` * `OPENSTACK_VM_INSTANCE_TYPE` * `OPENSTACK_VM_NAME` * `OPENSTACK_VM_SECURITY_GROUP` * `PROCESS_GROUP_AZURE_HOST_NAME` * `PROCESS_GROUP_AZURE_SITE_NAME` * `PROCESS_GROUP_CUSTOM_METADATA` * `PROCESS_GROUP_DETECTED_NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_LISTEN_PORT` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_PREDEFINED_METADATA` * `PROCESS_GROUP_TAGS` * `PROCESS_GROUP_TECHNOLOGY` * `PROCESS_GROUP_TECHNOLOGY_EDITION` * `PROCESS_GROUP_TECHNOLOGY_VERSION` * `QUEUE_NAME` * `QUEUE_TECHNOLOGY` * `QUEUE_VENDOR` * `SERVICE_AKKA_ACTOR_SYSTEM` * `SERVICE_CTG_SERVICE_NAME` * `SERVICE_DATABASE_HOST_NAME` * `SERVICE_DATABASE_NAME` * `SERVICE_DATABASE_TOPOLOGY` * `SERVICE_DATABASE_VENDOR` * `SERVICE_DETECTED_NAME` * `SERVICE_ESB_APPLICATION_NAME` * `SERVICE_IBM_CTG_GATEWAY_URL` * `SERVICE_IIB_APPLICATION_NAME` * `SERVICE_MESSAGING_LISTENER_CLASS_NAME` * `SERVICE_NAME` * `SERVICE_PORT` * `SERVICE_PUBLIC_DOMAIN_NAME` * `SERVICE_REMOTE_ENDPOINT` * `SERVICE_REMOTE_SERVICE_NAME` * `SERVICE_TAGS` * `SERVICE_TECHNOLOGY` * `SERVICE_TECHNOLOGY_EDITION` * `SERVICE_TECHNOLOGY_VERSION` * `SERVICE_TOPOLOGY` * `SERVICE_TYPE` * `SERVICE_WEB_APPLICATION_ID` * `SERVICE_WEB_CONTEXT_ROOT` * `SERVICE_WEB_SERVER_ENDPOINT` * `SERVICE_WEB_SERVER_NAME` * `SERVICE_WEB_SERVICE_NAME` * `SERVICE_WEB_SERVICE_NAMESPACE` * `VMWARE_DATACENTER_NAME` * `VMWARE_VM_NAME` * `WEB_APPLICATION_NAME` * `WEB_APPLICATION_NAME_PATTERN` * `WEB_APPLICATION_TAGS` * `WEB_APPLICATION_TYPE` |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `PROCESS_CUSTOM_METADATA_KEY` -> CustomProcessMetadataConditionKey * `HOST_CUSTOM_METADATA_KEY` -> CustomHostMetadataConditionKey * `PROCESS_PREDEFINED_METADATA_KEY` -> ProcessMetadataConditionKey * `STRING` -> StringConditionKey * `STATIC` -> StaticConditionKey Возможные значения: * `HOST_CUSTOM_METADATA_KEY` * `PROCESS_CUSTOM_METADATA_KEY` * `PROCESS_PREDEFINED_METADATA_KEY` * `STATIC` * `STRING` |

### JSON-модели тела ответа

```
{



"description": "sampleDescription",



"entitySelectorBasedRules": [



{



"enabled": true,



"entitySelector": "type(HOST) AND cpuCores(4)"



}



],



"name": "sampleAutoTag",



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



"type": "SERVICE",



"valueFormat": "myTagValue {Service:DetectedName}"



}



]



}
```

## Пример

В этом примере запрос запрашивает свойства автоматически применяемого тега **Infrastructure - Linux** с ID **7c82c170-b380-4fa7-992a-453f3e73047b**.

Конфигурация имеет следующие настройки:

![GET example](https://dt-cdn.net/images/get-example-1036-b0d81737f7.png)

GET example

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/autoTags/7c82c170-b380-4fa7-992a-453f3e73047b \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/autoTags/7c82c170-b380-4fa7-992a-453f3e73047b
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



7



],



"clusterVersion": "1.176.0.20190808-181828"



},



"id": "7c82c170-b380-4fa7-992a-453f3e73047b",



"name": "Infrastructure - Linux",



"rules": [



{



"type": "HOST",



"enabled": true,



"valueFormat": "prodLinux",



"propagationTypes": [],



"conditions": [



{



"key": {



"attribute": "HOST_OS_TYPE"



},



"comparisonInfo": {



"type": "OS_TYPE",



"operator": "EQUALS",



"value": "LINUX",



"negate": false



}



},



{



"key": {



"attribute": "HOST_NAME"



},



"comparisonInfo": {



"type": "STRING",



"operator": "BEGINS_WITH",



"value": "PreProd",



"negate": true,



"caseSensitive": true



}



}



]



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")
* [Теги и метаданные](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")