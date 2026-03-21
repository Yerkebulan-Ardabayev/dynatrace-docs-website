---
title: Уведомления о проблемах
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-03-06T21:09:42.896584
---

* Классический
* 2-минутное чтение

Dynatrace предоставляет полноценный мониторинг стека технологий для вашей полной ИТ-инфраструктуры и автоматически обнаруживает, если какая-либо часть вашего развертывания не соответствует необходимому качеству с точки зрения производительности или показателей ошибок. Когда Dynatrace обнаруживает такое необычное поведение системы, он создает одну проблему, содержащую все инциденты, которые имеют одну и ту же коренную причину.

Dynatrace позволяет вам автоматически отправлять уведомления о проблемах в вашу предпочитаемую систему управления инцидентами или ChatOps. Открытые проблемы постоянно обновляются на основе эволюционирующего воздействия и коррелирующих событий. Чтобы избежать спама уведомлений, уведомления о проблемах отправляются в системы третьих лиц только тогда, когда проблемы обнаруживаются впервые и когда они окончательно решаются.

Управление инцидентами

ChatOps

Управление корпоративными услугами

Пользовательские интеграции

Эти системы помогают организациям управлять большим количеством инцидентов в нескольких командах. Системы управления инцидентами предлагают функции, такие как отслеживание уведомлений об инцидентах, определение уровней эскалации и графики дежурств. Обычно системы управления инцидентами предлагают широкий спектр каналов уведомлений, таких как колл-центры, пейджеры и мобильные уведомления. Dynatrace предлагает интеграции из коробки для основных систем управления инцидентами, таких как [Opsgenie](problem-notifications/opsgenie-integration.md "Настройка интеграции с Dynatrace."), [VictorOps](problem-notifications/victorops-integration.md "Узнайте, как настроить интеграцию с Dynatrace."), [PagerDuty](problem-notifications/pagerduty-integration.md "Узнайте, как отправлять уведомления о проблемах из Dynatrace в PagerDuty."), [xMatters](problem-notifications/xmatters-integration.md "Узнайте, как создать уведомления о проблемах, добавив URL-адрес вебхука xMatters из вашего экземпляра xMatters в настройки Dynatrace.") и [Jira](problem-notifications/jira-integration.md "Настройка интеграции с Dynatrace.").

[Jira](problem-notifications/jira-integration.md) [Opsgenie](problem-notifications/opsgenie-integration.md) [PagerDuty](problem-notifications/pagerduty-integration.md) [Trello](problem-notifications/trello-integration.md) [VictorOps](problem-notifications/victorops-integration.md) [xMatters](problem-notifications/xmatters-integration.md)

Сегодня системы чата широко используются командами DevOps для выявления входящих проблем, обсуждения последующих действий и архивации уроков, извлеченных из опыта. Dynatrace предлагает интеграции из коробки для популярных систем ChatOps, таких как [Slack](problem-notifications/slack-integration.md "Настройка интеграции уведомлений о проблемах в Slack, которая может поддерживать вас в курсе всех проблем Dynatrace.") и [Microsoft Teams](problem-notifications/microsoft-teams-integration.md "Настройка интеграции уведомлений о проблемах в Microsoft Teams, которая может поддерживать вас в курсе всех проблем, обнаруженных Dynatrace.").

[Microsoft Teams](problem-notifications/microsoft-teams-integration.md) [Slack](problem-notifications/slack-integration.md)

Системы управления корпоративными услугами широко используются крупными предприятиями для организации всех типов ИТ- и не-ИТ-услуг и ресурсов. Эти системы используются компаниями для организации своих ИТ-услуг в соответствии с глобальными стандартами, такими как ITIL (Библиотека инфраструктуры информационных технологий). Все инциденты, связанные с обслуживанием аппаратного и программного обеспечения, отслеживаются и запускают рабочие процессы. Dynatrace предлагает сертифицированную интеграцию с [ServiceNow](problem-notifications/servicenow-integration.md "Подключите вашу среду мониторинга к вашему экземпляру ServiceNow."), самой популярной системой управления корпоративными услугами в формате SaaS.

[ServiceNow](problem-notifications/servicenow-integration.md)

Если Dynatrace еще не предлагает интеграцию из коробки для вашей конкретной системы, вы можете настроить [интеграцию электронной почты](problem-notifications/email-integration.md "Получайте электронные письма всякий раз, когда Dynatrace обнаруживает проблему в вашей среде, которая влияет на реальных пользователей.") или [интеграцию вебхука](problem-notifications/webhook-integration.md "Узнайте, как интегрировать уведомления о проблемах с помощью пользовательского вебхука.").

[Электронная почта](problem-notifications/email-integration.md) [Вебхук](problem-notifications/webhook-integration.md)