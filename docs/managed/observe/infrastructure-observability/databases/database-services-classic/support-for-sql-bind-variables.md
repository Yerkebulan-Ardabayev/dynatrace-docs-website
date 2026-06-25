---
title: Support for SQL bind variables
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/databases/database-services-classic/support-for-sql-bind-variables
scraped: 2026-05-12T11:37:13.329936
---

# Support for SQL bind variables

# Support for SQL bind variables

* How-to guide
* 4-min read
* Updated on Apr 26, 2023

Bind variables are a means of parameterizing SQL statements so that the statements have question marks or parameters in their **where** clauses, such as:

* SQL server: `select count (*) from report where tenant = @tenant`
* Java JDBC: `select count (*) from report where tenant = ?`

Bind variables allow the database server to prepare the statement once and execute it multiple times without reparsing or reanalyzing it.

Bind variables aren't applicable to statements that use literals, such as:

```
select count (*) from report where tenant = âxxxxâ
```

These statements can't be parameterized and are reparsed and reanalyzed by the database server with each execution.

Bind variables generate high network and storage demands. To learn more about bind variables support and its availability, see [FAQ](#faq) below.

## Enable capture of SQL bind variables

To enable SQL bind value capture

1. Go to **Settings** > **Server-side service monitoring** > **Deep monitoring**.
2. Expand **Database** and turn on/off **Capture SQL bind values** on the global level.
3. Optional To override the global setup, go to **Process group override**.

   1. To add an override, select **Add process group override** and select the affected process group.
   2. Optional To select a specific process from the selected process group, select the process from the dropdown list.
   3. Select **Add**.
4. Select **Save changes**.

![Capture SQL bind values](https://dt-cdn.net/images/capture-sql-bind-values-942-067033b12f.png)

Capture SQL bind values

Whether you enable this setting site-wide or for individual process groups, you can use Dynatrace OneAgent to capture the values of bind variables. This is applicable to the following technologies:

* ADO.net
* JDBC
* PHP database frameworks

If the array returned by `executeBatch()` contains more than one element, indicating multiple commands were executed, Dynatrace masks the values of the bind variables to ensure data privacy. This is because different executions of `executeBatch()` may aggregate multiple commands, necessitating the masking of bind variable values to prevent the exposure of sensitive information.

## Example of masked and unmasked SQL bind values

A sample result of this feature is distributed tracing. The following webpage illustrates the masking of bind variables.

![Purepath example](https://dt-cdn.net/images/purepath-example-1413-383ad7b07c.png)

Purepath example

Bind variables are considered confidential as they can contain IDs and other sensitive values. [Learn how to ensure the data privacy of your customers](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

Only users who have permission to view a specific entity or management zone can view the bind variables within that entity or zone.

![Purepath example for authorized users](https://dt-cdn.net/images/purepath-example-for-authorized-users-1413-46e0584d5a.png)

Purepath example for authorized users

## FAQ

Does capturing bind variables have negative consequences?

This feature can capture a lot of sensitive data - consequently you should consider its usage carefully.
The feature can also capture a lot of data and increase your network traffic and your storage requirement for distributed traces.
Bind variables can also lead to increased processing and storage demands for your Managed Cluster.