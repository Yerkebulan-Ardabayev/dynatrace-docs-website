---
title: Настройка Real User Monitoring Classic с помощью JavaScript API для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum
---

# Настройка Real User Monitoring Classic с помощью JavaScript API для веб-приложений

# Настройка Real User Monitoring Classic с помощью JavaScript API для веб-приложений

* Практическое руководство
* 16 минут на чтение
* Обновлено 05 марта 2026 г.

Dynatrace позволяет расширить стандартный функционал Real User Monitoring с помощью RUM JavaScript API. С его помощью можно создавать пользовательские действия, сообщать об ошибках, включать Session Replay и многое другое.

RUM JavaScript API включён в состав RUM JavaScript, который автоматически внедряется OneAgent. Если OneAgent не установлен, можно использовать [агентless-мониторинг](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), чтобы вставить RUM JavaScript вручную.

## Возможности

RUM JavaScript API, который вызывается непосредственно из кода приложения, предоставляет множество дополнительных возможностей.

* **Создание пользовательских действий**  
  Если нужно отслеживать определённую функциональность приложения, которую Dynatrace не захватывает автоматически, можно определить собственные пользовательские действия.  
  Допустим, требуется отслеживать конкретный элемент интерфейса, который появляется в ответ на клик пользователя, но не вызывает веб-запрос. В этом случае Dynatrace не посчитает этот клик пользовательским действием. С помощью RUM JavaScript API такие пользовательские взаимодействия всё равно можно отслеживать.
* **Определение пользовательских имён для действий пользователя**  
  RUM JavaScript API можно использовать, чтобы [задать собственные имена пользовательских действий](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.") и переопределить стандартное поведение именования.
* **Сообщение об ошибках**  
  Иногда встречаются ошибки, которые Dynatrace по умолчанию распознать не может. С помощью функции сообщения об ошибках RUM JavaScript API можно сообщать об ошибках, которые затем отображаются в [разделе **Errors**](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/performance-analysis#top-errors "Understand the available types of performance analysis that are provided by Dynatrace.") страницы обзора приложения.
* **Добавление и расширение мониторинга сторонних ресурсов**  
  Когда активен модуль resource timing, захватываются все ресурсы из resource timings. Изображения и файлы JavaScript захватываются с помощью модуля сторонних ресурсов. RUM JavaScript API можно использовать для захвата дополнительных ресурсов.
* **Добавление пользовательских тегов**  
  С помощью [пользовательских тегов](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") можно [отслеживать поведение конкретных пользователей](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") во всей среде приложения, а также между сессиями, устройствами и браузерами.
* **Отправка свойств**  
  RUM JavaScript API можно использовать для отправки свойств сессии и пользовательских действий. Обратите внимание, что сначала нужно [определить свойства сессии и пользовательских действий в настройках RUM-приложения](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). В противном случае Dynatrace отклонит отправленные свойства.
* **Включение или отключение Session Replay**  
  С помощью RUM JavaScript API можно включить или отключить функцию [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.").

## Документация

Документация RUM JavaScript API содержит информацию обо всех возможностях настройки RUM, а также полезные примеры кода. Документацию по JavaScript API можно посмотреть онлайн либо скачать ZIP-архив из своей среды для просмотра руководства офлайн.

Онлайн-руководство по RUM JavaScript API

Офлайн-руководство по RUM JavaScript API

Чтобы получить доступ к онлайн-руководству, перейдите в [документацию по JavaScript API﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html).

Чтобы скачать руководство по RUM JavaScript API из своей среды

1. В Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Advanced setup**.
2. В разделе **JavaScript tag API** выберите **Download documentation and samples**.

## Разница между RUM JavaScript API

Обратите внимание, что Dynatrace предоставляет два API, связанных с Dynatrace Real User Monitoring Classic.

* RUM JavaScript API, который описан в этой теме, предназначен для расширения стандартных возможностей Real User Monitoring для приложения.
* [RUM JavaScript REST API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.") часто используется, чтобы получить самую свежую версию RUM JavaScript для [агентless RUM](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."). После этого нужно вручную вставить тег или код RUM JavaScript на каждую HTML-страницу приложения. С помощью этого API также можно получить список всех приложений с ручной вставкой в своей среде и проверить самую актуальную версию RUM JavaScript.

## Похожие темы

* [Документация по RUM JavaScript API﻿](https://docs.dynatrace.com/javascriptapi/doc/interfaces/dtrum_types.DtrumApi.html)