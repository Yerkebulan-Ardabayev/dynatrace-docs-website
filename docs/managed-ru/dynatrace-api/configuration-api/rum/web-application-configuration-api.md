---
title: Web application configuration API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-05-12T11:04:27.810111
---

# Web application configuration API

# Web application configuration API

* Reference
* Published Jan 24, 2019

API **Web application configuration** позволяет управлять конфигурацией [веб-приложений](/managed/discover-dynatrace/get-started/glossary#app "Познакомьтесь с терминологией Dynatrace.").

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений смотрите [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает Dynatrace mobile и custom app config API.").

[### Список всех

Обзор всех веб-приложений.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-all "List all web applications via the Dynatrace API.")[### Просмотр веб-приложения

Получить параметры веб-приложения по его ID.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application "View parameters of a web application via the Dynatrace API.")

[### Создание веб-приложения

Создать новое веб-приложение с точно нужными параметрами.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.")[### Редактирование веб-приложения

Обновить существующее веб-приложение или создать новое приложение с указанным ID.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application "Update a web application via the Dynatrace API.")[### Удаление веб-приложения

Удалить ненужное веб-приложение.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application "Delete a web application via the Dynatrace API.")

Приложение по умолчанию предварительно настроено в вашем окружении Dynatrace. По умолчанию весь трафик идёт в это приложение. После того как вы настроите свои собственные [приложения](/managed/discover-dynatrace/get-started/glossary#app "Познакомьтесь с терминологией Dynatrace."), весь трафик, который не подходит ни под одно из ваших приложений, идёт в приложение по умолчанию.

[### Просмотр конфигурации

Получить параметры веб-приложения по умолчанию.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration "View configuration of the default web application via the Dynatrace API.")[### Обновление конфигурации

Обновить параметры веб-приложения по умолчанию.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration "Update configuration of the default web application via the Dynatrace API.")

### Проверка конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Всех приложений](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps "View data privacy configuration of all applications via the Dynatrace API.")
* [Определённого приложения](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-web-app "View data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app "View data privacy configuration of the default application via the Dynatrace API.")

### Обновление конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Определённого приложения](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app "Edit data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app "Edit data privacy configuration of the default application via the Dynatrace API.")

[### Просмотр ключевых пользовательских действий

Получить список ключевых пользовательских действий в приложении.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration "View key user actions of a web application via the Dynatrace API.")[### Редактирование списка ключевых пользовательских действий

Отметить пользовательское действие как ключевое в приложении.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/post-configuration "Add a key user action to a web application via the Dynatrace API.")[### Удаление ключевого пользовательского действия

Удалить пользовательское действие из списка ключевых действий в приложении.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration "Remove a key user action from a web application via the Dynatrace API.")

[### Просмотр правил ошибок

Обзор конфигурации правил ошибок.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration "Read error rules of an application via the Dynatrace API.")[### Обновление правил ошибок

Обновить конфигурацию конфигурации.](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration "Update error rules of an application via the Dynatrace API.")