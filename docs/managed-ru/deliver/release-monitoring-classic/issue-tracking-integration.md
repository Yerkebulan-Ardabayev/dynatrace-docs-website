---
title: Issue-tracking integration
source: https://docs.dynatrace.com/managed/deliver/release-monitoring-classic/issue-tracking-integration
---

# Issue-tracking integration

# Issue-tracking integration

* Практическое руководство
* Чтение за 2 минуты
* Опубликовано 14 сентября 2020

Чтобы получать статистику по issue релизов для отслеживаемых сущностей и настраивать динамические запросы, можно интегрировать систему отслеживания issue с Dynatrace.

## Поддерживаемые интеграции

В настоящее время Dynatrace поддерживает интеграцию с

* Jira on-premises
* Jira cloud
* GitHub
* GitLab
* ServiceNow

## Интеграция системы отслеживания issue

Чтобы интегрировать систему отслеживания issue

1. Перейти в **Settings Classic** > **Cloud Automation** > **Issue-tracking for releases**.
2. Выбрать **Add issue-tracking query**.
3. Ввести необходимую информацию (**Issue label**, [**Issue query**](#query), **Issue type**, **Issue-tracking system**, **Target URL**[1](#fn-1-1-def), [**Username**, а также **Password** или **Token**](#credentials)).
4. Если есть ошибки конфигурации, внизу страницы отобразится сообщение об ошибке (`Please resolve errors before saving...`). Нужно выбрать **Show errors**, чтобы увидеть ошибки конфигурации (выделены красным).
5. Опционально можно выбрать **Check configuration**, чтобы проверить соединение между Dynatrace и системой отслеживания issue.
6. Выбрать **Save changes**, чтобы сохранить конфигурацию.

1

Для GitLab, чтобы задать запросы для нескольких проектов, можно ввести конечную точку `/groups` API.

Пример конфигурации

![Add tracker](https://dt-cdn.net/images/2021-04-26-08-06-21-1478-2c90218945.png)

Add tracker

### Issue query

В поле **Issue query** можно указывать запросы с плейсхолдерами, которые разрешаются во время выполнения (для динамической фильтрации).  
Примеры:

* **Jira on-premises/Jira cloud:** `issueType = Bug and component in ({PRODUCT}) and affectedVersion in ({VERSION})`
* **GitHub:** `is:issue is:open label:{PRODUCT} label:{VERSION}`
* **GitLab:** `search={PRODUCT} {VERSION}&state=opened&scope=issues`

#### Исключение

Для **ServiceNow** плейсхолдеры не поддерживаются. Инциденты можно запрашивать по значениям атрибутов инцидента в формате `<col_name><operator><value>`.  
Пример: `correlation_displayLIKEDYNATRACE^active=true`. В этом случае фильтрация применится к записям, которые содержат `DYNATRACE` в столбце `correlation_display` и которые сейчас активны.  
По остальным операторам нужно обратиться к [документации ServiceNow API﻿](https://dt-url.net/0w03qc9).

Поддерживается любой запрос, который можно записать в виде параметра запроса `sysparm_query`.

### Учётные данные

Поля **Username**, **Password** и **Token** заполняются следующим образом:

* Для **GitHub** нужно ввести имя пользователя и OAuthToken
* Для **GitLab** нужно ввести токен API с правами на чтение
* Для **Jira on-premises** нужно ввести имя пользователя и пароль
* Для **Jira cloud** нужно ввести имя пользователя и OAuthToken
* Для **ServiceNow** нужно ввести имя пользователя и пароль

После добавления системы отслеживания issue в Dynatrace статистику по issue, связанным с отслеживаемыми сущностями, можно увидеть в разделе **Release inventory** на странице **Releases**. Например, если в release inventory есть записи для приложения **Cassandra** с версией `3.11`, интеграция с системой отслеживания issue предоставит количество багов для Cassandra версии 3.11.

Пример интеграции с системой отслеживания issue

![Example integration](https://dt-cdn.net/images/2021-04-26-08-20-46-1549-374692d0dd.png)

Example integration

## Ограничения

Можно создать максимум 20 конфигураций отслеживания issue.

## Устранение неполадок

Ниже приведено решение проблемы, с которой сталкивались некоторые пользователи: [Automated release monitoring issue-tracking integration: no query results matching the filter﻿](https://dt-url.net/5o038bi).