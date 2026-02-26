---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-02-26T21:27:38.735193
---

# Dynatrace Assist

# Dynatrace Assist

* Latest Dynatrace
* App
* 2-min read
* Updated on Feb 11, 2026

**Dynatrace Assist** позволяет вам общаться с Dynatrace Intelligence и задавать вопросы о данных в вашей среде, а также общие вопросы, чтобы помочь вам с настройкой Dynatrace и пониманием наших основных концепций.

### Права доступа

В следующей таблице описаны необходимые права доступа.

document:documents:write

хранить разговоры в хранилище документов

document:documents:read

читать разговоры из хранилища документов

document:documents:delete

удалять разговоры из хранилища документов

davis-copilot:conversations:execute

использовать функцию разговора с копилотом

hub:catalog:read

чтение каталога для отображения приложения, которое запустило разговор

davis-copilot:nl2dql:execute

использовать функцию агентного копилота

davis-copilot:dql2nl:execute

использовать функцию агентного копилота

mcp-gateway:servers:invoke

использовать функцию агентного копилота

mcp-gateway:servers:read

использовать функцию агентного копилота

davis:analyzers:read

использовать функцию агентного копилота

Чтобы использовать **Dynatrace Assist** с функциями генеративного ИИ, вам необходимы только следующие права доступа:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

Остальные права доступа в таблице необходимы только в том случае, если вы хотите использовать полный объем возможностей агентного Dynatrace Assist. Для получения дополнительной информации см. [Права доступа агентного Dynatrace Assist](#assist-agentic-permissions).

Для получения дополнительной информации см. [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

## Начало работы

![Начните работу быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Попросите Dynatrace Assist суммировать все открытые проблемы, чтобы получить быстрый обзор вашей среды.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Попросите Dynatrace Assist объяснить ваши журналы, чтобы быстро получить информацию, потенциальное влияние, вероятные причины и рекомендуемые следующие шаги.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Получите помощь в выявлении и исправлении уязвимостей, таких как SQL-инъекции.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 из 4Начните работу быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.

### Использование интерфейса разговора Dynatrace Assist

После включения Dynatrace Intelligence генеративного ИИ в вашей среде и настройки прав доступа пользователя, вы должны увидеть новую иконку ниже **Поиск** в доке.

1. В Dynatrace, выберите **Dynatrace Assist**.
2. Откроется новое окно с интерфейсом разговора.
3. Введите ваш вопрос. См. [Примеры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.") для вдохновения.
4. Выберите **Выполнить** ![Выполнить](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Выполнить") и подождите, пока ответ будет сгенерирован.

* Вы можете задавать дополнительные вопросы.
* Каждый ответ содержит список источников, которые были получены для генерации ответа. Вы можете обратиться к этим [источникам](#sources) для получения дополнительной информации.
* Разговоры сохраняются автоматически. Их можно переименовать или удалить из списка разговоров.
* Вы можете отменить генерацию ответа, уточнить вашу подсказку и затем отправить вопрос снова.
* Вы можете использовать интерфейс разговора поверх любого приложения.

Ответы генерируются на основе ресурсов, связанных с Dynatrace. Если модель не может ответить на ваш вопрос, вы увидите сообщение об ошибке:

* Извините, но я не могу ответить на этот запрос. Пожалуйста, попробуйте перефразировать его или добавить дополнительный контекст.

### Использование агентного Dynatrace Assist

**Dynatrace Assist** позволяет вам использовать Dynatrace агентный ИИ и [инструменты и возможности MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.") для доступа и анализа данных вашей среды и использования их для выполнения задач (таких как перечисление проблем или генерация и выполнение запросов DQL) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** делится некоторой дополнительной информацией, такой как результаты вызовов инструментов, с предприятиями, которые размещают LLM, на основе которых построены Dynatrace агентный и генеративный ИИ. Для получения дополнительной информации о третьих сторонах см. [Используется ли моя информация для обучения Dynatrace Intelligence генеративного ИИ?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Узнайте о часто задаваемых вопросах и найдите ответы.").

С включенным агентным ИИ вы можете попросить **Dynatrace Assist** проанализировать и предоставить информацию о данных и безопасности вашей среды. Для примеров см. [Спросите о данных в вашей среде](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts#assist-ask-about-the-data "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.").

#### Права доступа агентного Dynatrace Assist

**Dynatrace Assist** уважает ваши права доступа пользователя. Это означает, что все агентные вызовы **Dynatrace Assist** выполняются в рамках ваших прав доступа пользователя, и результаты не будут включать ничего вне этого.

Чтобы использовать агентный **Dynatrace Assist**, вам необходимо:

* Иметь достаточные права доступа.
* Включить агентный ИИ для **Dynatrace Assist**. Чтобы включить агентный ИИ:

  1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** > **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
  2. Убедитесь, что **Включить генеративный ИИ** включен.
  3. Включите **Включить агентный ИИ**.

Агентный **Dynatrace Assist** может быть недоступен для вас, если вы не соответствуете необходимым условиям, указанным выше, или если вы доступ к **Dynatrace Assist** из [Встроенных стартовых точек разговора](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace.").

Вам также потребуются дополнительные права доступа для вызова агентных инструментов. Для списка инструментов и прав доступа, необходимых для них, см. [Инструменты MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.").

#### Маскирование ПII

Агентный **Dynatrace Assist** не предоставляет никакого маскирования ПII. Чтобы защитить ваши данные, когда **Dynatrace Assist** обнаруживает ПII в подсказке пользователя, запрос автоматически блокируется и подсказка не отправляется в LLM для обработки.

#### Вызов нескольких инструментов

При взаимодействии с **Dynatrace Assist** в агентном режиме **Assist** может вызвать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** вызвать более 10 инструментов одновременно, он не сможет выполнить взаимодействие.

### Оставьте отзыв

Вы можете оставить отзыв, используя встроенный механизм отзыва.

Выберите ![Большой палец вверх](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Большой палец вверх") если Dynatrace Assist сгенерировал ответ, который соответствует вашим ожиданиям и правильно интерпретировал вашу подсказку.

Выберите ![Большой палец вниз](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Большой палец вниз") если Dynatrace Assist сгенерировал ответ, который не соответствует вашим ожиданиям или неправильно интерпретировал вашу подсказку. Пожалуйста, предоставьте дополнительный контекст, чтобы мы могли понять, как мы можем улучшить эту функциональность, чтобы она соответствовала вашим потребностям и ожиданиям.

Ваш отзыв не используется для автоматического обучения моделей. Он рассматривается только командой продукта для мониторинга качества ответов и улучшения основного предложения продукта.

### Источники, использованные для генерации ответов

**Dynatrace Assist** обогащает свои ответы на основе официальных источников Dynatrace, таких как:

* Документация Dynatrace
* [Разработчик Dynatrace](https://developer.dynatrace.com/)
* [Сообщество Dynatrace](https://community.dynatrace.com/)
* [Хаб Dynatrace](https://www.dynatrace.com/hub/)
* [Новости и ресурсы Dynatrace](https://www.dynatrace.com/news/product-news/)
* [Веб-сайт Dynatrace](https://www.dynatrace.com/)

## Концепции

Пройдите следующий процесс, чтобы научиться использовать **Dynatrace Assist**

[01Встроенные стартовые точки разговора

* Справка
* Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)[02Примеры подсказок Dynatrace Assist

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



* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Embedded conversation starters](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Learn how to trigger predefined prompts in various Dynatrace applications.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Dynatrace MCP server](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp "Learn about the Dynatrace MCP server and how you can connect to it.")