---
title: Detection and monitoring
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored
scraped: 2026-05-12T12:05:12.534695
---

# Detection and monitoring

# Detection and monitoring

* Explanation
* 4-min read
* Updated on Jul 26, 2024

Dynatrace provides you with insights into the database load, response times, and failure rates. Even connection acquisition times can be monitored. As Dynatrace is a full-stack solution, it also provides insights from the infrastructure perspective of your databasesâjust by deploying OneAgent on the database hosts. This adds a second view into health metrics like CPU or memory utilization and even network health. Even log files are included in the analysis.

With code-level database monitoring you can:

* See the impact of your database statements on the response times of your services.
* Find expensive database statements based on the service calls or user actions from which they originate.
* Find out which services talk to databases most frequently.
* See how much load is placed on your databases by individual services.
* Understand why some statements are slow.
* Be notified of increased SQL statement costs and execution.

Database calls and PurePathÂ® technology

The distributed trace of a database request shows a particular database statement executed by the application. Because the traces are captured within the application and not on the database itself, you will see database statements traces only if the application that makes them either sends distributed traces to the [OpenTelemetry trace ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") or is monitored via the OneAgent. If there are no distributed traces already started by the said application, you can define a custom service. See the **Method hotspots** page to choose a method that is called before the database request in the same thread.

Attributes used for detection are marked with an asterisk â± on the [database](/managed/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new "Analyze your database services with Dynatrace (new page).") overview page, under **Properties and tags**.

## How database activity is monitored

In monitoring databases, Dynatrace doesn't consider methods, but rather commits, queries, and modifications related to your database services. By monitoring such calls, Dynatrace is able to deliver automatic root-cause analysis for performance problems with your database services. For example, if your database queries or commits slow down, we'll notify you immediately. We'll even show you which services are impacted by the problem.

Database calls that are made through monitored Java, .NET, PHP and Node.js processes are monitored automatically as long as the interaction with the database relies on a [supported database framework](/managed/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks."), such as JDBC, ADO.NET, or PDO. When OneAgent is installed on the host that runs your application server, Dynatrace ensures that all database statements are logged, as long as deep monitoring is active for the calling processes and the database request is appended to an existing PurePathÂ® distributed trace. As soon as the first calls to your database are monitored, the **Databases** page is updated with the new database entry.

When monitoring database activity, Dynatrace shows you which database statements are executed most often and which statements take up the most time. You can also see which services execute the database statements. For example, Dynatrace knows automatically when a service begins sending too many database statements and pushes a database server beyond its capacity.

When a database-related problem is raised, for example due to a drop in response time, Dynatrace tells you if there is a correlation between the problem and any load increase on a related service, which may be the root cause of the problem.

## Enable monitoring

Dynatrace monitors a number of database technologies with your OneAgent deployment, as well as using ActiveGate extensions you can run from an ActiveGate connecting remotely to your database server.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

To learn how to enable monitoring for a specific database technology, select the required extension.

* [Cassandraï»¿](https://www.dynatrace.com/hub/detail/cassandra/?query=cassandra&filter=all)
* [Couchbaseï»¿](https://www.dynatrace.com/hub/detail/couchbase/?query=couch+base&filter=all)
* [CouchDBï»¿](https://www.dynatrace.com/hub/detail/couchdb/?query=couched&filter=all)
* [PostgreSQLï»¿](https://www.dynatrace.com/hub/detail/postgresdb-remote-monitoring/?query=PostgreSQL&filter=all)
* [Redisï»¿](https://www.dynatrace.com/hub/detail/redis/?query=redis&filter=all)
* [IBM DB2](/managed/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.")
* [Microsoft SQLï»¿](https://www.dynatrace.com/hub/detail/microsoft-sql-server-2/?query=microsoft+sql&filter=all)
* [MySQLï»¿](https://www.dynatrace.com/hub/detail/mysql/?query=mysql&filter=all)
* [SAP HANAï»¿](https://www.dynatrace.com/hub/detail/sap-hana-database-remote-monitoring/?query=sap+hana&filter=all)

If you can't install OneAgent on a database host itself, you can get visibility through our integrations with cloud providers (AWS and Azure) by using an ActiveGate extension or by reporting important metrics via a custom device that you set up.