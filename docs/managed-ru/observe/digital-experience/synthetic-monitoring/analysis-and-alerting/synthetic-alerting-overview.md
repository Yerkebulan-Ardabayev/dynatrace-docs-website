---
title: Synthetic alerting overview
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview
scraped: 2026-05-12T11:32:07.273784
---

# Synthetic alerting overview

# Synthetic alerting overview

* Explanation
* 7-min read
* Updated on Dec 16, 2024

Синтетические мониторы Dynatrace позволяют отслеживать доступность и производительность. При нарушении порогового значения по доступности или производительности монитор создаёт проблему.

Уведомления о проблемах настраиваются следующим образом:

1. Укажите [пороговые значения](#thresholds).
2. Создайте [профили оповещений](#alerting-profiles), чтобы определить, какие проблемы вызывают уведомления и когда. Это позволяет задавать разные уровни срочности и влияния на клиентов, варьируя доставку оповещений по типу проблемы и её продолжительности.
3. Настройте [интеграции](#integrations) для доставки оповещений, например по электронной почте.
4. Необязательно: настройте [окна обслуживания](#maintenance-windows).

* Даже без настроенных интеграций проблемы автоматически отображаются на странице **Problems**, на [странице Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") для затронутого монитора, а также в [мобильном приложении Dynatrace](/managed/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Узнайте, как подключить окружения Dynatrace к мобильному приложению Dynatrace для получения оповещений о проблемах.").
* Отображение проблем и получение оповещений в течение окон обслуживания зависит от того, как вы [настроили окна обслуживания](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Создавайте окна обслуживания и определяйте их область.").
* Можно применить [глобальную настройку, чтобы всегда исключать окна обслуживания из расчётов доступности Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Поймите расчёты метрик Synthetic Monitoring.") на периоды обслуживания.

Потенциал оповещений Dynatrace Synthetic Monitoring в полной мере реализуется в сочетании с [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом."): вы не только получаете уведомление о проблеме, но и видите, какие реальные пользователи затронуты и где находится первопричина в вашем стеке приложений.

## Пороговые значения

Пороговые значения для создания проблем по доступности и производительности задаются в настройках синтетического монитора после его создания. Перейдите в **Synthetic Classic**, выберите монитор и нажмите **Edit**. Подробнее см. в разделе [Настройка браузерного монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.").

Не забудьте нажать **Save changes** для сохранения настроек монитора.

### Доступность

На вкладке **Outage handling** в разделе **Settings** монитора можно настроить:

* Глобальные проблемы при недоступности всех отслеживаемых расположений (включено по умолчанию) и/или
* Локальные проблемы при заданном числе последовательных сбоев в указанном количестве расположений

Дополнительно можно:

* Включить повторную попытку при ошибке для браузерных мониторов.
* Исключить определённые HTTP-коды статуса из генерации сбоев/ошибок в настройках браузерных мониторов.

Подробнее об обнаружении и разрешении проблем доступности см. в разделах [Настройка браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Узнайте о настройке браузерных мониторов и clickpath-ов.") и [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#availability-problems "Поймите расчёты метрик Synthetic Monitoring.").

### Производительность

На вкладке **Performance thresholds** в разделе **Settings** монитора можно включить пороговые значения производительности и задать пороговое время в секундах для монитора в целом и для каждого действия.

Запись и редактирование clickpath-ов основаны на событиях, а пороговые значения производительности задаются для монитора в целом и для отдельных действий. Разницу между событиями и действиями см. в разделе [Количество действий, потребляемых браузерными clickpath-ами](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.").

Задаётся статическое время производительности в секундах (например, для соответствия SLA). В качестве ориентира можно использовать отображаемую среднюю производительность за последние 24 часа. Значения средней производительности отображаются как для монитора в целом, так и для отдельных событий.

![Performance thresholds](https://dt-cdn.net/images/performancethresholds1-915-98e1ae390c.png)

Performance thresholds

Рекомендуется устанавливать эти пороговые значения не ранее чем через 24 часа после активации монитора, чтобы можно было опираться на отображаемые здесь данные средней производительности.

Подробнее об обнаружении и разрешении проблем производительности см. в разделах [Настройка браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#performance-thresholds "Узнайте о настройке браузерных мониторов и clickpath-ов.") и [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#performance-problems "Поймите расчёты метрик Synthetic Monitoring.").

## Проблемы

Синтетический монитор, нарушающий пороговое значение, создаёт [проблему](/managed/dynatrace-intelligence "Ознакомьтесь с возможностями Davis AI."). Монитор, нарушающий единственное пороговое значение доступности (глобальная доступность или последовательные сбои в указанном числе расположений), создаёт одну проблему независимо от числа возникновений. При нарушении двух пороговых значений создаются две проблемы.

Монитор, нарушающий пороговые значения производительности для монитора в целом и/или отдельных действий, создаёт одну проблему для каждого расположения. Например, если монитор нарушает пороговые значения для суммы всех действий и для отдельного действия в двух расположениях мониторинга, отображаются две проблемы производительности: по одной для каждого расположения.

Область уведомлений о проблемах для активных проблем находится в правом верхнем углу веб-интерфейса Dynatrace. В **Synthetic Classic** мониторы с проблемами выделяются красной рамкой.

![Synthetic dashboard problems](https://dt-cdn.net/images/syntheticdashboardproblems-1249-6b40abc6ed.png)

Synthetic dashboard problems

Выберите нужный монитор, чтобы просмотреть страницу сведений и список активных и разрешённых проблем за выбранный период. Выберите проблему для перехода к её деталям.

![Synthetic details problems](https://dt-cdn.net/images/syntheticmonitorproblems-1445-6095f5f09f.png)

Synthetic details problems

Все проблемы также доступны на странице **Problems**. На изображениях ниже показаны страница **Problems** и сведения о проблеме [производительности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#performance-thresholds "Узнайте о настройке браузерных мониторов и clickpath-ов.") и [доступности](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#outage-handling "Узнайте о настройке браузерных мониторов и clickpath-ов.") (локальный сбой).

Существует три основных [типа проблем](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах, уровнях серьёзности и логике их создания.") для браузерных и HTTP-мониторов:

* Глобальный сбой
* Локальный сбой
* Нарушение порогового значения производительности

![Problems dashboard](https://dt-cdn.net/images/problemsdashboard-1422-a5a00b621f.png)

Problems dashboard

![Performance problem](https://dt-cdn.net/images/problemdetailperformance-1135-d83946a92a.jpg)

Performance problem

![Local availability problem](https://dt-cdn.net/images/problemdetailavailability-1461-9d8d4670f6.jpg)

Local availability problem

Просто войдите в систему с вашими учётными данными, чтобы получать push-уведомления для доступных вам окружений в [мобильном приложении Dynatrace](/managed/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Узнайте, как подключить окружения Dynatrace к мобильному приложению Dynatrace для получения оповещений о проблемах.") для iOS и Android.

![Dynatrace mobile app notifications](https://dt-cdn.net/images/mobileappnotifications-324-abecfcbd89.png)

Dynatrace mobile app notifications

![Dynatrace environments in the mobile app](https://dt-cdn.net/images/mobileapptenants-324-ec733503b6.png)

Dynatrace environments in the mobile app

## Профили оповещений

Профили оповещений позволяют точно контролировать, какие условия вызывают уведомления о проблемах и когда. Перейдите в **Settings** > **Alerting** > **Problem alerting profiles**.

![Create an alerting profile](https://dt-cdn.net/images/alertingprofilessetup-2646-5cb6c11357.png)

Create an alerting profile

Здесь можно назвать и создать новый профиль оповещений (нажмите **Add alerting profile**). Разверните существующий профиль для его редактирования. Созданные здесь профили оповещений доступны для выбора при настройке [интеграций](#integrations) для уведомлений о проблемах.

Оповещения **Availability** и **Slowdown** (**Problem severity level**) относятся к Synthetic Monitoring.

![Add severity rules to an alerting profile](https://dt-cdn.net/images/severityrulecreation-2592-b2a4dc6251.png)

Add severity rules to an alerting profile

По умолчанию системные правила оповещения срабатывают немедленно для проблем доступности и через 30 минут для проблем производительности (Slowdown); эти значения можно изменить.

С помощью профилей оповещений и интеграций можно настраивать разные уровни серьёзности в зависимости от типа проблемы и её продолжительности. Например, профиль Default отправляет оповещения об **Availability** немедленно, а оповещения **Slowdown** (для проблем производительности) через 30 минут.

Разным профилям оповещений можно назначить разных получателей (интеграции), чтобы эскалировать проблему по мере её продолжительности. Например, можно мгновенно уведомлять сетевой операционный центр, а бизнес-подразделение только через час.

Для определения мониторов, которые должны вызывать эти оповещения, также можно использовать теги. Например, с помощью тегов можно настроить так, чтобы только наиболее чувствительные тесты вызывали оповещения определённым заинтересованным сторонам.

## Интеграции

Synthetic Monitoring позволяет интегрироваться со многими сторонними системами, такими как электронная почта, для уведомлений о проблемах. Перейдите в **Settings** > **Integrations** > **Problem notifications** > **Add notification** для настройки интеграции.

![Add a notification for an integration](https://dt-cdn.net/images/notificationsetup-2642-de99d1c606.png)

Add a notification for an integration

![Integrate with notification systems](https://dt-cdn.net/images/notificationtype-2650-f7ee671c56.png)

Integrate with notification systems

Уведомления о проблемах автоматически передаются на дашборд Synthetic и в мобильное приложение Dynatrace даже без настроенных интеграций.

Каждая интеграция предполагает настройку шаблона сообщения, указание получателей, URL, учётных данных и других полей. Шаблоны можно настраивать с помощью нескольких полей. Также можно создать собственную интеграцию с использованием web hooks.

Интеграция всегда связана с единственным профилем оповещений, который отдельно определяет, когда и для каких объектов и типов проблем доставляется оповещение. Изначально интеграция использует профиль оповещений Default. Его можно изменить и добавить собственные профили.

**Чтобы начать получать оповещения**, добавьте свой адрес электронной почты в интеграцию с электронной почтой и свяжите её с профилем оповещений. Убедитесь, что интеграция имеет статус **Active**.

**Чтобы прекратить получать оповещения**, удалите свой адрес электронной почты из интеграции или деактивируйте или удалите интеграцию.

![Select an alerting profile](https://dt-cdn.net/images/alertingprofile-2600-1dc938b8e8.png)

Select an alerting profile

## Окна обслуживания

[Окна обслуживания](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Узнайте, когда использовать окно обслуживания. Ознакомьтесь с поддерживаемыми типами.") — это разовые или повторяющиеся периоды времени, в которые приостанавливается обнаружение проблем и, при необходимости, оповещение. Также можно продолжать обнаружение проблем и оповещение в течение окна обслуживания.

Окна обслуживания настраиваются в **Settings** > **Maintenance windows** > **Monitoring, alerting and availability**. В частности, приведённая ниже настройка позволяет приостановить обнаружение проблем и оповещение. Рекомендуется установить **Disable problem detection during maintenance**, чтобы уведомления не передавались на системные дашборды и через сторонние инструменты.

![Problem detection setting in maintenance windows](https://dt-cdn.net/images/mwindowproblemdetection-433-6d4e871188.png)

Problem detection setting in maintenance windows