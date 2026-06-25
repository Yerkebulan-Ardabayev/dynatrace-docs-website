---
title: Analyze database services (classic page)
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services
scraped: 2026-05-12T12:15:26.387759
---

# Analyze database services (classic page)

# Analyze database services (classic page)

* Explanation
* 6-min read
* Updated on Jun 20, 2023

Starting with Dynatrace 1.269, we have totally redesigned the database overview page.

* To switch to the [new database overview page](/managed/observe/infrastructure-observability/databases/database-services-classic/analyze-database-services-new "Analyze your database services with Dynatrace (new page)."), just turn on **Try it out** at the top of the database overview page. You can switch back to the classic design if you decide that you prefer it.
* The documentation below describes the classic design.

Dynatrace monitors the response time, failure rate, throughput, and more of every database statement executed by your applications.

To analyze the performance of a database

1. Go to **Database Services**.
2. To access a database service overview page, select the database you want to analyze.

![Database overview](https://dt-cdn.net/images/database-overview-1297-02a737c3d3.png)

Database overview

The infographics on the database service overview page provide insight into various aspects of database performance, including **SQL queries or procedures**, **SQL modifications**, **SQL transactions**, any detected problems or availability issues, hotspots, and more. The exact list of included tiles depends on the database technology you're monitoring. Each tile contains **Response time**, **Failure rate**, and **Throughput** metrics.

To analyze the individual statements that contribute to a database statement, in the database overview page, select **View database statements**.

## Database details

At the bottom of the **Details** page, you can find a list of all the **Database statements** executed during the selected timeframe. By default, they are sorted by median response time, but you can sort the list by total time, response time, or slowest 10%, and filter it by statement, database name, vendor, process, or hostname.

![Database details page](https://dt-cdn.net/images/database-details-page-1293-85e42be938.png)

Database details page

Select any statement to view its full details. For each statement, Dynatrace shows the number of **Executions**/min, **Total executions**, **Total time**, **Response time** median and slowest 10% of executions, and **Failure rate**.

Statement limits

By default, the length of database statements is limited to 4KB (KiloBytes). This setting isn't configurable. Database statements that exceed this limit are trimmed to 4KB.

### Database service backtrace

To access backtrace analysis for a certain statement

1. In the database statements list, go to the row of the statement you want to analyze.
2. Select **More** (**â¦**) > **Service backtrace**.

![Database service-level backtrace - application](https://dt-cdn.net/images/database-service-level-backtrace-application-1490-89f24b7b0f.png)

Database service-level backtrace - application

The **Backtrace** page provides details on the clicks that triggered the selected permutation of the SQL statement, and it allows you to see which chain of services and which code leads to a particular statement. By selecting a specific application in the backtrace, you can find all the user actions from this application that trigger the database statement you're analyzing.

Example

In the image above, you can see in the **Incoming requests** column that **1,200** database requests on `easyTravelBusiness` originate from **668** user actions.

By selecting `www.easyTravelBusiness.com`, the row indicating that **668** user actions led to **1,150** requests on `easyTravel Customer Frontend` is highlighted. With this selection, you see that three different user actions from `www.easytravel.com` trigger this statement. You can also see the chain of services that trigger it. To investigate further increments of the number of requests in the chain, select any of the subsequent statements in the service call chain.

![Database service-level backtrace - chain](https://dt-cdn.net/images/database-service-level-backtrace-chain-1490-b807b8f624.png)

Database service-level backtrace - chain

With a new selection (`easyTravel Customer Frontend` in the image above), the lower section of the service backtrace page adapts, and you now see that the **668** user actions from `www.easyTravelBusiness.com` call two requests on `easyTravel Customer Frontend` (`/orange-booking-payment.jsf` and `/orange-booking-finish.jsf`). If some of these requests have failed, you can analyze them in the corresponding tab, **Reasons for failed requests**. In this example, we're more interested in the code that leads to the database calls, so we select the **Stacktrace** tab to view the executed code in context.

### Response time distribution

To understand the response time distribution of the command, select **Analyze outliers** on the **Details** page.

The **Response time distribution** page shows the number of requests that fell within various response time ranges. Select any column in the chart to analyze the requests that fell within that specific response time range. This enables you to see if certain statements are called frequently and contribute relatively significantly to the response time.

![Outliers - response time distribution](https://dt-cdn.net/images/database-response-time-distribution-1309-417be68a11.png)

Outliers - response time distribution

## Analyze performance degradation

With Dynatrace database monitoring, you can analyze performance degradation. The statements responsible for a detected slowdown are highlighted in the list of statements at the bottom of the **Details** page.

![Database - response time degradation](https://dt-cdn.net/images/database-4-1090-03b012cb2e.png)

Database - response time degradation

In the example below, the detected response time degradation was caused by two statements (`Aggregations in BookingCollection` and `Aggregations in JourneyCollection`).

To see which service executed a specific statement that led to a database slowdown, go to the statement backtrace.

![Slow database statements](https://dt-cdn.net/images/mysql-7-966-2c43e07703.png)

Slow database statements

Here, `easyTravel-Business` is the service executing the statement causing the slowdown.

![Database service - slow statements](https://dt-cdn.net/images/database-6-1286-28bedc7573.png)

Database service - slow statements

## Analyze database errors

Each tile on the database service overview page features a **Failure rate** graph (1).

![Database - analyze failures](https://dt-cdn.net/images/database-analyze-failures-1755-bca922ddef.png)

Database - analyze failures

Select the **Failure rate** graph (1) to open the failures tab on the **Details** page.

The failed **database statements** table at the bottom of the page immediately shows which statements failed along with their failure rates.

1. Select **View details of failures** to understand the root cause of the failures.  
   Dynatrace determines the causes of the high failure rate, giving you the information to resolve database issues and eliminate future errors.

   ![Failure rate - database details](https://dt-cdn.net/images/failure-rate-database-details-1753-9ba03aabd4.png)

   Failure rate - database details
2. To further analyze the issue, select **Distributed traces** ![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces") or **Backtrace** ![Backtrace](https://dt-cdn.net/images/backtrace-icon-69e2c66211.svg "Backtrace").

   ![Failure analysis](https://dt-cdn.net/images/failure-analysis-1925-81fd9dc157.png)

   Failure analysis

### Quick problem overview

On the database service overview page, the **Current hotspots** section (2) offers a quick view of the problem, highlighting the statement with the highest failure rate. By selecting a statement in this section (2) you can directly view the failures tab on its **Details** page.

![View of the statement with the highest failure rate from current hotspots.png](https://dt-cdn.net/images/failure-rate-current-hotspots-1760-57af484dd4.png)

View of the statement with the highest failure rate from current hotspots.png

## Service flow for SQL analysis

[**Service flow**](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") visualizes the sequence of service calls that are triggered by each service request in your environment. With the service flow, you see the flow of service calls, including database-service calls, from the perspective of a single service, request, or their filtered subset. While SQL analysis is available at multiple locations in the service-analysis workflow, it's the primary analysis view for databases in the **Service flow** view.

To view the service flow triggered by a specific database service

1. Go to **Services**.
2. Select the service you want to analyze.
3. On the service overview page, under **Understand dependencies**, select **View service flow**.

![Service flow - SQL analysis](https://dt-cdn.net/images/service-flow-sql-analysis-1759-f706b49d27.png)

Service flow - SQL analysis

Example

In the example above, the database-service flow is filtered to focus on a particular chain of calls. Whenever the `easyTravel Customer Frontend` calls `JourneyService`, **0.01%** of the **response time contribution** can be attributed to `EasyTravelBusiness` MongoDB service.

To view the database statements that were executed by the selected flow within the analysis time frame, select **View database statements**. This can be tremendously valuable because it helps you understand why a database contributes a certain amount of time.

![Multidimesional analysis of top dimensions](https://dt-cdn.net/images/multidimesional-analysis-sql-analysis-1752-aa2f7307ab.png)

Multidimesional analysis of top dimensions

For one of the **top dimensions**, select **More** (**â¦**) and then

* Select **Outliers** to understand the spread of response times.
* Select **Statement details** to understand the evolution of each SQL statement over time, along with the average **Rows returned** count.
* Select **Service backtrace** to see which user clicks led to the slowest executions of this MongoDB statement.

As you can see, Dynatrace database-statement analysis views provide powerful database usage-focused analysis.

## Related topics

* [Top database statements](/managed/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")
* [Service backtrace](/managed/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.")