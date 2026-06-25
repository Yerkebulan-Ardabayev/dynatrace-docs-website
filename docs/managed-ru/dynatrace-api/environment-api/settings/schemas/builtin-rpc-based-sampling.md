---
title: Settings API - Trace sampling for RPC requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rpc-based-sampling
scraped: 2026-05-12T11:45:54.821599
---

# Settings API - Trace sampling for RPC requests schema table

# Settings API - Trace sampling for RPC requests schema table

* Published Jun 09, 2025

### Trace sampling для RPC-запросов (`builtin:rpc-based-sampling)`

Этот параметр позволяет настроить, как OneAgent обрабатывает конкретные Remote Procedure Calls (RPC), когда требуется sampling. Точнее, вы можете указать OneAgent важность конкретных RPC относительно других RPC. RPC с более высокой важностью будут чаще захватываться, и наоборот. Дополнительно можно полностью отключить трассировку для конкретных RPC. Full-Stack Monitoring включает заданный объём данных трейсов. Каждый учитываемый ГиБ памяти хоста или приложения добавляет в ваше окружение определённый объём ingest rate трейсов. В зависимости от объёма транзакций OneAgent захватывает end-to-end трейсы каждую минуту вплоть до пикового объёма. Adaptive Traffic management автоматически подстраивает sampling rate сбора трейсов так, чтобы собранные данные не превышали включённый объём. Подробнее об этом см. [здесь](https://dt-url.net/na03wq0)

Эта конфигурация представляет собой упорядоченный список правил. У каждого правила есть условия по протоколу, имени удалённой операции, имени удалённого сервиса или имени эндпоинта RPC. Применяется первое правило, у которого выполнены все условия. Каждое несработавшее правило добавляет накладные расходы в одну микросекунду на мониторимый процесс. Все строковые сравнения условий чувствительны к регистру. Используйте переключатель в колонке "Enabled", чтобы включать или выключать правило.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rpc-based-sampling` | * `group:service-monitoring` * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rpc-based-sampling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rpc-based-sampling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rpc-based-sampling` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Отключить трассировку для совпавших RPC-запросов `ignore` | boolean | Для совпавших RPC-запросов трейсы захватываться не будут. Это применяется всегда, даже когда Adaptive Traffic Management неактивен. | Required |
| Важность RPC `factor` | enum | Выберите масштабирующий коэффициент для текущего sampling rate системы. Учтите, что важность принимается во внимание только когда требуется sampling. Возможные значения: * `0` * `1` * `2` * `3` * `4` * `5` * `6` * `8` * `9` * `10` * `11` * `12` * `13` * `14` | Required |
| Протокол `wireProtocolType` | enum | Укажите RPC-протокол, который можно использовать для сопоставления RPC. Возможные значения: * `1` * `2` * `3` * `4` * `5` * `6` * `7` * `8` * `9` * `10` | Required |
| Имя удалённой операции `remoteOperationName` | text | Укажите имя RPC-операции. Если имя удалённой операции пустое, для сопоставления RPC должны быть указаны имя удалённого сервиса или имя эндпоинта. | Optional |
| Условие сравнения имени удалённой операции `remoteOperationNameComparisonType` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Имя удалённого сервиса `remoteServiceName` | text | Укажите имя удалённого сервиса RPC. Если имя удалённого сервиса пустое, для сопоставления RPC должны быть указаны имя удалённой операции или имя эндпоинта. | Optional |
| Условие сравнения имени удалённого сервиса `remoteServiceNameComparisonType` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Имя эндпоинта `endpointName` | text | Укажите имя эндпоинта RPC. Если имя эндпоинта пустое, для сопоставления RPC должны быть указаны имя удалённой операции или имя удалённого сервиса. | Optional |
| Условие сравнения имени эндпоинта `endpointNameComparisonType` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |