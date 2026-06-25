---
title: Настройка Session Replay для Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/session-replay-android
scraped: 2026-05-12T11:33:32.742794
---

# Настройка Session Replay для Android

# Настройка Session Replay для Android

* How-to guide
* 7-min read
* Updated on Feb 18, 2026

На этой странице описано, как включить и настроить Session Replay для Android-приложений.

## Полный Session Replay

[Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.") для Android позволяет захватывать взаимодействия клиентов с вашим мобильным приложением и воспроизводить каждый тап, свайп и поворот экрана в виде фильма.

## Session Replay для анализа сбоев

Также вы можете использовать его для получения дополнительного контекста при анализе сбоев в виде видеозаписей, воспроизводящих действия пользователя перед обнаруженным [сбоем](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.").

## Предварительные условия

Убедитесь, что ваша система соответствует следующим требованиям:

* Dynatrace версии 1.303
* OneAgent для Android версии 8.303
* Real User Monitoring включён для вашего приложения
* Действующая лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат

## Поддерживаемые технологии и известные ограничения

* Поддерживается Android 5.0+ (API уровня 21+).
* Поддерживается Android Gradle plugin 7.0+.
* Поддерживается Kotlin версии 1.9+.

  + Kotlin версии 1.8 поддерживается для обеспечения совместимости с Kotlin.
* Jetpack Compose версии 1.4+ поддерживается начиная с OneAgent для Android версии 8.325.
* Session Replay недоступен для кроссплатформенных фреймворков, таких как Cordova, React Native, Flutter, Xamarin и других.
* Для гибридного приложения Session Replay поддерживается только для нативной части приложения. Для браузерной части Session Replay не поддерживается.
* Поддерживаются только библиотеки AndroidX. Такие классы, как Activity или Fragment из com.android.support, не поддерживаются.
* Не рекомендуется использовать другие инструменты для отчётов о сбоях совместно с Dynatrace Session Replay.
* Session Replay может захватывать только определённые события. Однако если вам нужно отслеживать конкретное представление или событие, не поддерживаемое по умолчанию, вы можете [захватить пользовательское событие](/managed/observe/digital-experience/session-replay/session-replay-android#capture-custom-events "Настройте Session Replay для Android-приложений, чтобы узнать, какие действия выполняют пользователи.").
* Воспроизводить записанные сессии можно только в [определённых браузерах](/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Узнайте, в каких браузерах работает Dynatrace Managed.").
* Подробнее см. [Технические ограничения Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Узнайте об ограничениях, применяемых к Session Replay.").

Session Replay — это видеоподобная реконструкция взаимодействий пользователя с мобильным приложением, основанная на захваченных событиях и данных. Из-за такого подхода воспроизведённая сессия может отличаться от реального пользовательского опыта. Известные проблемы:

* Фрагменты с анимациями появления/исчезновения могут вызывать проблемы, особенно при коротких анимациях.
* Кнопки с плавающим действием (floating action buttons) могут вызывать проблемы с маскированием данных.
* Атрибут inputType в компоненте Button может привести к тому, что кнопки будут отображаться без текста при захвате.

## Включение Session Replay для Android

Если вы ещё не сделали этого, выполните все шаги, описанные в мастере инструментирования.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое хотите настроить.
3. В правом верхнем углу плитки с именем приложения выберите **More** (**...**) > **Edit**.
4. В настройках приложения выберите **General** > **Enablement and cost control**.
5. Включите **Enable Full Session Replay** или **Enable Session Replay on crashes**. Доступны следующие варианты:

   * При включении Full Mobile Session Replay на 100% будут захватываться все сессии.
   * При включении Full Mobile Session Replay менее чем на 100% будут захватываться случайно выбранные сессии.
   * При включении Session Replay on Crashes гарантируется, что независимо от настройки Enable Full Session Replay и значения управления стоимостью и трафиком, все сессии со сбоями будут захвачены.
6. В настройках приложения выберите **Instrumentation wizard**, затем выберите **Android** или **iOS**.
7. Следуйте шагам в мастере инструментирования.

Для Android Gradle plugin версий 4.0 и 4.1 необходимо изменить параметр компиляции на Java 8. Это можно сделать на шаге мастера инструментирования **Apply the Dynatrace plugin and add the plugin configuration**. Добавьте следующий код в файл сборки верхнего уровня:

```
compileOptions {
    sourceCompatibility 1.8
    targetCompatibility 1.8
}
```

Для Android Gradle plugin 4.2+ Java 8 используется по умолчанию, поэтому изменение конфигурации не требуется.

## Маскирование конфиденциальных данных

### Уровни маскирования данных

Session Replay поставляется с тремя предопределёнными уровнями маскирования:

* **Safest** — все редактируемые текстовые поля, изображения, метки, веб-представления и переключатели маскируются.
* **Safe** — все редактируемые текстовые поля маскируются.
* **Custom** — по умолчанию маскирует те же элементы, что и **Safest**, но вы можете точно определить, какие компоненты или представления приложения должны маскироваться. Подробнее см. [Настройка пользовательского маскирования](#custom-masking).

### Изменение уровня маскирования

По умолчанию OneAgent применяет уровень маскирования **Safest**. Для изменения на уровень **Safe** или **Custom** используйте API для настройки OneAgent. При выборе уровня **Custom** см. [Настройка пользовательского маскирования](#custom-masking) для получения сведений о настройке маскируемых компонентов или представлений.

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

При установке [уровня маскирования данных](#masking-levels) в **Custom** вы можете использовать дополнительные методы API для определения, какие компоненты или представления должны маскироваться. Вы можете:

* [Маскировать представления](#mask-views).
* [Маскировать представления с использованием android:tag](#mask-views-android-tag).
* [Маскировать представления с использованием тега маскирования](#mask-views-masking-tag).
* [Маскировать компоненты Jetpack Compose](#mask-jc-composables).

#### Маскирование представлений

Вы можете включать или отключать маскирование глобально или для выбранных компонентов, таких как текстовые поля, изображения, метки, веб-представления и переключатели.

```
Set<Class<? extends View>> set = new HashSet<Class<? extends View>>(){{
    add(ImageView.class);
    add(WebView.class);
}};

new MaskingConfiguration.Custom().addMaskedView(ImageView.class); // Adds one masked view
new MaskingConfiguration.Custom().addMaskedViews(set); // Adds all masked views
new MaskingConfiguration.Custom().removeMaskedView(ImageView.class); // Removes one masked view
new MaskingConfiguration.Custom().removeAllMaskedViews(); // Removes all masked views
```

Необходимо применить конфигурацию пользовательского маскирования, чтобы она вступила в силу. Пример кода см. в [Изменение уровня маскирования на Custom и удаление всех маскированных представлений](#change-masking-level-custom-remove-all-masked-views).

#### Маскирование представлений с использованием `android:tag`

Вы также можете включать или отключать маскирование выбранных представлений на основе их `android:tag`.

```
Set<Integer> set = new HashSet<Integer>(){{
    add(R.id.view_id1);
    add(R.id.view_id2);
}};

new MaskingConfiguration.Custom().addMaskedIds(set);
new MaskingConfiguration.Custom().addNonMaskedIds(set);
new MaskingConfiguration.Custom().removeMaskedIds(set);
new MaskingConfiguration.Custom().removeNonMaskedIds(set);
```

Необходимо применить конфигурацию пользовательского маскирования, чтобы она вступила в силу.

#### Маскирование представлений с использованием тега маскирования

Вы также можете маскировать представление, добавив тег маскирования `data-dtrum-mask` в `android:tag` представления. Представление с этим тегом маскирования всегда маскируется.

#### Маскирование компонентов Jetpack Compose

Jetpack Compose предоставляет функцию ручного маскирования, позволяющую управлять тем, какие компоненты маскируются в Session Replay. Для маскирования компонента используйте модификатор `dtMask`.

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

## Включение журналов Session Replay

Журналы Session Replay можно включить так же, как и для OneAgent. Подробнее см. [Включение журналов отладки для Dynatrace Android Gradle plugin или OneAgent SDK](/managed/observe/digital-experience/mobile-applications/instrument-android-app/debug-logging-oneagent "Активируйте журналы отладки OneAgent.").

## Захват пользовательских событий

Session Replay записывает только определённые события. Однако вы можете отслеживать событие, не поддерживаемое по умолчанию.

```
DynatraceSessionReplay.trackCustomEvent("User logged")
```

## Изменение режима передачи на Wi-Fi для изображений

По умолчанию все данные — информация о захваченных событиях и изображениях — отправляются через любое соединение. Однако вы можете настроить передачу изображений только при подключении к Wi-Fi для экономии мобильного трафика пользователей.

```
DynatraceSessionReplay.setConfiguration(
    Configuration.builder()
    .withDataTransmissionMode(DataTransmissionMode.NOT_METERED_NETWORK)
    .build()
)
```

## Устранение неполадок

* [Сессии пользователей не записываются вообще](https://dt-url.net/cp2385m)
* [Сессии пользователей записываются, но Session Replay недоступен](https://dt-url.net/4m038d9)

## Связанные темы

* [Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.")
* [Просмотр отчётов о сбоях для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Проверьте последние отчёты о сбоях для ваших мобильных приложений.")