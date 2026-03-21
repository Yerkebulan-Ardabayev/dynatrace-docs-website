---
title: Коннектор Slack
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/slack
scraped: 2026-03-03T21:22:08.797257
---

# Slack Connector


* Latest Dynatrace

Ваша среда Dynatrace может интегрироваться с рабочим пространством Slack с помощью Slack Connector ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector"). Вы можете автоматизировать отправку сообщений в Slack на основе событий и расписаний, определённых для вашего [рабочего процесса](../../workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.").

## Настройка интеграции со Slack

### Шаг 1. Разрешение внешних запросов

Внешние запросы обеспечивают исходящие сетевые подключения из вашей среды Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным эндпоинтам из AppEngine с помощью функций приложений и функций в Dashboards, Notebooks и Automations.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
2. Выберите **New host pattern**.
3. Добавьте доменные имена.
4. Выберите **Add**.

Таким образом вы можете гранулярно контролировать веб-сервисы, к которым ваши функции могут подключаться.

### Шаг 2. Предоставление разрешений для Workflows

Некоторые разрешения необходимы для Workflows, чтобы выполнять действия от вашего имени. Другие разрешения требуются действиями, которые поставляются вместе с коннектором **Slack**.

Для тонкой настройки разрешений, предоставленных Workflows:

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения помимо общих разрешений Workflows.

   * `app-settings:objects:read`
   * `app-settings:objects:write`
   * `state:app-states:read`
   * `state:app-states:write`
   * `state:app-states:delete`
   * `state:user-app-states:read`
   * `state:user-app-states:write`
   * `state:user-app-states:delete`

Подробнее об общих разрешениях пользователей Workflows см. [Разрешения пользователей для рабочих процессов](../security.md#user-permission "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Workflows").

### Шаг 3. Создание приложения Slack

Для взаимодействия действий рабочего процесса Slack Connector с вашим рабочим пространством Slack сначала необходимо создать приложение Slack для Dynatrace и авторизовать его подключение к Slack.

1. Перейдите на [Slack API](https://api.slack.com/apps) и выберите **Create an App**.
2. В окне **Create an app** выберите **From an app manifest**.
3. В окне **Pick a workspace to develop your app** выберите рабочее пространство Slack, к которому вы хотите подключиться, и выберите **Next**.
4. В окне **Enter app manifest below** вставьте YAML-манифест, приведённый ниже, во вкладку YAML.
   Замените `<app-name>` и `<bot-name>` на значения по вашему выбору (например, `Dynatrace`). Подробнее о YAML-манифесте см. [документацию Slack](https://api.slack.com/reference/manifests).

   ```
   display_information:


   name: <app-name>


   features:


   bot_user:


   display_name: <bot-name>


   always_online: false


   oauth_config:


   scopes:


   bot:


   - channels:join


   - channels:read


   - chat:write


   - chat:write.public


   - files:read


   - files:write


   - groups:read


   - im:read


   - mpim:read


   - reactions:read


   - reactions:write


   settings:


   org_deploy_enabled: false


   socket_mode_enabled: false


   token_rotation_enabled: false
   ```

### Шаг 4. Авторизация подключения к Slack

Ваш Slack Connector в Dynatrace требует OAuth-токен для авторизации отправки сообщений в Slack.

1. Перейдите на [Slack API](https://api.slack.com/apps/), выберите **Your Apps** в правом верхнем углу и выберите только что созданное приложение.
2. Перейдите в **Features** > **OAuth & Permissions**.
   Если вы являетесь администратором рабочего пространства, вы сможете скопировать OAuth-токен для вашего рабочего пространства. В противном случае вам нужно будет выбрать **Request to Install**. После того как ваш администратор активирует приложение, вы получите доступ к OAuth-токену.
3. Скопируйте OAuth-токен.
4. Вернитесь в Dynatrace, перейдите в **Settings** и выберите **Connections** > **Connectors** > **Slack**.
5. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**, дайте вашему подключению Slack имя и вставьте OAuth-токен в поле **Bot token**.
6. Выберите **Create**.

### Примеры входных данных

Действие рабочего процесса может использоваться для отправки сообщений, отформатированных в Markdown, или интерактивных сообщений на основе [Block Kit](https://app.slack.com/block-kit-builder/) в Slack.

* **Connection**: выберите любое подключение из выпадающего списка, например `dynatrace-notifications-sandbox`.
* **Message**: см. примеры в следующей таблице.
* **Interactions**

  Выберите **Run**, чтобы отправить сообщение в ваш канал Slack.

  + **Output**:
* **Примеры журнала вывода**

  + **Успешно**:

    ```
    [INFO] POST https://slack.com/api/chat.postMessage called successfully


    [INFO] Message has been posted successfully
    ```
  + **Ошибка**:

    ```
    [ERROR] Slack API error while calling 'chat.postMessage': 'no_text'
    ```

#### Пример 1: JSON Block Kit Builder

Вы можете использовать Block Kit Builder для создания богато отформатированных сообщений для Slack.
Варианты форматирования текста описаны в [справочнике Slack Markdown](https://docs.slack.dev/messaging/formatting-message-text/#basic-formatting).
После разработки сообщения скопируйте JSON-вывод и адаптируйте его под свои нужды
в Dynatrace Workflows, используя выражения рабочих процессов.

```
{


"blocks": [


{


"type": "header",


"text": {


"type": "plain_text",


"text": "ð¨ Dynatrace Alert: High CPU Usage Detected",


"emoji": true


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "*Alert Details:*\nâ¢ *Entity*: `Host-1234`\nâ¢ *Metric*: CPU Usage\nâ¢ *Threshold*: > 90%\nâ¢ *Current Value*: 95%"


}


},


{


"type": "divider"


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "ð¡ *Recommended Actions:*"


}


},


{


"type": "actions",


"elements": [


{


"type": "button",


"text": {


"type": "plain_text",


"text": "Acknowledge Alert"


},


"style": "primary",


"value": "acknowledge_alert"


},


{


"type": "button",


"text": {


"type": "plain_text",


"text": "View in Dynatrace"


},


"url": "https://dynatrace.example.com/alert/1234",


"style": "danger"


}


]


},


{


"type": "context",


"elements": [


{


"type": "mrkdwn",


"text": "Triggered at: 2026-01-08 14:30 UTC"


}


]


}


]


}
```

Slack не имеет встроенного языка шаблонов.
Используйте нашу функциональность шаблонов.
Подробнее см. [Выражения Dynatrace](../reference.md "Ознакомьтесь с выражениями рабочих процессов").
Выражения будут разрешены во время выполнения, создавая статическую полезную нагрузку карточки, которая будет отправлена.

#### Пример 2: Динамические сообщения с выражениями

Если вы хотите создать структурированное сообщение с несколькими полями данных, вы можете использовать Slack Block Kit для разработки такого сообщения. См. следующий пример:

```
{


"blocks": [


{


"type": "header",


"text": {


"type": "plain_text",


"text": "production-payment-service",


"emoji": true


}


},


{


"type": "section",


"text": {


"type": "plain_text",


"emoji": true,


"text": "2024-01-09T11:30:00+01:00"


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "```Error: Connection timeout after 5000ms\n  at PaymentGateway.connect (gateway.js:45)\n  at processPayment (service.js:123)```"


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "DT App function: `processPayment`"


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "DT entity service: `SERVICE-A1B2C3D4E5F6G7H8`"


}


}


]


}
```

Для воспроизведения этого поведения вы можете использовать выражения. Тот же пример выше может быть создан с помощью следующего фрагмента:

```
{%- set data = [


{


"dt_app_id": "production-payment-service",


"instance": "2024-01-09T10:30:00Z",


"error": "Error: Connection timeout after 5000ms\n  at PaymentGateway.connect (gateway.js:45)\n  at processPayment (service.js:123)",


"dt_app_function": "processPayment",


"dt_entity_service": "SERVICE-A1B2C3D4E5F6G7H8"


}


]


-%}


{


"blocks": [


{% for item in data %}


{


"type": "header",


"text": {


"type": "plain_text",


"text": "{{ item.dt_app_id }}",


"emoji": true


}


},


{


"type": "section",


"text": {


"type": "plain_text",


"emoji": true,


"text": "{{ item.instance | to_datetime(timezone='Europe/Vienna') }}"


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": {{ ("```" ~ item.error ~ "```") | to_json }}


}


},


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "DT App function: `{{ item.dt_app_function }}`"


}


},


{% if 'dt_entity_service' in item %}


{


"type": "section",


"text": {


"type": "mrkdwn",


"text": "DT entity service: `{{ item.dt_entity_service }}`"


}


}


{% endif %}


{% if not loop.last %},{% endif %}


{% endfor %}


]


}
```

#### Ключевые техники, использованные в этом примере:

* `{% set data = [...] %}` — определите данные встроенно или используйте `result("task_name")` для ссылки на результаты задач рабочего процесса.
* `{{ item.field }}` — доступ к свойствам объекта.
* `| to_datetime(timezone='...')` — форматирование меток времени.
* `| to_json` — экранирование специальных символов для совместимости с JSON.
* `{% if condition %}` — условные блоки.
* `{% for item in data %}` — итерация по массивам.

Дополнительные возможности выражений см. в [Справочнике по выражениям](../reference.md "Ознакомьтесь с выражениями рабочих процессов").

## Использование Workflows со Slack

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), чтобы создать новый рабочий процесс.
2. В панели **Choose trigger** выберите триггер, наиболее подходящий для ваших нужд.
3. На узле триггера выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), чтобы просмотреть доступные действия.
4. В панели **Choose action** найдите `slack` и выберите **Send message**.
5. Выберите предварительно настроенное подключение Slack.
6. Выберите канал для отправки сообщения.

   Используйте идентификатор канала Slack

   Мы рекомендуем использовать идентификатор канала Slack. Вы также можете использовать имя канала Slack или идентификатор канала Slack; однако не все функции действия **Send Message** будут доступны.
7. Укажите тело сообщения.
   Отформатируйте сообщение с помощью [Slack Markdown](https://api.slack.com/reference/surfaces/formatting#basics). Также можно использовать [выражения рабочих процессов](../reference.md "Ознакомьтесь с выражениями рабочих процессов") в качестве входных данных.
8. Чтобы протестировать ваш рабочий процесс, выберите **Run**.

## Устранение неполадок

Ниже приведены решения проблем, с которыми столкнулись некоторые пользователи при интеграции со Slack.

* [Ошибка недействительного подключения для Slack](https://dt-url.net/2503800)
* [Ошибка отсутствия обязательных полей в Slack](https://dt-url.net/596382w)
* [Канал Slack не отображается в списке доступных каналов](https://dt-url.net/tq038te)
* [Ошибка недостаточных разрешений в Slack](https://dt-url.net/09438li)
* [Вложение текстового файла отображается как бинарный файл](https://dt-url.net/z423x5i)

## Связанные темы

* [Отправка уведомлений Slack о проблемах](../../alerting-and-notifications/workflows-tutorial-problems-slack.md "Узнайте, как отправлять уведомления Slack о проблемах с помощью простого рабочего процесса.")
