---
title: Отправка уведомлений Dynatrace в xMatters
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration
scraped: 2026-05-12T11:24:53.080496
---

# Отправка уведомлений Dynatrace в xMatters

# Отправка уведомлений Dynatrace в xMatters

* Чтение: 2 мин
* Обновлено 17 июля 2024 г.

xMatters — платформа обеспечения доступности цифровых сервисов, предотвращающая превращение технических проблем в бизнес-проблемы. Благодаря этой интеграции Dynatrace активно передаёт оповещения о проблемах вместе со всеми связанными метаданными в ваш экземпляр xMatters. Можно подтверждать оповещения xMatters и комментировать проблемы, обнаруженные Dynatrace, с любого предпочитаемого устройства. xMatters автоматически фиксирует ваши ответы в Dynatrace.

## Настройка xMatters

Для настройки xMatters см. страницу [Dynatrace](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace) в документации xMatters Workflows.

Встроенная версия интеграции xMatters, требующая токен API, больше не доступна. Если она нужна в качестве справки, см. раздел [Previous versions](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace#PreviousVersions) интеграции Dynatrace в официальной документации xMatters.

## Настройка Dynatrace

1. Перейдите в **Settings** и выберите **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
   Игнорируйте **Save changes** до конца настройки.
3. Выберите **xMatters** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name** — произвольное имя интеграции, которое будет отображаться в Dynatrace на странице **Problem notifications** после завершения настройки.
   * **xMatters URL** — URL вебхука xMatters.
   * Необязательно: включите **Accept any SSL certificate**. Рекомендуется использовать действительный SSL-сертификат (даже для внутренних установок), но для удобства можно проигнорировать проверку сертификата.
   * Необязательно: **Additional HTTP headers** — пользовательские HTTP-заголовки, например «Content-Type» или «Authorization», если конечная точка требует токен аутентификации в заголовке или требуется иной тип контента, например «text/plain» или «application/xml».
   * **Custom payload** — после обнаружения или устранения проблемы эта настраиваемая полезная нагрузка передаётся через **HTTP POST** в целевую систему. Используйте специальные заполнители для динамического заполнения нагрузки информацией о проблеме — состоянием или заголовком.
   * Назначьте [профиль оповещений](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Узнайте, как создавать профили оповещений и управлять ими.").
5. Выберите **Send test notification**, чтобы убедиться, что интеграция с xMatters работает.
6. Нажмите **Save changes**.

После завершения интеграции с Dynatrace вновь созданная интеграция с xMatters появится в списке интеграций на странице **Problem notifications**.