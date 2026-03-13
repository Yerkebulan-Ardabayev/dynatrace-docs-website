---
title: Problem notifications
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-03-06T21:09:42.896584
---

# Уведомления о проблемах

# Уведомления о проблемах

* Classic
* Время чтения: 2 мин
* Обновлено 10 октября 2022 г.

Dynatrace обеспечивает полностековый мониторинг вашей ИТ-инфраструктуры и автоматически определяет, если какая-либо часть вашего развертывания не соответствует требуемому качеству с точки зрения производительности или частоты ошибок. Каждый раз, когда Dynatrace обнаруживает такое аномальное поведение системы, создается единая проблема, которая объединяет все инциденты с общей корневой причиной.

Dynatrace позволяет автоматически отправлять уведомления о проблемах в предпочитаемую вами стороннюю систему управления инцидентами или ChatOps-сервис. Открытые проблемы постоянно обновляются по мере изменения влияния и корреляции событий. Чтобы избежать спама уведомлениями, уведомления о проблемах отправляются в сторонние системы только при первоначальном обнаружении проблемы и при её окончательном решении.

Управление инцидентами

ChatOps

Управление корпоративными сервисами

Пользовательские интеграции

Эти системы помогают организациям управлять большим количеством инцидентов в нескольких командах. Системы управления инцидентами предлагают такие функции, как отслеживание уведомлений об инцидентах, определение уровней эскалации и графики дежурств. Как правило, системы управления инцидентами предлагают широкий спектр каналов уведомлений, таких как колл-центры, пейджеры и мобильные push-уведомления. Dynatrace предоставляет готовые интеграции с основными системами управления инцидентами, такими как [Opsgenie](problem-notifications/opsgenie-integration.md "Настройка интеграции Opsgenie с Dynatrace."), [VictorOps](problem-notifications/victorops-integration.md "Узнайте, как настроить интеграцию VictorOps с Dynatrace."), [PagerDuty](problem-notifications/pagerduty-integration.md "Узнайте, как отправлять уведомления о проблемах из Dynatrace в PagerDuty."), [xMatters](problem-notifications/xmatters-integration.md "Узнайте, как создавать уведомления о проблемах, добавив URL-адрес вебхука xMatters из вашего экземпляра xMatters в настройки Dynatrace.") и [Jira](problem-notifications/jira-integration.md "Настройка интеграции Jira с Dynatrace.").

[Jira](problem-notifications/jira-integration.md) [Opsgenie](problem-notifications/opsgenie-integration.md) [PagerDuty](problem-notifications/pagerduty-integration.md) [Trello](problem-notifications/trello-integration.md) [VictorOps](problem-notifications/victorops-integration.md) [xMatters](problem-notifications/xmatters-integration.md)

Сегодня чат-системы широко используются DevOps-командами для сортировки входящих проблем, обсуждения дальнейших действий и архивирования извлеченных уроков. Dynatrace предоставляет готовые интеграции с популярными ChatOps-системами, такими как [Slack](problem-notifications/slack-integration.md "Настройте интеграцию уведомлений о проблемах через Slack, чтобы быть в курсе всех проблем Dynatrace.") и [Microsoft Teams](problem-notifications/microsoft-teams-integration.md "Настройте интеграцию уведомлений о проблемах через Microsoft Teams, чтобы быть в курсе всех обнаруженных Dynatrace проблем.").

[Microsoft Teams](problem-notifications/microsoft-teams-integration.md) [Slack](problem-notifications/slack-integration.md)

Системы управления корпоративными сервисами широко используются крупными предприятиями для организации всех видов ИТ- и не-ИТ-сервисов и ресурсов. Эти системы используются компаниями для организации ИТ-сервисов в соответствии с глобальными стандартами, такими как ITIL (Information Technology Infrastructure Library). Все инциденты, связанные с аппаратными и программными сервисами, отслеживаются и запускают рабочие процессы. Dynatrace предлагает сертифицированную интеграцию с [ServiceNow](problem-notifications/servicenow-integration.md "Подключите вашу среду мониторинга к экземпляру ServiceNow.") -- самой популярной SaaS-системой управления корпоративными сервисами.

[ServiceNow](problem-notifications/servicenow-integration.md)

Если Dynatrace ещё не предоставляет готовую интеграцию для вашей конкретной системы, вы можете настроить [интеграцию по электронной почте](problem-notifications/email-integration.md "Получайте электронные письма каждый раз, когда Dynatrace обнаруживает проблему в вашей среде, затрагивающую реальных пользователей.") или [интеграцию через вебхук](problem-notifications/webhook-integration.md "Узнайте, как интегрировать уведомления о проблемах с помощью пользовательского вебхука.").

[Email](problem-notifications/email-integration.md) [Webhook](problem-notifications/webhook-integration.md)
