---
title: Проверка работоспособности вашего приложения
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/app-health-check
scraped: 2026-03-05T21:38:54.552227
---

# Проверка работоспособности приложения

# Проверка работоспособности приложения

* Classic
* Практическое руководство
* 4 минуты чтения
* Обновлено 20 марта 2024 г.

Dynatrace предоставляет специальную страницу для проверки работоспособности веб-приложения.

Страница **Application health check** содержит информацию о наиболее распространённых проблемах, которые могут влиять на веб-приложение. На этой странице можно проверить работоспособность приложения, узнать, какие версии RUM JavaScript используются в данный момент, или убедиться в корректности внедрения RUM JavaScript. Изучение этой страницы должно быть первым шагом при устранении любых проблем с RUM, когда данные отсутствуют частично или полностью.

Чтобы перейти на страницу **Application health check**:

1. Перейдите в раздел **Web**.
2. Выберите приложение, работоспособность которого требуется проверить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**...**) > **Health check**.

На странице **Application health check** доступны следующие разделы:

[**Распределение версий RUM JavaScript**](app-health-check.md#rum-js-version "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**Статус RUM**](app-health-check.md#rum-status "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")[**Диагностика внедрения RUM JavaScript**](app-health-check.md#injection-diagnostics "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")

![Application health check page](https://dt-cdn.net/images/app-health-check-3030-5a500c4f25.png)

## Распределение версий RUM JavaScript

В этом разделе можно узнать, какая версия RUM JavaScript используется наиболее часто в вашем приложении, а также проверить распределение версий RUM JavaScript.

Выберите **Show more**, чтобы отобразить таблицу с количеством запросов за последние 30 дней и 24 часа для каждой обнаруженной версии RUM JavaScript.

В этом разделе также указываются версии RUM JavaScript, для которых данные RUM отбрасываются. Для получения данных RUM обновите RUM JavaScript до версии выше указанной в этом разделе.

## Статус RUM

В разделе **RUM status** можно проверить, активирован ли RUM для вашего приложения, связанных групп процессов и хостов. Кроме того, этот раздел объясняет, почему Dynatrace не фиксирует данные RUM для определённых пользовательских сессий.

В данном разделе могут отображаться следующие проблемы и предупреждения, связанные с конфигурацией RUM:

## Диагностика внедрения RUM JavaScript

Изучите этот раздел, чтобы получить информацию о статусе внедрения RUM JavaScript. Здесь можно проверить количество попыток внедрения, узнать соотношение неудачных и успешных внедрений, а также просмотреть причины сбоев внедрения.

Выберите **Run injection diagnostics**, чтобы проверить статус внедрения RUM JavaScript.

После завершения диагностики доступна следующая информация:

* Количество попыток внедрения
* Список целевых процессов
* Количество и процент неудачных внедрений
* Количество и процент успешных внедрений

Выберите **Show more** для просмотра причин сбоев внедрения и пяти наиболее частых URL-адресов для каждой проблемы.

Раздел **Диагностика внедрения RUM JavaScript** не отображается, если ваше приложение не является автоматически внедряемым приложением — в частности, если вы [вручную вставили RUM JavaScript](set-up-agentless-real-user-monitoring.md "Set up agentless monitoring for your web applications.") на страницы своего приложения.
