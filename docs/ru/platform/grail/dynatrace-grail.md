---
title: What is Dynatrace Grail?
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-grail
scraped: 2026-02-23T21:20:42.580969
---

# What is Dynatrace Grail?

# What is Dynatrace Grail?

* Latest Dynatrace
* Explanation
* 7-min read
* Updated on Jan 28, 2026

The Grailâ¢ data lakehouse at the heart of the Dynatrace platform enables contextual analytics across unified observability, security, and business data. It is purpose-built for data observed and collected from digital services at exabyte scale.

As a data lakehouse, Grail combines the cost efficiency advantages of data lakes with the analytics capabilities of data warehouses, and adds extreme performance through massively parallel processing.

Grail provides:

* Answers to questions you could never get before through contextual analytics.
* Unified observability, security and business dataâcost effectively and at exabyte scale.
* Any-question-any-time real-time analytics with always hydrated zero-latency cold/hot storage.
* Increased productivity as no-index datawarping technology as well as schema-on-read drastically reduces data preparation efforts by magnitudes.
* Simplified compliance as Grail securely integrates with [Dynatrace Intelligence hypermodal AI](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."), [AppEngine](/docs/platform/appengine "Develop feature-rich Dynatrace apps for you and the world!"), [AutomationEngine](/docs/platform/automationengine "Combine observability, security, and business data with causal AI to easily automate BizDevSecOps workflows at enterprise scale."), and more as part of the Dynatrace platform.

## Contextual analytics

Grail provides answers to questions you could never get before as it unifies observability, security, and business data, but, even more importantly, maintains a graph context with causal dependencies among data. This is only possible as Grail incorporates a unique combination of graph, event, timeseries, and NoSQL database approaches.

Contextual analytics works on heterogeneous data, including metrics, logs, traces, user-behavior, sessions, profiles, vulnerabilities, metadata, and much more, all equally well, and puts them into context. Contextualizing data is done fully automatically, without the need for tagging or defining schemas upon data ingestion or during storage.

Contextual analytics leverages Dynatrace Intelligence causal AI to follow dependencies and therefore, uniquely enabling investigations such as:

* Understanding a precise root-cause of an issue in a distributed microservice cloud application.
* Following the path of an attack in a security investigation to provide a risk assessment.
* Segmenting business data by revenue.
* Automatically showing and analyzing surrounding log and trace data when investigating problems such as user checkout degradation.

## Exabyte scale

Grail breaks through the limits of common index-enabled databases and thus is uniquely capable of bringing all data types together into a single place and de-siloing information, while retaining full granularity. It does this by:

* Processing and storing up to 1,000 TB of data per day, depending on the data ingestion channels (such as OneAgent or API) and the nature of the signals. To ensure optimal performance, a tailored scaling strategy is essential. To see the actual limits, see [OpenPipeline limits](/docs/platform/openpipeline/reference/limits "Reference limits of Dynatrace OpenPipeline.").
* Providing a Massive Parallel Processing (MPP) query engine, enabling rapid processing of any query any time, without requiring any upfront definitions.
* Utilizing datawarping to retrieve data from always hydrated zero-latency cold/hot storage, while eliminating the overhead cost and scalability limits of indexes.

## Always hydrated zero-latency cold/hot storage

Grail revolutionizes data management by natively providing seamless data-lake technology, eliminating the traditional processes of rehydration and the need to export data to external storage solutions like AWS S3 for reducing costs, and thus streamlining operations.

Grail features an advanced automatic cold/hot data management system that ensures data remains fully accessible with zero latency, effectively offering always-hydrated data.

* Always-hydrated means that data is always available with zero latency, eliminating the need for rehydration.
* Grail doesn't need any index, removing the costly overhead and inflexibility of predefined schemas.
* Users will not notice any difference between cold and hot data, thanks to massively parallel processing and datawarping.
* Grail performs automatic data management based on access patterns.
* Grail eliminates the need to export data to external cloud storage and follow lengthy and costly rehydration operations, thus eliminating the need for a separate datalake.

## Capabilities of Grail

When using Grail, you benefit from capabilities such as:

* Data integration: unify all your heterogenous data in one single data store.
* Real-time data processing during high-volume ingest.
* Flexible data transformation on ingest via OpenPipeline.
* Easy retention management.
* Schemaless data organization: data is always stored in context without the need to define any schema. Ask any question any time.
* Realtime insights without index overhead, enabling you to search and analyze any kind of dataâtext, characters, or patterns, regardless of whether it's indexed.
* AI-powered analytics and automation utilizing Dynatrace Intelligence , Smartscape, and AutomationEngine.
* Exploratory data analytics running complex queries in Dashboards or Notebooks, utilizing an optimized query engine.
* Data governance: control access to your data as well as your applications using a single, unified system.
* Data observability: ensure availability, reliability, and quality of data.

## Meet compliance and data privacy requirements

At Dynatrace, we take our responsibility to safeguard your data seriously. We have implemented different levels of data protection and strictly adhere to the principles of privacy by design and privacy by default.

* Grail provides true hard deletion of data for enforcing strongest privacy requirements.
* Grail offers fine-grained access control at the table, bucket, and record level, including field-based permissions to exclude privacy-relevant fields from being displayed.
* With OneAgent and OpenPipeline, Dynatrace provides data masking and filtering at capture and ingest.
* Grail guarantees environment-specific keying for data isolation to protect against unauthorized access.
* Direct access to stored data by users is not permitted, safeguarding the integrity and security of the data. Instead, data retrieval and queries can only be conducted through DQL queries using the Query Processing layer, which acts as a secure gateway, ensuring that data retrieval is efficient, super-fast, and secure.

## Immutable data storage

Immutable data storage in Grail is designed with a fundamentally immutable data architecture. This means that once data is ingested, it canât be altered. All dataâwhether logs, events, spans, or metricsâis stored as records, each of which is treated as an atomic, unchangeable unit.

These records are grouped into time-ordered data packets, each approximately 1 GB in size. These packets are stored in cloud object storage such as Amazon S3, Azure Blob, or Google Cloud Storage. When data is queried, Grail loads the entire packet into memory and evaluates the individual records from there.

Because of this architecture:

* Modifying a single record is not possible.
* To delete a record, the entire packet must be rewritten.
* Only authorized users can use the Deletion API to delete individual records or entire packets.
* Every deletion operation is fully audited and logged.
* Dynatrace itself does not modify or delete customer data. Deletion of data by Dynatrace can only occur through explicit customer support requests, and even then, only entire packets can be removed, not individual records within them. This approach ensures data integrity, auditability, and compliance, making Grail a secure and reliable foundation for observability and analytics.

## Guidance: using Grail vs. conventional databases



Grail is optimized for extreme throughput and extreme volumes of immutable data converged into one unified place for cost-effective storage and high-performance query. It incorporates elements of ACID and BASE providing full flexibility and contextual analytics.

Scenario

Grail

Conventional DBs

From tera- to exabyte scale of immutable data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

For heterogeneous data in context

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

For real-time instant query any-question any-time

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Observability, security data, and business data from digital systems

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

For cost-effectiveness as a data lake

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Minimize data interfaces and data flow

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

ACID transactional guarantees

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

When you need highly frequent updates to data records

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Conventional databases are either built to handle transactional data in low volume following the ACID paradigm, or implement the BASE paradigm known from NoSQL databases.

ACID stands for:

* Atomicity: Ensures that a transaction either fully completes or fails entirely. No partial changes occur.
* Consistency: Guarantees that data remains consistent, adhering to all constraints even during transactional modifications.
* Isolation: Prevents concurrent transactions from interfering with each other. Each transaction sees the world as if executed sequentially.
* Durability: Once a transaction is complete, its changes are permanently recorded.

ACID databases are used for scenarios where data integrity and reliability is paramount. Most relational database management systems (such as Oracle, MySQL, and PostgreSQL) support the ACID paradigm.

BASE is an alternative to ACID and is especially suited for distributed systems where high availability, fault tolerance and scalability is required.

BASE stands for:

* Basically Available: The system remains operational even in the face of failures, albeit with potentially reduced functionality.
* Soft state: The system's state may change over time due to eventual consistency.
* Eventually consistent: Updates propagate through the system eventually, but not necessarily immediately.

NoSQL databases like Cassandra, Redis, and Amazon DynamoDB are examples of storage systems designed around the BASE paradigm.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Log Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")
* [Business Observability](/docs/observe/business-observability "Basic concepts, setup and configuration, and use cases for Dynatrace Business Observability")