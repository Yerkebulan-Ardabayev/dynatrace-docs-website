---
title: Инструментирование мобильных приложений с помощью плагина Flutter Dynatrace в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/flutter
---

# Инструментирование мобильных приложений с помощью плагина Flutter Dynatrace в RUM Classic

# Инструментирование мобильных приложений с помощью плагина Flutter Dynatrace в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Обновлено 22 июня 2026 г.

Плагин Flutter Dynatrace добавляет Dynatrace OneAgent для Android и iOS в приложение Flutter и предоставляет API для использования ручного инструментирования при сборе данных Flutter/Dart.

Подробную техническую документацию см. на странице [Dynatrace Flutter Plugin﻿](https://pub.dev/packages/dynatrace_flutter_plugin) на сайте pub.dev.

## Предварительные требования

* Dynatrace версии 1.203+
* Dart версии 2.12+
* Flutter версии 1.12.0+
* Gradle версии 8.0+
* Android версии 6.0+ (API 23+)
* Java 17+
* iOS версии 15+

## Настройка мобильного приложения Flutter

1. В Dynatrace перейти в **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести название приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.
4. На странице настроек приложения выбрать **Instrumentation wizard** > **Flutter**.
5. Выполнить шаги, описанные в мастере.

### Демонстрация

Пример инструментирования компактного приложения см. на вкладке **Example** страницы [Dynatrace Flutter plugin﻿](https://pub.dev/packages/dynatrace_flutter_plugin/example).