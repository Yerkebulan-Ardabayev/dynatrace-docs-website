---
title: Настройка Session Replay для iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/session-replay-ios
scraped: 2026-05-12T11:33:35.180369
---

# Настройка Session Replay для iOS

# Настройка Session Replay для iOS

* How-to guide
* 8-min read
* Updated on Feb 27, 2026

На этой странице описано, как включить и настроить Session Replay для iOS-приложений.

Для приложений, скомпилированных с Xcode 26, требуется OneAgent для iOS версии 8.323 или более поздней.

## Полный Session Replay

[Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.") для iOS позволяет захватывать взаимодействия клиентов с вашим мобильным приложением и воспроизводить каждый тап, свайп и поворот экрана в виде фильма.

## Session Replay для анализа сбоев

Также вы можете использовать его для получения дополнительного контекста при анализе сбоев в виде видеозаписей, воспроизводящих действия пользователя перед обнаруженным [сбоем](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.").

## Предварительные условия

Убедитесь, что ваша система соответствует следующим требованиям:

* Dynatrace версии 1.303
* OneAgent для iOS версии 8.323
* Real User Monitoring включён для вашего приложения
* Действующая лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат
* Swift 5+
* iOS 12+
* Xcode 16+
* SwiftUI поддерживается.

* Real User Monitoring включён для вашего приложения
* Действующая лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат

* [Вторичный диск](/managed/observe/digital-experience/session-replay/enable-session-replay-web#session-replay-disk "Узнайте о предварительных условиях и процедуре включения Session Replay.") настроен для хранения данных сессий пользователей

  Расчёт размера вторичного диска

  При расчёте размера вторичного диска учтите следующее:

  + Размер обычной мобильной сессии составляет около 300 КБ
  + Срок хранения по умолчанию — 35 дней
  + Всегда полезно иметь некоторый запас
    Используя эти оценки, рекомендуется рассчитывать размер вторичного диска по формуле:  
    `Размер вторичного диска = Сессий со сбоем в день × Средний размер сессии (300 КБ) × Срок хранения (35 дней) × Буфер (1.5)`

## Известные ограничения и проблемы

### Технические ограничения

* Поддерживается iOS 12.0+.
* Swift 5+
* Xcode 15+
* SwiftUI поддерживается.
* Session Replay недоступен для tvOS и iPadOS.
* Session Replay недоступен для кроссплатформенных фреймворков, таких как Cordova, React Native, Flutter, Xamarin и аналогичных.
* Для гибридного приложения Session Replay поддерживается только для нативной части приложения. Для браузерной части Session Replay поддерживает только события загрузки веб-страниц.
* Не рекомендуется использовать другие инструменты для отчётов о сбоях совместно с Dynatrace Session Replay.
* Session Replay может захватывать только определённые события. Если вам нужно отслеживать конкретное представление или событие, не поддерживаемое по умолчанию, вы можете [захватить пользовательское событие](#capture-custom-events).
* Воспроизводить записанные сессии можно только в [определённых браузерах](/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Узнайте, в каких браузерах работает Dynatrace Managed.").
* Для iOS 26-приложений, скомпилированных с Xcode 26, функция маскирования доступна только с OneAgent для iOS версии 8.323+.

Подробнее см. [Технические ограничения Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Узнайте об ограничениях, применяемых к Session Replay.").

Session Replay — это видеоподобная реконструкция взаимодействий пользователя с мобильными приложениями, основанная на захваченных событиях и данных. Из-за такого подхода воспроизведённые сессии могут отличаться от реального пользовательского опыта.

## Включение Session Replay для iOS

Если вы ещё не сделали этого, выполните все шаги, описанные в мастере инструментирования.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое хотите настроить.
3. В правом верхнем углу плитки с именем приложения выберите **More** (**...**) > **Edit**.
4. В настройках приложения выберите **General** > **Enablement and cost control**.
5. Включите **Enable Full Session Replay** и/или **Enable Session Replay on crashes**. Доступны следующие варианты:

   * При включении Full Mobile Session Replay на 100% будут захватываться все сессии.
   * При включении Full Mobile Session Replay менее чем на 100% будут захватываться случайно выбранные сессии.
   * При включении Session Replay on Crashes гарантируется, что независимо от настройки Enable Full Session Replay и значения управления стоимостью и трафиком, все сессии со сбоями будут захвачены.
6. В настройках приложения выберите **Instrumentation wizard**, затем выберите **Android** или **iOS**.
7. Следуйте шагам в мастере инструментирования.

### Включение Session Replay для SwiftUI-приложений

OneAgent для iOS версии 8.249+

Если вы уже [инструментировали своё SwiftUI-приложение](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Используйте Dynatrace SwiftUI instrumentor для мониторинга SwiftUI-приложений."), вы можете дополнительно включить Session Replay для него.

Для включения Session Replay в инструментированном SwiftUI-приложении:

1. Выполните все шаги [инструкции по включению Session Replay](#enable-session-replay) выше.
2. Установите [ключ конфигурации `DTXSwiftUIEnableSessionReplayInstrumentation`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "С помощью ключей конфигурации можно точно настроить автоматическое инструментирование iOS-приложений.") в значение `true` в файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит идентификационную и конфигурационную информацию приложения. Используйте его для тонкой настройки конфигурации инструментирования.") вашего проекта.

   ```
   <key>DTXSwiftUIEnableSessionReplayInstrumentation</key>
   <true/>
   ```

#### Поддерживаемые SwiftUI-контейнеры

Session Replay поддерживается для следующих SwiftUI-контейнеров:

* [List](https://developer.apple.com/documentation/swiftui/list/)
* [LazyVGrid](https://developer.apple.com/documentation/swiftui/lazyvgrid)
* [LazyHGrid](https://developer.apple.com/documentation/swiftui/lazyhgrid)

#### Известные ограничения для SwiftUI-приложений

Dynatrace не инструментирует следующие SwiftUI-контейнеры:

* Lists внутри расширений
* Lists со статическим контентом
* Lists, у которых источник данных не соответствует протоколу `Equatable`

## Маскирование конфиденциальных данных

### Уровни маскирования данных

Session Replay поставляется с тремя предопределёнными уровнями маскирования:

* **Safest** — все редактируемые текстовые поля, изображения, метки, веб-представления и переключатели маскируются.
* **Safe** — все редактируемые текстовые поля маскируются.
* **Custom** — по умолчанию маскирует те же элементы, что и **Safest**, но вы можете точно определить, какие компоненты или представления должны маскироваться. Подробнее см. [Настройка пользовательского маскирования](#custom-masking).

### Изменение уровня маскирования

По умолчанию OneAgent применяет уровень маскирования **Safest**. Для изменения на уровень **Safe** или **Custom** используйте API для настройки OneAgent. При выборе уровня **Custom** см. [Настройка пользовательского маскирования](#custom-masking) для получения сведений о настройке маскируемых компонентов.

#### Пример 1: Изменение уровня маскирования на Safe

Используйте следующий код для установки уровня маскирования Safe.

```
let maskingConfiguration = MaskingConfiguration(maskingLevelType: .safe)

try? AgentManager.setMaskingConfiguration(maskingConfiguration)
```

### Настройка пользовательского маскирования

При установке [уровня маскирования данных](#data-masking-levels) в **Custom** вы можете использовать дополнительные методы API для определения маскируемых компонентов или представлений. Вы можете:

* [Включать или отключать правила маскирования](#enable-disable-masking-rules).
* [Маскировать представления с использованием accessibilityIdentifier](#mask-views-accessibilityIdentifier).
* [Маскировать представления с использованием тега маскирования](#mask-views-masking-tag).

#### Включение или отключение правил маскирования

Вы можете включать или отключать правила глобально или для выбранных компонентов, таких как текстовые поля, изображения, метки, веб-представления и переключатели.

```
try? maskingConfiguration.add(rule: .maskAllImages) // Adds one rule
try? maskingConfiguration.remove(rule: .maskAllSwitches) // Removes one rule
try? maskingConfiguration.addAllRules() // Adds all rules
try? maskingConfiguration.removeAllRules() // Removes all rules
```

При удалении всех правил маскирования Session Replay не будет маскировать ничего. При включении всех правил эффект эквивалентен уровню Safest.

#### Маскирование представлений с использованием accessibilityIdentifier

Вы можете включать или отключать маскирование выбранных представлений на основе их accessibilityIdentifier.

```
try? maskingConfiguration.addMaskedView(viewIds: ["masked_view_id"])
try? maskingConfiguration.removeMaskedView(viewIds: ["masked_view_id"])
try? maskingConfiguration.addNonMaskedView(viewIds: ["nonMasked_view_id"])
try? maskingConfiguration.removeNonMaskedView(viewIds: ["nonMasked_view_id"])
```

#### Маскирование представлений с использованием тега маскирования

Вы также можете маскировать представление, добавив тег маскирования data-dtrum-mask в accessibilityIdentifier представления. Представление с этим тегом маскирования всегда маскируется.

## Включение журналов Session Replay

Журналы Session Replay можно включить так же, как и для OneAgent. Подробнее см. [Журналы отладки OneAgent для iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Включите журналы отладки для OneAgent.").

## Захват пользовательских событий

Session Replay записывает только определённые события. Дополнительно можно захватывать пользовательские события, не поддерживаемые по умолчанию. Можно захватить пользовательское событие со скриншотом конкретного представления, конкретной области экрана или всего экрана.

Все методы для захвата пользовательских событий могут выбросить ошибку TrackCustomEventError.notInMainThread при попытке захвата из потока, отличного от основного. Рекомендуется использовать конструкцию do-catch, пока всё не заработает корректно; затем её можно заменить более простым вариантом.

```
do {
    try AgentManager.trackCustomEvent(name: "my_event_name", view: nil)
} catch {
    print(error)
}
```

### Конкретное представление

Захват пользовательского события со скриншотом конкретного представления:

```
try? AgentManager.trackCustomEvent(name: "my_view_name", view: myView)
```

### Конкретная область экрана

Захват пользовательского события со скриншотом конкретной области экрана:

```
try? AgentManager.trackCustomEvent(name: "my_view_name", frame: anyFrame)
```

### Весь экран

Захват пользовательского события со скриншотом всего экрана:

```
try? AgentManager.trackCustomEvent(name: "my_view_name")
```

## Изменение режима передачи на Wi-Fi для изображений

По умолчанию все данные — информация о захваченных событиях и изображениях — отправляются через любое соединение. Однако вы можете настроить передачу изображений только при подключении к Wi-Fi для экономии мобильного трафика пользователей.

```
AgentManager.setTransmissionMode(.wifi) // .data by default
```

## Отладчик скриншотов

Отладчик скриншотов Session Replay позволяет видеть момент создания скриншотов, какие части экрана захватываются и какие данные (текстовые поля, изображения, метки, веб-представления и переключатели) маскируются.

Вы можете использовать отладчик скриншотов Session Replay при запуске мобильного приложения в симуляторе, не дожидаясь закрытия сессии и её загрузки в Dynatrace.

![Отладчик скриншотов](https://dt-cdn.net/images/session-replay-screenshot-debugger-25-62c2c0bcf4.gif)

Отладчик скриншотов

После включения отладчика скриншотов Session Replay вы можете видеть соответствующие ключи в вашем проекте. Обратите внимание, что эти ключи не передаются в код приложения при release или archive-сборках, поэтому они никогда не включаются в production-код. Эти ключи используются только для debug-запусков.

![Отладчик скриншотов](https://dt-cdn.net/images/xcode-936-179db4b123.webp)

Отладчик скриншотов

Для включения отладчика скриншотов Session Replay:

1. В Xcode выберите **Edit Scheme** в меню Scheme для изменения схемы приложения.
2. В настройках схемы приложения выберите действие **Run**, затем перейдите на вкладку **Arguments**.
3. В разделе Environment Variables добавьте один или оба из следующих ключей:

   * **DTXDebugMasking**. Этот ключ показывает скриншоты, сделанные Session Replay, включая маскированный контент и элементы управления. Для каждого захваченного скриншота отображается краткая вспышка.
   * **DTXDebugFrameHighlight**. Этот ключ выделяет захваченную часть экрана красной рамкой, чтобы вы точно знали, какая область захватывается.

## Устранение неполадок

* [Сессии пользователей не записываются вообще](https://dt-url.net/yw438pl)
* [Сессии пользователей записываются, но Session Replay недоступен](https://dt-url.net/74638c2)

## Связанные темы

* [Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.")
* [Просмотр отчётов о сбоях для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Проверьте последние отчёты о сбоях для ваших мобильных приложений.")