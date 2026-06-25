---
title: Advanced use cases with Go templating
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/configuration-as-code-advanced-use-case
scraped: 2026-05-12T12:03:04.641946
---

# Advanced use cases with Go templating

# Advanced use cases with Go templating

* Tutorial
* 4-min read
* Published Mar 21, 2023

[Go templateï»¿](https://pkg.go.dev/text/template) is a templating language built into the Go programming language that allows you to define templates with placeholders and fill them with dynamic content. Dynatrace Configuration as Code via Monaco, when combined with Go templating, can solve advanced use cases for managing and deploying Dynatrace configurations.

Go templates can be used with the [JSON template file](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") to generate dynamic content based on variables and functions defined in Go.

If you choose to utilize Go templating in conjunction with Dynatrace, we cannot guarantee support for any issues or complications that may arise.

While we strive to provide comprehensive support to our users, the use of Go templating falls outside our official support guidelines. We encourage you to proceed with caution and ensure that you have the necessary expertise to address any potential issues that may arise.

## Testing Go templating

We recommend that you test the output of Go templating using the [gotemplate.ioï»¿](https://gotemplate.io/) tool.

1. Transform the YAML parameter from YAML to JSON using the [YAML to JSONï»¿](https://onlineyamltools.com/convert-yaml-to-json) tool and add it to the DATA section in `gotemplate.io`.

   **YAML example:**

   ```
   itemList:



   - name: Item 1



   price: 10.99



   description: This is item 1



   - name: Item 2



   price: 19.99



   description: This is item 2
   ```

   **JSON conversion:**

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
2. Write the Go template to test output.

   **Go template:**

   ```
   {{- range $i, $e := .itemList}}



   {{$i}}. {{$e.name}} is priced at {{$e.price}}. {{$e.description}}



   {{- end}}
   ```

   **Output:**

   ```
   0. Item 1 is priced at 10.99. This is item 1



   1. Item 2 is priced at 19.99. This is item 2
   ```

This displays the power of Go templating to dynamically generate content. In the case of the Dynatrace Monaco CLI, the content will be JSON.

## Advanced use case: list of key-value pairs

There are several examples of setting schema/APIs where a parameter in the JSON object expects a list of key-value pairs.

For example, the schema `builtin:failure-detection.service.general-parameters` manages the **General failure detection parameters** page (**Services** > [service] > **Settings** > **Failure detection** > **General parameters**).

### JSON

The resulting JSON from the `builtin:failure-detection.service.general-parameters` schema is displayed below. The `successForcingExceptions` field, as well as others in this JSON, expect a list of key-value pairs with the optional added complexity of either `classPattern` or `messagePattern`.

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

Go templating can be applied to dynamically generate the list of key-value pairs JSON.

### config.yaml

Dynatrace Monaco CLI projects contain both a `config.yaml` and JSON template file. This is an example of a `config.yaml` file for the schema mentioned. In this example, the parameter `sucForExcep` references `successForcingExceptions`. It contains each exception and an optional `classPattern` and/or `messagePattern`.

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

### JSON with Go templating

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

Let's break down the Go templating being applied on the JSON.

1. The `enabled` parameter is handled as a Boolean to validate whether any additional templating should be applied.

   ```
   {{- if .enabled -}}



   ...



   {{- end}}
   ```
2. The `successForcingExceptions` parameter is a list of key-value pairs. This is because the `successForcingExceptions` field accepts `classPattern` or `messagePattern` or both. The `range` Go function is used to iterate over the initial list, and then another range is used to iterate over the list of key-value pairs.

   ```
   {{- range $i, $e := .successForcingExceptions}}



   ...



   {{- range $j, $elem := $e.exception}}



   ...



   {{- end}}



   ...



   {{- end}}
   ```
3. The JSON syntax for a list of key-value pairs uses commas to separate distinct pairs or dictionaries. The following Go templating generates commas to create valid JSON syntax.

   ```
   {{- range $i, $e := .successForcingExceptions}}



   {{- if $i}},{{- end}}



   ...



   {{- end}
   ```
4. The `index` Go function is used to validate whether the key equals `classPattern` or `messagePattern` to determine which Go templating to apply.

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