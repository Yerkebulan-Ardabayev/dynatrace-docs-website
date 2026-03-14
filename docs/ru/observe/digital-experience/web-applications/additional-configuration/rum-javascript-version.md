---
title: Управление версией RUM JavaScript
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version
scraped: 2026-03-03T21:29:57.852417
---

# Управление версией RUM JavaScript

# Управление версией RUM JavaScript

* Практическое руководство
* Опубликовано 01 июля 2025 г.

Вы можете управлять тем, какая версия RUM JavaScript используется для каждого из ваших веб-приложений. Доступные варианты включают как минимум версии **Latest stable** и **Previous stable**. В зависимости от того, когда было создано ваше окружение, могут также предоставляться дополнительные версии для Internet Explorer; подробнее см. в разделе [RUM JavaScript для Internet Explorer](#rum-javascript-for-ie). Вы также можете настроить [пользовательскую версию](#custom-version) для вашего окружения, которая будет добавлена в список доступных версий.

## Настройка версии RUM JavaScript для приложения

Чтобы выбрать версию RUM JavaScript:

1. Перейдите в раздел **Web**.
2. Выберите приложение, которое вы хотите настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **RUM JavaScript updates**.
5. Выберите необходимую версию RUM JavaScript из раскрывающегося списка.
6. Нажмите **Save changes**.

## Настройка пользовательской версии для вашего окружения

Чтобы настроить пользовательскую версию для вашего окружения:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Custom RUM JavaScript version**.
2. Выберите необходимую версию из раскрывающегося списка.
3. Нажмите **Save changes**.

После настройки версии RUM JavaScript, как описано в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version), в раскрывающемся списке появится вариант пользовательской версии.

## RUM JavaScript для Internet Explorer

* Поддержка Internet Explorer 7–10 прекращена начиная с версии RUM JavaScript 1.265.
* Поддержка Internet Explorer 11 прекращена начиная с версии RUM JavaScript 1.293.

В результате, начиная с этих версий, RUM JavaScript не может инициализироваться в данных браузерах и, следовательно, не может отправлять данные RUM в Dynatrace. В консоли браузера будет отображаться сообщение о том, что RUM JavaScript отключён или что браузер не может выполнить синтаксический анализ RUM JavaScript.

В зависимости от того, когда было создано ваше окружение, доступны определённые версии RUM JavaScript, обеспечивающие совместимость с Internet Explorer 7–10 и Internet Explorer 11 соответственно.

Версия RUM JavaScript 1.263 является последней версией, совместимой с Internet Explorer 7–10, а версия RUM JavaScript 1.291 является последней версией, совместимой с Internet Explorer 11. Эти версии предоставляются «как есть» и больше не будут получать обновлений.

### Internet Explorer 7–10

* **Окружения, созданные в Dynatrace версии 1.266 и выше**: использование версии RUM JavaScript, совместимой с Internet Explorer 7–10, недоступно.
* **Окружения, созданные до Dynatrace версии 1.266**: вы можете выбрать версию RUM JavaScript, совместимую с Internet Explorer 7–10. Выберите вариант **Latest IE7-10 supported** на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version).

### Internet Explorer 11

* **Окружения, созданные в Dynatrace версии 1.294 и выше**: использование версии RUM JavaScript, совместимой с Internet Explorer 11, недоступно.
* **Окружения, созданные до Dynatrace версии 1.294**: вы можете выбрать версию RUM JavaScript, совместимую с Internet Explorer 11. Выберите вариант **Latest IE11 supported** на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version).

### Internet Explorer 11 в режиме совместимости (Compatibility View)

Если ваше приложение может просматриваться в Internet Explorer 11 с включённым режимом совместимости, используйте версию **Latest IE7-10 supported**, а не **Latest IE11 supported**. Если выбрать версию **Latest IE11 supported**, RUM JavaScript не инициализируется, и в консоли браузера отобразится следующее сообщение:

```
Unsupported Internet Explorer version detected. Only version 11 (without Compatibility View) is supported!
```
