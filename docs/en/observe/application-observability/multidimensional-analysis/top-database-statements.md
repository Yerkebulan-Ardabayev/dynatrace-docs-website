---
title: Top database statements
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis/top-database-statements
scraped: 2026-02-15T09:07:13.074075
---

# Top database statements

# Top database statements

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The **Top database statements** view enables you to understand the overall database activity rather than just the activity of a single database. This view can also be used to better analyze end-to-end database activities during specific timeframes.

To access the **Top database statements** page

1. Go to **Multidimensional Analysis** or ![Databases Services Classic](https://dt-cdn.net/images/databases-512-6aa6fff194.png "Databases Services Classic") **Database Services Classic**.
2. Select **Top database statements**.

## Analyze database statements

The **Top database statements** page displays a chart indicating the top SQL and NoSQL statements in your environment over time. The chart also highlights a few top statements based on execution count. The table following the chart lists the 100 **top dimensions**.

![Top database statements page](https://dt-cdn.net/images/top-database-statements-3564-3bd08ea1b1.png)

You can configure a view by adjusting **Metric** and the other parameters or by adding a filter.

* Different metrics, such as **Fetch count**, **Response time**, and **Row count**, result in different order of the statements. Depending on the time consumption per statement, the frequency of statement execution, or error rate, the page first lists statements that are executed more frequently or are more expensive from a resource perspective, from the highest value of the chosen metric to the lowest.
* You can use **Filter requests** to narrow down the list of database statements.

Filter request examples

The following example shows a view configured with the metric **Response time**, filtered by value range `â¥100ms`. The list shows all database statements which response took at least 100 ms.

![Response time filter in top database statement analysis](https://dt-cdn.net/images/response-time-filter-in-top-database-statement-analysis-3684-0962b8fba9.png)

The view in this example is configured with the metric **Fetch count** filtered by value range `â¥5`. The list shows database statement with at least 5 database fetches per execution.

![Fetch count in top database statements analysis](https://dt-cdn.net/images/fetch-count-in-top-database-statements-analysis-3548-bdb184cbd0.png)

* You can export the table data in a comma-separated values (CSV) file.

  1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

     ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
  2. Select **Export visible data** or **Export table data**.

     Option

     Exported data

     Fields

     Number of entries

     **Export visible data**

     The currently displayed area of the table, taking into account applied filters

     Only visible data

     Up to 100 top dimensions

     **Export table data**

     All table data

     All the available data related to top dimensions

     Up to 100 top dimensions
* The chart uses [trace and request data](/docs/observe/application-observability/multidimensional-analysis#data-source "Configure a multidimensional analysis view and save it as a calculated metric."), which has different data retention periods. For timeframes containing data older than 10 days, you can turn on the **Show data retention** toggle to better understand which data is available for which period directly from the chart.

## Analyze individual SQL statements

To access several statement-specific analysis views, including **Service backtrace** and **Outliers** analysis, select **More** (**â¦**).

### Database statement details

You can directly access analysis for individual statements by selecting **Filter**. Alternatively, select **More** (**â¦**) > **Statement details**.

![Distributed traces of individual database statement](https://dt-cdn.net/images/distributed-traces-top-database-statements-1593-b6fb81c79e.png)

Select a statement to view all permutations of the selected query. Dynatrace aggregates the inserts, updates, and deletes on a per-table basis.

![Details of an individual database statement](https://dt-cdn.net/images/details-individual-statements-1564-56ba5e5697.png)

### Database service backtrace

To access backtrace analysis for the selected statement, select **Service backtrace** from the **Analyze** menu. The **Backtrace** page provides details on the user interaction that triggered the selected SQL statement permutation and the user interaction or service request that originated the statement. Select any of the incoming requests to view a visualization of the backtrace.

![Backtrace for top database statements](https://dt-cdn.net/images/backtrace-for-top-database-statements-1699-76085f0963.png)

### Response time distribution

To understand the response time distribution of the command, select **Outliers** from the **Analyze** menu. The **Response time distribution** page shows the number of requests that fell within various response time ranges. Select any column in the chart to analyze the specific requests that fell within that specific response time range.

![Response time distribution of requests of a service](https://dt-cdn.net/images/response-time-distribution-database-statements-1800-8ff28dc6c7.png)

### View single executions

To view the individual executions of each command, select **More** (**â¦**) > **Distributed traces** > **Trace**.

The **Fetches** column shows the number of database round trips per SQL execution. Because most database drivers page result sets, roundtrips are normally fetched in sets of **Rows returned** per fetch. Therefore, if a result set has 200 rows and you have a fetch size of 50 rows per fetch, it will take 4 fetches to get all the data. More fetches mean slower response time. However, having too large of a fetch size can also lead to poor memory usage and you typically wouldn't read an entire data set anyway.

Select any execution in the list to access its distributed trace.

![PurePathÂ® trace of an execution](https://dt-cdn.net/images/purepath-database-statements-1597-d6db847c88.png)

## Example: Understand SQL for Service flow

While SQL analysis is available at multiple locations in the service-analysis workflow, it has been added as the primary analysis view for databases in the [**Service flow**](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") view. The following example indicates a service flow that has already been filtered to focus on a particular chain of calls. You can see that, whenever the **Customer Frontend** service calls the **JourneyService**, **58%** of the **response time contribution** can be attributed to the **EasyTravel** SQL service.

![From service flow to database statement](https://dt-cdn.net/images/from-service-flow-to-database-statement-1748-bff9188259.png)

The default action has changed and now displays **View database statements**.

You can perform several types of analysis:

1. To see the database statements that were executed by the selected flow within the analysis timeframe, select **View database statements**. This can be tremendously valuable because it shows you why a database contributes a specified amount of time.
2. To reveal which statements have the highest overall response time, sort the **Top dimensions** list by **Count/min**.

![Example of SQL service multidimensional analysis](https://dt-cdn.net/images/example-of-sql-service-multidimensional-analysis-3574-7c039d0068.png)

3. Select **More** (**â¦**) and then:

* Select **Outliers** to see the distribution of response times.
* Select **Distributed traces** to understand the evolution of each individual SQL statement over time, along with the average **Rows returned** count.
* Select **Service backtrace** to see which user clicks led to the slowest executions of the statement.