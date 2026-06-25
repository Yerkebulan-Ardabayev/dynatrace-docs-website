---
title: Количество действий, потребляемых браузерными clickpath-ами
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths
scraped: 2026-05-12T11:32:15.522695
---

# Количество действий, потребляемых браузерными clickpath-ами

# Количество действий, потребляемых браузерными clickpath-ами

* How-to guide
* 2-min read
* Published May 16, 2018

Dynatrace Synthetic Monitoring создаёт отдельное синтетическое действие для каждого взаимодействия со страницей, генерирующего веб-запрос: загрузки страницы, события навигации или XHR. Синтетические действия (аналог пользовательских действий в Real User Monitoring) хранят данные о производительности, собранные при воспроизведении событий clickpath-а.

Чтобы узнать, сколько синтетических действий потребляет конкретный браузерный clickpath:

1. Перейдите в **Synthetic Classic**.
2. Выберите нужный браузерный clickpath.
3. На странице Synthetic details раздел **Properties** отображает количество синтетических действий (в сравнении с событиями) для данного clickpath-а.

   ![Actions on Synthetic details page](https://dt-cdn.net/images/syntheticdetailsactions-1656-e9e2013dc3.png)

   Actions on Synthetic details page

   Отображается количество действий и событий, частота, расположения и текущее потребление за выбранный период. Количество действий, потребляемых данным clickpath-ом ежедневно, рассчитывается следующим образом.

   `4 executions per hour (runs every 15 minutes) × 24 x 2 locations × 5 actions = 960 synthetic actions`

   На карточке **Synthetic events and actions** можно переключаться между просмотром всех событий (по умолчанию) и только действий (включить **Show events with timings only**).

   ![KPM events](https://dt-cdn.net/images/kpm-events-948-247a3b2545.png)

   KPM events

При записи или редактировании clickpath-а вы заметите, что взаимодействие с веб-приложением фиксируется в виде [событий](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий, создаваемых при записи браузерного clickpath-а."). На снимках экрана ниже показаны события, зафиксированные при [записи скрипта](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") и в [режиме редактирования](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.").

![Browser clickpath events during recording workflow](https://dt-cdn.net/images/clickpatheventsinitial-2150-8146d11425.png)

Browser clickpath events during recording workflow

![Clickpath events in edit mode](https://dt-cdn.net/images/recordedclickpath2-2127-04b0b07f47.png)

Clickpath events in edit mode

Событие не равнозначно действию: действиями называются только события, генерирующие веб-запросы. Поэтому в вашем скрипте может быть меньше действий, чем событий. Такие события, как нажатие на поле ввода или ввод текста в форму, не генерируют сетевых запросов. Они важны с функциональной точки зрения, но не генерируют данных о производительности. При первоначальной [настройке clickpath-а](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") страница Summary чётко отображает количество событий и действий в clickpath-е.

![Clickpath summary](https://dt-cdn.net/images/summaryclickpath1-1676-5c00606bdd.png)

Clickpath summary

Список событий доступен для просмотра и редактирования в любое время: выберите монитор в **Synthetic Classic** > **Edit** > **Recorded clickpath**.

## Связанные темы

* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring (DEM) по модели Dynatrace Platform Subscription.")
* [Digital Experience Monitoring (единицы DEM)](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring на основе единиц DEM.")