---
title: Удалённое управление конфигурацией OneAgent и ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/bulk-configuration
scraped: 2026-05-12T11:55:00.738795
---

# Удалённое управление конфигурацией OneAgent и ActiveGate

# Удалённое управление конфигурацией OneAgent и ActiveGate

* How-to guide
* 9-min read
* Published May 31, 2022

Используйте удалённое управление конфигурацией, чтобы настраивать несколько OneAgent или ActiveGate одной командой вместо выполнения одних и тех же действий по одному (будь то при установке, путём редактирования конфигурационных файлов или с помощью инструмента командной строки `oneagentctl`).

При использовании удалённого управления конфигурацией действие по-прежнему выполняется на соответствующих хостах, но вы инициируете и контролируете его централизованно через **Deployment Status** в веб-интерфейсе Dynatrace или через API Dynatrace.

Прежде чем начать, ознакомьтесь с [возможностями](#capabilities) и [ограничениями](#limitations), чтобы убедиться, что удалённое управление конфигурацией подходит для ваших нужд и вашего развёртывания.

## Возможности

С помощью удалённого управления конфигурацией вы можете одной командой выполнить любое из следующих действий для нескольких OneAgent или ActiveGate, соответствующих требованиям к версии.

### OneAgent

| Действие | Требуемая версия Dynatrace | Требуемая версия OneAgent |
| --- | --- | --- |
| Назначение [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.") | 1.252+ | 1.237+ |
| Назначение [сетевой зоны](/managed/manage/network-zones/oneagent-connectivity "Узнайте, как сетевые зоны определяют приоритет ActiveGate для подключения OneAgent.") | 1.252+ | 1.237+ |
| Назначение [тегов](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#tags "Узнайте, как добавлять теги и задавать дополнительные свойства для мониторируемого хоста.") | 1.268+ | 1.263+ |
| Назначение [свойств](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Узнайте, как добавлять теги и задавать дополнительные свойства для мониторируемого хоста.") | 1.268+ | 1.263+ |
| Назначение параметров связи | 1.294+ | 1.285+ |

### ActiveGate

| Действие | Требуемая версия Dynatrace | Требуемая версия ActiveGate |
| --- | --- | --- |
| Назначение [группы ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#group "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.") | 1.252+ | 1.237+ |
| Назначение [сетевой зоны](/managed/manage/network-zones/activegate-connectivity "Узнайте, как сетевые зоны определяют приоритет ActiveGate для подключения Environment ActiveGate.") | 1.252+ | 1.237+ |

Удалённое управление конфигурацией работает для OneAgent в режимах Full-Stack и Infrastructure Monitoring, а также для хост-ориентированных ActiveGate. OneAgent и ActiveGate должны поддерживать связь с вашим окружением.

## Ограничения

Удалённое управление конфигурацией НЕ работает с:

* OneAgent, развёрнутым с помощью Dynatrace Operator
* OneAgent в режиме Application-only
* OneAgent на Solaris
* Контейнеризованными ActiveGate

Назначение параметров связи можно выполнить только через веб-интерфейс.

## Разрешения

Рекомендуем ограничить количество пользователей, которым разрешено использовать удалённое управление конфигурацией. Несколько пользователей, выполняющих настройку одновременно, могут не знать о действиях друг друга. Это относится как к веб-интерфейсу, так и к API. Разрешения IAM обеспечивают очень детальный контроль, что позволяет избежать конфликтов.

### Разрешения IAM

Пользователи, выполняющие удалённое управление конфигурацией, должны состоять в группе, привязанной к политике со следующими разрешениями IAM:

* `deployment:oneagents.network-zones:write`
* `deployment:oneagents.host-groups:write`
* `deployment:oneagents.host-tags:write`
* `deployment:oneagents.host-properties:write`

* `deployment:oneagents.communication-settings:write`

* `deployment:activegates.network-zones:write`
* `deployment:activegates.groups:write`

С помощью разрешений IAM можно ограничить действия пользователя до одного конфигурационного действия, например разрешить только изменение назначения группы хостов OneAgent.

Дополнительные сведения о разрешениях IAM в Dynatrace смотрите в разделе [Работа с политиками](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками").

### Токены доступа

Для внесения изменений в конфигурацию через API Dynatrace необходим [токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Узнайте о концепции токена доступа и его областях.") со следующими областями:

* **Write OneAgents** (`oneAgents.write`) — для проверки полезной нагрузки, создания предварительного просмотра и запуска изменения конфигурации для OneAgent
* **Write ActiveGates** (`activeGates.write`) — для проверки полезной нагрузки, создания предварительного просмотра и запуска изменения конфигурации для ActiveGate

### Администраторы кластера

Назначение параметров связи для OneAgent может быть выполнено без дополнительных настроек администраторами кластера Dynatrace Managed.

## Процедуры через веб-интерфейс

Рабочий процесс удалённой настройки через веб-интерфейс Dynatrace аналогичен для OneAgent и ActiveGate.

### Настройка OneAgent

Вы можете назначить нескольким OneAgent следующие параметры:

* Группа хостов
* Сетевая зона
* Теги
* Свойства

Чтобы обновить несколько OneAgent по любому из указанных параметров:

1. Перейдите в **Deployment Status** > **OneAgents**.
2. Отфильтруйте и выберите OneAgent, которые необходимо настроить. Можно использовать флажок ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") в заголовке таблицы для выбора всех отфильтрованных OneAgent или выбирать их по одному.

   После выбора OneAgent в нижней части страницы появляется панель редактирования.
3. Выберите изменение конфигурации, которое необходимо выполнить.

   * изменить группу хостов
   * изменить сетевую зону
   * изменить теги хоста
   * изменить свойства хоста
4. Нажмите **Run action**.

   Откроется мастер **Remote configuration management** для внесения изменений в конфигурацию выбранных OneAgent. Изменения не применяются до тех пор, пока вы не нажмёте **Apply changes** и не подтвердите необходимые перезапуски. До этого момента можно изменить или отменить действие.
5. Укажите изменение, которое необходимо применить ко всем выбранным OneAgent. В зависимости от выбранного действия можно:

   * Добавить или удалить назначение группы хостов
   * Добавить или удалить назначение сетевой зоны
   * Добавить или удалить теги хоста
   * Добавить или удалить свойства хоста
6. Нажмите **Next**.
7. Проверьте внесённые изменения.
8. Нажмите **Apply changes**.
9. Нажмите **Continue**, чтобы запустить массовое действие.

   * OneAgent будет перезапущен для применения изменений назначения сетевой зоны, назначения группы хостов, а также тегов и свойств в Dynatrace версии 1.308+.
   * При изменении назначения группы хостов необходимо вручную перезапустить процессы, внедрённые OneAgent. Перезапуск внедрённых процессов при изменении назначения сетевой зоны не требуется.
10. Пока массовое действие выполняется, строка состояния в верхней части страницы **Deployment status** информирует вас о ходе выполнения. Нельзя запустить другое массовое действие до завершения текущего.

Изменение сетевых зон и групп хостов может занять до 10 минут. Удаление свойств и тегов хоста может занять до семи часов.

### Настройка параметров связи OneAgent

Версия кластера целевого окружения должна быть не ниже версии OneAgent.

Чтобы обновить параметры связи нескольких OneAgent:

1. Перейдите в **Deployment Status** > **OneAgents**.
2. Отфильтруйте и выберите OneAgent, которые необходимо настроить. Можно использовать флажок ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") в заголовке таблицы для выбора всех отфильтрованных OneAgent или выбирать их по одному.

   После выбора OneAgent в нижней части страницы появляется панель редактирования.
3. Выберите **modify communication settings**.
4. Нажмите **Run action**.

   Откроется мастер **Remote configuration management** для внесения изменений в конфигурацию выбранных OneAgent. Изменения не применяются до тех пор, пока вы не нажмёте **Apply changes** и не подтвердите необходимые перезапуски. До этого момента можно изменить или отменить действие.
5. Выберите **target environment**.
6. Укажите URL целевого окружения.
7. Нажмите **Next**.
8. Укажите свойства параметров связи:

   * **Tenant token**
   * **Communication endpoints**
9. Нажмите **Next**.
10. Запустите **Connection test**. Можно просмотреть выбранные версии OneAgent, сетевые зоны и используемые ими ActiveGate. После запуска теста подключения статус каждого OneAgent отображается в таблице. Перейти к следующему шагу можно после завершения теста подключения. Обновить можно только те OneAgent, которые успешно протестировали новые параметры подключения.
11. Нажмите **Next**.
12. Нажмите **Apply changes**.
13. Пока массовое действие выполняется, строка состояния в верхней части страницы **Deployment status** информирует вас о ходе выполнения. Нельзя запустить другое массовое действие до завершения текущего.

Обновлённые OneAgent перезапустятся автоматически и станут доступны в целевом окружении в течение до 10 минут. После изменения конфигурации они прекратят передавать данные в исходное окружение. Однако для их перевода в статус отключённых может потребоваться до 10 минут.

Чтобы повторно включить полный мониторинг стека для мониторируемых процессов, необходимо перезапустить их вручную.

### Настройка ActiveGate

Вы можете назначить нескольким ActiveGate следующие параметры:

* Группа ActiveGate
* Сетевая зона

Чтобы обновить несколько ActiveGate по любому из указанных параметров:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Отфильтруйте и выберите ActiveGate, которые необходимо настроить. Можно использовать флажок ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") в заголовке таблицы для выбора всех отфильтрованных ActiveGate или выбирать их по одному.
3. После выбора ActiveGate в нижней части страницы появляется панель редактирования.
4. Выберите изменение конфигурации, которое необходимо выполнить.

   * изменить группу ActiveGate
   * изменить сетевую зону
5. Выберите нужную конфигурацию и нажмите **Run action**.

   Откроется мастер **Remote configuration management** для внесения изменений в конфигурацию выбранных ActiveGate. Изменения не применяются до тех пор, пока вы не нажмёте **Apply changes** и не подтвердите необходимые перезапуски. До этого момента можно изменить или отменить действие.
6. Укажите изменение, которое необходимо применить ко всем выбранным ActiveGate. В зависимости от выбранного действия можно:

   * Добавить или удалить назначение группы ActiveGate
   * Добавить или удалить назначение сетевой зоны
7. Нажмите **Next**.
8. Проверьте внесённые изменения.
9. Нажмите **Apply changes**, чтобы запустить массовое действие.
10. Пока массовое действие выполняется, строка в верхней части страницы **Deployment status** информирует вас о ходе выполнения. Не запускайте другое массовое действие до завершения текущего. Перезапуск ActiveGate для применения изменений не требуется.

Применение изменений может занять до 10 минут.

## Процедуры через API

API Dynatrace содержит набор эндпоинтов для безопасного и контролируемого удалённого управления конфигурацией.

Дополнительные сведения смотрите в разделе [API удалённого управления конфигурацией](/managed/dynatrace-api/environment-api/remote-configuration "Узнайте, что предлагает API удалённого управления конфигурацией.").

### Пример управления конфигурацией OneAgent

Ниже приведён пример назначения нескольких OneAgent группе хостов через API Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Фильтрация OneAgent для настройки**](/managed/ingest-from/bulk-configuration#step-1 "Выполнение конфигурации OneAgent и ActiveGate на хостах со страницы Deployment status или массово через API Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создание полезной нагрузки**](/managed/ingest-from/bulk-configuration#step-2 "Выполнение конфигурации OneAgent и ActiveGate на хостах со страницы Deployment status или массово через API Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Проверка полезной нагрузки**](/managed/ingest-from/bulk-configuration#step-3 "Выполнение конфигурации OneAgent и ActiveGate на хостах со страницы Deployment status или массово через API Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Создание предварительного просмотра**](/managed/ingest-from/bulk-configuration#step-4 "Выполнение конфигурации OneAgent и ActiveGate на хостах со страницы Deployment status или массово через API Dynatrace.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Запуск массовой настройки**](/managed/ingest-from/bulk-configuration#step-5 "Выполнение конфигурации OneAgent и ActiveGate на хостах со страницы Deployment status или массово через API Dynatrace.")

### Шаг 1. Фильтрация OneAgent для настройки

Используйте эндпоинт [API OneAgent на хосте](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через API Dynatrace."), чтобы указать список OneAgent, для которых необходимо изменить назначение хоста.

В качестве критериев фильтрации можно использовать любые доступные свойства OneAgent. Например, чтобы получить список всех OneAgent, установленных на Windows, выполните следующий запрос.

```
curl --request GET \



--url 'https://myenvironment.com/api/v2/oneagents?osType=WINDOWS \



--header 'Authorization: Api-Token <token>'
```

### Шаг 2. Создание полезной нагрузки

Полезная нагрузка содержит список OneAgent, для которых будет выполнено массовое действие, и его параметры. Приведённая ниже полезная нагрузка изменит назначение группы хостов на `some-host-group` для трёх указанных OneAgent, идентифицированных по их идентификаторам хостов.

```
{



"entities": ["HOST-0000000000000001", "HOST-0000000000000002", "HOST-0000000000000003"],



"operations": [



{



"operation": "SET",



"attribute": "hostGroup",



"value": "some-host-group"



}



]



}
```

### Шаг 3. Проверка полезной нагрузки

Перед запуском задания конфигурации можно проверить созданную полезную нагрузку, выполнив следующий запрос. В приведённом ниже примере полезная нагрузка передаётся в запрос в виде файла `payload.json`.

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement/validator \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

Корректная полезная нагрузка возвращает ответ `HTTP 204`. Некорректная нагрузка возвращает ответ с описанием нарушения.

### Шаг 4. Создание предварительного просмотра

Перед внесением фактического изменения конфигурации можно создать предварительный просмотр. Он содержит информацию о том, сколько объектов в данный момент настроено в соответствии с полезной нагрузкой и сколько будет настроено после отправки запроса на изменение.

Шаг предварительного просмотра не поддерживается для тегов и свойств.

Чтобы запустить предварительный просмотр, выполните следующий запрос:

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement/preview \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

Ответ содержит информацию о том, сколько OneAgent назначено группе хостов и сколько будет назначено после завершения настройки.

```
{



"previews": [



{



"operation": "SET",



"attribute": "hostgroup",



"existingEntitiesCount": 3,



"targetEntitiesCount": 6



}



]



}
```

### Шаг 5. Запуск массовой настройки

Чтобы запустить массовую настройку, выполните следующий запрос:

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

Успешный запрос возвращает ответ `HTTP 201`, означающий, что задание конфигурации запущено. Изменение применяется не мгновенно. Каждый OneAgent сначала выполняет настройку самостоятельно, затем отправляет информацию в ваше окружение, после чего кластер Dynatrace обновляет назначение группы хостов. Применение изменений в вашем окружении может занять до 10 минут.

Проверить изменение можно, выполнив запрос [API OneAgent на хосте](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через API Dynatrace.") с фильтром по группе хостов, в которую вы только что добавили хосты.

```
curl --request GET \



--url 'https://myenvironment.com/api/v2/oneagents?hostGroupName=some-host-group \



--header 'Authorization: Api-Token <token>'
```

Ответ должен содержать три идентификатора хостов, добавленных в задание конфигурации.

### Настройка параметров связи OneAgent

Версия кластера целевого окружения должна быть не ниже версии OneAgent.

Чтобы изменить назначение хоста для OneAgent:

1. Выполните [вызов API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Проверка конфигурации экземпляров OneAgent на ваших хостах через API Dynatrace."), чтобы отфильтровать OneAgent, для которых необходимо изменить назначение хоста.
2. Выполните [вызов API](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр информации о подключении OneAgent через API Dynatrace."), чтобы получить следующие параметры целевого окружения:

   * tenantUUID
   * tenantToken
   * formattedCommunicationEndpoints
3. Выполните следующий [вызов API](/managed/dynatrace-api/environment-api/remote-configuration/oneagent/post-dry-run "Проверка возможности подключения хостов к целевому окружению."), чтобы убедиться, что хосты могут взаимодействовать с целевым окружением:

   Требуемая область токена: `oneAgents.write`.

   ```
   POST https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/managedRemoteCommunicationSettings/dryRun



   accept: application/json; charset=utf-8



   Authorization: Api-Token <TOKEN>



   Content-Type: application/json



   {



   "additionalCommunicationAddresses": "<formattedCommunicationEndpoints>",



   "entities": [



   "<HOST-1>",



   "<HOST-2>"



   ],



   "environmentId": "<tenantUUID>",



   "proxy": "{optional proxy parameter}",



   "tenantToken": "<tenantToken>"



   }
   ```

   Если `processedEntitiesCount` меньше `totalEntitiesCount`, выполните следующий вызов API для проверки статуса задачи:

   ```
   GET https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/remoteConfigurationManagement/<task-id>



   Authorization: Api-Token <TOKEN>
   ```

   Повторяйте запрос до получения ошибки или до тех пор, пока `processedEntitiesCount` не станет равным `totalEntitiesCount`. Формат ответа аналогичен пробному запуску. Требуемая область токена: `oneAgents.read`.
4. Выполните следующий [вызов API](/managed/dynatrace-api/environment-api/remote-configuration/oneagent/execute-migration "Миграция хостов в целевое окружение.") для завершения миграции:

   Выполняйте вызов только при успешном пробном запуске. Требуемая область токена: `oneAgents.write`.

   ```
   POST https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/managedRemoteCommunicationSettings/execute



   accept: application/json; charset=utf-8



   Authorization: Api-Token <TOKEN>



   Content-Type: application/json



   {



   ... same payload like for dryRun



   }
   ```

   Формат ответа аналогичен пробному запуску.

   Обновлённые OneAgent перезапустятся автоматически и станут доступны в целевом окружении в течение до 10 минут. После изменения конфигурации они прекратят передавать данные в исходное окружение. Однако для их перевода в статус отключённых может потребоваться до 10 минут.

   Выполните следующий вызов API для проверки статуса задачи и убедитесь, что миграция завершена:

   ```
   GET https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/remoteConfigurationManagement/<task-id>



   Authorization: Api-Token <TOKEN>
   ```