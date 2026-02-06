---
title: Problem notifications
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-02-06T15:59:50.823777
---

# Уведомления о проблемах

# Уведомления о проблемах

* 2 минуты чтения
* Обновлено 10 октября 2022 г.

Dynatrace предоставляет полную информацию о мониторинге всей вашей ИТ-операции и автоматически определяет, не соответствует ли какая-либо часть вашего развертывания требуемому качеству с точки зрения производительности или частоты ошибок.Всякий раз, когда Dynatrace обнаруживает такое аномальное поведение системы, она создает единую проблему, объединяющую все инциденты, имеющие одну и ту же основную причину.

Dynatrace позволяет автоматически отправлять уведомления о проблемах в предпочитаемую вами стороннюю службу управления инцидентами или службу ChatOps.Открытые проблемы постоянно обновляются на основе меняющегося воздействия и корреляции событий.Чтобы избежать спама в уведомлениях, уведомления о проблемах передаются сторонним системам только тогда, когда проблемы изначально обнаружены и когда они в конечном итоге решены.

Управление инцидентами

Чат-опсы

Управление корпоративными услугами

Пользовательские интеграции

Эти системы помогают организациям управлять большим количеством инцидентов между несколькими командами.Системы управления инцидентами предлагают такие функции, как отслеживание уведомлений об инцидентах, определение уровня эскалации и графики дежурств.Обычно системы управления инцидентами предлагают широкий спектр каналов уведомлений, таких как колл-центры, пейджеры и мобильные push-уведомления.Dynatrace предлагает готовые интеграции с основными системами управления инцидентами, такими как [Опсгени](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration "Configure Opsgenie integration with Dynatrace."), [ВикторОпс](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration "Learn how to configure VictorOps integration with Dynatrace."), [ПейджерДьюти](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration "Learn how to send problem notifications from Dynatrace to PagerDuty."), [xMatters](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration "Learn how to create problem notifications by adding an xMatters webhook URL from your xMatters instance to Dynatrace settings.") и [Джира](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration "Configure Jira integration with Dynatrace.").

[Джира](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration) [Опсгени](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration) [ПейджерДьюти](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration) [Трелло](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration) [ВикторОпс](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration) [xMatters](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration)

Сегодня системы чата широко используются командами DevOps для сортировки поступающих проблем, обсуждения последующих действий и архивирования извлеченных уроков.Dynatrace предлагает готовые интеграции с популярными системами ChatOps, такими как [Слабый](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration "Set up a Slack problem-notification integration that can keep you updated on all Dynatrace problems.") и [Команды Майкрософт](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration "Set up a Microsoft Teams problem-notification integration that can keep you updated on all Dynatrace-detected problems.").

[Команды Майкрософт](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration) [Слабый](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration)

Системы управления корпоративными услугами широко используются крупными предприятиями для организации всех типов ИТ- и не связанных с ИТ услуг и ресурсов.Эти системы используются компаниями для организации своих ИТ-услуг в соответствии с мировыми стандартами, такими как ITIL (Библиотека инфраструктуры информационных технологий).Все инциденты, связанные с обслуживанием аппаратного и программного обеспечения, отслеживаются и запускают рабочие процессы.Dynatrace предлагает сертифицированную интеграцию с [СервисNow](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration "Connect your monitoring environment with your ServiceNow instance."), самой популярной SaaS-системой управления корпоративными услугами.

[СервисNow](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration)

Если Dynatrace еще не предлагает готовую интеграцию для вашей конкретной системы, вы можете настроить [интеграция электронной почты](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.") или [интеграция вебхука](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Learn how to integrate problem-notifications using a custom webhook.").

[Электронная почта](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration) [Вебхук](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration)