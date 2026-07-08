---
title: Manage a Monaco project
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration/projects
---

# Manage a Monaco project

# Manage a Monaco project

* Explanation
* 3-min read
* Updated on Nov 24, 2025

A project is a folder containing specially named sub-folders representing APIs. The API folders contain another layer of folders defining configurations. The configuration folders contain YAML files specifying what gets deployed.

## APIs

To list all supported APIs and folder names, see [Configuration types and access permissions](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco").

## Configurations

A configuration consists of two parts:

* YAML file defining parameters, dependencies, name, and template
* JSON template file

### Configuration YAML file

The configuration YAML file contains basic information about the configuration to deploy. This includes the name of the configuration, the location of the template file, and the parameters usable in the template file. Parameters can be overwritten based on what group or environment is currently deployed.

### JSON template file

The JSON template contains the payload that will be uploaded to the Dynatrace API endpoints. It allows you to reference all defined parameters of the configuration via `{{ .PARAMETER_NAME }}` syntax. For example:

`template.json`:

```
{



"name": "{{ .name }}",



"type": "{{ .type }}",



"value": {{ .numericValue }}



}
```

`config.yaml`:

```
configs:



- id: sample



config:



name: "Sample"



parameters:



type: "simple"



numericValue: 42



[...]
```

As you can see, it's also possible to reference the name of a configuration.

The Dynatrace Monaco CLI uses Go templates, which, in theory, allow you to define more complex templates, but we **highly** recommend that you keep templates as simple as possible. Referencing variables via `{{ .PARAMETER_NAME }}` should be sufficient.

For more on advanced templating use cases, see [Advanced use cases with Go templating](/managed/deliver/configuration-as-code/monaco/guides/configuration-as-code-advanced-use-case "Effectively utilize Go templating in projects with Dynatrace Configuration as Code via Monaco.").

Some configurations use the same templating characters as the Dynatrace Monaco CLI `{{ ... }}`.

It is required to escape the templating characters used in the desired JSONs as follows:

* `{{` becomes `` {{`{{`}} ``
* `}}` becomes `` {{`}}`}} ``

With [`monaco download`](/managed/deliver/configuration-as-code/monaco/reference/commands#download "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)"), these characters will be escaped automatically for all configuration types.

For example,

```
{



"value": "{{someValue}}"



}
```

becomes

```
{



"value": "{{`{{`}}someValue{{`}}`}}"



}
```