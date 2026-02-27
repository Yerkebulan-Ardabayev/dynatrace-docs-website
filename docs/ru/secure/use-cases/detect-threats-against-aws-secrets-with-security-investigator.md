---
title: Detect threats against your AWS Secrets with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator
scraped: 2026-02-27T21:18:55.512728
---

# Detect threats against your AWS Secrets with Investigations

# Detect threats against your AWS Secrets with Investigations

* Latest Dynatrace
* Tutorial
* Published Nov 26, 2024

In today's digital landscape, protecting your cryptographic secrets in a cloud environment is more critical than ever. Secrets such as API keys, passwords, and encryption keys used in your applications are vital parts of your applications that, when leaked, could jeopardize your whole business. That's why analyzing threats against secrets is essential to ensure your data's integrity, confidentiality, and availability.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you

* [Detect externally generated keys in AWS KMS](#keys)
* [Detect unprivileged requests trying to read Secrets](#requests)
* [Detect requesting non-existing secrets](#secrets)

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in the maintenance and security of cloud applications in AWS.

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



The following are use cases demonstrating how to build the above query to analyze AWS Secrets with Dynatrace.

1. Detect externally generated keys in AWS KMS

When creating a new key in [AWS Key Management Service (KMS)ï»¿](https://dt-url.net/4g23uoc), you can choose the key material origin for the key: whether the keys are kept under AWS control or handled externally.

By default, key origin material is `AWS_KMS`, which means that KMS creates the key material.

When keys are handled externally, thereâs an increased risk that the keys might leak, thus endangering the data that is protected with the key: the key could leak from elsewhere and its location could be unknown.

To detect key creations where external key material was used

1. Create a filter to fetch only events with the name `CreateKey`.
2. Add a statement to the filter to exclude all origins that begin with `AWS_`.

   Currently, there are two options (`AWS_KMS` and `EXTERNAL`), so you could filter by `External` origin, but having the filtering out could be be more future-proof.

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

2. Detect unprivileged requests trying to read Secrets

Unauthorized requests to read secrets is an indication of either a hacking attempt or a system misconfiguration. Unauthorized requests might mean that an attacker has compromised credentials from your system and is now trying to extract Secrets from your AWS account (but luckily without success).

In this use-case, we go through two scenarios that target different unprivileged access attempts to your secrets: [requesting secrets without KMS privileges](#no-kms-privilege) and [requesting unauthorized secrets](#unauthorized-secret).

#### Requests without KMS privileges

In case of missing KMS privileges, you can assume these accounts were not supposed to access any secrets in your environments. If this still happens, this is (either malicious or accidental) credential misuse or misconfiguration. Either way, this requires your attention.

To see if someone is trying to access such events in your CloudTrail logs

1. Create a filter to fetch only `GetSecretValue` events and with an `AccessDenied` error code.
2. Add a new filtering condition to see only errors with an `Access to KMS is not allowed` message.
3. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `ARN` of the user of the unauthorized attempts.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   and event[errorMessage] == "Access to KMS is not allowed"



   | summarize event_count = count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn]



   }
   ```

If your query returns any results, they would look like this:

| **sourceIPAddress** | **region** | **arn** | **event\_count** |
| --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 3 |

#### Unauthorized Secret requests

In this case, the account is trying to load privileges to which it doesnât have access. The secret configuration might be incorrect, or the account might be being used for secrets it wasnât meant to be used for. The last possibility introduces a potential security threat if the intent is malicious.

To see if such events occur in your CloudTrail logs

1. Create a filter to fetch only `GetSecretValue` events and with an `AccessDenied` error code.
2. If the requested secret doesn't exist or the user doesn't have access to it, the secret's ARN is mentioned in the error message. Parse out the `secretID` from the error message.
3. Show only the events where `secretID` is present.
4. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `userARN` of the user of the unauthorized attempts.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   | parse event[errorMessage], "LD ':secret:' STRING:secretId"



   | filter isNotNull(secretId)



   | summarize count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn],



   secretId



   }
   ```

If your query returns any results, they would look like this:

| **sourceIPAddress** | **awsRegion** | **arn** | **secretId** | **event\_count** |
| --- | --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 123abc | 3 |

3. Detect requesting non-existing secrets

Requesting secrets that don't exist might indicate a security issue (for example, when someone is trying to enumerate your secrets to extract them and tries all kinds of secrets that might not exist) or an operational issue (secrets used by the service are no longer available, thus creating service issues).

To see if such events are present in your CloudTrail logs

1. Create a filter to fetch the `GetSecretValue` events.
2. Append the filter conditions to fetch only events with a `ResourceNotFoundException` error message.
3. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `userARN` and collect the number of events and distinct secrets fetched by this user in the respective AWS region from the specific IP address.

   If you see a large number of distinct secrets being fetched from a single `userARN`, it might be a secret enumeration. If the number of different secrets is low, something has probably happened to the secret (a wrong set of privileges, the secret has been removed, or similar).

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "ResourceNotFoundException"



   | summarize {



   event_count = count(),



   distinct_secrets = countDistinct(event[requestParameters][secretId])



   }, by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN   = event[userIdentity][arn]



   }



   | sort distinct_secrets desc
   ```

## Related topics

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")