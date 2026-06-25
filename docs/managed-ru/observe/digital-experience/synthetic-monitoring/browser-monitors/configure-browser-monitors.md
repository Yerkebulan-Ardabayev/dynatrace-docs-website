---
title: Настройка браузерных мониторов
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors
scraped: 2026-05-12T11:31:45.322340
---

# Настройка браузерных мониторов

# Настройка браузерных мониторов

* How-to guide
* 15-min read
* Updated on Mar 30, 2026

Настраивайте браузерные мониторы при первоначальной установке и в любое время после этого.

При создании браузерного монитора ([по одному URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как настроить браузерный монитор по одному URL для проверки доступности сайта.") или [clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.")) настройки отображаются после выбора **Create a browser monitor**. Эти настройки являются подмножеством полного набора, доступного в режиме редактирования (описан ниже) после развёртывания монитора. Например, пороговые значения [производительности](#performance-thresholds) или [доступности](#outage-handling) можно задать только после создания монитора.

## Настройка существующего браузерного монитора

Для настройки или редактирования существующего монитора по одному URL или браузерного clickpath-а

1. Перейдите в **Synthetic Classic**.
2. Выберите браузерный монитор для настройки.
3. Нажмите **Edit** в быстрых ссылках для перехода к настройкам монитора. Также можно перейти в **Synthetic Classic**, установить флажок рядом с нужным монитором и нажать **Edit** внизу страницы.
4. Перейдите по вкладкам **Monitor settings** слева для настройки параметров (описание ниже; часть параметров доступна при первоначальной настройке монитора).

   * [General](#monitor-setup)
   * [Recorded clickpath](#recorded-clickpath)
   * [Frequency and locations](#frequency-locations)
   * [Validate content](#validate-content)
   * [Outage handling](#outage-handling)
   * [Performance thresholds](#performance-thresholds)
   * [Monitor scripts](#monitor-scripts)
   * [Advanced setup](#advanced-setup)
   * [Metrics](#metrics)
5. **Save changes** в правом нижнем углу после завершения редактирования. (Можно также **Discard changes**.)

## General

Укажите **Monitor name**. Имя ограничено 500 символами.

Для [браузерных мониторов по одному URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как настроить браузерный монитор по одному URL для проверки доступности сайта.") здесь можно отредактировать **HTTP/HTTPS URL** монитора. (Для [clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") эта информация хранится в [событии Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.").)

### Профиль устройства

Свойства эмулируемого устройства: профиль/тип **Device**, ориентация, **Screen size**, **Bandwidth** и **User agent**.

Профиль устройства по умолчанию: **Desktop**.

* Для профилей мобильных устройств (включая планшеты) можно выбрать ориентацию и **Bandwidth**. **User agent** выбирается автоматически, но может быть изменён.
* Для **Custom**-устройства укажите, является ли оно **Mobile device**, выберите ориентацию, **Bandwidth** и **Screen size**. Этот профиль использует user agent Dynatrace по умолчанию, который можно изменить.
* Для профилей десктопа и ноутбука можно выбрать **Bandwidth**. Эти профили используют user agent Dynatrace по умолчанию.

User agent по умолчанию

* User agent Dynatrace по умолчанию при записи и локальном воспроизведении имеет формат `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 RuxitSynthetic/1.0 v0 t0 cfeatureHash=7efgijmoqtvx caes=1 ccux=1 sia=1 smf=1`, где:

  + `{version}` — текущая версия браузера, используемая при записи.
  + `v0` и `t0` идентифицируют трафик Synthetic Monitoring.
  + `sia=1` указывает на более быстрое внедрение RUM JavaScript (значение может быть `1` или `0`).
  + `smf=1` указывает на мониторинг страниц в фреймах (требует включения **Capture performance metrics for pages loaded in frames** в [**Advanced setup**](#advanced-setup); значение `0`, если не включено).
  + `cfeatureHash=<value>` появляется при включении пользовательских настроек RUM JavaScript в **Advanced setup**.
  + Другие пары ключ-значение, начинающиеся с `c`, появляются при наличии пользовательских свойств RUM JavaScript в **Advanced setup**.

    ![Custom JS tag properties](https://dt-cdn.net/images/browsermonitorcustomjsconfig-619-249e8a4425.png)

    Custom JS tag properties
* User agent по умолчанию для выполнения браузерных мониторов из публичных или частных расположений Synthetic имеет формат `Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 RuxitSynthetic/1.0 v{id} t{id} ath{id} alt{id} cfeatureHash=7efgijmoqtvx caes=1 ccux=1 sia=1 smf=1`, где:

  + `{id}` представляет длинные ID, используемые Dynatrace для идентификации выполнения монитора.
  + Другие параметры описаны выше.

  Обратите внимание: даже если задан пользовательский user agent, Dynatrace всегда автоматически добавляет `RuxitSynthetic/1.0 v{id} t{id} ath{id} alt{id}`, `sia`, `smf` и, при наличии, `cfeaturehash` и пары ключ-значение, начинающиеся с `c`, чтобы трафик Synthetic Monitoring мог быть идентифицирован.

Ограничение полосы пропускания

Параметры ограничения полосы пропускания Synthetic Monitoring, их скорости и задержки:

| Bandwidth | Download | Upload | Latency |
| --- | --- | --- | --- |
| DSL | 2 Mb/s | 1 Mb/s | 5ms RTT |
| GPRS | 50 kb/s | 20 kb/s | 500ms RTT |
| Good 2G | 450 kb/s | 150 kb/s | 150ms RTT |
| Good 3G | 1 Mb/s | 750 kb/s | 40ms RTT |
| Regular 2G | 250 kb/s | 50 kb/s | 300ms RTT |
| Regular 3G | 750 kb/s | 250 kb/s | 100ms RTT |
| Regular 4G | 4 Mb/s | 3 Mb/s | 20ms RTT |
| WiFi | 30 Mb/s | 15 Mb/s | 2ms RTT |

Если устройство монитора больше не доступно в списке

Все настройки устройства (размер экрана, полоса пропускания, ориентация) сохраняются; выбор устройства меняется на **Custom**.

### Ключевые метрики производительности

Этот параметр доступен только в режиме редактирования.

Для каждого load action и XHR action в браузерном мониторе или clickpath-е можно выбрать одну ключевую метрику производительности.

[**Ключевые метрики производительности**](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Узнайте, как использовать правильные ключевые метрики производительности для оптимизации данных о пользовательском опыте.") позволяют выбирать цели производительности, наиболее подходящие для каждого отслеживаемого приложения. Например, для традиционного веб-приложения можно выбрать User action duration. Для других приложений, где важнее скорость взаимодействия, а не UI, можно оптимизировать время загрузки JavaScript-ресурсов. По умолчанию для load и XHR actions выбирается **Visually complete** — метрика, измеряющая время полного отрисовки видимой части браузера пользователя.

Поскольку Dynatrace собирает список ключевых метрик производительности из коробки, можно изменить выбор в настройках монитора и сразу получить исторические данные.

![Monitor settings KPM](https://dt-cdn.net/images/monitorsettingskpm-849-ebdc51e729.png)

Monitor settings KPM

Ключевая метрика производительности рассчитывается и отображается как среднее на [странице Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") в визуализациях производительности и на [карточке Synthetic events and actions](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#events-actions "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").

### Назначенные приложения

Этот параметр доступен только в режиме редактирования.

Если синтетический монитор связан с одним из отслеживаемых приложений, можно назначить монитор на это приложение для отслеживания его доступности и производительности. Обнаруженные проблемы автоматически связываются с приложением. Если монитор недоступен, связанное приложение также считается недоступным.

Нажмите **Assign to application** и выберите приложение из списка. Монитор можно назначить на несколько приложений, а одно приложение может иметь несколько назначенных мониторов.

Браузерный монитор можно назначить на веб-приложение.

На этой вкладке также отображаются отдельные списки автоматически назначенных и вручную связанных приложений. Вручную связанные приложения можно отвязать здесь.

Обратите внимание: невозможно заблокировать трафик Synthetic Monitoring для RUM-приложений путём [исключения ботов, поисковых роботов или IP-адресов расположений Synthetic](/managed/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Отключите Real User Monitoring для определённых IP-адресов, браузеров, ботов и поисковых роботов.").

![Browser monitor: Assigned applications](https://dt-cdn.net/images/bm-assigned-applications-1320-1d1646a6b1.png)

Browser monitor: Assigned applications

## Recorded clickpath

Вы можете редактировать [записанный clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.").

Если записанный clickpath захватил учётные данные, например пароль, отображается опция сохранения их в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище."). На изображении ниже показан записанный clickpath с захваченным паролем.

![Captured credential](https://dt-cdn.net/images/clickpathcapturedpasswordkeystroke1-1348-ee32fa536a.png)

Captured credential

Подробнее об учётных данных см. в разделах [событие Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") и [событие Keystroke](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#keystroke "Узнайте о типах событий при записи браузерного clickpath-а.").

Нажмите **Record again** для перезаписи clickpath-а. Можно выбрать: перезаписать clickpath полностью (с первого URL события) или после воспроизведения до указанного события. Обратите внимание: при полной перезаписи с нуля все JavaScript-события, предшествующие начальному событию Navigate, будут удалены — см. [События браузерных clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

![Record a clickpath again](https://dt-cdn.net/images/recordagainclickpath-344-85b24812cc.png)

Record a clickpath again

Также можно выполнить локальное воспроизведение (**Play back clickpath**) для проверки корректности работы записанного clickpath-а.

Если с браузерным монитором связаны учётные данные (публичные или только для владельца), пользователям нужно ввести учётные данные для локального воспроизведения. Однако если включить **Enable local playback of Synthetic browser monitors without entering credentials** в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище."), пользователи смогут воспроизводить браузерный монитор без ввода доступных им учётных данных.

Например, при воспроизведении clickpath-а с одним публичным credential и одним credential только для владельца другого пользователя вводить публичный credential не нужно. Фактически это означает, что воспроизведение clickpath-а с учётными данными без доступа к ним может быть невозможно.

![Play back clickpath](https://dt-cdn.net/images/playbackclickpathcredentials-1882-d0bebc2291.png)

Play back clickpath

Можно оставить окно воспроизведения открытым после завершения (**Keep window open after playback**), например, для отладки сбойного выполнения или тестирования JavaScript-кода на сайте.

* Каждый запуск монитора начинается в чистом состоянии: с очищенным кэшем браузера и пустым [локальным хранилищем](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
* Локальное воспроизведение в Dynatrace работает в режиме эмуляции на основе профиля устройства и user agent, выбранных при настройке монитора. То есть воспроизведение эмулирует выбранное устройство. При переходе к тому же URL вне Dynatrace впечатление может отличаться.

Вы не ограничены одним режимом просмотра и редактирования clickpath-а: можно переключаться между UI и script mode, выбирая **Clickpath** или **Script**. Подробности о редактировании clickpath-а в формате JSON см. в разделе [Script mode для настройки браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте и редактируйте браузерные мониторы в формате JSON.").

В visual/UI mode доступны следующие элементы управления для редактирования событий скрипта:

При необходимости можно удалить события из clickpath-а, нажав **x** в столбце **Delete** для соответствующего события. Также можно добавлять события: нажмите **Add synthetic event**. Укажите имя, [тип события](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий при записи браузерного clickpath-а.") и событие, после которого оно должно следовать.

![Add synthetic event](https://dt-cdn.net/images/addsyntheticevent-367-3353ee375a.jpg)

Add synthetic event

Используйте стрелки **Move up/down** для изменения порядка событий. Обратите внимание: первому [событию Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") clickpath-а могут предшествовать только [JavaScript-события](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

Хотя мы стараемся называть события интуитивно понятно, при необходимости можно редактировать имена событий, просто кликнув в поле имени.

Кроме того, можно настроить каждое событие, наведя курсор и кликнув, когда курсор изменится на указатель. В деталях события можно удалить его, выбрав **Delete synthetic event**. Обратите внимание: первое [событие Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") clickpath-а удалить нельзя.

![Edit a synthetic event](https://dt-cdn.net/images/editsyntheticevent-1638-9dc9afa1ef.png)

Edit a synthetic event

Доступные для редактирования поля зависят от типа события — подробные описания см. в разделе [События браузерных clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий при записи браузерного clickpath-а."). После завершения редактирования обязательно нажмите **Save changes**. При необходимости выберите **Close details** для выхода из деталей события.

![Synthetic event UI](https://dt-cdn.net/images/recordedclickpatheditevent1-1369-f196cf21e4.jpg)

Synthetic event UI

Событие clickpath-а — это не то же самое, что действие. Подробности см. в разделе [Количество действий, потребляемых браузерными clickpath-ами](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.").

## Frequency and locations

Расписание мониторинга определяется двумя факторами: как часто запускается браузерный монитор и из скольких расположений.

Dynatrace предлагает глобальную сеть [публичных расположений Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.") из коробки. Также можно [создавать частные расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") в собственной сетевой инфраструктуре. Как публичные, так и частные расположения отображаются на этой странице настроек.

Частота и количество расположений определяют количество выполнений монитора в час. Например, запуск монитора из 3 расположений каждые 15 минут даёт 12 выполнений в час (4 раза в час из каждого из 3 расположений). Выполнения монитора равномерно распределены в течение выбранного интервала. То есть для монитора, запускаемого из 3 расположений каждые 15 минут, выполнения запускаются с интервалом 5 минут.

Можно выбрать частоту каждые **5**, **10**, **15** или **30** минут; каждый **1**, **2** или **4** часа. Также можно настроить монитор для выполнения [**Только по запросу**](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполняйте синтетические мониторы по запросу из публичных или частных расположений."). Можно выбрать несколько глобальных расположений для выполнения браузерного монитора.

Обратите внимание: все публичные расположения Synthetic работают по координированному всемирному времени (UTC). Если скрипту монитора требуется местное время или часовой пояс, можно использовать [метод `api.getContext()`](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#retrieve-data "Узнайте о типах событий при записи браузерного clickpath-а.") и системные часы для реализации условной логики.

## Validate content

Для браузерных мониторов по одному URL эта вкладка отображается в настройках монитора и доступна только в режиме редактирования.

Для браузерных clickpath-ов можно настроить валидацию контента для каждого события на вкладке [**Recorded clickpath**](#recorded-clickpath) в настройках монитора. Также можно настроить валидацию в процессе [записи](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") для записанных или вручную добавленных событий clickpath-а.

Валидация контента помогает убедиться, что браузерный монитор загружает ожидаемый контент страницы или элемент. Валидации выполняются с помощью правил: нажмите **Add custom content validation** для определения правила.

В браузерных clickpath-ах валидация определяется для каждого события; для мониторов по одному URL, содержащих одно событие, валидация определяется для монитора в целом.

Валидация выполняется после следования всем редиректам, даже если первый ответ содержит HTML.

Можно валидировать по конкретному тексту на странице, конкретному элементу, тексту внутри элемента или тексту в DOM или любом ресурсе. Можно настроить прохождение или провал монитора/события на основе критериев валидации. Если критерии прохождения не выполнены (или критерии провала выполнены), монитор/событие завершается с ошибкой и выполнение прерывается.

![Validation criteria](https://dt-cdn.net/images/validationcriteria-505-c8d37c1f14.png)

Validation criteria

**Target window** определяет вкладку, в которой находится текст/элемент. `window[0]` — первая открытая вкладка, `window[1]` — вторая. Также может быть `window[N].frames[X]`, где `X` — номер `iframe` на вкладке `N`. Фреймы можно объединять в цепочки: `window[N].frames[X].frames[Y]` означает, что элементы находятся во фрейме `Y`, вложенном во фрейм `X` на вкладке `N`.

Также можно использовать плейсхолдер в значении **Target window**, например `window[0].frames[{index}]`, где `{index}` — переменная, определённая ранее с помощью метода `api.setValue()` в [событии JavaScript](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

Если валидация основана на видимом тексте (**contains text**), тексте в конкретном элементе (**contains text in element**) или разметке в DOM или ресурсе (**contains text in DOM or any resource**), нужно **Specify text** (регистр не учитывается). Значения плейсхолдеров заключайте в скобки, например `{email}`. Опционально текст можно задать как регулярное выражение (**Evaluate as regular expression**).

Если валидация ищет элемент (**contains element**) или текст в конкретном элементе (**contains text in element**), нужно указать CSS-селекторы или DOM-локаторы для воспроизведения: нажмите **Add locator**, выберите **DOM** или **CSS** и укажите ссылку на локатор. При вставке строки локатора удалите символы `>`.

Можно добавлять и менять порядок любого количества локаторов. Валидация выполняется в заданном порядке до совпадения локатора.

Можно добавлять и менять порядок нескольких валидаций для события/монитора. Валидация выполняется в заданном порядке; при нарушении любого правила монитор завершается с ошибкой.

![Validation rules](https://dt-cdn.net/images/multiplevalidationrules1-1018-cd40d6f038.jpg)

Validation rules

Пример 1 — Валидация контента по видимому тексту

Выберите **contains visible text** и укажите искомый текст (регистр не учитывается). Этот текст должен быть виден на веб-странице. Определите, должен ли монитор проваливаться или проходить на основе введённого текста. В примере ниже монитор настроен на провал, если найден текст из [плейсхолдера](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.") (указанного ранее в скрипте).

![Text validation](https://dt-cdn.net/images/bm-validation-visible-text-1077-bc4cd9ebad.png)

Text validation

Пример 2 — Валидация контента по элементу

Выберите **contains element**. Нужно указать локатор для элемента, который хотите валидировать.

Для поиска локатора откройте инструменты разработчика для веб-страницы (правый клик > **Inspect**). Правый клик на нужном элементе > **Copy** > **Copy selector**. Вставьте **CSS**-селектор, удалив символы `>`.

Пример ниже показывает правило валидации на основе наличия элемента.

![Validate element by locator](https://dt-cdn.net/images/bm-validation-element-1061-f83021f60d.png)

Validate element by locator

Пример 3 — Валидация контента по тексту в элементе

Выберите **contains text in element**. Помимо текстовой строки для поиска, нужно указать локатор для элемента, содержащего текст. Строка не обязана быть видимой на странице, но должна быть частью текста между открывающим и закрывающим тегами элемента; строка не может содержать имена или значения атрибутов.

Для поиска локатора откройте инструменты разработчика. Правый клик на нужном элементе > **Copy** > **Copy selector**. Вставьте **CSS**-селектор, удалив символы `>`.

На скриншотах ниже показан конкретный элемент, содержащий текст `Mozilla`, в инструментах разработчика и соответствующее правило валидации в браузерном мониторе.

![Inspect text in an element](https://dt-cdn.net/images/bm-validation-text-in-element-1596-19b95e6ffd.png)

Inspect text in an element

![Validate text in an element](https://dt-cdn.net/images/bm-validation-text-in-element2-1056-52fc79316b.png)

Validate text in an element

Пример 4 — Валидация контента по тексту в DOM или ресурсе

Выберите **contains text in DOM or any resource** для валидации контента по любой строке в DOM, включая комментарии, имена и значения атрибутов.

Для поиска строки откройте инструменты разработчика. Скопируйте нужный текст и вставьте его в правило валидации.

На скриншотах ниже показаны атрибут и значение для URL назначения (`href="/en-US/firefox/browsers/"`) в DOM. Выбранная строка используется как текст валидации для браузерного монитора.

![Validate any text in DOM](https://dt-cdn.net/images/bm-validation-dom-text-986-d047d350a2.png)

Validate any text in DOM

![Validation rule for text in DOM](https://dt-cdn.net/images/bm-validation-dom-text2-1061-e185f50d1a.png)

Validation rule for text in DOM

Здесь можно воспроизвести браузерный монитор по одному URL (**Play back monitor**). Подробнее о [локальном воспроизведении](#recorded-clickpath) выше.

## Outage handling

Настройки обработки сбоев определяют действия при сбоях монитора (сбои доступности). Поведение обработки сбоев по умолчанию можно задать на уровне окружения для всех браузерных мониторов или всех HTTP-мониторов: перейдите в **Settings** > **Web and mobile monitoring** и выберите соответствующую вкладку **Outage handling**. Можно использовать значения по умолчанию Dynatrace (**Use defaults**) для определения обработки сбоев на уровне окружения. При включении эти значения применяются ко всем браузерным или HTTP-мониторам, не переопределяющим их настройками уровня монитора.

На уровне монитора этот параметр доступен только в режиме редактирования. Параметры обработки сбоев на уровне окружения и монитора одинаковы. Можно переопределить значения по умолчанию на уровне монитора. Также можно восстановить значения уровня окружения (**Remove override**).

Можно отключить генерацию проблем для глобальных и локальных сбоев, если тестируете нестабильный сайт или запланированы простои, о которых не нужно получать оповещения.

* **Generate a problem and send an alert when this monitor is unavailable at all configured locations**

  Этот параметр включён по умолчанию для новых мониторов. Он оповещает о глобальных сбоях доступности: когда все расположения одновременно фиксируют сбой.

  По умолчанию проблема глобального сбоя создаётся при однократном сбое всех расположений. Однако можно указать количество последовательных сбоев (от 1 до 5) для создания проблемы глобального сбоя.
* **Generate a problem and send an alert when this monitor is unavailable for one or more consecutive runs at any location**

  Позволяет создавать проблему при последовательных сбоях в одном или нескольких расположениях. На уровне окружения можно выбрать количество сбоев. На уровне монитора можно также определить количество расположений, которые должны зафиксировать сбой для создания проблемы локального сбоя.

  В примере ниже монитор настроен для `4` расположений, и проблема создаётся, если `3` из `4` расположений не могут получить доступ к сайту в течение `2` или более последовательных выполнений.

* **Automatic retry on error**

  При включении этого параметра (включён по умолчанию) браузерные мониторы по одному URL и clickpath-ы автоматически повторяются из того же расположения при ошибках. При последующем успехе первоначальная точка данных об ошибке удаляется. Такой подход снижает количество ложноположительных ошибок.

  Повторная попытка выполняется независимо от пороговых значений доступности. Повторная попытка не потребляет дополнительные DEM Units.

  Возможно, потребуется отключить повторные попытки при расследовании проблем, которые повторные попытки могут маскировать. При отключении повторных попыток каждый сбой монитора засчитывается в сбой доступности.

![Outage handling](https://dt-cdn.net/images/outagebrowser-912-b097cf6dcf.png)

Outage handling

Проблема сбоя разрешается, когда происходит столько же последовательных успешных выполнений, сколько настроено неуспешных для создания проблемы. Успешные выполнения должны произойти в количестве расположений = общее количество расположений минус количество расположений, необходимых для проблемы, плюс 1.

Обратите внимание: при разрешении проблемы глобального сбоя в одном или нескольких расположениях всё ещё могут происходить сбои мониторов. Настройте правила локального сбоя для получения оповещений об этом.

Дополнительную информацию о [Расчётах Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Узнайте о расчётах метрик Synthetic Monitoring.") см. в разделах:

* Разница между [разрешением сбоя и тайм-аутом](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#availability-problems "Узнайте о расчётах метрик Synthetic Monitoring.").
* [Исключение выполнений синтетического монитора в окна обслуживания из расчётов доступности](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Узнайте о расчётах метрик Synthetic Monitoring.").

## Performance thresholds

Этот параметр доступен только в режиме редактирования.

Пороговые значения производительности позволяют проактивно реагировать на задержки сайта.

Нажмите **Add threshold**. Для clickpath-ов можно задать пороговое значение для монитора в целом (**Total duration of all events**) и/или для отдельных событий. Обратите внимание: можно выбирать только события, генерирующие сетевую активность. Для браузерных мониторов по одному URL можно задать пороговое значение только для монитора в целом.

![Select an action for performance thresholds](https://dt-cdn.net/images/selectactionperfthreshold-616-a67b623c23.png)

Select an action for performance thresholds

Отображается среднее значение производительности за последние 24 часа для помощи в установке порога. Просто введите **Threshold in seconds** и нажмите **Save**. Можно задать несколько пороговых значений производительности.

![Set a performance threshold](https://dt-cdn.net/images/setperfthreshold1-520-e72b94612b.png)

Set a performance threshold

Пороговые значения производительности можно удалять или редактировать в любое время.

Пороговые значения производительности определяются как **Total duration** монитора или отдельных событий, которые, в свою очередь, могут включать несколько load или XHR actions. (Total duration недоступна как метрика для отдельных load или XHR actions при просмотре [Multidimensional analysis](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов.") или [графика водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов.").)

![Performance thresholds](https://dt-cdn.net/images/performancethresholds1-915-98e1ae390c.png)

Performance thresholds

Dynatrace создаёт проблему производительности, если монитор в данном расположении нарушает **любое** из заданных пороговых значений в 3 из 5 последних выполнений, если только для монитора не открыто окно обслуживания. Нарушения должны происходить в одном расположении. Несколько расположений могут иметь такие нарушения и включаться в одну проблему.

Проблема закрывается, если пороговые значения не нарушаются в 5 последних выполнениях в каждом из ранее затронутых расположений.

Дополнительную информацию см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#performance-problems "Узнайте о расчётах метрик Synthetic Monitoring.").

## Monitor script

Эта вкладка отображается для браузерных мониторов по одному URL и содержит код скрипта монитора в формате JSON. Скрипт можно редактировать напрямую в веб-интерфейсе Dynatrace или **Download** для редактирования в текстовом редакторе. Подробности см. в разделе [Script mode для настройки браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте и редактируйте браузерные мониторы в формате JSON.").

## Advanced setup

На этой вкладке расположены элементы управления для:

* [Аутентификации при входе](#login-authentication) (только для браузерных мониторов по одному URL)
* [Аутентификации по сертификату](#certificate-authentication)
* [HTTP-заголовков](#http-headers)
* [Блокировки запросов](#block-requests)
* [Игнорирования кодов состояния](#ignore-status-codes)
* [Куков](#cookies)
* [Обхода правил CSP](#bypass-csp)
* [Захвата метрик для страниц в фреймах](#performance-frames)
* [Использования устаревших JavaScript-фреймворков](#deprecated-js)

При создании браузерных мониторов по одному URL или clickpath-ов эти элементы управления перечислены как **Additional options** для настройки монитора.

### Enable global login authentication

Dynatrace упрощает автоматический вход на страницы, защищённые паролем. Это реализуется с помощью технологии Dynatrace LoginSense, обеспечивающей интеллектуальный и безопасный вход в веб-приложение при каждом выполнении браузерного монитора.

#### Браузерные мониторы по одному URL

При первоначальной настройке монитора по одному URL можно выбрать **Enable global login authentication** и выбрать между методами **HTTP authentication** и **Kerberos authentication**. В режиме редактирования этот параметр доступен для мониторов по одному URL в разделе **Advanced setup**. Подробности см. в разделе [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#http-single-page "Узнайте, как настроить методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring.").

##### Аутентификация через веб-форму

Устарело

Аутентификация через веб-форму больше не поддерживается для браузерных мониторов по одному URL. Вместо этого создайте [браузерный clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") для сценариев, требующих веб-формы входа. Ранее настроенные мониторы по одному URL продолжат работу, однако рекомендуется перезаписать их как clickpath-ы, чтобы чётко разделить каждый шаг входа.

Перезапись обязательна, если вы хотите изменить любую часть настроек монитора. Сохранить изменения в текущем формате больше нельзя.

Начиная с Dynatrace версии 1.324+, мониторы по одному URL с формой входа будут автоматически обновлены путём добавления бесплатного шага JavaScript для поддержки процесса входа.

#### Записанные браузерные clickpath-ы

При первоначальной настройке браузерного clickpath-а **Enable global login authentication** не поддерживается для записи.

Для браузерных clickpath-ов аутентификация при входе не отображается в **Advanced setup** в режиме редактирования.

* Для **аутентификации через веб-форму** можно просто записать ввод учётных данных в веб-форму. Позже можно отредактировать clickpath для использования учётных данных из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").
* Для **HTTP-based схем аутентификации** нужно вручную ввести имя пользователя и пароль в собственном диалоге браузера при записи clickpath-а. Затем в [событии Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") записанного clickpath-а в режиме редактирования включите **Enable HTTP authentication**.

Дополнительную информацию см. в разделе [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Узнайте, как настроить методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring.").

#### Использование учётных данных из хранилища

Можно выбрать существующий credential (**Select credentials**). В списке отображаются только доступные вам учётные данные: публичные или только для владельца, созданные вами.

![Credentials in the credential vault](https://dt-cdn.net/images/screenshot-2025-08-18-175320-652-bb35409fa6.png)

Credentials in the credential vault

Можно **Create new credentials**, введя **Username** и **Password**. Укажите имя для credential и нажмите **Save to vault**. Учётные данные, созданные таким образом, автоматически получают разрешения только для владельца.

Для создания учётных данных в script или UI mode в браузерном мониторе таким образом необходимо иметь [разрешение на доступ к хранилищу учётных данных](/managed/manage/credential-vault#access-cv "Храните и управляйте учётными данными в хранилище."). Всегда можно захватить введённые учётные данные как часть записанного clickpath-а.

Кто может редактировать монитор с учётными данными?

* Если монитор связан с публичным credential, любой член команды может включать/выключать, удалять или редактировать монитор.

* Если браузерный монитор (clickpath или по одному URL) связан с ограниченным credential (только для владельца или для нескольких пользователей), любой пользователь может менять определённые поля, даже без доступа к используемому credential. Можно редактировать имя монитора, настройки эмуляции устройства, условия ожидания, частоту, расположения, оповещения о сбоях, пороговые значения производительности, метрики, связанные приложения, валидацию и игнорируемые HTTP-коды состояния. Также можно менять токен или credential типа user ID/password. Можно создать credential в настройках монитора в режиме редактирования. Нужно будет заменить все учётные данные в мониторе на доступные вам. Замена credential другого пользователя на доступный вам необратима.

  Элементы управления, которые нельзя редактировать, такие как URL, включение/выключение HTTP-аутентификации, добавление или удаление событий clickpath-а, ввод данных в Keystroke и **Advanced setup** в настройках монитора, будут неактивными или отображать сообщение об ошибке при попытке сохранить изменения в script или UI mode.

* Можно включать/выключать или удалять синтетический монитор, защищённый owner-only credential другого пользователя.

Подробнее о разрешениях на учётные данные в разделе [Хранилище учётных данных для синтетических мониторов](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").

### Use client certificates

Dynatrace версии 1.272+

ActiveGate версии 1.271+

Можно настроить аутентификацию по сертификату для браузерных мониторов, выполняемых из любого [публичного расположения](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.") и [частных расположений](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") с Linux-based ActiveGate ([контейнеризированными](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Разворачивайте и управляйте контейнеризированными, автомасштабируемыми частными расположениями Synthetic на Kubernetes/RedHat OpenShift.") и неконтейнеризированными). Этот элемент управления доступен в режиме редактирования для браузерных мониторов по одному URL и clickpath-ов.

Перед записью clickpath-а на сайте, требующем аутентификации по сертификату, убедитесь, что нужный сертификат установлен в браузере. При переходе к сайту в окне записи собственный диалог браузера выберет правильный сертификат.

Если хотя бы один сертификат в цепочке истёк, вся цепочка может быть отклонена, что приводит к сбою выполнений монитора. Результаты могут отличаться при использовании той же цепочки сертификатов с HTTP-монитором или при ручном выполнении команды curl на хосте.

После записи clickpath-а нужно указать сертификат для выполнения браузерного монитора в **Advanced setup** в режиме редактирования.

1. Откройте вкладку **Advanced setup** в настройках браузерного монитора.
2. Включите **Use client certificates**.
3. Нажмите **Add client certificate**.
4. Введите **Domain**, для которого действителен сертификат.
5. Выберите сертификат из списка сертификатных учётных данных. Или нажмите **Create new credential**, чтобы загрузить и использовать новый клиентский сертификат. Любой созданный сертификатный credential автоматически помечается как [только для владельца](/managed/manage/credential-vault#work-with-credentials "Храните и управляйте учётными данными в хранилище.") и сохраняется в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").

   Можно загрузить файлы сертификатов в формате PFX, P12 или PEM.

   ![Certificate authentication setting for browser monitors](https://dt-cdn.net/images/bm-client-certificates-788-4347c846d7.png)

   Certificate authentication setting for browser monitors
6. Нажмите **Add entry**.
7. Повторите эти шаги для добавления нескольких сертификатов. Каждый сертификат должен быть привязан к одному домену.
8. **Save changes**.

### Enable additional HTTP headers

Монитор создаётся с минимальным набором заголовков, требуемых протоколом. Для включения пользовательских заголовков:

1. Выберите **Enable additional HTTP headers**.
2. Введите имя (**Header**) и значение (**Value**).
3. Нажмите **Add another header** при необходимости.

Можно задать несколько HTTP-заголовков. Они будут применяться ко всем запросам монитора.

Чтобы задать заголовки только для конкретных запросов, установите флажок **Only apply headers to requests matching a pattern** и определите **Pattern**. После этого заголовок применяется только к запросам, соответствующим шаблону.

![HTTP headers](https://dt-cdn.net/images/enablehttpheaders-481-88d1794c8b.jpg)

HTTP headers

### Block specific requests

Можно заблокировать один или несколько запросов, указав полные URL или шаблоны. URL или строка regex не должны превышать 90 символов, регистр не учитывается.

Блокировка запросов позволяет анализировать их влияние на производительность приложения и оптимизировать его.

Включите **Block specific requests**. Затем можно указать полный URL, как показано ниже.

![Block requests](https://dt-cdn.net/images/blockrequests-571-973bf40e24.jpg)

Block requests

Также можно определить шаблоны, например `http:*://*/*.png` или `https*://*/*.png` для блокировки всех запросов к PNG-изображениям.

Совпадающие запросы блокируются в течение всего выполнения монитора и не зависят от событий.

Если не удаётся заблокировать конкретные запросы, см. статью сообщества Dynatrace [Unable to block specific requests (owing to limitations on the length of regular expressions)](https://dt-url.net/w0i2xhk).

### Ignore specific status codes

Позволяет исключить HTTP-коды состояния 400–599 из причин сбоев доступности/ошибок при их встрече в запросе основного документа. Как правило, это базовая страница load action. Если этот параметр включён и базовая страница load action возвращает HTTP-ошибки 400–599, сбой доступности не создаётся.

Можно указать точный код состояния, диапазон или маску класса состояния. Для разделения нескольких значений используйте запятые; для диапазона используйте дефис (`-`) без пробелов, например `404, 405-410, 5xx`. Можно применить правило только к запросам документов, соответствующих конкретному регулярному выражению (**Only apply to document request matching this regex**).

* Этот параметр не применяется к XHR-запросам или запросам документов в iframes; браузерные мониторы не завершаются с ошибкой при сбое XHR-запроса или запроса документа в iframe.
* Этот параметр применяется к будущим выполнениям, то есть выполнениям после включения параметра.

### Set cookies

Куки позволяют хранить информацию о состоянии браузера на стороне клиента, чтобы каждое выполнение монитора основывалось на одном состоянии и можно было точно отслеживать базовую производительность.

Куки можно задавать в **Additional options** при создании браузерного монитора или в **Advanced setup** в режиме редактирования. Эти куки действительны в течение всего выполнения монитора. Для установки куков только для конкретной части clickpath-а используйте событие Cookie.

В режиме редактирования включите **Set cookies**, затем укажите **Name** и **Value** кука. Каждый кук должен быть уникальным в списке.

Следующие символы не допускаются в значении кука: `;,\"`. Укажите **Domain** кука и, при желании, **Path** к куку. **Save** кук.

Нажмите **Add cookie** для определения дополнительных куков.

![Cookies in browser monitors](https://dt-cdn.net/images/setcookies-1362-458e753377.jpg)

Cookies in browser monitors

### Bypass Content Security Policy (CSP) of monitored page

Если настроена Content Security Policy, она, скорее всего, будет препятствовать отправке браузером данных мониторинга в Dynatrace Cluster. В качестве первого и предпочтительного метода обхода CSP отслеживаемых страниц в браузерном мониторе по одному URL или clickpath-е включите этот параметр.

Если по какой-то причине использовать этот параметр невозможно, см. расширенные решения в статье сообщества Dynatrace [Browser monitors: Issues with Content Security Policy](https://dt-url.net/ycs2x56).

### Capture performance metrics for pages loaded in frames

Включите этот переключатель для захвата данных производительности страниц в iframes или framesets. Итоговый [график водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов.") для [действия](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.") будет содержать результаты для каждого фрейма. Можно выбрать страницу для просмотра данных водопада.

### Enable using deprecated JavaScript frameworks

Начиная с Dynatrace версии 1.266+, поддержка некоторых JavaScript-фреймворков прекращена. Включите этот переключатель для использования этих устаревших фреймворков для непрерывности мониторов и скриптов.

Устаревшие фреймворки включаются в разделе **JavaScript framework support** в **Advanced setup**.

![Enabled deprecated JS frameworks](https://dt-cdn.net/images/bm-js-frameworks-2489-252f0042fb.jpg)

Enabled deprecated JS frameworks

Выберите **Use default** для использования значения этого параметра по умолчанию для окружения мониторинга Dynatrace. Обратите внимание: изменить значение по умолчанию можно только обратившись в службу поддержки.

![Enable support for deprecated JS frameworks](https://dt-cdn.net/images/bm-deprecated-js-toggle-740-950dc00038.png)

Enable support for deprecated JS frameworks

В script mode параметр `"useIESupportedAgent": true` включает поддержку устаревших JavaScript-фреймворков; при значении `false` параметр не отображается в скрипте браузерного монитора, и любые настройки включения устаревших фреймворков (`javaScriptFrameworkSupport`) игнорируются.

## Metrics

Dynatrace Synthetic Monitoring позволяет сохранять настройки метрик (фильтры и факторы разбивки) как [вычисляемые метрики](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#calculated-metrics "Узнайте, как анализировать точки данных браузерных мониторов.") и отслеживать их производительность в течение [длительного периода](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Проверьте сроки хранения данных для различных типов данных."). На этой вкладке отображаются все вычисляемые метрики для монитора и количество вычисляемых метрик для всего окружения мониторинга. Настройки на этой вкладке доступны только в режиме редактирования.

Разверните метрику для просмотра деталей. Можно отключать/включать, удалять или создавать пользовательские графики и оповещения на основе вычисляемой метрики. Изменить имя, ключ или конфигурацию метрики после создания нельзя, однако можно выбрать, отображать ли факторы разбивки в пользовательских графиках на основе метрики.

![Metrics tab](https://dt-cdn.net/images/metricstab-1668-02913a6de4.png)

Metrics tab