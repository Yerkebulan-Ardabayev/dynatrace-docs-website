---
title: Настройка Monaco YAML файла - список особых типов конфигурации
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas
scraped: 2026-03-06T21:33:46.968318
---

# Файл конфигурации Monaco YAML — список специальных типов конфигурации


* Latest Dynatrace
* 6 мин. чтения

В этом разделе описывается, как должна присутствовать только одна конечная точка конфигурации. Также описываются типы конфигурации с нестандартным поведением и специфическими ограничениями при работе с соответствующими API.
Подробнее см. [поддерживаемые типы Configuration API](../monaco-api-support-and-access-handling.md#supported-api-types "Список поддержки Monaco API и обработки прав доступа.").

## Единая конечная точка конфигурации

Эти конфигурации являются глобальными для среды Dynatrace и создаются однократно.
В отличие от других конфигураций, обычно существует некоторая конфигурация по умолчанию, которую можно обновить.

Имейте в виду, что в вашей конфигурации должна присутствовать только одна такая конфигурация.
Наличие нескольких конфигураций, например, в нескольких проектах, развёрнутых за один запуск, приводит к тому, что активной в среде Dynatrace будет последняя применённая конфигурация.

## Неуникальное имя

Monaco предполагает уникальное имя конфигурации и использует его как идентификатор при создании или обновлении конфигурации.
Это верно для большинства конфигураций, создаваемых в веб-интерфейсе Dynatrace или через вызовы API.

Некоторые конфигурации могут иметь одинаковые имена, что вызывает проблемы для CLI Dynatrace Monaco.
Например, может существовать несколько дашбордов с именем `MyDashboard`.
Если присутствует более одной конфигурации с одинаковым именем, CLI Dynatrace Monaco не может гарантировать, что при поиске по имени обновляется правильная конфигурация. Аналогичные проблемы возникают при загрузке.

CLI Dynatrace Monaco специально обрабатывает эти API конфигурации, чтобы обеспечить следующее:

* Они получают известный идентификатор, если были созданы через CLI Dynatrace Monaco.
* Они сохраняются с их идентификатором Dynatrace, а не с именем, при загрузке.

## Вычисляемые метрики

Имена типов вычисляемых метрик должны быть глобально уникальными.
В противном случае Monaco может выдать ошибки `duplicate config name`.

В целом вычисляемые метрики ведут себя как типы с неуникальным именем, но используют `metricKey`, который вы можете определить как идентификатор, поэтому описанная выше автоматическая обработка невозможна.

Хотя API и веб-интерфейс позволяют создавать несколько конфигураций с одинаковым `name`, CLI Dynatrace Monaco не может однозначно идентифицировать эти конфигурации.
После [загрузки](../reference/commands-saas.md#download "Как использовать приложение Monaco CLI, включая аргументы и параметры.") вы можете увидеть ошибки `duplicate config name` для типов вычисляемых метрик.

Тип `calculated-metrics-log`, который позволяет настраивать метрики для устаревшего Logs v1, требует дополнительной специальной обработки. Подробнее см. [JSON вычисляемых метрик логов](special-configuration-types-saas.md#log-metrics-json "Список специальных типов конфигурации Monaco.") ниже.

## Объекты Settings 2.0

Обработка объектов Settings 2.0 отличается от классических конфигураций.
В отличие от последних, которые обычно идентифицируются по имени, объекты Settings 2.0 могут не иметь уникального имени или вообще не иметь имени.
Вместо этого им назначается внешний идентификатор `externalId`, который позволяет однозначно их идентифицировать.

`externalId` состоит из префикса `monaco:`, за которым следует идентификатор, сгенерированный CLI Dynatrace Monaco при развёртывании.

Чтобы обеспечить надёжное обновление существующих объектов Settings 2.0, CLI Dynatrace Monaco записывает исходные идентификаторы объектов Dynatrace при загрузке и включает их в поле конфигурации YAML `originObjectId`.

Объекты Settings также имеют специальные требования к своим JSON-шаблонам. Подробнее см. [JSON Settings](special-configuration-types-saas.md#settings-json "Список специальных типов конфигурации Monaco.") ниже.

## Специальные требования к JSON-шаблонам

Некоторые типы конфигурации имеют специальные требования к своим JSON-данным и могут потребовать ручного внимания.

### JSON дашборда

Когда вы создаёте дашборд, он по умолчанию является приватным.
Все дашборды, определённые через Configuration as Code, должны быть опубликованы для других пользователей; в противном случае их сможет видеть только владелец токена доступа, использованного для развёртывания.
Вы можете изменить это в **Settings** дашборда или изменив ваш зафиксированный `json`-файл.

Мы рекомендуем следующие значения для `dashboardMetadata`:

```
"dashboardMetadata": {


"name": "{{ .name }}",


"shared": true,


"sharingDetails": {


"linkShared": true,


"published": true


},


"dashboardFilter": {


"timeframe": "",


"managementZone": {


"id": "{{ .managementZoneId }}",


"name": "{{ .managementZoneName }}"


}


}


}
```

Эта конфигурация выполняет следующее:

* Ссылается на имя дашборда как на [переменную](#configuration-yaml-structure)
* Делает дашборд доступным для других пользователей
* Устанавливает фильтр зоны управления на весь дашборд, опять же как переменную, обычно [ссылающуюся из другой конфигурации](yaml-configuration-saas.md#reference "Структура файла конфигурации Monaco YAML.") TODO

Фильтрация всего дашборда по зоне управления гарантирует, что плитки дашборда будут отображать только те данные, которые предназначены для отображения, и устраняет возможную необходимость определять фильтры для отдельных плиток.

* CLI Dynatrace Monaco версии 1.208+: конфигурация дашборда должна иметь свойство owner. Свойство owner в `dashboardMetadata` является обязательным и должно содержать ненулевое значение.
* CLI Dynatrace Monaco версии 1.208+: свойство `sharingDetails` в `dashboardMetadata` больше не присутствует.

### JSON вычисляемых метрик логов

API вычисляемых метрик логов требует соблюдения следующих специфических соглашений об именовании.
Чтобы Dynatrace Monaco учитывал эти конфигурации, `metricKey` метрики логов должен быть повторно использован как `name` конфигурации.

Если вы сталкиваетесь с ошибками развёртывания конфигурации, попробуйте установить одинаковое значение для `metricKey` и `displayName`.

Вам необходимо сослаться как минимум на `metricKey` метрики логов как на `{{ .name }}` в JSON-файле, как показано здесь:

```
configs:


- id: some-log-metric-config


config:


name:  "cal.log:this-is-some-metric"


[...]
```

И в соответствующем JSON:

```
{


"metricKey": "{{ .name }}",


"active": true,


"displayName": "{{ .name }}",


[...]


}
```

### JSON условного именования

API условного именования не предоставляет параметр `name`.
Поскольку CLI Dynatrace Monaco требует свойство name в `config.yaml`, его необходимо сопоставить с полем `displayName` в JSON-шаблоне.

Тип `PROCESS_GROUP`:

```
{


"type": "PROCESS_GROUP",


"nameFormat": "Test naming PG for {Host:DetectedName}",


"displayName": "{{ .name }}",


[...]


}
```

Тип `HOST`:

```
{


"type": "HOST",


"nameFormat": "Test - {Host:DetectedName}",


"displayName": "{{ .name }}",


[...]


}
```

Тип `SERVICE`:

```
{


"type": "SERVICE",


"nameFormat": "{ProcessGroup:KubernetesNamespace} - {Service:DetectedName}",


"displayName": "{{ .name }}",


...


}
```

### JSON Settings 2.0

Settings API имеет дополнительные свойства, не связанные с конкретными схемами.
Это требует от CLI Dynatrace Monaco установки дополнительных параметров.

JSON-шаблоны для Settings должны содержать только фактическое содержимое `value`.

Например, в то время как ответ API для конфигурации пользовательского оповещения (`builtin:davis.anomaly-detectors`) выглядит так:

```
{


"items": [


{


"objectId": "XYZ",


"value": {


"enabled": false,


"title": "Error when adding item to cart",


"description": "",


"source": "Anomaly Detection",


"executionSettings": {


"queryOffset": 3


},


"analyzer": {


"name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",


"input": [


{


"key": "query",


"value": "timeseries cartFailedToAddItem=sum(log.cartFailedToAddItem)"


},


{


"key": "slidingWindow",


"value": "3"


},


{


"key": "violatingSamples",


"value": "1"


},


{


"key": "dealertingSamples",


"value": "3"


},


{


"key": "alertCondition",


"value": "ABOVE"


},


{


"key": "alertOnMissingData",


"value": "false"


},


{


"key": "threshold",


"value": "0"


}


]


},


"eventTemplate": {


"properties": [


{


"key": "event.name",


"value": "Cart Failure increase"


},


{


"key": "event.description",


"value": "The {metricname} value was {alert_condition} normal behavior."


},


{


"key": "event.type",


"value": "ERROR_EVENT"


},


{


"key": "dt.event.allow_davis_merge",


"value": "true"


}


]


}


}


}


]


"totalCount": 89,


"pageSize": 1,


"nextPageKey": "XY"


}
```

JSON-шаблон Dynatrace Monaco требует только содержимое `value`:

```
{


"enabled": false,


"title": "Error when adding item to cart",


"description": "",


"source": "Anomaly Detection",


"executionSettings": {


"queryOffset": 3


},


"analyzer": {


"name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",


"input": [


{


"key": "query",


"value": "timeseries cartFailedToAddItem=sum(log.cartFailedToAddItem)"


},


{


"key": "slidingWindow",


"value": "3"


},


{


"key": "violatingSamples",


"value": "1"


},


{


"key": "dealertingSamples",


"value": "3"


},


{


"key": "alertCondition",


"value": "ABOVE"


},


{


"key": "alertOnMissingData",


"value": "false"


},


{


"key": "threshold",


"value": "0"


}


]


},


"eventTemplate": {


"properties": [


{


"key": "event.name",


"value": "Cart Failure increase"


},


{


"key": "event.description",


"value": "The {metricname} value was {alert_condition} normal behavior."


},


{


"key": "event.type",


"value": "ERROR_EVENT"


},


{


"key": "dt.event.allow_davis_merge",


"value": "true"


}


]


}


}
```

При использовании [команды загрузки](../reference/commands-saas.md#download "Как использовать приложение Monaco CLI, включая аргументы и параметры.") это происходит автоматически.