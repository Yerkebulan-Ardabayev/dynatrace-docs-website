---
title: Захват дополнительных типов взаимодействия для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/capture-interaction-types
---

# Захват дополнительных типов взаимодействия для веб-приложений в RUM Classic

# Захват дополнительных типов взаимодействия для веб-приложений в RUM Classic

* Практическое руководство
* Чтение 2 мин
* Обновлено 20 марта 2023 г.

Для [XHR-действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#xhr-action "Узнайте, что такое пользовательские действия и как они помогают понять, что делают пользователи с приложением.") Real User Monitoring определяет следующие типы взаимодействия:

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

Чтобы выбрать, какие типы взаимодействия Dynatrace должен захватывать автоматически

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Advanced setup**.
5. Прокрутить вниз до раздела **Wrappers for addEventListener and attachEvent** и с помощью переключателей включить или исключить типы взаимодействия из захвата. Некоторые опции доступны как для режима **Global event capture**, так и для режимов `addEventListener`/`attachEvent`.

   Разница между опциями Global event capture и addEventListener / attachEvent

   Опция **Global event capture** регистрирует единственный listener на объекте document страницы для захвата возникающих событий.

   Модуль `addEventListener`/`attachEvent` проходит по узлам DOM и регистрирует listener'ы непосредственно на конкретных элементах. Вместо регистрации единственного глобального listener'а на объекте document (как в случае с опцией **Global event capture**), этот модуль добавляет listener'ы на все кнопки, элементы ввода и другие элементы UI. Это увеличивает накладные расходы, поскольку требуется сканировать все узлы DOM.

   Модуль `addEventListener`/`attachEvent` может понадобиться в следующих случаях:

   * когда настройка приложения останавливает распространение событий;
   * когда фреймворк настройки JavaScript не позволяет добавить listener на сам элемент document;
   * в случае другой уникальной настройки безопасности.

   ![Wrappers for addEventListener and attachEvent](https://dt-cdn.net/images/global-event-capture-1031-01ba0aaab3.png)

   Wrappers for addEventListener and attachEvent

## Похожие темы

* [Пользовательские действия в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что делают пользователи с приложением.")