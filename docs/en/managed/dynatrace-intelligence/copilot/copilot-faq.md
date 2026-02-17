---
title: Dynatrace Intelligence generative AI FAQ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-faq
scraped: 2026-02-17T21:30:37.322160
---

# Dynatrace Intelligence generative AI FAQ

# Dynatrace Intelligence generative AI FAQ

* Latest Dynatrace
* Troubleshooting
* 4-min read
* Updated on Jan 28, 2026

If you have any questions related to Dynatrace Intelligence generative AI, start by seeing if they have already been answered in the FAQ.

## Generative AI availability

What are the prerequisites for using Dynatrace Intelligence generative AI?

* Your environment must be SaaS and running the latest Dynatrace.
* You must enable Dynatrace Intelligence generative AI on your environment.
* You must assign permission to the relevant users or user groups.

For details, see [Getting started with generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

Is Dynatrace Intelligence generative AI available on SaaS and Managed?

Dynatrace Intelligence generative AI will be available for all Dynatrace SaaS customers using the latest Dynatrace. Both AWS and Azure accounts are supported.

Dynatrace Intelligence generative AI is not available for Dynatrace Managed customers.

Does my account need to be on DPS to use Dynatrace Intelligence generative AI?

No. Dynatrace Intelligence generative AI is available on any SaaS environment running the latest Dynatrace, irrespective of your licensing model.

Will Dynatrace Intelligence generative AI be licensed?

No. There is no licensing associated with our current generative AI functionality. However, even though Dynatrace Intelligence generative AI is not charged for, all queries that are executed by generative AI are subject to licensing consumption according to your existing licensing agreement. If you are concerned about the cost of auto-executing generated queries, you can choose to generate DQL only, without executing it. For more information, see [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

How will Dynatrace Intelligence generative AI impact my license consumption?

Dynatrace Intelligence generative AI itself has no impact on your license consumption. However, all queries that are executed by the generative AI are subject to license consumption according to your existing license agreement. For more information, see [Will Dynatrace Intelligence generative AI be licensed?](/docs/dynatrace-intelligence/copilot/copilot-faq#davis-copilot-license "Learn about frequently asked questions and find your answers.").

## Dynatrace Intelligence generative AI and customer data

Is my data used to train Dynatrace Intelligence generative AI?

No. Customer data and customer prompts are not used for training. Dynatrace Intelligence generative AI is based on a [retrieval augmented generation](/docs/dynatrace-intelligence/copilot/copilot-overview#copilot-what-to-expect "Learn about data security and other aspects of Dynatrace Intelligence generative AI.") (RAG) approach, which means that data and additional context is used only to enrich prompts. The model does not learn from this. Customer data isn't used to automatically fine-tune, train, or improve any models or services, either by Dynatrace or by enterprise vendors hosting the LLM.

Is my data used to train the Dynatrace Intelligence generative AI model for other customers?

No, customer data is not used to train Dynatrace Intelligence generative AI at all. There is no risk of customer data being shared between environments.

Does Dynatrace Intelligence generative AI collect my data?

For the basic Dynatrace Intelligence generative AI functionality, there is no access to customer data. The generic query generation relies only on public domain knowledge (Semantic Dictionary, DQL documentation, etc.) and an extensive, curated dataset that is managed by Dynatrace. The only customer context that generative AI has access to is the user's prompt.

However, if you enable environment-aware queries, Dynatrace Intelligence generative AI will create a semantic index that is stored in the Dynatrace platform. Creating a semantic index allows generative AI to generate more accurate queries that identify and reference relevant entities, events, and metrics. This lets you run deeper and more complex data analysis by asking about the specifics of the data in your environment. Keep in mind that:

* You have full control over which data in Grail is semantically indexed by Dynatrace Intelligence generative AI on the level of Grail data objects and buckets.
* Even when environment-aware queries are enabled, your data is still stored only within your environment, and the data fragments that are used to enrich your prompts are not used to train or fine-tune the model.

Does Dynatrace Intelligence generative AI respect user permissions?

Yes. Dynatrace Intelligence generative AI respects user privileges, and it may provide different responses to different users based on their access rights.

## Using Generative AI

Where can I use Dynatrace Intelligence generative AI?

The Dynatrace Intelligence generative AI functionality currently allows you to conduct quick data analysis in Notebooks and Dashboards by generating DQL based on your natural language prompts.

How can I provide feedback?

You can provide feedback directly in the Notebooks or Dashboards apps. To learn how to give feedback through Dashboards and Notebooks, see [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

Can Dynatrace Intelligence generative AI handle questions in foreign languages?

Yes. Dynatrace Intelligence generative AI does respond to commands and questions in languages other than English.

How can I track and monitor Dynatrace Intelligence generative AI adoption across my environment?

We have a ready-made self-adoption dashboard available, which provides a comprehensive overview of:

* Active users
* Performance
* Feature adoption
* Interaction success rate
* Prompt details
* Response error details
* Query executions
* User feedback.

You or your administrators can use this dashboard to get a better understanding of which generative AI features are being used, to review user prompts and AI responses, and to get insights into users' satisfaction with the features. The dashboard can be found under the title **Generative AI feature adoption**.

All interactions with Dynatrace Intelligence generative AI are logged in Grail as `dt.system.events` and require relevant permissions to retrieve and view such events.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence generative AI.")
* [Dynatrace Intelligence generative AI data privacy and security](/docs/dynatrace-intelligence/copilot/copilot-data-privacy "Learn about Dynatrace Intelligence generative AI data privacy and security policy.")