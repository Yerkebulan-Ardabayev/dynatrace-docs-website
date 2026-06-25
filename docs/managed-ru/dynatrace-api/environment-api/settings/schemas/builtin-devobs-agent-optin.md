---
title: Settings API - Enable Observability For Developers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-devobs-agent-optin
scraped: 2026-05-12T11:44:54.768223
---

# Settings API - Enable Observability For Developers schema table

# Settings API - Enable Observability For Developers schema table

* Published Aug 05, 2024

### Enable Observability For Developers (`builtin:devobs.agent.optin)`

Observability For Developers даёт мгновенный доступ к данным уровня кода без добавления кода или ожидания развёртывания. С Observability For Developers можно быстрее проводить траблшутинг и понимать сложные современные cloud-native приложения.

Примечание: включение Observability For Developers расходует Container Monitoring units.

Подробнее см. [Code Monitoring documentation](https://docs.dynatrace.com/docs/manage/dynatrace-platform-subscription/capabilities/container-monitoring#code-monitoring)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:devobs.agent.optin` | * `group:observability-for-developers` | `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.agent.optin` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:devobs.agent.optin` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:devobs.agent.optin` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Observability For Developers `enabled` | boolean | - | Required |