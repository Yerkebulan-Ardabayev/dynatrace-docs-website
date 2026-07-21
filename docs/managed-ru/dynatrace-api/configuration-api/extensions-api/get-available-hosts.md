---
title: Extensions API - GET available hosts
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-available-hosts
---

# Extensions API - GET available hosts

# Extensions API - GET available hosts

* Справка
* Опубликовано 06 марта 2020 г.

Возвращает список всех доступных хостов, на которых работает указанная технология.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{technology}/availableHosts` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Название запрашиваемой технологии. Элемент может принимать следующие значения * `ACTIVEMQ_CLIENT` * `ACTIVE_MQ` * `ACTIVE_MQ_ARTEMIS` * `ADOBE_EXPERIENCE_MANAGER` * `ADO_NET` * `AIOHTTP` * `AIX` * `AKKA` * `AMAZON_BEDROCK` * `AMAZON_REDSHIFT` * `AMQP` * `APACHE_CAMEL` * `APACHE_CASSANDRA` * `APACHE_COUCH_DB` * `APACHE_DERBY` * `APACHE_HTTP_CLIENT_ASYNC` * `APACHE_HTTP_CLIENT_SYNC` * `APACHE_HTTP_SERVER` * `APACHE_KAFKA` * `APACHE_LOG4J` * `APACHE_PEKKO` * `APACHE_SOLR` * `APACHE_STORM` * `APACHE_SYNAPSE` * `APACHE_TOMCAT` * `APPARMOR` * `APPLICATION_INSIGHTS_SDK` * `ASP_DOTNET` * `ASP_DOTNET_CORE` * `ASP_DOTNET_CORE_SIGNALR` * `ASP_DOTNET_SIGNALR` * `ASYNC_HTTP_CLIENT` * `AWS_DYNAMO_DB` * `AWS_EVENT_BRIDGE` * `AWS_KINESIS` * `AWS_LAMBDA` * `AWS_RDS` * `AWS_S3` * `AWS_SERVICE` * `AWS_SNS_CLIENT` * `AWS_SQS` * `AXIS` * `AZURE_BLOB` * `AZURE_EVENT_HUB` * `AZURE_FUNCTIONS` * `AZURE_SERVICE_BUS` * `AZURE_SERVICE_FABRIC` * `AZURE_STORAGE` * `BOSHBPM` * `BOTTLE` * `CICS_FILE_ACCESS` * `CITRIX` * `CITRIX_COMMON` * `CITRIX_DESKTOP_DELIVERY_CONTROLLERS` * `CITRIX_DIRECTOR` * `CITRIX_LICENSE_SERVER` * `CITRIX_PROVISIONING_SERVICES` * `CITRIX_STOREFRONT` * `CITRIX_VIRTUAL_DELIVERY_AGENT` * `CITRIX_WORKSPACE_ENVIRONMENT_MANAGEMENT` * `CITRIX_XEN` * `CLOUDFOUNDRY` * `CLOUDFOUNDRY_AUCTIONEER` * `CLOUDFOUNDRY_BOSH` * `CLOUDFOUNDRY_GOROUTER` * `CLR` * `CODEIGNITER` * `COLDFUSION` * `CONFLUENT_KAFKA_CLIENT` * `CONTAINERD` * `CORE_DNS` * `COSMOSDB` * `COUCHBASE` * `CRIO` * `CXF` * `DATASTAX` * `DB2` * `DB2_CLIENT` * `DIEGO_CELL` * `DOCKER` * `DOTNET` * `DOTNET_REMOTING` * `DRUPAL` * `DYNATRACE` * `ELASTIC_SEARCH` * `ENVOY` * `ERLANG` * `ETCD` * `F5_LTM` * `FALCON` * `FASTAPI` * `FLASK` * `FSHARP` * `GARDEN` * `GLASSFISH` * `GO` * `GOOGLE_CLOUD_FUNCTIONS` * `GRAAL_NATIVE_IMAGE` * `GRAAL_TRUFFLE` * `GRAPH_QL` * `GRPC` * `GRSECURITY` * `HADOOP` * `HADOOP_HDFS` * `HADOOP_YARN` * `HAPROXY` * `HEAT` * `HELIDON` * `HESSIAN` * `HORNET_Q` * `HTTPX` * `IBM_CICS_REGION` * `IBM_CICS_TRANSACTION_GATEWAY` * `IBM_IMS_CONNECT_REGION` * `IBM_IMS_CONTROL_REGION` * `IBM_IMS_MESSAGE_PROCESSING_REGION` * `IBM_IMS_SOAP_GATEWAY` * `IBM_INTEGRATION_BUS` * `IBM_MQ` * `IBM_MQ_CLIENT` * `IBM_WEBSHPRERE_APPLICATION_SERVER` * `IBM_WEBSHPRERE_LIBERTY` * `IBM_WEBSPHERE_APPLICATION_SERVER` * `IBM_WEBSPHERE_LIBERTY` * `IIS` * `IIS_APP_POOL` * `ISTIO` * `JAVA` * `JAVA_HTTPURLCONNECTION` * `JAVA_HTTPURLCONNETION` * `JAX_WS` * `JBOSS` * `JBOSS_EAP` * `JBOSS_LOGMANAGER` * `JDK_HTTP_CLIENT` * `JDK_HTTP_SERVER` * `JERSEY` * `JETTY` * `JOOMLA` * `JRUBY` * `JYTHON` * `KOTLIN` * `KOTLIN_COROUTINES` * `KTOR_CLIENT` * `KTOR_SERVER` * `KUBERNETES` * `LAMINAS` * `LARAVEL` * `LIBC` * `LIBVIRT` * `LINKERD` * `LINUX_SYSTEM` * `LOGSTASH_LOGBACK_ENCODER` * `MAGENTO` * `MARIADB` * `MEMCACHED` * `MICRONAUT` * `MICROSOFT_SQL_SERVER` * `MONGODB` * `MONGODB_CLIENT` * `MONGODB_CLIENT_DOTNET` * `MSSQL_CLIENT` * `MULE_ESB` * `MYSQL` * `MYSQL_CONNECTOR` * `NETFLIX_SERVO` * `NETTY` * `NGINX` * `NODE_JS` * `OK_HTTP_CLIENT` * `ONEAGENT_SDK` * `OPENCENSUS` * `OPENSHIFT` * `OPENSTACK_COMPUTE` * `OPENSTACK_CONTROLLER` * `OPENTELEMETRY` * `OPENTRACING` * `OPEN_LIBERTY` * `ORACLE_DATABASE` * `ORACLE_DB_LISTENER` * `ORACLE_WEBLOGIC` * `OWIN` * `OWIN_KATANA` * `PERL` * `PHP` * `PHP_FPM` * `PLAY` * `PODMAN` * `POSTGRE_SQL` * `POSTGRE_SQL_DOTNET_DATA_PROVIDER` * `POWER_DNS` * `PROGRESS` * `PYTHON` * `QOS_LOGBACK` * `QUARKUS` * `R2DBC` * `RABBITMQ_CLIENT` * `RABBIT_MQ` * `REACTOR_CORE` * `REDIS` * `REQUESTS` * `RESTEASY` * `RESTLET` * `RIAK` * `RKE2` * `RSOCKET` * `RUBY` * `RUNC` * `RXJAVA` * `SAG_WEBMETHODS_IS` * `SANIC` * `SAP` * `SAP_HANADB` * `SAP_HYBRIS` * `SAP_MAXDB` * `SAP_SYBASE` * `SCALA` * `SECURITY_SOFTWARE` * `SELINUX` * `SHAREPOINT` * `SHELL` * `SLIM` * `SPARK` * `SPRING` * `SQLITE` * `STARLETTE` * `SYMFONY` * `THRIFT` * `TIBCO` * `TIBCO_BUSINESS_WORKS` * `TIBCO_EMS` * `TORNADO` * `UNDERTOW_IO` * `URLLIB3` * `VARNISH_CACHE` * `VERTX` * `VIM2` * `VIOS` * `VIRTUAL_MACHINE_KVM` * `VIRTUAL_MACHINE_QEMU` * `WCF` * `WILDFLY` * `WINDOWS_CONTAINERS` * `WINDOWS_SYSTEM` * `WINK` * `WORDPRESS` * `YII` * `ZERO_MQ` * `ZOS_CONNECT` | path | Обязательный |
| tag | string[] | Фильтрует итоговый набор хостов по указанному тегу. Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам. | query | Необязательный |
| managementZone | integer | Возвращает только хосты, входящие в указанную management zone. | query | Необязательный |
| hostGroupId | string | Фильтрует итоговый набор хостов по указанной группе хостов. Укажите Dynatrace ID нужной группы хостов. | query | Необязательный |
| hostGroupName | string | Фильтрует итоговый набор хостов по указанной группе хостов. Укажите имя нужной группы хостов. | query | Необязательный |
| pageSize | integer | Количество результатов на странице. Должно быть от 1 до 500 | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostList](#openapi-definition-HostList) | Успешно |

### Объекты тела ответа

#### Объект `HostList`

Список хостов, поддерживаемых расширением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hosts | [Host](#openapi-definition-Host)[] | Список хостов |
| nextPageKey | string | Ключ следующей страницы, используется для постраничной навигации |
| totalResults | integer | Общее число результатов |

#### Объект `Host`

Данные хоста. Содержит ID, имя, группу хостов и теги.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hostGroup | [HostGroup](#openapi-definition-HostGroup) | Host Group, к которой принадлежит хост. |
| id | string | ID хоста |
| managementZones | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation)[] | Список management zones, к которым принадлежит хост. |
| name | string | Имя хоста |
| tags | [TagInfo](#openapi-definition-TagInfo)[] | Список тегов хоста. |

#### Объект `HostGroup`

Host Group, к которой принадлежит хост.

| Элемент | Тип | Описание |
| --- | --- | --- |
| meId | string | Dynatrace ID сущности группы хостов. |
| name | string | Имя Dynatrace сущности, отображаемое в интерфейсе. |

#### Объект `EntityShortRepresentation`

Краткое представление Dynatrace сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание Dynatrace сущности. |
| id | string | ID Dynatrace сущности. |
| name | string | Имя Dynatrace сущности. |

#### Объект `TagInfo`

Тег Dynatrace сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать следующие значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега. Для пользовательских тегов здесь указывается значение тега. |
| value | string | Значение тега. Не применяется к пользовательским тегам. |

### Модели тела ответа JSON

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

## Похожие темы

* [Разработка собственных Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")