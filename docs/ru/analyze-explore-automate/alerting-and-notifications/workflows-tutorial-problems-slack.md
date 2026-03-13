---
title: Отправка Slack-уведомлений о проблемах
source: https://www.dynatrace.com/docs/analyze-explore-automate/alerting-and-notifications/workflows-tutorial-problems-slack
scraped: 2026-03-04T21:36:56.983118
---

# Отправка Slack-уведомлений о проблемах

# Отправка Slack-уведомлений о проблемах

* Последняя Dynatrace
* Учебное пособие
* 4 мин. чтения
* Обновлено 19 октября 2025 г.

Проблемы автоматически создаются в Dynatrace при обнаружении аномалий или условий оповещения в вашей среде.
В ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Рабочих процессах** создайте простой рабочий процесс, который отслеживает проблемы и автоматически отправляет уведомления в ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector") Slack при каждой новой проблеме.
Это руководство покажет вам, как это сделать.

## Что вы узнаете

В этом учебном пособии вы узнаете, как оповещать вашу команду в реальном времени, автоматически отправляя детали новой проблемы в определённый канал Slack.

Кратко, вы будете:

1. [Создавать простой рабочий процесс](/docs/analyze-explore-automate/workflows/simple-workflow#create-simple-workflow "Создайте и запустите простой рабочий процесс.").
2. Добавлять [триггер события](/docs/analyze-explore-automate/workflows/trigger/event-trigger "Руководство по созданию триггеров событий автоматизации рабочих процессов в Dynatrace Workflows.") для [проблем Davis](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Руководство по созданию триггеров событий автоматизации рабочих процессов в Dynatrace Workflows.").
3. Настроить [сообщение Slack](/docs/analyze-explore-automate/workflows/actions/slack "Отправка сообщений в рабочие пространства Slack").
4. Сохранить и запустить рабочий процесс для получения уведомлений.
5. Проверить, что ваш рабочий процесс работает как ожидалось.

## Предварительные требования

* У вас должно быть разрешение на настройку и запуск простого рабочего процесса.
  Например, разрешение, предоставляемое политикой по умолчанию для [стандартного пользователя](/docs/manage/identity-access-management/permission-management/default-policies "Справочник по политикам Dynatrace по умолчанию").
* Вы должны выбрать необходимые разрешения в [настройках авторизации](/docs/analyze-explore-automate/workflows/security#authorization-settings "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Workflows").

  + Вы должны разрешить необходимые права для

    - Доступа к ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Рабочим процессам**.
    - Записи и выполнения рабочего процесса.
      Дополнительную информацию см. в [настройках авторизации](/docs/analyze-explore-automate/workflows/security#user-permission "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Workflows").
* Вы [настроили интеграцию со Slack](/docs/analyze-explore-automate/workflows/actions/slack#setup-slack-integration "Отправка сообщений в рабочие пространства Slack").

## Шаги

1. [Создайте простой рабочий процесс](/docs/analyze-explore-automate/workflows/simple-workflow#create-simple-workflow "Создайте и запустите простой рабочий процесс.").

   1. Перейдите в ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Рабочие процессы**.
   2. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Рабочий процесс** в верхнем правом углу страницы.
   3. Выберите заголовок рабочего процесса.
      По умолчанию это `Untitled workflow`, и введите понятное имя.
      Тип рабочего процесса по умолчанию установлен как простой рабочий процесс.
2. Добавьте [триггер события](/docs/analyze-explore-automate/workflows/trigger/event-trigger "Руководство по созданию триггеров событий автоматизации рабочих процессов в Dynatrace Workflows.") для [проблем Davis](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Руководство по созданию триггеров событий автоматизации рабочих процессов в Dynatrace Workflows.").

   1. В разделе **Выберите триггер** выберите [триггер проблемы Davis](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Руководство по созданию триггеров событий автоматизации рабочих процессов в Dynatrace Workflows.").
   2. Установите **Состояние проблемы** на **активная или закрытая**.
      Эта опция означает, что проблема может быть как активной, так и закрытой.
      Эта настройка заставляет рабочий процесс запускаться дважды: один раз, когда проблема становится активной, и ещё раз, когда она закрывается.
   3. В выпадающем списке **Категория события** выберите **Выбрать все**.
   4. Опционально — выберите **Запросить прошлые события**, чтобы увидеть самые последние события проблем, которые запустили бы этот рабочий процесс.
   5. Опционально — введите **Теги сущностей** или **Дополнительный пользовательский запрос-фильтр**, чтобы запускать рабочий процесс только для релевантных проблем.
3. Настройте [сообщение Slack](/docs/analyze-explore-automate/workflows/actions/slack "Отправка сообщений в рабочие пространства Slack").

   1. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Добавить задачу** на узле триггера.
   2. В разделе **Выберите действие** выберите тип действия ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector") **Отправить сообщение**.
      Дайте типу действия понятное название.
   3. Выберите предварительно настроенное подключение Slack.
   4. Выберите подключение Slack из выпадающего списка **Подключение**.
   5. Выберите канал Slack для вашего сообщения из выпадающего списка **Канал**.
   6. В поле **Сообщение** введите следующее:

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

      Эта конфигурация использует заполнители контекста события для динамического заполнения сообщения Slack соответствующими деталями проблемы.

      Триггер проблем Davis возвращает запись проблемы.
      Вы можете использовать любое поле из записи проблемы, хранящейся в `dt.davis.problems`, в сообщении Slack.
4. Сохраните и запустите рабочий процесс для отправки Slack-уведомлений.

   1. Нажмите **Создать черновик**.
   2. Нажмите **Развернуть**.
   3. Нажмите **Запустить**, чтобы увидеть выбранное событие проблемы, которое будет использоваться для рабочего процесса.
5. Убедитесь, что ваш рабочий процесс работает как ожидалось:

   1. Перейдите к вашему рабочему процессу.
   2. Нажмите **Запустить**.
   3. Нажмите **Запустить** ещё раз для выполнения рабочего процесса.

      Журналы выполнения недоступны для простого рабочего процесса.
      Если произошла ошибка, вы можете найти детали ошибки справа в панели деталей задачи.

## Заключение

Вы создали простой рабочий процесс, который отправляет сообщения в Slack при открытии или закрытии проблем.
Эта настройка помогает обеспечить немедленное информирование вашей команды о критических проблемах в вашей среде.

Вы можете расширить этот рабочий процесс:

* Добавив условия для обработки конкретных категорий или уровней серьёзности проблем.
* Добавив шаги автоматического устранения в ваш рабочий процесс.

Этот рабочий процесс — отличная отправная точка для автоматизации реагирования на инциденты и повышения операционной осведомлённости.

## Связанные темы

* [Создание простого рабочего процесса в Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Создайте и запустите простой рабочий процесс.")
* [Приложение Problems](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Problems для быстрого определения коренной причины инцидентов в вашей среде.")
* [Коннектор Slack](/docs/analyze-explore-automate/workflows/actions/slack "Отправка сообщений в рабочие пространства Slack")