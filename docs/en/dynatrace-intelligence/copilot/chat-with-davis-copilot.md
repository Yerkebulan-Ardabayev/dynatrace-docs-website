---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-03-06T21:33:52.070519
---

# Dynatrace Assist


* Latest Dynatrace
* App
* 2-min read
* Updated on Mar 03, 2026

**Dynatrace Assist** allows you to chat with Dynatrace Intelligence and ask questions about the data in your environment, as well as general questions to help you with onboarding to Dynatrace and understanding our core concepts.

### Permissions

The following table describes the required permissions.

document:documents:write

store conversations in document store

document:documents:read

read conversations from document store

document:documents:delete

delete conversations from document store

davis-copilot:conversations:execute

use copilot conversation feature

hub:catalog:read

reading the catalog to display which app triggered a conversation

davis-copilot:nl2dql:execute

use copilot agentic feature

davis-copilot:dql2nl:execute

use copilot agentic feature

mcp-gateway:servers:invoke

use copilot agentic feature

mcp-gateway:servers:read

use copilot agentic feature

davis:analyzers:read

use copilot agentic feature

To use  **Dynatrace Assist** in the generative AI mode, you only need the following permissions:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

You require the remaining permissions in the table only if you want to use the full extent of agentic Dynatrace Assist capabilities. For more information, see [Dynatrace Assist agentic permissions](copilot-getting-started.md#assist-agentic "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

For more information, see Getting started with Dynatrace Intelligence agentic and generative AI.

## Get started

![Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Ask Dynatrace Assist to summarize all open problems to get a quick overview of your environment.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Ask Dynatrace Assist to explain your logs to quickly get the insights, potential impact, likely causes and recommended next steps.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Get help with identifying and fixing vulnerabilities, such as SQL injections.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 of 4Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.

### Use Dynatrace Assist conversational interface

After enabling Dynatrace Intelligence generative AI on your environment and setting the user permissions, you should see a new icon  below the **Search**  in the dock.

1. In Dynatrace, select  **Dynatrace Assist**.
2. A new window opens with the chat interface.
3. Type your question. See examples for inspiration.
4. Select **Run** ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") and wait for the response to be generated.

   * You can ask follow-up questions.
   * Every response contains a list of sources that were retrieved to generate the answer. You can consult these [sources](#sources) for further information.
   * Conversations are saved automatically. These can be renamed or deleted from the overview list of conversations.
   * You can cancel the response generation, refine your prompt, and then re-send the question.
   * You can use the chat interface on top of any application.

Answers are generated based on Dynatrace-related resources. If the model is unable to respond to your question, you'll see an error message:

* I'm sorry, but I can't respond to this request. Please try rephrasing it or adding additional context.

### Use Dynatrace Assist agentic capabilities

With agentic AI enabled, you can ask  **Dynatrace Assist** to analyze and provide insights on the data and security of your environment. For examples, see Ask about the data in your environment.

For more information about getting started with agentic  **Dynatrace Assist**, see [Enable agentic AI for Dynatrace Assist](copilot-getting-started.md#assist-agentic "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

### Give feedback

You can provide feedback using the built-in feedback mechanism.

Select ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up") if Dynatrace Assist has generated a response that has met your expectations and interpreted your prompt correctly.

Select ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down") if Dynatrace Assist has generated a response that has failed to meet your expectations or has incorrectly interpreted your prompt. Please provide additional context for us to understand how we can improve this functionality to meet your needs and expectations.

Your feedback isn't used to automatically train any models. It's reviewed only by the product team to monitor the response quality and improve the core product offering.

### Sources consulted to generate responses

**Dynatrace Assist** enriches its answers based on the official Dynatrace sources, such as:

* Dynatrace Documentation
* [Dynatrace Developerï»¿](https://developer.dynatrace.com/)
* [Dynatrace Communityï»¿](https://community.dynatrace.com/)
* [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/)
* [Dynatrace news and resourcesï»¿](https://www.dynatrace.com/news/product-news/)
* [Dynatrace websiteï»¿](https://www.dynatrace.com/)

## Concepts

Go through the following process to learn using  **Dynatrace Assist**

[01Embedded conversation starters

* Reference
* Learn how to trigger predefined prompts in various Dynatrace applications.](chat-with-davis-copilot/copilot-conv-starters.md)02Dynatrace Assist prompt examples

* Reference
* Learn what kind of prompts work well in Dynatrace Assist.

## Use cases

You can use agentic  **Dynatrace Assist** to:

* Ask general questions about the Dynatrace product.
* Make use of the MCP tools and capabilities.
* Perform tasks without the need to open the app or drill-down to another app.
* Combine tools in one request to perform multiple tasks.
* Combine tools to perform tasks and get answers to general questions at the same time.

## Related topics

* Get started with Dynatrace Intelligence agentic and generative AI
* Embedded conversation starters
* Dynatrace Intelligence agentic and generative AI FAQ
* Dynatrace MCP server