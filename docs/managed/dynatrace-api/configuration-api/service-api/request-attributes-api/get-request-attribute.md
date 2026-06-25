---
title: Request attributes API - GET a request attribute
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-attributes-api/get-request-attribute
scraped: 2026-05-12T11:20:32.434311
---

# Request attributes API - GET a request attribute

# Request attributes API - GET a request attribute

* Reference
* Published Sep 03, 2019

Gets parameters of the specified request attribute.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required request attribute. | path | Required |
| includeProcessGroupReferences | boolean | Flag to include process group references to the response.  Process Group group references aren't compatible across environments. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RequestAttribute](#openapi-definition-RequestAttribute) | Success |

### Response body objects

#### The `RequestAttribute` object

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | Aggregation type for the request values. The element can hold these values * `ALL_DISTINCT_VALUES` * `AVERAGE` * `COUNT_DISTINCT_VALUES` * `COUNT_VALUES` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` |
| confidential | boolean | Confidential data flag. Set `true` to treat the captured data as confidential. |
| dataSources | [DataSource[]](#openapi-definition-DataSource) | The list of data sources. |
| dataType | string | The data type of the request attribute. The element can hold these values * `DOUBLE` * `INTEGER` * `STRING` |
| enabled | boolean | The request attribute is enabled (`true`) or disabled (`false`). |
| id | string | The ID of the request attribute. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the request attribute. |
| normalization | string | String values transformation.  If the **dataType** is not `string`, set the `Original` here. The element can hold these values * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| skipPersonalDataMasking | boolean | Personal data masking flag. Set `true` to skip masking.  Warning: This will potentially access personalized data. |

#### The `DataSource` object

| Element | Type | Description |
| --- | --- | --- |
| capturingAndStorageLocation | string | Specifies the location where the values are captured and stored.  Required if the **source** is one of the following: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  Not applicable in other cases.  If the **source** value is `REQUEST_HEADER` or `RESPONSE_HEADER`, the `CAPTURE_AND_STORE_ON_BOTH` location is not allowed. The element can hold these values * `CAPTURE_AND_STORE_ON_BOTH` * `CAPTURE_AND_STORE_ON_CLIENT` * `CAPTURE_AND_STORE_ON_SERVER` * `CAPTURE_ON_CLIENT_STORE_ON_SERVER` |
| cicsSDKMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. |
| cicsTransactionCallType | string | CICS transaction call type condition for which the value is captured.  Required if the **source** is: `CICS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases. The element can hold these values * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` |
| enabled | boolean | The data source is enabled (`true`) or disabled (`false`). |
| iibLabelMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. |
| iibMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. |
| iibNodeType | string | The IBM integration bus node type for which the value is captured.  This, iibNodeTypeCondition (different type of the same field) or `iibMethodNodeCondition` is required if the **source** is: `IIB_NODE`.  Not applicable in other cases. The element can hold these values * `AGGREGATE_CONTROL_NODE` * `AGGREGATE_REPLY_NODE` * `AGGREGATE_REQUEST_NODE` * `CALLABLE_FLOW_REPLY_NODE` * `COLLECTOR_NODE` * `COMPUTE_NODE` * `DATABASE_NODE` * `DATABASE_RETRIEVE_NODE` * `DATABASE_ROUTE_NODE` * `DECISION_SERVICE_NODE` * `DOT_NET_COMPUTE_NODE` * `FILE_READ_NODE` * `FILTER_NODE` * `FLOW_ORDER_NODE` * `GROUP_COMPLETE_NODE` * `GROUP_GATHER_NODE` * `GROUP_SCATTER_NODE` * `HTTP_ASYNC_REQUEST` * `HTTP_ASYNC_RESPONSE` * `HTTP_HEADER` * `HTTP_INPUT` * `HTTP_REPLY` * `HTTP_REQUEST` * `JAVA_COMPUTE_NODE` * `JMS_CLIENT_RECEIVE` * `JMS_CLIENT_REPLY_NODE` * `JMS_HEADER` * `JMS_INPUT_NODE` * `JMS_OUTPUT_NODE` * `JMS_REPLY_NODE` * `MQ_GET_NODE` * `MQ_INPUT_NODE` * `MQ_OUTPUT_NODE` * `MQ_REPLY_NODE` * `PASSTHRU_NODE` * `PUBLICATION_NODE` * `RESET_CONTENT_DESCRIPTOR_NODE` * `REST_ASYNC_REQUEST_NODE` * `REST_ASYNC_RESPONSE_NODE` * `REST_REQUEST_NODE` * `RE_SEQUENCE_NODE` * `ROUTE_NODE` * `SAP_REPLY_NODE` * `SCA_REPLY_NODE` * `SECURITY_PEP` * `SEQUENCE_NODE` * `SOAP_ASYNC_REQUEST_NODE` * `SOAP_ASYNC_RESPONSE_NODE` * `SOAP_EXTRACT_NODE` * `SOAP_INPUT_NODE` * `SOAP_REPLY_NODE` * `SOAP_REQUEST_NODE` * `SOAP_WRAPPER_NODE` * `SR_RETRIEVE_ENTITY_NODE` * `SR_RETRIEVE_IT_SERVICE_NODE` * `THROW_NODE` * `TRACE_NODE` * `TRY_CATCH_NODE` * `VALIDATE_NODE` * `WS_REPLY_NODE` * `XSL_MQSI_NODE` |
| iibNodeTypeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. |
| imsTransactionCallType | string | IMS transaction call type condition for which the value is captured.  Required if the **source** is: `IMS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases. The element can hold these values * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` |
| methods | [CapturedMethod[]](#openapi-definition-CapturedMethod) | The method specification if the **source** value is `METHOD_PARAM`.  Not applicable in other cases. |
| parameterName | string | The name of the web request parameter to capture.  Required if the **source** is one of the following: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  Not applicable in other cases. |
| scope | [ScopeConditions](#openapi-definition-ScopeConditions) | Conditions for data capturing. |
| serverVariableTechnology | string | The technology of the server variable to capture if the **source** value is `SERVER_VARIABLE`. \n\n Not applicable in other cases. The element can hold these values * `ASP_NET` |
| sessionAttributeTechnology | string | The technology of the session attribute to capture if the **source** value is `SESSION_ATTRIBUTE`. \n\n Not applicable in other cases. The element can hold these values * `ASP_NET` * `ASP_NET_CORE` * `JAVA` * `PHP` |
| source | string | The source of the attribute to capture. Works in conjunction with **parameterName** or **methods** and **technology**. The element can hold these values * `CICS_PATH_NAME` * `CICS_SDK` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_CALL_TYPE` * `CICS_TRANSACTION_GROUP_ID` * `CICS_UNIT_OF_WORK_ID` * `CICS_USER_ID` * `CLIENT_IP` * `CUSTOM_ATTRIBUTE` * `DLI_DB_OR_LTERM_NAME` * `DLI_SEGMENT_NAME` * `IIB_LABEL` * `IIB_NODE` * `IMS_TRANSACTION_CALL_TYPE` * `IMS_UNIT_OF_WORK_ID` * `IMS_USER_ID` * `METHOD_PARAM` * `MQ_CORRELATION_ID` * `MQ_MESSAGE_ID` * `MQ_MESSAGE_SIZE` * `POST_PARAMETER` * `QUERY_PARAMETER` * `REQUEST_HEADER` * `RESPONSE_HEADER` * `SERVER_VARIABLE` * `SESSION_ATTRIBUTE` * `SPAN_ATTRIBUTE` * `URI` * `URI_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` |
| spanAttributeKey | string | The key of the span attribute to capture.  Required if the **source** is: `SPAN_ATTRIBUTE`.  Not applicable in other cases. |
| technology | string | The technology of the method to capture if the **source** value is `METHOD_PARAM`. \n\n Not applicable in other cases. The element can hold these values * `DOTNET` * `JAVA` * `PHP` |
| valueProcessing | [ValueProcessing](#openapi-definition-ValueProcessing) | Process values as specified. |

#### The `ValueCondition` object

IBM integration bus label node name condition for which the value is captured.

| Element | Type | Description |
| --- | --- | --- |
| negate | boolean | Negate the comparison. |
| operator | string | Operator comparing the extracted value to the comparison value. The element can hold these values * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` * `NOT_EMPTY` |
| value | string | The value to compare to. |

#### The `CapturedMethod` object

| Element | Type | Description |
| --- | --- | --- |
| argumentIndex | integer | The index of the argument to capture. Set `0` to capture the return value, `1` or higher to capture a mehtod argument.  Required if the **capture** is set to `ARGUMENT`.  Not applicable in other cases. |
| capture | string | What to capture from the method. The element can hold these values * `ARGUMENT` * `CLASS_NAME` * `METHOD_NAME` * `OCCURRENCES` * `SIMPLE_CLASS_NAME` * `THIS` |
| deepObjectAccess | string | The getter chain to apply to the captured object. It is required in one of the following cases:  The **capture** is set to `THIS`. The **capture** is set to `ARGUMENT`, and the argument is not a primitive, a primitive wrapper class, a string, or an array.  Not applicable in other cases. |
| method | [MethodReference](#openapi-definition-MethodReference) | Configuration of a method to be captured. |

#### The `MethodReference` object

Configuration of a method to be captured.

| Element | Type | Description |
| --- | --- | --- |
| argumentTypes | string[] | The list of argument types. |
| className | string | The class name where the method to capture resides.  Either this or the **fileName** must be set. |
| fileName | string | The file name where the method to capture resides.  Either this or **className** must be set. |
| fileNameMatcher | string | The operator of the comparison.  If not set, `EQUALS` is used. The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| methodName | string | The name of the method to capture. |
| modifiers | string[] | The modifiers of the method to capture. The element can hold these values * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` |
| returnType | string | The return type. |
| visibility | string | The visibility of the method to capture. The element can hold these values * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` |

#### The `ScopeConditions` object

Conditions for data capturing.

| Element | Type | Description |
| --- | --- | --- |
| hostGroup | string | Only applies to this host group. |
| processGroup | string | Only applies to this process group. Note that this can't be transferred between different clusters or environments. |
| serviceTechnology | string | Only applies to this service technology. The element can hold these values * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOCKERDEAMON` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MONGODB_ROUTER` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `ZERO_MQ` * `ZOS_CONNECT` |
| tagOfProcessGroup | string | Only apply to process groups matching this tag. |

#### The `ValueProcessing` object

Process values as specified.

| Element | Type | Description |
| --- | --- | --- |
| extractSubstring | [ExtractSubstring](#openapi-definition-ExtractSubstring) | Preprocess by extracting a substring from the original value. |
| splitAt | string | Split (preprocessed) string values at this separator. |
| trim | boolean | Prune Whitespaces. Defaults to false. |
| valueCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. |
| valueExtractorRegex | string | Extract value from captured data per regex. |

#### The `ExtractSubstring` object

Preprocess by extracting a substring from the original value.

| Element | Type | Description |
| --- | --- | --- |
| delimiter | string | The delimiter string. |
| endDelimiter | string | The end-delimiter string.  Required if the **position** value is `BETWEEN`. Otherwise not allowed. |
| position | string | The position of the extracted string relative to delimiters. The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

### Response body JSON models

```
{



"aggregation": "ALL_DISTINCT_VALUES",



"confidential": false,



"dataSources": [



{



"capturingAndStorageLocation": "CAPTURE_AND_STORE_ON_SERVER",



"enabled": true,



"parameterName": "query",



"scope": {



"tagOfProcessGroup": "SearchFrontend"



},



"source": "QUERY_PARAMETER"



}



],



"dataType": "STRING",



"enabled": true,



"name": "Query Term",



"normalization": "TO_LOWER_CASE",



"skipPersonalDataMasking": false



}
```

## Related topics

* [Request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")