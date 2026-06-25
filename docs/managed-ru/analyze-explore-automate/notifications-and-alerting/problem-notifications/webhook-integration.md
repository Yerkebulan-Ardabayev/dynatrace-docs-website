---
title: Отправка уведомлений Dynatrace через вебхуки
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration
scraped: 2026-05-12T11:24:48.677530
---

# Отправка уведомлений Dynatrace через вебхуки

# Отправка уведомлений Dynatrace через вебхуки

* Чтение: 3 мин
* Обновлено 11 сентября 2024 г.

Dynatrace предлагает несколько готовых интеграций, автоматически передающих уведомления о проблемах в сторонние системы управления инцидентами и ChatOps. Если ваша система не поддерживается готовой интеграцией, можно легко настроить настраиваемую интеграцию через вебхук. При таком подходе каждый раз, когда Dynatrace обнаруживает проблему, влияющую на реальных пользователей, вебхук инициирует запрос `HTTP POST` к указанному целевому URL.

Полезная нагрузка запроса `HTTP POST` полностью настраиваема. По умолчанию запросы используют валидный синтаксис JSON — за исключением случаев, когда определён иной HTTP-заголовок Content-Type, при котором Dynatrace пропускает проверку JSON и не экранирует полезную нагрузку согласно синтаксису JSON.

Информационные заполнители, такие как **{ProblemTitle}** и **{State}**, используются для заполнения пользовательского JSON динамической информацией о каждой обнаруженной проблеме.

Чтобы настроить уведомления о проблемах через пользовательский вебхук:

1. Перейдите в **Settings Classic** > **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
3. Выберите **Custom integration** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name**
     Произвольное имя интеграции, которое будет отображаться в Dynatrace в разделе **Settings Classic** > **Integration** > **Problem notifications** после завершения настройки.
   * Необязательно: включите **Secret webhook URL**.
     Включите этот параметр для скрытия URL вебхука (конечной точки вебхука) в настройках уведомлений, обеспечивая дополнительный уровень безопасности путём скрытия конфиденциальной информации.
   * **Webhook URL**
     Целевой URL, на который через **HTTP POST** отправляется полезная нагрузка. URL может содержать HTTP-параметры, например токен аутентификации, если целевая система работает с токенами вместо базовой аутентификации.
   * Необязательно: **Additional HTTP headers**
     Укажите дополнительные HTTP-заголовки, например «Content-Type» или «Authorization». Пользовательские HTTP-заголовки используются, если конечная точка требует токен аутентификации в заголовке или если требуется отправить другой тип контента, например «text/plain» или «application/xml».
   * **Custom payload**
     После обнаружения или устранения проблемы эта настраиваемая полезная нагрузка передаётся через **HTTP POST** в целевую систему.

     Заполнители

     В разделе **Available placeholders** на странице настройки перечислены заполнители, доступные для этой интеграции. Заполнители автоматически заменяются информацией о проблеме — состоянием или заголовком.
   * Необязательно: включите **Accept any SSL certificate**.
   * Необязательно: включите **Call webhook if new events merge into existing problems**.
   * Назначьте [профиль оповещений](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.").
5. Выберите **Send test notification**, чтобы убедиться, что интеграция через вебхук работает.
6. **Save changes**.

## Пример JSON с заполнителями

Пример валидного определения уведомления о проблеме через JSON-вебхук:

```
{



"ImpactedEntities": {ImpactedEntities},



"ImpactedEntity": "{ImpactedEntity}",



"PID": "{PID}",



"ProblemDetailsHTML": "{ProblemDetailsHTML}",



"ProblemDetailsJSON": {ProblemDetailsJSON},



"ProblemID": "{ProblemID}",



"ProblemImpact": "{ProblemImpact}",



"ProblemTitle": "{ProblemTitle}",



"Problem URL": "https://example.com",



"State": "{State}",



"Tags": "{Tags}"



}
```

`{ImpactedEntities}` и `{ProblemDetailsJSON}` являются типами данных JSON и не должны заключаться в кавычки.

После обнаружения проблемы заполнители заменяются реальными значениями — пример итоговой полезной нагрузки:

```
{



"ImpactedEntities": [



{"type": "HOST", "name": "MyHost1", "entity": "HOST-XXXXXXXXXXXXX" },



{"type": "SERVICE", "name": "MyService1", "entity": "SERVICE-XXXXXXXXXXXXX"}



],



"ImpactedEntity": "MyHost1, MyService1",



"PID": "99999",



"ProblemDetailsHTML": "<h1>Dynatrace problem notification test run details</h1>",



"ProblemDetailsJSON": {"ID" : "99999" },



"ProblemID": "999",



"ProblemImpact": "INFRASTRUCTURE",



"ProblemTitle": "Dynatrace problem notification test run",



"Problem URL": "https://example.com",



"State": "OPEN",



"Tags": "testtag1, testtag2"



}
```