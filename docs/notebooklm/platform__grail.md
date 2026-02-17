# Dynatrace Documentation: platform/grail

Generated: 2026-02-17

Files combined: 21

---


## Source: dynatrace-grail.md


---
title: What is Dynatrace Grail?
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-grail
scraped: 2026-02-17T04:46:53.195776
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


---


## Source: dpl-architect.md


---
title: DPL Architect
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/dpl-architect
scraped: 2026-02-17T04:58:16.713600
---

# DPL Architect

# DPL Architect

* Latest Dynatrace
* Reference
* Updated on Feb 28, 2024

Latest Dynatrace

The DPL Architect tool helps you

* Extract fields from records.
* Create the right data pattern to save time in developing DPL patterns.
* Get instant feedback about the effectiveness and coverage of your patterns for your specific use case.
* Save and reuse your existing DPL patterns for faster access to data analytics use cases.
* Use preset patterns for the most popular technologies.

## How it works

DPL Architect provides instant feedback to your DPL pattern expression without the need to re-execute your DQL query. This saves you time and energy when determining what DPL expression you need. Feedback is given in two contexts: base dataset and match preview dataset.

### Base dataset

The base dataset is created from the original query executed in Notebooks. The same query is executed in DPL Architect and saved as a base dataset to show you what portion is matched by the pattern you created.

![Base dataset](https://dt-cdn.net/images/image-2023-07-09-23-26-30-663-2294-742f00c80e.png)

### Match preview dataset

The match preview dataset consists of records displayed in DPL Architect. When you open DPL Architect, the record from where you started to extract additional fields is displayed in the match preview editor. You can add additional lines from the base dataset by selecting [**Add to preview**](#visual-feedback) and, if needed, you can create additional records manually. The portion of the record that matches the DPL pattern is highlighted so that you can visualize the progress of your pattern.

![Match Preview dataset](https://dt-cdn.net/images/image-2023-07-09-23-29-23-054-2352-31d5669db5.png)

## Access DPL Architect

You can currently access DPL Architect from

* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks")

  Show me how

  1. In **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks"), open the ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") menu and select **Logs** > **Fetch logs**.
  2. In the query section, select **Run query**.
  3. In the results section, select a cell and then select **Extract fields** from the pop-up menu.

  ![Extract fields](https://dt-cdn.net/images/extract-fields-793-11d23cd027.png)
* [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.")

  Show me how

  While using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), there are several ways to access DPL Architect. For instructions, see [Extract](/docs/secure/investigations/extract-fields "Pull specific data points from logs in Investigations.").

## Use DPL Architect

Once you open DPL Architect, you can

* [Enter a schema pattern](#add-pattern)
* [View matching records](#matching)
* [Preview with highlighted syntax](#preview)
* [View extracted fields](#view-results)
* [Get visual feedback about your pattern quality](#visual-feedback)
* [Experiment with multiple patterns](#multiple-patterns)
* [Apply your pattern to the query](#apply-pattern)
* [Use preset patterns](#preset-patterns)

![Default pattern](https://dt-cdn.net/images/default-pattern-1532-08ecb0ab33.png)

### Enter a schema pattern

Use the expression editor to enter your schema pattern and start field extractions. Start typing and use the autocomplete suggestions.

* If the pattern is in the correct format, **Pattern is valid** is displayed.
* If the pattern format contains errors, **Pattern error: â¦** indicates the line and position of the invalid element.

![DPL expression editor](https://dt-cdn.net/images/2023-04-21-18-36-49-819-d897a39622.png)

### View matching records

[**Base dataset**](#base-dataset) displays how many records from the original query results match your pattern.

![Matching records](https://dt-cdn.net/images/2023-04-21-19-19-31-1839-c862944146.png)

### Preview with highlighted syntax

* [**Match preview editor**](#match-preview) checks if the schema pattern you entered matches the record. The portion of the record that matches the DPL pattern is highlighted.

![match preview](https://dt-cdn.net/images/match-preview-1522-b64f0262ce.png)

* **Add log record** adds a row so you can enter a custom data record to the preview, in addition to the existing data, for pattern validation.

### View extracted fields

**Results** displays the extracted fields as new columns if, in your pattern, you add names to the extracted fields after the colon (for example, `IPADDR:client_ip`).

![Query results](https://dt-cdn.net/images/results-1585-68c93a5fb3.png)

### Get visual feedback about your pattern quality

Select **Add to preview** (located to the right of the base dataset) to

* Add records from your query result to your match preview component and get visual feedback about your pattern quality.
* Find out which records from the original result set match your pattern.
* Add the unmatched records to the preview set to further improve your DPL pattern.

### Experiment with multiple patterns

You can have multiple DPL patterns opened at the same time in different tabs. This way you can

* Reuse parts of existing patterns
* Try different scenarios
* Compare pattern performance

When working with multiple patterns, use these commands:

* Select **New** to create a new pattern.
* Select **Save** to save your pattern.
* Select **Saved patterns** to show or hide a list of saved patterns.

Unsaved patterns persist after closing DPL Architect and are only dismissed when you close the tabs manually.

### Apply your pattern to the query

* Select **Insert pattern** to add the pattern to the parse command at the end of the original query.
* Select **Close** to return to the query section, and rerun the query to see the extracted fields in the results.

## Preset patterns

DPL Architect provides a variety of preset patterns for the most popular technologies in the field, such as AWS, Microsoft, and Google Cloud.

These patterns can be

* Used out of the box to extract all fields from a specific event.
* Customized based on your preference.

### Access preset patterns

To access the preset patterns, select **Saved patterns** > **Dynatrace patterns**.
For faster access, preset patterns are logically divided into a folder structure.

![Dynatrace preset patterns for DPL Architect](https://dt-cdn.net/images/image-12-1364-de47643fe0.png)

### List of preset patterns

See below for the list of preset patterns.

Pattern

Description

`apache/access`

Apache HTTP servers access log pattern. See: [Apache log filesï»¿](https://dt-url.net/lb038dx)

`apache/error-default`

Apache HTTP servers error log pattern. See: [Apache log filesï»¿](https://dt-url.net/lb038dx)

`aws/cloudfront`

AWS CloudFront default log pattern. See: [Standard log file fieldsï»¿](https://dt-url.net/8l238a9)

`aws/cloudtrail`

Extracts all the fields from AWS CloudTrail JSON-formatted log record. See: [CloudTrail log file examplesï»¿](https://dt-url.net/hg43865)

`aws/elb`

Extracts all the fields from AWS Elastic Load Balancer log record. See: [Access logs for your Application Load Balancerï»¿](https://dt-url.net/67m386h)

`aws/route53-query`

Extracts all the fields from JSON-formatted AWS Route53 resolver query log record. See: [Route 53 Resolver query log exampleï»¿](https://dt-url.net/b76389g)

`aws/s3-server-access`

Extracts all the fields from AWS S3 server access log records. See: [Amazon S3 server access log formatï»¿](https://dt-url.net/4i838sr)

`aws/vpc-flow-default`

Extracts all the fields from the AWS VPC Flow logs default format. See: [Flow log recordsï»¿](https://dt-url.net/tsa38nd)

`aws/vpc-flow-default`

Extracts the fields from the AWS VPC Flow logs custom format, when all the fields have been added in the default order. See: [Flow log recordsï»¿](https://dt-url.net/tsa38nd)

`gcp/scc`

Extracts the relevant fields from GPC Security Command Centers' records. See: [REST Resource: organizations.sources.findingsï»¿](https://dt-url.net/6gc38t3)

`haproxy/http`

Extracts all the fields from HAProxy HTTP default log records. See: [HAProxy Configuration Manualï»¿](https://dt-url.net/74e38p0)

`iis/default`

Extracts all the fields from Microsoft IIS access logs. See: [Configure Logging in IISï»¿](https://dt-url.net/g8g38i7)

`k8s/audit`

Extracts all the fields from JSON-formatted Kubernetes apiservers' audit log records. See: [kube-apiserver Audit Configurationï»¿](https://dt-url.net/3yi38ir)

`k8s/coredns-query`

Extracts all the fields from CoreDNS default query logs. See: [CoreDNS logï»¿](https://dt-url.net/pfk38xe)

## Use case

### Investigate security incidents in Kubernetes clusters

Application Security

In this use case, you work with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze unauthorized requests in your Kubernetes audit logs. See how you can get a precise extraction of fields from complex data and instant feedback on your patterns about their effectiveness and coverage, without the need to re-execute queries, to find the origin of your unauthorized requests and get accurate results about what happened.

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")

## Further resources

For additional insights into DPL Architect, see

* Blog: [Speed up your security investigations with DPL Architectï»¿](https://dt-url.net/mn0380l)
* Dynatrace University tutorial:

  Additional insights into DPL Architect

## Related topics

* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")
* [Investigations](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.")
* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")


---


## Source: log-processing-positional-matchers.md


---
title: DPL Positional Matchers
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-positional-matchers
scraped: 2026-02-17T04:58:21.631657
---

# DPL Positional Matchers

# DPL Positional Matchers

* Latest Dynatrace
* Reference
* Published Nov 08, 2022

## Beginning of string

**BOS, BOF**

Matches beginning of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting the first line in the string:

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104
```

```
BOF LD:header EOL;
```

Results in the first line parsed into the `header` field. Parsing following lines fails, as they do not begin at the start of file marker.

| header |
| --- |
| `''name'';''age''` |
|  |

## Middle of string

**MOS, MOF**

Matches any bytes in the middle of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting records after the first row in the string

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104
```

```
MOF LD:name ';' INT:age EOL
```

Results in lines 2 and 3 parsed to fields `name` and `age`. Line 1 fails to parse as it begins with the beginning of the string marker.

| name | age |
| --- | --- |
|  | `-1` |
| `Homer Simpson` | `40` |
| `Charles Montgomery Burns` | `40` |

## End of string

**EOS, EOF**

Matches end of string

output type

quantifier

configuration

none

none

none

#### Example

Extracting the last line of the string:

```
"name";"age"



Homer Simpson;40



Charles Montgomery Burns;104



total:2 persons, average age: 72 years
```

The following pattern matches only when the last line is followed by the end of string marker:

```
LD:footer EOS
```

Results in the last line being extracted to the `footer` field. First three lines fail to parse as they are not the last in the string.

| footer |
| --- |
|  |
| `total:2 persons, average age: 72 years` |


---


## Source: dynatrace-pattern-language.md


---
title: Dynatrace Pattern Language
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language
scraped: 2026-02-17T05:09:55.836050
---

# Dynatrace Pattern Language

# Dynatrace Pattern Language

* Latest Dynatrace
* Explanation
* Updated on Aug 11, 2022

Dynatrace Pattern Language (DPL) is a pattern language that allows you to describe patterns using matchers, where a matcher is a mini-pattern that matches a certain type of data. For example, `INTEGER` (or `INT`) matches integer numbers, and `IPADDR` matches IPv4 or IPv6 addresses. There are matchers available to handle all kinds of data types.

## Usage

Use DPL to:

* Parse a record field into multiple output fields with the [DQL parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "DQL extraction commands").
* Reshape incoming data for better understanding, analysis, or further processing in [Log processing](/docs/analyze-explore-automate/logs/lma-log-processing "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.").

For instant feedback on the effectiveness and coverage of your patterns for your specific use case, use [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.").

## Pattern Structure

A written pattern is interpreted from left to right, ignoring extra whitespaces, line breaks, and comments in between. You can write the pattern describing an integer followed by a single space, IP address, and line break as the following one-liner:

```
INT ' ' IPADDR:ip EOL
```

Or you can write the same pattern in a more explanatory way:

```
/* this pattern expects an integer number and an IP address



separated by single space in each line */



INT       //an integer



' '       //followed by single space



IPADDR:ip //followed by IPv4 or IPv6 address, extracted as a new field, `ip`



EOL       //line is terminated with line feed character
```

With [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect."), you can use [preset patterns](/docs/platform/grail/dynatrace-pattern-language/dpl-architect#preset-patterns "Extract fields with Dynatrace Pattern Language Architect.") for the most popular technologies.

## Matching vs Parsing

You don't necessarily need all data elements in the input data for analysis. For instance, field separators or end-of-record markers in a log line are useful only for parsing, but we don't need them when we run the queries. All matchers in a defined pattern must match, but only a subset of them may also extract (parse) data.

A matcher will extract data only when it has been assigned an [export name](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers#exportname "Explore DPL syntax for optional controlling elements (modifiers).") - this is an arbitrary name of your choice, which becomes the name of the field you use in query statements.

In the following example, the pattern has:

* 11 matchers in total
* 4 matchers that are extracting data

![DPL language reference](https://dt-cdn.net/images/dpl-ref-2133-49fd05dd03.png)

## Matcher structure

A DPL pattern consists of one or more matcher expressions. They can be separated by whitespace or commas or newlines. For a handy reference guide to all matchers, see the [DPL Grammar page](/docs/platform/grail/dynatrace-pattern-language/log-processing-grammar "Complete grammar list of Dynatrace Pattern Language (DPL) syntax.").

### Matcher types

In general, a matcher expression can be any of the following:

* Built-in matchers for many frequently used data types (numeric, time, network, and so on)
* [literal expressions](/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression "Explore DPL syntax for handling literal expressions.")
* [character groups](/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings "Explore DPL syntax for handling lines and strings."), which are arbitrary set of characters to be matched (Regular Expression compatible)
* [Reference to another pattern expression](/docs/platform/grail/dynatrace-pattern-language/log-processing-macros "Explore DPL syntax for creating a series of matcher expressions (subpatterns)."), to facilitate building complex patterns in a modular way

### Matcher grouping

Matcher expressions can be grouped:

* [sequence group](/docs/platform/grail/dynatrace-pattern-language/log-processing-sequence-group "Explore DPL syntax for sequence group matching where all its members must match.")âdefines an ordered sequence of matchers
* [alternatives group](/docs/platform/grail/dynatrace-pattern-language/log-processing-alternatives-group "Explore DPL syntax for Alternatives group.")âdefines a list of matchers to choose from
* [array](/docs/platform/grail/dynatrace-pattern-language/log-processing-array "The DPL ARRAY allows parsing repeated sequences of variable number data elements, specified by a pattern supplied as an argument.")âto parse repeated data elements
* [structure](/docs/platform/grail/dynatrace-pattern-language/log-processing-structure "Explore DPL syntax for structuring data.")âto capture parsed data as composite type
* [enum group](/docs/platform/grail/dynatrace-pattern-language/log-processing-enum "The DPL Enum constructor allows matching for a set of predefined strings and converts them into respectively assigned integer values.")âto match strings to numeric values
* [JSON](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.")âto parse JSON structures

### Matcher Expression Syntax

A matcher expression consists of the matcher itself and optional controlling elements (modifiers) arranged in the following order (from right to left, where square brackets indicate optional elements):

```
[lookaround] MATCHER_EXPR ['(' configuration ')'] [quantifier] [mod_optional] [':'export_name]
```

Note that whitespace characters and newlines are allowed between the elements. Placing elements in a different order (for instance, by placing `mod_optional` after the `export_name`) will cause a syntax error.

### Matcher operators

Matcher expressions have `operators`:

* Some matchers allow [configuration](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers).") specifying their behavior. For instance, a timestamp needs an expected format definition.
* Most matchers and groupings can be added with a [quantifier](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers).") to tell the engine how many times it should try to match.
* All matchers and groupings can be declared to be [optional](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers)."). If the element in the expected position is missing, the engine outputs NULL to the resultset and continues with the next matcher in the expression.
* All matchers and groupings can be assigned an [export name](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers)."), which is the name of the field exposed to the query layer.

  The sole purpose of pattern matching is to make data elements available for the query engine. However, not all matched elements are needed for queries (such as field separators in tabulated files), so an export name is a mechanism for the user to declare which data elements are exposed for queries (at the same time providing a name for the query fields). A matcher without an export name still does its job matching the pattern, but it's not visible in queries.
* All matchers and groupings can ["look around"](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers).") (backward or forward), mainly to enable decision-making (conditional branching).

## Example

The following is an example of step-by-step pattern matching.  
Suppose we have a comma-separated record (terminated with the line feed character) with the following fields:

* order number - integer
* username - consisting of upper and lower case letters and numbers (but not a comma)
* ipv4 address of the user

```
1,alice,192.168.1.1



2,bob,10.6.24.18



3,mallory,192.168.1.3
```

This structure can be described by the following pattern expression:

```
INT:seq



','



LD:uname



','



IPADDR:user_ip



EOL
```

where:

* line 1: integer matcher for the order number, visible in queries as 'seq' on line 2,4 constant string matcher for the field separator, not visible in queries
* line 3: line data matcher, visible in queries as 'uname'
* line 5: IP address matcher, visible in queries as 'user\_ip'
* line 6: chargroup matcher for the line feed terminating the record

The pattern matching engine tries to apply the pattern by utilizing matchers in the order in which they were defined. The example above starts by trying to match `INT:seq` at the first byte of input data. This happens to be `1`. As it is suitable for an integer type, it moves on to the next byte.

Next, the engine finds the byte to be a comma. This does not match with an integer, so the `INT:seq` matcher is completed by converting `1` to an integer and the next matcher in the pattern is selected: `','`. The engine tries it for a current position of data and finds a match.

So the data pointer is moved on to the next byte (pointing to the first letter of `bob`). As the constant string matcher contained just one character, the matcher is considered complete and the engine takes the next one in the pattern: `[a-zA-Z0-9]*:uname`. The [quantifier](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers "Explore DPL syntax for optional controlling elements (modifiers).") `*` forces `[a-zA-Z0-9]*:uname` to consume a variable number of bytes (zero or more), so it keeps matching until it finds a byte not matching its defined characters. This happens at the second comma (just after `bob`), where the engine considers the `[a-zA-Z0-9]*:uname` matcher complete and takes the next one: `','`. Again, it tries to match it to the byte at the current position and succeeds.

The data pointer is moved to the next byte, pointing to the beginning of `192.168.1.1`. As `','` is completed, the engine takes `IPV4ADDR:user_ip`. Trying it from the current position, a match is found and the data pointer is moved forward 11 bytes, now pointing to a newline character. The engine finds a match for it using the last matcher in the pattern: `[\n]`.

Now the data pointer is advanced to the next byte, the pattern iterator is reset, and the cycle continues with trying the first matcher of the pattern against the currently pointed data. This continues until the end of the input data.

If the engine encounters data for which it is unable to find a match, it resets the pattern iterator, marks this byte as unmatched, and moves on to the next byte. This continues until a match is found or there is no more data. Eventually, the following structured data is the output:

| seq | uname | user\_ip |
| --- | --- | --- |
| `1` | `alice` | `192.168.1.1` |
| `2` | `bob` | `10.6.24.18` |
| `3` | `mallory` | `192.168.1.3` |

## Related topics

* [Log processing (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-processing "Create log processing rules that reshape your incoming log data for better analysis or further processing.")


---


## Source: commands.md


---
title: DQL commands
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/commands
scraped: 2026-02-17T04:55:01.729375
---

# DQL commands

# DQL commands

* Latest Dynatrace
* Reference
* Updated on Nov 19, 2025

This page provides a list of DQL commands grouped by categories. To get more in-depth information on a specific command, click on its name.

## [Data source commands](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands "DQL data source commands")

Name

Description

[data](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#data "DQL data source commands")

Generates sample data during query runtime.

[describe](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#describe "DQL data source commands")

Describes the on-read schema extraction definition for a given data object.

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

Loads data from the specified resource.

[load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands")

Loads data from the specified resource. It's used with [lookup data](/docs/platform/grail/lookup-data "Learn about lookup data in Grail.").

## [Metric commands](/docs/platform/grail/dynatrace-query-language/commands/metric-commands "DQL metric commands")

Name

Description

[timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands")

Combines loading, filtering and aggregating metrics data into a time series output.

[metrics](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#metrics "DQL metric commands")

Retrieves metric series.

## [Filter and search commands](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands "DQL filter and search commands")

Name

Description

[dedup](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#dedup "DQL filter and search commands")

Removes duplicates from a list of records.

[filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands")

Reduces the number of records in a list by keeping only those records that match the specified condition.

[filterOut](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut "DQL filter and search commands")

Removes records that match a specific condition.

[search](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search "DQL filter and search commands")

Searches for records that match the specified search condition.

## [Selection and modification commands](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "DQL selection and modification commands")

Name

Description

[fields](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands")

Keeps only specified fields.

[fieldsAdd](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsAdd "DQL selection and modification commands")

Evaluates an expression and appends or replaces a field.

[fieldsKeep](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsKeep "DQL selection and modification commands")

Keeps selected fields.

[fieldsRemove](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRemove "DQL selection and modification commands")

Removes fields from the result.

[fieldsRename](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fieldsRename "DQL selection and modification commands")

Renames a field.

## [Extraction and parsing commands](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands")

Name

Description

[parse](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "DQL extraction commands")

Parses a record field and puts the result into one or more fields as specified in the pattern.

## [Ordering commands](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands "DQL ordering commands")

Name

Description

[limit](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#limit "DQL ordering commands")

Limits the number of returned records.

[sort](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "DQL ordering commands")

Sorts the records.

## [Structuring commands](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands "DQL structuring commands")

Name

Description

[expand](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#expand "DQL structuring commands")

Expands an array into separate records.

[fieldsFlatten](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#fieldsFlatten "DQL structuring commands")

Extracts/flattens fields from a nested record.

## [Aggregation commands](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands "DQL aggregation commands")

Name

Description

[fieldsSummary](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#fieldsSummary "DQL aggregation commands")

Calculates the cardinality of field values that the specified fields have.

[makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands")

Creates timeseries from the data in the stream.

[summarize](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands")

Groups together records that have the same values for a given field and aggregates them.

## [Correlation and join commands](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands "DQL correlation and join commands")

Name

Description

[append](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append "DQL correlation and join commands")

Appends a given list of records by the records returned by a sub-query.

[join](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join "DQL correlation and join commands")

Joins all records from the source and the sub-query as long as they fulfill the join condition.

[joinNested](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join-nested "DQL correlation and join commands")

Adds matching results from the sub-query as an array of nested records.

[lookup](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#lookup "DQL correlation and join commands")

Adds fields from a subquery to the source table by finding a match between a field in the source table and the lookup table.

## [Smartscape commands](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands "DQL Smartscape commands")

Name

Description

[smartscapeNodes](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeNodes "DQL Smartscape commands")

Loads Smartscape nodes using a type pattern (use `*` for all types).

[smartscapeEdges](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeEdges "DQL Smartscape commands")

Loads Smartscape edges using an edge type pattern (use `*` for all types).

[traverse](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#traverse "DQL Smartscape commands")

Traverses source nodes to target nodes in the specified direction, following edge types defined by edgeTypes.

## Related topics

* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: data-types.md


---
title: DQL data types
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/data-types
scraped: 2026-02-17T04:55:16.278439
---

# DQL data types

# DQL data types

* Latest Dynatrace
* Reference
* Updated on Oct 24, 2024

The Dynatrace Query Language operates with strongly typed data: the functions and operators accept only declared types of data. The type is assigned to data during parsing or by using casting functions. DQL also recognizes value types expressed in literal notation (for example, using constant values in functions).

## Primitive types

### Boolean

Boolean has only two possible values: `true` and `false`.

* **Literal notation**  
  A Boolean value can be expressed using either uppercase or lowercase letters: `true`, `TRUE`, `false`, `FALSE`
* **Converting to Boolean**

  + Converts string values `true`, `TRUE` to a `true` Boolean value, and other values to `false`.
  + Converts numeric value `0` to Boolean `false`. Converts other numeric values to Boolean `true`.

  ```
  ...



  | fields toBoolean("true"), toBoolean("TrUe"), toBoolean("1"), toBoolean(3), toBoolean("test"), toBoolean(0)
  ```
* **Expressions**

  ```
  boolean_expr1 AND boolean_expr2



  boolean_expr1 OR boolean_expr2



  boolean_expr1 XOR boolean_expr2



  NOT boolean_expr
  ```

### Long

The signed long has a minimum value of -2^63 and a maximum value of 2^63-1.

* **Literal notation**  
  LONG can be expressed in decimal or hexadecimal notation:  
  **decimal:** `-9223372036854775808` to `9223372036854775807`  
  **hexadecimal:** `0x0` to `0xFFFFFFFFFFFFFFFF`
* **Converting to Long**

  ```
  ..



  | fields toLong("83457264009472472"), toLong(30), toLong(25.34)
  ```

### Double

Double-precision 64-bit IEEE 754 floating point.

* **Literal notation**

  **decimal:** `2.34`
  **scientific:** `2.4e2`
* **Converting to Double**  
  Converts numeric values and expressions to a double value.

  ```
  ...



  | fields toDouble("1234.5"), toDouble(4+3/2)
  ```

### Timestamp

A reference to a point in time with the precision of a nanosecond.

The primary usage for time expressions is the specification of a custom query timeframe in the DQL query string:

```
fetch logs, from:-2h, to:-20m
```

**Functions and comparison**

```
...



| fields time = toTimestamp("2022-08-01T12:00:00+01:00")



| fieldsAdd time == now(), time > now()-10d, newTime = time + 3d
```

### Timeframe

A specific time frame with a start time and an end time as timestamps with nanosecond precision.
To execute the full query result including nanoseconds, change the visualization of the data in Notebooks to raw.

```
data record(tf = timeframe(from:now()-2h, to:now()))



| fields tf, tf[start], tf[end]
```

### Duration

A duration between two timestamps, consisting of an amount and a time unit.

```
...



| fields duration = 1s
```

**Time literals**

The following time literals can be used to express durations:

* `ns`: nanoseconds
* `ms`: milliseconds
* `s`: seconds
* `m`: minutes
* `h`: hours
* `d`: days[1](#fn-1-1-def)
* `w`: weeks
* `M`: months
* `q`: quarters
* `y`: years

1

When you use `d` in calculations, it is treated as a calendar day, otherwise it represents a duration of `24h`.

**Calendar durations**

You can use calendar durations (`d`, `w`, `M`, `q` and `y`) in calculations as shown in the example below, but not as field values.

```
fetch logs, from: now()-1M+2w
```

**Creating a duration**

In many cases, a parsed numeric value semantically represents a duration. The `duration()` function allows the creation of a field of type `duration` with the intended unit using the available time literals.

```
...



| fields     dur = 62



| fieldsAdd  dur_ms = duration(dur, unit:"ms")



| fieldsAdd  dur_ms > 50ms
```

**Converting to duration**

Converting a nanoseconds value to a `duration`:

```
...



...



| fields     dur = toDuration(62*1000000000*60*60*24)



| fieldsAdd  dur > 60d
```

Converting the period between timestamp1 and timestamp2 to a `duration`:

To illustrate, we calculate the age of the latest log message seen from a specific host.

```
...



...



fetch       logs



| filter    dt.entity.host == "HOST-DD5679D1A0C6426C"



| sort      timestamp desc



| limit     1



| fields    timestamp, age_message = now()-timestamp
```

### String

Sequence of characters with a specified character set.

* **Literal notation**  
  Enclose the string in double quotes. Escape double quote in the string with a backslash `\` if needed. A string can contain single quotes.  
  Optionally, you can enclose strings in triple quotes, such as """someString""".

  + Inside triple quotes, no escaping is necessary.
  + Triple quotes are not allowed as part of the string. In such a scenario, you can use the standard strings or the [concat](/docs/platform/grail/dynatrace-query-language/functions/string-functions#concat "A list of DQL string functions.") function.
* **Converting to String**  
  All DQL datatypes can be converted to a string:

  ```
  ...



  | fields toString(toBoolean(1)), toString(array(1,2,3)), toString(1), toString(toTimestamp(now())), toString(toIpAddress("192.168.0.1"))
  ```

### IpAddress

Represents an IPv4 or IPv6 address.

### UID

A data type that is used to represent 64-bit identifiers and 128-bit identifiers.

You can use the following DQL functions to create `UID` data:

* [uid64](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid64 "A list of DQL conversion and casting functions.")
* [uid128](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid128 "A list of DQL conversion and casting functions.")
* [toUid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toUid "A list of DQL conversion and casting functions.")

## Complex types

### Array

A data structure that contains a sequence of values, each identified by index.

* **Accessing array elements**

  ```
  ...



  | fieldsAdd int_array = array(1,2,2,3,4,5)



  | fields first_element = int_array[0], fifth_element = int_array[4]
  ```
* **Comparing arrays**  
  Only the equals operator `==` can be directly used on arrays.

  ```
  ...



  | ...



  | fields a=array(1,2), b=array(1,2,3), c=array("a","b"), d=toArray("c,d")



  | fields a == b, arraySize(b) > arraySize(c)
  ```

See the complete list of [DQL array functions](/docs/platform/grail/dynatrace-query-language/functions#array-functions "A list of DQL functions.") for further information.

### Record

A set of key-value pair data whose value can be any DQL data type.

* **Accessing RECORD Elements**  
  Data elements can be accessed by the key:

  ```
  ...



  | fields person = record({name="john", age=33, address=record({city="Atlanta", pcode="30308"})})



  | fields person[name], person[address][pcode]
  ```
* **Converting to RECORD**  
  The function `record(expression,...)` converts one or more expressions returning any data type to `RECORD`:

  ```
  ...



  | fields t = record(a=1+2,b=3,c=toString(timestamp))
  ```

  Parsing

  Parsing JSON or key-value pair strings results in `RECORD` data.

  ```
  STRUCTURE{matcher_expr, ...}:fieldname



  JSON{matcher_expr, ...}:fieldname



  KVP{matcher_expr, ...}:fieldname



  $subpattern:fieldname
  ```
* **Parsing Key-value pair data**

  ```
  ...



  | fields str = "name=\"john\"; age=33; city=\"Atlanta\""



  | parse str, "KVP{LD:key'='(LONG:valueLong | STRING:valueStr)'; '?}:person"



  | fields person[name], person[age], person[city]
  ```
* **Parsing JSON data**

  ```
  ...



  | fields str = "{\"type\":\"update\",\"host\":\"CI_preprod_1\",\"version\":\"10.2.2367\"}"



  | parse str,"JSON:event"



  | fields event[type], event[host], event[version]
  ```

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: dql-best-practices.md


---
title: DQL best practices
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-best-practices
scraped: 2026-02-17T04:57:09.282010
---

# DQL best practices

# DQL best practices

* Latest Dynatrace
* Reference
* Updated on Oct 13, 2025

This page describes actions you can take to improve query performance.

### Narrow the query time range

A shorter analysis window provides better performance based on identical data sets. Use available timeframe selectors provided by the user interface or directly specify the query time range within the [fetch command](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.").

```
fetch bizevents, from:-10m
```

### Utilize available sampling options

Grail samples incoming data on write and allows the selection of these partitions within the DQL [fetch command](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands."). Depending on the specified value, a fraction (`1/<samplingRatio>`) of all available raw records is returned.

The applicable value ranges for sampling are:

* 1: Default value, resulting in no applied sampling.
* 10
* 100
* 1000
* 10000

The following query uses sampling to improve query performance to observe an approximation of the number of spans per function invocation.

```
fetch spans, samplingRatio:100



| summarize c=count(), by: { span.kind, code.namespace, code.function }



| fieldsAdd c = c*100
```

### Further options to limit the scanned amount of data

The DQL [fetch command](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.") provides further options to limit data processing by

* stopping processing after a specified amount of data

```
fetch logs, scanLimitGBytes:100
```

* filtering on specific Grail Buckets

```
fetch logs, bucket:{"default_logs", "logs_365_*"}
```

### Recommended order of commands

Recommended order of commands

1. Reduce the number of processed records by filtering the data using, for example, the `filter` or `search` commands.

   * Try avoiding transformations like `| filter matchesValue(lower(k8s.namespace.name), "astro*")` and filter directly on the field such as: `| filter k8s.namespace.name ~ "astro*"`.
   * Try matching against words or phrases for text searches using `| filter content ~ "refused"`
   * Try to use inclusive filters and avoid negations such as `| filter not k8s.namespace.name ~ "astro*"`
   * Avoid `join` and `lookup` for filtering unless necessary. Filtering on enriched fields is suggested.
2. Select the amount of processed data by selecting fields early using the `fields`, `fieldsKeep`, or `fieldsRemove` commands.
3. Process the resulting dataset to achieve the required result set. Typically, non-transformative commands are used, such as `fieldsAdd`, `parse`, `append`.
4. Aggregate your data set using the `summarize` command to create a tabular result and `maketimeseries` if a time chart is required. Don't use `limit` before aggregating the data to prevent wrong aggregates unless intended.

**Example**

Applying the mentioned practices above leads to the following blueprint:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10



| filter loglevel=="ERROR" and k8s.namespace.name ~ "astroshop"



| filter content ~ "error"



| summarize c=count(), by:pod.name



| sort c desc



| limit 5
```

It is recommended to place `sort` at the end of the query. Sorting right after `fetch`, and continuing the query will reduce the query performance.

**Examples**

This example shows a query, where we put `sort` right after `fetch`.

It is recommended to place `sort` at the end of the query. Sorting right after `fetch` and then continuing the query will reduce the query performance. Example:

```
fetch logs



| sort timestamp desc



| filter content ~ "error"
```

This example shows the recommended order of putting `sort` at the end of the query.

```
fetch logs



| filter content ~ "error"



| sort timestamp desc
```

You can repeat the same command within one query and still stick to the recommended order. In the below example, you first filter the fetched content, then again you filter the parsed content, but the `sort` command and `summarize` function retain their positions:

```
fetch logs, bucket:{"astroshop_log_*"}, from:-1d@d, samplingRatio:10



| filter loglevel == "ERROR" and k8s.namespace.name ~ "astroshop"



| parse content, "ipaddr:ip ld ' POST ' ld:action ' HTTP/1.1 ' long:status ld"



| filter action == "/cart" or action == "/cart/checkout"



| summarize count = count(), by:{ ip, log.source }



| sort count desc
```

### Use string comparisons with care

* Use `==` or `!=` whenever the value of a field is known.

  ```
  fetch logs



  | filter k8s.container.name == "coredns"
  ```
* Use `~` whenever the value of a field is only partly known or unknown.

  ```
  fetch logs



  | filter k8s.container.name ~ "core*"
  ```

### Fields names to be avoided or used in backticks

It is not recommended to use the below eight reserved keywords as field identifiers (field names) or dimensions:

* true
* false
* null
* mod
* and
* or
* xor
* not

However, you can still use these words as field names, identifiers and dimensions if you put them in backticks ('`')

For example, if you have a dimension named 'true':

```
...



| fields x = true // creates a boolean field that is always true
```

```
...



| fields x = `true` // allows to access the custom dimension named 'true'
```

Similarly, if you need to sort by a field named 'not':

```
...



| sort not desc // sorts by a boolean value of dimension `desc`
```

```
...



| sort `not` desc // sorts descending by a field named `not`
```

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")


---


## Source: dql-comparison.md


---
title: DQL compared to SQL and more
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-comparison
scraped: 2026-02-17T04:54:57.011292
---

# DQL compared to SQL and more

# DQL compared to SQL and more

* Latest Dynatrace
* Reference
* Published Oct 17, 2022

This page compares the most common use cases between DQL and other well-established data query and processing languages like SQL, Splunk's SPL, and Microsoft's Kusto Query Language.

### Loading data for querying

#### Dynatrace Query Language (DQL)

```
fetch events
```

#### Structured Query Language (SQL)

```
SELECT * FROM events
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*
```

#### Kusto Query Language (KQL)

```
events
```

### Filtering

Narrows the number of records based on a filter expression. In this example, we are searching for payment events.

#### Dynatrace Query Language (DQL)

```
fetch events



| filter event.type == "travel.funnel.booking-payment"
```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment"
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event* | where event.type = "travel.funnel.booking-payment"
```

#### Kusto Query Language (KQL)

```
events



| where ['event.type'] == "travel.funnel.booking-payment"
```

We can add as many filters as needed to the pipeline. For example, we can look for bookings made by higher level loyalty customers traveling with children.

#### Dynatrace Query Language (DQL)

```
fetch events



| filter event.type == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0
```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*



| where event.type = "travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0
```

#### Kusto Query Language (KQL)

```
events



| where ['event.type'] == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0
```

### Field selection

Selecting just the relevant fields can be done in any pipeline stage. In this example, we will select only the product of successful bookings.

#### Dynatrace Query Language (DQL)

```
fetch events



| filter event.type == "travel.funnel.booking-payment"



| fields product
```

#### Structured Query Language (SQL)

```
SELECT product FROM events WHERE 'event.type'="travel.funnel.booking-payment"
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*



| where event.type = "travel.funnel.booking-payment"



| fields product
```

#### Kusto Query Language (KQL)

```
event



| where ['event.type'] == "travel.funnel.booking-payment"



| project product
```

### Calculations and sorting

We can transform the selected records in the pipelines. For example, we select the booked trips' duration in days and we will turn it into weeks.

#### Dynatrace Query Language (DQL)

```
fetch event



| filter event.type == "travel.funnel.booking-payment"



| fieldsAdd journeyWeeks = journeyDuration/7



| sort journeyWeeks desc
```

#### Structured Query Language (SQL)

```
SELECT journeyDuration/7 AS journeyWeeks FROM events WHERE 'event.type'="travel.funnel.booking-payment" ORDER BY journeyWeeks DESC
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*



| where event.type = "travel.funnel.booking-payment"



| eval journeyweeks = journeyDuration/7



| sort -journeyweeks
```

#### Kusto Query Language (KQL)

```
event



| where ['event.type'] == "travel.funnel.booking-payment"



| project journeyWeeks = journeyDuration/7



| sort journeyweeks desc
```

### Grouping

If we are interested only in unique values in our key, we can deduplicate the results by grouping them.

#### Dynatrace Query Language (DQL)

```
fetch events



| summarize count(), by:event.type



| fields event.type
```

#### Structured Query Language (SQL)

```
SELECT DISTINCT 'event.type' FROM events
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*



| stats count by event.type
```

#### Kusto Query Language (KQL)

```
events



| summarize by event.type
```

### Aggregation

After grouping selected records based on a field, we can aggregate the results to a new output.

#### Dynatrace Query Language (DQL)

```
fetch events



| filter event.type == "travel.funnel.booking-payment"



| summarize sum = sum(amount), by:travelAgency
```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum FROM events GROUP BY sum, travelAgency WHERE 'event.type' == "travel.funnel.booking-payment"
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*



| where event.type = "travel.funnel.booking-payment"



| stats sum(amount) as total_amount by travelAgency
```

#### Kusto Query Language (KQL)

```
event



| filter event.type == "travel.funnel.booking-payment"



| summarize sum = sum(amount) by travelAgency
```

Let's take a look at a bit more complex use case, where we want to add a new field, based on a mathematical expression, to our result table.

#### Dynatrace Query Language (DQL)

```
fetch events



| filter event.type == "travel.funnel.booking-payment"



| summarize sum = sum(amount), by:{travelAgency, travelers}



| fieldsAdd has_more_than_2 = travelers > 2
```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum, travelers > 2  AS has_more_than_2 FROM events  GROUP BY sum, has_more_than_2, travelAgency, travelers WHERE 'event.type' == "travel.funnel.booking-payment"
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*



| where event.type = "travel.funnel.booking-payment"



| stats sum(amount) as total_amount by travelAgency, travelers



| eval has_more_than_2 = travelers > 2
```

#### Kusto Query Language (KQL)

```
events



| where ['event.type'] == "travel.funnel.booking-payment"



| summarize sumBytes = sum(amount) by travelAgency, travelers



| project has_more_than_2 = travelers > 2
```

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: dql-guide.md


---
title: Use DQL queries
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-guide
scraped: 2026-02-17T04:55:02.853892
---

# Use DQL queries

# Use DQL queries

* Latest Dynatrace
* Reference
* Updated on Oct 05, 2023

The Dynatrace Query Language (DQL) introduces important concepts you should understand as you get started.

A DQL query is a read-only request to process data and return results. The request is stated in plain text, using a pipeline-based data-flow model that is easy to read, author, and automate.

## Chaining commands with the pipe operator

A DQL query contains at least one or more commands, each of which returns tabular output containing records (lines or rows) and fields (columns). All commands are sequenced by a | (pipe). The data flows or is funneled from one command to the next. The data is filtered or manipulated at each step and then streamed into the following step.

![Diagram showing how you can chain commands in DQL.](https://dt-cdn.net/images/dql-command-chain-1625-35b1bc0640.png)

After each operation, DQL returns a table or collection of tables containing data. The pipe operator funnels those tables into the next operation, where they're further processed or manipulated. This makes it easy to incrementally chain operations until the final, intended result is achieved.

Because the channeling of information from one operator to another is sequential, the query operator order is important and can affect both results and performance.

The best way to learn DQL is to start with some basic queries.

## Load data

The DQL `fetch` command defines which data to load from Dynatrace and optionally process in the following processing pipeline steps.

The `fetch` command requires a reference to the kind of data that should be retrieved by the initial processing pipeline. The following example uses logs.

```
fetch logs



| filter loglevel == "ERROR"



| summarize numErr = count()
```

The statement begins with loading (`fetch`) all ingested logs. Since no query timeframe was specified in the first stage, the time range specified in the Dynatrace user interface is applied. It contains three commandsâ`fetch`, `filter`, and `summarize`âeach separated by a pipe.

The log records are fed into the filter command, which reduces the number of output records based on the specified filter expression. The last line returns a table with one field and one record containing the count of remaining rows.

| **numErr** |
| --- |
| `34` |

You can also change the data type to `events` by using the `fetch` command and following it with `events`. The example query shows the sum value for the `amount` field in the events data set.

```
fetch events



| summarize Total_amount = sum(amount)
```

Total\_amount

`1,064,497`

## Specify timeframe

We suggest using the controls offered by the user interface to select your query time frame.

However, the DQL statement allows you to override the UI selection by using the `from` or `to` parameter to specify your intended time range.
Unless specified in the application or in the API, the default timeframe is 2 hours.

This example with relative time ranges queries logs from the last two hours:

```
fetch logs, from:now() - 2h
```

This example queries logs from the last 24 hours, excluding the last two hours:

```
fetch logs, from:now() - 24h, to:now() - 2h
```

You can also use absolute time ranges with the `timeframe` parameter:

```
fetch logs, timeframe:"2021-10-20T00:00:00Z/2021-10-28T12:00:00Z"
```

## Filter by Boolean expression

Narrow down the requested records with `filter`. Use operators like `==` or `!=` to include or exclude fields with specific values. Functions like `endsWith` or `contains` let you include fields that end with or contain a specific string.

```
fetch logs, from:now() - 2h



| filter loglevel == "SEVERE" or loglevel == "ERROR" and not endsWith(log.source,"audit.log")
```

## Select a subset of fields

```
fetch logs



| fields timestamp, loglevel, log.source, content
```

## Order results with sort

By default, the sort command sorts records in ascending order. In the following example, we sort results in descending order.

```
fetch logs



| filter loglevel == "SEVERE" or loglevel == "ERROR"



| fields timestamp, loglevel, dt.process.name, host.name, content



| limit 5



| sort timestamp desc
```

## Aggregations

This example calculates the number of `booking.process.started` events. Intentionally only business days and hours (Mon-Fri, 8:00 AM to 5:00 PM) are accepted by the aggregation.

```
fetch bizevents



| filter event.type=="booking.process.started"



| fieldsAdd hour=formatTimestamp(timestamp,format:"hh"), day_of_week=formatTimestamp(timestamp,format:"EE")



| filterOut (day_of_week  == "Sat" or day_of_week == "Sun") or (toLong(hour) <= 08 or toLong(hour) >= 17)



| summarize numStarts = count(), by:{product}
```

## Aggregations over time

DQL provides dedicated commands such as [makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to aggregate a list of raw event records into a chartable timeseries. Let's observe the logs grouped by the log level and a 5-minute aggregation interval:

```
fetch logs



| filter loglevel == "SEVERE" or loglevel == "ERROR"



| makeTimeseries count = count(), by:loglevel, interval:5m
```

## Learn DQL App

You can learn DQL through hands-on experience with interactive tutorials in the Learn DQL App. You can use the app, if you are a customer with access to Dynatrace SaaS environment or if you are a registered member of the Dynatrace Community. You can also sign up for a 15 day free trial to try out the app. To find out more about the Learn DQL app see the [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/learn-dql/?query=learn+dql&filter=all). To access the app visit [Discover Dynatraceï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.learndql/).

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: dql-reference.md


---
title: DQL language reference
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-reference
scraped: 2026-02-17T04:55:06.377792
---

# DQL language reference

# DQL language reference

* Latest Dynatrace
* Reference
* Updated on Nov 06, 2025

A DQL query contains at least one or more [commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands."), each of which returns tabular output containing records (lines or rows) and fields (columns). All commands are sequenced by a | (pipe). Data flows or is piped from one command to the next. The data is filtered or manipulated at each step and then streamed into the following step.

## DQL Syntax

The syntax can be described as follows:

`command parameter,.. [, optionalparameter],... | command â¦`

A syntactically valid example of a DQL query is:

```
fetch bizevents | summarize count()
```

A DQL command consists of mandatory and optional parameters which are comma-separated:

`summarize [field=] aggregation [, ...] [, by:{ [field=] groupexpression [, ...]}]`

* Mandatory parameters

  + aggregation
* Optional parameters

  + field
  + groupexpression

The required parameter is `aggregation`. For this command to be syntactically valid, at least one call to an [aggregation function](/docs/platform/grail/dynatrace-query-language/functions#aggregation-functions "A list of DQL functions.") has to be specified.

```
| summarize count()
```

Optionally, an assignment by using the equals sign `(=)` overrides the default field name from `count()` to `event_count`.

```
| summarize event_count = count()
```

The optional `by:` parameter defines a list of `groupexpression`. The output will have as many records as there are distinct values of all the `groupexpression`.

```
| summarize event_count = count(), by:{country=client.loc_cc, customer}
```

## Field naming rules

DQL Syntax verification applies the following naming rules:

![An example of a DQL query showing demonstrating the use of a command,  parameters and field identifiers.](https://dt-cdn.net/images/dql-ref-2418-19b3237798.png)

* Field names can use any sequence of Unicode characters.
* Field names using any character other than `a-zA-Z0-9_.` must be enclosed in backticks.
* Field names starting with any character other than `a-zA-Z_` must be enclosed in backticks.
* Backslash `\` is used as escape character.
* You need to escape backticks and backslashes in the field name.

Examples of valid field names are:

* `dt.entity.host`
* `location_US_EAST_1`
* `` `my host*` `` â must be enclosed in backticks
* `` `LOCAL_MACHINE\\Software` `` â uses a single backslash in the field name

## Parameters

Parameters for commands or functions have to be separated with a comma. Optional parameters need to be named.

Parameters can be:

* a value or an expression (for example: `now()-1h`)
* an execution block (for example: `[fetch logs]`). The execution block holds a sub-query.
* a group of parameters (see below)

### Parameter groups

If several parameters, either mandatory or optional, belong together, you should group them with curly braces (`{}`). This is especially important if the group is named. Using curly braces doesn't affect the data type. If you choose to group your parameters, you won't be able to use [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") with them.

The below example shows two groups of parameters. The first group holds the aggregations (not named), while the second group holds the fields by which to summarize (`by:`).

```
| summarize {min(value), max(value)}, by:{field1, field2}
```

## Sequential data processing

The following DQL query uses seven pipeline steps to get from raw log data to an aggregated table showing performance statistics for task execution.

![An example of a DQL query showing demonstrating the use of a command, a function, parameters and an expression.](https://dt-cdn.net/images/new-dql-query-3-1763-7b83cbcf34.png)

* **Line 1**

  ```
  fetch       logs, from:now()-10m
  ```

  You retrieve the log data using the [`fetch`](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands") command. In addition, the optional `from:` parameter specifies the query start timestamp.
* **Line 2**

  ```
  // fetched all logs from the last hour: now() â 1h to now()
  ```

  Commented out line. This line will be omitted in query execution.
* **Line 3**

  ```
  | filter    endsWith(log.source, "pgi.log")
  ```

  The [`filter`](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") command filters the log records based on the [`endsWith`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#endsWith "A list of DQL string functions.") function that retrieves log files whose names end with the predefined string (the `pgi.log` string).
* **Line 4**

  ```
  | parse     content, "LD IPADDR:ip ':' LONG:payload SPACE LD 'HTTP_STATUS' SPACE INT:http_status  LD (EOL| EOS)"
  ```

  We use the [`parse`](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands#parse "DQL extraction commands") command to extract key-value pairs containing execution statistics out of the raw log text string. In this case, it adds the `IP address`, `payload` and `http_status` fields to the result and transforms their data types into required formats.
* **Line 5, 6, 7, 8**

  ```
  | summarize total_payload = sum(payload),



  failedRequests = countIf(http_status >= 400),



  successfulRequests = countIf(http_status < 400),



  by:{ip, host.name}
  ```

  The [`summarize`](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") command is a key element of DQL as it allows multiple aggregations across one or more fields. This query groups the results by `ip` and `host.name`. The retrieved records include the total value of payload, calculated using the [`sum`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum "A list of DQL aggregation functions.") function, and two columns calculated using the [`countif`](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countIf "A list of DQL aggregation functions.") function:

  + a column with numbers of failed requests (defined as those having `http_status` >=400)
  + a column with numbers of successful requests (defined as those having `http_status` <400)  
    This query groups the retrieved records by `ip` and `host.name`.
* **Line 9**

  ```
  |fieldsAdd total_payload_MB = total_payload/1000000
  ```

  With the [`fieldsAdd`](/docs/platform/grail/dynatrace-query-language/commands#fields-add "A list of DQL commands.") command, you add a new field showing the total payload converted into megabytes, basing on a mathematical expression.
* **Line 10**

  ```
  |fields    ip, host.name, failedRequests, successfulRequests, total_payload_MB
  ```

  With the [`fields`](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands") command, you can determine which fields you need to retrieve.
* **Line 11**

  ```
  | sort  failedRequests desc
  ```

  The [`sort`](/docs/platform/grail/dynatrace-query-language/commands/ordering-commands#sort "DQL ordering commands") command is used to finalize the result. In this case, the results are sorted according to the number of failed requests, from the highest to lowest.

## DQL key building blocks

* [Commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [Functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")  
  Functions can be used to perform any desired computation on fields of [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.").

* [Data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")  
  The Dynatrace Query Language operates with strongly typed data: functions and operators accept only declared types of data. The type is assigned to data during parsing or by using casting functions. DQL also recognizes value types expressed in literal notation (for example, using constant values in functions).

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: dql-use-cases.md


---
title: DQL use cases
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-use-cases
scraped: 2026-02-17T04:56:43.523162
---

# DQL use cases

# DQL use cases

* Latest Dynatrace
* Reference
* Published Jan 16, 2023

The following use cases show some of the ways you can use Dynatrace Query Language to leverage data ingested into Grail.

### Parse JSON data and aggregate records

In this use case, let's assume that you need to check how many transactions were conducted by each payment service provider, and the share of each provider in the total number of transactions.

The content field for every record looks as below:

```
{



"country_code":"US",



"session_id":"6a6c6b6d6a7c7b7f7a7c7b7a7f7",



"invoicing_data":null,



"bill_to":{



"first_name":"John",



"last_name":"Doe",



"email":"john.doe@gmail.com",



"phone":null



},



"payment_provider":"paypal"



}
```

You can use the `parse` command in combination with the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") for parsing JSON objects. The query parses the `payment_provider` field from the JSON data and groups the number of transactions by each provider using the `summarize` command, as well as calculates the total count of transactions. The share is calculated in a separate column, next to each provider's number of transactions.

```
fetch logs



| parse content, "JSON:json"



| fields payment = json[payment_provider]



| summarize



bank_card=countIf(payment=="bank_card"), bank_cardPer=toDouble(countIf(payment=="bank_card"))/toDouble(count()),



apple_pay=countIf(payment=="apple_pay"),apple_payPerc=toDouble(countIf(payment=="apple_pay"))/toDouble(count()),



paypal=countIf(payment=="paypal"),paypalPerc=toDouble(countIf(payment=="paypal"))/toDouble(count()),



google_pay=countIf(payment=="google_pay"),google_payPerc=toDouble(countIf(payment=="google_pay"))/toDouble(count()),



unpaid_booking=countIf(payment=="unpaid_booking"),unpaid_bookingPerc=toDouble(countIf(payment=="unpaid_booking"))/toDouble(count()),



total=count()
```

Results:

bank\_card

bank\_cardPer

apple\_pay

apple\_payPerc

paypal

paypalPerc

google\_pay

google\_payPerc

unpaid\_booking

unpaid\_bookingPerc

total

345

0.19425675675675674

353

0.19876126126126126

360

0.20270270270270271

364

0.20495495495495494

354

0.19932432432432431

1776

### Extract the first 'n' characters from the field.

In this example, you have a field called `kiosk` and need to extract the first three characters to identify the location abbreviation of the kiosk.

```
{



"kiosk": "LAOBAUA729"



}
```

```
...



| parse kiosk, "DATA{3}:kioskLoc"



| fields kiosk, kioskLoc
```

Results:

kiosk

kioskLoc

LAOBAUA729

LAO

### Extract information from an XML element

In this use case, an API gateway creates logs in XML format and you want to extract some information from it.

The XML field for every record looks as below:

```
<log-entry serial='1467' domain='bca_icas_soa'>



<date>Fri Sep 21 2023</date>



<time utc='1380295304719'>11:21:44</time>



<date-time>2012-09-21T11:21:44</date-time>



<type>xmlfirewall</type>



<class>xmlfirewall</class>



<object>example-Firewall</object>



<level num='3'>error</level>



<transaction-type>error</transaction-type>



<transaction>6187</transaction>



<client>127.0.0.1</client>



<code>0x01130007</code>



<file></file>



<message>Failed to establish backend connection</message>



</log-entry>
```

In the DQL query, you need to use the [DPL matcher](/docs/platform/grail/dynatrace-pattern-language/dpl-xml "Find out how to use XML matchers with DPL.") to extract the whole XML element:

```
...



| parse content, "XML(excludeRoot=true):xml"



| fields domain = xml[`@domain`],



serial = toLong(xml[`@serial`]),



object = xml[object],



transaction = xml[transaction],



code = xml[code]
```

Results:

domain

serial

object

transaction

code

bca\_icas\_soa

1467

example-Firewall

6187

0x01130007

### Investigate security incidents in Kubernetes clusters Threat hunting

Application Security

In this use case, you perform queries using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze unauthorized requests in your Kubernetes audit logs. Follow different investigation paths, navigate between executed queries, and get a detailed overview of your results in the original format.

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")


---


## Source: string-functions.md


---
title: String functions
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/string-functions
scraped: 2026-02-16T21:13:36.221322
---

# String functions

# String functions

* Latest Dynatrace
* Reference
* Updated on Jan 29, 2026

String functions allow you to create expressions that manipulate text strings in a variety of ways.

Case sensitivity

All string matching functions are case-sensitive per default. If otherwise required, the `caseSensitive` parameter provides the ability to change the behavior.

```
...



| fieldsAdd str_found = contains(content, "FlushCommand", caseSensitive:false)
```

## concat

Concatenates the expressions into a single string.

#### Syntax

`concat(expression, â¦ [, delimiter: ])`

#### Parameters

Parameter

Type

Description

Required

expression

double, long, string

A numeric or string expressions that should be concatenated with others.

Required

delimiter

string

Constant string to be inserted between each concatenated value. Default: `""` (empty string).

Optional

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(a = "DQL", b = "is", c = "awesome!")



| fieldsAdd concat(a, b, c, delimiter: " ")
```

Run in Playground

Query result:

a

b

c

concat(a, b, c, delimiter: " ")

`DQL`

`is`

`awesome!`

`DQL is awesome!`

## contains

Searches the string expression for a substring. Returns `true` if the substring was found, `false` otherwise.

#### Syntax

`contains(expression, substring [, caseSensitive])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The field or expression to check.

Required

substring

string

The substring that should be contained.

Required

caseSensitive

boolean

Whether the search should be done in a case-sensitive way. The default value is `true`.

Optional

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd contains(content, "DQL"),



contains(content, "dql", caseSensitive: false),



contains(content, "Query")
```

Run in Playground

Query result:

content

contains(content, "DQL")

contains(content, "dql", caseSensitive:FALSE)

contains(content, "Query")

`DQL is awesome!`

`true`

`true`

`false`

`Dynatrace Query Language`

`false`

`false`

`true`

## decodeUrl

Returns a URL-decoded string.

#### Syntax

`decodeUrl(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression that will be decoded.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail"),



record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd decodeUrl(content)
```

Run in Playground

Query result:

content

decodeUrl(content)

`https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail`

`https://www.dynatrace.com/platform/grail`

`https://www.dynatrace.com/platform/grail`

`https://www.dynatrace.com/platform/grail`

## encodeUrl

Encodes a URL string by replacing characters that aren't numbers or letters with percentage symbols and hexadecimal numbers.

#### Syntax

`encodeUrl(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression that will be encoded.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "https://www.dynatrace.com/platform/grail")



| fieldsAdd encodeUrl(content)
```

Run in Playground

Query result:

content

encodeUrl(content)

`https://www.dynatrace.com/platform/grail`

`https%3A%2F%2Fwww.dynatrace.com%2Fplatform%2Fgrail`

## endsWith

Checks if a string expression ends with a suffix. Returns `true` if does, `false` otherwise.

#### Syntax

`endsWith(expression, suffix [, caseSensitive])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression that will be checked.

Required

suffix

string

The suffix string with which the expression should end.

Required

caseSensitive

boolean

Whether the check should be done in a case-sensitive way.

Optional

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd endsWith(content, "awesome!"),



endsWith(content, "AWESOME!", caseSensitive: false),



endsWith(content, "Language")
```

Run in Playground

Query result:

content

endsWith(content, "awesome!")

endsWith(content, "AWESOME!", caseSensitive:FALSE)

endsWith(content, "Language")

`DQL is awesome!`

`true`

`true`

`false`

`Dynatrace Query Language`

`false`

`false`

`true`

## escape

Returns an escaped string.

Escaping rules

1. Single and double quotes are escaped. Backticks are not escaped.

Input

Output

`"`

`\"`

`'`

`\'`

2. Backslashes are escaped.

Input

Output

`\`

`\\`

3. ASCII characters backspace, form feed, new line, carriage return, horizontal tabs are escaped.

Input

Output

`<backspace>`

`\b`

`<form feed>`

`\f`

`<new line>`

`\n`

`<carriage return>`

`\r`

`<horizontal tab>`

`\t`

4. ASCII characters within the range 0x20 - 0x7e (printable ASCII characters), that are not covered by any of the above rules, stay as they are.

Input

Output

`a`

`a`

`1`

`1`

5. All other ASCII characters are represented as `\xhh`. This applies to the following characters

   * characters within the range 0x00 - 0x07
   * character 0x0b (vertical tab)
   * characters within the range 0x0e - 0x1f
   * character 0x7f

Input

Output

`<vertical tab>`

`\x0b`

6. All characters in extended ASCII space (0x80-0xff) and Unicode characters outside of the ASCII space are represented as `\uhhhh`.

Input

Output

`Ã¶`

`\u00f6`

#### Syntax

`escape(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string expression

The string expression that will be escaped.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo@bar.com""")



| fieldsAdd escape(content)
```

Run in Playground

Query result:

| content | escape(content) |
| --- | --- |
| `"foo@bar.com` | `\"foo@bar.com` |

## getCharacter

Returns the character at a given position from a string expression. Negative values for the position parameter are counted from the end of the string. If a position refers to a position outside the string, the function returns NULL.

#### Syntax

`getCharacter(expression, position)`

#### Parameters

Parameter

Type

Description

Required

expression

string

Required

position

long

The position at which to get the character.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd getCharacter(content, 1),



getCharacter(content, 17),



getCharacter(content, -1)
```

Run in Playground

Query result:

content

getCharacter(content, 1)

getCharacter(content, 17)

getCharacter(content, -1)

`DQL is awesome!`

`Q`

*null*

`!`

`Dynatrace Query Language`

`y`

`a`

`e`

## indexOf

Returns the index of the first occurrence of a substring in a string expression.
Starts to search forward from a given index. Negative values for the `from` parameter are counted from the end of the string.
The default value for `from` is `0` (the search from the start of the string).
The search is case-sensitive.
If the defined substring is not found, the function returns `-1`.

#### Syntax

`indexOf(expression, substring [, from])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression in which the substring is searched for.

Required

substring

string

The substring expression to search for in the expression.

Required

from

long

The index from which to start the forward search for the first occurrence of the substring within the expression. Negative values are counted from the end of the string.

Optional

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd indexOf(content, "a"),



indexOf(content, "a", from: 10),



indexOf(content, "Query")
```

Run in Playground

Query result:

content

indexOf(content, "a")

indexOf(content, "a", from:10)

indexOf(content, "Query")

`DQL is awesome!`

`7`

`-1`

`-1`

`Dynatrace Query Language`

`3`

`17`

`10`

## jsonField

Parses a JSON string and extracts one value selected by its name.

#### Syntax

`jsonField(expression, fieldName [, seek])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The JSON string that should be parsed.

Required

fieldName

string

The string literal with the key to be extracted.

Required

seek

boolean

Flag indicating if the function should search for the first valid JSON object in the expression. The default value is `false`.

Optional

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{



"name":"John",



"children":["Mallory", "Mary"],



"address":{"city":"Boston", "zip":"02210"}



}""")



| fieldsAdd jsonField(content, "name")
```

Run in Playground

Query result:

content

jsonField(content, "name")

`{"name":"John", "children":["Mallory", "Mary"], "address":{"city":"Boston", "zip":"02210"}}`

`John`

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonField(content, "name", seek:false)



| fieldsAdd jsonField(content, "name", seek:true)
```

Run in Playground

Query result:

content

jsonField(content, "name", seek:FALSE)

jsonField(content, "name", seek:TRUE)

`JSON: {"name": "John"} ...`

`null`

`John`

## jsonPath

Parses a JSON string and extracts one value selected by a JSONPath expression.

#### Syntax

`jsonPath(expression, jsonPath [, seek])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The JSON string that should be parsed.

Required

jsonPath

string

The string literal with the JSONPath expression of the value to be extracted.

Required

seek

boolean

Flag indicating if the function should search for the first valid JSON object in the expression. The default value is `false`.

Optional

#### Returns

The data type of the returned value is `long`, `double`, `boolean`, `string`, `array` or `record`.

#### Examples

##### Example 1

```
data record(content = """{



"name":"John",



"children":["Mallory", "Mary"],



"address":{"city":"Boston", "zip":"02210"}



}""")



| fieldsAdd jsonPath(content, "$.children[0]")



| fieldsAdd jsonPath(content, "$.address.city")



| fieldsAdd jsonPath(content, "$['address']['zip']")
```

Run in Playground

Query result:

content

jsonPath(content, "$.children[0]")

jsonPath(content, "$.address.city")

jsonPath(content, "$['address']['zip']")

`{"name":"John", "children":["Mallory", "Mary"], "address":{"city":"Boston", "zip":"02210"}}`

`Mallory`

`Boston`

`02210`

##### Example 2

```
data record(content = """JSON: {"name": "John"} ...""")



| fieldsAdd jsonPath(content, "$.name", seek:false)



| fieldsAdd jsonPath(content, "$.name", seek:true)
```

Run in Playground

Query result:

content

jsonPath(content, "$.name", seek:FALSE)

jsonPath(content, "$.name", seek:TRUE)

`JSON: {"name": "John"} ...`

`null`

`John`

## lastIndexOf

Returns the index of the last occurrence of a substring in a string expression. Starts to search backward from a given index. Negative values for the from parameter are counted from the end of the string. The default value for from is -1 (search from the end of the string). The search is case-sensitive. If the substring is not found, the function returns `-1`.

#### Syntax

`lastIndexOf(expression, substring [, from])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression in which the substring is searched for.

Required

substring

string

The substring expression to search for in the expression.

Required

from

long

Optional

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lastIndexOf(content, "a"),



lastIndexOf(content, "a", from: 10),



lastIndexOf(content, "Query")
```

Run in Playground

Query result:

content

lastIndexOf(content, "a")

lastIndexOf(content, "a", from:10)

lastIndexOf(content, "Query")

`DQL is awesome!`

`7`

`7`

`-1`

`Dynatrace Query Language`

`21`

`6`

`10`

## levenshteinDistance

Computes the Levenshtein distance between two input strings.

#### Syntax

`levenshteinDistance(expression, expression)`

#### Parameters

Parameter

Type

Description

Required

first expression

string

The first string expression to compute the Levenshtein distance from.

Required

second

string

The second string expression to compute the Levenshtein distance from.

Required

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(a = "DQL is awesome!", b = "Grail is awesome!"),



record(a = "Dynatrace Query Language", b = "DQL"),



record(a = "Dynatrace Query Language", b = "dynatrace query language")



| fieldsAdd levenshteinDistance(a, b)
```

Run in Playground

Query result:

a

b

levenshteinDistance(a, b)

`DQL is awesome!`

`Grail is awesome!`

`5`

`Dynatrace Query Language`

`DQL`

`21`

`Dynatrace Query Language`

`dynatrace query language`

`3`

## like

Tests if a string expression matches a pattern. If the pattern does not contain percent signs, `like()` acts as the `==` operator (equality check). A percent character in the pattern `(%)` matches any sequence of zero or more characters. An underscore in the pattern `(\_)` matches a single character.

#### Syntax

`like(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

Required

pattern

string

Required

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd like(content, "%DQL%"),



like(content, "D%L%"),



like(content, "D_L%")
```

Run in Playground

Query result:

content

like(content, "%DQL%")

like(content, "D%L%")

like(content, "D\_L%")

`DQL is awesome!`

`true`

`true`

`true`

`Dynatrace Query Language`

`false`

`true`

`false`

## lower

Converts a string to lowercase.

#### Syntax

`lower(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to convert to lowercase.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd lower(content)
```

Run in Playground

Query result:

content

lower(content)

`DQL is awesome!`

`dql is awesome!`

`Dynatrace Query Language`

`dynatrace query language`

## matchesPattern

Tests if a string expression matches the DPL pattern and returns `true` if it does, otherwise, returns `false`.

#### Syntax

`matchesPattern(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

A field or string expression to test.

Required

pattern

string

The matching pattern.

Required

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "2023-11-01 12:52:12 : 766"),



record(content = "2023-11-01 12:53:00:123"),



record(content = "2023-11-01 12:55:59 : 192.168.0.1")



| fieldsAdd matchesPattern(content, "TIME ' : ' LONG"),



matchesPattern(content, "TIME ' : ' IP")
```

Run in Playground

Query result:

| content | matchesPattern(content, "TIME ' : ' LONG") | matchesPattern(content, "TIME ' : ' IP") |
| --- | --- | --- |
| `2023-11-01 12:52:12 : 766` | `true` | `false` |
| `2023-11-01 12:53:00:123` | `false` | `false` |
| `2023-11-01 12:55:59 : 192.168.0.1` | `false` | `true` |

## matchesPhrase

Matches a phrase against the input string expression using token matchers.

#### Syntax

`matchesPhrase(expression, phrase [, caseSensitive])`

#### Parameters

Parameter

Type

Description

Required

expression

string, array

The expression (string or array of strings) that should be checked.

Required

phrase

string

The phrase to search for.

Required

caseSensitive

boolean

Whether the match should be done case-sensitive. Default: `false`.

Optional

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = array("DQL", "is", "awesome", "!", "Dynatrace Query Language"))



| fieldsAdd matchesPhrase(content, "DQL"),



matchesPhrase(content, "Dyna"),



matchesPhrase(content, "query"),



matchesPhrase(content, "query", caseSensitive: true)
```

Run in Playground

Query result:

content

matchesPhrase(content, "DQL")

matchesPhrase(content, "Dyna")

matchesPhrase(content, "query")

matchesPhrase(content, "query", caseSensitive:TRUE)

`DQL is awesome!`

`true`

`false`

`false`

`false`

`Dynatrace Query Language`

`false`

`false`

`true`

`false`

`[DQL, is, awesome, !, Dynatrace Query Language]`

`true`

`false`

`true`

`false`

## matchesValue

Searches records for a specific value in a given attribute. Returns `true` or `false`.

#### Syntax

`matchesValue(expression, value, â¦ [, caseSensitive])`

#### Parameters

Parameter

Type

Description

Required

expression

string, array

The expression (string or array of strings) that should be checked.

Required

value

string, array

The value to search for using patterns (supports an array of patterns or a list of patterns).

Required

caseSensitive

boolean

Whether the match should be done case-sensitive. Default: `false`.

Optional

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

Values are matched case-insensitive by default:

```
data record(content = "User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "User*"),



matchesValue(content, "user*"),



matchesValue(content, "user*", caseSensitive: true)
```

Run in Playground

Query result:

content

matchesValue(content, "User\*")

matchesValue(content, "user\*")

matchesValue(content, "user\*", caseSensitive:TRUE)

`User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1`

`true`

`true`

`false`

##### Example 2

Values are matched from the beginning. To match parts of the value, use `*` as wildcard symbol:

```
data record(content = "User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1")



| fieldsAdd matchesValue(content, "192.168.0.1"),



matchesValue(content, "*192.168.0.1"),



matchesValue(content, "*failed to log*")
```

Run in Playground

Query result:

content

matchesValue(content, "192.168.0.1")

matchesValue(content, "\*192.168.0.1")

matchesValue(content, "\*failed to log\*")

`User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1`

`false`

`true`

`true`

##### Example 3

Only ASCII characters are matched case-insensitive:

```
data record(content = "Ãsterreich")



| fieldsAdd matchesValue(content, "Ã¶sterreich"),



matchesValue(content, "Ãsterreich")
```

Run in Playground

Query result:

content

matchesValue(content, "Ã¶sterreich")

matchesValue(content, "Ãsterreich")

`Ãsterreich`

`false`

`true`

##### Example 4

The function handles values of arrays in "any-match" manner.

```
data record(technologies = array("Java11", "java17"))



| fieldsAdd matchesValue(technologies, "Java11"),



matchesValue(technologies, "java"),



matchesValue(technologies, "java*")
```

Run in Playground

Query result:

technologies

matchesValue(technologies, "Java11")

matchesValue(technologies, "java")

matchesValue(technologies, "java\*")

`[Java11, java17]`

`true`

`false`

`true`

#### Multi-pattern comparison

The `matchesValue()` function supports matching against multiple patterns. You can use it by either providing an array or a list of patterns with the `value` parameter. Only strings are supported as patterns. Other datatypes don't produce a match and are ignored. The `matchesValue()` function returns true if any of the patterns matches. In case none of the patterns produce a match, `false` is returned.

#### Example

```
data record(content = array("DQL", "is", "awesome", "!"))



| fieldsAdd matchesValue(content, array("Grail", "dql")),



matchesValue(content, {"Grail", "dql"}),



matchesValue(content, {"Grail", "dq*"}),



matchesValue(content, {"Grail", "dq*"}, caseSensitive: true)
```

Run in Playground

Query result:

content

matchesValue(content, array("Grail", "dql"))

matchesValue(content, {"Grail", "dql"})

matchesValue(content, {"Grail", "dq\*"})

matchesValue(caseSensitive:TRUE, content, {"Grail", "dq\*"})

`DQL, is, awesome, !`

`true`

`true`

`true`

`false`

## parse

Extracts a single value from a string as specified in the pattern or a record if there are multiple named matchers.

#### Syntax

`parse(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

A field or string expression to parse.

Required

pattern

string

The parse pattern. Must conform with patterns (see [DPL](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")).

Required

#### Returns

The `parse` function returns a single value, which can be either of primitive type or a record. The result is of primitive type in case of a single named matcher in the DPL pattern. If there are multiple named matchers in the pattern, then the result is a record containing fields corresponding to the names of the matchers.
Fields created from the output of the `parse` function by default get the name of the named matcher in the DPL pattern. In case of multiple named matchers in the pattern, the default field name is `parsed_record`. You can also define alternative field names using an alias expression.

#### Examples

##### Example 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parse(src, "LONG:result"),



value = parse(src, "LONG:result"),



parse(src, "LONG:field1 ' ' LONG:field2")
```

Run in Playground

Query result:

| src | result | value | parsed\_record |
| --- | --- | --- | --- |
| `1 2` | `1` | `1` | **field1**: `1` **field2**: `2` |
| `45 46 47 48` | `45` | `45` | **field1**: `45` **field2**: `46` |

## parseAll

Extracts several values from a string as specified in the pattern.
Unlike the [`parse`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parse "A list of DQL string functions.") function, `parseAll` returns an array all the time. The array can be empty if no patterns matched. A single element can be primitive type or a record.

#### Syntax

`parseAll(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

A field or string expression to parse.

Required

pattern

string

The parse pattern. Must conform with [DPL patterns](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.").

Required

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(src = "1 2"),



record(src = "45 46 47 48")



| fieldsAdd parseAll(src, "LONG:result"),



value = parseAll(src, "LONG:result"),



parseAll(src, "LONG:field1 ' ' LONG:field2")
```

Run in Playground

Query result:

| src | result | value | parsed\_records |
| --- | --- | --- | --- |
| `1 2` | `[1, 2]` | `[1, 2]` | [**field1:** `1` **field2** `2`] |
| `45 46 47 48` | `[45, 46, 47, 48]` | `[45, 46, 47, 48]` | [**field1:** `45` **field2** `46`, **field1:** `47` **field2** `48`] |

## punctuation

Extracts punctuation characters out of an input string.

#### Syntax

`punctuation(expression, [, count] [, withSpace])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression from which the punctuation characters are extracted.

Required

count

positive integer

The maximum number of returned punctuation characters. Default: `32`.

Optional

withSpace

boolean

Whether space characters should be included. Default: `false`.

Optional

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

In this example, we extract the punctuation characters from each input string.

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "${placeholder}")



| fieldsAdd punctuation(content),



punctuation(content, count: 2),



punctuation(content, count: 2, withSpace: true)
```

Run in Playground

Query result:

content

punctuation(content)

punctuation(content, count:2)

punctuation(content, count:2, withSpace:TRUE)

`DQL is awesome!`

`!`

`!`

`__`

`Dynatrace Query Language`

*empty string*

*empty string*

`__`

`${placeholder}`

`${}`

`${`

`${`

## replacePattern

Replaces each substring of a string that matches the DPL pattern with the given string. The pattern must be defined as a constant string expression. For additional details about pattern syntax, see the [DPL documentation](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.").

#### Syntax

`replacePattern(expression, pattern, replacement)`

#### Parameters

Parameter

Type

Description

Required

expression

string

A field or string expression to replace.

Required

pattern

string

The replacing pattern.

Required

replacement

string

The string that should replace the found substrings.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL 2019-08-01 09:30:00"),



record(content = "Dynatrace Query L4nguage")



| fieldsAdd replacePattern(content, "TIME", "is awesome!"),



replacePattern(content, "LONG", "a")
```

Run in Playground

Query result:

| content | replacePattern(content, "TIME", "is awsome!") | replacePattern(content, "LONG", "a") |
| --- | --- | --- |
| `DQL 2019-08-01 09:30:00` | `DQL is awesome!` | `DQL aaa a:a:a` |
| `Dynatrace Query L4nguage` | `Dynatrace Query L4nguage` | `Dynatrace Query Language` |

## replaceString

Replaces each substring of a string with a given string. This function replaces only exactly matched substrings from the original string to the replacement. Matching is case-sensitive and doesn't use any wildcards. All found patterns will be replaced if they do not intersect. For instance, replacing `abcabca` in a string with `abca` pattern produces only one replacement. Only the first occurrence at the beginning of the string will be replaced.

#### Syntax

`replaceString(expression, substring, replacement)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The field or expression where substrings should be replaced.

Required

substring

string

The substring that should be replaced.

Required

replacement

string

The string that should replace the found substrings.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "abcabca")



| fieldsAdd replaceString(content, "awesome", "simple"),



replaceString(content, "abca", "xyz")
```

Run in Playground

Query result:

content

replaceString(content, "awesome", "simple")

replaceString(content, "abca", "xyz")

`DQL is awesome!`

`DQL is simple!`

`DQL is awesome!`

`Dynatrace Query Language`

`Dynatrace Query Language`

`Dynatrace Query Language`

`abcabca`

`abcabca`

`xyzbca`

## splitByPattern

Splits a string into an array at each occurrence of the DPL pattern.

#### Syntax

`splitByPattern(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

A field or string expression to split.

Required

pattern

string

The splitting pattern. Must conform with [DPL patterns](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.").

Required

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "one $1 two $4 three"),



record(content = "foo $1000 bar"),



record(content = "no separator"),



record(content = "")



| fieldsAdd splitByPattern(content, " ' $' LONG ' ' ")
```

Run in Playground

Query result:

| content | splitByPattern(content, " ' $' LONG ' ' ") |
| --- | --- |
| `one $1 two $4 three` | `[one, two, three]` |
| `foo $1000 bar` | `[foo, bar]` |
| `no separator` | `[no separator]` |
| *empty string* | `[]` |

## splitString

Splits a string according to the parameters set.  
Retrieves an array of substrings of the specified expression that are adjacent to occurrences of the given pattern.  
Parameters are interpreted literally. For example, splitting `www.dynatrace.org` by `.` results in `www` and `dynatrace` and `org`.  
Using an empty string as a pattern splits the string into one-byte substrings. For example, a split of four characters becomes an array of four strings having one byte each (splitting the `"1234"` expression results in `array("1", "2", "3", "4")`).

The non-ASCII characters are represented by multiple bytes. Splitting a string containing such characters by `""` breaks these bytes apart into separate invalid strings.

If the pattern is not found in the expression, it returns an array that contains only the input expression.

If the expression starts with one or more occurrences of the pattern, an empty string will be added for each occurrence. For example, `splitString("abc", "a")` results in `"", "bc"`. Analogically, empty strings are added if the pattern is found at the end of the expression.

An empty string is also added for adjacent occurrences of the pattern that do not border the start or end of the string. For example, `splitString("abbc", "b")` results in `"a", "", "c"`.

If the pattern is empty, it splits the expression into one-byte substrings. For example, `splitString("abc", "")` results in `"a", "b", "c"`.

#### Syntax

`splitString(expression, pattern)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to split up into an array.

Required

pattern

string

The pattern to split the string expression at, or the empty string to split into one-byte strings.

Required

#### Returns

The data type of the returned value is `array`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd splitString(content, " "),



splitString(content, "is"),



splitString(content, ""),



splitString(content, "XYZ")
```

Run in Playground

Query result:

content

splitString(content, " ")

splitString(content, "is")

splitString(content, "")

splitString(content, "XYZ")

`DQL is awesome!`

`[DQL, is, awesome!]`

`[DQL , awesome!]`

`[D, Q, L, , i, s, , a, w, e, s, o, m, e, !]`

`[DQL is awesome!]`

`Dynatrace Query Language`

`[Dynatrace, Query, Language]`

`[Dynatrace Query Language]`

`[D, y, n, a, t, r, a, c, e, , Q, u, e, r, y, , L, a, n, g, u, a, g, e]`

`[Dynatrace Query Language]`

## startsWith

Checks if a string expression starts with a prefix. Returns `true` if does, `false` otherwise.

#### Syntax

`startsWith(expression, prefix [, caseSensitive])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression that will be checked.

Required

prefix

string

The prefix string with which the expression should start.

Required

caseSensitive

boolean

Whether the check should be done in a case-sensitive way.

Optional

#### Returns

The data type of the returned value is `boolean`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd startsWith(content, "D"),



startsWith(content, "dql", caseSensitive: false)
```

Run in Playground

Query result:

content

startsWith(content, "D")

startsWith(content, "dql", caseSensitive:FALSE)

`DQL is awesome!`

`true`

`true`

`Dynatrace Query Language`

`true`

`false`

## stringLength

Returns the length of a string expression. Length is defined as the number of UTF-16 code units, which is often the same as the number of characters in the string. In some cases, the number of characters is smaller than the number of UTF-16 code units, for example when Combining Diacritical Marks are used, or if characters outside the Basic Multilingual Plane (BMP), such as Emoji, are present.

If your use case requires consistent length for the same characters, consider ingesting strings after Unicode normalization.

No specific normalization form is guaranteed for Dynatrace-provided strings.

#### Syntax

`stringLength(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to get the number of UTF-16 code units for.

Required

#### Returns

The data type of the returned value is `long`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language"),



record(content = "ðâð¦º")



| fieldsAdd stringLength(content)
```

Run in Playground

Query result:

content

stringLength(content)

`DQL is awesome!`

`15`

`Dynatrace Query Language`

`24`

`ðâð¦º`

`5`

## substring

Gets a code unit range using a start index (inclusive) and an end index (exclusive).

Returns an empty string if from `>=` to.

`Indexes >=0` are relative to the start of the string and address consecutive characters from left to right, starting from the index position.

`Indexes <=-1` are relative to the last character of the string and are used to address characters from the right side of an expression, for example, `-2` is the penultimate character.

`Positive indexes` beyond the bounds of the string are assigned to the string length.

`Negative indexes` beyond the bounds of the string are equal to `0`. For example, in the `321` string, the index `-4` is beyond the bounds of the string therefore it equals `0`. However, the index `-2` is located within the bounds of that string and extracts `21` if used as a `from` the index.

The returned substring never starts or ends with an incomplete UTF-16 surrogate pair. Instead of that, it starts or ends with a question mark. This safeguards against the creation of invalid Unicode strings.

#### Syntax

`substring(expression [, from] [, to])`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to get a substring of.

Required

from

long

Index of first code unit to include in sub-string, inclusive, relative to start of `expression` if positive, relative to end if negative. Clamped at string bounds.

Optional

to

long

Index of last code unit to include in sub-string, exclusive, relative to start of `expression` if positive, relative to end if negative. Clamped at string bounds.

Optional

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd substring(content, from: 4),



substring(content, from: -2),



substring(content, from: 4, to: 9),



substring(content, from: -42, to: 42)
```

Run in Playground

Query result:

content

substring(content, from:4)

substring(content, from:-2)

substring(content, from:4, to:9)

substring(content, from:-42, to:42)

`DQL is awesome!`

`is awesome!`

`e!`

`is aw`

`DQL is awesome!`

`Dynatrace Query Language`

`trace Query Language`

`ge`

`trace`

`Dynatrace Query Language`

## trim

Removes leading and trailing whitespaces. Any code point <= ASCII 32 in decimal is considered a whitespace, where ASCII 32 is a blank space.

#### Syntax

`trim(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to remove leading and trailing white-space from.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = " DQL is awesome!"),



record(content = " Dynatrace Query Language ")



| fieldsAdd trim(content)
```

Run in Playground

Query result:

content

trim(content)

`" DQL is awesome!"`

`DQL is awesome!`

`" Dynatrace Query Language "`

`Dynatrace Query Language`

## unescape

Returns an unescaped string.

Unescaping rules

1. Single quotes, double quotes and backticks are unescaped.

Input

Output

`\"`

`"`

`\'`

`'`

`` \` ``

`` ` ``

2. Backslashes are unescaped.

Input

Output

`\\`

`\`

3. ASCII characters bell, backspace, form feed, new line, carriage return, horizontal tab and vertical tab are unescaped.

Input

Output

`\a`

`<bell>`

`\b`

`<backspace>`

`\f`

`<form feed>`

`\n`

`<new line>`

`\r`

`<carriage return>`

`\t`

`<horizontal tab>`

`\v`

`<vertical tab>`

4. `\xhh` within standard ASCII space (0x00 - 0x7f) is replaced by the related character.

Input

Output

`\x40`

`@`

`\x64`

`d`

5. `\xhh` within extended ASCII space (0x80 - 0xff) is interpreted as `\u00hh` and replaced by the related Unicode character.

Input

Output

`\xff`

`Ã¿`

6. `\uhhhh` is replaced by the related Unicode character.

Input

Output

`\u002e`

`.`

`\u0064`

`d`

#### Syntax

`unescape(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string expression

The string expression that will be unescaped.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = """"foo\x40bar\u002ecom""")



| fieldsAdd unescape(content)
```

Run in Playground

Query result:

| content | unescape(content) |
| --- | --- |
| `"foo\x40bar\u002ecom` | `"foo@bar.com` |

## unescapeHtml

Unescapes HTML in a string by replacing ASCII characters with HTML syntax.

#### Syntax

`unescapeHtml(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression that will be unescaped.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is &lt;bold&gt;awesome&lt;/bold&gt;!"),



record(content = "&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;")



| fieldsAdd unescapeHtml(content)
```

Run in Playground

Query result:

content

unescapeHtml(content)

`DQL is &lt;bold&gt;awesome&lt;/bold&gt;!`

`DQL is <bold>awesome</bold>!`

`&lt;a href=&quot;https://www.dynatrace.com/platform/grail&quot;&gt;Dynatrace Query Language&lt;/a&gt;`

`<a href="https://www.dynatrace.com/platform/grail">Dynatrace Query Language</a>`

## upper

Converts a string to uppercase.

#### Syntax

`upper(expression)`

#### Parameters

Parameter

Type

Description

Required

expression

string

The string expression to convert to uppercase.

Required

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(content = "DQL is awesome!"),



record(content = "Dynatrace Query Language")



| fieldsAdd upper(content)
```

Run in Playground

Query result:

content

upper(content)

`DQL is awesome!`

`DQL IS AWESOME!`

`Dynatrace Query Language`

`DYNATRACE QUERY LANGUAGE`

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: functions.md


---
title: DQL functions
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions
scraped: 2026-02-17T04:55:14.575483
---

# DQL functions

# DQL functions

* Latest Dynatrace
* Reference
* Updated on Feb 02, 2026

DQL functions grouped by category. For in-depth information on a specific function, select its name.

## [Aggregation functions](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions "A list of DQL aggregation functions.")

Aggregation functions compute results from a list of records.

Name

Description

[avg](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#avg "A list of DQL aggregation functions.")

Calculates the average value of a field for a list of records.

[collectArray](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#collectArray "A list of DQL aggregation functions.")

Collects the values of the provided field into an array.

[collectDistinct](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#collectDistinct "A list of DQL aggregation functions.")

Collects distinct values of the provided field into an array.

[correlation](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#correlation "A list of DQL aggregation functions.")

Calculates the Pearson correlation of two numeric fields for a list of records.

[count](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#count "A list of DQL aggregation functions.")

Counts the total number of records.

[countDistinct](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinct "A list of DQL aggregation functions.")

Calculates the cardinality of unique values of a field for a list of records.

[countDistinctApprox](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinctApprox "A list of DQL aggregation functions.")

Calculates the cardinality of unique values of a field for a list of records based on a stochastic estimation.

[countDistinctExact](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countDistinctExact "A list of DQL aggregation functions.")

Calculates the cardinality of unique values for the provided expression up to a maximum of 1M distinct values.

[countIf](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#countIf "A list of DQL aggregation functions.")

Counts the number of records that match the condition.

[max](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#max "A list of DQL aggregation functions.")

Calculates the maximum value of a field for a list of records.

[median](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#median "A list of DQL aggregation functions.")

Calculates the median of an expression.

[min](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#min "A list of DQL aggregation functions.")

Calculates the minimum value of a field for a list of records.

[percentile](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#percentile "A list of DQL aggregation functions.")

Calculates a given percentile of an expression.

[stddev](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#stddev "A list of DQL aggregation functions.")

Calculates the standard deviation of a field for a list of records.

[sum](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#sum "A list of DQL aggregation functions.")

Calculates the sum of a field for a list of records.

[takeAny](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeAny "A list of DQL aggregation functions.")

Returns any non-null value of a field for a list of records.

[takeFirst](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeFirst "A list of DQL aggregation functions.")

Returns the first value of a field for a list of records.

[takeLast](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeLast "A list of DQL aggregation functions.")

Returns the last value of a field for a list of records.

[takeMax](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeMax "A list of DQL aggregation functions.")

Returns the maximum value of a field for a list of records.

[takeMin](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#takeMin "A list of DQL aggregation functions.")

Returns the minimum value of a field for a list of records.

[variance](/docs/platform/grail/dynatrace-query-language/functions/aggregation-functions#variance "A list of DQL aggregation functions.")

Calculates the variance of a field for a list of records.

## [String functions](/docs/platform/grail/dynatrace-query-language/functions/string-functions "A list of DQL string functions.")

String functions allow you to create expressions that manipulate text strings in a variety of ways.

Name

Description

[concat](/docs/platform/grail/dynatrace-query-language/functions/string-functions#concat "A list of DQL string functions.")

Concatenates the expressions into a single string.

[contains](/docs/platform/grail/dynatrace-query-language/functions/string-functions#contains "A list of DQL string functions.")

Searches the string expression for a substring.

[decodeUrl](/docs/platform/grail/dynatrace-query-language/functions/string-functions#decodeUrl "A list of DQL string functions.")

Returns a URL-decoded string.

[encodeUrl](/docs/platform/grail/dynatrace-query-language/functions/string-functions#encodeUrl "A list of DQL string functions.")

Encodes a URL string.

[endsWith](/docs/platform/grail/dynatrace-query-language/functions/string-functions#endsWith "A list of DQL string functions.")

Checks if a string expression ends with a suffix.

[escape](/docs/platform/grail/dynatrace-query-language/functions/string-functions#escape "A list of DQL string functions.")

Returns an escaped string.

[getCharacter](/docs/platform/grail/dynatrace-query-language/functions/string-functions#getCharacter "A list of DQL string functions.")

Returns the character at a given position from a string expression.

[indexOf](/docs/platform/grail/dynatrace-query-language/functions/string-functions#indexOf "A list of DQL string functions.")

Returns the index of the first occurrence of a substring in a string expression.

[jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.")

Parses a JSON string and extracts one value selected by its name.

[jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.")

Parses a JSON string and extracts one value selected by a JSONPath expression.

[lastIndexOf](/docs/platform/grail/dynatrace-query-language/functions/string-functions#lastIndexOf "A list of DQL string functions.")

Returns the index of the last occurrence of a substring in a string expression.

[levenshteinDistance](/docs/platform/grail/dynatrace-query-language/functions/string-functions#levenshteinDistance "A list of DQL string functions.")

Computes the Levenshtein distance between two input strings.

[like](/docs/platform/grail/dynatrace-query-language/functions/string-functions#like "A list of DQL string functions.")

Tests if a string expression matches a pattern.

[lower](/docs/platform/grail/dynatrace-query-language/functions/string-functions#lower "A list of DQL string functions.")

Converts a string to lowercase.

[matchesPattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPattern "A list of DQL string functions.")

Tests if a string expression matches the DPL pattern.

[matchesPhrase](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPhrase "A list of DQL string functions.")

Matches a phrase against the input string expression using token matchers.

[matchesValue](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesValue "A list of DQL string functions.")

Searches records for a specific value in a given attribute. Returns true or false.

[parse](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parse "A list of DQL string functions.")

Extracts a single value from a string as specified in the pattern or a record if there are multiple named matchers.

[parseAll](/docs/platform/grail/dynatrace-query-language/functions/string-functions#parseAll "A list of DQL string functions.")

Extracts several values from a string as specified in the pattern.

[punctuation](/docs/platform/grail/dynatrace-query-language/functions/string-functions#punctuation "A list of DQL string functions.")

Extracts punctuation characters out of an input string.

[replacePattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.")

Replaces each substring of a string that matches the DPL pattern with the given string.

[replaceString](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replaceString "A list of DQL string functions.")

Replaces each substring of a string with a given string

[splitByPattern](/docs/platform/grail/dynatrace-query-language/functions/string-functions#splitByPattern "A list of DQL string functions.")

Splits a string into an array at each occurrence of the DPL pattern.

[splitString](/docs/platform/grail/dynatrace-query-language/functions/string-functions#splitString "A list of DQL string functions.")

Splits a string according to the parameters set.

[startsWith](/docs/platform/grail/dynatrace-query-language/functions/string-functions#startsWith "A list of DQL string functions.")

Checks if a string expression starts with a prefix. Returns true if does, false otherwise.

[stringLength](/docs/platform/grail/dynatrace-query-language/functions/string-functions#stringLength "A list of DQL string functions.")

Returns the length of a string expression.

[substring](/docs/platform/grail/dynatrace-query-language/functions/string-functions#substring "A list of DQL string functions.")

Gets a code unit range using a start index (inclusive) and an end index (exclusive).

[trim](/docs/platform/grail/dynatrace-query-language/functions/string-functions#trim "A list of DQL string functions.")

Removes leading and trailing whitespaces.

[unescape](/docs/platform/grail/dynatrace-query-language/functions/string-functions#unescape "A list of DQL string functions.")

Returns an unescaped string.

[unescapeHtml](/docs/platform/grail/dynatrace-query-language/functions/string-functions#unescapeHtml "A list of DQL string functions.")

Unescapes HTML in a string by replacing ASCII characters with HTML syntax.

[upper](/docs/platform/grail/dynatrace-query-language/functions/string-functions#upper "A list of DQL string functions.")

Converts a string to uppercase.

## [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")

Conversion and casting functions convert the expression or value from one data type to another type.

Name

Description

[asArray](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asArray "A list of DQL conversion and casting functions.")

Returns array value if the value is array, otherwise, returns null.

[asBinary](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asBinary "A list of DQL conversion and casting functions.")

Returns binary value (byte array) if the value is binary, otherwise, returns null.

[asBoolean](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asBoolean "A list of DQL conversion and casting functions.")

Returns boolean value if the value is boolean, otherwise, returns null.

[asDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asDouble "A list of DQL conversion and casting functions.")

Returns double value if the value is double, otherwise, returns null.

[asDuration](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asDuration "A list of DQL conversion and casting functions.")

Returns duration value if the value is duration, otherwise, returns null.

[asIp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asIp "A list of DQL conversion and casting functions.")

You can use this function to cast to an IP address.

[asLong](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asLong "A list of DQL conversion and casting functions.")

Returns long value if the value is long, otherwise, null.

[asNumber](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asNumber "A list of DQL conversion and casting functions.")

Returns same value if the value is integer, long, double, otherwise. returns null.

[asRecord](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asRecord "A list of DQL conversion and casting functions.")

Returns record value if the value is record, otherwise, returns null.

[asString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asString "A list of DQL conversion and casting functions.")

Returns string value if the value is string, otherwise, returns null.

[asTimeframe](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asTimeframe "A list of DQL conversion and casting functions.")

Returns timeframe value if the value is timeframe, otherwise. returns null.

[asTimestamp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asTimestamp "A list of DQL conversion and casting functions.")

Returns timestamp value if the value is timestamp, otherwise, returns null.

[asUid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asUid "A list of DQL conversion and casting functions.")

Returns a uid value if the value is a uid, otherwise, returns null.

[decode](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#decode "A list of DQL conversion and casting functions.")

The decode functions allow decoding an encoded string representation into a plain string or binary data.

[encode](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#encode "A list of DQL conversion and casting functions.")

The encode functions allow encoding binary data and plain strings into an encoded string representation.

[getHighBits](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#getHighBits "A list of DQL conversion and casting functions.")

Extracts the most significant bits of a uid value or IP address.

[getLowBits](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#getLowBits "A list of DQL conversion and casting functions.")

Extracts the least significant bits of a uid value or IP address.

[hexStringToNumber](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#hexStringToNumber "A list of DQL conversion and casting functions.")

Converts a hexadecimal string to a number.

[isUid128](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUid128 "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uid128.

[isUid64](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUid64 "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uid64.

[isUuid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#isUuid "A list of DQL conversion and casting functions.")

Tests if a uid value is of subtype uuid.

[numberToHexString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#numberToHexString "A list of DQL conversion and casting functions.")

Converts a number to a hexadecimal string.

[toArray](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toArray "A list of DQL conversion and casting functions.")

Returns the value if it is an array.

[toBoolean](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toBoolean "A list of DQL conversion and casting functions.")

Converts a value to Boolean if the value is of a suitable type.

[toDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDouble "A list of DQL conversion and casting functions.")

Converts a value to double if the value is of a suitable type.

[toDuration](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDuration "A list of DQL conversion and casting functions.")

Converts a value to duration if the value is of a suitable type.

[toIp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toIp "A list of DQL conversion and casting functions.")

You can use this function to convert an expression to an IP address.

[toLong](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toLong "A list of DQL conversion and casting functions.")

Converts a value to long if the value is of a suitable type.

[toString](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toString "A list of DQL conversion and casting functions.")

Returns the string representation of a value.

[toTimeframe](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toTimeframe "A list of DQL conversion and casting functions.")

Converts a value to timeframe if the value is of a suitable type.

[toTimestamp](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toTimestamp "A list of DQL conversion and casting functions.")

Converts a value to timestamp if the value is of a suitable type.

[toUid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toUid "A list of DQL conversion and casting functions.")

Converts a value to uid if the value is of a suitable type.

[type](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#type "A list of DQL conversion and casting functions.")

Returns the type of value as a string.

[uid128](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid128 "A list of DQL conversion and casting functions.")

Creates a uid of subtype uid128 from two long expressions.

[uid64](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uid64 "A list of DQL conversion and casting functions.")

Creates a uid of subtype uid64 from a long expression.

[uuid](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#uuid "A list of DQL conversion and casting functions.")

Creates a uid of subtype uuid from two long expressions.

[smartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#smartscapeId "A list of DQL conversion and casting functions.")

Creates a smartscapeId from the given string and long expression.

[asSmartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#asSmartscapeId "A list of DQL conversion and casting functions.")

Returns smartscapeId value if the value is `smartscapeId`, otherwise returns `null`.

[toSmartscapeId](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toSmartscapeId "A list of DQL conversion and casting functions.")

Converts a value to `smartscapeId` if the value is of a suitable type.

## [Conditional functions](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions "A list of DQL conditional functions.")

Functions that return a conditional result.

Name

Description

[coalesce](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#coalesce "A list of DQL conditional functions.")

Returns the first non-null argument, if any, otherwise null.

[if](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#if "A list of DQL conditional functions.")

Evaluates the condition, and returns the value of either the then or else parameter.

## [Boolean functions](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions "A list of DQL boolean functions.")

Functions that evaluate boolean expressions and test the presence of values.

Name

Description

[isFalseOrNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isFalseOrNull "A list of DQL boolean functions.")

Evaluates if an expression is false or null.

[isNotNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNotNull "A list of DQL boolean functions.")

Tests if a value is not null.

[isNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNull "A list of DQL boolean functions.")

Tests if a value is null.

[isTrueOrNull](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isTrueOrNull "A list of DQL boolean functions.")

Evaluates if an expression is true or null.

## [Time functions](/docs/platform/grail/dynatrace-query-language/functions/time-functions "A list of DQL time functions.")

Time functions return the decimal number for a particular time value, calculate the number of time units (days, months, years) between two dates, and allow to determine timestamps and timeframes, among others.

Name

Description

[duration](/docs/platform/grail/dynatrace-query-language/functions/time-functions#duration "A list of DQL time functions.")

Creates a duration from the given amount and time unit.

[formatTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#formatTimestamp "A list of DQL time functions.")

Formats a given timestamp according to a format string using a given pattern.

[getDayOfMonth](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfMonth "A list of DQL time functions.")

Extracts the day of the month from a timestamp.

[getDayOfWeek](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfWeek "A list of DQL time functions.")

Extracts the day of the week from a timestamp.

[getDayOfYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getDayOfYear "A list of DQL time functions.")

Extracts the day of the year from a timestamp.

[getEnd](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getEnd "A list of DQL time functions.")

Extracts the end timestamp from a timeframe.

[getHour](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getHour "A list of DQL time functions.")

Extracts the hour from a timestamp.

[getMinute](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getMinute "A list of DQL time functions.")

Extracts the minute from a timestamp.

[getMonth](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getMonth "A list of DQL time functions.")

Extracts the month from a timestamp.

[getStart](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getStart "A list of DQL time functions.")

Extracts the start timestamp from a timeframe.

[getSecond](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getSecond "A list of DQL time functions.")

Extracts the second from a timestamp.

[getYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getYear "A list of DQL time functions.")

Extracts the year from a timestamp.

[getWeekOfYear](/docs/platform/grail/dynatrace-query-language/functions/time-functions#getWeekOfYear "A list of DQL time functions.")

Extracts the week of the year from a timestamp.

[now](/docs/platform/grail/dynatrace-query-language/functions/time-functions#now "A list of DQL time functions.")

Returns the current time as a fixed timestamp of the query start.

[timeframe](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timeframe "A list of DQL time functions.")

Creates a timeframe structure from the given start and end timestamps.

[timestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestamp "A list of DQL time functions.")

Creates a timestamp using provided values in mandatory parameters.

[timestampFromUnixMillis](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixMillis "A list of DQL time functions.")

Creates a timestamp from the given milliseconds since Unix epoch.

[timestampFromUnixNanos](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixNanos "A list of DQL time functions.")

Creates a timestamp from the given nanoseconds since Unix epoch.

[timestampFromUnixSeconds](/docs/platform/grail/dynatrace-query-language/functions/time-functions#timestampFromUnixSeconds "A list of DQL time functions.")

Creates a timestamp from the given seconds since Unix epoch.

[unixMillisFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixMillisFromTimestamp "A list of DQL time functions.")

Converts a timestamp into milliseconds since Unix epoch.

[unixNanosFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixNanosFromTimestamp "A list of DQL time functions.")

Converts a timestamp into nanoseconds since Unix epoch.

[unixSecondsFromTimestamp](/docs/platform/grail/dynatrace-query-language/functions/time-functions#unixSecondsFromTimestamp "A list of DQL time functions.")

Converts a timestamp into seconds since Unix epoch.

## [Array functions](/docs/platform/grail/dynatrace-query-language/functions/array-functions "A list of DQL array functions.")

Functions related to a collection of items of the same data type stored at adjacent memory locations.

Name

Description

[array](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array "A list of DQL array functions.")

Creates an array from the list of given parameters.

[arrayAvg](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-avg "A list of DQL array functions.")

Returns the average of an array.

[arrayConcat](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-concat "A list of DQL array functions.")

Concatenates multiple arrays into a single array.

[arrayCumulativeSum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#arrayCumulativeSum "A list of DQL array functions.")

Returns the cumulative sum, also known as the running total, of the elements of the input array.

[arrayDelta](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-delta "A list of DQL array functions.")

Returns an array where each element is the difference from the previous non-null element.

[arrayDiff](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-diff "A list of DQL array functions.")

Calculates the element-wise difference between consecutive elements in an array.

[arrayDistinct](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-distinct "A list of DQL array functions.")

Returns the array without duplicates.

[arrayElement](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-element "A list of DQL array functions.")

Extracts a single element with the given index from an array.

[arrayFirst](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-first "A list of DQL array functions.")

Returns the first non-null element of an array.

[arrayFlatten](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-flatten "A list of DQL array functions.")

Returns a flattened array.

[arrayIndexOf](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-index-of "A list of DQL array functions.")

Returns position of the first member in the array, which is equal to the given value.

[arrayLast](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-last "A list of DQL array functions.")

Returns the last non-null element of an array.

[arrayLastIndexOf](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-last-index-of "A list of DQL array functions.")

Returns position of the last member in the array, which is equal to the given value.

[arrayMax](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-max "A list of DQL array functions.")

Returns the biggest number of an array.

[arrayMedian](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-median "A list of DQL array functions.")

Returns the median of the members of an array.

[arrayMin](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-min "A list of DQL array functions.")

Returns the smallest number of an array.

[arrayMovingAvg](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-avg "A list of DQL array functions.")

Replaces each element of the input array with the average of current and previous elements within the window.

[arrayMovingMax](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-max "A list of DQL array functions.")

Replaces each element of the input array with the maximum of current and previous elements within the window.

[arrayMovingMin](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-min "A list of DQL array functions.")

Replaces each element of the input array with the minimum of current and previous elements within the window.

[arrayMovingSum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-moving-sum "A list of DQL array functions.")

Replaces each element of the input array with the sum of current and previous elements within the window.

[arrayPercentile](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-percentile "A list of DQL array functions.")

Calculates a given percentile of an array.

[arrayRemoveNulls](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-remove-nulls "A list of DQL array functions.")

Returns the array where null elements are removed.

[arrayReverse](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-reverse "A list of DQL array functions.")

Returns the array with elements in reversed order.

[arraySize](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-size "A list of DQL array functions.")

Returns the size of an array.

[arraySlice](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-slice "A list of DQL array functions.")

Extracts a slice from the input array using a `from` index (inclusive) and a `to` index (exclusive).

[arraySort](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-sort "A list of DQL array functions.")

Returns the array with elements sorted in ascending order by default.

[arraySum](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-sum "A list of DQL array functions.")

Returns the sum of an array.

[arraytoString](/docs/platform/grail/dynatrace-query-language/functions/array-functions#array-to-String "A list of DQL array functions.")

Converts an array into a string.

## [Vector distance functions](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions "A list of DQL vector distance functions.")

Functions that calculate the distance between numeric array expressions.

Name

Description

[vectorL1Distance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorL1Distance "A list of DQL vector distance functions.")

Calculates the taxicab distance between numeric array expressions.

[vectorL2Distance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorL2Distance "A list of DQL vector distance functions.")

Calculates the Euclidean distance between numeric array expressions.

[vectorCosineDistance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorCosineDistance "A list of DQL vector distance functions.")

Calculates the cosine distance between numeric array expressions.

[vectorInnerProductDistance](/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions#vectorInnerProductDistance "A list of DQL vector distance functions.")

Calculates the negative dot product between numeric array expressions.

## [Network functions](/docs/platform/grail/dynatrace-query-language/functions/network-functions "A list of DQL array functions.")

Functions related to IP addresses.

Name

Description

[ip](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ip "A list of DQL array functions.")

You can use this function to create an IP address.

[ipIn](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIn "A list of DQL array functions.")

This function can be used to check if a list of IP addresses or an IP network (e.g. 127.0.0.1/8) contains particular IP addresses

[ipIsLinkLocal](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsLinkLocal "A list of DQL array functions.")

Checks if an IP address is a link-local IP address.

[ipIsLoopback](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsLoopback "A list of DQL array functions.")

Checks if an IP address is a loopback IP address.

[ipIsPrivate](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsPrivate "A list of DQL array functions.")

Checks if an IP address is a private IP address.

[ipIsPublic](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipIsPublic "A list of DQL array functions.")

Checks if an IP address is a public IP address.

[ipMask](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipMask "A list of DQL array functions.")

You can use this function to mask an IP address with given bits.

[isIp](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIp "A list of DQL array functions.")

Checks if an expression is an IPv4/v6 address.

[isIpV4](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIpV4 "A list of DQL array functions.")

Checks if an expression is an IPv4 address.

[isIpV6](/docs/platform/grail/dynatrace-query-language/functions/network-functions#isIpV6 "A list of DQL array functions.")

Checks if an expression is an IPv6 address.

## [Hash functions](/docs/platform/grail/dynatrace-query-language/functions/hash-functions "A list of DQL hash functions.")

Hash related functions.

Name

Description

[hashCrc32](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashCrc32 "A list of DQL hash functions.")

Returns a CRC32 hash for a given string expression.

[hashMd5](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashMd5 "A list of DQL hash functions.")

Computes the MD5 hash for a given string expression.

[hashSha1](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha1 "A list of DQL hash functions.")

Computes the SHA-1 hash for a given string expression.

[hashSha256](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha256 "A list of DQL hash functions.")

Returns a SHA-256 hash for the given expression.

[hashSha512](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashSha512 "A list of DQL hash functions.")

Returns a SHA-512 hash for the given expression.

[hashXxHash32](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashXxHash32 "A list of DQL hash functions.")

Returns a xxHash32 hash for a given string expression.

[hashXxHash64](/docs/platform/grail/dynatrace-query-language/functions/hash-functions#hashXxHash64 "A list of DQL hash functions.")

Returns a xxHash64 hash for a given string expression.

## [Bitwise functions](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions "A list of DQL bitwise functions.")

Bitwise operations performing on long expressions.

Name

Description

[bitwiseAnd](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseAnd "A list of DQL bitwise functions.")

Calculates the bitwise and between two long expressions.

[bitwiseCountOnes](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseCountOnes "A list of DQL bitwise functions.")

Counts the bits assigned to one of the long expressions.

[bitwiseNot](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseNot "A list of DQL bitwise functions.")

Inverts the bits included in the long expression.

[bitwiseShiftLeft](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseShiftLeft "A list of DQL bitwise functions.")

Shifts the long expressions by the number of given bits to the left.

[bitwiseShiftRight](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseShiftRight "A list of DQL bitwise functions.")

Shifts the long expression by number of given bits to the right.

[bitwiseOr](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseOr "A list of DQL bitwise functions.")

Calculates the bitwise or between two long expressions.

[bitwiseXor](/docs/platform/grail/dynatrace-query-language/functions/bitwise-functions#bitwiseXor "A list of DQL bitwise functions.")

Calculates the bitwise xor between two long expressions.

## [Mathematical functions](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions "A list of DQL mathematical functions.")

Functions executing mathematical calculations.

Name

Description

[abs](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#abs "A list of DQL mathematical functions.")

Returns the absolute value of numeric\_expression.

[acos](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#acos "A list of DQL mathematical functions.")

Computes arc cosine of expression.

[asin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#asin "A list of DQL mathematical functions.")

Computes arc sine of expression.

[atan](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#atan "A list of DQL mathematical functions.")

Computes the arc tangent of expression.

[atan2](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#atan2 "A list of DQL mathematical functions.")

Computes the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta).

[bin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#bin "A list of DQL mathematical functions.")

Rounds values down to a multiple of a given numeric bin size.

[ceil](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#ceil "A list of DQL mathematical functions.")

Calculates the smallest (closest to negative infinity) double value greater than or equal to the numeric\_expression; is equal to a mathematical integer.

[cos](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cos "A list of DQL mathematical functions.")

Computes the trigonometric cosine of an angle expression (in radians).

[cosh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cosh "A list of DQL mathematical functions.")

Computes the hyperbolic cosine of an angle expression.

[cbrt](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#cbrt "A list of DQL mathematical functions.")

Calculates the real cubic root of a numeric expression.

[degreeToRadian](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#degreeToRadian "A list of DQL mathematical functions.")

Converts the numeric expression of an angle in degrees to an approximately equivalent angle as expressed in radians.

[e](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#e "A list of DQL mathematical functions.")

Returns Eulerâs number.

[exp](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#exp "A list of DQL mathematical functions.")

Calculates the exponential function e^x, where e is the Euler's number and x is a numeric expression.

[floor](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#floor "A list of DQL mathematical functions.")

Calculates the largest (closest to positive infinity) double value less than or equal to the numeric\_expression; and is equal to a mathematical integer.

[hypotenuse](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#hypotenuse "A list of DQL mathematical functions.")

Returns sqrt (x^2 + y^2).

[log](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log "A list of DQL mathematical functions.")

Calculates the natural logarithm (the base is e, the Euler's number) of a numeric expression.

[log1p](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log1p "A list of DQL mathematical functions.")

Calculates log(1+x), where log is the natural logarithm and x is a numeric expression.

[log10](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#log10 "A list of DQL mathematical functions.")

Calculates the decadic (common) logarithm (the base is 10) of a numeric expression.

[pi](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#pi "A list of DQL mathematical functions.")

Returns the constant value of PI (Archimedesâ number).

[power](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#power "A list of DQL mathematical functions.")

Raises a numeric expression to a given power.

[radianToDegree](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#radianToDegree "A list of DQL mathematical functions.")

Converts the numeric expression of an angle in radians to an approximately equivalent angle as expressed in degrees.

[random](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#random "A list of DQL mathematical functions.")

Creates a random double value.

[range](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#range "A list of DQL mathematical functions.")

Aligns the given value/timestamp to value range based on the provided alignment parameter.

[round](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#round "A list of DQL mathematical functions.")

Rounds any numeric value to the specified number of decimal places.

[signum](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#signum "A list of DQL mathematical functions.")

Returns the signum (sign) result of an argument.

[sin](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sin "A list of DQL mathematical functions.")

Computes the trigonometric sine of angle expression (in radians).

[sinh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sinh "A list of DQL mathematical functions.")

Computes the hyperbolic sine of expression.

[sqrt](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#sqrt "A list of DQL mathematical functions.")

Computes the positive square root of a numeric expression.

[tan](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#tan "A list of DQL mathematical functions.")

Computes the trigonometric tangent of angle expression (in radians).

[tanh](/docs/platform/grail/dynatrace-query-language/functions/mathematical-functions#tanh "A list of DQL mathematical functions.")

Computes the hyperbolic tangent of expression.

## [Join functions](/docs/platform/grail/dynatrace-query-language/functions/join-functions "A list of DQL join functions.")

Functions that join records from subqueries.

Name

Description

[lookup](/docs/platform/grail/dynatrace-query-language/functions/join-functions#lookup "A list of DQL join functions.")

Returns a record from a subquery (the lookup table) producing a match between a field in the source table (sourceField) and a field in the lookup table (lookupField).

[getNodeName](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeName "A list of DQL join functions.")

Returns the Smartscape node name.

[getNodeField](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeField "A list of DQL join functions.")

Returns the field value for a Smartscape node.

## [General functions](/docs/platform/grail/dynatrace-query-language/functions/general-functions "A list of DQL general functions.")

Functions with a general purpose.

Name

Description

[classicEntitySelector](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions.")

Returns entities matching the specified entity selector.

[entityAttr](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions.")

Returns the attribute value for an entity.

[entityName](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-name "A list of DQL general functions.")

Returns the name of an entity.

[exists](/docs/platform/grail/dynatrace-query-language/functions/general-functions#exists "A list of DQL general functions.")

Tests if a field exists.

[in](/docs/platform/grail/dynatrace-query-language/functions/general-functions#in "A list of DQL general functions.")

Tests if a value is a member of an array.

[record](/docs/platform/grail/dynatrace-query-language/functions/general-functions#record "A list of DQL general functions.")

Creates a record from the keys and values of the parameter.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: operators.md


---
title: DQL operators
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/operators
scraped: 2026-02-17T04:55:12.666445
---

# DQL operators

# DQL operators

* Latest Dynatrace
* Reference
* 22-min read
* Updated on Oct 28, 2025

The following table shows a list of all the DQL operators.

Operator

Description

`+`

Addition

`-`

Subtraction or arithmetic negation

`*`

Multiplication

`/`

Division

`%`

Modulo

`<`

Less than

`<=`

Less than or equal to

`>`

Greater than

`>=`

Greater than or equal to

`==`

Equals

`!=`

Does not equal

`not`

Logical NOT (negation)

`and`

Logical AND

`or`

Logical OR

`xor`

Logical XOR (exclusive or)

`in`

Subquery comparison

`@`

Time alignment

`~`

Search

The precedence for the operators is as follows (from strongest to weakest):

* `-` (arithmetic negation)
* `*`, `/`, `%`
* `@`
* `+`, `-` (subtraction)
* `~`
* `==`, `!=`, `>`, `>=`, `<`, `<=`
* `in`
* `not`
* `and`
* `xor`
* `or`

## Arithmetic operators

You can use arithmetic operators with numbers, represented by both the types `long` or `double`. In addition, some operators support the types `timestamp`, `timeframe`, `duration` or `ip`.

Operator

Description

Example

`+`

Addition

`2 + 2.5`

`-`

Subtraction

`0.2 - 0.11`

`*`

Multiplication

`4 * 5`, `60 * 1s`

`/`

Division

`10 / 2`, `1h / 60`

`%`

Modulo

`4 % 2`

`-`

Arithmetic negation

`-1`

### ADDITION

| ADDITION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timestamp) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timestamp) | Applicable (duration) | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Applicable (IP) | Applicable (IP) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### SUBTRACTION

| SUBTRACTION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Applicable (timestamp) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (timeframe) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Applicable (IP) | Applicable (IP) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (IP) | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### MULTIPLICATION

| MULTIPLICATION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration, rounded to full nanos) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Applicable (duration) | Applicable (duration, rounded to full nanos) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### DIVISION

Integer division

When you divide a `long` value by another `long` value using the `/` operator, the result is also a `long` value, and any fractional part is discarded. To get a result with the fractional part (a `double` value), you need to convert or cast at least one of the operands to `double` (e.g., by using the [toDouble](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions#toDouble "A list of DQL conversion and casting functions.") function).

| DIVISION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Applicable (duration rounded to full nanos) | Applicable (duration rounded to full nanos) | Not applicable | Not applicable | Not applicable | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

The data type resulting from the operation is indicated in parentheses in the table above.

### MODULO

| MODULO | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable (double) | Applicable (double) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

### ARITHMETIC NEGATION

| NEGATION | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SELF | Applicable (long) | Applicable (double) | Not applicable | Not applicable | Not applicable | Applicable (duration) | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

## Comparison operators

Operator

Description

Example

`<`

Less than

`8 < 9`, `now()-1m < now()`

`<=`

Less than or equal to

`4 <= 5`

`>`

Greater than

`5 > 4`, `"a" > "A"`

`>=`

Greater than or equal to

`4 >=4`

### Comparison operators (<, <=, >, >=)

* ( ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") ) - `true` or `false` based on the result of the operator
* ( ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") ) - `null`

| <, <=, >, >= | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |

## Equality operators

Operator

Description

Example

`==`

Equals

`2 == 2`

`!=`

Does not equal

`1 != 2`

Equality comparisons (`==`, `!=`) use a tri-state boolean algebra (`true`, `false`, `null`). This means that if any side of the equality comparison is `null`, the overall result of the comparison is `null`.
There are four DQL functions that cover scenarios where missing or `null` records need to be retrieved:

* The [`isTrueOrNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isTrueOrNull "A list of DQL boolean functions.")
* The [`isFalseOrNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isFalseOrNull "A list of DQL boolean functions.")
* The [`isNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNull "A list of DQL boolean functions.")
* The [`isNotNull` function](/docs/platform/grail/dynatrace-query-language/functions/boolean-functions#isNotNull "A list of DQL boolean functions.")

For example, the below query that uses basic filtering does not provide records with `null` or missing values:

```
fetch logs



| filter log.source != "logsourcename"  // does not provide the records where `log.source` is null or missing
```

However, using the `isTrueOrNull` function includes those records with `null` and missing values:

```
fetch logs



| filter isTrueOrNull(log.source != "logsourcename") // also provides the records where `log.source` is null or missing
```

### Equality operators (==, !=)

* ( ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") ) - `false` for non-comparable types in case of `==` operator, `true` for non-compatible types in case of `!=` operator
* ( ![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") ) - `true` or `false` based on the result of the operator
* `null` - if one of the operands is `null`
* `null == null` - `null`

| ==, != | Long | Double | String | Boolean | Timestamp | Duration | Timeframe | Binary | IP | UID | Array | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Long | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Double | Applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| String | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Boolean | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timestamp | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Duration | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Timeframe | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| Binary | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable | Not applicable |
| IP | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable | Not applicable |
| UID | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable | Not applicable |
| Array | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable | Not applicable |
| Record | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Applicable |

## Logical operators

Operator

Description

Example (yields true)

`not`

Logical NOT (negation) - Negates a logical state

`not 2==1`

`and`

Logical AND (multiplication) - Yields `true` if both operands are `true`.

`not 2==1 and 1<2`

`or`

Logical OR (addition) - Yields `true` if one of the operands is `true`, regardless of the other operand.

`1 < 2 or 1 > 2`

`xor`

Logical XOR (exclusive OR) - Yields `true` if one of the operands is `true`, but `false` in case both are `true`.

`1 < 2 xor 1 > 2`

The behavior of logical operators follows the tri-state boolean logic.

* **AND**

  + `true` AND `null` = `null`
  + `null` AND `true` = `null`
  + `false` AND `null` = `false`
  + `null` AND `false` = `false`
  + `null` AND `null` = `null`
* **OR**

  + `true` OR `null` = `true`
  + `null` OR `true` = `true`
  + `false` OR `null` = `null`
  + `null` OR `false` = `null`
  + `null` OR `null` = `null`
* **XOR**

  + `true` XOR `null` = `null`
  + `null` XOR `true` = `null`
  + `false` XOR `null` = `null`
  + `null` XOR `false` = `null`
  + `null` XOR `null` = `null`
* **NOT**

  + NOT `null` = `null`

## Iterative expressions

Iterative expressions can be used to evaluate every element of a given array or every i-th element of one or more arrays.

### iAny

Checks an iterative boolean expression and returns `true`, if the expression was true at least once, `false` if it wasn't. For example:

```
fetch logs



| fieldsAdd a = array(1, 2, 3)



| filter iAny(a[] > 2)
```

### iCollectArray

Collects the results of an iterative expression into an array. For example:

```
fetch logs



| fieldsAdd a = array(1, 2, 3), b = array(10, 11, 12)



| fieldsAdd iCollectArray(a[] + b[])
```

### iIndex

Allows to access the index of an iterative expression element. For example, you can add the index of a value in the array and expand the array.

```
data record(a = array(2, 3, 7, 7, 1))



| fields a = record(value = a[], index = iIndex())



| expand a



| fields value = a[value], index = a[index]
```

iIndex only works in expressions where at least one iterative expression is present.

## Operators for subqueries

### in

The `in` comparison operator evaluates the occurrence of a value returned by the left side's expression within a list of values returned by the right side's DQL subquery.

**Syntax**

`expression in [execution block]`

**Usage and constraints**

Name

Type

Mandatory

Constraints

Description

left side

expression

yes

Either a field identifier or an expression.

The element to be found in the list returned by the right side's subquery.

right side

execution block

yes

It has to return a single field providing a list of values.

The DQL Subquery which returns the list of values to compare against.

**Example**

This example shows how to use the `in` keyword for filtering a host metric for the host's attribute:

```
timeseries avg(dt.host.cpu.usage), filter:dt.entity.host in [fetch dt.entity.host



| fieldsAdd tags



| expand tags



| filter tags == "ServiceNow" | fields id]
```

## Time alignment

The `@` operator aligns a timestamp to the provided time unit. It rounds down the timestamp to the beginning of the time unit.

#### Syntax

`[timestamp|duration|calendarDuration] @ unit`

#### Left side

On the left side of the `@` operator, you can use a `timestamp` expression, a `duration` expression, or a calendar duration.  
If you use the `@` operator without an expression on the left side, the operator will use the timestamp expression `now()` and will align the current time to the time unit. For example, `@h` is the beginning of the current hour, and equivalent to `now()@h`. Expressions of type `duration` and calendar durations are considered as an offset to `now()`.  
For example, `-2M@..`. is equivalent to `(now() - 2M)@...`.

#### Right side

The time unit can be any DQL supported [duration unit](/docs/platform/grail/dynatrace-query-language/data-types#duration "A list of DQL data types.") including `s` (second), `m` (minute), `h` (hour), or a calendar duration unit like `d` (day), `w` (week), `M` (month), `q` (quarter), and `y` (year).

Duration units (`h`, `m`, `s`, `ms`, `us`, and `ns`) allow to add a factor, for example, `@3h`.  
Leaving the factor out is equivalent to setting it to `1`. Note the following constraints when adding such factor:

* `h` supports all divisors of `24`: `1h`, `2h`, `3h`, `4h`, `6h`, `8h`, `12h`, `24h`. `@24h` is similar to `@1d` but might differ in the case of daylight-saving times.
* `m` and `s` support all divisors of `60`: `1m`, `2m`, `3m`, `4m`, `5m`, `6m`, `10m`, `12m`, `15m`, `20m`, `30m`, `60m`, and equivalently for `s`.
* `ms`, `us`, and `ns` support all divisors of `1000`.

By default, the week unit `w` uses the first day of the week as defined by your configured locale.
To explicitly specify the first day of the week, you can use the following time units:

* `w0` (Sunday)
* `w1` (Monday)
* `w2` (Tuesday)
* `w3` (Wednesday)
* `w4` (Thursday)
* `w5` (Friday)
* `w6` (Saturday)
* `w7` (Sunday)

For example, `@w1` means midnight of Monday of the current week.

##### Examples

For the following examples, the current time is Wednesday, 04 September 2024, 14:47:05+0200.

Time modifier

Description

Resulting time

`-2h@h`

2 hours ago, aligned to the hour

Wednesday, 04 September 2024, 12:00:00+0200

`-1d@d`

Yesterday, aligned to the day

Tuesday, 03 September 2024, 00:00:00+0200

`-7d@d`

7 days ago, aligned to the day

Wednesday, 28 August 2024, 00:00:00+0200

`@w0`

Start of this week, from Sunday

Sunday, 01 September 2024, 00:00:00+0200

`@w1`

Start of this week, from Monday

Monday, 02 September 2024, 00:00:00+0200

`@M`

Start of this month

Sunday, 01 September 2024, 00:00:00+0200

`-1M@M`

Start of last month

Thursday, 01 August 2024, 00:00:00+0200

`@q`

Start of this quarter

Monday, 01 July 2024, 00:00:00+0200

`@y`

Start of this year

Monday, 01 January 2024, 00:00:00+0100

## Search

You can use the `~` operator in expressions to match the value of an expression against a given search string. The performed comparison is case-insensitive and supports pattern matching using wildcards. The `~` operator returns a `boolean` value: `true` in case of a match, and `false` otherwise.

#### Syntax

`expression ~ "string literal"`

#### Left side

You can use any expression on the left side of the `~`operator. For details on how different data types work with this operator, see the [Returns](#search-returns) section.

#### Right side

The string literal to search for. It can be one of the following:

* A search string without a wildcard (`*`). For example:

  ```
  content ~ "error"
  ```
* A search string with a wildcard (`*`) as first and/or last character. For example:

  ```
  user ~ "*dynatrace.com"
  ```

#### Returns

##### Search strings without wildcards

The `~` operator searches the value as a string token inside a string. Its behavior depends on the data type of the expression on the left side:

* If the expression is of type `string`, the operator searches the value as a token inside the string. It's case-insensitive. For example, `"Hello World"` matches `~"world"`, but `"HelloWorld"` doesn't.
* If the expression is of type `long`, `double`, `smartscape ID`, `IP address`, or `UID`, the operator only matches if the string representation of its value is equal to the search string. For example, the IP address `192.0.0.1` matches `~"192.0.0.1"`, but not `~"192"`.
* If the expression is of type `array`, each element is checked. The operator matches if at least one of the elements in the array does.
* If the expression is of type `record`, the operator matches if any field name or value matches.
* If the expression is of type `boolean`, `timestamp`, `duration`, or `binary`, the result is always false.

Expression type

Expression value

Operation

Result

Note

String

`"Hello WORLD!"`

`~"world"`

`true`

String

`"helloWorld"`

`~"World"`

`false`

`helloWorld` is one token since there are no separators.

String

`"192.168.0.7"`

`~"192"`

`true`

As itâs a string, the field has four tokens.

IP

`192.168.0.7`

`~"192"`

`false`

Only strings are tokenized.

IP

`192.168.0.7`

`~"192.168.0.7"`

`true`

The value is auto-converted, so there's an exact match.

Long

`12`

`~"12"`

`true`

The value is auto-converted, so there's an exact match.

UID

`uuid(1,2)`

`~"00000000-0000-0001-0000-000000000002"`

`true`

The value is not tokenized, but can be auto-converted.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST-0000000000000001"`

`true`

The value is auto-converted.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"host-0000000000000001"`

`false`

For a Smartscape ID, the check is case-sensitive.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST"`

`false`

The value isn't tokenized.

Record

`record(firstName="John",lastName="Doe")`

`~"john"`

`true`

Search also works in nested fields.

Record

`record(firstName="John",lastName="Doe")`

`~"lastName"`

`true`

Search also works in the names of nested fields.

Record

`record(firstName="John",lastName="Doe")`

`~"name"`

`false`

`firstName` and `lastName` are one token since they don't contain separators.

Record

`record(first name="John",last name="Doe")`

`~"name"`

`true`

Search also works in the names of nested fields.

Array

`array(1,2,3,5,8,13)`

`~"3"`

`true`

One element of the array is 3, which can be auto-converted to match `~"3"`.

Boolean

`true`

`~"true"`

`false`

Booleans aren't supported.

Duration

`1h`

`~"1h"`

`false`

Durations aren't supported.

##### Search strings with wildcards

The operator searches the pattern in the tokens of a string. Its behavior depends on the data type of the expression on the left side:

* If the expression is of type `string`, the result is true if at least one of the tokens matches the pattern.
* If the expression is of type `array`, the result is true if one of the elements of the array matches the pattern.
* If the expression is of type `record`, the result is true if the name or value of a nested field matches the pattern.
* If the expression is of any other type (`long`, `double`, `smartscape ID`, `IP address`, `UID`, `boolean`, `timestamp`, `duration`, or `binary`) patterns aren't supported and the result is always `false`.

Expression type

Expression value

Operation

Result

Note

String

`"AuthenticationError"`

`~"*error"`

`true`

String

`"There was an AuthenticationError"`

`~"authentication*"`

`true`

String

`"There was an NoAuthenticationError"`

`~"authentication*"`

`false`

String

`"helloWorld"`

`~"*ow*"`

`true`

String

`"hello world"`

`~"*ow*"`

`false`

String

`"192.168.0.7"`

`~"192.168.*"`

`true`

It matches as it's a string and not an IP address.

Record

`record(firstName="John",lastName="Doe")`

`~"*name"`

`true`

The string matches the name of the nested field in the record.

Record

`record(firstName="John",lastName="Doe")`

`~"*do*"`

`true`

The string matches the record.

Array

`array("hello", "world", "myCustomName")`

`~"my*"`

`true`

The string matches within the array.

IP

`192.168.0.7`

`~"192*"`

`false`

Only strings allow patterns.

Long

`192`

`~"1*"`

`false`

Only strings allow patterns.

Smartscape ID

`smartscapeId("HOST", 1)`

`~"HOST*"`

`false`

Only strings allow patterns.

Boolean

`true`

`~"t*"`

`false`

Only strings allow patterns.

Duration

`1h`

`~"*h"`

`false`

Only strings allow patterns.

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: dynatrace-query-language.md


---
title: Dynatrace Query Language
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language
scraped: 2026-02-17T04:46:10.991281
---

# Dynatrace Query Language

# Dynatrace Query Language

* Latest Dynatrace
* Reference
* Updated on Jan 28, 2026

Dynatrace Query Language (DQL) is a powerful tool to explore your data and discover patterns, identify anomalies and outliers, create statistical modeling, and more based on data stored in [Dynatrace Grail storage](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.").

DQL offers maximum flexibility because it is built for processing arbitrary event data, requiring no up-front description of the input data's schema contrary to relational databases like SQL tables.

Read [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") to get started or explore the language.

[### How to use DQL

Find out how DQL works and what are DQL key concepts.](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")[### Language reference

Learn about DQL syntax in detail.](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")[### Learn DQL

Get hands-on experience with interactive tutorials on how to use DQL.](/docs/platform/grail/dynatrace-query-language/dql-guide#learn-dql-app "Find out how DQL works and what are DQL key concepts.")[### Migrating to DQL

Compare DQL to other common query languages.](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")[### DQL examples for logs

Find out what you can do with logs using DQL.](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")[### DQL examples for security data

Use DQL to query your security data on Grail.](/docs/secure/threat-observability/dql-examples "DQL examples for security data powered by Grail.")[### DQL examples for business events

Find out what you can do with business events using DQL.](/docs/observe/business-observability/bo-analysis "Analyze and present business event data.")[### DQL examples for Davis problems and events

Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")[### DQL examples for metrics

Use DQL to query your metric observability data.](/docs/analyze-explore-automate/metrics/dql-examples "DQL timeseries examples")

## Related topics

* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")


---


## Source: lookup-data.md


---
title: Lookup data in Grail
source: https://www.dynatrace.com/docs/platform/grail/lookup-data
scraped: 2026-02-16T21:27:42.348307
---

# Lookup data in Grail

# Lookup data in Grail

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Oct 07, 2025

Preview

Storing lookup data in [Grail](#grail) enables you to enrich your observability data with your custom data. You can upload your lookup data and join it with your existing data in Grail, such as `logs`, `events`, `spans`, or `metrics`.

![A diagram demonstrating how lookup data in Grail works. ](https://dt-cdn.net/images/diagram-spc-file-storage-in-grail-web-res-docs-1920-a87d521cbd.png)

Dynatrace stores lookup data as tabular files in the Resource Store, which is part of Grail. You can upload and manage your lookup data through the [Resource Store API](#lookup-files-rest-api). Once stored in Grail, you can use your lookup files to enrich your data within [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries.

You can define lookup tables in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), which currently provides the only user interface for creating and managing lookup tables without using the API. For instructions, see [Create and use lookup tables](/docs/secure/investigations/enhance-results#lookup "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

## Lookup files

Static data, such as lookup tables, can be permanently stored in Grail as files. We reference files via a file path such as `/lookups/http_status_codes`. The following conventions apply to file paths, effectively organizing the files stored in Grail in a folder-like structure:

* Must contain only alphanumeric characters (`a-zA-Z0-9`), `-`, `_`, `.`, or `/`.
* Must start with `/`.
* Must end with `a-zA-Z0-9`.
* Must contain at least two `/` characters.
* Between any two consecutive `/` characters, there must be at least one alphanumeric character (`a-zA-Z0-9`).

The file path must start with `/lookups` when storing lookup data in Grail.

### Organize your files

The naming conventions allow you to organize your files like a regular file system. Using prefixes that mimic folders, such as in the file path `/lookups/my_team/allow_list`, makes it convenient to find and manage your lookup files stored in Grail.

## Permissions

To read lookup data stored in Grail, the policy bound to your user group must contain the following permission:

* `storage:files:read`

To upload lookup data to Grail via REST API or to delete it, the policy bound to your user group must contain the following permissions:

* `storage:files:write`
* `storage:files:delete`

All permissions can be restricted to specific paths or prefixes, giving users access to only a limited set of files. To learn more about setting up the required permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

When creating an OAuth token or platform token to make API calls from an API client, ensure these permissions are also configured for the token. The user linked to that OAuth token or platform token must have these permissions assigned.

Preview opt-in

Customers with [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") can join the preview for lookup data in Grail. During the preview phase, the `storage:files` permissions are not included in the default Grail policies. You can opt into the preview program by manually adding permissions to access lookup files to your custom policies.

You can configure permissions with [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health."). To grant full access to all lookup data in `/lookups/`, you can create a policy (**Identity & access management** > **Policy management** >  **Create policy**) with the following statements:

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:write WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:delete WHERE storage:file-path startsWith "/lookups/";
```

As another example, to give read-only access to all lookup data in `/lookups/`, you can use the following statement:

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";
```

## Limits

The following limits apply for storing lookup data in Grail:

| Limit | Value |
| --- | --- |
| Maximum number of files per environment | `100` (during preview) |
| Maximum file size | `100 MBÂ` |
| Maximum number of fields | `128` |

Upon completion of the preview and lifting the maximum number of files that can be stored per environment, the usage of lookup data in Grail can generate Events powered by Grail consumption.

## Manage lookup files

### Manage lookup files via REST API

You can manage your lookup files in Grail via the Resource Store API. Dynatrace offers API calls to:

* Upload your lookup data to Grail
* Delete your lookup data from Grail
* Test parsing the lookup data you want to upload with DPL

To update a file's content, you need to reupload the whole file and overwrite the existing file.

The Resource Store API uses the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") to parse uploaded data and convert it into a tabular storage format. This provides complete flexibility regarding the uploaded data, supporting various text-based formats, including `CSV`, `JSONL`, or `XML`.

### Access API documentation

To access the Swagger API documentation for the Resource Store API and to start making API requests using Swagger:

1. Search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail - Resource Store**.
3. Optional Authenticate with your API token if you want to use Swagger to execute your requests. For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context."). Select the **Try it out** button to interact with the API directly from the documentation.
4. Perform one of the following actions.

To do this

Go to **Lookup Data** and select this

Test parsing your to-be-uploaded lookup data without storing the result in Grail.

**POST/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern**

Upload your lookup data and store it as a new tabular file in Grail or replace an existing one.

**POST/platform/storage/resource-store/v1/files/tabular/lookup:upload**

Delete the file from the Resource Store.

**POST/platform/storage/resource-store/v1/files:delete**

### Parse lookup data

The API provides the `/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern` endpoint, which previews the uploaded results without persisting them as a file in Grail. The endpoint helps you define the DPL pattern that fits the format of your data.

The endpoint accepts input as `multipart/form-data` with a `content` part for the uploaded data and a `request` part for additional parameters. The only required parameter in the request part is the `parsePattern` parameter, which provides the DPL pattern to parse the uploaded text-based data. For more details, see the Swagger API documentation.

You can define any DPL pattern that matches your data. Every pattern match produces a record. The following example shows uploaded CSV data in the following format:

```
Code,Category,Message



100,informational,Continue



101,informational,Switching Protocols



...
```

The DPL pattern `INT:code ',' LD:category ',' LD:message` matches the content and produces a record with fields `code`, `category`, and `message` for every line except for the header line. You can use the `skippedRecords` parameter to exclude header lines where the pattern matches also the header lines.

With the same data in JSONL format you can use the `JSON:json` DPL pattern:

```
{"code": 100, "category": "informational", "message": "Continue"}



{"code": 101, "category": "informational", "message": "Switching Protocols"}



...
```

Suppose the specified DPL pattern results in a single record-type field. In that case, nested fields are extracted to the root level by default. This behavior is configurable via the `autoFlatten` parameter.

Suppose you also provide a `lookupField` parameter in the API request. In that case, the specified field will be used to deduplicate the result if identical values appear in multiple records.

The following example shows a curl command for interacting with the Resource Store API using a platform token to test a DPL pattern:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern' \



-H 'accept: */*' \



-H 'Content-Type: multipart/form-data' \



-H 'Authorization: Bearer <platformtoken>' \



-F 'request={



"parsePattern":"JSON:json",



"lookupField":"code"



}' \



-F 'content=@http_status_codes.jsonl'
```

The response includes the number of records that matched the pattern and a preview of up to 100 records.

### Store lookup data

The API provides the `/platform/storage/resource-store/v1/files/tabular/lookup:upload` endpoint, which allows you to upload and store your lookup data as a tabular file in Grail.

The endpoint accepts input as `multipart/form-data` with a `content` part for the uploaded data and a `request` part for additional parameters. In the content part, you can submit your data in a text-based format. For details, see [Parse lookup data](#parse-lookup-data). The required parameters in the request part are:

* `parsePattern` for providing the DPL pattern to parse the uploaded data
* `lookupField` for defining the extracted field with the identifier of the record
* `filePath` as the fully qualified file path of the tabular file to store the lookup data in Grail

Use the `displayName` and `description` parameters to include additional meta information. For more details, see the Swagger API documentation.

If you want to update the contents of a file, you need to reupload it. If the `filePath` already exists, use the `overwrite` parameter.

The following example shows a curl command for interacting with the Resource Store API using a platform token to store your lookup data:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files/tabular/lookup:upload' \



-H 'accept: */*' \



-H 'Content-Type: multipart/form-data' \



-H 'Authorization: Bearer <platformtoken>' \



-F 'request={



"parsePattern":"JSON:json",



"lookupField":"code",



"filePath":"/lookups/http_status_codes",



"displayName":"My lookup data",



"description":"Description of my lookup data"



}' \



-F 'content=@http_status_codes.jsonl'
```

### Delete lookup data

You can use the `/platform/storage/resource-store/v1/files:delete` endpoint to delete files that are no longer needed. The only required parameter is the `filePath` parameter, referencing the file to be deleted. Note that deleting a file is irreversible.

The following example shows a curl command for interacting with the Resource Store API using a platform token to delete an existing lookup file:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files:delete' \



-H 'accept: */*' \



-H 'Content-Type: application/json' \



-H 'Authorization: Bearer <platformtoken>' \



-d '{"filePath": "/lookups/http_status_codes"}'
```

### Manage lookup files with DQL

With DQL, you can fetch the `dt.system.files` table to get a list of all accessible files stored in Grail:

```
fetch dt.system.files
```

If you want to search for specific files, you can add the [search](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search "DQL filter and search commands") or [filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") commands to the above example. The autocomplete suggestions within the DQL Code Editor will also help you find your files.

Use the [load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands") command if you want to inspect the contents of a file:

```
load "/lookups/http_status_codes"
```

## Enrich your data

You can use the [load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands") command to retrieve the tabular data from your lookup files in DQL and combine it with commands such as [lookup](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#lookup "DQL correlation and join commands") or [join](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join "DQL correlation and join commands") to add additional context to your observability data:

```
fetch spans



| lookup [ load "/lookups/http_status_codes" ],



Â  Â  sourcefield: http.response.status_code,



Â  Â  lookupField: code
```


---


## Source: advanced-permission-setup.md


---
title: Configure advanced permissions with security context
source: https://www.dynatrace.com/docs/platform/grail/organize-data/advanced-permission-setup
scraped: 2026-02-16T21:30:11.878830
---

# Configure advanced permissions with security context

# Configure advanced permissions with security context

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 20, 2025

This guide outlines Dynatrace permission set up for your data-from basic access controls to advanced configurations such as enriching data with `dt.security_context`, applying OpenPipeline processors for conditional access, and managing IAM policies with boundaries and templates for scalable control.

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## General permission setup

You can set up access controls for your data and entities using the guides below.

* [OneAgent permission setup](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Kubernetes permission setup](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#security-context-and-cost-allocation "Guides for telemetry enrichment on Kubernetes")

* [Logs permission setup](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Traces permission setup](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [Entities permission setup](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context")
* [OpenPipeline permission setup](/docs/platform/grail/organize-data/advanced-permission-setup#set-up-the-security-context-in-openpipeline "Configure advanced permissions with security context.")

## Set up the security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your specific data.

### Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes to your [data within OpenPipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
After configuring your pipeline, add `Set Security Context` processors on the `Permission` tab.

To define the `dt.security_context` attribute

1. Define a matching condition to filter records to assign the security context.

   For example: `matchesValue(http.route, â/basketâ)`
2. Add the `dt.security_context` for those records. The value of this attribute can be a literal value, for example `TeamA`, or a value copied from another field present on the record.
3. Verify your security context is set correctly.

   When new data arrives, the security context processors of OpenPipeline assign a `dt.security_context` attribute with the value `TeamA`. Open a Notebook to confirm that your security context processors handled the records. To verify, use a DQL query such as:

   `fetch logs | filter matchesValue(dt.security_context, "TeamA")`
4. Repeat this configuration for all the applicable data types (logs, metrics, spans).

Based on the created attribute, you can enforce security-related user and group policies, as described in the next section.

## Enforce access controls

You can [enforce access controls](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") to ensure that teams only access data that is relevant to them by using policy statements such as:

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH (â*-database-*â);



ALLOW storage:logs:read WHERE storage:dt.security_context = "TeamA" AND storage:dt.host_group.id MATCH ("shared_host_*");
```

You can also use [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") or [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating") for easier management of your access controls.

## Related topics

* [Set up Grail permissions for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Metadata enrichment of all telemetry originating from Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")


---


## Source: assign-permissions-in-grail.md


---
title: Permissions in Grail
source: https://www.dynatrace.com/docs/platform/grail/organize-data/assign-permissions-in-grail
scraped: 2026-02-17T04:55:58.649099
---

# Permissions in Grail

# Permissions in Grail

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Jan 26, 2026

Permissions can be assigned at the bucket, table, record, and field level. Without permissions, your users can't query data from Grail.

![Bucket and table permissions logic ](https://dt-cdn.net/images/new-bucket-and-table-permissions-diagram-1991-07901aebd8.png)

## Set up permissions

To set up the bucket and table-level permissions

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Policy management**.
3. Select **Create policy**.
4. Add the policy details:

   * **Name**
   * **Description**
   * **Policy statement**âuse the following format:

     ```
     ALLOW storage:buckets:read WHERE <conditions>;



     ALLOW <table permission> WHERE <conditions>;
     ```

   See below for supported bucket and table permissions.
5. Select **Create policy**.

## Bucket permissions

All bucket permissions need to start with `storage:buckets:read`. Their scope can be limited by a `WHERE` clause that includes one of the following operators:

* `=`, tests for equality.
* `STARTSWITH`, tests for a prefix.
* `IN`, tests for equality for any value of a list.
* `MATCH`, tests for pattern matching for any pattern of a list. It generalizes and expands both `STARTSWITH` and `IN` operators.

After the `WHERE` clause, you can filter your results by specifying buckets or tables:

* WHERE storage:bucket-name
* WHERE storage:table-name

The example below shows how to include only buckets prefixed with `default_` or the `common_logs` bucket.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*", "common_logs");
```

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Included queries

Logs only

This only applies if `Log Management & Analytics - Retain with Included Queries` is on your rate card.

Included queries

For more information about retained log data and included query log data, see [Retain with Included Queries](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

Bucket permissions let you define user group access to

* All retained log data.
  Queries may generate `Log Management & Analytics - Query` consumption.
* Only included query log data.
  Queries will not generate additional `Log Management & Analytics - Query` consumption.

To define access, you use the `storage:query-consumption` condition.
This condition has two possible values.

* `ON_DEMAND`: Queries can scan all retained data.
  This is the default value: if not specified, users have access to all retained data.
* `INCLUDED`: Queries can scan only included query data.

This can be combined with the `storage:bucket-name` condition to restrict access on a per-bucket level.

Example use cases

The following examples describe how to use bucket permissions to grant access to

* Included query data in all buckets.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";
  ```
* Included query data in a specific bucket (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="INCLUDED";
  ```
* Included query data in all buckets, and additionally all retained data in a specific bucket (`common_logs`).

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="INCLUDED";



  ALLOW storage:buckets:read WHERE storage:bucket-name="common_logs" AND storage:query-consumption="ON_DEMAND";
  ```
* All retained data in all buckets.

  ```
  ALLOW storage:buckets:read WHERE storage:query-consumption="ON_DEMAND";
  ```

  or

  ```
  ALLOW storage:buckets:read;
  ```

## Table permissions

Besides granting access to buckets, you also need to configure table permissions.

Table name

Permission

Affected DQL functions/commands

logs

storage:logs:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

events

storage:events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

security.events

storage:security.events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

metrics

storage:metrics:read

[timeseries](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands")

bizevents

storage:bizevents:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

spans

storage:spans:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

entities

storage:entities:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands"), [classicEntitySelector](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions."), [entityAttr](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions."), [entityName](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-name "A list of DQL general functions.")

smartscape

storage:smartscape:read

[smartscapeNodes](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeNodes "DQL Smartscape commands"), [smartscapeEdges](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands#smartscapeEdges "DQL Smartscape commands"), [getNodeName()](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeName "A list of DQL join functions."), [getNodeField()](/docs/platform/grail/dynatrace-query-language/functions/join-functions#getNodeField "A list of DQL join functions.")

dt.system.events

storage:system:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

user.events

storage:user.events:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

user.sessions

storage:user.sessions:read

[fetch](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#fetch "DQL data source commands")

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Bucket level permissions

You can restrict table permissions to certain buckets using the `WHERE` clause. For example:

```
ALLOW storage:logs:read WHERE storage:bucket-name="default_logs";
```

### Record level permissions

You can define fine-grained permissions for records that are stored in Grail. The permissions are added to the existing table permissions by adding the `WHERE` clause. For example:

```
ALLOW storage:logs:read WHERE storage:dt.security_context="TeamA";
```

Supported fields:

Field name

IAM condition

Supported IAM tables

`event.kind`

`storage:event.kind`

`events`, `security.events`, `bizevents`, `system`

`event.type`

`storage:event.type`

`events`, `security.events`, `bizevents`, `system`

`event.provider`

`storage:event.provider`

`events`, `security.events`, `bizevents`, `system`

`k8s.namespace.name`

`storage:k8s.namespace.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`k8s.cluster.name`

`storage:k8s.cluster.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`host.name`

`storage:host.name`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`dt.host_group.id`

`storage:dt.host_group.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`metric.key`

`storage:metric.key`

`metrics`

`log.source`

`storage:log.source`

`logs`

`dt.security_context`

`storage:dt.security_context`

`events`, `security.events`, `bizevents`, `system`, `logs`, `metrics`, `spans`, `entities`, `smartscape`, `user.events`, `user.sessions`

`gcp.project.id`

`storage:gcp.project.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`aws.account.id`

`storage:aws.account.id`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`azure.subscription`

`storage:azure.subscription`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`azure.resource.group`

`storage:azure.resource.group`

`events`, `security.events`, `bizevents`, `logs`, `metrics`, `spans`, `smartscape`

`frontend.name`

`storage:frontend.name`

`user.events`, `user.sessions`, `metrics`, `smartscape`

For details that are not available as a dedicated field, set the `dt.security_context` field either at the data source or in the processing pipeline.

### Combining bucket and record level permissions

You can combine both bucket and record level in your table permissions. For example this statement will provide access to all logs in the `unrestricted_logs` bucket and only specific records in the `default_logs` bucket:

```
ALLOW storage:logs:read WHERE storage:bucket-name="unrestricted_logs";



ALLOW storage:logs:read WHERE storage:bucket-name="default_logs" AND storage:dt.security_context="TeamA";
```

### Support for multiple values with MATCH operator

For efficiency reasons, record filters using the `=`, `IN` or `STARTSWITH` operators apply to fields holding a single string. You might have cases where the fields you want to use for filtering contain multiple values, in conjunction with a "for any value" set semantic. Such case is possible with the `MATCH` operator.

For example, the following statement will return results for records with `dt.security_context` holding either a `crn-70400-` prefixed string, or an array with a `crn-70400-` prefixed string as one of its elements.

```
// will match both "crn-70400-alpha" and ["crn-70131", "crn-70400-beta", "crn-70500"]



ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("crn-70400-*");
```

Note that you must use the `MATCH` operator to get "for any value" set semantic. Using `=`, `STARTSWITH` or `IN` when the field holds an array will always return `false`. If you expect your record filters might contain an array, use the `MATCH` operator in your IAM statements.

Example 1 - Grant team access to logs

As a Dynatrace administrator, I would like to ensure that each of my application teams can only access logs from their own Kubernetes namespace (records identifiable through `k8s.namespace.name`) and logs that belong to the basic infrastructure (records identifiable through `dt.host_group.id`).

Solution:

Create a policy for each team that grants them access to their logs.

Make sure that the user has access to all relevant buckets.

```
ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



ALLOW storage:logs:read WHERE storage:k8s.namespace.name="namespace1";



ALLOW storage:logs:read WHERE storage:dt.host_group.id MATCH ("shared_host_*");
```

Example 2 - Grant team access to logs from lambda functions

As a Dynatrace administrator, I would like to set up access for my application teams to access logs from lambda functions based on the team tag. For example `team` = `A`.

Solution:

1. Define the log processing rule with a security context that adds the `dt.security_context` field based on the lambda tag.
2. Create a policy for each team that grants them access based on the security context field.

   Make sure that the user has access to all relevant buckets.

   ```
   ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



   ALLOW storage:logs:read WHERE storage:dt.security_context MATCH ("TeamA");
   ```

Example 3 - Business analytics

As an administrator, I want to control access to business events that contain financial data. They can be identified using the `event.kind` field.

Solution:

Create a policy to grant access for specific users to records in `bizevents` for the specific `event.kind` (`Opportunity Field History`).

Make sure that the user has access to all relevant buckets.

```
ALLOW storage:buckets:read WHERE â¦ // Ensure that the user has access to all relevant buckets



ALLOW storage:bizevents:read WHERE storage:event.kind="Opportunity Field History";
```

Example 4 - System events

As an administrator, I want to provide selected users access to billing events but not to any other system events.

Solution:

Create a policy to grant access to records in `dt_system_events` for the specific `event.type` with the value `BILLING_EVENT`.

```
ALLOW storage:buckets:read WHERE storage:bucket-name="dt_system_events"



ALLOW storage:system:read WHERE storage:event.kind="BILLING_EVENT"
```

### Record permission limits

The following configuration limitations apply to record permissions:

* Number of statements per policy (100)
* Number of policies per account (200)

### Permissions for entities

Permissions for entities allow you to define IAM policies that control data access on entities.

In contrast to monitoring data, entity permissions only allow filtering for the `dt.security_context` field.

For more information, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").

## Field permissions

You can use field permissions to hide fields that might contain sensitive data. For this purpose, we provide fieldsets. A field is considered sensitive when it's part of a fieldset. Once a field is part of a fieldset, only users with the right permissions can use it in DQL queries for filtering and grouping. For other users, it won't show up in the query results.

You require permission to access fieldsets in order to use sensitive fields. For example, if you want to use `builtin-sensitive-spans` fields in DQL queries, you need the following permission:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="builtin-sensitive-spans"
```

The three predefined fieldsets are:

* `builtin-sensitive-spans` - drops all fields on `spans` that are considered sensitive
* `builtin-request-attributes-spans` - drops all fields on `spans` that contain request attribute data that was marked sensitive
* `builtin-sensitive-user-events-and-sessions` - drops all fields in `user.events` and `user.sessions` that are considered sensitive

* The predefined fieldsets apply to `spans`, `user.events` and `user.sessions` only. They don't apply to `logs` or `events`.
* You can define your custom fieldsets, and to which scope they apply (either buckets, or tables, otherwise all buckets and tables).
* If you don't have sufficient permissions, sensitive fields won't be shown in the result.
* You can use the field permissions with `smartscape`, but not with `entities`.

### Define custom fieldsets via API

You can manage your custom fieldsets via REST API

1. In Dynatrace, search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail - Fieldsets**.
3. Authenticate with your API token.  
   For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
4. Perform one of the following actions.

To do this

Go to **Fieldsets** and select this

Get all fieldsets

**GET /fieldsets**

Create a new fieldset

**POST /fieldsets**

Get fieldsets by UID

**GET /fieldsets/{fieldsetUid}**

Update a fieldset. All fields will be overwritten.

**PUT /fieldsets/{fieldsetUid}**

Delete a fieldset

**DELETE /fieldsets/{fieldsetUid}**

#### Example

This call creates the fieldset `sensitive-fields-retail`, removing the `credit_card` and `DOB` fields from DQL query results in the `logs_retail` bucket.

##### Request URL

```
POST https://myapps.mydomain.com/platform/storage/fieldsets/v1/fieldsets
```

##### Request body

```
{



"name": "sensitive-fields-retail",



"description": "Sensitive fields retail",



"enabled": true,



"scope": "BUCKET",



"fields": [



"credit_card",



"DOB"



],



"buckets": [



"logs_retail"



]



}
```

To unmask the `credit_card` and `DOB` fields, you need the following permission:

```
ALLOW storage:fieldsets:read WHERE storage:fieldset-name="sensitive-fields-retail"
```

## File permissions

Preview

To manage your lookup data stored in Grail, you require the following permissions:

* `storage:files:read` - to read lookup data data via DQL.
* `storage:files:write` - to upload lookup data via REST API.
* `storage:files:delete` - to delete lookup data via REST API.

All of these permissions support the `storage:file-path` condition using one of the following operators:

* `=` (equals) - indicating an exact match.
* `IN` - indicating a range.
* `startsWith` - with an expression put in quotation marks.

The following example shows how to provide full access to lookup data stored in `/lookups/`.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:write WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:delete WHERE storage:file-path startsWith "/lookups/";
```

You can use the folder-like structure to manage access to different subsets of your lookup files with permissions, as in the following example.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/public/";
```

To give read-only access to a specific file, you could also use a permission similar to the following.

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/http_status_codes";
```

For more information, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Predefined global policies

There are several predefined global policies, each set per table (logs, events, bizevents, security events, metrics, entities, spans), and three additional, general policies:

* Read all data
* Read default monitoring data
* Read all system data

### Access to all logs

This policy provides access to all logs from Grail, and narrows the bucket permission with a `WHERE` condition that limits the results to the log table.

This statement provides access to all built-in and custom buckets.

```
ALLOW storage:buckets:read WHERE storage:table-name= "logs";



ALLOW storage:logs:read;
```

### Read all data

This permission statement gives you access to all tables and all buckets, therefore it needs to be used only in justified cases.

```
ALLOW storage:buckets:read;



ALLOW storage:system:read,



storage:events:read,



storage:security.events:read,



storage:logs:read,



storage:metrics:read,



storage:entities:read,



storage:bizevents:read,



storage:spans:read,



storage:smartscape:read;
```

### Read all default monitoring data

This policy retrieves all default monitoring data.

In the first line, this policy statement gives access to all default buckets. The `WHERE` condition narrows the search to buckets whose name starts with `default`. Subsequently, the next lines list all the needed table permissions.

This statement does not give access to custom buckets.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("default_*");



ALLOW storage:events:read,



storage:logs:read,



storage:metrics:read,



storage:entities:read,



storage:bizevents:read,



storage:spans:read,



storage:smartscape:read;
```

### Read all system data

This permission statement first narrows the results to system buckets, whose name starts with `dt`. Then, it gives you access to all tables that contain system data, for example audit `events`, billing `events`, and query execution events. It can be useful for system admins.

```
ALLOW storage:buckets:read WHERE storage:bucket-name MATCH ("dt_*");



ALLOW storage:system:read;
```

## Best practices

* Ensure that you also have bucket permissions.
* If there is an unconditional table permission in any other policy available for a user, the `WHERE` clause is irrelevant and the user will always be able to view all records from that table.
* Use the `MATCH` operator to simplify your statements instead of combination of `=`, `IN` and `STARTSWITH`, as there is a 100-statement limit per policy.
* When using the `MATCH` operator with wildcards (`*`) in record filters, it's best to place wildcards before or after word separators such as: `-`, `_`, `.`, or `/`. This is because `matchesValue` used in DQL queries, performs better when word separators are present. For example, `... WHERE storage:dt.host_group.id MATCH ("db-tech-*")` is more efficient than `... WHERE storage:dt.host_group.id MATCH ("db-tech*")`.
* Make sure to combine logs, events and metrics where applicable (to further save on the 100 statement policy [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax#iam-example-statements-combined "IAM policy statement syntax."))
* When you create custom fieldsets, make sure to avoid including any essential fields in your fieldset (such as `timestamp`, `id`, `content`).

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.")


---


## Source: organize-data.md


---
title: Organize data
source: https://www.dynatrace.com/docs/platform/grail/organize-data
scraped: 2026-02-17T05:03:27.201979
---

# Organize data

# Organize data

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 02, 2025

## Grail data model

Dynatrace Grail organizes data in buckets, tables, and views to ensure efficient storage, flexible access, and scalable querying.

Buckets are the logical storage units where records are stored. Buckets are always associated with a specific record type, such as logs, events, or spans. Each record type has a predefined built-in bucket. Administrators can create custom buckets to optimize performance, apply different retention times, or meet specific compliance requirements.

Tables group records by type. Fetching a table retrieves records from all corresponding buckets. For example, the `logs` table includes all log records, regardless of whether they're stored in the default logs bucket or a custom one. This abstraction allows you to access data uniformly, independent of the underlying storage structure.

System tables such as `dt.system.buckets`, `dt.system.data_objects`, and `dt.system.files` represent information that is not stored in buckets.

Views are virtual tables defined by queries on existing tables. They provide a filtered or transformed perspective of the underlying records. For example, you can use `dt.entity.*` views to query classic entities.

## Built-in Grail buckets

There is a set of predefined built-in buckets that cannot be modified, including:

* Default buckets, whose name starts with `default_`
* System buckets, whose name starts with `dt_`

### Built-in buckets with corresponding retention periods

This section has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

These are examples of built-in buckets with corresponding retention periods.
For a full list of available built-in buckets, run this DQL query:

```
fetch dt.system.buckets



| filter startsWith(name, "default_") or startsWith(name, "dt_")
```

Run in Playground

Name

Table

Retention

`default_events`

events

35 days

`default_securityevents_builtin`

security.events

3 years

`default_securityevents`

security.events

1 year

`default_bizevents`

bizevents

35 days

`default_logs`

logs

35 days

`default_metrics`

metrics

15 months

`default_spans`

spans

10 days

`dt_system_events`

dt.system.events

1 year

`default_application_snapshots`

application.snapshots

10 days

## Custom Grail buckets

You can create a bucket tailored to your needs. Grail buckets behave like folders in a file system and are designed for records that should be handled together. For example, you might need to store together:

* Data with the same retention period
* Data that needs to be queried/analyzed together
* Data that needs to be deleted at the same time

Defining buckets can improve query performance by reducing query execution time and the scope of data read. Finally, having your data stored in a bucket streamlines your permission management because you can easily provide a user group or single users with access to needed data.

The default limit per environment is 80 buckets, typically satisfying ingestion volumes up to 5TB/day per table (e.g. logs). For larger ingestion volumes, more buckets can be requested in coordination with your Dynatrace account team.

For custom buckets, the possible retention periods range from 1 day to 10 years, with an additional week.

Shortening the retention period on update requests will delete the data that is over the new period.  
Any operation that deletes data is a long-running process. Deleting data can take up to a few days, depending on the amount of data you've deleted.

## Manage custom Grail buckets

To manage your buckets, ensure that you have configured the following permissions:

* `storage:bucket-definitions:read`
* `storage:bucket-definitions:write`
* `storage:bucket-definitions:delete`
* `storage:bucket-definitions:truncate`

With [**Storage Management**ï»¿](https://dt-url.net/s4038cj) you can:

* Create custom buckets for events, security events, bizevents, logs, and spans.
* Edit custom buckets.
* Delete custom buckets.

### Creating new buckets with Storage Management

To create a new custom Grail bucket with Storage Management you need to specify:

* Unique bucket name. It has to be between 3-100 characters long and has to start with a letter. The bucket name can only contain lowercase alphanumeric characters, underscores and hyphens. The bucket name can't be edited or changed at a later time.
* Display name. You can use this field to describe your bucket.
* Retention period between 1-3657 days.

### Manage custom Grail buckets via REST API

To manage your custom Grail buckets via REST API

1. Search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail Storage Management**.
3. Authenticate with your API token.

   For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
4. Perform one of the following actions.

   | To do this | Go to **Bucket Definitions** and select this |
   | --- | --- |
   | List my buckets | **GET/bucket-definitions** |
   | Create buckets | **POST/bucket-definitions** |
   | Update buckets | **PATCH/bucket-definitions/{bucketName}**   or   **PUT/bucket-definitions/{bucketName}** |
   | Truncate buckets | **POST/bucket-definitions/{bucketName}:truncate** |
   | Delete buckets | **DELETE/bucket-definitions/{bucketName}** |

The delete buckets operation is irreversible. This operation will remove the content of a given bucket and then delete the bucket itself. Delete is an asynchronous task. Runtime will depend on the amount of data that has to be removed. The status of this operation can be tracked via the status field within `GET bucket definitions`.
Status will show **deleting** as long as data will be drained, and finally the bucket will be deleted. Afterwards, the bucket will cease to exist.
This operation can be executed on all types of buckets, except buckets where **bucketName** starts with `dt_` or `default_`. Before a bucket is deleted, checks are performed to verify that the bucket is not in use. To delete a bucket, you need the `storage:bucket-definitions:delete` permission.

See when to [create custom buckets and how to allow access to them](/docs/platform/upgrade#organize-your-data "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

## Related topics

* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")


---


## Source: querying-monitored-entities.md


---
title: Query monitored entities in Grail
source: https://www.dynatrace.com/docs/platform/grail/querying-monitored-entities
scraped: 2026-02-17T05:12:48.042864
---

# Query monitored entities in Grail

# Query monitored entities in Grail

* Latest Dynatrace
* Reference
* 13-min read
* Updated on Oct 13, 2025

This is a guide to effectively using Dynatrace Query Language (DQL) to query monitored entities. This involves using generic DQL features such as expanding arrays, joining data using the `lookup` command, and using the built-in parse functionality.

## Query entity types

To query monitored entities by their respective type, you can use the `dt.entity.*` views.

To initiate the query, start with a blank query in your notebooks and enter `fetch dt.entity`. This triggers an auto-complete dialog where you can select the desired entity type.

![Example of auto-complete for entity types.](https://dt-cdn.net/images/ft-entity-2-1439-af70ed8841.png)

For example, executing the `fetch dt.entity.host` query retrieves all host entities. By default, entity records include the ID and entity name.

```
fetch dt.entity.host
```

`entity.name`

`id`

HOST-1

HOST-123

HOST-2

HOST-456

HOST-3

HOST-789

HOST-4

HOST-101

HOST-5

HOST-111

HOST-6

HOST-131

HOST-7

HOST-141

To include additional details, you can use the `fieldsAdd` command. As you start typing, the auto-complete feature suggests available fields for the entity type.

Another way to get started is to use one of the built-in topology query snippets.

![Example of how to get started by using built-in topology query snippets.](https://dt-cdn.net/images/topology-1447-687b6417ca.png)

## Query relationships

Relationships are exposed as fields and can be added similarly to other fields. For instance, you can add the `runs` relationship to your host records to obtain a list of all entities running on the host.

```
fetch dt.entity.host



| fieldsAdd runs
```

`entity.name`

`id`

`runs`

HOST-1

HOST-123

runs: Complex record

HOST-2

HOST-456

runs: Complex record

HOST-3

HOST-789

runs: Complex record

The `runs` field is a nested record that contains a field for each entity type running on a specific host. Depending on the cardinality, these fields are either strings representing a single entity ID or arrays of strings representing a list of entity IDs. In notebooks, select a nested record in the results list to see its contents.

If you only want to see process groups running on that host, you can specify this in the `fieldsAdd` command. The auto-complete feature will provide a list of possible identifier types.

Selecting a type refines the query to only return an array containing the process group IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.process_group]
```

`entity.name`

`id`

`runs[dt.entity.process_group]`

HOST-1

HOST-123

runs: PROCESS\_GROUP-D123, PROCESS\_GROUP-567, PROCESS\_GROUP-012

HOST-2

HOST-456

runs: PROCESS\_GROUP-D234, PROCESS\_GROUP-234, PROCESS\_GROUP-F10

HOST-3

HOST-789

runs: PROCESS\_GROUP-D567, PROCESS\_GROUP-789, PROCESS\_GROUP-123

The field names for relationships differ from the original relationship names in the previous Dynatrace. Instead of using a single name prefixed with `fromRelationship` and `toRelationship`, the fields have different names on both sides.

See the [relationship mapping table](#relationship-mapping-table) below to understand how second-generation relationships are represented as DQL fields.

Note that 1:n relationships only return 100 entity IDs per type, per record. In such cases, we recommend using `classicEntitySelector()` instead.

## Entity lookups

You can use the `lookup` command to join data from related entities.

For example, to include the host tags with your service instances, you can access the host from a service instance by following the `runs_on` relationship.

```
fetch dt.entity.service_instance



| fieldsAdd runs_on[dt.entity.host]
```

`entity.name`

`id`

`runs_on[dt.entity.host]`

Mapped Instance for answer\_queue on ActiveMQ Artemis

SERVICE\_INSTANCE-1AB2

HOST-1

Mapped Instance for Requests executed in the background threads of eT-demo-1-BussinessBackend

SERVICE\_INSTANCE-A123

HOST-2

It's important to note that service instances always run on a single host, which means that you obtain a single host ID per service instance record. This allows you to use the `lookup` command to add the hostname to your records. The hostname is added as the `lookup.entity.name` field.

```
fetch dt.entity.service_instance



| fieldsAdd runs_on[dt.entity.host]



| lookup sourceField:`runs_on[dt.entity.host]`, lookupField:id, [ fetch dt.entity.host ]
```

`entity.name`

`id`

`runs_on[dt.entity.host]`

`lookup.entity.name`

`lookup.id`

Mapped Instance for answer\_queue on ActiveMQ Artemis

SERVICE\_INSTANCE-2AB1

HOST-1

AB1-abc

HOST-1

Mapped Instance for Requests executed in the background threads of eT-demo-1-BussinessBackend

SERVICE\_INSTANCE-B123

HOST-2

BA1-cba

HOST-2

Mapped Instance for :80

SERVICE\_INSTANCE-C321

HOST-3

BA1-cba

HOST-2

## Expand relationships

Hosts can run multiple service instances, so the `runs[dt.entity.service_instance]` field is an array of entity IDs.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

dw123

HOST-1

SERVICE\_INSTANCE-AB123

dw123

HOST-1

SERVICE\_INSTANCE-CB123

dw123

HOST-1

SERVICE\_INSTANCE-DB123

abc/123

HOST-2

SERVICE\_INSTANCE-AB902

The `lookup` command doesn't apply to arrays of IDs, so you need to use the `expand` command first to retrieve individual records per service instance ID.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

dw123

HOST-1

SERVICE\_INSTANCE-DB123

dw456

HOST-2

SERVICE\_INSTANCE-BA987

dw789

HOST-3

SERVICE\_INSTANCE-CA687

dw652

HOST-4

SERVICE\_INSTANCE-1AB2

In this example, the first record expands into three. Now you can use the `lookup` command to get the service instance details that you include in the `lookup` field.

```
fetch dt.entity.host



| fieldsAdd runs[dt.entity.service_instance]



| expand runs[dt.entity.service_instance]



| lookup sourceField:`runs[dt.entity.service_instance]`, lookupField:id, [ fetch dt.entity.service_instance]
```

`entity.name`

`id`

`runs[dt.entity.service_instance]`

`lookup.entity.name`

`lookup.id`

dw123

HOST-1

SERVICE\_INSTANCE-AB123

Mapped instance for easytravelazure-weather-service

SERVICE\_INSTANCE-AB123

dw123

HOST-1

SERVICE\_INSTANCE-CB123

Mapped Instance for weather-service-restify

SERVICE\_INSTANCE-CB123

dw123

HOST-1

SERVICE\_INSTANCE-DB123

Mapped Instance for easytravelazure-weather-express

SERVICE\_INSTANCE-DB123

abc/123

HOST-2

SERVICE\_INSTANCE-AB902

Mapped Instance for easytravel-frontend

SERVICE\_INSTANCE-AB902

## Entity tags

Entity tags consist of up to three values: context, key, and value. Dynatrace creates a string representation of these values in the following format:

`[<context>]<key>:<value>`

* All occurrences of the `[`, `]`, and `:` characters need to be escaped using the `\` character.
* The `tags` field returns the string representations of these fields.

The following query example retrieves a list of host entity tags.

```
fetch dt.entity.host



| expand tags, alias:tag



| fields tag
```

`tag`

AppSec:Node.js

[Azure]tenant:CustomerA

HostName:dw123

AppSec:.NET

[AWS]created\_at:2023-07-07T12:20:10Z

[Environment]tema:cpn

You can use the `expand` command to optimize tag filtering. This example filters hosts based on a specific cluster name.

```
fetch dt.entity.host



| expand tags



| filter contains(tags, "[Environment]Cluster.Name:prod-eu-west-6-ireland")
```

`entity.name`

`id`

`tags`

HOST-1

HOST-C2

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-2

HOST-C3

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-3

HOST-C4

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-4

HOST-C5

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

HOST-5

HOST-C6

tags:[Environment]Cluster.Name:prod-eu-west-6-ireland

If you need structured access to the key, context, or value, you can use the following DPL parse expression to split the string representation into individual fields.

```
fetch dt.entity.host



| expand tags, alias:tag_string



| parse tag_string, """(('['LD:tag_context ']' LD:tag_key (!<<'\\' ':') LD:tag_value)|(LD:tag_key (!<<'\\' ':') LD:tag_value)|LD:tag_key)"""
```

`entity.name`

`id`

`tag_string`

`tag_context`

`tag_key`

`tag_value`

HOST-1

HOST-73

Maxk:WebService2-ABC

undefined

Maxk:WebService2-ABC

undefined

HOST-1

HOST-73

testtests:testspreiser

undefined

testtests:testspreiser

undefined

HOST-1

HOST-73

Maxk:WebService3-ABC

undefined

Maxk:WebService3-ABC

undefined

## List fields and relationships

Use the `describe` command to obtain a list of fields and relationships for each entity view.

For example, to retrieve a list of all fields and relationships for the `service_instance` entity view, enter `describe dt.entity.service_instance`:

```
describe dt.entity.service_instance
```

Take this information into account when working with different fields:

* Most entity fields have the same names as in the API v2 environment (for example, gcpZone and oneAgentCustomName).
* The first and last observation timestamp of an entity is stored in the lifetime field, represented as a timeframe type comprising a start and end timestamp. The lifetime of an entity needs to overlap with the query timeframe for the entity to be included in the query.
* Several entity names are prefixed with 'entity.' (for example, `entity.conditional_name`)
* Relationships are returned as records, to learn more about them, see [entity relationships](/docs/semantic-dictionary/model/dt-entities#entity-relationships "Get to know the Semantic Dictionary models related to topology.").

The `describe` command is a valuable tool to explore the Grail data schema.

```
describe dt.entity.service_instance



| filter in(data_types, "record")
```

`field`

`data_types`

belongs\_to

record

runs\_on

record

sends\_to

record

icon

record

receives\_from

record

instance\_of

record

## Permissions

You need the `storage:entities:read` permission to query entities.

Grail doesn't apply management zone filters. Users having the `storage:entities:read` permission can query all entities.

## Entity selectors

You can use the `classicEntitySelector()` function to simplify starting DQL entity queries. This command takes an entity selector as a string argument and provides a list of entity IDs in return. You can use this list to filter entities based on ID.

For example, you can filter service instances running on hosts with a specific tag.

```
fetch dt.entity.service



| filter in(id, classicEntitySelector("type(service), fromRelationship.runsOnHost(type(host), tag([AWS]Category:ABC))"))
```

`entity.name`

`id`

123

123

123

123

123

123

123

123

123

123

You can also obtain this result using native DQL with the following query.

```
fetch dt.entity.service



| fieldsAdd host.id = runs_on[dt.entity.host]



| expand host.id



| lookup sourceField:host.id, lookupField: id, fields:host.tags=tags, [ fetch dt.entity.host]



| expand host.tags



| filter host.tags == "[AWS]Category:ABC"
```

`entity.name`

`id`

`host.id`

`host.tags`

123

123

123

123

123

123

123

123

123

123

123

123

123

123

123

123

This query has limitations, such as returning only 100 hosts per service entity, and is generally more complex than the previous example using the `classicEntitySelector` function.

### Filtering along relationships

When your query evaluates relationships, we recommend using the [`classicEntitySelector`](/docs/platform/grail/dynatrace-query-language/functions/general-functions#classic-entity-selector "A list of DQL general functions.") function instead of native DQL queries.

In the following examples, the native DQL query will be slower and might yield incomplete results compared to the `classicEntitySelector` query:

```
// fetch all hosts that run Java processes



// using native DQL



fetch dt.entity.host



| expand pgi=contains[dt.entity.process_group_instance]



| filter pgi in [



fetch dt.entity.process_group_instance



| filter matchesValue(softwareTechnologies, "*JAVA*")



| fields id



]
```

```
// fetch all hosts that run Java processes



// using classicEntitySelector()



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))
```

### Combine `classicEntitySelector` with native DQL filters

If you already use the `classicEntitySelector` function, it is better to add all filter criteria into the function call rather than add additional native filter statements. The mixed query is slower than the query that contains all filter conditions in the entity selector.

```
// fetch all LINUX hosts that run Java processes



// using a mix of classicEntitySelector and native DQL filters



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))



| fieldsAdd osType



| filter osType == "LINUX"
```

```
// fetch all LINUX hosts that run Java processes



// using only classicEntitySelector



fetch dt.entity.host



| filter in (id, classicEntitySelector("type(host),osType(LINUX),toRelationship.isProcessOf(type(PROCESS_GROUP_INSTANCE),softwareTechnologies(JAVA))"))



| fieldsAdd osType
```

## Relationship mapping table

Entity relationships in the previous Dynatrace (for example, the environment API v2) are mapped to the new names in DQL records according to the following table.

Relationship name

From > To

To > From

belongsTo

belongs\_to

contains

calls

calls

called\_by

candidateTalksWith

called\_by

calls

hostsComputeNode

hosts

hosted\_by

indirectlySendsToQueue

indirectly\_sends\_to

indirectly\_receives\_from

isAccessibleBy

accessible\_by

can\_access

isApplicationMethodOf

belongs\_to

contains

isApplicationMethodOfGroup

belongs\_to

contains

isApplicationOfSyntheticTest

monitored\_by

monitors

isAzrAppServicePlanOf

contains

belongs\_to

isAzrEventHubNamespaceOfEventHub

contains

belongs\_to

isAzrMgmtGroupOfAzrTenant

belongs\_to

contains

isAzrServiceBusNamespaceOfQueue

contains

belongs\_to

isAzrServiceBusNamespaceOfTopic

contains

belongs\_to

isAzrSQLDatabaseOfElasticPool

belongs\_to

contains

isAzrSqlServerOfDatabase

contains

belongs\_to

isAzrSqlServerOfElasticPool

belongs\_to

contains

isAzrStorageAccountOfAzrEventHub

contains

belongs\_to

isAzrSubscriptionOfAzrMgmtGroup

belongs\_to

contains

isAzrSubscriptionOfAzrTenant

belongs\_to

contains

isAzrSubscriptionOfCredentials

contains

belongs\_to

isBalancedBy

balanced\_by

balances

isBoshDeploymentOfHost

contains

belongs\_to

isCfFoundationOfHost

contains

belongs\_to

isCgiOfCa

belongs\_to

contains

isCgiOfCai

belongs\_to

contains

isCgiOfCluster

belongs\_to

contains

isCgiOfHost

belongs\_to

contains

isCgiOfNamespace

belongs\_to

contains

isChildOf

child\_of

parent\_of

isClusterOfCa

cluster\_of

clustered\_by

isClusterOfCai

cluster\_of

clustered\_by

isClusterOfCni

cluster\_of

clustered\_by

isClusterOfHost

cluster\_of

clustered\_by

isClusterOfKubernetesSvc

cluster\_of

clustered\_by

isClusterOfNamespace

cluster\_of

clustered\_by

isClusterOfNode

cluster\_of

isClusterOfPg

clustered\_by

cluster\_of

clustered\_by

isCnpOfCai

belongs\_to

contains

isDatastoreOf

belongs\_to

contains

isDeviceApplicationMethodOf

belongs\_to

contains

isDeviceApplicationMethodOfGroup

belongs\_to

contains

isDiskOf

belongs\_to

contains

isDockerContainerOf

contains

belongs\_to

isDockerContainerOfPg

contains

belongs\_to

isEbsVolumeOf

belongs\_to

contains

isGroupOf

group\_of

groups

isHostGroupOf

group\_of

groups

isHostOfContainer

hosts

hosted\_by

isInstanceOf

instance\_of

instantiates

isKubernetesSvcOfCa

balances

balanced\_by

isKubernetesSvcOfCai

balances

balanced\_by

isLocatedIn

belongs\_to

contains

isMainPgiOfCgi

belongs\_to

contains

isMemberOf

belongs\_to

contains

isMemberOfScalingGroup

belongs\_to

contains

isNamespaceOfCa

contains

belongs\_to

isNamespaceOfCai

contains

belongs\_to

isNamespaceOfCni

contains

belongs\_to

isNamespaceOfCnp

contains

belongs\_to

isNamespaceOfKubernetesSvc

contains

belongs\_to

isNamespaceOfPg

contains

belongs\_to

isNamespaceOfService

contains

belongs\_to

isNetworkClientOf

calls

called\_by

isNetworkClientOfHost

calls

called\_by

isNetworkClientOfProcessGroup

calls

called\_by

isNetworkInterfaceOf

belongs\_to

contains

isNodeOfHost

belongs\_to

contains

isOpenstackAvZoneOf

belongs\_to

contains

isPartOf

belongs\_to

contains

isPgAppOf

belongs\_to

contains

isPgiOfCgi

belongs\_to

contains

isPgOfCa

belongs\_to

contains

isPgOfCai

belongs\_to

contains

isPgOfCg

belongs\_to

contains

isProcessOf

belongs\_to

contains

isProcessRunningOpenstackVm

belongs\_to

contains

isRuntimeComponentOf

belongs\_to

contains

isSameAs

same\_as

same\_as

isServedByDcrumService

served\_by

serves

isServiceMethodOf

belongs\_to

contains

isServiceMethodOfService

belongs\_to

contains

isServiceOf

belongs\_to

contains

isServiceOfProcessGroup

belongs\_to

contains

isSiteOf

contains

belongs\_to

isSoftwareComponentOfPgi

belongs\_to

contains

isStepOf

belongs\_to

contains

isUserActionOf

belongs\_to

contains

listensOnQueue

belongs\_to

contains

manages

manages

managed\_by

monitors

monitors

monitored\_by

propagatesTo

propagates\_to

propagated\_from

receivesFromQueue

receives\_from

sends\_to

runsOn

runs\_on

runs

runsOnHost

runs\_on

runs

runsOnProcessGroupInstance

runs\_on

runs

runsOnResource

runs\_on

runs

sendsToQueue

sends\_to

receives\_from

talksWithCandidate

calls

called\_by

affects

affects

affected\_by

isRelatedTo

related\_to

related\_to

## Troubleshooting

* **The DQL query returns different or fewer entities than API v2 environment**
  Verify that you are using the same query timeframe `fetch dt.entity.*`. The `classicEntitySelector()` function only returns entities that have a lifetime that overlaps with the query timeframe. By default, DQL queries are executed for the last 2 hours, whereas the default timeframe in the API environment is 72 hours.

## Related topics

* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")
* [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")


---


## Source: smartscape-on-grail.md


---
title: Smartscape on Grail
source: https://www.dynatrace.com/docs/platform/grail/smartscape-on-grail
scraped: 2026-02-17T04:55:41.028101
---

# Smartscape on Grail

# Smartscape on Grail

* Latest Dynatrace
* Explanation
* Updated on Jan 16, 2026
* Preview

Smartscape on Grail is a Grail-native storage that automatically records topological data, such as monitored entities and relationships.

Smartscape on Grail uses the power of DQL queries to:

* Represent entities as nodes.
* Represent relationships as edges.
* Traverse from one node to another.

This gives you deeper insight into your data records and allows you to manipulate and extract necessary information for further analysis.

## Access Smartscape on Grail

Smartscape on Grail is fully integrated into DQL and introduces new commands and functions that you can use to:

* Query nodes and edges.
* Enrich monitoring data, such as logs and spans, with entity details.
* Navigate the topology.
* Filter your topology based on complex relations.

Costs and DPS license

Smartscape on Grail is included in the DPS license. This means that data returned from Smartscape queries doesn't incur any additional cost.

## Smartscape on Grail features

### Mutable data

The data stored in traditional bucketsâsuch as logs, events, spans, or metric data pointsâis ingested for a particular timestamp and never changes. In comparison, Smartscape nodes and edges are mutable and can change over time.

### Smartscape IDs

Smartscape nodes are identified via an ID, represented by a Grail datatype `Smartscape ID`. Smartscape IDs are updated regularly through the upsert events.

A Smartscape ID consists of the entity type and a 16-symbol long number. It can be represented by a following string:

* `ENTITY_TYPE-000000000000007B`

The Smartscape type is fully compatible with its string representation, meaning that you can compare a string to Smartscape ID.

### Type

Every node has a type field that describes the entity type and determines the schema of the entity. The Semantic Dictionary contains the schema for each of the types. By convention, node types are always formatted in uppercase, like `HOST`, `K8S_NAMESPACE`, and `AWS_EC2_INSTANCE`.

### Lifetime

Because nodes are updated regularly, they don't have a single timestamp field. Instead, nodes have two timeframe fields that represent the node's lifetime:

* `lifetime.start`: the first time when the node was discovered.
* `lifetime.end`: the time when the node was last observed.

While the `lifetime.start` field will remain unchanged, the `lifetime.end` field will be continuously updated with every incoming upsert event as long as the node is still being observed.

Based on the query timeframe, you will see only those nodes that have a lifetime overlapping with the query timeframe. For example, a node with a `lifetime.end` field containing yesterday's data won't be included in a query result for the last 2 hours.

### Edges

Edges are relationships that connect two nodes to each other. An edge always stores an edge type (such as `runs_on`, `calls` or `relates_to`), and two IDs of two different nodes.

How an edge is stored on a node depends on whether the edge is static or dynamic:

* Static: the edge inherits the node's lifetime.
* Dynamic: the edge is recorded for a specific point in time.

Edges stored statically are included in results where the query timeframe overlaps with the node's lifetime, whereas dynamic edges are included in query results based on a timeframe when the edge was recorded.

Static edges are mostly based on configuration, such as when a disk is configured to be attached to a specific host. Dynamic edges are typically based on monitoring signals that reveal a specific relationship between nodes, such as when a service based on traces calls another service.

### Node references

All static edges can be accessed through the source node via the `references` field. While this field is hidden by default, you can display it and use it in queries with the help of the `fieldsAdd` command.

You can see the examples of using the `references` field below:

Display the references field by using fieldsAdd for all nodes

```
smartscapeNodes "*"



| fieldsAdd references
```

Summarize containers by the host ID they're running on

```
smartscapeNodes CONTAINER



| summarize by:references[runs_on.host], count()
```

### Data retention

Data retention is fixed at 35 days. This means that nodes whose `lifetime.end` is older than 35 days will be deleted, including all static edges. Dynamic edges will be cleaned up after 35 days as well.

### Signal's connection to Smartscape nodes

A signal's fields that start with `dt.smartscape.__type__` and contain Smartscape IDs indicate that the signal has originated within a given node. A single signal can have multiple `dt.smartscape.__type__` fields.

Optionally, a signal can also have:

* A `dt.smartscape_source.id` field that points to the exact source that produced the signal.
* A `dt.smartscape_source.type` field that describes the type of the entity that produced the signal.

### Tags

Each node has a special field called `tags` that contains different nested fields recognized as tags.

Currently, tags can only be set at the data source. That means that, for example:

* Kubernetes monitoring adds labels and annotations as tags.
* Cloud monitoring adds AWS tags.
* OneAgent adds agent tags.

### Security context

Similar to other data stored in Grail, Smartscape nodes have a `dt.security_context` field that can contain multiple values.

The `dt.security_context` field is an optional node field and is empty by default, since the regular permission fields are fully supported and often sufficient.

### Field permissions

You can configure and use [fieldsets](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-fields "Find out how to assign permissions to buckets and tables in Grail.") with the `smartscape` table to apply filters to all data returned by Smartscape commands (`smartscapeNodes` and `smartscapeEdges`). Be aware that only certain fields can be filtered out for all entity types simultaneously.

See the example of a field set configuration below:

Define a new fieldset to filter Kubernetes configuration details

To define a new fieldset that filters the Kubernetes configuration details that are stored in the `k8s.object` field, you can use the API with the following request:

```
POST /fieldsets



{



"name": "sensitive-field-k8s-object",



"description": "Make k8s.object sensitive",



"enabled": true,



"scope": "TABLE",



"fields": [



"k8s.object"



],



"tables": [



"smartscape"



]



}
```

Now only users that have the permission `ALLOW storage:fieldsets:read WHERE storage:fieldset-name="sensitive-field-k8s-object"` will be able to read the details of this field.

### Classic entity IDs

Node types used by Smartscape on Grail might be different from classic entity types. This means that the entity or node ID might also be different (for example, `CLOUD_APPLICATION_INSTANCE` is called `K8S_POD` in Smartscape on Grail). To avoid confusion, Smartscape nodes include an `id_classic` field that contains the entity ID of the corresponding classic entity. Classic entity IDs are available for K8s entities, core entities, and services.

If there are no corresponding classic entities (for example, with [Clouds](/docs/observe/infrastructure-observability/cloud-platform-monitoring "The cloud platforms Dynatrace can monitor")), there are no `id_classic` fields on those nodes.

## Differences between classic entities and Smartscape on Grail

Feature

Classic entity store

Smartscape on Grail

Query all entities regardless of their type

*Not supported*

`smartscapeNodes "*"`

Query HOST entities

`fetch dt.entity.host`

`smartscapeNodes HOST`

Query all relationships regardless of type, source or target

*Not supported*

`smartscapeEdges "*"`

References in Signal data

`dt.entity.__type__`

`dt.smartscape.__type__`

Enrich entity name

`entityName(dt.entity.__type__)`

`getNodeName(dt.smartscape.__type__)`

Enrich any other field (for example, tags)

`entityAttr(dt.entity.__type__, "tags")`

`getNodeField(dt.smartscape.__type__, "tags")`

Get a list of entity IDs based on entity selector

`classicEntitySelector("type(HOST),toRelationships.runsOn(type(SERVICE),tag("owner:Joe"))")`

*Not supported*

Get a list of entity IDs based on entity traversal

*Not supported*

```
smartscapeNodes SERVICE



| filter tags[owner] == "Joe"



| traverse runs_on, HOST



| fields id
```

## Smartscape segments

Smartscape nodes can be filtered with the help of

* "All data" segment
* "Entity" segment rules

Only Smartscape nodes can be filtered using segments, meaning that Smartscape edges can't be filtered.

## Extract via OpenPipeline

[OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") offers dedicated stages for node and edge extraction and processing. Use OpenPipeline to extract topological data from any signal for the following purposes:

* Custom entity type definition, such as extensions
* Additional information on Dynatrace built-in types

## Related topics

* [DQL Smartscape commands](/docs/platform/grail/dynatrace-query-language/commands/smartscape-commands "DQL Smartscape commands")
* [Join functions](/docs/platform/grail/dynatrace-query-language/functions/join-functions "A list of DQL join functions.")
* [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")
* [DPL Smartscape ID](/docs/platform/grail/dynatrace-pattern-language/log-processing-smartscape "Explore DPL syntax for parsing out Smartscape ID from strings.")
* [DPL Grammar](/docs/platform/grail/dynatrace-pattern-language/log-processing-grammar "Complete grammar list of Dynatrace Pattern Language (DPL) syntax.")


---
