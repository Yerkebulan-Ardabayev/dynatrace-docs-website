---
title: PagerDuty
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/pagerduty
scraped: 2026-03-06T21:27:05.600890
---

# PagerDuty


* Latest Dynatrace
* 5-min read
* Updated on May 07, 2025

Ваша среда Dynatrace может интегрироваться со средой PagerDuty с помощью PagerDuty Connector ![PagerDuty](https://dt-cdn.net/images/pagerduty-for-workflows-257-0cd4ce0d3a.png "PagerDuty"), что позволяет автоматически создавать инциденты на основе ваших данных мониторинга.

## Настройка интеграции

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Предоставление разрешений для Workflows**](pagerduty.md#permissions "Automate creation of incidents in PagerDuty based on your monitoring data and events.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание API-ключа PagerDuty**](pagerduty.md#api-key "Automate creation of incidents in PagerDuty based on your monitoring data and events.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Настройка подключения PagerDuty**](pagerduty.md#connection "Automate creation of incidents in PagerDuty based on your monitoring data and events.")

### Шаг 1. Предоставление разрешений для Workflows

Некоторые разрешения необходимы для Workflows, чтобы выполнять действия от вашего имени. Другие разрешения требуются для действий, поставляемых вместе с PagerDuty Connector.

Для настройки разрешений, предоставленных Workflows

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения помимо общих разрешений Workflows.

   * `app-settings:objects:read`
   * `state:app-states:read`
   * `state:app-states:write`
   * `state:app-states:delete`

Подробнее об общих разрешениях пользователей Workflows см. в разделе [Пользовательские разрешения для Workflows](../security.md#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Шаг 2. Создание API-ключа PagerDuty

Для взаимодействия с PagerDuty вам понадобится API-ключ. Чтобы узнать, как его получить, обратитесь к [официальной документации PagerDuty](https://dt-url.net/jo03j4l).

### Шаг 3. Настройка подключения PagerDuty

Вам необходимо настроить подключение для каждой из ваших сред PagerDuty.

Для настройки подключения

1. Перейдите в **Settings** и выберите **Connections** > **Connectors** > **PagerDuty**.
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
3. Укажите понятное имя для вашего подключения.
4. При необходимости измените URL API PagerDuty.
5. Укажите ваш API-ключ PagerDuty.
6. Выберите **Create**.

## Доступные действия

Следующие действия рабочих процессов доступны для интеграции PagerDuty. Каждое действие соответствует конечной точке API PagerDuty.

## Создание инцидента PagerDuty

Для создания инцидента необходимо предоставить перечисленную ниже информацию. Вы можете задать значения напрямую в действии **Create an incident** или извлечь их из PagerDuty с помощью соответствующего действия.

| Поле | Описание | Обязательность |
| --- | --- | --- |
| From | Идентификатор пользователя, создающего инцидент | Обязательно |
| Title | Заголовок инцидента | Обязательно |
| Service ID | Идентификатор сервиса в вашей среде PagerDuty | Обязательно |
| Urgency | Срочность инцидента | Необязательно |
| Additional incident details | Описание инцидента | Необязательно |
| Assignee ID | Идентификатор назначенного ответственного за инцидент | Необязательно |
| Escalation policy ID | Идентификатор политики эскалации | Необязательно |
| Conference number | Номер телефона конференц-связи для конференц-моста | Необязательно |
| Conference URL | URL конференц-моста, например ссылка на веб-конференцию или канал Slack | Необязательно |
| Incident key | Уникальный идентификатор данного инцидента. В большинстве случаев это идентификатор события Dynatrace. | Необязательно |

Подробнее о каждом параметре см. в разделе [Create an incident](https://dt-url.net/b723jjs) в официальной документации PagerDuty.

Для создания рабочего процесса, создающего инцидент PagerDuty

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), чтобы создать новый рабочий процесс.
2. В панели **Choose trigger** выберите триггер, наиболее подходящий для ваших потребностей.
3. На узле триггера выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), чтобы просмотреть доступные действия.
4. (Необязательно) В панели **Choose action** найдите `PagerDuty` и выберите одно из действий по извлечению информации.
5. (Необязательно) При необходимости добавьте дополнительные действия по извлечению информации. Убедитесь, что они размещены параллельно.
6. На одном из узлов извлечения информации выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), найдите `PagerDuty` и выберите **Create an incident**.
7. На каждом из оставшихся узлов извлечения информации выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") и перетащите линию к действию **Create an incident**.
8. В действии **Create an incident** выберите [подключение](#connection) к вашей среде PagerDuty.
9. Настройте поля ввода по мере необходимости. Чтобы узнать, как использовать выходные данные узлов извлечения информации, см. [Справочник выражений](../reference.md "Get to know the workflows expression").
10. Для тестирования рабочего процесса выберите **Run**.

## Устранение неполадок

Ниже приведены решения проблем, с которыми сталкиваются некоторые пользователи.

* [PagerDuty: ошибка отсутствия обязательных полей](https://dt-url.net/gt038mx)
* [PagerDuty: ошибка недостаточных разрешений](https://dt-url.net/2e23837)
