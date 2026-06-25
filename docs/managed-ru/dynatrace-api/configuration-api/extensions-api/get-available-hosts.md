---
title: Extensions API - GET available hosts
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-available-hosts
scraped: 2026-05-12T11:19:59.042374
---

# Extensions API - GET available hosts

# Extensions API - GET available hosts

* Reference
* Published Mar 06, 2020

Выводит список всех доступных хостов, на которых работает указанная технология.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Имя требуемой технологии Возможные значения: * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOCKERDEAMON` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MONGODB_ROUTER` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `ZERO_MQ` * `ZOS_CONNECT` | path | Required |
| tag | string[] | Фильтрует результирующий набор хостов по указанному тегу.  Вы можете указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам. | query | Optional |
| managementZone | integer | Возвращать только хосты, входящие в указанную management zone. | query | Optional |
| hostGroupId | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите Dynatrace ID интересующей вас host group. | query | Optional |
| hostGroupName | string | Фильтрует результирующий набор хостов по указанной host group.  Укажите имя интересующей вас host group. | query | Optional |
| pageSize | integer | Количество результатов на страницу. Должно быть от 1 до 500 | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostList](#openapi-definition-HostList) | Успех |

### Объекты тела ответа

#### Объект `HostList`

Список хостов, поддерживаемых расширением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hosts | [Host[]](#openapi-definition-Host) | Список хостов |
| nextPageKey | string | Ключ следующей страницы, используемый для постраничного вывода |
| totalResults | integer | Общее количество результатов |

#### Объект `Host`

Детали хоста. Содержит ID, имя, host group и теги.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | Host group, которому принадлежит хост. |
| id | string | ID хоста |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Список management zone, которым принадлежит хост. |
| name | string | Имя хоста |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Список тегов хоста. |

#### Объект `HostGroup`

Host group, которому принадлежит хост.

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | ID сущности Dynatrace для host group. |
| name | string | Имя сущности Dynatrace, отображаемое в UI. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Кастомные теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  Кастомные теги содержат здесь значение тега. |
| value | string | Значение тега.  Не применимо к кастомным тегам. |

### JSON-модели тела ответа

```
{



"hosts": [



{



"hostGroup": {



"meId": "HOST_GROUP-CF1DA380B3A53F17",



"name": "example host group"



},



"id": "HOST-0000000000000000",



"managementZones": [



{



"id": "000000000000000000",



"name": "example zone"



}



],



"name": "example host",



"tags": [



"tagA",



"tagB"



]



}



],



"nextPageKey": "string",



"totalResults": 1



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")