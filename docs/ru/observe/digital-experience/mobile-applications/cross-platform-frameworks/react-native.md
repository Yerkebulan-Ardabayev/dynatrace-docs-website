---
title: Instrument mobile apps with Dynatrace React Native plugin
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native
scraped: 2026-03-05T21:25:22.621291
---

# Инструментирование мобильных приложений с помощью плагина Dynatrace React Native

# Инструментирование мобильных приложений с помощью плагина Dynatrace React Native

* Classic
* How-to guide
* 4-min read
* Updated on Nov 26, 2024

Наш плагин React Native позволяет вам автоматически инструментировать ваши приложения React Native с помощью Dynatrace OneAgent для Android и iOS. Плагин предоставляет API для добавления ручного инструментирования и совместим с обычными, извлечёнными проектами React Native.

Подробную техническую документацию см. на странице [плагина Dynatrace React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin) на сайте npm.

Следуйте приведённым ниже шагам для настройки плагина Dynatrace React Native для вашего мобильного приложения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте мобильное приложение в Dynatrace**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#create-app-in-ui "Автоматическое инструментирование ваших приложений React Native с помощью OneAgent.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройте плагин React Native**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#set-up-plugin "Автоматическое инструментирование ваших приложений React Native с помощью OneAgent.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Соберите и запустите приложение**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native#build-and-run-app "Автоматическое инструментирование ваших приложений React Native с помощью OneAgent.")

## Предварительные требования

* React 16.8+
* React Native 0.60+
* Android версии 5.0+ (API 21+)
* Gradle версии 7.0+
* Android Gradle plugin версии 7.0+
* Java 11
* iOS версии 12+

## Шаг 1: Создайте мобильное приложение в Dynatrace

Чтобы создать мобильное приложение в Dynatrace:

1. В Dynatrace перейдите в раздел **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя для вашего приложения и выберите **Create mobile app**. Откроется страница настроек приложения.

## Шаг 2: Настройте плагин React Native

1. В настройках приложения выберите **Instrumentation wizard** > **React Native**. Мастер инструментирования проведёт вас через процесс настройки.
2. Установите плагин Dynatrace React Native:

   React Native 0.60.0+

   * Выполните `npm install @dynatrace/react-native-plugin`.
   * Только для iOS: если вы используете pods, перейдите в каталог `ios` и выполните `pod install` для установки новой зависимости Dynatrace в ваш проект Xcode.
3. Зарегистрируйте трансформер Dynatrace: в корне проекта создайте или расширьте `metro.config.js` так, чтобы он содержал свойство `transformer.babelTransformerPath`:

   ```
   module.exports = {



   transformer: {



   babelTransformerPath: require.resolve('@dynatrace/react-native-plugin/lib/dynatrace-transformer')



   },



   reporter: require("@dynatrace/react-native-plugin/lib/dynatrace-reporter")



   };
   ```
4. Из мастера инструментирования скачайте файл `dynatrace.config.js` и поместите его в корневой каталог вашего проекта рядом с `app.json`. Если вы обновляетесь с предыдущей версии плагина Dynatrace React Native, скопируйте старые значения конфигурации из `dynatrace.config` в новый файл `dynatrace.config.js`.
5. Обновите конфигурацию Babel в файле `babel.config.js`, если вы используете следующие версии Metro или Expo:

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

## Шаг 3: Соберите и запустите приложение

* Выполните `npx instrumentDynatrace` в корне вашего проекта React Native, чтобы применить конфигурацию, заданную в файле `dynatrace.config.js`. Эта команда настраивает проекты как для Android, так и для iOS.
* Выполните `react-native run-android` или `react-native run-ios`, чтобы пересобрать и запустить ваше приложение.

  Если вы обновляетесь до React Native 0.70+ или используете @react-native-community/cli версии 9.x+, обратите внимание, что наш автоматизированный скрипт, запускающийся перед каждой командой `react-native run-android` или `react-native run-ios`, больше не работает. Если вы изменили конфигурацию в файле `dynatrace.config.js`, выполните `npx instrumentDynatrace` для применения новой конфигурации.
* При каждом изменении конфигурации в файле `dynatrace.config.js` выполните следующие команды и затем пересоберите приложение:

  1. `npx instrumentDynatrace` -- для применения новой конфигурации из `dynatrace.config.js`
  2. `react-native start --reset-cache` -- для сброса кеша. Без сброса кеша может использоваться смесь старой и новой конфигурации.
* Укажите пользовательские пути через [пользовательские аргументы](https://www.npmjs.com/package/@dynatrace/react-native-plugin#customizing-paths-for-configuration).

## Именование действий пользователя

См. [Правила именования действий пользователя](/docs/observe/digital-experience/rum-concepts/user-actions#user-action-naming-rules "Узнайте, что такое действия пользователя и как они помогают понять, что пользователи делают с вашим приложением.") для получения подробной информации об именовании действий пользователя в Dynatrace.

#### Представления React

* `displayName`: проверяет, установлено ли отображаемое имя для представлений React.
* `class name`: если отображаемое имя недоступно, используется имя класса, взятое из свойства name конструктора.

#### Touchables

* Accessibility label
* Если оба не заданы, выполняется поиск внутреннего текста
* Для кнопки-изображения выполняется поиск источника

#### Button Title

* Accessibility label
* Для кнопки-изображения выполняется поиск источника
* Если ничего не найдено, выполняется поиск внутреннего текста

Если вы минифицируете код React Native, вы можете использовать настройку `keep_classname` для сохранения имени класса.

## Связанные темы

* [Мониторинг React](https://www.dynatrace.com/technologies/react-monitoring/)
