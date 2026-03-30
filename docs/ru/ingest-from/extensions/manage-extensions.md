---
title: Управление расширениями
source: https://www.dynatrace.com/docs/ingest-from/extensions/manage-extensions
scraped: 2026-03-06T21:24:23.338562
---

* Latest Dynatrace
* 7 мин. чтения

Управляйте расширениями Dynatrace для сотен технологий.

## Предварительные требования

### Разрешения

hub:catalog:read

для получения сведений о расширениях

storage:entities:read

чтение сущностей из хранилища

storage:logs:read

Для чтения логов

storage:buckets:read

Для чтения любых данных

storage:system:read

Чтение системных данных

storage:metrics:read

Для чтения метрик с помощью DQL

settings:objects:read

Чтение объектов настроек

settings:objects:write

Запись объектов настроек

state:user-app-states:read

Для чтения любых данных

state:user-app-states:write

Запись пользовательских предпочтений

### На что следует обратить внимание

Если вы не можете получить доступ к ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, убедитесь, что у вас есть необходимые [разрешения](#permissions), в частности начинающиеся с `extensions:configuration` и `extensions:definitions`. Дополнительную информацию см. в разделах Работа с политиками и [Политика IAM — права на чтение и запись конфигураций расширений](https://community.dynatrace.com/t5/Dynatrace-tips/IAM-Policy-Read-and-write-permissions-on-extensions/m-p/220907) в Dynatrace Community.

## Обзор

Расширения позволяют расширить возможности Dynatrace для сбора данных и доменной экспертизы для сотен технологий. Приложение Extensions — это ваш центральный ресурс для управления и настройки Extensions 2.0.

![Вкладка «Конфигурации мониторинга» отображает конфигурации, доступные для каждого расширения. Включает версию расширения, используемую каждой конфигурацией, и статус каждой конфигурации.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.42.png)![Вкладка «Состояние здоровья» показывает состояние расширения для каждой конфигурации мониторинга.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.57.png)![Изучите логи, связанные с состоянием каждого расширения.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.18.png)![Начните мониторинг новых источников данных.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.46.png)![Управляйте всеми Extensions 2.0, установленными в вашей среде.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.51.26.png)

1 из 5 — Вкладка «Конфигурации мониторинга» отображает конфигурации, доступные для каждого расширения. Включает версию расширения, используемую каждой конфигурацией, и статус каждой конфигурации.

## Dynatrace Hub

### Загрузка пользовательского расширения из Dynatrace Hub

1. Перейдите в ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Загрузить пользовательское расширение**.
2. Выберите архив расширения и загрузите его в Dynatrace.

Dynatrace Hub проверяет архив и структуру расширения и автоматически активирует его после успешной загрузки.

Большинство полей заполняются автоматически на основе YAML-файла расширения. Вы можете предоставить информацию о примечаниях к выпуску, объясняющую причину изменения версии расширения.

### Развёртывание расширения из Dynatrace Hub

1. Перейдите в ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Обнаружение**.
2. Найдите расширение в списке или воспользуйтесь строкой поиска. Все расширения, уже установленные в вашей среде, отмечены как **Установлено**.
3. Выберите плитку расширения, которое хотите добавить, затем выберите **Добавить в среду**.

Теперь вы можете проверить **Информацию о продукте**, **Содержимое расширения**, **Доступные версии**, **Конфигурации мониторинга** и **Состояние здоровья** вашего расширения, выбирая соответствующие вкладки.

#### Определение устройств

Выберите **Добавить устройство**, чтобы определить устройства, с которых вы хотите получать данные, и укажите данные подключения к устройству:

* IP-адрес или имя устройства
* Порт
* Версия SNMP и соответствующие данные аутентификации

#### Запуск мониторинга

Ваше расширение появляется в Dynatrace Hub. Следующий шаг — предоставить конфигурацию мониторинга для вашего расширения. Подробные шаги зависят от источника данных вашего расширения. Дополнительную информацию см. в:

* [Расширения SNMP](supported-extensions/data-sources/snmp.md#activate-extension "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик и событий SNMP.")
* [Расширения WMI](supported-extensions/data-sources/wmi.md#activate-extension "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")
* [Расширения Prometheus](../extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions.md#activate-extension "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик Prometheus.")
* [Расширения Oracle SQL](supported-extensions/data-sources/sql/oraclesql.md#activate-extension "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик из Oracle Database.")
* [Расширения Microsoft SQL](supported-extensions/data-sources/sql/microsoft-sql.md#activate-extension "Расширьте наблюдаемость в Dynatrace с помощью декларативного приёма метрик из Microsoft SQL Server.")

### Обновление расширения из Dynatrace Hub

Для обновления расширения просто загрузите новую версию. Dynatrace Hub автоматически активирует новую версию расширения.

Каждое обновление расширения перезаписывает конфигурацию событий метрик, которая может поставляться с расширением. Это означает, что любые настройки, внесённые в параметры событий метрик, будут сброшены к значениям по умолчанию при обновлении расширения. Рекомендуется записать пользовательские конфигурации и повторно применить их после обновления, если это необходимо.

### Удаление расширения из Dynatrace Hub

Вы можете удалить расширение полностью или удалить конкретную версию расширения.

Для удаления расширения:

1. Перейдите в ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Управление**.
2. Найдите расширение, которое хотите удалить, и выберите > **Удалить**.

Для удаления версий расширения:

1. Перейдите в ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Управление**.
2. Выберите плитку расширения, чтобы открыть подробности.
3. Выберите **Доступные версии** > **Удалить**.

При удалении версии Dynatrace Hub активирует последнюю доступную версию.

## Dynatrace API

### Разрешения API

* Вам нужен токен API со следующими разрешениями для управления жизненным циклом расширения:

  + API v2

    - Read extensions
    - Write extensions
    - Read extension environment configurations
    - Write extension environment configurations
    - Read extension monitoring configurations
    - Write extension monitoring configurations
  + API v1

    - Read configuration
    - Write configuration

### Загрузка расширения через Dynatrace API

Выполните следующую команду для загрузки пакета расширения в вашу среду. В этом примере используется URL Dynatrace:

```
curl -X POST "https://{env-id}.live.dynatrace.com/api/v2/extensions" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token {api-token}" \


-H "Content-Type: multipart/form-data" \


-F "file=@MyCustomExtension.zip;type=application/zip"
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `MyCustomExtension.zip` на фактическое имя файла вашего пакета расширения.

После успешной загрузки Dynatrace API возвращает основные сведения о расширении, включая имя расширения, версию и минимальную версию Dynatrace, необходимую для запуска расширения:

```
{


"extensionName":"custom:my.company.extension",


"version":"1.0.0",


"author":{


"name":"My Company"


},


"dataSources":[


],


"variables":[


],


"featureSets":[


],


"minDynatraceVersion":"1.213.0"


}
```

### Активация расширения через Dynatrace API

После загрузки расширения в вашу среду необходимо активировать конфигурацию среды. Этот шаг необходим, поскольку вы можете загрузить до 10 версий расширения, но использовать только одну версию одновременно. При активации расширения вы указываете, какую версию использовать.

Выполните следующую команду для активации расширения в вашей среде. В этом примере используется URL Dynatrace.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token {api-token}" \


-H "Content-Type: application/json; charset=utf-8" \


-d "{\"version\":\"{version}\"}"
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `{extensionName}` на фактическое имя расширения.
* `{version}` на версию расширения, которую хотите активировать.

Чтобы определить имя расширения, извлеките пакет расширения, извлеките файл `extensions.zip` из пакета и откройте файл `extension.yaml`.

После успешной активации Dynatrace API возвращает версию активированного расширения. Например:

```
{"version":"1.0.0"}
```

### Запуск мониторинга через Dynatrace API

Для запуска мониторинга необходимо добавить как минимум одну версию конфигурации мониторинга. Формат JSON-тела запроса зависит от отслеживаемого источника данных.

```
curl -X POST "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName>/monitoringConfigurations" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token {api-token}" \


-H "Content-Type: application/json; charset=utf-8" \


--data @{monitoring-configuration} -i
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `{extensionName}` на фактическое имя расширения.
* `{version}` на версию расширения, которую хотите активировать.
* `{monitoring-configuration}` на имя файла, содержащего JSON-тело с конфигурацией мониторинга. Подробности о формате см. в разделе [SNMP](develop-your-extensions/data-sources/snmp-extensions.md#monitoring-configuration "Узнайте, как создать расширение SNMP с помощью фреймворка Extensions.").

После успешного вызова Dynatrace API возвращает объект `MonitoringConfigurationResponse`. Например:

```
[


{ "objectId": "vu9U3hXa3q0AAAABACVleHQ6Y29tLmR5bmF0cmFjZS5zY2hlbWEtc25tcC1nZW5lcmljAAhhZ19ncm91cAAHRTJFVEVTVAAkMWMxZTlhMDctNzVkYi0zZjI0LWI4OGUtZmIxYWRiNGNjYTY4vu9U3hXa3q0", "code": 200 }


]
```

Через несколько минут перейдите в Обозреватель метрик и найдите метрики, определённые для вашего расширения.

### Обновление расширения через Dynatrace API

Для обновления расширения необходимо загрузить новый пакет расширения и активировать новую конфигурацию среды.

#### Загрузка обновлённого пакета расширения через API

Для загрузки пакета используйте ту же команду, что и для загрузки начальной версии расширения. Если имя файла нового пакета расширения изменилось, необходимо использовать новое имя.

#### Активация новой версии конфигурации через API

Для активации версии конфигурации среды необходимо добавить параметр версии в вызов API. Используйте один из следующих методов для определения версии:

* После успешной загрузки Dynatrace API возвращает основные сведения о расширении, включая версию.
* Найдите версию в файле `extension.yaml` внутри пакета расширения.
* Выполните вызов API Получить версии расширения.

Выполните следующую команду для активации новой версии. В этом примере используется URL Dynatrace.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token  {api-token}" \


-H "Content-Type: application/json; charset=utf-8" \


-d "{\"version\":\"{version}\"}"
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `{extensionName}` на фактическое имя расширения.
* `{version}` на версию расширения, которую хотите активировать.

После успешной активации Dynatrace API возвращает версию активированного расширения. Например:

```
{"version":"1.1.0"}
```

Если необходимо вернуться к более ранней версии, выполните команду выше с другим параметром версии.

### Удаление расширения через Dynatrace API

Если вы загрузили несколько версий расширения, необходимо удалить все версии для полного удаления расширения из вашей среды. Вы можете использовать GET версий расширения для получения списка всех версий расширения, доступных в вашей среде.

#### Удаление конфигурации среды через API

Для удаления текущей активной конфигурации среды используйте DELETE конфигурации среды. В этом примере используется URL Dynatrace.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token {api-token}"
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `{extensionName}` на фактическое имя расширения.

После успешной деактивации Dynatrace API возвращает версию деактивированного расширения. Например:

```
{"version":"1.1.0"}
```

#### Удаление версии расширения через API

Для удаления версии расширения используйте DELETE версии расширения. В этом примере используется URL Dynatrace.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/{version}" \


-H "accept: application/json; charset=utf-8" \


-H "Authorization: Api-Token {api-token}"
```

Замените:

* `{env-id}` на ваш идентификатор среды.
* `{api-token}` на токен API с необходимыми [разрешениями](#prerequisites).
* `{extensionName}` на фактическое имя расширения.
* `{version}` на версию расширения, которую хотите удалить.

После успешного удаления версии Dynatrace API возвращает следующий ответ:

```
{


"extensionName":"custom:my.company.extension",


"version":"1.0.0",


"author":{


"name":"My Company"


},


"dataSources":[


],


"variables":[


],


"featureSets":[


],


"minDynatraceVersion":"1.213.0"


}
```

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

Изучите ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** в Dynatrace Hub.](https://www.dynatrace.com/hub/detail/extension-manager/)