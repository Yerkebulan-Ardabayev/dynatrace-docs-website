---
title: OneAgent SDK для Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk
---

# OneAgent SDK для Android в RUM Classic

# OneAgent SDK для Android в RUM Classic

* Обзор
* Чтение: 1 мин
* Обновлено 05 марта 2026 г.

OneAgent SDK для Android можно использовать для отправки дополнительных сведений о мобильных пользовательских сессиях приложения. OneAgent SDK для Android позволяет создавать пользовательские действия, измерять веб-запросы, отправлять ошибки и помечать конкретных пользователей. В этом разделе описано, как включить эти возможности.

OneAgent SDK автоматически добавляется плагином [Dynatrace Android Gradle﻿](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как плагин Dynatrace Android Gradle может автоматически инструментировать проект вашего Android-приложения."). Также можно добавить OneAgent SDK, если нужно использовать [автономную ручную инструментацию](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android для ручной инструментации проекта вашего Android-приложения.") проекта вашего Android-приложения.

Вся техническая информация доступна в разделе [JavaDoc для OneAgent SDK для Android﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/).

Через пару месяцев мы прекратим устанавливать cookie для доменов схемы file для гибридных приложений. Подробности и необходимые действия см. в разделе [Отключение cookie для доменов file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#file-domain-cookies "Узнайте, как обогатить мониторинг пользовательского опыта в Android с помощью OneAgent SDK.").