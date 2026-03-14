---
title: Автоматизация устранения уязвимостей с Atlassian Rovo Dev и Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/ai-remediation-atlassian-rovo-dev
scraped: 2026-03-01T21:24:59.058380
---

# Автоматизация устранения уязвимостей с помощью Atlassian Rovo Dev и Dynatrace


* Latest Dynatrace
* Tutorial
* Опубликовано 29 января 2026 г.
* Preview

## Обзор

Dynatrace помогает командам разработчиков сосредоточиться на главном, верифицируя уязвимости с учётом контекста среды выполнения и оптимизируя их устранение через [Atlassian Rovo Dev](https://www.atlassian.com/software/rovo-dev). Этот сценарий демонстрирует, как определять приоритеты и устранять уязвимости, влияющие на продуктовые приложения, с бесшовной интеграцией с Jira для управления задачами и Bitbucket для создания pull-запросов. Он поддерживает два пути реализации в зависимости от того, где вы хотите проводить сортировку и запускать исправления -- оба основаны на Dynatrace MCP и интеграциях Atlassian.

## Проблема

Сканеры уязвимостей обнаруживают сотни высоких и критических CVE в зависимостях приложений, но им не хватает контекста среды выполнения. Не зная, какие библиотеки фактически загружены и какие пути кода выполняются в продакшене, разработчики сталкиваются с трудным выбором: пытаться исправить каждую уязвимость -- тратя ценное время на проблемы, не влияющие на продакшен, -- или расставлять приоритеты на основе догадок, рискуя упустить уязвимости, которые действительно влияют на критически важные для бизнеса сервисы.

Отсутствие контекста порождает усталость от оповещений и замедляет устранение. Командам нужен способ сосредоточиться на уязвимостях, подтверждённо влияющих на продакшен, при этом с уверенностью снижая приоритет тех, которые не представляют реальной угрозы.

## Решение

Dynatrace интегрируется с Atlassian Rovo Dev через Model Context Protocol (MCP), обогащая опыт разработчика контекстом среды выполнения и валидацией [Runtime Vulnerability Analytics (RVA)](../application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних и собственных библиотек, отслеживание прогресса устранения и создание правил мониторинга."). Это позволяет Rovo Dev предпринимать целенаправленные действия прямо из IDE:

* Подтверждённые уязвимости имеют приоритет для устранения: Rovo Dev запрашивает у Dynatrace уязвимости, валидированные средой выполнения, обеспечивая фокус разработчиков на проблемах, действительно влияющих на продакшен.
* Интеллектуальное управление задачами: Rovo Dev создаёт задачи в Jira для подтверждённых находок, автоматически проверяя наличие дубликатов перед созданием, и обновляет задачи по мере устранения.
* Сквозной рабочий процесс устранения: от обнаружения уязвимости до исправления кода, создания pull-запроса и обновления задачи -- всё без выхода из IDE.

Это снижает шум и трудозатраты разработчиков, обеспечивая устранение только релевантных уязвимостей при сохранении полной прослеживаемости в Jira.

Вы можете реализовать это решение двумя способами в зависимости от того, где вы хотите сортировать уязвимости и запускать устранение:

* [**Рабочий процесс на основе IDE/CLI**](#ide-cli-workflow): использует [Rovo Dev в IDE](https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-the-ide/) или [Rovo Dev CLI](https://support.atlassian.com/rovo/docs/use-rovo-dev-cli/) как основную точку взаимодействия, подключённую к серверу Dynatrace MCP. Разработчики взаимодействуют с Rovo Dev для запроса уязвимостей, применения исправлений, создания pull-запросов в Bitbucket и управления задачами в Jira.
* [**Рабочий процесс, управляемый Dynatrace**](#dynatrace-workflow): использует [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../analyze-explore-automate/workflows.md "Автоматизация ИТ-процессов с помощью Dynatrace Workflows -- реакция на события, планирование задач и подключение сервисов.") в качестве триггера и механизма обработки, с автоматическим созданием задач в Jira. Затем разработчики используют Rovo Dev для работы с задачами, применения исправлений и завершения цикла устранения.

## Предварительные требования

Ниже приведены требования для [Atlassian](#atlassian) и [Dynatrace](#dt).

### Atlassian

* Иметь доступ к экземпляру Jira Cloud вашей организации.
* [Установить расширение Atlassian](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-vs-code/) (VS Code, JetBrains IDEs) в вашу IDE.
* [Установить Atlassian Rovo Dev](https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-the-ide/) в вашу IDE.
* [Создать API-токен Atlassian для аутентификации](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) со следующими правами проекта:

  + `Browse projects`
  + `Create issues`
  + `Edit issues`
  + `Transition issues`
  + `Add comments`
  + `Link issues`
* Настроить Bitbucket или любой другой Git-репозиторий с правами записи в вашей IDE (необходимо для того, чтобы Rovo Dev мог коммитить изменения кода и создавать pull-запросы от вашего имени). Убедитесь, что ИИ-агент имеет права на отправку в ветки и создание pull-запросов.
* [Настроить Rovo Dev](https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-the-ide/#Authentication-for-Rovo-Dev) с интеграциями Jira и Bitbucket.

### Dynatrace

* Настроить мониторинг с помощью [Dynatrace OneAgent](../../platform/oneagent.md "Узнайте о возможностях мониторинга OneAgent.") для продуктовых сервисов.
* [Включить Runtime Vulnerability Analytics](../application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних и собственных библиотек, отслеживание прогресса устранения и создание правил мониторинга.").
* [Создать токен платформы Dynatrace](../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md "Создание персонализированных токенов платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.") со следующими правами:

  + `mcp-gateway:servers:invoke`
  + `mcp-gateway:servers:read`
  + `davis-copilot:conversations:execute`
  + `davis-copilot:nl2dql:execute`
  + `davis-copilot:dql2nl:execute`
  + `storage:entities:read`
  + `storage:smartscape:read`
  + `storage:buckets:read`
  + `storage:bucket-definitions:read`
  + `storage:security.events:read`

## Рабочий процесс на основе IDE/CLI

В этом сценарии разработчик взаимодействует с Rovo Dev в своей IDE для запроса уязвимостей у Dynatrace, применения исправлений и управления всем жизненным циклом устранения через Jira и Bitbucket.

### Как это работает (рабочий процесс на основе IDE)

1. Dynatrace обнаруживает уязвимости в продуктовых приложениях через Runtime Vulnerability Analytics.
2. Разработчик открывает свою IDE с затронутым репозиторием и вызывает Rovo Dev.
3. Разработчик запрашивает у Rovo Dev уязвимости для соответствующего сервиса (например, "List critical vulnerabilities for the frontend service"). Rovo Dev использует сервер Dynatrace MCP для получения уязвимостей, валидированных средой выполнения.
4. Разработчик выбирает уязвимость и запрашивает подробную информацию у Dynatrace.
5. Rovo Dev проверяет Jira на наличие существующих задач; если их нет, создаёт новую задачу с деталями уязвимости.
6. Разработчик поручает Rovo Dev применить исправление на основе контекста задачи Jira.
7. Rovo Dev анализирует кодовую базу, применяет необходимые изменения и запускает тесты.
8. Rovo Dev создаёт pull-запрос в Bitbucket с исправлением и связывает его с задачей Jira.
9. Задача Jira обновляется ссылкой на pull-запрос и переводится в статус "In Review".
10. Разработчики проверяют и объединяют pull-запрос.

### Начало работы (рабочий процесс на основе IDE)

Для начала работы выполните следующие шаги.

1. Настройка сервера Dynatrace MCP

1. [Запросите доступ к серверу Dynatrace MCP](../../../common/whats-new/preview-releases.md#mcp-server "Узнайте о наших Preview-релизах и как принять в них участие.").
2. Настройте сервер MCP в настройках Rovo Dev вашей IDE, как показано ниже, убедившись, что вы заменили

   * `<DYNATRACE_TENANT>` на вашу среду, например `mytenant.apps.dynatrace.com`
   * `<DYNATRACE_PLATFORM_TOKEN>` на токен Dynatrace, созданный в разделе предварительных требований

```
{


"mcpServers": {


"dynatrace": {


"transport": "sse",


"url": "https://<DYNATRACE_TENANT>/platform/mcp-gateway/sse",


"headers": {


"Authorization": "Api-Token <DYNATRACE_PLATFORM_TOKEN>"


}


}


}


}
```

2. Добавление пользовательских инструкций для агента Dynatrace

Вы можете предоставить пользовательские инструкции для управления Rovo Dev при взаимодействии с Dynatrace. Скачайте [файл `instructions.md`](https://dt-url.net/cp2300s) и настройте его одним из следующих способов:

* **Вариант 1**: [Файл глобальной памяти](https://support.atlassian.com/rovo/docs/set-custom-instructions-for-code-reviews/)

  1. В Rovo Dev нажмите меню (три точки) и выберите Open Global Memory file.
  2. Добавьте содержимое файла instructions.md для предоставления инструкций, специфичных для Dynatrace, во всех ваших проектах.
* **Вариант 2**: [Инструкции на уровне репозитория](https://support.atlassian.com/rovo/docs/use-memory-in-rovo-dev-cli/)

  1. Создайте файл `AGENTS.md` в корне вашего репозитория (или папки в контексте).
  2. Добавьте содержимое файла `instructions.md` для предоставления инструкций агента Dynatrace, специфичных для проекта.

Файл инструкций содержит руководство по запросу уязвимостей, интерпретации событий безопасности Dynatrace и лучшим практикам устранения.

3. Настройка интеграций Atlassian

1. Убедитесь, что Rovo Dev подключён к вашему экземпляру Jira Cloud. Следуйте [руководству по настройке Rovo Dev](https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-the-ide/) для аутентификации.
2. Подключите Rovo Dev к вашему репозиторию Bitbucket для создания pull-запросов. Для аутентификации можно использовать [расширение Atlassian VSC](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-vs-code/).
3. Клонируйте затронутый репозиторий локально и откройте его в вашей IDE.

4. Взаимодействие с Rovo Dev

Используйте запросы на естественном языке для управления рабочим процессом:

* Запрос уязвимостей:

  ```
  List all critical vulnerabilities from Dynatrace
  ```
* Получение деталей уязвимости:

  ```
  Get details for [this] vulnerability from Dynatrace
  ```
* Создание задачи Jira (с проверкой дубликатов):

  ```
  Create a Jira ticket for this vulnerability, but only if there isn't an existing ticket already
  ```
* Применение исправлений на основе контекста задачи:

  ```
  Based on the Jira ticket context, analyze my codebase and apply the necessary fixes for this vulnerability
  ```
* Создание pull-запроса:

  ```
  Create a pull request for this fix to the main branch
  ```
* Обновление задачи Jira:

  ```
  Update the Jira ticket with the PR link and move it to "In Review"
  ```

## Рабочий процесс, управляемый Dynatrace

Этот сценарий использует [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../analyze-explore-automate/workflows.md "Автоматизация ИТ-процессов с помощью Dynatrace Workflows -- реакция на события, планирование задач и подключение сервисов.") для автоматической сортировки уязвимостей и создания задач Jira, при этом Rovo Dev обрабатывает фазу устранения.

### Как это работает (сортировка, управляемая Dynatrace)

1. Dynatrace обнаруживает уязвимости через Runtime Vulnerability Analytics.
2. Рабочий процесс Dynatrace выполняется по настроенному расписанию для выявления новых критических уязвимостей, подтверждённых средой выполнения.
3. Рабочий процесс использует [Davis CoPilot](../../dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью рабочих процессов.") для обобщения результатов и автоматически создаёт задачи Jira для подтверждённых уязвимостей.
4. Разработчик получает уведомление о задаче Jira и открывает затронутый репозиторий в своей IDE.
5. Разработчик загружает задачу Jira в качестве контекста, выбирая её в расширении Atlassian, предоставляя полные детали уязвимости.
6. При необходимости разработчик может получить дополнительный контекст наблюдаемости через настроенный сервер Dynatrace MCP.
7. Разработчик поручает Rovo Dev применить исправление, создать pull-запрос в Bitbucket и обновить задачу.
8. Разработчики проверяют и объединяют pull-запрос.

### Начало работы (рабочий процесс, управляемый Dynatrace)

Для начала работы выполните следующие шаги.

1. Развёртывание рабочего процесса Dynatrace

Скачайте и разверните [рабочий процесс Dynatrace](https://dt-url.net/fa036fq).

2. Настройка Rovo Dev

1. Убедитесь, что Rovo Dev подключён к вашему экземпляру Jira Cloud. Следуйте [руководству по настройке Rovo Dev](https://support.atlassian.com/rovo/docs/work-with-rovo-dev-in-the-ide/) для аутентификации.
2. Подключите Rovo Dev к вашему репозиторию Bitbucket для создания pull-запросов. Для аутентификации можно использовать [расширение Atlassian VSC](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-vs-code/).
3. Клонируйте затронутый репозиторий локально и откройте его в вашей IDE.

3. Устранение на основе контекста Jira

Когда задача Jira назначена:

1. Откройте затронутый репозиторий в вашей IDE.
2. Загрузите задачу Jira в качестве контекста в Rovo Dev.

   ![rovo-dev](https://dt-cdn.net/images/addjiratickettocontext-53a92840c4.gif)
3. Используйте естественный язык для управления устранением:

   ```
   Based on the Jira ticket context, apply the fix for this vulnerability, create a PR, and update the ticket
   ```

## Дополнительные сценарии использования

[Сервер Dynatrace MCP](../../../common/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp.md "Узнайте о сервере Dynatrace MCP и о том, как к нему подключиться.") предоставляет дополнительные инструменты, которые Rovo Dev может использовать, обеспечивая дополнительные сценарии использования, такие как:

* **Реагирование на инциденты**: запрос активных проблем у Dynatrace, получение анализа первопричин и создание задач инцидентов в Jira с полным контекстом наблюдаемости.
* **Оптимизация производительности**: получение данных о медленных транзакциях, аналитики по запросам к базам данных и зависимостях сервисов для информирования усилий по оптимизации.
* **Планирование ёмкости**: использование прогнозирования временных рядов для предсказания утилизации ресурсов и создание проактивных задач по ёмкости.
* **Контекст наблюдаемости для существующих задач**: для любой задачи Jira запрос логов, трассировок, метрик и взаимосвязей сущностей у Dynatrace для ускорения устранения неполадок.

## Связанные темы

* [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Runtime Vulnerability Analytics](../application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних и собственных библиотек, отслеживание прогресса устранения и создание правил мониторинга.")
* [Workflows](../../analyze-explore-automate/workflows.md "Автоматизация ИТ-процессов с помощью Dynatrace Workflows -- реакция на события, планирование задач и подключение сервисов.")
* [Приложение Dynatrace Intelligence (Preview)](../../dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью рабочих процессов.")
