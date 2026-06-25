---
title: Специальные типы конфигурации Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration/special-configuration-types
scraped: 2026-05-12T12:35:11.736594
---

# Monaco special configuration types

# Monaco special configuration types

* Explanation
* 6-min read
* Updated on Oct 21, 2025

Следующие типы конфигурации имеют нестандартное поведение и ограничения, обусловленные особенностями соответствующих Dynatrace API.

## Конечная точка с единственной конфигурацией

Эти конфигурации являются глобальными для окружения Dynatrace и **существуют только в единственном экземпляре**. В отличие от других конфигураций, обычно имеется некоторая конфигурация по умолчанию, которую API или Dynatrace Monaco CLI позволяет обновить.

Необходимо убедиться, что в вашей конфигурации присутствует только одна такая конфигурация. Наличие нескольких конфигураций (например, в нескольких проектах, развёртываемых за один запуск) приведёт к тому, что в окружении Dynatrace будет активна последняя применённая конфигурация.

## Неуникальное имя

Dynatrace Monaco CLI предполагает, что **имя конфигурации уникально**, и использует его в качестве идентификатора при принятии решения о создании или обновлении конфигурации. Это справедливо для большинства конфигураций при создании через UI Dynatrace или через API.

Однако у некоторых конфигураций могут быть совпадающие имена, что создаёт проблемы для Dynatrace Monaco CLI. Например, может существовать несколько дашбордов с именем **My Dashboard**. Если присутствует более одной конфигурации с таким именем, Dynatrace Monaco CLI не может гарантировать обновление нужной при поиске по имени. Аналогичные проблемы возникают при загрузке.

Для решения этой проблемы предусмотрена специальная обработка для данных API конфигурации, обеспечивающая:

* Присвоение известного идентификатора при создании конфигурации через Dynatrace Monaco CLI.
* Хранение с идентификатором Dynatrace, а не с именем, при загрузке.

### Вычисляемые метрики

Вычисляемые метрики в целом ведут себя как типы с неуникальным именем, но используют задаваемый `metricKey` в качестве идентификаторов, поэтому описанная выше автоматизированная обработка неприменима.

Для большинства типов вычисляемых метрик достаточно вручную обеспечить уникальность имён.

Тип `calculated-metrics-log`, позволяющий настраивать метрики для устаревшего Logs v1, требует дополнительной специальной обработки, как описано в разделе [JSON вычисляемых метрик логов](/managed/deliver/configuration-as-code/monaco/configuration/special-configuration-types#log-metrics-json "Dynatrace Configuration as Code via Monaco - special configuration types.") ниже.

## Объекты Settings 2.0

Обработка объектов Settings 2.0 отличается от обычных конфигураций.
В отличие от последних, которые обычно идентифицируются по имени, объекты Settings 2.0 могут не иметь уникального имени или вообще не иметь имени.
Вместо этого им присваивается внешний идентификатор `externalId`, обеспечивающий их уникальную идентификацию.

`externalId` состоит из префикса `monaco:`, за которым следует идентификатор, генерируемый Dynatrace Monaco CLI при развёртывании.

Кроме того, для надёжного обновления существующих объектов Settings 2.0 Dynatrace Monaco CLI хранит исходные идентификаторы объектов Dynatrace при загрузке и включает их в поле конфигурации YAML `originObjectId`.

Объекты Settings также имеют специальные требования к JSON-шаблонам. Подробнее см. в разделе [JSON для Settings](/managed/deliver/configuration-as-code/monaco/configuration/special-configuration-types#settings-json "Dynatrace Configuration as Code via Monaco - special configuration types.") ниже.

## Специальные требования к JSON-шаблонам

Некоторые типы конфигурации имеют особые требования к JSON-полезным нагрузкам и могут потребовать ручного внимания.

### JSON дашборда

При создании дашборда в Dynatrace он по умолчанию является приватным.
Все дашборды, определённые через Configuration as Code, необходимо сделать общедоступными для других пользователей; в противном случае их сможет просматривать только владелец токена доступа, использованного при развёртывании.
Это можно изменить в настройках дашборда или просто отредактировав зафиксированный `json`-файл.
Для `dashboardMetadata` рекомендуются следующие значения:

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

Данная конфигурация:

* Ссылается на имя дашборда как на [переменную](#configuration-yaml-structure)
* Делает дашборд общедоступным для других пользователей
* Устанавливает фильтр зоны управления на весь дашборд также в виде переменной, скорее всего [ссылающейся на другую конфигурацию](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#reference "Learn how to set up your Monaco YAML configuration.")

  Фильтрация всего дашборда по зоне управления гарантирует, что плитки дашборда получают только нужные данные, и устраняет необходимость определять фильтры для отдельных плиток.

* Dynatrace версии 1.208+: конфигурация дашборда должна содержать свойство owner. Свойство owner в `dashboardMetadata` является обязательным и должно содержать ненулевое значение.
* Dynatrace версии 1.208+: свойство `sharingDetails` в `dashboardMetadata` больше не присутствует.

### JSON вычисляемых метрик логов

Существует известное ограничение обходного решения Dynatrace Monaco CLI для слегка нестандартного API **вычисляемых метрик логов**, требующего соблюдения специальных соглашений об именовании конфигурации: при создании пользовательских метрик логов `name` конфигурации должен совпадать с `metricKey` метрики лога.

Кроме того, загрузка конфигурации может завершиться ошибкой, если новая конфигурация метрики только что создана, а другая конфигурация зависит от неё. Для обхода этой проблемы установите для `metricKey` и `displayName` одинаковое значение.

Таким образом, необходимо ссылаться как минимум на `metricKey` метрики лога через `{{ .name }}` в JSON-файле следующим образом:

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

Поскольку в Dynatrace API **условного именования** нет параметра `name`, следует сопоставить `{{ .name }}` с `displayName`. Например:

```
{



"type": "PROCESS_GROUP",



"nameFormat": "Test naming PG for {Host:DetectedName}",



"displayName": "{{ .name }}",



[...]



}
```

Это также применяется к типу `HOST`:

```
{



"type": "HOST",



"nameFormat": "Test - {Host:DetectedName}",



"displayName": "{{ .name }}",



[...]



}
```

И к типу `SERVICE`:

```
{



"type": "SERVICE",



"nameFormat": "{ProcessGroup:KubernetesNamespace} - {Service:DetectedName}",



"displayName": "{{ .name }}",



...



}
```

### JSON для Settings

Поскольку полезная нагрузка [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") содержит ряд свойств, которые не относятся непосредственно к схеме и могут потребовать задания Dynatrace Monaco CLI, JSON-шаблоны для settings должны включать только фактическое содержимое конфигурации `value`.

Например, хотя ответ API для авто-тегирования (`builtin:tags.auto-tagging`) имеет вид:

```
{



"items": [



{



"objectId": "vu9U3hXafawfawfawABnRlbmFudAAkZmY0ZTQxZDUtYmM2Yi0zMmFlLThhYmMtNDg3NTFiNWRkMWVhvu9U3hXa3q0",



"value": {



"name": "Application Tag",



"rules": [



{



"enabled": true,



"valueNormalization": "Leave text as-is",



"type": "ME",



"attributeRule": {



"entityType": "APPLICATION",



"conditions": [



{



"key": "WEB_APPLICATION_NAME",



"operator": "CONTAINS",



"stringValue": "My App Name",



"caseSensitive": true



}



]



}



}



]



}



}



],



"totalCount": 1,



"pageSize": 100



}
```

Шаблон Configuration as Code должен быть ограничен содержимым `value`:

```
{



"name": "Application Tag",



"rules": [



{



"enabled": true,



"valueNormalization": "Leave text as-is",



"type": "ME",



"attributeRule": {



"entityType": "APPLICATION",



"conditions": [



{



"key": "WEB_APPLICATION_NAME",



"operator": "CONTAINS",



"stringValue": "My App Name",



"caseSensitive": true



}



]



}



}



]



}
```