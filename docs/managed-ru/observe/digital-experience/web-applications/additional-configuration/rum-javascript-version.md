---
title: Управление версией RUM JavaScript
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version
scraped: 2026-05-12T11:34:18.207825
---

# Управление версией RUM JavaScript

# Управление версией RUM JavaScript

* How-to guide
* Published Jul 01, 2025

Можно управлять тем, какая версия RUM JavaScript используется для каждого веб-приложения. Доступные варианты включают как минимум версии **Latest stable** и **Previous stable**. В зависимости от того, когда была создана среда, могут также предоставляться дополнительные версии для Internet Explorer; подробнее см. в разделе [RUM JavaScript для Internet Explorer](#rum-javascript-for-ie). Кроме того, можно настроить [пользовательскую версию](#custom-version) для среды, которая будет добавлена в список доступных для выбора версий.

## Настройка версии RUM JavaScript для приложения

Чтобы выбрать версию RUM JavaScript:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **RUM JavaScript updates**.
5. Выберите нужную версию RUM JavaScript из раскрывающегося списка.
6. Выберите **Save changes**.

## Настройка пользовательской версии для среды

Чтобы настроить пользовательскую версию для среды:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Custom RUM JavaScript version**.
2. Выберите нужную версию из раскрывающегося списка.
3. Выберите **Save changes**.

После настройки версии RUM JavaScript согласно разделу [Настройка версии RUM JavaScript для приложения](#configure-js-version) в раскрывающемся списке появится вариант пользовательской версии.

## RUM JavaScript для Internet Explorer

* Поддержка Internet Explorer 7–10 прекращена начиная с версии RUM JavaScript 1.265.
* Поддержка Internet Explorer 11 прекращена начиная с версии RUM JavaScript 1.293.

В результате, начиная с этих версий, RUM JavaScript не может инициализироваться в данных браузерах и, следовательно, не может отправлять данные RUM в Dynatrace. В консоли браузера будет отображаться сообщение о том, что RUM JavaScript отключён или браузер не может разобрать RUM JavaScript.

В зависимости от того, когда была создана среда, могут быть доступны конкретные версии RUM JavaScript, обеспечивающие совместимость с Internet Explorer 7–10 и Internet Explorer 11 соответственно.

Версия RUM JavaScript 1.263 является последней, совместимой с Internet Explorer 7–10, а версия 1.291 — последней, совместимой с Internet Explorer 11. Эти версии предоставляются в текущем состоянии и больше не обновляются.

### Internet Explorer 7–10

* **Среды, созданные в Dynatrace версии 1.266+**: использование версии RUM JavaScript, совместимой с Internet Explorer 7–10, недоступно.
* **Среды, созданные до Dynatrace версии 1.266**: можно выбрать версию RUM JavaScript, совместимую с Internet Explorer 7–10. Для этого на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version) выберите вариант **Latest IE7-10 supported**.

### Internet Explorer 11

* **Среды, созданные в Dynatrace версии 1.294+**: использование версии RUM JavaScript, совместимой с Internet Explorer 11, недоступно.
* **Среды, созданные до Dynatrace версии 1.294**: можно выбрать версию RUM JavaScript, совместимую с Internet Explorer 11. Для этого на шаге 5 инструкции в разделе [Настройка версии RUM JavaScript для приложения](#configure-js-version) выберите вариант **Latest IE11 supported**.

### Internet Explorer 11 с режимом совместимости

Если приложение может просматриваться через Internet Explorer 11 с включённым режимом совместимости, используйте версию **Latest IE7-10 supported**, а не **Latest IE11 supported**. При выборе версии **Latest IE11 supported** RUM JavaScript не инициализируется, и в консоли браузера отобразится следующее сообщение:

```
Unsupported Internet Explorer version detected. Only version 11 (without Compatibility View) is supported!
```