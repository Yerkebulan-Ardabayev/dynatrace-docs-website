---
title: Отправка уведомлений Dynatrace в PagerDuty
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration
scraped: 2026-05-12T11:24:56.771742
---

# Отправка уведомлений Dynatrace в PagerDuty

# Отправка уведомлений Dynatrace в PagerDuty

* Чтение: 3 мин
* Обновлено 25 апреля 2024 г.

Dynatrace предлагает [готовую интеграцию](#out-of-the-box-integration), которая автоматически передаёт уведомления Dynatrace о проблемах в вашу среду PagerDuty. Эта интеграция предоставляет ответственным в PagerDuty ссылку на карточку проблемы Dynatrace.

Пользовательский вебхук

Если вам нужны дополнительные поля уведомлений, вместо готовой интеграции можно настроить [пользовательский вебхук](#custom-integration). Дополнительные сведения о настройке интеграции через пользовательский вебхук в Dynatrace см. в разделе [Интеграция через вебхук](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Узнайте, как настроить уведомления о проблемах через пользовательский вебхук.").

## Готовая интеграция

Чтобы настроить интеграцию уведомлений о проблемах с PagerDuty:

1. В **Dynatrace** перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Выберите **Add notification**.
3. Выберите **PagerDuty** из доступных типов уведомлений.

3. Введите следующую информацию:

   * **Display name** — произвольное имя интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * **Account** — имя вашей учётной записи PagerDuty. Только информационное поле. Не используется в вызове API.
   * **Service name**
     Введите «Dynatrace» как целевое имя сервиса. Только информационное поле. Не используется в вызове API.
   * **Service key**
     Вставьте сюда автоматически сгенерированный ключ сервиса PagerDuty.

     Это значение используется в вызове API и должно совпадать с ключом интеграции PagerDuty. Ключ интеграции PagerDuty уникален и связан с сервисом PagerDuty в каталоге сервисов.
4. Завершите настройку и сохраните.

## Пользовательская интеграция через вебхук

Если вам нужны дополнительные поля уведомлений, используйте эту процедуру для интеграции Dynatrace и PagerDuty через пользовательский вебхук.

1. Перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Выберите **Set up notifications**, а затем **Custom integration**.
3. Настройте интеграцию.
   Пример настроек пользовательской интеграции с PagerDuty

   ![Конфигурация вебхука PagerDuty](https://dt-cdn.net/images/pagerduty-webhook-356-b94d1693cf.png)

   Конфигурация вебхука PagerDuty

   * **Name**
     Только информационное поле. Не используется в вызове API.
   * **Webhook URL**
     Должен быть `https://events.pagerduty.com/v2/enqueue`.
   * **Custom payload**
     Следует структуре payload API очереди PagerDuty.