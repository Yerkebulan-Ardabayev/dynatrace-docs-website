---
title: Автоматизация устранения уязвимостей с GitHub Copilot и Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/ai-remediation-github-copilot
scraped: 2026-03-06T21:30:19.746089
---

# Автоматизация устранения уязвимостей с помощью GitHub Copilot и Dynatrace


* Latest Dynatrace
* Preview

## Обзор

Не каждую проблему в коде нужно исправлять. Dynatrace помогает командам разработки сосредоточиться на том, что действительно важно, проверяя уязвимости с учётом контекста выполнения и упрощая устранение через [GitHub Copilot](https://docs.github.com/en/copilot).
Этот сценарий демонстрирует, как приоритизировать и устранять уязвимости, влияющие на производственные приложения. Он поддерживает два пути реализации в зависимости от того, где вы хотите проводить сортировку и инициировать исправления — оба работают на основе интеграции Dynatrace и GitHub.

## Проблема

В сложных кодовых базах количество обнаруженных уязвимостей может быть огромным. Хотя ИИ-агенты, такие как GitHub Copilot, могут помогать с автоматическим устранением, человеческая проверка и утверждение по-прежнему необходимы. Изменения кода также могут привести к нарушению работы, что увеличивает накладные расходы на разработку. Это делает эффективную приоритизацию и сортировку уязвимостей с поддержкой богатого контекста критически важной для поддержания скорости и стабильности разработки.

## Решение

Dynatrace интегрируется с GitHub, обогащая [оповещения Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) контекстом выполнения и валидацией Runtime Vulnerability Analytics (RVA). Это позволяет GitHub Copilot выполнять целевые действия:

* **Подтверждённые уязвимости исправляются автоматически**: GitHub Copilot открывает pull request с безопасным исправлением для каждой уязвимости, подтверждённой Dynatrace.

  Пример

  ![Агент GitHub Copilot применяет исправления](https://dt-cdn.net/images/30603523-539a-49f2-a8ea-bdecf457877f-1056-0f4f097777.png)
* **Неподтверждённые уязвимости отклоняются с указанием причины**: если Dynatrace проверил уязвимость во время выполнения и уязвимая библиотека не загружена или уязвимая функция не используется, уязвимость не подтверждается, и GitHub Copilot отклоняет оповещение с пояснением причины.

  Пример

  ![Агент GitHub Copilot автоматически отклоняет неподтверждённые уязвимости](https://dt-cdn.net/images/5ef668ff-9db4-4027-a740-3c9bbe7cb836-1061-4c1d7cd672.png)

Это снижает информационный шум и трудозатраты разработчиков, обеспечивая устранение только релевантных уязвимостей.

Вы можете реализовать это решение двумя способами в зависимости от того, где вы хотите проводить сортировку уязвимостей и инициировать устранение:

* [**Рабочий процесс на основе GitHub**](#github-based): использует Dynatrace MCP Server, интегрированный с [агентом GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) или в качестве пользовательского агента безопасности Dynatrace [custom agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents), запускаемого через [рабочие процессы GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows).
* [**Рабочий процесс на основе Dynatrace**](#dynatrace-driven): использует [Dynatrace ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../analyze-explore-automate/workflows.md "Автоматизация IT-процессов с помощью Dynatrace Workflows.") в качестве триггера и механизма обработки, с [генеративным ИИ](https://docs.github.com/en/copilot) в качестве инструмента анализа на основе ИИ.

## Рабочий процесс на основе GitHub

Этот сценарий использует рабочий процесс GitHub Actions для обнаружения новых критических уязвимостей и запуска GitHub Copilot для исправления только тех, которые подтверждены Dynatrace.

### Как это работает (рабочий процесс на основе GitHub)

![Рабочий процесс на основе GitHub — как это работает](https://dt-cdn.net/images/image-60-2043-f1d3d4c1d0.png)

1. [GitHub Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide) обнаруживает уязвимости в зависимостях кода.
2. Рабочий процесс GitHub запускается с настроенной периодичностью для проверки новых критических уязвимостей.
3. При обнаружении новых уязвимостей создаётся GitHub issue и назначается GitHub Copilot.
4. GitHub Copilot проверяет каждую уязвимость, запрашивая контекст выполнения и подтверждение RVA через Dynatrace MCP.
5. Подтверждённые уязвимости устраняются в pull request; неподтверждённые отклоняются в Dependabot с указанием причины.
6. Разработчики проверяют и сливают pull request.

### Начало работы (рабочий процесс на основе GitHub)

Для начала выполните следующие шаги.

1. Настройка Dynatrace

* Настройте мониторинг с помощью Dynatrace OneAgent для производственных сервисов.
* [Включите Runtime Vulnerability Analytics](../application-security/vulnerability-analytics.md#start "Мониторинг, визуализация, анализ и устранение уязвимостей.").
* Создайте токен платформы Dynatrace с необходимыми разрешениями для доступа к серверу MCP и запросов к различным типам событий.

  1. Список разрешений

  + `mcp-gateway:servers:invoke`
  + `mcp-gateway:servers:read`
  + `davis-copilot:conversations:execute`
  + `davis-copilot:nl2dql:execute`
  + `davis-copilot:dql2nl:execute`
  + `davis-copilot:document-search:execute`
  + `storage:entities:read`
  + `storage:smartscape:read`
  + `storage:buckets:read`
  + `storage:bucket-definitions:read`
  + `storage:security.events:read`
* [Запросите доступ к Dynatrace MCP Server](../../../common/whats-new/preview-releases.md#mcp-server "Узнайте о Preview-релизах и способах участия в них.").

2. Подготовка репозитория GitHub

1. [Включите Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository). Это обеспечит обнаружение уязвимостей в зависимостях и создание оповещений.
2. [Сгенерируйте fine-grained personal access token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) с необходимыми разрешениями.

   1. Список разрешений

   * **Read**:

     + `Variables`
     + `Administration`
     + `Dependabot secrets`
     + `Environments`
     + `Metadata`
     + `Webhooks`
     + `Secrets`
   * **Read and write**:

     + `Dependabot alerts`
     + `Actions`
     + `Code scanning alerts`
     + `Custom properties`
     + `Issues`
     + `Pull requests`
     + `Workflows`
     + `Contents`
3. Сохраните PAT, созданный на шаге 2, [как секрет GitHub для среды Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment#setting-environment-variables-in-copilots-environment) с именем `COPILOT_SPONSOR_PAT`. Этот секрет предоставляется агенту GitHub Copilot в качестве переменной среды, позволяя ему аутентифицироваться и выполнять действия в вашем репозитории от вашего имени.
4. [Назначьте лицензию Copilot пользователю-спонсору](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access).

3. Подключение GitHub Copilot к Dynatrace

Для подключения GitHub Copilot к Dynatrace MCP Server:

1. [Настройте Dynatrace MCP Server в вашем репозитории GitHub](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).
2. Сохраните токен платформы Dynatrace как секрет GitHub для среды Copilot с именем `COPILOT_MCP_DT_API_TOKEN`.
3. В репозитории GitHub перейдите в **Settings** > **Copilot** > **Agents**.
4. Добавьте конфигурацию MCP-сервера следующего вида:

   ```
   {
   "mcpServers":
   {
   "dynatrace": {
   "type": "http",
   "url": "https://pia1134d.dev.apps.dynatracelabs.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp",
   "headers": {
   "Authorization": "Bearer $COPILOT_MCP_DT_API_TOKEN"
   },
   "tools": ["*"]
   }
   }
   }
   ```

   Убедитесь, что вы заменили `your-tenant-id` на идентификатор вашей среды Dynatrace.

Для справки см. [Расширение агента GitHub Copilot с помощью Model Context Protocol (MCP)](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).

4. Добавление инструкций для GitHub Copilot

Чтобы направить агента GitHub Copilot по процедуре проверки с Dynatrace, а также предоставить необходимые знания DQL для успешного взаимодействия с Dynatrace MCP, у вас есть два варианта:

* **Направьте агента GitHub Copilot через глобальный файл инструкций**: скачайте файл [`copilot-instructions.md`](https://dt-url.net/ug032yv) и добавьте его в `.github/`. Инструкции см. в [Добавление пользовательских инструкций для репозитория GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).
* **Определите пользовательского агента Dynatrace для GitHub Copilot**: скачайте файл [`dynatrace-security-agent.md`](https://dt-url.net/8r032d2) и добавьте его в `.github/agents`.

5. Настройка рабочего процесса GitHub

Скачайте [`dependabot-alerts-processing.yml`](https://dt-url.net/po23283) и добавьте его в `.github/workflows/`. Этот процесс проверяет наличие новых критических уязвимостей и запускает GitHub Copilot для устранения только тех, которые подтверждены Dynatrace.

Подробности см. в [Создание первого рабочего процесса](https://docs.github.com/en/actions/get-started/quickstart#creating-your-first-workflow).

После настройки GitHub Copilot начнёт сортировку и устранение уязвимостей по мере обнаружения новых оповещений.

Вы можете [протестировать рабочий процесс](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow), чтобы убедиться, что всё работает правильно.

## Рабочий процесс на основе Dynatrace

Этот сценарий использует Dynatrace для приёма и сортировки оповещений GitHub Advanced Security (GHAS), а затем запускает GitHub Copilot для применения исправлений только для уязвимостей, подтверждённых данными о выполнении.

### Как это работает (рабочий процесс на основе Dynatrace)

![Рабочий процесс на основе Dynatrace — как это работает](https://dt-cdn.net/images/image-61-2188-3661817c05.png)

1. GitHub Advanced Security (GHAS) обнаруживает уязвимости через [Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).
2. Интеграция Dynatrace с GHAS принимает эти оповещения с помощью расширения GitHub Advanced Security и сохраняет их в Grail для анализа.
3. Рабочий процесс Dynatrace выполняет сортировку оповещений с использованием контекста выполнения и действия генеративного ИИ Dynatrace Intelligence для валидации. Подробнее см. Приложение Dynatrace Intelligence (Preview).
4. Создаётся GitHub issue и назначается GitHub Copilot, включая как подтверждённые, так и неподтверждённые уязвимости.
5. Агент GitHub Copilot автоматически подбирает задачу, устраняет подтверждённые уязвимости и отклоняет неподтверждённые.
6. Разработчики проверяют и сливают pull request с применёнными исправлениями.

### Начало работы (рабочий процесс на основе Dynatrace)

Для начала выполните следующие шаги.

1. Настройка Dynatrace

* [Включите Runtime Vulnerability Analytics](../application-security/vulnerability-analytics.md#start "Мониторинг, визуализация, анализ и устранение уязвимостей.").
* [Запросите доступ к Dynatrace MCP Server](../../../common/whats-new/preview-releases.md#mcp-server "Узнайте о Preview-релизах и способах участия в них.").
* Создайте токен платформы Dynatrace с необходимыми разрешениями для доступа к серверу MCP и запросов к различным типам событий.
* Установите и настройте интеграцию с GitHub Advanced Security в Dynatrace.

2. Подготовка репозитория GitHub

1. [Включите Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository) для обнаружения уязвимостей в зависимостях.
2. [Сгенерируйте fine-grained personal access token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) с необходимыми разрешениями.

   1. Список разрешений

   * **Read**:

     + `Variables`
     + `Administration`
     + `Dependabot secrets`
     + `Environments`
     + `Metadata`
     + `Webhooks`
     + `Secrets`
   * **Read and write**:

     + `Dependabot alerts`
     + `Actions`
     + `Code scanning alerts`
     + `Custom properties`
     + `Issues`
     + `Pull requests`
     + `Workflows`
     + `Contents`
3. Сохраните PAT, созданный на шаге 2, [как секрет GitHub для среды Copilot](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment#setting-environment-variables-in-copilots-environment) с именем `COPILOT_SPONSOR_PAT`. Этот секрет предоставляется агенту GitHub Copilot в качестве переменной среды, позволяя ему аутентифицироваться и выполнять действия в вашем репозитории от вашего имени.

3. Подключение GitHub Copilot к Dynatrace

Для подключения GitHub Copilot к Dynatrace MCP Server:

1. Сохраните токен платформы Dynatrace как секрет GitHub с именем `COPILOT_MCP_DT_API_TOKEN`.
2. В репозитории GitHub перейдите в **Settings** > **Copilot** > **Agents**.
3. Добавьте конфигурацию MCP-сервера следующего вида:

   ```
   {
   "mcpServers":
   {
   "dynatrace": {
   "type": "http",
   "url": "https://pia1134d.dev.apps.dynatracelabs.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp",
   "headers": {
   "Authorization": "Bearer $COPILOT_MCP_DT_API_TOKEN"
   },
   "tools": ["*"]
   }
   }
   }
   ```

   Убедитесь, что вы заменили `<your-dynatrace-mcp-endpoint>` на URL вашего Dynatrace MCP.

Для справки см. [Расширение агента GitHub Copilot с помощью Model Context Protocol (MCP)](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).

4. Добавление инструкций для GitHub Copilot

Чтобы адаптировать рекомендации агента GitHub Copilot к вашим стандартам кодирования и политикам безопасности, у вас есть два варианта:

* **Направьте агента GitHub Copilot через глобальный файл инструкций**: скачайте файл [`copilot-instructions.md`](https://dt-url.net/ug032yv) и добавьте его в `.github/`. Инструкции см. в [Добавление пользовательских инструкций для репозитория GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).
* **Определите пользовательского агента Dynatrace для GitHub Copilot**: скачайте файл [`dynatrace-security-agent.md`](https://dt-url.net/8r032d2) и добавьте его в `.github/agents`.

После настройки GitHub Copilot начнёт сортировку и устранение уязвимостей по мере обнаружения новых оповещений.

5. Развёртывание и планирование рабочего процесса сортировки Dynatrace

Для автоматизации сортировки уязвимостей и создания задач скачайте следующие два рабочих процесса Dynatrace для оповещений Dependabot и загрузите их в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**:

1. [GitHub Dependabot alert verification.yml](https://dt-url.net/97432ns): это родительский рабочий процесс, который выполняет следующие действия:

   * Запрашивает новые критические результаты GitHub Dependabot.
   * Проверяет их с использованием контекста выполнения.
   * Подготавливает содержимое задачи и вызывает дочерний рабочий процесс.
2. [GitHub issue creation and Copilot assignment.yml](https://dt-url.net/ss632s6): это дочерний рабочий процесс, вызываемый родительским для:

   * Создания GitHub issue с результатами проверки.
   * Назначения задачи GitHub Copilot для устранения.

   **Перед запуском рабочего процесса**:

   * Сохраните personal access token (PAT) GitHub, созданный на шаге 2 (**Подготовка репозитория GitHub**), в хранилище Dynatrace, чтобы рабочий процесс мог безопасно к нему обращаться.
   * Обновите конфигурацию ввода по умолчанию дочернего рабочего процесса, указав владельца и репозиторий, в котором должна быть создана GitHub issue.
   * В HTTP-действиях дочернего рабочего процесса укажите ссылку на учётные данные, сохранённые в хранилище, для аутентификации запросов к API GitHub.

После настройки GitHub Copilot будет помогать в устранении уязвимостей, предлагая изменения кода на основе новых оповещений.
