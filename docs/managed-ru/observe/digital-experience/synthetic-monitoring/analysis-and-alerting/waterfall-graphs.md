---
title: Waterfall graphs
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs
scraped: 2026-05-12T11:31:36.926847
---

# Waterfall graphs

# Waterfall graphs

* Explanation
* 11-min read
* Updated on Feb 26, 2024

Иногда для понимания влияния определённых расположений, локальных CDN-партнёров или других переменных необходимо анализировать отдельные выполнения браузерных мониторов. Анализ водопада — отличный инструмент для просмотра подробной информации о различных ресурсах, составляющих конкретное load action или XHR action в выполнении.

График водопада — это графическое отображение каждого запроса и загруженного ресурса для действия, которым может быть полная загрузка страницы (load action) или обновление контекста внутри страницы без перехода на новый URL (XHR action). Анализ на уровне ресурсов и страниц основан на [тайм-аутах W3C](/managed/observe/digital-experience/rum-concepts/user-action-metrics "Узнайте, какие метрики Dynatrace рассчитывает для пользовательских действий и что означает каждая из них.").

Графики водопада доступны на Synthetic [странице **Multidimensional analysis**](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов.") для каждого [действия](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.") в событиях с замерами времени в [выполнениях](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#data-points "Узнайте, как анализировать точки данных браузерных мониторов.") браузерных мониторов (как по одному URL, так и clickpath-ов).

В сочетании с [точечным графиком](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Узнайте, как анализировать точки данных браузерных мониторов.") и фильтрами на странице **Multidimensional analysis** графики водопада помогают выявить конкретные ресурсы в конкретных выполнениях, вызывающих сбои или нарушения производительности. [Ключевые выводы](#findings) для каждого водопада преобразуют данные водопада в доступную и практически применимую информацию.

На изображениях ниже показаны графики водопада для load action и XHR action соответственно.

![Load action waterfall](https://dt-cdn.net/images/waterfallloadaction1-1205-086b74aa33.png)

Load action waterfall

![XHR action waterfall](https://dt-cdn.net/images/waterfallxhraction1-1274-efc6bcbdc0.png)

XHR action waterfall

Неуспешные выполнения могут содержать графики водопада для составных действий вплоть до момента сбоя монитора. В зависимости от события, в котором произошёл сбой, и типа ошибки графики водопада могут присутствовать даже для мониторов с 0% доступностью и, соответственно, без данных о производительности на уровне монитора.

## Понимание данных в графиках водопада

Первая запись в графике водопада (**Loading of page** для load action или URL для XHR action) показывает общую **длительность пользовательского действия**. Длительность пользовательского действия также обозначена вертикальной временной линией **A**.

Информацию о влиянии перехода Synthetic Recorder (расширение браузера Chrome) на Manifest Version 3 см. в разделе [Устранение неполадок, связанных с MV3, в браузерных мониторах](#troubleshoot-mv3).

Наведите курсор на запись для просмотра дополнительной информации о **Number of resources** (количестве загруженных ресурсов) или отдельных **URLs** (URL). (Количество ресурсов первой и третьих сторон см. в разделе [Выводы](#findings).)

![First entry in a load action waterfall](https://dt-cdn.net/images/waterfallloadactionloadingofpage-1112-882a1717d2.png)

First entry in a load action waterfall

![First entry in an XHR action waterfall](https://dt-cdn.net/images/waterfallxhractionfirstentry-1174-cd6dcb60a3.png)

First entry in an XHR action waterfall

В графике водопада основные записи организованы в три категории: [запросы документов](#document-requests), [XHR-запросы](#xhr-requests) и [запросы ресурсов](#resources). Наведите курсор на запрос или ресурс для просмотра полного URL.

### Запросы документов

Для load actions, загружающих всю страницу, в этом разделе перечислены базовая страница и любой контент, отображаемый во фреймах. Начальный запрос, обычно базовая страница, выделен фиолетовым. Для XHR actions в этом разделе обычно показываются запросы документов в iframe-ах.

Временные метрики базовой страницы лежат в основе вертикальных временных линий уровня страницы, отображаемых на диаграмме. Например, начало времени загрузки базовой страницы отмечает метрику W3C Navigation start (вертикальная временная линия **N**). Load actions имеют другой набор [событий времени уровня страницы](#filters) по сравнению с XHR actions.

Если для переходимой страницы настроен редирект, показываются запрос документа и ресурсы страницы, на которую выполнен редирект.

Наведите курсор на запись для просмотра разбивки времени загрузки по компонентам. Компоненты Processing, OnDOMContentLoaded и OnLoad применимы только к базовой странице.

Dynatrace Synthetic Monitoring включает время обработки в отображение и расчёт водопада. Время обработки — это время, затраченное на выполнение JavaScript или просто накладные расходы браузера, — представлено в виде разрыва между окончанием одного ресурса и началом следующего. Время обработки показывается как компонент времени загрузки базовой страницы.

![Base page](https://dt-cdn.net/images/waterfallloadactionbasepage1-1406-9cc7f0b23f.png)

Base page

### XHR-запросы

Load actions, а также XHR actions могут содержать XHR/fetch-вызовы или запросы ресурсов, не приводящие к полной загрузке страницы. Пример создания XHR-запросов: ввод текста в поле формы и отображение динамически меняющихся предложений автодополнения.

Начальный XHR в XHR action выделен фиолетовым, а его временные метрики отображаются как временные метрики уровня страницы в вертикальных линиях. XHR actions имеют другой набор [событий времени уровня страницы](#filters) по сравнению с load actions.

Записи XHR отображают тайминги ресурсов W3C, а также время любых JavaScript-колбэков — в компоненте Callback. Компонент Callback применим только к XHR.

![Component timings for an XHR](https://dt-cdn.net/images/waterfallxhractioninitialcomponenttimings-586-2be36bf9a7.png)

Component timings for an XHR

### Запросы ресурсов

Ресурсы перечислены в порядке запроса и отображаются с отступом, показывающим смещение от начала навигации по странице до момента вызова каждого ресурса. Проверьте [верхнюю запись](#waterfall-data) в графике водопада для просмотра общего количества загруженных ресурсов; см. раздел [Выводы](#findings) для просмотра разбивки по первой и третьим сторонам.

Время загрузки каждого ресурса и его компоненты показываются в соотношении с другими ресурсами и в контексте общих временных метрик W3C уровня страницы. Наведите курсор на ресурс для просмотра деталей тайминга.

Ресурсы можно [группировать и фильтровать](#filters).

Неуспешные ресурсы помечены красным. Наведите курсор на ресурс для пояснения. Обратите внимание: неуспешный ресурс не обязательно приводит к сбою действия или монитора.

![Failed resource request](https://dt-cdn.net/images/waterfallfailedresource1-589-cca3366f7a.png)

Failed resource request

Если в [настройках монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#advanced-setup "Узнайте о настройке браузерных мониторов и clickpath-ов.") заблокированы запросы к указанным доменам/URL/типам ресурсов, ресурсы из таких доменов отображаются без подробных тайм-аутов.

![Blocked request](https://dt-cdn.net/images/waterfallblockedrequest-628-61d68bd691.png)

Blocked request

Можно строить график производительности (**HTML downloaded** / **Response end**) любого запроса, включая запросы документов и XHR, по точкам данных в [точечном графике](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Узнайте, как анализировать точки данных браузерных мониторов."), нажав **Analyze over time**.

![Analyze a request over time](https://dt-cdn.net/images/scatterplotanalyzeovertime-1619-07e12cf69a.png)

Analyze a request over time

## Выводы

Davis, AI-движок причинно-следственного анализа Dynatrace, автоматически определяет ключевые выводы для каждого водопада. Выводы — это ключевые статистические данные и советы, фиксирующие, как ресурсы могут влиять на временные метрики W3C уровня страницы для начального запроса действия: базовой страницы для load actions или начального XHR для XHR actions. Начальные запросы формируют первое впечатление новых посетителей. Ключевые выводы помогают определить, какие ресурсы можно оптимизировать: ресурсы, влияющие на Visually complete (опыт пользователя выше сгиба), несжатые текстовые ресурсы, большие ресурсы или медленные CDN-ресурсы.

Нажмите **Show all findings** для расширения списка выводов над водопадом. Выберите вывод, чтобы выделить связанные ресурсы на графике водопада.

![Top findings expanded](https://dt-cdn.net/images/waterfalltopfinding-1196-54e42a27e5.png)

Top findings expanded

Вывод **Visually complete** сравнивает таймаут действия с любым настроенным пороговым значением и выделяет любые изображения, влияющие на метрику. (Пороговые значения и тайм-ауты можно настроить в настройках браузерного монитора: **Advanced setup** > **Enable custom RUM JavaScript settings** > **Configure parameters for Visually complete and Speed index calculation**.)

![Visually complete finding](https://dt-cdn.net/images/waterfallvcfinding-650-f2d19da580.png)

Visually complete finding

Ещё один вывод выделяет несжатые текстовые ресурсы: если несжатый текстовый ресурс превышает 860 байт, данные о сжатии при наведении курсора выделяются красным. Это пороговое значение может быть настраиваемым ([см. ниже](#finding-thresholds)).

![Uncompressed resource](https://dt-cdn.net/images/waterfalluncompressedresource-586-e65284b928.png)

Uncompressed resource

### Пороговые значения для выводов водопада

Если для веб-приложений, с которыми работает браузерный монитор, включён Real User Monitoring (RUM), можно задать пороговые значения для выводов водопада в настройках приложения.

Здесь также можно найти значения по умолчанию для выводов. Например, можно определить, как привязать **Speed index** к **Visually complete** или какой размер считается слишком большим при предупреждении о размере ресурсов.

Настройка пороговых значений для выводов водопада

1. Перейдите в **Web**.
2. Выберите приложение для настройки.
3. В правом верхнем углу страницы обзора приложения нажмите **More** (**...**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Advanced setup**.
5. Скорректируйте нужные пороговые значения в разделе **Waterfall finding thresholds**.

### Распределённые трассировки PurePath для видимости в инфраструктуру приложений

Вывод **Traces** отображается, когда браузерный монитор работает с веб-приложением, на стороне сервера которого установлен [OneAgent](/managed/ingest-from/dynatrace-oneagent "Ознакомьтесь с важными концепциями OneAgent и узнайте, как установить и эксплуатировать OneAgent на разных платформах.") с соответствующим мониторингом на стороне сервера. Вывод отображает связанные вызовы сервисов. Если монитор связан с веб-приложением без соответствующего мониторинга на стороне сервера, вывод **Traces** не отображается, поскольку нет отслеживаемых сервисов.

Технология PurePath трассирует веб-запрос через вашу инфраструктуру приложения, позволяя видеть, что стоит за производительностью на уровне приложения. Если один или два запроса занимают большую часть времени на медленной странице, можно перейти к распределённой трассировке, чтобы увидеть, например, слишком ли много запросов к базе данных или один медленный запрос. Затем эту информацию можно использовать для повышения производительности или анализа ошибок.

При выборе вывода связанные запросы и ресурсы выделяются в водопаде. Можно выбрать ссылку в ключевом выводе для перехода ко всем доступным распределённым трассировкам или навести курсор на отдельный запрос для перехода к конкретной распределённой трассировке. Вероятно, вы захотите анализировать распределённые трассировки для [динамических запросов](/managed/discover-dynatrace/get-started/glossary#request "Ознакомьтесь с терминологией Dynatrace.") ([запросов документов](#document-requests) или [XHR](#xhr-requests)), а не для отдельных ресурсов. На изображении ниже при наведении курсора на запрос документа отображается ссылка **View trace** для этого запроса.

![Traces top finding and single request Purepath trace](https://dt-cdn.net/images/waterfalltracesfinding-1121-556a6c6eed.png)

Traces top finding and single request Purepath trace

В представлении списка **Distributed traces** выберите ресурс/запрос и перейдите к просмотру **Trace**.

![Traces accessed from Synthetic waterfall](https://dt-cdn.net/images/tracesfromwaterfall-1491-340c596da0.png)

Traces accessed from Synthetic waterfall

* При высокой нагрузке на процессы Dynatrace OneAgent автоматически корректирует отправляемые данные. Поэтому некоторые распределённые трассировки могут быть недоступны. В таких случаях в выводе **Traces** появляется сообщение об [Adaptive Traffic Management](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Улучшайте работоспособность и производительность Dynatrace Managed с помощью адаптивных функций управления трафиком.").

* Переход от отдельного ресурса (на основе тайм-аутов ресурсов W3C) к распределённой трассировке (зафиксированной OneAgent) обеспечивается путём сравнения URL. Если применяются правила перезаписи или части URL не идентичны на стороне клиента и сервера, кнопка **View trace** для ресурса не отображается. В таких случаях можно получить доступ ко всем распределённым трассировкам через вывод **Traces**.

## Ошибки JavaScript

Можно анализировать детали ошибок JavaScript, обнаруженных при выполнении load actions или XHR actions. Ошибки JavaScript отображаются как красные вертикальные маркеры на графике водопада в точке их возникновения во время выполнения. Щёлкните маркер для анализа деталей этой ошибки. Ошибки JavaScript не приводят к сбою монитора, и сбой монитора напрямую не связан с какими-либо ошибками JavaScript.

![Waterfall JavaScript error](https://dt-cdn.net/images/waterfalljserror-1198-234304aad2.jpg)

Waterfall JavaScript error

При фильтрации [точечного графика](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Узнайте, как анализировать точки данных браузерных мониторов.") по ошибкам JavaScript можно щёлкнуть любую точку данных, чтобы автоматически выбрать событие и загрузить водопад с ошибкой JavaScript.

Страница сведений об ошибке для каждой обнаруженной ошибки JavaScript включает полную трассировку стека, определяющую точную строку кода, ответственную за ошибку. Эта информация может значительно ускорить устранение таких ошибок.

![JavaScript error details](https://dt-cdn.net/images/jserrordetails-1680-b4b1d8ef5d.jpg)

JavaScript error details

## Группировка, фильтры и легенда

Инструменты группировки и фильтрации помогают сосредоточиться на нужных запросах в водопаде. Элементы управления группировкой и фильтрацией можно комбинировать.

**Группировка по домену** организует ресурсы по доменам первой стороны, третьих сторон и CDN. Можно просматривать порядок загрузки и детали тайм-аутов для конкретных доменов.

**Группировка по типу** позволяет видеть основные категории ресурсов первой стороны, третьих сторон и CDN: изображения, скрипты (JavaScript), CSS и прочие.

![Group resources by type](https://dt-cdn.net/images/waterfallgroupbytype1-1206-c6a1a11b85.png)

Group resources by type

Обратите внимание: тайм-ауты уровня группы представляют сквозные тайм-ауты загрузки ресурсов данного типа/домена; они не суммируются, поскольку ресурсы могут загружаться параллельно.

Фильтры позволяют сосредоточиться на ресурсах, наиболее влияющих на пользовательский опыт. Можно просматривать полный водопад или **Focus on** только те ресурсы, которые загружались до значимых событий браузера, таких как DOM interactive или Visually complete.

![Filter resources by browser event](https://dt-cdn.net/images/waterfallfilterbyevent1-1203-ad6b72b76f.png)

Filter resources by browser event

В легенде в нижней части водопада перечислены следующие элементы с подробными описаниями:

* Метрики W3C уровня страницы
* Ошибки JavaScript
* Компоненты тайм-аутов ресурсов

Выберите любой из них для исключения/включения из графика водопада. На изображениях ниже показаны события браузера и компоненты тайм-аутов ресурсов для load actions и XHR actions соответственно.

![Legend for load actions](https://dt-cdn.net/images/legend1loadactionwaterfall-1112-ee3b169f08.png)

Legend for load actions

![Legend for XHR actions](https://dt-cdn.net/images/legendxhractionwaterfall1-1225-a7c2e4c4e0.png)

Legend for XHR actions

## Устранение неполадок, связанных с MV3, в браузерных мониторах

Dynatrace Synthetic Recorder, являющийся расширением браузера Google Chrome, переходит на Manifest Version 3 (MV3) — последнюю итерацию платформы расширений Chrome. В результате этого обязательного перехода в работе Synthetic Recorder происходят изменения, которые могут потребовать обходных решений в конфигурациях браузерных мониторов или коде приложения.

Ознакомьтесь со следующими статьями на [форуме устранения неполадок в сообществе Dynatrace](https://dt-url.net/dy122xtf).

* [Missing XHR actions for third-party iframes](https://dt-url.net/2zg2xr6)
* [Unable to block specific requests owing to limitations on the length of regular expressions](https://dt-url.net/w0i2xhk)
* [`window.dispatchEvent` and `window.addEventListener` functions in application code](https://dt-url.net/1ck2xb1)
* [401 failures on challenge-response pages](https://dt-url.net/62m2x72)