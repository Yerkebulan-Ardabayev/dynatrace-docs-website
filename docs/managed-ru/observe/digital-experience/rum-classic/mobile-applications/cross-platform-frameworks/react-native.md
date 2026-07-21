---
title: Инструментирование мобильных приложений с плагином Dynatrace React Native в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native
---

# Инструментирование мобильных приложений с плагином Dynatrace React Native в RUM Classic

# Инструментирование мобильных приложений с плагином Dynatrace React Native в RUM Classic

* Практическое руководство
* Чтение 4 мин
* Обновлено 10 июля 2026 г.

Плагин React Native позволяет автоматически инструментировать приложения React Native с помощью Dynatrace OneAgent для Android и iOS. Плагин предоставляет API для добавления ручного инструментирования и совместим с raw, ejected проектами React Native.

Подробную техническую документацию можно найти на странице [плагина Dynatrace React Native﻿](https://www.npmjs.com/package/@dynatrace/react-native-plugin) на сайте npm.

Ниже описаны шаги по настройке плагина Dynatrace React Native для мобильного приложения.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание мобильного приложения в Dynatrace**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#create-app-in-ui "Auto-instrument your React Native applications with OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка плагина React Native**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#set-up-plugin "Auto-instrument your React Native applications with OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Сборка и запуск приложения**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#build-and-run-app "Auto-instrument your React Native applications with OneAgent.")

## Требования

* React 16.8+
* React Native 0.60+
* Android версии 6.0+ (API 23+)
* Gradle версии 8.0+
* Android Gradle plugin версии 8.1.1+
* Java 17
* iOS версии 15+

## Шаг 1 Создание мобильного приложения в Dynatrace

Чтобы создать мобильное приложение в Dynatrace

1. В Dynatrace перейти в **Mobile**.
2. Выбрать **Create mobile app**.
3. Ввести имя приложения и выбрать **Create mobile app**. Откроется страница настроек приложения.

## Шаг 2 Настройка плагина React Native

1. На странице настроек приложения выбрать **Instrumentation wizard** > **React Native**. Мастер инструментирования проведёт через процесс настройки.
2. Установить плагин Dynatrace React Native:

   React Native 0.60.0+

   * Вызвать `npm install @dynatrace/react-native-plugin`.
   * Только для iOS Если используются pods, перейти в директорию `ios` и выполнить `pod install`, чтобы установить новую зависимость Dynatrace в проект Xcode.
3. В мастере инструментирования скачать файл `dynatrace.config.js` и поместить его в корневую директорию проекта рядом с `app.json`. При обновлении с предыдущей версии плагина Dynatrace React Native скопировать старые значения конфигурации из `dynatrace.config` в новый файл `dynatrace.config.js`.
4. Добавить babel-плагин `@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace` и JSX runtime `@dynatrace/react-native-plugin` в файл `babel.config.js`:

   @babel/plugin-transform-react-jsx

   Expo

   ```
   module.exports = {



   presets: [



   ['module:@react-native/babel-preset'], // or 'module:metro-react-native-babel-preset'



   ],



   plugins: [



   '@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace',



   [



   '@babel/plugin-transform-react-jsx',



   {



   runtime: 'automatic',



   importSource: "@dynatrace/react-native-plugin"



   },



   ],



   ],



   };
   ```

   ```
   module.exports = function (api) {



   api.cache(true);



   return {



   presets: [



   ['babel-preset-expo',



   {



   jsxRuntime: 'automatic',



   jsxImportSource: '@dynatrace/react-native-plugin',



   },



   ],



   ],



   plugins: [



   '@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace',



   ],



   };



   };
   ```
5. Включить режим согласия пользователя (user opt-in): приложение должно включать уведомление о конфиденциальности, чтобы пользователи могли настроить свои предпочтения приватности. Можно вставить следующий вызов API для включения мониторинга Dynatrace:

   ```
   import { Dynatrace, DataCollectionLevel, UserPrivacyOptions } from '@dynatrace/react-native-plugin';



   // Privacy settings configured below are only provided



   // to allow a quick start with capturing monitoring data.



   // This has to be requested from the user



   // (for example, in a privacy settings screen) and the user decision



   // has to be applied similar to this example.



   const privacyConfig = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



   Dynatrace.applyUserPrivacyOptions(privacyConfig);
   ```

## Шаг 3 Сборка и запуск приложения

* Выполнить `npx instrumentDynatrace` в корне проекта React Native, чтобы применить конфигурацию, заданную в файле `dynatrace.config.js`. Эта команда настраивает и Android, и iOS проекты.
* Выполнить `react-native run-android` или `react-native run-ios`, чтобы пересобрать и запустить приложение.

  При обновлении до React Native 0.70+ или использовании @react-native-community/cli версии 9.x+ учесть, что автоматический скрипт, запускавшийся перед каждой командой `react-native run-android` или `react-native run-ios`, больше не работает. При изменении конфигурации в файле `dynatrace.config.js` выполнить `npx instrumentDynatrace`, чтобы применить новую конфигурацию.
* При каждом изменении конфигурации в файле `dynatrace.config.js` выполнить следующие команды, а затем пересобрать приложение.

  1. `npx instrumentDynatrace`, чтобы применить новую конфигурацию из `dynatrace.config.js`
  2. `react-native start --reset-cache`, чтобы сбросить кэш. Без сброса кэша возможно смешение старой и новой конфигураций.
* Указать пользовательские пути через [пользовательские аргументы﻿](https://www.npmjs.com/package/@dynatrace/react-native-plugin#customizing-paths-for-configuration).

## Именование пользовательских действий

Подробнее об именовании пользовательских действий в Dynatrace см. [Правила именования пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#user-action-naming-rules "Learn what user actions are and how they help you understand what users do with your application.").

#### React views

* `displayName`: проверяет, задано ли для React views имя для отображения.
* `class name`: если имя для отображения недоступно, используется имя класса, взятое из свойства name конструктора.

#### Touchables

* Метка доступности (accessibility label)
* Если ни один из вариантов не задан, выполняется поиск внутреннего текста
* Для кнопки-изображения выполняется поиск источника

#### Button Title

* Метка доступности (accessibility label)
* Для кнопки-изображения выполняется поиск источника
* Если ничего не найдено, выполняется поиск внутреннего текста

При минификации кода React Native можно использовать параметр `keep_classname`, чтобы сохранить имя класса.

## Похожие темы

* [Мониторинг React﻿](https://www.dynatrace.com/technologies/react-monitoring/)