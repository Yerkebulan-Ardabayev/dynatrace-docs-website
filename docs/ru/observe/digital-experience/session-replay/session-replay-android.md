---
title: Настройка Session Replay для Android
source: https://www.dynatrace.com/docs/observe/digital-experience/session-replay/session-replay-android
scraped: 2026-03-02T21:21:17.753446
---

# Настройка Session Replay для Android

# Настройка Session Replay для Android

* Практическое руководство
* Время чтения: 7 мин.
* Обновлено 18 февраля 2026

На этой странице описано, как включить и настроить Session Replay для ваших Android-приложений.

## Полный Session Replay

[Session Replay](../session-replay.md "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются ваши клиенты.") на Android позволяет записывать взаимодействия ваших клиентов с мобильным приложением и воспроизводить каждое нажатие, свайп, поворот экрана в режиме, подобном видео.

## Session Replay при сбоях

Кроме того, вы можете использовать его для получения дополнительного контекста для анализа сбоев в виде видеоподобных записей экрана, воспроизводящих действия пользователя, предшествовавшие обнаруженному [сбою](../rum-concepts/user-and-error-events.md#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий пользователей и ошибок, фиксируемых Dynatrace.")

## Предварительные требования

Убедитесь, что ваша система соответствует следующим требованиям:

* Dynatrace версии 1.303
* OneAgent для Android версии 8.303
* Включен мониторинг реальных пользователей для вашего приложения
* Активная лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат

## Поддерживаемые технологии и известные ограничения

* Поддерживается Android 5.0+ (API level 21+).
* Поддерживается Android Gradle plugin 7.0+.
* Поддерживается Kotlin версии 1.9+.

  + Kotlin версии 1.8 поддерживается благодаря обратной совместимости Kotlin
* Jetpack Compose версии 1.4+ поддерживается начиная с OneAgent для Android версии 8.325.
* Session Replay недоступен для кроссплатформенных фреймворков, таких как Cordova, React Native, Flutter, Xamarin и других.
* Для гибридных приложений Session Replay поддерживается только для нативной части приложения. Session Replay не поддерживается для браузерной части гибридного приложения.
* Поддерживаются только библиотеки поддержки AndroidX. Классы, такие как Activity или Fragment в com.android.support, не поддерживаются.
* Мы рекомендуем не использовать другие инструменты отчетности о сбоях вместе с Dynatrace Session Replay.
* Session Replay может записывать только определенные события. Однако, если вам нужно отслеживать конкретное представление или событие, не поддерживаемое по умолчанию, вы можете [записать пользовательское событие](session-replay-android.md#capture-custom-events "Настройте Session Replay для ваших Android-приложений, чтобы узнать, какие действия выполняют ваши пользователи.").
* Воспроизводить пользовательские сессии, записанные с помощью Session Replay, можно только в [определенных браузерах](../../../discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements.md#session-replay "Узнайте, в каких браузерах могут работать приложения Dynatrace.").
* Дополнительную информацию см. в разделе [Технические ограничения Session Replay для веб-приложений](session-replay-restrictions-web.md "Узнайте, какие ограничения применяются к Session Replay.").

Session Replay -- это видеоподобная реконструкция взаимодействия пользователя с мобильным приложением, использующая записанные события и данные. Из-за такого подхода воспроизводимая сессия может отличаться от фактического пользовательского опыта. Известные проблемы

* Фрагменты с анимациями входа/выхода могут вызывать проблемы, особенно при коротких анимациях.
* Плавающие кнопки действий могут вызывать проблемы с маскированием данных.
* Атрибут inputType внутри компонента Button может приводить к тому, что кнопки отображаются без текста при записи.

## Включение Session Replay на Android

Если вы еще не сделали этого, выполните все шаги, описанные в мастере инструментирования.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое вы хотите настроить.
3. Выберите **More** (**...**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **General** > **Enablement and cost control**.
5. Включите **Enable Full Session Replay** или **Enable Session Replay on crashes**. Доступны следующие варианты:

   * Включение полного мобильного Session Replay на 100% -- все сессии будут записаны
   * Включение полного мобильного Session Replay на менее чем 100% -- случайно выбранные сессии будут записаны
   * Включение Session Replay при сбоях гарантирует, что независимо от настройки Enable Full Session Replay и значения контроля стоимости и трафика, все сессии со сбоями будут записаны.
6. В настройках приложения выберите **Instrumentation wizard**, затем выберите **Android** или **iOS**.
7. Следуйте шагам мастера инструментирования.

Для Android Gradle plugin версий 4.0 и 4.1 необходимо изменить опцию компиляции на Java 8. Это можно сделать на шаге мастера инструментирования под названием **Apply the Dynatrace plugin and add the plugin configuration**. Добавьте следующий код в файл сборки верхнего уровня:

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

* **Safest** -- маскируются все редактируемые текстовые поля, изображения, надписи, веб-представления и переключатели.
* **Safe** -- маскируются все редактируемые текстовые поля.
* **Custom** -- по умолчанию маскирует те же элементы, что и **Safest**, но вы можете точно определить, какие компоненты или представления приложения должны быть маскированы. Подробнее см. [Настройка пользовательского маскирования](#custom-masking).

### Изменение уровня маскирования

По умолчанию OneAgent применяет уровень маскирования **Safest**. Чтобы изменить его на уровень **Safe** или **Custom**, используйте API для настройки OneAgent. Если вы выбрали уровень **Custom**, см. [Настройка пользовательского маскирования](#custom-masking) для получения подробностей о том, какие компоненты или представления приложения должны быть маскированы.

#### Пример 1: Изменение уровня маскирования на Safe

Используйте следующий код для установки уровня маскирования Safe.

```
MaskingConfiguration config = new MaskingConfiguration.Safe();



// .Safest or .Custom



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Пример 2: Изменение уровня маскирования на Custom

Используйте следующий код для установки уровня маскирования Custom. Дополнительные параметры см. в [Настройка пользовательского маскирования](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom();



// .Safest or .Safe



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Пример 3: Изменение уровня маскирования на Custom и удаление всех маскированных представлений

Используйте следующий код для установки уровня маскирования Custom и удаления всех маскированных представлений (removeAllMaskedViews). Дополнительные параметры см. в [Настройка пользовательского маскирования](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom().removeAllMaskedViews();



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

### Настройка пользовательского маскирования

Если вы установили [уровень маскирования данных](#masking-levels) в **Custom**, вы можете использовать дополнительные методы API для определения того, какие компоненты или представления приложения должны быть маскированы. Вы можете:

* [Маскировать представления](#mask-views).
* [Маскировать представления с помощью android:tag](#mask-views-android-tag).
* [Маскировать представления с помощью тега маскирования](#mask-views-masking-tag).
* [Маскировать компоненты Jetpack Compose](#mask-jc-composables).

#### Маскирование представлений

Вы можете включить или отключить маскирование глобально или для выбранных компонентов, таких как текстовые поля, изображения, надписи, веб-представления и переключатели.

```
Set&lt;Class<? extends View&gt;> set = new HashSet&lt;Class<? extends View&gt;>()\\{{



add(ImageView.class);



add(WebView.class);



}};



new MaskingConfiguration.Custom().addMaskedView(ImageView.class); // Adds one masked view



new MaskingConfiguration.Custom().addMaskedViews(set); // Adds all masked views



new MaskingConfiguration.Custom().removeMaskedView(ImageView.class); // Removes one masked view



new MaskingConfiguration.Custom().removeAllMaskedViews(); // Removes all masked views
```

Вам необходимо применить конфигурацию пользовательского маскирования, чтобы она вступила в силу. См. [Изменение уровня маскирования на Custom и удаление всех маскированных представлений](#change-masking-level-custom-remove-all-masked-views) для примера кода.

#### Маскирование представлений с помощью `android:tag`

Вы также можете включить или отключить маскирование выбранных представлений на основе их `android:tag`.

```
Set&lt;Integer&gt; set = new HashSet&lt;Integer&gt;()\\{{



add(R.id.view_id1);



add(R.id.view_id2);



}};



new MaskingConfiguration.Custom().addMaskedIds(set);



new MaskingConfiguration.Custom().addNonMaskedIds(set);



new MaskingConfiguration.Custom().removeMaskedIds(set);



new MaskingConfiguration.Custom().removeNonMaskedIds(set);
```

Вам необходимо применить конфигурацию пользовательского маскирования, чтобы она вступила в силу. См. [Изменение уровня маскирования на Custom и удаление всех маскированных представлений](#change-masking-level-custom-remove-all-masked-views) для примера кода.

#### Маскирование представлений с помощью тега маскирования

Вы также можете маскировать представление, добавив тег маскирования `data-dtrum-mask` к `android:tag` представления. Представление с этим тегом маскирования всегда маскируется.

#### Маскирование компонентов Jetpack Compose

Jetpack Compose предоставляет функциональность ручного маскирования, которая позволяет контролировать, какие компоненты маскируются в Session Replay. Для маскирования компонента используйте модификатор `dtMask`.

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

## Включение логов Session Replay

Вы можете включить логи Session Replay так же, как и для OneAgent. Подробнее см. [Включение отладочного логирования для Dynatrace Android Gradle plugin или OneAgent SDK](../mobile-applications/instrument-android-app/debug-logging-oneagent.md "Активируйте отладочные логи OneAgent.").

## Запись пользовательских событий

Session Replay записывает только определенные события. Однако вы можете отслеживать событие, не поддерживаемое по умолчанию.

```
DynatraceSessionReplay.trackCustomEvent("User logged")
```

## Изменение режима передачи на Wi-Fi для изображений

По умолчанию все данные -- информация о записанных событиях и изображения -- отправляются через любое соединение. Однако вы можете настроить передачу изображений только при подключении пользователей к Wi-Fi для экономии мобильного трафика.

```
DynatraceSessionReplay.setConfiguration(



Configuration.builder()



.withDataTransmissionMode(DataTransmissionMode.NOT_METERED_NETWORK)



.build()



)
```

## Устранение неполадок

* [Пользовательские сессии не записываются вообще](https://dt-url.net/cp2385m)
* [Пользовательские сессии записываются, но Session Replay недоступен](https://dt-url.net/4m038d9)

## Связанные темы

* [Session Replay](../session-replay.md "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются ваши клиенты.")
* [Просмотр отчетов о сбоях для мобильных приложений](../mobile-applications/analyze-and-use/crash-reports-mobile.md "Просмотрите последние отчеты о сбоях для ваших мобильных приложений.")