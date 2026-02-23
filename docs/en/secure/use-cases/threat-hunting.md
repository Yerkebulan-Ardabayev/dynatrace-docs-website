---
title: Threat hunting and forensics
source: https://www.dynatrace.com/docs/secure/use-cases/threat-hunting
scraped: 2026-02-23T21:30:33.046737
---

# Threat hunting and forensics

# Threat hunting and forensics

* Latest Dynatrace
* Tutorial
* Published Mar 14, 2024

When threat hunting, time and precision are crucial. You need to be as fast and accurate as possible to find and act upon information. As a security analyst investigating security incidents or threat hunting, you often need to

* Navigate between multiple executed queries and their results
* Manage the evidence gathered during investigations and reuse it when building additional queries
* Ensure that

  + The investigation is maintained in context.
  + The tools for such activities support quick query creation and a detailed overview of the results.

In the following, we demonstrate how you can achieve these goals using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

## Target audience

This page is intended for Security teams performing threat hunting or analyzing security incidents, such as the Incident Response team or Security Analysts.

## Scenario

In the following, we address a scenario in which you get a notification from an external source about a suspiciously high number of unauthorized requests towards our Kubernetes control plane between `2024-02-13 16:00:00` and `2024-02-13 18:59:59`. Your Kubernetes cluster has been set up to AWS EKS cluster, and logs are forwarded to Dynatrace.

As a security analyst, you want to understand if this is related to malicious activities or if it may be an indication of a cyber security incident. During this investigation, you will follow the trail of your findings to illustrate the nature of threat hunting and incident solving.

## Prerequisites

* [Set up Kubernetes observability with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* Set up AWS logging to CloudWatch:

  + [Set up EKS Cluster loggingï»¿](https://dt-url.net/va038gi)
  + [Set up VPC Flow loggingï»¿](https://dt-url.net/ya238ol)
  + [Set up K8S DNS logging](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks/k8s-dns-logs "Learn how to ingest Kubernetes-related DNS logs from AWS to Dynatrace.")
* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Basic knowledge of

  + [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
  + [Dynatrace Pattern Language (DPL)](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")
  + How DNS name resolving works in Kubernetes clusters

## Investigation path 1: Analyze Kubernetes audit logs

First, you want to understand which activities caused the notification about the high number of unauthorized requests in your Kubernetes audit logs.
Open [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") and create a new investigation.

1. Set the timeframe

In the [timeframe section](/docs/secure/investigations/define-timeframes#selector "Adjust time ranges for data analysis and event correlation in Investigations."), set the timeframe from `2024-02-13 16:00:00` to `2024-02-13 18:59:59`, when the unauthorized requests occurred.

![set the timeframe](https://dt-cdn.net/images/2024-03-06-08-15-45-1914-2f0de669a4.png)

2. Fetch Kubernetes cluster audit logs

1. Kubernetes audit logs are forwarded to Dynatrace with `aws.log_group` and `log_stream` values attached. To fetch all the unique AWS CloudWatch log groups that are ingested to Dynatrace, copy-paste the following [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") in the query input.

   ```
   fetch logs



   | summarize count(), by: aws.log_group
   ```
2. Select **Run** to execute the query.

   ![fetch kubernetes cluster audit logs](https://dt-cdn.net/images/2024-03-06-08-45-30-1910-d1342717df.png)

   At this point, you notice a circle has appeared in the **Query tree** section in the upper right. This is called a root node and marks the starting point of your investigation. From here on, every time you modify and execute a query, a new node will be added in the query tree, allowing you to navigate among queries while keeping the history of your investigation intact. For details, see [query tree](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis.").

3. Filter by log group name

1. In the query results, find the record with the log group collecting the EKS control plane logs (in our example, `/aws/eks/unguard-secla-demo/cluster`) and [add it as a filter](/docs/secure/investigations#fields "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to your DQL query.

   ![Add a filter for the log group name](https://dt-cdn.net/images/2024-03-06-09-01-16-1530-51987a9960.png)
2. To view only the control plane audit events, modify the `filter` command in the query input by adding the [`and` operator](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") and the [`contains` string function](/docs/platform/grail/dynatrace-query-language/functions/string-functions#contains "A list of DQL string functions.") as follows:

   ```
   | filter aws.log_group == "/aws/eks/unguard-secla-demo/cluster" and contains(aws.log_stream, "audit")
   ```
3. In the query input, remove the `summarize` command and select **Run** to execute the query.

   ![view only the control plane audit events](https://dt-cdn.net/images/2024-03-06-09-19-12-1919-c2f0267459.png)

4. Inspect the content

In the query results table, right-click on any cell in the **content** field and select **View field details** to view the raw content of the field. For details, see [Explore data in the original format](/docs/secure/investigations/enhance-results#view-details "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

![Inspect the content](https://dt-cdn.net/images/2024-03-07-16-43-25-1546-aa18860a77.png)

5. Extract fields from JSON

1. In the query results table, right-click on any cell in the **Content** field and select [**Extract fields**](/docs/secure/investigations/extract-fields#field "Pull specific data points from logs in Investigations.") to navigate to [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.").
2. Select **Saved patterns**.
3. In **Dynatrace patterns**, select **k8s** > **audit**.

   ![extract field](https://dt-cdn.net/images/2024-03-06-18-41-50-1547-0df2e723b3.png)

   When extracting fields from a JSON structure, you can define only a partial schema for the fields that are relevant for your use case. To continue your investigation, you need to select only the relevant fields.
4. In the query input of DPL Architect, replace the pattern as follows:

   ```
   JSON{



   STRING:verb,



   JSON{string:username}(flat=true):user,



   JSON_ARRAY{ipaddr}(typed=true):sourceIPs,



   JSON{string+:resource}(flat=true):objectRef,



   JSON{int:code}(flat=true):responseStatus



   }(flat=true)
   ```
5. Select **Results** for an overview of the fields that will be extracted from the [match preview dataset](/docs/platform/grail/dynatrace-pattern-language/dpl-architect#match-preview "Extract fields with Dynatrace Pattern Language Architect.").

   ![display results](https://dt-cdn.net/images/2024-03-06-14-28-54-816-6ec66c1606.png)
6. Select **Insert pattern** to append the pattern to your DQL query.

   ![Insert pattern in DPL Architect](https://dt-cdn.net/images/2024-03-11-08-59-35-613-d01beb3deb.png)
7. Select **Run** to execute the query.

6. Filter events

To find out which IPs have unauthorized activity, you need to

* [Expand](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#expand "DQL structuring commands") the source IP array
* [Summarize](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") the results with the relevant fields extracted previously
* [Filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") the results to view only unauthorized requests (`401`) and forbidden requests (`403`)

1. In the query input, add the following DQL snippet, then select **Run** to execute the query.

   ```
   | expand sourceIPs



   | summarize count(), by: {sourceIPs, username, verb, resource=objectRef, responseStatus}



   | filter in(responseStatus, {401, 403})
   ```
2. In the results table menu, sort results by count to see which IP addresses had the most connections.

   ![filter the relevant events](https://dt-cdn.net/images/2024-03-07-08-11-17-1448-777bfa0c1e.png)

It looks like you found the origin of your security notification:

* An unauthorized external IP address is trying to fetch secrets from your control plane (in our example, `198.51.100.2`, with `401` response code and 122 connections). This is not surprising, since security scanners are attempting this daily from the internet.
* A private IP address is trying to enumerate pods repeatedly (in our example, `172.31.29.138`, with `403` response code and 2090 connections). It seems to be one of the pods in your Kubernetes cluster, and such behavior might indicate a compromised pod!

7. Add IPs as evidence

Both IP addresses need to be analyzed further, but the one with a `403` response and 2090 attempts is more critical and requires special attention.

To save the IPs as [evidence](/docs/secure/investigations/manage-evidence "Collect and preserve investigation artifacts in Investigations."), you can add the first IP (`198.51.100.2`) to a preset evidence list and the second one (`172.31.29.138`) to a new customized evidence list:

1. Right-click on `198.51.100.2`, then select **Add to evidence list** > **Suspicious IPs**.
2. Right-click on `172.31.29.138`, select **Add to evidence list** > **New evidence list** and enter a name, for example, "Suspicious pod".

   ![add to IP collections](https://dt-cdn.net/images/2024-03-07-08-32-32-357-51a8b2b145.png)

## Investigation path 2: Investigate potential target

To understand what the pod did and which other service logs you need for your investigation, you can start with the network logs. For AWS, the best place to start is the [VPC network flow logsï»¿](https://dt-url.net/6c0385l).

1. Fetch VPC flow logs

1. Using the [query tree](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis.") created during your investigation, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step.
2. In the query results, find the record with the log group that contains your VPC flow logs (in our example, `/aws/vpc/unguard-secla-demo/vpc-flow-logs`), and add it as a filter to the DQL query.

   ![VPC flow logs](https://dt-cdn.net/images/2024-03-06-16-11-40-1905-ed76689a2c.png)

   The node in the query tree has changed its icon, which means youâre in the middle of editing the query. You can either revert to the original query to update the results table or execute the modified query. When you run the modified query, a new node is created with the respective query and its results. You can [give the node a distinctive name and color](/docs/secure/investigations/query-tree "Visualize and structure complex queries in Investigations.") to recognize it later.
3. In the query input, remove the `summarize` command, then select **Run** to execute the modified query.

   ![execute modified query](https://dt-cdn.net/images/2024-03-07-18-21-06-1913-6f988f1771.png)

   This creates a second branch in the query tree. A branch is the visual representation of an investigation path. Let's see where this new path takes us.

2. Extract fields

For more accurate results, you need to extract fields from the log records with DPL Architect.

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **aws** > **vpc-flow-full**.
4. Select **Insert pattern**.
5. Select **Run** to execute the query.

3. Filter results

Since youâre interested only in the results from the suspicious pod, you can add a filter to your DQL query based on the evidence created in the [Add evidence for later use](#evidence) step.

1. Go to **Evidence lists** and select the evidence menu for the `Suspicious pod` list to see the filtering options and the suitable field names that match the `IPADDR` type.
2. Select **Filter for** > **Filter within field `pkt_srcaddr`**. This appends the filter to your DQL query.

   ![Filter by evidence](https://dt-cdn.net/images/2024-03-07-08-51-47-790-18cc53cc6c.png)
3. To get a better overview about the network connections, append the following command to the DQL query in the query input:

   ```
   | summarize count(), by: { pkt_dstaddr, protocol, action, dstport}



   | sort `count()` desc
   ```
4. Select **Run** to execute the query.

You can see that the suspicious pod has most often connected to the cluster's DNS service via UDP port 53.

![Better overview of network connections](https://dt-cdn.net/images/2024-03-07-09-20-38-1421-bf0a76a211.png)

There could be an application misconfiguration or something suspicious might be happening with that pod.

## Investigation path 3: Identify what data the pod sent out

To look for the DNS names resolved by a pod you need to check the CoreDNS logs. If configured properly, the query logs are visible in the CoreDNS container logs.

1. Fetch coreDNS logs

1. To fetch CoreDNS container logs, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step and modify the query in the query input as follows:

   ```
   fetch logs



   | filter k8s.container.name == "coredns"
   ```
2. Select **Run** to execute the query. This creates a third branch in the query tree.

   ![Fetch coreDNS logs](https://dt-cdn.net/images/2024-03-07-19-14-29-1919-bdcb4fef59.png)

2. Extract fields

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **k8s** > **coredns-query**.
4. Select **Insert pattern**.
5. Select **Run** to execute the query.

3. Filter results

To view only records containing the DNS requests originating from your suspicious pod, select the **source\_ip** column header, then select **Filter for** > **Suspicious pod**.

![Filter the source_ip field by the suspicious pod](https://dt-cdn.net/images/2024-03-07-09-52-47-539-9ece6d7f6f.png)

4. Extract domain name

There could be quite a lot of DNS requests in the results table. For a better understanding of the resolved hostnames, you need to extract the domain name portion from the name field and summarize results based on it.

1. In the query input, add the following snippet to the DQL query:

   ```
   | parse name, "ld* '.'? ( (ld '.' ld):domain '.' eos)"



   | summarize count = count(), by: {domain}
   ```
2. Select **Run** to execute the query.

   You notice that, besides internal or local domains, one suspicious domain (`tiitha-maliciousdomain.com`) is being resolved quite a lot!

   ![suspicious domain identified](https://dt-cdn.net/images/2024-03-07-10-01-49-503-598f18f1d7.png)

5. Add domain as evidence

1. In the query results table, right-click on the suspicious domain name, then select **Add to evidence list** > **New evidence list**.
2. Enter a name for your new evidence list, for example, **Attacker domain**.

   ![Add attacker domain as evidence](https://dt-cdn.net/images/2024-03-07-18-32-15-488-857db7fc3a.png)

6. Filter by attacker domain

1. In the query results table, select the cell with the suspicious domain, then select **Filter for** to add a filter to the query that fetches only requests that include the attacker domain.

   ![Filter for the malicious domain](https://dt-cdn.net/images/2024-03-07-10-17-10-1039-fc84720720.png)
2. In the query input, remove the `summarize` command and select **Run** to execute the query.

   It looks like there's some kind of data movement between the suspicious pod and the attacker domain. Looking at the query names and considering the number of queries, data appears to be extracted via DNS tunneling.

   ![data is being extracted via DNS tunnelling](https://dt-cdn.net/images/2024-03-07-10-24-01-1450-8d1cdc2027.png)

7. Analyze DNS requests

As there are thousands of DNS requests towards that particular domain, you may want to aggregate the data to determine how to proceed further.

1. In the query results, select the **type** column header, then select [**Summarize**](/docs/secure/investigations/enhance-results#aggregate "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").
2. Select **Run** to execute the query.

   ![Summarize by type](https://dt-cdn.net/images/2024-03-07-10-40-41-399-c7c4bf8285.png)

   You notice many A, AAAA, and TXT requests from the pod. You start investigating the A requests.
3. In the query results table, right-click on an **A** cell and select **Filter for** to add a filter to the DQL query.
4. In the query input, remove the `summarize` command and select **Run** to execute the query.

   To determine what is being sent out, you need to extract the subdomain portion of the domain. For this, you need to analyze one of the DNS queries that is resolving the attacker domain.
5. Double-click on any cell in the query results table.
6. In the **Details (â¦)** window, check the data in the **name** field.

   It seems that the DNS name is structured by an ID followed by the payload portion encoded in hex, and these parts are delimited by `.`.

   ![Inspect the name](https://dt-cdn.net/images/2024-03-07-11-09-13-997-28d0d5a17a.png)
7. To parse and decode the payload, add the following DQL snippet to the DQL query:

   ```
   | parse name, """ld:id '.' ld:payload '.tiitha-maliciousdomain'"""



   | fieldsAdd payload=replaceString(payload,".","")



   | fields timestamp, id, payload=decodeBase16ToString(payload)



   | sort timestamp, id
   ```

   The result proves that data from your pod is definitely being extracted and sent out!

   ![data from pod is extracted and sent out](https://dt-cdn.net/images/2024-03-07-11-11-40-1106-e7433155ee.png)

## Investigation path 4: Find out how the commands were sent to the pod

You know for sure the pod is sending information to an external DNS server, but you havenât figured out how it gets the commands. Since TXT-type DNS queries enable larger responses and are sometimes used for malicious transactions as well, you need to take a look at those requests. Since CoreDNS records don't contain the response payload, you turn to Route53 logs.

1. Analyze TXT records

1. Using the query tree, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step.
2. In the query results, find the record with your Route53 log group (in our example, `/aws/route53/unguard-secla-demo/resolver-logs`) and add it as a filter to your DQL query.
3. In the query input, remove the `summarize` command and select **Run** to execute the query. This creates a fourth branch in the query tree.

   ![Analyze TXT records](https://dt-cdn.net/images/2024-03-07-18-55-59-1919-a0b7fff314.png)

2. Extract fields from log records

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **aws** > **route53-query**.
4. You need to extract the `query_name`, `query_type`, `srcaddr`, and `answers` values from the log record. In the query input, you can replace the pattern as follows:

   ```
   json{



   string:query_name,



   string:query_type,



   json_array:answers,



   ipaddr:srcaddr



   }(flat=true)
   ```
5. Select **Insert pattern**.
6. Select **Run** to execute the query.

3. Filter data

1. In the query results, select the `query_name` column header, then select **Filter for** > **Attacker domain**.
2. Select **Run** to execute the query.

   You only care about the queries with the TXT type, so you can append the filter with the appropriate expression. Since the answers portion is an array, expand the field so that each value in the array is a separate record. The only fields you need are `srcaddr`, `query_name`, and the `Rdata` element from the answer object.
3. In the query input, modify the `filter` command by adding the following snippet:

   ```
   | filter endsWith(query_name, "tiitha-maliciousdomain.com.") and query_type == "TXT"



   | expand answers



   | fields srcaddr, uery_name, answer=answers[Rdata]
   ```
4. Select **Run** to execute the query.

   Your hypothesis is correct: the TXT DNS queries were used to fetch the commands. The executed commands (including the Kubernetes control plane requests as curl commands) show up as responses in your DNS logs!

   ![Correct hypothesis: TXT DNS queries were used to fetch the commands](https://dt-cdn.net/images/2024-03-07-19-02-39-1919-08659833f4.png)

## Conclusion

You've found out what happened but haven't figured out what else the pod has done, what process or activity is triggering the DNS requests, who controls the data extraction, how and when the pod was infected, and other relevant aspects of a security incident.

From here on, the complexity of the investigation will only grow, and the ability to navigate between different stages of an investigation is even more crucial. All these questions might trigger a new branch in the query tree, if not a separate investigation. Our investigation introduces many additional questions that require answers.

## Related topics

* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")