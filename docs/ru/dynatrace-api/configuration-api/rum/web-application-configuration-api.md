---
title: Web application configuration API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-03-06T21:35:47.089943
---

# API конфигурации веб-приложений


**API конфигурации веб-приложений** позволяет управлять конфигурацией [веб-приложений](../../../discover-dynatrace/get-started/glossary.md#app "Get acquainted with Dynatrace terminology.").

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [API для мобильных и пользовательских приложений](mobile-custom-app-configuration.md "Learn what the Dynatrace mobile and custom app config API offers.").

[### Список всех приложений

Получить обзор всех веб-приложений.](web-application-configuration-api/web-application/get-all.md "List all web applications via the Dynatrace API.")[### Просмотр веб-приложения

Получить параметры веб-приложения по его идентификатору.](web-application-configuration-api/web-application/get-web-application.md "View parameters of a web application via the Dynatrace API.")

[### Создание веб-приложения

Создать новое веб-приложение с точными требуемыми параметрами.](web-application-configuration-api/web-application/post-web-application.md "Create a web application via the Dynatrace API.")[### Редактирование веб-приложения

Обновить существующее веб-приложение или создать новое приложение с указанным идентификатором.](web-application-configuration-api/web-application/put-web-application.md "Update a web application via the Dynatrace API.")[### Удаление веб-приложения

Удалить ненужное веб-приложение.](web-application-configuration-api/web-application/del-web-application.md "Delete a web application via the Dynatrace API.")

Приложение по умолчанию предварительно настроено в вашей среде Dynatrace. По умолчанию весь трафик направляется в это приложение. После настройки собственных [приложений](../../../discover-dynatrace/get-started/glossary.md#app "Get acquainted with Dynatrace terminology.") весь трафик, не соответствующий ни одному из ваших приложений, направляется в приложение по умолчанию.

[### Просмотр конфигурации

Получить параметры веб-приложения по умолчанию.](web-application-configuration-api/default-application/get-configuration.md "View configuration of the default web application via the Dynatrace API.")[### Обновление конфигурации

Обновить параметры веб-приложения по умолчанию.](web-application-configuration-api/default-application/put-configuration.md "Update configuration of the default web application via the Dynatrace API.")

### Проверка конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Всех приложений](web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps.md "View data privacy configuration of all applications via the Dynatrace API.")
* [Конкретного приложения](web-application-configuration-api/data-privacy/get-data-privacy-web-app.md "View data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](web-application-configuration-api/data-privacy/get-data-privacy-default-app.md "View data privacy configuration of the default application via the Dynatrace API.")

### Обновление конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Конкретного приложения](web-application-configuration-api/data-privacy/put-data-privacy-web-app.md "Edit data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](web-application-configuration-api/data-privacy/put-data-privacy-default-app.md "Edit data privacy configuration of the default application via the Dynatrace API.")

[### Просмотр ключевых пользовательских действий

Получить список ключевых пользовательских действий в приложении.](web-application-configuration-api/key-user-actions/get-configuration.md "View key user actions of a web application via the Dynatrace API.")[### Редактирование списка ключевых пользовательских действий

Отметить пользовательское действие как ключевое в приложении.](web-application-configuration-api/key-user-actions/post-configuration.md "Add a key user action to a web application via the Dynatrace API.")[### Удаление ключевого пользовательского действия

Удалить пользовательское действие из списка ключевых действий в приложении.](web-application-configuration-api/key-user-actions/del-configuration.md "Remove a key user action from a web application via the Dynatrace API.")

[### Просмотр правил ошибок

Получить обзор конфигурации правил ошибок.](web-application-configuration-api/error-rules/get-configuration.md "Read error rules of an application via the Dynatrace API.")[### Обновление правил ошибок

Обновить конфигурацию правил ошибок.](web-application-configuration-api/error-rules/put-configuration.md "Update error rules of an application via the Dynatrace API.")
