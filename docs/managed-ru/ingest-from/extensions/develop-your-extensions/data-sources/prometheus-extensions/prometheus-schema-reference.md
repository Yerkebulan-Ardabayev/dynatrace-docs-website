---
title: Справочник по источнику данных Prometheus
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference
---

# Справочник по источнику данных Prometheus

# Справочник по источнику данных Prometheus

* Справочник
* Чтение: 13 мин
* Обновлено 10 нояб. 2025 г.

Это общее описание файла YAML расширения на основе источника данных Prometheus и способов объявления метрик и измерений, которые нужно собирать с помощью расширения.

## Область данных

Составьте перечень конечных точек Prometheus, на которые нужно ссылаться в расширении, а также метрик и значений измерений.

В примере создаётся простое расширение, собирающее метрики Rabbit MQ.

```
name: com.dynatrace.extension.prometheus-rabbitmq



version: 1.0.0



minDynatraceVersion: '1.236'



author:



name: Dynatrace



dashboards:



- path: 'dashboards/dashboard_exporter.json'



alerts:



- path: 'alerts/alert_socket_usage.json'



# Extension based on official rabbitmq prometheus exporter available metrics



# list of metrics visible here https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbitmq_prometheus/metrics.md



prometheus:



- group: rabbitmq metrics



interval:



minutes: 1



featureSet: all



dimensions:



- key: rabbitmq



value: const:rabbitmq



subgroups:



# global counters



- subgroup: rabbitmq global counter



dimensions:



- key: global_counters



value: const:global_counters



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_acknowledged_total



value: metric:rabbitmq_global_messages_acknowledged_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_confirmed_total



value: metric:rabbitmq_global_messages_confirmed_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_delivered_consume_auto_ack_total



value: metric:rabbitmq_global_messages_delivered_consume_auto_ack_total



type: count



featureSet: global
```

Определение области мониторинга Prometheus начинается с узла `prometheus` YAML. Все параметры под этим узлом относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Узнайте подробнее о концепции Dynatrace Extensions.") (в данном случае Prometheus).

## Измерения

Для каждого уровня (group, subgroup) можно задать до 25 измерений (итого 50 измерений на метрику).

### Ключ измерения

Строка ключа измерения должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

### Значение измерения

Для задания измерений метрик доступны следующие способы:

* Обычный текст. Добавьте префикс `const:` или просто укажите нужный текст

  ```
  dimensions:



  - key: extension.owner



  value: const:Joe.Doe@somedomain.com
  ```

  или

  ```
  dimensions:



  - key: extension.owner



  value: Joe.Doe@somedomain.com
  ```
* [Метка Prometheus﻿](https://prometheus.io/docs/practices/naming/#metric-and-label-naming)

  ```
  dimensions:



  - key: customdimension.job



  value: label:job



  filter: const:$eq(prometheus)
  ```

  Все метки, предоставляемые Prometheus, автоматически создаются как измерения. Явно задавать измерение на основе метки нужно только в следующих случаях:

  + применение фильтрации по значениям,
  + задание пользовательского ключа измерения.

### Фильтрация извлечённых строк метрик

При извлечении строк метрик можно добавить логику фильтрации: в отчёт попадут только строки, значение измерения которых соответствует критериям фильтра.

Фильтр задаётся на основе условия следующим образом:

* **Starts with** – используется квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with** – используется квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains** – используется квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals** – используется квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для перечисленных выражений также доступны квалификаторы:

  + `const:$and` – объединяет два и более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or` – объединяет два и более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not` – инвертирует выражение. Пример:

    ```
    filter: const:$not(<expr>)
    ```

Для создания сложных фильтров можно объединять два и более фильтра через запятую с помощью логических выражений:

```
dimensions:



- key: technology



value: other



- key: job



value: label:job



filter: const:$or($eq(),$not($or($eq(prometheus),$eq(rabbitmq-server),$eq(redis_exporter),$eq(node_exporter)))
```

## Метрики

Для каждого уровня (group, subgroup) можно задать до 100 метрик. При этом на уровне runtime действует жёсткое ограничение в 1 000 метрик на расширение, что меньше суммарных лимитов допустимых групп и подгрупп.

Например:

```
prometheus:



- group: rabbitmq metrics



interval: 1m



featureSet: all



dimensions:



- key: instance



value: $reference(metric:rabbitmq_identity_info, ref:rabbitmq_node)



subgroups:



# global counters



- subgroup: rabbitmq global counter



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_acknowledged_total



value: metric:rabbitmq_global_messages_acknowledged_total



type: count



featureSet: global



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_confirmed_total



value: metric:rabbitmq_global_messages_confirmed_total



type: count



featureSet: global
```

### Ключ метрики

Строка ключа метрики должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metric-key-required "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

Для версий Dynatrace 1.215 и 1.217 узел metric требует параметра `id` вместо `key`. Начиная с версии Dynatrace 1.219 рекомендуется использовать параметр `key`, так как `id` будет объявлен устаревшим.

#### Рекомендации по ключам метрик

Метрики, загружаемые в Dynatrace с помощью расширения, являются частью тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко различимыми в Dynatrace, рекомендуется добавлять к имени метрики префикс с именем расширения. Это гарантирует уникальность ключа метрики и позволяет легко соотнести метрику с конкретным расширением в среде.

### Значение метрики

Ключ метрики Prometheus, из которого нужно извлечь значение метрики, указывается с префиксом `metric:`.

### Тип

Фреймворк Dynatrace Extensions поддерживает все исходные форматы Prometheus metric payload. Подробнее: [Metric payload](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Learn how the data ingestion protocol for Dynatrace Metrics API works."). Чтобы указать тип метрики, используйте атрибут `type`.

| Тип, экспортируемый Prometheus | Ingestion в Dynatrace |
| --- | --- |
| [Counter﻿](https://dt-url.net/hq634n9) | `count` |
| [Gauge﻿](https://dt-url.net/a2434zx) | `gauge` |
| [Histogram﻿](https://dt-url.net/5x034gl) | **Примечание**: [timeseries percentile](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") доступен только DPS-клиентам с тарифным планом **Metrics powered by Grail**. Функция вычисляет запрошенный перцентиль значения выражения в каждом бакете, поэтому естественным образом применяется с гистограммами.  * Часть count как `<metric-key>_count` * Часть total sum как `<metric-key>_sum.count` * Отдельные бакеты, разбитые по измерению `le` с идентификатором бакета, как `<metric-key>_bucket.count`  Сбор метрик отдельных бакетов отключён по умолчанию. Подробнее о включении: [advanced extension monitoring configuration description](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#advanced "Learn about Prometheus extensions in the Extensions framework."). Примеры кода для Histogram. Стандартная метрика Prometheus histogram включает:  * `HELP` и `TYPE` * Данные бакетов и сводные метрики для `sum` и `count`  ```  # HELP http_response_time_seconds Time to respond to request  # TYPE http_response_time_seconds histogram  http_response_time_seconds_bucket{code="200",method="GET",path="/banners/post-auth",service="platform",le="0.005"} 1  ...  http_response_time_seconds_sum{code="404",method="POST",path="/revoke",service="platform"} 0.016945976  http_response_time_seconds_count{code="404",method="POST",path="/revoke",service="platform"} 1 ```  Метаданные метрики можно определить в файле `extensions.yaml` как показано ниже:  ```  metrics:  - key: http_response_time_seconds_count  metadata:  displayName: HTTP response time (Histogram count of observed events)  description: Time to respond to request  - key: http_response_time_seconds_sum.count  metadata:  displayName: HTTP response time (Histogram total sum of all observed values)  description: Time to respond to request  unit: Second  - key: http_response_time_seconds_bucket.count  metadata:  displayName: HTTP response time (Histogram buckets split by le)  description: Time to respond to request  unit: Second ```  Чтобы собирать метрики histogram в секции источника данных Prometheus файла `extensions.yaml`:  * Использовать базовое имя метрики без суффикса summary * Указать тип как `histogram`  ```  prometheus:  - group: CipherTrust Metrics  subgroups:  - subgroup: HTTP Traffic  featureSet: HTTP_Traffic  metrics:  - key: http_response_time_seconds  value: metric:http_response_time_seconds  type: histogram ``` |
| [Summary﻿](https://dt-url.net/7g234n1) | * Часть count как `<metric-key>_count` * Часть total sum как `<metric-key>_sum.count` * Отдельные квантили, разбитые по измерению quantile с указанием квантиля, как `<metric-key>` |

## Metric metadata

Extension может определять метаданные для каждой метрики, доступной в Dynatrace. Например, можно добавить отображаемое имя метрики и единицу измерения, которые используются для фильтрации в [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

Все метаданные метрик нужно определять в секции `metrics` файла YAML расширения, чтобы они корректно были связаны с конфигурацией метрики.

```
name: custom:example-extension-name



version: 1.0.0



minDynatraceVersion: "1.236"



author:



name: Dynatrace



metrics:



- key: your.metric.name



metadata:



displayName: Display name of the metric visible in Metrics browser



unit: Count
```

## Feature set

Feature sets, это категории, по которым организуются данные, собираемые расширением. Feature sets можно определять на уровне group, subgroup или metric. В этом примере создаётся Prometheus-расширение, собирающее метрики приложения и сети. Это отражается в организации метрик по соответствующим feature sets `prometheus_app_metrics` и `prometheus_net_metrics`.

```
prometheus:



- group: prometheus metrics



interval: 1m



metrics:



- key: com.dynatrace.extension.prometheus.app



value: prometheus.app



featureSet: prometheus_app_metrics



- key: com.dynatrace.extension.prometheus.net



value: prometheus.net



featureSet: prometheus_net_metrics
```

При активации расширения через monitoring configuration мониторинг можно ограничить одним из feature sets. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях feature sets могут отражать сегменты среды. В таком случае при создании monitoring configuration можно выбрать feature set и соответствующую группу ActiveGate, способную подключиться к конкретному сегменту.

Все метрики, не отнесённые ни к одному feature set, считаются дефолтными и передаются всегда.

Метрика наследует feature set subgroup, а subgroup наследует feature set group. Feature set, определённый на уровне метрики, переопределяет feature set на уровне subgroup, который в свою очередь переопределяет feature set на уровне group.

## Interval

Интервал, с которым выполняется измерение данных. Интервалы можно определять на уровне group, subgroup или отдельной метрики. Минимальная гранулярность интервала, одна минута. Максимальный интервал, 2880 минут (2 дня, 48 часов).

Для JMX data sources задать интервал невозможно.

Например:

```
interval:



minutes: 5
```

Формат выше поддерживается начиная со schema version 1.217. Для более ранних schema versions используется следующий формат (поддерживается до schema version 1.251):

```
interval: 5m
```

```
prometheus:



- group: prometheus metrics



interval: 1m



dimensions:



- key: technology



value: prometheus



metrics:



- key: com.dynatrace.extension.prometheus-rabbitmq.global.global_messages_delivered_get_auto_ack_total



value: metric:rabbitmq_global_messages_delivered_get_auto_ack_total



type: count
```

Метрика наследует интервал subgroup, а subgroup наследует интервал group. Интервал, определённый на уровне метрики, переопределяет интервал на уровне subgroup, который в свою очередь переопределяет интервал на уровне group.

## Monitoring configuration

После определения scope конфигурации нужно указать Prometheus endpoints, с которых собираются данные.

Monitoring configuration, это JSON payload, определяющий детали подключения, учётные данные и feature sets для мониторинга. Подробнее: [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Пример payload для активации Prometheus-расширения:

```
[



{



"scope": "ag_group-default",



"value": {



"version": "1.0.0",



"description": "name",



"enabled": true,



"activationContext": "REMOTE",



"prometheusRemote": {



"endpoints": [



{



"url": "https://myPrometheusServer/metrics",



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}



"autoDiscovery": [



{



"autoDiscoveryType": "dns_sd_config",



"dnsType": "a",



"dnsPort": 1111,



"refreshInterval": "30"



}



]



}



]



},



"featureSets": [



"myFeatureSet"



]



}



}



]
```

Когда исходный файл YAML расширения готов, его нужно упаковать, подписать и загрузить в среду Dynatrace. Подробнее: [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемый JSON payload с вашей monitoring configuration.

Также можно использовать Dynatrace API для загрузки схемы расширения, которая поможет создать JSON payload для monitoring configuration.

Используйте endpoint [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.").

Отправьте следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Нужно заменить `{extension-name}` и `{extension-version}` значениями из файла YAML расширения. При успешном вызове возвращается схема JSON.

### Область применения

Каждый хост OneAgent или ActiveGate, на котором запущено расширение, должен иметь корневой сертификат для проверки его подлинности. Подробнее: [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Описание того, как подписать расширение, загрузить сертификаты и пользовательские расширения, а также настроить права доступа к сертификатам в Dynatrace Extensions Framework.").

Для удалённого расширения область применения, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет выполнять данную конфигурацию мониторинга. Если планируется использовать единственный ActiveGate, его нужно назначить в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Подробнее: [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Основные понятия групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

#### Локальное расширение

Для локального расширения область применения, это хост, группа хостов или зона управления, для которой будет выполняться расширение. Также можно выбрать мониторинг всей среды (опционально с ограничением по тегам).

* При определении хоста в качестве области применения используйте следующий формат:

  ```
  "scope": "<HOST_ID>",
  ```

  Замените `<HOST_ID>` идентификатором сущности хоста, как в следующем примере:

  ```
  "scope": "HOST-A1B2345678C9D001",
  ```
* При определении группы хостов в качестве области применения используйте следующий формат:

  ```
  "scope": "HOST_GROUP-<HOST_GROUP_ID>",
  ```

  Замените `<HOST_GROUP_ID>` идентификатором сущности группы хостов, как в следующем примере:

  ```
  "scope": "HOST_GROUP-AB123C4D567E890",
  ```

  Идентификатор группы хостов можно найти в URL [страницы настроек группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Описание того, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."). Например:

  ```
  https://{your-environment-id}.live.dynatrace.com/#settings/hostgroupconfiguration;id=HOST_GROUP-AB123C4D567E890;hostGroupName=my-host-group
  ```
* При определении зоны управления в качестве области применения используйте следующий формат:

  ```
  "scope": "management_zone-<MANAGEMENT-ZONE>",
  ```

  Замените `<MANAGEMENT-ZONE>` именем зоны управления, как в следующем примере:

  ```
  "scope": "management_zone-sampleManagementZone",
  ```

  Зону управления можно найти на [странице **Management zones settings**](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Применение зон управления для организации среды Dynatrace и управления доступом пользователей к конкретным данным.").
* При определении среды в качестве области применения используйте следующий формат:

  ```
  "scope": "environment",
  ```

  Также можно добавить теги для фильтрации хостов, на которых будет применяться данная конфигурация:

  ```
  "activationTags": [



  "dt.owner:lama"



  ]
  ```

Если активировать локальное расширение Prometheus и определить [endpoint](#url) Prometheus Server, запущенного на том же хосте, метрики, собранные с этого сервера, могут поступать из различных endpoints, а не только с endpoint на этом хосте; при этом все метрики будут обогащены контекстом хоста с установленным OneAgent.

### Version

Версия данной конфигурации мониторинга. Одно расширение может выполняться с несколькими конфигурациями мониторинга.

### Description

Понятное описание особенностей данной конфигурации мониторинга.

### Enabled

Если установлено значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Activation context

* Для удалённых расширений установите `activationContext` в значение `REMOTE`
* Для локальных расширений установите `activationContext` в значение `LOCAL`

### URL

URL, это endpoint Prometheus, из которого расширение собирает метрики. Максимальная длина URL составляет 500 символов.

* Для локальных расширений определите endpoint Prometheus в узле `prometheusLocal`.
* Для удалённых расширений определите endpoint Prometheus в узле `prometheusRemote`.

Можно определить следующие типы endpoints:

* `/metrics` – возвращает метрики в текстовом формате Prometheus.
* `/api/v1/` – путь API, за которым может непосредственно следовать endpoint `query` или `metadata`.

Если одни и те же метрики собираются из разных endpoints (сервер Prometheus или экспортёр данных), часть метрик может быть перезаписана, поскольку ключи будут идентичны вне зависимости от endpoint. Чтобы избежать этого, к каждой метрике автоматически добавляется дополнительное измерение `activation_endpoint`.

### Authentication

Данные аутентификации, переданные в Dynatrace API при активации конфигурации мониторинга, обфусцируются и не могут быть получены повторно.

#### No authentication

По умолчанию поддерживается только для HTTP-endpoints.

```
"authentication": {



"scheme": "none"



}
```

#### Bearer

Для аутентификации Bearer требуется только токен.

```
"authentication": {



"scheme": "bearer",



"token": "myToken"



}
```

#### Basic

Для Basic-аутентификации требуются только имя пользователя и пароль.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}
```

#### AWS - requires AWS access key, secret key, and region.

Для AWS-аутентификации требуются ключ доступа AWS, секретный ключ и регион.

```
"authentication": {



"scheme": "aws",



"accessKey": "accessKey",



"secretKey": "secretKey",



"region": "us-east-2"



}
```

При попытке использовать HTTP-endpoint со схемой bearer, basic или AWS фреймворк расширений выдаёт ошибку, чтобы предотвратить передачу конфиденциальных данных по незащищённому соединению. Если же передача данных по HTTP допустима, установите свойству `skipVerifyHttps` значение `true`.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password",



"skipVerifyHttps": "true"



}
```

#### Credential vault

Только для удалённого мониторинга

Тип аутентификации Credential vault обеспечивает более защищённый подход к использованию расширений за счёт безопасного хранения учётных данных пользователей и управления ими. Для использования этого типа необходимо быть владельцем учётных данных и иметь хранилище учётных данных, соответствующее следующим критериям:

* **Тип учётных данных**: пользователь и пароль для Basic Authentication, а также имя пользователя и Programmatic Access Token (PAT) для аутентификации Programmatic Access Token (PAT)
* **Область учётных данных**: включены области Synthetic (при использовании внешнего хранилища) и Extension authentication
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"skipVerifyHttps": false,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

Для SSL-взаимодействия между Prometheus и экспортёрами Prometheus сертификат хоста Prometheus нужно добавить в системное хранилище доверенных сертификатов на машинах ActiveGate, на которых выполняется расширение.

Порядок добавления сертификата в системное хранилище доверенных сертификатов см. в документации соответствующей операционной системы.

### Feature sets

Добавьте список наборов функций (feature sets), которые нужно отслеживать. Чтобы включить все наборы функций, добавьте `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Advanced

При необходимости можно задать дополнительные настройки, управляющие HTTP-соединением с endpoints Prometheus:

* `timeoutSecs`  
  Целое число от 0 до 50. Количество секунд ожидания ответа от endpoint Prometheus.
* `retries`  
  Количество повторных попыток соединения. Максимальное число попыток, 3.
* `collectHistogramBuckets`  
  Включить или отключить загрузку [бакетов метрик гистограммы Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#type "Описание расширений Prometheus в рамках фреймворка Extensions.").

Возможно максимум 3 повторные попытки соединения по 50 секунд каждая.

Суммарное время ожидания не должно превышать [интервал](#interval), установленный для метрик.

### Auto Discovery

Только для удалённого мониторинга

Автообнаружение (Autodiscovery), это функция, которая автоматически разрешает DNS-endpoints. Если автообнаружение настроено, URL становится DNS-именем.

```
"configuration": [



{



"configurationType": "dns_sd_config",



"dnsType": "a",



"dnsPort": 1111,



"refreshInterval": "30m"



}



]
```

* **Тип автообнаружения**: доступен только тип `DNS`.
* **Тип DNS**: тип выполняемого DNS-запроса. Доступен только тип `A`, соответствующий IPv4-адресам.
* **Порт DNS**: задаёт порт, назначенный всем IP-адресам, разрешённым DNS.
* **Интервал обновления DNS (сек.)**: задаёт интервал обновления в секундах для часто меняющихся IP-адресов.

## Resource consumption

Потребление ресурсов зависит от количества endpoints Prometheus. Первый endpoint потребляет 25 МБ оперативной памяти и 0,2%–0,5% CPU. Каждый последующий endpoint потребляет 0,5 МБ оперативной памяти и ~0,2% CPU.

| Endpoints | Средний CPU | Макс. CPU | RAM (МБ) | Хост (тип инстанса EC2) |
| --- | --- | --- | --- | --- |
| 100 | 1.0% | 2.5% (пик в начале) | 60 | XS (`c5.large`) |
| 1 | 0.2% | 0.5% (пик в начале) | 25 | XS (`c5.large`) |