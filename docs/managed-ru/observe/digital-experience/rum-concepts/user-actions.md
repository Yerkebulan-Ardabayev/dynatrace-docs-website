---
title: Пользовательские действия
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/user-actions
scraped: 2026-05-12T11:10:13.739089
---

# Пользовательские действия

# Пользовательские действия

* Explanation
* 12-min read
* Updated on Apr 10, 2026

Пользовательское действие — это взаимодействие с интерфейсом конечного пользователя, которое включает обращение к веб-серверу и может потенциально содержать несколько вложенных вызовов. Это переход из одного представления в другое, инициированный пользователем, например загрузка страницы, клик или касание.

## Типы пользовательских действий для веб-приложений

Web applications

Для [веб-приложений](/managed/observe/digital-experience/rum-concepts/applications#web "Узнайте о мониторируемых приложениях в мониторинге реальных пользователей и о различных типах приложений, поддерживаемых Dynatrace.") в Dynatrace доступны следующие типы пользовательских действий:

* [Действия загрузки](#load-action)
* [XHR-действия](#xhr-action)
* [Пользовательские действия](#custom-action)

Ключевое различие между этими типами действий заключается в способе расчёта длительности действия и наборе доступных метрик.

### Действия загрузки

Действие загрузки определяется как фактическая загрузка страницы в браузере. Когда вы вводите URL в браузере и нажимаете **Enter**, выполняется действие загрузки. В ходе этого типа действия загружается множество ресурсов: изображения, HTML и CSS.

#### Длительность действия загрузки

Длительность действия — это время, необходимое для завершения действия загрузки. Конкретно: время начала пользовательского действия равно времени `navigationStart` по стандарту W3C. Если этот атрибут недоступен, время начала равно времени инициализации [RUM JavaScript](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Выберите формат RUM JavaScript-сниппета, наиболее подходящий для вашего случая") в браузере. Время окончания — момент завершения последнего обработчика `onload`. Обработчик `onload` — это обработчик событий в JavaScript, используемый для вызова выполнения JavaScript после полной загрузки страницы, фрейма или изображения. Если обработчиком `onload` запущены [`XMLHttpRequests`](#xhr-action), пользовательское действие завершается после завершения `XMLHttpRequest`.

![Цикл загрузки страницы](https://cdn.bfldr.com/B686QPH3/as/jz8qb74kgs3xt4n6k9fk6nx/User_actions_-_Light_Mode?auto=webp&format=png&position=1)

Цикл загрузки страницы

#### Тайминги действия загрузки

Для отображения длительности конкретных шагов в процессе действия загрузки используются следующие измерения.

| Измерение | Описание | Определение в терминах спецификации W3C |
| --- | --- | --- |
| **DNS lookup** | Время разрешения имени хоста для целевого URL | `window.performance.timing.domainLookupEnd` - `window.performance.timing.domainLookupStart` |
| **TCP connect** | Время установки TCP-соединения с сервером (включая SSL) | `window.performance.timing.connectEnd` - `window.performance.timing.connectStart` |
| **Secure connect** | Время защиты установленного соединения с сервером. Включает SSL-рукопожатие и SOCKS. | `window.performance.timing.connectEnd` - `window.performance.timing.secureConnectionStart` |
| **Redirect time** | Время следования HTTP-перенаправлениям | `window.performance.timing.redirectEnd` - `window.performance.timing.redirectStart` |
| **Request** | Время запроса страницы с сервера до получения первого байта | `window.performance.timing.responseStart` - `window.performance.timing.requestStart` |
| **Response** | Время получения ответа | `window.performance.timing.responseEnd` - `window.performance.timing.responseStart` |
| **Time to first byte (TTFB)** | Время до получения первого байта ответа от сервера, кэша приложения или локального ресурса | `window.performance.timing.responseStart` |
| **Server time** | Время, затраченное на серверную обработку страницы | `window.performance.timing.responseStart` - `window.performance.timing.requestStart` |
| **Network time** | Время запроса и получения ресурсов (включая DNS lookup, redirect и TCP connect) | `window.performance.timing.responseEnd` - `window.performance.timing.fetchStart` - (`window.performance.timing.responseStart` - `window.performance.timing.requestStart`) |
| **Frontend time** | Время браузера на отрисовку страницы | `User action duration` - `Server time` - `Network time` |
| **Processing** | Время между загрузкой DOM и началом события загрузки | `window.performance.timing.loadEventStart` - `window.performance.timing.domLoading` |
| **Application cache** | Время проверки соответствующих кэшей приложения. Включает время до установки соединения с сервером. | `window.performance.timing.domainLookupStart` - `window.performance.timing.fetchStart` |
| **OnDomContentLoaded** | Время выполнения обработчиков `OnDomContentLoaded` | `window.performance.timing.domContentLoaded` - `window.performance.timing.domLoading` |
| **OnLoad** | Время обработки события загрузки | `window.performance.timing.loadEventEnd` - `window.performance.timing.loadEventStart` |
| **Callback** | Время выполнения XHR-коллбэков | N/A |
| **First paint** | Время до отрисовки первого элемента, отличного от фона по умолчанию | N/A |
| **First input start** | Момент первого взаимодействия пользователя со страницей, например, клик по элементу управления | N/A |
| **First input delay** | Время от первого взаимодействия со страницей до момента, когда пользовательский агент может ответить на него | N/A |
| **First contentful paint** | Время до отрисовки первого контента (текста или изображений) | N/A |
| **Largest contentful paint** | Время до отрисовки наибольшего элемента в области просмотра | N/A |
| **Cumulative layout shift** | Показатель непредвиденного смещения видимых элементов для действия загрузки | N/A |
| **Visually complete** | Время полной отрисовки контента в области просмотра | N/A |
| **Speed index** | Показатель, измеряющий скорость отрисовки видимых частей страницы | N/A |
| **User action duration** | Время, необходимое для завершения загрузки страницы. Включает время загрузки XHR-запросов, инициированных до `loadEventEnd`, а также время загрузки динамических ресурсов и выполнения скриптов, запущенных изменениями DOM. | N/A |

### XHR-действия

Dynatrace непрерывно отслеживает взаимодействия пользователя с каждой страницей. Если взаимодействие пользователя приводит к вызовам `XmlHttpRequests` или `fetch()`, создаётся XHR-действие. Dynatrace также определяет наличие дополнительных XHR, запускаемых в коллбэке начального XHR, и так далее. В этом случае Dynatrace ожидает завершения всех запросов. Отслеживая DOM, Dynatrace также может идентифицировать ресурсы, добавленные в коллбэках, и ожидает их загрузки перед завершением действия.

XHR-действие начинается с клика пользователя на элемент управления веб-страницы. Все [метрики](/managed/observe/digital-experience/rum-concepts/user-action-metrics "Узнайте, какие метрики Dynatrace рассчитывает для пользовательских действий и что означает каждая из них.") рассчитываются относительно этого момента времени и основаны на начальном XHR, запускающем пользовательское действие.

По умолчанию RUM фиксирует определённые типы взаимодействий. Вы можете настроить RUM на обнаружение дополнительных типов взаимодействий. Подробнее см. [Захват дополнительных типов взаимодействий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types "Выберите, какие типы взаимодействий RUM должен определять для ваших веб-приложений.").

#### XmlHttpRequest

Большинство современных приложений, включая одностраничные приложения (SPA), полагаются на одно действие загрузки, которое скачивает фреймворк и инициализирует страницу. После этого [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) страницы изменяется через JavaScript, а всё взаимодействие с веб-сервером осуществляется через [`XmlHttpRequest`](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Узнайте, почему нужно активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и как настроить мониторинг реальных пользователей для XHR-действий.").

![XHR-действия](https://cdn.bfldr.com/B686QPH3/as/2rntrf3ptpjmwsjgbgc7kk7/XHR_actions_-_Light_Mode?auto=webp&format=png&position=1)

XHR-действия

#### Fetch API

[Fetch API](https://fetch.spec.whatwg.org/) предоставляет интерфейс для получения ресурсов, в том числе через сеть. Он похож на `XMLHttpRequest`, но предоставляет более гибкий набор возможностей. Универсальные определения объектов `Request`, `Response` и других объектов сетевых запросов в Fetch позволяют использовать их в любой момент: в сервис-воркерах, Cache API или везде, где нужно обрабатывать или изменять запросы и ответы. Fetch также поддерживает Cross Origin Resource Sharing (CORS).

Пользовательские действия, основанные на Fetch API, отображаются в Dynatrace как XHR-действия. Вы можете настроить RUM на [автоматическое обнаружение и захват информации о запросах Fetch API](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Узнайте, почему нужно активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и как настроить мониторинг реальных пользователей для XHR-действий.").

### Пользовательские действия

Вместо того чтобы полагаться на генерацию пользовательских действий по умолчанию, вы можете точно настроить мониторинг реальных пользователей, добавив дополнительные пользовательские действия непосредственно в HTML вашего приложения. Это может быть полезно, если автоматическая генерация пользовательских действий не фиксирует определённые действия или вы хотите ввести конкретные детальные тайминги в мониторинг вашего приложения. Например, можно измерить время открытия выпадающего меню на чистом JavaScript или длительность выполнения какого-либо JavaScript-кода. Для определения пользовательских действий используйте [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить мониторинг реальных пользователей с помощью JavaScript API.").

## Длительность пользовательского действия

Ниже представлена информация о максимальной длительности пользовательского действия в Dynatrace и о компонентах длительности для веб-приложений.

### Максимальная длительность пользовательского действия

Максимальная длительность пользовательского действия зависит от типа приложения.

Web application

Mobile app

Custom app

Максимальная длительность пользовательского действия в веб-приложении составляет 3 минуты. Если пользовательское действие длится дольше, Dynatrace фиксирует его как действие длиной 3 минуты.

Максимальная длительность пользовательского действия в мобильном приложении зависит от типа действия.

* **Автоматически генерируемые действия**

  По умолчанию максимальная длительность автоматически генерируемого мобильного пользовательского действия составляет 1 минуту. Вы можете увеличить этот предел до 9 минут, хотя делать это не рекомендуется. Для Android см. [Настройка мониторинга пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#configure-user-action-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent."); для iOS используйте [ключ конфигурации `DTXAutoActionMaxDurationMilliseconds`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью ключей конфигурации можно точно настроить автоматическое инструментирование iOS-приложений.").

  Если автоматически генерируемое пользовательское действие длится дольше настроенного максимума, оно закрывается и передаётся в Dynatrace с длительностью, незначительно превышающей настроенный максимум.

* **Пользовательские действия**

  Максимальная длительность мобильного пользовательского действия составляет 9 минут.

  Если пользовательское действие длится более 9 минут и не закрыто, оно удаляется и не передаётся в Dynatrace.

Максимальная длительность пользовательского действия в пользовательских приложениях составляет 10 минут. Если пользовательское действие длится дольше, оно удаляется и не передаётся в Dynatrace.

### Компоненты длительности пользовательского действия для веб-приложений

Длительность пользовательского действия можно разбить на три компонента:

* **Server time**: время, затраченное на серверную обработку страницы
* **Network time**: время запроса и получения ресурсов (включая DNS lookup, redirect и TCP connect)
* **Frontend time**: время браузера на отрисовку страницы

Эти компоненты составляют общую длительность пользовательского действия.

Длительность пользовательского действия рассчитывается следующим образом:

**User action duration** = (`loadEventEnd` или `endTimeOfLastXHR`) - `actionStart`

В этом расчёте:

actionStart
:   `navigationStart` для загрузок страниц или «время клика» для XHR-действий и пользовательских навигаций, таких как клик на кнопку или ссылку

endTimeOfLastXHR
:   Если XHR-вызовы запускаются в процессе и не завершаются до `loadEventEnd`, вместо времени `loadEventEnd` используется время окончания последнего XHR-вызова.

Компоненты длительности пользовательского действия рассчитываются следующим образом:

**Server time** = `responseStart` - `requestStart`

**Network time** = (`requestStart` - `actionStart`) + (`responseEnd` - `responseStart`)

**Frontend time** = `User action duration` - `Server time` - `Network time`

Примеры компонентов пользовательского действия приведены ниже.

Компоненты пользовательского действия для отдельного экземпляра в сессии пользователя

![Представление сессии пользователя](https://dt-cdn.net/images/user-session-view-updated-2472-c33e411c76.png)

Представление сессии пользователя

Компоненты пользовательского действия, агрегированные для одного пользовательского действия (по всем экземплярам)

![Представление пользовательского действия](https://dt-cdn.net/images/useractionview-1785-9f221a3aac.png)

Представление пользовательского действия

Компоненты пользовательского действия, агрегированные для всего приложения

![Обзор приложения](https://dt-cdn.net/images/appoverview-1789-db21269b45.png)

Обзор приложения

## Правила именования пользовательских действий

Многие приложения позволяют пользователям достигать одной и той же цели с помощью разных элементов управления и разными путями. При мониторинге таких приложений бывает сложно различать действия, имеющие одинаковый результат и цель, но выполняемые через разные части интерфейса. Аналогично, если приложение переведено на несколько языков, одна и та же функция или элемент интерфейса могут отображаться под разными названиями. С помощью правил именования пользовательских действий Dynatrace может обнаруживать такие тонкие различия и интеллектуально группировать пользовательские действия, достигающие одной цели, в логические группы для мониторинга.

Dynatrace автоматически удаляет некоторые распространённые токены `sessionid` из имён пользовательских действий, например `jsessionid` для Java-контейнеров, стандартный `sessionid` для PHP, а также `CFID` и `CFTOKEN` для ColdFusion. Тем не менее в вашей среде может присутствовать множество вариаций идентификаторов сессий. Если Dynatrace автоматически не распознаёт и не удаляет идентификаторы сессий из некоторых имён пользовательских действий, необходимо настроить пользовательские правила именования для [веб-](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Настройте автоматически генерируемые имена пользовательских действий для ваших веб-приложений."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/naming-rules-mobile "Настройте автоматически генерируемые имена пользовательских действий для ваших мобильных приложений.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Настройте автоматически генерируемые имена пользовательских действий для ваших пользовательских приложений.").

При настройке пользовательских правил именования для веб-, мобильных и пользовательских приложений учтите, что ввод в разделах **Add placeholder** и **Add naming rule** чувствителен к регистру. Нечувствительным к регистру можно сделать только уже настроенное имя пользовательского действия.

## Дочерние действия

Дочерние действия — это действия, прикреплённые к основному (родительскому) пользовательскому действию. Дочерние действия можно создавать для веб-, мобильных и пользовательских приложений.

Для веб-приложений дочерние действия создаются с помощью RUM JavaScript API, а именно метода [`enterXhrAction`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enterxhraction).

Для мобильных и пользовательских приложений Dynatrace предоставляет API-метод для создания дочернего действия.

[Android SDK](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#child-actions) [iOS SDK](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#create-child-action) [Xamarin](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#manual-sub-action) [.NET MAUI](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#manual-sub-action) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#a-namecustomsubactionacreate-custom-sub-actions) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#create-custom-sub-actions) [OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#create-custom-actions)

Возможная вложенность дочерних действий зависит от типа приложения и используемой технологии.

Web applications

Количество дочерних действий, прикреплённых к родительскому, не ограничено, как и количество уровней вложенности.

Однако учтите, что дочерние действия не отображаются на [странице деталей сессии пользователя](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте о сегментации и фильтрации сессий пользователей."), а вложенность дочерних действий не сохраняется на [странице waterfall-анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать данные мониторинга пользовательских действий через waterfall-анализ.") для родительского действия, к которому прикреплены эти дочерние действия.

Android, iOS

Количество дочерних действий, прикреплённых к родительскому, не ограничено. Однако допускается только девять уровней вложенности дочерних действий: можно создать одно родительское действие и девять уровней дочерних (когда дочернее действие A добавляется к родительскому, дочернее B — к A, дочернее C — к B и т.д.). Также см. [Структура сессии пользователя для отдельного пользователя](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется сессия пользователя, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице деталей сессии пользователя](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте о сегментации и фильтрации сессий пользователей."), но их можно просматривать на [странице waterfall-анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать данные мониторинга пользовательских действий через waterfall-анализ.") для родительского действия. Хотя вложенность дочерних действий не полностью сохраняется во view waterfall-анализа и все дочерние действия отображаются как дочерние 1-го уровня, из таймингов всё равно можно понять структуру вложенности.

Flutter, React Native, Xamarin, .NET MAUI, OpenKit

Количество дочерних действий, прикреплённых к пользовательскому действию, не ограничено. Однако допускается только один уровень вложенности: нельзя создать дочернее действие для другого дочернего действия (дочерние действия не могут иметь собственных дочерних действий). Также см. [Структура сессии пользователя для отдельного пользователя](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется сессия пользователя, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице деталей сессии пользователя](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте о сегментации и фильтрации сессий пользователей."), но их можно просматривать на [странице waterfall-анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать данные мониторинга пользовательских действий через waterfall-анализ.") для пользовательского действия, к которому они прикреплены.

## Ключевые пользовательские действия

В большинстве приложений есть пользовательские действия, особенно важные для успеха вашего цифрового бизнеса. Примеры таких действий: регистрация, оформление заказа и поиск товаров. Подобные ключевые пользовательские действия могут выполняться дольше остальных или, наоборот, требовать более короткого времени выполнения, чем в среднем.

Например, предположим, что вы установили глобальный [порог Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") в 3 секунды. Хотя этот порог может быть приемлемым для большинства пользовательских действий, для действия регистрации он может быть неприемлемым. Или же может существовать действие поиска, достаточно сложное, чтобы требовать больше отведённых 3 секунд.

Вы можете пометить пользовательское действие как ключевое и настроить рейтинг Apdex для ключевых пользовательских действий в ваших [веб-](/managed/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в веб-приложениях."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в мобильных приложениях.") и [пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в пользовательских приложениях.").

## Связанные темы

* [Создание пользовательских имён для действий пользователей в веб-приложениях](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Настройте автоматически генерируемые имена пользовательских действий для ваших веб-приложений.")
* [Создание пользовательских имён для действий пользователей в мобильных приложениях](/managed/observe/digital-experience/mobile-applications/additional-configuration/naming-rules-mobile "Настройте автоматически генерируемые имена пользовательских действий для ваших мобильных приложений.")
* [Создание пользовательских имён для действий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Настройте автоматически генерируемые имена пользовательских действий для ваших пользовательских приложений.")
* [Настройка ключевых пользовательских действий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в веб-приложениях.")
* [Настройка ключевых пользовательских действий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в мобильных приложениях.")
* [Настройка ключевых пользовательских действий для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Обозначьте действие как ключевое и настройте рейтинг Apdex для ключевых действий в пользовательских приложениях.")