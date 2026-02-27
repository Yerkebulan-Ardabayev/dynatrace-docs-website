# Документация Dynatrace: dynatrace-intelligence/copilot
Язык: Русский (RU)
Сгенерировано: 2026-02-27
Файлов в разделе: 9
---

## dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters.md

---
title: Embedded conversation starters
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters
scraped: 2026-02-26T21:25:20.347027
---

# Embedded conversation starters

# Embedded conversation starters

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jan 30, 2026

Dynatrace applications like ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, ![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**, ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases**, and ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** allow you to trigger a predefined, contextual Dynatrace Assist prompt to increase your productivity and conversation efficiency.

## Prerequisites

To access the application integrations, ensure the following:

* Dynatrace Intelligence generative AI has been enabled on the environment level. For details, see [Enable Dynatrace Intelligence generative AI on your environment](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Learn how to set up Dynatrace Intelligence generative AI.").
* You have permissions to access the conversational recommender skill. For details, see [User permissions](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Learn how to set up Dynatrace Intelligence generative AI.").

## Dynatrace Assist in Kubernetes

You can quickly get an explanation of any warning signals with Generative AI in Kubernetes, powered by  **Dynatrace Assist**. This allows you to get insights into the event details, typical root causes, and common remediation steps without accessing the documentation or other Dynatrace-related sources directly.

To access this functionality:

1. Navigate to any list page in the Kubernetes app (such as Clusters, Nodes, Namespaces, or Workloads).
2. Select any warning signal, and then select **Explain warning signal**.
3. **Dynatrace Assist** will open and auto-execute the predefined prompt.
4. Generative AI will provide a response that details:

   * A general explanation about the event.
   * Typical root causes for the event, starting with the most common ones.
   * Common remediation steps for each of the root causes.

## Dynatrace Assist in Vulnerabilities

Dynatrace Intelligence generative AI provides explanations of vulnerabilities to support understanding and remediation.

To access the functionality

1. In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), select a vulnerability.
2. In the upper-right corner of the vulnerability details pane, select  **Explain vulnerability**.

Generative AI will provide a response that details:

* A description of the vulnerability and its underlying cause
* The potential impact and conditions under which it may be exploited
* The affected libraries, services, or code locations
* Relevant entry points or execution paths
* Recommended remediation actions, such as library upgrades or configuration changes

The structure and level of detail vary depending on the vulnerability type and the available context. Explanations are tailored to the characteristics of each vulnerability to support assessment and remediation.

## Dynatrace Assist in Threats & Exploits

Dynatrace Intelligence generative AI can provide contextual, plain-language explanations of detection findings to accelerate understanding and response.

To access the functionality

1. In [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts."), select a finding.
2. In the upper-right corner of the finding details pane, select  **Explain finding**.

Generative AI will provide a response that details:

* A description of the threat or exploit and its underlying conditions
* The potential impact and likelihood of exploitation
* The affected entities and relevant attack paths
* Indicators that contribute to the threat assessment
* Recommended actions to reduce exposure or validate the finding

The structure and level of detail vary depending on the threat type, available context, and the nature of the exploit. Explanations are tailored to the characteristics of each insight to support evaluation and response.

## Dynatrace Assist in Security Posture Management

Dynatrace Intelligence generative AI provides explanations of configuration assessments to support understanding of compliance findings and misconfigurations.

To access the functionality

1. In [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings."), on the **Assessment results** page, select a rule.
2. On the **Assessed resources** tab, select  **Explain assessment**.

Generative AI will provide a response that details:

* The intent and requirements of the configuration rule
* The specific configuration values that caused the assessment to fail
* The potential security or operational risks associated with the misconfiguration
* The affected resources
* Recommended remediation steps or configuration adjustments

The structure and level of detail vary depending on the rule type, the available configuration data, and whether the assessment is automated or manual. Explanations are tailored to the characteristics of each rule to support evaluation and remediation.

## Dynatrace Assist in Databases

In **Databases** ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases"), Dynatrace Intelligence generative AI can provide natural language explanations of execution plans, breakdowns of relevant details, and recommendations on how to improve statement performance.

Query execution plans provide detailed information on how a database will execute an SQL query. While these provide the raw data on how to improve query performance and reduce resource consumption, they require expert knowledge to read and interpret. With the Generative AI integration, non-expert database users, such as developers, gain the knowledge they need to optimize their application performance and database utilization.

To summarize an execution plan with Generative AI:

1. In **Databases** ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases"), go to **Explorer**.
2. In the rightmost column, select the  statement performance icon.
3. Expand the statement you would like to improve. If an execution plan is not already available, you can request one.
4. Select the **Execution plan** tab, and select  **Summarize execution plan**.
5. **Dynatrace Assist** will open and auto-execute the predefined prompt.
6. Generative AI will provide a response with insight on the selected database execution plan.

## Dynatrace Assist in Problems

In **Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new"), Dynatrace Intelligence generative AI can provide clear summaries of problems, their root causes, and the suggested remediation steps. Generative AI explains individual issues in clear language from the problem details page and can perform a comparative analysis when multiple problems are selected from the list view. This helps you identify common root causes and propose corrective steps without relying on a team of experts or waiting for critical insights.

To explain a single problem with Generative AI

1. Navigate to any problem detail page.
2. Select  **Explain** in the upper-right corner of the page.
3. **Dynatrace Assist** will open and auto-execute the predefined prompt.
4. Generative AI will provide a response that details:

   * An explanation of what happened.
   * Why the problem occurred.
   * Actionable steps to remediate the problem.

To explain multiple problems with Generative AI

1. Navigate to the problem list page.
2. Select up to 5 problems.
3. Select  **Explain** above the table.
4. **Dynatrace Assist** will open and auto-execute the predefined prompt.
5. Generative AI will provide a response that details:

   * An explanation of each problem and why it occurred
   * Actionable steps to remediate the problem
   * Any relationship between the problems

## Dynatrace Assist in Dashboards



You can use the power of DQL to integrate  **Dynatrace Assist** into your [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") tiles.

By adding `| fieldsAdd prompt` and `| fieldsAdd execute` commands, you can predefine and auto-execute prompts in  **Dynatrace Assist**, allowing you to quickly get an explanation about the query results, or receive suggestions on how to improve the query or resolve a problem.

You can also provide additional information to  **Dynatrace Assist** via the supplementary context by adding the following:

```
| parse "{\"result\":[{\"type\":\"supplementary\", \"value\":\"The character`*` often represents sensitive data that has been masked\"}]}", "LD JSON_ARRAY:contexts"



// or for a dynamic context
```

While the supplementary context is hidden in the chat UI, it can help Generative AI provide better answers for your use case. For example, you can ask  **Dynatrace Assist** to use information from a certain field when answering your prompt:

```
| fieldsAdd supplementaryContext = concat("{\"result\":[{\"type\":\"supplementary\", \"value\":\"Use the following info to answer the question: ", record.summary, "\"}]}")



| parse supplementaryContext , "LD JSON_ARRAY:contexts"
```

To integrate  **Dynatrace Assist** into your [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") tiles

1. Go to [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and open a dashboard you can edit.
2. Select a dashboard tile that contains a DQL query.
3. Select  **Edit** to open the edit menu on the right.
4. In the  **DQL** section of the edit menu, add the following to your standard query:

   ```
   | fieldsAdd prompt = concat("{your question}",  your.field.name)



   | fieldsAdd execute = true
   ```

   * If you want to predefine the prompt without automatically executing it, remove `| fieldsAdd execute = true`.
   * This integration doesn't work for queries with the `makeTimeseries` command.

To open the integrated  **Dynatrace Assist**

1. Select the  next to your chosen field entry.
2. Select **Open withâ¦** >  **Ask a question**.

If you've added `| fieldsAdd execute = true` to your query, the predefined prompt will be executed once you open  **Dynatrace Assist**. Otherwise, you'll be able to change or edit the prompt in the message window before manually executing it.

## Dynatrace Assist in Notebooks

You can use the power of DQL to integrate  **Dynatrace Assist** into your [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

By adding `| fieldsAdd prompt` and `| fieldsAdd execute` commands, you can predefine and auto-execute prompts in  **Dynatrace Assist**, allowing you to quickly get an explanation about the query results, or receive suggestions on how to improve the query or resolve a problem.

You can also provide additional information to  **Dynatrace Assist** via the supplementary context by adding the following:

```
| parse "{\"result\":[{\"type\":\"supplementary\", \"value\":\"The character`*` often represents sensitive data that has been masked\"}]}", "LD JSON_ARRAY:contexts"



// or for a dynamic context
```

While the supplementary context is hidden in the chat UI, it can help Generative AI provide better answers for your use case. For example, you can ask  **Dynatrace Assist** to use information from a certain field when answering your prompt:

```
| fieldsAdd supplementaryContext = concat("{\"result\":[{\"type\":\"supplementary\", \"value\":\"Use the following info to answer the question: ", record.summary, "\"}]}")



| parse supplementaryContext , "LD JSON_ARRAY:contexts"
```

To integrate  **Dynatrace Assist** into your [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

1. Go to [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and open a notebook you can edit.
2. Select a notebook section that contains a DQL query.
3. Select the query field and add the following to your standard query:

   ```
   | fieldsAdd prompt = concat("{your question}",  your.field.name)



   | fieldsAdd execute = true
   ```

   * If you want to predefine the prompt without automatically executing it, remove `| fieldsAdd execute = true`.
   * This integration doesn't work for queries with the `makeTimeseries` command.

To open the integrated  **Dynatrace Assist**

1. Select the  next to your chosen field entry.
2. Select **Open withâ¦** >  **Ask a question**.

If you've added `| fieldsAdd execute = true` to your query, the predefined prompt will be executed once you open  **Dynatrace Assist**. Otherwise, you'll be able to change or edit the prompt in the message window before manually executing it.

## Feedback

If you have any feedback, you can provide it directly in the chat window. For more information, see [Give feedback](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot#feedback "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.").

## Related topics

* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")

---

## dynatrace-intelligence/copilot/chat-with-davis-copilot.md

---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-02-27T21:24:10.532873
---

# Dynatrace Assist

# Dynatrace Assist

* Latest Dynatrace
* App
* 2-min read
* Updated on Feb 11, 2026

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

To use  **Dynatrace Assist** with generative AI features, you only need the following permissions:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

You require the remaining permissions in the table only if you want to use the full extent of agentic Dynatrace Assist capabilities. For more information, see [Dynatrace Assist agentic permissions](#assist-agentic-permissions).

For more information, see [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

## Get started

![Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Ask Dynatrace Assist to summarize all open problems to get a quick overview of your environment.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Ask Dynatrace Assist to explain your logs to quickly get the insights, potential impact, likely causes and recommended next steps.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Get help with identifying and fixing vulnerabilities, such as SQL injections.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 of 4Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.

### Use Dynatrace Assist conversational interface

After enabling Dynatrace Intelligence generative AI on your environment and setting the user permissions, you should see a new icon  below the **Search**  in the dock.

1. In Dynatrace, select  **Dynatrace Assist**.
2. A new window opens with the chat interface.
3. Type your question. See [examples](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Learn what kind of prompts work well in Dynatrace Assist.") for inspiration.
4. Select **Run** ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") and wait for the response to be generated.

   * You can ask follow-up questions.
   * Every response contains a list of sources that were retrieved to generate the answer. You can consult these [sources](#sources) for further information.
   * Conversations are saved automatically. These can be renamed or deleted from the overview list of conversations.
   * You can cancel the response generation, refine your prompt, and then re-send the question.
   * You can use the chat interface on top of any application.

Answers are generated based on Dynatrace-related resources. If the model is unable to respond to your question, you'll see an error message:

* I'm sorry, but I can't respond to this request. Please try rephrasing it or adding additional context.

### Use agentic Dynatrace Assist

**Dynatrace Assist** allows you to use Dynatrace agentic AI and [MCP tools and capabilities](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Learn about the Dynatrace MCP server and how you can connect to it.") to access and analyze your environment data and use it to perform tasks (such as listing problems or generating and executing DQL queries) in addition to answering general questions about Dynatrace.

Agentic  **Dynatrace Assist** shares some additional information, such as tool call results, with enterprise vendors hosting the LLMs that Dynatrace agentic and generative AI are based on. For more information about third parties, see [Is my data used to train Dynatrace Intelligence generative AI?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Learn about frequently asked questions and find your answers.").

With agentic AI enabled, you can ask  **Dynatrace Assist** to analyze and provide insights on the data and security of your environment. For examples, see [Ask about the data in your environment](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts#assist-ask-about-the-data "Learn what kind of prompts work well in Dynatrace Assist.").

#### **Dynatrace Assist** agentic permissions

**Dynatrace Assist** respects your user permissions. This means that all agentic  **Dynatrace Assist** calls are done within the scope of your user permissions and the results won't include anything outside of it.

To use the agentic  **Dynatrace Assist**, you need to

* Have sufficient permissions.
* Have agentic AI enabled for  **Dynatrace Assist**. To enable agentic AI

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
  2. Ensure that **Enable generative AI** is turned on.
  3. Turn on **Enable agentic AI**.

Agentic  **Dynatrace Assist** might not be available for you if you don't meet the prerequisites mentioned above or if you access  **Dynatrace Assist** from the [Embedded conversation starters](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Learn how to trigger predefined prompts in various Dynatrace applications.").

You will also need additional permissions for calling the agentic AI tools. For the list of tools and permissions they require, see [MCP tools](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Learn about the Dynatrace MCP server and how you can connect to it.").

#### PII masking

Agentic  **Dynatrace Assist** doesn't provide any PII masking. In order to protect your data, when  **Dynatrace Assist** detects PII in the user prompt, the request is automatically blocked and the prompt isn't sent to the LLM for processing.

#### Calling multiple tools

While interacting with  **Dynatrace Assist** in agentic mode, **Assist** can call up to 10 internal MCP tools per response. If your request requires  **Dynatrace Assist** to call more than 10 tools simultaneously, it'll be unable to complete the interaction.

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
* Learn how to trigger predefined prompts in various Dynatrace applications.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)[02Dynatrace Assist prompt examples

* Reference
* Learn what kind of prompts work well in Dynatrace Assist.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts)

## Use cases

You can use agentic  **Dynatrace Assist** to:

* Ask general questions about the Dynatrace product.
* Make use of the MCP tools and capabilities.
* Perform tasks without the need to open the app or drill-down to another app.
* Combine tools in one request to perform multiple tasks.
* Combine tools to perform tasks and get answers to general questions at the same time.

## Related topics

* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Встроенные стартовые разговоры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace. ")
* [Часто задаваемые вопросы о Dynatrace Intelligence генеративном ИИ](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")
* [Сервер Dynatrace MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp "Узнайте о сервере Dynatrace MCP и о том, как вы можете подключиться к нему.")

---

## dynatrace-intelligence/copilot/copilot-data-privacy.md

---
title: Dynatrace Intelligence generative AI data privacy and security
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-data-privacy
scraped: 2026-02-27T21:24:45.771102
---

# Dynatrace Intelligence generative AI data privacy and security

# Dynatrace Intelligence generative AI data privacy and security

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Jan 28, 2026

At Dynatrace, we take our responsibility to safeguard your data seriously. Understand how Dynatrace Intelligence generative AI uses your data and understand your responsibility to keep your data secure.

## Prompt data

Although we mask Personally Identifiable Information (PII), we still recommend exercising caution when including personal or confidential information in your prompts.

Your prompts are sent to LLMs hosted by enterprise vendors such as Microsoft Azure AI and AWS Bedrock, which power Dynatrace Intelligence generative AI. Enterprise vendors don't store the data you submit or the responses you receive. The prompts you submit and the responses you receive are used only to serve your experience. Enterprise vendors also don't use the prompts to fine-tune or improve any models or services, or to train models across customers or environments.

Each data request is sent to the LLM individually, over an SSL-encrypted service, processed by respective enterprise vendors, and sent back to Dynatrace. If your environment is located in EMEA, your prompts are processed in an EU region. If your environment is located in NORAM, LATAM, or APAC, your prompts are processed in a US region.

Dynatrace may store the prompts submitted to Dynatrace Intelligence generative AI and the responses provided by the LLMs to understand the use cases, contextualize the feedback on the responses, and identify additional user expectations.

Learn more about the [Dynatrace Intelligence generative AI architecture and data flow](/docs/dynatrace-intelligence/copilot/copilot-overview#copilot-data-flow "Learn about data security and other aspects of Dynatrace Intelligence generative AI.").

## PII masking

Dynatrace version 1.305+

PII masking is in place for user prompts interacting with all standard generative AI functionality. This ensures that sensitive information included in your prompts won't be forwarded to LLMs hosted by enterprise vendors.

Currently masked fields include:

* Email address
* Phone number
* IBAN information
* Credit card number
* IP address
* US bank number
* US social security number
* US ABA routing numbers
* URL query parameters (only parameters with more than two characters are considered)
* Canadian Social Insurance Number (SIN)

In our logs and calls to LLM models, we replace values from the identified patterns above with fake patterns. This means that you'll be able see IBANs in logs, for example, but they'll be made up of random numbers, replacing the original values included in your prompts.

Agentic  **Dynatrace Assist** doesn't provide any PII masking. In order to protect your data, when  **Dynatrace Assist** detects PII in the user prompt, the request is automatically blocked and the prompt isn't sent to the LLM for processing.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")

---

## dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides.md

---
title: Discover relevant troubleshooting guides with Dynatrace Intelligence generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides
scraped: 2026-02-27T21:11:38.518947
---

# Discover relevant troubleshooting guides with Dynatrace Intelligence generative AI

# Discover relevant troubleshooting guides with Dynatrace Intelligence generative AI

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI helps you resolve problems faster by automatically surfacing relevant troubleshooting guides, such as notebooks or dashboards created by your team.

To reduce the mean time to repair (MTTR), you can leverage Dynatrace Intelligence generative AI document suggestions in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to check if your team has created any troubleshooting guides for problems similar to the one you've encountered.

## Who this is for

This article is for any users who want to quickly and effectively troubleshoot and remediate active problems in their environment.

## What you will learn

In this article, you'll learn how Dynatrace Intelligence generative AI can suggest relevant troubleshooting guides to assist with problem remediation.

## Before you begin

Dynatrace Intelligence generative AI periodically indexes notebooks and dashboards that have been labeled as troubleshooting guides and shared within the environment.

* By default, semantic vector indexing of the guides occurs every 6 hours.
* In order for Dynatrace Intelligence generative AI to index and suggest your document, you have to share it with all users in your environment. Dynatrace Intelligence generative AI won't index or suggest any private documents or documents shared only with specific users. To learn more about sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

### Prior knowledge

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")

### Prerequisites

* Dynatrace SaaS environment.
* You have completed the Dynatrace Intelligence generative AI setup described in [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").
* You have document suggestions enabled in your environment. Document indexing enablement is a part of the [Enable Dynatrace Intelligence generative AI on your environment](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Learn how to set up Dynatrace Intelligence generative AI.") guide.
* You have the `ALLOW davis-copilot:document-search:execute;` permission. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Get document suggestions to remediate problems

1. Go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and open the problem you need to resolve.
2. On the problem details page, select **Troubleshooting**. You will be able to see any troubleshooting guides you have created for the problem, as well as any relevant documents suggested by Dynatrace Intelligence generative AI.

   Dynatrace Intelligence generative AI only indexes documents that are recognized as troubleshooting guides. Dashboards and notebooks created directly from ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** are automatically recognized as troubleshooting guides and do not require the `[TSG]` prefix.

   If you create a troubleshooting guide directly from ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, you have to prefix the document title with `[TSG]` to indicate it is a troubleshooting guide.

   Regardless of how the document was created, it still has to be shared at the environment level to be indexed by Dynatrace Intelligence generative AI.
3. Optional Provide the keywords or part of a keyword in the **Name**  search field to filter the suggested documents by name.
4. Optional Select the **Type** (`Notebooks`, `Dashboards`) to filter the suggested documents by type. By default, both types are selected for document suggestions.
5. Select **View â¦** on the document you want to view. This action will take you to the troubleshooting guide for further investigation.

## Pin documents directly to a problem

When you create a document from a problem details page, it is automatically pinned to that specific problem. Pinned documents aren't included in the suggested document list. Instead, the TSGs are linked to the problem from which they were created. This ensures that documents created within a problem remain attached and prevents scenarios where the AI might exclude them from the suggested list due to a lack of similarity.

The documents are pinned to problems by setting the `id` field within the document store. The pattern used for problem pinning consists of:

* A string `problem-TSG`.
* A dash `-`.
* A problem ID (`event.id` in the Problem Grail record).
* A dash `-`.
* A random UUID represented by a string.

You can see the general pattern in the example below:

`problem-TSG-{problem_ID}-{random-UUID}`

Since underscore `_` present in a problem ID isn't supported by the document identifier, it needs to be replaced by a dash `-`, as seen in the example below:

`problem-TSG-1589269324049748129-1747888020000V2-225b65bd-ab67-4efe-9d71-742de9b87387`

The random UUID appended to the end of the pattern ensures the uniqueness of each document and allows multiple documents to be pinned to the same problem without conflicts.

Pinning documents to problems allows you to attach additional analysis results and domain-specific knowledge directly to the detected problems. You can pin a document to a problem via workflows or API for seamless external integrations.

### Create and attach a notebook to a detected problem via Workflows

By using a JavaScript workflow action, you can automatically create and attach a document (notebook or dashboard) with your domain-specific analysis results to a detected problem.

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select  to create a new workflow.
2. Select the preferred trigger type.
3. Select  **Add task**.
4. In the **Choose action** section, select **Run JavaScript**.
5. In the **Input** section, enter the following script:

   ```
   import { documentsClient } from "@dynatrace-sdk/client-document";



   import { credentialVaultClient } from '@dynatrace-sdk/client-classic-environment-v2';



   import { execution } from '@dynatrace-sdk/automation-utils';



   function generateGUID() {



   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {



   const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);



   return v.toString(16);



   });



   }



   export default async function ({ execution_id }) {



   const ex = await execution(execution_id);



   const problem_event = ex.params.event;



   var problem_id = problem_event['event.id'];



   problem_id = problem_id.replace('_', '-'); // Replace the unsupported character



   // Create a new Notebook and pin it to the triggering problem



   try {



   const notebookContent = {



   defaultTimeframe: { from: "now()-2h", to: "now()" },



   defaultSegments: [],



   sections: [



   {"id":"19ebed94-69a9-4a6e-b392-7bb7b0deb330","type":"markdown","markdown":"# Domain Analysis Results\n\nHere goes the external, domain-specific analysis results"}



   ],



   };



   const generatedNotebook = await documentsClient.createDocument({



   body: {



   name: "[TSG] Domain Analysis Results",



   type: "notebook",



   description: "A notebook containing domain specific analysis results",



   id: "problem-TSG-" + problem_id + "-" + generateGUID(),



   content: new Blob([JSON.stringify(notebookContent)], { type: "application/json" }),



   },



   });



   // Make the document public



   const updated = await documentsClient.updateDocument({



   id: generatedNotebook.id,



   optimisticLockingVersion: generatedNotebook.version,



   body: {



   isPrivate: false,



   }



   })



   } catch (error) {



   console.error("Error creating notebook:", error);



   }



   return { };



   }
   ```

Once the newly created notebook is attached to the AI-detected problem, you'll be able to see it in the troubleshooting section. The document will also be suggested to you for similar problems in the future.

![An example of analysis results in the Problems app.](https://dt-cdn.net/images/problems-analysis-results-2147-303c6e5b9b.png)

## Related topics

* [Dynatrace Intelligence генеративный ИИ обзор](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Проблемы приложения](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро определить коренную причину инцидентов в вашей среде.")

---

## dynatrace-intelligence/copilot/copilot-getting-started.md

---
title: Get started with Dynatrace Intelligence generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-02-27T21:18:10.252210
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

---

## dynatrace-intelligence/copilot/copilot-overview.md

---
title: Dynatrace Intelligence генеративный ИИ обзор
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-overview
scraped: 2026-02-27T21:23:47.314899
---

# Dynatrace Intelligence генеративный ИИ обзор

# Dynatrace Intelligence генеративный ИИ обзор

* Последнее Dynatrace
* Объяснение
* 5-минутное чтение
* Обновлено 4 февраля 2026 г.

Dynatrace Intelligence генеративный ИИ предназначен для повышения производительности, помощи в настройке и ermögления изучения данных с помощью естественного языка.

## Dynatrace Intelligence генеративный ИИ

Dynatrace Intelligence генеративный ИИ основан на большой языковой модели (LLM). Модель, используемая Dynatrace ИИ, генерирует ответы на основе ваших входных данных и является вероятностной. Это означает, что ответы генерируются путем прогнозирования наиболее вероятного следующего слова или текста на основе данных, с которыми они были созданы, и предоставленного контекста. Dynatrace Intelligence генеративный ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте).

Из-за этого подхода эти модели иногда могут表现аться неточно, неполно или ненадежно. Это означает, что существует риск того, что ответ, который вы получите, не точно отражает введенный вами запрос или что сгенерированный контент звучит разумно, но является неполным или неточным.

Мы рекомендуем вам тщательно оценить ответы, которые вы получаете от Dynatrace Intelligence генеративного ИИ. Если генеративный ИИ отвечает неточно, пожалуйста, предоставьте обратную связь直接 из ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** или  **Dynatrace Assist**.

## Обзор навыков генеративного ИИ

Сервис Dynatrace Intelligence генеративного ИИ предлагает различные и специализированные навыки. В настоящее время генеративный ИИ предлагает четыре навыка:

* NL2DQL: этот навык обеспечивает функциональность быстрого анализа **Prompt**, доступную в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. NL2DQL переводит ваши запросы на естественном языке в DQL запросы. Для получения подробной информации см. [Запрос с помощью естественного языка](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Используйте Dynatrace Intelligence генеративный ИИ для перевода ваших запросов на естественном языке в DQL запросы").
* DQL2NL: этот навык обеспечивает функциональность **Объяснить запрос** в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. DQL2NL предоставляет сводку и объяснение существующих DQL запросов, чтобы помочь вам лучше понять DQL. Для получения подробной информации см. [Сводка и объяснение запросов](/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot "Узнайте, как сводить и объяснять запросы с помощью навыка Dynatrace Intelligence генеративного ИИ DQL2NL").
* Рекомендатель разговора: этот навык обеспечивает  **Dynatrace Assist**, наш глобальный интерфейс разговора. Рекомендатель разговора может отвечать на ваши вопросы о помощи Dynatrace, настройке и использовании. Для получения подробной информации см. [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Задайте вопросы на естественном языке и получите быстрые ответы от Dynatrace Assist, вашего помощника генеративного ИИ.").

  + **Dynatrace Assist** также предлагает контекстно-зависимые разговоры в приложениях, таких как ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, или ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. Контекстно-зависимые разговоры запускают предопределенные, контекстно-зависимые запросы и предоставляют вам контекстное объяснение, шаги по исправлению и сводку. Для получения подробной информации см. [Контекстно-зависимые разговоры Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные запросы в различных приложениях Dynatrace").
* Предложения документов: этот навык обеспечивает функциональность предложения руководства по устранению неполадок в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**. Рекомендация по устранению неполадок улучшает решение проблем, автоматически выделяя релевантные руководства по устранению неполадок, такие как тетради или панели управления, созданные вашей командой. Для получения подробной информации см. [Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence генеративного ИИ](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Узнайте, как Dynatrace Intelligence генеративный ИИ может предложить руководства по устранению неполадок для исправления проблем.").

Поскольку навыки, предлагаемые Dynatrace Intelligence генеративным ИИ, высоко специализированы, быстрый анализ в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** не может ответить на общие вопросы, и  **Dynatrace Assist** может производить неточные DQL запросы.

## Архитектура и поток данных Dynatrace Intelligence генеративного ИИ

Dynatrace Intelligence генеративный ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте). Это означает, что Dynatrace Intelligence генеративный ИИ будет обогащать ваш запрос релевантным дополнительным контентом или контекстом, который отправляется в основную LLM для генерации подходящего ответа. Контент или контекст, используемый для обогащения вашего запроса, зависит от того, какой базовый навык запрашивается.

Данные и дополнительный контекст используются только для обогащения запросов; модель не учится на этом. Данные клиентов не используются для автоматического уточнения, обучения или улучшения моделей или сервисов. Для получения более подробной информации см. [Как генерируются ответы NL2DQL?](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#nl2dql-answers-generation "Используйте Dynatrace Intelligence генеративный ИИ для перевода ваших вопросов на естественном языке в DQL запросы")

## Ограничения использования Dynatrace Intelligence генеративного ИИ

Не существует ограничения на количество взаимодействий, которые вы можете иметь с генеративным ИИ. Однако существует ограничение на пропускную способность. Это означает, что каждый пользователь может задать 25 вопросов в течение 15-минутного интервала.

Существует аналогичное ограничение на количество вопросов, которые могут быть заданы всеми пользователями в вашей среде одновременно. Ваша среда может обрабатывать до 60 вопросов в течение 15-минутного интервала.

Если вы превысили любое из ограничений, вы увидите сообщение об ошибке: "Извините, но я не смог сгенерировать ответ для вас из-за необычно высокого спроса. Пожалуйста, попробуйте еще раз через минуту".

## Часто задаваемые вопросы

Если вы хотите узнать больше о Dynatrace Intelligence генеративном ИИ, посетите нашу [страницу часто задаваемых вопросов](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.").

## Связанные темы

* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")

---

## dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips.md

---
title: Dynatrace Intelligence generative AI - Tips for writing better prompts
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips
scraped: 2026-02-26T21:20:57.526666
---

# Dynatrace Intelligence generative AI - Tips for writing better prompts

# Dynatrace Intelligence generative AI - Tips for writing better prompts

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI is a helpful tool for getting insights from your data without needing to learn DQL. However, as generative AI, it sometimes needs a bit of structure to ensure you get the best results. The following are tips for writing better prompts for quickly analyzing data in Notebooks and Dashboards.

## Tip 1: Make your prompt clear

Natural language is often nuanced and ambiguous, but making your prompt clear should generate better DQL queries:

* Remove and rewrite any words or phrases that aren't clear or could be interpreted in different ways.
* Avoid the use of subjective language like "interesting findings" that is open to interpretation.
* Write in short, simple sentences. You can combine multiple short sentences in a prompt; Dynatrace Intelligence generative AI understands this better than a single long or complex sentence.
* Start your prompt with **"Show me"** instead of phrases such as **"I would like to see"** and **"Tell me about"**.
* Ask yourself if a DQL expert could create a query from your prompt. If not, it probably needs to be clearer.

**Try:**

* Show me the average CPU usage for each host.

**Avoid:**

* CPU usage.
* I want to see an overall summary of the CPU usage for each host over the last week.

## Tip 2: Make your prompt specific

If you know the table where your data is located, specify it. It is especially helpful to be specific about elements such as "events" or "bizevents".

**Try:**

* Show me the number of new trip bizevents for the last day.
* Show me all error logs.

**Avoid:**

* Show me new trips.
* Show me errors.

## Tip 3: Sequence your prompt

When you're writing a complex prompt, it's good practice to make the order of the individual steps clear. Try writing the process in a step-by-step manner.

**Try:**

* First get all logs with errors, then extract the host ID only. Then lookup the CPU usage for the host IDs.

**Avoid:**

* Get the host ID from all logs with errors and lookup CPU usage.

## Tip 4: Try to gradually refine your prompt

If your prompt doesn't seem to work, try refining it to identify where Dynatrace Intelligence generative AI is getting stuck. Start with a simple statement, then gradually add more details.

For example, start with writing only the main part, such as **"Show all logs"**.

Optional If the prompt doesn't give you the intended results, gradually change it until it does. For example, **"Show me the number of logs by status"**.

Once the simpler steps work, add additional steps one by one, for example, **"Show me the number of logs by status as a timeseries"**.

## Tip 5: Use DQL syntax in your prompt

Using keywords from the DQL syntax keywords in your prompts will often generate better DQL queries. Some of the most common keywords are:

* Fetch
* Filter
* Sort
* Summarize
* Lookup

**Try:**

* Fetch all error logs and lookup the host name.

**Avoid:**

* Look at logs with errors and add matching results from the host names.

## Tip 6: Follow the DQL hierarchy in your prompt

We recommend that you get familiar with the [DQL documentation](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). The more you can reflect the DQL syntax hierarchy in your prompt, including command order, the more effective your prompts will be. For example:

* Mention filters at the beginning of your prompt
* Mention sort orders at the end of your prompt

## Known limitations

We are actively working on improving and extending the Dynatrace Intelligence generative AI abilities. You might run into issues with some of the use cases that are still in progress, for example:

* Requesting a specific visualization in your prompt. Prompts like **"Show me logs by status as pie chart"** aren't supported yet and will not work.
* Running forecasts with Dynatrace Intelligence data analyzers. Prompts like **"Forecast whenâ¦"** aren't supported yet and will not work. However, you can provide Dynatrace Intelligence generative AI with a prompt starting with **"Show meâ¦"**, and then enable a Dynatrace Intelligence data analyzer on this section or tile.
* Specifying management zones via the prompt.

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence generative AI.")

---

## dynatrace-intelligence/copilot/quick-analysis-copilot-dql.md

---
title: Query with natural language
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql
scraped: 2026-02-27T21:22:51.128281
---

# Query with natural language

# Query with natural language

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

You can use Dynatrace Intelligence generative AI in Dashboards and Notebooks to explore your data through natural language. It allows you to translate your conversational prompts directly into DQL queries that reflect the context of your environment. You can choose to auto-execute generated queries or generate DQL only.

## Prerequisites

This page assumes that you have completed the setup described in [Getting started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.").

## Use generative AI in Notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open or create a notebook you can edit.
2. Open the  **Add** menu and select  **Prompt**. A new Generative AI notebook section is created with an empty prompt box.
3. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
4. Optional If your prompt doesn't specify the timeframe, you can still specify it in your section header. The default is **Last 2 hours**.
5. Select **Run**. Generative AI creates and runs the query for you.

   Optional If you want to see the generated query before running it, open the  menu next to the **Run** button and select **Generate DQL only**.
6. Review the results.

   * You can review the query by expanding **DQL**  on the right.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the section header and select **Create DQL section** to create a DQL section from this query.
   * You can edit your original prompt, regenerate the query, and run it to update the results.  
     If you select **Rerun sections**, the Notebooks app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
7. Optional Select the  **Options** in the section header to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

## Use generative AI in Dashboards

1. Go to [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and open or create a dashboard you can edit.
2. Open the  **Add** menu and select  **Prompt**.

   * A new Dynatrace Intelligence generative AI dashboard tile is created
   * A panel on the right displays:

     + An empty tile title field you can customize
     + A prompt box followed by some examples you can select to try
     + A **Run** button
3. Optional At the top of the prompt definition panel, enter a tile title.
4. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
5. Optional If your prompt doesn't specify a timeframe, you can still specify it for the dashboard in your dashboard header (default is **Last 2 hours**) or the **Custom timeframe** settings (for a tile-specific timeframe).
6. Select **Run**. Generative AI creates and runs the query for you.
7. Review the results.

   * To review the query, expand **DQL**  under the prompt box.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the tile header and select **Create DQL tile** to create a DQL tile from this query.
   * You can edit your original prompt and run it to update the query and results.  
     If you refresh your dashboard, the Dashboards app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
8. Optional Select the **Visual** tab to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

Even though Dynatrace Intelligence generative AI is not charged for, all queries that are executed by generative AI are subject to licensing consumption according to your existing licensing agreement.

## Environment-aware queries

Environment-aware queries enrich Dynatrace Intelligence generative AI with your environment data. This lets you generate more accurate queries that identify and reference relevant entities, events, spans, logs, and metrics from your environment. You can also run more complex data analyses by asking Dynatrace Intelligence generative AI about the specifics of your data. To learn more about how to control and manage which data Dynatrace Intelligence generative AI has access to and how to enable environment-aware queries, see [Enable environment-aware queries](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-environment-aware-queries "Learn how to set up Dynatrace Intelligence generative AI.").

### Dynatrace Intelligence generative AI semantic index

Once enabled, Dynatrace Intelligence generative AI periodically scans your Grail data to create its own semantic index. Certain data fragments are sent to Microsoft Azure OpenAI during the semantic indexing. Examples of such data fragments include metric keys, dimensions, and field names. When a user provides a prompt, Dynatrace Intelligence generative AI first identifies the most relevant fragments from the data it has indexed. OUr generative AI then sends the user prompt, the relevant data fragments, and some examples of field values observed in your environment to Microsoft Azure OpenAI for processing.

Having environment-aware queries enabled allows Dynatrace Intelligence generative AI to identify unique data fields and custom metrics in your environment and helps you do your analysis by combining your prompt with the relevant, unique data fields and types.

Let's assume you're tracking travel bookings for new trips. In this case, you'd want to track:

* profit made on each booking as a bizevent
* applicable discounts as a bizevent
* length of time it takes customers to complete a booking as a custom metric

With this in mind, you could give Dynatrace Intelligence generative AI the following command: **"Show me the average money made and the price reduction for new trips, over the last month"**.

If you have environment-aware queries enabled, the following DQL will be generated, providing you with results relevant to your environment:

```
fetch bizevents , from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {profit= avg(profit), discount= avg(discount)}
```

Dynatrace Intelligence generative AI is capable of inferring that "money made" refers to the profit field, and that "price reduction" refers to the discount field, even if your prompt didn't use the correct field names.

If you don't have environment-aware queries enabled, Dynatrace Intelligence generative AI will try to refer to the fields by the names you provided. The following, incorrect DQL would be generated since the fields don't exist in your environment:

```
fetch bizevents, from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {avg_money_made = avg(money_made), avg_price_reduction = avg(price_reduction)}
```

Alternatively, you could ask Dynatrace Intelligence generative AI the following question: **"On average, how long does it take customers to book new trips?"**

If you have environment-aware queries enabled, the following DQL will be generated, providing you with results relevant to your environment:

```
timeseries avg(new_trip_booking_duration)
```

If you don't have environment-aware queries enabled, you'll likely get an error message since Dynatrace Intelligence generative AI would be unable to correctly map your question to your custom metric key. In this case, our generative AI can't provide a valid DQL query because it can't find a matching generic, built-in metric.

### User-based data access

Since Dynatrace Intelligence generative AI respects user privileges, it may provide different responses to different users based on their access rights.

## How are NL2DQL responses generated?



![Dynatrace Intelligence generative AI diagram explaining how NL2QL responses are generated](https://dt-cdn.net/images/davis-copilot-nl2dql-responses-1920-1a15aa1055.png)

Dynatrace Intelligence generative AI NL2DQL response process can be summarized in 4 steps.

1. Dynatrace Intelligence generative AI receives a request from a user.
2. If the request is well-formulated and recognized (see [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.") for more information), Dynatrace Intelligence generative AI matches the user request with the Dynatrace-owned content, such as documentation and curated query examples, and passes the prompt to LLM.

   If you have enabled environment-aware queries, the relevant data fragments will be used enrich the prompt alongside Dynatrace-owned content.
3. The LLM generates a response and checks if the DQL is valid.
4. The response is returned to the relevant app, Notebooks or Dashboards, and the output is displayed to the user.

## Give feedback

To help us improve Dynatrace Intelligence generative AI, you can provide feedback directly from your notebook or dashboard. Under the prompt box:

* Select ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up") if Dynatrace Intelligence generative AI has interpreted your prompt correctly and has generated and run a DQL query that meets your expectations.
* Select ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down") if Dynatrace Intelligence generative AI has generated and run a DQL query that has failed to meet your expectations or has incorrectly interpreted your prompt. Please provide additional context for us to understand how we can improve this functionality to meet your needs and expectations.

Do not share personal or confidential information in your feedback.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence generative AI.")

---

## dynatrace-intelligence/copilot.md

---
title: Dynatrace Интеллект агентного и генеративного ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot
scraped: 2026-02-27T21:12:07.760766
---

# Dynatrace Интеллект агентного и генеративного ИИ

# Dynatrace Интеллект агентного и генеративного ИИ

* Последнее Dynatrace
* Приложение
* 2-минутное чтение
* Обновлено 28 января 2026 г.

Dynatrace Интеллект генеративный ИИ, разработанный Dynatrace, позволяет исследовать данные с помощью естественного языка, помогая в обучении и повышении производительности. Dynatrace Интеллект генеративный ИИ принимает ваш запрос и переводит его в DQL, и способен автоматически выполнять сгенерированные запросы DQL.

## Случаи использования

* Быстрее ознакомиться с DQL, переводя запросы на естественном языке в готовые к использованию запросы.
* Сэкономить время, генерируя и выполняя сгенерированные запросы DQL вместо написания их вручную.
* Получить ответы на вопросы о помощи и обучении быстро, без необходимости доступа к документации или другим ресурсам поддержки Dynatrace.
* Лучше понять существующие DQL, получая краткие описания и объяснения запросов.
* Попросите Dynatrace Assist предоставить контекстные сведения:

  + Получите четкие описания проблем, их коренных причин и предложенных шагов по исправлению в приложении Problems.
  + Получите объяснения сигналов предупреждения в приложении Kubernetes.
  + Получите объяснения планов выполнения в приложении Databases на естественном языке.
* Откройте для себя релевантные руководства по устранению неполадок, чтобы ускорить процесс исправления проблем.

[#### Обзор Dynatrace Интеллекта генеративного ИИ

Узнайте о безопасности данных и других аспектах Dynatrace Интеллекта генеративного ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-overview)[#### Начало работы с Dynatrace Интеллектом генеративным ИИ

Узнайте, как настроить Dynatrace Интеллект генеративный ИИ.

* Руководство по началу работы

Прочитайте это руководство](/docs/dynatrace-intelligence/copilot/copilot-getting-started)

## Анализ данных с помощью генеративного ИИ

[#### Запрос с помощью естественного языка

Используйте Dynatrace Интеллект генеративный ИИ, чтобы перевести ваши вопросы на естественном языке в запросы DQL

* Обзор

Посмотрите обзор](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql)[#### Dynatrace Интеллект генеративный ИИ - Советы по написанию лучших запросов

Узнайте лучшие практики для написания более точных запросов.

* Справочник

Прочитайте этот справочник](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips)[#### Примеры быстрого анализа с помощью генеративного ИИ

Узнайте больше о том, какие запросы хорошо работают в Dynatrace Интеллекте генеративном ИИ.

* Справочник

Прочитайте этот справочник](/docs/dynatrace-intelligence/use-cases/copilot-examples)[#### Суммировать и объяснить запросы

Узнайте, как суммировать и объяснять запросы с помощью Dynatrace Интеллекта генеративного ИИ DQL2NL.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot)

## Спросите Dynatrace Assist

[#### Dynatrace Assist

Задайте вопросы с помощью естественного языка и получите быстрые ответы от Dynatrace Assist, вашего генеративного ИИ-помощника.

* Приложение

Изучите это приложение](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot)[#### Встроенные стартовые разговоры

Узнайте, как запустить предопределенные запросы в различных приложениях Dynatrace.

* Справочник

Прочитайте этот справочник](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)

Для получения более подробной информации о том, какие запросы хорошо работают в **Dynatrace Assist**, см. [примеры запросов](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие запросы хорошо работают в Dynatrace Assist.").

## Векторное совпадение документов

[#### Откройте для себя релевантные руководства по устранению неполадок с помощью Dynatrace Интеллекта генеративного ИИ

Узнайте, как Dynatrace Интеллект генеративный ИИ может предложить руководства по устранению неполадок для исправления проблем.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides)

## Узнайте больше

[#### Dynatrace Интеллект генеративный ИИ: политика безопасности и конфиденциальности данных

Узнайте о политике безопасности и конфиденциальности данных Dynatrace Интеллекта генеративного ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-data-privacy)[#### Dynatrace Интеллект генеративный ИИ: часто задаваемые вопросы

Узнайте о часто задаваемых вопросах и найдите ответы.

* Руководство по устранению неполадок

Прочитайте это руководство](/docs/dynatrace-intelligence/copilot/copilot-faq)

---
