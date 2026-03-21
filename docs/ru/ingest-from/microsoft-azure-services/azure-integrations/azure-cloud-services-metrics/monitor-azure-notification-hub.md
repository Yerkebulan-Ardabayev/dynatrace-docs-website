---
title: Мониторинг Azure Notification Hub
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-notification-hub
scraped: 2026-03-03T21:25:28.391388
---

* Latest Dynatrace
* How-to guide
* 7-min read

Dynatrace загружает метрики из Azure Metrics API для Azure Notification Hub. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.201+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Enable Azure monitoring in Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** содержит список всех экземпляров (пользовательских устройств), принадлежащих группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса доступен предустановленный дашборд, вы получите его со всеми рекомендуемыми метриками на странице **Дашборды**. Вы можете искать конкретные дашборды, отфильтровав по **Preset**, а затем по **Name**.

Для существующих мониторируемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Дашборды**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем выберите **Save**.

Вносить изменения непосредственно в предустановленный дашборд нельзя, но его можно клонировать и редактировать. Для клонирования дашборда откройте меню (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка, его можно скрыть. Для этого откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Notification hub](https://dt-cdn.net/images/dashboard-60-1408-5577f14a52.png)

## Доступные метрики

| Название | Описание | Единица | Рекомендуется |
| --- | --- | --- | --- |
| incoming | Количество всех успешных вызовов API отправки | Count | Применимо |
| incoming.all.failedrequests | Общее количество неудачных входящих запросов для центра уведомлений | Count | Применимо |
| incoming.all.requests | Общее количество входящих запросов для центра уведомлений | Count | Применимо |
| incoming.scheduled | Отправленные запланированные push-уведомления | Count |  |
| incoming.scheduled.cancel | Отменённые запланированные push-уведомления | Count |  |
| installation.all | Операции управления установкой | Count |  |
| installation.delete | Операции удаления установки | Count |  |
| installation.get | Операции получения установки | Count |  |
| installation.patch | Операции обновления установки | Count |  |
| installation.upsert | Операции создания или обновления установки | Count |  |
| notificationhub.pushes | Все исходящие уведомления центра уведомлений | Count | Применимо |
| outgoing.allpns.badorexpiredchannel | Количество push-уведомлений, которые не удалось доставить из-за истечения срока действия или недействительности канала/токена/registrationId в регистрации | Count |  |
| outgoing.allpns.channelerror | Количество push-уведомлений, которые не удалось доставить из-за недействительности канала, неправильной привязки к приложению, ограничения скорости или истечения срока действия | Count |  |
| outgoing.allpns.invalidpayload | Количество push-уведомлений, которые не удалось доставить из-за ошибки недопустимой полезной нагрузки, возвращённой PNS | Count |  |
| outgoing.allpns.pnserror | Количество push-уведомлений, которые не удалось доставить из-за проблем со связью с PNS (исключая проблемы аутентификации) | Count |  |
| outgoing.allpns.success | Количество всех успешных уведомлений | Count |  |
| outgoing.apns.badchannel | Количество push-уведомлений, которые не удалось доставить из-за недействительного токена (код состояния APNS: 8) | Count |  |
| outgoing.apns.expiredchannel | Количество токенов, признанных недействительными каналом обратной связи APNS | Count |  |
| outgoing.apns.invalidcredentials | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные или учётные данные заблокированы | Count |  |
| outgoing.apns.invalidnotificationsize | Количество push-уведомлений, которые не удалось доставить из-за слишком большой полезной нагрузки (код состояния APNS: `7`) | Count |  |
| outgoing.apns.pnserror | Количество push-уведомлений, которые не удалось доставить из-за ошибок связи с APNS | Count |  |
| outgoing.apns.success | Количество всех успешных уведомлений | Count |  |
| outgoing.gcm.authenticationerror | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные, учётные данные заблокированы или `SenderId` неправильно настроен в приложении (результат GCM: `MismatchedSenderId`) | Count |  |
| outgoing.gcm.badchannel | Количество push-уведомлений, которые не удалось доставить из-за того, что `registrationId` в регистрации не распознан (результат GCM: `Invalid Registration`) | Count |  |
| outgoing.gcm.expiredchannel | Количество push-уведомлений, которые не удалось доставить из-за истечения срока действия `registrationId` в регистрации (результат GCM: `NotRegistered`) | Count |  |
| outgoing.gcm.invalidcredentials | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные или учётные данные заблокированы | Count |  |
| outgoing.gcm.invalidnotificationformat | Количество push-уведомлений, которые не удалось доставить из-за неправильного формата полезной нагрузки (результат GCM: `InvalidDataKey` или `InvalidTtl`) | Count |  |
| outgoing.gcm.invalidnotificationsize | Количество push-уведомлений, которые не удалось доставить из-за слишком большой полезной нагрузки (результат GCM: `MessageTooBig`) | Count |  |
| outgoing.gcm.pnserror | Количество push-уведомлений, которые не удалось доставить из-за ошибок связи с GCM | Count |  |
| outgoing.gcm.success | Количество всех успешных уведомлений | Count |  |
| outgoing.gcm.throttled | Количество push-уведомлений, которые не удалось доставить из-за ограничения скорости GCM для данного приложения (код состояния GCM: `501`-`599` или `result:Unavailable`) | Count |  |
| outgoing.gcm.wrongchannel | Количество push-уведомлений, которые не удалось доставить из-за того, что `registrationId` в регистрации не связан с текущим приложением (результат GCM: `InvalidPackageName`) | Count |  |
| outgoing.mpns.authenticationerror | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные или учётные данные заблокированы | Count |  |
| outgoing.mpns.badchannel | Количество push-уведомлений, которые не удалось доставить из-за того, что `ChannelURI` в регистрации не распознан (статус MPNS: `404 not found`) | Count |  |
| outgoing.mpns.channeldisconnected | Количество push-уведомлений, которые не удалось доставить из-за отключения `ChannelURI` в регистрации (статус MPNS: `412 not found`) | Count |  |
| outgoing.mpns.dropped | Количество push-уведомлений, отброшенных MPNS (заголовок ответа MPNS: X-NotificationStatus: `QueueFull or Suppressed`) | Count |  |
| outgoing.mpns.invalidcredentials | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные или учётные данные заблокированы | Count |  |
| outgoing.mpns.invalidnotificationformat | Количество push-уведомлений, которые не удалось доставить из-за слишком большой полезной нагрузки уведомления | Count |  |
| outgoing.mpns.pnserror | Количество push-уведомлений, которые не удалось доставить из-за ошибок связи с MPNS | Count |  |
| outgoing.mpns.success | Количество всех успешных уведомлений | Count |  |
| outgoing.mpns.throttled | Количество push-уведомлений, которые не удалось доставить из-за ограничения скорости MPNS для данного приложения (WNS MPNS: `406 Not Acceptable`) | Count |  |
| outgoing.wns.authenticationerror | Уведомление не доставлено из-за ошибок связи с Windows Live, недействительных учётных данных или неправильного токена | Count |  |
| outgoing.wns.badchannel | Количество push-уведомлений, которые не удалось доставить из-за того, что ChannelURI в регистрации не распознан (статус WNS: 404 not found) | Count |  |
| outgoing.wns.channeldisconnected | Уведомление отброшено из-за ограничения скорости `ChannelURI` в регистрации (заголовок ответа WNS: X-WNS-DeviceConnectionStatus: `Disconnected`) | Count |  |
| outgoing.wns.channelthrottled | Уведомление отброшено из-за ограничения скорости `ChannelURI` в регистрации (заголовок ответа WNS: X-WNS-NotificationStatus: `ChannelThrottled`) | Count |  |
| outgoing.wns.dropped | Уведомление отброшено из-за ограничения скорости `ChannelURI` в регистрации (X-WNS-NotificationStatus: dropped, но не X-WNS-DeviceConnectionStatus: `Disconnected`) | Count |  |
| outgoing.wns.expiredchannel | Количество push-уведомлений, которые не удалось доставить из-за истечения срока действия `ChannelURI` (статус WNS: `410 Gone`) | Count |  |
| outgoing.wns.invalidcredentials | Количество push-уведомлений, которые не удалось доставить из-за того, что PNS не принял предоставленные учётные данные, учётные данные заблокированы или Windows Live не распознает учётные данные | Count |  |
| outgoing.wns.invalidnotificationformat | Формат уведомления недопустим (статус WNS: `400`). Обратите внимание, что WNS отклоняет не все недопустимые полезные нагрузки | Count |  |
| outgoing.wns.invalidnotificationsize | Полезная нагрузка уведомления слишком велика (статус WNS: `413`) | Count |  |
| outgoing.wns.invalidtoken | Токен, предоставленный WNS, недействителен (статус WNS: `401 Unauthorized`) | Count |  |
| outgoing.wns.pnserror | Уведомление не доставлено из-за ошибок связи с WNS | Count |  |
| outgoing.wns.success | Количество всех успешных уведомлений | Count |  |
| outgoing.wns.throttled | Количество push-уведомлений, которые не удалось доставить из-за ограничения скорости WNS для данного приложения (статус WNS: `406 Not Acceptable`) | Count |  |
| outgoing.wns.tokenproviderunreachable | Windows Live недоступен | Count |  |
| outgoing.wns.wrongtoken | Токен, предоставленный WNS, действителен, но для другого приложения (статус WNS: `403 Forbidden`). Это может произойти, если `ChannelURI` в регистрации связан с другим приложением. | Count |  |
| registration.all | Количество всех успешных операций регистрации (создание, обновление, запросы и удаление) | Count |  |
| registration.create | Количество всех успешных созданий регистрации | Count |  |
| registration.delete | Количество всех успешных удалений регистрации | Count |  |
| registration.get | Количество всех успешных запросов регистрации | Count |  |
| registration.update | Количество всех успешных обновлений регистрации | Count |  |
| scheduled.pending | Ожидающие запланированные уведомления | Count |  |