---
title: Dynatrace Intelligence (Preview) app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows
scraped: 2026-03-06T21:29:56.714019
---

# Приложение Dynatrace Intelligence (Preview)

# Приложение Dynatrace Intelligence (Preview)

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 3 мин
* Обновлено 4 февраля 2026 г.
* Preview

С помощью ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** вы можете автоматизировать запросы к генеративному ИИ Dynatrace Intelligence и настроить его реагирование на изменения в среде по мере их возникновения, обобщая события и ежедневные действия и предлагая оптимальные решения для открытых проблем и изменений в коде.

Вы также можете запланировать повторное выполнение рабочих процессов и настроить отправку ответов генеративного ИИ Dynatrace Intelligence на вашу электронную почту или в каналы Slack.
Запланированное и повторяющееся выполнение рабочих процессов помогает экономить время и позволяет сосредоточиться на других задачах, пока генеративный ИИ Dynatrace Intelligence анализирует входящие изменения за вас.

## Сценарии использования

## Предварительные требования

Для использования действия генеративного ИИ Dynatrace Intelligence в рабочих процессах убедитесь, что у вас есть следующее разрешение:

* **Conversational recommender** `ALLOW davis-copilot:conversations:execute;`

  Для получения дополнительной информации о назначении разрешения **Conversational recommender** см. [Права пользователей](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Узнайте, как настроить агентный и генеративный ИИ Dynatrace Intelligence.").

Для использования **Dynatrace Intelligence (Preview)** вам необходимо

1. Убедиться, что у вас есть подписка Hub на канал Preview генеративного ИИ Dynatrace Intelligence.

   Если у вас нет подписки, обратитесь к вашему менеджеру по работе с клиентами (CSM).
2. Установить **Dynatrace Intelligence (Preview)**.

Чтобы установить **Dynatrace Intelligence (Preview)**

1. В ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") Dynatrace Hub найдите **Dynatrace Intelligence (Preview)**.
2. Выберите **Dynatrace Intelligence (Preview)** и нажмите **Install**.

## Ограничения

Стандартные ограничения использования **агентного и генеративного ИИ Dynatrace Intelligence** также применяются к **Dynatrace Intelligence (Preview)**:

Это означает, что если вы запланируете частое автоматическое выполнение рабочего процесса, вся остальная функциональность генеративного ИИ Dynatrace Intelligence может быть ограничена из-за достижения лимита запросов. Если вы столкнётесь с ограничением использования, обратитесь к вашему CSM или сообщите нам в [группе пользователей Agentic AI Preview](https://dt-url.net/copilot-community) в нашем сообществе.

## Настройка действия генеративного ИИ Dynatrace Intelligence в рабочем процессе

Чтобы создать рабочий процесс с действием **Dynatrace Intelligence (Preview)**

1. В Dynatrace перейдите в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
2. Выберите **Workflow**, чтобы создать новый рабочий процесс.
3. Выберите [триггер рабочего процесса](/docs/analyze-explore-automate/workflows/trigger "Введение в триггеры автоматизации рабочих процессов."), который запустит выполнение рабочего процесса.
4. Выберите **Add task**.
5. Введите `Dynatrace Intelligence` в поле поиска или выберите **Dynatrace Intelligence** > **Define prompt**.
6. Настройте действие:

   * В поле **Prompt** введите ваш вопрос или запрос. Вы также можете добавить инструкции по форматированию для лучшего соответствия вашему сценарию использования.

     В это поле можно ввести максимум 5 000 символов.
   * Необязательно: в поле **Additional context** предоставьте дополнительный контекст (например, фрагмент кода или дополнительную информацию о проблеме или событии), на который генеративный ИИ Dynatrace Intelligence будет ссылаться при выполнении вашего запроса. В этом поле можно ссылаться на результат предыдущего действия рабочего процесса.

     В это поле можно ввести максимум 20 000 символов.
   * Включите **Auto-trim**, чтобы автоматически обрезать ваш запрос и дополнительный контекст при превышении лимита символов. Если **Auto-trim** отключён и ваш запрос или дополнительный контекст превышают лимит символов, выполнение действия завершится ошибкой.
   * Установите **Document retrieval** в значение `Dynatrace`, если вы хотите, чтобы генеративный ИИ Dynatrace Intelligence обращался к источникам Dynatrace, таким как документация, сообщество и портал разработчиков, для обогащения ответов. Если **Document retrieval** установлен в значение `Disabled`, генеративный ИИ будет опираться на свою базовую модель для выполнения вашего запроса.
7. Необязательно: добавьте дополнительные действия рабочего процесса до или после действия генеративного ИИ Dynatrace Intelligence для поддержки вашего сценария использования.
8. Выберите **Save**.
9. Затем выберите **Run** для выполнения рабочего процесса.

Чтобы узнать о конкретных сценариях использования и о том, как применять действие генеративного ИИ Dynatrace Intelligence в рабочих процессах, см. [Обобщение открытых проблем с помощью Dynatrace Intelligence (Preview)](/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples "Используйте Dynatrace Intelligence (Preview) для обобщения открытых проблем и предложения шагов по их устранению.").

## Связанные темы

* [Workflows](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.")
* [Обзор агентного и генеративного ИИ Dynatrace Intelligence](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах агентного и генеративного ИИ Dynatrace Intelligence.")
* [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Задавайте вопросы на естественном языке и получайте быстрые ответы от Dynatrace Assist, вашего генеративного ИИ-помощника.")
* [Обобщение открытых проблем с помощью Workflows](/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples "Используйте Dynatrace Intelligence (Preview) для обобщения открытых проблем и предложения шагов по их устранению.")
* [Агентные рабочие процессы](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/agentic-workflows "Основные концепции использования агентных рабочих процессов для автоматизации сложных задач, основанных на данных, с использованием генеративного и агентного ИИ.")
