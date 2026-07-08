---
title: Request attributes API - PUT a request attribute
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-attributes-api/put-request-attribute
---

# Request attributes API - PUT a request attribute

# Request attributes API - PUT a request attribute

* Reference
* Published Sep 03, 2019

Updates the specified request attribute.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |

## Authentication

To execute this request, you need an access token with `CaptureRequestData` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the request attribute to be updated.  If you set the ID in the body as well, it must match this ID. | path | Required |
| body | [RequestAttribute](#openapi-definition-RequestAttribute) | - | body | Required |

### Request body objects

#### The `RequestAttribute` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | Aggregation type for the request values. The element can hold these values * `ALL_DISTINCT_VALUES` * `AVERAGE` * `COUNT_DISTINCT_VALUES` * `COUNT_VALUES` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Required |
| confidential | boolean | Confidential data flag. Set `true` to treat the captured data as confidential. | Required |
| dataSources | [DataSource](#openapi-definition-DataSource)[] | The list of data sources. | Required |
| dataType | string | The data type of the request attribute. The element can hold these values * `DOUBLE` * `INTEGER` * `STRING` | Required |
| enabled | boolean | The request attribute is enabled (`true`) or disabled (`false`). | Required |
| id | string | The ID of the request attribute. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| name | string | The name of the request attribute. | Required |
| normalization | string | String values transformation.  If the **dataType** is not `string`, set the `Original` here. The element can hold these values * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Required |
| skipPersonalDataMasking | boolean | Personal data masking flag. Set `true` to skip masking.  Warning: This will potentially access personalized data. | Required |

#### The `DataSource` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| capturingAndStorageLocation | string | Specifies the location where the values are captured and stored.  Required if the **source** is one of the following: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  Not applicable in other cases.  If the **source** value is `REQUEST_HEADER` or `RESPONSE_HEADER`, the `CAPTURE_AND_STORE_ON_BOTH` location is not allowed. The element can hold these values * `CAPTURE_AND_STORE_ON_BOTH` * `CAPTURE_AND_STORE_ON_CLIENT` * `CAPTURE_AND_STORE_ON_SERVER` * `CAPTURE_ON_CLIENT_STORE_ON_SERVER` | Optional |
| cicsSDKMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. | Optional |
| cicsTransactionCallType | string | CICS transaction call type condition for which the value is captured.  Required if the **source** is: `CICS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases. The element can hold these values * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` | Optional |
| enabled | boolean | The data source is enabled (`true`) or disabled (`false`). | Required |
| iibLabelMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. | Optional |
| iibMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. | Optional |
| iibNodeType | string | The IBM integration bus node type for which the value is captured.  This, iibNodeTypeCondition (different type of the same field) or `iibMethodNodeCondition` is required if the **source** is: `IIB_NODE`.  Not applicable in other cases. The element can hold these values * `AGGREGATE_CONTROL_NODE` * `AGGREGATE_REPLY_NODE` * `AGGREGATE_REQUEST_NODE` * `CALLABLE_FLOW_REPLY_NODE` * `COLLECTOR_NODE` * `COMPUTE_NODE` * `DATABASE_NODE` * `DATABASE_RETRIEVE_NODE` * `DATABASE_ROUTE_NODE` * `DECISION_SERVICE_NODE` * `DOT_NET_COMPUTE_NODE` * `FILE_READ_NODE` * `FILTER_NODE` * `FLOW_ORDER_NODE` * `GROUP_COMPLETE_NODE` * `GROUP_GATHER_NODE` * `GROUP_SCATTER_NODE` * `HTTP_ASYNC_REQUEST` * `HTTP_ASYNC_RESPONSE` * `HTTP_HEADER` * `HTTP_INPUT` * `HTTP_REPLY` * `HTTP_REQUEST` * `JAVA_COMPUTE_NODE` * `JMS_CLIENT_RECEIVE` * `JMS_CLIENT_REPLY_NODE` * `JMS_HEADER` * `JMS_INPUT_NODE` * `JMS_OUTPUT_NODE` * `JMS_REPLY_NODE` * `MQ_GET_NODE` * `MQ_INPUT_NODE` * `MQ_OUTPUT_NODE` * `MQ_REPLY_NODE` * `PASSTHRU_NODE` * `PUBLICATION_NODE` * `RESET_CONTENT_DESCRIPTOR_NODE` * `REST_ASYNC_REQUEST_NODE` * `REST_ASYNC_RESPONSE_NODE` * `REST_REQUEST_NODE` * `RE_SEQUENCE_NODE` * `ROUTE_NODE` * `SAP_REPLY_NODE` * `SCA_REPLY_NODE` * `SECURITY_PEP` * `SEQUENCE_NODE` * `SOAP_ASYNC_REQUEST_NODE` * `SOAP_ASYNC_RESPONSE_NODE` * `SOAP_EXTRACT_NODE` * `SOAP_INPUT_NODE` * `SOAP_REPLY_NODE` * `SOAP_REQUEST_NODE` * `SOAP_WRAPPER_NODE` * `SR_RETRIEVE_ENTITY_NODE` * `SR_RETRIEVE_IT_SERVICE_NODE` * `THROW_NODE` * `TRACE_NODE` * `TRY_CATCH_NODE` * `VALIDATE_NODE` * `WS_REPLY_NODE` * `XSL_MQSI_NODE` | Optional |
| iibNodeTypeCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. | Optional |
| imsTransactionCallType | string | IMS transaction call type condition for which the value is captured.  Required if the **source** is: `IMS_TRANSACTION_CALL_TYPE`.  Not applicable in other cases. The element can hold these values * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` | Optional |
| methods | [CapturedMethod](#openapi-definition-CapturedMethod)[] | The method specification if the **source** value is `METHOD_PARAM`.  Not applicable in other cases. | Optional |
| parameterName | string | The name of the web request parameter to capture.  Required if the **source** is one of the following: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  Not applicable in other cases. | Optional |
| scope | [ScopeConditions](#openapi-definition-ScopeConditions) | Conditions for data capturing. | Optional |
| serverVariableTechnology | string | The technology of the server variable to capture if the **source** value is `SERVER_VARIABLE`. \n\n Not applicable in other cases. The element can hold these values * `ASP_NET` | Optional |
| sessionAttributeTechnology | string | The technology of the session attribute to capture if the **source** value is `SESSION_ATTRIBUTE`. \n\n Not applicable in other cases. The element can hold these values * `ASP_NET` * `ASP_NET_CORE` * `JAVA` * `PHP` | Optional |
| source | string | The source of the attribute to capture. Works in conjunction with **parameterName** or **methods** and **technology**. The element can hold these values * `CICS_PATH_NAME` * `CICS_SDK` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_CALL_TYPE` * `CICS_TRANSACTION_GROUP_ID` * `CICS_UNIT_OF_WORK_ID` * `CICS_USER_ID` * `CLIENT_IP` * `CUSTOM_ATTRIBUTE` * `DLI_DB_OR_LTERM_NAME` * `DLI_SEGMENT_NAME` * `IIB_LABEL` * `IIB_NODE` * `IMS_TRANSACTION_CALL_TYPE` * `IMS_UNIT_OF_WORK_ID` * `IMS_USER_ID` * `METHOD_PARAM` * `MQ_CORRELATION_ID` * `MQ_MESSAGE_ID` * `MQ_MESSAGE_SIZE` * `POST_PARAMETER` * `QUERY_PARAMETER` * `REQUEST_HEADER` * `RESPONSE_HEADER` * `SERVER_VARIABLE` * `SESSION_ATTRIBUTE` * `SPAN_ATTRIBUTE` * `URI` * `URI_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` | Required |
| spanAttributeKey | string | The key of the span attribute to capture.  Required if the **source** is: `SPAN_ATTRIBUTE`.  Not applicable in other cases. | Optional |
| technology | string | The technology of the method to capture if the **source** value is `METHOD_PARAM`. \n\n Not applicable in other cases. The element can hold these values * `DOTNET` * `JAVA` * `PHP` | Optional |
| valueProcessing | [ValueProcessing](#openapi-definition-ValueProcessing) | Process values as specified. | Optional |

#### The `ValueCondition` object

IBM integration bus label node name condition for which the value is captured.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| negate | boolean | Negate the comparison. | Required |
| operator | string | Operator comparing the extracted value to the comparison value. The element can hold these values * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` * `NOT_EMPTY` | Required |
| value | string | The value to compare to. | Required |

#### The `CapturedMethod` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| argumentIndex | integer | The index of the argument to capture. Set `0` to capture the return value, `1` or higher to capture a mehtod argument.  Required if the **capture** is set to `ARGUMENT`.  Not applicable in other cases. | Optional |
| capture | string | What to capture from the method. The element can hold these values * `ARGUMENT` * `CLASS_NAME` * `METHOD_NAME` * `OCCURRENCES` * `SIMPLE_CLASS_NAME` * `THIS` | Required |
| deepObjectAccess | string | The getter chain to apply to the captured object. It is required in one of the following cases:  The **capture** is set to `THIS`. The **capture** is set to `ARGUMENT`, and the argument is not a primitive, a primitive wrapper class, a string, or an array.  Not applicable in other cases. | Optional |
| method | [MethodReference](#openapi-definition-MethodReference) | Configuration of a method to be captured. | Required |

#### The `MethodReference` object

Configuration of a method to be captured.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| argumentTypes | string[] | The list of argument types. | Required |
| className | string | The class name where the method to capture resides.  Either this or the **fileName** must be set. | Optional |
| fileName | string | The file name where the method to capture resides.  Either this or **className** must be set. | Optional |
| fileNameMatcher | string | The operator of the comparison.  If not set, `EQUALS` is used. The element can hold these values * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| methodName | string | The name of the method to capture. | Required |
| modifiers | string[] | The modifiers of the method to capture. The element can hold these values * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` | Required |
| returnType | string | The return type. | Required |
| visibility | string | The visibility of the method to capture. The element can hold these values * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` | Required |

#### The `ScopeConditions` object

Conditions for data capturing.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| hostGroup | string | Only applies to this host group. | Optional |
| processGroup | string | Only applies to this process group. Note that this can't be transferred between different clusters or environments. | Optional |
| serviceTechnology | string | Only applies to this service technology. The element can hold these values * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIOHTTP` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `BOTTLE` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FALCON` * `FASTAPI` * `FLASK` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KTOR_CLIENT` * `KTOR_SERVER` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `R2DBC` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SANIC` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `STARLETTE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `TORNADO` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `YII` * `ZERO_MQ` * `ZOS_CONNECT` | Optional |
| tagOfProcessGroup | string | Only apply to process groups matching this tag. | Optional |

#### The `ValueProcessing` object

Process values as specified.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| extractSubstring | [ExtractSubstring](#openapi-definition-ExtractSubstring) | Preprocess by extracting a substring from the original value. | Optional |
| splitAt | string | Split (preprocessed) string values at this separator. | Optional |
| trim | boolean | Prune Whitespaces. Defaults to false. | Required |
| valueCondition | [ValueCondition](#openapi-definition-ValueCondition) | IBM integration bus label node name condition for which the value is captured. | Optional |
| valueExtractorRegex | string | Extract value from captured data per regex. | Optional |

#### The `ExtractSubstring` object

Preprocess by extracting a substring from the original value.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| delimiter | string | The delimiter string. | Required |
| endDelimiter | string | The end-delimiter string.  Required if the **position** value is `BETWEEN`. Otherwise not allowed. | Optional |
| position | string | The position of the extracted string relative to delimiters. The element can hold these values * `AFTER` * `BEFORE` * `BETWEEN` | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The request attribute with the specified ID has been created. The ID of the new configuration is returned. |
| **204** | - | Success. Request attribute has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}/validator` |

### Authentication

To execute this request, you need an access token with `CaptureRequestData` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

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

## Related topics

* [Request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")