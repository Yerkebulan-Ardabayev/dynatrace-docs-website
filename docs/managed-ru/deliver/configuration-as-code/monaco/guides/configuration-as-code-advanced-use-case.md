---
title: Продвинутые сценарии с шаблонами Go
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/configuration-as-code-advanced-use-case
scraped: 2026-05-12T12:03:04.641946
---

# Advanced use cases with Go templating

# Advanced use cases with Go templating

* Tutorial
* 4-min read
* Published Mar 21, 2023

[Шаблоны Go](https://pkg.go.dev/text/template) — это язык шаблонизации, встроенный в язык программирования Go, позволяющий определять шаблоны с заполнителями и наполнять их динамическим содержимым. Dynatrace Configuration as Code через Monaco в сочетании с шаблонами Go позволяет решать продвинутые задачи управления и развёртывания конфигураций Dynatrace.

Шаблоны Go можно использовать с [файлом шаблона JSON](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") для генерации динамического содержимого на основе переменных и функций Go.

Если вы выбираете использование шаблонов Go совместно с Dynatrace, мы не можем гарантировать поддержку в случае возникновения каких-либо проблем или осложнений.

Несмотря на стремление обеспечить всестороннюю поддержку, использование шаблонов Go выходит за рамки наших официальных правил поддержки. Рекомендуем проявлять осторожность и убедиться в наличии необходимой экспертизы для решения возможных проблем.

## Тестирование шаблонов Go

Рекомендуем тестировать вывод шаблонов Go с помощью инструмента [gotemplate.io](https://gotemplate.io/).

1. Преобразуйте YAML-параметр из YAML в JSON с помощью инструмента [YAML to JSON](https://onlineyamltools.com/convert-yaml-to-json) и добавьте его в секцию DATA на `gotemplate.io`.

   **Пример YAML:**

   ```
   itemList:



   - name: Item 1



   price: 10.99



   description: This is item 1



   - name: Item 2



   price: 19.99



   description: This is item 2
   ```

   **Преобразование в JSON:**

   ```
   {



   "itemList": [



   {



   "name": "Item 1",



   "price": 10.99,



   "description": "This is item 1"



   },



   {



   "name": "Item 2",



   "price": 19.99,



   "description": "This is item 2"



   }



   ]



   }
   ```
2. Напишите шаблон Go для проверки вывода.

   **Шаблон Go:**

   ```
   {{- range $i, $e := .itemList}}



   {{$i}}. {{$e.name}} is priced at {{$e.price}}. {{$e.description}}



   {{- end}}
   ```

   **Вывод:**

   ```
   0. Item 1 is priced at 10.99. This is item 1



   1. Item 2 is priced at 19.99. This is item 2
   ```

Это наглядно демонстрирует возможности шаблонов Go для динамической генерации содержимого. В случае Dynatrace Monaco CLI это содержимое будет JSON.

## Продвинутый сценарий: список пар ключ-значение

Существует несколько примеров схем settings/API, где параметр в JSON-объекте ожидает список пар ключ-значение.

Например, схема `builtin:failure-detection.service.general-parameters` управляет страницей **General failure detection parameters** (**Services** > [service] > **Settings** > **Failure detection** > **General parameters**).

### JSON

Ниже представлен результирующий JSON схемы `builtin:failure-detection.service.general-parameters`. Поле `successForcingExceptions`, как и другие поля в этом JSON, ожидает список пар ключ-значение с необязательной сложностью в виде `classPattern` или `messagePattern`.

```
{



"enabled": true,



"exceptionRules": {



"ignoreAllExceptions": false,



"successForcingExceptions": [



{



"classPattern": "class.pattern.2",



"messagePattern": "optional.message.2"



},



{



"classPattern": "class.pattern.1"



}



],



"ignoredExceptions": [],



"customHandledExceptions": [],



"customErrorRules": [],



"ignoreSpanFailureDetection": false



}



}
```

Шаблоны Go можно применять для динамической генерации JSON со списком пар ключ-значение.

### config.yaml

Проекты Dynatrace Monaco CLI содержат `config.yaml` и файл шаблона JSON. Ниже пример файла `config.yaml` для упомянутой схемы. В этом примере параметр `sucForExcep` ссылается на `successForcingExceptions`. Он содержит каждое исключение и необязательные `classPattern` и/или `messagePattern`.

```
configs:



- id: exampleServiceGeneralFailureDegradation



type:



settings:



schema: builtin:failure-detection.service.general-parameters



scope: SERVICE-ID



config:



name: exampleServiceGeneralFailureDegradation



template: object.json



skip: false



parameters:



enabled: true



successForcingExceptions:



type: value



value:



- exception:



- classPattern: "class.pattern.1"



- messagePattern: "optional.message.1"



- exception:



- classPattern: "class.pattern.2"
```

### JSON с шаблонами Go

```
{



"enabled": {{ .enabled}}



{{- if .enabled -}}



,



"exceptionRules": {



"ignoreAllExceptions": false,



"successForcingExceptions": [



{{- range $i, $e := .successForcingExceptions}}



{{- if $i}},{{- end}}



{



{{- range $j, $elem := $e.exception}}



{{- if $j}},{{- end}}



{{- if (index $elem "classPattern")}}



"classPattern": "{{$elem.classPattern}}"



{{- end}}



{{- if (index $elem "messagePattern")}}



"messagePattern": "{{$elem.messagePattern}}"



{{- end}}



{{- end}}



}



{{- end}}



],



"ignoredExceptions": [],



"customHandledExceptions": [],



"customErrorRules": [],



"ignoreSpanFailureDetection": false



}



{{- end}}



}
```

Рассмотрим применение шаблонов Go к JSON подробнее.

1. Параметр `enabled` обрабатывается как булево значение для проверки необходимости применения дополнительной шаблонизации.

   ```
   {{- if .enabled -}}



   ...



   {{- end}}
   ```
2. Параметр `successForcingExceptions` — это список пар ключ-значение, поскольку поле `successForcingExceptions` принимает `classPattern`, `messagePattern` или оба. Функция `range` Go используется для итерации по исходному списку, а вложенный `range` — для итерации по списку пар ключ-значение.

   ```
   {{- range $i, $e := .successForcingExceptions}}



   ...



   {{- range $j, $elem := $e.exception}}



   ...



   {{- end}}



   ...



   {{- end}}
   ```
3. Синтаксис JSON для списка пар ключ-значение использует запятые для разделения отдельных пар или словарей. Следующая шаблонизация Go генерирует запятые для создания корректного синтаксиса JSON.

   ```
   {{- range $i, $e := .successForcingExceptions}}



   {{- if $i}},{{- end}}



   ...



   {{- end}
   ```
4. Функция `index` Go используется для проверки того, равен ли ключ `classPattern` или `messagePattern`, чтобы определить, какой шаблон Go применять.

   ```
   ...



   {{- if (index $elem "classPattern")}}



   "classPattern": "{{$elem.classPattern}}"



   {{- end}}



   {{- if (index $elem "messagePattern")}}



   "messagePattern": "{{$elem.messagePattern}}"



   {{- end}}



   ...
   ```