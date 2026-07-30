---
title: Settings API - OS services monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-os-services-monitoring
---

# Settings API - OS services monitoring schema table

# Settings API - OS services monitoring schema table

* Опубликовано 5 дек. 2023

### OS services monitoring (`builtin:os-services-monitoring`)

Настройка оповещений для OS-сервисов в нежелательных состояниях для Windows и Linux systemd.
Примечание: если мониторинг включён для метрики полной доступности, происходит потребление пользовательских метрик. Подробнее см. [документацию](https://dt-url.net/vl03xzk).

Оставить отзыв об этой функции можно в [Dynatrace Community](https://dt-url.net/nl02tbm).

Чтобы настроить оповещение для определённой группы OS-сервисов, нужно сначала создать новую политику. Укажите, о каких состояниях сервисов нужно получать оповещения, затем добавьте правила обнаружения, чтобы сообщить Dynatrace, какие именно OS-сервисы вас интересуют. Можно задать несколько правил обнаружения.

Политики задаются отдельно для каждой поддерживаемой операционной системы, часть параметров и свойств различается между ними.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:os-services-monitoring` | * `group:monitoring` | `HOST` - Хост  `HOST_GROUP` - Host Group  `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:os-services-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:os-services-monitoring` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с разрешением **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| System `system` | enum | Элемент принимает следующие значения: * `WINDOWS` * `LINUX` | Required |
| Rule name `name` | text | - | Required |
| Monitor `monitoring` | boolean | Переключатель включает или отключает мониторинг метрики доступности для данной политики. Метрики доступности формируют пользовательские метрики. Примеры потребления описаны в [документации﻿](https://dt-url.net/vl03xzk). Каждый отслеживаемый сервис потребляет одну пользовательскую метрику.  **Функцию нельзя настроить на хостах в режиме Discovery** | Required |
| Alert `alerting` | boolean | Переключатель включает или отключает оповещение для данной политики | Required |
| Alert if service is not installed `notInstalledAlerting` | boolean | По умолчанию Dynatrace не отправляет оповещение, если сервис не установлен. Переключатель включает или отключает эту функцию | Required |
| Service status condition for alerting `statusConditionWindows` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$eq(paused)` - совпадает с сервисами в состоянии paused.  Доступные логические операции:  * `$not($eq(paused))` - совпадает с сервисами в состоянии, отличном от paused. * `$or($eq(paused),$eq(running))` - совпадает с сервисами в состоянии paused или running.  В качестве параметра условия используйте одно из следующих значений:  * `running` * `stopped` * `start_pending` * `stop_pending` * `continue_pending` * `pause_pending` * `paused` | Required |
| Service status condition for alerting `statusConditionLinux` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$eq(failed)` - совпадает с сервисами в состоянии failed.  Доступные логические операции:  * `$not($eq(active))` - совпадает с сервисами в состоянии, отличном от active. * `$or($eq(inactive),$eq(failed))` - совпадает с сервисами в состоянии inactive или failed.  В качестве параметра условия используйте одно из следующих значений:  * `reloading` * `activating` * `deactivating` * `failed` * `inactive` * `active` | Required |
| Alerting delay `alertActivationDuration` | integer | Количество **10-секундных циклов измерения** до срабатывания оповещения.  Задайте это значение для управления скоростью оповещения. Минимальное значение равно 1 и соответствует одному 10-секундному замеру. При значении 30 оповещение срабатывает через 5 минут. | Required |
| Detection rules `detectionConditionsWindows` | [windowsDetectionCondition](#windowsDetectionCondition)[] | - | Required |
| Detection rules `detectionConditionsLinux` | [linuxDetectionCondition](#linuxDetectionCondition)[] | - | Required |
| Properties `metadata` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value свойств, прикрепляемых к вызванному событию. Доступные ключи свойств можно получить через [Events API v2﻿](https://dt-url.net/9622g1w). Кроме того, любой атрибут ресурса Host может подставляться динамически (agent 1.325+). | Required |

##### Объект `windowsDetectionCondition`

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | Элемент принимает следующие значения: * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Service property `property` | enum | Элемент принимает следующие значения: * `DisplayName` * `ServiceName` * `Path` * `StartupType` * `Manufacturer` | Required |
| Condition `condition` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$match(ip?tables*)` - совпадает со строкой с подстановочными символами: `*` - любое количество символов (включая ноль), `?` - ровно один символ. * `$contains(ssh)` - совпадает, если `ssh` встречается в значении свойства сервиса. * `$eq(sshd)` - совпадает, если `sshd` точно совпадает со значением свойства сервиса. * `$prefix(ss)` - совпадает, если `ss` является префиксом значения свойства сервиса. * `$suffix(hd)` - совпадает, если `hd` является суффиксом значения свойства сервиса.  Доступные логические операции:  * `$not($eq(sshd))` - совпадает, если значение свойства сервиса отличается от `sshd`. * `$and($prefix(ss),$suffix(hd))` - совпадает, если значение свойства сервиса начинается с `ss` и заканчивается на `hd`. * `$or($prefix(ss),$suffix(hd))` - совпадает, если значение свойства сервиса начинается с `ss` или заканчивается на `hd`.  Скобки **(** и **)**, являющиеся частью проверяемого свойства, **необходимо экранировать тильдой (~)** | Required |
| Condition `startupCondition` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$eq(manual)` - совпадает с сервисами, запускаемыми вручную.  Доступные логические операции:  * `$not($eq(auto))` - совпадает с сервисами с типом запуска, отличным от Automatic. * `$or($eq(auto),$eq(manual))` - совпадает, если тип запуска сервиса равен Automatic или Manual.  В качестве параметра условия используйте одно из следующих значений:  * `manual` для Manual * `manual_trigger` для Manual (Trigger Start) * `auto` для Automatic * `auto_delay` для Automatic (Delayed Start) * `auto_trigger` для Automatic (Trigger Start) * `auto_delay_trigger` для Automatic (Delayed Start, Trigger Start) * `disabled` для Disabled | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | - | Required |

##### Объект `linuxDetectionCondition`

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Rule scope `ruleType` | enum | Элемент принимает следующие значения: * `RuleTypeOsService` * `RuleTypeHost` | Optional |
| Service property `property` | enum | Элемент принимает следующие значения: * `ServiceName` * `StartupType` | Required |
| Condition `condition` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$match(ip?tables*)` - совпадает со строкой с подстановочными символами: `*` - любое количество символов (включая ноль), `?` - ровно один символ. * `$contains(ssh)` - совпадает, если `ssh` встречается в значении свойства сервиса. * `$eq(sshd)` - совпадает, если `sshd` точно совпадает со значением свойства сервиса. * `$prefix(ss)` - совпадает, если `ss` является префиксом значения свойства сервиса. * `$suffix(hd)` - совпадает, если `hd` является суффиксом значения свойства сервиса.  Доступные логические операции:  * `$not($eq(sshd))` - совпадает, если значение свойства сервиса отличается от `sshd`. * `$and($prefix(ss),$suffix(hd))` - совпадает, если значение свойства сервиса начинается с `ss` и заканчивается на `hd`. * `$or($prefix(ss),$suffix(hd))` - совпадает, если значение свойства сервиса начинается с `ss` или заканчивается на `hd`.  Скобки **(** и **)**, являющиеся частью проверяемого свойства, **необходимо экранировать тильдой (~)** | Required |
| Condition `startupCondition` | text | Строка должна соответствовать обязательному формату. См. [мониторинг сервисов ОС﻿](https://dt-url.net/vl03xzk).  * `$eq(enabled)` - совпадает с сервисами, у которых тип запуска равен enabled.  Доступные логические операции:  * `$not($eq(enabled))` - совпадает с сервисами с типом запуска, отличным от enabled. * `$or($eq(enabled),$eq(disabled))` - совпадает с сервисами, у которых тип запуска равен enabled или disabled.  В качестве параметра условия используйте одно из следующих значений:  * `enabled` * `enabled-runtime` * `static` * `disabled` * `indirect` * `linked` * `linked-runtime` | Required |
| Resource attribute `hostMetadataCondition` | [HostMetadataCondition](#HostMetadataCondition) | Атрибуты ресурса Host, это измерения, обогащающие хост, включая пользовательские метаданные, то есть определяемые пользователем пары ключ-значение, назначаемые хостам, которые отслеживает Dynatrace.  Пользовательские метаданные позволяют дополнить данные мониторинга контекстом, специфичным для нужд организации: именами окружений, принадлежностью командам, версиями приложений и другими сведениями.  См. [Определение тегов и метаданных для хостов﻿](https://dt-url.net/w3hv0kbw).  Примечание: начиная с версии 1.325 поддерживаются атрибуты ресурса Host в дополнение к пользовательским метаданным хоста. | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Key `metadataKey` | text | Введите `dt.` для подсказок по ключам. | Required |
| Value `metadataValue` | text | Введите `{` для подсказок по плейсхолдерам. | Required |

##### Объект `HostMetadataCondition`

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Key must exist `keyMustExist` | boolean | При включённом параметре условие требует, чтобы атрибут ресурса существовал и соответствовал ограничениям; при отключённом ключ необязателен, но при наличии должен соответствовать ограничениям. | Required |
| Key `metadataKey` | text | - | Required |
| Condition `metadataCondition` | text | Строка должна соответствовать обязательному формату.  * `$match(ver*_1.2.?)` - совпадает со строкой с подстановочными символами: `*` - любое количество символов (включая ноль), `?` - ровно один символ. * `$contains(production)` - совпадает, если `production` встречается в значении метаданных хоста. * `$eq(production)` - совпадает, если `production` точно совпадает со значением метаданных хоста. * `$prefix(production)` - совпадает, если `production` является префиксом значения метаданных хоста. * `$suffix(production)` - совпадает, если `production` является суффиксом значения метаданных хоста.  Доступные логические операции:  * `$not($eq(production))` - совпадает, если значение метаданных хоста отличается от `production`. * `$and($prefix(production),$suffix(main))` - совпадает, если значение метаданных хоста начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))` - совпадает, если значение метаданных хоста начинается с `production` или заканчивается на `main`.  Скобки **(** и **)**, являющиеся частью проверяемого свойства, **необходимо экранировать тильдой (~)** | Required |