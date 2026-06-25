---
title: Multidimensional analysis for browser monitors
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors
scraped: 2026-05-12T11:19:16.823433
---

# Multidimensional analysis for browser monitors

# Multidimensional analysis for browser monitors

* Explanation
* 12-min read
* Updated on Feb 27, 2024

Многомерный анализ Dynatrace позволяет анализировать выполнения браузерных мониторов по нескольким измерениям фильтрации.

Страница **Multidimensional analysis** строит графики [производительности](#performance), [доступности](#availability) и [количества ошибок](#errors) за выбранный период. Можно выбрать [более короткий диапазон анализа](#analysis-range) и просматривать отдельные точки данных на точечном графике и в виде списка. В верхней части страницы отображаются долгосрочные данные (временные ряды), затем [точечный график](#scatter-plot) и отдельные [точки данных](#data-points) за период до 35 дней с текущего момента. Для точек данных можно просматривать [графики водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов.") для действий и сведения об ошибках, если они есть.

С точечного графика значений производительности отдельных точек данных можно настраивать широкий диапазон метрик производительности на уровне страницы и ресурсов для создания [вычисляемых метрик](#calculated-metrics).

Для каждой точки данных можно просматривать скриншоты всех событий; графики водопада доступны для каждого действия в событиях с замерами времени.

Страница **Multidimensional analysis** открывается путём перехода с различных мест [страницы Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").

![MDA for browser monitor performance](https://dt-cdn.net/images/syntheticmdaperformance1-1847-281a0cb232.png)

MDA for browser monitor performance

![MDA for browser monitor availability](https://dt-cdn.net/images/syntheticmdaavailability-1330-792a27f9a3.png)

MDA for browser monitor availability

![MDA for browser monitor errors](https://dt-cdn.net/images/syntheticmdaerrors-1316-a0e59c0e13.png)

MDA for browser monitor errors

## Диапазон анализа

При просмотре [доступности](#availability), [производительности](#performance) или [ошибок](#errors) заштрихованная область на графике тренда обозначает диапазон анализа — подмножество глобального периода. Щёлкните в другом месте графика, чтобы переместить диапазон анализа; [точечный график](#scatter-plot) и список [точек данных](#data-points) фильтруются соответственно.

При наведении курсора на график появляются кнопки со стрелками ![Left and right arrows](https://dt-cdn.net/images/analysisarrowbuttons-49-c49391e1bc.png "Left and right arrows"), с помощью которых можно перемещать период вперёд и назад во времени, например с 10:30-12:30 на 08:30-10:30. Обратите внимание: размер периода и диапазона анализа при этом не изменяется.

Используйте кнопки масштабирования ![Zoom in and out](https://dt-cdn.net/images/analysiszoombuttons-49-744f9d7427.png "Zoom in and out") для регулировки периода: увеличение (**+** = более короткий период) или уменьшение (**-** = более длинный период). Размер диапазона анализа соответственно корректируется при использовании кнопок масштабирования; можно также использовать раскрывающийся список для изменения диапазона анализа.

![Analysis range](https://dt-cdn.net/images/analysisrange1-1666-a00a164538.png)

Analysis range

При наличии проблемы сплошные красные полосы над графиками производительности или доступности обозначают длительность проблемы. Щёлкните проблему, чтобы выбрать её длительность в качестве диапазона анализа. [Точечный график](#scatter-plot) и [точки данных](#data-points) фильтруются соответственно.

![Problem duration](https://dt-cdn.net/images/analysisrangeproblem-1688-38499191d4.png)

Problem duration

## Анализ доступности

При нажатии **Analyze availability** на [странице Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#availability "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") вы переходите на страницу **Multidimensional analysis**, которая показывает график тренда доступности для всех расположений мониторинга.

![Analyze availability of all locations](https://dt-cdn.net/images/mdaavailabilityalllocations1-1663-add9daa0b0.png)

Analyze availability of all locations

При выборе конкретного расположения на странице Synthetic details вы переходите на страницу анализа, отфильтрованную по этому расположению.

Многомерный анализ доступности включает возможность фильтрации графика (и соответствующего [точечного графика](#scatter-plot) и [точек данных](#data-points)) для просмотра данных по **All locations** или отдельному расположению мониторинга.

Наведите курсор на любую точку графика для просмотра сведений о доступности в этот момент времени.

Красные области обозначают сбои: ширина области обозначает время сбоя, высота — процент сбоя. Сбои — это периоды с точками данных ошибок или сбоями.

Сплошные красные полосы над графиком доступности обозначают длительность проблем доступности (глобальный или локальный сбой). Щёлкните полосу проблемы, чтобы увидеть длительность сбоя. [Точки данных](#data-points) за период проблемы отображаются автоматически. Выберите ссылку на проблему для перехода на страницу деталей проблемы.

![Availability problem in MDA](https://dt-cdn.net/images/mdaavailabilityproblem-329-39fe431e29.png)

Availability problem in MDA

* Ошибки монитора не приводят к [проблемам](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#problems "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details."), если они не нарушают [пороговые значения доступности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Узнайте о настройке браузерных мониторов и clickpath-ов.") или если пороговые значения не включены.
* Отображение проблем в веб-интерфейсе Dynatrace и получение оповещений в течение окон обслуживания зависит от того, как вы [настроили окна обслуживания](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Создавайте окна обслуживания и определяйте их область.").
* [Окна обслуживания можно исключать из расчётов доступности](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Поймите расчёты метрик Synthetic Monitoring.") с помощью глобальной настройки.

## Анализ производительности

Открыть страницу **Multidimensional analysis** для данных о производительности со [страницы Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") можно несколькими способами. [Выбранные по умолчанию ключевые метрики производительности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов.") переносятся на страницу анализа, однако их можно изменить ([см. ниже](#mda-performance)).

* Выберите [**Analyze performance**](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#performance "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") для просмотра тренда производительности для всех расположений мониторинга. Выбранный на странице деталей тип событий (события с load actions, события с XHR actions или все события) переносится на страницу **Multidimensional analysis**. Результирующий график производительности разбивается по событию. Отображаемая метрика зависит от выбранного типа событий: **Total duration** для всех событий и выбранные ключевые метрики производительности для событий с load actions или XHR actions.

  ![Analyze performance by event type](https://dt-cdn.net/images/mdaperformanceactiontype-1520-1916a1b752.png)

  Analyze performance by event type
* Выберите конкретное расположение на странице деталей для просмотра анализа производительности, отфильтрованного по этому расположению.
* Нажмите **Analyze** рядом с событием в [карточке Synthetic events and actions](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#events-actions "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details."), чтобы просмотреть график этого события по всем расположениям. Тип действия, например **Load actions**, выбирается автоматически. График производительности автоматически разбивается по метрике.

  ![Analyze performance one event](https://dt-cdn.net/images/mdaperformanceoneevent-1512-9b501c5761.png)

  Analyze performance one event

Наведите курсор на любую точку графика для просмотра производительности ключевых метрик в этот момент времени.

Сплошные красные полосы над графиком производительности обозначают длительность проблем (нарушений пороговых значений или сбоев доступности). Щёлкните полосу проблемы, чтобы увидеть её длительность. [Точки данных](#data-points) за период проблемы отображаются автоматически. Выберите ссылку на проблему для перехода на страницу деталей проблемы.

![Performance problem in MDA](https://dt-cdn.net/images/mdaperformanceproblem1-404-4314be9617.png)

Performance problem in MDA

### Многомерный анализ производительности

При просмотре производительности за выбранный [диапазон анализа](#analysis-range) фильтры позволяют строить графики производительности и фильтровать соответствующий [точечный график](#scatter-plot) и [точки данных](#data-points) по нескольким измерениям:

![MDA filters for performance](https://dt-cdn.net/images/mdafiltersperformance-807-084f15bd3a.png)

MDA filters for performance

* **Location**: выберите все расположения или отдельное расположение мониторинга.
* **Action type**: просматривайте производительность для load actions, XHR actions, custom actions или всех actions.
* **Performance metric**: в этом списке отображаются те же [ключевые метрики производительности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов."), которые доступны в настройках монитора и для которых данные производительности фиксируются из коробки. Тогда как [страница Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") строит одну ключевую метрику производительности на тип действия, страница **Multidimensional analysis** предоставляет все доступные метрики на тип действия.

  + При фильтрации по **All actions** в тренде доступен только просмотр **Total duration**.
  + При фильтрации по **Load actions** или **XHR actions** в тренде **Total duration** недоступна. Эта метрика применима только к производительности монитора или событий в целом, не к типам действий внутри событий.
* **Event**: выберите все или конкретное событие скрипта Synthetic. Из этого списка можно выбрать только событие с замерами времени; события без данных о времени неактивны.
* **Split by**: выберите **Location**, **Action type**, **Metric** или **Event**. При выборе критерия разбивки соответствующий список неактивен.

  ![Performance MDA splitting factor](https://dt-cdn.net/images/mdasplitby-811-2b18640f01.png)

  Performance MDA splitting factor

### Точечный график

Тогда как график тренда в верхней части страницы может показывать агрегированные данные, точечный график показывает производительность для каждой точки данных в диапазоне анализа. Точечный график всегда отображает производительность независимо от того, анализируете ли вы [производительность](#performance), [доступность](#availability) или [ошибки](#errors) на странице **Multidimensional analysis**.

Выбранный на странице Synthetic details тип действий (load, XHR или все события) переносится на точечный график. Точечный график показывает ключевые метрики производительности по умолчанию (указанные в [настройках монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов.")) для load actions и XHR actions; при выборе **All events** на странице Synthetic details точечный график показывает **Total duration**.

Фильтры, выбранные вверху страницы для многомерного анализа производительности, влияют на точечный график. Например, на изображении ниже выборы **Location**, **Action type**, **Performance metric** и **Event** из графика тренда переносятся на точечный график. (Выбор **All actions** в графике тренда переключается на **Load actions** в точечном графике.)

![Scatter plot filters](https://dt-cdn.net/images/scatterplotfilters-1496-3bfad65ab4.png)

Scatter plot filters

Точечный график также имеет собственный независимый фильтр метрик производительности, позволяющий просматривать разные метрики в графике тренда и точечном графике. Фильтр метрик точечного графика предлагает больше вариантов метрик на уровне страницы и ресурсов, которые можно настраивать для создания [**вычисляемых метрик**](#calculated-metrics).

Точечный график можно фильтровать только для точек данных ошибок (выберите **Error** > **Yes**), конкретной ошибки (**Error codes**), **Location**, события скрипта Synthetic **Event** или **Request**. Эти фильтры независимы от фильтров графика тренда. Фильтр **Request** показывает каждый запрос из каждого действия и предназначен для использования с [графиком водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов."). При анализе отдельного запроса ресурса в водопаде нажмите **Analyze over time** для просмотра производительности ресурса по точкам данных на точечном графике.

![Scatter plot filters](https://dt-cdn.net/images/scatterplotfilters3-1499-a38e7e64f9.png)

Scatter plot filters

## Вычисляемые метрики

Помимо [ключевых метрик производительности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов."), которые можно выбрать в качестве метрик отображения по умолчанию для load actions и XHR actions, Dynatrace предлагает и строит графики нескольких других метрик на уровне страницы и ресурсов (см. также [Графики водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов.")). Все эти метрики перечислены в списке **Analyze** для [точечных графиков](#scatter-plot).

Хотя до 35 дней исторических данных всегда доступно для ключевых метрик производительности, для пользовательских настроек любой другой метрики можно фиксировать [долгосрочные данные](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Ознакомьтесь со сроками хранения различных типов данных."), создав вычисляемую метрику. Данные временных рядов для вычисляемой метрики доступны с момента её создания.

Выберите метрику и примените нужные фильтры в точечном графике, затем нажмите **Create metric**. При желании включите фактор разбивки в диалоге создания метрики. Можно изменить **Metric name** и **Metric key**. По умолчанию ключ метрики отражает имя метрики и включает имя монитора. После создания вычисляемой метрики её имя, ключ и конфигурацию изменить нельзя.

Можно создать до 100 вычисляемых метрик на монитор и до 500 на окружение мониторинга. Обратите внимание: вычисляемые метрики доступны только для конкретного браузерного монитора, для которого они созданы (например, нельзя использовать вычисляемую метрику, созданную для одного монитора, при построении графика другого монитора).

Замечания о метриках

* **Total duration** — метрика уровня монитора или события и недоступна для конкретных типов действий (load, XHR).
* Ориентированные на отрисовку метрики **First paint**, **First contentful paint** и **Largest contentful paint** применимы только к load actions.
* Расчёт **Visually complete** можно настроить, управляя различными пороговыми значениями и тайм-аутами, а также исключая определённые элементы из расчёта. Эти параметры задаются в настройках браузерного монитора: **Advanced setup** > **Enable custom RUM JavaScript settings** > **Configure parameters for Visually complete and Speed index calculation**.
* Некоторые метрики или измерения метрик не поддерживают создание вычисляемых метрик. В таких случаях при попытке создания метрики появляется сообщение, или фактор разбивки неактивен.

![Create a calculated metric](https://dt-cdn.net/images/createcalculatedmetric-1660-6bd30535bd.png)

Create a calculated metric

Рекомендуется создавать вычисляемые метрики для тех метрик, которые ещё не предложены как [ключевые метрики производительности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#kpm "Узнайте о настройке браузерных мониторов и clickpath-ов.") в настройках браузерных мониторов.

Рекомендуется, чтобы имя метрики отражало любые разбивки и фильтры, что упрощает её отличие от похожих метрик.

После этого можно настроить диаграмму в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных данных.") или [пользовательское оповещение](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace.") для вычисляемой метрики. Нажмите **Manage this metric** для перехода на вкладку **Metrics** настроек монитора, откуда можно отключать/включать, удалять метрики или создавать диаграммы и оповещения на основе вычисляемых метрик для данного монитора.

![Calculated metric created](https://dt-cdn.net/images/calculatedmetriccreated-328-109d3aab05.png)

Calculated metric created

## Анализ ошибок

При нажатии **Analyze errors** на [карточке Errors](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#errors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") на странице Synthetic details вы переходите на страницу **Multidimensional analysis**, показывающую гистограмму количества ошибок по коду ошибки за единицу времени для всех расположений за период. Высота каждого столбца представляет частоту кодов ошибок. При нажатии **Analyze** ![Analyze](https://dt-cdn.net/images/analyze-icon-e97b8dab47.svg "Analyze") рядом с отдельным кодом ошибки вы переходите на страницу анализа, отфильтрованную по этому коду ошибки. [Точечный график](#scatter-plot) и [точки данных](#data-points) автоматически фильтруются для показа только ошибок.

Наведите курсор на любой столбец графика для просмотра количества ошибок в этот момент времени.

![Analyze all errors](https://dt-cdn.net/images/mdaallerrors-1499-51f21b7a1d.png)

Analyze all errors

### Многомерный анализ ошибок

Для многомерного анализа ошибок доступны следующие фильтры:

* **Location**: выберите все расположения или отдельное расположение мониторинга.
* **Error**: выберите все коды ошибок или единственный код ошибки.
* **Event**: выберите все или отдельное событие скрипта Synthetic. Из этого списка можно выбрать только событие с замерами времени (действие); события без данных о времени неактивны.
* **Split by**: выберите **Location**, **Error code** или **Event**.

## Точки данных

Страница **Multidimensional analysis** позволяет выбрать конкретный набор выполнений в [диапазоне анализа](#analysis-range), отфильтрованный с помощью многомерного анализа, чтобы сосредоточиться на конкретном действии в отдельной точке данных для устранения проблем производительности или доступности.

Список отображаемых точек данных соответствует комбинации фильтров, выбранных для [точечного графика](#scatter-plot) и многомерного анализа [производительности](#performance), [доступности](#availability) или [ошибок](#errors).

По умолчанию точки данных перечислены от самых последних. Выполнения по требованию в списке помечены как **on-demand**. При наведении курсора на точку данных в точечном графике можно просмотреть метку времени начала, расположение и значение ключевой метрики производительности. Точки данных ошибок (сбои доступности) помечены красным и отображают код ошибки.

Выберите точку данных для просмотра скриншотов и анализа на уровне событий, включая графики водопада для событий с замерами времени (действий).

Сведения о выполнении включают метки времени начала и конца, а также расположение. Тип выполнения **Execution type**:

* **on-demand** — для выполнений по требованию.
* **standard** — для запланированных выполнений.
* **re-run** — для выполнений, повторённых при ошибке (включён [**Automatic retry on error**](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Узнайте о настройке браузерных мониторов и clickpath-ов.")).
* **on-update** — для выполнений после обновления скрипта монитора.

Можно переключаться между всеми событиями и только событиями с замерами времени (то есть событиями с действиями и графиками водопада). Нажмите **Close details** для возврата к списку точек данных.

![Switch to view events with timings](https://dt-cdn.net/images/events-with-timings-1181-3cd5daebe7.png)

Switch to view events with timings

Успешные точки данных отображают эталонные скриншоты, сделанные для каждого события. (Подробнее о том, как делаются скриншоты, см. в разделе [Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors#screenshots "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").) Обратите внимание: даже успешные точки данных могут содержать действия с отдельными ошибками ресурсов, отмеченными красным на графике водопада.

![Successful data point](https://dt-cdn.net/images/bm-successful-data-point-1871-c7c20fc7b0.png)

Successful data point

Точки данных ошибок отображают скриншоты, сделанные во время конкретного выполнения, что позволяет сравнить **Actual** (фактический) и **Expected** (эталонный) скриншоты. Неуспешная точка данных и действие помечены красным. Нажмите **Show difference**, чтобы увидеть процент и области несоответствия, выделенные на наложенном изображении.

![Error data point](https://dt-cdn.net/images/bm-error-data-point-1879-3592365d74.png)

Error data point

## Связанные темы

* [API вычисляемых метрик — Synthetic](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Управляйте вычисляемыми синтетическими метриками через Dynatrace configuration API.")