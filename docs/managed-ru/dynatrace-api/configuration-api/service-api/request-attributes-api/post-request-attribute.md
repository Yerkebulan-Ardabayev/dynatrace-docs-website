---
title: Request attributes API - POST a request attribute
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-attributes-api/post-request-attribute
scraped: 2026-05-12T11:20:30.093418
---

# Request attributes API - POST a request attribute

# Request attributes API - POST a request attribute

* Reference
* Published Sep 03, 2019

Создаёт новый атрибут запроса.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `CaptureRequestData`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [RequestAttribute](#openapi-definition-RequestAttribute) | В теле не нужно указывать ID, поскольку идентификаторы назначаются автоматически. | body | Required |

### Объекты тела запроса

#### Объект `RequestAttribute`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregation | string | Тип агрегации значений запроса. Возможные значения: * `ALL_DISTINCT_VALUES` * `AVERAGE` * `COUNT_DISTINCT_VALUES` * `COUNT_VALUES` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Required |
| confidential | boolean | Флаг конфиденциальных данных. Установите `true`, чтобы считать захваченные данные конфиденциальными. | Required |
| dataSources | [DataSource[]](#openapi-definition-DataSource) | Список источников данных. | Required |
| dataType | string | Тип данных атрибута запроса. Возможные значения: * `DOUBLE` * `INTEGER` * `STRING` | Required |
| enabled | boolean | Атрибут запроса включён (`true`) или отключён (`false`). | Required |
| id | string | ID атрибута запроса. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| name | string | Имя атрибута запроса. | Required |
| normalization | string | Преобразование строковых значений.  Если **dataType** не `string`, укажите здесь `Original`. Возможные значения: * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` | Required |
| skipPersonalDataMasking | boolean | Флаг маскирования персональных данных. Установите `true`, чтобы пропустить маскирование.  Предупреждение: при этом возможен доступ к персонализированным данным. | Required |

#### Объект `DataSource`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| capturingAndStorageLocation | string | Указывает место, где значения захватываются и хранятся.  Обязательно, если **source** равно одному из: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  В остальных случаях не применяется.  Если значение **source** равно `REQUEST_HEADER` или `RESPONSE_HEADER`, расположение `CAPTURE_AND_STORE_ON_BOTH` не допускается. Возможные значения: * `CAPTURE_AND_STORE_ON_BOTH` * `CAPTURE_AND_STORE_ON_CLIENT` * `CAPTURE_AND_STORE_ON_SERVER` * `CAPTURE_ON_CLIENT_STORE_ON_SERVER` | Optional |
| cicsSDKMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени узла-метки IBM integration bus, для которого захватывается значение. | Optional |
| cicsTransactionCallType | string | Условие типа вызова транзакции CICS, для которого захватывается значение.  Обязательно, если **source** равно `CICS_TRANSACTION_CALL_TYPE`.  В остальных случаях не применяется. Возможные значения: * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` | Optional |
| enabled | boolean | Источник данных включён (`true`) или отключён (`false`). | Required |
| iibLabelMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени узла-метки IBM integration bus, для которого захватывается значение. | Optional |
| iibMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени узла-метки IBM integration bus, для которого захватывается значение. | Optional |
| iibNodeType | string | Тип узла IBM integration bus, для которого захватывается значение.  Это поле, iibNodeTypeCondition (другой тип того же поля) или `iibMethodNodeCondition` обязательно, если **source** равно `IIB_NODE`.  В остальных случаях не применяется. Возможные значения: * `AGGREGATE_CONTROL_NODE` * `AGGREGATE_REPLY_NODE` * `AGGREGATE_REQUEST_NODE` * `CALLABLE_FLOW_REPLY_NODE` * `COLLECTOR_NODE` * `COMPUTE_NODE` * `DATABASE_NODE` * `DATABASE_RETRIEVE_NODE` * `DATABASE_ROUTE_NODE` * `DECISION_SERVICE_NODE` * `DOT_NET_COMPUTE_NODE` * `FILE_READ_NODE` * `FILTER_NODE` * `FLOW_ORDER_NODE` * `GROUP_COMPLETE_NODE` * `GROUP_GATHER_NODE` * `GROUP_SCATTER_NODE` * `HTTP_ASYNC_REQUEST` * `HTTP_ASYNC_RESPONSE` * `HTTP_HEADER` * `HTTP_INPUT` * `HTTP_REPLY` * `HTTP_REQUEST` * `JAVA_COMPUTE_NODE` * `JMS_CLIENT_RECEIVE` * `JMS_CLIENT_REPLY_NODE` * `JMS_HEADER` * `JMS_INPUT_NODE` * `JMS_OUTPUT_NODE` * `JMS_REPLY_NODE` * `MQ_GET_NODE` * `MQ_INPUT_NODE` * `MQ_OUTPUT_NODE` * `MQ_REPLY_NODE` * `PASSTHRU_NODE` * `PUBLICATION_NODE` * `RESET_CONTENT_DESCRIPTOR_NODE` * `REST_ASYNC_REQUEST_NODE` * `REST_ASYNC_RESPONSE_NODE` * `REST_REQUEST_NODE` * `RE_SEQUENCE_NODE` * `ROUTE_NODE` * `SAP_REPLY_NODE` * `SCA_REPLY_NODE` * `SECURITY_PEP` * `SEQUENCE_NODE` * `SOAP_ASYNC_REQUEST_NODE` * `SOAP_ASYNC_RESPONSE_NODE` * `SOAP_EXTRACT_NODE` * `SOAP_INPUT_NODE` * `SOAP_REPLY_NODE` * `SOAP_REQUEST_NODE` * `SOAP_WRAPPER_NODE` * `SR_RETRIEVE_ENTITY_NODE` * `SR_RETRIEVE_IT_SERVICE_NODE` * `THROW_NODE` * `TRACE_NODE` * `TRY_CATCH_NODE` * `VALIDATE_NODE` * `WS_REPLY_NODE` * `XSL_MQSI_NODE` | Optional |
| iibNodeTypeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени узла-метки IBM integration bus, для которого захватывается значение. | Optional |
| imsTransactionCallType | string | Условие типа вызова транзакции IMS, для которого захватывается значение.  Обязательно, если **source** равно `IMS_TRANSACTION_CALL_TYPE`.  В остальных случаях не применяется. Возможные значения: * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` | Optional |
| methods | [CapturedMethod[]](#openapi-definition-CapturedMethod) | Спецификация метода, если значение **source** равно `METHOD_PARAM`.  В остальных случаях не применяется. | Optional |
| parameterName | string | Имя захватываемого параметра веб-запроса.  Обязательно, если **source** равно одному из: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  В остальных случаях не применяется. | Optional |
| scope | [ScopeConditions](#openapi-definition-ScopeConditions) | Условия захвата данных. | Optional |
| serverVariableTechnology | string | Технология захватываемой серверной переменной, если значение **source** равно `SERVER_VARIABLE`. \n\n В остальных случаях не применяется. Возможные значения: * `ASP_NET` | Optional |
| sessionAttributeTechnology | string | Технология захватываемого атрибута сессии, если значение **source** равно `SESSION_ATTRIBUTE`. \n\n В остальных случаях не применяется. Возможные значения: * `ASP_NET` * `ASP_NET_CORE` * `JAVA` * `PHP` | Optional |
| source | string | Источник захватываемого атрибута. Работает совместно с **parameterName** или **methods** и **technology**. Возможные значения: * `CICS_PATH_NAME` * `CICS_SDK` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_CALL_TYPE` * `CICS_TRANSACTION_GROUP_ID` * `CICS_UNIT_OF_WORK_ID` * `CICS_USER_ID` * `CLIENT_IP` * `CUSTOM_ATTRIBUTE` * `DLI_DB_OR_LTERM_NAME` * `DLI_SEGMENT_NAME` * `IIB_LABEL` * `IIB_NODE` * `IMS_TRANSACTION_CALL_TYPE` * `IMS_UNIT_OF_WORK_ID` * `IMS_USER_ID` * `METHOD_PARAM` * `MQ_CORRELATION_ID` * `MQ_MESSAGE_ID` * `MQ_MESSAGE_SIZE` * `POST_PARAMETER` * `QUERY_PARAMETER` * `REQUEST_HEADER` * `RESPONSE_HEADER` * `SERVER_VARIABLE` * `SESSION_ATTRIBUTE` * `SPAN_ATTRIBUTE` * `URI` * `URI_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` | Required |
| spanAttributeKey | string | Ключ захватываемого атрибута span.  Обязательно, если **source** равно `SPAN_ATTRIBUTE`.  В остальных случаях не применяется. | Optional |
| technology | string | Технология захватываемого метода, если значение **source** равно `METHOD_PARAM`. \n\n В остальных случаях не применяется. Возможные значения: * `DOTNET` * `JAVA` * `PHP` | Optional |
| valueProcessing | [ValueProcessing](#openapi-definition-ValueProcessing) | Обработать значения заданным образом. | Optional |

#### Объект `ValueCondition`

Условие имени узла-метки IBM integration bus, для которого захватывается значение.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| negate | boolean | Инвертировать сравнение. | Required |
| operator | string | Оператор, сравнивающий извлечённое значение со значением для сравнения. Возможные значения: * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` | Required |
| value | string | Значение для сравнения. | Required |

#### Объект `CapturedMethod`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| argumentIndex | integer | Индекс захватываемого аргумента. Установите `0`, чтобы захватить возвращаемое значение, `1` или больше, чтобы захватить аргумент метода.  Обязательно, если **capture** установлено в `ARGUMENT`.  В остальных случаях не применяется. | Optional |
| capture | string | Что захватывать из метода. Возможные значения: * `ARGUMENT` * `CLASS_NAME` * `METHOD_NAME` * `OCCURRENCES` * `SIMPLE_CLASS_NAME` * `THIS` | Required |
| deepObjectAccess | string | Цепочка геттеров, применяемая к захваченному объекту. Обязательна в одном из следующих случаев:  **capture** установлено в `THIS`. **capture** установлено в `ARGUMENT`, и аргумент не является примитивом, классом-обёрткой примитива, строкой или массивом.  В остальных случаях не применяется. | Optional |
| method | [MethodReference](#openapi-definition-MethodReference) | Конфигурация захватываемого метода. | Required |

#### Объект `MethodReference`

Конфигурация захватываемого метода.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| argumentTypes | string[] | Список типов аргументов. | Required |
| className | string | Имя класса, в котором находится захватываемый метод.  Должно быть установлено либо это поле, либо **fileName**. | Optional |
| fileName | string | Имя файла, в котором находится захватываемый метод.  Должно быть установлено либо это поле, либо **className**. | Optional |
| fileNameMatcher | string | Оператор сравнения.  Если не установлен, используется `EQUALS`. Возможные значения: * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| methodName | string | Имя захватываемого метода. | Required |
| modifiers | string[] | Модификаторы захватываемого метода. Возможные значения: * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` | Required |
| returnType | string | Возвращаемый тип. | Required |
| visibility | string | Видимость захватываемого метода. Возможные значения: * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` | Required |

#### Объект `ScopeConditions`

Условия захвата данных.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| hostGroup | string | Применяется только к этой группе хостов. | Optional |
| processGroup | string | Применяется только к этой группе процессов. Учтите, что это нельзя перенести между разными кластерами или окружениями. | Optional |
| serviceTechnology | string | Применяется только к этой технологии сервиса. Возможные значения: * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `ZERO_MQ` * `ZOS_CONNECT` | Optional |
| tagOfProcessGroup | string | Применять только к группам процессов с этим тегом. | Optional |

#### Объект `ValueProcessing`

Обработать значения заданным образом.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| extractSubstring | [ExtractSubstring](#openapi-definition-ExtractSubstring) | Предобработка путём извлечения подстроки из исходного значения. | Optional |
| splitAt | string | Разбивать (предобработанные) строковые значения по этому разделителю. | Optional |
| trim | boolean | Удалять пробелы. По умолчанию false. | Required |
| valueCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени узла-метки IBM integration bus, для которого захватывается значение. | Optional |
| valueExtractorRegex | string | Извлечь значение из захваченных данных по регулярному выражению. | Optional |

#### Объект `ExtractSubstring`

Предобработка путём извлечения подстроки из исходного значения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| delimiter | string | Строка-разделитель. | Required |
| endDelimiter | string | Строка конечного разделителя.  Обязательна, если значение **position** равно `BETWEEN`. В остальных случаях не допускается. | Optional |
| position | string | Позиция извлекаемой строки относительно разделителей. Возможные значения: * `AFTER` * `BEFORE` * `BETWEEN` | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Атрибут запроса создан. Возвращается ID новой конфигурации. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `CaptureRequestData`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

* [Атрибуты запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.")