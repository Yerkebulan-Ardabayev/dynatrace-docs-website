---
title: Анализ пользовательских сеансов в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions
---

# Анализ пользовательских сеансов в RUM Classic

# Анализ пользовательских сеансов в RUM Classic

* Практическое руководство
* Чтение за 21 минуту
* Обновлено 12 окт. 2023 г.

Dynatrace версия 1.224+

Хотя анализ отдельных пользовательских сеансов может быть полезен в некоторых ситуациях, такой анализ зачастую неполный. Пользователи приложения ведут себя непредсказуемо, выполняют разные задачи с разными целями, находятся в разных географических регионах и используют бесчисленные комбинации устройств, операционных систем и браузеров.

Dynatrace поддерживает сегментацию пользовательских сеансов с помощью мощного механизма фильтрации. Анализ пользовательских сеансов Dynatrace позволяет разбивать, группировать и комбинировать пользовательские сеансы приложения в осмысленные сегменты на основе общих характеристик отдельных пользовательских сеансов: операционной системы, типа браузера, местоположения или тега пользователя. Например, можно сегментировать анализ по следующим типам браузеров: настольный, мобильный или синтетический. Таким образом можно глубоко погружаться в агрегированные результаты, чтобы находить значимые сведения о проблемах производительности, с которыми может сталкиваться лишь небольшая часть пользователей.

## Анализ пользовательского сеанса

Как проанализировать пользовательскую сессию

1. Перейти в **Session Segmentation**.
2. Нажать на текстовое поле в верхней части страницы (см. **1** на примере ниже) и выбрать один из доступных атрибутов фильтрации.
   После выбора атрибута отображается список доступных для этого фильтра значений.

   ### Доступные атрибуты фильтрации

   | Категория атрибута | Атрибут | Описание |
   | --- | --- | --- |
   | Applications | Application | Выбор названия приложения, которое нужно проанализировать. |
   |  | Application type | Указывает, нужно ли анализировать сессии веб-, мобильных или пользовательских приложений. |
   |  | Browser monitor | Выбор названия [browser monitor](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site."), используемого для Synthetic Monitoring. |
   | Browser | Browser type | Фильтрация сессий по тому, были ли они выполнены с помощью десктопного, планшетного или мобильного браузера, или виртуально через synthetic-агент или ботов. |
   |  | Browser family | Фильтрация сессий по использованному браузеру. |
   |  | Browser version | Использовать этот атрибут, чтобы фильтровать сессии не только по конкретному браузеру, но и по конкретной версии браузера. |
   |  | Screen width | Фильтрация пользовательских сессий по конкретной ширине экрана. |
   |  | Screen height | Фильтрация пользовательских сессий по конкретной высоте экрана. |
   | Operating system | Operating system family | Фильтрация сессий по семейству операционной системы (Windows, Linux, iOS и т. д). |
   |  | Operating system version | Выбор конкретной версии ОС. |
   | Location | Continent | Фильтрация сессий по континенту, с которого они происходят. |
   |  | Country | Фильтрация сессий по стране, из которой они происходят. |
   |  | Region | Фильтрация сессий по географическому региону, из которого они происходят. |
   |  | City | Фильтрация сессий по городу, из которого они происходят. |
   | Mobile | Application version | Использовать этот фильтр для просмотра сессий конкретной версии мобильного приложения. |
   |  | Crashes | Выбор `Yes` или `No` для фильтрации сессий, в которых произошёл или не произошёл [crash](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."). |
   |  | Device | Фильтрация сессий по типу мобильного устройства, использованного для доступа к приложению. |
   |  | Manufacturer | Фильтрация пользовательских сессий по конкретному производителю мобильного устройства. |
   |  | Rooted or jailbroken | Выбор `Yes` или `No` для фильтрации мобильных сессий, в которых устройство рутовано/джейлбрейкнуто или является подлинным. Если статус устройства неизвестен или не определён, сессии получают значение `null` и не отображаются в результатах. Пользовательские приложения всегда сообщают неизвестный или не определённый статус. |
   | User | User tag | Выбор [user tag](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") для анализа сессий конкретного пользователя. |
   |  | Internal user ID | Фильтрация сессий по уникальному ID пользователя, инициировавшего пользовательскую сессию. |
   |  | User type | Выбор, нужно ли анализировать пользовательские сессии роботов, synthetic-пользователей или реальных пользователей. |
   |  | New user | Выбор `Yes` или `No` для фильтрации сессий по тому, являются ли пользователи новыми или вернувшимися. |
   | Session | Live | Выбор `Yes` или `No` для отображения [live или завершённых](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#live-vs-completed-user-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") сессий. |
   |  | Session Replay Classic | Выбор `Yes` или `No` для отображения пользовательской сессии с [Session Replay Classic](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") или без него. |
   |  | Bounced | Выбор `Yes` или `No` для фильтрации сессий, которые были или не были отказными (bounced sessions, это сессии, которые немедленно покидаются). Отказ, это особый тип пользовательской сессии, состоящий только из одного пользовательского действия. Высокий показатель отказов нежелателен. |
   |  | Converted | Выбор `Yes` или `No` для анализа тех пользовательских сессий, в которых была или не была достигнута связанная цель конверсии. |
   |  | Session conversion count | Фильтрация сессий по количеству раз, когда сессия достигает любой из целей конверсии сессии. |
   |  | Conversion goal | Выбор конкретной цели конверсии для изучения тех пользовательских сессий, в которых эта цель была достигнута. |
   |  | Has errors | Выбор `Yes` или `No` для явной фильтрации сессий, в которых были или не были обнаружены ошибки. |
   |  | Error count | Указание диапазона количества ошибок. Используется для того, чтобы сосредоточиться на пользовательских сессиях, в которых ошибок больше определённого числа (если оставить верхнюю границу пустой), меньше или равно значению (если оставить нижнюю границу пустой), или которые попадают в конкретный диапазон значений. |
   |  | Error type | Указание, нужно ли анализировать сессии с request-, reported-, custom- или JavaScript-ошибками. |
   |  | IP | Фильтрация сессий по IP-адресам. |
   |  | IPS | Фильтрация сессий по конкретному интернет-провайдеру. |
   |  | Duration | Указание длительности сессии в минутах. Используется для фильтрации сессий длительностью больше или равной значению (если оставить верхнюю границу пустой), меньше или равной значению (если оставить нижнюю границу пустой), или попадающих в конкретный диапазон значений. |
   | Session properties | Session date properties | Фильтрация пользовательских сессий по конкретному [свойству](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.") даты сессии и его значению. |
   |  | Session double properties | Фильтрация пользовательских сессий по конкретному double-свойству сессии и его значению. |
   |  | Session long properties | Фильтрация пользовательских сессий по конкретному long-свойству сессии и его значению. |
   |  | Session string properties | Фильтрация пользовательских сессий по конкретному строковому свойству сессии и его значению. |
   | User actions | User action count | Указание диапазона целых чисел, представляющих количество пользовательских действий, выполненных в рамках одной сессии. Это помогает выявить, например, сессии с большим количеством действий. |
   |  | User action name | Указание пользовательского действия, чтобы можно было анализировать все сессии, включающие хотя бы один экземпляр этого действия. |
   |  | User action date properties | Фильтрация пользовательских сессий по конкретному [свойству](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.") даты пользовательского действия и его значению. |
   |  | User action double properties | Фильтрация пользовательских сессий по конкретному double-свойству пользовательского действия и его значению. |
   |  | User action string properties | Фильтрация пользовательских сессий по конкретному строковому свойству пользовательского действия и его значению. |
   |  | User action long properties | Фильтрация пользовательских сессий по конкретному long-свойству пользовательского действия и его значению. |
   | Pages | Page name | Отображение сессий, в которых пользователь заходил на указанную страницу. |
   |  | Page group | Отображение сессий, в которых пользователь заходил на страницу из указанной группы страниц. |
   | Usability | Rage click count | Указание диапазона количества [rage click](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."). Используется для того, чтобы сосредоточиться на пользовательских сессиях, в которых rage click больше определённого числа (если оставить верхнюю границу пустой), меньше или равно значению (если оставить нижнюю границу пустой), или которые попадают в конкретный диапазон значений. |
   |  | User experience score | Отображение пользовательских сессий с [user experience score](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") Satisfying, Tolerable или Frustrating. |
   |  | Rage tap count | Указание диапазона количества [rage tap](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."). Используется для того, чтобы сосредоточиться на мобильных пользовательских сессиях, в которых rage tap больше определённого числа (если оставить верхнюю границу пустой), меньше или равно значению (если оставить нижнюю границу пустой), или которые попадают в конкретный диапазон значений. |

   В фильтрах оператор тильда (`~`) не работает как ключевое слово `LIKE` в [USQL](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
3. Выбрать интересующее значение атрибута. Некоторые атрибуты предоставляют текстовые поля, которые можно использовать для свободного текстового поиска. Также можно выбрать несколько значений одного атрибута, это работает как оператор `OR` для этого атрибута.
4. Повторить процесс для всех интересующих атрибутов. После определения фильтра нажать в любом месте за пределами текстового поля.

Результат заданных фильтров выдаёт список первых 500 сессий, упорядоченных по времени начала новейшей сессии. Чтобы изменить порядок, отсортировать столбцы таблицы по возрастанию или убыванию.
5. Выбрать метку времени сессии (см. **3** на примере ниже), чтобы перейти на страницу деталей пользовательской сессии. Либо, чтобы проанализировать сессии одного пользователя, выбрать имя пользователя (см. **2** на примере ниже), чтобы перейти на [страницу деталей этого пользователя](/managed/observe/digital-experience/rum-classic/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

![User sessions page](https://dt-cdn.net/images/new-user-sessions-page-3342-dd45c41c38.png)

User sessions page

Использовать [селектор периода времени](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") в строке меню, чтобы настроить период анализа пользовательских сессий.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

Timeframe selector: menu bar

Элементы управления селектора периода времени

Глобальный селектор периода времени служит фильтром времени, который в большинстве случаев позволяет выбрать конкретный период анализа, сохраняющийся на всех страницах и представлениях продукта при переходах в рамках анализа.

![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

Timeframe selector: presets

* Вкладка **Presets** содержит список всех доступных стандартных периодов времени. Выбор одного из них меняет период на выбранный пресет.
* Вкладка **Custom** показывает календарь. Нужно щёлкнуть по дню начала, щёлкнуть по дню окончания, а затем выбрать **Apply**, чтобы задать этот диапазон дней как период времени.

  + Выбранные интервалы календаря устанавливаются с окончанием в начале следующего дня (время задаётся как `00:00`). Например, если в календаре выбраны 3 сентября и 4 сентября, период начинается 3 сентября в `00:00` и заканчивается **5** сентября в `00:00`, чтобы не упустить последнюю минуту временного диапазона. Отображаемое время можно редактировать.
* Вкладка **Recent** показывает недавно использованные периоды времени. Выбор одного из них возвращает к этому периоду.
* Элементы управления **<** и **>** сдвигают временной диапазон вперёд или назад во времени. Шаг сдвига равен длине исходного временного диапазона. Например, если текущий диапазон это `Last 2 hours` (двухчасовой диапазон, заканчивающийся сейчас), выбор **<** сдвигает диапазон на два часа назад, до `-4h to -2h` (двухчасовой диапазон, закончившийся два часа назад).
* Наведение курсора на период времени показывает время начала, продолжительность и время окончания.

  ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

  Timeframe selector: hover

Выражения селектора периода времени

При выборе текущего периода времени в строке меню отображается редактируемое выражение периода времени.

* При чтении слева направо выражение периода времени содержит время начала, оператор `to` и время окончания.
* Если явное время окончания не указано, подразумеваются `to` и `now`. Например, `-2h` то же самое, что `-2h to now`.
* Поддерживаемые единицы: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (можно также использовать целые слова, такие как `minutes` и `quarter`)

| **Примеры выражений периода времени** | **Значение** |
| --- | --- |
| `today` | От начала сегодняшнего дня до начала завтрашнего дня. |
| `yesterday` | От начала вчерашнего дня до начала сегодняшнего дня. Аналогично `-1d/d to today`. |
| `yesterday to now` | От начала вчерашнего дня до текущего времени сегодня. |
| `previous week` | Предыдущие семь полных дней. Если сегодня понедельник, диапазон составит с предыдущего понедельника по предыдущее воскресенье (вчера). |
| `this year` | Текущий календарный год, с 1 января этого года в `00:00` по 1 января следующего года в `00:00`. |
| `last 6 weeks` | Последние 42 дня (6 недель * 7 дней), заканчивающиеся сейчас. Эквивалентно `-6w to now`. |
| `-2h` | От 2 часов (120 минут) назад до текущего времени (`now` подразумевается). Эквивалентно `Last 2 hours` и `-2h to now`. |
| `-4d to -1h30m` | От 4 дней (96 часов) назад до 1,5 часов назад. |
| `-1w` | Последние 7 дней (168 часов), от этого времени 7 дней назад до текущего времени (`now`). Эквивалентно `-7d` и `-168h`. |
| `-1w/w` | От начала предыдущей календарной недели до текущего времени (now).  * При использовании `-1w/w` в пятницу днём в 15:00 получится диапазон длиной 11 дней 15 часов, начинающийся с начала предыдущего понедельника, так как `/w` округляет вниз до начала недели. * При использовании `-1w` без `/w` в пятницу днём в 15:00 время начала будет ровно на 7 дней (168 часов) раньше: предыдущая пятница в 15:00.  В целом, `/` в сочетании с единицей (такой как `/d`, `/w`, `/M` и `/y`) означает округление даты или времени вниз до начала указанной единицы времени. Например, `-3d` означает ровно 72 часа назад, тогда как `-3d/d` означает три дня назад с округлением вниз до ближайшего дня (начиная с времени `00:00`, начала дня). Используй `now/d` для обозначения начала сегодняшнего дня. |
| `-1w/w + 8h` | Начиная с начала прошлой недели плюс 8 часов (8:00 утра понедельника).  * Обрати внимание, что операторы `+` и `-` можно использовать с единицами, метками времени и `now`. |
| `-1d/d+9h00m to -1d/d+17h00m` | Рабочие часы вчера, с 09:00 до 17:00 (с 9 утра до 5 вечера). |
| `2020-08-16 21:28 to 2020-08-19 10:02` | Абсолютный диапазон, состоящий из абсолютных дат и времени начала и окончания в формате `YYYY-MM-DD hh:mm`.  * Если указана дата, но время опущено (например, просто `2020-08-16`), время считается началом дня (`00:00`) * Если указано время, но дата опущена (например, просто `21:28`), датой считается сегодняшний день |
| `1598545932346 to 1598837052346` | Метки времени Unix epoch в миллисекундах. |

Пользовательские сессии, которые [активны](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#live-vs-completed-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") в период времени, заданный в селекторе периода времени, показываются в списке сессий. **Analysis over time** [finding](#drill-down-using-findings), напротив, показывает только те сессии, которые начались в заданный период времени.

Например, если период времени задан как 12:00–12:05, а сессия, начавшаяся в 11:55, всё ещё активна в течение этого периода, эта сессия показывается в списке сессий, но не учитывается для **Analysis over time** finding. Это происходит потому, что сессия началась до заданного периода времени.

## Углублённый анализ с помощью findings

Панель findings расположена слева на странице **User sessions**. Эта панель содержит готовые findings и различные визуализации для разных атрибутов. Например, выбор категории **Application versions** покажет, у какой версии приложения больше пользовательских сессий, а выбор категории **Applications** покажет данные по агрегированным сессиям для каждого из приложений.

![Mobile application versions on the User sessions page](https://dt-cdn.net/images/user-seesions-mobile-app-versions-1635-29a25ad4eb.png)

Версии мобильного приложения на странице User sessions

![Findings panel on the new user sessions page](https://dt-cdn.net/images/findings-panel-on-the-new-user-sessions-page-3342-e11184615c.png)

Панель findings на новой странице user sessions

## Фокус на сессиях отдельного пользователя

Можно сфокусироваться на пользовательских сессиях конкретного пользователя. Выбор пользователя в столбце **User** переводит на [страницу обзора пользователя](/managed/observe/digital-experience/rum-classic/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

Чтобы найти пользовательские сессии конкретного пользователя, выбери [**User tag**](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") в поле **Filter by**, а затем выбери нужного пользователя. Например, чтобы отобразить пользовательские сессии пользователя `Zara`, добавь фильтр **User tag:** `Zara`. Затем выбери **Zara** в столбце **User**, чтобы перейти на страницу обзора этого пользователя.

![User sessions of a particular user](https://dt-cdn.net/images/user-sessions-of-a-particulra-user-2460-63bd6314da.png)

Пользовательские сессии конкретного пользователя

Чтобы узнать, как присвоить каждому пользователю приложения уникальное имя пользователя, ознакомься со следующими страницами в зависимости от типа приложения и операционной системы:

* [Веб-приложения](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.")
* Мобильные приложения

  + [Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
  + [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
  + [Cordova﻿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user)
  + [Flutter﻿](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser)
  + [React Native﻿](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user)
  + [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user "Monitor Xamarin apps with Dynatrace OneAgent.")
  + [.NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui#identify-user "Monitor .NET MAUI applications with Dynatrace OneAgent.")
* [Пользовательские приложения: OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users "Read how Dynatrace OpenKit can be used from the developer's point of view.")

Выбери одну из сессий пользователя `Zara`, чтобы посмотреть дополнительные детали. Например, можно проверить все действия, которые пользователь `Zara` выполнил в течение выбранной сессии. Детали сессии содержат важную информацию об устройстве, такую как разрешение устройства, производитель, операционная система, геолокация и IP-адрес.

![User session details page](https://dt-cdn.net/images/usmobile2-1-1438-7fd0911d36.png)

Страница деталей пользовательской сессии

## Просмотр деталей ошибок

Анализ сессий также можно использовать, чтобы получить детали [ошибок](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), возникающих в приложении.

Чтобы открыть страницу деталей ошибки

1. Перейди в **Session Segmentation**.
2. В поле **Filter by** установи **Error type** в одно из следующих значений в зависимости от типа приложения:

   | Error type | Description | Web | Mobile | Custom |
   | --- | --- | --- | --- | --- |
   | Request error | Обнаруживается браузером и OneAgent на серверах | Applicable | Applicable | Applicable |
   | Reported error | Сообщается вручную через выделенный метод "report an error" API | Not applicable | Applicable | Applicable |
   | Custom error | Сообщается вручную через RUM JavaScript API | Applicable | Not applicable | Not applicable |
   | JavaScript error | Исключения JavaScript, выбрасываемые браузером | Applicable | Not applicable | Not applicable |
3. Выбери интересующую пользовательскую сессию, чтобы открыть страницу деталей сессии.
4. В разделе **Events and actions** разверни действие пользователя, содержащее ошибку, и выбери **Perform waterfall analysis**.
5. Выполни одно из следующих действий в зависимости от типа приложения:

   * Веб-приложения На странице **Waterfall analysis** выбери плитку **Error**, а затем выбери ошибку. Откроется страница деталей ошибки.
   * Мобильные и пользовательские приложения Прокрути вниз до раздела **Web request errors** или **Reported errors** и выбери ошибку. Откроется страница деталей ошибки.

#### Страница деталей ошибки

Страница деталей ошибки предоставляет ценную информацию об ошибках приложения.

Страница деталей ошибки веб-запроса

Страница деталей сообщённой ошибки

![Web request error details page](https://dt-cdn.net/images/web-request-error-details-page-1772-928bb94d69.png)

Страница деталей ошибки веб-запроса

![Reported error details page](https://dt-cdn.net/images/reported-error-details-page-new-1644-60289f33a5.png)

Страница деталей сообщённой ошибки

На ней отображаются такие детали ошибки, как оценочное количество ошибок, провайдер (для ошибки запроса), технология (для сообщённой ошибки) и другие. Страница также перечисляет затронутые пользовательские сессии и затронутые действия пользователя, выбор действия пользователя или пользовательской сессии открывает её детали. Разбивка по распределению показывает информацию об относительной частоте операционных систем, версий ОС, версий приложения и устройств, а разбивка по странам показывает все затронутые страны и соответствующий им уровень ошибок.

## Проверка сессий с rage-событиями

Когда приложение не реагирует быстро, текстовая метка выглядит как кнопка, или переключатель скрыт под другим переключателем, пользователи могут раздражённо повторно нажимать или тапать по затронутому элементу интерфейса. Dynatrace распознаёт такое поведение как [rage-событие](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."): **rage click** или **rage tap**.

Чтобы просмотреть пользовательские сессии с rage-событиями

1. Перейди в **Session Segmentation**.
2. Установи **Filter by** в **Rage click count:** `≥1` или **Rage tap count:** `≥1`.
3. Выбери интересующую пользовательскую сессию, чтобы открыть страницу деталей сессии.
4. Прокрути вниз до раздела **Events and actions** и разверни событие rage click или rage tap, чтобы посмотреть его детали.

## Изучение сбоев

Мобильные и пользовательские приложения

Когда сессия пользователя завершается [сбоем](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."), можно использовать анализ сессий, чтобы просмотреть полную последовательность действий пользователя, предшествовавших сбою. Также можно открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро проследить первопричины этого сбоя.

1. Перейти в **Session Segmentation**.
2. Установить **Filter by** со следующими фильтрами:

   * **Application type:** `Mobile`, чтобы отобразить только мобильные пользовательские сессии, или **Application type:** `Custom`, чтобы получить пользовательские сессии, зафиксированные в пользовательских приложениях
   * **Crashes:** `Yes`, чтобы показать сессии, завершившиеся сбоем
   * Mobile applications **Session Replay Classic:** `Yes`, чтобы отобразить сессии, записанные с помощью Session Replay Classic при сбоях для приложений [Android](/managed/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay Classic for your Android apps to learn which actions your users perform.") или [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.")
3. Выбрать интересующую пользовательскую сессию, чтобы открыть страницу с её деталями.
4. Mobile applications Чтобы посмотреть запись Session Replay Classic, перейти на вкладку **Session Replay** и выбрать **Play** ![Replay](https://dt-cdn.net/images/replay-button-optimized-41ad05863e.svg "Replay").  
   Последнее событие сессии, это сбой, который отображается красной точкой на временной шкале. Использовать элементы управления Session Replay Classic для детального анализа сбоя.

   ![Mobile user session with Session Replay Classic](https://dt-cdn.net/images/mobile-user-session-with-session-replay-2134-d486b7d1b9.png)

   Mobile user session with Session Replay Classic
5. Чтобы просмотреть все действия и события пользователя, предшествовавшие сбою, прокрутить вниз до раздела **Events and actions**.
6. Чтобы просмотреть отчёт о сбое, развернуть событие сбоя, а затем выбрать **Open crash details**.  
   Отчёт о сбое предоставляет информацию об устройстве пользователя и трассировку стека. Также можно проанализировать группы сбоев для [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/crash-reports-mobile#crash-groups "Check the latest crash reports for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/crash-reports-custom#crash-groups "Check the latest crash reports for your custom applications.") или скачать трассировку стека сбоя.

   ![Opening the mobile crash report](https://dt-cdn.net/images/open-mobile-crash-details-2132-311049ce33.png)

   Opening the mobile crash report

## Анализ одной сессии в разных доменах

По техническим и security-причинам нельзя анализировать одну пользовательскую сессию в разных доменах.

Допустим, пользователь в рамках одной «сессии» посещает два совершенно разных домена. Как Dynatrace зафиксирует это, учитывая, что оба домена инструментированы Dynatrace?

На самом деле будут видны две отдельные пользовательские сессии:

1. Первая сессия начинается с загрузки страницы первого домена и завершается, когда пользователь переходит по ссылке на страницу другого домена (второго домена).
2. Вторая сессия начинается с первой загрузки страницы на втором домене и завершается при выполнении любого из [критериев завершения пользовательской сессии](#user-session-end).

Это происходит по следующим причинам:

* **Техническая причина**: cookie нельзя передавать между доменами, за исключением поддоменов.
* **Security-причина**: это функция безопасности браузеров и ограничение, общее для всех вендоров.

## Анализ в реальном времени

* Получить доступ к живым пользовательским сессиям через плитку **Live user activity** на дашборде.

![Live user activity](https://dt-cdn.net/images/live-user-activity-1567-1df03a6ae5.png)

Live user activity

* Перейти на одну из страниц проблем и выбрать **See user sessions sample**.

![Problem details page](https://dt-cdn.net/images/user-sessions-problems-pages-1635-7fb715b445.png)

Problem details page

* Затронутые сессии также можно открыть напрямую с одной из страниц проблем.

![User sessions affected by a problem](https://dt-cdn.net/images/user-sessions-from-problems-pages-to-sessions-page-1634-805c05bb34.png)

User sessions affected by a problem

* Для завершённых пользовательских сессий доступны отказы (bounces) и конверсии.

![Conversions and bounces on the User sessions page](https://dt-cdn.net/images/user-sessions-conversions-and-bounces-1639-f3a0e84129.png)

Conversions and bounces on the User sessions page

## Примеры

Эти примеры показывают, как можно получить представление о поведении пользователей с помощью анализа пользовательских сессий Dynatrace.

Фильтрация пользовательских сессий по длительности сессии

Пользовательские сессии можно фильтровать по длительности: длиннее или короче определённого значения либо в заданном диапазоне. На скриншоте ниже показаны пользовательские сессии длительностью не менее 10 секунд.

![Filter user sessions based on user session duration](https://dt-cdn.net/images/image005-2550-69ae07a8ad.png)

Filter user sessions based on user session duration

Поиск всех пользовательских сессий, включающих хотя бы один экземпляр определённых действий пользователя

Можно найти все пользовательские сессии, которые включают хотя бы один экземпляр любого из нескольких действий пользователя в их clickpath.

![Search for user sessions with specific user actions](https://dt-cdn.net/images/image007-2550-ced4628b80.png)

Search for user sessions with specific user actions

Создание сложных фильтров

Посмотреть панель фильтров в примере ниже. Этот поиск находит пользовательские сессии, соответствующие следующим критериям:

* **Application type: Web** и **Browser Type: Desktop Browser**. Пользователь обратился к одному из веб-приложений через desktop-браузер.
* **Duration 60s**. Сессия длилась не менее 1 минуты.
* **Action count = 5**. За время сессии пользователь выполнил пять действий.
* **User action name: test**. В пользовательской сессии произошло пользовательское действие с именем `test`.

![Create complex filters](https://dt-cdn.net/images/image009-2550-759db59a94.png)

Create complex filters

Изучение категорий на панели находок

Для каждой категории на панели находок есть отдельный раздел, показывающий визуализации и находки по этой конкретной категории. Например, **Application type** показывает текущее распределение, распределение во времени и географическое распределение разных типов приложений. Географическая карта показывает цветом тип приложения с наибольшим количеством сессий.

![Application type category view](https://dt-cdn.net/images/image011-2122-def628c232.png)

Application type category view

Можно выбрать любую из находок и легко применить её, выбрав **Apply selection as a filter** в нижнем левом углу страницы.

![Apply current category as a filter](https://dt-cdn.net/images/image013-2540-899b1a7298.png)

Apply current category as a filter

## Связанные темы

* [Пользовательские сессии в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* [Эффективная поддержка клиентов с помощью session segmentation](/managed/observe/digital-experience/dem-use-cases/customer-support-with-session-segmentation "Learn how to resolve customer complaints using session segmentation.")