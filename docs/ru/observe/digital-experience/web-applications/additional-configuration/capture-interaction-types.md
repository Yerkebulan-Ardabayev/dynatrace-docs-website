---
title: Capture additional interaction types for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types
scraped: 2026-03-06T21:30:24.896704
---

# Захват дополнительных типов взаимодействий для веб-приложений

# Захват дополнительных типов взаимодействий для веб-приложений

* Classic
* How-to guide
* 2-min read
* Updated on Mar 20, 2023

Для [XHR-действий](../../rum-concepts/user-actions.md#xhr-action "Learn what user actions are and how they help you understand what users do with your application.") Real User Monitoring обнаруживает следующие типы взаимодействий:

* Click
* Double click
* Mouse down
* Mouse up
* Scroll

* Key down
* Key up
* Touch start
* Touch end
* Change

Чтобы выбрать, какие типы взаимодействий Dynatrace должен захватывать автоматически

1. Перейдите в раздел **Web**.
2. Выберите приложение, которое хотите настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**â¦**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Advanced setup**.
5. Прокрутите вниз до раздела **Wrappers for addEventListener and attachEvent** и используйте переключатели, чтобы включить или исключить типы взаимодействий из захвата. Некоторые параметры доступны как для режима **Global event capture**, так и для режимов `addEventListener`/`attachEvent`.

   Разница между параметрами Global event capture и addEventListener / attachEvent

   Параметр **Global event capture** регистрирует единственный слушатель на объекте document страницы для захвата инициированных событий.

   Модуль `addEventListener`/`attachEvent` обходит узлы DOM и регистрирует слушателей непосредственно на конкретных элементах. Вместо регистрации единственного глобального слушателя на объекте document (как в случае с параметром **Global event capture**), этот модуль добавляет слушателей на все кнопки, поля ввода и другие элементы пользовательского интерфейса. Это увеличивает накладные расходы, поскольку все узлы DOM должны быть проверены.

   Использование модуля `addEventListener`/`attachEvent` может потребоваться в следующих случаях:

   * Когда ваша конфигурация останавливает распространение событий
   * Когда фреймворк JavaScript предотвращает добавление слушателя на сам элемент document
   * В случае особой конфигурации безопасности

   ![Wrappers for addEventListener and attachEvent](https://dt-cdn.net/images/global-event-capture-1031-01ba0aaab3.png)

## Связанные темы

* [User actions](../../rum-concepts/user-actions.md "Learn what user actions are and how they help you understand what users do with your application.")
