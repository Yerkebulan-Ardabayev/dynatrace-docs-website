---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-03-06T21:33:52.070519
---

# Dynatrace Assist

# Dynatrace Assist

* Последняя версия Dynatrace
* Приложение
* Время чтения: 2 мин
* Обновлено 03 марта 2026 г.

**Dynatrace Assist** позволяет общаться с Dynatrace Intelligence и задавать вопросы о данных в вашей среде, а также общие вопросы, которые помогут вам освоить Dynatrace и понять основные концепции.

### Разрешения

В следующей таблице описаны необходимые разрешения.

document:documents:write

сохранение диалогов в хранилище документов

document:documents:read

чтение диалогов из хранилища документов

document:documents:delete

удаление диалогов из хранилища документов

davis-copilot:conversations:execute

использование функции диалогов Copilot

hub:catalog:read

чтение каталога для отображения приложения, инициировавшего диалог

davis-copilot:nl2dql:execute

использование агентной функции Copilot

davis-copilot:dql2nl:execute

использование агентной функции Copilot

mcp-gateway:servers:invoke

использование агентной функции Copilot

mcp-gateway:servers:read

использование агентной функции Copilot

davis:analyzers:read

использование агентной функции Copilot

Для использования **Dynatrace Assist** в режиме генеративного ИИ вам потребуются только следующие разрешения:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

Остальные разрешения из таблицы необходимы только в том случае, если вы хотите использовать все агентные возможности Dynatrace Assist. Подробнее см. в разделе [Агентные разрешения Dynatrace Assist](copilot-getting-started.md#assist-agentic "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

Подробнее см. в разделе [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](copilot-getting-started.md "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

## Начало работы

![Get started quickly and easily by asking Dynatrace Assist a question. Try out one of the examples to see what's possible.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Ask Dynatrace Assist to summarize all open problems to get a quick overview of your environment.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Ask Dynatrace Assist to explain your logs to quickly get the insights, potential impact, likely causes and recommended next steps.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Get help with identifying and fixing vulnerabilities, such as SQL injections.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 из 4. Начните быстро и легко, задав вопрос Dynatrace Assist. Попробуйте один из примеров, чтобы узнать о возможностях.

### Использование диалогового интерфейса Dynatrace Assist

После включения генеративного ИИ Dynatrace Intelligence в вашей среде и настройки разрешений пользователей вы увидите новый значок  под кнопкой **Поиск**  в панели.

1. В Dynatrace выберите  **Dynatrace Assist**.
2. Откроется новое окно с интерфейсом чата.
3. Введите свой вопрос. Для вдохновения см. [примеры](chat-with-davis-copilot/dynatrace-assist-prompts.md "Learn what kind of prompts work well in Dynatrace Assist.").
4. Нажмите **Run** ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") и дождитесь генерации ответа.

   * Вы можете задавать уточняющие вопросы.
   * Каждый ответ содержит список источников, использованных для генерации ответа. Вы можете обратиться к этим [источникам](#sources) для получения дополнительной информации.
   * Диалоги сохраняются автоматически. Их можно переименовать или удалить из списка диалогов.
   * Вы можете отменить генерацию ответа, уточнить запрос и отправить вопрос повторно.
   * Вы можете использовать интерфейс чата поверх любого приложения.

Ответы генерируются на основе ресурсов, связанных с Dynatrace. Если модель не может ответить на ваш вопрос, вы увидите сообщение об ошибке:

* К сожалению, я не могу ответить на этот запрос. Пожалуйста, попробуйте перефразировать его или добавить дополнительный контекст.

### Использование агентных возможностей Dynatrace Assist

При включенном агентном ИИ вы можете попросить **Dynatrace Assist** проанализировать данные и безопасность вашей среды и предоставить аналитические сведения. Примеры см. в разделе [Вопросы о данных вашей среды](chat-with-davis-copilot/dynatrace-assist-prompts.md#assist-ask-about-the-data "Learn what kind of prompts work well in Dynatrace Assist.").

Подробнее о начале работы с агентным **Dynatrace Assist** см. в разделе [Включение агентного ИИ для Dynatrace Assist](copilot-getting-started.md#assist-agentic "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

### Обратная связь

Вы можете оставить обратную связь с помощью встроенного механизма.

Нажмите ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up"), если Dynatrace Assist сгенерировал ответ, который соответствует вашим ожиданиям и правильно интерпретировал ваш запрос.

Нажмите ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down"), если Dynatrace Assist сгенерировал ответ, который не соответствует вашим ожиданиям или неправильно интерпретировал ваш запрос. Пожалуйста, предоставьте дополнительный контекст, чтобы мы могли понять, как улучшить эту функциональность в соответствии с вашими потребностями и ожиданиями.

Ваша обратная связь не используется для автоматического обучения каких-либо моделей. Она рассматривается только командой продукта для мониторинга качества ответов и улучшения основного продукта.

### Источники, используемые для генерации ответов

**Dynatrace Assist** обогащает свои ответы на основе официальных источников Dynatrace, таких как:

* Документация Dynatrace
* [Dynatrace Developer](https://developer.dynatrace.com/)
* [Dynatrace Community](https://community.dynatrace.com/)
* [Dynatrace Hub](https://www.dynatrace.com/hub/)
* [Новости и ресурсы Dynatrace](https://www.dynatrace.com/news/product-news/)
* [Веб-сайт Dynatrace](https://www.dynatrace.com/)

## Концепции

Пройдите следующий процесс, чтобы научиться использовать **Dynatrace Assist**

[01Встроенные стартеры диалогов

* Справочник
* Узнайте, как запускать предопределенные запросы в различных приложениях Dynatrace.](chat-with-davis-copilot/copilot-conv-starters.md)[02Примеры запросов Dynatrace Assist

* Справочник
* Узнайте, какие запросы хорошо работают в Dynatrace Assist.](chat-with-davis-copilot/dynatrace-assist-prompts.md)

## Сценарии использования

Вы можете использовать агентный **Dynatrace Assist** для:

* Задавайте общие вопросы о продукте Dynatrace.
* Используйте инструменты и возможности MCP.
* Выполняйте задачи без необходимости открывать приложение или переходить в другое приложение.
* Комбинируйте инструменты в одном запросе для выполнения нескольких задач.
* Комбинируйте инструменты для выполнения задач и получения ответов на общие вопросы одновременно.

## Связанные темы

* [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](copilot-getting-started.md "Learn how to set up Dynatrace Intelligence agentic and generative AI.")
* [Встроенные стартеры диалогов](chat-with-davis-copilot/copilot-conv-starters.md "Learn how to trigger predefined prompts in various Dynatrace applications.")
* [Часто задаваемые вопросы об агентном и генеративном ИИ Dynatrace Intelligence](../../../common/dynatrace-intelligence/copilot/copilot-faq.md "Learn about frequently asked questions and find your answers.")
* [Dynatrace MCP server](../../../common/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp.md "Learn about the Dynatrace MCP server and how you can connect to it.")
