---
title: DPL Architect
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/dpl-architect
scraped: 2026-02-17T21:30:45.268964
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