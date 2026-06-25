---
title: Settings API - Frequent issue detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-frequent-issues
scraped: 2026-05-12T11:47:34.594146
---

# Settings API - Frequent issue detection schema table

# Settings API - Frequent issue detection schema table

* Published Dec 05, 2023

### Определение частых проблем (`builtin:anomaly-detection.frequent-issues)`

Dynatrace автоматически обнаруживает частые проблемы за период в одну неделю. Проблема автоматически переводится в категорию частых, если она обнаруживается несколько раз в течение дня и за недельный период и при этом не усугубляется. После классификации как частая, оповещения автоматически отключаются. Если частая проблема усугубляется, оповещения снова отправляются. На этой странице можно отключить определение частых проблем для всех топологических уровней.  
См. [help documentation](https://dt-url.net/ex4v0pcw) об определении частых проблем.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.frequent-issues` | * `group:anomaly-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.frequent-issues` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Определять частые проблемы внутри приложений `detectFrequentIssuesInApplications` | boolean | - | Required |
| Определять частые проблемы внутри транзакций и сервисов `detectFrequentIssuesInTransactionsAndServices` | boolean | - | Required |
| Определять частые проблемы внутри инфраструктуры `detectFrequentIssuesInInfrastructure` | boolean | - | Required |
| Определять частые проблемы на singleton-сущности окружения `detectFrequentIssuesInEnvironment` | boolean | События, поднимаемые на этом уровне, обычно возникают, когда не применима конкретная топологическая сущность, часто на основе данных типа логов и метрик. Это не влияет на обнаружение проблем внутри приложений, транзакций, сервисов или инфраструктуры. | Optional |