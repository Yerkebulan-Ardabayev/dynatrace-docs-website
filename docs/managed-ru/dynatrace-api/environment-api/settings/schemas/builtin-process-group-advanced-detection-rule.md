---
title: Settings API - Advanced detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-advanced-detection-rule
scraped: 2026-05-12T11:46:20.996175
---

# Settings API - Advanced detection rules schema table

# Settings API - Advanced detection rules schema table

* Published Dec 05, 2023

### Расширенные правила обнаружения (`builtin:process-group.advanced-detection-rule)`

Расширенные правила обнаружения process group позволяют адаптировать логику обнаружения для глубоко мониторимых процессов, **используя свойства, которые автоматически обнаруживаются** OneAgent при запуске процесса.

Расширенные правила обнаружения могут извлекать дополнительные идентификаторы process group и instance из процессов, чтобы точно настроить логику автоматического обнаружения OneAgent. [Подробнее о custom process-group detection](https://dt-url.net/1722wrz)

Примечание: правила обнаружения меняют состав, структуру и identity процесс-группы, не только имя. Если нужно изменить только имя по умолчанию, используйте вместо этого naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`).

Правила обнаружения process group влияют только на процессы, глубоко мониторимые Dynatrace OneAgent, и требуют перезапуска процессов, чтобы изменение в идентификации и группировке вступило в силу.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.advanced-detection-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.advanced-detection-rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Обнаружение process group `processDetection` | [processGroupDetection](#processGroupDetection) | Применять это правило к процессам, у которых выбранное свойство содержит указанную строку. | Required |
| Извлечение process group `groupExtraction` | [processGroupExtraction](#processGroupExtraction) | Можно задать свойства, которые будут использоваться для идентификации process groups. | Required |
| Извлечение process instance `instanceExtraction` | [processInstanceExtraction](#processInstanceExtraction) | Можно задать свойства, которые будут использоваться для идентификации process instances. | Required |

##### Объект `processGroupDetection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойство `property` | text | - | Required |
| Содержащаяся строка `containedString` | text | (чувствительно к регистру) | Required |
| Ограничить это правило конкретными типами процессов. `restrictToProcessType` | text | Примечание: не все типы можно определить при запуске. | Optional |

##### Объект `processGroupExtraction`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойство `property` | text | - | Required |
| `delimiter` | [delimiter](#delimiter) | По желанию ограничьте это свойство между *From* и *To*. | Required |
| Самостоятельное правило `standaloneRule` | boolean | Если эта опция выбрана, поведение Dynatrace по умолчанию отключается для обнаруженных процессов. Для разделения process group используется только это правило.  Если опция не выбрана, это правило дополняет обнаружение process group по умолчанию.  [Примеры см. на странице помощи.](https://dt-url.net/1722wrz) | Required |

##### Объект `processInstanceExtraction`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Свойство `property` | text | - | Optional |
| `delimiter` | [delimiter](#delimiter) | По желанию ограничьте это свойство между *From* и *To*. | Required |

##### Объект `delimiter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Разделитель с `from` | text | - | Required |
| Разделитель до `to` | text | - | Required |
| Игнорировать числа `removeIds` | boolean | (например, версии, hex, даты и build-номера) | Required |