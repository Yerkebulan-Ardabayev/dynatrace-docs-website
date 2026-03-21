---
title: Отправка уведомлений Slack для __KEEP000__
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/use-cases/workflows-tutorial-problems-slack
scraped: 2026-02-18T05:48:39.343910
---

# Отправка уведомлений в Slack о проблемах


* Latest Dynatrace
* Tutorial

Проблемы автоматически создаются Dynatrace при обнаружении аномалий или выполнении условий оповещений в вашей среде.
В ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** создайте простой рабочий процесс, который отслеживает проблемы и автоматически отправляет уведомления в ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector") Slack при возникновении новой проблемы.
В этом руководстве показано, как это сделать.

## Что вы узнаете

В этом руководстве вы узнаете, как оповещать свою команду в реальном времени, автоматически отправляя подробности о новой проблеме в определённый канал Slack.

Кратко вы будете:

1. [Создавать простой рабочий процесс](../simple-workflow.md#create-simple-workflow "Build and run a simple workflow.").
2. Добавлять [триггер событий](../trigger/event-trigger.md "Guide to creating workflow automation event triggers in Dynatrace Workflows.") для [проблем Davis](../trigger/event-trigger.md#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").
3. Настраивать [сообщение в Slack](../actions/slack.md "Send messages to Slack Workspaces").
4. Сохранять и запускать рабочий процесс для отправки уведомлений.
5. Проверять, что рабочий процесс работает корректно.

## Предварительные требования

* У вас должно быть разрешение на настройку и запуск простого рабочего процесса.
  Например, разрешение, предоставляемое стандартной политикой для [стандартного пользователя](../../../manage/identity-access-management/permission-management/default-policies.md "Dynatrace default policies reference").
* Необходимо выбрать соответствующие разрешения в [настройках авторизации](../security.md#authorization-settings "Guide on security aspects of workflow automation in Dynatrace Workflows").

  + Вам следует предоставить необходимые разрешения для:

    - Доступа к ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
    - Создания и выполнения рабочего процесса.
      Подробнее см. [настройки авторизации](../security.md#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").
* У вас настроена [интеграция со Slack](../actions/slack.md#setup-slack-integration "Send messages to Slack Workspaces").

## Шаги

1. [Создайте простой рабочий процесс](../simple-workflow.md#create-simple-workflow "Build and run a simple workflow.").

   1. Перейдите в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
   2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow** в правом верхнем углу страницы.
   3. Выберите название рабочего процесса.
      По умолчанию оно задано как `Untitled workflow` — введите осмысленное название.
      Тип рабочего процесса по умолчанию установлен как простой рабочий процесс.
2. Добавьте [триггер событий](../trigger/event-trigger.md "Guide to creating workflow automation event triggers in Dynatrace Workflows.") для [проблем Davis](../trigger/event-trigger.md#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").

   1. В разделе **Select trigger** выберите [триггер проблем Davis](../trigger/event-trigger.md#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").
   2. Установите **Problem state** в значение **active or closed**.
      Этот вариант означает, что проблема может быть как активной, так и закрытой.
      Эта настройка приводит к двойному срабатыванию рабочего процесса: один раз при активации проблемы и ещё раз при её закрытии.
   3. В раскрывающемся списке **Event category** выберите **Select all**.
   4. Необязательно Выберите **Query past events**, чтобы увидеть последние события проблем, которые запустили бы этот рабочий процесс.
   5. Необязательно Введите **Entity tags** или **Additional custom filter query**, чтобы рабочий процесс запускался только для релевантных проблем.
3. Настройте [сообщение в Slack](../actions/slack.md "Send messages to Slack Workspaces").

   1. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add task** на узле триггера.
   2. В разделе **Choose action** выберите действие ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector") **Send message**.
      Дайте действию осмысленное название.
   3. Выберите предварительно настроенное подключение к Slack.
   4. Выберите подключение к Slack из раскрывающегося списка **Connection**.
   5. Выберите канал Slack для вашего сообщения из раскрывающегося списка **Channel**.
   6. В поле **Message** введите следующее:

      ```
      {


      "blocks": [


      {


      "type": "header",


      "text": {


      "type": "plain_text",


      "text": "{{ ':white_check_mark:' if event()['event.status'] == 'CLOSED' else ':warning:' }} {{ 'RESOLVED' if event()['event.status'] == 'CLOSED' else 'OPEN' }} - {{ event()['event.name']}}",


      "emoji": true


      }


      },


      {


      "type": "section",


      "text": {


      "type": "mrkdwn",


      "text": "- *Problem link*: <{{ environment().url }}/ui/intent/dynatrace.davis.problems/view-problem#%7B%22event.id%22%3A%22{{ event()['event.id'] }}%22,%22event.kind%22%3A%22{{event()['event.kind']}}%22%7D|{{ event()['display_id'] }}> \n- *Impacted Entities:* `{{ event()['affected_entity_ids'] }}`\n- *Problem duration:* `{{ (event().get('resolved_problem_duration', 0) | int) / 1000000 / 1000 / 60 }} minutes`"


      }


      },


      {


      "type": "section",


      "text": {


      "type": "mrkdwn",


      "text": {{ ('>' ~ event()['event.description']) | replace('\n', '\n>') | to_json }}


      }


      },


      {


      "type": "divider"


      },


      {


      "type": "section",


      "text": {


      "type": "mrkdwn",


      "text": "*Workflow link*: <{{ environment().url }}/ui/apps/dynatrace.automations/workflows/{{ execution().workflow.id }}|Workflow>"


      }


      }


      ]


      }
      ```

      Эта конфигурация использует контекстные заполнители событий для динамического заполнения сообщения Slack соответствующими деталями проблемы.

      Триггер проблем Davis возвращает запись о проблеме.
      Вы можете использовать любое поле из записи проблемы, хранящейся в `dt.davis.problems`, в сообщении Slack.
4. Сохраните и запустите рабочий процесс для отправки уведомлений в Slack.

   1. Выберите **Create draft**.
   2. Выберите **Deploy**.
   3. Выберите **Run**, чтобы увидеть выбранное событие проблемы, которое будет использовано для рабочего процесса.
5. Убедитесь, что ваш рабочий процесс работает корректно:

   1. Перейдите к вашему рабочему процессу.
   2. Выберите **Run**.
   3. Выберите **Run** ещё раз для выполнения рабочего процесса.

      Журналы выполнения недоступны для простого рабочего процесса.
      В случае возникновения ошибки вы можете найти подробности ошибки справа на панели деталей задачи.

## Заключение

Вы создали простой рабочий процесс, который отправляет сообщения в Slack при открытии или закрытии проблем.
Эта настройка помогает обеспечить немедленное информирование вашей команды о критических проблемах в среде.

Вы можете расширить этот рабочий процесс, добавив:

* Условия для обработки определённых категорий проблем или уровней критичности.
* Шаги автоматического устранения в ваш рабочий процесс.

Этот рабочий процесс является отличной отправной точкой для автоматизации реагирования на инциденты и повышения операционной осведомлённости.

## Связанные темы

* [Создание простого рабочего процесса в Dynatrace Workflows](../simple-workflow.md "Build and run a simple workflow.")
* [Приложение Problems](../../../dynatrace-intelligence/davis-problems-app.md "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Slack Connector](../actions/slack.md "Send messages to Slack Workspaces")
