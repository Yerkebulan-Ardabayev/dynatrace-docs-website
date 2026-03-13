---
title: Monaco resources
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/monaco-manage-resources
scraped: 2026-03-01T21:24:34.545844
---

# Ресурсы Monaco

# Ресурсы Monaco

* Последняя версия Dynatrace
* Справочник
* Время чтения: 8 мин
* Опубликовано 22 июля 2025 г.

Для запуска Monaco необходимо определить [манифест развёртывания](/docs/deliver/configuration-as-code/monaco/monaco-concepts#deploy-manifest "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов."), [каталоги проектов](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов.") и [конфигурацию ресурсов](/docs/deliver/configuration-as-code/monaco/monaco-concepts#resource-configuration "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов."), чтобы управлять ресурсами.

## Манифест развёртывания

Файл [манифеста развёртывания](/docs/deliver/configuration-as-code/monaco/monaco-concepts#deploy-manifest "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов.") имеет три ключа верхнего уровня: `manifestVersion`, `projects` и `environmentGroups`.

### Пример manifest.yaml

Пример файла manifest.yaml:

```
manifestVersion: 1.0



projects:



- name: infra



path: shared/infrastructure



- name: general



path: general



type: grouping



environmentGroups:



- name: dev



environments:



- name: test-env-1



url:



value: https://<YOUR-DT-DEV-ENV-ID>.apps.dynatrace.com



auth:



token:



name: DEV_TOKEN



oAuth:



clientId:



name: DEV_CLIENT_ID



clientSecret:



name: DEV_CLIENT_SECRET



- name: test-env-2



url:



value: https://<YOUR-DT-SPRINT-ENV-ID>.apps.dynatrace.com



auth:



token:



name: SPRINT_TOKEN



oAuth:



clientId:



name: SPRINT_CLIENT_ID



clientSecret:



name: SPRINT_CLIENT_SECRET



- name: prod



environments:



- name: prod-env-1



url:



type: environment



value: https://<YOUR-DT-PROD-ENV-ID>.apps.dynatrace.com



auth:



token:



name: PROD_TOKEN



oAuth:



clientId:



name: PROD_CLIENT_ID



clientSecret:



name: PROD_CLIENT_SECRET
```

### manifestVersion

Манифест должен содержать `manifestVersion` в качестве ключа верхнего уровня.
Это простая строка, которая используется для проверки того, может ли текущая версия Monaco корректно разобрать манифест.

В настоящее время поддерживается версия манифеста `1.0`.
Примечания к выпуску будут содержать подробности о расширении манифеста или выпуске новых версий.

### projects

Все записи в разделе [`projects`](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов.") указывают проекты для развёртывания с помощью Monaco.
Чтобы указать для проекта:

* Имя, укажите ключ `name`.
* Путь, укажите `path`.
* Тип, укажите ключ `type`.

Задайте значения для этих ключей.

Существует два типа проектов: `simple` и `grouping`.

#### Простые проекты (тип по умолчанию)

Простой проект является типом по умолчанию и определяется двумя свойствами:

* Обязательное `name`: не может содержать символы косой черты (`/` или `\`). Например, `/ or Dynatrace Software Intelligence Platform`, следует отличать от путей файловой системы.

* Необязательное `path`: если не указано, в качестве пути будет использоваться `name`.
  Всегда должен использовать прямую косую черту (/) в качестве разделителя, независимо от вашей операционной системы (Linux, Windows, Mac).

#### Группирующие проекты

Группирующий проект загружает все подпапки указанного пути как простые проекты.
Группирующий проект предлагает упрощённый способ объединения нескольких проектов вместе.

* Обязательное `name`: используется как префикс для результирующего простого проекта.
* Точка (`.`) будет использоваться в качестве разделителя `<project.name>.<subfolder_name>`.

### environmentGroups

Окружение -- это окружение Dynatrace.
Вы можете группировать эти окружения вместе в одну группу окружений с помощью типа `environmentGroups`.
Вы можете применить конфигурацию к `environmentGroup`, что неявно применит её ко всем окружениям в группе.
Группировка предпроизводственных и производственных окружений может быть полезной, как показано в начальном примере [`manifest.yaml`](#sample-manifest) выше.

#### environment

Тип `environment` состоит из разделов `name`, `url` и `auth`.

* `name`: Внутреннее для Monaco имя данного окружения Dynatrace.
  Имя может быть любой глобально уникальной строкой.
  Оно должно быть уникальным.
* `url`: URL окружения Dynatrace.

  Определение `url` окружения состоит из

  + `type`
  + `value`

  URL окружения может быть определён непосредственно в манифесте или через ссылку на переменную окружения.

  + Определение напрямую

  ```
  url:



  type: value



  value: "https://<YOUR-ENV-ID>.apps.dynatrace.com"
  ```

  + Через переменную окружения

  ```
  url:



  type: environment



  value: YOUR_URL_ENV_VAR
  ```
* `auth`: Метод аутентификации Dynatrace API.
  Он определяет всю информацию, необходимую для аутентифицированного использования Dynatrace API.

Поскольку эти конфигурации являются конфиденциальными, Dynatrace Monaco CLI не позволяет определять их напрямую, а всегда загружает из переменных окружения.
Сделайте эти секреты доступными как переменные окружения, следуя инструкциям для вашей операционной системы или инструмента CI/CD.

Всегда определяйте `token`, указывающий токен доступа для общей конфигурации и настроек, включая последнюю версию Dynatrace Platform.

Токены доступа для Dynatrace Monaco CLI всегда требуют как минимум разрешение "Access problem and event feed, metrics, and topology (`DataExport`) -- API v1" для запроса общей информации о вашем окружении.

Вам необходимо настроить каждый доступный тип конфигурации с определёнными разрешениями. Для получения более подробной информации см. [Поддержка Monaco API и обработка разрешений доступа](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling "Список поддержки Monaco API и обработки разрешений доступа.").

В большинстве случаев вам потребуется токен как минимум со следующими разрешениями:

* "Access problem and event feed, metrics, and topology (`DataExport`) -- API v1"
* "Read configuration (`ReadConfig`) -- API v2"
* "Write configuration (`WriteConfig`) -- API v2"
* "Read settings (`settings.read`) -- API v2"
* "Write settings (`settings.write`) -- API v2"

Для общей информации об аутентификации по токену доступа см. [Dynatrace API - Токены и аутентификация](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Вам необходим раздел OAuth, указывающий учётные данные OAuth-клиента.

Как правило, учётные данные OAuth-клиента для Dynatrace Monaco CLI должны иметь как минимум следующие области:

* Run apps (`app-engine:apps:run`) -- Это разрешение необходимо для доступа к конечным точкам метаданных Dynatrace.
* View settings objects for schema (`settings:objects:read`)
* Create settings objects for schema (`settings:objects:write`)
* View settings schemas (`settings:schemas:read`)

#### projects

[`projects`](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "Список концепций Monaco, таких как манифест развёртывания, проекты и конфигурация ресурсов.") -- это каталоги, используемые для логической группировки конфигураций API.
Примером проекта может быть сервис, где все конфигурации, относящиеся к этому сервису, находятся в папке.
Проекты могут состоять из нескольких файлов и каталогов.

Папка проекта содержит подпапки со специальными именами, которые представляют API.
Отдельные папки API далее содержат ещё один уровень папок, определяющих конфигурации.
Папки конфигураций, в конечном итоге, содержат YAML-файлы, указывающие, какие ресурсы будут развёрнуты.

#### Конфигурационные файлы

Конфигурационные файлы состоят из

* [YAML-файла конфигураций](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas "Структура YAML-файла конфигурации Monaco."), определяющего параметры, зависимости, имя и шаблон
* JSON-файла шаблона

Dynatrace Monaco CLI использует шаблоны Go, которые позволяют определять более сложные шаблоны. Тем не менее, мы рекомендуем сохранять шаблоны простыми -- ссылки на переменные через `{{ .PARAMETER_NAME }}` должно быть достаточно.

##### Важная дополнительная информация для создания новых шаблонов

JSON-файлы, которые можно загрузить с помощью Monaco, являются JSON-объектами, которые принимает/возвращает соответствующий Dynatrace API.
Добавление новой конфигурации обычно выполняется через пользовательский интерфейс Dynatrace, если вы не знаете структуры JSON-конфигураций достаточно хорошо, чтобы предпочесть их написание вручную.
Вы можете загрузить конфигурации через соответствующую конечную точку GET, определённую в Dynatrace Configuration API, и они должны быть подготовлены для автоматического развёртывания.

* Зарегистрированная конфигурация не должна включать `id` сущности.
  Сущность может быть создана или обновлена, если существует одноимённая.
  `name` должно быть определено как переменная.
* Избегайте жёстко закодированных значений для информации об окружении, таких как ссылки на другие автоматически развёртываемые сущности, теги и зоны управления.
  Указывайте их как переменные.
* Пустые/null-значения, которые являются необязательными при создании объекта.
  Большинство конечных точек API GET возвращают больше данных, чем необходимо для создания объекта.
  Многие поля пусты или равны null и могут быть опущены, например **tileFilters** на дашборде.

Особые требования к JSON-шаблонам

Некоторые типы конфигураций имеют особые требования к их JSON-полезным нагрузкам и могут потребовать ручной модификации для использования с Configuration as Code.
