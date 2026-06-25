---
title: Инструментирование мобильных приложений с помощью плагина Dynatrace Flutter
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/flutter
scraped: 2026-05-12T11:23:19.793919
---

# Инструментирование мобильных приложений с помощью плагина Dynatrace Flutter

# Инструментирование мобильных приложений с помощью плагина Dynatrace Flutter

* How-to guide
* 1-min read
* Updated on Nov 26, 2024

Плагин Dynatrace Flutter добавляет Dynatrace OneAgent для Android и iOS в Flutter-приложение и предоставляет API для ручного инструментирования при сборе данных Flutter/Dart.

Подробная техническая документация доступна на странице [Dynatrace Flutter Plugin](https://pub.dev/packages/dynatrace_flutter_plugin) на сайте pub.dev.

## Предварительные требования

* Dynatrace версии 1.203+
* Dart версии 2.12+
* Flutter версии 1.12.0+
* Gradle версии 7.0+
* Android версии 5.0+ (уровень API 21+)
* Java 11+
* iOS версии 12+

## Настройка Flutter-приложения для мобильного мониторинга

1. В Dynatrace перейдите в раздел **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница параметров приложения.
4. В параметрах приложения выберите **Instrumentation wizard** > **Flutter**.
5. Выполните шаги, описанные в мастере.

### Демонстрация

Пример инструментирования компактного приложения см. на вкладке **Example** страницы [Dynatrace Flutter plugin](https://pub.dev/packages/dynatrace_flutter_plugin/example).