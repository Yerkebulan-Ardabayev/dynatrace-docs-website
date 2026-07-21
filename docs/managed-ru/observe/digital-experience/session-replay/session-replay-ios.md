---
title: Настройка Session Replay Classic для iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/session-replay-ios
---

# Настройка Session Replay Classic для iOS

# Настройка Session Replay Classic для iOS

* Практическое руководство
* Чтение занимает 8 минут
* Обновлено 03 июня 2026 г.

На этой странице описано, как включить и настроить Session Replay для приложений iOS.

Для приложений, скомпилированных с Xcode 26, требуется OneAgent для iOS версии 8.323 или выше.

## Full Session Replay Classic

[Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") на iOS позволяет фиксировать взаимодействие клиентов с мобильным приложением и воспроизводить каждое касание, свайп, поворот экрана в формате, похожем на видео.

## Session Replay Classic при сбоях

Кроме того, его можно использовать для получения дополнительного контекста при анализе сбоев в виде видеоподобных записей экрана, воспроизводящих действия пользователя, предшествующие обнаруженному [сбою](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.").

## Предварительные требования

Убедись, что система соответствует следующим требованиям:

* Dynatrace версии 1.303
* OneAgent для iOS версии 8.323
* Real User Monitoring включён для приложения
* Активная лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат
* Swift 5+
* iOS 15+
* Xcode 16+
* SwiftUI поддерживается.

* Real User Monitoring активирован для приложения
* Активная лицензия Dynatrace Digital Experience Monitoring
* URL веб-интерфейса имеет доверенный сертификат

* [Дополнительный диск](/managed/observe/digital-experience/session-replay/enable-session-replay-web#session-replay-disk "Learn the prerequisites and the procedure for enabling Session Replay Classic.") настроен для хранения данных пользовательских сессий

  Расчёт размера дополнительного диска

  Чтобы рассчитать размер дополнительного диска, учитывай следующее:

  + Размер обычной мобильной пользовательской сессии составляет около 300 КБ
  + Период хранения данных по умолчанию, 35 дней
  + Небольшой запас всегда полезен
    Используя эти оценки, рекомендуется рассчитывать размер дополнительного диска по следующей формуле:  
    `Размер дополнительного диска = Сессии, завершившиеся сбоем в день * Средний размер сессии (300 КБ) * Период хранения (35 дней) * Запас (1.5)`

## Известные ограничения и проблемы

### Технические ограничения

* Поддерживается iOS 15.0+.
* Swift 5+
* Xcode 16+
* SwiftUI поддерживается.
* Session Replay недоступен для tvOS и iPadOS.
* Session Replay недоступен для кроссплатформенных фреймворков, таких как Cordova, React Native, Flutter, Xamarin и подобных.
* Для гибридного приложения Session Replay поддерживается только для нативной части приложения. Для браузерной части Session Replay поддерживает только события загрузки веб-страницы.
* Рекомендуется не использовать другие инструменты отслеживания сбоев вместе с Dynatrace Session Replay.
* Session Replay может фиксировать только определённые события. Однако, если нужно отслеживать конкретное представление или событие, которое не поддерживается по умолчанию, можно [зафиксировать пользовательское событие](#capture-custom-events).
* Воспроизвести пользовательские сессии, записанные с Session Replay, можно только в [определённых браузерах](/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Browser and TLS requirements for the Dynatrace Managed web UI, including supported browsers for Session Replay and Synthetic Monitoring.").
* Для приложений iOS 26, собранных с Xcode 26, функциональность маскирования доступна только с OneAgent для iOS версии 8.323+.

Дополнительные сведения см. в разделе [Технические ограничения для Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay Classic.").

Session Replay представляет собой видеоподобную реконструкцию взаимодействий пользователя с мобильными приложениями на основе зафиксированных событий и данных. Из-за такого подхода воспроизведённые сессии могут отличаться от фактического пользовательского опыта. Известные проблемы

## Включение Session Replay Classic на iOS

Если это ещё не сделано, выполни все шаги, описанные в мастере инструментирования.

1. Перейди в **Mobile**.
2. Выбери мобильное приложение, которое нужно настроить.
3. Выбери **More** (**…**) > **Edit** в правом верхнем углу плитки с названием приложения
4. В настройках приложения выбери **General** > **Enablement and cost control**.
5. Включи **Enable Full Session Replay** и (или) **Enable Session Replay on crashes**. Доступны следующие варианты:

   * Включение Full Mobile Session Replay на 100%: будут зафиксированы все сессии
   * Включение Full Mobile Session Replay на значении менее 100%: будут зафиксированы случайно выбранные сессии
   * Включение Session Replay on Crashes гарантирует, что независимо от настройки Enable Full Session Replay и её значения const и traffic control, все сессии со сбоем будут зафиксированы
6. В настройках приложения выбери **Instrumentation wizard**, затем выбери **Android** или **iOS**.
7. Следуй шагам мастера инструментирования.

### Включение Session Replay Classic для приложений SwiftUI

OneAgent для iOS версии 8.249+

Если приложение SwiftUI уже [проинструментировано](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps."), для такого мобильного приложения можно дополнительно включить Session Replay.

Чтобы включить Session Replay для проинструментированного приложения SwiftUI

1. Выполни все шаги инструкции [**Enable Session Replay**](#enable-session-replay) выше.
2. Установи для [конфигурационного ключа `DTXSwiftUIEnableSessionReplayInstrumentation`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") значение `true` в файле [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") проекта.

   ```
   <key>DTXSwiftUIEnableSessionReplayInstrumentation</key>



   <true/>
   ```

#### Поддерживаемые контейнеры SwiftUI

Session Replay поддерживается для следующих контейнеров SwiftUI:

* [List﻿](https://developer.apple.com/documentation/swiftui/list/)
* [LazyVGrid﻿](https://developer.apple.com/documentation/swiftui/lazyvgrid)
* [LazyHGrid﻿](https://developer.apple.com/documentation/swiftui/lazyhgrid)

#### Известные ограничения для приложений SwiftUI

Dynatrace не инструментирует следующие контейнеры SwiftUI:

* Списки внутри extensions
* Списки со статическим содержимым
* Списки, у которых объект-источник данных не соответствует протоколу `Equatable`

## Маскирование конфиденциальных данных

### Уровни маскирования данных

Session Replay поставляется с тремя предустановленными уровнями маскирования:

* **Safest**, маскируются все редактируемые текстовые поля, изображения, метки, веб-представления и переключатели.
* **Safe**, маскируются все редактируемые текстовые поля.
* **Custom**, по умолчанию маскирует те же элементы, что и **Safest**, но можно самостоятельно определить, какие именно компоненты приложения или представления должны маскироваться. Подробности см. в разделе [Настройка пользовательского маскирования](#custom-masking).

### Изменение уровня маскирования

По умолчанию OneAgent применяет уровень маскирования **Safest**. Чтобы изменить его на уровень **Safe** или **Custom**, используй API для настройки OneAgent. Если выбран уровень **Custom**, подробности о том, как задать, какие компоненты приложения или представления должны маскироваться, см. в разделе [Настройка пользовательского маскирования](#custom-masking).

#### Пример 1: изменение уровня маскирования на Safe

Используй следующий код, чтобы установить уровень маскирования Safe.

```
let maskingConfiguration = MaskingConfiguration(maskingLevelType: .safe)



try? AgentManager.setMaskingConfiguration(maskingConfiguration)
```

### Настройка пользовательского маскирования

Если для [уровня маскирования данных](#data-masking-levels) установлено значение **Custom**, можно использовать дополнительные методы API, чтобы определить, какие компоненты приложения или представления должны маскироваться. Можно:

* [Включить или отключить правила маскирования](#enable-disable-masking-rules).
* [Маскировать представления с помощью accessibilityIdentifier](#mask-views-accessibilityIdentifier).
* [Маскировать представления с помощью тега маскирования](#mask-views-masking-tag).

#### Включение или отключение правил маскирования

Правила можно включать или отключать глобально или для отдельных выбранных компонентов, таких как текстовые поля, изображения, метки, веб-представления и переключатели.

```
try? maskingConfiguration.add(rule: .maskAllImages) // Adds one rule



try? maskingConfiguration.remove(rule: .maskAllSwitches) // Removes one rule



try? maskingConfiguration.addAllRules() // Adds all rules



try? maskingConfiguration.removeAllRules() // Removes all rules
```

Если удалить все правила маскирования, Session Replay не будет маскировать ничего. Если включить все правила маскирования, это эквивалентно уровню маскирования Safest.

#### Маскирование представлений с помощью accessibilityIdentifier

Можно включать или отключать маскирование выбранных представлений на основе их accessibilityIdentifier.

```
try? maskingConfiguration.addMaskedView(viewIds: ["masked_view_id"])



try? maskingConfiguration.removeMaskedView(viewIds: ["masked_view_id"])



try? maskingConfiguration.addNonMaskedView(viewIds: ["nonMasked_view_id"])



try? maskingConfiguration.removeNonMaskedView(viewIds: ["nonMasked_view_id"])
```

#### Маскирование представлений с помощью тега маскирования

Представление также можно замаскировать, добавив тег маскирования data-dtrum-mask в accessibilityIdentifier представления. Представление с этим тегом маскирования маскируется всегда.

## Включение классических логов Session Replay

Классические логи Session Replay включаются так же, как и для OneAgent. Подробности см. в разделе [Отладочное логирование для OneAgent на iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.")

## Захват пользовательских событий

Session Replay фиксирует только определённые события. Дополнительно можно захватывать пользовательские события, которые не поддерживаются по умолчанию. Пользовательское событие можно захватить со скриншотом конкретного представления, конкретной области экрана или всего экрана целиком

Все методы захвата пользовательских событий могут выбрасывать ошибку TrackCustomEventError.notInMainThread, если попытаться захватить пользовательское событие из потока, который не является основным. Рекомендуется использовать конструкцию do-catch, пока всё не заработает как надо, а затем можно заменить её более простой версией, которая при возникновении ошибки просто не захватывает пользовательское событие

```
do {



try AgentManager.trackCustomEvent(name: "my_event_name", view: nil)



} catch {



print(error)



}
```

### Конкретное представление

Захват пользовательского события со скриншотом конкретного представления

```
try? AgentManager.trackCustomEvent(name: "my_view_name", view: myView)
```

### Конкретная область экрана

Захват пользовательского события со скриншотом конкретной области экрана

```
try? AgentManager.trackCustomEvent(name: "my_view_name", frame: anyFrame)
```

### Весь экран

Захват пользовательского события со скриншотом всего экрана

```
try? AgentManager.trackCustomEvent(name: "my_view_name")
```

## Изменение режима передачи изображений на Wi-Fi

По умолчанию все данные, информация о захваченных событиях и изображения, отправляются по любому соединению. Однако можно настроить передачу изображений только при подключении пользователей к Wi-Fi, чтобы сэкономить их мобильный трафик

```
AgentManager.setTransmissionMode(.wifi) // .data by default
```

## Отладчик скриншотов

Отладчик скриншотов Session Replay позволяет видеть, когда делаются скриншоты, какие части экрана захватываются и какие данные, текстовые поля, изображения, надписи, веб-представления и переключатели, маскируются

Отладчик скриншотов Session Replay можно использовать при запуске мобильного приложения в симуляторе, поэтому не нужно ждать, пока сессия закроется и загрузится в Dynatrace.

![Screenshot debugger](https://dt-cdn.net/images/session-replay-screenshot-debugger-25-62c2c0bcf4.gif)

Отладчик скриншотов

После включения отладчика скриншотов Session Replay в проекте появляются соответствующие ключи. Обрати внимание, что эти ключи не отправляются в код приложения для релизных или архивных сборок, поэтому они никогда не попадают в продакшн-код. Эти ключи используются только для отладочных запусков.

![Screenshot debugger](https://dt-cdn.net/images/xcode-936-179db4b123.webp)

Отладчик скриншотов

Чтобы включить отладчик скриншотов Session Replay:

1. В Xcode выбрать **Edit Scheme** в меню Scheme, чтобы изменить схему приложения
2. В настройках схемы приложения выбрать действие **Run**, затем перейти на вкладку **Arguments**
3. В разделе Environment Variables добавить один или оба следующих ключа

   * **DTXDebugMasking**. Этот ключ показывает скриншоты, сделанные Session Replay, включая замаскированное содержимое и элементы управления интерфейсом. При каждом захвате скриншота отображается кратковременная вспышка
   * **DTXDebugFrameHighlight**. Этот ключ выделяет захваченную часть экрана красной рамкой, чтобы точно знать, какая часть экрана захватывается

## Устранение неполадок

* [Пользовательские сессии вообще не записываются﻿](https://dt-url.net/yw438pl)
* [Пользовательские сессии записываются, но Session Replay недоступен﻿](https://dt-url.net/74638c2)

## Похожие темы

* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Просмотр отчётов о сбоях мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")