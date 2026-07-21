---
title: Настройка Session Replay Classic для Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/session-replay-android
---

# Настройка Session Replay Classic для Android

# Настройка Session Replay Classic для Android

* Практическое руководство
* 7 минут на чтение
* Обновлено 22 июня 2026 г.

На этой странице описано, как включить и настроить Session Replay для приложений Android.

## Полный Session Replay Classic

[Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") на Android позволяет фиксировать взаимодействия клиентов с мобильным приложением и воспроизводить каждое касание, свайп, поворот экрана в формате, похожем на видео.

## Session Replay Classic для сбоев

Кроме того, его можно использовать для получения дополнительного контекста при анализе сбоев в виде видеозаписей экрана, воспроизводящих действия пользователя, предшествующие обнаруженному [сбою](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.")

## Предварительные требования

Убедись, что система соответствует следующим требованиям:

* Dynatrace версии 1.303
* OneAgent для Android версии 8.303
* Real User Monitoring включён для приложения
* Активная лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат

## Поддерживаемые технологии и известные ограничения

* Поддерживается Android 6.0+ (уровень API 23+).
* Поддерживается Android Gradle plugin 8.1.1+.
* Поддерживается Kotlin версии 2.1.0+.
* Jetpack Compose версии 1.4+ поддерживается начиная с OneAgent для Android версии 8.325.
* Session Replay недоступен для кроссплатформенных фреймворков, таких как Cordova, React Native, Flutter, Xamarin и других
* Для гибридного приложения Session Replay поддерживается только для нативной части приложения. Session Replay не поддерживается для браузерной части гибридного приложения.
* Поддерживаются только библиотеки AndroidX support. Такие классы, как Activity или Fragment в com.android.support, не поддерживаются.
* Рекомендуется не использовать другие инструменты отчётности о сбоях вместе с Dynatrace Session Replay.
* Session Replay может фиксировать только определённые события. Однако если нужно отслеживать конкретное представление или событие, которое не поддерживается по умолчанию, можно [зафиксировать пользовательское событие](/managed/observe/digital-experience/session-replay/session-replay-android#capture-custom-events "Set up Session Replay Classic for your Android apps to learn which actions your users perform.").
* Воспроизвести пользовательские сессии, записанные с помощью Session Replay, можно только в [определённых браузерах](/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Browser and TLS requirements for the Dynatrace Managed web UI, including supported browsers for Session Replay and Synthetic Monitoring.").
* Дополнительные сведения см. в разделе [Технические ограничения Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay Classic.").

Session Replay представляет собой видеоподобную реконструкцию взаимодействия пользователя с мобильным приложением, использующую зафиксированные события и данные. Из-за такого подхода воспроизведённая сессия может отличаться от фактического пользовательского опыта. Известные проблемы

* Фрагменты с анимациями появления и исчезновения могут вызывать проблемы, особенно при коротких анимациях.
* Плавающие кнопки действий (floating action buttons) могут вызывать проблемы с маскированием данных.
* Атрибут inputType в компоненте Button может приводить к тому, что кнопки при записи отображаются без текста.

## Включение Session Replay Classic на Android

Если это ещё не сделано, нужно выполнить все шаги, описанные в мастере инструментирования.

1. Перейти в раздел **Mobile**.
2. Выбрать мобильное приложение, которое нужно настроить.
3. Выбрать **More** (**…**) > **Edit** в верхнем правом углу плитки с именем приложения.
4. В настройках приложения выбрать **General** > **Enablement and cost control**.
5. Включить **Enable Full Session Replay** или **Enable Session Replay on crashes**. Доступны следующие варианты:

   * Включение Full Mobile Session Replay на 100%: будут зафиксированы все сессии
   * Включение Full Mobile Session Replay на значении ниже 100%: будет зафиксирована случайно выбранная сессия
   * Включение Session Replay on Crashes гарантирует, что независимо от настройки Enable Full Session Replay и её значения const и traffic control, все сессии со сбоем будут зафиксированы.
6. В настройках приложения выбрать **Instrumentation wizard**, затем выбрать **Android** или **iOS**.
7. Выполнить шаги мастера инструментирования.

Для версий Android Gradle plugin 4.0 и 4.1 нужно изменить опцию компиляции на Java 8. Это можно сделать на шаге мастера инструментирования под названием **Apply the Dynatrace plugin and add the plugin configuration**. Добавить следующий код в файл сборки верхнего уровня:

```
compileOptions {



sourceCompatibility 1.8



targetCompatibility 1.8



}
```

Для Android Gradle plugin 4.2+ Java 8 используется по умолчанию, поэтому изменение конфигурации не требуется.

## Маскирование конфиденциальных данных

### Уровни маскирования данных

Session Replay поставляется с тремя предустановленными уровнями маскирования:

* **Safest**, маскируются все редактируемые текстовые поля, изображения, метки, веб-представления и переключатели.
* **Safe**, маскируются все редактируемые текстовые поля.
* **Custom**, по умолчанию маскирует те же элементы, что и **Safest**, но можно точно определить, какие компоненты приложения или представления должны быть маскированы. Подробности см. в разделе [Настройка пользовательского маскирования](#custom-masking).

### Изменение уровня маскирования

По умолчанию OneAgent применяет уровень маскирования **Safest**. Чтобы изменить его на уровень **Safe** или **Custom**, нужно использовать API для настройки OneAgent. Если выбран уровень **Custom**, подробности о том, как задать, какие компоненты приложения или представления должны быть маскированы, см. в разделе [Настройка пользовательского маскирования](#custom-masking).

#### Пример 1: изменение уровня маскирования на Safe

Используй следующий код, чтобы установить уровень маскирования Safe.

```
MaskingConfiguration config = new MaskingConfiguration.Safe();



// .Safest or .Custom



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Пример 2: изменение уровня маскирования на Custom

Используй следующий код, чтобы установить уровень маскирования Custom. Дополнительные параметры см. в разделе [Настройка пользовательского маскирования](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom();



// .Safest or .Safe



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Пример 3: изменение уровня маскирования на Custom и удаление всех маскированных представлений

Используй следующий код, чтобы установить уровень маскирования Custom и удалить все маскированные представления (removeAllMaskedViews). Дополнительные параметры см. в разделе [Настройка пользовательского маскирования](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom().removeAllMaskedViews();



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

### Настройка пользовательского маскирования

Если [уровень маскирования данных](#masking-levels) установлен на **Custom**, можно использовать дополнительные методы API, чтобы определить, какие компоненты приложения или представления должны быть маскированы. Можно:

* [Маскировать представления](#mask-views).
* [Маскировать представления с помощью android:tag](#mask-views-android-tag).
* [Маскировать представления с помощью тега маскирования](#mask-views-masking-tag).
* [Маскировать композиции Jetpack Compose](#mask-jc-composables).

#### Маскирование представлений

Можно включить или отключить маскирование глобально или для выбранных компонентов, таких как текстовые поля, изображения, метки, веб-представления и переключатели.

```
Set<Class<? extends View>> set = new HashSet<Class<? extends View>>() {



add(ImageView.class);



add(WebView.class);



};



new MaskingConfiguration.Custom().addMaskedView(ImageView.class); // Adds one masked view



new MaskingConfiguration.Custom().addMaskedViews(set); // Adds all masked views



new MaskingConfiguration.Custom().removeMaskedView(ImageView.class); // Removes one masked view



new MaskingConfiguration.Custom().removeAllMaskedViews(); // Removes all masked views
```

Чтобы пользовательская конфигурация маскирования вступила в силу, её нужно применить. Пример кода см. в разделе [Изменение уровня маскирования на Custom и удаление всех маскированных представлений](#change-masking-level-custom-remove-all-masked-views).

#### Маскирование представлений с помощью `android:tag`

Можно также включить или отключить маскирование выбранных представлений на основе их `android:tag`.

```
Set<Integer> set = new HashSet<Integer>() {



add(R.id.view_id1);



add(R.id.view_id2);



};



new MaskingConfiguration.Custom().addMaskedIds(set);



new MaskingConfiguration.Custom().addNonMaskedIds(set);



new MaskingConfiguration.Custom().removeMaskedIds(set);



new MaskingConfiguration.Custom().removeNonMaskedIds(set);
```

Чтобы пользовательская конфигурация маскирования вступила в силу, её нужно применить. Пример кода см. в разделе [Изменение уровня маскирования на Custom и удаление всех маскированных представлений](#change-masking-level-custom-remove-all-masked-views).

#### Маскирование представлений с помощью тега маскирования

Представление также можно маскировать, добавив тег маскирования `data-dtrum-mask` в `android:tag` представления. Представление с этим тегом маскирования маскируется всегда.

#### Маскирование композиций Jetpack Compose

Jetpack Compose предоставляет функциональность ручного маскирования, которая позволяет управлять тем, какие композиции (composables) маскируются в Session Replay. Чтобы замаскировать композицию, нужно использовать модификатор `dtMask`.

```
import com.dynatrace.agent.compose.api.dtMask



@Composable



fun MyScreen() {



Column {



Text(



text = "This text will be masked",



modifier = Modifier.dtMask()



)



}



}
```

## Включение классических журналов Session Replay

Логи Session Replay включаются так же, как и для OneAgent. Подробнее см. в [Enable debug logging for Dynatrace Android Gradle plugin or OneAgent SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/debug-logging-oneagent "Activate the debug logs from OneAgent.").

## Захват пользовательских событий

Session Replay записывает только определённые события. Тем не менее можно отслеживать событие, которое не поддерживается по умолчанию.

```
DynatraceSessionReplay.trackCustomEvent("User logged")
```

## Изменение режима передачи изображений на Wi-Fi

По умолчанию все данные, информация о зафиксированных событиях и изображения, передаются через любое подключение. Однако можно настроить передачу изображений только при подключении пользователей к Wi-Fi, чтобы сэкономить их мобильный трафик.

```
DynatraceSessionReplay.setConfiguration(



Configuration.builder()



.withDataTransmissionMode(DataTransmissionMode.NOT_METERED_NETWORK)



.build()



)
```

## Устранение неполадок

* [User sessions are not recorded at all﻿](https://dt-url.net/cp2385m)
* [User sessions are recorded, but Session Replay is not available﻿](https://dt-url.net/4m038d9)

## Похожие темы

* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [View crash reports for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")