---
title: Отправка Dynatrace уведомлений в PagerDuty
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration
scraped: 2026-03-06T21:11:50.165388
---

# Отправка уведомлений Dynatrace в PagerDuty


* Classic
* 3-min read
* Updated on Apr 25, 2024

Для расширенных возможностей и автоматизации рабочих процессов (например, адресных уведомлений и устранения проблем) см. [Workflows Connectors](../../workflows/actions.md "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

Dynatrace предлагает [готовую интеграцию](#out-of-the-box-integration), которая автоматически передаёт уведомления о проблемах Dynatrace в вашу среду PagerDuty. Эта интеграция предоставляет ответственным сотрудникам PagerDuty ссылку на карточку проблемы в Dynatrace.

Пользовательский webhook

Если вам нужны дополнительные поля уведомлений, вы можете настроить [пользовательский webhook](#custom-integration) вместо готовой интеграции.

## Готовая интеграция

Чтобы настроить интеграцию уведомлений о проблемах с PagerDuty

1. В **Dynatrace** перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Нажмите **Add notification**.
3. Выберите **PagerDuty** из доступных типов уведомлений.

3. Введите следующую информацию:

   * **Display name** — произвольное название этой интеграции, которое будет отображаться в Dynatrace в разделе **Settings** > **Integration** > **Problem notifications** после завершения настройки.
   * **Account** — имя вашей учётной записи PagerDuty. Только информационное поле. Не используется в вызове API.
   * **Service name**
     Введите «Dynatrace» в качестве имени целевой службы. Только информационное поле. Не используется в вызове API.
   * **Service key**
     Вставьте сюда автоматически сгенерированный ключ службы PagerDuty.

     Это значение используется в вызове API и должно совпадать с ключом интеграции PagerDuty, созданным PagerDuty. Ключ интеграции PagerDuty является уникальным и связан со службой PagerDuty, определённой в каталоге служб PagerDuty.
4. Завершите настройку и сохраните.

## Пользовательская интеграция через webhook

Если вам нужны дополнительные поля уведомлений, используйте эту процедуру для интеграции Dynatrace и PagerDuty с помощью пользовательского webhook.

1. Перейдите в **Settings** > **Integration** > **Problem notifications**.
2. Нажмите **Set up notifications** и выберите **Custom integration**.
3. Настройте интеграцию.
   Пример настроек пользовательской интеграции PagerDuty

   ![PagerDuty webhook configuration](https://dt-cdn.net/images/pagerduty-webhook-356-b94d1693cf.png)

   * **Name**
     Только информационное поле. Не используется в вызове API.
   * **Webhook URL**
     Должен быть `https://events.pagerduty.com/v2/enqueue`.
   * **Custom payload**
     Следует структуре полезной нагрузки API очереди PagerDuty.

### Дополнительная информация

* Общие сведения о настройке пользовательской интеграции в Dynatrace см. в разделе [Webhook integration](webhook-integration.md "Learn how to integrate problem-notifications using a custom webhook.").
* Документацию PagerDuty по интеграции PagerDuty с Dynatrace через пользовательский webhook см. в [Dynatrace Integration Guideï»¿](https://www.pagerduty.com/docs/guides/dynatrace-integration-guide/) на сайте PagerDuty.
