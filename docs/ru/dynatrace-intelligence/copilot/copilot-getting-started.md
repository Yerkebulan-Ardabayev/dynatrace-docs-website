---
title: Get started with Dynatrace Intelligence agentic and generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-03-06T21:13:25.807648
---

# Начало работы с агентным и генеративным ИИ Dynatrace Intelligence

# Начало работы с агентным и генеративным ИИ Dynatrace Intelligence

* Последняя версия Dynatrace
* Практическое руководство
* Время чтения: 3 мин.
* Обновлено 03 марта 2026

Агентный и генеративный ИИ Dynatrace Intelligence включен на уровне учетной записи по умолчанию, что означает, что все ваши окружения автоматически имеют к нему доступ. Однако функциональность ИИ все равно необходимо включить на уровне окружения через страницу настроек, которая предоставляет вам полный контроль над тем, как агентный и генеративный ИИ Dynatrace Intelligence включается и настраивается в вашем окружении.

## Включение генеративного ИИ Dynatrace Intelligence в вашем окружении

Чтобы включить генеративный ИИ Dynatrace Intelligence в вашем окружении

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable generative AI**.

![Включение генеративного ИИ в настройках](https://dt-cdn.net/images/generative-ai-settings-1913-24ab3b085b.png)

Если вы не видите страницу настроек, убедитесь, что вам назначены политики `Setting Reader` и `Setting Writer`. Для получения дополнительной информации см. [разрешения на чтение и запись](../../manage/identity-access-management/use-cases/access-settings.md#example-read-and-write-permissions "Grant access to Settings").

### Разрешения пользователей

После включения генеративного ИИ Dynatrace Intelligence на уровне окружения вам все равно потребуется предоставить доступ к различным навыкам генеративного ИИ вашим пользователям. Для этого необходимо привязать группу, к которой они принадлежат, к политике со следующим выражением, разрешающим доступ к генеративному ИИ:

* **Перевод естественного языка в DQL** (`ALLOW davis-copilot:nl2dql:execute;`)
* **Перевод DQL в естественный язык** (`ALLOW davis-copilot:dql2nl:execute;`)
* **Диалоговый рекомендатель** (`ALLOW davis-copilot:conversations:execute;`)

Для получения дополнительной информации об управлении политиками см. [Управление политиками IAM](../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

## Включение агентного ИИ для Dynatrace Assist

**Dynatrace Assist** позволяет использовать агентный ИИ Dynatrace и [инструменты и возможности MCP](../../../common/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp.md#server "Learn about the Dynatrace MCP server and how you can connect to it.") для доступа и анализа данных вашего окружения, а также для выполнения задач (таких как просмотр проблем или генерация и выполнение DQL-запросов) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** передает некоторую дополнительную информацию, такую как результаты вызовов инструментов, корпоративным поставщикам, размещающим LLM, на которых основан агентный и генеративный ИИ Dynatrace. Для получения дополнительной информации о третьих сторонах см. [Используются ли мои данные для обучения генеративного ИИ Dynatrace Intelligence?](../../../common/dynatrace-intelligence/copilot/copilot-faq.md#copilot-training-on-data "Learn about frequently asked questions and find your answers.").

Для использования агентного **Dynatrace Assist** необходимо

* Иметь достаточные разрешения.
* Включить агентный ИИ для **Dynatrace Assist**. Чтобы включить агентный ИИ

  1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
  2. Убедитесь, что **Enable generative AI** включен.
  3. Включите **Enable agentic AI**.

Агентный **Dynatrace Assist** может быть недоступен, если вы не выполняете указанные выше предварительные требования или если вы обращаетесь к **Dynatrace Assist** через [встроенные стартеры диалогов](chat-with-davis-copilot/copilot-conv-starters.md "Learn how to trigger predefined prompts in various Dynatrace applications.").

### Разрешения агентного режима **Dynatrace Assist**

Вам также потребуются дополнительные разрешения для вызова инструментов агентного ИИ. Список инструментов и требуемых разрешений см. в разделе [Инструменты MCP](../../../common/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp.md#server "Learn about the Dynatrace MCP server and how you can connect to it.").

### Маскирование персональных данных (PII)

Агентный **Dynatrace Assist** не обеспечивает маскирование персональных данных (PII). Для защиты ваших данных, когда **Dynatrace Assist** обнаруживает PII в пользовательском запросе, запрос автоматически блокируется и не отправляется в LLM для обработки.

### Вызов нескольких инструментов

При взаимодействии с **Dynatrace Assist** в агентном режиме **Assist** может вызывать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** одновременного вызова более 10 инструментов, завершить взаимодействие не удастся.

## Доступ к данным на основе пользователей

Агентный и генеративный ИИ Dynatrace Intelligence учитывает привилегии и разрешения пользователей. Это означает, что

* Он может предоставлять различные ответы разным пользователям в зависимости от их прав доступа.
* Все вызовы агентного **Dynatrace Assist** выполняются в рамках ваших пользовательских разрешений, и результаты не будут содержать ничего, выходящего за их пределы.

## Включение предложений документов

Предложение документов -- это навык агентного и генеративного ИИ Dynatrace Intelligence, который позволяет рекомендовать вам руководства по устранению неполадок, созданные в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, на основе векторного сходства. Вы можете использовать предложения документов агентного и генеративного ИИ Dynatrace Intelligence в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** для быстрого получения руководств по устранению неполадок, написанных вами или вашей командой для аналогичных проблем, и сокращения среднего времени восстановления (MTTR).

Если вы хотите, чтобы агентный и генеративный ИИ Dynatrace Intelligence предлагал руководства по устранению неполадок для аналогичных или повторяющихся проблем, вам необходимо разрешить ему выполнять поиск и индексацию документов, созданных в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и доступных всем пользователям вашего окружения. Для обеспечения полного контроля над безопасностью ваших данных эта функциональность является опциональной и отключена по умолчанию.

Чтобы агентный и генеративный ИИ Dynatrace Intelligence мог индексировать и предлагать ваш документ, он должен быть доступен всем пользователям вашего окружения. Агентный и генеративный ИИ Dynatrace Intelligence не будет индексировать или предлагать приватные документы или документы, доступные только определенным пользователям. Подробнее о совместном доступе к документам см. [Совместный доступ к документам](../../discover-dynatrace/get-started/dynatrace-ui/share.md "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

Чтобы включить предложения документов

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable document suggestions**, чтобы разрешить агентному и генеративному ИИ Dynatrace Intelligence загружать руководства по устранению неполадок и предлагать их вам.

По умолчанию агентный и генеративный ИИ Dynatrace Intelligence индексирует руководства по устранению неполадок каждые 6 часов.

### Семантическое векторное индексирование

Агентный и генеративный ИИ Dynatrace Intelligence использует семантическое векторное индексирование для предложения релевантных панелей мониторинга и блокнотов для устранения неполадок, доступных в окружении. Он непрерывно индексирует содержимое панелей мониторинга и блокнотов, распознанных как руководства по устранению неполадок. Когда пользователь обращается к представлению устранения неполадок для конкретной проблемы, генеративный ИИ сравнивает описание проблемы с проиндексированными данными, используя семантическое сходство, для предложения наиболее релевантных руководств.

Этот процесс основан на векторных представлениях как описания проблемы, так и содержимого проиндексированной панели мониторинга или блокнота. Чем меньше семантическое расстояние между описанием проблемы и документом, тем выше его оценка релевантности. Это означает, что такой документ с большей вероятностью будет предложен агентным и генеративным ИИ Dynatrace Intelligence в качестве релевантного руководства по устранению неполадок.

## Включение запросов с учетом окружения

Запросы с учетом окружения могут обогатить агентный и генеративный ИИ Dynatrace Intelligence данными вашего окружения. Это позволяет генерировать более точные запросы, которые идентифицируют и ссылаются на релевантные сущности, события, спаны, логи и метрики из вашего окружения.

Если вы хотите, чтобы агентный и генеративный ИИ Dynatrace Intelligence учитывал детали и структуры данных вашего окружения, вам необходимо разрешить доступ к Grail. Для обеспечения полного контроля над безопасностью ваших данных эта функциональность является опциональной, и администраторы могут указать, к каким таблицам данных и бакетам агентный и генеративный ИИ Dynatrace Intelligence не имеет права доступа.

Чтобы включить запросы с учетом окружения

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable environment-aware queries**.

Построение или обновление семантического индекса после внесения изменений может занять до 24 часов. Если запросы с учетом окружения отключены и семантический индекс уже существует, агентный и генеративный ИИ Dynatrace Intelligence удалит все данные, специфичные для окружения, в течение 24 часов и вернется к использованию общедоступных источников для построения DQL-запросов. Семантический индекс хранится только на вашем тенанте Dynatrace.

Подробнее о семантическом индексировании и запросах с учетом окружения см. [Запросы с учетом окружения](quick-analysis-copilot-dql.md#environment-aware-queries "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

### Настройка доступа к данным

После включения запросов с учетом окружения вы сможете увидеть настройки для конфигурации данных, к которым агентный и генеративный ИИ Dynatrace Intelligence не имеет права доступа.

Чтобы настроить доступ к данным

1. Перейдите в **Configure data access**.
2. Выберите **Add a new rule**.
3. Выберите тип данных, которые вы хотите исключить из доступа Dynatrace Intelligence, в поле **Type**.
4. Введите имя бакета или таблицы в поле **Name**.
5. Выберите **Save changes**.

## Связанные темы

* [Часто задаваемые вопросы об агентном и генеративном ИИ Dynatrace Intelligence](../../../common/dynatrace-intelligence/copilot/copilot-faq.md "Learn about frequently asked questions and find your answers.")
* [Запросы на естественном языке](quick-analysis-copilot-dql.md "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Агентный и генеративный ИИ Dynatrace Intelligence -- советы по написанию лучших промптов](quick-analysis-copilot-dql/copilot-tips.md "Learn best practices for writing more accurate prompts.")
