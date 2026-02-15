---
title: Summarize open problems with Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples
scraped: 2026-02-15T09:12:14.836078
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