---
title: Справочник команд Dynatrace Monaco CLI
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/reference/commands
scraped: 2026-05-12T12:35:01.236249
---

# Dynatrace Monaco CLI command reference

# Dynatrace Monaco CLI command reference

* Reference
* 23-min read
* Updated on Nov 13, 2025

Данная шпаргалка по командам Dynatrace Configuration as Code через Monaco (Dynatrace Monaco CLI) описывает основные команды для управления конфигурационными файлами.

## Команда deploy

Команда `deploy` развёртывает конфигурации в окружения, определённые в заданном файле [манифеста развёртывания](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").

### Использование

`monaco deploy graph <manifest.yaml> [flags]`

#### Пример

Наиболее простой способ использования `deploy` — запустить команду без флагов, передав имя файла манифеста развёртывания. При этом все конфигурации из раздела `project` файла манифеста применяются ко всем окружениям, определённым в разделе `environments`.

```
monaco deploy manifest.yaml
```

### Позиционные аргументы (обязательные)

| Аргумент | Описание |
| --- | --- |
| `<manifest.yaml>` | Файл манифеста, определяющий проекты для развёртывания и целевые окружения. |

### Флаги (необязательные)

| Флаг | Описание |
| --- | --- |
| `--continue-on-error` или `-c` | Продолжать развёртывание при возникновении ошибки. Позволяет применить все корректные конфигурации к окружениям, даже если другие некорректны или не удалось развернуть. Использование этого флага может привести к цепочке ошибок для взаимозависимых конфигураций. |
| `--dry-run` или `-d` | Проверить структуру файлов конфигурации без их развёртывания. При установленном флаге `monaco deploy` проверяет корректность JSON-шаблонов и возможность разбора YAML-файлов конфигурации. `dry-run` не подключается к Dynatrace и не может проверить содержимое отправляемого JSON. Развёртывание всё равно может завершиться ошибками HTTP 400 Bad Request после успешного `dry-run`, если содержимое JSON-шаблона некорректно. |
| `--environment <name>` или `-e <name>` | Применить конфигурации к конкретным окружениям из файла манифеста. Для указания нескольких окружений повторите флаг или разделите значения запятой (`,`). Флаг взаимоисключающий с `--group`. Если флаг не задан, используются все окружения. |
| `--group <name>` или `-g <name>` | Применить конфигурации к конкретным [группам окружений](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."). Флаг взаимоисключающий с `--environment`. Если флаг не задан, используются все окружения. |
| `--project <name>` или `-p <name>` | Задать один или несколько проектов для развёртывания. Если флаг не задан, развёртываются все проекты из манифеста. |

### Прокси

В окружениях, где доступ к API Dynatrace возможен только через прокси-сервер, Dynatrace Monaco CLI предоставляет опцию указания адреса прокси при выполнении команды:

Linux/macOS

Windows

```
HTTPS_PROXY=localhost:5000 monaco deploy example.yaml
```

```
$env:HTTPS_PROXY="localhost:5000"



monaco deploy example.yaml
```

## Команда download

Команда `download` позволяет загружать конфигурации из окружения Dynatrace в виде файлов Dynatrace Monaco CLI. Используйте эту возможность, чтобы не начинать с нуля.

### Использование

Подключение к окружению Dynatrace для загрузки можно определить двумя способами: через файл манифеста или путём прямого указания параметров через флаги CLI.

`monaco download [connection flags] [flags]`

Справка

Для просмотра всех опций используйте флаг `--help`:

```
monaco download --help
```

#### Через манифест

1. [Создайте файл манифеста](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."), если его ещё нет.
2. Запустите Dynatrace Monaco CLI с командой `download`:

   ```
   monaco download --manifest your-manifest.yaml --environment environment-name
   ```

   Если вы назвали файл манифеста по умолчанию — `manifest.yaml` — флаг `manifest` можно опустить:

   ```
   monaco download --environment environment-name
   ```

##### Флаги подключения (обязательные)

| Флаг | Описание |
| --- | --- |
| `--manifest <filepath>` или `-m <filepath>` | Путь к файлу манифеста для информации о подключении. По умолчанию: `manifest.yaml` в текущей папке. |
| `--environment <name>` или `-e <name>` | Задать окружение из манифеста для загрузки конфигураций. |

#### Прямая загрузка

Флаги команды позволяют загрузить окружение напрямую без использования манифеста.

Аутентификация

Секреты аутентификации всегда загружаются из переменных окружения, поэтому при использовании флага `--token` необходимо передавать имя переменной, а не сам секрет.

В примере переменная окружения называется `ACCESS_TOKEN_ENV_VAR`.

Команда `monaco download --url https://env.dynatrace.com --token ACCESS_TOKEN_ENV_VAR` создаст манифест для начала работы.

После прямой загрузки у вас будет всё необходимое для `deploy` загруженной конфигурации.

##### Флаги подключения (обязательные)

| Флаг | Описание |
| --- | --- |
| `--url <url>` | URL окружения Dynatrace для загрузки конфигурации. Для подключения требуется токен доступа через `--token`. Флаг взаимоисключающий с `--manifest` или `--environment`. |
| `--token <environment variable name>` | Переменная окружения с токеном доступа. Обязательна при использовании `--url`. |

### Флаги (необязательные)

Помимо флагов подключения, существует ряд опций для обоих режимов загрузки.

| Флаг | Описание |
| --- | --- |
| `--output-folder <filepath>` или `-o <filepath>` | Задать имя выходной папки для хранения загруженных конфигураций. По умолчанию создаётся новая папка с именем `download` и текущей временной меткой. |
| `--project <name>` или `-p <name>` | Имя проекта для сгенерированного набора загруженных конфигураций. По умолчанию: `project`. |
| `--api <name>` или `-a <name>` | Загрузить один или несколько классических API конфигурации, включая устаревшие. (Повторите флаг или используйте значения через запятую.) |
| `--settings-schema <name>` или `-s <name>` | Загрузить объекты Settings 2.0 по одной или нескольким схемам. (Повторите флаг или используйте значения через запятую.) |
| `--only-apis` | Загрузить только классические API конфигурации. Устаревшие API не включаются. |
| `--only-settings` | Загрузить только объекты Settings 2.0. Классические API конфигурации не включаются. |
| `--force` или `-f` | Принудительно перезаписать существующий `manifest.yaml` вместо создания дополнительного `manifest_{timestamp}.yaml`. При [загрузке через манифест](/managed/deliver/configuration-as-code/monaco/reference/commands#dowload-manifest "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)"): никогда не добавлять имя исходного окружения к имени папки проекта. |

### Фильтрация

По умолчанию команда `download` исключает ряд конфигураций.

Возможности фильтрации варьируются от полного исключения типа конфигурации до исключения конкретных объектов.

Некоторые типы исключены, так как Dynatrace API не возвращает полную информацию о них. Как правило, эти типы содержат секреты, которые нельзя экспортировать после создания:

* `aws-credentials`
* `azure-credentials`
* `kubernetes-credentials`
* `credential-vault`
* `extension`

Конкретные объекты конфигурации исключаются, если являются конфигурациями только для чтения, которые нельзя изменить.

#### Отключение фильтров

Dynatrace Monaco CLI версии 2.2.0+

Фильтрацию можно отключить для загрузки всего. Имейте в виду, что такая загрузка создаёт проект, который нельзя развернуть напрямую и который требует ручной постобработки.

Фильтрами управляют следующие переменные окружения:

| Переменная окружения | Описание |
| --- | --- |
| `MONACO_FEAT_DOWNLOAD_FILTER` | Управляет всей фильтрацией при загрузке. При значении `false` фильтры не применяются. Имеет приоритет над всеми остальными флагами фильтрации. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS` | Управляет фильтрацией Settings 2.0. При значении `false` все settings загружаются без фильтрации. Имеет приоритет над `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE`. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE` | Управляет фильтрацией Settings 2.0. При значении `false` загружаются настройки, отмеченные API как `unmodifiable`. |
| `MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS` | Управляет фильтрацией классических [типов Config API](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco"). При значении `false` все конфигурации Config API загружаются без фильтрации. |

Например, для загрузки всех классических типов Config API без фильтрации, включая немодифицируемые объекты Settings 2.0:

Linux/macOS

Windows

```
export MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS=false



export MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE=false



monaco download [flags]
```

```
$env:MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS=false



$env:MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE=false



monaco download [flags]
```

### Параллельные загрузки

Для максимально быстрой загрузки больших наборов конфигураций команда `download` выполняет несколько одновременных API-вызовов к Dynatrace.

Для настройки числа параллельных запросов используйте переменную окружения `MONACO_CONCURRENT_REQUESTS`:

Linux/macOS

Windows

```
MONACO_CONCURRENT_REQUESTS=15 monaco download [flags]
```

```
$env:MONACO_CONCURRENT_REQUESTS=15



monaco download [flags]
```

По умолчанию выполняется не более пяти одновременных запросов к Dynatrace. При необходимости ускорить загрузку (если окружение и сеть позволяют) можно увеличить это число.

При возникновении проблем с загрузкой — например, если внутренняя сетевая настройка ограничивает и сбрасывает запросы — уменьшите число параллельных запросов.

### Разрешение зависимостей

При загрузке Dynatrace Monaco CLI разрешает ссылки между конфигурациями для их последующей загрузки в правильном порядке. Для этого все загруженные JSON-шаблоны анализируются на предмет идентификаторов всех конфигураций.

Стандартный алгоритм разрешения зависимостей требователен к CPU и может работать медленно на оборудовании или в контейнерах с ограниченными ресурсами.

Monaco CLI версии 2.0.2+: доступен быстрый алгоритм, который снижает нагрузку на CPU в обмен на увеличенные требования к памяти. Для активации:

1. Убедитесь, что на машине доступно не менее 16–32 ГБ ОЗУ и несколько сотен ГБ в виде swap.
2. Установите переменную окружения `MONACO_FEAT_FAST_DEPENDENCY_RESOLVER` в `true`.

   Linux/macOS

   Windows

   ```
   MONACO_FEAT_FAST_DEPENDENCY_RESOLVER=true monaco download [flags]
   ```

   ```
   $env:MONACO_FEAT_FAST_DEPENDENCY_RESOLVER=true



   monaco download [flags]
   ```

## Команда delete

Команда `delete` — удобный способ удаления конфигураций из окружений Dynatrace.

Как правило, долгоживущие конфигурации в production-окружениях удалять нежелательно, однако иногда это необходимо.

Dynatrace Monaco CLI также используется для управления эфемерными конфигурациями в средах разработки — в этом случае Monaco удобен для очистки временных конфигураций.

### Использование

`monaco delete [--manifest manifest.yaml] [--file delete.yaml] [FLAGS]`

Команда delete требует двух YAML-файлов:

* Файл манифеста со списком окружений Dynatrace, из которых нужно удалить конфигурацию
* Файл удаления с определением конфигураций для удаления

Если имена файлов не указаны, команда ищет `manifest.yaml` и `delete.yaml` в текущей папке.

#### Пример

Предположим, есть файл [манифеста развёртывания](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") `deployment-file.yaml` со следующей структурой:

```
projects:



- name: infrastructure



path: infrastructure



environments:



- group: development



entries:



- name: development



url:



type: value



value: "https://mytenant.live.dynatrace.com"



auth:



token:



name: "TestIt"
```

И файл `delete.yaml` со следующей структурой:

```
delete:



- type: java-service



name: my-java-service-config
```

Следующая команда удалит конфигурацию `my-java-service-config` в проекте `infrastructure` из development-окружения:

```
monaco delete --manifest deployment-file.yaml --file delete.yaml
```

### Флаги (необязательные)

| Флаг | Описание |
| --- | --- |
| `--manifest <filepath>` или `-m <filepath>` | Удалить конфигурации из окружений, определённых в конкретном файле манифеста. По умолчанию: `manifest.yaml` в текущей папке. |
| `--file <filepath>` | Удалить конфигурации, определённые в конкретном [файле удаления](/managed/deliver/configuration-as-code/monaco/reference/commands#delete-yaml "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)"). По умолчанию: `delete.yaml` в текущей папке. |
| `--environment <name>` или `-e <name>` | Задать одно или несколько окружений для удаления конфигураций. Взаимоисключающий с `--group`. |
| `--group <name>` или `-g <name>` | Задать одну или несколько [групп окружений](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") для удаления конфигураций. Взаимоисключающий с `--environment`. |

### Файл удаления `delete.yaml`

Файл удаления (по умолчанию `delete.yaml`) — YAML-документ со списком конфигураций для удаления.

Каждая запись может ссылаться на конфигурацию **напрямую** — по её ID объекта Dynatrace, или **косвенно** — через координаты.

Только объекты, созданные или подключённые Monaco, можно удалять через косвенные ссылки по координатам.

Если вы загрузили существующие конфигурации и хотите удалить их таким способом, сначала необходимо хотя бы однократно развернуть загруженный проект, чтобы объекты были доступны для удаления.

Файл удаления не может содержать записи для конфигураций `dashboard-share-settings` или `openpipeline` — такие конфигурации удалить нельзя.

#### Прямая ссылка

Для прямой ссылки необходимо задать `type` и `objectId`, где `type` — тип конфигурации, `objectId` — ID конфигурации из Dynatrace.

```
- type: management-zone



objectId: origin-object-ID
```

#### Косвенная ссылка

В зависимости от [типа конфигурации](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type "Learn how to set up your Monaco YAML configuration.") косвенная ссылка немного отличается.

* [Тип API](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-config-api "Learn how to set up your Monaco YAML configuration.")

  Для записи API задайте:

  + `name`: имя конфигурации
  + `type`: один из [поддерживаемых типов API](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco")

  ```
  - name: my-mz



  type: management-zone
  ```
* [Тип Settings](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-setting "Learn how to set up your Monaco YAML configuration.")

  Для записи Settings задайте:

  + `project`: имя проекта конфигурации
  + `id`: ID записи конфигурации в файле `config.yaml`
  + `type`: один из [ID схем Settings 2.0](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#settings "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco")

  ```
  - project:  my-project



  id:       my-auto-tag



  type:     builtin:auto.tagging
  ```
* [Тип Automation](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-automation "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI версии 2.6.0+

  Для записи Automation задайте:

  + `project`: имя проекта конфигурации
  + `type`: одно из значений: `workflow`, `scheduling-rule` или `business-calendar`
  + `id`: ID записи конфигурации в файле `config.yaml`

  ```
  - project: my-project



  type:    workflow



  id:      my-workflow
  ```
* [Тип Bucket](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-bucket "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI версии 2.9.0+

  Для записи Bucket задайте:

  + `project`: имя проекта
  + `type`: значение `bucket`
  + `id`: ID записи конфигурации в файле `config.yaml`

  ```
  - project: my-project



  type:    bucket



  id:      my-bucket
  ```
* [Тип Document](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-document "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI версии 2.15.0+

  Для записи Document задайте:

  + `project`: имя проекта
  + `type`: значение `document`
  + `id`: ID записи конфигурации в файле `config.yaml`

  ```
  - project: my-project



  type: document



  id: monaco-config-id
  ```

  Через косвенную ссылку Monaco может удалять только документы, изначально созданные им. Для удаления документов, созданных другими способами, используйте прямую ссылку.

* [Тип Segment](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-segment "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI версии 2.19.0+

  Для записи Segment задайте:

  + `project`: имя проекта
  + `type`: значение `segment`
  + `id`: ID записи конфигурации в файле `config.yaml`

  ```
  - project: my-project



  type:    segment



  id:      my-segment
  ```
* [Тип Service-Level Objective (SLO)](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-service-level-objective-slo "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI версии 2.22.0+

  Для записи SLO задайте:

  + `project`: имя проекта
  + `type`: значение `slo-v2`
  + `id`: ID записи конфигурации в файле `config.yaml`

  ```
  - project: my-project



  type:    slo-v2



  id:      my-slo
  ```

#### Устаревший краткий синтаксис (устарело)

Monaco пока поддерживает альтернативный синтаксис для записей файла удаления:

```
delete:



- <api/name> OR <schema/config-id>



- …
```

Однако этот синтаксис устарел и в будущих версиях поддерживаться не будет. Рекомендуется использовать более структурированный формат выше.

## Команды generate

Команда `monaco generate` предоставляет несколько подкоманд для генерации вспомогательных файлов на основе конфигурации.

### Генерация файла удаления

Dynatrace Monaco CLI версии 2.6.0+

Команда `monaco generate deletefile` создаёт файл удаления конфигурации для использования с [командой delete](/managed/deliver/configuration-as-code/monaco/reference/commands#delete "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)").

#### Использование

`monaco generate deletefile <manifest.yaml> [flags]`

##### Пример

```
monaco generate deletefile my_manifest.yaml -o deletefiles --file my-projects-delete-file.yaml -p my_project
```

#### Позиционные аргументы (обязательные)

| Аргумент | Описание |
| --- | --- |
| `<manifest.yaml>` | Файл манифеста, для которого генерируется файл удаления. Для каждой конфигурации из проектов манифеста создаётся запись. |

#### Флаги (необязательные)

| Флаг | Описание |
| --- | --- |
| `--file <filepath>` | Имя создаваемого файла удаления. Если файл с таким именем уже существует, добавляется временная метка. По умолчанию: `delete.yaml`. |
| `--output-folder <filepath>` или `-o <filepath>` | Имя выходной папки для генерации файла удаления. По умолчанию: текущая директория. |
| `--project <name>` или `-p <name>` | Задать один или несколько проектов для генерации записей файла удаления. Если не задан, используются все проекты манифеста. |

Команда `generate deletefile` не может обработать конфигурации, содержащие ссылки в поле name, и завершится ошибкой при их наличии.

**Пример проблемной конфигурации:**

```
configs:



- id: appRule



config:



name:



configId: application



configType: application-web



property: name



type: reference



template: rule.json



skip: false



type:



api: app-detection-rule
```

**Обходное решение:** создайте файл удаления вручную или обновите сгенерированный файл, задав имя конфигурации без ссылок. Корректный синтаксис см. в [формате файла удаления](/managed/deliver/configuration-as-code/monaco/reference/commands#delete-yaml "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)").

### Генерация файла DOT с графом зависимостей

Dynatrace Monaco CLI версии 2.6.0+

Команда `monaco generate graph` создаёт DOT-представления зависимостей между конфигурациями из проектов заданного манифеста.

[Формат DOT](https://dt-url.net/oo0365m) — стандартизированный текстовый формат для представления графов. Визуальные представления можно создавать с помощью таких инструментов, как [Graphviz](https://dt-url.net/zg2369w).

#### Использование

`monaco generate graph <manifest.yaml> [flags]`

##### Пример

```
monaco generate graph manifest.yaml -e dev-environment -o mygraphs_folder
```

#### Позиционные аргументы (обязательные)

| Аргумент | Описание |
| --- | --- |
| `<manifest.yaml>` | Файл манифеста, для которого генерируются графы зависимостей. Для каждого окружения создаётся один DOT-файл. |

#### Флаги (необязательные)

| Флаг | Описание |
| --- | --- |
| `--output-folder <filepath>` или `-o <filepath>` | Имя выходной папки для генерации DOT-файлов. По умолчанию: текущая директория. |
| `--environment <name>` или `-e <name>` | Задать одно или несколько окружений для создания графов зависимостей. Взаимоисключающий с `--group`. |
| `--group <name>` или `-g <name>` | Задать одну или несколько [групп окружений](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") для создания графов зависимостей. Взаимоисключающий с `--environment`. |
| `--id-encoding [default,json]` | Dynatrace Monaco CLI версии 2.12.0+. Установите `json` для генерации DOT-файла с кодировкой координат каждого узла в JSON вместо стандартного строкового представления. JSON-кодировка удобна при автоматизированной обработке сгенерированных DOT-файлов. |

### Генерация JSON-схем для YAML-файлов

Dynatrace Monaco CLI версии 2.10.0+

Команда `monaco generate schemas` создаёт файлы [JSON-схем](https://json-schema.org/) для YAML-файлов Monaco: манифеста, конфигурации и файлов удаления.

Файлы схем можно интегрировать с большинством распространённых IDE и продвинутых редакторов напрямую или через бесплатные плагины.

#### Использование

`monaco generate schemas [flags]`

##### Пример

```
monaco generate schemas -o monaco_schema_folder
```

#### Использование сгенерированных файлов схем с Visual Studio Code

Ниже описан рекомендуемый пример использования с [Visual Studio Code](https://code.visualstudio.com/).

При использовании другого редактора или IDE следуйте соответствующей документации по регистрации JSON-схем.

Предварительные условия:

* Файлы JSON-схем Monaco сгенерированы и пути к ним известны
* Установлена последняя версия [Visual Studio Code](https://code.visualstudio.com/) для вашей ОС
* В Visual Studio Code установлено [расширение YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

После установки расширения YAML можно связать конкретные схемы с файлами Monaco.

Общую информацию о настройке расширения YAML см. в [документации расширения](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml#associating-schemas).

Рекомендуемая запись в `settings.json` Visual Studio Code:

```
"yaml.schemas": {



"file:///<path-to-your-schema-folder>/monaco-config.schema.json": "**/*config*.yaml",



"file:///<path-to-your-schema-folder>/monaco-manifest.schema.json": "**/*manifest*.yaml",



"file:///<path-to-your-schema-folder>/monaco-delete-file.schema.json": "**/*delete*.yaml"



}
```

В примере выше:

* Замените `<path-to-your-schema-folder>` на путь к сгенерированной папке. Рекомендуется использовать абсолютные пути.
* Предполагается соблюдение соглашений об именовании из данной документации и сгенерированных файлов. При использовании других соглашений об именовании манифеста, конфигурации или YAML-файлов удаления измените конфигурацию соответствующим образом.

Обновление схем

Поскольку формат файлов манифеста или конфигурации может меняться между версиями, регенерируйте определения схем с текущей версией Monaco.

#### Флаги (необязательные)

| Флаг | Описание |
| --- | --- |
| `--output-folder <filepath>` или `-o <filepath>` | Имя выходной папки для генерации JSON-схем. По умолчанию: директория `schemas/` в текущей директории. |

## Глобальные флаги (необязательные)

Следующие необязательные флаги применимы ко всем командам.

| Флаги | Описание |
| --- | --- |
| `--support-archive` | Создать [архив поддержки](/managed/deliver/configuration-as-code/monaco/reference/logging#support-archive "Logging reference for Dynatrace Configuration as Code via Monaco"). |
| `--verbose` или `-v` | Включить [подробные отладочные логи](/managed/deliver/configuration-as-code/monaco/reference/logging#timestamps "Logging reference for Dynatrace Configuration as Code via Monaco"). |