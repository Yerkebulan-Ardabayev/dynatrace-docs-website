---
title: Send Dynatrace notifications to xMatters
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration
scraped: 2026-03-06T21:11:38.259950
---

# Отправка уведомлений Dynatrace в xMatters

# Отправка уведомлений Dynatrace в xMatters

* Classic
* 2-min read
* Updated on Jul 17, 2024

xMatters — это платформа обеспечения доступности цифровых сервисов, которая предотвращает превращение технических проблем в бизнес-инциденты. С помощью этой интеграции xMatters Dynatrace активно передаёт оповещения о проблемах вместе со всеми связанными метаданными в ваш экземпляр xMatters. Вы можете подтверждать оповещения xMatters и оставлять комментарии к проблемам, обнаруженным Dynatrace, с любого удобного устройства. xMatters автоматически записывает ваши ответы в Dynatrace.

## Настройка xMatters

Сведения о настройке xMatters см. на странице [Dynatrace](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace) в документации xMatters Workflows.

Встроенная версия интеграции xMatters, требующая токен API, больше не доступна. Если она нужна вам в качестве справочного материала, см. раздел [Previous versions](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace#PreviousVersions) интеграции Dynatrace в официальной документации xMatters.

## Настройка Dynatrace

1. Перейдите в **Settings** и выберите **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
   Игнорируйте **Save changes** до завершения настройки.
3. Выберите **xMatters** из доступных типов уведомлений.
4. Настройте уведомление:

   * **Display name** — произвольное имя этой интеграции, которое будет отображаться в Dynatrace на странице **Problem notifications** после завершения настройки.
   * **xMatters URL** — URL-адрес вебхука xMatters.
   * Необязательно: включите параметр **Accept any SSL certificate**. Мы рекомендуем использовать действительный SSL-сертификат (даже для внутренних установок), однако для удобства можно пропустить проверку сертификата.
   * Необязательно: **Additional HTTP headers** — пользовательские поля HTTP-заголовка, например `Content-Type` или `Authorization`, которые можно использовать, если целевой конечной точке требуется токен аутентификации в HTTP-заголовке или если вы хотите отправить другой тип содержимого, например `text/plain` или `application/xml`.
   * **Custom payload** — после обнаружения или устранения проблемы этот настраиваемый пейлоад отправляется через **HTTP POST** в целевую систему. Используйте специальные заполнители для динамического заполнения пейлоада информацией о проблеме, такой как состояние или название проблемы.
   * Назначьте [Alerting profile](../alerting-profiles.md "Learn how to create and manage alerting profiles.").
5. Выберите **Send test notification**, чтобы убедиться в работоспособности интеграции с xMatters.
6. Выберите **Save changes**.

После завершения интеграции с Dynatrace вы увидите свою новую интеграцию xMatters в списке интеграций на странице **Problem notifications**.
