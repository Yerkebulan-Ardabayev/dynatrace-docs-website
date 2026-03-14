---
title: Новинка: Анализ пользовательских сессий
source: https://www.dynatrace.com/docs/observe/digital-experience/session-segmentation/new-user-sessions
scraped: 2026-03-02T21:18:42.759294
---

# Новинка: Анализ пользовательских сессий


* How-to guide
* 21-min read
* Updated on Oct 12, 2023

Dynatrace версия 1.224+

Хотя анализ отдельных пользовательских сессий может быть полезен в некоторых ситуациях, такой анализ зачастую неполный. Пользователи вашего приложения ведут себя непредсказуемо, выполняют разные задачи с разными целями, находятся в различных географических регионах и используют бесчисленное множество комбинаций устройств, операционных систем и браузеров.

Dynatrace поддерживает сегментацию пользовательских сессий с помощью мощного механизма фильтрации. Анализ пользовательских сессий Dynatrace позволяет делить, группировать и объединять пользовательские сессии вашего приложения в значимые сегменты на основе общих характеристик отдельных сессий — операционной системы, типа браузера, местоположения или пользовательского тега. Например, вы можете сегментировать анализ по следующим типам браузеров: десктопный, мобильный или синтетический. Таким образом, вы можете глубоко исследовать агрегированные результаты и находить значимые сведения о проблемах с производительностью, которые могут быть характерны только для небольшой части ваших пользователей.

## Анализ пользовательской сессии

Чтобы проанализировать пользовательскую сессию

1. Перейдите в раздел ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Нажмите на текстовое поле в верхней части страницы (см. **1** на примере ниже) и выберите один из доступных атрибутов фильтрации.
   После выбора атрибута в списке отображаются доступные значения для этого фильтра.

   ### Доступные атрибуты фильтрации

   | Категория атрибута | Атрибут | Описание |
   | --- | --- | --- |
   | Приложения | Application | Выберите имя приложения, которое хотите проанализировать. |
   |  | Application type | Укажите, хотите ли вы анализировать сессии веб-, мобильных или пользовательских приложений. |
   |  | Browser monitor | Выберите имя [монитора браузера](../synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor.md "Learn how to set up a single-URL browser monitor to check the availability of your site."), используемого для синтетического мониторинга. |
   | Браузер | Browser type | Фильтруйте сессии в зависимости от того, использовался ли десктопный, планшетный или мобильный браузер, либо виртуальный через синтетического агента или ботов. |
   |  | Browser family | Фильтруйте сессии по используемому браузеру. |
   |  | Browser version | Используйте этот атрибут, если хотите фильтровать сессии не только по конкретному браузеру, но и по его версии. |
   |  | Screen width | Фильтруйте пользовательские сессии по конкретной ширине экрана. |
   |  | Screen height | Фильтруйте пользовательские сессии по конкретной высоте экрана. |
   | Операционная система | Operating system family | Фильтруйте сессии по семейству операционной системы (Windows, Linux, iOS и т.д.). |
   |  | Operating system version | Выберите конкретную версию ОС. |
   | Местоположение | Continent | Фильтруйте сессии по континенту, откуда они поступают. |
   |  | Country | Фильтруйте сессии по стране, откуда они поступают. |
   |  | Region | Фильтруйте сессии по географическому региону, откуда они поступают. |
   |  | City | Фильтруйте сессии по городу, откуда они поступают. |
   | Мобильные | Application version | Используйте этот фильтр для просмотра сессий для конкретной версии вашего мобильного приложения. |
   |  | Crashes | Выберите `Yes` или `No` для фильтрации сессий, в которых произошёл или не произошёл [сбой](../rum-concepts/user-and-error-events.md#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."). |
   |  | Device | Фильтруйте сессии по типу мобильного устройства, используемого для доступа к приложению. |
   |  | Manufacturer | Фильтруйте пользовательские сессии по конкретному производителю мобильного устройства. |
   |  | Rooted or jailbroken | Выберите `Yes` или `No` для фильтрации мобильных сессий, где устройство рутировано/взломано или нет. Если статус устройства неизвестен или не определён, сессии имеют значение `null` и не отображаются в результатах. Пользовательские приложения всегда сообщают о неизвестном или неопределённом статусе. |
   | Пользователь | User tag | Выберите [пользовательский тег](../rum-concepts/user-and-error-events.md#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") для анализа сессий конкретного пользователя. |
   |  | Internal user ID | Фильтруйте сессии по уникальному идентификатору пользователя, инициировавшего пользовательскую сессию. |
   |  | User type | Выберите, хотите ли вы анализировать пользовательские сессии роботов, синтетических пользователей или реальных пользователей. |
   |  | New user | Выберите `Yes` или `No` для фильтрации сессий в зависимости от того, являются ли пользователи новыми или вернувшимися. |
   | Сессия | Live | Выберите `Yes` или `No`, чтобы отображать [активные или завершённые](../rum-concepts/user-session.md#live-vs-completed-user-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") сессии. |
   |  | Session Replay | Выберите `Yes` или `No` для отображения пользовательских сессий с [Session Replay](../session-replay.md "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") или без него. |
   |  | Bounced | Выберите `Yes` или `No` для фильтрации сессий, которые были или не были отказными (отказные сессии — это сессии, от которых немедленно отказались). Отказ — это особый тип пользовательской сессии, состоящий всего из одного действия. Высокий показатель отказов нежелателен. |
   |  | Converted | Выберите `Yes` или `No` для анализа пользовательских сессий, в которых связанная цель конверсии была или не была достигнута. |
   |  | Session conversion count | Фильтруйте сессии по количеству раз, когда сессия достигает любой из целей конверсии. |
   |  | Conversion goal | Выберите конкретную цель конверсии для анализа пользовательских сессий, где эта цель была достигнута. |
   |  | Has errors | Выберите `Yes` или `No` для явной фильтрации сессий, в которых произошли или не произошли ошибки. |
   |  | Error count | Укажите диапазон числа ошибок. Используйте это для фильтрации сессий с более чем определённым числом ошибок (если оставить верхнюю границу пустой), меньше или равным значению (если оставить нижнюю границу пустой) или в определённом диапазоне. |
   |  | Error type | Укажите, хотите ли вы анализировать сессии с ошибками запросов, сообщёнными, пользовательскими или JavaScript-ошибками. |
   |  | IP | Фильтруйте сессии по IP-адресам. |
   |  | IPS | Фильтруйте сессии по конкретному интернет-провайдеру. |
   |  | Duration | Укажите продолжительность сессии в минутах. Используйте это для фильтрации сессий с продолжительностью больше или равной значению (если оставить верхнюю границу пустой), меньше или равной значению (если оставить нижнюю границу пустой) или в определённом диапазоне. |
   | Свойства сессий | Session date properties | Фильтруйте пользовательские сессии по конкретному свойству даты сессии ([property](../web-applications/additional-configuration/define-user-action-and-session-properties.md "Define custom string, numeric, and date properties for your monitored web applications.")) и его значению. |
   |  | Session double properties | Фильтруйте пользовательские сессии по конкретному свойству типа double и его значению. |
   |  | Session long properties | Фильтруйте пользовательские сессии по конкретному свойству типа long и его значению. |
   |  | Session string properties | Фильтруйте пользовательские сессии по конкретному строковому свойству и его значению. |
   | Действия пользователя | User action count | Укажите диапазон целых чисел, представляющих количество действий пользователя в рамках одной сессии. Это помогает, например, выявлять сессии с большим числом действий. |
   |  | User action name | Укажите действие пользователя для анализа всех сессий, включающих хотя бы один экземпляр этого действия. |
   |  | User action date properties | Фильтруйте пользовательские сессии по конкретному свойству даты действия пользователя ([property](../web-applications/additional-configuration/define-user-action-and-session-properties.md "Define custom string, numeric, and date properties for your monitored web applications.")) и его значению. |
   |  | User action double properties | Фильтруйте пользовательские сессии по конкретному свойству типа double действия пользователя и его значению. |
   |  | User action string properties | Фильтруйте пользовательские сессии по конкретному строковому свойству действия пользователя и его значению. |
   |  | User action long properties | Фильтруйте пользовательские сессии по конкретному свойству типа long действия пользователя и его значению. |
   | Страницы | Page name | Отображайте сессии, в которых пользователь обращался к указанной странице. |
   |  | Page group | Отображайте сессии, в которых пользователь обращался к странице из указанной группы страниц. |
   | Удобство использования | Rage click count | Укажите диапазон числа [кликов в ярости](../rum-concepts/user-and-error-events.md#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."). Используйте это для фильтрации сессий с более чем определённым числом кликов в ярости (если оставить верхнюю границу пустой), меньше или равным значению (если оставить нижнюю границу пустой) или в определённом диапазоне. |
   |  | User experience score | Отображайте пользовательские сессии с оценкой пользовательского опыта «Удовлетворительно», «Терпимо» или «Неприемлемо» ([user experience score](../rum-concepts/scores-and-ratings/user-experience-score.md "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.")). |
   |  | Rage tap count | Укажите диапазон числа [нажатий в ярости](../rum-concepts/user-and-error-events.md#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."). Используйте это для фильтрации мобильных пользовательских сессий с более чем определённым числом нажатий в ярости (если оставить верхнюю границу пустой), меньше или равным значению (если оставить нижнюю границу пустой) или в определённом диапазоне. |

   В фильтрах оператор тильды (`~`) работает не так, как ключевое слово `LIKE` в [USQL](custom-queries-segmentation-and-aggregation-of-session-data.md "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
3. Выберите интересующее вас значение атрибута. Некоторые атрибуты предоставляют текстовые поля для поиска в свободной форме. Также можно выбрать несколько значений одного атрибута; это работает как оператор `OR` для этого атрибута.
4. Повторите этот процесс для всех интересующих вас атрибутов. Определив фильтр, нажмите в любом месте за пределами текстового поля.

   Результат определённых фильтров выдаёт список первых 500 сессий, упорядоченных по времени начала новейшей сессии. Чтобы изменить порядок, отсортируйте столбцы таблицы по возрастанию или убыванию.
5. Выберите временную метку сессии (см. **3** на примере ниже), чтобы перейти на страницу сведений о сессии. Либо, чтобы проанализировать сессии отдельного пользователя, выберите имя пользователя (см. **2** на примере ниже), чтобы перейти на [страницу сведений о пользователе](analyze-all-sessions-of-a-single-user.md "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

![User sessions page](https://dt-cdn.net/images/new-user-sessions-page-3342-dd45c41c38.png)

Используйте [селектор временного диапазона](../../../analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe.md "Learn about Dynatrace dashboard timeframe and management zone settings.") в строке меню для настройки периода анализа пользовательских сессий.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

Элементы управления селектором временного диапазона

Глобальный селектор временного диапазона служит фильтром времени, который в большинстве случаев позволяет выбрать конкретный период анализа, сохраняющийся на всех страницах и представлениях при навигации.

![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

* Вкладка **Presets** содержит список всех стандартных временных диапазонов. Выберите один из них, чтобы установить этот период.
* Вкладка **Custom** отображает календарь. Нажмите на начальный день, затем на конечный день и нажмите **Apply**, чтобы выбрать этот диапазон дней.

  + Выбранные в календаре интервалы устанавливаются так, чтобы заканчиваться в начале следующего дня (со временем `00:00`). Например, если вы выбираете с 3 по 4 сентября, временной диапазон начинается 3 сентября в `00:00` и заканчивается **5** сентября в `00:00`, чтобы вы не пропустили последнюю минуту диапазона. Отображаемое время можно редактировать.
* Вкладка **Recent** отображает недавно использованные временные диапазоны. Выберите один из них, чтобы вернуться к нему.
* Элементы управления **<** и **>** сдвигают диапазон вперёд или назад. Шаг равен длине исходного диапазона. Например, если текущий диапазон — `Last 2 hours` (двухчасовой диапазон, заканчивающийся сейчас), нажмите **<**, чтобы сдвинуть диапазон на два часа назад — к `-4h to -2h`.
* Наведите курсор на временной диапазон, чтобы увидеть время начала, длительность и время окончания.

  ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

Выражения селектора временного диапазона

При выборе текущего временного диапазона в строке меню отображается редактируемое выражение временного диапазона.

* Читая слева направо, выражение временного диапазона содержит время начала, оператор `to` и время окончания.
* Если явное время окончания отсутствует, подразумеваются `to` и `now`. Например, `-2h` эквивалентно `-2h to now`.
* Поддерживаемые единицы: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (можно также использовать полные слова, например `minutes` и `quarter`)

Пользовательские сессии, которые [активны](../rum-concepts/user-session.md#live-vs-completed-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") в течение временного диапазона, заданного в селекторе, отображаются в списке сессий. Находка **Analysis over time** ([findings](#drill-down-using-findings)), напротив, показывает только те сессии, которые начались в рамках заданного временного диапазона.

Например, если временной диапазон установлен с 12:00 до 12:05, а сессия, начавшаяся в 11:55, всё ещё активна в этом диапазоне, она отображается в списке сессий, но не учитывается в находке **Analysis over time**, поскольку она началась до заданного временного диапазона.

## Детализация с помощью находок

Панель находок расположена в левой части страницы **User sessions**. Эта панель содержит стандартные находки и различные визуализации для различных атрибутов. Например, выберите категорию **Application versions**, чтобы увидеть, какая версия приложения имеет больше пользовательских сессий, или категорию **Applications**, чтобы просмотреть данные о агрегированных сессиях для каждого из ваших приложений.

![Mobile application versions on the User sessions page](https://dt-cdn.net/images/user-seesions-mobile-app-versions-1635-29a25ad4eb.png)

![Findings panel on the new user sessions page](https://dt-cdn.net/images/findings-panel-on-the-new-user-sessions-page-3342-e11184615c.png)

## Фокус на сессиях отдельного пользователя

Вы можете сосредоточиться на пользовательских сессиях конкретного пользователя. Выберите пользователя в столбце **User**, чтобы перейти на [страницу обзора этого пользователя](analyze-all-sessions-of-a-single-user.md "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

Для поиска пользовательских сессий конкретного пользователя выберите [**User tag**](../rum-concepts/user-and-error-events.md#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") в поле **Filter by** и выберите нужного пользователя. Например, чтобы отобразить пользовательские сессии пользователя `Zara`, добавьте фильтр **User tag:** `Zara`. Затем выберите **Zara** в столбце **User**, чтобы перейти на страницу обзора этого пользователя.

![User sessions of a particular user](https://dt-cdn.net/images/user-sessions-of-a-particulra-user-2460-63bd6314da.png)

Чтобы узнать, как пометить каждого пользователя вашего приложения уникальным именем, обратитесь к следующим страницам в зависимости от типа приложения и операционной системы:

* [Веб-приложения](../web-applications/additional-configuration/identify-individual-users-for-session-analysis.md "Tag individual users via the JavaScript API for session analysis.")
* Мобильные приложения

  + [Android](../mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md#tag-specific-users "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
  + [iOS](../mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios.md#tag-specific-users "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
  + [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user)
  + [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser)
  + [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user)
  + [Xamarin](../mobile-applications/cross-platform-frameworks/xamarin-nuget.md#identify-user "Monitor Xamarin apps with Dynatrace OneAgent.")
  + [.NET MAUI](../mobile-applications/cross-platform-frameworks/maui.md#identify-user "Monitor .NET MAUI applications with Dynatrace OneAgent.")
* [Пользовательские приложения: OpenKit](../../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md#tag-specific-users "Read how Dynatrace OpenKit can be used from the developer's point of view.")

Выберите одну из сессий `Zara`, чтобы просмотреть дополнительные сведения. Например, можно проверить все действия, выполненные пользователем `Zara` в течение выбранной сессии. Сведения о сессии содержат важную информацию об устройстве, такую как разрешение устройства, производитель, операционная система, геолокация и IP-адрес.

![User session details page](https://dt-cdn.net/images/usmobile2-1-1438-7fd0911d36.png)

## Просмотр сведений об ошибках

Анализ сессий можно также использовать для получения подробной информации об [ошибках](../rum-concepts/user-and-error-events.md#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), возникающих в вашем приложении.

Чтобы перейти на страницу сведений об ошибке

1. Перейдите в раздел ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. В поле **Filter by** установите **Error type** в одно из следующих значений в зависимости от типа приложения:

   | Тип ошибки | Описание | Веб | Мобильные | Пользовательские |
   | --- | --- | --- | --- | --- |
   | Request error | Обнаружена браузером и OneAgent на ваших серверах | Применимо | Применимо | Применимо |
   | Reported error | Сообщена вручную через специальный метод API «report an error» | Неприменимо | Применимо | Применимо |
   | Custom error | Сообщена вручную через RUM JavaScript API | Применимо | Неприменимо | Неприменимо |
   | JavaScript error | Исключения JavaScript, выброшенные браузером | Применимо | Неприменимо | Неприменимо |
3. Выберите интересующую вас пользовательскую сессию, чтобы открыть страницу сведений о сессии.
4. В разделе **Events and actions** разверните действие пользователя, содержащее ошибку, и выберите **Perform waterfall analysis**.
5. Выполните одно из следующих действий в зависимости от типа приложения:

   * Веб-приложения: на странице **Waterfall analysis** выберите плитку **Error** и затем выберите ошибку. Откроется страница сведений об ошибке.
   * Мобильные и пользовательские приложения: прокрутите вниз до раздела **Web request errors** или **Reported errors** и выберите ошибку. Откроется страница сведений об ошибке.

#### Страница сведений об ошибке

Страница сведений об ошибке предоставляет ценную информацию об ошибках вашего приложения.

Страница сведений о ошибке веб-запроса

Страница сведений о сообщённой ошибке

![Web request error details page](https://dt-cdn.net/images/web-request-error-details-page-1772-928bb94d69.png)

![Reported error details page](https://dt-cdn.net/images/reported-error-details-page-new-1644-60289f33a5.png)

На странице отображаются сведения об ошибке, такие как расчётное количество ошибок, провайдер (для ошибки запроса), технология (для сообщённой ошибки) и прочее. Также на странице перечислены затронутые пользовательские сессии и затронутые действия пользователей — выберите действие или сессию, чтобы просмотреть их сведения. В разбивке по распределению отображается информация об относительных частотах операционных систем, версий ОС, версий приложений и устройств, а в разбивке по странам — все затронутые страны и соответствующие показатели частоты ошибок.

## Проверка сессий с событиями ярости

Когда приложение не реагирует быстро, текстовый ярлык выглядит как кнопка или переключатель скрыт под другим переключателем, пользователи могут многократно нажимать или касаться затронутого элемента управления интерфейсом в раздражении. Dynatrace определяет такое поведение как [событие ярости](../rum-concepts/user-and-error-events.md#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."): **rage click** (клик в ярости) или **rage tap** (нажатие в ярости).

Чтобы просмотреть пользовательские сессии с событиями ярости

1. Перейдите в раздел ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Установите **Filter by** в **Rage click count:** `≥1` или **Rage tap count:** `≥1`.
3. Выберите интересующую вас пользовательскую сессию, чтобы открыть страницу сведений о сессии.
4. Прокрутите вниз до раздела **Events and actions** и разверните событие клика или нажатия в ярости, чтобы просмотреть его сведения.

## Анализ сбоев

Мобильные и пользовательские приложения

Когда пользовательская сессия заканчивается [сбоем](../rum-concepts/user-and-error-events.md#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."), анализ сессий можно использовать для просмотра полной последовательности действий пользователя, предшествовавших сбою. Также можно открыть отчёт о сбое, чтобы получить всю информацию на уровне кода и быстро найти первопричины сбоя.

1. Перейдите в раздел ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Установите **Filter by** следующим образом:

   * **Application type:** `Mobile` для отображения только мобильных пользовательских сессий или **Application type:** `Custom` для получения пользовательских сессий из пользовательских приложений
   * **Crashes:** `Yes` для отображения сессий, завершившихся сбоем
   * Мобильные приложения **Session Replay:** `Yes` для отображения сессий, записанных с Session Replay при сбоях для приложений [Android](../session-replay/session-replay-android.md "Set up Session Replay for your Android apps to learn which actions your users perform.") или [iOS](../session-replay/session-replay-ios.md "Prerequisites and the procedure for enabling Session Replay for your iOS apps.")
3. Выберите интересующую вас пользовательскую сессию, чтобы открыть страницу сведений о сессии.
4. Мобильные приложения: для просмотра записи Session Replay перейдите на вкладку **Session Replay** и нажмите **Play** ![Replay](https://dt-cdn.net/images/replay-button-optimized-41ad05863e.svg "Replay").
   Последнее событие сессии — это сбой, отмеченный красной точкой на временной шкале. Используйте элементы управления Session Replay для детального анализа сбоя.

   ![Mobile user session with Session Replay](https://dt-cdn.net/images/mobile-user-session-with-session-replay-2134-d486b7d1b9.png)
5. Чтобы просмотреть все действия и события пользователя, предшествовавшие сбою, прокрутите вниз до раздела **Events and actions**.
6. Чтобы просмотреть отчёт о сбое, разверните событие сбоя и выберите **Open crash details**.
   Отчёт о сбое предоставляет информацию об устройстве пользователя и трассировку стека. Также можно анализировать группы сбоев для [мобильных](../mobile-applications/analyze-and-use/crash-reports-mobile.md#crash-groups "Check the latest crash reports for your mobile applications.") и [пользовательских приложений](../custom-applications/analyze-and-use/crash-reports-custom.md#crash-groups "Check the latest crash reports for your custom applications.") или скачать трассировку стека сбоя.

   ![Opening the mobile crash report](https://dt-cdn.net/images/open-mobile-crash-details-2132-311049ce33.png)

## Анализ одной сессии на разных доменах

По техническим и соображениям безопасности невозможно анализировать одну пользовательскую сессию на разных доменах.

Предположим, ваш пользователь посещает два совершенно разных домена в рамках одной «сессии». Как Dynatrace зафиксирует это, если оба домена инструментированы с помощью Dynatrace?

Вы фактически увидите две отдельные пользовательские сессии:

1. Первая сессия начинается с загрузки страницы первого домена и заканчивается, когда пользователь переходит по ссылке, ведущей на веб-страницу другого домена (второго домена).
2. Вторая сессия начинается с первой загрузки страницы на втором домене и заканчивается, когда выполняется любой из [критериев завершения пользовательской сессии](#user-session-end).

Это происходит по следующим причинам:

* **Техническая причина**: файлы cookie не могут совместно использоваться разными доменами, за исключением поддоменов.
* **Причина безопасности**: это функция безопасности браузеров и ограничение, которое разделяют все поставщики.

## Анализ в реальном времени

* Доступ к активным пользовательским сессиям через плитку **Live user activity** на дашборде.

![Live user activity](https://dt-cdn.net/images/live-user-activity-1567-1df03a6ae5.png)

* Перейдите на одну из страниц проблем и выберите **See user sessions sample**.

![Problem details page](https://dt-cdn.net/images/user-sessions-problems-pages-1635-7fb715b445.png)

* Затронутые сессии также доступны непосредственно с одной из страниц проблем.

![User sessions affected by a problem](https://dt-cdn.net/images/user-sessions-from-problems-pages-to-sessions-page-1634-805c05bb34.png)

* Данные об отказах и конверсиях доступны для завершённых пользовательских сессий.

![Conversions and bounces on the User sessions page](https://dt-cdn.net/images/user-sessions-conversions-and-bounces-1639-f3a0e84129.png)

## Примеры

Эти примеры показывают, как можно получить представление о поведении пользователей с помощью анализа пользовательских сессий Dynatrace.

Фильтрация пользовательских сессий по продолжительности

Вы можете фильтровать пользовательские сессии по продолжительности: длиннее или короче определённого значения либо в определённом диапазоне. На скриншоте ниже отображаются пользовательские сессии с продолжительностью не менее 10 секунд.

![Filter user sessions based on user session duration](https://dt-cdn.net/images/image005-2550-69ae07a8ad.png)

Поиск всех пользовательских сессий, содержащих хотя бы один экземпляр конкретных действий

Вы можете искать все пользовательские сессии, содержащие хотя бы один экземпляр любого из нескольких действий пользователя в их пути кликов.

![Search for user sessions with specific user actions](https://dt-cdn.net/images/image007-2550-ced4628b80.png)

Создание сложных фильтров

Обратите внимание на строку фильтра в примере ниже. Этот поиск соответствует пользовательским сессиям, отвечающим следующим критериям:

* **Application type: Web** и **Browser Type: Desktop Browser**. Пользователь обращался к одному из ваших веб-приложений через десктопный браузер.
* **Duration 60s**. Сессия длилась не менее 1 минуты.
* **Action count = 5**. В течение сессии пользователь выполнил пять действий.
* **User action name: test**. В пользовательской сессии произошло действие `test`.

![Create complex filters](https://dt-cdn.net/images/image009-2550-759db59a94.png)

Изучение категорий на панели находок

Для каждой категории на панели находок есть отдельный раздел, отображающий визуализации и находки для этой категории. Например, **Application type** показывает текущее распределение, распределение во времени и географическое распределение различных типов приложений. На географической карте отображается цвет типа приложения с наибольшим числом сессий.

![Application type category view](https://dt-cdn.net/images/image011-2122-def628c232.png)

Вы можете выбрать любую из находок и легко применить её, нажав **Apply selection as a filter** в левом нижнем углу страницы.

![Apply current category as a filter](https://dt-cdn.net/images/image013-2540-899b1a7298.png)

## Связанные темы

* [Пользовательские сессии](../rum-concepts/user-session.md "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* [Эффективная поддержка клиентов с сегментацией сессий](../dem-use-cases/customer-support-with-session-segmentation.md "Learn how to resolve customer complaints using session segmentation.")
