---
title: Отправка Dynatrace уведомлений через вебхуки
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration
scraped: 2026-03-06T21:11:45.096983
---

# Отправка уведомлений Dynatrace через вебхуки


Dynatrace предлагает несколько готовых интеграций, которые автоматически отправляют уведомления о проблемах в сторонние системы управления инцидентами и ChatOps.
Однако если ваша сторонняя система не поддерживается готовой интеграцией, вы можете легко настроить настраиваемую интеграцию через вебхук. При таком подходе всякий раз, когда Dynatrace обнаруживает проблему в вашей среде, затрагивающую реальных пользователей, вебхук запускает запрос `HTTP POST` к целевому URL-адресу, который вы указываете.

Тело сообщения запроса `HTTP POST` полностью настраиваемо. По умолчанию запросы используют корректный синтаксис JSON — за исключением случаев, когда вы определяете другой заголовок типа содержимого HTTP, в этом случае Dynatrace пропускает валидацию JSON и не экранирует полезную нагрузку согласно синтаксису JSON.

Заполнители информации, такие как **{ProblemTitle}** и **{State}**, используются для наполнения пользовательского JSON динамической информацией о каждой обнаруженной проблеме.

Чтобы интегрировать уведомления о проблемах с помощью пользовательского вебхука:

1. Перейдите в **Settings Classic** > **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
3. Выберите **Custom integration** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name**
     Это произвольное имя данной интеграции, которое будет отображаться в Dynatrace в разделе **Settings Classic** > **Integration** > **Problem notifications** после завершения настройки.
   * Необязательно: Включите **Secret webhook URL**.
     Включите этот параметр, чтобы скрыть URL-адрес вебхука (конечную точку вебхука) в настройках уведомлений, обеспечивая дополнительный уровень безопасности путём сокрытия конфиденциальной информации от отображения.
   * **Webhook URL**
     Целевой URL-адрес, на который запрос **HTTP POST** должен отправлять полезную нагрузку. Этот URL может содержать параметры HTTP, такие как токен аутентификации, если целевая система работает с токенами аутентификации вместо базовой аутентификации.
   * Необязательно: **Additional HTTP headers**
     Укажите дополнительные поля HTTP-заголовка, например 'Content-Type' или 'Authorization'. Эти пользовательские поля HTTP-заголовка могут использоваться, если целевой конечной точке требуется токен аутентификации в HTTP-заголовке, или если вы хотите отправить другой тип содержимого, например 'text/plain' или 'application/xml'.
   * **Custom payload**
     После обнаружения или устранения проблемы эта настраиваемая полезная нагрузка отправляется через **HTTP POST** в целевую систему.

     Заполнители

     Раздел **Available placeholders** на странице конфигурации содержит список заполнителей, которые можно использовать для данной интеграции. Заполнители автоматически заменяются информацией, связанной с проблемой, например статусом или заголовком проблемы.
   * Необязательно: Включите **Accept any SSL certificate**.
   * Необязательно: Включите **Call webhook if new events merge into existing problems**.
   * Назначьте профиль оповещения.
5. Выберите **Send test notification**, чтобы убедиться в работоспособности интеграции вебхука.
6. **Save changes**.

## Пример JSON с заполнителями

Ниже приведён пример корректного определения уведомления о проблеме в формате JSON для вебхука:

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

После обнаружения проблемы заполнители заменяются фактическими значениями и результатами, как показано в этом примере полезной нагрузки:

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
