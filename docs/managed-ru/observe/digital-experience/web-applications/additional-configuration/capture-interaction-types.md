---
title: Захват дополнительных типов взаимодействий для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types
scraped: 2026-05-12T11:34:20.738803
---

# Захват дополнительных типов взаимодействий для веб-приложений

# Захват дополнительных типов взаимодействий для веб-приложений

* How-to guide
* 2-min read
* Updated on Mar 20, 2023

Для [XHR-действий](/managed/observe/digital-experience/rum-concepts/user-actions#xhr-action "Learn what user actions are and how they help you understand what users do with your application.") Real User Monitoring обнаруживает следующие типы взаимодействий:

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

Чтобы выбрать типы взаимодействий, которые Dynatrace должен захватывать автоматически:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Advanced setup**.
5. Прокрутите страницу вниз до раздела **Wrappers for addEventListener and attachEvent** и с помощью переключателей включите или отключите захват нужных типов взаимодействий. Некоторые параметры доступны как для **Global event capture**, так и для режимов `addEventListener`/`attachEvent`.

   Различие между параметрами Global event capture и addEventListener / attachEvent

   Параметр **Global event capture** регистрирует единственный обработчик на объекте документа страницы для захвата срабатывающих событий.

   Модуль `addEventListener`/`attachEvent` обходит узлы DOM и регистрирует обработчики непосредственно на конкретных элементах. Вместо регистрации единственного глобального обработчика на объекте документа (как при использовании параметра **Global event capture**), этот модуль добавляет обработчики ко всем кнопкам, полям ввода и другим элементам UI. Это увеличивает накладные расходы, поскольку необходимо сканировать все узлы DOM.

   Модуль `addEventListener`/`attachEvent` может потребоваться в следующих случаях:

   * Когда ваша конфигурация останавливает распространение событий.
   * Когда используемый JavaScript-фреймворк препятствует добавлению обработчика на сам элемент документа.
   * При наличии особой конфигурации безопасности.

   ![Wrappers for addEventListener and attachEvent](https://dt-cdn.net/images/global-event-capture-1031-01ba0aaab3.png)

   Wrappers for addEventListener and attachEvent

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")