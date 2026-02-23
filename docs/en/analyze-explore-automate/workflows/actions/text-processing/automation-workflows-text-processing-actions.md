---
title: Actions for Text Processing Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/text-processing/automation-workflows-text-processing-actions
scraped: 2026-02-23T21:26:19.214163
---

# Actions for Text Processing Connector

# Actions for Text Processing Connector

* Latest Dynatrace
* Reference
* 5-min read
* Published Oct 08, 2025

Below is a list of workflow actions available for Text Processing.

## Path syntax details

* Dot notation: Use a `.` dot to navigate through nested objects or arrays.
* Array indexing: Use `.[index]` to access specific elements in an array.
* Escaping special characters: Use square brackets and quotes for property names with spaces or special characters, for example, `.["some property"]`.
* Update entire content: Use `.` to modify the entire content. To be able to update the entire content is useful if the JSON or YAML is a simple string or integer instead of an object, for example, "simple-string".

### Escaping templating syntax

You may encounter double curly braces templating syntax when dealing with JSON or YAML files.

[workflow expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") also use double curly bracket notation.

It is possible to escape `{{` and `}}` with `{{ '{{' }}` and `{{ '}}' }}` respectively, however; actions provided by Text Processing only support valid JSON or YAML syntax.
Should the expression evaluation result yield an action input that is not considered valid in respect to [JSONï»¿](https://www.json.org/json-en.html) or [YAMLï»¿](https://yaml.org/spec/1.2.2/), the workflow execution state is [`Error`](/docs/analyze-explore-automate/workflows/running#workflow-execution-states "Run and monitor workflows created in Dynatrace Workflows.").

In the official Jinja documentation, read more about [escape mechanismsï»¿](https://jinja.palletsprojects.com/en/stable/templates/#escaping).

## Set JSON value

Configures a JSON file.

### Inputs

Field

Description

Required

Example syntax

**JSON content**

The full content of the JSON.

Required

```
{ "obj1": { "innerObj1": { "array": [ { "theObjectInsideTheArray": "value1" }, { "theObjectInsideTheArray": "value2" } ] } } }
```

**Path**

The path to the property that is added or changed.

Required

* Nested object: `.obj1.innerObj1`
* Array element: `.obj1.innerObj1.array[2].theObjectInsideTheArray`
* Property with spaces: `.["some property"]`
* Top-level array: `.[0].someObjectInTheToplevelArray`
* Entire content: `.`

**Value**

The new value for the property path.

Required

`{"new-key": "new-value"}`

### Results

```
{



"json": "<updated json content>"



}
```

### Example

This is an example input for the **Set JSON value** action where we change the value of `name` from "Max" to "Michael".

* **JSON content**

  ```
  {



  "persons": [



  {



  "name": "Max"



  },



  {



  "name": "John"



  }



  ]



  }
  ```
* **Path**: `.persons[0].name`
* **Value**: "Michael"

### Example result

This is the result of running the **Set JSON value** action as part of a workflow.
The first name was changed to Michael.

```
{



"persons": [



{



"name": "Michael"



},



{



"name": "John"



}



]



}
```

## Set YAML value

Manipulates a YAML.
Supports multi-document YAML files.

### Inputs

Field

Description

Required

Example syntax

**YAML content**

The full content of the YAML.

Required

```
obj1:



innerObj1:



array:



- theObjectInsideTheArray: value1



- theObjectInsideTheArray: value2
```

**Path**

The path to the property that is added or changed.

Required

* Nested object: `.obj1.innerObj1`
* Array element: `.obj1.innerObj1.array[0].theObjectInsideTheArray`
* Property with spaces: `.["some property"]`
* Top-level array: `.[0].someObjectInTheTopLevelArray`
* Entire content: `.`

**Value**

The new value for the property path.

Required

`'new-value'`

**Document index**

Relevant only for YAML files containing multiple documents. Index starts at `0`.

Optional

```
obj1:



key: value1



---



obj2:



key: value2
```

To modify the second document, set `documentIndex` to `1`.

### Results

```
{



âyamlâ: â<updated yaml content>â



}
```

### Example

This is an example input for the **Set YAML value** action where we change the value of `name` from "Max" to "Michael".

* **YAML content**

  ```
  ---



  persons:



  - name: John



  - name: Sarah



  ---



  persons:



  - name: Max



  - name: Jeff
  ```
* **Path**
  `.persons[0]`
* **Document index**
  1
* **Value**
  `{ name: "Michael" }`

### Example result

This is the result of running the **Set JSON value** action as part of a workflow. The name was changed to Michael.

```
persons:



- name: John



- name: Sarah



---



persons:



- name: Michael



- name: Jeff
```

## Get JSON value

Retrieves a value from a JSON file.

| Field | Description | Required |
| --- | --- | --- |
| **JSON content** | The full content of the JSON. | Required |
| **Path** | The path to the property that is retrieved. | Required |

### Result

* **JSON content**

  ```
  {



  "person": {



  "name": "John Doe"



  "age": 30,



  }



  }
  ```
* **Path**: `.person`

  ```
  {



  "json": {



  "name": "John Doe",



  "age": 30



  }



  }
  ```

## Get YAML value

Retrieves a value from a YAML file.
Supports multi-document YAML files.

| Field | Description | Required |
| --- | --- | --- |
| **YAML content** | The full content of the YAML. | Required |
| **Document index** | Relevant only for YAML files containing multiple documents. Index starts at `0`. | Optional |
| **Path** | The path to the property that is retrieved. | Required |

### Result

* **YAML content**

  ```
  person:



  name: "John doe"



  age: 30
  ```
* **Path**: `.person`

  ```
  {



  "yaml": "name: \"John Doe\"\nage: 30"



  }
  ```