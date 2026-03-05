---
title: Начало работы с Dynatrace Intelligence агентным и генеративным ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-03-05T21:23:14.793631
---

# Начало работы с Dynatrace Intelligence агентным и генеративным ИИ

# Начало работы с Dynatrace Intelligence агентным и генеративным ИИ

* Последнее Dynatrace
* Руководство по началу работы
* 3-минутное чтение
* Обновлено 03 марта 2026 г.

Dynatrace Intelligence агентный и генеративный ИИ включен на уровне учетной записи по умолчанию, что означает, что все ваши среды автоматически имеют доступ к нему. Однако функциональность ИИ должна быть включена на уровне среды через страницу настроек, которая предлагает вам полный контроль над тем, как Dynatrace Intelligence агентный и генеративный ИИ включен и настроен в вашей среде.

## Включение Dynatrace Intelligence генеративного ИИ в вашей среде

Чтобы включить Dynatrace Intelligence генеративный ИИ в вашей среде

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить генеративный ИИ**.

![Включение генеративного ИИ в настройках](https://dt-cdn.net/images/generative-ai-settings-1913-24ab3b085b.png)

Если вы не видите страницы настроек, убедитесь, что у вас есть политики `Setting Reader` и `Setting Writer`. Для получения дополнительной информации см. [разрешения на чтение и запись](/docs/manage/identity-access-management/use-cases/access-settings#example-read-and-write-permissions "Предоставление доступа к настройкам").

### Разрешения пользователей

После включения Dynatrace Intelligence генеративного ИИ на уровне среды вам все равно придется предоставить доступ к различным навыкам генеративного ИИ вашим пользователям. Для этого необходимо привязать группу, к которой они принадлежат, к политике с следующим утверждением, которое позволяет доступ к генеративному ИИ:

* **Перевод естественного языка в DQL** (`ALLOW davis-copilot:nl2dql:execute;`)
* **Перевод DQL в естественный язык** (`ALLOW davis-copilot:dql2nl:execute;`)
* **Рекомендатель по разговорам** (`ALLOW davis-copilot:conversations:execute;`)

Для получения дополнительной информации о управлении вашими политиками см. [Управление политиками IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace").

## Включение агентного ИИ для Dynatrace Assist

**Dynatrace Assist** позволяет вам использовать Dynatrace агентный ИИ и [инструменты и возможности MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и о том, как вы можете подключиться к нему.") для доступа и анализа данных вашей среды и использования их для выполнения задач (таких как перечисление проблем или генерация и выполнение запросов DQL) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** делится некоторой дополнительной информацией, такой как результаты вызовов инструментов, с корпоративными поставщиками, которые размещают LLM, на основе которых построены Dynatrace агентный и генеративный ИИ. Для получения дополнительной информации о третьих сторонах см. [Используется ли моя информация для обучения Dynatrace Intelligence генеративному ИИ?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Узнайте о часто задаваемых вопросах и найдите ответы на них").

Чтобы использовать агентный **Dynatrace Assist**, вам необходимо

* Иметь достаточные разрешения.
* Иметь агентный ИИ, включенный для **Dynatrace Assist**. Чтобы включить агентный ИИ

  1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
  2. Убедитесь, что **Включить генеративный ИИ** включен.
  3. Включите **Включить агентный ИИ**.

Агентный **Dynatrace Assist** может быть недоступен для вас, если вы не соответствуете вышеуказанным предварительным требованиям или если вы доступ к **Dynatrace Assist** из [встроенных стартовых разговоров](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace").

### Разрешения агентного Dynatrace Assist

Вам также понадобятся дополнительные разрешения для вызова инструментов агентного ИИ. Для списка инструментов и необходимых им разрешений см. [инструменты MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и о том, как вы можете подключиться к нему.").

### Маскирование ПII

Агентный **Dynatrace Assist** не предоставляет никакого маскирования ПII. Чтобы защитить ваши данные, когда **Dynatrace Assist** обнаруживает ПII в запросе пользователя, запрос автоматически блокируется и запрос не отправляется в LLM для обработки.

### Вызов нескольких инструментов

При взаимодействии с агентным **Dynatrace Assist** он может вызывать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** вызвать более 10 инструментов одновременно, он не сможет завершить взаимодействие.

## Доступ к данным на основе пользователей

Dynatrace Intelligence агентный и генеративный ИИ уважает привилегии и разрешения пользователей. Это означает, что

* Он может предоставлять разные ответы разным пользователям на основе их прав доступа.
* Все вызовы агентного **Dynatrace Assist** выполняются в рамках прав доступа пользователя, и результаты не будут включать ничего вне его.

## Включение предложения документов

Предложение документов — это навык Dynatrace Intelligence агентного и генеративного ИИ, который позволяет ему рекомендовать вам руководства по устранению неполадок, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов** на основе векторной подобия. Вы можете использовать предложение документов Dynatrace Intelligence агентного и генеративного ИИ в ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы**, чтобы быстро получить руководства по устранению неполадок, написанные вами или вашей командой для подобных проблем, и уменьшить среднее время ремонта (MTTR).

Если вы хотите, чтобы Dynatrace Intelligence агентный и генеративный ИИ предлагал руководства по устранению неполадок для подобных или повторяющихся проблем, вам необходимо разрешить ему искать и индексировать документы, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**, и общие со всеми пользователями в вашей среде. Чтобы обеспечить полный контроль над безопасностью ваших данных, эта функциональность является опциональной и выключена по умолчанию.

Чтобы Dynatrace Intelligence агентный и генеративный ИИ мог индексировать и предлагать ваш документ, он должен быть общим со всеми пользователями в вашей среде. Dynatrace Intelligence агентный и генеративный ИИ не будет индексировать или предлагать никакие частные документы или документы, общие только с определенными пользователями. Чтобы узнать больше о обмене документами, см. [Обмен документами](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Обмен документами Dynatrace (панелями приборов, тетрадями и запусками) с другими пользователями Dynatrace в вашей компании.").

Чтобы включить предложение документов

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить предложения документов**, чтобы разрешить Dynatrace Intelligence агентному и генеративному ИИ ингестировать руководства по устранению неполадок и предлагать их вам.

По умолчанию Dynatrace Intelligence агентный и генеративный ИИ индексирует руководства по устранению неполадок каждые 6 часов.

### Семантическое векторное индексирование

Dynatrace Intelligence агентный и генеративный ИИ использует семантическое векторное индексирование, чтобы предлагать соответствующие панели приборов и тетради по устранению неполадок, общие в среде. Он непрерывно индексирует содержимое панелей приборов и тетрадей, признанных руководствами по устранению неполадок. Когда пользователь доступ к представлению устранения неполадок для конкретной проблемы, генеративный ИИ сравнивает описание проблемы с индексированными данными, используя семантическое подобие, чтобы предлагать наиболее релевантные руководства.

Этот процесс основан на векторных представлениях как описания проблемы, так и индексированного содержимого документа или панели приборов. Чем меньше семантическое расстояние между описанием проблемы и документом, тем выше его релевантность. Это означает, что документ с большей вероятностью будет предложен Dynatrace Intelligence агентным и генеративным ИИ в качестве релевантного руководства по устранению неполадок.

## Включение запросов, осведомленных о среде



Environment-aware queries can enrich Dynatrace Intelligence agentic and generative AI with your environment's data. This lets you generate more accurate queries that identify and reference relevant entities, events, spans, logs, and metrics from your environment.

If you want Dynatrace Intelligence agentic and generative AI to be aware of the details and structures of your environment's data, you'll need to allow access to Grail. To ensure you have full control over the security of your data, this functionality is opt-in, and admin users can specify which data tables and buckets Dynatrace Intelligence agentic and generative AI is not allowed to access.

To enable environment-aware queries

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Turn on **Enable environment-aware queries**.

It can take up to 24 hours for Dynatrace Intelligence agentic and generative AI to build or amend the semantic index after changes are made. If environment-aware queries are disabled and the semantic index already exists, Dynatrace Intelligence agentic and generative AI purges all environment-specific data within 24 hours, and returns to using publicly available sources for building DQL queries. The semantic index is stored only on your Dynatrace tenant.

To learn more about semantic indexing and environment-aware queries, see [Environment-aware queries](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#environment-aware-queries "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

### Configure your data access

After enabling environment-aware queries, you'll be able to see the settings for configuring data that Dynatrace Intelligence agentic and generative AI isn't allowed to access.

To configure your data access

1. Go to **Configure data access**.
2. Select **Add a new rule**.
3. Select the type of data you want to exclude from Dynatrace Intelligence access in the **Type** field.
4. Type the name of the bucket or table in the **Name** field.
5. Select **Save changes**.

## Related topics

* [Dynatrace Intelligence agentic and generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence agentic and generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")