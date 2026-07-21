---
title: Request attributes API - GET a request attribute
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-attributes-api/get-request-attribute
---

# Request attributes API - GET a request attribute

# Request attributes API - GET a request attribute

* Справочник
* Опубликовано 3 сентября 2019 г.

Получает параметры указанного атрибута запроса.

Запрос возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать такой токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного атрибута запроса. | path | Обязательный |
| includeProcessGroupReferences | boolean | Флаг для включения в ответ ссылок на группы процессов.  Ссылки на группы процессов несовместимы между разными окружениями. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RequestAttribute](#openapi-definition-RequestAttribute) | Успешно |

### Объекты тела ответа


#### Объект `RequestAttribute`


| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации для значений запроса. Элемент может принимать следующие значения * `ALL_DISTINCT_VALUES` * `AVERAGE` * `COUNT_DISTINCT_VALUES` * `COUNT_VALUES` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` |
| confidential | boolean | Флаг конфиденциальных данных. Установить `true`, чтобы обрабатывать захваченные данные как конфиденциальные. |
| dataSources | [DataSource](#openapi-definition-DataSource)[] | Список источников данных. |
| dataType | string | Тип данных атрибута запроса. Элемент может принимать следующие значения * `DOUBLE` * `INTEGER` * `STRING` |
| enabled | boolean | Атрибут запроса включён (`true`) или отключён (`false`). |
| id | string | ID атрибута запроса. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| name | string | Название атрибута запроса. |
| normalization | string | Преобразование строковых значений. Если **dataType** не равен `string`, здесь нужно указать `Original`. Элемент может принимать следующие значения * `ORIGINAL` * `TO_LOWER_CASE` * `TO_UPPER_CASE` |
| skipPersonalDataMasking | boolean | Флаг маскирования персональных данных. Установить `true`, чтобы пропустить маскирование.  Предупреждение: это потенциально даёт доступ к персонализированным данным. |


#### Объект `DataSource`


| Элемент | Тип | Описание |
| --- | --- | --- |
| capturingAndStorageLocation | string | Указывает место, где захватываются и хранятся значения.  Требуется, если **source** имеет одно из следующих значений: `GET_PARAMETER`, `URI`, `REQUEST_HEADER`, `RESPONSE_HEADER`.  Не применяется в остальных случаях.  Если значение **source** равно `REQUEST_HEADER` или `RESPONSE_HEADER`, местоположение `CAPTURE_AND_STORE_ON_BOTH` не допускается. Элемент может принимать следующие значения * `CAPTURE_AND_STORE_ON_BOTH` * `CAPTURE_AND_STORE_ON_CLIENT` * `CAPTURE_AND_STORE_ON_SERVER` * `CAPTURE_ON_CLIENT_STORE_ON_SERVER` |
| cicsSDKMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие названия узла метки IBM integration bus, при котором захватывается значение. |
| cicsTransactionCallType | string | Условие типа вызова транзакции CICS, при котором захватывается значение.  Требуется, если **source** равен: `CICS_TRANSACTION_CALL_TYPE`.  Не применяется в остальных случаях. Элемент может принимать следующие значения * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` |
| enabled | boolean | Источник данных включён (`true`) или отключён (`false`). |
| iibLabelMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие названия узла метки IBM integration bus, при котором захватывается значение. |
| iibMethodNodeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие названия узла метки IBM integration bus, при котором захватывается значение. |
| iibNodeType | string | Тип узла IBM integration bus, для которого захватывается значение.  Этот элемент, `iibNodeTypeCondition` (другой тип того же поля) или `iibMethodNodeCondition` требуется, если **source** равен: `IIB_NODE`.  Не применяется в остальных случаях. Элемент может принимать следующие значения * `AGGREGATE_CONTROL_NODE` * `AGGREGATE_REPLY_NODE` * `AGGREGATE_REQUEST_NODE` * `CALLABLE_FLOW_REPLY_NODE` * `COLLECTOR_NODE` * `COMPUTE_NODE` * `DATABASE_NODE` * `DATABASE_RETRIEVE_NODE` * `DATABASE_ROUTE_NODE` * `DECISION_SERVICE_NODE` * `DOT_NET_COMPUTE_NODE` * `FILE_READ_NODE` * `FILTER_NODE` * `FLOW_ORDER_NODE` * `GROUP_COMPLETE_NODE` * `GROUP_GATHER_NODE` * `GROUP_SCATTER_NODE` * `HTTP_ASYNC_REQUEST` * `HTTP_ASYNC_RESPONSE` * `HTTP_HEADER` * `HTTP_INPUT` * `HTTP_REPLY` * `HTTP_REQUEST` * `JAVA_COMPUTE_NODE` * `JMS_CLIENT_RECEIVE` * `JMS_CLIENT_REPLY_NODE` * `JMS_HEADER` * `JMS_INPUT_NODE` * `JMS_OUTPUT_NODE` * `JMS_REPLY_NODE` * `MQ_GET_NODE` * `MQ_INPUT_NODE` * `MQ_OUTPUT_NODE` * `MQ_REPLY_NODE` * `PASSTHRU_NODE` * `PUBLICATION_NODE` * `RESET_CONTENT_DESCRIPTOR_NODE` * `REST_ASYNC_REQUEST_NODE` * `REST_ASYNC_RESPONSE_NODE` * `REST_REQUEST_NODE` * `RE_SEQUENCE_NODE` * `ROUTE_NODE` * `SAP_REPLY_NODE` * `SCA_REPLY_NODE` * `SECURITY_PEP` * `SEQUENCE_NODE` * `SOAP_ASYNC_REQUEST_NODE` * `SOAP_ASYNC_RESPONSE_NODE` * `SOAP_EXTRACT_NODE` * `SOAP_INPUT_NODE` * `SOAP_REPLY_NODE` * `SOAP_REQUEST_NODE` * `SOAP_WRAPPER_NODE` * `SR_RETRIEVE_ENTITY_NODE` * `SR_RETRIEVE_IT_SERVICE_NODE` * `THROW_NODE` * `TRACE_NODE` * `TRY_CATCH_NODE` * `VALIDATE_NODE` * `WS_REPLY_NODE` * `XSL_MQSI_NODE` |
| iibNodeTypeCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие названия узла метки IBM integration bus, при котором захватывается значение. |
| imsTransactionCallType | string | Условие типа вызова транзакции IMS, при котором захватывается значение.  Требуется, если **source** равен: `IMS_TRANSACTION_CALL_TYPE`.  Не применяется в остальных случаях. Элемент может принимать следующие значения * `CTG` * `DPL` * `EXPLICIT_ADK` * `HTTP` * `IMS_CONNECT` * `IMS_CONNECT_API` * `IMS_ITRA` * `IMS_MSC` * `IMS_PGM_SWITCH` * `IMS_SHARED_QUEUES` * `IMS_TRANS_EXEC` * `MQ` * `SOAP` * `START` * `TTX` * `TX` * `UNKNOWN` * `ZOS_CONNECT` |
| methods | [CapturedMethod](#openapi-definition-CapturedMethod)[] | Спецификация метода, если значение **source** равно `METHOD_PARAM`.  Не применяется в остальных случаях. |
| parameterName | string | Название параметра веб-запроса для захвата.  Требуется, если **source** имеет одно из следующих значений: `POST_PARAMETER`, `GET_PARAMETER`, `REQUEST_HEADER`, `RESPONSE_HEADER`, `CUSTOM_ATTRIBUTE`.  Не применяется в остальных случаях. |
| scope | [ScopeConditions](#openapi-definition-ScopeConditions) | Условия захвата данных. |
| serverVariableTechnology | string | Технология серверной переменной для захвата, если значение **source** равно `SERVER_VARIABLE`. \n\n Не применяется в остальных случаях. Элемент может принимать следующие значения * `ASP_NET` |
| sessionAttributeTechnology | string | Технология атрибута сессии для захвата, если значение **source** равно `SESSION_ATTRIBUTE`. \n\n Не применяется в остальных случаях. Элемент может принимать следующие значения * `ASP_NET` * `ASP_NET_CORE` * `JAVA` * `PHP` |
| source | string | Источник атрибута для захвата. Работает совместно с **parameterName** или **methods** и **technology**. Элемент может принимать следующие значения * `CICS_PATH_NAME` * `CICS_SDK` * `CICS_SYSTEM_ID` * `CICS_TASK_ID` * `CICS_TRANSACTION_CALL_TYPE` * `CICS_TRANSACTION_GROUP_ID` * `CICS_UNIT_OF_WORK_ID` * `CICS_USER_ID` * `CLIENT_IP` * `CUSTOM_ATTRIBUTE` * `DLI_DB_OR_LTERM_NAME` * `DLI_SEGMENT_NAME` * `IIB_LABEL` * `IIB_NODE` * `IMS_TRANSACTION_CALL_TYPE` * `IMS_UNIT_OF_WORK_ID` * `IMS_USER_ID` * `METHOD_PARAM` * `MQ_CORRELATION_ID` * `MQ_MESSAGE_ID` * `MQ_MESSAGE_SIZE` * `POST_PARAMETER` * `QUERY_PARAMETER` * `REQUEST_HEADER` * `RESPONSE_HEADER` * `SERVER_VARIABLE` * `SESSION_ATTRIBUTE` * `SPAN_ATTRIBUTE` * `URI` * `URI_PATH` * `WEBSERVICE_METHOD` * `WEBSERVICE_NAME` |
| spanAttributeKey | string | Ключ атрибута span для захвата.  Требуется, если **source** равен: `SPAN_ATTRIBUTE`.  Не применяется в остальных случаях. |
| technology | string | Технология метода для захвата, если значение **source** равно `METHOD_PARAM`. \n\n Не применяется в остальных случаях. Элемент может принимать следующие значения * `DOTNET` * `JAVA` * `PHP` |
| valueProcessing | [ValueProcessing](#openapi-definition-ValueProcessing) | Обработка значений согласно указанным настройкам. |


#### Объект `ValueCondition`


Условие названия узла метки IBM integration bus, при котором захватывается значение.


| Элемент | Тип | Описание |
| --- | --- | --- |
| negate | boolean | Инвертировать сравнение. |
| operator | string | Оператор, сравнивающий извлечённое значение со значением сравнения. Элемент может принимать следующие значения * `BEGINS_WITH` * `BEGINS_WITH_ANY_OF` * `CONTAINS` * `ENDS_WITH` * `ENDS_WITH_ANY_OF` * `EQUALS` * `EQUALS_ANY_OF` * `NOT_EMPTY` |
| value | string | Значение для сравнения. |


#### Объект `CapturedMethod`


| Элемент | Тип | Описание |
| --- | --- | --- |
| argumentIndex | integer | Индекс аргумента для захвата. Установить `0`, чтобы захватить возвращаемое значение, `1` или выше, чтобы захватить аргумент метода.  Требуется, если **capture** установлен в `ARGUMENT`.  Не применяется в остальных случаях. |
| capture | string | Что захватывать из метода. Элемент может принимать следующие значения * `ARGUMENT` * `CLASS_NAME` * `METHOD_NAME` * `OCCURRENCES` * `SIMPLE_CLASS_NAME` * `THIS` |
| deepObjectAccess | string | Цепочка геттеров, применяемая к захваченному объекту. Требуется в одном из следующих случаев: **capture** установлен в `THIS`. **capture** установлен в `ARGUMENT`, а аргумент не является примитивом, классом-обёрткой примитива, строкой или массивом.  Не применяется в остальных случаях. |
| method | [MethodReference](#openapi-definition-MethodReference) | Конфигурация метода для захвата. |


#### Объект `MethodReference`


Конфигурация метода для захвата.

| Элемент | Тип | Описание |
| --- | --- | --- |
| argumentTypes | string[] | Список типов аргументов. |
| className | string | Имя класса, в котором находится захватываемый метод. Нужно задать это или **fileName**. |
| fileName | string | Имя файла, в котором находится захватываемый метод. Нужно задать это или **className**. |
| fileNameMatcher | string | Оператор сравнения. Если не задан, используется `EQUALS`. Элемент может принимать значения * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| methodName | string | Имя захватываемого метода. |
| modifiers | string[] | Модификаторы захватываемого метода. Элемент может принимать значения * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` |
| returnType | string | Возвращаемый тип. |
| visibility | string | Видимость захватываемого метода. Элемент может принимать значения * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` |


#### Объект `ScopeConditions`


Условия для захвата данных.


| Элемент | Тип | Описание |
| --- | --- | --- |
| hostGroup | string | Применяется только к этой host group. |
| processGroup | string | Применяется только к этой process group. Обратите внимание, что это нельзя перенести между разными кластерами или окружениями. |
| serviceTechnology | string | Применяется только к этой технологии сервиса. Элемент может принимать значения * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIOHTTP` * `AIX` * `AKKA` * `AMAZON_BEDROCK` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_KINESIS` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_S3` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_BLOB` * `AZURE_EVENT_HUB` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `BOTTLE` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FALCON` * `FASTAPI` * `FLASK` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `HTTPX` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KTOR_CLIENT` * `KTOR_SERVER` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `R2DBC` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `REQUESTS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SANIC` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `STARLETTE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `TORNADO` * `UNDERTOW_IO` * `URLLIB3` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `YII` * `ZERO_MQ` * `ZOS_CONNECT` |
| tagOfProcessGroup | string | Применяется только к process groups, соответствующим этому тегу. |


#### Объект `ValueProcessing`


Обработка значений согласно заданным параметрам.


| Элемент | Тип | Описание |
| --- | --- | --- |
| extractSubstring | [ExtractSubstring](#openapi-definition-ExtractSubstring) | Предобработка путём извлечения подстроки из исходного значения. |
| splitAt | string | Разбить (предобработанные) строковые значения по этому разделителю. |
| trim | boolean | Обрезать пробелы. По умолчанию false. |
| valueCondition | [ValueCondition](#openapi-definition-ValueCondition) | Условие имени label node IBM integration bus, для которого захватывается значение. |
| valueExtractorRegex | string | Извлечь значение из захваченных данных по regex. |


#### Объект `ExtractSubstring`


Предобработка путём извлечения подстроки из исходного значения.


| Элемент | Тип | Описание |
| --- | --- | --- |
| delimiter | string | Строка-разделитель. |
| endDelimiter | string | Конечная строка-разделитель. Обязательна, если значение **position** равно `BETWEEN`. В остальных случаях не допускается. |
| position | string | Позиция извлекаемой строки относительно разделителей. Элемент может принимать значения * `AFTER` * `BEFORE` * `BETWEEN` |


#### Объект `ConfigurationMetadata`


Метаданные, полезные для отладки


| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

### Тело ответа JSON моделей

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

## Похожие темы

* [Атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запроса, и научитесь использовать их на всех уровнях всех представлений анализа сервисов.")