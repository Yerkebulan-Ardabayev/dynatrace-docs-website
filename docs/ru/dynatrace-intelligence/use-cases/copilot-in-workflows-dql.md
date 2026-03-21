---
title: Оптимизация затрат DQL с помощью Workflows
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-in-workflows-dql
scraped: 2026-03-06T21:33:02.783409
---

# Оптимизация стоимости DQL с помощью Workflows


* Актуальная версия Dynatrace
* Preview

С помощью [Dynatrace Intelligence (Preview)](../dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью Workflows.") вы можете автоматизировать обобщение проблем и попросить генеративный ИИ Dynatrace Intelligence предложить шаги по устранению, которые могут быть отправлены на вашу электронную почту.

## Обзор

С помощью этого руководства:

* Вы познакомитесь с оптимизацией стоимости Dynatrace Query Language (DQL) с использованием Dynatrace Intelligence (Preview).
* Вы узнаете, как автоматизировать получение инсайтов и рекомендаций для снижения затрат на выполнение запросов.

## Целевая аудитория

Это руководство написано для:

* Инженеров по наблюдаемости
* Владельцев платформ
* Специалистов по FinOps
* SRE

## Сценарий

* Автоматическое обнаружение дорогостоящих DQL-запросов.
* Получение предложений по оптимизации и действий по снижению затрат по электронной почте или в чате.

Чтобы помочь командам более эффективно управлять затратами на наблюдаемость, этот сценарий демонстрирует, как автоматизировать выявление и оптимизацию дорогостоящих выполнений Dynatrace Query Language (DQL).

Простой рабочий процесс, запланированный для ежедневного запуска, обнаруживает 20 самых дорогих запросов за последние 24 часа. Благодаря интеграции генеративного ИИ Dynatrace Intelligence в этот рабочий процесс каждый запрос автоматически анализируется на предмет возможностей оптимизации.

Генеративный ИИ предоставляет персонализированные рекомендации по снижению стоимости запросов и отправляет эти инсайты непосредственно авторам запросов по электронной почте. Это помогает проактивно контролировать затраты и повышать эффективность запросов без ручного вмешательства.

## Прежде чем начать

### Предварительные требования

Для использования Dynatrace Intelligence (Preview) убедитесь, что у вас есть:

* Разрешение **Conversational recommender** (`ALLOW davis-copilot:conversations:execute;`).
* Установленное приложение **Dynatrace Intelligence (Preview)**.
* Доступ к метрикам использования DQL и данным о тарификации.

## Шаги

1. Настройка триггера рабочего процесса

1. Перейдите в **Workflows**.
2. Нажмите **+ Workflow**, чтобы создать новый рабочий процесс.
3. В триггерах выберите **Fixed time trigger**.
4. Настройте поля:

* Установите **Run at** на желаемое время.
* Установите **Rule** на **Every day**.

2. Получение дорогостоящих запросов

1. Нажмите **+ Add task**.
2. В поле поиска введите **DQL query** или выберите **Execute DQL Query** из списка действий Workflow.
3. Переименуйте задачу в `dql_query`.
4. В поле **DQL query** добавьте следующий запрос:

   ```
   fetch dt.system.query_executions, from:now() - 24h


   | filter status == "SUCCEEDED"


   | summarize executionCount = count(), sum = sum(scanned_bytes.on_demand), user = collectDistinct(user.email), app = collectDistinct(client.application_context), by: {query_string}


   | sort sum desc


   | limit 20
   ```

3. Запрос к генеративному ИИ Dynatrace Intelligence для поиска улучшений каждого запроса

1. Нажмите **+ Add task**.
2. В поле поиска введите **Dynatrace Intelligence** или выберите **Define prompt** из списка действий Workflow.
3. Настройте генеративный ИИ Dynatrace Intelligence:

* В поле **Prompt** введите следующий промпт:

  ```
  I've supplied you with result of a DQL Grail query. This result has information about top 20 expensive executed by users in last 24 hours.


  Create a json array with the following info:


  - query: that is the original query that is given in the result


  - email: email of the user who executed the query


  - improvement: tell me the reasons why query is expensive and how can user improve it


  - context: any relevant context where the query is executed and so on


  Make sure that there is no other text beside the json array and no backticks or anything
  ```
* В поле **Additional context** введите следующее:
  `{{result('dql_query').records}}`
* Включите **Auto-trim**.
* Убедитесь, что **Document retrieval** установлен в **Disabled**.
* Переименуйте задачу в `davis_copilot`.

4. Отправка результатов генеративного ИИ Dynatrace Intelligence на электронную почту пользователей

1. Нажмите **+ Add task**.
2. В поле поиска введите **Send email** или выберите **Send email** из списка действий Workflow. Дополнительную информацию о действиях электронной почты в Workflow см. в разделе [Email](../../analyze-explore-automate/workflows/actions/email.md "Автоматизируйте отправку готовых электронных писем на основе событий и расписаний, определённых для ваших рабочих процессов.").
3. Введите имя задачи рабочего процесса.
4. Настройте поля:

* В **Configure email > Recipients** установите поле **To** на `{{_.list.email}}`. Это электронная почта пользователя.
* В поле **Content, Subject** введите следующий текст: `Expensive query executed`.
* Установите содержимое поля **Message**:

  ```
  Hi {{_.list.email}},


  You've executed an expensive query that could be optimized to reduce costs. Below are the details to help you improve it:


  ---


  ### Query Details:


  - **Original Query**:


  `{{_.list.query}}`


  - **Suggested Improvements**:


  {{_.list.improvement}}


  - **Context**:


  {{_.list.context}}


  ---


  Taking these steps can help improve performance and reduce expenses.


  Thanks,


  Your Admin
  ```
* Перейдите на вкладку **Options** и настройте поля следующим образом:

* Включите **Loop task**.
* Введите `list` в поле **Item variable name** и введите `{{result('davis_copilot').text}}` в поле **List**.

5. Завершение настройки рабочего процесса

1. Нажмите **Deploy**, чтобы развернуть рабочий процесс.
2. Нажмите **Run**, чтобы протестировать рабочий процесс.

## Связанные темы

* [Dynatrace Assist](../copilot/chat-with-davis-copilot.md "Задавайте вопросы на естественном языке и получайте быстрые ответы от Dynatrace Assist — вашего генеративного ИИ-помощника.")
* [Приложение Dynatrace Intelligence (Preview)](../dynatrace-intelligence-integrations/copilot-for-workflows.md "Узнайте, как автоматизировать действия и ответы генеративного ИИ Dynatrace Intelligence с помощью Workflows.")
* [Обзор агентного и генеративного ИИ Dynatrace Intelligence](../copilot/copilot-overview.md "Узнайте о безопасности данных и других аспектах агентного и генеративного ИИ Dynatrace Intelligence.")
* [Workflows](../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.")
