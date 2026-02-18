# Dynatrace Documentation: dynatrace-intelligence/dynatrace-intelligence-integrations

Generated: 2026-02-18

Files combined: 2

---


## Source: copilot-for-workflows.md


---
title: Dynatrace Intelligence (Preview) app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows
scraped: 2026-02-18T05:45:03.972584
---

# Dynatrace Intelligence (Preview) app

# Dynatrace Intelligence (Preview) app

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Feb 04, 2026
* Preview

With ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, you can automate requests to Dynatrace Intelligence generative AI and have it react to changes in the environment as they happen, summarizing events and daily activities and suggesting optimal solutions for open problems and changes within the code.

You can also schedule the repeated workflow execution and configure it to send Dynatrace Intelligence generative AI responses to your email or Slack channels.
The scheduled and repeated workflow execution helps save time and lets you focus on other tasks while Dynatrace Intelligence generative AI reviews and analyzes the incoming changes for you.

## Use cases

## Prerequisites

To use the Dynatrace Intelligence generative AI workflow action, ensure that you have the following permission:

* **Conversational recommender** `ALLOW davis-copilot:conversations:execute;`

  For more information about assigning the **Conversational recommender** permission, see [User permissions](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Learn how to set up Dynatrace Intelligence generative AI.").

To use  **Dynatrace Intelligence (Preview)**, you need to

1. Ensure that you have a Hub subscription for the Dynatrace Intelligence generative AI Preview channel.

   If you don't have a subscription, please reach out to your Customer Success Manager (CSM).
2. Install  **Dynatrace Intelligence (Preview)**.

To install  **Dynatrace Intelligence (Preview)**

1. In ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") Dynatrace Hub, search for  **Dynatrace Intelligence (Preview)**.
2. Select  **Dynatrace Intelligence (Preview)** and select **Install**.

## Limits

Standard usage limits for  **Generative AI** are also applied to  **Dynatrace Intelligence (Preview)**:

Item

Maximum limit

Individual user requests

25 requests per 15 minutes

All user requests across the environment

60 requests per 15 minutes

This means that, if you schedule the automatic workflow execution to run frequently, all other Dynatrace Intelligence generative AI functionality might get throttled due to reaching the request limit. If you do run into the usage limit, please reach out to your CSM or let us know in the [Agentic AI Preview User Groupï»¿](https://dt-url.net/copilot-community) in our Community.

## Set up a Dynatrace Intelligence generative AI workflow action

To create a workflow with  **Dynatrace Intelligence (Preview)** action

1. In Dynatrace, go to ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
2. Select  **Workflow** to create a new workflow.
3. Choose a [workflow trigger](/docs/analyze-explore-automate/workflows/trigger "Introduction to workflow automation triggers for workflows.") that will prompt the execution of the workflow.
4. Select  **Add task**.
5. Type `Dynatrace Intelligence` into the  search field or select  **Dynatrace Intelligence** >  **Define prompt**.
6. Configure the action:

   * In the **Prompt** field, enter your question or request. You can also add specific formatting instructions to better suit your use case.

     You can enter a maximum of 5,000 characters in this field.
   * Optional In the **Additional context** field, provide any additional context (for example, a code snippet or a supplementary information about a problem or event) you want Dynatrace Intelligence generative AI to reference when executing your prompt. You can reference an output from a previous workflow action in this field.

     You can enter a maximum of 20,000 characters in this field.
   * Enable **Auto-trim** to automatically trim your prompt and additional context if the character limit is exceeded. If **Auto-trim** is disabled and your prompt or additional context exceed the character limit, the action execution will fail.
   * Set **Document retrieval** to `Dynatrace` if you want Dynatrace Intelligence generative AI to look up Dynatrace sources like Documentation, Community and Developer Portal to enrich its answers. If **Document retrieval** is set to `Disabled`, generative AI will rely on its foundational model to execute your prompt.
7. Optional Add any additional workflow action before or after Dynatrace Intelligence generative AI action to support your use case.
8. Select  **Save**.
9. Next, select  **Run** to execute the workflow.

To learn about specific use cases and how you can use the Dynatrace Intelligence generative AI workflow action, see [Summarize open problems with Dynatrace Intelligence (Preview)](/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples "Use Dynatrace Intelligence (Preview) to summarize open problems and suggest remediation steps.").

## Related topics

* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.")
* [Summarize open problems with Workflows](/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples "Use Dynatrace Intelligence (Preview) to summarize open problems and suggest remediation steps.")
* [Agentic workflows](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/agentic-workflows "Basic concepts of using agentic workflows to automate complex, data-driven tasks more flexibly by leveraging generative and agentic AI.")


---


## Source: davis-for-notebooks.md


---
title: Dynatrace Intelligence for Notebooks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/davis-for-notebooks
scraped: 2026-02-18T05:57:39.707512
---

# Dynatrace Intelligence for Notebooks

# Dynatrace Intelligence for Notebooks

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence for Notebooks runs a range of analyzers directly in Notebooks, providing on-spot results and enabling you to fine-tune your custom alert configurations.

## Anomaly Detection

With ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** combined with the power of [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."), you can custom-build powerful configurations to detect anomalies in metrics, logs, business data, or a combination of them. To preview and fine-tune your Anomaly Detection configuration before deploying it to action, use a Dynatrace Intelligence for Notebooks analysis option:

* [Auto-adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration.")âDynatrace calculates the threshold automatically and adapts it dynamically to your data's behavior.
* [Seasonal baseline](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "How Dynatrace Intelligence suggests seasonal baseline thresholds for a scope of entities.")âDynatrace creates a confidence band for data with seasonal patterns
* [Static threshold](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "When to use a static threshold for your anomaly detection.")âthe threshold that doesn't change over time.

For each of these options, you can configure a [missing data alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "How to set up an alert for missing measurements."). Missing data and threshold conditions are combined by the **OR** logic.

To run an anomaly detection analysis in Notebooks

1. Go to **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Open your notebook or create a new one.
3. Add a **Query Grail** section and [query](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") the data you're interested in, or add a **Metrics** section and select the required metric.

   For a DQL query, use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
4. Select **Options**.
5. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
6. Select the required anomaly detection analyzer and configure its parameters.
7. Select **Run analysis**.

Dynatrace Intelligence analyses the data and shows potential alerts. Note that these are just indicative simulationsâno real alerts are triggered based on this analysis.

![An example of anomaly detection on seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-anomaly-detection-1920-dbbd5f3499.png)

## Forecast analysis

Dynatrace Intelligence predictive AI analysis foresees future values of any time series of numeric values based on the accumulated data. To trigger a [forecast analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

1. Go to **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Open your notebook or create a new one.
3. Add a **Query Grail** section and [query](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") the data you're interested in, or add a **Metrics** section and select the required metric.
4. Select **Options**.
5. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
6. Select the **Forecast** analyzer and configure its parameters.
7. Select **Run analysis**.

Dynatrace Intelligence calculates the forecast and shows it, extending your visualization.

![An example of a forecast for seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-prediction-1920-0137a2c619.png)

## Related topics

* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [[Video] Introduction to Anomaly Detection based on DQLï»¿](https://www.youtube.com/watch?v=-GxLlr9oGGA)


---
