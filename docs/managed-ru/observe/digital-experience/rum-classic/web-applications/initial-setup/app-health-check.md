---
title: Проверка работоспособности приложения в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/app-health-check
---

# Проверка работоспособности приложения в RUM Classic

# Проверка работоспособности приложения в RUM Classic

* Практическое руководство
* Чтение: 4 мин
* Обновлено 20 марта 2024 г.

Dynatrace предлагает отдельную страницу, на которой можно проверить работоспособность веб-приложения.

Страница **Application health check** содержит информацию о наиболее распространённых проблемах, которые могут повлиять на веб-приложение. На этой странице можно проверить работоспособность приложения, посмотреть, какие версии RUM JavaScript используются в данный момент, или убедиться, что RUM JavaScript внедрён корректно. Просмотр этой страницы должен быть первым шагом при устранении неполадок RUM, когда данные отсутствуют частично или полностью.

Чтобы перейти на страницу **Application health check**

1. Перейти в **Web**.
2. Выбрать приложение, работоспособность которого нужно проверить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Health check**.

На странице **Application health check** доступны следующие разделы:

[**RUM JavaScript version distribution**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/app-health-check#rum-js-version "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**RUM status**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/app-health-check#rum-status "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**RUM JavaScript injection diagnostics**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/app-health-check#injection-diagnostics "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")

![Application health check page](https://dt-cdn.net/images/app-health-check-3030-5a500c4f25.png)

Application health check page

## RUM JavaScript version distribution

В этом разделе можно узнать, какая версия RUM JavaScript используется в приложении чаще всего, и посмотреть распределение версий RUM JavaScript.

Выбрать **Show more**, чтобы открыть таблицу с количеством запросов (за последние 30 дней и за последние 24 часа) для каждой обнаруженной версии RUM JavaScript.

В этом разделе также показано, для каких версий RUM JavaScript данные RUM отбрасываются. Чтобы получать данные RUM, нужно обновить RUM JavaScript до более новой версии, чем указано в этом разделе.

## RUM status

В разделе **RUM status** можно увидеть, активирован ли RUM для приложения, связанных групп процессов и хостов. Кроме того, этот раздел объясняет, почему Dynatrace не собирает данные RUM для определённых пользовательских сессий.

В этом разделе могут отображаться следующие проблемы и предупреждения, связанные с конфигурацией:

| Проблема или предупреждение | Пояснение |
| --- | --- |
| Not applicable RUM disabled for application | Если RUM отключён для приложения, нужно перейти по указанной ссылке, чтобы включить RUM. |
| Not applicable RUM disabled for process groups | Если RUM отключён для групп процессов, связанных с приложением, нужно перейти по указанным ссылкам, чтобы настроить эти группы процессов. |
| Not applicable RUM disabled for hosts | Если RUM отключён для хостов, связанных с приложением, нужно перейти по указанным ссылкам, чтобы настроить эти хосты. |
| Not applicable Not enough DEM units | Если закончились [DEM units](/managed/license/classic-licensing/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), RUM отключается и Dynatrace не получает данные от приложения. Нужно увеличить квоту DEM unit или включить [DEM overages](/managed/license/classic-licensing/digital-experience-monitoring-units#dem-overages "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."). |
| Information Opt-in mode enabled | Когда включён режим [Data-collection and opt-in mode](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-opt-in-mode-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region."), Dynatrace не собирает данные, пока для конкретных пользовательских сессий не будет вызван специальный метод API. Если нужно, чтобы Dynatrace собирал данные для всех пользовательских сессий, этот режим нужно отключить. |
| Information Do Not Track mode enabled | Когда включён режим [Comply with "Do Not Track" browser settings](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") с опцией **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**, Dynatrace не собирает данные, если у пользователя в браузере включена настройка "Do Not Track". Если нужно игнорировать настройку браузера "Do Not Track" и собирать данные RUM от всех браузеров, этот режим нужно отключить. Как вариант, можно выбрать опцию **Capture anonymous user sessions for "Do Not Track"-enabled browsers**, чтобы отправлять анонимизированные данные из таких браузеров. |

## RUM JavaScript injection diagnostics

Этот раздел содержит информацию о статусе внедрения RUM JavaScript. Здесь можно проверить количество попыток внедрения, узнать соотношение неудачных и успешных внедрений и посмотреть причины сбоев внедрения.

Выбрать **Run injection diagnostics**, чтобы проверить статус внедрения RUM JavaScript.

По завершении диагностики становится доступна следующая информация:

* Количество попыток внедрения
* Список целевых процессов
* Количество и процент неудачных внедрений
* Количество и процент успешных внедрений

Выбрать **Show more**, чтобы посмотреть причины сбоев внедрения и по пять основных URL для каждой проблемы.

Раздел **RUM JavaScript injection diagnostics** не отображается, если приложение не относится к приложениям с автоматическим внедрением, то есть если RUM JavaScript был [добавлен в приложение вручную](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").