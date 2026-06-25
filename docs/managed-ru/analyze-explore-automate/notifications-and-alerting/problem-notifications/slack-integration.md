---
title: Отправка уведомлений Dynatrace в Slack
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration
scraped: 2026-05-12T11:24:54.325253
---

# Отправка уведомлений Dynatrace в Slack

# Отправка уведомлений Dynatrace в Slack

* Чтение: 2 мин
* Обновлено 25 апреля 2024 г.

Интеграция уведомлений о проблемах со Slack позволяет командам всегда быть в курсе потенциальных рисков в приложениях, сервисах и инфраструктуре. Команды также могут использовать интегрированный канал Slack для обсуждения инцидентов, оценки решений и обмена ссылками на похожие проблемы.

## Настройка интеграции со Slack

1. В Slack создайте входящий вебхук (Incoming Webhook) согласно [документации Slack](https://api.slack.com/messaging/webhooks).
2. Скопируйте сгенерированный URL вебхука в буфер обмена. URL вебхука должен выглядеть так: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`.
3. В Dynatrace перейдите в **Settings** > **Integration** > **Problem notifications**.
4. Выберите **Add notification**.
5. Выберите **Slack** из доступных типов уведомлений.
6. Введите следующую информацию:

   * **Display name**
     Произвольное имя интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * **URL**
     Вставьте URL вебхука.
   * **Channel**
     Введите имя канала Slack.
   * **Message**
     Введите пользовательское сообщение — оно может содержать текст и заполнители, связанные с проблемой.

     Заполнители

     В разделе **Available placeholders** на странице настройки перечислены заполнители, доступные для этой интеграции. Заполнители автоматически заменяются реальными значениями.
7. Назначьте [профиль оповещений](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.").
8. Выберите **Send test notification**, чтобы убедиться, что интеграция со Slack работает.
9. **Save changes**.

После этого вы будете получать уведомления Dynatrace о проблемах в своём канале Slack с пользовательским сообщением.

Пример

![Пример интеграции со Slack](https://dt-cdn.net/images/example-1664-91d9af0698.png)

Пример интеграции со Slack

## Устранение неполадок

* [Уведомления о проблемах Dynatrace не поступают в Slack](https://dt-url.net/ti03ks4)