# Документация Dynatrace: dynatrace-intelligence/use-cases
Язык: Русский (RU)
Сгенерировано: 2026-02-24
Файлов в разделе: 6
---

## dynatrace-intelligence/use-cases/copilot-examples.md

---
title: Generative AI quick analysis examples
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-examples
scraped: 2026-02-24T21:28:17.597844
---

# Generative AI quick analysis examples

# Generative AI quick analysis examples

* Latest Dynatrace
* Reference
* 9-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI can help you analyze data for many different use cases. See the examples below to understand what kind of DQL output you can expect from your prompts.

See the selected pairs to understand what kind of DQL output you can expect from your prompts.

## Analyze logs with generative AI

## Analyze events with generative AI

## Analyze business events with generative AI

## Analyze Davis events with generative AI

## Analyze spans with generative AI

## Analyze metrics with generative AI

## Analyze entities with generative AI

## Analyze problems with generative AI

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")

---

## dynatrace-intelligence/use-cases/copilot-in-workflows-dql.md

---
title: Optimize DQL cost with Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-dql
scraped: 2026-02-24T21:22:48.283491
---

# Optimize DQL cost with Workflows

# Optimize DQL cost with Workflows

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Feb 05, 2026
* Preview

With [Dynatrace Intelligence (Preview)](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows."), you can automate problem summarization and ask Dynatrace Intelligence generative AI to suggest remediation steps that can be sent to your email.

## Overview

With this guide:

* You get introduced to cost optimization for Dynatrace Query Language (DQL) using Dynatrace Intelligence (Preview).
* You learn how to automate insights and recommendations to reduce query execution costs.

## Target Audience

This guide is written for:

* Observability engineers
* Platform owners
* FinOps practitioners
* SREs

## Scenario

* Automatically detect high-cost DQL queries.
* Receive optimization suggestions and cost-saving actions via email or chat.

To help teams manage observability costs more effectively, this use case demonstrates how to automate the identification and optimization of expensive Dynatrace Query Language (DQL) executions.

A simple workflow, scheduled to run once daily, detects the top 20 most costly queries from the past 24 hours. By integrating Dynatrace Intelligence generative AI into this workflow, each query is automatically analyzed for optimization opportunities.

Our generative AI provides tailored recommendations to reduce query costs and sends these insights directly to the respective query authors via email. This helps you to proactively control costs and improve query efficiency without manual intervention.

## Before You Begin

### Prerequisites

To use Dynatrace Intelligence (Preview), ensure that you have:

* **Conversational recommender** (`ALLOW davis-copilot:conversations:execute;`) permission.
* Installed  **Dynatrace Intelligence (Preview)**.
* Access to DQL usage metrics and billing data.

## Steps

1. Configure a workflow trigger

1. Go to **Workflows**.
2. Select **+ Workflow** to create a new workflow.
3. From triggers, select **Fixed time trigger**.
4. Configure the fields:

* Set the **Run at** to your desired time.
* Set the **Rule** to **Every day**.

2. Get the expensive queries

1. Select **+ Add task**.
2. In the search field, enter **DQL query**, or select **Execute DQL Query** from the list of the Workflow actions.
3. Rename the task to `dql_query`.
4. In the **DQL query** field, add the following query:

   ```
   fetch dt.system.query_executions, from:now() - 24h



   | filter status == "SUCCEEDED"



   | summarize executionCount = count(), sum = sum(scanned_bytes.on_demand), user = collectDistinct(user.email), app = collectDistinct(client.application_context), by: {query_string}



   | sort sum desc



   | limit 20
   ```

3. Ask Dynatrace Intelligence generative AI to find the improvements for every query

1. Select **+ Add task**.
2. In the search field, enter **Dynatrace Intelligence**, or select **Define prompt** from the list of the Workflow actions.
3. Configure Dynatrace Intelligence generative AI:

* In the **Prompt** field, enter the following prompt:

  ```
  I've supplied you with result of a DQL Grail query. This result has information about top 20 expensive executed by users in last 24 hours.



  Create a json array with the following info:



  - query: that is the original query that is given in the result



  - email: email of the user who executed the query



  - improvement: tell me the reasons why query is expensive and how can user improve it



  - context: any relevant context where the query is executed and so on



  Make sure that there is no other text beside the json array and no backticks or anything
  ```
* In the **Additional context** field, enter the following:
  `{{result('dql_query').records}}`
* Enable **Auto-trim**.
* Ensure that **Document retrieval** is set to **Disabled**.
* Rename the task to `davis_copilot`.

4. Send Dynatrace Intelligence generative AI results to user's emails

1. Select **+ Add task**.
2. In the search field, enter **Send email**, or select **Send email** from the list of the Workflow actions. For more information about the Email workflow actions, see [Email](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
3. Enter the workflow task name.
4. Configure the fields:

* In **Configure email > Recipients**, set the **To** field to `{{_.list.email}}`. This is the email of the user.
* In the **Content, Subject** field, enter the following text: `Expensive query executed`.
* Set the **Message** field to the following:

  ```
  Hi {{_.list.email}},



  You've executed an expensive query that could be optimized to reduce costs. Below are the details to help you improve it:



  ---



  ### Query Details:



  - **Original Query**:



  `{{_.list.query}}`



  - **Suggested Improvements**:



  {{_.list.improvement}}



  - **Context**:



  {{_.list.context}}



  ---



  Taking these steps can help improve performance and reduce expenses.



  Thanks,



  Your Admin
  ```
* Go to the **Options** tab and configure the fields as following:

* Enable **Loop task**.
* Enter `list` in the **Item variable name** field and enter `{{result('davis_copilot').text}}` in the **List** field.

5. Finalize workflow configuration

1. Select **Deploy** to deploy the workflow.
2. Select **Run** to test the workflow.

## Related topics

* [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.")
* [Dynatrace Intelligence (Preview) app](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows.")
* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")

---

## dynatrace-intelligence/use-cases/copilot-in-workflows-examples.md

---
title: Summarize open problems with Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples
scraped: 2026-02-24T21:31:25.522175
---

# Summarize open problems with Workflows

# Summarize open problems with Workflows

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Feb 05, 2026
* Preview

With [Dynatrace Intelligence (Preview)](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows."), you can automate problem summarization and ask Dynatrace Intelligence generative AI to suggest remediation steps that can be sent to your email.

## Target audience

This guide is written for:

* Operations engineers
* Pipeline engineers
* Systems engineers
* Site reliability engineers (SREs)
* Build automation engineers

## Scenario

Letâs assume you want to automate analyzing new problems and get immediate suggestions for resolving the issue.
To do this, you need to create a workflow that uses Dynatrace Intelligence generative AI to summarize all open problems and automatically suggest the best way to remediate them.
When a new problem is opened, the workflow will automatically run, and the Dynatrace Intelligence generative AI response will be sent to your email.

## Before you begin

### Prerequisites

To use Dynatrace Intelligence (Preview), ensure that you have:

* **Conversational recommender** (`ALLOW davis-copilot:conversations:execute;`) permission.
* Installed  **Dynatrace Intelligence (Preview)**.

## Steps

1. Configure a workflow trigger

1. Go to ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") Workflows.
2. Select  **Workflow** to create a new workflow.
3. From **Event** triggers, select a **Davis problem trigger**.
4. Configure the fields:

   * Set the **Event state** to `active`.
   * Set the **Event category** to `Custom`.
   * Set **Affected entities** to `include entities with all defined tags below`.
   * Set **Additional custom filter query** to

     ```
     matchesPhrase(event.name, "Host cpu stateful custom alert 1h")
     ```

     This example demonstrates filtering for a specific problem.
     However, you can apply a filter to include all new problems as well.

1. An example of setting a Davis problems trigger

![An example of setting a Davis Problem trigger for new problems.](https://dt-cdn.net/images/generative-ai-in-workflows-set-trigger-1920-775b0ee285.png)

2. Extract problem details

1. Select  Add task.
2. In the  search field, enter `Run JavaScript`, or select **Run JavaScript** from the list of the ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow** actions. For more information about the JavaScript workflow action, see [Run JavaScript action for Workflows](/docs/analyze-explore-automate/workflows/default-workflow-actions/run-javascript-workflow-action "Execute JavaScript action for your workflows.").
3. Enter the workflow task name.
4. In the **Input** tab, enter the following **Source code**:

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function ({ executionId }) {



   const ex = await execution(executionId);



   let rawEvent = ex.params.event;



   let problemDescription = rawEvent["event.description"];



   return {



   description : rawEvent["event.description"],



   problem_id : rawEvent["display_id"]



   };



   }
   ```

1. An example of setting a JavaScript action

![An example of setting a javascript action to extract problem details](https://dt-cdn.net/images/copilot-in-workflows-run-javascript-1896-4a0406181b.png)

3. Ask Dynatrace Intelligence generative AI to summarize the problem and suggest remediation steps

1. Select  Add task.
2. In the  search field, enter `Dynatrace Intelligence`, or select  **Define prompt** from the list of the ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow** actions.
3. Configure Dynatrace Intelligence generative AI:

   * In the **Prompt** field, enter the following prompt:

     ```
     A new Davis Problem with id {{result("extract_problem_details").problem_id}} has just been opened. Please provide a summary of what happened and actionable steps to remediate it. Provide output as plain text without any formatting or markdown
     ```
   * In the **Additional context** field, enter the following:

     ```
     Use the following information about the Davis Problem with Id {{result("extract_problem_details")["problem_id"]}}:



     """



     {{result("extract_problem_details")["description"]}}



     """
     ```
   * Enable **Auto-trim**.
   * Set **Document retrieval** to `Disabled`.

1. An example of preparing a Dynatrace Intelligence generative AI prompt

![An example of setting a Dynatrace Intelligence action to summarize new problems.](https://dt-cdn.net/images/set-dynatrace-intelligence-action-in-workflows-1920-8fd3190dc2.png)

4. Send Dynatrace Intelligence generative AI results to your email

1. Select  Add task.
2. In the  search field, enter `Send email`, or select ![Email for Workflows](https://dt-cdn.net/images/email-for-workflows-new-256-f6c0e2d343.png "Email for Workflows") **Send email** from the list of the ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow** actions. For more information about the Email workflow actions, see [Email](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
3. Enter the workflow task name.
4. Configure the fields:

   * In **Configure email** > **Recipients**, set the **To** field to your email address. If you want to add more than one email address, use `;` to separate them.
   * In the **Content**, **Subject** field, enter the following text:

     ```
     New Davis Problem {{ result("extract_problem_details")["problem_id"] }} started
     ```
   * Set the **Message** field to the following:

     ```
     A Davis Problem with ID {{ result("extract_problem_details")["problem_id"] }} has been opened.



     Dynatrace Intelligence generative AI has analyzed it and provided the following information:



     {{ result("analyze_problem_with_davis_copilot")["text"] }}
     ```

1. An example of an email configuration

![An example of configuring an email to send Dynatrace Intelligence generative AI results.](https://dt-cdn.net/images/generative-ai-in-workflows-send-email-1920-47ec9a8954.png)

5. Finalize workflow configuration

1. Select  **Save**.
2. Select  **Run** to test the workflow.

Once a new problem appears, you should receive an email from `no-reply@dev.apps.dynatracelabs.com`. You can see the example of the message content below:

![An example of an email from Dynatrace Intelligence generative AI in workflows use case](https://dt-cdn.net/images/copilot-in-workflows-email-example-1584-f32b4d0bbb.png)

## Related topics

* [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.")
* [Dynatrace Intelligence (Preview) app](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows.")
* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Dynatrace Intelligence (Preview) app](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows.")

---

## dynatrace-intelligence/use-cases/create-alert-in-logs.md

---
title: Create log alerts for a log event or summary of log data
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/create-alert-in-logs
scraped: 2026-02-24T21:27:08.168202
---

# Create log alerts for a log event or summary of log data

# Create log alerts for a log event or summary of log data

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Jan 28, 2026

One of the uses of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** is to alert users of abnormal behavior. For example, using the `makeTimeseries` DQL command, you can set up a custom alert to analyze or alert on various data such as business events or logs. In this case, the custom alert queries the raw data every minute. However, if you have infrequent log entries, or if you're interested in a specific log event, you can use alternative solutions that are more cost- and time-effective.

In this tutorial, you will learn how to

* Create a log alert for a specific log event.
* Create a log alert for a specific time period.

## Prerequisites

* Access to a Dynatrace SaaS environment
* Installed ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**

For the [Create a log alert on a summary of log data using DQL](#create-log-custom-alert-with-dql) use case, you will also need the following:

* [Configured ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** permissions](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")

## Raise a log alert based on a specific log event

If you want to monitor a specific log event and be notified when it occurs, you can create an alert based on a filtered query to avoid processing the entire raw log.

Let's assume you want to set an alert that notifies you every time NGINX logs containing the `Connection refused` error is captured. In addition, you want to extract the following information from the log content to get a quick overview of the event:

* Error number
* Client IP address
* `http_request` line that results in an error.

To save time and effort, you can set a log alert instead of an anomaly detection alert. In this case, you don't have to make a timeseries. Instead, you just need to create a filtered query that will show only the specific event, for example:

```
fetch logs



| filter matchesValue(process.technology, "nginx")



| filter matchesValue(loglevel, "ERROR")



| filter matchesPhrase(content, "Connection refused")



| fields timestamp,content, process.technology



| parse content, "LD '[error] ' INT:error_number '#' INT LD 'Connection refused' LD 'client:' SPACE? IPADDR:client_ip LD 'request:' SPACE? DQS:http_request"



| sort timestamp desc
```

Creating a log alert doesn't require you to have access to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**. You only need **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events"). To learn more about creating alerts through **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events"), see [Set up a log alert](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

## Raise a log alert on a summary of log data over a time period

If you want to get an overview of the log data over a specific period, for example, if the data has infrequent log entries, you can use one of the approaches:

* Create a dedicated log metric.
* Use DQL to create a log alert on a summary of log data.

### Create a dedicated log metric

Creating a dedicated log metric allows you to reuse the log metric across apps like **Dashboards** ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") and **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") and create alerts without incurring additional costs.

To learn how to create log metrics, see [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.").

Suppose you created a log metric, `log.conn_refused_count`, which collects every log entry with a `Connection refused` error.

![An example of the Analyze and alert settings for a log metric graph, with anomaly detection selected, in the Notebooks app.](https://dt-cdn.net/images/notebooks-log-metric-analyze-and-alert-1741-740d26f404.png)

Since the data in the log metric contains only the necessary logs, you can create the alert using the regular `timeseries` DQL command and the name of your log metric as a parameter.

### Create a log alert on a summary of log data using DQL

Using DQL allows you to create complex queries and apply multiple filters and sorting conditions. This approach gives you more control on what data you want to capture and what kind of information you want to see in your alerts.

To create a log alert on a summary of log data

1. Open **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Select  **Notebook** >  **New section** >  **DQL** to create a new section.
3. Fill out the field similar to the example below:

   ```
   fetch logs



   | filter dt.system.bucket == "{your bucket name}"



   | filter matchesPhrase(content, "Connection refused")



   | makeTimeseries count(), interval:1m
   ```
4. Optional Select  **Run** to test and ensure that your command works properly.
5. Select  **Options** and select  **Analyze and alert**.
6. Turn on the Dynatrace Intelligence data analyzer if it's not active.
7. Select the required analyzer and configure it. For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.").
8. Select **Run analysis**.
9. Once you're satisfied with the result, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** and select **Anomaly Detection**.  
   This action takes you to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
10. Expand **Create an event template** and configure the event triggered by the configuration. For details, see [Event template](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#event-template "How to set up an alert for missing measurements.").
11. Select **Create**.

![An example of the Analyze and alert settings for a bucket log metric graph, with anomaly detection selected, in the Notebooks app.](https://dt-cdn.net/images/notebooks-bucket-log-metric-analyze-and-alert-1744-cef4fa6326.png)

Extracting data from the `default_logs` bucket might induce additional costs. If your logs are available in a specific bucket, we recommend using `filter dt.system.bucket == "{your bucket}"` to increase efficiency.

If you don't have access to your team's or department's bucket, you can create a private one following the [bucket assignment](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.") documentation.

## Conclusion

Apart from standard Anomaly Detection alerts, Dynatrace offers other solutions, such as:

* Creating a log alert for a specific event.
* Creating an alert of log data over a period of time.

If you followed these steps, now you know how to create log alerts for specific events and a summary of the log data over a period of time.

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [[Video] Elevating Security with Anomaly Detectionï»¿](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Video] Anomaly Detection and Data Observabilityï»¿](https://www.youtube.com/watch?v=HPQi63mQg3w)

---

## dynatrace-intelligence/use-cases/davis-dql-examples.md

---
title: Dynatrace Intelligence DQL examples
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-dql-examples
scraped: 2026-02-24T21:18:22.552249
---

# Dynatrace Intelligence DQL examples

# Dynatrace Intelligence DQL examples

* Latest Dynatrace
* Reference
* 7-min read
* Updated on Jan 28, 2026

These examples illustrate how to build powerful and flexible health dashboards by using DQL to slice and dice all Dynatrace Intelligence reported problems and events.

Davis problems represent results that originate from the Dynatrace Intelligence root-cause analysis runs. In Grail, Davis problems and their updates are stored as Grail events.

* [Problem example 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Count the total number of problems in the last 24 hours.
* [Problem example 2](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample2 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Count the current number of active problems.
* [Problem example 3](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample3 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Chart the number of problems in the last 7 days to identify a trend within your environment stability.
* [Problem example 4](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample4 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Identify the top 10 problem-affected entities within your environment.
* [Problem example 5](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample5 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Join entity attributes with detected problems and apply a name filter.
* [Problem example 6](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample6 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Load the last state of a given problem.
* [Problem example 7](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample7 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Load all active problems and exclude all those that are marked as duplicates.
* [Problem example 8](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample8 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Calculate the mean time to resolve for problems over time.
* [Problem example 9](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample9 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Show a chart of the concurrently open problems over time.

Davis events represent raw events that originate from various custom alerts within Dynatrace or within the OneAgent. Examples here are OneAgent-detected CPU saturation events or high garbage collection time events.

* [Davis event example 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpdaviseventexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Chart the number of process restart events in the last 7 days.

## Count the total number of problems in the last 24 hours

* Fetches table `dt.davis.problems`.
* Uses the summarize DQL command to get the total number of distinct problems.
* The `event.id` holds the unique problem ID, which is stable across all refreshes and updates that Dynatrace Intelligence reports for the same problem.

```
fetch dt.davis.problems, from:now()-24h, to:now()



| summarize {problemCount = countDistinct(event.id)}
```

**Query result**

## Count the current number of distinct active problems

* Fetches table `dt.davis.problems`.
* Groups the result by the unique `event.id` field, which contains the problem ID.
* Filters out all problems that are no longer in state `ACTIVE`. To do this, the DQL command `takeLast` of the field `event.status` receives the last state.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE"



| summarize {activeProblems = countDistinct(event.id)}
```

**Query result**

## Chart the number of problems from the last 7 days

* Fetches table `dt.davis.problems`.
* Shows the number of problems that occurred during the day over the span of 7 days.
* Counts in a resolution of 6-hour bins.
* Allows to identify stability trends within your environment

```
fetch dt.davis.problems, from:now()-7d



| makeTimeseries count(default:0)
```

**Query result**

## Identify the top 3 problem-affected entities within your environment

* Fetches table `dt.davis.problems`.
* Expands the arrays field containing all affected entity IDs into individual fields.
* Counts all unique problems grouped by the affected entity IDs.
* Sorts by that problem count.
* Returns the top 3 entity IDs.

```
fetch dt.davis.problems



| expand affected_entity_ids



| summarize count = countDistinct(display_id), by:{affected_entity_ids}



| sort count, direction:"descending"



| limit 3
```

**Query result**

## Fetch all problems for a host with the name "myhost"

This example joins entity attributes in order to filter all problems with a given host name.

* Fetches table `dt.davis.problems`.
* Expands the arrays field containing all affected entity IDs into individual fields.
* Does a topology and entity lookup on the `affected_entity_ids` field.
* Enriches the resulting records with two entity fields that are prefixed with `host.`: `host.id` and `host.name`.
* Applies a filter for the host name `myhost`.

```
fetch dt.davis.problems



| expand affected_entity_ids



| fieldsAdd host.name = entityName(affected_entity_ids, type: "dt.entity.host")



| filter host.name == "myhost"
```

**Query result**

## Load the last state of a given problem

This example shows you how to filter problems by a unique ID.

* Fetches table `dt.davis.problems`.
* Filters by the unique display identifier of the problem.
* Allows to find problems connected to a particular ID.

```
fetch dt.davis.problems



| filter display_id == "P-24051200"
```

**Query result**

## Load all active problems and exclude all those that are marked as duplicates

This example shows you how to fetch all active problems that weren't marked as duplicates.

Since the duplicate flag appears during the lifecycle of a problem, the update events need to be sorted by timestamp. Then, the events need to be summarized by taking the last state of the duplicate and status fields. It's possible to correctly apply the filter only after you sort the events by the timestamp.

* Fetches table `dt.davis.problems`.
* Filters out problems that are marked as duplicates.
* Filters out problems that were closed already.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE" and not dt.davis.is_duplicate == "true"
```

**Query result**

## Calculate the mean time of resolving problems over time

This example shows you how to calculate the mean time that was needed to resolve all the reported problems by summarizing the delta between start and end of each problem over time.

* Fetches table `dt.davis.problems`.
* Flattens the problem fields into the record.
* Filters out all frequent and duplicate problems.
* Returns all closed problems.
* Converts the values into a time series of averages over time.

```
fetch dt.davis.problems, from:now()-7d



| filter event.status == "CLOSED"



| filter dt.davis.is_frequent_event == false and dt.davis.is_duplicate == false and maintenance.is_under_maintenance == false



| makeTimeseries `AVG Problem duration in hours` = avg(toLong(resolved_problem_duration)/3600000000000.0), time:event.end
```

## Show a chart of the concurrently open problems over time

This example shows how to create a chart displaying the number of concurrently open problems over time. The resolution gaps are filled with the `spread` command.

* Fetches table `dt.davis.problems`.
* Creates a time series of the problem count.
* Fills the gaps between start and end timestamps of a problem with the correct count by using the `spread` command.

```
fetch dt.davis.problems



| makeTimeseries count = count(), spread: timeframe(from: event.start, to: coalesce(event.end, now()))
```

## Chart the number of CPU saturation and high-memory events in the last 7 days

* Fetches table `dt.davis.events` for the last 7 days.
* Counts in a resolution of 60-minute bins.

```
fetch dt.davis.events, from:now()-7d, to:now()



| filter event.kind == "DAVIS_EVENT"



| filter event.type == "OSI_HIGH_CPU" or event.type == "OSI_HIGH_MEMORY"



| makeTimeseries count =  count(default: 0)
```

**Query result**

---

## dynatrace-intelligence/use-cases/davis-for-workflows.md

---
title: AI in Workflows - Predictive maintenance of cloud disks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-for-workflows
scraped: 2026-02-24T21:22:46.935376
---

# AI in Workflows - Predictive maintenance of cloud disks

# AI in Workflows - Predictive maintenance of cloud disks

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence data analyzers offer a broad range of general-purpose artificial intelligence and machine learning (AI/ML) functionality, such as learning and predicting time series, detecting anomalies, or identifying metric behavior changes within time series. Dynatrace Intelligence enables you to seamlessly integrate those analyzers into your custom workflows. An example use case is a fully automated task of predicting and remediating future capacity demands. It helps you to avoid critical outages by being notified days in advance before incidents even arise.

## Install Dynatrace Intelligence (Preview)

To use Dynatrace Intelligence actions, you first need to install **Dynatrace Intelligence (Preview)** from Dynatrace Hub.

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Dynatrace Intelligence (Preview)**.
2. Select **Dynatrace Intelligence (Preview)** and select **Install**.

After installation, Dynatrace Intelligence actions appear automatically in the **Chose action** section of [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

## Example use case

This use case shows how you can leverage the Dynatrace Intelligence predictive AI analyzer to foresee future disk capacity needs and raise predictive alerts weeks before critical incidents occur.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Grant necessary permissions](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#permissions "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Explore capacity measurements](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#explore "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Define a trigger schedule](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#schedule "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

Configure the forecast](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#forecast "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

Evaluate the result](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#evaluate "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

Remediate before it happens](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#remediate "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

Review raised problems](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#problems "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")

### Step 1 Grant necessary permissions

A successful Dynatrace Intelligence analysis requires proper access rights.

1. In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, go to **Settings** > **Authorization settings**.
2. Grant the following primary permission.

   ```
   app-engine:functions:run
   ```
3. Grant the following secondary permissions.

   ```
   davis:analyzers:read



   davis:analyzers:execute



   storage:bizevents:read



   storage:buckets:read



   storage:events:read



   storage:logs:read



   storage:metrics:read



   storage:spans:read



   storage:system:read
   ```
4. In the top right, select **Save**.

### Step 2 Explore capacity measurements in a notebook

Predictive capacity management starts within [**Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") where you need to configure your capacity indicators. The image below shows an example of the free disk percentage indicator for an operations team.

![An example of an AI data analysis forecast.](https://dt-cdn.net/images/notebooks-data-analyzer-forecast-1891-28bee08431.png)

Once you have the required indicators, it's time to build the workflow that triggers a forecast at regular intervals.

### Step 3 Define a trigger schedule

In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, configure the required schedule to trigger the forecast. To learn how, see [Workflow schedule trigger](/docs/analyze-explore-automate/workflows/trigger/schedules "Guide to creating workflow automation schedule triggers in Dynatrace Workflows."). The image below shows the workflow that runs at 8:00 AM to trigger the forecast of all the disks that are likely to run out of space in the next week.

![Example of a Dynatrace Intelligence trigger in the Workflows app.](https://dt-cdn.net/images/workflows-forecast-trigger-1920-652d16e024.png)

### Step 4 Configure the forecast

To trigger the forecast from a workflow, you need the **Analyze data** action. The action uses the forecast analysis and a data set for the forecast. You can use any time series data for the forecast. All you need is to fetch it from Grail via a DQL query. Here, we define a set of disks for which we want to predict capacity. We use the `dt.host.disk.free` metric, but you can use any capacity metricâhost CPU, memory, network load. You can even extract the value from a log line.

Our forecast is trained on a relative timeframe of the last seven days, specified in the DQL query. It predicts 100 data points; that is, the original 120 points fetched from Grail are expanded by predicted 100 data points, spanning approximately one week into the future. See the DQL query below.

The action returns all the forecasted time series, which could be hundreds or thousands of individual disk predictions.

To configure this forecast in the action

1. Add a new **Analyze data** action.
2. Set the name of the action as `predict_disk_capacity`.
3. Select the **Generic Forecast Analysis** as an analyzer.
4. In **Time series data**, specify the following DQL query:

   ```
   timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}, bins: 120, from:now()-7d, to:now()
   ```
5. Set **Data points to predict** as `100`.

![Dynatrace Intelligence forecast for workflows in the Workflows app.](https://dt-cdn.net/images/dynatrace-intelligence-forecast-for-workflows-1920-de2e97e37b.png)

### Step 5 Evaluate the result

The next workflow action tests each prediction to determine whether the disk will run out of space during the next week. It's a **Run JavaScript** action, running the custom TypeScript code, checking threshold violations, and passing all violations to the next action. It returns a custom object with a boolean flag (`violation`) and an array containing violation details (`violations`).

1. Add a new **Run JavaScript** action.
2. Set the name of the action as `check_prediction`.
3. Use the following source code.

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   const THRESHOLD = 15;



   const TASK_ID = 'predict_disk_capacity';



   export default async function ({ executionId }) {



   const exe = await execution(executionId);



   const predResult = await exe.result(TASK_ID);



   const result = predResult['result'];



   const predictionSummary = { violation: false, violations: new Array<Record<string, string>>() };



   console.log("Total number of predicted lines: " + result.output.length);



   // Check if prediction was successful.



   if (result && result.executionStatus == 'COMPLETED') {



   console.log('Prediction was successful.')



   // Check each predicted result, if it violates the threshold.



   for (let i = 0; i < result.output.length; i++) {



   const prediction = result.output[i];



   // Check if the prediction result is considered valid



   if (prediction.analysisStatus == 'OK' && prediction.forecastQualityAssessment == 'VALID') {



   const lowerPredictions = prediction.timeSeriesDataWithPredictions.records[0]['dt.davis.forecast:lower'];



   const lastValue = lowerPredictions[lowerPredictions.length-1];



   // check against the threshold



   if (lastValue < THRESHOLD) {



   predictionSummary.violation = true;



   // we need to remember all metric properties in the result,



   // to inform the next actions which disk ran out of space



   predictionSummary.violations.push(prediction.timeSeriesDataWithPredictions.records[0]);



   }



   }



   }



   console.log(predictionSummary.violations.length == 0 ? 'No violations found :)' : '' + predictionSummary.violations.length + ' capacity shortages were found!')



   return predictionSummary;



   } else {



   console.log('Prediction run failed!');



   }



   }
   ```

### Step 6 Remediate before it happens



You have a variety of remediation actions to follow up on predicted capacity shortages. In our example, the workflow raises a Davis problem and sends a Slack message for each potential shortage. Both are conditional actions that only trigger if the forecast predicts any disk space shortages.

Each raised Davis problem carries custom properties that provide insight into the situation and help to identify the problematic disk.

![An example of a Dynatrace Intelligence conditional action.](https://dt-cdn.net/images/workflows-forecast-conditional-action-1920-8dbefdfc44.png)

To send a message

1. Add a new **Send message** action.
2. Set the name of the action as `send_message`.
3. Configure the message. To learn how, see [Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces").
4. Open the **Conditions** tab.
5. Select the `success` condition for the **check\_prediction** action.
6. Add the following custom condition:

   ```
   {{ result('check_prediction').violation }}
   ```

To raise a Davis problem

1. Add a new **Run JavaScript** action.
2. Set the name of the action as `raise_violation_events`.
3. Use the following source code.

   ```
   import { eventsClient, EventIngestEventType } from "@dynatrace-sdk/client-classic-environment-v2";



   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function ({ executionId }) {



   const exe = await execution(executionId);



   const checkResult = await exe.result('check_prediction');



   const violations = await checkResult.violations;



   // Raise an event for each violation



   violations.forEach(function (violation) {



   eventsClient.createEvent({



   body : {



   eventType: EventIngestEventType.ResourceContentionEvent,



   title: 'Predicted Disk Capacity Alarm',



   entitySelector: 'type(DISK),entityId("' + violation['dt.entity.disk'] + '")',



   properties: {



   'dt.entity.host' : violation['dt.entity.host']



   }



   }



   });



   });



   };
   ```
4. Open the **Conditions** tab.
5. Select the `success` condition for the **check\_prediction** action.
6. Add the following custom condition.

   ```
   {{ result('check_prediction').violation }}
   ```

### Step 7 Review all Dynatrace Intelligence predicted capacity problems

In Dynatrace, the operations team can review all predicted capacity shortages in the Dynatrace Intelligence problems feed.

Raising a problem is an optional remediation step that you can skip completely, opting for notifications for responsible teams. In this example it illustrates the flexibility and power of the AutomationEngine combined with the analytical capabilities of Dynatrace Intelligence and Grail.

![An example of Dynatrace Intelligence Capacity Prediction and Predictive Alerts.](https://dt-cdn.net/images/problems-predictive-capacity-alert-3600-89a8dfa6a9.png)

## Related topics

* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

---
