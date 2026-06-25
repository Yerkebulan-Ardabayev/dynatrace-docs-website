---
title: Settings API - Log ingest rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-storage-settings
scraped: 2026-05-12T11:43:13.291991
---

# Settings API - Log ingest rules schema table

# Settings API - Log ingest rules schema table

* Published Dec 05, 2023

### Правила ingest логов (`builtin:logmonitoring.log-storage-settings)`

Включайте и исключайте конкретные источники логов для анализа в Dynatrace Log Monitoring. Ingest записей логов работает по правилам ниже, которые используют сопоставители (log path, log levels, process groups, k8s-специфичные селекторы и т.п.).

Чтобы загружать логи, создайте новое правило ingest. Используйте подсказки или введите источник лога вручную. Доступные источники логов можно посмотреть на экранах Process Group Instance. Если нужного источника нет в списке, задайте пользовательский источник лога.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-storage-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-storage-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активно `enabled` | boolean | - | Required |
| Имя `config-item-title` | text | - | Required |
| Отправлять в storage `send-to-storage` | boolean | Если `true`, совпавшие логи включаются в storage. Если `false`, совпавшие логи исключаются из storage. | Required |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |

##### Объект `Matcher`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут `attribute` | enum | Возможные значения: * `dt.entity.process_group` * `log.source` * `log.source.origin` * `log.content` * `loglevel` * `journald.unit` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` * `winlog.eventid` * `winlog.provider` * `winlog.task` * `winlog.opcode` * `winlog.username` * `winlog.keywords` | Required |
| Оператор `operator` | enum | Возможные значения: * `MATCHES` | Required |
| `values` | set | - | Required |