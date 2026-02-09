---
title: "Dynatrace Assist"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
updated: 2026-02-09
---

# Dynatrace Assist

# Dynatrace Assist

* Latest Dynatrace
* App
* 2-min read
* Updated on Jan 28, 2026

**Dynatrace Assist** allows you to chat with Dynatrace Assist and ask general help questions to help you with onboarding to Dynatrace and understanding our core concepts.

### Permissions

The following table describes the required permissions.

Permission

Description

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

.css-b62m3t-container{position:relative;box-sizing:border-box;}

.css-7pg0cj-a11yText{z-index:9999;border:0;clip:rect(1px, 1px, 1px, 1px);height:1px;width:1px;position:absolute;overflow:hidden;padding:0;white-space:nowrap;}

.css-1hac4vs-dummyInput{background:0;border:0;caret-color:transparent;font-size:inherit;grid-area:1/1/2/3;outline:0;padding:0;width:1px;color:transparent;left:-100px;opacity:0;position:relative;-webkit-transform:scale(.01);-moz-transform:scale(.01);-ms-transform:scale(.01);transform:scale(.01);}.css-14oxtc6{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:grid;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-box-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-overflow-scrolling:touch;position:relative;overflow:hidden;box-sizing:border-box;}

.css-w54w9q-singleValue{grid-area:1/1/2/3;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;box-sizing:border-box;}

10

rows per page

Page

.css-b62m3t-container{position:relative;box-sizing:border-box;}

.css-7pg0cj-a11yText{z-index:9999;border:0;clip:rect(1px, 1px, 1px, 1px);height:1px;width:1px;position:absolute;overflow:hidden;padding:0;white-space:nowrap;}

.css-1hac4vs-dummyInput{background:0;border:0;caret-color:transparent;font-size:inherit;grid-area:1/1/2/3;outline:0;padding:0;width:1px;color:transparent;left:-100px;opacity:0;position:relative;-webkit-transform:scale(.01);-moz-transform:scale(.01);-ms-transform:scale(.01);transform:scale(.01);}.css-14oxtc6{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:grid;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-box-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-overflow-scrolling:touch;position:relative;overflow:hidden;box-sizing:border-box;}

.css-w54w9q-singleValue{grid-area:1/1/2/3;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;box-sizing:border-box;}

1

of 1

For more information, see [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

Get started

Content sources

Prompt examples

![Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Ask Dynatrace Assist to summarize all open problems to get a quick overview of your environment.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Ask Dynatrace Assist to explain your logs to quickly get the insights, potential impact, likely causes and recommended next steps.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Get help with identifying and fixing vulnerabilities, such as SQL injections.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 of 4Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.

## Use Dynatrace Assist conversational interface

After enabling Dynatrace Intelligence generative AI on your environment and setting the user permissions, you should see a new icon  below the **Search**  in the dock.

1. In Dynatrace, select  **Dynatrace Assist**.
2. A new window opens with the chat interface.
3. Type your question. See [examples](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot#prompt-examples "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.") for inspiration.
4. Select **Run** ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") and wait for the response to be generated.

   * You can ask follow-up questions.
   * Every response contains a list of sources that were retrieved to generate the answer. You can consult these [sources](#sources) for further information.
   * Conversations are saved automatically. These can be renamed or deleted from the overview list of conversations.
   * You can cancel the response generation, refine your prompt, and then re-send the question.
   * You can use the chat interface on top of any application.

Answers are generated based on Dynatrace-related resources. If the model is unable to respond to your question, you'll see an error message:

* I'm sorry, but I can't respond to this request. Please try rephrasing it or adding additional context.

## Give feedback

You can provide feedback using the built-in feedback mechanism.

Select ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up") if Dynatrace Assist has generated a response that has met your expectations and interpreted your prompt correctly.

Select ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down") if Dynatrace Assist has generated a response that has failed to meet your expectations or has incorrectly interpreted your prompt. Please provide additional context for us to understand how we can improve this functionality to meet your needs and expectations.

## Learning modules

Go through the following process to learn using  **Dynatrace Assist**

[01Embedded conversation starters

* Reference
* Learn how to trigger predefined prompts in various Dynatrace applications.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)

**Dynatrace Assist** enriches its answers based on the official Dynatrace sources, such as Dynatrace Documentation and Dynatrace Community. For details, see below.

## Sources consulted to generate responses

* Dynatrace Documentation
* [Dynatrace Developerï»¿](https://developer.dynatrace.com/)
* [Dynatrace Communityï»¿](https://community.dynatrace.com/)
* [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/)
* [Dynatrace news and resourcesï»¿](https://www.dynatrace.com/news/product-news/)
* [Dynatrace websiteï»¿](https://www.dynatrace.com/)

**Dynatrace Assist** can help answer your questions for a variety of different topics and use cases that relate to Dynatrace specifically, as well as software, observability, and technology in general. See the examples below to understand what kind of questions  **Dynatrace Assist** can help you with.

We recommend that you start a new conversation for a new topic to improve Dynatrace Assist response accuracy.

## Get started with Dynatrace

* How do I get started with sending OpenTelemetry to Dynatrace?
* What are Dynatrace workflows, how do I get started with them, and how will this improve the way I work with Dynatrace?
* Introduce all basic DQL commands and provide examples of each one.

## Understand how Dynatrace works

* What is the difference between an event and a problem in Dynatrace?
* How is the Dynatrace Security Score calculated, and why is this important for my environment?
* What are the reasons why I canât find historical data, and how can I fix this?

## How to configure parts of Dynatrace

* How can I configure an SLO?
* How do I set up an alert?
* How do I set a maintenance window via API?

## Get help with onboarding to Dynatrace App development

* What is the Dynatrace AppEngine and how do I get started with building my own app?
* What are the requirements for using the Dynatrace App Toolkit? What are the tutorial steps for getting started?
* Does Dynatrace have a design system and how can it help me build an app?

## Related topics

* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Embedded conversation starters](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Learn how to trigger predefined prompts in various Dynatrace applications.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
