---
title: Red Hat Событийно-ориентированное Ansible
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-even-driven-ansible
scraped: 2026-03-03T21:30:53.933975
---

# Red Hat Event-Driven Ansible


* Latest Dynatrace
* Предварительный просмотр

Предварительный просмотр

При интеграции вашей среды Dynatrace с контроллером Red Hat Event-Driven Ansible с помощью коннектора Red Hat Ansible ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows")
вы можете автоматически отправлять события в контроллер Event-Driven Ansible, используя плагин источника событий dt\_webhook.

## Настройка интеграции

Для использования действий рабочих процессов Red Hat Ansible необходимо сначала установить коннектор Red Hat Ansible ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows") из Dynatrace Hub.

1. В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") выберите **Red Hat Ansible**.
2. Выберите **Install**, а затем следуйте описанному ниже процессу для настройки среды Event-Driven Ansible, предоставления разрешений и настройки подключения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройка контроллера Event-Driven Ansible для интеграции с Dynatrace**](redhat-even-driven-ansible.md#setup-eda "Отправка событий в Red Hat Event-Driven Ansible")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Предоставление разрешений для Workflows**](redhat-even-driven-ansible.md#permissions "Отправка событий в Red Hat Event-Driven Ansible")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка подключения к Red Hat Event-Driven Ansible**](redhat-even-driven-ansible.md#connection "Отправка событий в Red Hat Event-Driven Ansible")

### Шаг 1. Конфигурация контроллера Event-Driven Ansible

Дополнительную информацию о контроллере Event-Driven Ansible см. в [руководстве пользователя контроллера Event-Driven Ansible](https://dt-url.net/7xg3n92).

#### Конфигурация проекта

Дополнительную информацию о настройке проекта см. в [руководстве пользователя контроллера Event-Driven Ansible](https://dt-url.net/p1i3n2u).

#### Event-Driven Ansible с упрощённой маршрутизацией событий (потоки событий)

##### Предварительные требования

* Red Hat Ansible Automation Platform 2.5+

#### Настройка среды принятия решений

При использовании потоков событий вы можете использовать стандартную среду принятия решений, предоставляемую Red Hat, например [Ansible-rulebook default-de](https://dt-url.net/oq03zp2).
При использовании потоков событий вам не нужно создавать пользовательскую среду принятия решений.

##### Конфигурация учётных данных

Перед созданием потока событий необходимо настроить учётные данные для аутентификации по токену.

1. В навигационной панели дашборда Ansible Automation Platform выберите **Automation Decisions** > **Infrastructure** > **Credentials**.
2. Выберите **Create credential**.
3. Введите следующие данные учётных данных.

Дополнительную информацию о настройке учётных данных см. в [разделе «Настройка учётных данных»](https://dt-url.net/6c23znj) в документации Red Hat.

##### Конфигурация потока событий

После настройки учётных данных вы можете создать поток событий.

1. В навигационной панели Ansible Automation Platform выберите **Automation Decisions** > **Event streams**.
2. Выберите **Create event stream**.
3. Введите следующие данные потока событий.

Дополнительную информацию о настройке потока событий см. в [разделе «Упрощённая маршрутизация событий»](https://dt-url.net/sv63zyi) в документации Red Hat.

##### Активация рулбука

Последний шаг — привязка созданного потока событий к активации рулбука.

1. В навигационной панели контроллера Event-Driven Ansible выберите **Rulebook Activations**.
2. Выберите **Create rulebook activation** и заполните обязательные поля.
3. Выберите поток событий:

   1. Нажмите значок шестерёнки и выберите `_SOURCE_1` из списка.
   2. Выберите поток событий, созданный на предыдущем шаге, и сохраните его.

   Дополнительную информацию о привязке потока событий к активации рулбука см. в [разделе «Привязка потоков событий к активациям»](https://dt-url.net/tka3z5c) в документации Red Hat.

Когда активация рулбука включена, события могут отправляться из действия рабочего процесса в контроллер Event-Driven Ansible.

Дополнительную информацию о настройке активации рулбука на контроллере Event-Driven Ansible см. в [разделе «Настройка активации рулбука»](https://dt-url.net/ev63nil) в документации Red Hat.

#### Event-Driven Ansible без упрощённой маршрутизации событий (потоков событий)

#### Предварительные требования

Коллекция [dynatrace.event\_driven\_ansible](https://dt-url.net/9le3nc2), содержащая **dt\_webhook**, должна быть установлена в среде принятия решений на контроллере Event-Driven Ansible.

#### Настройка среды принятия решений

Дополнительную информацию о настройке новой среды принятия решений см. в [руководстве пользователя контроллера Event-Driven Ansible](https://dt-url.net/p603rfl).

#### Конфигурация плагина источника событий и рулбука

Активация рулбука используется для включения источника событий. Поэтому необходимо настроить рулбук.

Рулбук должен находиться в настроенном репозитории проекта в директории `/rulebooks`. Дополнительную информацию см. в [примере рулбука Event-Driven Ansible](https://dt-url.net/qr03nps).

Первая часть рулбука — конфигурация источника событий (плагина источника). Вторая часть конфигурации рулбука содержит сами правила. Правило включает условия и действия.

**Пример рулбука для dt\_webhook**

Для использования плагина [dt\_webhook](https://dt-url.net/5w23n6c) вам необходимо настроить его как источник в вашем рулбуке. Необходимо установить следующие аргументы.

* `host`

  + Это может быть, например, localhost или 0.0.0.0.
* `port`

  + Настройте порт, который будет использоваться плагином источника для прослушивания событий.
  + Подсказки:

    - URL API в **Red Hat Event-Driven Ansible Connection** имеет тот же `port`, что и определён здесь.
    - [Предварительное требование](https://dt-url.net/fu43nbr) для конфигурации порта.
* `token`

  + Определите здесь имя переменной для токена, например `dt_webhook_token`.
  + Подсказки:

    - Эта переменная токена будет установлена в активации рулбука позже на контроллере Red Hat Event-Driven Ansible.
    - `dt_webhook_token` — это просто пример имени переменной токена. Имя может быть другим, но оно должно совпадать в активации рулбука и конфигурации рулбука.

  ```
  ---


  - name: Listen for events on dt_webhook


  hosts: all


  sources:


  - dynatrace.event_driven_ansible.dt_webhook:


  host: 0.0.0.0


  port: 5000


  token: '{{ dt_webhook_token }}'


  rules:


  - name: API Endpoint not available


  condition: event.payload.eventData["event.name"] is match ("Monitoring not available")


  action:


  run_job_template:


  name: "Trigger test playbook"


  organization: "Default"
  ```

Когда конфигурация рулбука завершена, убедитесь, что ваш репозиторий проекта синхронизирован с контроллером Event-Driven Ansible, выбрав **Sync project** в списке проектов.

![Синхронизация проектов](https://dt-cdn.net/images/eda-project-sync-1917-a8723ab2bc.webp)

Следующий шаг — настройка активации рулбука. Выберите **Rulebook Activations** в навигационной панели контроллера Event-Driven Ansible.
Выберите **Create rulebook activation** и заполните обязательные поля.

В поле **Variables** вы определяете токен, устанавливая переменную токена из **конфигурации рулбука**. Переменные рулбука указываются в формате JSON/YAML.

Убедитесь, что имя переменной идентично в активации рулбука и конфигурации рулбука.

![Настройка активации рулбука](https://dt-cdn.net/images/eda-rulebook-activation-1918-d3fc9c9876.webp)

Дополнительную информацию о настройке активации рулбука на контроллере Event-Driven Ansible см. в [разделе «Настройка активации рулбука»](https://dt-url.net/ev63nil).

Когда активация рулбука включена, события могут отправляться из действия рабочего процесса в контроллер Event-Driven Ansible.

### Шаг 2. Предоставление разрешений для Workflows

Для выполнения действий от вашего имени Workflows требуются определённые разрешения.

Чтобы точно настроить разрешения, предоставленные Workflows:

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения помимо общего разрешения Workflows.

* `app-settings:objects:read`
* `state:app-states:read`
* `state:app-states:write`
* `state:app-states:delete`

Дополнительную информацию об общих пользовательских разрешениях Workflows см. в [Пользовательские разрешения для рабочих процессов](../../security.md#user-permission "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Workflows").

### Шаг 3. Настройка подключения к Red Hat Ansible

Вам необходимо настроенное подключение для ваших сред Red Hat Event-Driven Ansible.

Это подключение соединяется с плагином dt\_webhook в Red Hat Event-Driven Ansible. Откройте определённый порт в вашем брандмауэре, чтобы обеспечить доступность плагина для этих подключений.
Если это невозможно, вы можете использовать [EdgeConnect](https://dt-url.net/at03rhn) для туннелирования трафика и обеспечения доступности среды.

Чтобы настроить подключение для **контроллера Red Hat Event-Driven Ansible**:

1. Перейдите в **Settings** и выберите **Connections** > **Connectors** > **Red Hat Ansible**.
2. Выберите вкладку **Event-Driven Ansible**.
3. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Connection**.
4. Укажите понятное имя для вашего подключения.
5. Выберите, хотите ли вы использовать поток событий.
6. Укажите URL вашего контроллера Red Hat Event-Driven Ansible:

   * при неиспользовании потока событий: `http://your-eda-controller.redhat.com:your-port` (должен включать `port`, настроенный в рулбуке Ansible).
   * при использовании потока событий: `http://your-aap.redhat.com/eda-event-streams/api/eda/v1/external_event_stream/a-uuid/post`.
7. Укажите токен плагина источника Red Hat Event-Driven Ansible.
8. Выберите **Create**.

## Доступное действие

Для контроллера Red Hat Event-Driven Ansible доступно следующее действие рабочего процесса.

## Отправка события в Event-Driven Ansible

Чтобы отправить событие в Event-Driven Ansible из вашего рабочего процесса, вам необходимо предоставить информацию, перечисленную ниже.

| Поле | Описание | Обязательность |
| --- | --- | --- |
| Event data | Данные события для отправки в виде валидного JSON | Необязательно |

Чтобы создать рабочий процесс, отправляющий событие в Event-Driven Ansible:

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить"), чтобы создать новый рабочий процесс.
2. В панели **Choose trigger** выберите триггер, наиболее подходящий для ваших нужд.
3. На узле триггера выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить"), чтобы просмотреть доступные действия.
4. На одном из узлов извлечения информации выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить"), найдите `Ansible` и выберите **Send event to Event-Driven Ansible**.
5. На каждом из оставшихся узлов извлечения информации выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") и перетащите линию к действию **Send event to Event-Driven Ansible**.
6. В действии **Send event to Event-Driven Ansible** выберите [подключение](#connection) к вашему **контроллеру Red Hat Event-Driven Ansible**.
7. Настройте поле данных события по необходимости. Чтобы узнать, как использовать выходные данные узлов извлечения информации, см. Справочник по выражениям.

   Данные события должны быть валидным JSON.
8. Чтобы протестировать ваш рабочий процесс, выберите **Run**.
