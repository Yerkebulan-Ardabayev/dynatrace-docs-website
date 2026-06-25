---
title: Settings API - OS services monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-os-services-monitoring
scraped: 2026-05-12T11:40:55.878373
---

# Settings API - OS services monitoring schema table

# Settings API - OS services monitoring schema table

* Опубликовано 5 декабря 2023

### Мониторинг OS services (`builtin:os-services-monitoring)`

Настройка оповещений для OS services в нежелательных состояниях для Windows и Linux systemd.
Note: при включении мониторинга для full availability metric происходит расход custom metric. Подробнее см. [documentation](https://dt-url.net/vl03xzk).

Оставьте отзыв об этой функции в [Dynatrace Community](https://dt-url.net/nl02tbm).

Чтобы настроить оповещение для определённой группы OS services, сначала создайте новую политику. Укажите, о каких состояниях службы вы хотите получать оповещения, затем добавьте detection rules, чтобы указать Dynatrace, какие именно OS services вас интересуют. Можно задать несколько detection rules.

Note: политики задаются для каждой поддерживаемой OS отдельно, и часть параметров и свойств между ними различается.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:os-services-monitoring` | * `group:monitoring` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Система `system` | enum | Возможные значения: * `WINDOWS` * `LINUX` | Required |
| Имя правила `name` | text | - | Required |
| Мониторить `monitoring` | boolean | Включите или выключите switch для включения/отключения мониторинга availability metric для этой политики. Availability metrics порождают custom metrics. Примеры расхода см. в [documentation](https://dt-url.net/vl03xzk). Каждый мониторимый service потребляет одну custom metric. **Функция недоступна для настройки на hosts в режиме Discovery** | Required |
| Оповещение `alerting` | boolean | Включите или выключите switch для включения/отключения alerting для этой политики | Required |
| Оповещать, если служба не установлена `notInstalledAlerting` | boolean | По умолчанию Dynatrace не оповещает, если служба не установлена. Включите или выключите switch, чтобы включить или отключить эту функцию | Required |
| Условие статуса службы для alerting `statusConditionWindows` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(paused)`, совпадает со службами в состоянии paused. Доступные логические операции: * `$not($eq(paused))`, совпадает со службами в состоянии, отличном от paused. * `$or($eq(paused),$eq(running))`, совпадает со службами либо в состоянии paused, либо running. Используйте одно из следующих значений как параметр для условия: * `running` * `stopped` * `start_pending` * `stop_pending` * `continue_pending` * `pause_pending` * `paused` | Required |
| Условие статуса службы для alerting `statusConditionLinux` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(failed)`, совпадает со службами в состоянии failed. Доступные логические операции: * `$not($eq(active))`, совпадает со службами в состоянии, отличном от active. * `$or($eq(inactive),$eq(failed))`, совпадает со службами либо в состоянии inactive, либо failed. Используйте одно из следующих значений как параметр для условия: * `reloading` * `activating` * `deactivating` * `failed` * `inactive` * `active` | Required |
| Задержка alerting `alertActivationDuration` | integer | Количество **10-секундных циклов измерений** до срабатывания alerting. Этим значением управляйте скоростью alerting. Минимальное значение 1 равно одному 10-секундному sample. Если задать 30, alerting сработает через 5 минут. | Required |
| Правила обнаружения `detectionConditionsWindows` | [windowsDetectionCondition](#windowsDetectionCondition)[] | - | Required |
| Правила обнаружения `detectionConditionsLinux` | [linuxDetectionCondition](#linuxDetectionCondition)[] | - | Required |
| Свойства `metadata` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value свойств, прикрепляемых к создаваемому event. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может подставляться динамически (agent 1.325+). | Required |

##### Объект `windowsDetectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Scope правила `ruleType` | enum | Возможные значения: * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Свойство службы `property` | enum | Возможные значения: * `DisplayName` * `ServiceName` * `Path` * `StartupType` * `Manufacturer` | Required |
| Условие `condition` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$match(ip?tables*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(ssh)`, совпадает, если `ssh` встречается в значении свойства службы. * `$eq(sshd)`, совпадает, если `sshd` равно значению свойства службы. * `$prefix(ss)`, совпадает, если `ss` является префиксом значения свойства службы. * `$suffix(hd)`, совпадает, если `hd` является суффиксом значения свойства службы. Доступные логические операции: * `$not($eq(sshd))`, совпадает, если значение свойства службы отличается от `sshd`. * `$and($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` и заканчивается на `hd`. * `$or($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` или заканчивается на `hd`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)** | Required |
| Условие `startupCondition` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(manual)`, совпадает со службами, запускаемыми вручную. Доступные логические операции: * `$not($eq(auto))`, совпадает со службами с типом запуска, отличным от Automatic. * `$or($eq(auto),$eq(manual))`, совпадает, если тип запуска службы Automatic либо Manual. Используйте одно из следующих значений как параметр для условия: * `manual` для Manual * `manual_trigger` для Manual (Trigger Start) * `auto` для Automatic * `auto_delay` для Automatic (Delayed Start) * `auto_trigger` для Automatic (Trigger Start) * `auto_delay_trigger` для Automatic (Delayed Start, Trigger Start) * `disabled` для Disabled | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | - | Required |

##### Объект `linuxDetectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Scope правила `ruleType` | enum | Возможные значения: * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Свойство службы `property` | enum | Возможные значения: * `ServiceName` * `StartupType` | Required |
| Условие `condition` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$match(ip?tables*)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(ssh)`, совпадает, если `ssh` встречается в значении свойства службы. * `$eq(sshd)`, совпадает, если `sshd` равно значению свойства службы. * `$prefix(ss)`, совпадает, если `ss` является префиксом значения свойства службы. * `$suffix(hd)`, совпадает, если `hd` является суффиксом значения свойства службы. Доступные логические операции: * `$not($eq(sshd))`, совпадает, если значение свойства службы отличается от `sshd`. * `$and($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` и заканчивается на `hd`. * `$or($prefix(ss),$suffix(hd))`, совпадает, если значение свойства службы начинается с `ss` или заканчивается на `hd`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)** | Required |
| Условие `startupCondition` | text | Строка должна соответствовать требуемому формату. См. [OS services monitoring](https://dt-url.net/vl03xzk). * `$eq(enabled)`, совпадает со службами с типом запуска enabled. Доступные логические операции: * `$not($eq(enabled))`, совпадает со службами с типом запуска, отличным от enabled. * `$or($eq(enabled),$eq(disabled))`, совпадает со службами либо enabled, либо disabled. Используйте одно из следующих значений как параметр для условия: * `enabled` * `enabled-runtime` * `static` * `disabled` | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | Host resource attributes, это dimensions, обогащающие host, включая custom metadata (пользовательские key-value пары, которые можно присваивать hosts, мониторимым Dynatrace). Через custom metadata можно дополнять данные мониторинга контекстом, специфичным для нужд организации: имена environment, ответственность команд, версии приложения и т.д. См. [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw). Note: начиная с версии 1.325 host resource attributes поддерживаются наряду с host custom metadata. | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок ключей. | Required |
| Значение `metadataValue` | text | Введите '{' для подсказок placeholder. | Required |

##### Объект `HostMetadataCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ должен существовать `keyMustExist` | boolean | Когда включено, условие требует, чтобы resource attribute существовал и удовлетворял ограничениям; когда выключено, ключ необязателен, но при наличии всё равно должен удовлетворять ограничениям. | Required |
| Ключ `metadataKey` | text | - | Required |
| Условие `metadataCondition` | text | Строка должна соответствовать требуемому формату. * `$match(ver*_1.2.?)`, совпадает со строкой с wildcards: `*` любое количество (включая ноль) символов и `?` ровно один символ. * `$contains(production)`, совпадает, если `production` встречается в значении host metadata. * `$eq(production)`, совпадает, если `production` равно значению host metadata. * `$prefix(production)`, совпадает, если `production` является префиксом значения host metadata. * `$suffix(production)`, совпадает, если `production` является суффиксом значения host metadata. Доступные логические операции: * `$not($eq(production))`, совпадает, если значение host metadata отличается от `production`. * `$and($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` или заканчивается на `main`. Скобки **(** и **)**, которые являются частью свойства, **должны экранироваться тильдой (~)** | Required |