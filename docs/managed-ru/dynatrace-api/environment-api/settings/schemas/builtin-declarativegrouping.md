---
title: Settings API - Declarative process grouping schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-declarativegrouping
scraped: 2026-05-12T11:48:37.867364
---

# Settings API - Declarative process grouping schema table

# Settings API - Declarative process grouping schema table

* Published Dec 05, 2023

### Декларативная группировка процессов (`builtin:declarativegrouping)`

Dynatrace автоматически мониторит process group известных типов технологий или потребляющие значительные ресурсы. С декларативной группировкой процессов вы можете автоматически мониторить дополнительные технологии.

Чтобы добавить новую process group, сначала задайте тип технологии. Тип может быть общим именем технологии или пользовательским. С каждым типом технологии можно связать несколько process group.

Затем дайте process group уникальное имя и идентификатор. Это имя используется для идентификации process group во всём Dynatrace-окружении. Наконец, добавьте правила обнаружения, чтобы Dynatrace автоматически распознавал процессы, входящие в эту группу.

Полные подробности см. в [Declarative process grouping](https://dt-url.net/j142w57)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:declarativegrouping` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:declarativegrouping` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:declarativegrouping` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:declarativegrouping` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя мониторимой технологии `name` | text | Примечание: передаётся только в режимах full-stack, infrastructure и discovery. | Required |
| Задайте process group `detection` | [ProcessDefinition](#ProcessDefinition)[] | Введите описательное отображаемое имя process group и уникальный идентификатор, по которым Dynatrace будет распознавать эту process group. | Required |

##### Объект `ProcessDefinition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отображаемое имя process group `processGroupName` | text | - | Required |
| Идентификатор process group `id` | text | Этот идентификатор используется Dynatrace для распознавания этой process group. | Required |
| Сообщать о process group `report` | enum | Это свойство сообщает OneAgent условие, при котором созданная Process group передаётся в Dynatrace. Возможные значения: * `always` * `highResourceUsage` * `never` | Required |
| Задайте правила обнаружения `rules` | [DetectionCondition](#DetectionCondition)[] | Задайте правила обнаружения процессов, выбрав свойство процесса и условие. С каждой process group можно связать несколько правил обнаружения. | Required |

##### Объект `DetectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Выберите свойство процесса `property` | enum | Возможные значения: * `executable` * `executablePath` * `commandLine` | Required |
| Условие `condition` | text | * $contains(svc), совпадает, если svc встречается в любом месте значения свойства процесса. * $eq(svc.exe), совпадает, если svc.exe в точности равно значению свойства процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения свойства процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения свойства процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. в [Declarative process grouping](https://dt-url.net/j142w57). | Required |