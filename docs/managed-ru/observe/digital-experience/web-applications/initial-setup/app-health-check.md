---
title: Проверка работоспособности приложения
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/app-health-check
scraped: 2026-05-12T11:34:51.603300
---

# Проверка работоспособности приложения

# Проверка работоспособности приложения

* How-to guide
* 4-min read
* Updated on Mar 20, 2024

Dynatrace предоставляет специальную страницу для проверки работоспособности веб-приложения.

Страница **Application health check** содержит информацию о наиболее распространённых проблемах, которые могут затронуть веб-приложение. На этой странице можно проверить работоспособность приложения, узнать, какие версии RUM JavaScript используются в данный момент, или убедиться в правильности инжекции RUM JavaScript. Изучение этой страницы должно быть первым шагом при устранении неполадок с RUM в случаях, когда данные отсутствуют частично или полностью.

Чтобы перейти на страницу **Application health check**:

1. Перейдите в **Web**.
2. Выберите приложение, работоспособность которого нужно проверить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Health check**.

На странице **Application health check** доступны следующие разделы:

[**RUM JavaScript version distribution**](/managed/observe/digital-experience/web-applications/initial-setup/app-health-check#rum-js-version "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.") [**RUM status**](/managed/observe/digital-experience/web-applications/initial-setup/app-health-check#rum-status "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.") [**RUM JavaScript injection diagnostics**](/managed/observe/digital-experience/web-applications/initial-setup/app-health-check#injection-diagnostics "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")

![Application health check page](https://dt-cdn.net/images/app-health-check-3030-5a500c4f25.png)

Application health check page

## Распределение версий RUM JavaScript

В этом разделе можно узнать, какая версия RUM JavaScript наиболее часто используется в приложении, и проверить распределение версий RUM JavaScript.

Выберите **Show more** для просмотра таблицы с количеством запросов — за последние 30 дней и 24 часа — для каждой обнаруженной версии RUM JavaScript.

В этом разделе также показано, для каких версий RUM JavaScript данные RUM отбрасываются. Для получения данных RUM обновите RUM JavaScript до более поздней версии, чем указанная в этом разделе.

## Статус RUM

В разделе **RUM status** можно видеть, активирован ли RUM для приложения, связанных групп процессов и хостов. Кроме того, этот раздел объясняет, почему Dynatrace не захватывает данные RUM для определённых пользовательских сессий.

В этом разделе могут отображаться следующие связанные с конфигурацией проблемы и предупреждения RUM:

| Проблема или предупреждение | Пояснение |
| --- | --- |
| Not applicable RUM disabled for application | Если RUM отключён для приложения, перейдите по предоставленной ссылке для его включения. |
| Not applicable RUM disabled for process groups | Если RUM отключён для групп процессов, связанных с приложением, перейдите по предоставленным ссылкам для настройки этих групп процессов. |
| Not applicable RUM disabled for hosts | Если RUM отключён для хостов, связанных с приложением, перейдите по предоставленным ссылкам для настройки этих хостов. |
| Not applicable Not enough DEM units | Если исчерпан лимит [единиц DEM](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), RUM отключён и Dynatrace не получает данных от приложения. Увеличьте квоту единиц DEM или включите [превышение DEM](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#dem-overages "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."). |
| Information Opt-in mode enabled | При включённом [режиме сбора данных и явного согласия](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-opt-in-mode-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") Dynatrace не захватывает никаких данных до вызова специального API-метода для конкретных пользовательских сессий. Если Dynatrace должен захватывать данные для всех пользовательских сессий, отключите этот режим. |
| Information Do Not Track mode enabled | При включённом режиме [Comply with "Do Not Track" browser settings](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") с опцией **Turn Real User Monitoring off for "Do Not Track"-enabled browsers** Dynatrace не захватывает никаких данных, если у пользователя включён параметр «Do Not Track» в браузере. Если нужно игнорировать настройку браузера «Do Not Track» и захватывать данные RUM со всех браузеров, отключите режим Do Not Track. Кроме того, можно выбрать опцию **Capture anonymous user sessions for "Do Not Track"-enabled browsers** для отправки анонимизированных данных с таких браузеров. |

## Диагностика инжекции RUM JavaScript

Изучите этот раздел для получения информации о статусе инжекции RUM JavaScript. Можно проверить количество попыток инжекции, соотношение неудачных и успешных инжекций, а также причины неудач.

Выберите **Run injection diagnostics** для проверки статуса инжекции RUM JavaScript.

По завершении диагностики доступна следующая информация:

* Количество попыток инжекции
* Список целевых процессов
* Количество и процент неудачных инжекций
* Количество и процент успешных инжекций

Выберите **Show more** для просмотра причин неудач инжекции и топ-5 URL для каждой проблемы.

Раздел **RUM JavaScript injection diagnostics** не отображается, если приложение не является автоматически инжектируемым — в частности, если [RUM JavaScript был вставлен вручную](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") в страницы приложения.