---
title: Управление версией RUM JavaScript в новом опыте RUM
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/rum-javascript-version
scraped: 2026-03-06T21:35:12.098693
---

# Управление версией RUM JavaScript в новом RUM Experience


* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

Вы можете управлять тем, какая версия RUM JavaScript используется для каждого веб-фронтенда. Доступные варианты включают версии **Latest stable** и **Previous stable**. Также можно настроить [пользовательскую версию](#custom-version) для вашей среды, которая будет добавлена в список доступных для выбора версий.

В зависимости от даты создания вашей среды могут также предоставляться дополнительные версии **Latest IE7-10 supported** и **Latest IE11 supported**. Однако эти версии несовместимы с новым RUM Experience и не могут быть выбраны, когда он включён.

## Настройка версии RUM JavaScript для фронтенда

Чтобы выбрать версию RUM JavaScript

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web**, чтобы просмотреть все веб-фронтенды.
3. Выберите фронтенд, который хотите настроить.
4. На вкладке **Settings** выберите ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Перейдите в **General** > **RUM JavaScript Updates**.
6. Выберите нужную версию RUM JavaScript из выпадающего списка.
7. Нажмите **Save changes**.

## Настройка пользовательской версии для вашей среды

Чтобы настроить пользовательскую версию для вашей среды

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **Versions and updates** > **Custom RUM JavaScript version**.
2. Выберите нужную версию из выпадающего списка.
3. Нажмите **Save changes**.

После настройки версии RUM JavaScript, как описано в разделе [Настройка версии RUM JavaScript для фронтенда](#configure-js-version), в выпадающем списке появится вариант пользовательской версии.
