---
title: Уведомления о проблемах
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-05-12T11:06:37.331814
---

# Уведомления о проблемах

# Уведомления о проблемах

* Чтение: 2 мин
* Обновлено 10 октября 2022 г.

Dynatrace предоставляет полный мониторинг всей IT-инфраструктуры и автоматически обнаруживает, если любая часть вашего развёртывания не соответствует требованиям по производительности или показателям ошибок. Каждый раз, когда Dynatrace обнаруживает такое нештатное поведение системы, создаётся единая проблема, содержащая все инциденты с одной и той же первопричиной.

Dynatrace позволяет автоматически отправлять уведомления о проблемах в предпочитаемую стороннюю систему управления инцидентами или ChatOps-сервис. Открытые проблемы непрерывно обновляются по мере изменения масштаба влияния и появления коррелирующих событий. Чтобы избежать спама уведомлениями, уведомления о проблемах отправляются в сторонние системы только при первоначальном обнаружении проблемы и при её окончательном устранении.

Управление инцидентами

ChatOps

Управление корпоративными сервисами

Пользовательские интеграции

Эти системы помогают организациям управлять большим количеством инцидентов в разных командах. Системы управления инцидентами предлагают такие функции, как отслеживание уведомлений об инцидентах, определение уровней эскалации и расписания дежурств. Как правило, системы управления инцидентами предлагают широкий спектр каналов уведомлений — колл-центры, пейджеры и мобильные push-уведомления. Dynatrace предлагает готовые интеграции с крупнейшими системами управления инцидентами: [Opsgenie](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration "Настройте интеграцию Opsgenie с Dynatrace."), [VictorOps](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration "Узнайте, как настроить интеграцию VictorOps с Dynatrace."), [PagerDuty](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration "Узнайте, как отправлять уведомления о проблемах из Dynatrace в PagerDuty."), [xMatters](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration "Узнайте, как создавать уведомления о проблемах, добавив URL-адрес вебхука xMatters из вашего экземпляра xMatters в настройки Dynatrace.") и [Jira](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration "Настройте интеграцию Jira с Dynatrace.").

[Jira](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration) [Opsgenie](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration) [PagerDuty](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration) [Trello](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration) [VictorOps](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration) [xMatters](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration)

Сегодня системы чата широко используются DevOps-командами для сортировки входящих проблем, обсуждения последующих действий и архивирования извлечённых уроков. Dynatrace предлагает готовые интеграции с популярными ChatOps-системами — [Slack](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration "Настройте интеграцию уведомлений о проблемах со Slack.") и [Microsoft Teams](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration "Настройте интеграцию уведомлений о проблемах с Microsoft Teams.").

[Microsoft Teams](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration) [Slack](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration)

Системы управления корпоративными сервисами широко используются крупными предприятиями для организации всех типов IT- и не-IT-сервисов и ресурсов. Такие системы применяются компаниями для организации IT-сервисов в соответствии с глобальными стандартами, например ITIL (Information Technology Infrastructure Library). Все инциденты, связанные с аппаратными и программными сервисами, отслеживаются и запускают рабочие процессы. Dynatrace предлагает сертифицированную интеграцию с [ServiceNow](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration "Подключите свою среду мониторинга к экземпляру ServiceNow.") — наиболее популярной SaaS-системой управления корпоративными сервисами.

[ServiceNow](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration)

Если Dynatrace ещё не предлагает готовой интеграции для вашей конкретной системы, можно настроить [интеграцию по электронной почте](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Получайте электронные письма при обнаружении Dynatrace проблем, влияющих на реальных пользователей.") или [интеграцию через вебхук](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Узнайте, как настроить уведомления о проблемах через пользовательский вебхук.").

[Email](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration) [Webhook](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration)