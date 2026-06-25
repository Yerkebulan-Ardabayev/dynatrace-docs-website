---
title: Отправка уведомлений Dynatrace в VictorOps
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration
scraped: 2026-05-12T11:24:55.531167
---

# Отправка уведомлений Dynatrace в VictorOps

# Отправка уведомлений Dynatrace в VictorOps

* Чтение: 2 мин
* Обновлено 10 октября 2022 г.

Dynatrace предлагает готовую интеграцию с VictorOps, которая автоматически передаёт уведомления Dynatrace о проблемах в вашу среду VictorOps.

Чтобы настроить интеграцию уведомлений о проблемах с VictorOps:

1. Перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
3. Выберите **VictorOps** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name**
     Произвольное имя интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * **API key**
     Введите здесь автоматически сгенерированный ключ API VictorOps.

     Как получить ключ API VictorOps

     1. Перейдите в свою учётную запись VictorOps.
     2. Перейдите в **Settings** > **Integrations** > **Rest Endpoint** > **Dynatrace** и скопируйте ключ API.
     3. Вернитесь в Dynatrace и вставьте его в поле **API key**.
   * **Routing key**
     Укажите ключ маршрутизации для отправки уведомлений о проблемах ответственной команде.
   * **Message**
     Введите пользовательское сообщение, содержащее текст и заполнители, связанные с проблемой.

     Заполнители

     В разделе **Available placeholders** на странице настройки перечислены заполнители, доступные для этой интеграции. Заполнители автоматически заменяются значениями в сообщении.
   * Назначьте [профиль оповещений](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.").
5. Выберите **Send test notification**, чтобы убедиться, что интеграция с VictorOps работает.
6. **Save changes**.