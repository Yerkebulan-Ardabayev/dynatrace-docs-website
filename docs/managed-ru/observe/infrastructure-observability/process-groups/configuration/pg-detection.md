---
title: Обнаружение групп процессов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection
scraped: 2026-05-12T11:37:44.636400
---

# Process group detection

# Обнаружение групп процессов

* How-to guide
* 10-min read
* Updated on Aug 07, 2023

Dynatrace определяет, какие процессы относятся к одной [группе процессов](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."), с помощью стандартного набора правил обнаружения.

Структуру групп процессов по умолчанию можно изменить, модифицируя логику обнаружения групп процессов в:

* **Settings** > **Processes and containers** > **Process group detection** — раздел с следующими страницами:

  + На странице **Built-in detection rules** можно включать или отключать конкретные переключатели обнаружения групп процессов. Наведите курсор на значок **info** справа от каждого переключателя для получения подробной информации.
  + На страницах [**Simple detection rules**](#simple) и [**Advanced detection rules**](#advanced) можно добавлять собственные правила обнаружения групп процессов, которые переопределяют правила по умолчанию.
  + На странице [Declarative process grouping](/managed/observe/infrastructure-observability/process-groups/configuration/declarative-process-grouping "Monitor specific processes using the declarative process grouping.") можно настраивать мониторинг конкретных процессов технологий, неизвестных Dynatrace.
* **Settings** > **Processes and containers** > **Containers** > **Cloud application and workload detection** — здесь можно определять правила для объединения похожих нагрузок Kubernetes в группы процессов.

* Настройки и правила обнаружения групп процессов требуют перезапуска процессов для применения изменений в их идентификации и группировке.
* Настройки и правила обнаружения групп процессов влияют только на состав групп процессов. Для изменения именования группы процессов необходимо использовать [правила именования групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming").
* Также можно использовать [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") для разделения кластеров на разные группы процессов.

## Простые правила обнаружения

Простые правила обнаружения групп процессов позволяют адаптировать логику обнаружения групп по умолчанию для глубоко отслеживаемых процессов через [**системные свойства Java**](#java) или [**переменные среды**](#env). Простое правило обнаружения можно создать через веб-интерфейс Dynatrace или [Settings API](#api) — см. [Пример JSON-payload для простого правила обнаружения](#eg1).

Простые правила обнаружения групп процессов эффективны только при установке OneAgent на хостах или образах для процессов, поддерживающих глубокий мониторинг.

Данная функция предназначена только для разделения группы процессов на несколько частей. Используйте её, если у вас есть разные развёртывания в одной группе процессов.

Создание простого правила обнаружения в веб-интерфейсе Dynatrace:

1. Перейдите в **Settings**.
2. Выберите **Processes and containers** > **Simple detection rules**.
3. Выберите **Add item**.
4. Установите **Property source** в значение **Java system property** или **Environment variable**.
5. Установите **Group identifier** в значение, которое Dynatrace будет использовать для идентификации групп процессов.
6. Необязательно: установите **Instance identifier** в значение, которое Dynatrace будет использовать для идентификации конкретных узлов кластера в группе процессов.

   Этот параметр полезен, если в настройке группы процессов используются конкретные имена для каждого узла. Если вы не уверены, оставьте поле пустым. Настройка по умолчанию — один узел на хост.
7. Необязательно: установите **Restrict this rule to specific process types** для типа процесса, к которому должно применяться правило.
8. Выберите **Save changes**.

### Системные свойства Java

Этот вариант позволяет создавать более детальные группы Java-процессов.
Системное свойство Java должно быть частью командной строки Java, чтобы OneAgent мог его обнаружить. Это может быть существующее системное свойство, уже используемое приложением (например, три разных значения `jetty.home` для трёх разных кластеров Solr), или можно добавить новое системное свойство. Если системное свойство доступно в командной строке, Dynatrace может его использовать.

### Переменные среды

Этот вариант охватывает Java- и не-Java-процессы, такие как NGINX, Apache HTTP Server, FPM/PHP, Node.js, IIS и .NET.
Переменные среды, выбранные в качестве идентификаторов групп процессов, должны существовать в области видимости обнаруживаемых процессов и быть видимы при запуске приложения.

* Для WebSphere это можно сделать в консоли WebSphere в разделе JVM.
* Для Tomcat и других — просто задайте переменную среды как часть скрипта запуска.

Рекомендуется создавать переменные среды, специфичные для обнаружения процессов. Переменные среды, служащие другим целям, например [`DT_TAGS`](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables#variables "Find out how Dynatrace enables you to define tags based on environment variables.") или [`DT_CUSTOM_PROP`](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment."), могут вызвать некорректные или непреднамеренные разделения, поскольку при обнаружении групп процессов оцениваются все значения переменных среды.

Идентификаторы также служат именем по умолчанию для обнаруженных групп процессов. Подробнее об определении переменных среды для IIS или служб Windows см. в разделе [Define your own process group metadata](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.").

**Пример:**

Предположим, что у вас есть два почти идентичных развёртывания Apache HTTP Server, находящихся в одном каталоге развёртывания, но на разных хостах. По умолчанию Dynatrace не может различить два развёртывания, поскольку они не имеют уникальных характеристик для идентификации. Рассмотрим следующее правило: `Apache process identified by environment variable MY_PG_NAME`.

Любой процесс Apache HTTP, включающий переменную среды `MY_PG_NAME` в своей области видимости, будет использовать содержимое "MY\_PG\_NAME" как в качестве идентификатора, так и имени по умолчанию. В этом сценарии можно заставить Dynatrace отдельно идентифицировать и именовать каждое развёртывание, присвоив одному переменную `MY_PG_NAME=dynatrace.com-production`, а другому — `MY_PG_NAME=dynatrace.com-staging`.

## Расширенные правила обнаружения

Расширенные правила обнаружения групп процессов позволяют создавать группу процессов путём объединения процессов из разных групп и адаптировать логику обнаружения для глубоко отслеживаемых процессов, используя свойства, автоматически обнаруживаемые OneAgent при запуске процесса. Расширенное правило можно создать через веб-интерфейс Dynatrace или [Settings API](#api) — см. [Пример JSON-payload для расширенного правила обнаружения](#eg2).

Расширенные правила обнаружения групп процессов эффективны только при установке OneAgent на хостах или образах для процессов, поддерживающих глубокий мониторинг.

Создание расширенного правила обнаружения в веб-интерфейсе Dynatrace:

1. Перейдите в **Settings**.
2. Выберите **Processes and containers** > **Advanced detection rules**.
3. Выберите **Add item**.
4. В разделе **Process group detection** определите, к каким процессам должно применяться правило. Например, к Java JAR-файлу, содержащему `ws-server.jar`.
5. В разделе **Process group extraction** выберите, какое значение свойства должно использоваться при обнаружении группы процессов.
6. Выберите, должно ли правило быть **standalone rule**.

   Этот вариант не рекомендуется в контейнеризованных средах, поскольку встроенное обнаружение должно обрабатывать всё автоматически. Подробнее см. в разделе [Standalone rules](#stand).
7. В разделе **Process instance extraction** выберите, следует ли использовать конкретные свойства для извлечения отдельных экземпляров процессов (узлов).
8. Выберите **Save changes**.

### Standalone rules

#### Когда включать этот параметр

Предположим, у вас есть группа процессов с несколькими процессами. Каждый процесс одновременно выполняет одну и ту же функцию для разных клиентов, использующих ваше приложение. Хотя каждый экземпляр процесса имеет одинаковое имя, каждый работает с уникальной клиентской конфигурацией, о которой у Dynatrace нет информации. Поэтому Dynatrace агрегирует все связанные процессы в одну группу для упрощения мониторинга.

В случаях, когда такая группировка неадекватна, можно определять правила обнаружения групп процессов, учитывающие специфику клиентов. Такие детали можно извлечь из вашей уникальной схемы развёртывания. Если у вас есть структура каталогов, включающая идентификатор клиента (например, `/opt/MyCustomerBasedApp/<CustomerId>/Service/MyService`), и эта структура одинакова на всех хостах, можно создать правило обнаружения групп процессов, специфичное для клиента, работающее на всех экземплярах процессов.

**Пример:**

Можно создать правило, применяемое к процессам, у которых пути к исполняемым файлам содержат фразу `MyCustomerBasedApp`. Для процессов, соответствующих этому требованию, строка между `/MyCustomerBasedApp/` и `/Service` в **Executable path** извлекается и используется для уникальной идентификации каждого экземпляра процесса.

![pg-standalone](https://dt-cdn.net/images/image-2-1284-3249e27cb7.png)

pg-standalone

#### Когда отключать этот параметр

Параметр **Standalone rules** можно отключить, когда в рамках одной среды нужно различать отдельные сущности (например, production и testing). В этом случае можно использовать обнаружение по умолчанию Dynatrace, дополняя его собственными знаниями о схеме развёртывания.

Можно определить второе свойство, идентифицирующее конкретные экземпляры процессов (или узлы кластера) внутри группы. Это полезно, если в настройке группы процессов используются конкретные имена для каждого экземпляра. Если вы не уверены, оставьте поле пустым. Настройка по умолчанию — один узел на хост.

**Пример:**

![pg-no-standalone](https://dt-cdn.net/images/image-1-1194-857811a02c.png)

pg-no-standalone

* Если ни один из вышеперечисленных вариантов обнаружения групп процессов не подходит, можно использовать переменную среды **DT\_CLUSTER\_ID** для группировки всех процессов с одинаковым значением этой переменной. Все процессы в среде мониторинга с одинаковым идентификатором кластера рассматриваются как члены одной группы процессов и разделяются только по хостам, на которых работают (например, кластеры Apache web servers, принадлежащие одной группе и обслуживающие один сайт). Убедитесь, что переменная **DT\_CLUSTER\_ID** задана только для конкретных процессов, а не на системном уровне! При системной установке все процессы могут быть объединены в одну группу, что нежелательно и не поддерживается.
* Для идентификации узлов в кластере процессов, работающих на одном хосте, используйте переменную среды **DT\_NODE\_ID**. Это указывает Dynatrace, какие процессы следует рассматривать как отдельные экземпляры группы.

## Декларативная группировка процессов

Dynatrace автоматически отслеживает группы процессов известных технологий или потребляющих значительные ресурсы. Декларативная группировка позволяет автоматически отслеживать дополнительные технологии путём переопределения поведения по умолчанию и настройки группировки процессов в группы процессов (PG) и экземпляры групп процессов (PGI). Подробнее см. в разделе [Declarative process grouping](/managed/observe/infrastructure-observability/process-groups/configuration/declarative-process-grouping "Monitor specific processes using the declarative process grouping.").

## Удобная конфигурация через Settings API

С помощью [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") можно легко:

* Изменять определение групп процессов
* Настраивать простые или расширенные правила обнаружения
* Конфигурировать декларативное обнаружение групп процессов

Использование Settings API:

1. [Создайте токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") и включите разрешение **Write settings** (`settings.write`).
2. Используйте эндпоинт [Get a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") для изучения требуемого JSON-формата конфигурации.

   Пример JSON-payload для простого правила обнаружения

   * SchemaID: `builtin:process-group.simple-detection-rule`

     ```json
     [
       {
         "schemaId": "builtin:process-group.simple-detection-rule",
         "scope": "environment",
         "value": {
           "enabled": true,
           "ruleType": "env",
           "groupIdentifier": "MY_PG_NAME",
           "instanceIdentifier": "MY_INSTANCE_NAME",
           "processType": "PROCESS_TYPE_APACHE_HTTPD"
         }
       }
     ]
     ```

   Пример JSON-payload для расширенного правила обнаружения

   * SchemaID: `builtin:process-group.advanced-detection-rule`

     ```json
     [
       {
         "schemaId": "builtin:process-group.advanced-detection-rule",
         "scope": "environment",
         "value": {
           "enabled": true,
           "processDetection": {
             "property": "JBOSS_SERVER_NAME",
             "containedString": "MyJBossServer",
             "restrictToProcessType": "PROCESS_TYPE_JBOSS"
           },
           "groupExtraction": {
             "property": "COMMAND_LINE_ARGS",
             "delimiter": {
               "from": "-environment=",
               "to": "-",
               "removeIds": true
             },
             "standaloneRule": false
           },
           "instanceExtraction": {}
         }
       }
     ]
     ```

   Пример JSON-payload для конфигурации декларативной группы процессов

   * SchemaID: `builtin:declarativegrouping`

     ```json
     [
       {
         "schemaId": "builtin:declarativegrouping",
         "scope": "environment",
         "value": {
           "name": "keepalived",
           "detection": [
             {
               "id": "keepalived",
               "processGroupName": "keepalived",
               "rules": [
                 {
                   "property": "executable",
                   "condition": "$eq(keepalived)"
                 },
                 {
                   "property": "executablePath",
                   "condition": "$prefix(/usr/sbin/keepalived)"
                 },
                 {
                   "property": "commandLine",
                   "condition": "$eq(-d)"
                 }
               ]
             }
           ]
         }
       }
     ]
     ```
3. Используйте эндпоинт [Post an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") для отправки конфигурации.

## Добавление конфигурации в Extensions 2.0

Текущую конфигурацию также можно прикрепить к расширению [Extensions 2.0](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."), чтобы пользовательское расширение поставлялось с предопределёнными правилами группировки процессов. Добавьте определение в файл [Extension YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.") как в следующем примере:

```yaml
---
name: custom:my-extension
version: 1.0.0
minDynatraceVersion: "1.218"
author:
  name: Joe Doe
processes:
- name: keepalived
  detection:
  - id: ext.keepalived
    processGroupName: keepalived
    rules:
    - property: executable
      condition: "$eq(keepalived)"
    - property: executablePath
      condition: "$prefix(/usr/sbin/keepalived)"
    - property: commandLine
      condition: "$eq(-d)"
```