---
title: Управление версией RUM JavaScript в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-javascript-version
---

# Управление версией RUM JavaScript в RUM Classic

# Управление версией RUM JavaScript в RUM Classic

* Практическое руководство
* Опубликовано 01 июля 2025

Можно управлять тем, какая версия RUM JavaScript используется для каждого веб-приложения. Доступные варианты включают как минимум версии **Latest stable** и **Previous stable**. В зависимости от того, когда было создано окружение, могут также предоставляться дополнительные версии для Internet Explorer, подробнее см. [RUM JavaScript для Internet Explorer](#rum-javascript-for-ie). Также можно настроить [пользовательскую версию](#custom-version) для окружения, которая будет добавлена в список доступных для выбора версий.

## Настройка версии RUM JavaScript для приложения

Чтобы выбрать версию RUM JavaScript

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **RUM JavaScript updates**.
5. Выбрать нужную версию RUM JavaScript из выпадающего списка.
6. Выбрать **Save changes**.

## Настройка пользовательской версии для окружения

Чтобы настроить пользовательскую версию для окружения

1. Перейти в **Settings** > **Web and mobile monitoring** > **Custom RUM JavaScript version**.
2. Выбрать нужную версию из выпадающего списка.
3. Выбрать **Save changes**.

После настройки версии RUM JavaScript, как описано в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version), в выпадающем списке появится вариант с пользовательской версией.

## RUM JavaScript для Internet Explorer

* Поддержка Internet Explorer 7–10 прекращена начиная с версии RUM JavaScript 1.265.
* Поддержка Internet Explorer 11 прекращена начиная с версии RUM JavaScript 1.293.

В результате, начиная с этих версий, RUM JavaScript не может инициализироваться в этих браузерах и, соответственно, не может отправлять данные RUM в Dynatrace. В консоли браузера будет отображаться сообщение о том, что RUM JavaScript отключён, либо о том, что браузер не может разобрать RUM JavaScript.

В зависимости от того, когда было создано окружение, доступны определённые версии RUM JavaScript, обеспечивающие совместимость с Internet Explorer 7–10 и Internet Explorer 11 соответственно.

Версия RUM JavaScript 1.263, это последняя версия, совместимая с Internet Explorer 7–10, а версия RUM JavaScript 1.291, это последняя версия, совместимая с Internet Explorer 11. Эти версии предоставляются как есть и больше не будут получать обновлений.

### Internet Explorer 7–10

* **Environment, созданные в Dynatrace версии 1.266+**: нельзя использовать версию RUM JavaScript, совместимую с Internet Explorer 7–10.
* **Environment, созданные до Dynatrace версии 1.266**: можно выбрать версию RUM JavaScript, совместимую с Internet Explorer 7–10. Выбрать опцию **Latest IE7-10 supported** на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version).

### Internet Explorer 11

* **Environment, созданные в Dynatrace версии 1.294+**: нельзя использовать версию RUM JavaScript, совместимую с Internet Explorer 11.
* **Environment, созданные до Dynatrace версии 1.294**: можно выбрать версию RUM JavaScript, совместимую с Internet Explorer 11. Выбрать опцию **Latest IE11 supported** на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version).

### Internet Explorer 11 с режимом совместимости

Если приложение может просматриваться через Internet Explorer 11 с включённым режимом совместимости (Compatibility View), нужно использовать версию **Latest IE7-10 supported**, а не версию **Latest IE11 supported**. Если выбрать версию **Latest IE11 supported**, RUM JavaScript не инициализируется, и в консоли браузера отобразится следующее сообщение:

```
Unsupported Internet Explorer version detected. Only version 11 (without Compatibility View) is supported!
```