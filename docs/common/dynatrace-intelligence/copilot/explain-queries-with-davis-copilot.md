---
title: "Summarize and explain queries"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot
updated: 2026-02-09
---

# Summarize and explain queries

# Summarize and explain queries

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

You can use Dynatrace Intelligence generative AI in Dashboards and Notebooks to translate DQL into natural language. Our generative AI can provide a summary as well as a detailed explanation of any existing DQL queries.

## Who this is for

This article is for any users who want to better understand or better DQL queries, or who want to familiarize themselves with DQL.

## What you will learn

In this article, you'll learn how to use Dynatrace Intelligence generative AI to summarize and explain DQL queries.

## Before you begin

Dynatrace Intelligence generative AI explanations are session-based and may vary in structure. This means that explanations donât persist across sessions, so youâll need to regenerate them after a session ends. While Dynatrace Intelligence generative AI often provides line-by-line explanations, it may instead group related lines into meaningful chunks (for example, when multiple lines form a single command or function).

### Prior knowledge

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

### Prerequisites

* Dynatrace SaaS environment.
* You have the `ALLOW davis-copilot:dql2nl:execute;` permission. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* You have completed the Dynatrace Intelligence generative AI setup described in [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

## Explain queries with generative AI in Notebooks

1. Go to [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and open a notebook you can edit.
2. Select a notebook section that contains a query you want to summarize or explain.
3. Open the  menu and select  **Explain query**. A summary followed by a detailed explanation is generated under the query input field.

![An example of Generative AI summary and explanation of a query in Dashboards. ](https://dt-cdn.net/images/dashboards-dynatrace-intelligence-explanation-detail-1049-1976d80ade.png)

## Explain queries with generative AI in Dashboards

1. Go to [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and open a dashboard you can edit.
2. Select a dashboard that contains a DQL query you want to summarize or explain.
3. Select  **Edit** to open the edit menu on the right.
4. In the  **DQL** section of the edit menu, select  **Explain query**. A summary followed by a detailed explanation is generated under  **Run**.

![An example of a Generative AI explanation and summary of a query in Dashboards.](https://dt-cdn.net/images/dashboards-dynatrace-intelligence-explanation-1920-e118fad823.png)

## Give feedback

To help us improve Dynatrace Intelligence generative AI, you can provide feedback directly from your notebook or dashboard. Under the generated explanation box:

* Select ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up") if generative AI has interpreted the query correctly and has generated an adequate explanation that meets your expectations.
* Select ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down") if generative AI has has incorrectly interpreted the DQL query or generated a query explanation that has failed to meet your expectations. Please provide additional context for us to understand how we can improve this functionality to meet your needs and expectations.

Do not share personal or confidential information in your feedback.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
