---
title: Настройка Real User Monitoring с помощью JavaScript API для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum
scraped: 2026-05-12T11:35:07.229095
---

# Настройка Real User Monitoring с помощью JavaScript API для веб-приложений

# Настройка Real User Monitoring с помощью JavaScript API для веб-приложений

* How-to guide
* 16-min read
* Updated on Mar 05, 2026

Dynatrace позволяет расширить стандартную функциональность Real User Monitoring с помощью RUM JavaScript API. Он позволяет создавать пользовательские действия, сообщать об ошибках, включать Session Replay и многое другое.

RUM JavaScript API входит в состав RUM JavaScript, который автоматически инжектируется OneAgent. Если OneAgent не установлен, можно использовать [безагентный мониторинг](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") для вставки RUM JavaScript вручную.

## Возможности

RUM JavaScript API, вызываемый непосредственно из кода приложения, предоставляет множество дополнительных возможностей.

* **Создание пользовательских действий пользователя**
  Если необходимо отслеживать определённую функциональность приложения, которую Dynatrace не фиксирует автоматически, можно определить собственные пользовательские действия.
  Предположим, нужно отслеживать конкретный элемент UI, появляющийся в ответ на щелчок пользователя, но не инициирующий веб-запрос. В таком случае Dynatrace не будет считать этот щелчок пользовательским действием. С помощью RUM JavaScript API можно по-прежнему отслеживать такие взаимодействия.
* **Определение пользовательских имён для действий**
  RUM JavaScript API позволяет [определять собственные имена пользовательских действий](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.") и переопределять поведение именования по умолчанию.
* **Сообщение об ошибках**
  Иногда встречаются ошибки, которые Dynatrace не распознаёт по умолчанию. Функциональность сообщения об ошибках RUM JavaScript API позволяет передавать информацию об ошибках, которые затем отображаются в разделе [**Errors**](/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.") страницы обзора приложения.
* **Добавление и расширение мониторинга сторонних ресурсов**
  При активном модуле тайминга ресурсов фиксируются все ресурсы из таймингов ресурсов. Изображения и JavaScript-файлы фиксируются сторонним модулем. RUM JavaScript API позволяет фиксировать дополнительные ресурсы.
* **Добавление тегов пользователей**
  С помощью [тегов пользователей](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") можно [отслеживать поведение отдельных пользователей](/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") в среде приложений на протяжении сессий, устройств и браузеров.
* **Сообщение о свойствах**
  RUM JavaScript API позволяет передавать свойства сессий и пользовательских действий. Обратите внимание, что предварительно необходимо [определить свойства сессий и пользовательских действий в настройках RUM-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). В противном случае Dynatrace будет отклонять передаваемые свойства.
* **Включение или отключение Session Replay**
  С помощью RUM JavaScript API можно включать или отключать функцию [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.").

## Документация

Документация RUM JavaScript API содержит информацию обо всех вариантах настройки RUM и полезные примеры кода. Можно воспользоваться онлайн-руководством или скачать ZIP-архив из своей среды для просмотра руководства в офлайн-режиме.

Онлайн-руководство по RUM JavaScript API

Офлайн-руководство по RUM JavaScript API

Для доступа к онлайн-руководству перейдите по ссылке [Документация JavaScript API](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html).

Чтобы скачать руководство по RUM JavaScript API из своей среды:

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Advanced setup**.
2. В разделе **JavaScript tag API** выберите **Download documentation and samples**.

## Различие между RUM JavaScript API

Обратите внимание, что Dynatrace предоставляет два API, связанных с Real User Monitoring.

* RUM JavaScript API, описанный в данном разделе, предназначен для расширения стандартных функций Real User Monitoring для приложения.
* [RUM JavaScript REST API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.") часто используется для получения последней версии RUM JavaScript для [безагентного RUM](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."). Полученный RUM JavaScript тег или код необходимо вручную вставить в каждую HTML-страницу приложения. С помощью этого API также можно получить список всех вручную вставленных приложений в среде и проверить последнюю версию RUM JavaScript.

## Связанные темы

* [Документация RUM JavaScript API](https://docs.dynatrace.com/javascriptapi/doc/interfaces/dtrum_types.DtrumApi.html)