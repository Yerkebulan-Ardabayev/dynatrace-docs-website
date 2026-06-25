---
title: Поддержка новых технологий
source: https://docs.dynatrace.com/managed/whats-new/technology
scraped: 2026-05-12T12:06:55.688530
---

# Поддержка новых технологий

# Поддержка новых технологий

* Справочник
* Published Jul 13, 2022

Ознакомьтесь с новыми технологиями, которые можно отслеживать с помощью Dynatrace, и узнайте, как начать работу. Здесь представлены операционные системы и кодовые модули OneAgent, мейнфрейм, бессерверные интеграции и расширения платформы.

Поддержка новых технологий может требовать активации через [функции OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.").

[Дорожную карту поддержки технологий](https://community.dynatrace.com/t5/Feedback-channel/Dynatrace-technology-support-roadmap/td-p/183451) можно найти в сообществе Dynatrace.

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Поддерживается основная версия 5**

  + Поддерживается основная версия 5, включая все её дополнительные версии: 5.1 и 5.2
  + Другие основные версии не поддерживаются: 6 и 7
* **Поддерживается дополнительная версия 5.1**

  + Поддерживается дополнительная версия 5.1, включая все её патч-версии: 5.1.1 и 5.1.2
  + Другие дополнительные версии не поддерживаются: 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Поддерживается патч-версия 5.1.1
  + Другие патч-версии не поддерживаются: 5.1.2 и 5.1.3
* **Поддерживается диапазон версий 5.1 — 5.3**

  + Поддерживаются дополнительные версии 5.1, 5.2 и 5.3, включая все их патч-версии: 5.1.1, 5.2.1 и 5.3.1
  + Другие дополнительные версии не поддерживаются: 5.0 и 5.4
* **Минимальная требуемая версия — 5+**

  + Поддерживаются все основные, дополнительные и патч-версии, начиная с версии 5: 5, 5.1, 5.1.1, 6

## 1.335 OneAgent

Развёртывание OneAgent начинается Apr 07, 2026

* Apache HTTP client 5.x (Java Mainframe module)
* Sanic 22.12+ (Python module)
* Falcon 4.0+ (Python module)
* Kombu 4.6.7+ (Python module)
* Bottle support 0.11+ (Python module)
* Azure SDK 3.9+ (Python module)
* Go 1.26 (Go module)
* GraphQL Yoga 5.7+ (Node.js module)
* Go toolchain with FIPS v1.25.5 (openssl-fips)
* NGINX 1.28.2 and 1.29.5 (NGINX module)
* Opentelemetry 2.9–2.26 (Java module)
* Opentelemetry agent 1.55–1.60 (Java module)

## 1.333 OneAgent

Развёртывание OneAgent начинается Mar 10, 2026

* Node.js 25 (Node.js module)
* GraphQL Yoga 5.7+ (Node.js module)
* NGINX 1.28.1(NGINX module)
* Vert.x HttpClient 3.6+, 4.x+ and 5.x+ (Java module)
* Vert.x WebClient 3.6+, 4.x+, and 5.x+ (Java module)
* Spring WebFlux 7 (Java module)
* Spring Integration 7 (Java module)
* Redisson 3+ (Java module)
* GraalVM 25 (Java Module)
* OpenAI 1.54.0+ (Python module)
* LangChain 1.0+ (Python module)
* Kombu 4.6.7+ (Python module)
* Amazon AWS Lambda SDK 1.18.0–1.52.0 (Go module)
* Amazon AWS SDK 1.39.1–1.41.1 (Go module)
* Confluent Golang 2.13 Client (Go module). OneAgent features: Go Kafka Consumer; Go Kafka Producer

## 1.331 OneAgent

Развёртывание OneAgent начинается Feb 10, 2026

* NGINX 1.29.4 (NGINX module)
* Go toolchain with FIPS v1.25.3 (openssl-fips)
* gRPC 1.78 (Go module)
* Undici HTTP client (Node.js module)
* Amazon SNS v1.15–1.38 for Go

## 1.329 OneAgent

Развёртывание OneAgent начинается Jan 7, 2026

* Node.js 24 (Node.js module)
* PHP 8.5 Zend Engine 4.5 (PHP module)
* NGINX v1.29.3 (NGINX module)
* gRPC v1.26+ (Python module)
* Pymongo v3.10+ (Python module)
* MySQLClient v2.0+ (Python module)
* HTTPX v0.20.0+ (Python module)
* Jedis Redis v6-7 (Java module)
* IBM z17
* z/OS 3.2 (OS module)
* IBM MQ 9.4 (MQ module)
* IBM CICS Transaction Server 6.3 (CICS module)

## 1.327 OneAgent

Развёртывание OneAgent начинается Nov 18, 2025

* NGINX v1.29.2
* Oracle Linux 10.0 (zRemote module)
* Rocky Linux 10.0 (zRemote module)
* Amazon AWS Lambda SDK v3.5.0+ (.NET Framework, .NET, and .NET Core)
* Amazon AWS SDK v1.13.0 - 1.39.0 (Go)
* Amazon DynamoDB v3.5.0+ (.NET Framework, .NET, and .NET Core)
* Amazon SNS v3.5.0+ (.NET Framework, .NET, and .NET Core)
* Confluent Golang 2.12 Client (Go module). OneAgent features: Go Kafka Consumer; Go Kafka Producer
* Jakarta EE 9 (Java z/OS module)

## 1.325 OneAgent

Развёртывание OneAgent начинается Oct 21, 2025

* Go v1.25 (Go module)
* Go toolchain with FIPS v1.24.6 (openssl-fips)
* NGINX v1.29.1
* Amazon Event Bridge v3.5.0+ (.NET Framework, .NET, and .NET Core)
* Amazon Kinesis v3.5.0+ (.NET Framework, .NET, and .NET Core)
* Python-Kafka v2.0.2+ (Python module)

## 1.323 OneAgent

Развёртывание OneAgent начинается Sep 23, 2025

* Go toolchain with FIPS v1.23.9 and 1.24.4 (openssl-fips)
* Amazon Kinesis v2 for Java
* Python-Kafka v1.4+ (Python module)
* SUSE Linux Enterprise Server 15.7 (OS module)
* Windows Desktop 11 24H2 (OS module)
* .NET OneAgent SDK V2
* WebSphere Liberty 24 (z/OS Java module)
* WebSphere Liberty 25 (z/OS Java module)
* RabbitMQ Client v4 and v5 (Java module)
* IBM Semeru 21 LTS (Java module)
* IBM IMS 15.6 (IMS Module)

## 1.321 OneAgent

Развёртывание OneAgent начинается Sep 10, 2025

* NGINX 1.29.0 (NGINX module)
* Amazon S3 v2 for Java
* Confluent Golang 2.11 Client (Go module). OneAgent features: Go Kafka Consumer; Go Kafka Producer
* RabbitMQ Client v7.x+ (.NET Framework)
* RabbitMQ Client v7.x+ (.NET and .NET Core)
* MassTransit v8.3.2+ (.NET framework)
* MassTransit v8.3.2+ (.NET and .NET Core)
* Red Hat Enterprise Linux 10.0 (zRemote Module)
* IBM Semeru 17 LTS (Java module)

## 1.319 OneAgent

Развёртывание OneAgent начинается Jul 29, 2025

* Amazon Event Bridge v1.11+ for Python
* Amazon SNS v1.11+ for Python
* Amazon Kinesis v2-3 for Node.js
* AWS SDK v1-2 for Java

## 1.317 OneAgent

Развёртывание OneAgent начинается Jul 1, 2025

* Amazon SQS 1.11+ for Python
* Amazon S3 1.11+ for Python
* Amazon Kinesis 1.11+ for Python
* Amazon DynamoDB 1.11+ for Python
* Amazon S3 v2-3 for Node.js
* Go 5.0 - 5.7 (PostgreSQL (jackc/pgx))
* Redis Cluster 3.1.6 to 6.2.0 (PHP Module)

## 1.315 OneAgent

Развёртывание OneAgent начинается Jun 3, 2025

* Go toolchain with FIPS 1.23.6 (openssl-fips)
* NGINX 1.28.0 (NGINX module)
* IBM AIX 7.3 TL3 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.")
* Redis-Py 3.4+ (Python module). OneAgent feature: Python Redis
* Confluent Golang 2.10 Client (Go module). OneAgent features: Go Kafka Consumer; Go Kafka Producer
* Amazon SNS v1-2 for Java. OneAgent feature: Java Amazon SNS
* Amazon AWS SDK v2-3 for Node.js
* Amazon AWS SDK v1.11+ for Python
* Amazon Event Bridge v2-3 for Node.js
* Amazon Event Bridge v1-2 for Java
* Amazon SNS v1-2 for Java
* Amazon DynamoDB v2-3 for Node.js
* Amazon DynamoDB v1 & v3 for Java

## 1.313 OneAgent

Развёртывание OneAgent начинается May 6, 2025

* NGINX 1.27.5 (NGINX module)
* NGINX Plus R34 (NGINX module)
* IBM App Connect Enterprise 13.0.2.0+ (ACE module)
* JBoss EAP (Application Server, Remoting, RMI-IIOP) v8 (Java module)
* Azure Linux 3
* Amazon SQS v2-3 for Node.js
* Amazon SNS v2-3 for Node.js
* Python-Oracledb 1.0.1+ (Python module). OneAgent feature: Python Oracledb
* AIOHTTP 3.0+ (Python module). OneAgent feature: Python Aiohttp

## 1.311 OneAgent

Развёртывание OneAgent начинается Apr 8, 2025

* Windows Desktop 11 23H2 (OS module)
* Go 1.24 (Go module)
* Confluent Golang 1.9 - 2.8 Client (Go module). OneAgent features: Go Kafka Consumer; Go Kafka Producer

## 1.309 OneAgent

Развёртывание OneAgent начинается Mar 11, 2025

* Windows Server 2025 (OS module)
* gRPC 1.69-1.73 (Go Module).
* MongoDB 1.3 - 1.13 (Go module). OneAgent feature: Go MongoDB
* Go toolchain with FIPS 1.22.9 (openssl-fips)
* NGINX 1.26.3 (NGINX module)
* NGINX 1.27.4 (NGINX module)
* Oracle HotSpot VM 24 (Java module)
* OpenJDK 24 (Java module)
* SAP JVM 24 (Java module)
* Amazon Corretto 24 (Java module)
* Azul Platform Core (Zulu) 24 (Java module)
* Bellsoft Liberica 24 (Java module)
* Eclipse Temurin (a.k.a. 'Adoptium') 24 (Java module)
* Cpython 3.8 - 3.13 (Python module).
* Flask 1.1.2+ (Python module). OneAgent feature: Python Celery
* Django 1.8+ (Python module). OneAgent feature: Python Django
* Tornado 6.0+ (Python module). OneAgent feature: Python Tornado
* FastAPI 0.44+ (Python module). OneAgent feature: Python FastAPI
* Starlette 0.12+ (Python module). OneAgent feature: Python Starlette
* Requests 2 (Python module). OneAgent feature: Python Requests
* urllib3 2.0+ (Python module). OneAgent feature: Python urllib3
* Celery 5.3+ (Python module). OneAgent feature: Python Celery
* SQL Alchemy 1.1+ (Python module). OneAgent feature: Python SQLAlchemy
* psycopg2 2.8.4+ (Python module). OneAgent feature: Python psycopg2
* Opentelemetry-python 1.1+ (Python Module)
* Python standard library: asyncio (Python module)
* Python standard library: concurrent.futures (Python module). OneAgent feature: Python concurrent.futures thread, Python concurrent.futures process
* Python standard library: threading (Python module). OneAgent feature: Python threading
* Python standard library: subprocess (Python module). OneAgent feature: Python subprocess
* Python standard library: queue (Python module). OneAgent feature: Python queue
* Alpine Linux (musl libc) on ARM64 for containers (Java, Node.js, Python, and Apache modules)

## 1.307 OneAgent

Развёртывание OneAgent начинается Feb 11, 2025

* Windows Server 2012 R2 (OS module)
* MassTransit.RabbitMQ library trace support for .NET (min v7.+)
* Alpine Linux (musl libc) on ARM64 for containers (NGINX module)
* Go toolchain with FIPS 1.22.7 (openssl-fips)
* PHP 8.4 (PHP module). [Начало работы](https://www.dynatrace.com/hub/detail/php/)

## 1.305 OneAgent

Развёртывание OneAgent начинается Jan 14, 2025

* .NET 9 (.NET module)
* Go toolchain with FIPS 1.21.13 (openssl-fips)
* Node.js 23 (Node.js module)
* NGINX 1.27.2 (NGINX module)
* NGINX Plus R33
* Red Hat Enterprise Linux 9.5 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Oracle Linux 9.5 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Rocky Linux 9.5 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")

## 1.303 OneAgent

Развёртывание OneAgent начинается Nov 5, 2024

* Go 1.23.2, 1.22.8 (Go module)
* Veritas File System detection (OS agent)

## 1.301 OneAgent

Развёртывание OneAgent начинается Nov 11, 2024

* Go 1.23 (Go Module)

## 1.299 OneAgent

Развёртывание OneAgent начинается Sep 9, 2024

* IBM CICS Transaction Server 6.2 (CICS module)
* Go toolchain with FIPS 1.21.10 - 1.21.11 (openssl-fips)
* Oracle HotSpot VM 23 (Java module)
* OpenJDK 23 (Java module)
* SAP JVM 23 (Java module)
* Amazon Corretto 23 (Java module)
* Azul Platform Core (Zulu) 23 (Java module)
* Bellsoft Liberica 23 (Java module)
* Eclipse Temurin (a.k.a. 'Adoptium') 23 (Java module)
* Kafka (IBM/sarama) 1.40+ (Go module)
* Kafka (Shopify/sarama) 1.18 - 1.39 (Go Module)
* SUSE Linux Enterprise Server 15.6 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.")
* Fedora 39, 40 (OS module)
* openSUSE 15.6 (OS module)
* Ubuntu 24.04 (OS module)

## 1.297 OneAgent

Развёртывание OneAgent начинается Aug 13, 2024

* Apache Tomcat access log enrichment (Java module). OneAgent feature: Java - Trace/span context enrichment for unstructured Apache Tomcat access logs
* Мониторинг логов для регионов IBM CICS и подсистем IBM IMS. [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")
* NGINX 1.26.1, 1.27 (NGINX module)

## 1.295 OneAgent

Развёртывание OneAgent начинается Jul 16, 2024

* GraalVM Native Image for Maven and Gradle projects (Java Native Image module). [Начало работы](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.")
* Go toolchain with FIPS (openssl-fips) modifications (Go module). OneAgent feature: Go FIPS
* RxJava 3 (Java module). OneAgent feature: Java RxJava v3+ tracing

## Kubernetes Operator 1.2.0

Выпущен Jun 24, 2024

* Полная поддержка наблюдаемости OpenShift на архитектуре s390x. [Начало работы с Full-Stack observability](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")

## 1.293 OneAgent

Развёртывание OneAgent начинается Jun 18, 2024

* IBM CICS outgoing HTTP (CICS module). OneAgent feature: CICS HTTP
* log4js (Node.js module)
* NGINX 1.25.5, 1.26.0 (NGINX module)
* NGINX Plus R32 (NGINX module)
* Software AG WebMethods Integration Server 10.7, 10.11, 10.15 (Java module)

## 1.291 OneAgent

Развёртывание OneAgent начинается May 21, 2024

* Azure Messaging Service Bus 7+ (.NET module)
* Bunyan 1+ log enrichment (Node.js module)

## 1.289 OneAgent

Развёртывание OneAgent начинается Apr 22, 2024

* Amazon SQS incoming messages (Java module). OneAgent feature: Java Amazon SQS
* Kafka Batch Listener (Java module). OneAgent feature: Java Spring Kafka Batch Listener
* NGINX 1.25.4 (NGINX module)
* redis-py (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.")

## 1.287 OneAgent

Развёртывание OneAgent начинается Mar 26, 2024

* Log analytics on Linux s390x (Log module). [Объявление](https://www.dynatrace.com/news/blog/enable-full-observability-for-linux-on-ibm-z-mainframe-now-with-logs/)
* W3C Trace Context propagation for KafkaJS headers (Node.js module). OneAgent feature: Send W3C Trace Context Kafka headers

## 1.285 OneAgent

Развёртывание OneAgent начинается Feb 27, 2024

* Alpine Linux (musl libc) for containers 3.18, 3.19
* WebSphere Liberty 22, 23 (z/OS Java module)

## 1.283 OneAgent

Развёртывание OneAgent начинается Jan 30, 2024

* MongoDB 1.3 - 1.13 (Go module). OneAgent feature: Go MongoDB
* OpenResty 25.3.1 (NGINX module)
* z/OS 3.1 (zDC module)

## 1.281 OneAgent

Развёртывание OneAgent начинается Jan 9, 2024

* NGINX Plus R31 (NGINX module)
* Node.js 21 (Node.js module)
* Node.js 14, 16, 18, 20, 21 on Linux s390x (Node.js module)
* OpenTelemetry 1.0.0 (PHP module)

## 1.279 OneAgent

Развёртывание OneAgent начинается Nov 20, 2023

* JMS 3.0 (Java module)
* Spring Webflux 6 (Java module)
* Spring WebFlux WebClient 6 (Java module)

## 1.277 OneAgent

Развёртывание OneAgent начинается Oct 31, 2023

* .NET 8 (.NET module)
* Azure Cosmos DB 3.18+ (.NET module). OneAgent feature: .NET Azure Cosmos DB
* IBM App Connect Enterprise CICSRequest node (ACE module)
* Jetty HTTP client 12 (Java module)
* Jedis Redi 5 (Java module)
* Go 1.21 (Go module)
* NGINX 1.25.2, 1.25.3 (NGINX module)
* Ubuntu 23.04 (OS module)

## 1.275 OneAgent

Развёртывание OneAgent начинается Oct 4, 2023

* Amazon SNS for .NET (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration#sqs-sns-out "Trace AWS Lambda functions using a .NET runtime")
* Amazon SQS for .NET (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration#sqs-sns-out "Trace AWS Lambda functions using a .NET runtime")
* OpenJDK 21 LTS (Java module)
* Rancher Kubernetes Engine 2 (OS module)

## 1.273 OneAgent

Развёртывание OneAgent начинается Sep 5, 2023

* .NET (GCP integration). [Начало работы](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")
* go-redis 7, 8, 9 (Go module). OneAgent feature: Go Redis (go-redis/redis)
* Java ForkJoin (Java module). OneAgent feature: Java/Scala ForkJoinPool
* JBoss LogManager 1.1+, 2, 3 (Java module)

## 1.271 OneAgent

Развёртывание OneAgent начинается Aug 7, 2023

* AlmaLinux 9.0, 9.1, 9.2 (OS module)
* Amazon SNS for Java (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Java API via OpenTelemetry interoperability.")
* Amazon SQS for Java (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Java API via OpenTelemetry interoperability.")
* Fedora 37, 38 (OS module)
* NGINX 1.25.0, 1.25.1 (NGINX module)
* NGINX Plus R30 (NGINX module)
* Node.js 20 (Node.js module)
* openSUSE 15.5 (OS module)
* OpenTelemetry agent 1.27, 1.28 (Java module)

## Расширения платформы

Выпущены в июле 2023 года на Dynatrace Hub

* Apache Cassandra (JMX data source). [Начало работы](https://www.dynatrace.com/hub/detail/cassandra/)
* HornetQ (JMX data source). [Начало работы](https://www.dynatrace.com/hub/detail/hornetq-1/)

## 1.267 OneAgent

Развёртывание OneAgent начинается Jun 7, 2023

* Akka HTTP server 10.2, 10.4, 10.5 (Java module)

## Расширения платформы

Выпущены в мае 2023 года на Dynatrace Hub

* .NET processes (WMI data source). [Начало работы](https://www.dynatrace.com/hub/detail/net/#get-started)
* Apache ActiveMQ Classic (JMX data source). [Начало работы](https://www.dynatrace.com/hub/detail/activemq/#get-started). OneAgent feature: Java Metric Extensions 2.0 (JMX)
* Apache Kafka (JMX data source). [Начало работы](https://www.dynatrace.com/hub/detail/net/#get-started). OneAgent feature: Java Metric Extensions 2.0 (JMX)
* IBM MQ. [Начало работы](https://www.dynatrace.com/hub/detail/ibm-mq-local/#get-started)
* TIBCO EMS. [Начало работы](https://www.dynatrace.com/hub/detail/tibco-ems-1/#get-started)

## 1.265 OneAgent

Развёртывание OneAgent начинается May 12, 2023

* CBL-Mariner 2 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* DataStax client for Apache Cassandra 4 (Java module)
* Fujitsu Interstage 13 (Java module)
* Jakarta RESTful Web Services 2.1+ (Java module). OneAgent feature: Java Servlet 5.0
* Lettuce 5.1.0 - 5.3, 6.0.3 - 6.1.6, 6.1.8 - 6.2 (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/redis/#get-started). OneAgent feature: Java Lettuce Redis client
* Netty, User action to distributed trace correlation (RUM JavaScript and Java module). OneAgent feature: Netty Real User Monitoring (RUM) to distributed trace correlation
* OpenTelemetry agent 1.24, 1.25 (Java module)
* Spring Data Redis 2.1+ (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/redis/#get-started). OneAgent feature: Java Lettuce Redis client
* NGINX 1.23.4, 1.24.0 (NGINX module)

## 1.263 OneAgent

Развёртывание OneAgent начинается Apr 17, 2023

* .NET 7 (.NET module)
* Amazon Corretto 20 (Java module)
* Azul Platform Core (Zulu) 20 (Java module)
* Bellsoft Liberica 20 (Java module)
* Eclipse Temurin (a.k.a. 'Adoptium') 20 (Java module)
* Flatcar Container Linux 3033 LTS (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Go 1.20 (Go module)
* IBM IMS terminal transactions (IMS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring#ims-terminal-transactions "Customize the Dynatrace CICS and IMS monitoring on z/OS."). OneAgent feature: z/OS IMS terminal transaction sensor
* log4net 2.0.6+ (.NET module). OneAgent feature: .NET - Trace/span context enrichment Framework log4net
* OpenJDK 20 (Java module)
* OpenTelemetry 1.11.1 - 1.14 (Go module)
* OpenTelemetry agent 1.23 (Java module)
* Oracle HotSpot VM 20 (Java module)
* SAP JVM 20 (Java module)

## 1.261 OneAgent

Развёртывание OneAgent начинается Mar 14, 2023

* Spring Web Services 4 (Java module). OneAgent feature: Java Servlet 5.0

## 1.259 OneAgent

Развёртывание OneAgent начинается Feb 20, 2023

* Apache Tomcat 10 (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/apache-tomcat/#get-started), OneAgent feature: Java Servlet 5.0
* Cassandra client (gocql/gocql) 1.0 - 1.3 (Go module). [Начало работы](https://www.dynatrace.com/hub/detail/cassandra/#get-started), OneAgent feature: Go CQL (gocql/gocql)
* IBM CICS file access methods VSAM and BDAM (IBM CICS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access "File access monitoring of CICS applications using the CICS module."), OneAgent feature: z/OS CICS file monitoring sensor
* IBM IMS [transaction-oriented BMPs](https://www.ibm.com/docs/en/ims/15.1.0?topic=bmps-batch-message-processing-transaction-oriented) (IBM IMS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims#bmp-tracing "Install the Dynatrace IMS module.")
* Jakarta Servlet 5, 6 (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/jakarta-servlet/#get-started), OneAgent feature: Java Servlet 5.0
* Jersey 3 (Java module). OneAgent feature: Java Servlet 5.0
* Jetty HTTP server 11 (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/eclipse-jetty/#get-started), OneAgent feature: Java Servlet 5.0
* NGINX 1.23.3 (NGINX module)
* RabbitMQ client (php-amqplib) 2.7+ (PHP module). [Начало работы](https://www.dynatrace.com/hub/detail/net-rabbitmq/#get-started), OneAgent feature: PHP RabbitMQ
* Undertow 2.3+ (Java module). OneAgent feature: Java Servlet 5.0
* WildFly 27 (Java module). OneAgent feature: Java Servlet 5.0

## 1.257 OneAgent

Развёртывание OneAgent начинается Jan 24, 2023

* Amazon SNS for Python (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#python-sqs-sns "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* Amazon SNS for Node.js (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#nodejs-sqs-sns "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* Apache HttpClient 5.2 (Java module).
* Google Cloud Run managed execution environment generation 1, 2 (Java module). [Начало работы](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun "Monitor Java application deployed on Google Cloud Run managed.")
* IBM App Connect Enterprise Callable nodes (IBM IIB/ACE module)
* IBM CICS Transaction Server JSON requests (IBM CICS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#web-services "Install the Dynatrace CICS module.")
* Node.js 19 (Node.js module)
* SUSE Linux Enterprise Server 15.4 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.")

## 1.255 OneAgent

Развёртывание OneAgent начинается Dec 12, 2022

* GraphQL 15+ (Node.js module). [Начало работы](https://www.dynatrace.com/hub/detail/graphql/#get-started)
* Microsoft SQL Server (denisenkom/go-mssqldb) 0.11.0-0.12.3 (Go module). [Начало работы](https://www.dynatrace.com/hub/detail/microsoft-sql-server-2/#get-started)
* Microsoft SQL Server (microsoft/go-mssqldb) 0.11.0-0.17.0 (Go module). [Начало работы](https://www.dynatrace.com/hub/detail/microsoft-sql-server-2/#get-started)

## 1.253 OneAgent

Развёртывание OneAgent начинается Nov 14, 2022

* Amazon SQS for Node.js (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* Amazon SQS for Python (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* PostgreSQL (jackc/pgx) 4.7 - 4.17 (Go module). [Начало работы](https://www.dynatrace.com/hub/detail/postgresql/#get-started)
* SQLite3 5.1+ (Node.js module)

## 1.251 OneAgent

Развёртывание OneAgent начинается Oct 14, 2022

* Akka Http client 10.0, 10.2 (Java module)
* Amazon Corretto 19 (Java module)
* Apache HttpCore 5.x (Java module)
* Azul Platform Core (Zulu) 19 (Java module)
* Bellsoft Liberica 19 (Java module)
* Eclipse Temurin (a.k.a. 'Adoptium') 19 (Java module)
* Go 1.16+ (GCP integration). [Начало работы](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")
* IBM z/OS Connect EE MQ service provider (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.")
* Jetty HTTP server 10 (Java module)
* Oracle HotSpot VM 19 (Java module)
* OpenJDK 19 (Java module)
* OpenTelemetry 0.0.12, 0.0.13, 0.0.14, 0.0.15 (PHP module)
* OpenTelemetry agent 1.17.x - 1.19.x (Java module)
* Node.js 16 (AWS Lambda integration)
* SAP JVM 19 (Java module)

## 1.249 OneAgent

Развёртывание OneAgent начинается Sep 15, 2022

* Amazon Linux 2022 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Go 1.19 (Go module). [Начало работы](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.")
* OpenTelemetry 1.8, 1.9 (Go module). [Начало работы](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.")
* Rocky Linux 9 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")

## 1.247 OneAgent

Развёртывание OneAgent начинается Aug 25, 2022

* Apache Camel 2.21+ (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/apache-camel/)
* IBM Semeru for z/OS 11 (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.")
* JMX 1.0+ (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.")
* Monolog 3.0 (PHP module)
* Python (GCP integration). [Начало работы](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Monitor Google Cloud Functions with OpenTelemetry for Python and Dynatrace.")
* Red Hat Fuse on OpenShift 7.0+ (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/red-hat-fuse/)
* Red Hat Fuse Standalone 7.0+ (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/red-hat-fuse/)

## 1.246 SaaS/Managed

Развёртывание начинается Jul 25, 2022 для SaaS и Aug 1, 2022 для Managed

* DynamoDB client SDK for Node.js (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#nodejs-instrumentation "Enable and use OpenTelemetry interoperability in AWS Lambda.")

## 1.245 SaaS

Развёртывание начинается Jul 6, 2022 для SaaS

* DynamoDB client SDK for .NET (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration#dynamo-db "Trace AWS Lambda functions using a .NET runtime")

## 1.245 OneAgent

Развёртывание OneAgent начинается Jul 19, 2022

* AlmaLinux 8.6+ (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Fedora 35, 36 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* IBM CICS Transaction Server 6.1 (CICS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics "Install the Dynatrace CICS module.")
* IBM Virtual I/O Server (AIX) 3.1 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#vios-installation "Learn how to download and install Dynatrace OneAgent on AIX.")
* Kong API Gateway (NGINX module). [Начало работы](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation#howto "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.")
* OpenTelemetry 0.0.10, 0.0.11 (PHP module)
* Python consumption plan (Azure integration). [Начало работы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")
* [RabbitMQ](https://www.npmjs.com/package/amqplib) client 0.9 (Node.js module). [Начало работы](https://www.dynatrace.com/hub/detail/net-rabbitmq/#get-started)

## 1.244 SaaS/Managed

Развёртывание начинается Jun 27, 2022 для SaaS и Jul 5, 2022 для Managed

* DynamoDB client SDK for Python (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#python-instrumentation "Enable and use OpenTelemetry interoperability in AWS Lambda.")

## 1.243 OneAgent

Развёртывание OneAgent начинается Jun 29, 2022

* Apache Log4j2 2.17.2 - 2.18 (Java module)
* JDBC 3, 4 (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#jdbc "Set up Java monitoring on z/OS using the Java module.")
* Node.js 18 (Node.js module)
* Node.js consumption plan (Azure integration). [Начало работы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")
* Microsoft OpenJDK 11 LTS, 17 LTS (Java module)
* [oracledb](https://www.npmjs.com/package/oracledb) 5 (Node.js module). [Начало работы](https://www.dynatrace.com/hub/detail/oracle-database/)
* Red Hat Enterprise Linux 9 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Ubuntu 22.04 LTS (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")

## 1.241 OneAgent

Развёртывание OneAgent начинается Jun 8, 2022

* .NET / .NET Core (AWS Lambda integration). [Начало работы](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Trace AWS Lambda functions using a .NET runtime")
* .NET / .NET Core consumption plan (Azure integration). [Начало работы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")
* Apache HttpClient 5.x (Java module)
* Azul Platform Core (Zulu) 18 (Java module)
* Bellsoft Liberica 18 (Java module)
* JMS 1.1 (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.")
* Node.js (GCP integration). [Начало работы](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")
* OpenJDK 18 (Java module)
* OpenTelemetry 0.0.9 (PHP module)
* Oracle HotSpot VM 18 (Java module)
* Rocky Linux 8 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* SAP JVM 18 (Java module)

## 1.239 OneAgent

Развёртывание OneAgent начинается Apr 27, 2022

* CentOS Stream 9 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* Go 18 (Go module)
* IBM AIX 7.3 TL0 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.")
* Kestrel (ASP.NET Core applications), Real User Monitoring (RUM JavaScript and .NET module).
* Ubuntu 21.10 (OS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")

## 1.237 OneAgent

Развёртывание OneAgent начинается Apr 1, 2022

* IBM App Connect Enterprise 12.0.3.0+ (ACE module)
* Apache HTTP Server 2.2, 2.4 on Linux ARM64 (Apache HTTP module)
* PHP 7.1, 7.2, 7.3, 7.4, 8.0, 8.1 on Linux ARM64 (PHP module). [Начало работы](https://www.dynatrace.com/hub/detail/php/)

## 1.235 OneAgent

Развёртывание OneAgent начинается Mar 7, 2022

* .NET / .NET Core 5.0, 6.0 on Linux ARM64 (.NET module). [Начало работы](https://www.dynatrace.com/hub/detail/net/)
* IBM App Connect Enterprise JavaCompute node (ACE module)
* IBM CICS terminal transactions (CICS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring#transaction-start-filters "Customize the Dynatrace CICS and IMS monitoring on z/OS.")
* IBM z/OS Connect EE IMS service provider (z/OS Java module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.")
* TIBCO ActiveMatrix BusinessWorks 6.6 - 6.8 (Java module)

## 1.233 OneAgent

Развёртывание OneAgent начинается Feb 7, 2022

* Go 17 (Go module)
* IBM IMS Fast Path (IMS module). [Начало работы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims "Install the Dynatrace IMS module.")
* Jedis Redis 4 (Java module)
* reactor-core 3 (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/reactor-core/)

## 1.231 OneAgent

Развёртывание OneAgent начинается Jan 10, 2022

* Apache Log4J2 2.7 - 2.12 (Java module)
* Logrus 1.7.1 - 1.9 (Go module)
* Zap 1.10 - 1.21 (Go module)
* Windows Server 2022 (OS module)

## 1.229 OneAgent

Развёртывание OneAgent начинается Nov 22, 2021

* Apache Kafka Streams API (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/apache-kafka/)
* Apache Log4J2 2.13.0, 2.13.1, 2.13.3, 2.14.x - 2.17.1 (Java module)
* Bellsoft Liberica 8 LTS, 11 LTS, 16, 17 LTS (Java module)
* Eclipse Temurin (a.k.a. 'Adoptium') 8 LTS, 11 LTS, 16, 17 LTS (Java module)
* IBM Semeru 8 LTS, 11 LTS, 16, 17 LTS (Java module)
* java.util.logging (Java module)
* Logback (QOS) 1 (Java module)
* OpenTelemetry 1.0 - 1.7 (Go module)
* Spring Cloud Stream (Java module). [Начало работы](https://www.dynatrace.com/hub/detail/apache-kafka/)