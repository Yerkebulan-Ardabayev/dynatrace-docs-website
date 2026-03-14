---
title: Problem notifications
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-03-06T21:09:42.896584
---

# Problem notifications


* Classic
* 2-min read
* Updated on Oct 10, 2022

Dynatrace provides full-stack monitoring insights into your complete IT operation and automatically detects if any part of your deployment doesnât fulfill the required quality in terms of performance or error rates. Whenever Dynatrace detects such abnormal system behavior, it creates a single problem that contains all incidents that share the same root cause.

Dynatrace enables you to automatically push problem notifications to your preferred third-party incident management or ChatOps service. Open problems are continuously updated based on evolving impact and correlating events. To avoid notification spam, problem notifications are only pushed to third-party systems when problems are initially detected and when they are ultimately resolved.

Incident management

ChatOps

Enterprise service management

Custom integrations

These systems help organizations manage large amounts of incidents across multiple teams. Incident management systems offer features such as incident-notification tracking, escalation-level definition, and on-duty schedules. Typically, incident management systems offer a wide range of notification channels, such as call centers, pagers, and mobile push notifications. Dynatrace offers out-of-the-box integrations for major incident management systems such as [Opsgenie](problem-notifications/opsgenie-integration.md "Configure Opsgenie integration with Dynatrace."), [VictorOps](problem-notifications/victorops-integration.md "Learn how to configure VictorOps integration with Dynatrace."), [PagerDuty](problem-notifications/pagerduty-integration.md "Learn how to send problem notifications from Dynatrace to PagerDuty."), [xMatters](problem-notifications/xmatters-integration.md "Learn how to create problem notifications by adding an xMatters webhook URL from your xMatters instance to Dynatrace settings."), and [Jira](problem-notifications/jira-integration.md "Configure Jira integration with Dynatrace.").

[Jira](problem-notifications/jira-integration.md) [Opsgenie](problem-notifications/opsgenie-integration.md) [PagerDuty](problem-notifications/pagerduty-integration.md) [Trello](problem-notifications/trello-integration.md) [VictorOps](problem-notifications/victorops-integration.md) [xMatters](problem-notifications/xmatters-integration.md)

Today, chat systems are widely used by DevOps teams to triage incoming issues, discuss follow-up actions and to archive lessons learned. Dynatrace offers out-of-the-box integrations for popular ChatOps systems such as [Slack](problem-notifications/slack-integration.md "Set up a Slack problem-notification integration that can keep you updated on all Dynatrace problems.") and [Microsoft Teams](problem-notifications/microsoft-teams-integration.md "Set up a Microsoft Teams problem-notification integration that can keep you updated on all Dynatrace-detected problems.").

[Microsoft Teams](problem-notifications/microsoft-teams-integration.md) [Slack](problem-notifications/slack-integration.md)

Enterprise service-management systems are widely used by large enterprises to organize all types of IT and non-IT related services and resources. These systems are used by companies to organize their IT services according to global standards, such as ITIL (Information Technology Infrastructure Library). All hardware and software service-related incidents are tracked and trigger workflows. Dynatrace offers a certified integration with [ServiceNow](problem-notifications/servicenow-integration.md "Connect your monitoring environment with your ServiceNow instance."), the most popular SaaS enterprise service-management system.

[ServiceNow](problem-notifications/servicenow-integration.md)

If Dynatrace doesnât yet offer an out-of-the-box integration for your specific system, you can set up an [email integration](problem-notifications/email-integration.md "Get email whenever Dynatrace detects a problem in your environment that affects real users.") or [webhook integration](problem-notifications/webhook-integration.md "Learn how to integrate problem-notifications using a custom webhook.").

[Email](problem-notifications/email-integration.md) [Webhook](problem-notifications/webhook-integration.md)