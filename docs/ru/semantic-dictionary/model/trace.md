---
title: Трассировки
source: https://www.dynatrace.com/docs/semantic-dictionary/model/trace
scraped: 2026-03-06T21:22:51.171538
---

# Трассировки

# Трассировки

* Latest Dynatrace
* Reference
* Published Feb 23, 2026

Распределённые трассировки используются для захвата транзакций, проходящих через систему. Трассировки
состоят из спанов, которые представляют собой единицы работы в рамках распределённой трассировки.

## Спаны CICS Transaction Gateway

Семантические соглашения для спанов запросов и ответов CTG, захваченных на сервере или клиенте CTG.
`span.kind` равен `client` для спанов, захваченных на клиенте CTG, и `server` для спанов, захваченных на сервере CTG. Это применяется как к запросам, так и к ответам.

CTG поддерживает различные типы запросов, такие как ECI, ESI или EPI. Тип вызова и коды ответов имеют различную семантику в зависимости от типа запроса.
Кроме того, некоторые поля заполняются только для определённых типов запросов.

### Запрос

Спаны запросов имеют атрибуты, соответствующие следующей таблице:

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.user_id` | string | experimental The user ID of the user who triggered this transaction. | `USER1`; `anon` |
| `ctg.request.call_type` | long | experimental Integer representing the call type of the CTG GatewayRequest. The set of possible values varies per request type. [1](#fn-1-1-def) | `2` |
| `ctg.request.commarea_length` | long | experimental Length of the COMMAREA. Only set when the request type is ECI. | `0` |
| `ctg.request.extend_mode` | long | experimental Integer representing the extended mode of the CTG GatewayRequest. Only set when the request type is ECI. [2](#fn-1-2-def) | `11` |
| `ctg.request.flow_type` | long | experimental Integer representing the flow type of the CTG GatewayRequest. [3](#fn-1-3-def) | `5` |
| `ctg.request.gateway_url` | string | experimental URL of the gateway. Only set on client-side spans. | `tcp://1.2.3.4:5678/` |
| `ctg.request.object_name` | string | experimental Name of the request object. Only set when the request type is ADMIN. |  |
| `ctg.request.server_id` | string | experimental ID of the server. Not set for all request types. | `IPICTEST` |
| `ctg.request.term_id` | string | experimental Name of the terminal resource. Only set when the request type is EPI. | `CN02` |
| `ctg.request.type` | string | experimental Type of the CTG GatewayRequest. | `BASE` |
| `ibm.cics.program` | string | resource experimental The name of the CICS program. | `EDUCHAN` |
| `network.transport` | string | stable [OSI Transport Layerï»¿](https://osi-model.com/transport-layer/) or [Inter-process Communication methodï»¿](https://en.wikipedia.org/wiki/Inter-process_communication) | `tcp`; `udp` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |
| `zos.transaction.id` | string | experimental The ID of this transaction. | `CEMT`; `DTAX`; `IVTNO` |

1

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

2

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

3

Значения определены в исходном коде IBM CTG API.

`ctg.request.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ADMIN` | Admin request. |
| `AUTH` | Authentication request. |
| `BASE` | Base. A base GatewayRequest without a further subtype. [1](#fn-2-1-def) |
| `ECI` | External Call Interface. Enables a client application to call a CICS program synchronously or asynchronously. [2](#fn-2-2-def) |
| `EPI` | External Presentation Interface. Enables a user application to install a virtual IBM 3270 terminal into a CICS server. [3](#fn-2-3-def) |
| `ESI` | External Security Interface. Enables user applications to perform security-related tasks. [4](#fn-2-4-def) |
| `XA` | CICS Request Exit. It can be used for request retry, dynamic server selection, and rejecting non-valid requests. [5](#fn-2-5-def) |

1

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequestï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequest)

2

[https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eciï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eci)

3

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epiï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epi)

4

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esiï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esi)

5

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exitï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exit)

`network.transport` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `inproc` | In-process communication. [1](#fn-3-1-def) |
| `other` | Something else (non-IP-based). |
| `pipe` | Named or anonymous pipe. |
| `tcp` | TCP |
| `udp` | UDP |
| `unix` | Unix domain socket. |

1

Указывает на то, что используется только внутрипроцессное взаимодействие без «реального» сетевого протокола в случаях, когда сетевые атрибуты обычно ожидаются. Как правило, все остальные сетевые атрибуты можно опустить.

### Ответ

Спаны ответов имеют атрибуты, соответствующие следующей таблице:

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ctg.request.type` | string | experimental Type of the CTG GatewayRequest. | `BASE` |
| `ctg.response.code` | long | experimental CTG response code. The set of possible values varies per request type. [1](#fn-4-1-def) | `-23` |

1

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

`ctg.request.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ADMIN` | Admin request. |
| `AUTH` | Authentication request. |
| `BASE` | Base. A base GatewayRequest without a further subtype. [1](#fn-5-1-def) |
| `ECI` | External Call Interface. Enables a client application to call a CICS program synchronously or asynchronously. [2](#fn-5-2-def) |
| `EPI` | External Presentation Interface. Enables a user application to install a virtual IBM 3270 terminal into a CICS server. [3](#fn-5-3-def) |
| `ESI` | External Security Interface. Enables user applications to perform security-related tasks. [4](#fn-5-4-def) |
| `XA` | CICS Request Exit. It can be used for request retry, dynamic server selection, and rejecting non-valid requests. [5](#fn-5-5-def) |

1

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequestï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequest)

2

[https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eciï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eci)

3

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epiï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epi)

4

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esiï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esi)

5

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exitï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exit)

## Пользовательские сервисы

Спаны пользовательских сервисов представляют точки входа в сервис или точки входа к конкретным компонентам внутри более крупного приложения. Кодовые модули OneAgent могут создавать спаны пользовательских сервисов с помощью правил автоматической инструментации или напрямую через API OneAgent SDK.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `custom_service.method` | string | experimental The service method of a custom service. This field only exists if a custom service was created via Dynatrace OneAgent SDK. | `startTask`; `run`; `authenticate` |
| `custom_service.name` | string | experimental The name of a custom service. This field only exists if a custom service was created via Dynatrace OneAgent SDK. | `MyCustomService`; `AuthenticationComponent` |
| `supportability.custom_service.rule_id` | uid | experimental The ID of a custom service configuration rule. This field is only present if a custom service was configured as an automatic instrumentation rule in Dynatrace. | `4d76194c11a9426197a9062548f9e66e` |

## Спаны клиента базы данных

Семантические соглашения для спанов клиента базы данных. `span.kind` для спанов клиента базы данных равен `client`.

Спан, представляющий операцию клиента базы данных, может включать саму операцию и последующую обработку результатов (например, выборку из результирующего набора SQL, операции с курсором MongoDB и т. п.).
Кроме того, несколько похожих операций с базой данных могут быть агрегированы в один спан для повышения эффективности.

Атрибуты `aggregation` предоставляют информацию о том, сколько операций с базой данных было агрегировано.

Атрибуты `db.result.*` представляют детали обработки результатов.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `db.affected_item_count` | long | experimental The number of items (rows, documents,â¦) affected. | `32` |
| `db.collection.name` | string | stable The name of a collection (table, container) within the database. | `customers`; `public.users` |
| `db.cosmosdb.request_charge` | double | experimental The cost of the request in [Azure Cosmos DB request units (RU)ï»¿](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units). | `4.95`; `2.0` |
| `db.dynamodb.table_names` | string[] | experimental The list of tables the request targets. | `['Cats', 'Dogs']` |
| `db.namespace` | string | stable The name of the database, fully qualified within the server address and port. | `customers`; `test.users` |
| `db.operation.name` | string | stable The name of the operation or command executed, for example the MongoDB command name, SQL keyword, Redis command name,â¦ [1](#fn-6-1-def) | `drop`; `findAndModify`; `SELECT`; `PREPARE`; `GetItem`; `set`; `LPUSH`; `mutateIn`; `ReadItems` |
| `db.query.parameters` | record[] | experimental The query parameters used in db.query.text represented as a key and value map. For database systems without named keys, the map key is the string representation of the index starting with 0. Several database requests may get aggregated into a single span. Each entry in the array holds the bind parameters for one database request. Tags: `sensitive-spans` | `[{'name': 'paul', 'age': '23'}, {'name': 'mary', 'age': '32'}]`; `[{'0': 'paul', '1': '23'}, {'0': 'mary', '1': '32'}]` |
| `db.query.text` | string | stable The database query being executed. [2](#fn-6-2-def) | `SELECT * FROM wuser_table`; `SET mykey "WuValue"` |
| `db.result.duration_max` | duration | experimental The maximum duration in nanoseconds used for fetching the result. | `345` |
| `db.result.duration_min` | duration | experimental The minimum duration in nanoseconds used for fetching the result. | `123` |
| `db.result.duration_sum` | duration | experimental The total duration in nanoseconds used for fetching the result. | `234` |
| `db.result.exception_count` | long | experimental The number of exceptions encountered while fetching the result. | `2` |
| `db.result.execution_count` | long | experimental The number of operations executed on the result (for example, fetches from SQL result set, MongoDB cursor operations). | `12` |
| `db.result.roundtrip_count` | long | experimental The number of round-trips triggered by fetching the result. | `2` |
| `db.system` | string | experimental An identifier for the database management system (DBMS) product being used. See below for a list of well-known identifiers. | `mongodb`; `mysql` |
| `network.transport` | string | stable [OSI Transport Layerï»¿](https://osi-model.com/transport-layer/) or [Inter-process Communication methodï»¿](https://en.wikipedia.org/wiki/Inter-process_communication) | `tcp`; `udp` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |

1

В зависимости от данных, предоставленных при приёме, этот атрибут может быть получен, например, путём разбора `db.query.text`. Разбор может завершиться неудачей, или результат может быть неточным.

2

Значение может быть очищено для исключения конфиденциальной информации.

`db.system` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `adabas` | Adabas (Adaptable Database System) |
| `amazon-documentdb` | Amazon DocumentDB |
| `aurora-mysql` | Amazon Aurora MySQL |
| `aurora-postgresql` | Amazon Aurora PostgreSQL |
| `cache` | InterSystems CachÃ© |
| `cassandra` | Apache Cassandra |
| `clickhouse` | ClickHouse |
| `cloudscape` | Cloudscape |
| `cockroachdb` | CockroachDB |
| `coldfusion` | ColdFusion IMQ |
| `cosmosdb` | Microsoft Azure Cosmos DB |
| `couchbase` | Couchbase |
| `couchdb` | CouchDB |
| `db2` | IBM Db2 |
| `derby` | Apache Derby |
| `dl/i` | IBM DL/I |
| `dynamodb` | Amazon DynamoDB |
| `edb` | EnterpriseDB |
| `elasticsearch` | Elasticsearch |
| `filemaker` | FileMaker |
| `firebird` | Firebird |
| `firstsql` | FirstSQL |
| `geode` | Apache Geode |
| `h2` | H2 |
| `hanadb` | SAP HANA |
| `hbase` | Apache HBase |
| `hive` | Apache Hive |
| `hsqldb` | HyperSQL DataBase |
| `informix` | Informix |
| `ingres` | Ingres |
| `instantdb` | InstantDB |
| `interbase` | InterBase |
| `keyspaces-cassandra` | Amazon Keyspaces for Apache Cassandra |
| `mariadb` | MariaDB |
| `maxdb` | SAP MaxDB |
| `memcached` | Memcached |
| `mongodb` | MongoDB |
| `mssql` | Microsoft SQL Server |
| `mssqlcompact` | Microsoft SQL Server Compact |
| `mysql` | MySQL |
| `neo4j` | Neo4j |
| `neptune` | Amazon Neptune |
| `netezza` | Netezza |
| `opensearch` | OpenSearch |
| `oracle` | Oracle Database |
| `other_sql` | Some other SQL database. Fallback only. See notes. |
| `pervasive` | Pervasive PSQL |
| `pointbase` | PointBase |
| `postgresql` | PostgreSQL |
| `progress` | Progress Database |
| `redis` | Redis |
| `redshift` | Amazon Redshift |
| `spanner` | Cloud Spanner |
| `sqlite` | SQLite |
| `sybase` | Sybase |
| `teradata` | Teradata |
| `valkey` | Valkey |
| `vertica` | Vertica |

`network.transport` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `inproc` | In-process communication. [1](#fn-7-1-def) |
| `other` | Something else (non-IP-based). |
| `pipe` | Named or anonymous pipe. |
| `tcp` | TCP |
| `udp` | UDP |
| `unix` | Unix domain socket. |

1

Указывает на то, что используется только внутрипроцессное взаимодействие без «реального» сетевого протокола в случаях, когда сетевые атрибуты обычно ожидаются. Как правило, все остальные сетевые атрибуты можно опустить.

### Поля для базы данных DL/I

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `db.dli.pcb` | string | experimental The name of the program communication block associated with this DL/I method. | `3`; `MYPCBNAM` |
| `db.dli.segment_name` | string | experimental The name of the last segment that was matched or returned. | `PARTROOT` |
| `db.dli.segment_level` | string | experimental The hierarchical level of the segment that was matched or returned. | `3`; `24` |
| `db.dli.processing_options` | string | experimental The PCB processing options. | `GR` |
| `db.dli.terminal_name` | string | experimental The DL/I database or logical terminal name associated with this DL/I method. | `HWSAM5ZD`; `10505` |
| `db.dli.status_code` | string | experimental The DL/I status code. | `QC` |
| `db.dli.pcb_type` | string | experimental The PCB type. | `DC`; `DL/I`; `F/P` |

`db.dli.pcb_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DC` | Data communications. |
| `DL/I` | DL/I db. |
| `F/P` | Fast Path. |

## Ссылки Dynatrace RUM

Семантические соглашения для RUM-ссылки на спанах Dynatrace. RUM-ссылка предоставляет информацию о связи бэкенда с фронтендом от трассировок к Dynatrace RUM.
В отличие от ссылок на спаны, которые ссылаются на другие спаны, RUM-ссылка связывает спан с пользовательским событием и/или пользовательской сессией.

### По tracestate

Информация RUM-ссылки для корреляции спана с пользовательским событием и пользовательской сессией.

Этот механизм работает как с инструментацией OneAgent, так и с OpenTelemetry, и устанавливается, когда Dynatrace RUM инициирует распределённую трассировку с использованием заголовков W3C Trace Context.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.instance.id` | string | resource stable The RUM application instance ID. (This was formerly called the "Visitor id", "internal user ID", and "rxVisitor cookie value".) | `3735928559`; `1742973444821E7E6Q3E3SG28ATQPAGTT6T8HU92VFRFQ` |
| `dt.rum.session.id` | string | stable A unique ID that represents the user session. | `HOPCPWKILUKHFHWRRQGBHHPAFLUJUOSH-0`; `23626166142035610_1-0` |
| `span.id` | uid | stable The `span.id` on the user event. This `span.id` can be used together with the `trace.id` from the span to find the user event. | `f76281848bd8288c` |

### По server-timing и cookie

Информация RUM-ссылки для корреляции спана с пользовательским событием и пользовательской сессией.

Этот механизм требует инструментации OneAgent и устанавливается через HTTP-заголовок ответа `server-timing` и контекст сессии из HTTP-cookie.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.instance.id` | string | resource stable The RUM application instance ID. (This was formerly called the "Visitor id", "internal user ID", and "rxVisitor cookie value".) | `3735928559`; `1742973444821E7E6Q3E3SG28ATQPAGTT6T8HU92VFRFQ` |
| `dt.rum.is_linking_candidate` | boolean | experimental Indicates that a user event likely exists that can be correlated to this trace. Use the `trace.id` from the span to find the user event. | `true` |
| `dt.rum.session.id` | string | stable A unique ID that represents the user session. | `HOPCPWKILUKHFHWRRQGBHHPAFLUJUOSH-0`; `23626166142035610_1-0` |

### Только по server-timing

Информация RUM-ссылки для корреляции спана с пользовательским событием.

Этот механизм требует инструментации OneAgent и устанавливается через HTTP-заголовок ответа `server-timing`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.is_linking_candidate` | boolean | experimental Indicates that a user event likely exists that can be correlated to this trace. Use the `trace.id` from the span to find the user event. | `true` |

### По cookie

Информация RUM-ссылки для корреляции спана с пользовательской сессией.

Этот механизм требует инструментации OneAgent и устанавливается через контекст сессии, захваченный из HTTP-cookie.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.instance.id` | string | resource stable The RUM application instance ID. (This was formerly called the "Visitor id", "internal user ID", and "rxVisitor cookie value".) | `3735928559`; `1742973444821E7E6Q3E3SG28ATQPAGTT6T8HU92VFRFQ` |
| `dt.rum.session.id` | string | stable A unique ID that represents the user session. | `HOPCPWKILUKHFHWRRQGBHHPAFLUJUOSH-0`; `23626166142035610_1-0` |

## События спанов Dynatrace

Семантические соглашения для событий спанов на спанах Dynatrace.

### Общее

В целом, событие спана не обязано следовать специфическим семантикам, но, как правило, события спанов имеют следующие общие атрибуты.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span_event.name` | string | stable Some span events have a defined semantics based on the name of the span event. | `exception` |
| `supportability.dropped_attributes_count` | long | experimental The number of attributes that were discarded on the source. Attributes can be discarded because their keys are too long or because there are too many attributes. | `1` |
| `supportability.non_persisted_attribute_keys` | string[] | experimental A string array of attribute keys that were not stored as they were not allow-listed or were removed during the pipeline steps. | `['"my_span_attribute", "db.name"']` |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the event originated, typically when the source created it. If no original timestamp is available, it will be populated at ingest time and required for all events. In the case of a correlated event (for example, ITIL events), this time could be different from the event.start time, as this time represents the actual timestamp when the "update" for the event was created. | `1649822520123123123` |

Помимо общих атрибутов, для событий спанов разрешены любые произвольные атрибуты.

### Исключение

Если во время спана возникают и фиксируются исключения, они доступны как события спана. События исключений имеют `span_event.name`, установленный в `exception`. Помимо следующих атрибутов, специфичных для события исключения, применяются все семантики из общего раздела.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `exception.caused_by_id` | uid | stable The `exception.id` of the exception the current exception was caused by. |  |
| `exception.escaped` | boolean | stable `true` indicates that the exception was recorded at a point where it is known that the exception escaped the scope of the span. |  |
| `exception.id` | uid | stable The identifier of an exception. It should be unique within a list of exceptions of a span. The identifier is used to reference the exception. |  |
| `exception.is_caused_by_root` | boolean | stable Is set to `true` if the exception is the first exception caused by the chain. |  |
| `exception.message` | string | stable A message that describes the exception. | `Division by zero` |
| `exception.stack_trace` | string | experimental The stack trace of the exception. The format depends on the technology and source. While OneAgent formats stack traces to unify them across technologies, stack traces from an OpenTelemetry source are in the format they were sent to Dynatrace. | `@https://www.foo.bar/path/main.js:59:26 e@https://www.foo.bar/path/lib/1.1/lib.js:2:30315` |
| `exception.type` | string | stable The type of the exception, for example, its fully-qualified class name. | `java.net.ConnectException`; `OSError` |
| `span_event.name` | string | stable Is set to `exception` for exception events. | `exception` |

### Оценка флага функциональности

Оценка флага ДОЛЖНА быть записана как событие на спане, во время которого она произошла. События флагов функциональности имеют `span_event.name`, установленный в `feature_flag.evaluation`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `feature_flag.context.id` | string | experimental The unique identifier for the flag evaluation context. For example, the targeting key. | `5157782b-2203-4c80-a857-dbbd5e7761db` |
| `feature_flag.key` | string | experimental The unique identifier of the feature flag. | `logo-color` |
| `feature_flag.provider.name` | string | experimental The name of the service provider that performs the flag evaluation. | `Flag Manager` |
| `feature_flag.result.reason` | string | experimental The reason code, which shows how a feature flag value was determined. | `static`; `targeting_match`; `error`; `default` |
| `feature_flag.result.variant` | string | experimental A semantic identifier for an evaluated flag value. [1](#fn-8-1-def) | `red`; `true`; `on` |
| `feature_flag.set.id` | string | experimental The identifier of the [flag setï»¿](https://openfeature.dev/specification/glossary/#flag-set) to that the feature flag belongs. | `proj-1`; `ab98sgs`; `service1/dev` |
| `feature_flag.version` | string | experimental The version of the ruleset used during the evaluation. This can be any stable value that uniquely identifies the ruleset. | `1`; `01ABCDEF` |
| `span_event.name` | string | stable Is set to `feature_flag.evaluation` for feature flag events. | `feature_flag.evaluation` |

1

Семантический идентификатор, обычно называемый вариантом, предоставляет способ ссылаться на значение, не включая само значение. Это может обеспечить дополнительный контекст для понимания смысла значения.
Например, вариант `red` может использоваться для значения `#c05543`.

### Бизнес-события

Если спан связан с бизнес-событием, идентификаторы бизнес-событий доступны как события спана. События спанов имеют `span_event.name`, установленный в `bizevent`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `event.id` | string | stable Unique identifier string of an event; is stable across multiple refreshes and updates. | `5547782627070661074_1647601320000` |
| `span_event.name` | string | stable Is set to `bizevent` for bizevent events. | `bizevent` |

## Ссылки спанов Dynatrace

Семантические соглашения для известных ссылок спанов.

### По идентификатору спана и трассировки

Ссылка на спан по `span.id` и `trace.id` ссылается на целевой спан в другой трассировке.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.id` | uid | stable A unique identifier for a span within a trace. The `span.id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `supportability.dropped_attributes_count` | long | experimental The number of attributes that were discarded on the source. Attributes can be discarded because their keys are too long or because there are too many attributes. | `1` |
| `supportability.non_persisted_attribute_keys` | string[] | experimental A string array of attribute keys that were not stored as they were not allow-listed or were removed during the pipeline steps. | `['"my_span_attribute", "db.name"']` |
| `trace.alternate_id` | uid | experimental The preserved trace ID when OneAgent and other tracing systems monitor the same process and the trace ID from the other tracing system was replaced by the OneAgent trace ID. The `trace.alternate_id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `trace.id` | uid | stable A unique identifier for a trace. The `trace.id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `trace.state` | string | experimental The trace state in the w3c-trace-context format. | `f4fe05b2-bd92206c@dt=fw4;3;abf102d9;c4592;0;0;0;2ee;5607;2h01;3habf102d9;4h0c4592;5h01;6h5f9a543f1184a52b1b744e383038911c;7h6564df6f55bd6eae,apmvendor=boo,foo=bar` |

Помимо перечисленных выше атрибутов, на обобщённой ссылке спана разрешены любые другие произвольные атрибуты.

### По идентификатору пользовательской ссылки

Ссылка на спан по `dt.tracing.custom_link.id` ссылается на другой спан со ссылкой спана на тот же `dt.tracing.custom_link.id`. Эта ссылка спана используется для технологий, в которых полное распространение контекста с идентификатором спана и трассировки невозможно, и между уровнями может передаваться лишь ограниченное количество информации.

`dt.tracing.link.direction` определяет иерархию между двумя спанами, имеющими ссылки спанов с одинаковым `dt.tracing.custom_link.id`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.tracing.custom_link.id` | uid | experimental The custom link ID to identify spans calling each other. The ID is derived from the custom link bytes. | `736bd2684696c4a8` |
| `dt.tracing.custom_link.original_bytes` | binary | experimental The original binary data of the custom link. | `ycXlxUBAQEDee9lm8pBcA8nF5cVAQEBA3nvZZvKQXAPee9lm8s4SAQ==` |
| `dt.tracing.custom_link.transformed_bytes` | binary | experimental The transformed binary data of the custom link. Only available if a mapping was applied. | `ycXlxUBAQEDee9lm8pBcA8nF5cVAQEBA3nvZZvKQXAPee9lm8s4SAQ==` |
| `dt.tracing.custom_link.type` | string | experimental The type of the custom link defines if a mapping of the `dt.tracing.custom_link.original_bytes` to the `dt.tracing.custom_link.transformed_bytes` was applied. | `generic` |
| `dt.tracing.link.direction` | string | experimental The direction of the span link to define the correct order between spans. | `outgoing` |
| `dt.tracing.link.is_sync` | boolean | experimental `true` indicates that the caller waits on the response. Only available on span links with `dt.tracing.link.direction` set to `outgoing`. |  |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the span was propagated. Only available on span links with `dt.tracing.link.direction` set to `outgoing`. | `1649822520123123123` |

### По идентификатору ссылки Dynatrace

Ссылка Dynatrace предоставляет дополнительные сведения о времени родительского и дочернего элементов в дополнение к `span.parent_id`.
Эти данные являются необязательными и предоставляются не всеми источниками данных спанов.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.tracing.link.direction` | string | experimental The direction of the span link to define the correct order between spans. | `outgoing` |
| `dt.tracing.link.id` | uid | experimental Unique identifier for a Dynatrace link. |  |
| `dt.tracing.link.is_sync` | boolean | experimental `true` indicates that the caller waits on the response. Only available on span links with `dt.tracing.link.direction` set to `outgoing`. |  |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the span was propagated. Only available on span links with `dt.tracing.link.direction` set to `outgoing`. | `1649822520123123123` |

### По внешней ссылке

Ссылка спана по `dt.tracing.foreign_link` ссылается на вышестоящую транзакцию. Это может быть ссылка между средами или ссылка между продуктами на распределённую трассировку в устаревшем продукте AppMon.
В зависимости от того, была ли информация о ссылке получена в двоичном или текстовом виде, будет установлено либо `dt.tracing.foreign_link.bytes`, либо `dt.tracing.foreign_link.text` соответственно.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.tracing.foreign_link.bytes` | binary | experimental An incoming foreign link (cross-environment or cross-product). | `00000004000000010000000200000003000000040000002300000001` |
| `dt.tracing.foreign_link.text` | string | experimental An incoming foreign link (cross-environment or cross-product). | `FW4;129;12;-2023406815;4539717;0;17;66;c511;2h02;3h12345678;4h676767`; `FW1;129;4711;59959450;-1859959450;3;17;0` |

### По заголовкам ответа

Ссылка спана по `dt.tracing.response.headers` ссылается на нижестоящую транзакцию. Это может быть ссылка между средами.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.tracing.response.headers` | record | experimental A collection of key-value pairs containing received response headers related to tracing from an outgoing call. There may be multiple values for each header. Used for cross-environment linking. | `{'traceresponse': ['00-7b9e3e4068167838398f50017bfad358-d4ffc7e33530967a-01'], 'x-dt-tracestate': ['9651e1a8-19506b7c@dt']}` |

## Спан Dynatrace

Семантические соглашения для спана Dynatrace и поля, которые пользователь может ожидать.

### Иерархические атрибуты

Следующие иерархические атрибуты являются обязательными.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.alternate_parent_id` | uid | experimental The alternative `span.id` of this span's parent span. If a trace is monitored by more tracing systems (for example, OneAgent and OpenTelemetry), there might be two parent spans. If the two parent spans differ, `span.parent_id` holds the ID of the parent span originating from same tenant of the span while `span.alternate_parent_id` holds the other parent span ID. The `span.alternate_parent_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `span.id` | uid | stable A unique identifier for a span within a trace. The `span.id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `span.is_subroutine` | boolean | experimental If set to `true`, it indicates that this span is a subroutine of its parent span. The spans represent functions running on the same thread on the same call stack. |  |
| `span.kind` | string | stable Distinguishes between spans generated in a particular context. | `server` |
| `span.parent_id` | uid | stable The `span.id` of this span's parent span. The `span.parent_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `trace.id` | uid | stable A unique identifier for a trace. The `trace.id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |

### Атрибуты времени

Атрибуты `start_time`, `end_time` и `duration` являются обязательными для всех спанов.
Атрибуты в пространстве имён `span.timing` являются необязательными и представляют измерения, предоставленные OneAgent.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `duration` | duration | stable The difference between `start_time` and `end_time` in nanoseconds. | `42` |
| `end_time` | timestamp | stable End time of a data point. Value is a UNIX Epoch time in nanoseconds and greater than or equal to the `start_time`. | `1649822520123123165` |
| `span.timing.cpu` | duration | stable The overall CPU time spent executing the span, including the CPU times of child spans that are running on the same thread on the same call stack. |  |
| `span.timing.cpu_self` | duration | stable The CPU time spent exclusively on executing this span, not including the CPU times of any children. |  |
| `start_time` | timestamp | stable Start time of a data point. Value is a UNIX Epoch time in nanoseconds and less than or equal to the `end_time`. | `1649822520123123123` |

### Атрибуты агрегирования

OneAgent может агрегировать спаны с одним родительским спаном в единый. Агрегированный спан содержит атрибуты, указывающие на то, что агрегирование произошло, и позволяющие восстановить детали.

Для агрегированных спанов `start_time` содержит наименьшее значение `start_time`, а `end_time` — наибольшее значение `end_time` среди всех агрегированных спанов. Как и для неагрегированных спанов, `duration` — это разница между `start_time` и `end_time`, которая может отличаться от `aggregation.duration_sum`, поскольку агрегированные спаны могли выполняться параллельно или между ними были промежутки.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aggregation.count` | long | stable The number of spans aggregated into this span. Because this span represents multiple spans, the value is >1. | `3` |
| `aggregation.duration_max` | duration | stable The duration in nanoseconds for the longest aggregated span. | `482` |
| `aggregation.duration_min` | duration | stable The duration in nanoseconds for the shortest aggregated span. | `42` |
| `aggregation.duration_samples` | duration[] | stable Array of reservoir sampled span durations of the aggregated spans. The duration samples can be used to estimate a more accurate duration distribution of aggregated spans rather than the average value. | `[42, 482, 301]` |
| `aggregation.duration_sum` | duration | stable The duration sum in nanoseconds for all aggregated spans. | `123` |
| `aggregation.exception_count` | long | stable The number of aggregated spans that included an exception. | `0`; `6` |
| `aggregation.parallel_execution` | boolean | stable `true` indicates that aggregated spans may have been executed in parallel. Therefore, `start_time + duration_sum` may exceed `end_time`. |  |

### Атрибуты выборки

Если спан не представляет один отдельный спан, он может иметь атрибуты для поддержки экстраполяции его значений.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `sampling.threshold` | long | experimental The sampling probability is encoded as `sampling.threshold` with respect to a 56-bit random integer `rv`. A span is sampled if `rv >= sampling.threshold`; the sampling threshold acts as a rejection threshold and can be interpreted as the number of spans discarded out of 2^56. The attribute is only available if the `sampling.threshold` is not `0`, and therefore sampling happened. The relationship between sampling probability and threshold is `sampling probability = (2^56-sampling.threshold) * 2^(-56)`. Hence, `sampling.threshold=0` means 100% sampling probability (collect all data), `sampling.threshold=2^55` corresponds to a sampling probability of 50%, `sampling.threshold=2^54` corresponds to a sampling probability of 75%. | `36028797018963968` |
| `supportability.alr_sampling_ratio` | long | experimental The denominator of the sampling ratio of the Dynatrace cluster, the attribute is only set if Adaptive Load Redution (ALR) is active on the Dynatrace cluster. A numerator is not specified, as it's always 1. If, for example, the Dynatrace cluster samples with a probability of 1/8 (12,5%), the value of `supportability.alr_sampling_ratio` would be 8 and the numerator is 1. | `8` |
| `supportability.atm_sampling_ratio` | long | experimental The denominator of the sampling ratio of an Adaptive Traffic Management (ATM) aware sampler. The attribute is always present if an ATM-aware sampler is active (this applies, for example, to Dynatrace OneAgent). A numerator is not specified, as it is always 1. If, for example, Dynatrace OneAgent samples with a probability of 1/16 (6,25%), the value of `supportability.atm_sampling_ratio` would be 16 and the numerator is 1. | `16` |
| `trace.capture.reasons` | string[] | experimental Explains why this trace was captured, multiple reasons can apply simultaneously. Note: The sampling approach ('atm' or 'fixed') is always placed at the first position in the array. These two values are mutually exclusive, though 'fixed' may appear with other capture triggers. Values: 'atm' (Dynatrace's intelligent sampling automatically adjusted trace capture based on traffic volume and system load), 'fixed' (trace captured due to configured percentage rules - either global settings or specific endpoint rules), 'custom' (trace captured because of custom correlation headers propagated between services or systems), 'mainframe' (trace originated from or includes IBM mainframe/z/OS components), 'serverless' (trace captured from serverless functions like AWS Lambda, Azure Functions, or similar platforms), 'rum' (trace initiated by user interactions in web browsers or mobile apps monitored by Dynatrace RUM agents). | `['atm']`; `['fixed']`; `['fixed', 'custom']`; `['fixed', 'rum']` |

В настоящее время выборка может происходить на двух этапах обработки данных. Независимо от того, где происходит выборка, спан имеет `sampling.threshold` для вычисления общей (эффективной) частоты дискретизации. Атрибуты поддерживаемости помогают понять выборку на разных этапах.

* OneAgent: если в OneAgent включено адаптивное управление трафиком (ATM), агент выполняет выборку PurePaths и атрибут `supportability.atm_sampling_ratio` добавляется ко всем затронутым спанам.
* Кластер Dynatrace: если кластер Dynatrace перегружен, он запускает адаптивное снижение нагрузки (ALR) и выполняет выборку PurePaths. Атрибут `supportability.alr_sampling_ratio` добавляется ко всем затронутым спанам.

Например, если OneAgent выполняет выборку с вероятностью 25%, спаны будут содержать атрибуты `sampling.threshold=54043195528445952` и `supportability.atm_sampling_ratio=4`.

Подробности об адаптивном управлении трафиком для распределённой трассировки можно найти в [документации](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.").

### Атрибуты кода

Когда спан логически представляет выполнение функции, он будет иметь атрибуты `code.*`, описывающие эту функцию.

Атрибуты `invoked.code.*` описывают функцию, в которой был запущен спан, но не обязательно завершён. Как правило, это функция, которая была инструментирована для запуска спана. Эти атрибуты заполняются только в случае несовпадения с `code.*`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `code.function` | string | experimental The method or function name, or equivalent (usually the rightmost part of the code unit's name). Represents the name of the function that is represented by this span. | `serveRequest` |
| `code.namespace` | string | experimental The namespace within which `code.function` is defined. Usually, the qualified class or module name, such that `code.namespace` + some separator + `code.function` forms a unique identifier for the code unit. | `com.example.MyHttpService` |
| `code.filepath` | string | experimental The source code file name that identifies the code unit as uniquely as possible. | `/usr/local/MyApplication/content_root/app/index.php` |
| `code.line.number` | long | experimental The line number within the source code file. | `1337` |
| `code.invoked.function` | string | experimental Like `code.function`, only it represents the function that was active when a span has been started. Typically, it's the function that has been instrumented. The spans duration does not reflect the duration of this function execution. It should only be set if it differs from `code.function`. | `invoke` |
| `code.invoked.namespace` | string | experimental Like `code.namespace`, only it represents the namespace of the function that was active when a span has been started. Typically, it's the function that has been instrumented. It should only be set if it differs from `code.namespace`. | `com.sun.xml.ws.server.InvokerTube$2` |
| `code.invoked.filepath` | string | experimental Like `code.filepath`, only it represents the file path of the function that was active when a span has been started. Typically, it is the function that has been instrumented. It should only be set if it differs from `code.filepath`. | `/usr/local/MyApplication/content_root/app/index.php` |
| `code.call_stack` | string | experimental The call stack of the `code.function`. The call stack starts with the `code.function`, and the stack frames are separated by a line feed. | `com.example.SampleClass.doProcessing(SampleClass.java) com.example.SampleClass.doSomeWork(SampleClass.java) com.example.SampleClass.main(SampleClass.java)` |

### События

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.events` | record[] | stable A collection of events. An event is an optional time-stamped annotation of the span and consists of a name and key-value pairs. |  |
| `supportability.dropped_events_count` | long | experimental The number of span events that were discarded on the source. | `1` |

События спанов имеют собственную семантику, определённую здесь.

#### События исключений

Если выход из спана произошёл через исключение или спан содержит другие события исключений, для ссылки на правильное исключение в списке `span.events` доступны следующие поля.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.exit_by_exception_id` | uid | stable The `exception.id` of the exception the its `span.events` with the current span exited. The referenced exception has set the attribute `exception.escaped` to true. |  |
| `span.is_exit_by_exception` | boolean | stable Set to `true` if an exception exited the span. If set to `false`, the span has exception events, but none exited the span. |  |

### Ссылки

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.links` | record[] | stable A collection of links. A link is a reference from this span to a whole trace or a span in the same or different trace. |  |
| `supportability.dropped_links_count` | long | experimental The number of span links that were discarded on the source. | `1` |

Ссылки спанов имеют собственную семантику, определённую здесь.

### RUM-ссылка

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rum_link` | record | experimental A RUM link provides backend to frontend linking information from traces to Dynatrace RUM. Unlike span links which reference other spans, the RUM link connects a span to a user event and/or user session. |  |

RUM-ссылка имеет собственную семантику, определённую здесь.

### Обнаружение сбоев

Поля, которые можно ожидать при обнаружении сбоев на спане Dynatrace.
Обнаружение сбоев применяется к спанам, представляющим запросы к конечным точкам и входящим прокси сервисной сети Istio.
Запрос считается неудачным, если обнаружена хотя бы одна причина сбоя и не совпадает ни одно правило принудительного успеха. Объединённый результат (сбой или успех) сохраняется в атрибуте `request.is_failed` (см. также Запрос).
Чтобы изменить поведение обнаружения сбоев, измените его конфигурацию.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.failure_detection.ruleset_id` | uid | experimental The `id` of the failure detection rule set (failure detection v2) that was applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66e` |
| `dt.failure_detection.general_parameters_id` | uid | experimental The `id` of the failure detection general parameters (failure detection v1) that were applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66f` |
| `dt.failure_detection.http_parameters_id` | uid | experimental The `id` of the failure detection HTTP parameters (failure detection v1) that were applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66a` |
| `dt.failure_detection.global_rule_id` | uid | experimental The `id` of the global failure detection rule (failure detection v1) that was applied to that span (uid128).  This is always used in conjunction with the `dt.failure_detection.global_parameters_id`. | `4d76194c11a9426197a9062548f9e66b` |
| `dt.failure_detection.global_parameters_id` | uid | experimental The `id` of the global failure detection parameters (failure detection v1) that were applied to that span (uid128).  This is always used in conjunction with the `dt.failure_detection.global_rule_id`. | `4d76194c11a9426197a9062548f9e66c` |
| `dt.failure_detection.verdict` | string | experimental The final failure detection verdict based on the results in `dt.failure_detection.results`. | `failure` |
| `dt.failure_detection.results` | record[] | experimental A collection of individual failure detection reasons and verdicts for each applied matching rule. If no entries exist, no rules matched, and the attribute does not exist. |  |

`dt.failure_detection.verdict` MUST be one of the following:

| Value | Description |
| --- | --- |
| `failure` | There is at least one result with verdict `failure` and no result with verdict `success`. |
| `success` | There is at least one result with verdict `success` or no result at all. |

Обнаружение сбоев имеет собственную семантику, определённую здесь.

### Атрибуты сервера и клиента

Эти атрибуты могут использоваться для описания клиента и сервера при сетевом взаимодействии на основе соединений, где одна сторона (клиент) инициирует соединение.
Это охватывает все сетевые взаимодействия TCP, поскольку TCP основан на соединениях и одна сторона инициирует соединение (исключение сделано для однорангового взаимодействия через TCP, где «пользовательская» поверхность протокола/API не раскрывает чёткого понятия клиента и сервера).
Это также охватывает сетевые взаимодействия UDP, где одна сторона инициирует взаимодействие, например QUIC (HTTP/3) и DNS.

В идеальной ситуации, без учёта прокси, нескольких IP-адресов или имён хостов, атрибуты `server.*` одинаковы как на клиентском, так и на серверном спане.

#### Атрибуты сервера

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |

##### `server.address`

Для IP-связи имя должно быть DNS-именем хоста службы. На стороне клиента оно соответствует имени удалённой службы, на стороне сервера представляет имя локальной службы, видимое клиентами извне.

При подключении к URL `https://example.com/foo`, `server.address` соответствует `"example.com"` как на стороне клиента, так и на стороне сервера.

На стороне клиента, как правило, передаётся в форме URL, строки подключения, имени хоста и т. д. Иногда имя хоста доступно только в виде строки, которая может содержать DNS-имя или IP-адрес.

Если `network.transport` равен `pipe`, абсолютный путь к файлу, представляющему его, используется как `server.address`.

Для Unix domain socket атрибут `server.address` представляет адрес удалённой конечной точки на стороне клиента и адрес локальной конечной точки на стороне сервера.

#### Атрибуты клиента

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `client.ip` | ipAddress | experimental The IP address of the client that makes the request. This can be IPv4 or IPv6. Tags: `sensitive-spans` `sensitive-user-events` | `194.232.104.141`; `2a01:468:1000:9::140` |
| `client.port` | long | stable Client port number. | `65123`; `80` |
| `client.isp` | string | experimental The name of the Internet Service Provider (ISP) associated with the client's IP address. | `Internet Service Provider Name` |
| `client.ip.is_public` | boolean | experimental Indicates whether IP is a public IP. | `true` |
| `client.app.name` | string | experimental The name of the client application used to perform the request. | `MS Outlook` |
| `client.address` | string | experimental Client address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name. | `client.example.com`; `10.1.2.80`; `[local]` |

### Атрибуты поддерживаемости

Атрибуты поддерживаемости помогают понять характеристики спана.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `supportability.dropped_attributes_count` | long | experimental The number of attributes that were discarded on the source. Attributes can be discarded because their keys are too long or because there are too many attributes. | `1` |
| `supportability.non_persisted_attribute_keys` | string[] | experimental A string array of attribute keys that were not stored as they were not allow-listed or were removed during the pipeline steps. | `['"my_span_attribute", "db.name"']` |
| `trace.alternate_id` | uid | experimental The preserved trace ID when OneAgent and other tracing systems monitor the same process and the trace ID from the other tracing system was replaced by the OneAgent trace ID. The `trace.alternate_id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `trace.state` | string | experimental The trace state in the w3c-trace-context format. | `f4fe05b2-bd92206c@dt=fw4;3;abf102d9;c4592;0;0;0;2ee;5607;2h01;3habf102d9;4h0c4592;5h01;6h5f9a543f1184a52b1b744e383038911c;7h6564df6f55bd6eae,apmvendor=boo,foo=bar` |

### Транзакции

Транзакции предоставляют унифицированную семантическую модель для всех типов транзакций сервиса. Транзакция представляет собой дискретную единицу входящей работы внутри сервиса: запрос к конечной точке, обработку сообщения или вызов FaaS.
Один корневой спан транзакции может одновременно иметь несколько установленных атрибутов типа. Например, Lambda, запущенная через HTTP, имеет и `transaction.is_faas_invocation = true`, и `transaction.is_endpoint_request = true`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `transaction.is_endpoint_request` | boolean | experimental Indicates that this transaction is an endpoint request. Set by the endpoint detection ruleset. |  |
| `transaction.is_faas_invocation` | boolean | experimental Indicates that this transaction is a FaaS invocation. Set when `faas.trigger` exists and `span.kind` is `server` or `consumer`. |  |
| `transaction.is_failed` | boolean | experimental Indicates that the transaction is considered failed according to the failure detection rules. Only present on the transaction root span. |  |
| `transaction.is_message_processing` | boolean | experimental Indicates that this transaction is a message processing transaction. Set when `messaging.operation.type == "PROCESS"`. |  |
| `transaction.is_root_span` | boolean | experimental Marks the root span of a transaction. A span becomes a transaction root if at least one transaction type attribute is set. |  |

#### Сервисная сеть

Спаны сервисной сети представляют запросы, проксируемые через уровень сервисной сети (например, Istio Envoy).
Они не представляют транзакции сервиса (`transaction.is_root_span` не установлен).

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `transaction.service_mesh.is_failed` | boolean | experimental Indicates that the service mesh request is considered failed according to the failure detection rules. Only present on the service mesh root span. |  |
| `transaction.service_mesh.is_root_span` | boolean | experimental Marks the root span of a service mesh request. Set by the service mesh detection ruleset. |  |

#### Атрибуты запроса

Атрибуты запроса позволяют обогащать спаны, собранные OneAgent, данными глубокого анализа, которые по умолчанию не фиксируются в данных трассировки.
Они моделируются как:

* Захваченные атрибуты, представляющие необработанное значение, сообщённое OneAgent.
* Атрибуты запроса, представляющие нормализованное значение для полного запроса.

Имена атрибутов запроса и захваченных атрибутов составляются из префиксов "captured\_attribute" и "request\_attribute" и имени, заданного пользователем в конфигурации:

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `captured_attribute.__attribute_name__` | array | stable Contains the span scoped raw values that were captured under the name `__attribute_name__` defined by the request attribute configuration. The values are mapped as an array according to the type of the captured attributes, so either boolean, double, long, or string. If the captured attributes have mixed types (e.g. long and string, or double and long, etc.), all attributes are converted to string and stored as string array. | `[42]`; `['Platinum']`; `[32, 16, 8]`; `['Special Offer', '1702']`; `['18.35', '16']` |
| `request_attribute.__attribute_name__` | array | stable Contains the request scoped reconciled values of the attribute named `__attribute_name__` defined by the request attribute configuration. The data type of the value depends on the request attribute definition. Tags: `sensitive-spans` | `42`; `Platinum`; `['Product A', 'Product B']`; `['Special Offer', '1702']` |

### Размер спана

Вычисленные размеры спана в байтах. `dt.ingest.size` вычисляется при получении спана, а `dt.retain.size` — до сохранения спана.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.ingest.size` | long | stable The size of the ingested data point in bytes. | `2005` |
| `dt.retain.size` | long | stable The size of the retained data point in bytes. | `2005` |

### Статус

Спан содержит статус, состоящий из кода и необязательного описательного сообщения. Статус особенно важен, если в коде приложения имеется известная ошибка, например исключение, в этом случае статус спана может быть установлен в `error`. Статус спана присутствует только в том случае, если он явно установлен в `error` или `ok`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.status_code` | string | stable Defines the status of a span, predominantly used to indicate a processing error. This field is absent if the reported span status is `unset`. | `error` |
| `span.status_message` | string | experimental An optional text that can provide a descriptive error message in case the `span.status_code` is `error`. | `Connection closed before message completed`; `Error sending request for url` |

#### Причины статуса ошибки

Следующие причины приводят к установке `span.status_code` в `error`:

* Если выход из спана произошёл через исключение, т. е. атрибут `span.is_exit_by_exception` установлен в `true`.
* Спаны HTTP:

  + Общее: для значений `http.response.status_code` в диапазоне `5xx`.
  + Если `span.kind` равен `client`: для значений `http.response.status_code` в диапазоне `4xx`.
* Спаны gRPC:

  + Если `span.kind` равен `client`: для всех значений `rpc.grpc.status_code` кроме `OK (0)`.
  + Если `span.kind` равен `server`: для значений `rpc.grpc.status_code` `UNKNOWN (2)`, `DEADLINE_EXCEEDED (4)`, `UNIMPLEMENTED (12)`, `INTERNAL (13)`, `UNAVAILABLE (14)`, `DATA_LOSS (15)`.

### Дополнительные атрибуты

Помимо перечисленных выше атрибутов, на спане разрешены любые другие произвольные атрибуты.

## Спаны ESB

Семантические соглашения для спанов ESB (Enterprise Service Bus). Спан ESB содержит информацию о среде, в которой создаётся спан. Эти метаданные включают, например, рабочий процесс, в котором размещён спан, и приложение или библиотеку, которой принадлежит рабочий процесс.

### Атрибуты

Имя `workflow` является обязательной информацией и в наибольшей степени способствует идентификации источника спана.
`application` и `library` обеспечивают высокоуровневое представление о том, к какому развёртыванию принадлежит спан.
Также стоит отметить, что `application` и `library` обычно рассматриваются как взаимоисключающие, хотя это никак не принудительно."

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `esb.application.name` | string | resource experimental The name of the application that owns the current workflow. | `myBusinessApp`; `YourServiceApp`; `any_work` |
| `esb.library.name` | string | resource experimental The name of the library that owns the current workflow. | `myWebServicesLib`; `YourMessagingLibrary`; `any_tools` |
| `esb.vendor` | string | resource experimental The name of vendor of the ESB technology of the current workflow. | `ibm`; `tibco` |
| `esb.workflow.is_subprocess` | boolean | experimental Defines whether the provided workflow is a subprocess or not. | `false` |
| `esb.workflow.name` | string | resource experimental The label of the current workflow. | `myMessageFlow`; `YourBusinessWorkflow`; `any_flow` |

## Результат обнаружения сбоев

Запись, содержащая поля, которые можно ожидать для результата обнаружения сбоев. Эти результаты являются частью (в виде массива записей) набора полей, используемых функцией обнаружения сбоев, и ссылаются на них через `failure_detection.results`.
Эта запись относится к обнаружению сбоев v1 и v2.

* Обнаружение сбоев v1 будет производить только один результат в массиве.
* Обнаружение сбоев v2 может производить несколько причин сбоев. Каждое совпавшее правило набора правил обнаружения сбоев будет производить один результат.

### Поля

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `custom_rule_name` | string | experimental Name of the custom rule that caused this result. Uniquely identifies the rule within a failure detection v2 rule set. Related to the `custom_rule` reason. | `Fail on my.failure.attribute==failed` |
| `exception_ids` | uid | experimental IDs of the exceptions that caused this rule result (more on exceptions). | `[123423523456, 523463467234]` |
| `reason` | string | experimental All possible failure detection reasons that caused a verdict. | `exception` |
| `request_attribute_name` | string | experimental Name of the request attribute that caused this result. Related to a custom error rule in a failure detection v1 configuration and the `custom_error_rule` reason. | `my special method count RA` |
| `verdict` | string | experimental All possible failure detection verdicts. | `failure` |

`reason` MUST be one of the following:

| Value | Description |
| --- | --- |
| `custom_error_rule` | Verdict is caused by a custom error rule (request attribute). Applicable in failure detection v1.  This reason always comes together with the `request_attribute_name` field. |
| `custom_rule` | Verdict is caused by a custom rule. Applicable in failure detection v2.  This reason always comes together with the `custom_rule_name` field. |
| `exception` | Verdict is caused by an exception. Applicable in failure detection v1 and v2. |
| `grpc_code` | Verdict is caused by the GRPC response code. Applicable in failure detection v2. |
| `http_code` | Verdict is caused by the HTTP response code. Applicable in failure detection v1 and v2. |
| `span_status` | Verdict is caused by the span status attribute. Applicable in failure detection v1 and v2. |

`verdict` MUST be one of the following:

| Value | Description |
| --- | --- |
| `failure` | Indicates that the rule failed. |
| `success` | Indicates that the rule was successful. |

## Функция как услуга (FaaS)

Поля, которые можно ожидать от бессерверных функций или функций как услуги (FaaS) на различных облачных платформах.
Существуют общие атрибуты и атрибуты, специфичные для входящих вызовов FaaS (на стороне сервера) и исходящих вызовов (функция FaaS как клиент, выполняющий вызовы).

### Общие атрибуты

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.account.id` | string | resource stable The 12-digit number, such as 123456789012, that uniquely identifies an AWS account. Tags: `permission` `primary-field` | `123456789012` |
| `aws.arn` | string | resource stable Amazon Resource Name (ARN). | `arn:aws:lambda:us-east-1:478983378254:function:acceptanceWeatherBackend` |
| `aws.region` | string | resource stable A specific geographical AWS Cloud location. Tags: `primary-field` | `us-east-1` |
| `azure.class_name` | string | resource experimental The fully qualified name of the class executing an Azure function. | `Host.Functions` |
| `azure.location` | string | resource stable A specific geographical location of Azure Cloud resource. Tags: `primary-field` | `westeurope` |
| `azure.resource.id` | string | resource experimental A unique, immutable identifier assigned to each Azure cloud resource. | `/subscriptions/27e9b03f-04d2-2b69-b327-32f433f7ed21/resourceGroups/demo-backend-rg/providers/Microsoft.ContainerService/managedClusters/demo-aks` |
| `azure.site_name` | string | resource experimental Globally unique deployment information about an Azure function. | `dt-function-scripted` |
| `azure.subscription` | string | resource stable An Azure subscription is a logical container used to provision resources in Azure. Tags: `permission` `primary-field` | `27e9b03f-04d2-2b69-b327-32f433f7ed21` |
| `cloud.account.id` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.account.id, azure.subscription, gcp.project.id, etc. | `111111111111`; `opentelemetry` |
| `cloud.platform` | string | resource deprecated Deprecated, no replacement available. [1](#fn-9-1-def) | `alibaba_cloud_ecs` |
| `cloud.provider` | string | resource stable Name of the cloud provider. | `alibaba_cloud` |
| `cloud.region` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.region, azure.location, gcp.region, etc. | `us-east-1` |
| `cloud.resource_id` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.arn, azure.resource.id, gcp.resource.name, etc. | `arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function`; `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID`; `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>` |
| `faas.max_memory` | long | resource experimental The amount of memory available to the serverless function in Bytes. |  |
| `faas.name` | string | resource experimental The name of the single function that this runtime instance executes. [2](#fn-9-2-def) | `my-function`; `myazurefunctionapp/some-function-name`; `test_function` |
| `faas.version` | string | resource experimental The immutable version of the function being executed. [3](#fn-9-3-def) | `14`; `254` |
| `gcp.project.id` | string | resource stable Identifier of the GCP project associated with this resource. Tags: `permission` `primary-field` | `dynatrace-gcp-extension` |
| `gcp.region` | string | resource stable A region is a specific geographical location where you can host your resources. Tags: `primary-field` | `europe-west3` |
| `gcp.resource.name` | string | resource stable The globally unique resource name in Google Cloud Platform convention. | `//cloudfunctions.googleapis.com/projects/gcp-example-project/locations/us-central1/functions/examplefunction` |

1

Префикс сервиса соответствует указанному в `cloud.provider`.

2

Это имя функции, настроенной/развёрнутой на платформе FaaS, и обычно оно отличается от имени функции обратного вызова
(которое может храниться в атрибутах спана `code.namespace`/`code.function`).

3

Значение поля зависит от облачного провайдера. Это поле не устанавливается для Azure.

### Входящие вызовы

В этом разделе описываются входящие вызовы FaaS, о которых сообщает сам экземпляр FaaS.
Для входящих спанов FaaS `span.kind` равен либо `server`, либо `consumer`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.request_id` | string | experimental The AWS request ID (e.g., value of `x-amzn-requestid`, `x-amzn-request-id`, or `x-amz-request-id` HTTP header, `awsRequestId` field in AWS lambda context object). | `0e7bc729-a468-57e8-8143-98f2eec5c925` |
| `aws.xray.trace_id` | string | experimental Contains the [AWS X-Rayï»¿](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) trace id (e.g., value of the `x-amzn-trace-id` HTTP header, `_X_AMZN_TRACE_ID` environment variable on AWS lambda) | `Root=1-63441c4a-abcdef012345678912345678`; `Self=1-63441c4a-12456789abcdef012345678;Root=1-67891233-abcdef012345678912345678` |
| `faas.coldstart` | boolean | experimental A boolean that is true if the serverless function is executed for the first time (aka cold-start). |  |
| `faas.document.collection` | string | experimental The table/collection name on which the operation above was executed. [1](#fn-10-1-def) | `my-coll-name` |
| `faas.document.name` | string | experimental The identifier for the specific item that changed after executing the operation above. [2](#fn-10-2-def) | `my-file.jpg`; `63eeb6e7d418cd98afb1c1d7` |
| `faas.document.operation` | string | experimental Relevant only for "datasource" trigger. The operation type which triggered the function invocation. | `delete` |
| `faas.document.time` | string | experimental The UTC ISO-8601 timestamp of the operation above. [3](#fn-10-3-def) | `2020-03-08T00:30:12.456Z` |
| `faas.event.__key__` | string | stable Faas event attribute, the `__key__` attribute in a Faas event represents the precise attribute name as received in the event. For example, it might be "faas.event.StackId" for the "StackId" attribute in an AWS CloudFormation event or "faas.event.IdentityPoolId" for the "IdentityPoolId" attribute in an AWS Cognito event. The value of this attribute is identical to the value received in the event. | `arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2b3c4d-5678-90ab-cdef-EXAMPLE11111`; `eu-west-1:12345678-1234-1234-1234-123456789012` |
| `faas.event_name` | string | experimental The API action that triggered the faas event. [4](#fn-10-4-def) | `ObjectCreated:Put (aws:s3)`; `INSERT (aws:dynamodb)` |
| `faas.event_source` | string | experimental The cloud service that originated the event. | `aws:cloudwatch`; `aws:cloudformation` |
| `faas.trigger` | string | experimental Type of the trigger which caused this function invocation. | `datasource` |

1

Применимо только для триггера `faas.trigger=datasource`

2

Применимо только для триггера `faas.trigger=datasource`

3

Применимо только для триггера `faas.trigger=datasource`

4

Значение этого атрибута специфично для сервиса, сгенерировавшего событие.

### Исходящие вызовы

В этом разделе описываются исходящие вызовы FaaS, о которых сообщает клиент, вызывающий экземпляр FaaS.
Для исходящих спанов FaaS `span.kind` равен либо `client`, либо `producer`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.request_id` | string | experimental The AWS request ID (e.g., value of `x-amzn-requestid`, `x-amzn-request-id`, or `x-amz-request-id` HTTP header, `awsRequestId` field in AWS lambda context object). | `0e7bc729-a468-57e8-8143-98f2eec5c925` |
| `aws.xray.trace_id` | string | experimental Contains the [AWS X-Rayï»¿](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) trace id (e.g., value of the `x-amzn-trace-id` HTTP header, `_X_AMZN_TRACE_ID` environment variable on AWS lambda) | `Root=1-63441c4a-abcdef012345678912345678`; `Self=1-63441c4a-12456789abcdef012345678;Root=1-67891233-abcdef012345678912345678` |
| `faas.invoked_name` | string | experimental The name of the invoked function. | `my-function` |
| `faas.invoked_provider` | string | experimental The cloud provider of the invoked function. Will be equal to the invoked function's `cloud.provider` resource attribute. | `alibaba_cloud` |
| `faas.invoked_region` | string | experimental The cloud region of the invoked function. [1](#fn-11-1-def) | `eu-central-1` |

1

Будет равно атрибуту ресурса `cloud.region` вызываемой функции.

## Спаны генеративного ИИ (GenAI)

Семантические соглашения для спанов, связанных с приложениями GenAI.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `gen_ai.embeddings.dimension.count` | long | experimental The number of dimensions the resulting output embeddings should have. | `512`; `1024` |
| `gen_ai.guardrail.id` | string | experimental Identifier of the guardrail that has been activated for the request. | `sensitive_data_guardrail` |
| `gen_ai.guardrail.input.latency` | long | experimental Processing time of prompt by guardrail in ms. | `123` |
| `gen_ai.guardrail.input.sensitive_information.patterns` | string[] | experimental Name of the patterns for sensitive information in prompt that triggered the Guardrail. | `['customer_identifier']` |
| `gen_ai.guardrail.input.sensitive_information.piis` | string[] | experimental Personal Identifiable Information categories in prompt that triggered the Guardrail. | `['ADDRESS', 'LICENSE_PLATE', 'DRIVER_ID']` |
| `gen_ai.guardrail.input.topic.names` | string[] | experimental Topics in prompt that triggered the Guardrail. | `['investment_advice', 'legal_advice', 'politics']` |
| `gen_ai.guardrail.input.words.lists` | string[] | experimental Word lists that triggered the guardrail for prompt. | `['custom-word-list']` |
| `gen_ai.guardrail.input.words.matches` | string[] | experimental Words in prompt that triggered the Guardrail. | `[]` |
| `gen_ai.guardrail.output.latency` | long | experimental Processing time of response by guardrail in ms. | `123` |
| `gen_ai.guardrail.output.sensitive_information.patterns` | string[] | experimental Name of the patterns for sensitive information in response that triggered the Guardrail. | `['customer_identifier']` |
| `gen_ai.guardrail.output.sensitive_information.piis` | string[] | experimental Personal Identifiable Information categories in response that triggered the Guardrail. | `['ADDRESS', 'LICENSE_PLATE', 'DRIVER_ID']` |
| `gen_ai.guardrail.output.topic.names` | string[] | experimental Topics in response that triggered the Guardrail. | `['investment_advice', 'legal_advice', 'politics']` |
| `gen_ai.guardrail.output.words.lists` | string[] | experimental Word lists that triggered the guardrail for response. | `['custom-word-list']` |
| `gen_ai.guardrail.output.words.matches` | string[] | experimental Words in response that triggered the Guardrail. | `[]` |
| `gen_ai.guardrail.version` | string | experimental Version of the guardrail that has been activated. | `DRAFT`; `5`; `12345678` |
| `gen_ai.operation.kind` | string | experimental AI framework operation being performed. | `workflow`; `task`; `agent`; `agent`; `tool`; `retrieval` |
| `gen_ai.operation.name` | string | experimental Name of operation being performed. | `chat`; `generate_content`; `text_completion` |
| `gen_ai.prompt_caching` | string | experimental Indicates how prompt cache has been used when handling the request. | `read`; `write` |
| `gen_ai.provider.name` | string | experimental Name of GenAI product being used. | `aws_bedrock`; `openai` |
| `gen_ai.request.encoding_formats` | string[] | experimental The encoding formats requested in an embeddings operation, if specified. | `['base64']`; `['float', 'binary']` |
| `gen_ai.request.frequency_penalty` | double | experimental Frequency penalty setting for GenAI request. | `0.4` |
| `gen_ai.request.max_tokens` | long | experimental Maximum number of tokens that the model can generate for a request. | `50` |
| `gen_ai.request.model` | string | experimental Model chosen to handle the request. | `amazon.nova-micro-v1:0`; `anthropic.claude-3-7-sonnet-20250219-v1:0` |
| `gen_ai.request.presence_penalty` | double | experimental Presence penalty setting for GenAI request. | `0.4` |
| `gen_ai.request.stop_sequences` | string[] | experimental List of sequences that will stop the model from generating further tokens. | `['forest', 'lived']` |
| `gen_ai.request.temperature` | double | experimental Temperature setting for GenAI request. | `0.8` |
| `gen_ai.request.top_k` | long | experimental Temperature setting for GenAI request. | `300` |
| `gen_ai.request.top_p` | double | experimental Temperature setting for GenAI request. | `0.6` |
| `gen_ai.response.finish_reasons` | string[] | experimental List of reasons why the model stopped generating tokens, corresponding to each generation received. | `['stop_sequence']`; `['stop_sequence', 'max_tokens']` |
| `gen_ai.response.id` | string | experimental Unique identifier of an LLM response. | `resp_0e7d0475962f0d2800691dd8cbf8108190b45198f77fa12d6e` |
| `gen_ai.response.model` | string | experimental Model that handled the request. | `amazon.nova-micro-v1:0`; `anthropic.claude-3-7-sonnet-20250219-v1:0` |
| `gen_ai.response.system_fingerprint` | string | experimental Identifier of system used to generate LLM response. | `fp_03e44fcc34` |
| `gen_ai.usage.input_tokens` | long | experimental Number of tokens sent to the model in the request. | `42` |
| `gen_ai.usage.output_tokens` | long | experimental Number of tokens generated by the model while handling the request. | `42` |
| `gen_ai.usage.prompt_caching.read_tokens` | long | experimental Number of tokens that has been read from cache. | `42` |
| `gen_ai.usage.prompt_caching.write_tokens` | long | experimental Number of tokens used to generate cache checkpoint. | `42` |

`gen_ai.operation.kind` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `agent` | Operation invoking an autonomous component that can make decisions or perform actions. |
| `retrieval` | Operation collecting documents for a RAG pipeline. |
| `task` | A specific operation or step within a workflow. |
| `tool` | Operation invoking a utility or function used within the application. |
| `workflow` | A high-level process or chain of operations. |

`gen_ai.operation.name` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `chat` | Operation of engaging in a conversational exchange with LLM. |
| `embeddings` | Operation of creating embeddings from user input. |
| `text_completion` | Operation of completing text based on user input by LLM. |

`gen_ai.prompt_caching` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `read` | Cache hit. Reading from cache. |
| `write` | Cache miss. Creating cache checkpoint. |

`gen_ai.provider.name` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `aws_bedrock` | Amazon Bedrock |
| `openai` | OpenAI |

## Спаны HTTP

Семантические соглашения для спанов клиента и сервера HTTP.
Они могут использоваться для схем HTTP и HTTPS и различных версий HTTP, таких как 1.1, 2 и SPDY.

### Общие поля

Общие поля, перечисленные в этом разделе, применяются как к клиентам, так и к серверам HTTP, в дополнение к специфическим полям, перечисленным в разделах [HTTP client](#http-client) и [HTTP server](#http-server) ниже.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `http.request.body.size` | long | stable The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Lengthï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size. | `3495` |
| `http.request.header.__key__` | string | stable HTTP request headers, `__key__` being the lowercase HTTP header name, for example, "http.request.header.accept-encoding". The value is a string. If multiple headers have the same name or multiple header values, the values will be comma-separated into a single string. Tags: `sensitive-spans` | `https://www.foo.bar/`; `gzip, deflate, br`; `1.2.3.4, 1.2.3.5` |
| `http.request.method` | string | stable HTTP request method. | `GET`; `POST`; `HEAD` |
| `http.response.body.size` | long | stable The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Lengthï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size. | `3495` |
| `http.response.header.__key__` | string | stable HTTP response headers, `__key__` being the lowercase HTTP header name, for example, "http.response.header.content-type". The value is a string. If multiple headers have the same name or multiple header values, the values will be comma-separated into a single string. | `909`; `text/html; charset=utf-8`; `abc, def` |
| `http.response.status_code` | long | stable [HTTP response status codeï»¿](https://tools.ietf.org/html/rfc7231#section-6). | `200` |
| `network.protocol.name` | string | stable [OSI Application Layerï»¿](https://osi-model.com/application-layer/) or non-OSI equivalent. | `amqp`; `http`; `mqtt` |
| `network.protocol.version` | string | experimental Version of the application layer protocol used. | `1.1`; `3.1.1` |

### HTTP-клиент

Этот тип спана представляет исходящий HTTP-запрос.

Для спана HTTP-клиента `span.kind` равен `client`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `server.address` | string | stable Host identifier of the ["URI origin"ï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to. | `example.com` |
| `server.port` | long | stable Port identifier of the ["URI origin"ï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |
| `url.fragment` | string | stable The URI fragment component. | `SemConv` |
| `url.full` | string | stable Absolute URL describing a network resource according to RFC3986. Tags: `sensitive-spans` | `https://www.foo.bar/docs/search?q=OpenTelemetry#SemConv` |
| `url.path` | string | stable The URI path component. | `/docs/search` |
| `url.query` | string | stable The URI query component. Tags: `sensitive-spans` | `q=OpenTelemetry` |
| `url.scheme` | string | stable The URI scheme component identifying the used protocol. | `https`; `ftp`; `telnet` |

### HTTP-сервер

Этот тип спана представляет входящий HTTP-запрос.

Для спана HTTP-сервера `span.kind` ДОЛЖЕН быть `server`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `client.ip` | ipAddress | experimental IP address of the original client (IPv4 or IPv6) making the request. This request might have passed several proxies or load balancers. The client IP is the result of resolving the socket connection, X-Forward-For, and other headers. Tags: `sensitive-spans` `sensitive-user-events` | `194.232.104.141`; `2a01:468:1000:9::140` |
| `http.route` | string | stable The matched route (path template in the format used by the respective server framework). | `/users/:userID?`; `Home/Index/{id?}` |
| `server.address` | string | stable Name of the local HTTP server that received the request. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `url.path` | string | stable The URI path component. | `/docs/search` |
| `url.query` | string | stable The URI query component. Tags: `sensitive-spans` | `q=OpenTelemetry` |
| `url.scheme` | string | stable The URI scheme component identifying the used protocol. | `https`; `ftp`; `telnet` |

## Спаны обмена сообщениями

### Общие атрибуты

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.batch.failed_count` | long | experimental The number of messages in the batch for which publishing failed. | `1`; `3`; `15` |
| `messaging.batch.failure_codes` | string[] | experimental The vendor-provided error codes explaining why an operation on the message broker failed. To limit attribute size, not all error codes might be included. | `['MalformedDetail', 'InvalidArgument']` |
| `messaging.batch.message_count` | long | stable The number of messages sent, received, or processed in the scope of the batching operation. | `1`; `2`; `3` |
| `messaging.client.id` | string | stable A unique identifier for the client that consumes or produces a message. | `aclient`; `myhost@68d46b89c9-c29qc` |
| `messaging.is_failed` | boolean | experimental Indicates that the messaging operation is considered failed according to the failure detection rules. Only present if the `messaging.operation.type` is `process`. |  |
| `messaging.message.body.size` | long | stable The (uncompressed) size of the message payload in bytes. | `2738` |
| `messaging.message.conversation_id` | string | stable The conversation ID identifying the conversation to which the message belongs, represented as a string. Sometimes called "Correlation ID". | `MyConversationId` |
| `messaging.message.header.__key__` | record | stable The message headers, `__key__` being the message header/attribute name, for example, "messaging.message.header.ExtendedPayloadSize". The data type of the value depends on the attribute. | `1024, "my-eu-bucket-3", ["a", "b"]` |
| `messaging.message.id` | string | stable A value used by the messaging system as an identifier for the message, represented as a string. | `452a7c7c7c7048c2f887f61572b18fc2` |
| `messaging.operation.type` | string | stable A string identifying the kind of messaging operation. | `peek` |
| `messaging.system` | string | stable An identifier for the messaging system. See below for a list of well-known identifiers. | `kafka`; `rabbitmq` |
| `network.protocol.name` | string | stable [OSI Application Layerï»¿](https://osi-model.com/application-layer/) or non-OSI equivalent. | `amqp`; `http`; `mqtt` |
| `network.transport` | string | stable [OSI Transport Layerï»¿](https://osi-model.com/transport-layer/) or [Inter-process Communication methodï»¿](https://en.wikipedia.org/wiki/Inter-process_communication) [1](#fn-12-1-def) | `inproc` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. [2](#fn-12-2-def) | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |

1

Необходимо только когда атрибуты `server.*` не применяются.

2

Это должен быть IP-адрес/имя хоста брокера (или другого однорангового узла сетевого уровня), которому отправляется/от которого получается это конкретное сообщение.

`messaging.operation.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `peek` | A message is received from a destination by a message consumer/server, but left there (`span.kind` is "consumer"). |
| `process` | A message previously received from a destination is processed by a message consumer (`span.kind` is "consumer"). |
| `publish` | A message is sent to a destination by a message producer (`span.kind` is "producer"). |
| `receive` | A message is received from a destination by a message consumer (`span.kind` is "consumer"). |

`messaging.system` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `activemq` | ActiveMQ |
| `artemis` | ActiveMQ Artemis |
| `aws_eventbridge` | Amazon EventBridge |
| `aws_sns` | Amazon Simple Notification Service (SNS) |
| `aws_sqs` | Amazon Simple Queue Service (SQS) |
| `azure_eventgrid` | Azure Event Grid |
| `azure_eventhubs` | Azure Event Hubs |
| `azure_servicebus` | Azure Service Bus |
| `gcp_pubsub` | Google Cloud Pub/Sub |
| `hornetq` | HornetQ |
| `jms` | Java Message Service |
| `kafka` | Apache Kafka |
| `mqseries` | IBM MQ |
| `msmq` | MSMQ |
| `rabbitmq` | RabbitMQ |
| `rocketmq` | Apache RocketMQ |
| `sag_webmethods_is` | Software AG, webMethods Integration Server |
| `tibco_ems` | Tibco EMS |
| `weblogic` | Oracle WebLogic |
| `websphere` | IBM WebSphere Application Server |

`network.transport` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `inproc` | In-process communication. [1](#fn-13-1-def) |
| `other` | Something else (non-IP-based). |
| `pipe` | Named or anonymous pipe. |
| `tcp` | TCP |
| `udp` | UDP |
| `unix` | Unix domain socket. |

1

Указывает на то, что используется только внутрипроцессное взаимодействие без «реального» сетевого протокола в случаях, когда сетевые атрибуты обычно ожидаются. Как правило, все остальные сетевые атрибуты можно опустить.

### Назначение сообщений

Назначение представляет собой компонент в системе обмена сообщениями, куда отправляются и откуда потребляются сообщения. Назначение обычно однозначно идентифицируется его именем в экземпляре системы обмена сообщениями. Примерами имени назначения могут быть URL или любой другой идентификатор конкретной очереди, темы или другой сущности в брокере.
Для спанов производителя и потребителя сообщений будут определены следующие атрибуты назначения:

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.destination.manager_name` | string | stable The destination's manager name [1](#fn-14-1-def) | `MyBroker` |
| `messaging.destination.name` | string | stable The message destination name [2](#fn-14-2-def) | `MyQueue`; `MyTopic` |
| `messaging.destination.temporary` | boolean | stable A boolean that is true if the message destination is temporary and might not exist anymore after messages are processed. |  |

1

Имя менеджера однозначно идентифицирует брокер.

2

Имя назначения однозначно идентифицирует конкретную очередь, тему или другую сущность в брокере.

### Обмен сообщениями Akka

#### Производитель Akka

Сторона отправителя через `ActorRef.tell()` или `ActorSelection.tell()` представлена спаном с `span.kind`, установленным в `producer`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.akka.actor.path` | string | experimental Path to actor inside actor system. | `/system/log1-Logging$DefaultLogger`; `/remote/akka.tcp/RequesterSystem@localhost:52133/user/requestActor/$a` |
| `messaging.akka.actor.system` | string | experimental Name of the actor system. | `RequesterSystem`; `ResponseSystem` |
| `messaging.akka.message.type` | string | experimental Fully qualified type name of the message. | `java.lang.String`; `akka.event.Logging$Info2`; `com.acme.twosuds.ResponseActor$RequestMessage` |
| `messaging.message.body.size` | long | stable The (uncompressed) size of the message payload in bytes. | `2738` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |

#### Потребитель Akka

Сторона получателя через `ActorCell.invoke()` (`inproc`) или `Actor.receive()` (`tcp`) представлена спаном с `span.kind`, установленным в `consumer`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.akka.actor.kind` | string | experimental Name of the top-level actor. See [The Akka actor hierarchyï»¿](https://doc.akka.io/docs/akka/2.5/guide/tutorial_1.html#the-akka-actor-hierarchy) [1](#fn-15-1-def) | `system`; `user` |
| `messaging.akka.actor.path` | string | experimental Path to actor inside actor system. [2](#fn-15-2-def) | `/system/log1-Logging$DefaultLogger`; `/remote/akka.tcp/RequesterSystem@localhost:52133/user/requestActor/$a` |
| `messaging.akka.actor.system` | string | experimental Name of the actor system. [3](#fn-15-3-def) | `RequesterSystem`; `ResponseSystem` |
| `messaging.akka.actor.type` | string | experimental Fully qualified type name of actor. [4](#fn-15-4-def) | `com.acme.RespondingActor` |
| `messaging.akka.message.type` | string | experimental Fully qualified type name of the message. | `java.lang.String`; `akka.event.Logging$Info2`; `com.acme.twosuds.ResponseActor$RequestMessage` |
| `messaging.message.body.size` | long | stable The (uncompressed) size of the message payload in bytes. | `2738` |
| `network.transport` | string | stable For Akka local, `network.transport` is set to `inproc`; for Akka remoting, it's set to `tcp`. | `inproc`; `tcp` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. [5](#fn-15-5-def) | `example.com` |
| `server.port` | long | stable Logical server port number. [6](#fn-15-6-def) | `65123`; `80` |

1

Недоступно при `network.transport` = `tcp`

2

Недоступно при `network.transport` = `inproc`

3

Недоступно при `network.transport` = `inproc`

4

Недоступно при `network.transport` = `tcp`

5

Недоступно при `network.transport` = `inproc`

6

Недоступно при `network.transport` = `inproc`

`network.transport` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `inproc` | In-process communication. [1](#fn-16-1-def) |
| `other` | Something else (non-IP-based). |
| `pipe` | Named or anonymous pipe. |
| `tcp` | TCP |
| `udp` | UDP |
| `unix` | Unix domain socket. |

1

Указывает на то, что используется только внутрипроцессное взаимодействие без «реального» сетевого протокола в случаях, когда сетевые атрибуты обычно ожидаются. Как правило, все остальные сетевые атрибуты можно опустить.

### Обмен сообщениями Kafka

Это соглашение расширяет семантическое соглашение по умолчанию для систем обмена сообщениями.

#### Производитель Kafka

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.destination.partition.id` | string | stable String representation of the partition ID the message is sent to or received from. | `1` |
| `messaging.kafka.message.key` | string | experimental The `key` property of the message. | `mykey` |
| `messaging.kafka.message.tombstone` | boolean | experimental A boolean that is true if the message is a tombstone. [1](#fn-17-1-def) | `true` |
| `messaging.kafka.offset` | long | experimental The offset of the message. | `42` |

1

Если сообщение является тумбстоуном, значение равно `true`. При отсутствии значение считается равным `false`.

#### Потребитель Kafka

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.consumer.group.name` | string | stable The name of the consumer group with which a consumer is associated. [1](#fn-18-1-def) | `my-group`; `indexer` |
| `messaging.destination.partition.id` | string | stable String representation of the partition ID the message is sent to or received from. | `1` |
| `messaging.kafka.message.key` | string | experimental The `key` property of the message. | `mykey` |
| `messaging.kafka.message.tombstone` | boolean | experimental A boolean that is true if the message is a tombstone. [2](#fn-18-2-def) | `true` |
| `messaging.kafka.offset` | long | experimental The offset of the message. | `42` |

1

Kafka [идентификатор группы потребителейï»¿](https://docs.confluent.io/platform/current/clients/consumer.html)

2

Если сообщение является тумбстоуном, значение равно `true`. При отсутствии значение считается равным `false`.

## Спаны RPC

Поля, описывающие удалённые вызовы процедур (также называемые «удалёнными вызовами методов» / «RMI») с помощью спанов.

Удалённый вызов процедуры описывается двумя отдельными спанами: одним на стороне клиента и одним на стороне сервера.

Для исходящих запросов `SpanKind` ДОЛЖЕН быть установлен в `client`, а для входящих — в `server`.

### Общие поля

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `network.protocol.name` | string | stable The protocol that is used in the remote procedure call or web service. It can be omitted if it matches with `rpc.system`. See below for a list of well-known identifiers. | `grpc`; `rest_http`; `soap`; `dotnet_remoting`; `hessian`; `java_rmi`; `json_rpc` |
| `rpc.method` | string | experimental The name of the (logical) method being called [1](#fn-19-1-def) | `exampleMethod` |
| `rpc.namespace` | string | experimental The namespace of the method being called. In SOAP, it would be the XML namespace. | `tempuri.org` |
| `rpc.service` | string | experimental The full (logical) name of the service being called, including its package name, if applicable. [2](#fn-19-2-def) | `myservice.EchoService` |
| `rpc.system` | string | experimental A string identifying the remoting system or framework. See below for a list of well-known identifiers. | `apache_cxf`; `dotnet_wcf`; `grpc`; `jax_ws` |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |

1

Это логическое имя метода с точки зрения интерфейса RPC, которое может отличаться от имени любого реализующего метода/функции. Атрибут `code.function` может использоваться для хранения последнего (например, метода, выполняющего вызов на стороне сервера, метода клиентской заглушки RPC на стороне клиента).

2

Это логическое имя сервиса с точки зрения интерфейса RPC, которое может отличаться от имени любого реализующего класса. Атрибут `code.namespace` может использоваться для хранения последнего (несмотря на название атрибута, он может включать имя класса, например класс с методом, фактически выполняющим вызов на стороне сервера, класс клиентской заглушки RPC на стороне клиента).

### RPC-сервер

Этот тип спана представляет входящий RPC-запрос.

Для спана RPC-сервера `SpanKind` равен `Server`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `code.function` | string | experimental The method or function name, or equivalent (usually the rightmost part of the code unit's name). Represents the name of the function that is represented by this span. [1](#fn-20-1-def) | `serveRequest` |
| `code.invoked.function` | string | experimental Like `code.function`, only it represents the function that was active when a span has been started. Typically, it's the function that has been instrumented. The spans duration does not reflect the duration of this function execution. It should only be set if it differs from `code.function`. | `invoke` |
| `code.invoked.namespace` | string | experimental Like `code.namespace`, only it represents the namespace of the function that was active when a span has been started. Typically, it's the function that has been instrumented. It should only be set if it differs from `code.namespace`. | `com.sun.xml.ws.server.InvokerTube$2` |
| `code.namespace` | string | experimental The namespace within which `code.function` is defined. Usually, the qualified class or module name, such that `code.namespace` + some separator + `code.function` forms a unique identifier for the code unit. [2](#fn-20-2-def) | `com.example.MyHttpService` |
| `network.transport` | string | stable [OSI Transport Layerï»¿](https://osi-model.com/transport-layer/) or [Inter-process Communication methodï»¿](https://en.wikipedia.org/wiki/Inter-process_communication) | `tcp`; `udp` |

1

В случае RPC `code.function` представляет функцию-обработчик, обрабатывающую RPC.

2

В случае RPC `code.namespace` представляет пространство имён функции-обработчика, обрабатывающей RPC.

### gRPC

Дополнительные соглашения для удалённых вызовов процедур через gRPC.

`rpc.framework` и `rpc.protocol` ДОЛЖНЫ быть установлены в `"grpc"`.

#### Атрибуты gRPC

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rpc.grpc.status_code` | long | experimental The [numeric status codeï»¿](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) of the gRPC request. |  |

[gRPCï»¿](https://grpc.io/)

### RMI

Дополнительные соглашения для удалённых вызовов процедур через RMI.

`rpc.framework` и `rpc.protocol` ДОЛЖНЫ быть установлены в `"java-rmi"`.

#### Поля RMI

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rpc.rmi.registry` | string | experimental The URL of a rmi endpoint. | `Calculator` |

[RMIï»¿](https://docs.oracle.com/javase/tutorial/rmi/)

## Спаны z/OS Connect EE

z/OS Connect EE (Enterprise Edition) — это продукт IBM, предоставляющий приложения и данные в подсистемах z/OS, таких как CICS, IMS или MQ, через RESTful API.
Реализация z/OS Connect EE (v3.0) построена на базе WebSphere Application Server для профиля z/OS Liberty.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ibm.cics.program` | string | resource experimental The name of the CICS program. [1](#fn-21-1-def) | `EDUCHAN` |
| `zosconnect.api.description` | string | experimental The z/OS Connect API description. | `The API for the CICS catalog manager sample application.` |
| `zosconnect.api.name` | string | experimental The z/OS Connect API name. | `catalog` |
| `zosconnect.api.version` | string | experimental The z/OS Connect API version. | `1.0.0` |
| `zosconnect.request.body.size` | long | experimental The size of the request payload in bytes. | `234` |
| `zosconnect.request.id` | long | experimental The z/OS Connect request ID. | `2215` |
| `zosconnect.request.type` | string | experimental The type of the REST request. [2](#fn-21-2-def) | `ADMIN` |
| `zosconnect.response.body.size` | long | experimental The size of the response payload in bytes. | `125` |
| `zosconnect.service.description` | string | experimental The z/OS Connect service description. | `EDUCHAN service using the CICS Service Provider` |
| `zosconnect.service.name` | string | experimental The z/OS Connect service name. | `placeOrder` |
| `zosconnect.service.provider.name` | string | experimental The service provider name. | `CICS-1.0` |
| `zosconnect.service.version` | string | experimental The z/OS Connect service version. | `2.0` |
| `zosconnect.sor.identifier` | string | experimental The system of record identifier. The format differs depending on the SOR type. [3](#fn-21-3-def) | `localhost:8080` |
| `zosconnect.sor.reference` | string | experimental The system of record reference. | `cicsConn` |
| `zosconnect.sor.resource` | string | experimental Identifier for the resource invoked on the system of record. The format differs depending on the SOR type. [4](#fn-21-4-def) | `01,DFH0XCMN` |
| `zosconnect.sor.type` | string | experimental The system of record type. | `CICS` |

1

Применимо только если zosconnect.sor.type равно CICS

2

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-datarequesttypeï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-datarequesttype)

3

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR\_IDENTIFIERï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR_IDENTIFIER)

4

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR\_RESOURCEï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR_RESOURCE)

`zosconnect.request.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ADMIN` | admin |
| `API` | api |
| `SERVICE` | service |
| `UNKNOWN` | unknown |

`zosconnect.sor.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CICS` | cics |
| `IMS` | ims |
| `MQ` | mq |
| `REST` | rest |
| `WOLA` | wola |

## Спаны z/OS

Семантические соглашения для спанов клиента и сервера z/OS. Они могут применяться для схем CICS и IMS.

### Общие атрибуты

Общие атрибуты, перечисленные в этом разделе, применяются как к клиентам, так и к серверам CICS и IMS, в дополнение к
специфическим атрибутам, перечисленным в разделах [CICS common](#cics-common), [CICS client](#cics-client) и [CICS server](#cics-server) ниже.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `zos.transaction.call_type` | string | experimental The type of transaction call that was invoked. | `CTG` |
| `zos.transaction.job_name` | string | resource experimental The jobname of the z/OS address space that the transaction executed in. | `CICSAOR0`; `CTGATM00`; `IMSCR15` |
| `zos.transaction.lpar_name` | string | resource experimental The name of the LPAR that the transaction executed on. | `S0W1`; `ABCD` |

### Общее для CICS

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.system_id` | string | resource experimental The system ID of the CICS region that this transaction executed on. | `C259`; `CICS` |
| `cics.transaction.task_id` | long | experimental The CICS task ID of this transaction. | `1234` |

### Клиент CICS

Этот тип спана представляет исходящий CICS-запрос.

Для спана клиента CICS `span.kind` равен `client`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.system_id` | string | resource experimental The system ID of the server CICS region that will contain the started server transaction. | `C259`; `CICS` |
| `zos.transaction.lpar_name` | string | resource experimental The LPAR name that hosts the CICS region that will contain the started server transaction. | `S0W1`; `ABCD` |

### Сервер CICS

Этот тип спана представляет входящий CICS-запрос.

Для спана сервера CICS `span.kind` ДОЛЖЕН быть `server`.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.system_id` | string | resource experimental The system ID of the client CICS region that triggered this transaction. | `C259`; `CICS` |
| `zos.transaction.lpar_name` | string | resource experimental The LPAR name that hosts the client CICS region. | `S0W1`; `ABCD` |