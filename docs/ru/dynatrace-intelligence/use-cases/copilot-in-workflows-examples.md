---
title: Сводка открытых проблем с помощью Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-examples
scraped: 2026-03-03T21:26:45.029733
---

# Суммирование открытых проблем с помощью Workflows

# Суммирование открытых проблем с помощью Workflows

* Latest Dynatrace
* Руководство
* Чтение: 4 мин
* Обновлено 5 февраля 2026 г.
* Preview

С помощью [Dynatrace Intelligence (Preview)](../dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью workflows.") вы можете автоматизировать суммирование проблем и попросить генеративный ИИ Dynatrace Intelligence предложить шаги по исправлению, которые будут отправлены на вашу электронную почту.

## Целевая аудитория

Это руководство написано для:

* Инженеров по эксплуатации
* Инженеров по пайплайнам
* Системных инженеров
* Инженеров по надёжности (SRE)
* Инженеров по автоматизации сборки

## Сценарий

Допустим, вы хотите автоматизировать анализ новых проблем и сразу получать предложения по их устранению.
Для этого необходимо создать workflow, который использует генеративный ИИ Dynatrace Intelligence для суммирования всех открытых проблем и автоматического предложения лучшего способа их устранения.
Когда открывается новая проблема, workflow запускается автоматически, и ответ генеративного ИИ Dynatrace Intelligence отправляется на вашу электронную почту.

## Перед началом работы

### Предварительные требования

Для использования Dynatrace Intelligence (Preview) убедитесь, что у вас есть:

* Разрешение **Conversational recommender** (`ALLOW davis-copilot:conversations:execute;`).
* Установленное приложение **Dynatrace Intelligence (Preview)**.

## Шаги

1. Настройка триггера workflow

1. Перейдите в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") Workflows.
2. Выберите **Workflow**, чтобы создать новый workflow.
3. В разделе триггеров **Event** выберите **Davis problem trigger**.
4. Настройте поля:

   * Установите **Event state** в значение `active`.
   * Установите **Event category** в значение `Custom`.
   * Установите **Affected entities** в значение `include entities with all defined tags below`.
   * Установите **Additional custom filter query** в значение

     ```
     matchesPhrase(event.name, "Host cpu stateful custom alert 1h")
     ```

     Этот пример демонстрирует фильтрацию по конкретной проблеме.
     Однако вы также можете применить фильтр для включения всех новых проблем.

1. Пример настройки триггера Davis problems

![Пример настройки триггера Davis Problem для новых проблем.](https://dt-cdn.net/images/generative-ai-in-workflows-set-trigger-1920-775b0ee285.png)

2. Извлечение деталей проблемы

1. Выберите Add task.
2. В поле поиска введите `Run JavaScript` или выберите **Run JavaScript** из списка действий ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow**. Дополнительную информацию о действии JavaScript в workflow см. в разделе [Действие Run JavaScript для Workflows](../../analyze-explore-automate/workflows/default-workflow-actions/run-javascript-workflow-action.md "Выполнение действия JavaScript для ваших workflows.").
3. Введите имя задачи workflow.
4. На вкладке **Input** введите следующий **Source code**:

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function () {



   const ex = await execution();



   let rawEvent = ex.params.event;



   let problemDescription = rawEvent["event.description"];



   return {



   description : rawEvent["event.description"],



   problem_id : rawEvent["display_id"]



   };



   }
   ```

1. Пример настройки действия JavaScript

![Пример настройки действия JavaScript для извлечения деталей проблемы](https://dt-cdn.net/images/copilot-in-workflows-run-javascript-1896-4a0406181b.png)

3. Запрос к генеративному ИИ Dynatrace Intelligence для суммирования проблемы и предложения шагов по исправлению

1. Выберите Add task.
2. В поле поиска введите `Dynatrace Intelligence` или выберите **Define prompt** из списка действий ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow**.
3. Настройте генеративный ИИ Dynatrace Intelligence:

   * В поле **Prompt** введите следующий запрос:

     ```
     A new Davis Problem with id {{result("extract_problem_details").problem_id}} has just been opened. Please provide a summary of what happened and actionable steps to remediate it. Provide output as plain text without any formatting or markdown
     ```
   * В поле **Additional context** введите следующее:

     ```
     Use the following information about the Davis Problem with Id {{result("extract_problem_details")["problem_id"]}}:



     """



     {{result("extract_problem_details")["description"]}}



     """
     ```
   * Включите **Auto-trim**.
   * Установите **Document retrieval** в значение `Disabled`.

1. Пример подготовки запроса к генеративному ИИ Dynatrace Intelligence

![Пример настройки действия Dynatrace Intelligence для суммирования новых проблем.](https://dt-cdn.net/images/set-dynatrace-intelligence-action-in-workflows-1920-8fd3190dc2.png)

4. Отправка результатов генеративного ИИ Dynatrace Intelligence на электронную почту

1. Выберите Add task.
2. В поле поиска введите `Send email` или выберите ![Email for Workflows](https://dt-cdn.net/images/email-for-workflows-new-256-f6c0e2d343.png "Email for Workflows") **Send email** из списка действий ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflow**. Дополнительную информацию о действиях Email в workflow см. в разделе [Email](../../analyze-explore-automate/workflows/actions/email.md "Автоматизируйте отправку готовых электронных писем на основе событий и расписаний, определённых для ваших workflows.").
3. Введите имя задачи workflow.
4. Настройте поля:

   * В разделе **Configure email** > **Recipients** укажите в поле **To** ваш адрес электронной почты. Если вы хотите добавить несколько адресов, используйте `;` для их разделения.
   * В поле **Content** > **Subject** введите следующий текст:

     ```
     New Davis Problem {{ result("extract_problem_details")["problem_id"] }} started
     ```
   * Установите поле **Message** в следующее значение:

     ```
     A Davis Problem with ID {{ result("extract_problem_details")["problem_id"] }} has been opened.



     Dynatrace Intelligence generative AI has analyzed it and provided the following information:



     {{ result("analyze_problem_with_davis_copilot")["text"] }}
     ```

1. Пример настройки электронной почты

![Пример настройки электронной почты для отправки результатов генеративного ИИ Dynatrace Intelligence.](https://dt-cdn.net/images/generative-ai-in-workflows-send-email-1920-47ec9a8954.png)

5. Завершение настройки workflow

1. Выберите **Save**.
2. Выберите **Run** для тестирования workflow.

После появления новой проблемы вы получите электронное письмо от `no-reply@dev.apps.dynatracelabs.com`. Пример содержимого сообщения показан ниже:

![Пример электронного письма от генеративного ИИ Dynatrace Intelligence в сценарии использования workflows](https://dt-cdn.net/images/copilot-in-workflows-email-example-1584-f32b4d0bbb.png)

## Связанные темы

* [Dynatrace Assist](../copilot/chat-with-davis-copilot.md "Задавайте вопросы на естественном языке и получайте быстрые ответы от Dynatrace Assist, вашего помощника на основе генеративного ИИ.")
* [Приложение Dynatrace Intelligence (Preview)](../dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью workflows.")
* [Обзор генеративного ИИ Dynatrace Intelligence](../copilot/copilot-overview.md "Узнайте о безопасности данных и других аспектах генеративного ИИ Dynatrace Intelligence.")
* [Workflows](../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.")
* [Приложение Dynatrace Intelligence (Preview)](../dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью workflows.")
