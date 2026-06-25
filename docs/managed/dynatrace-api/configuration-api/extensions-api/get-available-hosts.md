---
title: Extensions API - GET available hosts
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-available-hosts
scraped: 2026-05-12T11:19:59.042374
---

# Extensions API - GET available hosts

# Extensions API - GET available hosts

* Reference
* Published Mar 06, 2020

Lists all available hosts that run the specified technology.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| technology | string | Name of requested technology The element can hold these values * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIX` * `AKKA` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOCKERDEAMON` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MONGODB_ROUTER` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `UNDERTOW_IO` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `ZERO_MQ` * `ZOS_CONNECT` | path | Required |
| tag | string[] | Filters the resulting set of hosts by the specified tag.  You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags. | query | Optional |
| managementZone | integer | Only return hosts that are part of the specified management zone. | query | Optional |
| hostGroupId | string | Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace IDs of the host group you're interested in. | query | Optional |
| hostGroupName | string | Filters the resulting set of hosts by the specified host group.  Specify the name of the host group you're interested in. | query | Optional |
| pageSize | integer | The number of results per result page. Must be between 1 and 500 | query | Optional |
| nextPageKey | string | The cursor for the next page of results. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [HostList](#openapi-definition-HostList) | Success |

### Response body objects

#### The `HostList` object

The list of hosts supported by extension.

| Element | Type | Description |
| --- | --- | --- |
| hosts | [Host[]](#openapi-definition-Host) | The list of hosts |
| nextPageKey | string | Next page key used for paging |
| totalResults | integer | Total number of results |

#### The `Host` object

Host details. Contains ID, name, host group, and tags.

| Element | Type | Description |
| --- | --- | --- |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | Host group to which the host belongs. |
| id | string | The ID of the host |
| managementZones | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | A list of management zones to which the host belongs. |
| name | string | The name of the host |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | A list of tags of the host. |

#### The `HostGroup` object

Host group to which the host belongs.

| Element | Type | Description |
| --- | --- | --- |
| meId | string | The Dynatrace entity ID of the host group. |
| name | string | The name of the Dynatrace entity, displayed in the UI. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

### Response body JSON models

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

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")