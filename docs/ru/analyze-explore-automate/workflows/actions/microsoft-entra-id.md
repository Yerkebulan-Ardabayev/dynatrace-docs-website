---
title: Microsoft Entra ID Коннектор
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id
scraped: 2026-03-05T21:39:12.282254
---

# Microsoft Entra ID Connector


* Latest Dynatrace
* 5-min read

Ваше окружение Dynatrace может интегрироваться с Microsoft Entra ID (ранее Azure Active Directory) в автоматизированных [рабочих процессах (workflows)](../../workflows.md "Automate IT processes with Dynatrace Workflows—react to events, schedule tasks, and connect services.").
Microsoft Entra ID Connector ![Microsoft Entra ID Connector](https://dt-cdn.net/hub/app_icon_entra_id_new.png "Microsoft Entra ID Connector") позволяет использовать готовые действия в Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") для автоматизации импорта команд из Entra ID (по различным триггерам) для определения владения сущностями и других сценариев использования в Dynatrace.
Microsoft Entra ID Connector подключается к Azure Cloud через [Microsoft Graph API](https://developer.microsoft.com/en-us/graph).

## Настройка

1. Разрешение внешних запросов

Внешние запросы позволяют осуществлять исходящие сетевые подключения из вашего окружения Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с функциями приложений и функциями в Dashboards, Notebooks и Automations.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Выберите  **New host pattern**.
3. Добавьте доменные имена.
4. Выберите **Add**.

Таким образом вы можете детально контролировать, к каким веб-сервисам могут подключаться ваши функции.

Вам необходимо добавить следующие доменные имена: `login.microsoftonline.com` и `graph.microsoft.com`.

2. Предоставление разрешений для Workflows

Workflows требует определённых разрешений для выполнения действий от вашего имени. Действия, входящие в состав Connector, требуют дополнительных разрешений.

Чтобы настроить разрешения, предоставленные Workflows

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и откройте **Settings** > **Authorization settings**.
2. Выберите следующие разрешения помимо общих разрешений Workflows.

   * `app-settings:objects:read`

Подробнее об общих пользовательских разрешениях Workflows см. в разделе [Пользовательские разрешения для workflows](../security.md#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

3. Настройка интеграции с Dynatrace

Настройте тенант Microsoft Azure для установления соединения с вашим окружением Dynatrace.

1. Откройте `portal.azure.com` для доступа к вашему тенанту Microsoft Azure.
2. Перейдите в **App registrations** для настройки нового приложения.

   Необходимые шаги по настройке описаны в разделе [Регистрация клиентского приложения в Azure Active Directory](https://dt-url.net/3w239qt).
3. Предоставьте вашему новому приложению Azure разрешение `Group.Read.All`.

   Для получения дополнительной информации см. [API Permissions](https://dt-url.net/v8439p2) и [Введение в разрешения и согласие](https://dt-url.net/7g639wa).
4. После регистрации приложения создайте новый секрет клиента. Подробности см. в разделе [Certificates & secrets](https://dt-url.net/bt839gp).

   * Для создания секрета клиента убедитесь, что у вас есть права администратора или вы являетесь владельцем приложения.
   * Обязательно сохраните **Value** (значение) секрета клиента (не **Secret ID**) после создания — оно понадобится для установления соединения с вашим окружением Dynatrace.

4. Авторизация подключения

Microsoft Entra ID Connector требует секрет клиента из Microsoft Azure для авторизации.

1. Получите следующие учётные данные из регистрации приложения в вашем тенанте Microsoft Azure на `portal.azure.com`.

   * Directory (tenant) ID: доступен в меню **Overview**
   * Application (client) ID: доступен в меню **Overview**
   * Client secret: **Value** (значение, не **Secret ID**) секрета клиента из предыдущего раздела [Настройка Microsoft Azure для интеграции с Dynatrace](#set-up-azure)
2. Вернитесь в Dynatrace, перейдите в **Settings** ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") > **Connections** > **Microsoft Entra ID**.
3. Выберите **Add item** и укажите следующую информацию.

   * **Connection name**: должно быть уникальным. Оно будет отображаться и доступно для выбора в поле подключения в Microsoft Entra ID Connector.
   * **Directory (tenant) ID**
   * **Application (client) ID**
   * **Type**: `Client secret`
   * **Client Secret**: это **Value** (значение) секрета клиента из раздела [Настройка Microsoft Azure для интеграции с Dynatrace](#set-up-azure).
4. Выберите **Create**.

#### Дополнительные примечания

* Для добавления настроек подключения вам необходимы следующие разрешения.

  ```
  ALLOW settings:objects:read, settings:objects:write, settings:schemas:read WHERE settings:schemaId = "app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection"
  ```

  Подробности см. в разделе [Разрешения и доступ](../../../manage/settings/settings-20.md#permissions-and-access "Introduction to the Settings 2.0 framework").

## Получение групп из Entra ID в рабочих процессах автоматизации

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow** в правом верхнем углу страницы.
2. В боковой панели выберите триггер, наиболее подходящий для ваших задач.
3. На узле триггера выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), чтобы просмотреть доступные действия.
4. В боковой панели **Choose action** найдите **Microsoft Entra ID** и выберите **Get groups**.
5. Во входных данных действия (**Input**) вы можете указать конкретные группы в **$filter**, если хотите отфильтровать результаты. Аналогично, в **$select** укажите, какие поля вы хотите получить из Entra ID. Синтаксис основан на [документации Entra ID API](https://dt-url.net/azure-api-docs).

   Важно для импорта групп Entra ID как [команд владения](../../../deliver/ownership/ownership-teams.md "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership."):

   * Вы всегда должны включать `id` и `displayName` в `$select`; эти поля сопоставляются с **Team identifier** (идентификатор команды) и **Team name** (название команды) импортированной команды владения соответственно.
   * Мы рекомендуем всегда включать параметр `mailNickname` в `get_groups`. Это поле имеет уникальные значения в Entra ID и устанавливается как уникальный, человекочитаемый **Supplementary Identifier** (дополнительный идентификатор) для вашей импортированной команды владения в Dynatrace.
   * **Object Id** из Entra ID, импортированный через параметр `id`, устанавливается как уникальный **Team identifier** (идентификатор команды), а также как **External ID** (внешний идентификатор) импортированной команды владения.
   * Параметр `mail` устанавливается как **Email** импортированной команды владения.

   ![Get groups input fields](https://dt-cdn.net/images/azure-connector-get-groups-input-698-0609c7d9dc.webp)
6. При необходимости добавьте действие **Import teams** (предоставляемое приложением [Ownership](../../../deliver/ownership-app.md#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information.") ![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership")), чтобы сохранить информацию о группах Entra ID как [команды владения](../../../deliver/ownership/ownership-teams.md "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") в **Settings** Dynatrace. Затем вы можете [назначить эти импортированные команды в качестве владельцев](../../../deliver/ownership/assign-ownership.md "Assign owners to entities using entity metadata like labels, environment variables, and tags.") любой отслеживаемой сущности в Dynatrace.
7. Для тестирования рабочего процесса выберите **Run**.

### Результат действия

Результатом `get_groups` является JSON-массив, где каждая запись представляет отдельную группу пользователей. Если при настройке действия для **$count** установлено значение `true`, панель **Results** отображает количество импортированных групп.

Значение `directory_id`, отображаемое в результатах, — это идентификатор тенанта Azure.

Ниже показан журнал успешного выполнения.

```
[INFO]    Successfully retrieved connection settings.


[INFO]    Successfully fetched authentication token.


[INFO]    Calling Entra-ID groups endpoint with the following query params: $filter=startswith(displayName, 'team-deco')&$select=id,displayName,description,mail,mailNickname&$count=true&$top=999


[INFO]    Successfully fetched Groups from Entra-ID.
```