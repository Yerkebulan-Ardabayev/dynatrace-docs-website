---
title: Analyze Amazon API Gateway access logs with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator
scraped: 2026-02-15T21:23:59.576362
---

# Analyze Amazon API Gateway access logs with Investigations

# Analyze Amazon API Gateway access logs with Investigations

* Latest Dynatrace
* Tutorial
* Published Jan 29, 2025

[Amazon API Gatewayï»¿](https://dt-url.net/dm03wn5) is a powerful service that enables you to build serverless web APIs using Lambda functions or to add "bolt-on security" for existing services. It can range from straightforward actions such as [applying TLS encryptionï»¿](https://dt-url.net/q823w6q) or [cachingï»¿](https://dt-url.net/bj43w6c) to more advanced measures such as [Access controlï»¿](https://dt-url.net/iq63wsn), [API throttlingï»¿](https://dt-url.net/km83wry), or [security loggingï»¿](https://dt-url.net/vqa3w97). API Gateway provides an extra layer of security that can be applied to your services quickly without modifying your underlying code.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you monitor and identify errors in your Amazon API Gateway access logs.

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in maintaining and securing cloud applications in AWS. It shows you how to make the most of the Amazon API Gateway logs ingested to Dynatrace to detect security issues.

## Prerequisites

* Create an [Amazon CloudWatch log groupï»¿](https://dt-url.net/r8c3wk1) for the Amazon API Gateway access logs
* [Set up Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.") for the log group to send the logs to Dynatrace
* Knowledge of

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

## Before you begin

Enable logging and ensure that the logs are saved to the CloudWatch log group (in this example, `/aws/apigateway/my-gateway-demo`) and sent to your Dynatrace environment.

1. Enable Amazon API Gateway logging

1. In AWS, go to the **API Gateway** service page.
2. Select your **API Gateway API** from the API list.

   In this example, an HTTP API has been used (API Gateway supports multiple API types and logging configurations are different for each of them).
3. In the sidebar menu, select **Monitor** > **Logging**.
4. Select **Choose a stage** to configure logging, then select **Edit**.
5. Turn on **Access logging**.
6. For **Log destination**, enter the ARN of the `/aws/apigateway/my-gateway-demo` log group.
7. For **Log format**, select `JSON` to simplify log record parsing.
8. In **Additional fields**, customize the log format, then select **Save**.

   For a list of available fields, see [Customize HTTP API access logsï»¿](https://dt-url.net/hk03wez).

   This example uses the following log format:

   ```
   {



   "requestId": "$context.requestId",



   "ip": "$context.identity.sourceIp",



   "requestTime": "$context.requestTime",



   "httpMethod": "$context.httpMethod",



   "routeKey": "$context.routeKey",



   "path": "$context.path",



   "status": "$context.status",



   "protocol": "$context.protocol",



   "responseLength": "$context.responseLength",



   "responseLatency": "$context.responseLatency",



   "integrationLatency": "$context.integrationLatency",



   "integrationStatus": "$context.integrationStatus",



   "errorMessage": "$context.error.message",



   "integrationErrorMessage": "$context.integrationErrorMessage"



   }
   ```

2. Verify that the API Gateway requests are logged

1. In Dynatrace, open ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** and select  **Investigation** to create a new investigation scenario.
2. To verify that the logs from the Amazon CloudWatch log group are reaching your Dynatrace environment, run the following query:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```

   Example result:

   ![fetch logs](https://dt-cdn.net/images/2025-01-27-11-45-07-1546-309fa661f3.png)

   If no logs are displayed, check your CloudWatch subscription filter and Data Firehose settings (including performance metrics, tenant and buffer settings).

## Get started

Analyze your Amazon API Gateway logs with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

1. Discover backend issues using latency metrics

1. How to decide which metrics to use

API Gateway logs contain a lot of helpful information that can be used to debug your backend applications. One standard metric to monitor from an API Gateway is latency. Two types of latencies can be monitored from API Gateway logs:

* **Integration latency**: The time between when API Gateway relays a request to the backend and when it receives a response from the backend.
* **Response latency**: The time between when API Gateway receives a request from a client and when it returns a response to the client. It includes the integration latency and other API Gateway overhead.

Deciding which metric to use for performance monitoring depends on your use case. Since this example focuses on the backend performance, not the whole request cycle, the integration latency will be used.

Follow the steps below to analyze and discover the services with the highest latency.

1. Fetch your API Gateway logs from Grail:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```
2. In the query results table, right-click on a field and select **View field details** to [view the log record in the original format](/docs/secure/investigations/enhance-results#view-details "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

   Example JSON-formatted log record:

   ```
   {



   "requestId": "Dzfa6gNrrks42Tw=",



   "ip": "14.21.74.45",



   "requestTime": "03/Jan/2025:09:22:13 +0000",



   "httpMethod": "GET",



   "routeKey": "ANY /",



   "path": "/getStuff",



   "status": "200",



   "protocol": "HTTP/1.1",



   "responseLength": "33",



   "responseLatency": "1671",



   "integrationLatency": "1665",



   "integrationStatus": "200",



   "errorMessage": "-",



   "integrationErrorMessage": "-"



   }
   ```
3. Add the following [parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands") to the DQL query to extract the `path` and `integrationLatency` properties from the JSON record.

   ```
   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"
   ```

   This example uses [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") and the [JSON matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.") to extract [selected matchers](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object#parse-selected "Explore DPL syntax for handling JSON Objects.") to separate fields.

   DPL pattern used:

   ```
   JSON{



   STRING:path,



   INT:integrationLatency



   }(flat=true)
   ```

   After running the query, you can see two new columns called **path** and **integrationLatency** in the results table.
4. To simplify viewing the results, add the following [`makeTimeseries` command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to the DQL query to create a metric from the API Gateway logs. The metric should have the path as a dimension and average latency per minute as the metric values.

   ```
   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   },



   by: { path },



   interval:1m
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"



   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   }, by: { path }, interval:1m
   ```

   Example result viewed as a chart:

   ![chart1](https://dt-cdn.net/images/2025-01-27-15-02-11-1530-a85e8ff3a0.png)

   It turns out you're experiencing some periodical latency issues for both service endpoints.

2. Identify latency issues and troubleshoot response codes

Follow the steps below to dig deeper into the response codes.

1. Extract the response codes as an additional column with an [INT matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int "Explore DPL syntax for handling numeric data."), as you're expecting to get an integer value from the field.

   DPL pattern used:

   ```
   JSON{ STRING:path, INT:status, INT:integrationLatency }(flat=true)
   ```

   You can see that the response code is called `status`.
2. To add the status as one of the dimensions for your metric, add the `status` field to the `by` parameter of your `maketimeseries` command.

   ```
   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   },



   by: { path, status },



   interval:1m
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status INT:integrationLatency }(flat=true)"



   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   }, by: { path, status }, interval:1m
   ```

   Example result viewed as a chart:

   ![chart 2](https://dt-cdn.net/images/2025-01-27-15-07-19-1529-0f585fe086.png)

   It turns out that no successful responses are returned: requests take longer, and all responses return a "Server Error" (HTTP/500).

3. Debug integration errors

Follow the steps below to continue debugging integration errors.

1. To analyze the error messages, extract an additional **integrationErrorMessage** field from the log record with a string matcher.

   DPL pattern used:

   ```
   JSON{



   STRING:path,



   INT:status,



   INT:integrationLatency,



   STRING:integrationErrorMessage



   }(flat=true)
   ```
2. Add the following snippet to the DQL query to aggregate the error messages and sort them by count:

   ```
   | summarize count(), by: { integrationErrorMessage }



   | sort `count()` desc
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



   | summarize count(), by: { integrationErrorMessage }



   | sort `count()` desc
   ```

   A distinct timeout error message stands out from results: `The Lambda function returned the following error: RequestId: 01fe3839-4974-40d5-960a-173fcb5ec786 Error: Task timed out after 5.00 seconds. Check your Lambda function code and try again.`
3. Extract the `Error` portion from the log record without the request ID to compare this error message with the others.

   DPL pattern used:

   ```
   LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error
   ```

   You now have two fields (**error** and **integrationErrorMessage**) that can contain the error message.
4. Add the following snippet to the DQL query to merge the two fields into one column with the `if` function and summarize based on that.

   ```
   | fields error = if(isnull(error), integrationErrorMessage, else: error)



   | summarize count(), by: { error }
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



   | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"



   | fields error = if(isnull(error), integrationErrorMessage, else: error)



   | summarize count(), by: { error }
   ```

   Example results:

   ![results](https://dt-cdn.net/images/2025-01-27-15-55-59-1538-7994d7382c.png)

   It turns out that timeout errors are the most frequent.
5. To see how the error messages distribute over the same period, create a metric based on the timeout errors as follows:

* Add a [`filterOut` command](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut "DQL filter and search commands") to remove the successful events
* Add the `timestamp` field to the [`fields` command](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands")
* Construct the `makeTimeseries` command to aggregate errors by count in one-minute interval.

  Your final query should look like this:

  ```
  fetch logs



  | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



  | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



  | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"



  | fields timestamp, error = if(isnull(error), integrationErrorMessage, else: error)



  | filterOut error == "-"



  | makeTimeseries count(default: 0), by: { error }, interval: 1m
  ```

  Example result viewed as a chart:

  ![chart 3](https://dt-cdn.net/images/2025-01-27-15-50-54-1509-00bad2a7dc.png)

  It turns out you're experiencing Lambda timeout problems, which are creating latency and server error issues in your API Gateway logs.

  To investigate this further, you'd have to look into the Lambda function and see why you're experiencing this behavior precisely at those times. It can be that certain scheduled jobs are running, resources are locked or overloaded, or some other dependencies are causing these issues.

## Related topics

* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")