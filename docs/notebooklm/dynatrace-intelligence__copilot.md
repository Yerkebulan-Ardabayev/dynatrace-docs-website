# Документация Dynatrace: dynatrace-intelligence/copilot
Язык: Русский (RU)
Сгенерировано: 2026-03-02
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
scraped: 2026-03-02T21:33:22.887033
---

# Dynatrace Assist

# Dynatrace Assist

* Последнее Dynatrace
* Приложение
* 2-минутное чтение
* Обновлено 11 февраля 2026 г.

**Dynatrace Assist** позволяет вам общаться с Dynatrace Intelligence и задавать вопросы о данных в вашей среде, а также общие вопросы, чтобы помочь вам с настройкой Dynatrace и пониманием наших основных концепций.

### Разрешения

В следующей таблице описаны необходимые разрешения.

document:documents:write

хранить разговоры в хранилище документов

document:documents:read

читать разговоры из хранилища документов

document:documents:delete

удалять разговоры из хранилища документов

davis-copilot:conversations:execute

использовать функцию разговора с пилотом

hub:catalog:read

чтение каталога для отображения приложения, которое запустило разговор

davis-copilot:nl2dql:execute

использовать функцию агента пилота

davis-copilot:dql2nl:execute

использовать функцию агента пилота

mcp-gateway:servers:invoke

использовать функцию агента пилота

mcp-gateway:servers:read

использовать функцию агента пилота

davis:analyzers:read

использовать функцию агента пилота

Чтобы использовать **Dynatrace Assist** с функциями генеративного ИИ, вам необходимы только следующие разрешения:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

Остальные разрешения в таблице необходимы только в том случае, если вы хотите использовать все возможности агентного Dynatrace Assist. Для получения дополнительной информации см. [Разрешения агентного Dynatrace Assist](#assist-agentic-permissions).

Для получения дополнительной информации см. [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

## Начало работы

![Начните работать быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Попросите Dynatrace Assist суммировать все открытые проблемы, чтобы получить быстрый обзор вашей среды.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Попросите Dynatrace Assist объяснить ваши журналы, чтобы быстро получить информацию, потенциальное влияние, вероятные причины и рекомендуемые следующие шаги.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Получите помощь в выявлении и исправлении уязвимостей, таких как SQL-инъекции.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 из 4Начните работать быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.

### Использование интерфейса разговора Dynatrace Assist

После включения Dynatrace Intelligence генеративного ИИ в вашей среде и настройки разрешений пользователя, вы должны увидеть новую иконку ниже **Поиск** в доке.

1. В Dynatrace, выберите **Dynatrace Assist**.
2. Откроется новое окно с интерфейсом разговора.
3. Введите свой вопрос. См. [Примеры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.") для вдохновения.
4. Выберите **Выполнить** ![Выполнить](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Выполнить") и подождите, пока ответ будет сгенерирован.

* Вы можете задавать дополнительные вопросы.
* Каждый ответ содержит список источников, которые были получены для генерации ответа. Вы можете ознакомиться с этими [источниками](#sources) для получения дополнительной информации.
* Разговоры сохраняются автоматически. Их можно переименовать или удалить из списка разговоров.
* Вы можете отменить генерацию ответа, уточнить свою подсказку и затем повторно отправить вопрос.
* Вы можете использовать интерфейс разговора поверх любого приложения.

Ответы генерируются на основе ресурсов, связанных с Dynatrace. Если модель не может ответить на ваш вопрос, вы увидите сообщение об ошибке:

* Извините, но я не могу ответить на этот запрос. Пожалуйста, попробуйте перефразировать его или добавить дополнительный контекст.

### Использование агентного Dynatrace Assist

**Dynatrace Assist** позволяет вам использовать Dynatrace агентный ИИ и [инструменты и возможности MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.") для доступа и анализа данных вашей среды и использования их для выполнения задач (таких как перечисление проблем или генерация и выполнение запросов DQL) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** делится некоторой дополнительной информацией, такой как результаты вызовов инструментов, с поставщиками предприятий, которые размещают LLM, на основе которых построены Dynatrace агентный и генеративный ИИ. Для получения дополнительной информации о третьих сторонах см. [Используется ли моя информация для обучения Dynatrace Intelligence генеративного ИИ?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Узнайте о часто задаваемых вопросах и найдите ответы.").

С включенным агентным ИИ вы можете попросить **Dynatrace Assist** проанализировать и предоставить информацию о данных и безопасности вашей среды. Для примеров см. [Спросите о данных в вашей среде](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts#assist-ask-about-the-data "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.").

#### Разрешения агентного Dynatrace Assist

**Dynatrace Assist** уважает ваши разрешения пользователя. Это означает, что все вызовы агентного **Dynatrace Assist** выполняются в рамках ваших разрешений пользователя, и результаты не будут включать ничего вне этого.

Чтобы использовать агентный **Dynatrace Assist**, вам необходимо:

* Иметь достаточные разрешения.
* Включить агентный ИИ для **Dynatrace Assist**. Чтобы включить агентный ИИ:

  1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** > **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
  2. Убедитесь, что **Включить генеративный ИИ** включен.
  3. Включите **Включить агентный ИИ**.

Агентный **Dynatrace Assist** может быть недоступен для вас, если вы не соответствуете вышеуказанным предварительным требованиям или если вы доступ к **Dynatrace Assist** из [Встроенных запускаемых разговоров](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запускать предопределенные подсказки в различных приложениях Dynatrace.").

Вам также потребуются дополнительные разрешения для вызова инструментов агентного ИИ. Для списка инструментов и необходимых им разрешений см. [Инструменты MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.").

#### Маскирование ПII

Агентный **Dynatrace Assist** не предоставляет никакого маскирования ПII. Чтобы защитить ваши данные, когда **Dynatrace Assist** обнаруживает ПII в подсказке пользователя, запрос автоматически блокируется и подсказка не отправляется в LLM для обработки.

#### Вызов нескольких инструментов

При взаимодействии с **Dynatrace Assist** в агентном режиме **Assist** может вызвать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** вызвать более 10 инструментов одновременно, он не сможет выполнить взаимодействие.

### Оставить отзыв

Вы можете оставить отзыв, используя встроенный механизм отзыва.

Выберите ![Большой палец вверх](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Большой палец вверх"), если Dynatrace Assist сгенерировал ответ, который соответствует вашим ожиданиям и правильно интерпретировал вашу подсказку.

Выберите ![Большой палец вниз](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Большой палец вниз"), если Dynatrace Assist сгенерировал ответ, который не соответствует вашим ожиданиям или неправильно интерпретировал вашу подсказку. Пожалуйста, предоставьте дополнительный контекст, чтобы мы могли понять, как улучшить эту функцию, чтобы она соответствовала вашим потребностям и ожиданиям.

Ваш отзыв не используется для автоматического обучения моделей. Он рассматривается только командой продукта для мониторинга качества ответов и улучшения основного продукта.

### Источники, использованные для генерации ответов

**Dynatrace Assist** обогащает свои ответы на основе официальных источников Dynatrace, таких как:

* Документация Dynatrace
* [Разработчик Dynatrace](https://developer.dynatrace.com/)
* [Сообщество Dynatrace](https://community.dynatrace.com/)
* [Хаб Dynatrace](https://www.dynatrace.com/hub/)
* [Новости и ресурсы Dynatrace](https://www.dynatrace.com/news/product-news/)
* [Сайт Dynatrace](https://www.dynatrace.com/)

## Концепции

Пройдите следующий процесс, чтобы научиться использовать **Dynatrace Assist**

[01Встроенные запускаемые разговоры

* Справка
* Узнайте, как запускать предопределенные подсказки в различных приложениях Dynatrace.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)[02Примеры подсказок Dynatrace Assist

* Справка
* Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts)

## Сценарии использования

Вы можете использовать агентный **Dynatrace Assist** для:

* Задания общих вопросов о продукте Dynatrace.
* Использования инструментов и возможностей MCP.
* Выполнения задач без необходимости открывать приложение или перехода к другому приложению.
* Объединения инструментов в одном запросе для выполнения нескольких задач.
* Объединения инструментов для выполнения задач и получения ответов на общие вопросы одновременно.

## Связанные темы

* [Начало работы с Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence generative AI.")
* [Встроенные стартовые разговоры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace. ")
* [Часто задаваемые вопросы о Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")
* [Сервер Dynatrace MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp "Узнайте о сервере Dynatrace MCP и о том, как можно к нему подключиться.")

---

## dynatrace-intelligence/copilot/copilot-data-privacy.md

---
title: Dynatrace Intelligence генеративный ИИ: конфиденциальность и безопасность данных
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-data-privacy
scraped: 2026-03-02T21:23:57.832006
---

# Dynatrace Intelligence генеративный ИИ: конфиденциальность и безопасность данных

# Dynatrace Intelligence генеративный ИИ: конфиденциальность и безопасность данных

* Последнее Dynatrace
* Объяснение
* 3-минутное чтение
* Обновлено 28 января 2026 г.

В Dynatrace мы серьезно относимся к своей ответственности за защиту ваших данных. Поймите, как Dynatrace Intelligence генеративный ИИ использует ваши данные и ваши обязанности по обеспечению безопасности ваших данных.

## Данные запроса

Хотя мы маскируем личную идентифицирующую информацию (PII), мы все равно рекомендуем проявлять осторожность при включении личной или конфиденциальной информации в ваши запросы.

Ваши запросы отправляются на LLM, размещенные у корпоративных поставщиков, таких как Microsoft Azure AI и AWS Bedrock, которые обеспечивают работу Dynatrace Intelligence генеративного ИИ. Корпоративные поставщики не хранят данные, которые вы отправляете, или ответы, которые вы получаете. Запросы, которые вы отправляете, и ответы, которые вы получаете, используются только для обеспечения вашего опыта. Корпоративные поставщики также не используют запросы для тонкой настройки или улучшения моделей или услуг, или для обучения моделей у разных клиентов или в разных средах.

Каждый запрос данных отправляется на LLM индивидуально, через SSL-шифрованный сервис, обрабатывается соответствующими корпоративными поставщиками и отправляется обратно в Dynatrace. Если ваша среда находится в регионе EMEA, ваши запросы обрабатываются в регионе ЕС. Если ваша среда находится в регионе NORAM, LATAM или APAC, ваши запросы обрабатываются в регионе США.

Dynatrace может хранить запросы, отправленные в Dynatrace Intelligence генеративный ИИ, и ответы, предоставленные LLM, чтобы понять варианты использования, контекстуализировать обратную связь по ответам и выявить дополнительные ожидания пользователей.

Узнайте больше о [Dynatrace Intelligence генеративном ИИ: архитектуре и потоке данных](/docs/dynatrace-intelligence/copilot/copilot-overview#copilot-data-flow "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.").

## Маскирование PII

Dynatrace версия 1.305+

Маскирование PII реализовано для запросов пользователей, взаимодействующих со стандартной функциональностью генеративного ИИ. Это гарантирует, что конфиденциальная информация, включенная в ваши запросы, не будет передана LLM, размещенным у корпоративных поставщиков.

В настоящее время маскируемые поля включают:

* Адрес электронной почты
* Номер телефона
* Информация IBAN
* Номер кредитной карты
* IP-адрес
* Номер банка США
* Номер социального страхования США
* Номер маршрутизации ABA США
* Параметры запроса URL (только параметры с более чем двумя символами учитываются)
* Номер страхового свидетельства Канады (SIN)

В наших журналах и вызовах моделей LLM мы заменяем значения из выявленных шаблонов выше на фальшивые шаблоны. Это означает, что вы сможете увидеть IBAN в журналах, например, но они будут состоять из случайных чисел, заменяющих исходные значения, включенные в ваши запросы.

Agentic  **Dynatrace Assist** не предоставляет никакого маскирования PII. Чтобы защитить ваши данные, когда  **Dynatrace Assist** обнаруживает PII в запросе пользователя, запрос автоматически блокируется и запрос не отправляется на LLM для обработки.

## Связанные темы

* [Dynatrace Intelligence генеративный ИИ: обзор](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Dynatrace Intelligence генеративный ИИ: часто задаваемые вопросы](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")

---

## dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides.md

---
title: Откройте для себя релевантные руководства по устранению неполадок с помощью Dynatrace Intelligence generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides
scraped: 2026-03-02T21:15:07.049288
---

# Откройте для себя релевантные руководства по устранению неполадок с помощью Dynatrace Intelligence generative AI

* Последнее Dynatrace
* Учебник
* Обновлено 28 января 2026 г.

Dynatrace Intelligence generative AI помогает вам быстрее решать проблемы, автоматически выделяя релевантные руководства по устранению неполадок, такие как блокноты или панели управления, созданные вашей командой.

Чтобы уменьшить среднее время ремонта (MTTR), вы можете использовать предложения документов Dynatrace Intelligence generative AI в приложении **Проблемы**, чтобы проверить, создала ли ваша команда какие-либо руководства по устранению неполадок для проблем, аналогичных той, с которой вы столкнулись.

## Для кого это

Эта статья предназначена для всех пользователей, которые хотят быстро и эффективно устранять и исправлять активные проблемы в своей среде.

## Что вы узнаете

В этой статье вы узнаете, как Dynatrace Intelligence generative AI может предложить релевантные руководства по устранению неполадок, чтобы помочь в решении проблем.

## Прежде чем начать

Dynatrace Intelligence generative AI периодически индексирует блокноты и панели управления, которые были помечены как руководства по устранению неполадок и共享ены в среде.

* По умолчанию, семантическая индексация векторов руководств происходит каждые 6 часов.
* Чтобы Dynatrace Intelligence generative AI мог индексировать и предлагать ваш документ, вы должны поделиться им со всеми пользователями в вашей среде. Dynatrace Intelligence generative AI не будет индексировать или предлагать какие-либо приватные документы или документы, поделиться которыми можно только с конкретными пользователями. Чтобы узнать больше о том, как делиться документами, см. [Поделиться документами](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Поделиться документами Dynatrace (панелями управления, блокнотами и запусками) с другими пользователями Dynatrace в вашей компании.").

### Предварительные знания

* [Обзор Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence generative AI.")
* [Начало работы с Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence generative AI.")
* [Приложение Проблемы](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро добраться до коренной причины инцидентов в вашей среде.")

### Предварительные условия

* Среда Dynatrace SaaS.
* Вы завершили настройку Dynatrace Intelligence generative AI, описанную в [Начало работы с Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence generative AI.").
* У вас включены предложения документов в вашей среде. Включение индексации документов является частью руководства [Включить Dynatrace Intelligence generative AI в вашей среде](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Узнайте, как настроить Dynatrace Intelligence generative AI.").
* У вас есть разрешение `ALLOW davis-copilot:document-search:execute;`. Чтобы узнать, как настроить разрешения, см. [Разрешения в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Узнайте, как назначать разрешения для бакетов и таблиц в Grail.").

## Получите предложения документов для решения проблем

1. Перейдите в приложение **Проблемы** и откройте проблему, которую вы хотите решить.
2. На странице подробной информации о проблеме выберите **Устранение неполадок**. Вы сможете увидеть любые руководства по устранению неполадок, которые вы создали для этой проблемы, а также любые релевантные документы, предложенные Dynatrace Intelligence generative AI.

   Dynatrace Intelligence generative AI индексирует только документы, которые распознаются как руководства по устранению неполадок. Панели управления и блокноты, созданные直接 из приложения **Проблемы**, автоматически распознаются как руководства по устранению неполадок и не требуют префикса `[TSG]`.

   Если вы создаете руководство по устранению неполадок напрямую из панели управления **Панели управления** или **Блокноты**, вам необходимо добавить префикс `[TSG]` к названию документа, чтобы указать, что это руководство по устранению неполадок.

   Независимо от того, как был создан документ, он должен быть поделен на уровне среды, чтобы быть проиндексированным Dynatrace Intelligence generative AI.
3. Необязательно Введите ключевые слова или часть ключевого слова в поле поиска **Имя**, чтобы отфильтровать предложенные документы по имени.
4. Необязательно Выберите **Тип** (`Блокноты`, `Панели управления`), чтобы отфильтровать предложенные документы по типу. По умолчанию оба типа выбраны для предложений документов.
5. Выберите **Просмотр...** на документ, который вы хотите просмотреть. Это действие перенесет вас на руководство по устранению неполадок для дальнейшего исследования.

## Закрепите документы непосредственно к проблеме

Когда вы создаете документ из страницы подробной информации о проблеме, он автоматически закрепляется к этой конкретной проблеме. Закрепленные документы не включаются в список предложенных документов. Вместо этого руководства по устранению неполадок связаны с проблемой, из которой они были созданы. Это гарантирует, что документы, созданные в проблеме, остаются прикрепленными и предотвращает сценарии, в которых ИИ может исключить их из предложенного списка из-за отсутствия сходства.

Документы закрепляются к проблемам путем установки поля `id` в хранилище документов. Шаблон, используемый для закрепления проблемы, состоит из:

* Строки `problem-TSG`.
* Тире `-`.
* Идентификатора проблемы (`event.id` в записи Проблемы Grail).
* Тире `-`.
* Случайного UUID, представленного строкой.

Вы можете увидеть общий шаблон в примере ниже:

`problem-TSG-{problem_ID}-{random-UUID}`

Поскольку символ подчеркивания `_` в идентификаторе проблемы не поддерживается идентификатором документа, его необходимо заменить тире `-`, как показано в примере ниже:

`problem-TSG-1589269324049748129-1747888020000V2-225b65bd-ab67-4efe-9d71-742de9b87387`

Случайный UUID, добавленный в конец шаблона, гарантирует уникальность каждого документа и позволяет нескольким документам быть закрепленными к одной и той же проблеме без конфликтов.

Закрепление документов к проблемам позволяет вам прикрепить дополнительные результаты анализа и доменные знания непосредственно к обнаруженным проблемам. Вы можете закрепить документ к проблеме через рабочие процессы или API для бесшовной внешней интеграции.

### Создайте и прикрепите блокнот к обнаруженной проблеме через Рабочие процессы

Используя действие рабочего процесса JavaScript, вы можете автоматически создать и прикрепить документ (блокнот или панель управления) с вашими доменными результатами анализа к обнаруженной проблеме.

1. Перейдите в **Рабочие процессы** и выберите создать новый рабочий процесс.
2. Выберите предпочитаемый тип триггера.
3. Выберите **Добавить задачу**.
4. В разделе **Выберите действие** выберите **Выполнить JavaScript**.
5. В разделе **Ввод** введите следующий скрипт:

   ```
   import { documentsClient } from "@dynatrace-sdk/client-document";



   import { credentialVaultClient } from '@dynatrace-sdk/client-classic-environment-v2';



   import { execution } from '@dynatrace-sdk/automation-utils';



   function generateGUID() {



   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c)?



   const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);



   return v.toString(16);



   });



   }



   export default async function ({ execution_id })?



   const ex = await execution(execution_id);



   const problem_event = ex.params.event;



   var problem_id = problem_event['event.id'];



   problem_id = problem_id.replace('_', '-'); // Замените неподдерживаемый символ



   // Создайте новый блокнот и закрепите его к проблеме



   try?



   const notebookContent =?



   defaultTimeframe: { from: "now()-2h", to: "now()" },?



   defaultSegments: [],?



   sections:?



   {"id":"19ebed94-69a9-4a6e-b392-7bb7b0deb330","type":"markdown","markdown":"# Доменные результаты анализа\n\nВот внешние, доменные результаты анализа"?



   ],?



   };



   const generatedNotebook = await documentsClient.createDocument?



   body:?



   name: "[TSG] Доменные результаты анализа",?



   type: "notebook",?



   description: "Блокнот, содержащий доменные результаты анализа",?



   id: "problem-TSG-" + problem_id + "-" + generateGUID(),?



   content: new Blob([JSON.stringify(notebookContent)], { type: "application/json" }),?



   };



   // Сделайте документ публичным



   const updated = await documentsClient.updateDocument?



   id: generatedNotebook.id,



   optimisticLockingVersion: generatedNotebook.version,



   body:?



   isPrivate: false,



   }



   } catch (error)?



   console.error("Ошибка создания блокнота:", error);



   }



   return { };



   }
   ```

Как только созданный блокнот будет прикреплен к проблеме, обнаруженной ИИ, вы сможете увидеть его в разделе устранения неполадок. Документ также будет предложен вам для аналогичных проблем в будущем.

![Пример результатов анализа в приложении Проблемы.](https://dt-cdn.net/images/problems-analysis-results-2147-303c6e5b9b.png)

## Связанные темы

* [Dynatrace Intelligence генеративный ИИ обзор](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Проблемы приложения](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро найти коренную причину инцидентов в вашей среде.")

---

## dynatrace-intelligence/copilot/copilot-getting-started.md

---
title: Начало работы с Dynatrace Intelligence генеративным ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-03-02T21:28:52.579872
---

# Начало работы с Dynatrace Intelligence генеративным ИИ

# Начало работы с Dynatrace Intelligence генеративным ИИ

* Последнее Dynatrace
* Руководство по началу работы
* 3-минутное чтение
* Обновлено 28 января 2026 г.

Dynatrace Intelligence генеративный ИИ включен на уровне учетной записи по умолчанию, что означает, что все ваши среды автоматически имеют доступ к нему. Однако функциональность генеративного ИИ должна быть включена на уровне среды через страницу настроек, которая предлагает вам полный контроль над тем, как Dynatrace Intelligence генеративный ИИ включен и настроен в вашей среде.

## Включение Dynatrace Intelligence генеративного ИИ в вашей среде

Чтобы включить Dynatrace Intelligence генеративный ИИ в вашей среде

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить генеративный ИИ**.

![Включение генеративного ИИ в ваших настройках](https://dt-cdn.net/images/generative-ai-settings-1913-24ab3b085b.png)

Если вы не видите страницу настроек, убедитесь, что у вас есть политики `Setting Reader` и `Setting Writer`. Для получения дополнительной информации см. [разрешения на чтение и запись](/docs/manage/identity-access-management/use-cases/access-settings#example-read-and-write-permissions "Предоставление доступа к настройкам").

## Разрешения пользователей

После включения Dynatrace Intelligence генеративного ИИ на уровне среды вам все равно придется предоставить доступ к различным навыкам генеративного ИИ вашим пользователям. Для этого вам необходимо привязать группу, к которой они принадлежат, к политике с следующим утверждением, которое позволяет доступ к генеративному ИИ:

* **Перевод естественного языка в DQL** (`ALLOW davis-copilot:nl2dql:execute;`)
* **Перевод DQL в естественный язык** (`ALLOW davis-copilot:dql2nl:execute;`)
* **Рекомендательная система для разговоров** (`ALLOW davis-copilot:conversations:execute;`)

Для получения дополнительной информации о управлении вашими политиками см. [Управление политиками IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace").

### Доступ к данным на основе пользователей

Поскольку Dynatrace Intelligence генеративный ИИ уважает права пользователей, он может предоставлять разные ответы разным пользователям на основе их прав доступа.

## Включение предложения документов

Предложение документов - это навык Dynatrace Intelligence генеративного ИИ, который позволяет ему рекомендовать вам руководства по устранению неполадок, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов** на основе векторной подобия. Вы можете использовать предложение документов Dynatrace Intelligence генеративного ИИ в ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы**, чтобы быстро получить доступ к руководствам по устранению неполадок, написанным вами или вашей командой для подобных проблем, и уменьшить среднее время ремонта (MTTR).

Если вы хотите, чтобы Dynatrace Intelligence генеративный ИИ предлагал руководства по устранению неполадок для подобных или повторяющихся проблем, вам необходимо разрешить ему искать и индексировать документы, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**, и общие для всех пользователей в вашей среде. Чтобы обеспечить полный контроль над безопасностью ваших данных, эта функциональность является опциональной и выключена по умолчанию.

Чтобы Dynatrace Intelligence генеративный ИИ мог индексировать и предлагать ваш документ, он должен быть общим для всех пользователей в вашей среде. Dynatrace Intelligence генеративный ИИ не будет индексировать или предлагать какие-либо частные документы или документы, общие только с определенными пользователями. Чтобы узнать больше о обмене документами, см. [Обмен документами](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Обмен документами Dynatrace (панелями приборов, тетрадями и запусками) с другими пользователями Dynatrace в вашей компании").

Чтобы включить предложение документов

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить предложения документов**, чтобы разрешить Dynatrace Intelligence генеративному ИИ обрабатывать руководства по устранению неполадок и предлагать их вам.

По умолчанию Dynatrace Intelligence генеративный ИИ индексирует руководства по устранению неполадок каждые 6 часов.

### Семантическое векторное индексирование

Dynatrace Intelligence генеративный ИИ использует семантическое векторное индексирование, чтобы предлагать релевантные руководства по устранению неполадок и панели приборов, общие в среде. Он непрерывно индексирует содержимое панелей приборов и тетрадей, признанных руководствами по устранению неполадок. Когда пользователь получает доступ к представлению устранения неполадок для конкретной проблемы, генеративный ИИ сравнивает описание проблемы с индексированными данными, используя семантическое подобие, чтобы предлагать наиболее релевантные руководства.

Этот процесс основан на векторных представлениях как описания проблемы, так и индексированного содержимого панели приборов или тетради. Чем меньше семантическое расстояние между описанием проблемы и документом, тем выше его релевантность. Это означает, что документ с большей вероятностью будет предложен Dynatrace Intelligence генеративным ИИ в качестве релевантного руководства по устранению неполадок.

## Включение запросов, осведомленных о среде

Запросы, осведомленные о среде Environment, могут обогащать Dynatrace Intelligence генеративный ИИ данными вашей среды. Это позволяет генерировать более точные запросы, которые идентифицируют и ссылаются на релевантные сущности, события, диапазоны, журналы и метрики из вашей среды.

Если вы хотите, чтобы Dynatrace Intelligence генеративный ИИ был осведомлен о деталях и структурах данных вашей среды, вам необходимо разрешить доступ к Grail. Чтобы обеспечить полный контроль над безопасностью ваших данных, эта функциональность является опциональной, и администраторы могут указать, какие таблицы и бакеты Dynatrace Intelligence генеративный ИИ не имеет права доступа.

Чтобы включить запросы, осведомленные о среде

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить запросы, осведомленные о среде**.

Может потребоваться до 24 часов, чтобы Dynatrace Intelligence генеративный ИИ построил или изменил семантический индекс после внесения изменений. Если запросы, осведомленные о среде, отключены и семантический индекс уже существует, Dynatrace Intelligence генеративный ИИ удаляет все средоспецифические данные в течение 24 часов и возвращается к использованию общедоступных источников для построения запросов DQL. Семантический индекс хранится только на вашем сервере Dynatrace.

Чтобы узнать больше о семантическом индексировании и запросах, осведомленных о среде, см. [Запросы, осведомленные о среде Environment](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#environment-aware-queries "Использование Dynatrace Intelligence генеративного ИИ для перевода ваших вопросов на естественном языке в запросы DQL").

### Настройка доступа к данным

После включения запросов, осведомленных о среде, вы сможете увидеть настройки для настройки данных, к которым Dynatrace Intelligence генеративный ИИ не имеет доступа.

Чтобы настроить доступ к данным

1. Перейдите к **Настройка доступа к данным**.
2. Выберите **Добавить новое правило**.
3. Выберите тип данных, который вы хотите исключить из доступа Dynatrace Intelligence, в поле **Тип**.
4. Введите имя бакета или таблицы в поле **Имя**.
5. Выберите **Сохранить изменения**.

## Связанные темы

* [Часто задаваемые вопросы о Dynatrace Intelligence генеративном ИИ](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")
* [Запрос с помощью естественного языка](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Использование Dynatrace Intelligence генеративного ИИ для перевода ваших вопросов на естественном языке в запросы DQL")
* [Советы по написанию лучших подсказок для Dynatrace Intelligence генеративного ИИ](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Узнайте лучшие практики для написания более точных подсказок.")

---

## dynatrace-intelligence/copilot/copilot-overview.md

---
title: Dynatrace Intelligence генеративный ИИ обзор
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-overview
scraped: 2026-03-02T21:16:26.735885
---

# Dynatrace Intelligence генеративный ИИ обзор

# Dynatrace Intelligence генеративный ИИ обзор

* Последнее Dynatrace
* Объяснение
* 5-минутное чтение
* Обновлено 4 февраля 2026 г.

Dynatrace Intelligence генеративный ИИ предназначен для повышения производительности, помощи в настройке и ermögления изучения данных с помощью естественного языка.

## Dynatrace Intelligence генеративный ИИ

Dynatrace Intelligence генеративный ИИ основан на большой языковой модели (LLM). Модель, используемая Dynatrace AI, генерирует ответы на основе ваших входных данных и является вероятностной. Это означает, что ответы генерируются путем прогнозирования наиболее вероятного следующего слова или текста на основе данных, с которыми они были созданы, и предоставленного контекста. Dynatrace Intelligence генеративный ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте). 

Из-за этого подхода эти модели иногда могут表现аться неточно, неполно или ненадежно. Это означает, что существует риск того, что ответ, который вы получите, не точно отражает запрос, который вы предоставили, или что сгенерированный контент звучит разумно, но является неполным или неточным.

Мы рекомендуем вам тщательно оценить ответы, которые вы получаете от Dynatrace Intelligence генеративного ИИ. Если генеративный ИИ отвечает неточно, пожалуйста, предоставьте обратную связь直接 из ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** или  **Dynatrace Assist**.

## Обзор навыков генеративного ИИ

Сервис Dynatrace Intelligence генеративного ИИ предлагает различные и специализированные навыки. В настоящее время генеративный ИИ предлагает четыре навыка:

* NL2DQL: этот навык обеспечивает функциональность быстрого анализа **Prompt**, доступную в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. NL2DQL переводит ваши запросы на естественном языке в DQL запросы. Для получения подробной информации см. [Запрос с помощью естественного языка](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Используйте Dynatrace Intelligence генеративный ИИ для перевода ваших вопросов на естественном языке в DQL запросы").
* DQL2NL: этот навык обеспечивает функциональность **Объяснить запрос** в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. DQL2NL предоставляет сводку и объяснение существующих DQL запросов, чтобы помочь вам лучше понять DQL. Для получения подробной информации см. [Сводка и объяснение запросов](/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot "Узнайте, как сводить и объяснять запросы с помощью навыка Dynatrace Intelligence генеративного ИИ DQL2NL.").
* Рекомендательная система для разговоров: этот навык обеспечивает  **Dynatrace Assist**, наш глобальный интерфейс для разговоров. Рекомендательная система для разговоров способна отвечать на ваши вопросы о помощи Dynatrace, настройке и использовании. Для получения подробной информации см. [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Задайте вопросы на естественном языке и получите быстрые ответы от Dynatrace Assist, вашего помощника генеративного ИИ.").

  + **Dynatrace Assist** также предлагает контекстно-зависимые разговоры в приложениях, таких как ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, или ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. Контекстно-зависимые разговоры запускают предопределенные, контекстно-зависимые запросы и предоставляют вам контекстное объяснение, шаги по исправлению и сводки. Для получения подробной информации см. [Контекстно-зависимые разговоры Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные запросы в различных приложениях Dynatrace.").
* Предложения документов: этот навык обеспечивает функциональность предложения руководства по устранению неполадок в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**. Рекомендация руководства по устранению неполадок улучшает решение проблем путем автоматического предоставления релевантных руководств по устранению неполадок, таких как ноутбуки или панели мониторинга, созданные вашей командой. Для получения подробной информации см. [Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence генеративного ИИ](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Узнайте, как Dynatrace Intelligence генеративный ИИ может предложить руководства по устранению неполадок для исправления проблем.").

Поскольку навыки, предлагаемые Dynatrace Intelligence генеративным ИИ, высоко специализированы, быстрый анализ в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** не может ответить на общие вопросы, и  **Dynatrace Assist** может производить неточные DQL запросы.

## Архитектура и поток данных Dynatrace Intelligence генеративного ИИ

Dynatrace Intelligence генеративный ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте). Это означает, что Dynatrace Intelligence генеративный ИИ будет обогащать ваш запрос релевантным дополнительным контентом или контекстом, который отправляется в основную LLM для генерации подходящего ответа. Контент или контекст, используемый для обогащения вашего запроса, зависит от того, какой базовый навык запрашивается.

Данные и дополнительный контекст используются только для обогащения запросов; модель не учится на этом. Данные клиентов не используются для автоматического уточнения, обучения или улучшения моделей или сервисов. Для получения более подробной информации см. [Как генерируются ответы NL2DQL?](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#nl2dql-answers-generation "Используйте Dynatrace Intelligence генеративный ИИ для перевода ваших вопросов на естественном языке в DQL запросы")

## Ограничения использования Dynatrace Intelligence генеративного ИИ

Не существует ограничения на количество взаимодействий, которые вы можете иметь с генеративным ИИ. Однако существует ограничение на пропускную способность. Это означает, что каждый пользователь может задать 25 вопросов в течение 15-минутного периода.

Аналогичное ограничение существует для количества вопросов, которые могут быть заданы всеми пользователями в вашей среде одновременно. Ваша среда может обрабатывать до 60 вопросов в течение 15-минутного периода.

Если вы превысили любое из ограничений, вы увидите сообщение об ошибке: "Мне жаль, но я не смог сгенерировать ответ для вас из-за необычно высокого спроса. Пожалуйста, попробуйте еще раз через минуту."

## Часто задаваемые вопросы

Если вы хотите узнать больше о Dynatrace Intelligence генеративном ИИ, посетите нашу [страницу часто задаваемых вопросов](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.").

## Связанные темы

* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")

---

## dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips.md

---
title: Dynatrace Intelligence generative AI - Tips for writing better prompts
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips
scraped: 2026-03-02T21:27:09.087228
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
title: Запрос с использованием естественного языка
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql
scraped: 2026-03-02T21:32:54.928652
---

# Запрос с использованием естественного языка

# Запрос с использованием естественного языка

* Последнее Dynatrace
* Обзор
* 5-минутное чтение
* Обновлено 28 января 2026 г.

Вы можете использовать Dynatrace Intelligence генеративный ИИ в панелях и тетрадях, чтобы изучать ваши данные с помощью естественного языка. Это позволяет вам переводить ваши разговорные подсказки непосредственно в запросы DQL, отражающие контекст вашей среды. Вы можете выбрать автоматическое выполнение сгенерированных запросов или сгенерировать только DQL.

## Предварительные условия

Эта страница предполагает, что вы завершили настройку, описанную в [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

## Использование генеративного ИИ в тетрадях

1. Перейдите к ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и откройте или создайте тетрадь, которую можно редактировать.
2. Откройте меню **Добавить** и выберите **Подсказка**. Создается новый раздел тетради генеративного ИИ с пустым полем подсказки.
3. В поле подсказки введите подсказку. Попробуйте `среднее использование процессора в процентах по хосту` или посмотрите примеры, отображаемые в веб-интерфейсе, для вдохновения.
4. Необязательно Если ваша подсказка не указывает временной интервал, вы можете указать его в заголовке раздела. По умолчанию используется **Последние 2 часа**.
5. Выберите **Выполнить**. Генеративный ИИ создает и выполняет запрос для вас.

   Необязательно Если вы хотите увидеть сгенерированный запрос перед его выполнением, откройте меню рядом с кнопкой **Выполнить** и выберите **Сгенерировать только DQL**.
6. Просмотрите результаты.

   * Вы можете просмотреть запрос, развернув **DQL**  справа.
   * Необязательно Вы не можете редактировать запрос напрямую в Dynatrace Intelligence генеративном ИИ, но у вас есть два варианта его повторного использования:

     + Скопируйте запрос и вставьте его вручную в другое место.
     + Откройте меню в заголовке раздела и выберите **Создать раздел DQL**, чтобы создать раздел DQL из этого запроса.
   * Вы можете редактировать свою исходную подсказку, сгенерировать запрос и выполнить его, чтобы обновить результаты.  
     Если вы выберете **Пересмотреть разделы**, приложение Тетради сначала проверит, были ли отредактированы какие-либо подсказки.

     + Если подсказка была отредактирована, DQL сначала будет сгенерирован и затем выполнен.
     + Если подсказки не были отредактированы, существующий сгенерированный DQL будет просто выполнен.
7. Необязательно Выберите **Параметры** в заголовке раздела, чтобы изменить визуализацию (см. [документацию по визуализациям](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Создайте, отредактируйте и просмотрите визуализации на ваших панелях и тетрадях Dynatrace.") для получения дополнительной информации).

   Автоматически выберите визуализацию

   Чтобы Dynatrace автоматически выбрал визуализацию для вашего запроса, включите **Авто-выбор** в правом верхнем углу панели настроек визуализации.

   * Если вы вручную выберете другую визуализацию, переключатель **Авто-выбор** будет выключен.
   * Чтобы Dynatrace снова автоматически выбрал визуализацию, включите **Авто-выбор**.

## Использование генеративного ИИ в панелях

1. Перейдите к [![Панели](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели") **Панели**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создайте интерактивные, настраиваемые представления, чтобы визуализировать, анализировать и делиться вашими данными наблюдаемости в режиме реального времени.") и откройте или создайте панель, которую можно редактировать.
2. Откройте меню **Добавить** и выберите **Подсказка**.

   * Создается новый плитка панели генеративного ИИ Dynatrace
   * Панель справа отображает:

     + Пустое поле названия плитки, которое можно настроить
     + Поле подсказки, за которым следуют некоторые примеры, которые можно выбрать для попытки
     + Кнопку **Выполнить**
3. Необязательно В верхней части панели определения подсказки введите название плитки.
4. В поле подсказки введите подсказку. Попробуйте `среднее использование процессора в процентах по хосту` или посмотрите примеры, отображаемые в веб-интерфейсе, для вдохновения.
5. Необязательно Если ваша подсказка не указывает временной интервал, вы можете указать его для панели в заголовке панели (по умолчанию используется **Последние 2 часа**) или в настройках **Пользовательский временной интервал** (для временного интервала, специфичного для плитки).
6. Выберите **Выполнить**. Генеративный ИИ создает и выполняет запрос для вас.
7. Просмотрите результаты.

   * Чтобы просмотреть запрос, разверните **DQL**  под полем подсказки.
   * Необязательно Вы не можете редактировать запрос напрямую в Dynatrace Intelligence генеративном ИИ, но у вас есть два варианта его повторного использования:

     + Скопируйте запрос и вставьте его вручную в другое место.
     + Откройте меню в заголовке плитки и выберите **Создать плитку DQL**, чтобы создать плитку DQL из этого запроса.
   * Вы можете редактировать свою исходную подсказку и выполнить ее, чтобы обновить запрос и результаты.  
     Если вы обновите панель, приложение Панели сначала проверит, были ли отредактированы какие-либо подсказки.

     + Если подсказка была отредактирована, DQL сначала будет сгенерирован и затем выполнен.
     + Если подсказки не были отредактированы, существующий сгенерированный DQL будет просто выполнен.
8. Необязательно Выберите вкладку **Визуализация**, чтобы изменить визуализацию (см. [документацию по визуализациям](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Создайте, отредактируйте и просмотрите визуализации на ваших панелях и тетрадях Dynatrace.") для получения дополнительной информации).

Хотя Dynatrace Intelligence генеративный ИИ не тарифицируется, все запросы, выполняемые генеративным ИИ, подлежат потреблению лицензии в соответствии с вашим существующим лицензионным соглашением.

## Запросы, осведомленные о Environment

Запросы, осведомленные о Environment, обогащают Dynatrace Intelligence генеративный ИИ данными вашей среды. Это позволяет генерировать более точные запросы, которые идентифицируют и ссылаются на соответствующие сущности, события, прыжки, журналы и метрики из вашей среды. Вы также можете выполнять более сложные анализы данных, спрашивая Dynatrace Intelligence генеративный ИИ о деталях ваших данных. Чтобы узнать больше о том, как контролировать и управлять доступом генеративного ИИ к данным и как включить запросы, осведомленные о среде, см. [Включить запросы, осведомленные о среде](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-environment-aware-queries "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

### Семантический индекс Dynatrace Intelligence генеративного ИИ

Как только будет включено, Dynatrace Intelligence генеративный ИИ периодически сканирует ваши данные Grail, чтобы создать свой собственный семантический индекс. Определенные фрагменты данных отправляются в Microsoft Azure OpenAI во время семантического индексирования. Примерами таких фрагментов данных являются ключи метрик, размерности и имена полей. Когда пользователь предоставляет подсказку, Dynatrace Intelligence генеративный ИИ сначала определяет наиболее актуальные фрагменты из данных, которые он проиндексировал. Затем наш генеративный ИИ отправляет подсказку пользователя, актуальные фрагменты данных и некоторые примеры значений полей, наблюдаемых в вашей среде, в Microsoft Azure OpenAI для обработки.

Включение запросов, осведомленных о среде, позволяет Dynatrace Intelligence генеративному ИИ идентифицировать уникальные поля данных и пользовательские метрики в вашей среде и помогает вам в анализе, сочетая вашу подсказку с актуальными, уникальными полями данных и типами.

Допустим, вы отслеживаете бронирования путешествий для новых поездок. В этом случае вы хотели бы отслеживать:

* прибыль, полученную от каждого бронирования, как событие бизнеса
* применимые скидки как событие бизнеса
* время, необходимое клиентам для завершения бронирования, как пользовательскую метрику

С учетом этого вы можете дать Dynatrace Intelligence генеративному ИИ следующую команду: **"Покажите мне среднюю сумму, заработанную, и снижение цены для новых поездок за последний месяц"**.

Если у вас включены запросы, осведомленные о среде, будет сгенерирован следующий DQL, предоставляющий вам результаты, актуальные для вашей среды:

```
fetch bizevents , from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {profit= avg(profit), discount= avg(discount)}
```

Dynatrace Intelligence генеративный ИИ может сделать вывод, что "сумма, заработанная" относится к полю прибыли, а "снижение цены" относится к полю скидки, даже если ваша подсказка не использовала правильные имена полей.

Если у вас не включены запросы, осведомленные о среде, Dynatrace Intelligence генеративный ИИ попытается сослаться на поля по именам, которые вы предоставили. Будет сгенерирован следующий, неправильный DQL, поскольку поля не существуют в вашей среде:

```
fetch bizevents, from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {avg_money_made = avg(money_made), avg_price_reduction = avg(price_reduction)}
```

Альтернативно, вы можете спросить Dynatrace Intelligence генеративный ИИ следующий вопрос: **"В среднем, сколько времени требуется клиентам для бронирования новых поездок?"**

Если у вас включены запросы, осведомленные о среде, будет сгенерирован следующий DQL, предоставляющий вам результаты, актуальные для вашей среды:

```
timeseries avg(new_trip_booking_duration)
```

Если у вас не включены запросы, осведомленные о среде, вы, скорее всего, получите сообщение об ошибке, поскольку Dynatrace Intelligence генеративный ИИ не сможет правильно сопоставить ваш вопрос с вашим пользовательским ключом метрики. В этом случае наш генеративный ИИ не может предоставить действительный запрос DQL, поскольку он не может найти совпадающую встроенную метрику.

### Доступ к данным на основе пользователя

Поскольку Dynatrace Intelligence генеративный ИИ уважает права пользователей, он может предоставлять разные ответы разным пользователям на основе их прав доступа.

## Как генерируются ответы NL2DQL?

![Dynatrace Intelligence генеративный ИИ диаграмма, объясняющая, как генерируются ответы NL2QL](https://dt-cdn.net/images/davis-copilot-nl2dql-responses-1920-1a15aa1055.png)

Процесс генерации ответов Dynatrace Intelligence генеративного ИИ NL2DQL можно суммировать в 4 шага.

1. Dynatrace Intelligence генеративный ИИ получает запрос от пользователя.
2. Если запрос хорошо сформулирован и распознан (см. [Dynatrace Intelligence генеративный ИИ - Советы по написанию лучших запросов](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Узнайте лучшие практики для написания более точных запросов.") для получения дополнительной информации), Dynatrace Intelligence генеративный ИИ сопоставляет запрос пользователя с контентом, принадлежащим Dynatrace, таким как документация и отобранные примеры запросов, и передает запрос в LLM.

   Если вы включили запросы, осведомленные о среде, соответствующие фрагменты данных будут использоваться для обогащения запроса вместе с контентом, принадлежащим Dynatrace.
3. LLM генерирует ответ и проверяет, является ли DQL действительным.
4. Ответ возвращается в соответствующее приложение, тетради или панели мониторинга, и вывод отображается пользователю.

## Оставьте отзыв

Чтобы помочь нам улучшить Dynatrace Intelligence генеративный ИИ, вы можете предоставить отзыв напрямую из вашей тетради или панели мониторинга. Под полем запроса:

* Выберите ![Большой палец вверх](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Большой палец вверх") если Dynatrace Intelligence генеративный ИИ правильно интерпретировал ваш запрос и сгенерировал и выполнил запрос DQL, соответствующий вашим ожиданиям.
* Выберите ![Большой палец вниз](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Большой палец вниз") если Dynatrace Intelligence генеративный ИИ сгенерировал и выполнил запрос DQL, который не оправдал ваших ожиданий или неправильно интерпретировал ваш запрос. Пожалуйста, предоставьте дополнительный контекст, чтобы мы могли понять, как улучшить эту функциональность, чтобы она соответствовала вашим потребностям и ожиданиям.

Не делитесь личной или конфиденциальной информацией в вашем отзыве.

## Связанные темы

* [Обзор Dynatrace Intelligence генеративный ИИ](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence генеративный ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Часто задаваемые вопросы о Dynatrace Intelligence генеративный ИИ](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")
* [Dynatrace Intelligence генеративный ИИ - Советы по написанию лучших запросов](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Узнайте лучшие практики для написания более точных запросов.")
* [Примеры быстрого анализа с помощью генеративного ИИ](/docs/dynatrace-intelligence/use-cases/copilot-examples "Узнайте больше о том, какие запросы работают хорошо в Dynatrace Intelligence генеративном ИИ.")

---

## dynatrace-intelligence/copilot.md

---
title: Dynatrace Intelligence агентное и генеративное ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot
scraped: 2026-03-01T21:11:19.065826
---

# Dynatrace Intelligence агентное и генеративное ИИ

# Dynatrace Intelligence агентное и генеративное ИИ

* Последнее Dynatrace
* Приложение
* 2-минутное чтение
* Обновлено 28 января 2026 г.

Dynatrace Intelligence генеративный ИИ, разработанный Dynatrace, позволяет исследовать данные с помощью естественного языка, помогая в обучении и повышении производительности. Dynatrace Intelligence генеративный ИИ принимает ваш запрос и переводит его в DQL, и способен автоматически выполнять сгенерированные запросы DQL.

## Случаи использования

* Быстрее ознакомиться с DQL, переводя запросы на естественном языке в готовые к использованию запросы.
* Сэкономить время, генерируя и выполняя сгенерированные запросы DQL вместо того, чтобы писать их вручную.
* Получить ответы на вопросы о помощи и обучении быстро, без необходимости доступа к документации или другим ресурсам поддержки Dynatrace.
* Лучше понять существующие DQL, получая краткие описания и объяснения запросов.
* Попросите Dynatrace Assist предоставить контекстные сведения:

  + Получите четкие описания проблем, их коренных причин и предложенных шагов по исправлению в приложении Problems.
  + Получите объяснения предупреждающих сигналов в приложении Kubernetes.
  + Получите объяснения планов выполнения в приложении Databases на естественном языке.
* Откройте для себя релевантные руководства по устранению неполадок, чтобы ускорить исправление проблем.

[#### Обзор Dynatrace Intelligence генеративного ИИ

Узнайте о безопасности данных и других аспектах Dynatrace Intelligence генеративного ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-overview)[#### Начало работы с Dynatrace Intelligence генеративным ИИ

Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.

* Руководство

Прочитайте это руководство](/docs/dynatrace-intelligence/copilot/copilot-getting-started)

## Анализ данных с помощью генеративного ИИ

[#### Запрос с помощью естественного языка

Используйте Dynatrace Intelligence генеративный ИИ, чтобы перевести ваши запросы на естественном языке в запросы DQL

* Обзор

Смотрите обзор](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql)[#### Dynatrace Intelligence генеративный ИИ - Советы по написанию лучших запросов

Узнайте лучшие практики для написания более точных запросов.

* Справочник

Прочитайте этот справочник](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips)[#### Примеры быстрого анализа с помощью генеративного ИИ

Узнайте больше о том, какие запросы работают хорошо в Dynatrace Intelligence генеративном ИИ.

* Справочник

Прочитайте этот справочник](/docs/dynatrace-intelligence/use-cases/copilot-examples)[#### Суммировать и объяснить запросы

Узнайте, как суммировать и объяснять запросы с помощью навыка Dynatrace Intelligence генеративного ИИ DQL2NL.

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

Для получения более подробной информации о том, какие запросы работают хорошо в **Dynatrace Assist**, смотрите [примеры запросов](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие запросы работают хорошо в Dynatrace Assist.").

## Векторное совпадение документов

[#### Откройте для себя релевантные руководства по устранению неполадок с помощью Dynatrace Intelligence генеративного ИИ

Узнайте, как Dynatrace Intelligence генеративный ИИ может предложить руководства по устранению неполадок для исправления проблем.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides)

## Узнайте больше

[#### Dynatrace Intelligence генеративный ИИ: политика безопасности и конфиденциальности данных

Узнайте о политике безопасности и конфиденциальности данных Dynatrace Intelligence генеративного ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-data-privacy)[#### Dynatrace Intelligence генеративный ИИ: часто задаваемые вопросы

Узнайте о часто задаваемых вопросах и найдите ответы.

* Устранение неполадок

Прочитайте этот справочник](/docs/dynatrace-intelligence/copilot/copilot-faq)

---
