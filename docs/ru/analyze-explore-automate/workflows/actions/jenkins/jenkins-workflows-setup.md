---
title: Set up Jenkins Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/jenkins/jenkins-workflows-setup
scraped: 2026-03-05T21:30:53.886389
---

# Настройка Jenkins Connector

# Настройка Jenkins Connector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 07, 2025

### Шаг 1 Добавление нового шаблона хоста во внешние запросы

Внешние запросы позволяют устанавливать исходящие сетевые соединения из вашей среды Dynatrace с внешними сервисами. Они позволяют управлять доступом к публичным конечным точкам из AppEngine с помощью функций приложений и функций в дашбордах, Notebooks и Automations.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
2. Выберите **New host pattern**.
3. Добавьте доменные имена.
4. Нажмите **Add**.

Таким образом вы можете детально контролировать, к каким веб-сервисам могут подключаться ваши функции.

### Шаг 2 Предоставление разрешений для Workflows

Для выполнения действий от вашего имени Workflows требуются определённые разрешения.
Другие разрешения необходимы для действий, входящих в состав самого Jenkins Connector.

Чтобы настроить разрешения для Workflows:

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения в дополнение к основному разрешению Workflows.

* Разрешения, необходимые для действий рабочего процесса Jenkins:

  + `app-settings:objects:read`

Подробнее об общих пользовательских разрешениях для Workflows см. в разделе [Пользовательские разрешения для рабочих процессов](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Шаг 3 Настройка подключения к Jenkins

Для каждой из ваших сред Jenkins необходимо настроить отдельное подключение.

Чтобы настроить подключение:

1. Откройте ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** и перейдите в **Connections** > **Jenkins**.
2. Выберите **Connection**.
3. Опишите ваше подключение к Jenkins.

   * **Connection name**: Введите понятное имя для вашего подключения.
   * **Jenkins URL**: Укажите URL вашей среды Jenkins.
   * **Username**: Введите ваше имя пользователя Jenkins.
   * **Password**: Введите ваш пароль Jenkins.
4. Нажмите **Create**.
