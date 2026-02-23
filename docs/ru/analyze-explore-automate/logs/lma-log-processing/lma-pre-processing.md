---
title: Log pre-processing with OpenPipeline with ready-made bundles
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing
scraped: 2026-02-23T21:27:10.793074
---

# Log pre-processing with OpenPipeline with ready-made bundles

# Log pre-processing with OpenPipeline with ready-made bundles

* Latest Dynatrace
* Explanation
* 3-min read
* Published Dec 12, 2025

Dynatrace SaaS version 1.330+

Pre-processing logs with OpenPipeline with ready-made technology bundles allows you to enrich and normalize data, ensuring faster, scalable log analysis for popular technologies.

## Benefits of using ready-made bundles

* Automatic enrichment of logs from supported technologies without manual configuration.
  This adds context for easier troubleshooting and allows grouping, filtering, and searching by meaningful attributesânot just raw text.
* Improved log structure and metadata for better filtering and querying.
* Simplified setup and processing for new tenants with built-in coverage for standard tech stacks.

## Key advantages

* Logs follow a consistent structure.
* Simplified querying for faster and more accurate results.
* Seamless interpretation across the entire log analysis process.

## Ready-made bundles for popular technologies

There is a list of ready-made bundles for popular technologies, which you can find as **Ingest sources**.

The advantages of the **Ingest sources** bundles are the following:

* Provide centralized pre-processing for logs, enabling scalable and flexible handling.
* Automatically applies predefined technology bundles to selected **Ingest sources**, with built-in parsing and enrichment rules.

Technology bundles are automatically applied and can't be customized.

### List of technology bundles

To find the list of out-of-the-box coverage for popular technologies as **Ingest sources**, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** .

**Ingest sources**

**Processor**

Amazon Data Firehose

* AWS App Runner
* AWS Cloud Trail
* Amazon Relational Database Service (RDS)
* Amazon Simple Notification Service (SNS)
* AWS Common
* Amazon Aurora
* Amazon API Gateway
* AWS Lambda
* Amazon Virtual Private Cloud Flow Default
* AWS Transit Gateway
* AWS WAF
* Amazon Cloudfront

Data Acquisition - AWS Data Firehose

* AWS Lambda
* AWS App Runner
* Amazon Relational Database Service (RDS)
* Amazon Aurora
* Amazon Simple Notification Service (SNS)
* Amazon API Gateway

Log ingestion API

* Amazon API Gateway
* Amazon Aurora
* Amazon CloudFront
* Amazon Virtual Private Cloud Flow Default
* AWS App Runner
* AWS Cloud Trail
* AWS Common
* AWS Lambda
* Amazon Relational Database Service (RDS)
* Amazon Simple Notification Service (SNS)
* AWS Transit Gateway
* AWS WAF
* Azure Services
* Azure Entra ID Audit Logs

OneAgent

* Elasticsearch
* Cassandra
* PostgreSQL
* Redis
* NodeJS
* PHP
* Java
* Python
* .NET
* Ruby
* Go
* RabbitMQ
* Apache Kafka
* Nginx
* HAProxy
* Apache Tomcat
* Apache HTTP
* JBoss
* Microsoft IIS
* Syslog

OpenTelemetry

None

## Related topics

* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")