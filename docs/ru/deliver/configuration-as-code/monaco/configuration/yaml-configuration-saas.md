---
title: Monaco configuration YAML file structure
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas
scraped: 2026-02-16T09:28:02.368937
---

# Monaco configuration YAML file structure

# Monaco configuration YAML file structure

* Latest Dynatrace
* Reference
* 14-min read
* Updated on Dec 15, 2025

The `configs` YAML file contains a list of configurations to be deployed.

Here is a basic example of an SLO `configs` YAML file:

```
configs:



- id: newSLO



type: slo-v2



config:



parameters:



target: 95



title: myNewSLO



entityScope: HOST-#######



template: slo-cpu-usage.json



skip: false
```

Here is a basic example of an SLO `slo-cpu-usage.json` YAML file:

```
{



"name": "{{ .title }}",



"description": "test SLO for template test",



"tags": [],



"customSli": {



"filterSegments": [],



"indicator": "timeseries sli=avg(dt.host.cpu.usage)\n, by: { \"{{ .entityScope }}\" }



\n  , filter: in(dt.entity.host, { $hosts })\n  | fieldsAdd entityName(dt.entity.host)"



},



"criteria": [



{



"target": {{ .target }},



"timeframeFrom": "now-7d",



"timeframeTo": "now",



"warning": 99



}



]



}
```

The top-level element of the configuration file is `configs`. Its value is a list of configurations.

Required Each configuration requires the following fields: `id`, `type`, and `config`.

You can override values from the `config` on the environment and environment-group levels.
The optional `groupOverrides` and `environmentOverrides` fields allow for this.

## `id` field

The `id` field identifies a `config` within the configurations.
It must be unique for the same [configType](/docs/deliver/configuration-as-code/monaco/reference/commands-saas "How to use the Monaco CLI application, including arguments and options.") and [project](/docs/deliver/configuration-as-code/monaco/configuration/monaco-manage-resources#projects "This a list of Monaco resources.").
This field is needed to reference the [parameters](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling#supported-api-types "This is a list of the Monaco API support and access permission handling.") and describe dependencies between single configs.

It is possible to have, for example, two dashboards with the same `id` but in two different projects.

The `id` field is only local to the Dynatrace Monaco CLI and does not correspond to the ID provided by the Dynatrace API.

## `type` field

The `type` field defines the type of Dynatrace configuration.

For a detailed list, see [Monaco configuration YAML file - list of type fields](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields "This is a list of type fields in the Monaco configuration YAML file.").

The types and subcategories

* `API`: selected Dynatrace APIs.
  For more information, see [Monaco API support and access permission handling](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling#supported-api-types "This is a list of the Monaco API support and access permission handling.").

  + `scope`
* `Settings API`

  + `Scope`
  + `Schema`
  + Optional `Schema version`
  + Optional `insertAfter`

    Not all **Settings** schemas support permission. Only applicable for objects based on schemas with ordered objects. Schema's ordered parameter is set to `true`.
    For more information, see [SettingsObjectUpdate object](/docs/dynatrace-api/environment-api/settings/objects/put-object#openapi-parameter-body-objects-openapienv2 "Edit a settings object via the Dynatrace API.").
  + Optional `permission`

    Not all **Settings** schemas support permission. Only applicable for objects based on schemas with ordered objects. Schema's ordered parameter is set to `true`.
    For more information, see [SettingsObjectUpdate object](/docs/dynatrace-api/environment-api/settings/objects/put-object#openapi-parameter-body-objects-openapienv2 "Edit a settings object via the Dynatrace API.").
* `Automation` defines a workflow.

  + `resource`
* `Bucket` defines Grail storage buckets for data storage.
* `Document` defines a dashboard, a notebook and a launchpad.

  + `kind`
  + Optional `private`
  + Optional `id`
* `OpenPipeline` customizes the Dynatrace data ingest flows.

  + `kind`

Dynatrace version 1.323+ OpenPipeline Configurations API is replaced by dedicated Settings API schemas. To avoid the following limitations, migrate to the new format, see [Migrate OpenPipeline configurations to Settings API](/docs/platform/openpipeline/migration-settings "Understand how to migrate your OpenPipeline configurations to new Settings API."). If you already use the new Settings API schemas, refer to [Type - Settings](#type-setting) instead.

* `Segment` defines the data segments and filter masks.
* `Service-level objectives (SLOs)` sets up a Dynatrace slo.

### Additional and optional fields

Depending on the configuration `type`, you might need to define additional fields or add optional fields.

Not all fields are available for all types.

Configuration `type` fields

* `scope`: applicable for the types `api` and `settings`.
  It allows for specifying dependencies and relationships.
* `schema` and `schemaVersion`: applicable for the `settings` type.
  It defines the specific settings schema, such as [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").
* `permission`: applicable for the type `settings`.
  It allows fine-grained access control to settings objects, based on IAM permissions.
* `insertAfter`: applicable for the type `settings`.
  It allows a custom ordering of the Settings objects.
* `resource`: applicable for the type `automation`.
  It defines the subcategory of the automation service.
* `kind`: applicable for the types `document` and `openpipeline`.
  It specifies the kind or category of the configuration type.
* `private`: applicable for the type `document`.
  It specifies the accessibility/visibility of the document in the environment, for example, public versus private.
* `id`: applicable for the type `document`.
  It specifies a user-defined ID for the document.
  If it's specified, it also needs to be directly referenced in the [deletefile](/docs/deliver/configuration-as-code/monaco/configuration#file-structure-for-direct-reference "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."), if you wish to delete the document later.
  For document creation, if this field is not set, Monaco generates a custom ID.
  On download, the `id` field is populated, if a custom ID was used to create the document.

## `config` field

The `config` field specifies the single configuration instance of the selected type and references the JSON template containing the JSON payload uploaded to the Dynatrace API endpoints.

The following fields

* Required `name`: identifies the configuration objects in the Dynatrace API.
* Required `template`: references the templating file to render the request to the Dynatrace API.
* Optional `skip`: specifies if the config shall be deployed or not.
* Optional `parameters`: specifies parameters propagated to the template.
* Optional `originObjectId`: automatically set when downloading the config objects.
  Dynatrace Monaco uses it as an additional identifier to update the existing resource when redeployed.

### String escape in config

All YAML values are generally escaped before being added to a configuration and uploaded to Dynatrace.
Using string escape ensures that filled-out templates are valid JSON when uploading.
Any new lines, special characters such as double quotes, are escaped.

```
parameters:



name: "Dev"



example1: "This is \\n already escaped."



example2: "This will \n be escaped."



example3: This "will" be escaped too.



text: |



This will also



be escaped.
```

### `name` property

Dynatrace Monaco CLI version 2.6.0 or earlierâThe `name` property is mandatory. You need to define it for all configuration types.

Dynatrace Monaco CLI version 2.7.0+âThe `name` property is required only for API-type configurations and is optional for other configuration types.

#### Configurations of type `api`

If the specified configuration is an [api type](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#type-field "This is a list of type fields in the Monaco configuration YAML file."), the `name` is used to identify configurations in a Dynatrace environment and ensure that they're updated when they already exist.

For this, the `name` needs to be used in the JSON template to fill the configuration's specific `name` property.
Usually, this is also just a `name`, but for some configurations, this may differ.
For more information, see the exceptional cases described for JSON templates [Work with Dynatrace Monaco CLI commands for Latest Dynatrace](/docs/deliver/configuration-as-code/monaco/reference/commands-saas "How to use the Monaco CLI application, including arguments and options.") and refer to the API documentation if in doubt.

When [downloading](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#download "How to use the Monaco CLI application, including arguments and options."), the names are automatically extracted and placed in the YAML for you.

When referencing the name in a JSON template, it needs to be used as it is, with no additional text or characters around it.

Use the `name` property in JSON like this `"{{ .name }}"`.

If you encounter issues with the configurations not being created several times instead of updated, check to make sure that your reference to the name does not contain any spaces or other characters that make what is sent to Dynatrace in the JSON different from the name defined in the YAML.

### Other configuration types



The `name` property isn't used to identify Dynatrace objects.
Instead, the configuration's coordinate, a combination of project, type, and configuration ID, or originObjectId, if present, is used.

The `name` property can still be used and, for some types, is automatically extracted when [downloading](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#download "How to use the Monaco CLI application, including arguments and options.").

### `skip` field

The `skip` field allows you to omit or skip the deployment of a specific configuration.
If `skip` is set to true, the Dynatrace Monaco CLI won't deploy the configuration.

The `skip` field behaves like [parameters](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#parameters "This is a list of type fields in the Monaco configuration YAML file.") and you can define it as a value or an environment parameter.
Typically, it's defined directly as a shorthand value.

It's most useful with environment overrides, where you want to deploy a configuration to one environment but exclude it from another.

### `parameters` field

The `parameters` field is used to provide selected values in a configuration template.
It's defined as YAML object with a type entry.
This type then further decides how the parameter object is interpreted.
The value of a parameter is only evaluated if it's referenced by a configuration that is going to be deployed.

The following parameter types are available:

* value
* environment
* reference and partial reference
* compound
* list
* file

#### `value` parameter

The `value` parameter is the simplest form of a parameter.
Besides the `type` property, it also requires the value property.
You can define anything as the value, even nested maps.
This value is then accessible in the template file.
Because the `value` parameters are the most common parameter type, there is a special short-form syntax to define them. You can provide the value if your parameter is neither an array nor a map.

An example of setting the `value` parameter:

```
parameters:



threshold: 15



complexThreshold:



type: value



value:



amount: 15



unit: sec
```

In the JSON template of this configuration, the `threshold` parameter can be accessed via `{{ .threshold }}`.
To access, for example, the `amount` of the `complexThreshold`, you could use `{{ .complexThreshold.amount }}`.

#### `environment` parameter

The `environment` type parameter allows you to reference an environment variable.
The environment variable's name to reference is defined via a `name` property.

You can provide a default value via the default property if the environment variable is absent.

The parameter can't be resolved if the `default` property is not set and the environment variable is missing.
The deployment fails when the `default` property is not set and the environment variable is missing.

The deployment will fail only if the parameter is relevant for deployment.
Parameters not referenced by the config for deployment are not evaluated.

The following example defines an `owner` and `target` parameter:

* The `owner` parameter evaluates the value of the `OWNER` environment variable.
  If the environment variable is not set, it evaluates to the value `"-"`.
* The target parameter evaluates to the value of the `TARGET` environment variable.
  It fails the deployment if the variable is not set at deployment time.

  An example of setting an `owner` and `target` parameter:

  ```
  parameters:



  owner:



  type: environment



  name: OWNER



  default: "-"



  target:



  type: environment



  name: TARGET
  ```

#### `reference` parameter

Dynatrace configurations often reference other configurations to support more complex use cases.
Monaco provides a specific `reference` parameter to support such configuration references.

To use the parameter reference type, provide the following required fields:

* `project`: the project name of the configuration the parameter is referencing.
* `configType`: the type of configuration that the parameter is referencing.
  For configurations of `settings` type, the value of `configType` should correspond to the schema ID, for example, `builtin:davis.anomaly-detectors`.
* `configId`: the ID of the configuration that the parameter is referencing.
* `property`: the field name to determine the parameter's value.
  If the property is set to `id` or `name`, the parameter resolves to the corresponding Dynatrace object's actual ID or name.

  In the following example, the `id` of a Site Reliability guardian is referenced within a workflow definition. The `guardianid` uses the Dynatrace object ID of the guardian configuration from the `other-project` project.

  ```
  configs:



  - id: myservice-srg-validation-workflow



  config:



  name: CasC-sample myService Performance Quality Gate Validation



  parameters:



  event_filter_service:



  value: myService



  type: value



  event_filter_stage:



  value: prod



  type: value



  event_filter_gate:



  value: performance gate



  type: value



  guardianid:



  configId: myservice-guardian



  configType: app:dynatrace.site.reliability.guardian:guardians



  property: id



  type: reference



  project: other-project



  template: myservice-srg-validation-workflow.json



  skip: false



  type:



  automation:



  resource: workflow
  ```

The Dynatrace Monaco CLI ensures the configuration is deployed in order, with the dependent configuration is being deployed first.

If you configure a cycle of dependencies, the deployment fails with an error.

##### Shorthand form syntax notion

The reference parameters are one of the most common parameter types; there is a special shorthand form syntax to define them as an array:

* Syntax: `[ <project>, <configType>, <configId>, <property> ]`
* Example: guardianId: `["other-project", "app:dynatrace.site.reliability.guardian:guardians", "myservice-guardian", "id"]`

No type is needed, as the type is inferred based on the syntax.

##### Partial reference

It's possible to omit some `reference` fields.
In this case, they're filled with the same value as the current config.
This can be used to simplify referencing configurations within the same project.

```
parameters:



mz_id:



type: reference



configType: management-zone



configId: main



property: id
```

While it's possible to omit `configType` and even `configId`, you can only leave the uppermost level empty, and you can't leave a gap.
So if `configType` is omitted, it must be the `project`.

While it's possible to omit `configType` and even `configId`, you can only leave the uppermost level empty, and you can't just leave a gap.
If `configType` is omitted, you need to leave out `project` too.

Below is a complete sample using shorthand references:

* infrastructure/management-zone/config.yaml

  ```
  configs:



  - id: main



  type:



  api: management-zone



  config:



  name: "Main zone"



  template: "zone.json"
  ```
* development/management-zone/config.yaml

  ```
  configs:



  - id: development



  type:



  api: management-zone



  config:



  name: "Development zone"



  template: "zone.json"
  ```
* ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** development/dashboard/config.yaml

  ```
  configs:



  - id: a_dashboard



  type:



  api: dashboard



  config:



  name: "Overview dashboard"



  template: "dashboard.json"



  - id: overview



  type:



  api: dashboard



  config:



  name: "Overview dashboard"



  template: "dashboard.json"



  parameters:



  zoneId: ["infrastructure", "management-zone", "main", "id"]



  devZoneId: ["management-zone", "development", "id"] # inferred project 'development'



  otherDashboard: ["a_dashboard", "id"] # inferred project 'development' and type 'dashboard'
  ```

#### `compound` parameter

The `compound` parameter comprises other parameters of the same configuration.

This parameter requires a couple of properties:

* A `format` string.
* A list of `references` to all referenced parameters.

The `format` string can be any string.
To use parameters in it, use the syntax `{{ .parameter }}`, where the parameter's name of the compound parameter you fill in.

An example of using a `compound` parameter:

```
parameters:



example:



type: compound



format: "{{ .resource.name }}: {{ .resource.percent }}%"



references:



- resource



progress:



type: value



value:



name: "Health"



percent: 40
```

This example produces the following outcome: `Health: 40%`.

Even though referenced parameters can only be from the same configuration, using the reference parameter can create a compound parameter with other configs.
This is also true for environment variables.

An example of using a compound parameter:

```
parameters:



example:



type: compound



format: "{{ .user }}'s dashboard is {{ .status }}"



references:



- user



- status



user:



type: environment



name: USER_NAME



status:



type: reference



configType: dashboarddocument



configId: my-dashboard



property: status
```

#### `list` parameter

The type `list` parameter allows you to define lists of [value parameters](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#value "This is a list of type fields in the Monaco configuration YAML file.").
When these are in a template, they're written as a JSON list surrounded by square brackets and separated by commas.
This parameter type generally applies when you require a simple list of things, such as emails or identifiers, that can be filled with any value parameter.

An example of using a `list` parameter:

```
Configs:



- id: myservice-slo-availability



config:



name: CasC-sample myService availability



parameters:



service_id:



name: SERVICE_ID



type: environment



tags: #INPUT: Customize your SLO with tags



type: list



values: ["service:myService", "dt.owner:myTeam"]



template: myservice-slo-availability.json



skip: false



type: slo-v2
```

An example of using a `list` parameter and a JSON template called myservice-slo-availability.json:

```
{



"criteria": [



{



"target": 95,



"timeframeFrom": "now-7d",



"timeframeTo": "now"



}



],



"customSli": {



"filterSegments": [],



"indicator": "timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }\n  , by: { dt.entity.service }\n  , filter: { in (dt.entity.service, { \"{{ .service_id }}\" }) }\n| fieldsAdd sli=(((total[]-failures[])/total[])*(100))\n| fieldsAdd entityName(dt.entity.service)\n| fieldsRemove total, failures"



},



"description": "Measures the proportion of successful service requests over time.",



"name": "{{ .name }}",



"tags": {{ .tags }}



}
```

As shown in the example above, you can define the `list` values in YAML either line by line or as an array.

When using a `list` parameter value in a JSON template, reference the value without any extra brackets.
`"emails": {{ .recipients }}`

#### `file` parameter

Dynatrace Monaco CLI version 2.14.0+

The type `file` parameter allows you to load content from a file on a disk.

An example of using a `file` parameter:

```
parameters:



comment: "// hello special comment"



myWf:



type: file        # parameter type "file"



path: "myWf.js"   # relative path to the file



references:       # other parameters names referenced in the content of the file



- comment
```

In the example, the parameter `myWf` is dynamically resolved to include the `myWf.js` content relative to the current configuration location.

You can reference this parameter within the JSON template as follows:

`{ "script" : {{ .myWf }} }`

You can include references to other parameters within the content of the referenced file.
Each reference parameter must be defined as a separate parameter and listed in the references section of the file parameter type.

In the given example, you can reference the additional parameter called `comment` within the content specified by the file parameter using the notation `{{ .comment }}`.



### `originObjectId`

When using the Dynatrace Monaco CLI to [download](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#download "How to use the Monaco CLI application, including arguments and options.") existing configurations from Dynatrace, the created YAML files contain an `originObjectId` for some configuration types.

The `originObjectId` holds the ID of the downloaded Dynatrace object.
Use `originObjectId` when you're planning on deploying again to the same Dynatrace environment to ensure that the existing object is correctly updated with the downloaded configuration.

For example, you could use it for an existing Settings 2.0 object that you extend with the data used to identify it correctly.

The `originObjectId` is optional and is set by Monacoâno user interaction or adaptations are needed here.

### Override configurations per environment or environment-group

There are many cases in which a configuration is similar but not the same between environments.

For example:

* An alert is sent to a different Slack channel for staging and production environments.
* A service's configuration should be skipped because it's not yet released.

To allow this, you can use the `groupOverrides` and `environmentOverrides` fields to override configuration values on an environment and environment-group level.

Both are generally defined similarly, differing only in whether they're applied to a group or a single environment.
You can define the environment or environment-group name to target and any configuration properties to modify.

In this example, a configuration gets some special configuration applied for two environments, and skip ensures that the configuration won't be deployed to the production-environments group:

```
configs:



- id: test-dashboard



type:



api: dashboard



config:



name: Test Dashboard



template: dashboard.json



parameters:



owner: Test User



content: "Some Text ..."



environmentOverrides:



- environment: dev-env-42



override:



name: Special Dev Dashboard



parameters:



content: "Some even better Text!"



- environment: staging-env-21



override:



name: Special Staging Dashboard



parameters:



content: "Some much better Text!"



groupOverrides:



- group: production-environments



override:



skip: true
```

## Related topics

* [Monaco configuration YAML file - list of type fields](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields "This is a list of type fields in the Monaco configuration YAML file.")