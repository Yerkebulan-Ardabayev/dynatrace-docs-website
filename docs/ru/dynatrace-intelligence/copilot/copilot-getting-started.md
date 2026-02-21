---
title: Get started with Dynatrace Intelligence generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-02-21T21:10:52.955546
---

# Get started with Dynatrace Intelligence generative AI

# Get started with Dynatrace Intelligence generative AI

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI is enabled on the account level by default, meaning that all your environments automatically have access to it. However, generative AI functionality must still be enabled on the environment level via the settings page, which offers you full control over how Dynatrace Intelligence generative AI is enabled and configured in your environment.

## Enable Dynatrace Intelligence generative AI on your environment

To enable Dynatrace Intelligence generative AI on your environment

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Turn on **Enable generative AI**.

![Enable generative AI in your settings](https://dt-cdn.net/images/generative-ai-settings-1913-24ab3b085b.png)

If you can't see the settings page, make sure you have `Setting Reader` and `Setting Writer` policies assigned. For more information, see [read and write permission](/docs/manage/identity-access-management/use-cases/access-settings#example-read-and-write-permissions "Grant access to Settings").

## User permissions

After enabling Dynatrace Intelligence generative AI on the environment level, you'll still need to give access to the various generative AI skills to your users. To do so, you have to bind the group they belong to a policy with the following statement that allows access to generative AI:

* **Natural language to DQL translation** (`ALLOW davis-copilot:nl2dql:execute;`)
* **DQL translation to natural language** (`ALLOW davis-copilot:dql2nl:execute;`)
* **Conversational recommender** (`ALLOW davis-copilot:conversations:execute;`)

For more information on managing your policies, see [Manage IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

### User-based data access

Since Dynatrace Intelligence generative AI respects user privileges, it may provide different responses to different users based on their access rights.

## Enable document suggestion

Document suggestion is a Dynatrace Intelligence generative AI skill that allows it to recommend to you troubleshooting guides created in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** based on vector similarity. You can leverage Dynatrace Intelligence generative AI's document suggestion in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to quickly retrieve troubleshooting guides written by you or your team for similar problems and reduce mean time to repair (MTTR).

If you want Dynatrace Intelligence generative AI to suggest troubleshooting guides for similar or repeatedly occurring problem, you'll need to allow it to search through and index documents created in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and shared with all users in your environment. To ensure you have full control over the security of your data, this functionality is opt-in and is turned off by default.

In order for Dynatrace Intelligence generative AI to index and suggest your document, it has to be shared with all users in your environment. Dynatrace Intelligence generative AI won't index or suggest any private documents or documents shared only with specific users. To learn more about sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

To enable document suggestion

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Turn on **Enable document suggestions** to allow Dynatrace Intelligence generative AI to ingest troubleshooting guides and suggest them to you.

By default, Dynatrace Intelligence generative AI indexes troubleshooting guides every 6 hours.

### Semantic vector indexing

Dynatrace Intelligence generative AI uses semantic vector indexing to suggest relevant troubleshooting dashboards and notebooks shared within the environment. It continuously indexes the content of dashboards and notebooks recognized as troubleshooting guides. When a user accesses the troubleshooting view for a specific problem, generative AI compares the problem description to the indexed data using semantic similarity to suggest the most relevant guides.

This process relies on vector representations of both the problem description and the indexed dashboard or notebook content. The smaller the semantic distance between the problem description and a document, the higher its relevance score. This means it's more likely for a document to be suggested by Dynatrace Intelligence generative AI as a relevant troubleshooting guide.

## Enable environment-aware queries

Environment-aware queries can enrich Dynatrace Intelligence generative AI with your environment's data. This lets you generate more accurate queries that identify and reference relevant entities, events, spans, logs, and metrics from your environment.

If you want Dynatrace Intelligence generative AI to be aware of the details and structures of your environment's data, you'll need to allow access to Grail. To ensure you have full control over the security of your data, this functionality is opt-in, and admin users can specify which data tables and buckets Dynatrace Intelligence generative AI is not allowed to access.

To enable environment-aware queries

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Turn on **Enable environment-aware queries**.

It can take up to 24 hours for Dynatrace Intelligence generative AI to build or amend the semantic index after changes are made. If environment-aware queries are disabled and the semantic index already exists, Dynatrace Intelligence generative AI purges all environment-specific data within 24 hours, and returns to using publicly available sources for building DQL queries. The semantic index is stored only on your Dynatrace tenant.

To learn more about semantic indexing and environment-aware queries, see [Environment-aware queries](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#environment-aware-queries "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

### Configure your data access

After enabling environment-aware queries, you'll be able to see the settings for configuring data that Dynatrace Intelligence generative AI isn't allowed to access.

To configure your data access

1. Go to **Configure data access**.
2. Select **Add a new rule**.
3. Select the type of data you want to exclude from Dynatrace Intelligence access in the **Type** field.
4. Type the name of the bucket or table in the **Name** field.
5. Select **Save changes**.

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")