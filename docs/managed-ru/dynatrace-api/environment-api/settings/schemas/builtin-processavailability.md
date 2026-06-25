---
title: Settings API - Process availability schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-processavailability
scraped: 2026-05-12T11:47:40.357918
---

# Settings API - Process availability schema table

# Settings API - Process availability schema table

* Published Dec 05, 2023

### Доступность процессов (`builtin:processavailability)`

Эта функция позволяет мониторить, что на вашем хосте работает минимальное число процессов, попадающих под заданное monitoring rule. Если процессов, соответствующих правилу, недостаточно, вы получаете оповещение. Если дополнительно включить **Process instance snapshots**, вы получаете детальный отчёт об активности самых ресурсоёмких процессов и о последней активности процессов, попадающих под правило.

Чтобы мониторить доступность определённой группы процессов, сначала задайте monitoring rule. Дайте правилу уникальное имя и добавьте detection rules, по которым Dynatrace будет сопоставлять процессы на вашем хосте.

Подробнее см. [Process availability](https://dt-url.net/v923x37)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:processavailability` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:processavailability` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:processavailability` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:processavailability` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя monitoring rule `name` | text | - | Required |
| Операционная система `operatingSystem` | Set<[OperatingSystem](#OperatingSystem)> | Выберите операционные системы, к которым нужно применить monitoring rule. Возможные значения: * `WINDOWS` * `LINUX` * `AIX` | Required |
| Минимальное число подходящих процессов `minimumProcesses` | integer | Укажите минимальное число процессов, попадающих под monitoring rule. Если на каком-либо хосте число процессов опускается ниже этого порога, срабатывает оповещение. | Required |
| Задать detection rules `rules` | [DetectionCondition](#DetectionCondition)[] | Задайте detection rules, выбрав property процесса и условие. У каждого monitoring rule может быть несколько связанных detection rules. | Required |
| Свойства `metadata` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value свойств, прикрепляемых к сработавшему событию. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может быть динамически подставлен (agent 1.325+). | Required |

##### Объект `DetectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Scope правила `ruleType` | enum | Возможные значения: * `RuleTypeProcess` * `RuleTypeHost` | Required |
| Выберите property процесса `property` | enum | Возможные значения: * `executable` * `executablePath` * `commandLine` * `fullCommandLine` * `user` | Required |
| Условие `condition` | text | * $contains(svc), совпадает, если svc встречается в значении property процесса. * $eq(svc.exe), совпадает, если svc.exe точно совпадает со значением property процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения property процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения property процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. [Process availability](https://dt-url.net/v923x37). | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | Host resource attributes, это dimensions, обогащающие хост, в том числе custom metadata, которые представляют собой пары ключ-значение, назначаемые хостам, мониторимым Dynatrace.  Задавая custom metadata, можно обогащать данные мониторинга контекстом, специфичным для нужд вашей организации: имена окружений, team ownership, версии приложений и любые другие релевантные детали.  См. [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw).  Примечание: начиная с версии 1.325 host resource attributes поддерживаются в дополнение к host custom metadata. | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок по ключам. | Required |
| Значение `metadataValue` | text | Введите '{' для подсказок по placeholder'ам. | Required |

##### Объект `HostMetadataCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ должен существовать `keyMustExist` | boolean | При включении условие требует, чтобы resource attribute существовал и удовлетворял ограничениям; при отключении ключ опционален, но если он присутствует, всё равно должен удовлетворять ограничениям. | Required |
| Ключ `metadataKey` | text | - | Required |
| Условие `metadataCondition` | text | Эта строка должна совпадать с требуемым форматом.  * `$match(ver*_1.2.?)`, совпадает со строкой с wildcards: `*`, любое число (включая ноль) символов, `?`, ровно один символ. * `$contains(production)`, совпадает, если `production` встречается в значении host metadata. * `$eq(production)`, совпадает, если `production` точно совпадает со значением host metadata. * `$prefix(production)`, совпадает, если `production` совпадает с префиксом значения host metadata. * `$suffix(production)`, совпадает, если `production` совпадает с суффиксом значения host metadata.  Доступные логические операции:  * `$not($eq(production))`, совпадает, если значение host metadata отличается от `production`. * `$and($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` или заканчивается на `main`.  Скобки **(** и **)**, входящие в сопоставляемое property, **должны экранироваться тильдой (~)** | Required |