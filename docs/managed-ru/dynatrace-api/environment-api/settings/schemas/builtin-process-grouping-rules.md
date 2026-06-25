---
title: Settings API - Process grouping rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-grouping-rules
scraped: 2026-05-12T11:45:40.909516
---

# Settings API - Process grouping rules schema table

# Settings API - Process grouping rules schema table

* Опубликовано 05 мая 2025 г.

### Правила группировки процессов (`builtin:process-grouping-rules)`

Dynatrace автоматически мониторит process groups известных технологических типов или потребляющие значительные ресурсы. С помощью process grouping rules можно автоматически мониторить дополнительные технологии.

Подробнее см. в [community post](https://dt-url.net/ea2319k).

Process grouping rules также работают для процессов с [deep monitoring enabled](https://dt-url.net/3203vvp).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:process-grouping-rules` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-grouping-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-grouping-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-grouping-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя custom-технологии `customTechnologyName` | text | Note: сообщается только в full-stack, infrastructure и discovery режимах. | Optional |
| Определить process groups `pgExtraction` | [ProcessGroupExtraction](#ProcessGroupExtraction)[] | Задайте process groups и процессы. | Required |

##### Объект `ProcessGroupExtraction`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| 1.1. Отображаемое имя process group (опц.) `name` | text | Если поле пустое, OneAgent автоматически назначит имя process group по типу процесса и свойствам, таким как имя исполняемого файла. Если ожидается, что правило совпадёт с несколькими процессами, настоятельно рекомендуется заполнить поле, поскольку без него неопределено, какой процесс станет источником имени группы. | Optional |
| 1.2. Сообщать о process group `report` | enum | Auto сообщает только о важных процессах, то есть deep monitored или с высоким потреблением ресурсов Возможные значения: * `always` * `auto` * `never` | Required |
| 1.3. Тип захватываемых процессов (опц.) `processType` | enum | Note: не все типы можно определить при старте.  Ограничьте правило конкретными типами процессов, чтобы не смешивать свойства deep monitored и не получать запутанные результаты. Возможные значения: * `PROCESS_TYPE_APACHE_HTTPD` * `PROCESS_TYPE_GLASSFISH` * `PROCESS_TYPE_GO` * `PROCESS_TYPE_IBM_CICS_REGION` * `PROCESS_TYPE_IBM_IMS_CONTROL` * `PROCESS_TYPE_IBM_IMS_MPR` * `PROCESS_TYPE_IIS_APP_POOL` * `PROCESS_TYPE_JBOSS` * `PROCESS_TYPE_JAVA` * `PROCESS_TYPE_NGINX` * `PROCESS_TYPE_NODE_JS` * `PROCESS_TYPE_PHP` * `PROCESS_TYPE_RUBY` * `PROCESS_TYPE_TOMCAT` * `PROCESS_TYPE_WEBLOGIC` * `PROCESS_TYPE_WEBSPHERE` | Optional |
| `detection` | [DetectionCondition](#DetectionCondition)[] | Задайте правила обнаружения процессов, к которым применяется это правило. **Должно быть задано хотя бы одно правило.** | Required |
| `pgIdSource` | [GroupIdSource](#GroupIdSource) | **3.1. Источник id для process group** | Required |
| `pgiIdSource` | [InstanceIdSource](#InstanceIdSource) | **3.2. Источник id для процесса (опц.)**  Задайте свойство, по которому идентифицируется процесс. | Optional |

##### Объект `DetectionCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| 2.1. Свойство `property` | text | - | Required |
| 2.2. Имя переменной `name` | text | Если Dynatrace обнаруживает это свойство при старте процесса, процесс будет сопоставлен с этим правилом группировки. | Required |
| 2.2. Условие `condition` | text | * $contains(svc), совпадает, если svc встречается где-либо в значении свойства процесса. * $eq(svc.exe), совпадает, если svc.exe точно совпадает со значением свойства процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения свойства процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения свойства процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. [documentation](https://dt-url.net/j142w57). | Required |
| С учётом регистра `caseSensitive` | boolean | Если включено, условия совпадения учитывают регистр. Если выключено, регистр не учитывается | Required |

##### Объект `GroupIdSource`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Standalone-правило `standaloneRule` | boolean | Действительно только для **deep monitored** процессов.  Если параметр выбран, поведение Dynatrace по умолчанию для обнаруженных процессов отключается. Для разделения process group используется только это правило.  Если параметр не выбран, правило вносит вклад в стандартное обнаружение process group Dynatrace.  [See our help page for examples.](https://dt-url.net/1722wrz) | Required |
| 3.1.1. Тип id `type` | enum | Выберите свойство, по которому идентифицируется process group. Можно взять custom-переменную или существующее свойство процесса. Возможные значения: * `CUSTOM` * `EXISTING` | Required |
| 3.1.2. Идентификатор process group `id` | text | Этот идентификатор используется Dynatrace для распознавания process group. | Required |
| 3.1.2. Свойство `property` | text | - | Required |
| Имя переменной `name` | text | Если Dynatrace обнаруживает это свойство при старте процесса, его значение используется для идентификации process group. | Required |
| 3.1.3. Расширенные настройки (опц.) `advancedSettings` | [AdvancedSettings](#AdvancedSettings) | Задайте расширенные параметры для настройки delimiters и обработки значений свойств.  Рассмотрим среду с процессами вида:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * и т.п.  Чтобы сгруппировать production *(prod)* и development *(dev)* процессы вместе, можно использовать свойство Command line с:  * **Delimiter** от `--env=` до `--id` для извлечения `prod12`  и `dev2` * включить **Ignore numbers**, чтобы преобразовать `prod12` в `prod*` и `dev2` в `dev*`. | Optional |

##### Объект `InstanceIdSource`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| 3.2.1. Свойство `property` | text | - | Optional |
| Имя переменной `name` | text | Если Dynatrace обнаруживает это свойство при старте процесса, его значение используется для более гранулярной идентификации process group. | Required |
| 3.2.2. Расширенные настройки (опц.) `advancedSettings` | [AdvancedSettings](#AdvancedSettings) | Задайте расширенные параметры для настройки delimiters и обработки значений свойств.  Рассмотрим среду с процессами вида:  * `python myScript.py --env=prod12 --id=12` * `python myScript.py --env=dev2 --id=2` * и т.п.  Чтобы сгруппировать production *(prod)* и development *(dev)* процессы вместе, можно использовать свойство Command line с:  * **Delimiter** от `--env=` до `--id` для извлечения `prod12`  и `dev2` * включить **Ignore numbers**, чтобы преобразовать `prod12` в `prod*` и `dev2` в `dev*`. | Optional |

##### Объект `AdvancedSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Делимитер от (опц.) `from` | text | - | Optional |
| Делимитер до (опц.) `to` | text | - | Optional |
| Игнорировать числа `ignoreNumbers` | boolean | (например, версии, hex, даты, номера сборок) | Required |