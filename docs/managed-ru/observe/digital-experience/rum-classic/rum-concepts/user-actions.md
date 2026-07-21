---
title: Пользовательские действия в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions
---

# Пользовательские действия в RUM Classic

# Пользовательские действия в RUM Classic

* Объяснение
* 12 мин чтения
* Обновлено 10 апр. 2026 г.

Пользовательское действие, это взаимодействие с интерфейсом конечного пользователя, которое включает обращение к веб-серверу и потенциально может содержать несколько вложенных вызовов. Это переход от одного представления к другому, вызванный вводом пользователя, например загрузкой страницы, кликом или касанием.

## Типы пользовательских действий для веб-приложений

Веб-приложения

В Dynatrace доступны следующие типы пользовательских действий для [веб-приложений](/managed/observe/digital-experience/rum-classic/rum-concepts/applications#web "Learn about monitored applications in Real User Monitoring Classic and the different application types supported by Dynatrace."):

* [Действия загрузки](#load-action)
* [XHR-действия](#xhr-action)
* [Пользовательские действия](#custom-action)

Ключевое отличие между этими типами действий заключается в способе расчёта длительности действия и в списке доступных метрик.

### Действия загрузки

Действие загрузки определяется как фактическая загрузка страницы в браузере. Если ввести URL в браузере и нажать **Enter**, происходит действие загрузки. В ходе этого типа действия загружается множество ресурсов, включая изображения, HTML и CSS.

#### Длительность действия загрузки

Длительность действия, это время, необходимое для полного завершения действия загрузки. Точнее, время начала пользовательского действия равно времени `navigationStart` по спецификации W3C. Если этот атрибут недоступен, время начала равно моменту инициализации [RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") в браузере. Время окончания, это момент, когда последний обработчик `onload` завершил свою задачу. Обработчик `onload`, это обработчик события в JavaScript, который используется для вызова выполнения JavaScript после полной загрузки страницы, фрейма или изображения. Если обработчик `onload` запускает какие-либо [`XMLHttpRequests`](#xhr-action), пользовательское действие завершается, когда завершается `XMLHttpRequest`.

![Page load cycle](https://cdn.bfldr.com/B686QPH3/as/jz8qb74kgs3xt4n6k9fk6nx/User_actions_-_Light_Mode?auto=webp&format=png&position=1)

Page load cycle

#### Тайминги действия загрузки

Следующие показатели используются для построения диаграммы длительности отдельных шагов процесса действия загрузки.

| Показатель | Описание | Определение в терминах спецификации W3C |
| --- | --- | --- |
| **DNS lookup** | Время, затраченное на разрешение имени хоста для целевого URL | `window.performance.timing.domainLookupEnd` − `window.performance.timing.domainLookupStart` |
| **TCP connect** | Время, затраченное на установление TCP-соединения с сервером (включая SSL) | `window.performance.timing.connectEnd` − `window.performance.timing.connectStart` |
| **Secure connect** | Время, затраченное на защиту соединения, установленного с сервером. Включает SSL-рукопожатие и SOCKS. | `window.performance.timing.connectEnd` − `window.performance.timing.secureConnectionStart` |
| **Redirect time** | Время, затраченное на прохождение HTTP-редиректов | `window.performance.timing.redirectEnd` − `window.performance.timing.redirectStart` |
| **Request** | Время от запроса страницы у сервера до получения первого байта | `window.performance.timing.responseStart` − `window.performance.timing.requestStart` |
| **Response** | Время, затраченное на получение ответа | `window.performance.timing.responseEnd` − `window.performance.timing.responseStart` |
| **Time to first byte (TTFB)** | Время до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса | `window.performance.timing.responseStart` |
| **Server time** | Время, затраченное на серверную обработку страницы | `window.performance.timing.responseStart` − `window.performance.timing.requestStart` |
| **Network time** | Время, затраченное на запрос и получение ресурсов (включая DNS lookup, редирект и время TCP-соединения) | `window.performance.timing.responseEnd` − `window.performance.timing.fetchStart` − (`window.performance.timing.responseStart` − `window.performance.timing.requestStart`) |
| **Frontend time** | Время, затраченное браузером на рендеринг страницы | `User action duration` − `Server time` − `Network time` |
| **Processing** | Время между загрузкой DOM и началом события Load | `window.performance.timing.loadEventStart` − `window.performance.timing.domLoading` |
| **Application cache** | Время, затраченное на проверку соответствующих кэшей приложения. Включает время до установления соединения с сервером. | `window.performance.timing.domainLookupStart` − `window.performance.timing.fetchStart` |
| **OnDomContentLoaded** | Время, затраченное на выполнение обработчиков `OnDomContentLoaded` | `window.performance.timing.domContentLoaded` − `window.performance.timing.domLoading` |
| **OnLoad** | Время, затраченное на обработку события load | `window.performance.timing.loadEventEnd` − `window.performance.timing.loadEventStart` |
| **Callback** | Время, затраченное на выполнение XHR-колбэков | Н/Д |
| **First paint** | Время, затраченное на отрисовку первого элемента фона, отличного от стандартного | Н/Д |
| **First input start** | Момент первого взаимодействия пользователя со страницей, например клика по элементу управления интерфейса | Н/Д |
| **First input delay** | Время от первого взаимодействия со страницей до момента, когда агент пользователя может отреагировать на это взаимодействие | Н/Д |
| **First contentful paint** | Время, затраченное на отрисовку первого фрагмента контента, такого как текст или изображения | Н/Д |
| **Largest contentful paint** | Время, затраченное на отрисовку самого крупного элемента в области просмотра | Н/Д |
| **Cumulative layout shift** | Оценка, измеряющая непредвиденное смещение видимых элементов веб-страницы при действии загрузки | Н/Д |
| **Visually complete** | Время, затраченное на полную отрисовку контента в области просмотра | Н/Д |
| **Speed index** | Оценка, измеряющая скорость отрисовки видимых частей страницы | Н/Д |
| **User action duration** | Время, затраченное на завершение загрузки страницы. Включает время загрузки XHR-запросов, инициированных до `loadEventEnd`, а также время загрузки динамических ресурсов и выполнения скриптов, вызванных изменениями DOM. | Н/Д |

### XHR-действия

Dynatrace непрерывно отслеживает взаимодействия пользователя с каждой страницей. Если взаимодействие пользователя приводит к вызовам `XmlHttpRequests` или `fetch()`, создаётся XHR-действие. Dynatrace также обнаруживает, запускаются ли дополнительные XHR в колбэке исходного XHR, и так далее. В этом случае Dynatrace ожидает завершения всех запросов. Отслеживая DOM, Dynatrace также может определять ресурсы, добавленные в колбэках. Затем Dynatrace ожидает завершения загрузки этих ресурсов, прежде чем завершить действие.

XHR-действие начинается с клика пользователя по элементу управления на веб-странице. Все [метрики](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") рассчитываются относительно этого момента времени и основаны на исходном XHR, который запускает пользовательское действие.

По умолчанию RUM фиксирует определённые типы взаимодействий. Можно настроить RUM на обнаружение ещё большего числа типов взаимодействий. Подробности см. в разделе [Захват дополнительных типов взаимодействий для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/capture-interaction-types "Choose which interaction types RUM should detect for your web applications.").

#### XmlHttpRequest

Большинство современных приложений, включая одностраничные приложения, полагаются на единственное действие загрузки, которое загружает фреймворк и инициализирует страницу. После этого [DOM﻿](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) страницы изменяется через JavaScript, а всё взаимодействие с веб-сервером выполняется через [`XmlHttpRequest`](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

![XHR actions](https://cdn.bfldr.com/B686QPH3/as/2rntrf3ptpjmwsjgbgc7kk7/XHR_actions_-_Light_Mode?auto=webp&format=png&position=1)

XHR actions

#### Fetch API

[Fetch API﻿](https://fetch.spec.whatwg.org/) предоставляет интерфейс для получения ресурсов, в том числе по сети. Он похож на `XMLHttpRequest`, но API предоставляет более гибкий набор функций. Общие определения `Request`, `Response` и других объектов сетевых запросов в Fetch позволяют использовать их в любой момент, когда это необходимо, будь то service workers, Cache API или что-либо ещё, что обрабатывает или изменяет запросы и ответы. Fetch также поддерживает Cross Origin Resource Sharing (CORS).

Пользовательские действия на основе Fetch API отображаются в Dynatrace как XHR-действия. Можно настроить RUM на [автоматическое обнаружение и захват информации о запросах Fetch API](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

### Пользовательские (custom) действия

Вместо того чтобы полагаться на автоматическую генерацию пользовательских действий, можно донастроить Real User Monitoring, добавив дополнительные пользовательские действия напрямую в HTML приложения. Это полезно, если автоматическая генерация пользовательских действий не улавливает конкретные действия или если нужно ввести точные тайминги в мониторинг приложения. Например, можно измерить, сколько времени занимает открытие выпадающего меню на чистом JavaScript, или измерить длительность выполнения какого-то JavaScript-кода. Чтобы определить пользовательские действия, используй [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API.").

## Длительность пользовательского действия

Ниже приведена информация о максимальной длительности пользовательского действия в Dynatrace и о составляющих пользовательского действия для веб-приложений.

### Максимальная длительность пользовательского действия

Максимальная длительность пользовательского действия зависит от типа приложения.

Веб-приложение

Мобильное приложение

Пользовательское приложение

Максимальная длительность веб-пользовательского действия составляет 3 минуты. Если пользовательское действие длится дольше, Dynatrace регистрирует такое действие как трёхминутное.

Максимальная длительность мобильного пользовательского действия зависит от типа действия.

* **Автоматически создаваемые действия**

  По умолчанию максимальная длительность автоматически созданного мобильного пользовательского действия установлена на 1 минуту. Этот лимит можно увеличить до 9 минут, хотя делать это не рекомендуется. Для Android см. [Настройка мониторинга пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#configure-user-action-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent."); для iOS используй [ключ конфигурации `DTXAutoActionMaxDurationMilliseconds`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

  Если автоматически созданное пользовательское действие длится дольше настроенной максимальной длительности, такое действие закрывается и передаётся в Dynatrace с длительностью, немного превышающей настроенное максимальное значение.
* **Пользовательские действия**

  Максимальная длительность мобильного пользовательского действия составляет 9 минут.

  Если пользовательское действие длится дольше 9 минут и не закрывается, такое действие отбрасывается и не передаётся в Dynatrace.

Максимальная длительность пользовательского действия в пользовательских приложениях составляет 10 минут. Если пользовательское действие длится дольше, такое действие отбрасывается и не передаётся в Dynatrace.

### Составляющие пользовательского действия для веб-приложений

Длительность пользовательского действия можно разложить на три компонента:

* **Время сервера**: время, затраченное на обработку страницы на стороне сервера
* **Время сети**: время, затраченное на запрос и получение ресурсов (включая время DNS-запроса, редиректа и TCP-подключения)
* **Время фронтенда**: время, затраченное браузером на рендеринг страницы

Эти компоненты формируют общую длительность пользовательского действия.

Длительность пользовательского действия рассчитывается следующим образом.

**Длительность пользовательского действия** = (`loadEventEnd` или `endTimeOfLastXHR`) − `actionStart`

В этом расчёте

actionStart
:   `navigationStart` для загрузок страниц или "время клика" для XHR-действий и пользовательской навигации, например клик по кнопке или ссылке

endTimeOfLastXHR
:   Если XHR-вызовы запускаются в процессе и не завершаются до `loadEventEnd`, вместо времени `loadEventEnd` используется время завершения последнего XHR-вызова.

Составляющие пользовательского действия рассчитываются следующим образом.

**Время сервера** = `responseStart` − `requestStart`

**Время сети** = (`requestStart` − `actionStart`) + (`responseEnd` − `responseStart`)

**Время фронтенда** = `Длительность пользовательского действия` − `Время сервера` − `Время сети`

Ниже приведены примеры составляющих пользовательского действия.

Составляющие пользовательского действия для одного экземпляра пользовательского действия в пользовательской сессии

![Представление пользовательской сессии](https://dt-cdn.net/images/user-session-view-updated-2472-c33e411c76.png)

Представление пользовательской сессии

Составляющие пользовательского действия, агрегированные для одного пользовательского действия, то есть по всем экземплярам пользовательского действия

![Представление пользовательского действия](https://dt-cdn.net/images/useractionview-1785-9f221a3aac.png)

Представление пользовательского действия

Составляющие пользовательского действия, агрегированные для всего приложения

![Обзор приложения](https://dt-cdn.net/images/appoverview-1789-db21269b45.png)

Обзор приложения

## Правила именования пользовательских действий

Многие приложения позволяют пользователям достигать одной и той же цели с помощью разных элементов управления интерфейсом и разными путями. При мониторинге таких приложений может быть сложно отличить действия, которые приводят к одному и тому же результату и цели, но выполняются через разные части интерфейса приложения. Аналогично, если приложение переведено на несколько языков, одна и та же функция приложения или элемент интерфейса может отображаться под разными названиями. С помощью правил именования пользовательских действий Dynatrace может обнаруживать такие тонкие различия и интеллектуально группировать пользовательские действия, преследующие одну и ту же цель, в логические группы для мониторинга.

Dynatrace автоматически удаляет из названий пользовательских действий определённые распространённые токены `sessionid`, например `jsessionid` для Java-контейнеров, стандартный `sessionid` для PHP и `CFID` и `CFTOKEN` для ColdFusion. Тем не менее в твоём окружении может присутствовать множество вариаций session ID. Если Dynatrace не распознаёт и не удаляет автоматически session ID из некоторых встречающихся названий пользовательских действий, нужно настроить пользовательские правила именования для [веб-](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/naming-rules-mobile "Customize automatically generated user action names for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/naming-rules-custom "Customize automatically generated user action names for your custom applications.").

При настройке пользовательских правил именования для веб-, мобильных и пользовательских приложений нужно помнить, что ввод в разделах **Add placeholder** и **Add naming rule** чувствителен к регистру. Регистронезависимым можно сделать только уже настроенное название пользовательского действия.

## Дочерние действия

Дочерние действия (child actions), это действия, привязанные к основному, или родительскому, действию пользователя. Дочерние действия можно создавать для веб, мобильных и пользовательских приложений.

Для веб-приложений дочерние действия создаются с помощью RUM JavaScript API, в частности с помощью метода [`enterXhrAction`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enterxhraction).

Для мобильных и пользовательских приложений Dynatrace предлагает метод API для создания дочернего действия.

[Android SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#child-actions) [iOS SDK](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-child-action) [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#manual-sub-action) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#manual-sub-action) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#a-namecustomsubactionacreate-custom-sub-actions) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#create-custom-sub-actions) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#create-custom-actions) 

Возможная вложенность дочерних действий зависит от типа приложения и используемой технологии.

Веб-приложения

Нет ограничения на количество дочерних действий, привязанных к родительскому действию, и нет ограничения на количество уровней.

Однако стоит учитывать, что дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), а вложенность дочерних действий не сохраняется на [странице анализа waterfall](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для родительского действия, к которому эти дочерние действия привязаны.

Android, iOS

Нет ограничения на количество дочерних действий, привязанных к родительскому действию. Однако стоит учитывать, что доступно только девять уровней дочерних действий: можно создать одно родительское действие и девять уровней дочерних действий (когда дочернее действие A добавляется к родительскому действию, дочернее действие B добавляется к дочернему действию A, дочернее действие C добавляется к дочернему действию B и так далее). Также см. [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно посмотреть на [странице анализа waterfall](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для родительского действия, к которому эти дочерние действия привязаны. Хотя вложенность дочерних действий не полностью сохраняется в представлении анализа waterfall и все дочерние действия отображаются как дочерние действия уровня 1, вложенность действий всё же можно понять по временным меткам.

Flutter, React Native, Xamarin, .NET MAUI, OpenKit

Нет ограничения на количество дочерних действий, привязанных к пользовательскому действию. Однако стоит учитывать, что доступен только один уровень дочерних действий: нельзя создать дочернее действие для другого дочернего действия (у дочерних действий не может быть своих дочерних действий). Также см. [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно посмотреть на [странице анализа waterfall](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для пользовательского действия, к которому эти дочерние действия привязаны.

## Ключевые пользовательские действия

Большинство приложений включают пользовательские действия, которые особенно важны для успеха цифрового бизнеса. Примерами таких действий являются регистрация, оформление заказа и поиск товаров. Такие ключевые пользовательские действия могут выполняться дольше остальных, либо к ним может предъявляться требование более короткой, чем в среднем, продолжительности.

Например, предположим, что глобальный [порог Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") установлен на 3 секунды. Хотя этот порог может быть приемлемым для большинства пользовательских действий, он может не подходить для действия регистрации. Либо может существовать действие поиска, которое довольно сложное и требует больше времени, чем отведённые 3 секунды.

Пользовательское действие можно отметить как ключевое пользовательское действие и настроить рейтинг Apdex для ключевых пользовательских действий в настройках [веб](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications."), [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Mark a user action as a key user action and configure Apdex rating for key user actions of your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-key-user-actions-custom "Mark a user action as a key user action and configure Apdex rating for key user actions of your custom applications.").

## Связанные темы

* [Создание пользовательских имён действий пользователя для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.")
* [Создание пользовательских имён действий пользователя для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/naming-rules-mobile "Customize automatically generated user action names for your mobile applications.")
* [Создание пользовательских имён действий пользователя для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/naming-rules-custom "Customize automatically generated user action names for your custom applications.")
* [Настройка ключевых пользовательских действий для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications.")
* [Настройка ключевых пользовательских действий для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Mark a user action as a key user action and configure Apdex rating for key user actions of your mobile applications.")
* [Настройка ключевых пользовательских действий для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-key-user-actions-custom "Mark a user action as a key user action and configure Apdex rating for key user actions of your custom applications.")