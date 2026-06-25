---
title: Synthetic details for browser monitors
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors
scraped: 2026-05-12T11:32:24.728485
---

# Synthetic details for browser monitors

# Synthetic details for browser monitors

* Explanation
* 14-min read
* Updated on Jan 24, 2024

Перейдите в **Synthetic Classic** и выберите браузерный монитор или clickpath, чтобы открыть **страницу Synthetic details**, которая предоставляет обзор результатов выполнения монитора с визуализациями, проблемами и свойствами монитора. Страница Synthetic details, основанная на AI-движке Davis, отображает сводную информацию: графики трендов, фильтры и быстрые ссылки для перехода к настройкам монитора, деталям проблемы или анализу водопада для неуспешного события.

![Clickpath details](https://dt-cdn.net/images/clickpathdetails-2188-0cc928c5df.png)

Clickpath details

Узнайте о новом интерфейсе для деталей браузерных мониторов

При выборе браузерного монитора в **Synthetic Classic** появляется переключатель для перехода в новый интерфейс деталей браузерных мониторов. Включение переключателя активирует новую страницу деталей для всех браузерных мониторов в вашем окружении.

![Browser monitors new UI toggle](https://dt-cdn.net/images/browsermonitordetailsnewuicta-1620-adeff8a0c3.png)

Browser monitors new UI toggle

Пока можно переключаться между новой и старой версиями страницы деталей для их сравнения. Используйте кнопку **Share feedback**, чтобы поделиться мнением о новом дизайне. Если закрыть панель в верхней части страницы деталей, она переместится в нижнюю часть.

![New UI enabled](https://dt-cdn.net/images/browsermonitordetailsctatoggleenabled-1620-687200891e.png)

New UI enabled

## Метрические визуализации

Верхняя панель показывает общую инфографику [доступности](#availability) или [производительности](#performance) монитора за выбранный период. Выберите любую инфографику для перехода к соответствующей карточке. Инфографика **Availability** показывает процент доступности и время простоя за выбранный период. Инфографика производительности настроена для отображения выбранных [**ключевых метрик производительности**](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов.") вместе с **Total duration**.

Также можно прокручивать эталонные [скриншоты](#screenshots) для каждого из [событий скрипта](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий, создаваемых при записи браузерного clickpath-а.") монитора.

Используйте панель фильтров в верхней части страницы для географической фильтрации всех данных Synthetic: по **Continent**, **Country**, **Region**, расположению мониторинга **Location** и облачному провайдеру **Cloud**.

Используйте быстрые ссылки в левом верхнем углу для перехода непосредственно к различным карточкам страницы деталей или для доступа к настройкам браузерного монитора (**Edit**, **Disable**, **Delete**). Отсюда также можно перейти на страницу многомерного анализа (**Analyze executions**), просмотреть **Synthetic sessions** на странице пользовательских сессий для связанного приложения или просмотреть **Report** о доступности.

Теги, применённые к браузерному монитору, отображаются под именем монитора. Нажмите **Add tag** для добавления дополнительных тегов. Обратите внимание: теги можно добавлять и удалять только со страницы деталей.

Фиолетовые маркеры над временными линиями доступности или производительности обозначают окна обслуживания. Выберите маркер для просмотра сведений об окне.

![Quick links](https://dt-cdn.net/images/clickpathdetailsinfographicsquicklinks-2190-a42e55aa2d.png)

Quick links

* Отображение проблем и получение оповещений в течение окон обслуживания зависит от того, как вы [настроили окна обслуживания](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Создавайте окна обслуживания и определяйте их область.").
* [Окна обслуживания можно исключать из расчётов доступности](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Поймите расчёты метрик Synthetic Monitoring.") с помощью глобальной настройки.

### Скриншоты

Эталонные скриншоты, отображаемые на верхней панели страницы Synthetic details, делаются в случае успешного выполнения монитора при его создании или редактировании, а затем раз в 24 часа из случайного расположения мониторинга (включая [частные расположения](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.")). Скриншоты делаются в конце каждого события скрипта (даже тех, у которых нет замеров времени). Скриншоты можно прокручивать здесь или выбирать для просмотра увеличенных версий.

![Synthetic details reference screenshots](https://dt-cdn.net/images/syntheticdetailsscreenshots-251-74aa173377.png)

Synthetic details reference screenshots

Обратите внимание: эталонные скриншоты всегда актуальны, даже при просмотре данных Synthetic за исторический период.

При сбое монитора скриншоты для каждого неуспешного выполнения (SCoE) доступны на [странице многомерного анализа](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов.").

### Хранение скриншотов

Для просмотра скриншотов из частных расположений Synthetic ваш ActiveGate с поддержкой Synthetic и браузер, через который вы обращаетесь к Dynatrace, должны иметь доступ к сервису Amazon S3.

* Для просмотра скриншотов из частных расположений Synthetic убедитесь, что ваш брандмауэр разрешает подключения к `ruxit-synth-screencap.s3.amazonaws.com`.
* Для хранения скриншотов из частных расположений обеспечьте доступ к `ruxit-synth-screencap.s3-accelerate.amazonaws.com`.

  + Скриншоты хранятся в отдельной папке для каждого окружения мониторинга, но S3 Bucket один и тот же (`ruxit-synth-screencap`). Доступ к скриншотам каждого окружения возможен только по прямой ссылке при условии авторизации в этом окружении.
  + Данные шифруются [ключом, управляемым Amazon S3](https://dt-url.net/4a02xvx). Этот ключ одинаков для всех окружений.

Дополнительную информацию см. в сообществе Dynatrace: [Can't see screenshots in browser monitor results](https://dt-url.net/mfw2xmb).

## Доступность

Карточка **Availability** показывает общую доступность по всем расположениям мониторинга с аннотациями глобальных/локальных сбоев и глобальных/локальных отсутствующих данных (например, при отключённом мониторе).

Обратите внимание: монитор может быть недоступен в одном или всех расположениях даже без настроенных [пороговых значений сбоев (глобальных или локальных)](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Узнайте о настройке браузерных мониторов и clickpath-ов."). Продолжительность сбоя — это сумма всех простоев за выбранный период без учёта перекрывающихся простоев. Подробнее о расчёте доступности и простоя см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Поймите расчёты метрик Synthetic Monitoring.").

На графике показана доступность для каждого расположения мониторинга. Расположения можно сортировать по имени **Location**, **Cloud** или **Availability**.

Периоды с недоступностью выделены красным. Наведите курсор на график **All locations**, чтобы увидеть количество расположений со сбоями или отсутствующими данными в любой момент времени.

![Availability card](https://dt-cdn.net/images/clickpathdetailsavailability-2187-a6e3121c0f.png)

Availability card

Разверните **All locations** для просмотра графиков доступности каждого расположения. Выберите блок простоя (красный) или доступности (фиолетовый) на временной линии любого расположения и нажмите **Analyze** для перехода к [многомерному анализу](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."), отфильтрованному по этому расположению. Также можно выбрать имя расположения или нажать **Analyze availability** для просмотра данных по всем расположениям.

Нажмите **Pin to dashboard**, чтобы закрепить плитку **Browser monitor** на классическом дашборде.

## Производительность

Карточка **Performance** показывает линии трендов **Total duration** для **all actions** монитора или выбранную ключевую метрику производительности для **load actions** или **XHR actions**. Можно просматривать производительность с разбивкой по **events** или по расположениям мониторинга **locations**.

![Performance card](https://dt-cdn.net/images/clickpathdetailsperformance-2225-4fad47a8bf.png)

Performance card

Обратите внимание: Total duration рассчитывается суммированием, а значения ключевой метрики производительности являются средними (например, **Visually complete**), вычисляемыми отдельно для load actions и XHR actions.

Ключевые метрики производительности

[**Ключевые метрики производительности**](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Узнайте, как использовать правильные ключевые метрики производительности для оптимизации данных о пользовательском опыте для каждого приложения.") позволяют выбирать цели производительности, наиболее соответствующие переменным потребностям каждого отслеживаемого приложения. Например, для оптимизации производительности традиционного веб-приложения можно выбрать User action duration. Для других приложений, где скорость взаимодействия важнее UI, можно оптимизировать время загрузки JavaScript-ресурсов. По умолчанию для load actions и XHR actions используется **Visually complete** — метрика, измеряющая время полного отображения видимой части браузера пользователя.

Поскольку Dynatrace фиксирует список ключевых метрик производительности из коробки, можно переключить выбор в настройках монитора и сразу получить исторические данные.

Как выбрать или переключить ключевую метрику производительности

Для каждого браузерного монитора или clickpath можно выбрать отдельную ключевую метрику производительности для load actions и XHR actions в [режиме редактирования](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов.") после создания монитора.

Пример значений ключевых метрик производительности

Значения ключевых метрик производительности вычисляются как средние. Рассмотрим транзакцию входа в систему, состоящую из трёх событий, каждое из которых приводит к одному load action:

* Начальная загрузка страницы (1 с Visually complete)
* Нажатие кнопки входа (5 с Visually complete)
* Переход на другую страницу (3 с Visually complete)

Показатель **Visually complete** для этих load actions составляет 3 секунды, тогда как **Total duration** может составлять 9 секунд.

Если открыть карточку [Synthetic events and actions](#events-actions), можно увидеть, что производительность рассчитывается только для событий с замерами времени. Подробнее см. в разделе [Количество действий, потребляемых браузерными clickpath-ами](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий."). При просмотре **all actions** на графике Total duration исключаются события без сетевой активности. При просмотре **load actions** или **XHR actions** отображаются графики ключевых метрик производительности для отдельных событий с соответствующими типами действий. Обратите внимание: событие может содержать комбинацию действий разных типов, например два load action и один XHR action.

Выберите событие или расположение в легенде, чтобы включить или исключить его из графика. Наведите курсор на график для просмотра производительности (ключевой метрики или Total duration) отдельных событий или расположений в заданный момент времени. Щёлкните и выберите **Analyze** для перехода к соответствующему временному диапазону на [странице многомерного анализа](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."), отфильтрованному по выбранному типу действия. Также можно нажать **Analyze performance** для перехода к производительности на странице многомерного анализа.

При нарушении [порогового значения производительности для Total duration всех событий](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#performance-thresholds "Узнайте о настройке браузерных мониторов и clickpath-ов.") над графиком **all actions** на время проблемы появляется сплошная красная полоса; пороговое значение отображается пунктирной красной линией. Выберите сплошную красную полосу для просмотра расположений, нарушивших пороговое значение, и ссылки на страницу обзора проблемы.

![Total duration violation](https://dt-cdn.net/images/clickpathdetailstotaldurationviolation-2188-7e5789306a.png)

Total duration violation

При нарушении пороговых значений отдельных событий карточка [Synthetic events and actions](#events-actions) выделяет нарушающие события, их длительность и задействованные пороговые значения.

## Synthetic events and actions

Карточка **Synthetic events and actions** помогает различать [события](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий, создаваемых при записи браузерного clickpath-а.") скрипта с замерами времени и без. Выберите **all events** или выберите **events with timings** и тип действия (**load actions** или **XHR actions**) для фильтрации карточки. При просмотре всех событий отображается средняя Total duration составных действий. При просмотре событий по типу действия отображается выбранная [ключевая метрика производительности](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Узнайте, как использовать правильные ключевые метрики производительности.").

События — это записанные взаимодействия, которые воспроизводятся при выполнении браузерного clickpath-а. Не все события обязательно вызывают сетевые запросы, например нажатие поля ввода или ввод текста в форму. Эти события важны с функциональной точки зрения, но не создают данных о производительности. События с замерами времени, то есть события, которые вызывают действия, являются основой данных о производительности.

![Synthetic events and actions card](https://dt-cdn.net/images/clickpathdetailseventsactionsfiltered-1090-3a1679e4fb.png)

Synthetic events and actions card

Разверните событие с замерами времени в списке событий, чтобы сравнить все метрики производительности составных действий на одном графике. Если событие содержит более одного типа действия, можно просматривать метрики по типу действия. Выберите метрику в легенде для её включения или исключения из графика производительности. Нажмите **Edit event** для редактирования события скрипта в настройках монитора. Нажмите **Analyze** для перехода на [страницу многомерного анализа](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."), отфильтрованную по этому событию.

![Synthetic event details](https://dt-cdn.net/images/clickpathdetailseventsactionsexpanded-1190-43583deb9c.png)

Synthetic event details

Dynatrace использует одну и ту же технологию для захвата данных реальных пользователей и синтетических данных, поэтому результаты синтетического мониторинга легко сопоставляются с реальными пользователями. Если браузерный монитор связан с приложением, Dynatrace автоматически показывает действия реальных пользователей для каждого события Synthetic с замерами времени: выберите ссылки **contributing actions**. Вы перейдёте на соответствующую страницу пользовательского действия с возможностью фильтрации по синтетическим пользователям.

![Link to real user action](https://dt-cdn.net/images/clickpathdetailslinktouseraction-2181-0c35574fed.png)

Link to real user action

![User action page](https://dt-cdn.net/images/clickpathdetailsuseractionpage-2188-aa91dbb3a8.png)

User action page

События выделяются при нарушении пороговых значений производительности. Разверните событие, чтобы увидеть его замеры времени и нарушенное пороговое значение. На время проблемы над составным графиком появляется сплошная красная полоса; пороговое значение отображается пунктирной красной линией. Выберите сплошную красную полосу для просмотра расположений, нарушивших пороговое значение, и ссылки на страницу обзора проблемы; соответствующая проблема также отображается на карточке [Problems](#problems).

![Event performance violation](https://dt-cdn.net/images/clickpathdetailseventviolation-1120-65f9eefc94.png)

Event performance violation

## Проблемы

Карточка **Problems** показывает проблемы производительности (нарушение порогового значения) и доступности (локальный или глобальный сбой) при включении соответствующих пороговых значений в [настройках монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов."). Разверните карточку для просмотра активных и разрешённых проблем за выбранный период.

Существует три основных типа проблем для браузерных мониторов:

* Глобальный сбой (доступность)
* Локальный сбой (доступность)
* Нарушение порогового значения производительности (производительность)

Здесь также отображаются [пользовательские оповещения](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts "Узнайте больше о пользовательских оповещениях и логике их создания.") на основе заданных пользователем пороговых значений.

![Problems card](https://dt-cdn.net/images/clickpathdetailsproblemscard-1094-0de0568223.png)

Problems card

Подробнее о расчёте доступности и производительности и генерации/снятии проблем см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Поймите расчёты метрик Synthetic Monitoring.").

Нажмите кнопку **More** (**...**) на карточке **Problems** для просмотра того же списка проблем на странице **Problems**. Здесь можно просмотреть частоту открытых и закрытых проблем за временные слоты выбранного периода.

![Problems page filtered by a synthetic monitor](https://dt-cdn.net/images/problemspagesyntheticmonitor-2210-d75a12d1e7.png)

Problems page filtered by a synthetic monitor

Разверните **Details** проблемы для просмотра её **Root cause** и **Alerting profiles**, используемых для определения необходимости отправки уведомлений. Перечислены все **Affected** объекты, связанные с первопричиной (например, отслеживаемый сервис или приложение).

![Expanded problem details](https://dt-cdn.net/images/clickpathproblemdetails-1094-e7c03bff41.png)

Expanded problem details

Выберите имя проблемы (например, **Multiple application problems**) на карточке **Problems** для перехода на страницу обзора проблемы. Обратите внимание: проблемы производительности могут объединять нарушения пороговых значений как на уровне монитора, так и на уровне событий. Выберите имя затронутого объекта (то есть затронутого синтетического монитора), чтобы отфильтровать страницу деталей по длительности проблемы.

![Synthetic monitoring problem overview page](https://dt-cdn.net/images/clickpathproblemoverviewpage-1422-4a8e3aca59.png)

Synthetic monitoring problem overview page

![Synthetic details filtered by problem duration](https://dt-cdn.net/images/clickpathdetailsfilteredbyproblem-2191-8c40ee9c5d.png)

Synthetic details filtered by problem duration

Проблемы вместе с составными [событиями](#events) и любыми [ошибками](#errors) доступности дают полное представление о количестве и масштабе проблем монитора.

## События

Карточка **Events** показывает все события, которые могут привести к проблемам. [Пользовательские события](/managed/dynatrace-api/environment-api/events-v1 "Узнайте, что можно делать с Events API Dynatrace."), загруженные в Dynatrace, также отображаются на этой карточке. В списке и на временной линии отображаются события как активных, так и разрешённых проблем.

Наведите курсор на временной слот на временной линии событий, чтобы увидеть тип и количество событий, созданных за этот интервал. Выберите временной слот для отображения событий внутри него.

Выберите тип события, например **Browser monitor performance threshold violation**, чтобы увидеть список событий. Для каждого расположения, в котором монитор нарушает пороговые значения производительности на уровне события или монитора, создаётся одно событие замедления. Выберите отдельное событие для просмотра деталей.

![Events card](https://dt-cdn.net/images/clickpathdetailsevents-1275-d03eaf75cd8.png)

Events card

## Ошибки

Карточка **Errors** отображает временную линию всех неуспешных выполнений монитора с соответствующими кодами ошибок, предоставляя удобный способ быстро найти основную причину сбоев монитора.

Сбой монитора засчитывается как сбой доступности (нарушение глобального или локального порогового значения). Ошибки без [проблем](#problems) могут появляться, если пороговые значения доступности не включены или ошибки не вызывают их нарушения. Нарушение порогового значения производительности не обязательно приводит к ошибке, если монитор при этом не завершается неуспешно.

Нажмите **Analyze errors** для просмотра выполнений с этими ошибками на [странице многомерного анализа](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."). Нажмите **Analyze** ![Analyze](https://dt-cdn.net/images/analyze-icon-e97b8dab47.svg "Analyze") рядом с отдельной ошибкой для просмотра многомерного анализа, отфильтрованного по этой ошибке.

Наведите курсор на любой временной слот на временной линии ошибок для просмотра количества ошибок по типу за этот интервал. Нажмите **Analyze** во всплывающей подсказке для перехода на страницу многомерного анализа с этим временным слотом.

![Errors card](https://dt-cdn.net/images/clickpathdetailserrors-1263-d3eaf75cd8.png)

Errors card

## Свойства

Карточка **Properties** кратко отображает ключевые свойства монитора и количество событий и потребление за выбранный период. Для браузерных мониторов по одному URL количество событий всегда равно 1.

![Browser monitor properties](https://dt-cdn.net/images/clickpathdetailsproperties-1091-01f1540444.png)

Browser monitor properties

## Карта мира

Карта мира показывает, онлайн ли ваши расположения мониторинга или есть ли сбой, помогая различить глобальные и локальные сбои. Выберите расположение на карте для просмотра доступности в этом расположении за выбранный период и статуса последнего выполнения (например, **Outage**). Затем нажмите **Analyze executions** для перехода на [страницу многомерного анализа](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов."), отфильтрованную по этому расположению.

**Assign monitor to application** (см. первое изображение ниже) переводит в настройки монитора, где можно [связать монитор с одним из отслеживаемых веб-приложений](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#assigned-applications "Узнайте о настройке браузерных мониторов и clickpath-ов."). Если для приложений, с которыми работает синтетический монитор, включён [Real User Monitoring (RUM)](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом."), Dynatrace автоматически связывает RUM-приложения с монитором, и отображается карточка **Monitored applications** (см. второе изображение ниже). Здесь можно просмотреть ключевые метрики приложения и перейти непосредственно к данным RUM.

Если с монитором связано RUM-приложение, появится переключатель для дополнения карты мира данными RUM. При сбое в расположении Synthetic можно немедленно сравнить трафик RUM. Данные RUM также служат хорошим индикатором того, из каких ещё расположений следует запускать синтетический монитор.

![World map with Synthetic locations](https://dt-cdn.net/images/syntheticdetailsworldmap1-633-816e0ba257.png)

World map with Synthetic locations

![World map with RUM data](https://dt-cdn.net/images/syntheticdetailsworldmap2-632-6955f42829.png)

World map with RUM data