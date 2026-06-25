---
title: События браузерных clickpath-ов
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events
scraped: 2026-05-12T11:31:56.001733
---

# События браузерных clickpath-ов

# События браузерных clickpath-ов

* Explanation
* 18-min read
* Updated on Feb 11, 2026

При записи [браузерного clickpath-а](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") взаимодействия с веб-приложением захватываются как серия событий. Существуют различные типы событий для имитации взаимодействия и управления clickpath-ом: переход по URL, клик, выбор опции, ввод данных или фрагмент JavaScript. Помимо типа, события обладают различными свойствами: цель (набор локаторов для идентификации веб-элементов на странице) и стратегия ожидания.

Типы событий браузерного clickpath-а и их свойства описаны ниже. События clickpath-а можно редактировать при первоначальной [настройке](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") или в любое время позже в режиме редактирования в настройках монитора (см. изображения ниже). Можно редактировать, изменять порядок, удалять и добавлять события.

![Clickpath events during recording workflow](https://dt-cdn.net/images/recordedclickath1-1031-d78914d312.png)

Clickpath events during recording workflow

![Clickpath events in edit mode](https://dt-cdn.net/images/recordedclickpath-1294-6483cd8f2e.png)

Clickpath events in edit mode

Событие скрипта Synthetic — это не то же самое, что действие: только события, генерирующие веб-запросы, содержат одно или несколько действий. Карточка [Synthetic events and actions](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#events-actions "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") на странице Synthetic details помогает различать события скрипта с таймингами и без. Synthetic actions (аналогичные [действиям пользователя](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое действия пользователя и как они помогают понять, что делают пользователи с приложением.") в Real User Monitoring) содержат данные производительности, собранные в ходе выполнений clickpath-а.

## Navigate

Событие Navigate имитирует ввод **URL** в адресную строку браузера и загрузку страницы.

Браузерные мониторы по одному URL состоят из одного события Navigate. Обратите внимание: выбор аутентификации через веб-форму автоматически настраивает монитор по одному URL с двумя событиями скрипта: Navigate и нередактируемым событием AutoLogin.

Для повышения безопасности синтетических мониторов Dynatrace блокирует отправку мониторами запросов на локальный хост (например, `localhost` или `127.0.0.1`).

В [записанных clickpath-ах](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") первое событие автоматически создаётся как событие Navigate. Однако при добавлении событий вручную или редактировании clickpath-а можно добавить [событие JavaScript](#javascript) как первое событие монитора. События Navigate могут предшествовать только одно или несколько событий JavaScript. Clickpath требует хотя бы одного события Navigate.

При полной перезаписи clickpath-а (**Record again** > **From the beginning of the clickpath**) все события JavaScript, предшествующие первому событию Navigate, будут удалены. Сохранить начальные JavaScript-события можно, выбрав запись после них (**After event** > **Select event**).

Переход на новую веб-страницу путём клика по ссылке на текущей странице создаёт [событие Click](#click) в профилях десктопа (или [событие Tap](#tap) на мобильных устройствах), а не Navigate.

См. разделы ниже о [ожидании](#wait) и [валидации](#validate).

### HTTP-аутентификация

Для браузерных clickpath-ов можно автоматизировать вход по указанному URL с использованием HTTP-based аутентификации: включите **Enable HTTP authentication**. Поддерживаемые методы: basic, digest, NTLM и Negotiate.

Для аутентификации через веб-форму в clickpath-е можно просто записать ввод учётных данных; Dynatrace автоматически их захватывает. После записи можно сохранить учётные данные в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") для автоматизации входа при выполнениях монитора — подробности см. в разделе [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Узнайте, как настроить методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring."). Информацию о записи ввода данных, включая учётные данные, в поля см. в разделе [событие Keystroke](#keystroke).

Dynatrace хранит все учётные данные Synthetic Monitoring в хранилище и управляет ими. Доступ к учётным данным контролируется; они могут быть только для владельца или публичными.

Можно выбрать существующий credential (**Select credentials**). В списке отображаются только доступные вам учётные данные: публичные или только для владельца, созданные вами.

Браузерные мониторы поддерживают имена пользователей в форматах `<username>` и `<domain>\<username>`.

![Navigate event HTTP authentication](https://dt-cdn.net/images/navigatehttpauthentication-652-d4048163be.png)

Navigate event HTTP authentication

Можно **Create new credentials**, введя **Username** и **Password**. Укажите имя для credential и нажмите **Save to vault**. Учётные данные, созданные таким образом, автоматически получают разрешения только для владельца.

Для создания учётных данных в script или UI mode необходимо иметь [разрешение на доступ к хранилищу учётных данных](/managed/manage/credential-vault#access-cv "Храните и управляйте учётными данными в хранилище."). Всегда можно захватить введённые учётные данные как часть записанного clickpath-а.

Кто может редактировать монитор с учётными данными?

* Если монитор связан с публичным credential, любой член команды может включать/выключать, удалять или редактировать монитор.

* Если браузерный монитор (clickpath или по одному URL) связан с ограниченным credential (только для владельца или для нескольких пользователей), любой пользователь может менять определённые поля, даже без доступа к используемому credential. Можно редактировать имя монитора, настройки эмуляции устройства, условия ожидания, частоту, расположения, оповещения о сбоях, пороговые значения производительности, метрики, связанные приложения, валидацию и игнорируемые HTTP-коды состояния. Также можно менять токен или credential типа user ID/password. Можно создать credential в настройках монитора в режиме редактирования. Нужно будет заменить все учётные данные в мониторе на доступные вам. Замена credential другого пользователя на доступный вам необратима.

  Элементы управления, которые нельзя редактировать, такие как URL, включение/выключение HTTP-аутентификации, добавление или удаление событий clickpath-а, ввод данных в Keystroke и **Advanced setup** в настройках монитора, будут неактивными или отображать сообщение об ошибке при попытке сохранить изменения в script или UI mode.

* Можно включать/выключать или удалять синтетический монитор, защищённый owner-only credential другого пользователя.

Подробнее о разрешениях на учётные данные в разделе [Хранилище учётных данных для синтетических мониторов](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").

## Click

В браузерных мониторах событие Click определяет место клика мышью на странице. Вставляется при клике на элемент, например ссылку, кнопку или поле.

См. разделы ниже о [ожидании](#wait) и [валидации](#validate).

Событие Click взаимодействует с конкретным элементом веб-страницы. Информация об определении элемента через [локаторы](#locators) — ниже.

## Tap

В профилях мобильных устройств (включая планшеты, ноутбуки с сенсорным экраном и пользовательские устройства, заданные как мобильные) событие Tap определяет место нажатия на экран пальцем. Например, Tap вставляется при нажатии на гиперссылку, кнопку или выборе поля.

При записи на профилях мобильных устройств курсор меняется на значок, представляющий кончик пальца.

![Mobile cursor](https://dt-cdn.net/images/mobilecursor1-500-b19cbb7194.png)

Mobile cursor

См. разделы ниже о [ожидании](#wait) и [валидации](#validate).

Событие Tap взаимодействует с конкретным элементом на экране. Информация об определении элемента через [локаторы](#locators) — ниже.

## Keystroke

Событие Keystroke захватывает строку, введённую в поле на веб-странице.

* Строка записывается в **Text value** и может редактироваться. По умолчанию весь текст захватывается как **Plain text**. Однако для паролей, сохранённых в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище."), тип текста — **Credentials**.

  Dynatrace хранит все учётные данные Synthetic Monitoring в хранилище и управляет ими. Доступ к учётным данным контролируется; они могут быть только для владельца или публичными.

  Ниже см. информацию о [захвате или установке пароля](#keystroke-cv) и [создании токена](#keystroke-token) в событии Keystroke.

  Кто может редактировать монитор с учётными данными?

  + Если монитор связан с публичным credential, любой член команды может включать/выключать, удалять или редактировать монитор.

  + Если браузерный монитор (clickpath или по одному URL) связан с ограниченным credential (только для владельца или для нескольких пользователей), любой пользователь может менять определённые поля, даже без доступа к используемому credential. Можно редактировать имя монитора, настройки эмуляции устройства, условия ожидания, частоту, расположения, оповещения о сбоях, пороговые значения производительности, метрики, связанные приложения, валидацию и игнорируемые HTTP-коды состояния. Также можно менять токен или credential типа user ID/password. Можно создать credential в настройках монитора в режиме редактирования. Нужно будет заменить все учётные данные в мониторе на доступные вам. Замена credential другого пользователя на доступный вам необратима.

    Элементы управления, которые нельзя редактировать, такие как URL, включение/выключение HTTP-аутентификации, добавление или удаление событий clickpath-а, ввод данных в Keystroke и **Advanced setup** в настройках монитора, будут неактивными или отображать сообщение об ошибке при попытке сохранить изменения в script или UI mode.

  + Можно включать/выключать или удалять синтетический монитор, защищённый owner-only credential другого пользователя.

  Подробнее о разрешениях на учётные данные в разделе [Хранилище учётных данных для синтетических мониторов](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").
* **Simulate Return key** автоматически имитирует нажатие клавиши Return после ввода, например для отправки строки поиска или запуска входа. При создании монитора в UI mode это избавляет от необходимости настраивать событие Click после ввода данных в поле.
* **Simulate blur event** (включён по умолчанию) определяет, имитируется ли событие потери фокуса, обычно когда текстовое поле теряет фокус.
* См. разделы ниже о [ожидании](#wait) и [валидации](#validate).
* Событие Keystroke взаимодействует с конкретным элементом на экране, например полем формы. Информация об определении элемента через [локаторы](#locators) — ниже.

### Захват или установка пароля в Keystroke

В событии Keystroke записанный пароль по умолчанию захватывается как **Plain text**. Можно **Save to credential vault** — тип данных автоматически меняется на **Credentials**.

**Reset text value** нужно только для очистки захваченного credential и преобразования поля в незашифрованный текст.

![Captured password in Keystroke](https://dt-cdn.net/images/capturedpasswordkeystroke-600-dafd05b943.png)

Captured password in Keystroke

Также можно использовать другой credential из хранилища или создать новый в событии Keystroke. Сначала измените тип данных на **Credentials**.

Можно выбрать существующий credential (**Select credentials**). В списке отображаются только доступные вам учётные данные: публичные или только для владельца, созданные вами.

Можно выбирать пары user ID/password или токен-учётные данные. Обратите внимание на изображении ниже: используется только пароль из полученной пары UID/password.

![Retrieve credentials to Keystroke](https://dt-cdn.net/images/keystrokecv1-598-dbf81f321f.png)

Retrieve credentials to Keystroke

Можно **Create new credentials**, введя **Username** и **Password**. Укажите имя для credential и нажмите **Save to vault**. Учётные данные, созданные таким образом, автоматически получают разрешения только для владельца.

Для создания учётных данных в script или UI mode необходимо иметь [разрешение на доступ к хранилищу учётных данных](/managed/manage/credential-vault#access-cv "Храните и управляйте учётными данными в хранилище."). Всегда можно захватить введённые учётные данные как часть записанного clickpath-а.

![Create a credential in Keystroke](https://dt-cdn.net/images/keystrokecreatepwd-449-4c4c0be424.png)

Create a credential in Keystroke

### Создание токена в Keystroke

В Keystroke можно использовать существующий токен с доступом к нему. Измените тип текста на **Credentials** и выберите ID нужного credential (**Select credentials**).

Для создания нового токена нажмите **Create new credentials**. Выберите **Token** в поле **Credential type**. Отредактируйте имя credential по умолчанию, укажите значение **Token** и нажмите **Save to vault**. Учётные данные, созданные таким образом, автоматически получают разрешения только для владельца.

Для создания учётных данных в script или UI mode необходимо иметь [разрешение на доступ к хранилищу учётных данных](/managed/manage/credential-vault#access-cv "Храните и управляйте учётными данными в хранилище.").

![Create a token in Keystroke](https://dt-cdn.net/images/keystrokecreatetoken-451-f7460abf9c.png)

Create a token in Keystroke

## Select option

Событие Select option описывает использование списков в clickpath-е.

**Index** описывает позицию выбранного элемента сверху; первый элемент в списке всегда обозначается `0`. Поле **Value** показывает текстовое значение выбранного элемента.

Нажмите **Add another selection** для добавления ещё одного элемента выбора в том же списке. Выбранные опции можно удалять.

См. разделы ниже о [ожидании](#wait) и [валидации](#validate).

Событие Select option взаимодействует с конкретным элементом на экране. Информация об определении элемента через [локаторы](#locators) — ниже.

## JavaScript

Событие JavaScript позволяет выполнять фрагменты JavaScript как часть браузерных clickpath-ов.

С помощью событий JavaScript можно создавать clickpath-ы для сценариев с динамическими элементами, где необходимо реагировать на страницу, например:

* Потоки входа с случайными контрольными вопросами
* Сложные селекторы дат
* Страницы с A/B-тестированием
* Рабочие процессы регистрации или оформления заказа
* Пользовательские валидации

Выполнение JavaScript на **PDF**-страницах не поддерживается.

Для **XML**-страниц поддержку можно включить, переключившись в [script mode](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте и редактируйте браузерные мониторы в формате JSON.") и включив `experimentalProperties` в разделе `configuration` следующим образом. Значение `value` свойства `enableXmlInjection` — регулярное выражение для URL целевой XML-страницы.

```
"experimentalProperties": [{



"name": "enableXmlInjection",



"value": ".*.xml$"



}



]
```

При выполнении синтетического монитора целевая XML-страница отображается в HTML.

В предоставленном редакторе определите фрагмент JavaScript, целевое окно и стратегию ожидания. API для хранения и получения значений, управления результатом события JavaScript или пропуска выполнения [описан ниже](#javascript-event-api).

![JavaScript event](https://dt-cdn.net/images/clickpathjavascriptevent-1456-e850427051.png)

JavaScript event

При добавлении событий вручную или редактировании clickpath-а можно добавить событие JavaScript как первое событие монитора, например для получения credential из хранилища и установки переменной для использования в URL [события Navigate](#navigate). Эта функция требует ActiveGate версии 1.225 и браузера версии 88+ в [частных расположениях Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

События Navigate могут предшествовать только одно или несколько событий JavaScript; clickpath требует хотя бы одного события Navigate.

При полной перезаписи clickpath-а (**Record again** > **From the beginning of the clickpath**) все события JavaScript, предшествующие первому событию Navigate, будут удалены. Сохранить начальные JavaScript-события можно, выбрав запись после них (**After event** > **Select event**).

### API события JavaScript

Событие JavaScript предлагает базовый API для следующих операций.

#### Хранение и получение значений между событиями монитора

* `api.setValue(key, value)` — устанавливает `value` для `key`. Используйте отдельный вызов `api.setValue()` для каждой пары ключ-значение.
* `api.getValue(key)` — возвращает значение `key`, установленное ранее с помощью `api.setValue()`.
* `api.getValues()` — возвращает объект с парами ключ-значение, установленными ранее с помощью `api.setValue()`.

Переменные можно передавать только в контексте одного выполнения браузерного clickpath-а. Также нужно убедиться, что при обращении к переменной данные за ней логически доступны монитору.

После установки глобальной переменной с помощью метода `api.setValue()` можно применять её значение с помощью соглашения `{variable_name}` в `api.getValue()` или `api.getValues()`. Также значение можно применять в последующих полях конфигурации браузерного clickpath-а с помощью соглашения `{variable_name}`. Интерфейс сообщает, когда это возможно.

Имена переменных и ключей ограничены 100 символами. Значения глобальных переменных ограничены 5000 символами.

#### Отметка событий как неуспешных или завершённых

* `api.fail(message)` — отмечает запрос как неуспешный, указывая `message` в качестве причины, и отмечает выполнение монитора как неуспешное. `message` отображается как **Failure reason** для выполнения на [странице Multidimensional analysis](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."). Параметр `message` ограничен 200 символами.
* `api.finish()` — завершает событие JavaScript, после чего выполняется следующее событие.
* `api.startAsyncSyntheticEvent()` — заставляет событие JavaScript ждать последующего вызова `api.finish()` или `api.fail()` для завершения. Поскольку этот метод переопределяет условие ожидания, рекомендуется установить время ожидания **None**.

#### Пропуск событий clickpath-а

Эти методы пропускают события после завершения текущего события.

* `api.skipNextSyntheticEvent()` — пропускает выполнение следующего события.
* `api.skipNextSyntheticEvents(n)` — пропускает выполнение следующих `n` последовательных событий.
* `api.skipSyntheticEvent(eventIndex)` — пропускает выполнение события с индексом `eventIndex`. Нумерация событий начинается с `1` и совпадает с номерами событий в веб-интерфейсе.
* `api.skipSyntheticEvents(eventIndexes)` — пропускает выполнение нескольких событий; массив `eventIndexes` задаёт индексы пропускаемых событий, например `api.skipSyntheticEvents([8, 9])`.

#### Базовое логирование

* `api.info(message)` — записывает `message` с уровнем лога `info`.
* `api.warn(message)` — записывает `message` с уровнем лога `warning`.
* `api.error(message)` — записывает `message` с уровнем лога `error`.

Параметр `message` ограничен 200 символами. После локального воспроизведения логирование отображается внизу веб-интерфейса Dynatrace. Нажмите **Show full log**, как показано на изображении ниже. При выполнении мониторов из [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") строки лога (с префиксом `[CUSTOM]`) можно найти в файле выполнения VUC-теста.

![Log file for local playback](https://dt-cdn.net/images/clickpathplaybacklog-948-59c22d46d4.png)

Log file for local playback

#### Получение данных

* `api.getCredential(id, type)` — возвращает значение credential по ID (`id`) и типу (`type`): `username`, `password` или `token`. Необходимо указать точное значение одного из вариантов автодополнения для ID credential; динамические идентификаторы, например переменные, не поддерживаются. В списке только [credential с доступом](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище.").

  Требует ActiveGate версии 1.212+ для [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

  В качестве лучшей практики безопасности рекомендуется использовать только выделенные тестовые учётные данные для синтетических мониторов.
* `api.getContext().location`

  + `api.getContext().location.name` — возвращает имя частного или публичного расположения, из которого выполняется монитор. Полезно при применении условной логики, например для отображения локализованных страниц или использования разных данных входа для каждого расположения.
  + `api.getContext().location.cloudPlatform` — возвращает имя облачной платформы, на которой развёрнуто [публичное расположение Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.").

  При локальном воспроизведении свойства контекста не определены. Рекомендуется задать значение по умолчанию для этого сценария.

### Примеры

Пример 1 — Генерация и установка динамического email-адреса для мониторинга процесса регистрации.

```
var email = 'synthetic' + Date.now() + '@example.com';



api.setValue('email', email);



document.getElementById('email').value = email;
```

Пример 2 — Получение случайного имени/фамилии из API-эндпоинта и установка при регистрации.

```
api.startAsyncSyntheticEvent();



fetch('https://randomuser.me/api/').then((resp) => resp.json()).then(function(data) {



document.getElementById('firstName').value = data.results[0].name.first;



document.getElementById('lastName').value = data.results[0].name.lastname;



api.finish();



}).catch(function(error) {



api.fail('Fetch request to randomuser.me failed');



});
```

Пример 3 — Использование платформы облака для различия расположений с одним именем.

```
if (api.getContext().location.name === "Sydney" &&



api.getContext().location.cloudPlatform === "AWS") {



document.getElementById("linkAustraliaAWS").click();



}



if (api.getContext().location.name === "Sydney" &&



api.getContext().location.cloudPlatform === "Alibaba") {



document.getElementById("linkAustraliaAlibaba").click();



}
```

Пример 4 — Использование разного user ID в зависимости от расположения монитора.

В этом примере user ID устанавливается в событии JavaScript и сохраняется в глобальной переменной для последующего использования в скобках (`{}`) в поле или через вызов `api.getValue()`. Как альтернатива установке переменной для user ID можно вставить credential из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").

```
//Default value for the user ID in case a location not defined below is used



var userid_by_loc = "ValueDoesNotExist";



try {



//Get the location name



var loc = api.getContext().location.name;



api.info("Location Name is: " + loc);



//Get the cloud platform the location is hosted in



var platform = api.getContext().location.cloudPlatform;



api.info("Cloud Platform is: " + platform);



//Set the user ID per location



if ((loc.indexOf("Los Angeles") >= 0) && (platform.includes("Google Cloud") >= 0)) {



userid_by_loc = 'LA_User';



} else if ((loc.indexOf("Oregon") >= 0) && (platform.includes("Google Cloud") >= 0)) {



userid_by_loc = 'Oregon_User';



} else if ((loc.indexOf("Chicago") >= 0) && (platform.includes("Azure") >= 0)) {



userid_by_loc = 'Chicago_User';



}



} catch (err) {



api.info("Error message: " + err.description);



}



//Set a global variable to store the user ID that has been set and use later



api.setValue("UserID", userid_by_loc);
```

## Cookie

Куки позволяют хранить информацию о состоянии браузера на стороне клиента, чтобы каждое выполнение монитора основывалось на одном состоянии и можно было точно отслеживать базовую производительность.

Куки можно задавать в **Additional options** при создании браузерного монитора или в **Advanced setup** в режиме редактирования. Эти куки действительны в течение всего выполнения монитора. Для установки куков только для конкретной части clickpath-а используйте событие Cookie.

В режиме редактирования включите **Set cookies**, затем укажите **Name** и **Value** кука. Каждый кук должен быть уникальным в списке.

Следующие символы не допускаются в значении кука: `;,\"`. Укажите **Domain** кука и, при желании, **Path** к куку. **Save** кук.

Нажмите **Add cookie** для определения дополнительных куков.

![Cookie event](https://dt-cdn.net/images/cookieevent-954-16d16730f2.jpg)

Cookie event

## Общие элементы управления

В этом разделе описаны элементы управления, общие для нескольких типов событий.

### Время ожидания до запуска следующего события

Хотя Dynatrace автоматически выбирает подходящее время ожидания для каждого события, можно настроить этот параметр вручную.

* **None**
* **Wait for page to load completely** ждёт завершения сетевой активности после запуска события загрузки. Это время ожидания по умолчанию (60 секунд) для загрузки новой страницы.
* **Wait for specific period of time** позволяет указать количество секунд ожидания между этим и следующим событием.
* **Wait for background network activity to complete** ждёт завершения всей сетевой активности после события. Это время ожидания по умолчанию для XHR и взаимодействий в одностраничных приложениях.

  Этот параметр недоступен для событий Navigate.
* **Wait for specific element to appear** позволяет ждать появления конкретного HTML-элемента на странице, указывая CSS или DOM локатор. Также можно указать текст для валидации в элементе и тайм-аут для поиска.
* **Wait for next event** ждёт появления одного из локаторов следующего события. То же самое, что **Wait for specific element to appear**, но автоматически использует локаторы следующего события.

Убедитесь, что заданное время ожидания не превышает программные значения тайм-аутов для браузерных clickpath-ов (см. ниже). При превышении тайм-аутов создаётся проблема.

* Тайм-аут скрипта: `5 минут`
* Тайм-аут события: `60 секунд`

Эти тайм-ауты нельзя изменить в веб-интерфейсе Dynatrace. Однако можно использовать метод [PUT configuration](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration "Обновляйте конфигурацию Synthetic Monitoring через Synthetic API v2.") Synthetic configuration API v2 для изменения тайм-аутов браузерных мониторов во всём окружении. На изображении ниже показано событие Navigate после глобального изменения тайм-аута через API с 60 до 150 секунд.

![Changed event timeout](https://dt-cdn.net/images/bm-changed-timeouts-571-4002d1c791.png)

Changed event timeout

### Validate content

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

Выберите **contains element**. Нужно указать локатор для элемента.

Для поиска локатора откройте инструменты разработчика (правый клик > **Inspect**). Правый клик на нужном элементе > **Copy** > **Copy selector**. Вставьте **CSS**-селектор, удалив символы `>`.

Пример показывает правило валидации на основе наличия элемента.

![Validate element by locator](https://dt-cdn.net/images/bm-validation-element-1061-f83021f60d.png)

Validate element by locator

Пример 3 — Валидация контента по тексту в элементе

Выберите **contains text in element**. Помимо текстовой строки, нужно указать локатор для элемента. Строка не обязана быть видимой, но должна быть частью текста между тегами элемента; имена или значения атрибутов не допускаются.

Для поиска локатора откройте инструменты разработчика. Правый клик на нужном элементе > **Copy** > **Copy selector**. Вставьте **CSS**-селектор, удалив символы `>`.

На скриншотах показан элемент с текстом `Mozilla` в инструментах разработчика и соответствующее правило валидации.

![Inspect text in an element](https://dt-cdn.net/images/bm-validation-text-in-element-1596-19b95e6ffd.png)

Inspect text in an element

![Validate text in an element](https://dt-cdn.net/images/bm-validation-text-in-element2-1056-52fc79316b.png)

Validate text in an element

Пример 4 — Валидация контента по тексту в DOM или ресурсе

Выберите **contains text in DOM or any resource** для валидации по любой строке в DOM, включая комментарии, имена и значения атрибутов.

Для поиска строки откройте инструменты разработчика. Скопируйте нужный текст и вставьте его в правило валидации.

На скриншотах показаны атрибут и значение URL назначения в DOM. Выбранная строка используется как текст валидации.

![Validate any text in DOM](https://dt-cdn.net/images/bm-validation-dom-text-986-d047d350a2.png)

Validate any text in DOM

![Validation rule for text in DOM](https://dt-cdn.net/images/bm-validation-dom-text2-1061-e185f50d1a.png)

Validation rule for text in DOM

### Редактирование локаторов элементов

Этот элемент управления доступен в событиях [Click](#click), [Tap](#tap), [Keystroke](#keystroke) и [Select option](#select-option).

Когда одно из указанных событий clickpath-а нацелено на конкретный элемент веб-страницы, можно просматривать и редактировать локаторы элементов в формате DOM или CSS. Локаторы помогают Dynatrace идентифицировать элемент при воспроизведении. Может захватываться несколько локаторов для надёжного обнаружения элемента даже при изменении частей кода страницы. В большинстве случаев захватываются CSS-локаторы. Локаторы оцениваются последовательно; если первый не найден, оценивается второй и т.д.

Нажмите **Add locator**, выберите **DOM** или **CSS** и укажите ссылку на локатор. Информацию о формате DOM-локаторов см. в разделе [Формат DOM-локаторов](#dom-locators) ниже.

Можно добавлять любое количество локаторов. Также можно редактировать или удалять любые существующие локаторы.

**Target window** определяет вкладку, в которой находится текст/элемент. `window[0]` — первая открытая вкладка, `window[1]` — вторая. Также может быть `window[N].frames[X]`. Фреймы можно объединять в цепочки.

Также можно использовать плейсхолдер в значении **Target window**, например `window[0].frames[{index}]`, где `{index}` — переменная, определённая ранее с помощью метода `api.setValue()` в [событии JavaScript](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

![Element locators](https://dt-cdn.net/images/editelementlocators-953-6be1f79a8b.jpg)

Element locators

#### Формат DOM-локаторов

Dynatrace версии 1.292+

Для элементов можно настраивать расширенные пользовательские DOM-локаторы. Правила ниже определяют поддерживаемый формат при использовании JavaScript в DOM-локаторах для доступа к элементам веб-страницы. Эти правила обусловлены переходом Dynatrace Synthetic Recorder (расширения Google Chrome) на Manifest Version 3 (MV3) — последнюю версию платформы расширений Chrome.

* Для **идентификации элемента** можно выполнить одно из следующего.

  + Начать DOM-локатор с [`document.`](https://dt-url.net/vf02y15).

    ```
    document.forms[0][1].options[0]



    document.getElementById('adminusername')



    document.querySelector("body > div.vf-body-container > div > div > section > flows").shadowRoot.querySelectorAll("#postalTown")[1]
    ```

    Например, `document.getElementById('adminusername')` — это способ доступа к элементу по ID; `getElementById` — метод `document`.
  + Использовать допустимое имя глобальной JavaScript-переменной в начале DOM-локатора для прямого доступа к элементу по ID. Переменная должна содержать ссылку на элемент с соответствующим ID. Например, для элемента `<div id="EmailAddress"></div>` можно указать следующий DOM-локатор.

    ```
    EmailAddress
    ```
* **XPath-выражения поддерживаются**.

  DOM-локатор, начинающийся с `document.`, может содержать XPath-выражение в параметре `xpathExpression` [метода `evaluate()`](https://dt-url.net/9x22yb8). В примере ниже XPath-выражение: `'//form[@id=\\'ctl00\\']/div[4]/div[3]/span'`.

  ```
  document.evaluate('//form[@id=\\'ctl00\\']/div[4]/div[3]/span', document, null, XPathResult.ANY_TYPE, null).iterateNext()
  ```
* DOM-локатор **должен быть цепочкой (последовательностью) вызовов методов, свойств или индексных сигнатур**, как показано в примерах ниже.

  ```
  document.method().method1()



  document.method().prop['2565']



  document.method( 11 , 'erert','123')



  document.getElementById('deviceList').querySelectorAll('a')[0]
  ```
* **Аргументы вызова методов** могут быть любыми из следующих:

  + Строки в двойных или одинарных кавычках
  + Числа
  + `null`
  + `undefined`
  + `document`
  + [`XPathResult.*`](https://dt-url.net/kr42yx2)

  ```
  document.method("str1")



  document.method('str2', null)



  document.method(undefined, document)



  document.method(XPathResult.ANY_TYPE)
  ```
* **Вычисления JavaScript внутри DOM-локаторов не поддерживаются**.

  ```
  // Not supported



  document.forms[1+2]
  ```
* **Глобальные переменные JavaScript внутри DOM-локаторов не поддерживаются**.

  ```
  // Not supported, where someVar is a global variable



  document.querySelector(someVar)
  ```

## Связанные темы

* [Synthetic configuration API v2 - PUT configuration](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration "Обновляйте конфигурацию Synthetic Monitoring через Synthetic API v2.")