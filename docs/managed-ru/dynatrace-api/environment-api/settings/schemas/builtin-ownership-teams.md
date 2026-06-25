---
title: Settings API - Ownership teams schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ownership-teams
scraped: 2026-05-12T11:44:41.584561
---

# Settings API - Ownership teams schema table

# Settings API - Ownership teams schema table

* Published Dec 05, 2023

### Команды ответственности (`builtin:ownership.teams)`

Задайте команды и назначьте им зоны ответственности. Свяжите команды с monitored entities в Dynatrace, указывая идентификатор команды в metadata сущности. [See documentation](https://dt-url.net/ownership)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ownership.teams` | * `group:ownership` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.teams` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ownership.teams` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.teams` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя команды `name` | text | - | Required |
| Описание `description` | text | - | Optional |
| Идентификатор команды `identifier` | text | Идентификатор команды используется для ссылки на команду из любой сущности Dynatrace. Если вы используете Kubernetes labels, учтите ограничение в 63 символа, накладываемое ими. | Required |
| Дополнительные идентификаторы `supplementaryIdentifiers` | Set<[SupplementaryIdentifier](#SupplementaryIdentifier)> | Дополнительные идентификаторы команды можно опционально использовать в дополнение к основному идентификатору, чтобы ссылаться на команду из любой сущности Dynatrace. Поддерживается до 3 дополнительных идентификаторов. | Required |
| Зоны ответственности `responsibilities` | [Responsibilities](#Responsibilities) | Включите все назначения ответственности, применимые к данной команде. | Required |
| Контактные данные `contactDetails` | [ContactDetails](#ContactDetails)[] | Задайте опции интеграции с мессенджерами или другие способы связи с командой. | Required |
| Ссылки `links` | [Link](#Link)[] | Включите ссылки на онлайн-ресурсы, где можно найти информацию, относящуюся к зонам ответственности команды. | Required |
| Дополнительная информация `additionalInformation` | [AdditionalInformation](#AdditionalInformation)[] | Задайте пары ключ/значение, дополнительно описывающие команду, например cost center, тип решения или принадлежность к business unit. | Required |
| External ID `externalId` | text | Это поле следует использовать только для целей автоматизации при импорте информации о команде. | Optional |

##### Объект `SupplementaryIdentifier`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Дополнительный идентификатор `supplementaryIdentifier` | text | - | Required |

##### Объект `Responsibilities`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Development `development` | boolean | Отвечает за разработку и сопровождение высококачественного ПО. Development-команды отвечают за изменения кода для устранения регрессий производительности, ошибок и уязвимостей безопасности. | Required |
| Security `security` | boolean | Отвечает за состояние безопасности организации. Команды с зоной ответственности по security должны понимать влияние, приоритет и ответственную команду по устранению уязвимостей безопасности. | Required |
| Operations `operations` | boolean | Отвечает за развёртывание и эксплуатацию ПО с упором на высокую доступность и производительность. Команды с зоной ответственности operations должны понимать влияние, приоритет и ответственную команду по устранению проблем, обнаруженных Dynatrace. | Required |
| Infrastructure `infrastructure` | boolean | Отвечает за администрирование, управление и поддержку IT-инфраструктуры, включая физические серверы, виртуализацию и cloud. Команды с зоной ответственности infrastructure отвечают за устранение проблем с железом, ресурсных ограничений и уязвимостей ОС. | Required |
| Line of Business `lineOfBusiness` | boolean | Отвечает за то, чтобы разрабатываемые приложения соответствовали бизнес-потребностям и требованиям к юзабилити со стороны пользователей, стейкхолдеров, клиентов и внешних партнёров. Команды с зоной ответственности line of business отвечают за понимание customer experience и его влияния на бизнес-цели. | Required |

##### Объект `ContactDetails`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип интеграции `integrationType` | enum | Возможные значения: * `JIRA` * `EMAIL` * `MS_TEAMS` * `SLACK` | Required |
| Email `email` | text | - | Required |
| Team `msTeams` | text | - | Required |
| Jira `jira` | [JiraConnection](#JiraConnection) | - | Required |
| Канал `slackChannel` | text | - | Required |
| URL `url` | text | - | Optional |

##### Объект `Link`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `linkType` | enum | Возможные значения: * `DOCUMENTATION` * `RUNBOOK` * `WIKI` * `DASHBOARD` * `HEALTH_APP` * `URL` * `REPOSITORY` | Required |
| URL `url` | text | - | Required |

##### Объект `AdditionalInformation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `key` | text | - | Required |
| Значение `value` | text | - | Required |
| URL `url` | text | - | Optional |

##### Объект `JiraConnection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Project `project` | text | - | Required |
| Default Assignee `defaultAssignee` | text | - | Required |