---
title: Тегирование отдельных пользователей для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis
scraped: 2026-05-12T11:35:02.443187
---

# Тегирование отдельных пользователей для веб-приложений

# Тегирование отдельных пользователей для веб-приложений

* How-to guide
* 5-min read
* Updated on Apr 01, 2026

Одной из ключевых функций Real User Monitoring является возможность уникальной идентификации отдельных пользователей в разных браузерах, устройствах и пользовательских сессиях.

С помощью [тегов пользователей](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") можно анализировать поведение и опыт конкретного пользователя через [анализ пользовательских сессий](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").
По умолчанию Dynatrace присваивает каждому новому пользователю уникальный случайный идентификатор. Однако можно назначать более информативные пользовательские теги, включающие, например, имена пользователей или адреса электронной почты.

Для веб-приложений настройка тегирования пользователей доступна через RUM JavaScript API или на основе метаданных страниц приложения.

## Тегирование пользователей через RUM JavaScript API

Используйте метод [`identifyUser`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#identifyuser) [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") для установки тега пользователя.

## Тегирование пользователей на основе источника страницы

Этот подход к тегированию пользователей основан на захвате доступных данных в источнике страницы приложения: имена пользователей или адреса электронной почты часто включены в текст DOM-элемента или переменную JavaScript. Полный список источников данных страницы см. в разделе [Доступные типы источников](#available-page-data-sources).

Например, демонстрационное приложение **easyTravel** включает имя пользователя в приветственное сообщение в правом верхнем углу главной страницы (см. изображение ниже). С помощью инструментов разработчика, встроенных в большинство браузеров, можно создать уникальный CSS-селектор для этого элемента.

![Usertags 2](https://dt-cdn.net/images/usertags2-1872-eaa3cbf0fe.png)

Usertags 2

### Добавление правила тега пользователя

После того как определено расположение имён пользователей в источнике страницы приложения, можно создать правило тега пользователя.

Чтобы добавить правило тега пользователя:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **User tags**.
5. Выберите **Add user tag rule**.
6. Выберите **Source type** и имя источника для данного правила тега.
   Доступные типы источников

   * **CSS selector**. Используйте, когда идентификатор пользователя виден на странице. Этот механизм захватывает значение `innerText/textContent` первого совпадения (доступно для браузеров, поддерживающих `querySelector`). Чтобы получить значение конкретного атрибута элемента, добавьте символ '@' и имя атрибута, например `#someDomElement@someAttribute`.
   * **JavaScript variable**. Используйте, когда идентификатор пользователя доступен как переменная JavaScript на объекте `window`. Например, если указана переменная JavaScript `userName`, RUM JavaScript получает значение из `window.userName`.
   * **Meta tag**. Используйте, когда идентификатор пользователя присутствует в одном из мета-тегов в источнике страницы. Указывает имя мета-тега, значение атрибута `content` которого Dynatrace будет захватывать.
   * **Cookie value**. Используйте, когда идентификатор пользователя присутствует в одном из существующих cookie.

     Если в качестве источника данных нужно использовать `Cookie value`, убедитесь, что cookie не имеют атрибута `HttpOnly`. В противном случае RUM JavaScript не сможет читать значения cookie, поскольку cookie с атрибутом `HttpOnly` недоступны для JavaScript.
   * **Query string**. Используйте, когда идентификатор пользователя является частью параметра строки запроса, который можно указать здесь.
   * **Server-side request attribute**. Используйте, когда для тегирования каждой пользовательской сессии необходимо использовать серверный [атрибут запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").
     После [определения атрибута запроса](/managed/observe/application-observability/services/request-attributes#define-request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") установите **Server-side request attribute** в качестве **Source type**. Обратите внимание, что атрибут запроса может фиксироваться не для каждого пользовательского действия и сессии, поскольку серверная распределённая трассировка может не быть захвачена из-за [адаптивного управления трафиком](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").
7. Необязательно: включите **Ignore case**, чтобы привести тег пользователя к нижнему регистру.
8. Необязательно: для обеспечения чистого извлечения значения имени пользователя включите **Apply cleanup rule** и введите регулярное выражение.
9. Выберите **Add user tag rule**.

### Проверка конфигурации тега пользователя

Чтобы убедиться в правильности применения конфигурации тега пользователя, сохраните конфигурацию и перезагрузите страницу приложения. Затем проверьте инжектированный JavaScript в обновлённом источнике страницы приложения.

Как показано в примере ниже, свойство с именем `md=` теперь отображается в метаданных страницы.

![Usertags 4](https://dt-cdn.net/images/usertags4-1873-d1f096ef61.png)

Usertags 4

Чтобы найти сессии конкретного пользователя:

1. Перейдите в **Session Segmentation**.
2. Выберите поле фильтра в верхней части страницы и выберите атрибут **User tag**.
3. Выберите тег пользователя из списка и нажмите **Apply**.

На странице **User sessions** теперь отображается список сессий данного пользователя. Можно выбрать конкретную сессию для просмотра подробностей. Или выберите имя пользователя, чтобы перейти на [страницу обзора пользователя](/managed/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

## Ограничения и примечания

* Можно добавить до 20 правил тегов пользователей на приложение.
* Все захваченные значения обрезаются до максимальной длины 100 символов.
* При использовании RUM JavaScript API для идентификации пользователей API может переопределять ранее настроенные правила на основе метаданных. Теги пользователей могут переопределять другие теги на основе метаданных.
* Все настроенные теги пользователей захватываются на каждой странице. RUM JavaScript используется для проверки каждого отслеживаемого пользовательского действия на соответствие каждому созданному правилу тега, поэтому рекомендуется сохранять список правил тегов минимальным для снижения накладных расходов.
* Последнее пользовательское действие в сессии, содержащее тег, используется как тег для всей сессии.
* Настройка конфиденциальности данных [Do Not Track](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") может влиять на тегирование пользователей.

  Если для вашего веб-приложения включён параметр **Comply with "Do Not Track" browser settings** и конкретный пользователь активировал в своём браузере функцию «Do Not Track», информация о теге пользователя не отправляется. Однако если пользователь отключил «Do Not Track» в своём браузере, его тег захватывается.
* Если политика организации запрещает отслеживание отдельных пользователей из соображений конфиденциальности, можно определять теги пользователей, соответствующие названиям команд или отделов. Таким образом, можно отслеживать опыт отдельных пользователей, не раскрывая идентифицирующей информации.