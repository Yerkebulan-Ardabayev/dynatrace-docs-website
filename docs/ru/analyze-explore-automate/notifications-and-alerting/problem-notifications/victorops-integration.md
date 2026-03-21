---
title: Отправка Dynatrace уведомлений в VictorOps
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration
scraped: 2026-03-06T21:11:48.414954
---

# Отправка уведомлений Dynatrace в VictorOps


* 2-min read

Dynatrace предлагает готовую интеграцию с VictorOps, которая автоматически передаёт уведомления о проблемах Dynatrace в вашу среду VictorOps.

Чтобы настроить интеграцию уведомлений о проблемах с VictorOps

1. Перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Нажмите **Add notification**.
3. Выберите **VictorOps** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name**
     Это произвольное имя данной интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * **API key**
     Введите здесь автоматически сгенерированный API-ключ VictorOps.

     Чтобы получить API-ключ VictorOps

     1. Перейдите в свою учётную запись VictorOps.
     2. Откройте **Settings** > **Integrations** > **Rest Endpoint** > **Dynatrace** и скопируйте API-ключ.
     3. Вернитесь в Dynatrace и вставьте его в поле **API key**.
   * **Routing key**
     Задайте ключ маршрутизации, чтобы отправлять уведомления о проблемах ответственной команде.
   * **Message**
     Вставьте пользовательское сообщение, включающее текст и заполнители, связанные с проблемой.

     Заполнители

     В разделе **Available placeholders** на странице настройки перечислены заполнители, которые можно использовать для данной интеграции. Заполнители автоматически заменяются значениями в сообщении.
   * Назначьте [Alerting profile](../alerting-profiles.md "Learn how to create and manage alerting profiles.").
5. Нажмите **Send test notification**, чтобы убедиться, что интеграция с VictorOps работает.
6. **Save changes**.
