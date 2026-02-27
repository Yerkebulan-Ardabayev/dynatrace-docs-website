---
title: Analyze AWS CloudTrail logs with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator
scraped: 2026-02-27T21:30:03.023876
---

# Analyze AWS CloudTrail logs with Investigations

# Analyze AWS CloudTrail logs with Investigations

* Latest Dynatrace
* Tutorial
* Published Nov 26, 2024

[AWS CloudTrailï»¿](https://dt-url.net/ax63uwp) is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service in an Amazon AWS environment are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you

* [Monitor sign-in failures to AWS console](#sign-in)
* [Create metrics for unauthorized API calls](#metrics)
* [Monitor AWS API throttling](#monitor)
* [Detect externally generated keys in AWS KMS](#keys)

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in maintaining and securing cloud applications in AWS.

## Prerequisites

* Store your CloudTrail logs to an S3 bucket or [CloudWatchï»¿](https://dt-url.net/mr03u6p).
* Send CloudTrail logs to Dynatrace. There are two options to stream logs:

  + [Amazon S3ï»¿](https://dt-url.net/c703wc8) Recommended
  + [Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Knowledge of

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

## Before you begin

Follow the steps below to fetch the AWS CloudTrail logs from Grail using ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** and prepare them for analysis.

1. Fetch AWS CloudTrail logs from Grail

Once your CloudTrail logs are ingested into Dynatrace, follow these steps to fetch the logs.

1. Open [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation** to create an investigation scenario.
3. In the query input section, insert the DQL query below.

   ```
   fetch logs, from: -30min



   | filter aws.service == "cloudtrail"
   ```
4. Select ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") **Run** to display results.

   The query will search for logs from the last 30 minutes, which have been forwarded from an AWS log group that contains the word `cloudtrail`.

   If you know in which Grail bucket the CloudTrail logs are stored, use filters to specify the bucket to improve the query performance.

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"
   ```

   For details, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

   The results table will be populated with the JSON-formatted events.
5. Right-click on an event and select **View field details** to see the JSON-formatted event in a structured way. This enables investigators to grasp the content of the event much faster.

   ![results table](https://dt-cdn.net/images/image-20241109-145818-3100-3e65568b52.png)
6. Navigate between events in the results table via the keyboard arrow keys or the navigation buttons in the upper part of the **View field details** window.

   ![field details](https://dt-cdn.net/images/image-20241106-153049-1-2040-9f9e875bf6.png)

2. Prepare the data for analysis

Follow the steps below to simplify log analysis, speed up investigations, and maintain the required precision for analytical tasks.

1. Add to your DQL query the [parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands") to extract the required data from the log records into separate fields.
2. Add the [JSON matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.") to extract the JSON-formatted log content as a JSON object into a separate field called `event`.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"
   ```
3. Double-click on any record in the results table to view the object in the **Record details** view. Expand the JSON elements to navigate through the object faster and add filters based on its content.

   ![Record details](https://dt-cdn.net/images/image-20241106-155245-1-2288-9851882d34.png)

## Get started



The following are use cases demonstrating how to build the above query to analyze AWS CloudTrail logs with Dynatrace.

1. Monitor sign-in failures to AWS console

Failures in authentication logs can be an indication for a potential attack towards your infrastructure. A malicious user could try to enumerate usernames or passwords to gain access to your AWS environment and take control of your business.

To monitor sign-in failures to the AWS console using CloudTrail logs

1. Add a filter statement to fetch only results with `signin.amazonaws.com` as the event source and `ConsoleLogin` as the event name.
2. Add a filter command for the `responseElements.ConsoleLogin` sub-element in the JSON object with the value `Failure` to see only failed login attempts.

   You can use the DQL snippet below.

   ```
   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName] == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"
   ```
3. Add the `summarize` command with your chosen fields to have an aggregated overview of the events.

   You can use the DQL snippet below.

   ```
   | summarize event_count = count(), by: {



   source  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

   Your final DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"



   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName]   == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"



   | summarize count(), by: {



   ipAddr  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

2. Create metrics for unauthorized API calls

Unauthorized API calls can indicate a hacking attempt or a system malfunction. These kinds of anomalies should be investigated to prevent unexpected costs or system takeovers by malicious users.

To identify the "top targets" from the API list

1. Create a filter to fetch only events, with an `AccessDenied` or `UnauthorizedOperation` error code.
2. Add the [makeTimeseries command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to convert your log results to metrics.
3. Add the `event[eventName]` value from the logs as a metrics dimension.
4. Sort the results to see only the top 10 APIs and limit the results to 10 records.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter in(event[errorCode], { "AccessDenied", "UnauthorizedOperation" })



   | makeTimeseries event_count = count(), by: { eventName = event[eventName] }



   | sort arrayAvg(event_count) desc



   | limit 10
   ```

   For more granularity, you can add more dimensions to the `makeTimeseries` command.

   For example, to see API call charts based on the user and the API endpoint, the summarization command would be as follows.

   ```
   | makeTimeseries count(), by: {



   user      = event[userIdentity][arn],



   eventName = event[eventName]



   }
   ```

   Example results visualized as a line chart:

   ![ results visualized to a line-chart ](https://dt-cdn.net/images/image-20241108-135013-2334-7d17f90671.png)

3. Monitor AWS API throttling

Monitoring request counts towards APIs is important from the availability, cost, and security perspectives. A throttling API might indicate either a brute-force attack, a denial-of-service attack, or an ongoing data exfiltration by a malicious actor.

To monitor AWS API throttling from AWS CloudTrail logs in Dynatrace

1. Create a filter to fetch only events with an error code `Client.RequestLimitExceeded`.
2. Add the [makeTimeseries command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to convert your log results to metrics.
3. Add the `event[eventName]` value from the logs as a metrics dimension.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[errorCode] == "Client.RequestLimitExceeded"



   | makeTimeseries count(), by: { eventName = event[eventName] }
   ```

4. Detect externally generated keys in AWS KMS

When creating a new key in [AWS Key Management Service (KMS)ï»¿](https://dt-url.net/4g23uoc), you can choose the key material origin for the key: whether the keys are kept under AWS control or handled externally.

By default, key origin material is `AWS_KMS`, which means that KMS creates the key material.

When keys are handled externally, thereâs an increased risk that the keys might leak, thus endangering the data which is protected with the key: the key could leak from elsewhere and its location could be unknown.

To detect such key creations, where external key material was used

1. Create a filter to fetch only events with the name `CreateKey`.
2. Add a statement to the filter to exclude all origins that begin with `AWS_`.

   Currently there are two options (`AWS_KMS` and `EXTERNAL`) so you could filter by `External` origin, but having the filtering out could be be more future-proof.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "CreateKey"



   | filterOut startsWith(event[requestParameters][origin], "AWS_")



   | fields {



   eventName = event[eventName],



   origin    = event[requestParameters][origin],



   keyUsage  = event[responseElements][keyMetadata][keyUsage],



   region    = event[awsRegion],



   userARN   = event[userIdentity][arn],



   keyId     = event[responseElements][keyMetadata][keyId]



   }
   ```

As a result, you get a table that contains the following information:

* **eventName**: CreateKey
* **origin**: EXTERNAL
* **keyUsage**: ENCRYPT\_DECRYPT
* **region**: us-east-1
* **userARN**: username
* **keyId**: 123acb

## Summary

These are some of the use cases that can be solved using CloudTrail logs and Dynatrace ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**. These logs are an endless source of information that enables Security and DevOps Engineers to conduct different investigations on their AWS infrastructure.

## Related topics

* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")