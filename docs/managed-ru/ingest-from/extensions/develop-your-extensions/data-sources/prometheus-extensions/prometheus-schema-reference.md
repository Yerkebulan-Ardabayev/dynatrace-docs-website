---
title: Справочник по источнику данных Prometheus
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference
scraped: 2026-05-12T12:08:18.392397
---

# Справочник по источнику данных Prometheus

# Справочник по источнику данных Prometheus

* Справочник
* Чтение: 13 мин
* Обновлено 10 ноября 2025 г.

Это общее описание YAML-файла расширения на основе источника данных Prometheus, а также способов объявления метрик и измерений для сбора в расширении.

## Область данных

Составьте перечень эндпоинтов Prometheus, которые нужно использовать в расширении, а также метрик и значений измерений.

В примере создаётся простое расширение для сбора метрик RabbitMQ.

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

Определение области мониторинга Prometheus начинается с узла `prometheus` в YAML. Все настройки под этим узлом относятся к объявленному [типу источника данных](/managed/ingest-from/extensions/concepts#data-source-type "Подробнее о концепции Dynatrace Extensions.") (в данном случае Prometheus).

## Измерения

На каждом уровне (группа, подгруппа) допускается определять до 25 измерений, что даёт в сумме до 50 измерений на метрику.

### Ключ измерения

Строка ключа измерения должна соответствовать [протоколу приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

### Значение измерения

Для определения измерений метрик доступны следующие методы:

* Обычный текст. Используйте префикс `const:` или просто добавьте нужный текст

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
* [Метка Prometheus](https://prometheus.io/docs/practices/naming/#metric-and-label-naming)

  ```
  dimensions:



  - key: customdimension.job



  value: label:job



  filter: const:$eq(prometheus)
  ```

  Все метки, предоставляемые Prometheus, автоматически создаются как измерения. Явно определять измерение на основе метки нужно только в следующих случаях:

  + применить фильтрацию значений,
  + определить пользовательский ключ измерения.

### Фильтрация извлечённых строк метрик

При извлечении строк метрик можно добавить логику фильтрации, чтобы передавались только те строки, значение измерения которых соответствует критериям фильтра.

Фильтр на основе условия определяется следующим образом:

* **Начинается с**: используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Заканчивается на**: используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Содержит**: используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Равно**: используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для перечисленных выше выражений также доступны следующие квалификаторы:

  + `const:$and`: объединение двух и более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or`: объединение двух и более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not`: отрицание выражения. Пример:

    ```
    filter: const:$not(<expr>)
    ```

Сложные фильтры создаются путём объединения двух и более фильтров через запятую с использованием логических выражений:

```
dimensions:



- key: technology



value: other



- key: job



value: label:job



filter: const:$or($eq(),$not($or($eq(prometheus),$eq(rabbitmq-server),$eq(redis_exporter),$eq(node_exporter)))
```

## Метрики

На каждом уровне (группа, подгруппа) допускается определять до 100 метрик. Однако во время выполнения действует жёсткий предел в 1000 метрик на расширение. Этот предел ниже суммарных ограничений для разрешённых групп и подгрупп.

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

Для Dynatrace версий 1.215 и 1.217 узел метрики требует параметра `id` вместо `key`. Начиная с Dynatrace версии 1.219 рекомендуется использовать параметр `key`, так как `id` будет устаревшим.

#### Рекомендации по ключам метрик

Метрики, принимаемые в Dynatrace с помощью расширения, являются лишь частью тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко идентифицируемыми в Dynatrace, рекомендуется добавлять к имени метрики префикс в виде имени расширения. Это гарантирует уникальность ключа метрики и позволяет легко привязать метрику к конкретному расширению в окружении.

### Значение метрики

Ключ метрики Prometheus, из которого нужно извлечь значение метрики, указывается с префиксом `metric:`.

### Тип

Платформа Dynatrace Extensions поддерживает все исходные форматы данных метрик Prometheus. Подробные сведения см. в разделе [Данные метрики](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API."). Для указания типа метрики используется атрибут `type`.

| Тип Prometheus | Приём в Dynatrace |
| --- | --- |
| [Counter](https://dt-url.net/hq634n9) | `count` |
| [Gauge](https://dt-url.net/a2434zx) | `gauge` |
| [Histogram](https://dt-url.net/5x034gl) | **Примечание**: [Перцентиль временного ряда](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") доступен только клиентам DPS с тарифным планом **Metrics powered by Grail**. Функция вычисляет запрошенный перцентиль значения выражения в каждом бакете, поэтому она естественно используется с гистограммами.  * Часть Count как `<metric-key>_count` * Часть Total sum как `<metric-key>_sum.count` * Отдельные бакеты, разделённые измерением `le`, обозначающим идентификатор бакета, как `<metric-key>_bucket.count`  Приём метрик отдельных бакетов отключён по умолчанию. Сведения о том, как включить его, см. в [описании расширенной конфигурации мониторинга расширений](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#advanced "Узнайте о расширениях Prometheus в платформе Extensions."). Примеры кода Histogram. Стандартная метрика гистограммы Prometheus включает:  * `HELP` и `TYPE` * Данные бакетов и сводные метрики `sum` и `count`  ```  # HELP http_response_time_seconds Time to respond to request  # TYPE http_response_time_seconds histogram  http_response_time_seconds_bucket{code="200",method="GET",path="/banners/post-auth",service="platform",le="0.005"} 1  ...  http_response_time_seconds_sum{code="404",method="POST",path="/revoke",service="platform"} 0.016945976  http_response_time_seconds_count{code="404",method="POST",path="/revoke",service="platform"} 1 ```  Метаданные метрики можно определить в файле `extensions.yaml`, как показано ниже:  ```  metrics:  - key: http_response_time_seconds_count  metadata:  displayName: HTTP response time (Histogram count of observed events)  description: Time to respond to request  - key: http_response_time_seconds_sum.count  metadata:  displayName: HTTP response time (Histogram total sum of all observed values)  description: Time to respond to request  unit: Second  - key: http_response_time_seconds_bucket.count  metadata:  displayName: HTTP response time (Histogram buckets split by le)  description: Time to respond to request  unit: Second ```  Для приёма метрик гистограммы в разделе источника данных Prometheus файла `extensions.yaml`:  * Используйте базовое имя метрики без суффикса сводки * Укажите тип `histogram`  ```  prometheus:  - group: CipherTrust Metrics  subgroups:  - subgroup: HTTP Traffic  featureSet: HTTP_Traffic  metrics:  - key: http_response_time_seconds  value: metric:http_response_time_seconds  type: histogram ``` |
| [Summary](https://dt-url.net/7g234n1) | * Часть Count как `<metric-key>_count` * Часть Total sum как `<metric-key>_sum.count` * Отдельные квантили, разделённые измерением квантиля, обозначающим квантиль, как `<metric-key>` |

## Метаданные метрик

Расширение может определять метаданные для каждой метрики, доступной в Dynatrace. Например, можно добавить отображаемое имя метрики и единицу измерения: оба параметра можно использовать для фильтрации в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace.").

Все метаданные метрик определяются в разделе `metrics` YAML-файла расширения для корректной привязки к конфигурации метрики.

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

## Набор функций

Наборы функций: категории, по которым организуются данные, собираемые расширением. Наборы функций можно определять на уровне группы, подгруппы или метрики. В этом примере создаётся расширение Prometheus для сбора метрик приложений и сети. Это отражается в организации метрик в связанные наборы функций `prometheus_app_metrics` и `prometheus_net_metrics`.

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

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) мониторинг можно ограничить одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сетях с высокой степенью сегментации наборы функций могут отражать сегменты окружения. При создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, которая может подключиться к этому сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются используемыми по умолчанию и всегда передаются.

Метрика наследует набор функций подгруппы, которая в свою очередь наследует набор функций группы. Набор функций, определённый на уровне метрики, переопределяет набор функций на уровне подгруппы, который в свою очередь переопределяет набор функций на уровне группы.

## Интервал

Интервал, с которым выполняется измерение данных. Интервалы можно определять на уровне группы, подгруппы или отдельной метрики с гранулярностью одной минуты. Максимальный интервал составляет 2880 минут (2 дня, 48 часов).

Для источников данных JMX задать интервал невозможно.

Например:

```
interval:



minutes: 5
```

Приведённый выше формат поддерживается начиная со схемы версии 1.217. Для более ранних версий схемы используйте следующий формат (поддерживается до версии схемы 1.251):

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

Метрика наследует интервал подгруппы, которая в свою очередь наследует интервал группы. Интервал, определённый на уровне метрики, переопределяет интервал на уровне подгруппы, который в свою очередь переопределяет интервал на уровне группы.

## Конфигурация мониторинга

После определения области конфигурации необходимо указать эндпоинты Prometheus, из которых будут собираться данные.

Конфигурация мониторинга представляет собой JSON-данные, определяющие параметры подключения, учётные данные и наборы функций для мониторинга. Подробные сведения см. в разделе [Запуск мониторинга](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Пример данных для активации расширения Prometheus:

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

Когда исходный YAML-файл расширения готов, упакуйте его, подпишите и загрузите в окружение Dynatrace. Подробные сведения см. в разделе [Управление жизненным циклом расширения](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемые JSON-данные с конфигурацией мониторинга.

Также можно использовать Dynatrace API для загрузки схемы расширения, которая поможет создать JSON-данные для конфигурации мониторинга.

Используйте эндпоинт [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "Просмотр схемы расширения через Dynatrace Extensions 2.0 API.").

Выполните следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Замените `{extension-name}` и `{extension-version}` значениями из YAML-файла расширения. При успешном вызове возвращается схема JSON.

### Область

Каждый хост OneAgent или ActiveGate, выполняющий расширение, должен иметь корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Для удалённого расширения область: группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет запускать эту конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время или после установки. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

#### Локальное расширение

Для локального расширения область: хост, группа хостов или зона управления, для которой будет выполняться расширение. Также можно выбрать мониторинг всего окружения (при необходимости с ограничением по тегам).

* При определении хоста в качестве области используйте следующий формат:

  ```
  "scope": "<HOST_ID>",
  ```

  Замените `<HOST_ID>` идентификатором сущности хоста, как в этом примере:

  ```
  "scope": "HOST-A1B2345678C9D001",
  ```
* При определении группы хостов в качестве области используйте следующий формат:

  ```
  "scope": "HOST_GROUP-<HOST_GROUP_ID>",
  ```

  Замените `<HOST_GROUP_ID>` идентификатором сущности группы хостов, как в этом примере:

  ```
  "scope": "HOST_GROUP-AB123C4D567E890",
  ```

  Идентификатор группы хостов можно найти в URL [страницы настроек группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."). Например:

  ```
  https://{your-environment-id}.live.dynatrace.com/#settings/hostgroupconfiguration;id=HOST_GROUP-AB123C4D567E890;hostGroupName=my-host-group
  ```
* При определении зоны управления в качестве области используйте следующий формат:

  ```
  "scope": "management_zone-<MANAGEMENT-ZONE>",
  ```

  Замените `<MANAGEMENT-ZONE>` именем зоны управления, как в этом примере:

  ```
  "scope": "management_zone-sampleManagementZone",
  ```

  Зону управления можно найти на [странице **Настройки зон управления**](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Применяйте зоны управления для организации окружения Dynatrace и управления доступом пользователей к конкретным данным.").
* При определении окружения в качестве области используйте следующий формат:

  ```
  "scope": "environment",
  ```

  Также можно добавить теги для фильтрации хостов, на которых будет выполняться эта конфигурация:

  ```
  "activationTags": [



  "dt.owner:lama"



  ]
  ```

Если активировать локальное расширение Prometheus и определить [эндпоинт](#url) сервера Prometheus, работающего на том же хосте, метрики, собранные с этого сервера, могут поступать из различных эндпоинтов, а не только с эндпоинта на этом хосте. При этом все метрики будут обогащены контекстом хоста с установленным OneAgent.

### Версия

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Описание

Описание особенностей данной конфигурации мониторинга в понятном для человека формате.

### Включено

При значении `true` конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Контекст активации

* Для удалённых расширений задайте `activationContext` значение `REMOTE`
* Для локальных расширений задайте `activationContext` значение `LOCAL`

### URL

URL: эндпоинт Prometheus, из которого расширение получает метрики. Максимальная длина URL составляет 500 символов.

* Для локальных расширений определите эндпоинт Prometheus в узле `prometheusLocal`.
* Для удалённых расширений определите эндпоинт Prometheus в узле `prometheusRemote`.

Доступны следующие типы эндпоинтов:

* `/metrics`: возвращает метрики в текстовом формате Prometheus.
* `/api/v1/`: путь API, который может непосредственно завершаться эндпоинтом `query` или `metadata`.

При сборе одинаковых метрик из разных эндпоинтов (сервера Prometheus или экспортёра данных) некоторые метрики могут быть перезаписаны, так как ключи совпадают независимо от эндпоинта. Во избежание этого к каждой метрике автоматически добавляется дополнительное измерение `activation_endpoint`.

### Аутентификация

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, обфусцируются и не могут быть получены.

#### Без аутентификации

По умолчанию поддерживается только для HTTP-эндпоинтов.

```
"authentication": {



"scheme": "none"



}
```

#### Bearer

Аутентификация Bearer требует только токен.

```
"authentication": {



"scheme": "bearer",



"token": "myToken"



}
```

#### Basic

Аутентификация Basic требует только имя пользователя и пароль.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}
```

#### AWS

Аутентификация AWS требует ключ доступа AWS, секретный ключ и регион.

```
"authentication": {



"scheme": "aws",



"accessKey": "accessKey",



"secretKey": "secretKey",



"region": "us-east-2"



}
```

При попытке использовать HTTP-эндпоинт со схемой bearer, basic или AWS платформа расширений выдаёт ошибку во избежание передачи конфиденциальных данных по незащищённому соединению. Если передача данных по HTTP заведомо допустима, установите свойство `skipVerifyHttps` в значение `true`.

```
"authentication": {



"scheme": "basic",



"username": "user",



"password": "password",



"skipVerifyHttps": "true"



}
```

#### Хранилище учётных данных

Только для удалённого мониторинга

Тип аутентификации через хранилище учётных данных обеспечивает более безопасный подход к использованию расширений путём защищённого хранения и управления учётными данными пользователя. Для использования этого типа необходимо быть владельцем учётных данных и иметь хранилище учётных данных, соответствующее следующим критериям:

* **Тип учётных данных**: пользователь и пароль
* **Область учётных данных**: включены области Synthetic (при использовании внешнего хранилища) и аутентификации Extension
* **Доступ только для владельца**: включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"skipVerifyHttps": false,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

Для SSL-связи между Prometheus и экспортёрами Prometheus сертификат хоста Prometheus необходимо добавить в доверенное хранилище операционной системы на машинах ActiveGate, выполняющих расширение.

Обратитесь к документации по операционной системе для получения сведений о добавлении сертификата в доверенное хранилище.

### Наборы функций

Добавьте список наборов функций для мониторинга. Чтобы передавать все наборы функций, укажите `all`.

```
"featureSets": [



"basic",



"advanced"



]
```

### Расширенные настройки

При необходимости можно определить расширенные настройки, управляющие HTTP-подключением к эндпоинтам Prometheus:

* `timeoutSecs`
  Целое число от 0 до 50. Количество секунд ожидания ответа от эндпоинта Prometheus.
* `retries`
  Количество повторных попыток подключения. Максимальное количество повторных попыток составляет 3.
* `collectHistogramBuckets`
  Включение или отключение приёма [бакетов метрик гистограммы Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#type "Узнайте о расширениях Prometheus в платформе Extensions.").

Допускается не более 3 повторных попыток подключения продолжительностью до 50 секунд каждая.

Следите за тем, чтобы общее время ожидания не превышало [интервал](#interval), заданный для метрик.

### Автообнаружение

Только для удалённого мониторинга

Автообнаружение: функция, которая автоматически разрешает DNS-эндпоинты. Если автообнаружение определено, URL становится DNS-именем.

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
* **Порт DNS**: указывает порт, назначенный всем IP-адресам, разрешённым DNS.
* **Интервал обновления DNS (сек)**: задаёт интервал в секундах для часто меняющихся IP-адресов.

## Потребление ресурсов

Потребление ресурсов зависит от количества эндпоинтов Prometheus. Первый эндпоинт потребляет 25 МБ ОЗУ и 0,2-0,5% ЦПУ. Каждый последующий эндпоинт потребляет 0,5 МБ ОЗУ и около 0,2% ЦПУ.

| Эндпоинты | Средний ЦПУ | Макс. ЦПУ | ОЗУ (МБ) | Хост (тип экземпляра EC2) |
| --- | --- | --- | --- | --- |
| 100 | 1,0% | 2,5% (всплеск в начале) | 60 | XS (`c5.large`) |
| 1 | 0,2% | 0,5% (всплеск в начале) | 25 | XS (`c5.large`) |