---
title: Extension YAML file
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/extension-yaml
scraped: 2026-03-06T21:35:32.192927
---

# YAML-файл расширения

# YAML-файл расширения

* Последняя версия Dynatrace
* Руководство
* Чтение: 5 мин
* Обновлено 19.09.2022

Файл `extension.yaml` определяет общую область применения вашего расширения и является основным элементом пакета расширения. Он хранит конфигурацию вашей среды и загружается в вашу среду как часть ZIP-пакета расширения.

В этом разделе описаны основные элементы файла `extension.yaml`, применимые к любому типу расширения из фреймворка Dynatrace Extensions. Для элементов, специфичных для конкретных типов источников данных, см.:

* [Расширение SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Узнайте, как создать расширение SNMP с помощью фреймворка Extensions.")
* [Расширение WMI](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью фреймворка Extensions.")
* [Расширение Prometheus](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью фреймворка Extensions.")
* [Расширение JMX](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx "Узнайте, как создать расширение JMX с помощью фреймворка Extensions.")
* [Расширение SQL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью фреймворка Extensions.")

## Схемы

При создании файла `extension.yaml` обязательно используйте схемы, предоставляемые через [Extensions API](/docs/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). Мы рекомендуем использовать редактор, поддерживающий валидацию схем и сниппеты, что значительно упрощает редактирование `extension.yaml`.

Мы рекомендуем использовать дополнение Dynatrace Extensions для VS Code, предоставляемое Dynatrace. Подробнее см. [Дополнение для VS Code](https://dt-url.net/tx03uks/).

Для загрузки схем Extensions:

1. Проверьте доступные версии схем с помощью эндпоинта [GET all schemas](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-all-schemas "Просмотр доступных версий схем расширений через Dynatrace Extensions 2.0 API."). Версии схем соответствуют версиям кластера Dynatrace.

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

   Ответ:

   ```
   {



   "versions": [



   "1.213.0",



   "1.215.0",



   ]



   }
   ```
2. Используйте эндпоинт [GET all files](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-all-files "Просмотр доступных файлов схем в версии схемы через Dynatrace Extensions 2.0 API.") для получения списка всех доступных схем для конкретной версии Dynatrace.
   Например:

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas/{dynatrace-version}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

   Ответ:

   ```
   {



   "files": [



   "metric.metadata.schema.json",



   "topology.schema.json",



   "generic.types.schema.json",



   "generic.relationships.schema.json",



   "snmp.schema.json",



   "metric.schema.json",



   "wmi.schema.json",



   "extension.schema.json"



   ]



   }
   ```
3. Используйте эндпоинт [GET a file](/docs/dynatrace-api/environment-api/extensions-20/schemas/get-file "Просмотр файла схемы расширения через Dynatrace Extensions 2.0 API.") для загрузки конкретного файла определённой версии. Например, чтобы загрузить `extension.schema.json` версии `1.215`:

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas/1.215/extension.schema.json" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

Также вы можете использовать репозиторий Dynatrace на GitHub для [схем расширений](https://github.com/dynatrace-extensions/extensions-schemas).

## Начало YAML-файла расширения

YAML-файл расширения начинается с базовой информации о расширении. Он также содержит необязательные ссылки на [ресурсы](/docs/ingest-from/extensions/concepts#extension-assets "Узнайте больше о концепции расширений Dynatrace."), используемые расширением.

* `name` — имя вашего расширения. Имя пользовательского расширения (не разработанного Dynatrace) должно начинаться с `custom:`. Строка должна соответствовать [требованиям протокола приёма](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.") для измерений.
* `version` — версия вашего расширения в формате `major`.`minor`.`build`, например `1.0.0`. Ваша среда Dynatrace может хранить 10 версий расширения, но только одна может быть активна в данный момент.
* `minDynatraceVersion` — самая ранняя версия Dynatrace, поддерживаемая расширением, заключённая в кавычки (`"`), например `"1.213"`.
* `author` — разработчик расширения или компания.
* `dashboards` — путь к определениям дашбордов в архиве `extension.zip` относительно YAML-файла расширения. Можно добавить до 10 определений.
* `alerts` — путь к определениям пользовательских событий метрик в архиве `extension.zip` относительно YAML-файла расширения. Можно добавить до 10 определений.

## Группы и подгруппы

Вы можете организовать метрики в группы и подгруппы, чтобы назначить метрики в группе определённым [измерениям](#dimensions) или [наборам функций](/docs/ingest-from/extensions/concepts#feature-sets "Узнайте больше о концепции расширений Dynatrace."), или управлять [интервалом](#interval), с которым они отправляются на уровне группы.

Для каждого расширения можно определить 10 групп, и каждая группа может содержать 10 подгрупп.

Например:

```
name: com.dynatrace.cisco-catalyst-health



version: 1.0.0



minDynatraceVersion: "1.238"



author:



name: Joe Doe



snmp:



- group: Device health



interval:



minutes: 1



dimensions:



- key: device.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.contact



value: oid:1.3.6.1.2.1.1.4.0



subgroups:



- subgroup: Device health (Temperature)



table: true



dimensions:



- key: envmon.temperature.desc



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.2



metrics:



- key: envmon.temperature.value



value: oid:1.3.6.1.4.1.9.9.13.1.3.1.3



type: gauge
```

## Интервал

Интервал, с которым выполняется измерение данных. Вы можете определять интервалы на уровне группы, подгруппы или отдельной метрики. Интервалы можно определять с точностью до одной минуты. Максимальный интервал составляет 2880 минут (2 дня, 48 часов).

Настройка интервала невозможна для источников данных JMX.

Например:

```
interval:



minutes: 5
```

Указанный формат поддерживается начиная с версии схемы 1.217. Для более ранних версий схем используйте следующий формат (поддерживается до версии схемы 1.251):

```
interval: 5m
```

## Метрики

Вы можете определять метрики на уровне расширения, группы и подгруппы. Детали извлечения значений метрик зависят от типа источника данных.
См.:

* [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Узнайте, как создать расширение SNMP с помощью фреймворка Extensions.")
* [WMI](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Узнайте, как создать расширение WMI с помощью фреймворка Extensions.")

### Лучшие практики для ключей метрик

Метрики, которые вы принимаете в Dynatrace с помощью расширения, — это лишь часть из тысяч метрик, встроенных и пользовательских, обрабатываемых Dynatrace. Чтобы сделать ключи ваших метрик уникальными и легко идентифицируемыми в Dynatrace, рекомендуется использовать имя расширения в качестве префикса к имени метрики. Это гарантирует уникальность ключа метрики и позволяет легко сопоставить метрику с конкретным расширением в вашей среде.

## Измерения

Вы можете определить измерение на уровне метрики, группы и подгруппы. Детали извлечения значений измерений зависят от типа источника данных.
См.:

* [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Узнайте, как создать расширение SNMP с помощью фреймворка Extensions.")
* [WMI](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Узнайте, как создать расширение WMI с помощью фреймворка Extensions.")
* [Prometheus](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions#dimensions "Узнайте, как создать расширение Prometheus с помощью фреймворка Extensions.")

## Переменные

Если вы хотите сделать ваше расширение настраиваемым через конфигурацию мониторинга, вы можете использовать переменные, которые будут заменены значениями, переданными из конфигурации мониторинга. Переменные можно использовать непосредственно в качестве значения измерения или с [фильтрами](#filters). Для использования переменных необходимо сначала объявить их в YAML-файле расширения:

```
vars:



- id: ifNameFilter



displayName: Pattern matching interfaces for which metrics should be queried



type: text



- id: ext.activationtag



displayName: Extension activation tag



type: text
```

Существует три типа переменных, которые можно использовать в определении переменных:

* `text` — позволяет указать простое текстовое значение.

  ```
  - id: textVariable



  type: text



  displayName: Variable



  description: "Detailed information about this variable"



  maxLength: 2000



  required: true



  defaultValue: "#ff1"



  pattern: ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$
  ```

  + `displayName` — имя, отображаемое в Dynatrace Hub.
  + `maxLength` — максимальная длина значения переменной (до 10 000).
  + `required` — обязательно ли предоставление значения для этой переменной.
  + `defaultValue` — значение по умолчанию, если значение не указано в REST API.
  + `pattern` — шаблон регулярного выражения, которому должно соответствовать предоставленное значение.
* `multiline-text` — позволяет указать простой текст с символами перевода строки. Подробнее о многострочном синтаксисе YAML см. [YAML Multiline](https://dt-url.net/1m034c2).

  ```
  - id: multilineVariable



  type: multiline-text



  displayName: Variable



  description: Detailed information about this variable



  maxLength: 2000



  required: true



  defaultValue: |



  Pipe



  style



  multiline
  ```

  + `maxLength` — максимальная длина значения переменной (до 10 000).
  + `required` — обязательно ли предоставление значения для этой переменной.
  + `defaultValue` — значение по умолчанию, если значение не указано в REST API.
* `enum` — позволяет определить собственный набор возможных значений.

  ```
  - id: Colors



  type: enum



  defaultValue: green



  description: Choose your favorite color!



  availableValues:



  - value: red



  displayName: Red as a rose



  - value: green



  displayName: Green as grass



  - value: white



  displayName: White as snow
  ```

  + Необязательный `defaultValue` — если определён, устанавливает значение по умолчанию для всего набора и делает переменную обязательной.

  Определите возможные значения в списке `availableValues`:

  + `value` — значение, передаваемое расширению.
  + `displayName` — имя, отображаемое в Dynatrace Hub.

## Фильтры

После определения фильтра как [переменной](#variables) вы можете добавить логику фильтрации, которая приведёт к отправке только тех измерений, которые соответствуют критериям фильтрации.

```
filter: var:ifNameFilter
```

Определите фильтр на основе условия следующим образом:

* **Начинается с** — используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Заканчивается на** — используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Содержит** — используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Равно** — используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для вышеупомянутых выражений также можно использовать квалификаторы:

  + `const:$and` — для объединения двух или более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or` — для объединения двух или более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not` — для отрицания выражения. Пример:

    ```
    filter: const:$not(<expr>)
    ```

Логика фильтрации отличается для расширений WMI, где вы передаёте условие в виде запроса. Подробнее см. [Фильтрация извлечённых измерений](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference#filter-extracted-dimensions "Узнайте о расширениях WMI в фреймворке Extensions.").