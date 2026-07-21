---
title: Настройка Real User Monitoring Classic для захвата XHR-действий
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions
---

# Настройка Real User Monitoring Classic для захвата XHR-действий

# Настройка Real User Monitoring Classic для захвата XHR-действий

* Практическое руководство
* 9 мин чтения
* Обновлено 29 апр. 2026 г.

Современные веб-приложения не полагаются на загрузку страниц для изменения UI после действий пользователя. Вместо этого каждое взаимодействие пользователя запускает один или несколько XHR-запросов для получения необходимых данных, изменяя тем самым только части UI. При включении поддержки XHR-действий добавляется видимость по каждому виду взаимодействия пользователя, а не только по обычным загрузкам страниц, которые захватываются по умолчанию. Эта опция значительно расширяет видимость в средах single-page application (SPA), построенных на различных JavaScript-фреймворках.

## Поддерживаемые JavaScript-фреймворки

Предлагается специальная поддержка для [Angular 2–16](#enable-angular-12-16-support). Для Angular 17+ [требуется дополнительная настройка](#enable-angular-17-support). Если для приложения используется другой JavaScript-фреймворк, попробуй [включить общую поддержку](#enable-generic-js-frameworks).

Окончание специальной поддержки для некоторых JavaScript-фреймворков

Специальная поддержка следующих JavaScript-фреймворков прекращена с выходом RUM JavaScript версии 1.265 и Dynatrace версии 1.266.

| JavaScript-фреймворки | Версии |
| --- | --- |
| AngularJS | 1.0 - 1.7 |
| Angular с SystemJS | 2 - 15 |
| Dojo | 1.6.1 - 1.13 |
| Ext JS | 3.4, 4, 5, 6 |
| ICEfaces | 1.8, 2, 3 |
| jQuery ( Backbone.js ) | 1.3 - 1.12, 2.0 - 2.2, 3.0 - 3.6 |
| MooTools | 1.4.5 - 1.6.0 |
| Prototype | 1.7 |
| Sencha Touch | 2.0 - 2.4 |

Если используется один из этих фреймворков, [включи общую поддержку](#enable-generic-js-frameworks).

Кроме того, если среда была создана до Dynatrace версии 1.266, можно использовать версию RUM JavaScript, которая предлагает специальную поддержку нужного фреймворка.

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Injection** > **RUM JavaScript updates**.
5. Выбери опцию **Latest IE7-10 supported** из выпадающего списка.

## Включение поддержки Angular 2–16

Если для приложения используется Angular 17+, следуй инструкциям в разделе [Включение поддержки Angular 17+](#enable-angular-17-support).

Чтобы включить поддержку Angular 2–16

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Capturing** > **Async web requests and SPAs**.
5. В разделе **JavaScript framework support** включи переключатель **Angular**.
6. Angular 12+ Введи имя пакета Angular.

   Что такое имя пакета Angular?

   Начиная с Angular версии 12, имя пакета Angular приложения нужно указывать в настройках Dynatrace. Иначе Real User Monitoring работать не будет.

   Для Angular 12 имя пакета зависит от имени проекта и больше не статично, тогда как для Angular 11 и более ранних версий имя пакета всегда `webpackjsonp`.

   Как найти имя пакета Angular для приложения

   1. Открой инструменты разработчика браузера и перейди на вкладку **Console**.
   2. Начни вводить `webpackChunk`. Браузер должен показать имя пакета для Angular-приложения. Скопируй это имя.  
      Например, имя пакета на скриншоте ниже, `webpackChunklite`.

      ![Поиск имени пакета Angular в консоли браузера](https://dt-cdn.net/images/find-angular-package-name-1918-f04cb24a1a.png)

      Поиск имени пакета Angular в консоли браузера

      Если в консоли отображается несколько записей `webpackChunk`, выбери ту, которая соответствует имени приложения. Также попробуй отключить расширения браузера, чтобы получить более чистый список.
      Если записей `webpackChunk` в консоли нет, вероятно, используется Angular версии 11 или более ранней. В этом случае имя пакета Angular указывать не нужно.
   3. Вставь имя, скопированное на шаге 2, в поле **Angular package name** в настройках приложения.

## Включение поддержки Angular 17+

Поскольку Angular 17 по умолчанию использует esbuild вместо Webpack, RUM JavaScript больше не может автоматически инструментировать Angular. По этой причине, если для приложения используется Angular 17+, обрати внимание, что требуется дополнительная настройка.

Чтобы включить поддержку Angular 17+, выполни следующие действия.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Включи общую поддержку JavaScript-фреймворков**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-config-web-ui "Разберись, зачем нужно включать поддержку определённых JavaScript-фреймворков для XHR-действий, и узнай, как настроить Real User Monitoring Classic для XHR-действий.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Реализуй захват исключений**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-exception-capture "Разберись, зачем нужно включать поддержку определённых JavaScript-фреймворков для XHR-действий, и узнай, как настроить Real User Monitoring Classic для XHR-действий.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настрой определение page group**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#angular-page-group-detection "Разберись, зачем нужно включать поддержку определённых JavaScript-фреймворков для XHR-действий, и узнай, как настроить Real User Monitoring Classic для XHR-действий.")

### Шаг 1. Включение общей поддержки JavaScript-фреймворков

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Capturing** > **Async web requests and SPAs**.
5. В разделе **JavaScript framework support** отключи переключатель **Angular**.
6. В разделе **Generic support** включи нужные опции.

   * Включи **Capture fetch() requests**, чтобы захватывать данные пользовательских действий для запросов на основе [Fetch API](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#fetch-api "Узнай, что такое пользовательские действия и как они помогают понять, что пользователи делают с приложением.").
   * Включи **Capture XmlHttpRequest (XHR)**, чтобы захватывать любое взаимодействие, приводящее к вызову XmlHttpRequest, как XHR-действие.

### Шаг 2. Реализация захвата исключений

В Angular есть обработчик исключений по умолчанию ([`ErrorHandler`﻿](https://angular.io/api/core/ErrorHandler)), который перехватывает исключения и записывает их в `console` с помощью `console.error`. Однако иногда для перехвата обработки ошибок используется пользовательский обработчик исключений.

#### Обработчик исключений по умолчанию

Если используется обработчик исключений по умолчанию, включи захват ошибок консоли, чтобы RUM JavaScript мог захватывать исключения для Angular 17+ приложений.

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Capturing** > **Custom configuration properties**.
5. Выбери **Add a custom configuration property** и введи `cce=1`.

   `cce` означает *capture console error* (захват ошибок консоли). Когда эта опция включена, RUM JavaScript сообщает о первом объекте `Error` или строке, которую он может найти в аргументах, переданных в `console.error`.

#### Пользовательский обработчик исключений

Если используется пользовательский обработчик исключений и исключения не записываются в `console`, о них нужно сообщать вручную.

```
export class CustomErrorHandler implements ErrorHandler {



handleError(error: any): void {



// Report the error



window.dtrum?.reportError(error);



// custom error handling



}



}



@NgModule({



...,



providers: [{provide: ErrorHandler, useClass: CustomErrorHandler}]



})
```

### Шаг 3. Настройка определения page group

Определение страниц и page group [по умолчанию](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/pages-and-pagegroups "Узнай, как использовать и определять страницы и page group в Dynatrace Real User Monitoring Classic.") основано на URL, а именно на путях и ID, которые Dynatrace определяет автоматически. Если готовая группировка страниц неверна или её нужно изменить, page group можно сообщать вручную с помощью Angular Router. Приведённый ниже пример кода можно использовать для получения page group из `routeConfig`, где ещё доступны имена-заполнители (например, `/journey/:id` вместо `/journey/1235`).

```
@NgModule({



imports: [RouterModule.forRoot(routes)],



exports: [RouterModule]



})



export class AppRoutingModule {



constructor(private router: Router) {



window.dtrum?.enableManualPageDetection();



this.router.events.subscribe((value: Event) => {



if (value.type === EventType.ActivationEnd) {



const snapshot = value.snapshot;



if (snapshot.routeConfig) {



const group = snapshot.routeConfig.path;



const name = snapshot.url.join("/");



window.dtrum?.setPage({



name,



group



});



}



}



});



}



}
```

См. также [Определение собственной группировки страниц](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/pages-and-pagegroups#configure-page-grouping "Узнай, как использовать и определять страницы и page group в Dynatrace Real User Monitoring Classic.").

### `dT_.initAngularNg()`

Не вызывать `dT_.initAngularNg()`, так как с Angular 17 он больше не работает. Сам вызов ничего не ломает, но и эффекта не даёт.

Для Angular 2–16 `dT_.initAngularNg` используется, чтобы передать объекты HTTP и Headers в Dynatrace при использовании `HttpModule` из @angular/http, либо чтобы передать объекты HTTP и HttpHeaders в Dynatrace при использовании `HttpClientModule` из @angular/common/http (Angular 5+).

## Включить общую поддержку JavaScript-фреймворков

Если приложение использует не Angular, а другой JavaScript-фреймворк, нужно включить общую поддержку для веб-запросов XHR и fetch().

1. Перейти в раздел **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Async web requests and SPAs**.
5. В разделе **Generic support** включить нужные опции:

   * Включить **Capture fetch() requests**, чтобы фиксировать данные пользовательских действий для запросов на основе [Fetch API](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#fetch-api "Learn what user actions are and how they help you understand what users do with your application.").
   * Включить **Capture XmlHttpRequest (XHR)**, чтобы фиксировать любое взаимодействие, приводящее к вызову XmlHttpRequest, как действие XHR.

## Включить поддержку отложенных действий

В зависимости от фреймворка XHR (AJAX) или архитектуры приложения может дополнительно потребоваться включить настройку поддержки отложенных действий. Эта настройка нужна, когда приложение не запускает вызовы XHR (AJAX) напрямую в обработчиках событий HTML-элементов, а откладывает их через вызовы `SetTimeout`.

1. Перейти в раздел **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Content capture**.
5. Включить **Timed action support**.

## Исключить отдельные вызовы XHR из мониторинга

Когда приложение отправляет запрос XHR или Fetch, он может фиксироваться одним из следующих способов:

* Если в данный момент не активно другое пользовательское действие и XHR был вызван взаимодействием пользователя, фиксируется отдельное действие XHR.
* Если в данный момент активно другое пользовательское действие и XHR не был вызван взаимодействием пользователя, активное пользовательское действие расширяется на длительность этого XHR.

Можно исключить отдельные вызовы XHR из мониторинга, например если приложение часто отправляет XHR-вызовы для проверки статуса, которые не нужны в пользовательских данных. При исключении таких запросов:

* Отдельные действия XHR не фиксируются.
* Исключённые XHR не продлевают длительность других пользовательских действий. Однако они всё же могут отображаться в [waterfall-анализе](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis."), если активна поддержка W3C resource timing (настройки приложения > **Capturing** > **Content capture** > **W3C resource timing support**).

### Настройка правил исключения XHR

Чтобы исключить вызовы XHR из мониторинга

1. Перейти в раздел **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Exclusions** > **XHR exclusions**.
5. Выбрать **Add an XHR exclusion rule** и указать регулярное выражение JavaScript, соответствующее URL запросов, которые нужно исключить.

Избегать неэффективных регулярных выражений

Неэффективные регулярные выражения могут вызывать проблемы с производительностью приложения, включая зависание браузера на несколько секунд. Для лучшей производительности стоит писать выражения, которые соответствуют подстроке URL, а не всему URL целиком. Это особенно актуально для длинных URL.

### Как применяются правила исключения XHR

RUM JavaScript проверяет регулярное выражение по URL с помощью [`RegExp.prototype.test()`﻿](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test). Регулярное выражение не обязано соответствовать полному URL, достаточно соответствия подстроке. URL может быть относительным или абсолютным, в зависимости от того, что было передано в вызов XHR или Fetch. Сопоставление не учитывает регистр, а прямые слэши (`/`) экранировать не нужно.

Сайты для тестирования регулярных выражений

При составлении регулярного выражения на сайте вроде [Regex101﻿](https://regex101.com/) нужно выбрать следующие параметры:

* Flavor **ECMAScript (JavaScript)**
* Разделитель `"`
* Флаг **Case insensitive match**

## Отсутствие действий XHR при использовании promise

При использовании [promise﻿](https://web.dev/promises/) Dynatrace не всегда создаёт пользовательские действия, поэтому можно заметить, что некоторые действия XHR отсутствуют.

Как Dynatrace обычно создаёт пользовательские действия:

1. Регистрируется взаимодействие пользователя со страницей, например клик, нажатие клавиши или событие прокрутки.
2. Если запрос XHR или fetch начинается в течение следующих 30 миллисекунд, создаётся пользовательское действие. Если запрос начинается позже, пользовательское действие не создаётся.

30-миллисекундный интервал продлевается неограниченно на время выполнения текущей синхронной операции, например, когда длительное вычисление в коде приложения занимает более 30 мс и XHR запускается только после завершения вычисления. Однако это применимо только в том случае, если выполнение происходит напрямую в обработчике события и не используются `setTimeout`, `setInterval` или promise.

При использовании promise код может выполняться асинхронно. По завершении выполнения кода исходный вызывающий код получает уведомление и может продолжить собственное выполнение. К сожалению, определить момент завершения выполнения кода невозможно: оно может уложиться в 30-миллисекундное окно, а может и нет. По этой причине в таких случаях рекомендуется использовать [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API.") для создания действий.

Чтобы проверить, использует ли пользовательское действие promise

1. Открыть инструменты разработчика браузера.
2. Выполнить действие в веб-приложении.
3. Проверить инициатора запроса.

   ![Check if a user action uses promises in browser's developer tools](https://dt-cdn.net/images/promise-then-2446-542a8c167e.png)

   Проверка, использует ли пользовательское действие promise, в инструментах разработчика браузера