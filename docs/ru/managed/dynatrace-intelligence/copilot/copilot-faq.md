---
title: Dynatrace Intelligence agentic and generative AI FAQ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-faq
scraped: 2026-03-06T21:34:50.006629
---

# Часто задаваемые вопросы по агентному и генеративному ИИ Dynatrace Intelligence

# Часто задаваемые вопросы по агентному и генеративному ИИ Dynatrace Intelligence

* Latest Dynatrace
* Устранение неполадок
* Чтение: 4 мин
* Обновлено 28 января 2026 г.

Если у вас есть вопросы, связанные с агентным и генеративным ИИ Dynatrace Intelligence, начните с проверки, не были ли они уже рассмотрены в разделе часто задаваемых вопросов.

## Доступность агентного и генеративного ИИ

Каковы предварительные требования для использования агентного и генеративного ИИ Dynatrace Intelligence?

* Ваша среда должна быть SaaS и работать на последней версии Dynatrace.
* Вы должны включить агентный и генеративный ИИ Dynatrace Intelligence в вашей среде.
* Вы должны назначить разрешения соответствующим пользователям или группам пользователей.

Подробности см. в разделе [Начало работы с генеративным ИИ](../../../dynatrace-intelligence/copilot/copilot-getting-started.md "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

Доступен ли агентный и генеративный ИИ Dynatrace Intelligence для SaaS и Managed?

Агентный и генеративный ИИ Dynatrace Intelligence будет доступен для всех клиентов Dynatrace SaaS, использующих последнюю версию Dynatrace. Поддерживаются учетные записи как AWS, так и Azure.

Агентный и генеративный ИИ Dynatrace Intelligence недоступен для клиентов Dynatrace Managed.

Нужна ли моей учетной записи подписка DPS для использования агентного и генеративного ИИ Dynatrace Intelligence?

Нет. Агентный и генеративный ИИ Dynatrace Intelligence доступен в любой среде SaaS, работающей на последней версии Dynatrace, независимо от вашей модели лицензирования.

Будет ли агентный и генеративный ИИ Dynatrace Intelligence лицензироваться?

Нет. С нашей текущей функциональностью генеративного ИИ не связано лицензирование. Однако, несмотря на то что агентный и генеративный ИИ Dynatrace Intelligence не тарифицируется, все запросы, выполняемые генеративным ИИ, подлежат потреблению лицензии в соответствии с вашим существующим лицензионным соглашением. Если вас беспокоит стоимость автоматического выполнения сгенерированных запросов, вы можете выбрать генерацию только DQL без его выполнения. Подробнее см. в разделе [Запросы на естественном языке](../../../dynatrace-intelligence/copilot/quick-analysis-copilot-dql.md "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

Как агентный и генеративный ИИ Dynatrace Intelligence повлияет на потребление моей лицензии?

Сам по себе агентный и генеративный ИИ Dynatrace Intelligence не влияет на потребление вашей лицензии. Однако все запросы, выполняемые генеративным ИИ, подлежат потреблению лицензии в соответствии с вашим существующим лицензионным соглашением. Подробнее см. в разделе [Будет ли агентный и генеративный ИИ Dynatrace Intelligence лицензироваться?](../../../../common/dynatrace-intelligence/copilot/copilot-faq.md#davis-copilot-license "Learn about frequently asked questions and find your answers.").

## Агентный и генеративный ИИ Dynatrace Intelligence и данные клиентов

Используются ли мои данные для обучения генеративного ИИ Dynatrace Intelligence?

Нет. Данные клиентов и запросы клиентов не используются для обучения. Генеративный ИИ Dynatrace Intelligence основан на подходе [генерации с дополнением извлечением](../../../dynatrace-intelligence/copilot/copilot-overview.md#copilot-what-to-expect "Learn about data security and other aspects of Dynatrace Intelligence agentic and generative AI.") (RAG), что означает, что данные и дополнительный контекст используются только для обогащения запросов. Модель на этом не обучается. Данные клиентов не используются для автоматической тонкой настройки, обучения или улучшения каких-либо моделей или сервисов ни со стороны Dynatrace, ни со стороны корпоративных поставщиков, размещающих LLM.

Агентный **Dynatrace Assist** передает некоторую дополнительную информацию, такую как результаты вызовов инструментов, корпоративным поставщикам, размещающим LLM, на которых основан агентный и генеративный ИИ Dynatrace. Подробнее о третьих сторонах см. в разделе [Используются ли мои данные для обучения генеративного ИИ Dynatrace Intelligence?](../../../../common/dynatrace-intelligence/copilot/copilot-faq.md#copilot-training-on-data "Learn about frequently asked questions and find your answers.").

Используются ли мои данные для обучения модели агентного и генеративного ИИ Dynatrace Intelligence для других клиентов?

Нет, данные клиентов вообще не используются для обучения агентного и генеративного ИИ Dynatrace Intelligence. Нет риска передачи данных клиентов между средами.

Собирает ли генеративный ИИ Dynatrace Intelligence мои данные?

Для базовой функциональности генеративного ИИ Dynatrace Intelligence доступ к данным клиентов отсутствует. Генерация общих запросов опирается только на общедоступные знания (семантический словарь, документацию DQL и т. д.) и обширный курируемый набор данных, управляемый Dynatrace. Единственный клиентский контекст, к которому имеет доступ генеративный ИИ, -- это запрос пользователя.

Однако, если вы включите запросы с учетом среды, генеративный ИИ Dynatrace Intelligence создаст семантический индекс, который хранится на платформе Dynatrace. Создание семантического индекса позволяет генеративному ИИ формировать более точные запросы, идентифицирующие и ссылающиеся на соответствующие сущности, события и метрики. Это позволяет проводить более глубокий и сложный анализ данных, задавая вопросы о специфике данных в вашей среде. Учитывайте следующее:

* Вы полностью контролируете, какие данные в Grail семантически индексируются генеративным ИИ Dynatrace Intelligence на уровне объектов данных и бакетов Grail.
* Даже при включенных запросах с учетом среды ваши данные по-прежнему хранятся только в вашей среде, а фрагменты данных, используемые для обогащения ваших запросов, не используются для обучения или тонкой настройки модели.

Соблюдает ли агентный и генеративный ИИ Dynatrace Intelligence разрешения пользователей?

Да. Агентный и генеративный ИИ Dynatrace Intelligence соблюдает привилегии пользователей и может предоставлять разные ответы разным пользователям в зависимости от их прав доступа.

## Использование агентного и генеративного ИИ

Где можно использовать генеративный ИИ Dynatrace Intelligence?

Функциональность генеративного ИИ Dynatrace Intelligence в настоящее время позволяет проводить быстрый анализ данных в Notebooks и Dashboards, генерируя DQL на основе ваших запросов на естественном языке.

Как я могу оставить отзыв?

Вы можете оставить отзыв непосредственно в приложениях Notebooks или Dashboards. Чтобы узнать, как оставить отзыв через Dashboards и Notebooks, см. [Запросы на естественном языке](../../../dynatrace-intelligence/copilot/quick-analysis-copilot-dql.md "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

Может ли агентный и генеративный ИИ Dynatrace Intelligence обрабатывать вопросы на иностранных языках?

Да. Агентный и генеративный ИИ Dynatrace Intelligence отвечает на команды и вопросы на языках, отличных от английского.

Как я могу отслеживать и контролировать внедрение агентного и генеративного ИИ Dynatrace Intelligence в моей среде?

У нас есть готовый дашборд для самостоятельной оценки внедрения, который предоставляет полный обзор:

* Активные пользователи
* Производительность
* Внедрение функций
* Процент успешных взаимодействий
* Детали запросов
* Детали ошибок ответов
* Выполнение запросов
* Отзывы пользователей.

Вы или ваши администраторы можете использовать этот дашборд для лучшего понимания того, какие функции генеративного ИИ используются, для просмотра запросов пользователей и ответов ИИ, а также для получения информации об удовлетворенности пользователей функциями. Дашборд можно найти под названием **Generative AI feature adoption**.

Все взаимодействия с генеративным ИИ Dynatrace Intelligence записываются в Grail как `dt.system.events` и требуют соответствующих разрешений для извлечения и просмотра таких событий.

## Связанные темы

* [Обзор агентного и генеративного ИИ Dynatrace Intelligence](../../../dynatrace-intelligence/copilot/copilot-overview.md "Learn about data security and other aspects of Dynatrace Intelligence agentic and generative AI.")
* [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](../../../dynatrace-intelligence/copilot/copilot-getting-started.md "Learn how to set up Dynatrace Intelligence agentic and generative AI.")
* [Запросы на естественном языке](../../../dynatrace-intelligence/copilot/quick-analysis-copilot-dql.md "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Агентный и генеративный ИИ Dynatrace Intelligence -- советы по написанию лучших запросов](../../../dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips.md "Learn best practices for writing more accurate prompts.")
* [Примеры быстрого анализа с генеративным ИИ](../../../dynatrace-intelligence/use-cases/copilot-examples.md "Learn more about what kind of prompts work well in Dynatrace Intelligence agentic and generative AI.")
* [Конфиденциальность и безопасность данных агентного и генеративного ИИ Dynatrace Intelligence](../../../dynatrace-intelligence/copilot/copilot-data-privacy.md "Learn about Dynatrace Intelligence agentic and generative AI data privacy and security policy.")