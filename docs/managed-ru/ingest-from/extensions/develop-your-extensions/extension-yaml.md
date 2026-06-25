---
title: Файл YAML расширения
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/extension-yaml
scraped: 2026-05-12T11:37:32.270165
---

# Файл YAML расширения

# Файл YAML расширения

* Практическое руководство
* Чтение: 5 мин
* Обновлено 19 сентября 2022 г.

Файл `extension.yaml` определяет общий охват расширения и является основным элементом пакета расширения. В нём хранится конфигурация окружения, и он загружается в окружение как часть пакета расширения ZIP.

В этой статье описаны основные элементы файла `extension.yaml`, применимые к любому типу расширений платформы Dynatrace Extensions. Для элементов, характерных для конкретных типов источников данных, см.:

* [Расширение SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Узнайте, как создать расширение SNMP с помощью платформы Extensions.")
* [Расширение WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Узнайте, как создать расширение WMI с помощью платформы Extensions.")
* [Расширение Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью платформы Extensions.")
* [Расширение JMX](/managed/ingest-from/extensions/develop-your-extensions/data-sources/jmx "Узнайте, как создать расширение JMX с помощью платформы Extensions.")
* [Расширение SQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions.")

## Схемы

При создании файла `extension.yaml` используйте схемы, предоставляемые через [Extensions API](/managed/dynatrace-api/environment-api/extensions-20 "Узнайте, как управлять расширениями с помощью Dynatrace Extensions 2.0 API."). Рекомендуется использовать редактор с поддержкой проверки схем и сниппетов: это значительно упрощает редактирование `extension.yaml`.

Рекомендуется использовать дополнение Dynatrace Extensions для VS Code. Дополнительные сведения см. в разделе [Дополнение для VS Code](https://dt-url.net/tx03uks/).

Чтобы загрузить схемы Extensions:

1. Проверьте доступные версии схем с помощью эндпоинта [GET all schemas](/managed/dynatrace-api/environment-api/extensions-20/schemas/get-all-schemas "Просмотрите доступные версии схем расширений через Dynatrace Extensions 2.0 API."). Версии схем соответствуют версиям Dynatrace Cluster.

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
2. Используйте эндпоинт [GET all files](/managed/dynatrace-api/environment-api/extensions-20/schemas/get-all-files "Просмотрите доступные файлы схем для конкретной версии Dynatrace через Dynatrace Extensions 2.0 API."), чтобы получить список всех доступных схем для конкретной версии Dynatrace.
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
3. Используйте эндпоинт [GET a file](/managed/dynatrace-api/environment-api/extensions-20/schemas/get-file "Просмотрите файл схемы расширения через Dynatrace Extensions 2.0 API."), чтобы загрузить конкретный файл нужной версии. Например, чтобы загрузить `extension.schema.json`, версия `1.215`:

   ```
   curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/schemas/1.215/extension.schema.json" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token {api-token}"
   ```

Также можно использовать репозиторий Dynatrace на GitHub для [схем Extensions](https://github.com/dynatrace-extensions/extensions-schemas).

## Начало файла YAML расширения

Файл YAML расширения начинается с основной информации о расширении. Он также содержит необязательные ссылки на [ресурсы](/managed/ingest-from/extensions/concepts#extension-assets "Подробнее о концепции Dynatrace Extensions."), используемые расширением.

* `name`: имя расширения. Имя пользовательского расширения (не разработанного Dynatrace) должно начинаться с `custom:`. Строка должна соответствовать [требованиям протокола приёма данных](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#dimension-optional "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.") для измерений.
* `version`: версия расширения в формате `major`.`minor`.`build`, например `1.0.0`. В окружении Dynatrace можно хранить 10 версий расширения, но одновременно активна только одна.
* `minDynatraceVersion`: наиболее ранняя версия Dynatrace, поддерживаемая расширением, в кавычках (`"`), например `"1.213"`.
* `author`: разработчик или компания, создавшая расширение.
* `dashboards`: путь к определениям дашборда в архиве `extension.zip` относительно файла YAML расширения. Допускается до 10 определений.
* `alerts`: путь к определениям пользовательских событий метрик в архиве `extension.zip` относительно файла YAML расширения. Допускается до 10 определений.

## Группы и подгруппы

Метрики можно организовывать в группы и подгруппы, чтобы назначать метрики внутри группы определённым [измерениям](#dimensions) или [наборам функций](/managed/ingest-from/extensions/concepts#feature-sets "Подробнее о концепции Dynatrace Extensions."), а также управлять [интервалом](#interval) сбора данных на уровне группы.

Для каждого расширения можно определить 10 групп, каждая из которых может содержать 10 подгрупп.

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

Интервал, с которым выполняется измерение данных. Интервалы можно задавать на уровне группы, подгруппы или отдельной метрики. Минимальная гранулярность интервала составляет одну минуту. Максимальный интервал составляет 2880 минут (2 дня, 48 часов).

Для источников данных JMX задать интервал невозможно.

Например:

```
interval:



minutes: 5
```

Указанный формат поддерживается начиная с версии схемы 1.217. Для более ранних версий схемы используйте следующий формат (поддерживается до версии схемы 1.251 включительно):

```
interval: 5m
```

## Метрики

Метрики можно определять на уровне расширения, группы и подгруппы. Способ извлечения значений метрик зависит от типа источника данных.
См.:

* [SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Узнайте, как создать расширение SNMP с помощью платформы Extensions.")
* [WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Узнайте, как создать расширение WMI с помощью платформы Extensions.")

### Рекомендации по ключам метрик

Метрики, поступающие в Dynatrace через расширение, являются лишь частью тысяч встроенных и пользовательских метрик, обрабатываемых Dynatrace. Чтобы ключи метрик были уникальными и легко идентифицировались в Dynatrace, рекомендуется добавлять к имени метрики префикс с именем расширения. Это гарантирует уникальность ключа метрики и позволяет легко связать метрику с конкретным расширением в окружении.

## Измерения

Измерение можно определить на уровне метрики, группы и подгруппы. Способ извлечения значений измерения зависит от типа источника данных.
См.:

* [SNMP](/managed/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#dimensions "Узнайте, как создать расширение SNMP с помощью платформы Extensions.")
* [WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions#dimensions "Узнайте, как создать расширение WMI с помощью платформы Extensions.")
* [Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions#dimensions "Узнайте, как создать расширение Prometheus с помощью платформы Extensions.")

## Переменные

Чтобы расширение было настраиваемым через конфигурацию мониторинга, применяйте переменные, которые заменяются значениями из конфигурации мониторинга. Переменные можно использовать напрямую как значение измерения или совместно с [фильтрами](#filters). Перед использованием переменные необходимо объявить в файле YAML расширения:

```
vars:



- id: ifNameFilter



displayName: Pattern matching interfaces for which metrics should be queried



type: text



- id: ext.activationtag



displayName: Extension activation tag



type: text
```

В определении переменных доступны три типа:

* `text`: позволяет задать значение в виде простого текста.

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

  + `displayName`: имя, отображаемое в Dynatrace Hub.
  + `maxLength`: максимальная длина значения переменной (до 10 000).
  + `required`: обязательность указания значения для данной переменной.
  + `defaultValue`: значение по умолчанию, если значение не задано в REST API.
  + `pattern`: шаблон регулярного выражения, которому должно соответствовать введённое значение.
* `multiline-text`: позволяет задать простой текст с символами новой строки. Подробнее о многострочном синтаксисе YAML см. [YAML Multiline](https://dt-url.net/1m034c2).

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

  + `maxLength`: максимальная длина значения переменной (до 10 000).
  + `required`: обязательность указания значения для данной переменной.
  + `defaultValue`: значение по умолчанию, если значение не задано в REST API.
* `enum`: позволяет задать собственный набор допустимых значений.

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

  + Необязательный `defaultValue`: если задан, устанавливает значение по умолчанию для всего набора и делает переменную обязательной.

  Определите допустимые значения в списке `availableValues`:

  + `value`: значение, передаваемое в расширение.
  + `displayName`: имя, отображаемое в Dynatrace Hub.

## Фильтры

После того как фильтр определён как [переменная](#variables), можно добавить логику фильтрации, чтобы передавались только те измерения, которые соответствуют критериям фильтрации.

```
filter: var:ifNameFilter
```

Определите фильтр на основе условия следующим образом:

* **Starts with**: используйте квалификатор `const:$prefix`. Пример:

  ```
  filter: const:$prefix(xyz)
  ```
* **Ends with**: используйте квалификатор `const:$suffix`. Пример:

  ```
  filter: const:$suffix(xyz)
  ```
* **Contains**: используйте квалификатор `const:$contains`. Пример:

  ```
  filter: const:$contains(xyz)
  ```
* **Equals**: используйте квалификатор `const:$eq`. Пример:

  ```
  filter: const:$eq(xyz)
  ```

  Для перечисленных выше выражений также доступны следующие квалификаторы:

  + `const:$and`: для объединения двух или более выражений оператором AND. Пример:

    ```
    filter: const:$and(<expr1>,<expr2>)
    ```
  + `const:$or`: для объединения двух или более выражений оператором OR. Пример:

    ```
    filter: const:$or(<expr1>,<expr2>)
    ```
  + `const:$not`: для отрицания выражения. Пример:

    ```
    filter: const:$not(<expr>)
    ```

Логика фильтрации для расширений WMI отличается: условие передаётся в виде запроса. Дополнительные сведения см. в разделе [Фильтрация извлечённых измерений](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference#filter-extracted-dimensions "Узнайте о расширениях WMI в платформе Extensions.").