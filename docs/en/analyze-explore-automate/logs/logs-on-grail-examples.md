---
title: Log on Grail examples
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/logs-on-grail-examples
scraped: 2026-02-26T21:17:17.093639
---

# Log on Grail examples

# Log on Grail examples

* Latest Dynatrace
* Overview
* 17-min read
* Updated on Oct 15, 2025

Log Management and Analytics powered by Grail enables you to pinpoint and retrieve any log data with the help of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). After reviewing the [fundamentals of DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts."), use the examples on this page to start getting answers from your log data.

To run DQL queries with logs on Grail, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** > **Advanced mode**.

* [Example 1](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample1 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Get the distribution of HTTP status codes and counts per error type.
* [Example 2](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample2 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Define an average cart size based on logs.
* [Example 3](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample3 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Track user changes with audit logs.
* [Example 4](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample4 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Create a log metric.
* [Example 5](/docs/analyze-explore-automate/logs/logs-on-grail-examples#logexample5 "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.") - Create a log alert.

### Example 1: Status codes and counts

In this example, you get the distribution of HTTP status codes and counts per error type.

The proxy server logs HTTP response status codes. You need to see the response code distribution over a certain timeframe, and focus on errors.

1. Search for relevant logs.  
   You need to start with a search for logs from the HAProxy instance. As the `haproxy` string is included in the log message, let's use the `contains()` function.

   ```
   fetch logs



   | filter contains(content, "haproxy")
   ```

   A search for the `haproxy` string is performed across all records in the timeframe, so you should narrow it to optimize the query. If the entity that produces logs can be identified in advance, it's much more cost-effective to search within that specific entity.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"
   ```

   **Results table**
2. Extract your metric from the content field.  
   The log content field includes the HTTP\_STATUS codes you need. Now let's use the `parse` command to create a [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") pattern with the following elements:

   * `LD`: start by matching any [line data](/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data "Explore DPL syntax for handling lines and strings.") at the beginning of the field
   * `'HTTP_STATUS '`: [literal expression](/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression "Explore DPL syntax for handling literal expressions.") that immediately precedes the numerical Http Status, and takes into account a space
   * `INT:httpstatus`: [integer](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer "Explore DPL syntax for handling numeric data.") that will be parsed out as a new field `httpstatus`

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"
   ```

   **Results table**
3. Filter a range of values.  
   You can select a range of values for further analysis using DQL. We select only the HTTP status codes that begin with 400 and higher, as those include client side and server side errors.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400
   ```
4. Aggregate the results.  
   You need to aggregate the results with count() to get a summary of how many times each status code occurs.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400



   | summarize count(), by:{httpstatus}
   ```

   **Results table**

### Example 2: Average cart size

In this example, you will define an average cart size based on logs.

Your application logs context data that is relevant to your business. You need to retrieve that data from logs and create a report for a specific timeframe.

1. Select the specific process data for a defined timeframe.  
   You need to query logs from the last three hours, which is your timeframe, and then specify the process that handles cart actions in your store, `cartservice cartservice-*`.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"
   ```

   **Results table**
2. Check the types and counts of products added to carts.  
   You need to get an overview of the type and quantity of products users added to their carts. Since logs contain various events, you need to specify the events where items were added to carts, using the `contains()` function. To clean up the results table, it is a good idea to leave only timestamp and log content.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content
   ```

   **Results table**
3. Extract the products and corresponding quantities.  
   You need to extract the product identifiers and quantities from logs with the `parse` command.  
   Using the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers."), create a pattern and match the following parts of the `content` field:

   * `LD`: start by matching any [line data](/docs/platform/grail/dynatrace-pattern-language/log-processing-lines-strings#line-data "Explore DPL syntax for handling lines and strings.") at the start of the field
   * `'userId='`: [literal expression](/docs/platform/grail/dynatrace-pattern-language/log-processing-literal-expression "Explore DPL syntax for handling literal expressions.") that immediately precedes user ID
   * `LD:userId`: any line data that will be parsed out as a new field with the `userId` name
   * `', productId='`: literal expression that ends user ID and separates it from product ID
   * `LD:productId`: any line data that will be parsed out as a new field with the `productId` name
   * `', quantity='`: literal expression that ends product ID and separates it from quantity
   * `INT:productQuantity`: [integer](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int-integer "Explore DPL syntax for handling numeric data.") that will be parsed out as a new field with the `productQuantity` name

   The remaining fields are ignored.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
   ```

   **Results table**
4. Clean the data.  
   As the user ID and the original log record are no longer relevant, let's clean up the result table using the `fields` command.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity
   ```

   **Results table**
5. Summarize events per product.  
   To see the total amount of each product added to a cart, use the `sum()` function.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize sum(productQuantity), by:{productId}
   ```

   **Results table**
6. Find the most popular products.  
   To understand the behavior of an average user, we want to determine the average size of the cart for each product. To do that, we use the `avg()` function and name the new field `averageProductQuantity`. Then we sort the average values from highest to lowest, and we limit the results so that we see the five most popular products.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize averageProductQuantity = avg(productQuantity), by:{productId}



   | sort averageProductQuantity desc



   | limit 5
   ```

   **Results table**

### Example 3: Track user changes

In this example, you track user changes with audit logs. You want to track the type and quantity of actions performed by users.

1. Check the availability of recent audits logs.

   * Find out if any audit logs have been available within the last five minutes.
   * Set the time range and filter only logs whose source path ends with your designated path.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")
   ```

   **Results table**
2. Extract relevant fields for a single user.

   * The retrieved table includes record updates, deletions, and creations.
   * If you limit your query to the last result, you can understand actions performed by a single user.

   Then we do the following:

   * Use `parse` to turn the `content` field into a JSON object
   * Use `fieldsAdd` to extract relevant fields from that object
   * Use `fields` to add a relevant field
   * Use `fieldsRemove` to retrieve only the columns that you need

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | limit 1



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings
   ```

   **Results table**
3. Get the users who performed updates and deletions.  
   To get users who made updates or deletions only:

   * Remove the `limit` command
   * Add a filter for the two action types: update and delete.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))
   ```

   **Results table**
4. Find out the change types and the number of changes performed by each user.  
   You can count the records using the `summarize` command.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize count(), by:{user,type}
   ```

   **Results table**
5. Count the events per user, split by action type (create, update, delete).  
   You can perform the calculation by combining the `summarize` commmand with the `countIf` function.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize {countIf(type=="CREATE"), countIf(type=="UPDATE"), countIf(type=="DELETE")}, by:{tenant, user}
   ```

   **Results table**

### Example 4: Create a log metric

In this example, you need to count how many refused connections are recorded in your log data. For that, filter the correct logs and turn the number of occurrences into a log metric.

* [Create connections refused metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-connections-refused-metric "Explore the Log Management and Analytics use case for creating a log metric.")

In this example, you need to monitor an attribute of your logs, and you need to keep an eye on the error levels reported in your logs from your K8s cluster.

* [Create log attribute metric](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric#lma-uc-create-log-attribute-metric "Explore the Log Management and Analytics use case for creating a log metric.")

### Example 5: Create a log alert

In this example, you need to set an alert based on the occurrence of log events. See how you can extract data from logs, create a processing rule, build an alert by forming a log event, and check if your alert captures logs that meet predefined criteria.

* [Set up alerts based on events extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.")

### Create anomaly detection metric

In this use case, you need to automate anomaly detection. See how you can extract data from logs, create a processing rule, create a metric, and create an alert that generates a notification if an anomaly occurs.

* [Set up custom alerts based on metrics extracted from logs](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics "How to create and configure Davis problems and custom alerts with metrics based on logs.")