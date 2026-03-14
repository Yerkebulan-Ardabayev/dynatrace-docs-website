---
title: Настройка GitLab Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-setup
scraped: 2026-03-06T21:36:42.472660
---

# Set up GitLab Connector

# Настройка GitLab Connector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 07, 2025

Используйте GitLab Connector ![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows") для интеграции вашей среды Dynatrace с репозиториями GitLab. Эта интеграция позволяет использовать действия GitLab Connector в вашем рабочем процессе для автоматического управления задачами и запросами на слияние на основе данных мониторинга и событий.

## Шаги

### Шаг 1. Добавление нового шаблона хоста во внешние запросы

Внешние запросы обеспечивают исходящие сетевые подключения из вашей среды Dynatrace к внешним сервисам. Они позволяют управлять доступом к публичным конечным точкам из AppEngine с функциями приложений, а также функциями в Dashboards, Notebooks и Automations.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
2. Выберите **New host pattern**.
3. Добавьте доменные имена.
4. Выберите **Add**.

Таким образом, вы можете детально управлять веб-сервисами, к которым могут подключаться ваши функции.

Необходимо добавить доменное имя `*.gitlab.com`.

### Шаг 2. Предоставление разрешений для Workflows

Помимо разрешений, необходимых Workflows для выполнения действий от вашего имени, существуют дополнительные разрешения, необходимые для использования действий GitLab Connector.

Для точной настройки разрешений, предоставляемых Workflows:

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующее разрешение в дополнение к общему разрешению Workflows:

* `app-settings:objects:read`

Для получения дополнительной информации о разрешениях пользователей Workflows см. раздел [Разрешения пользователей для рабочих процессов](../../security.md#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Шаг 3. Авторизация подключения к GitLab

Для каждой из ваших сред GitLab необходимо настроить отдельное подключение.

Для настройки подключения:

1. Перейдите в **Settings** и выберите **Connections** > **Connectors** > **GitLab**.
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
3. Определите параметры подключения к GitLab.

   * **Connection name**: Укажите понятное имя для вашего подключения.
   * **GitLab URL**: Добавьте URL вашей среды GitLab.
   * **GitLab token**: Укажите ваш токен API GitLab.
4. Выберите **Create**.

Токен GitLab должен иметь области видимости `api`, `read_repository`, `read_user` и `write_repository`.
Области видимости можно пропустить, если соответствующие действия не используются.
Обратитесь к документации GitLab для получения подробной информации о том, какая область видимости необходима для каждого действия.

## Связанные темы

* [Действия для GitLab Connector](gitlab-workflows-actions.md "List of available actions in GitLab Connector.")
* [GitLab Connector](../gitlab.md "Integrate Workflows with GitLab.")
