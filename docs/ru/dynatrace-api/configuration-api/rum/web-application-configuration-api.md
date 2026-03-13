---
title: Web application configuration API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-03-06T21:35:47.089943
---

# API конфигурации веб-приложений

# API конфигурации веб-приложений

* Справочник
* Опубликовано 24 января 2019 г.

**API конфигурации веб-приложений** позволяет управлять конфигурацией [веб-приложений](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.").

Этот API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [API для мобильных и пользовательских приложений](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

[### Список всех приложений

Получить обзор всех веб-приложений.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-all "List all web applications via the Dynatrace API.")[### Просмотр веб-приложения

Получить параметры веб-приложения по его идентификатору.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application "View parameters of a web application via the Dynatrace API.")

[### Создание веб-приложения

Создать новое веб-приложение с точными требуемыми параметрами.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.")[### Редактирование веб-приложения

Обновить существующее веб-приложение или создать новое приложение с указанным идентификатором.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application "Update a web application via the Dynatrace API.")[### Удаление веб-приложения

Удалить ненужное веб-приложение.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application "Delete a web application via the Dynatrace API.")

Приложение по умолчанию предварительно настроено в вашей среде Dynatrace. По умолчанию весь трафик направляется в это приложение. После настройки собственных [приложений](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.") весь трафик, не соответствующий ни одному из ваших приложений, направляется в приложение по умолчанию.

[### Просмотр конфигурации

Получить параметры веб-приложения по умолчанию.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration "View configuration of the default web application via the Dynatrace API.")[### Обновление конфигурации

Обновить параметры веб-приложения по умолчанию.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration "Update configuration of the default web application via the Dynatrace API.")

### Проверка конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Всех приложений](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps "View data privacy configuration of all applications via the Dynatrace API.")
* [Конкретного приложения](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-web-app "View data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app "View data privacy configuration of the default application via the Dynatrace API.")

### Обновление конфиденциальности данных

Просмотр параметров конфиденциальности данных для

* [Конкретного приложения](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app "Edit data privacy configuration of an application via the Dynatrace API.")
* [Приложения по умолчанию](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app "Edit data privacy configuration of the default application via the Dynatrace API.")

[### Просмотр ключевых пользовательских действий

Получить список ключевых пользовательских действий в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration "View key user actions of a web application via the Dynatrace API.")[### Редактирование списка ключевых пользовательских действий

Отметить пользовательское действие как ключевое в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/post-configuration "Add a key user action to a web application via the Dynatrace API.")[### Удаление ключевого пользовательского действия

Удалить пользовательское действие из списка ключевых действий в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration "Remove a key user action from a web application via the Dynatrace API.")

[### Просмотр правил ошибок

Получить обзор конфигурации правил ошибок.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration "Read error rules of an application via the Dynatrace API.")[### Обновление правил ошибок

Обновить конфигурацию правил ошибок.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration "Update error rules of an application via the Dynatrace API.")
