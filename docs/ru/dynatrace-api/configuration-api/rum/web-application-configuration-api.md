---
title: Конфигурация веб-приложения API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-02-21T21:19:53.273636
---

# Конфигурация веб-приложения API

# Конфигурация веб-приложения API

* Справка
* Опубликовано 24 января 2019 г.

**Конфигурация веб-приложения** API позволяет управлять конфигурацией [веб-приложений](/docs/discover-dynatrace/get-started/glossary#app "Ознакомьтесь с терминологией Dynatrace.").

Эта API поддерживает только веб-приложения. Для мобильных и пользовательских приложений см. [Конфигурация мобильных и пользовательских приложений API](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Узнайте, что предлагает конфигурация мобильных и пользовательских приложений Dynatrace API.").

[### Список всех

Получите обзор всех веб-приложений.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-all "Список всех веб-приложений через Dynatrace API."[### Просмотр веб-приложения

Получите параметры веб-приложения по его ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application "Просмотр параметров веб-приложения через Dynatrace API.")

[### Создание веб-приложения

Создайте новое веб-приложение с необходимыми параметрами.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Создание веб-приложения через Dynatrace API."[### Редактирование веб-приложения

Обновите существующее веб-приложение или создайте новое приложение с указанным ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application "Обновление веб-приложения через Dynatrace API."[### Удаление веб-приложения

Удалите веб-приложение, которое больше не нужно.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application "Удаление веб-приложения через Dynatrace API.")

По умолчанию приложение предварительно настроено в вашей среде Dynatrace. По умолчанию все трафик направляется в это приложение. После настройки своих собственных [приложений](/docs/discover-dynatrace/get-started/glossary#app "Ознакомьтесь с терминологией Dynatrace."), весь трафик, который не соответствует ни одному из ваших приложений, направляется в приложение по умолчанию.

[### Просмотр конфигурации

Получите параметры веб-приложения по умолчанию.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration "Просмотр конфигурации веб-приложения по умолчанию через Dynatrace API."[### Обновление конфигурации

Обновите параметры веб-приложения по умолчанию.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration "Обновление конфигурации веб-приложения по умолчанию через Dynatrace API.")

### Проверка конфиденциальности данных

Просмотрите параметры конфиденциальности данных для

* [Все приложения](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps "Просмотр конфигурации конфиденциальности данных всех приложений через Dynatrace API.")
* [Конкретное приложение](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-web-app "Просмотр конфигурации конфиденциальности данных приложения через Dynatrace API.")
* [Приложение по умолчанию](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app "Просмотр конфигурации конфиденциальности данных приложения по умолчанию через Dynatrace API.")

### Обновление конфиденциальности данных

Просмотрите параметры конфиденциальности данных для

* [Конкретное приложение](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app "Редактирование конфигурации конфиденциальности данных приложения через Dynatrace API.")
* [Приложение по умолчанию](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app "Редактирование конфигурации конфиденциальности данных приложения по умолчанию через Dynatrace API.")

[### Просмотр ключевых действий пользователя

Получите список ключевых действий пользователя в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration "Просмотр ключевых действий пользователя веб-приложения через Dynatrace API."[### Редактирование списка ключевых действий пользователя

Отметьте действие пользователя как ключевое действие в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/post-configuration "Добавление ключевого действия пользователя в веб-приложение через Dynatrace API."[### Удаление ключевого действия пользователя

Удалите действие пользователя из списка ключевых действий в приложении.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration "Удаление ключевого действия пользователя из веб-приложения через Dynatrace API.")

[### Просмотр правил ошибок

Получите обзор конфигурации правил ошибок.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration "Просмотр правил ошибок приложения через Dynatrace API."[### Обновление правил ошибок

Обновите конфигурацию правил ошибок.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration "Обновление правил ошибок приложения через Dynatrace API.")