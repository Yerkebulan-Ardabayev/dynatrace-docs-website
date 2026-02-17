---
title: Optimize DQL cost with Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-dql
scraped: 2026-02-17T05:12:44.777769
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