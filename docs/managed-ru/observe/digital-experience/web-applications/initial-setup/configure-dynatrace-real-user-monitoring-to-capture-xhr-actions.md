---
title: Настройка Real User Monitoring для захвата XHR-действий
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions
scraped: 2026-05-12T11:34:19.573016
---

# Настройка Real User Monitoring для захвата XHR-действий

# Настройка Real User Monitoring для захвата XHR-действий

* How-to guide
* 9-min read
* Updated on Apr 29, 2026

Современные веб-приложения не зависят от загрузки страниц для изменения пользовательского интерфейса после ввода пользователя. Вместо этого каждое взаимодействие пользователя инициирует один или несколько XHR-запросов для получения необходимых данных, изменяя тем самым только части интерфейса. При активации поддержки XHR-действий обеспечивается видимость каждого типа взаимодействия пользователя, а не только обычных загрузок страниц, захватываемых по умолчанию. Этот параметр значительно расширяет видимость в средах одностраничных приложений (SPA) на основе различных JavaScript-фреймворков.

## Поддерживаемые JavaScript-фреймворки

Доступна специальная поддержка для [Angular 2–16](#enable-angular-12-16-support). Для Angular 17+ [требуется дополнительная настройка](#enable-angular-17-support). Если для приложения используется другой JavaScript-фреймворк, попробуйте [активировать общую поддержку](#enable-generic-js-frameworks).

Прекращение специальной поддержки определённых JavaScript-фреймворков

Специальная поддержка следующих JavaScript-фреймворков прекращена начиная с выхода версии RUM JavaScript 1.265 и Dynatrace версии 1.266.

| JavaScript-фреймворк | Версии |
| --- | --- |
| AngularJS | 1.0 - 1.7 |
| Angular with SystemJS | 2 - 15 |
| Dojo | 1.6.1 - 1.13 |
| Ext JS | 3.4, 4, 5, 6 |
| ICEfaces | 1.8, 2, 3 |
| jQuery ( Backbone.js ) | 1.3 - 1.12, 2.0 - 2.2, 3.0 - 3.6 |
| MooTools | 1.4.5 - 1.6.0 |
| Prototype | 1.7 |
| Sencha Touch | 2.0 - 2.4 |

При использовании одного из этих фреймворков [активируйте общую поддержку](#enable-generic-js-frameworks).

Кроме того, если среда была создана до Dynatrace версии 1.266, можно использовать версию RUM JavaScript, предлагающую специальную поддержку для фреймворка.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **RUM JavaScript updates**.
5. Выберите вариант **Latest IE7-10 supported** из раскрывающегося списка.

## Активация поддержки Angular 2–16

Если для приложения используется Angular 17+, следуйте инструкциям в разделе [Активация поддержки Angular 17+](#enable-angular-17-support).

Чтобы включить поддержку Angular 2–16:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Async web requests and SPAs**.
5. В разделе **JavaScript framework support** включите переключатель **Angular**.
6. Angular 12+: введите имя Angular-пакета.

   Что такое имя Angular-пакета?

   Начиная с Angular версии 12, необходимо указывать имя Angular-пакета приложения в настройках Dynatrace. В противном случае Real User Monitoring не будет работать.

   Для Angular 12 имя пакета зависит от имени проекта и больше не является статичным, тогда как для Angular 11 и более ранних версий имя пакета всегда `webpackjsonp`.

   Чтобы найти имя Angular-пакета для приложения:

   1. Откройте инструменты разработчика браузера и перейдите на вкладку **Console**.
   2. Начните вводить `webpackChunk`. Браузер должен отобразить имя пакета для Angular-приложения. Скопируйте его.
      Например, имя пакета на скриншоте ниже — `webpackChunklite`.

      ![Finding the Angular package name in the browser console](https://dt-cdn.net/images/find-angular-package-name-1918-f04cb24a1a.png)

      Finding the Angular package name in the browser console

      При наличии нескольких записей `webpackChunk` в консоли выберите ту, которая соответствует имени приложения. Также попробуйте отключить расширения браузера для получения более чистого списка.
      Если в консоли нет записей `webpackChunk`, вероятно, используется Angular версии 11 или более ранней — в этом случае имя Angular-пакета указывать не нужно.
   3. Вставьте имя, скопированное на шаге 2, в поле **Angular package name** в настройках приложения.

## Активация поддержки Angular 17+

Поскольку Angular 17 использует esbuild вместо Webpack по умолчанию, RUM JavaScript больше не может автоматически инструментировать Angular. По этой причине, если для приложения используется Angular 17+, требуется дополнительная настройка.

Для включения поддержки Angular 17+ выполните следующие действия.

**Шаг 1: [Активация общей поддержки JavaScript-фреймворка](#angular-config-web-ui)**

**Шаг 2: [Реализация захвата исключений](#angular-exception-capture)**

**Шаг 3: [Настройка обнаружения групп страниц](#angular-page-group-detection)**

### Шаг 1: Активация общей поддержки JavaScript-фреймворка

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Async web requests and SPAs**.
5. В разделе **JavaScript framework support** отключите переключатель **Angular**.
6. В разделе **Generic support** включите нужные параметры.

   * Включите **Capture fetch() requests** для захвата данных пользовательских действий для запросов на основе [Fetch API](/managed/observe/digital-experience/rum-concepts/user-actions#fetch-api "Learn what user actions are and how they help you understand what users do with your application.").
   * Включите **Capture XmlHttpRequest (XHR)** для захвата любого взаимодействия, приводящего к XmlHttpRequest-вызову, как XHR-действия.

### Шаг 2: Реализация захвата исключений

Angular имеет обработчик исключений по умолчанию ([`ErrorHandler`](https://angular.io/api/core/ErrorHandler)), который перехватывает исключения и записывает их в `console` с помощью `console.error`. Однако иногда используется пользовательский обработчик исключений для перехвата обработки ошибок.

#### Обработчик исключений по умолчанию

Если используется обработчик исключений по умолчанию, включите захват ошибок консоли, чтобы RUM JavaScript мог захватывать исключения для Angular 17+ приложений.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Custom configuration properties**.
5. Выберите **Add a custom configuration property** и введите `cce=1`.

   `cce` означает *capture console error* (захват ошибок консоли). При включении этой опции RUM JavaScript сообщает о первом объекте `Error` или строке, которую может найти в аргументах, переданных в `console.error`.

#### Пользовательский обработчик исключений

При наличии пользовательского обработчика исключений, не записывающего исключения в `console`, необходимо сообщать об исключениях вручную.

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

### Шаг 3: Настройка обнаружения групп страниц

Стандартное [обнаружение страниц и групп страниц](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.") основано на URL — путях и идентификаторах, автоматически определяемых Dynatrace. Если стандартная группировка страниц неверна или её нужно изменить, можно вручную сообщать о группах страниц с помощью Angular Router. Приведённый ниже пример кода можно использовать для получения группы страниц из `routeConfig`, где имена placeholder ещё доступны (например, `/journey/:id` вместо `/journey/1235`).

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

Также см. раздел [Определение собственной группировки страниц](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups#configure-page-grouping "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.").

### `dT_.initAngularNg()`

Не вызывайте `dT_.initAngularNg()`, так как эта функция больше не работает с Angular 17. Её вызов не нарушает работу, но и не имеет эффекта.

Для Angular 2–16 `dT_.initAngularNg` используется для передачи объектов HTTP и Headers в Dynatrace при использовании `HttpModule` из @angular/http или объектов HTTP и HttpHeaders при использовании `HttpClientModule` из @angular/common/http (Angular 5+).

## Активация общей поддержки JavaScript-фреймворка

Если приложение использует JavaScript-фреймворк, отличный от Angular, включите общую поддержку для XHR и fetch()-запросов.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Async web requests and SPAs**.
5. В разделе **Generic support** включите нужные параметры:

   * Включите **Capture fetch() requests** для захвата данных пользовательских действий для запросов на основе [Fetch API](/managed/observe/digital-experience/rum-concepts/user-actions#fetch-api "Learn what user actions are and how they help you understand what users do with your application.").
   * Включите **Capture XmlHttpRequest (XHR)** для захвата любого взаимодействия, приводящего к XmlHttpRequest-вызову, как XHR-действия.

## Включение поддержки действий с таймером

В зависимости от XHR (AJAX)-фреймворка или архитектуры приложения может также потребоваться включение настройки поддержки действий с таймером. Эта настройка необходима, когда приложение не инициирует XHR (AJAX)-вызовы непосредственно в обработчиках событий HTML-элементов, а откладывает их через вызовы `SetTimeout`.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Content capture**.
5. Включите **Timed action support**.

## Исключение конкретных XHR-вызовов из мониторинга

Когда приложение выполняет XHR или Fetch-запрос, он может быть захвачен одним из следующих способов:

* Если никакое другое пользовательское действие не является активным и XHR был инициирован взаимодействием пользователя, захватывается отдельное XHR-действие.
* Если другое пользовательское действие является активным и XHR не был инициирован взаимодействием пользователя, активное пользовательское действие расширяется для включения продолжительности XHR.

Можно исключить конкретные XHR-вызовы из мониторинга — например, если приложение отправляет частые XHR-запросы на основе статуса, которые не нужно видеть в пользовательских данных. При исключении этих запросов:

* Отдельные XHR-действия не захватываются.
* Исключённые XHR не продлевают продолжительность других пользовательских действий. Однако они всё равно могут появляться в [анализе водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis."), если активна поддержка W3C resource timing (настройки приложения > **Capturing** > **Content capture** > **W3C resource timing support**).

### Настройка правил исключения XHR

Чтобы исключить XHR-вызовы из мониторинга:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Exclusions** > **XHR exclusions**.
5. Выберите **Add an XHR exclusion rule** и укажите регулярное выражение JavaScript, соответствующее URL запросов, которые нужно исключить.

Избегайте неэффективных регулярных выражений

Неэффективные регулярные выражения могут вызывать проблемы с производительностью приложения, включая зависания браузера на несколько секунд. Для лучшей производительности пишите выражения, соответствующие подстроке URL, а не всему URL. Это особенно актуально для длинных URL.

### Применение правил исключения XHR

RUM JavaScript проверяет регулярное выражение по URL с помощью [`RegExp.prototype.test()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test). Регулярное выражение не должно соответствовать всему URL, а только его подстроке. URL может быть относительным или абсолютным в зависимости от того, что было передано в XHR или Fetch-вызов. Сопоставление выполняется без учёта регистра, и прямые косые черты (`/`) не нужно экранировать.

Сайты для тестирования регулярных выражений

При составлении регулярного выражения на сайте, например [Regex101](https://regex101.com/), выберите следующие параметры:

* Тип **ECMAScript (JavaScript)**
* Разделитель `"`
* Флаг **Case insensitive match**

## Отсутствие XHR-действий при использовании промисов

При использовании [промисов](https://web.dev/promises/) Dynatrace не всегда создаёт пользовательские действия, поэтому некоторые XHR-действия могут отсутствовать.

Как Dynatrace обычно создаёт пользовательские действия:

1. Регистрируется взаимодействие пользователя со страницей — например, событие нажатия, нажатия клавиши или прокрутки.
2. Если XHR или fetch-запрос начинается в течение следующих 30 миллисекунд, создаётся пользовательское действие. Если запрос начинается позже, пользовательское действие не создаётся.

30-миллисекундный временной интервал расширяется неограниченно для текущего синхронного выполнения — например, когда длительное вычисление в коде приложения занимает более 30 мс и XHR начинается только после завершения вычисления. Однако это применяется только при выполнении кода непосредственно в обработчике событий без использования `setTimeout`, `setInterval` или промисов.

При использовании промисов код может выполняться асинхронно. Когда выполнение кода завершено, исходный вызывающий получает уведомление и может продолжить выполнение своего кода. К сожалению, невозможно определить, когда завершится выполнение кода; оно может произойти в пределах или за пределами 30-миллисекундного окна. По этой причине рекомендуется использовать [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") для создания действий в таких случаях.

Чтобы проверить, использует ли пользовательское действие промисы:

1. Откройте инструменты разработчика браузера.
2. Выполните действие в веб-приложении.
3. Проверьте инициатор запроса.

   ![Check if a user action uses promises in browser's developer tools](https://dt-cdn.net/images/promise-then-2446-542a8c167e.png)

   Check if a user action uses promises in browser's developer tools