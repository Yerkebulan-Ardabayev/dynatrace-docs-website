---
title: Отправка Dynatrace уведомлений в Microsoft Teams
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration
scraped: 2026-03-06T21:11:51.891771
---

# Отправка уведомлений Dynatrace в Microsoft Teams


* Classic
* Чтение займёт 2 минуты
* Обновлено 22 янв. 2026 г.

Для расширенных возможностей и автоматизации рабочих процессов (например, целевых уведомлений и устранения проблем) см. раздел [Workflows Connectors](../../workflows/actions.md "Используйте готовые действия Dynatrace для ваших рабочих процессов и интегрируйте Dynatrace со сторонними системами.").

Deprecation

В связи с [выводом из эксплуатации коннекторов Office 365 в Microsoft Teams](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/), эта интеграция устарела, и создание новых коннекторов станет невозможным после 15 августа 2024 года. Существующие коннекторы продолжат работу до конца марта 2026 года.

Следуйте инструкциям Microsoft по переходу с коннекторов Office 365 на Microsoft Workflows.

Уведомления Dynatrace можно отправлять в каналы Microsoft Teams, чтобы ваши команды всегда знали о любых проблемах в ваших приложениях, службах и инфраструктуре. Интеграция канала Microsoft Teams с Dynatrace даёт вашим командам возможность обсуждать инциденты, оценивать решения и ссылаться на аналогичные проблемы, оставаясь в курсе статуса и серьёзности проблем.

Для настройки интеграции Microsoft Teams и Dynatrace

1. В Microsoft Teams создайте Incoming Webhook согласно [официальной документации Microsoft](https://dt-url.net/w3237oc).
2. В Dynatrace перейдите в **Settings** > **Integration** > **Problem notifications**.
3. Нажмите **Add notification**.
4. Выберите **Custom integration** из списка доступных типов уведомлений.
5. Настройте уведомление:

   * Введите **Display name** для этой интеграции. Это произвольное имя интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * Вставьте URL-адрес webhook Microsoft Teams (Microsoft Teams Connector URL) в поле **Webhook URL**.
   * Необязательно: Включите **Accept any SSL certificate**. Мы рекомендуем использовать действительный SSL-сертификат (даже для внутренних установок), но вы можете игнорировать сертификат для удобства.
   * Введите специфический для Microsoft Teams JSON-payload в формате:

     ```
     {


     "title":"{ProblemTitle}",


     "text":"{ProblemDetailsHTML}",


     "themeColor":"EA4300"


     }
     ```

     Формат payload коннектора можно полностью настроить. Подробнее о формате Microsoft Teams Connector см. на этой [странице документации Microsoft](https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference/).
6. Нажмите **Send test notification**, чтобы убедиться в работоспособности интеграции с Teams.
7. **Save changes**.

После интеграции Dynatrace и Microsoft Teams вы будете получать все обнаруженные Dynatrace проблемы непосредственно в каналах Teams.

Example

![Экран Microsoft Teams, интегрированного с Dynatrace](https://dt-cdn.net/images/msteams-integrated-1380-16dcf8dd22.png)
