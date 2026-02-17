---
title: Embedded conversation starters
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters
scraped: 2026-02-17T05:08:23.675955
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