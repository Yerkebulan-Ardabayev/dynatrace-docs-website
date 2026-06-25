---
title: Settings API - Trace sampling for HTTP requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-url-based-sampling
scraped: 2026-05-12T11:46:00.163679
---

# Settings API - Trace sampling for HTTP requests schema table

# Settings API - Trace sampling for HTTP requests schema table

* Published Dec 05, 2023

### Trace sampling для HTTP-запросов (`builtin:url-based-sampling)`

Этот параметр позволяет настроить, как OneAgent обрабатывает конкретные HTTP-запросы, когда требуется sampling. Точнее, вы можете указать OneAgent важность конкретных HTTP-запросов относительно других. HTTP-запросы по URL с большей важностью будут чаще захватываться, и наоборот. Дополнительно можно полностью отключить трассировку для конкретных HTTP-запросов. Full-Stack Monitoring включает заданный объём данных трейсов. Каждый учитываемый ГиБ памяти хоста или приложения добавляет в ваше окружение определённый объём ingest rate трейсов. В зависимости от объёма транзакций OneAgent захватывает end-to-end трейсы каждую минуту вплоть до пикового объёма. Adaptive Traffic management автоматически подстраивает sampling rate сбора трейсов так, чтобы собранные данные не превышали включённый объём. Подробнее об этом см. [здесь](https://dt-url.net/2y23wt3)

Подсказка: используйте Multi-dimensional analysis (`<your-dynatrace-url>//ui/diagnostictools/mda?mdaId=atm`) для обзора текущих sample rate по URL. Дополнительно используйте контекстное меню URL для удобного повышения или понижения масштаба отдельных URL.

Эта конфигурация представляет собой упорядоченный список правил. У каждого правила есть условия по методу запроса, URL-пути и query-параметрам. Применяется первое правило, у которого выполнены все условия. Каждое несработавшее правило добавляет накладные расходы в одну микросекунду на мониторимый процесс. Все строковые сравнения условий чувствительны к регистру. Используйте переключатель Enabled, чтобы включать или выключать правило.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:url-based-sampling` | * `group:service-monitoring` * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-based-sampling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:url-based-sampling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-based-sampling` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Отключить трассировку для совпавших HTTP-запросов `ignore` | boolean | Для совпавших HTTP-запросов трейсы захватываться не будут. Это применяется всегда, даже когда Adaptive Traffic Management неактивен. | Required |
| Важность конкретного URL `factor` | enum | Выберите масштабирующий коэффициент для текущего sampling rate системы. Учтите, что важность принимается во внимание только когда требуется sampling. Возможные значения: * `0` * `1` * `2` * `3` * `4` * `5` * `6` * `8` * `9` * `10` * `11` * `12` * `13` * `14` | Required |
| URL-путь `path` | text | Укажите URL-путь, не включая предшествующие или последующие элементы URL. Между двумя сегментами пути можно использовать wildcard '\*\*', чтобы пропустить эту часть. Если путь пустой, для сопоставления URL должен быть указан хотя бы один query-параметр. | Optional |
| Условие сравнения пути `pathComparisonType` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `CONTAINS` * `DOES_NOT_CONTAIN` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `ENDS_WITH` * `DOES_NOT_END_WITH` | Required |
| Query-параметры `queryParameters` | Set<[QueryParameter](#QueryParameter)> | Добавьте URL-параметры в любом порядке. **Все** указанные параметры должны присутствовать в query URL для совпадения. | Required |
| Любой HTTP-метод `httpMethodAny` | boolean | Масштабирующий коэффициент для совпавших URL применяется к любому HTTP-методу. | Required |
| HTTP-метод `httpMethod` | Set<[HttpMethod](#HttpMethod)> | Возможные значения: * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `CONNECT` * `OPTIONS` * `TRACE` * `PATCH` | Required |

##### Объект `QueryParameter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя query-параметра `name` | text | - | Required |
| Значение query-параметра `value` | text | Значение должно быть равно для совпадения. | Optional |
| Значение query-параметра не определено `valueIsUndefined` | boolean | Если включено, значение трактуется как undefined (/...&foo), иначе как пустое (/...&foo=). | Required |