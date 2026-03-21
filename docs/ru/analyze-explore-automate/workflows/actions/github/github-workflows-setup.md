---
title: Настройка GitHub Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup
scraped: 2026-03-05T21:36:46.023049
---

Ваша среда Dynatrace может интегрироваться с репозиториями GitHub с помощью GitHub Connector ![GitHub](https://dt-cdn.net/images/github-for-workflows-new-lxjn9po-256-94579b3812.png "GitHub"). После настройки вы сможете использовать действия GitHub Connector в своём рабочем процессе для автоматического управления задачами и запросами на слияние на основе данных мониторинга и событий.

## Предварительное требование

Вам необходимо разрешение `app-engine:apps:install`.

## Шаги

### Шаг 1. Добавление нового шаблона хоста в раздел External requests

Внешние запросы обеспечивают исходящие сетевые соединения из вашей среды Dynatrace с внешними сервисами. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с помощью функций приложений и функций в Дашбордах, Блокнотах и Автоматизациях.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
2. Нажмите **New host pattern**.
3. Добавьте доменные имена.
4. Нажмите **Add**.

Таким образом вы можете детально управлять тем, к каким веб-сервисам могут подключаться ваши функции.

Вам необходимо добавить доменное имя `api.github.com`.

### Шаг 2. Предоставление разрешений для Workflows

Помимо разрешений, необходимых для выполнения действий от вашего имени в Workflows, существуют дополнительные разрешения, необходимые для использования действий GitHub Connector.

Для тонкой настройки разрешений, предоставленных Workflows

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения в дополнение к общему разрешению Workflows.

   * `app-settings:objects:read`

Для получения дополнительной информации об общих разрешениях пользователей Workflows см. [Разрешения пользователей для рабочих процессов](../../security.md#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Шаг 3. Авторизация подключения к GitHub

Вам необходимо настроить подключения для каждой из ваших сред GitHub.

Для настройки подключения

1. Создайте персональный токен доступа для своей учётной записи GitHub, как описано в разделе [Управление персональными токенами доступа](https://dt-url.net/icbd0ux9). Поддерживаются только облачные планы GitHub, например GitHub Enterprise Cloud. Планы GitHub Enterprise Server не поддерживаются.
2. Перейдите в **Settings** и выберите **Connections** > **Connectors** > **GitHub**.
3. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
4. Настройте подключение к GitHub.

   * **Connection name**: Укажите понятное и уникальное имя для подключения.
   * **GitHub Type**: Выберите тип механизма авторизации.
   * **GitHub token**: Укажите ваш токен GitHub API.
5. Нажмите **Create**.

Ограничьте разрешения персонального токена доступа

Мы настоятельно рекомендуем ограничить разрешения персональных токенов доступа до необходимого минимума. Необходимые разрешения для каждого действия можно найти на [странице GitHub Actions](github-workflows-actions.md "Integrate Workflows with GitHub services to utilize GitHub Connector actions."). Дополнительную информацию об ограничении доступа к определённому репозиторию или разрешений/областей видимости см. в разделе [Управление персональными токенами доступа](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). Это гарантирует, что ваш персональный токен доступа может использоваться только для доступа и изменения разрешённых репозиториев.

## Связанные темы

* [Действия для GitHub Connector](github-workflows-actions.md "Integrate Workflows with GitHub services to utilize GitHub Connector actions.")
