---
title: Поддержка новых технологий
source: https://www.dynatrace.com/docs/whats-new/technology
scraped: 2026-03-06T21:12:54.357617
---

# Поддержка новых технологий

# Поддержка новых технологий

* Последняя версия Dynatrace
* Справочник
* Опубликовано 13 июля 2022 г.

Откройте для себя новые технологии, которые можно отслеживать с помощью Dynatrace, и узнайте, как начать работу. Включены операционные системы и кодовые модули OneAgent, мейнфреймы, интеграции с serverless и расширения платформы.

Поддержка новых технологий может потребовать подключения через [функции OneAgent](../ingest-from/dynatrace-oneagent/oneagent-features.md "Управляйте функциями OneAgent глобально и для каждой группы процессов.").

[Дорожная карта поддержки технологий](https://community.dynatrace.com/t5/Feedback-channel/Dynatrace-technology-support-roadmap/td-p/183451) доступна в сообществе Dynatrace.

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Поддерживается основная версия 5**

  + Поддерживается основная версия 5, включая все её дополнительные версии, такие как 5.1 и 5.2
  + Другие основные версии не поддерживаются, такие как 6 и 7
* **Поддерживается дополнительная версия 5.1**

  + Поддерживается дополнительная версия 5.1, включая все её патч-версии, такие как 5.1.1 и 5.1.2
  + Другие дополнительные версии не поддерживаются, такие как 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Поддерживается патч-версия 5.1.1
  + Другие патч-версии не поддерживаются, такие как 5.1.2 и 5.1.3
* **Поддерживается диапазон версий 5.1–5.3**

  + Поддерживаются дополнительные версии 5.1, 5.2 и 5.3, включая все их патч-версии, такие как 5.1.1, 5.2.1 и 5.3.1
  + Другие дополнительные версии не поддерживаются, такие как 5.0 и 5.4
* **Требуемая минимальная версия 5+**

  + Поддерживаются все основные, дополнительные и патч-версии начиная с версии 5, такие как 5, 5.1, 5.1.1 и 6

## 1.331 OneAgent

Развёртывание начинается 10 февраля 2026 г. для OneAgent

* NGINX 1.29.4 (модуль NGINX)
* Go toolchain с FIPS v1.25.3 (openssl-fips)
* gRPC 1.78 (модуль Go)
* Undici HTTP client (модуль Node.js)
* Amazon SNS v1.15–1.38 для Go

## 1.329 OneAgent

Развёртывание начинается 7 января 2026 г. для OneAgent

* Node.js 24 (модуль Node.js)
* PHP 8.5 Zend Engine 4.5 (модуль PHP)
* NGINX v1.29.3 (модуль NGINX)
* gRPC v1.26+ (модуль Python)
* Pymongo v3.10+ (модуль Python)
* MySQLClient v2.0+ (модуль Python)
* HTTPX v0.20.0+ (модуль Python)
* Jedis Redis v6-7 (модуль Java)
* IBM z17
* z/OS 3.2 (модуль OS)
* IBM MQ 9.4 (модуль MQ)
* IBM CICS Transaction Server 6.3 (модуль CICS)

## 1.327 OneAgent

Развёртывание начинается 18 ноября 2025 г. для OneAgent

* NGINX v1.29.2
* Oracle Linux 10.0 (модуль zRemote)
* Rocky Linux 10.0 (модуль zRemote)
* Amazon AWS Lambda SDK v3.5.0+ (.NET Framework, .NET и .NET Core)
* Amazon AWS SDK v1.13.0–1.39.0 (Go)
* Amazon DynamoDB v3.5.0+ (.NET Framework, .NET и .NET Core)
* Amazon SNS v3.5.0+ (.NET Framework, .NET и .NET Core)
* Confluent Golang 2.12 Client (модуль Go). Функции OneAgent: Go Kafka Consumer; Go Kafka Producer
* Jakarta EE 9 (модуль Java z/OS)

## 1.325 OneAgent

Развёртывание начинается 21 октября 2025 г. для OneAgent

* Go v1.25 (модуль Go)
* Go toolchain с FIPS v1.24.6 (openssl-fips)
* NGINX v1.29.1
* Amazon Event Bridge v3.5.0+ (.NET Framework, .NET и .NET Core)
* Amazon Kinesis v3.5.0+ (.NET Framework, .NET и .NET Core)
* Python-Kafka v2.0.2+ (модуль Python)

## 1.323 OneAgent

Развёртывание начинается 23 сентября 2025 г. для OneAgent

* Go toolchain с FIPS v1.23.9 и 1.24.4 (openssl-fips)
* Amazon Kinesis v2 для Java
* Python-Kafka v1.4+ (модуль Python)
* SUSE Linux Enterprise Server 15.7 (модуль OS)
* Windows Desktop 11 24H2 (модуль OS)
* .NET OneAgent SDK V2
* WebSphere Liberty 24 (модуль Java z/OS)
* WebSphere Liberty 25 (модуль Java z/OS)
* RabbitMQ Client v4 и v5 (модуль Java)
* IBM Semeru 21 LTS (модуль Java)
* IBM IMS 15.6 (модуль IMS)

## 1.321 OneAgent

Развёртывание начинается 10 сентября 2025 г. для OneAgent

* NGINX 1.29.0 (модуль NGINX)
* Amazon S3 v2 для Java
* Confluent Golang 2.11 Client (модуль Go). Функции OneAgent: Go Kafka Consumer; Go Kafka Producer
* RabbitMQ Client v7.x+ (.NET Framework)
* RabbitMQ Client v7.x+ (.NET и .NET Core)
* MassTransit v8.3.2+ (.NET framework)
* MassTransit v8.3.2+ (.NET и .NET Core)
* Red Hat Enterprise Linux 10.0 (модуль zRemote)
* IBM Semeru 17 LTS (модуль Java)

## 1.319 OneAgent

Развёртывание начинается 29 июля 2025 г. для OneAgent

* Amazon Event Bridge v1.11+ для Python
* Amazon SNS v1.11+ для Python
* Amazon Kinesis v2-3 для Node.js
* AWS SDK v1-2 для Java

## 1.317 OneAgent

Развёртывание начинается 1 июля 2025 г. для OneAgent

* Amazon SQS 1.11+ для Python
* Amazon S3 1.11+ для Python
* Amazon Kinesis 1.11+ для Python
* Amazon DynamoDB 1.11+ для Python
* Amazon S3 v2-3 для Node.js
* Go 5.0–5.7 (PostgreSQL (jackc/pgx))
* Redis Cluster 3.1.6–6.2.0 (модуль PHP)

## 1.315 OneAgent

Развёртывание начинается 3 июня 2025 г. для OneAgent

* Go toolchain с FIPS 1.23.6 (openssl-fips)
* NGINX 1.28.0 (модуль NGINX)
* IBM AIX 7.3 TL3 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md "Узнайте, как установить OneAgent на AIX.")
* Redis-Py 3.4+ (модуль Python). Функция OneAgent: Python Redis
* Confluent Golang 2.10 Client (модуль Go). Функции OneAgent: Go Kafka Consumer; Go Kafka Producer
* Amazon SNS v1-2 для Java. Функция OneAgent: Java Amazon SNS
* Amazon AWS SDK v2-3 для Node.js
* Amazon AWS SDK v1.11+ для Python
* Amazon Event Bridge v2-3 для Node.js
* Amazon Event Bridge v1-2 для Java
* Amazon SNS v1-2 для Java
* Amazon DynamoDB v2-3 для Node.js
* Amazon DynamoDB v1 и v3 для Java

## 1.313 OneAgent

Развёртывание начинается 6 мая 2025 г. для OneAgent

* NGINX 1.27.5 (модуль NGINX)
* NGINX Plus R34 (модуль NGINX)
* IBM App Connect Enterprise 13.0.2.0+ (модуль ACE)
* JBoss EAP (Application Server, Remoting, RMI-IIOP) v8 (модуль Java)
* Azure Linux 3
* Amazon SQS v2-3 для Node.js
* Amazon SNS v2-3 для Node.js
* Python-Oracledb 1.0.1+ (модуль Python). Функция OneAgent: Python Oracledb
* AIOHTTP 3.0+ (модуль Python). Функция OneAgent: Python Aiohttp

## 1.311 OneAgent

Развёртывание начинается 8 апреля 2025 г. для OneAgent

* Windows Desktop 11 23H2 (модуль OS)
* Go 1.24 (модуль Go)
* Confluent Golang 1.9–2.8 Client (модуль Go). Функции OneAgent: Go Kafka Consumer; Go Kafka Producer

## 1.309 OneAgent

Развёртывание начинается 11 марта 2025 г. для OneAgent

* Windows Server 2025 (модуль OS)
* gRPC 1.69-1.73 (модуль Go)
* MongoDB 1.3–1.13 (модуль Go). Функция OneAgent: Go MongoDB
* Go toolchain с FIPS 1.22.9 (openssl-fips)
* NGINX 1.26.3 (модуль NGINX)
* NGINX 1.27.4 (модуль NGINX)
* Oracle HotSpot VM 24 (модуль Java)
* OpenJDK 24 (модуль Java)
* SAP JVM 24 (модуль Java)
* Amazon Corretto 24 (модуль Java)
* Azul Platform Core (Zulu) 24 (модуль Java)
* Bellsoft Liberica 24 (модуль Java)
* Eclipse Temurin (a.k.a. 'Adoptium') 24 (модуль Java)
* Cpython 3.8–3.13 (модуль Python)
* Flask 1.1.2+ (модуль Python). Функция OneAgent: Python Celery
* Django 1.8+ (модуль Python). Функция OneAgent: Python Django
* Tornado 6.0+ (модуль Python). Функция OneAgent: Python Tornado
* FastAPI 0.44+ (модуль Python). Функция OneAgent: Python FastAPI
* Starlette 0.12+ (модуль Python). Функция OneAgent: Python Starlette
* Requests 2 (модуль Python). Функция OneAgent: Python Requests
* urllib3 2.0+ (модуль Python). Функция OneAgent: Python urllib3
* Celery 5.3+ (модуль Python). Функция OneAgent: Python Celery
* SQL Alchemy 1.1+ (модуль Python). Функция OneAgent: Python SQLAlchemy
* psycopg2 2.8.4+ (модуль Python). Функция OneAgent: Python psycopg2
* Opentelemetry-python 1.1+ (модуль Python)
* Python standard library: asyncio (модуль Python)
* Python standard library: concurrent.futures (модуль Python). Функция OneAgent: Python concurrent.futures thread, Python concurrent.futures process
* Python standard library: threading (модуль Python). Функция OneAgent: Python threading
* Python standard library: subprocess (модуль Python). Функция OneAgent: Python subprocess
* Python standard library: queue (модуль Python). Функция OneAgent: Python queue
* Alpine Linux (musl libc) на ARM64 для контейнеров (модули Java, Node.js, Python и Apache)

## 1.307 OneAgent

Развёртывание начинается 11 февраля 2025 г. для OneAgent

* Windows Server 2012 R2 (модуль OS)
* Поддержка трассировки MassTransit.RabbitMQ для .NET (min v7.+)
* Alpine Linux (musl libc) для контейнеров 3.18, 3.19 (модуль NGINX)
* Go toolchain с FIPS 1.22.7 (openssl-fips)
* PHP 8.4 (модуль PHP). [Начало работы](https://www.dynatrace.com/hub/detail/php/)

## 1.305 OneAgent

Развёртывание начинается 14 января 2025 г. для OneAgent

* .NET 9 (модуль .NET)
* Go toolchain с FIPS 1.21.13 (openssl-fips)
* Node.js 23 (модуль Node.js)
* NGINX 1.27.2 (модуль NGINX)
* NGINX Plus R33
* Red Hat Enterprise Linux 9.5 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Oracle Linux 9.5 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Rocky Linux 9.5 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")

## 1.303 OneAgent

Развёртывание начинается 5 ноября 2024 г. для OneAgent

* Go 1.23.2, 1.22.8 (модуль Go)
* Обнаружение файловой системы Veritas (агент OS)

## 1.301 OneAgent

Развёртывание начинается 4 ноября 2024 г. для OneAgent

* Go 1.23 (модуль Go)

## 1.299 OneAgent

Развёртывание начинается 9 сентября 2024 г. для OneAgent

* IBM CICS Transaction Server 6.2 (модуль CICS)
* Go toolchain с FIPS 1.21.10–1.21.11 (openssl-fips)
* Oracle HotSpot VM 23 (модуль Java)
* OpenJDK 23 (модуль Java)
* SAP JVM 23 (модуль Java)
* Amazon Corretto 23 (модуль Java)
* Azul Platform Core (Zulu) 23 (модуль Java)
* Bellsoft Liberica 23 (модуль Java)
* Eclipse Temurin (a.k.a. 'Adoptium') 23 (модуль Java)
* Kafka (IBM/sarama) 1.40+ (модуль Go)
* Kafka (Shopify/sarama) 1.18–1.39 (модуль Go)
* SUSE Linux Enterprise Server 15.6 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux.md "Узнайте, как загрузить и установить Dynatrace OneAgent на Linux.")
* Fedora 39, 40 (модуль OS)
* openSUSE 15.6 (модуль OS)
* Ubuntu 24.04 (модуль OS)

## 1.297 OneAgent

Развёртывание начинается 13 августа 2024 г. для OneAgent

* Обогащение журналов доступа Apache Tomcat (модуль Java). Функция OneAgent: Java - Обогащение контекстом трассировки/спана для неструктурированных журналов доступа Apache Tomcat
* Мониторинг журналов для регионов IBM CICS и подсистем IBM IMS. [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs.md "Мониторинг журналов z/OS с помощью Dynatrace.")
* NGINX 1.26.1, 1.27 (модуль NGINX)

## 1.295 OneAgent

Развёртывание начинается 16 июля 2024 г. для OneAgent

* GraalVM Native Image для проектов Maven и Gradle (модуль Java Native Image). [Начало работы](../ingest-from/technology-support/application-software/java/graalvm-native-image.md "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.")
* Go toolchain с FIPS (openssl-fips) (модуль Go). Функция OneAgent: Go FIPS
* RxJava 3 (модуль Java). Функция OneAgent: Java RxJava v3+ tracing

## Kubernetes Operator 1.2.0

Выпущено 24 июня 2024 г.

* Полная поддержка наблюдаемости OpenShift на архитектуре s390x. [Начало работы с Full-Stack observability](../ingest-from/setup-on-k8s/deployment.md "Развёртывание Dynatrace Operator на Kubernetes")

## 1.293 OneAgent

Развёртывание начинается 18 июня 2024 г. для OneAgent

* IBM CICS outgoing HTTP (модуль CICS). Функция OneAgent: CICS HTTP
* log4js (модуль Node.js)
* NGINX 1.25.5, 1.26.0 (модуль NGINX)
* NGINX Plus R32 (модуль NGINX)
* Software AG WebMethods Integration Server 10.7, 10.11, 10.15 (модуль Java)

## 1.291 OneAgent

Развёртывание начинается 21 мая 2024 г. для OneAgent

* Azure Messaging Service Bus 7+ (модуль .NET)
* Bunyan 1+ log enrichment (модуль Node.js)

## 1.289 OneAgent

Развёртывание начинается 22 апреля 2024 г. для OneAgent

* Входящие сообщения Amazon SQS (модуль Java). Функция OneAgent: Java Amazon SQS
* Kafka Batch Listener (модуль Java). Функция OneAgent: Java Spring Kafka Batch Listener
* NGINX 1.25.4 (модуль NGINX)
* redis-py (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")

## 1.287 OneAgent

Развёртывание начинается 26 марта 2024 г. для OneAgent

* Аналитика журналов на Linux s390x (модуль Log). [Объявление](https://www.dynatrace.com/news/blog/enable-full-observability-for-linux-on-ibm-z-mainframe-now-with-logs/)
* Распространение W3C Trace Context для заголовков KafkaJS (модуль Node.js). Функция OneAgent: Отправка заголовков W3C Trace Context Kafka

## 1.285 OneAgent

Развёртывание начинается 27 февраля 2024 г. для OneAgent

* Alpine Linux (musl libc) для контейнеров 3.18, 3.19
* WebSphere Liberty 22, 23 (модуль Java z/OS)

## 1.283 OneAgent

Развёртывание начинается 30 января 2024 г. для OneAgent

* MongoDB 1.3–1.13 (модуль Go). Функция OneAgent: Go MongoDB
* OpenResty 25.3.1 (модуль NGINX)
* z/OS 3.1 (модуль zDC)

## 1.281 OneAgent

Развёртывание начинается 9 января 2024 г. для OneAgent

* NGINX Plus R31 (модуль NGINX)
* Node.js 21 (модуль Node.js)
* Node.js 14, 16, 18, 20, 21 на Linux s390x (модуль Node.js)
* OpenTelemetry 1.0.0 (модуль PHP)

## 1.279 OneAgent

Развёртывание начинается 20 ноября 2023 г. для OneAgent

* JMS 3.0 (модуль Java)
* Spring Webflux 6 (модуль Java)
* Spring WebFlux WebClient 6 (модуль Java)

## 1.277 OneAgent

Развёртывание начинается 26 октября 2023 г. для OneAgent

* .NET 8 (модуль .NET)
* Azure Cosmos DB 3.18+ (модуль .NET). Функция OneAgent: .NET Azure Cosmos DB
* IBM App Connect Enterprise CICSRequest node (модуль ACE)
* Jetty HTTP client 12 (модуль Java)
* Jedis Redi 5 (модуль Java)
* Go 1.21 (модуль Go)
* NGINX 1.25.2, 1.25.3 (модуль NGINX)
* Ubuntu 23.04 (модуль OS)

## 1.275 OneAgent

Развёртывание начинается 4 октября 2023 г. для OneAgent

* Amazon SNS для .NET (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md#sqs-sns-out "Трассировка AWS Lambda-функций с использованием среды выполнения .NET")
* Amazon SQS для .NET (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md#sqs-sns-out "Трассировка AWS Lambda-функций с использованием среды выполнения .NET")
* OpenJDK 21 LTS (модуль Java)
* Rancher Kubernetes Engine 2 (модуль OS)

## 1.273 OneAgent

Развёртывание начинается 5 сентября 2023 г. для OneAgent

* .NET (интеграция GCP). [Начало работы](../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet.md "Мониторинг Google Cloud Functions с OpenTelemetry для .NET и Dynatrace.")
* go-redis 7, 8, 9 (модуль Go). Функция OneAgent: Go Redis (go-redis/redis)
* Java ForkJoin (модуль Java). Функция OneAgent: Java/Scala ForkJoinPool
* JBoss LogManager 1.1+, 2, 3 (модуль Java)

## 1.271 OneAgent

Развёртывание начинается 7 августа 2023 г. для OneAgent

* AlmaLinux 9.0, 9.1, 9.2 (модуль OS)
* Amazon SNS для Java (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java.md "Подключение расширения Dynatrace AWS Lambda к Java API OpenTelemetry.")
* Amazon SQS для Java (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java.md "Подключение расширения Dynatrace AWS Lambda к Java API OpenTelemetry.")
* Fedora 37, 38 (модуль OS)
* NGINX 1.25.0, 1.25.1 (модуль NGINX)
* NGINX Plus R30 (модуль NGINX)
* Node.js 20 (модуль Node.js)
* openSUSE 15.5 (модуль OS)
* OpenTelemetry agent 1.27, 1.28 (модуль Java)

## Расширения платформы

Выпущено в июле 2023 г. в Dynatrace Hub

* Apache Cassandra (источник данных JMX). [Начало работы](https://www.dynatrace.com/hub/detail/cassandra/)
* HornetQ (источник данных JMX). [Начало работы](https://www.dynatrace.com/hub/detail/hornetq-1/)

## 1.267 OneAgent

Развёртывание начинается 7 июня 2023 г. для OneAgent

* Akka HTTP server 10.2, 10.4, 10.5 (модуль Java)

## Расширения платформы

Выпущено в мае 2023 г. в Dynatrace Hub

* Процессы .NET (источник данных WMI). [Начало работы](https://www.dynatrace.com/hub/detail/net/#get-started)
* Apache ActiveMQ Classic (источник данных JMX). [Начало работы](https://www.dynatrace.com/hub/detail/activemq/#get-started). Функция OneAgent: Java Metric Extensions 2.0 (JMX)
* Apache Kafka (источник данных JMX). [Начало работы](https://www.dynatrace.com/hub/detail/net/#get-started). Функция OneAgent: Java Metric Extensions 2.0 (JMX)
* IBM MQ. [Начало работы](https://www.dynatrace.com/hub/detail/ibm-mq-local/#get-started)
* TIBCO EMS. [Начало работы](https://www.dynatrace.com/hub/detail/tibco-ems-1/#get-started)

## 1.265 OneAgent

Развёртывание начинается 12 мая 2023 г. для OneAgent

* CBL-Mariner 2 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* DataStax client для Apache Cassandra 4 (модуль Java)
* Fujitsu Interstage 13 (модуль Java)
* Jakarta RESTful Web Services 2.1+ (модуль Java). Функция OneAgent: Java Servlet 5.0
* Lettuce 5.1.0–5.3, 6.0.3–6.1.6, 6.1.8–6.2 (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/redis/#get-started). Функция OneAgent: Java Lettuce Redis client
* Netty, User action to distributed trace correlation (RUM JavaScript и модуль Java). Функция OneAgent: Netty Real User Monitoring (RUM) to distributed trace correlation
* OpenTelemetry agent 1.24, 1.25 (модуль Java)
* Spring Data Redis 2.1+ (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/redis/#get-started). Функция OneAgent: Java Lettuce Redis client
* NGINX 1.23.4, 1.24.0 (модуль NGINX)

## 1.263 OneAgent

Развёртывание начинается 17 апреля 2023 г. для OneAgent

* .NET 7 (модуль .NET)
* Amazon Corretto 20 (модуль Java)
* Azul Platform Core (Zulu) 20 (модуль Java)
* Bellsoft Liberica 20 (модуль Java)
* Eclipse Temurin (a.k.a. 'Adoptium') 20 (модуль Java)
* Flatcar Container Linux 3033 LTS (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Go 1.20 (модуль Go)
* IBM IMS terminal transactions (модуль IMS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring.md#ims-terminal-transactions "Настройка мониторинга CICS и IMS на z/OS."). Функция OneAgent: z/OS IMS terminal transaction sensor
* log4net 2.0.6+ (модуль .NET). Функция OneAgent: .NET - Обогащение контекстом трассировки/спана Framework log4net
* OpenJDK 20 (модуль Java)
* OpenTelemetry 1.11.1–1.14 (модуль Go)
* OpenTelemetry agent 1.23 (модуль Java)
* Oracle HotSpot VM 20 (модуль Java)
* SAP JVM 20 (модуль Java)

## 1.261 OneAgent

Развёртывание начинается 14 марта 2023 г. для OneAgent

* Spring Web Services 4 (модуль Java). Функция OneAgent: Java Servlet 5.0

## 1.259 OneAgent

Развёртывание начинается 20 февраля 2023 г. для OneAgent

* Apache Tomcat 10 (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/apache-tomcat/#get-started), Функция OneAgent: Java Servlet 5.0
* Cassandra client (gocql/gocql) 1.0–1.3 (модуль Go). [Начало работы](https://www.dynatrace.com/hub/detail/cassandra/#get-started), Функция OneAgent: Go CQL (gocql/gocql)
* IBM CICS file access methods VSAM и BDAM (модуль IBM CICS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access.md "Мониторинг доступа к файлам CICS."), Функция OneAgent: z/OS CICS file monitoring sensor
* IBM IMS [transaction-oriented BMPs](https://www.ibm.com/docs/en/ims/15.1.0?topic=bmps-batch-message-processing-transaction-oriented) (модуль IBM IMS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims.md#bmp-tracing "Установка модуля Dynatrace IMS.")
* Jakarta Servlet 5, 6 (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/jakarta-servlet/#get-started), Функция OneAgent: Java Servlet 5.0
* Jersey 3 (модуль Java). Функция OneAgent: Java Servlet 5.0
* Jetty HTTP server 11 (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/eclipse-jetty/#get-started), Функция OneAgent: Java Servlet 5.0
* NGINX 1.23.3 (модуль NGINX)
* RabbitMQ client (php-amqplib) 2.7+ (модуль PHP). [Начало работы](https://www.dynatrace.com/hub/detail/net-rabbitmq/#get-started), Функция OneAgent: PHP RabbitMQ
* Undertow 2.3+ (модуль Java). Функция OneAgent: Java Servlet 5.0
* WildFly 27 (модуль Java). Функция OneAgent: Java Servlet 5.0

## 1.257 OneAgent

Развёртывание начинается 24 января 2023 г. для OneAgent

* Amazon SNS для Python (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md#python-sqs-sns "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")
* Amazon SNS для Node.js (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md#nodejs-sqs-sns "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")
* Apache HttpClient 5.2 (модуль Java)
* Google Cloud Run managed execution environment generation 1, 2 (модуль Java). [Начало работы](../ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md "Мониторинг Java-приложений, развёрнутых на Google Cloud Run managed.")
* IBM App Connect Enterprise Callable nodes (модуль IBM IIB/ACE)
* IBM CICS Transaction Server JSON requests (модуль IBM CICS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics.md#web-services "Установка модуля Dynatrace CICS.")
* Node.js 19 (модуль Node.js)
* SUSE Linux Enterprise Server 15.4 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux.md "Узнайте, как загрузить и установить Dynatrace OneAgent на Linux.")

## 1.255 OneAgent

Развёртывание начинается 12 декабря 2022 г. для OneAgent

* GraphQL 15+ (модуль Node.js). [Начало работы](https://www.dynatrace.com/hub/detail/graphql/#get-started)
* Microsoft SQL Server (denisenkom/go-mssqldb) 0.11.0-0.12.3 (модуль Go). [Начало работы](https://www.dynatrace.com/hub/detail/microsoft-sql-server-2/#get-started)
* Microsoft SQL Server (microsoft/go-mssqldb) 0.11.0-0.17.0 (модуль Go). [Начало работы](https://www.dynatrace.com/hub/detail/microsoft-sql-server-2/#get-started)

## 1.253 OneAgent

Развёртывание начинается 14 ноября 2022 г. для OneAgent

* Amazon SQS для Node.js (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")
* Amazon SQS для Python (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")
* PostgreSQL (jackc/pgx) 4.7–4.17 (модуль Go). [Начало работы](https://www.dynatrace.com/hub/detail/postgresql/#get-started)
* SQLite3 5.1+ (модуль Node.js)

## 1.251 OneAgent

Развёртывание начинается 14 октября 2022 г. для OneAgent

* Akka Http client 10.0, 10.2 (модуль Java)
* Amazon Corretto 19 (модуль Java)
* Apache HttpCore 5.x (модуль Java)
* Azul Platform Core (Zulu) 19 (модуль Java)
* Bellsoft Liberica 19 (модуль Java)
* Eclipse Temurin (a.k.a. 'Adoptium') 19 (модуль Java)
* Go 1.16+ (интеграция GCP). [Начало работы](../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go.md "Инструментирование Google Cloud Functions в Go с OpenTelemetry.")
* IBM z/OS Connect EE MQ service provider (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java.md "Настройка мониторинга Java на z/OS.")
* Jetty HTTP server 10 (модуль Java)
* Oracle HotSpot VM 19 (модуль Java)
* OpenJDK 19 (модуль Java)
* OpenTelemetry 0.0.12, 0.0.13, 0.0.14, 0.0.15 (модуль PHP)
* OpenTelemetry agent 1.17.x–1.19.x (модуль Java)
* Node.js 16 (интеграция AWS Lambda)
* SAP JVM 19 (модуль Java)

## 1.249 OneAgent

Развёртывание начинается 15 сентября 2022 г. для OneAgent

* Amazon Linux 2022 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Go 1.19 (модуль Go). [Начало работы](../ingest-from/technology-support/application-software/go.md "Обзор поддержки Go в Dynatrace.")
* OpenTelemetry 1.8, 1.9 (модуль Go). [Начало работы](../ingest-from/technology-support/application-software/go.md "Обзор поддержки Go в Dynatrace.")
* Rocky Linux 9 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")

## 1.247 OneAgent

Развёртывание начинается 25 августа 2022 г. для OneAgent

* Apache Camel 2.21+ (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/apache-camel/)
* IBM Semeru для z/OS 11 (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java.md "Настройка мониторинга Java на z/OS.")
* JMX 1.0+ (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics.md "Настройка мониторинга JMX-метрик для Java-приложений на z/OS.")
* Monolog 3.0 (модуль PHP)
* Python (интеграция GCP). [Начало работы](../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python.md "Мониторинг Google Cloud Functions с OpenTelemetry для Python и Dynatrace.")
* Red Hat Fuse на OpenShift 7.0+ (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/red-hat-fuse/)
* Red Hat Fuse Standalone 7.0+ (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/red-hat-fuse/)

## 1.246 SaaS/Managed

Развёртывание начинается 25 июля 2022 г. для SaaS и 1 августа 2022 г. для Managed

* DynamoDB client SDK для Node.js (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md#nodejs-instrumentation "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")

## 1.245 SaaS

Развёртывание начинается 6 июля 2022 г. для SaaS

* DynamoDB client SDK для .NET (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md#dynamo-db "Трассировка AWS Lambda-функций с использованием среды выполнения .NET")

## 1.245 OneAgent

Развёртывание начинается 19 июля 2022 г. для OneAgent

* AlmaLinux 8.6+ (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Fedora 35, 36 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* IBM CICS Transaction Server 6.1 (модуль CICS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics.md "Установка модуля Dynatrace CICS.")
* IBM Virtual I/O Server (AIX) 3.1 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix.md#vios-installation "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.")
* Kong API Gateway (модуль NGINX). [Начало работы](../ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation.md#howto "Узнайте, как принудительно инструментировать NGINX во время выполнения.")
* OpenTelemetry 0.0.10, 0.0.11 (модуль PHP)
* Python consumption plan (интеграция Azure). [Начало работы](../ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python.md "Мониторинг Azure Functions с OpenTelemetry для Python и Dynatrace.")
* [RabbitMQ](https://www.npmjs.com/package/amqplib) client 0.9 (модуль Node.js). [Начало работы](https://www.dynatrace.com/hub/detail/net-rabbitmq/#get-started)

## 1.244 SaaS/Managed

Развёртывание начинается 27 июня 2022 г. для SaaS и 5 июля 2022 г. для Managed

* DynamoDB client SDK для Python (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability.md#python-instrumentation "Включение и использование взаимодействия OpenTelemetry в AWS Lambda.")

## 1.243 OneAgent

Развёртывание начинается 29 июня 2022 г. для OneAgent

* Apache Log4j2 2.17.2–2.18 (модуль Java)
* JDBC 3, 4 (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java.md#jdbc "Настройка мониторинга Java на z/OS.")
* Node.js 18 (модуль Node.js)
* Node.js consumption plan (интеграция Azure). [Начало работы](../ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md "Мониторинг Azure Functions с OpenTelemetry для Node.js и Dynatrace.")
* Microsoft OpenJDK 11 LTS, 17 LTS (модуль Java)
* [oracledb](https://www.npmjs.com/package/oracledb) 5 (модуль Node.js). [Начало работы](https://www.dynatrace.com/hub/detail/oracle-database/)
* Red Hat Enterprise Linux 9 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Ubuntu 22.04 LTS (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")

## 1.241 OneAgent

Развёртывание начинается 8 июня 2022 г. для OneAgent

* .NET / .NET Core (интеграция AWS Lambda). [Начало работы](../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration.md "Трассировка AWS Lambda-функций с использованием среды выполнения .NET")
* .NET / .NET Core consumption plan (интеграция Azure). [Начало работы](../ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace.")
* Apache HttpClient 5.x (модуль Java)
* Azul Platform Core (Zulu) 18 (модуль Java)
* Bellsoft Liberica 18 (модуль Java)
* JMS 1.1 (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java.md "Настройка мониторинга Java на z/OS.")
* Node.js (интеграция GCP). [Начало работы](../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs.md "Мониторинг Google Cloud Functions с OpenTelemetry для Node.js и Dynatrace.")
* OpenJDK 18 (модуль Java)
* OpenTelemetry 0.0.9 (модуль PHP)
* Oracle HotSpot VM 18 (модуль Java)
* Rocky Linux 8 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* SAP JVM 18 (модуль Java)

## 1.239 OneAgent

Развёртывание начинается 27 апреля 2022 г. для OneAgent

* CentOS Stream 9 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")
* Go 18 (модуль Go)
* IBM AIX 7.3 TL0 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md "Узнайте, как установить OneAgent на AIX.")
* Kestrel (ASP.NET Core applications), Real User Monitoring (RUM JavaScript и модуль .NET)
* Ubuntu 21.10 (модуль OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md "Узнайте, как установить OneAgent на Linux.")

## 1.237 OneAgent

Развёртывание начинается 1 апреля 2022 г. для OneAgent

* IBM App Connect Enterprise 12.0.3.0+ (модуль ACE)
* Apache HTTP Server 2.2, 2.4 на Linux ARM64 (модуль Apache HTTP)
* PHP 7.1, 7.2, 7.3, 7.4, 8.0, 8.1 на Linux ARM64 (модуль PHP). [Начало работы](https://www.dynatrace.com/hub/detail/php/)

## 1.235 OneAgent

Развёртывание начинается 7 марта 2022 г. для OneAgent

* .NET / .NET Core 5.0, 6.0 на Linux ARM64 (модуль .NET). [Начало работы](https://www.dynatrace.com/hub/detail/net/)
* IBM App Connect Enterprise JavaCompute node (модуль ACE)
* IBM CICS terminal transactions (модуль CICS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring.md#transaction-start-filters "Настройка мониторинга CICS и IMS на z/OS.")
* IBM z/OS Connect EE IMS service provider (модуль Java z/OS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java.md "Настройка мониторинга Java на z/OS.")
* TIBCO ActiveMatrix BusinessWorks 6.6–6.8 (модуль Java)

## 1.233 OneAgent

Развёртывание начинается 7 февраля 2022 г. для OneAgent

* Go 17 (модуль Go)
* IBM IMS Fast Path (модуль IMS). [Начало работы](../ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims.md "Установка модуля Dynatrace IMS.")
* Jedis Redis 4 (модуль Java)
* reactor-core 3 (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/reactor-core/)

## 1.231 OneAgent

Развёртывание начинается 10 января 2022 г. для OneAgent

* Apache Log4J2 2.7–2.12 (модуль Java)
* Logrus 1.7.1–1.9 (модуль Go)
* Zap 1.10–1.21 (модуль Go)
* Windows Server 2022 (модуль OS)

## 1.229 OneAgent

Развёртывание начинается 22 ноября 2021 г. для OneAgent

* Apache Kafka Streams API (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/apache-kafka/)
* Apache Log4J2 2.13.0, 2.13.1, 2.13.3, 2.14.x–2.17.1 (модуль Java)
* Bellsoft Liberica 8 LTS, 11 LTS, 16, 17 LTS (модуль Java)
* Eclipse Temurin (a.k.a. 'Adoptium') 8 LTS, 11 LTS, 16, 17 LTS (модуль Java)
* IBM Semeru 8 LTS, 11 LTS, 16, 17 LTS (модуль Java)
* java.util.logging (модуль Java)
* Logback (QOS) 1 (модуль Java)
* OpenTelemetry 1.0–1.7 (модуль Go)
* Spring Cloud Stream (модуль Java). [Начало работы](https://www.dynatrace.com/hub/detail/apache-kafka/)
* winston 3 (модуль Node.js)
