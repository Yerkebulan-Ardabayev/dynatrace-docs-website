---
title: Инструментирование мобильных приложений с помощью плагина Dynatrace React Native
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native
scraped: 2026-05-12T11:23:03.543614
---

# Инструментирование мобильных приложений с помощью плагина Dynatrace React Native

# Инструментирование мобильных приложений с помощью плагина Dynatrace React Native

* How-to guide
* 4-min read
* Updated on Nov 26, 2024

Плагин React Native позволяет автоматически инструментировать React Native-приложения с помощью Dynatrace OneAgent для Android и iOS. Плагин предоставляет API для добавления ручного инструментирования и совместим с необработанными и выгруженными проектами React Native.

Подробная техническая документация доступна на странице [Dynatrace React Native plugin](https://www.npmjs.com/package/@dynatrace/react-native-plugin) на сайте npm.

Для настройки плагина Dynatrace React Native в мобильном приложении выполните следующие шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте мобильное приложение в Dynatrace**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#create-app-in-ui "Автоматически инструментируйте React Native-приложения с помощью OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте плагин React Native**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#set-up-plugin "Автоматически инструментируйте React Native-приложения с помощью OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Соберите и запустите приложение**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#build-and-run-app "Автоматически инструментируйте React Native-приложения с помощью OneAgent.")

## Предварительные требования

* React 16.8+
* React Native 0.60+
* Android версии 5.0+ (уровень API 21+)
* Gradle версии 7.0+
* Android Gradle plugin версии 7.0+
* Java 11
* iOS версии 12+

## Шаг 1 Создание мобильного приложения в Dynatrace

Чтобы создать мобильное приложение в Dynatrace:

1. В Dynatrace перейдите в раздел **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница параметров приложения.

## Шаг 2 Настройка плагина React Native

1. В параметрах приложения выберите **Instrumentation wizard** > **React Native**. Мастер инструментирования проведёт вас через процесс настройки.
2. Установите плагин Dynatrace React Native:

   React Native 0.60.0+

   * Выполните `npm install @dynatrace/react-native-plugin`.
   * Только iOS: если используются pods, перейдите в каталог `ios` и выполните `pod install`, чтобы установить новую зависимость Dynatrace в проект Xcode.
3. Зарегистрируйте трансформер Dynatrace: в корне проекта создайте или расширьте файл `metro.config.js` так, чтобы он содержал свойство `transformer.babelTransformerPath`:

   ```
   module.exports = {



   transformer: {



   babelTransformerPath: require.resolve('@dynatrace/react-native-plugin/lib/dynatrace-transformer')



   },



   reporter: require("@dynatrace/react-native-plugin/lib/dynatrace-reporter")



   };
   ```
4. В мастере инструментирования загрузите файл `dynatrace.config.js` и поместите его в корневой каталог проекта рядом с `app.json`. При обновлении с предыдущей версии плагина Dynatrace React Native скопируйте старые значения конфигурации из `dynatrace.config` в новый файл `dynatrace.config.js`.
5. Обновите конфигурацию Babel в файле `babel.config.js`, если используются следующие версии Metro или Expo:

   * Metro 0.72.0+
   * Expo 44.0.0+ или babel-preset-expo 9.0.0+

   Metro

   Expo

   С использованием `metro-react-native-babel-preset`:

   ```
   module.exports = {



   presets: [



   ['module:metro-react-native-babel-preset'],



   ],



   plugins: [



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

   С использованием `babel-preset-expo`:

   ```
   module.exports = {



   presets: [



   ['babel-preset-expo',



   {



   jsxRuntime: 'automatic',



   jsxImportSource: '@dynatrace/react-native-plugin',



   },



   ],



   ],



   };
   ```

## Шаг 3 Сборка и запуск приложения

* Выполните `npx instrumentDynatrace` в корне React Native-проекта для применения конфигурации из файла `dynatrace.config.js`. Эта команда настраивает как Android-, так и iOS-проекты.
* Выполните `react-native run-android` или `react-native run-ios` для пересборки и запуска приложения.

  При обновлении до React Native 0.70+ или использовании версии @react-native-community/cli 9.x+ автоматическое выполнение скрипта перед каждой командой `react-native run-android` или `react-native run-ios` больше не работает. Если конфигурация в файле `dynatrace.config.js` была изменена, выполните `npx instrumentDynatrace` для применения новой конфигурации.
* При каждом изменении конфигурации в файле `dynatrace.config.js` последовательно выполните следующие команды, а затем пересоберите приложение.

  1. `npx instrumentDynatrace` — для применения новой конфигурации из `dynatrace.config.js`
  2. `react-native start --reset-cache` — для сброса кэша. Без сброса кэша возможно смешение старой и новой конфигураций.
* Укажите пользовательские пути через [пользовательские аргументы](https://www.npmjs.com/package/@dynatrace/react-native-plugin#customizing-paths-for-configuration).

## Именование пользовательских действий

Подробнее об именовании пользовательских действий в Dynatrace см. в разделе [Правила именования пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions#user-action-naming-rules "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с приложением.").

#### React-представления

* `displayName`: проверяет, задано ли отображаемое имя для React-представлений.
* `class name`: если отображаемое имя недоступно, используется имя класса — свойство `name` из конструктора.

#### Нажимаемые элементы

* Метка специальных возможностей
* Если оба варианта недоступны, выполняется поиск внутреннего текста
* Для кнопки-изображения выполняется поиск источника

#### Заголовок кнопки

* Метка специальных возможностей
* Для кнопки-изображения выполняется поиск источника
* Если ничего не найдено, выполняется поиск внутреннего текста

При минификации кода React Native можно использовать параметр `keep_classname` для сохранения имени класса.

## Связанные темы

* [React monitoring](https://www.dynatrace.com/technologies/react-monitoring/)