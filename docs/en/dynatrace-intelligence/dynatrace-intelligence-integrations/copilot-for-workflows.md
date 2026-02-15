---
title: Dynatrace Intelligence (Preview) app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows
scraped: 2026-02-15T09:10:55.233021
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