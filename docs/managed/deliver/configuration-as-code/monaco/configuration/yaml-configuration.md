---
title: Monaco YAML Configuration
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration
scraped: 2026-05-12T12:35:14.056800
---

# Monaco YAML Configuration

# Monaco YAML Configuration

* Overview
* 20-min read
* Updated on Jul 25, 2025

Each configuration YAML file contains a list of configurations to be deployed.

A basic configuration YAML file looks like this:

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
```

As you can see, the top-level element is `configs`. Its value is a list of configurations. Each configuration requires the following fields: `id`, `type`, and `config`.

It's also possible to override values from `config` on the environment and environment-group level. For this, there exist the optional `groupOverrides` and `environmentOverrides` fields.

## ID

The `id` field identifies a config within the configurations. It has to be unique for the same configType and project. So it's possible to have, for example, two dashboards with the same `id` in two different projects. Note that the field is only local to the Dynatrace Monaco CLI. It has nothing to do with the ID provided by the Dynatrace API. One important use case for this `id` is when using [reference parameters](#reference).

## Type

The `type` field defines the type of the Dynatrace configuration.

A `type` can be one of the supported [Configuration types](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco").

### Type - API

An API `type` can be defined as:

```
type:



api: dashboard
```

or in shorthand form as:

```
type: dashboard
```

See the list of [supported configuration types](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco") for all possible `api` values.

#### Scope parameter

Some API-type configurations have a parent-child relationship with another configuration. Such configurations require a `scope` field that points to the parent configuration.

[Parameter](#parameters) `scope` can be defined as either a [value](#value), [reference](#reference), or [environment](#environment) parameter.

Because such configurations are made in the scope of their parent API, referencing the parent configuration's ID is a useful way of configuring entities after they've been created via the Dynatrace Monaco CLI.

In the sample below, a mobile application is configured, and then key user actions for this application are made.

```
configs:



- id: mobile-application-id



config:



name: my-mobile-app



template: mobile-app.json



skip: false



type:



api: application-mobile



- id: MyKua



type:



api:



name: key-user-actions-mobile



template: kua.json



scope:



configId: mobile-application-id



configType: application-mobile



property: id



type: reference
```

### Type - Settings

[Settings](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") are defined by their `schema`, `scope`, and an optional `schemaVersion`.

A settings `type` can be defined as:

```
type:



settings:



schema: builtin:tags.auto-tagging



scope: environment
```

The `schema` and `schemaVersion` are simply defined as text.

#### Scope parameter

[Parameter](#parameters) `scope` can be defined as either a [value](#value), [reference](#reference), or [environment](#environment) parameter.

In the sample above, it's defined as a shorthand [value](#value) parameter with the value of `environment`, creating a setting in the scope of the entire Dynatrace environment.

Because many settings are made in the scope of a Dynatrace entity, referencing another configuration's ID is a useful way of configuring entities after they've been created via the Dynatrace Monaco CLI.

In the sample below, a web application is configured, and then settings for this application are made.

```
configs:



- id: MyApp



type:



api: application-web



config:



name: My Sample Web Application



template: application.json



- id: MyApp_RUMSettings



type:



settings:



schema: builtin:rum.web.enablement



scope:



type: reference



configType: application-web



configId: MyApp



property: id



config:



name: MyApp_RUMSettings



template: rum-settings.json
```

As you can see, the `scope` of the `rum.web.enablement` setting is a reference to the web application.

#### InsertAfter parameter

Dynatrace Monaco CLI version 2.14.0+

To enforce a specific ordering of Settings 2.0 objects, use the `insertAfter` [parameter](#parameters).
During deployment, Monaco ensures that the settings object is deployed after the referenced one.

The `insertAfter` parameter can be used to:

* Define a [reference](#reference) parameter to insert after a different Monaco configuration.
* Define a [value](#value) parameter to define a hardcoded ID after which the configuration should be added. Dynatrace Monaco CLI version 2.21.0+
* The value `front` or `back` is used to add the configuration either to the front or the back of the list. Dynatrace Monaco CLI version 2.21.0+

Example reference

Example hardcoded ID

Example front/back

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter:



configId: c2314e1b-409c-3eaf-9efa-5dc593b14aff  # Monaco config id



property: id                                    # Dynatrace id property of the referenced config (must be "id")



type: reference                                 # reference type parameter (must be "reference")
```

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter:



value: 43e637dd-ca80-4593-94c4-e2077717555e # hardcoded ID of the configuration this configuration should be inserted AFTER



type: value                                 # value type parameter (must be "value")
```

```
type:



settings:



schema: builtin:container.monitoring-rule



schemaVersion: 0.0.1



scope: environment



insertAfter: front  # or `back` to add this configuration to the front or back of the other configurations
```

If more than one Monaco configuration or project defines `front` or `back`, there is no guarantee which configuration is the very first or last.

#### Permissions parameter

Dynatrace Monaco CLI version 2.23.0+

Use the `allUsers` permission option to set access permissions like `no access`, `read access` or `write access` for certain settings objects.

The `allUsers` option can be used with the following values:

* `none`: The owner has full access to the settings object, while other users have no access.
* `read`: The owner has full access to the settings object, while other users only have read-only access.
* `write`: Every user has full access to the settings object.

Users require both `settings:objects:read` and `settings:objects:write` permissions to read and write settings.

Even if the `allUsers` permission is set to `write` users must still have the necessary permissions to view and edit settings objects.

Example not shared

Example read-only

Example read & write

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: none
```

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: read
```

```
type:



settings:



schema: app:your-owner-based-access-control-app:your-schema-id



schemaVersion: 0.0.1



scope: environment



permissions:



allUsers: write
```

## Config

The `config` field offers the following fields:

* `name`âName used to identify objects in the Dynatrace API
* `template`âDefines templating file used to render the request to the Dynatrace API (for details, see [Manage a Monaco project](/managed/deliver/configuration-as-code/monaco/configuration/projects "Manage a project folder with Dynatrace Configuration as Code via Monaco."))
* Optional `skip`âIf set to `true`, the Dynatrace Monaco CLI will not deploy this configuration
* Optional `parameters`âList of parameters available in the template
* Optional `originObjectId`âSet on download, this field defines the ID of the Dynatrace configuration object from which this config originates. It's used on deployment as an additional identifier.

### Name

* Dynatrace Monaco CLI version 2.6.0 or earlierâThe `name` property is mandatory and needs to be defined for all configuration types.
* Dynatrace Monaco CLI version 2.7.0+âThe `name` property is required only for API-type configurations and is optional for other configuration types.

#### For API type

For configurations of [type API](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-config-api "Learn how to set up your Monaco YAML configuration."), the `name` is used to identify configurations in a Dynatrace environment and ensure that they are updated when they already exist.

For this, the `name` needs to be used in the [JSON template](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") to fill the specific name property of the configuration. Usually, this is also just `name`, but for some configurations, this may differ; see the special cases described for [JSON templates](/managed/deliver/configuration-as-code/monaco/configuration/projects#json-template-file "Manage a project folder with Dynatrace Configuration as Code via Monaco.") and refer to the [API documentation](/managed/dynatrace-api "Find out what you need to use the Dynatrace API.") if in doubt.

When referencing the `name` in a JSON template, it needs to be used as is, with no additional text or characters around it.

The name property in JSON should always be used like this:

```
"{{ .name }}"
```

If you encounter issues with configurations not being created several times instead of updated, check to make sure that your reference to the name does not contain any accidental spaces or other characters that make what is sent to Dynatrace in the JSON different from the name defined in the YAML.

#### For other configuration types

The `name` property isn't used to identify Dynatrace objects. Instead, the configuration's coordinate (a combination of project, type, and configuration ID) or `originObjectId` (if present) is used.

### Skip

The `skip` field makes it possible to omit (skip) deployment of a certain configuration. If `skip` is set to `true`, the Dynatrace Monaco CLI will not deploy the configuration.

The `skip` field behaves like a [parameter](#parameters) and can be defined as either a [value](#value) or [environment](#environment) parameter. Usually, it's defined directly as a shorthand [value](#value) as can be seen in several examples.

It's often useful in combination with [environment overrides](#env-overrides), where you want to deploy a configuration to one environment but exclude it from another.

### Parameters

Parameters are used to provide values in configuration templates. They are defined as YAML objects with a `type` entry. This `type` then further decides how the parameter object is interpreted. One important property of parameters is that they are lazy: the value of a parameter is only evaluated if it's referenced by a configuration that is going to be deployed.

The following parameter types are available:

* [Value](#value)
* [Environment](#environment)
* [Reference](#reference)
* [Compound](#compound)
* [List](#list)
* [File](#file)

#### Value

The value parameter is the simplest form of a parameter. Besides the `type` property, it also requires the `value` property. You can define whatever you like as the value, even nested maps. This value is then accessible in the template file.

Because `value` parameters are the most common parameter type, there is a special short-form syntax to define them: you can simply provide the value if your parameter is neither an array nor a map.

For example:

```
parameters:



threshold: 15



complexThreshold:



type: value



value:



amount: 15



unit: sec
```

In the template of this config, you could then access the `threshold` parameter via `{{ .threshold }}`. To access, for example, the `amount` of the `complexThreshold`, you could use `{{ .complexThreshold.amount }}`.

#### Environment

Parameters of type `environment` allow you to reference an environment variable. The name of the environment variable to reference is defined via a `name` property.

* You can provide a default value (via the `default` property) for cases in which the environment variable is not present.
* If the `default` property is not set and the env variable is missing, the parameter cannot be resolved. This will fail the deployment.

  This is the case only if the parameter is relevant to be deployed. Parameters not referenced by the config to deploy are not evaluated.

Example:

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

In the above example:

* The `owner` parameter will evaluate to the value of the `OWNER` environment variable. If the environment variable is not present, it will evaluate to value `-`.
* The `target` parameter will evaluate to the value of the `TARGET` environment variable. It will fail the deployment if the variable is not set at deployment time.

#### Reference

Because it's often necessary to reference a property of another configuration, the Dynatrace Monaco CLI offers a special `reference` parameter that allows one configuration to depend on almost any parameter of another configuration.

To use the `reference` type parameter, provide the following required fields:

* `project`âThe project name of the configuration the parameter is referencing.
* `configType`âThe type of configuration that the parameter is referencing.

  For configurations of type `settings`, the value of `configType` should correspond to the schema ID (for example, `builtin:tags.auto-tagging`).
* `configId`âThe ID of the configuration that the parameter is referencing.
* `property`âThe field name to determine the value of the parameter.

  If `property` is set to `id` or `name`, the parameter will resolve to the corresponding Dynatrace object's actual ID or name.

In the example below, the value of `mz_id` will be the Dynatrace object ID of the configuration of type `management-zone` with ID `management-zone-config` from the `project-1` project:

```
parameters:



mz_id:



type: reference



project: project-1



configType: management-zone # or builtin:management-zones if referencing "settings" type configurations



configId: management-zone-config



property: id
```

The Dynatrace Monaco CLI will make sure that the deployment of configuration is ordered and that the dependent config is deployed first.

If you configure a cycle of dependencies, the deployment will fail with an error.

##### Short notation

Because `reference` parameters are one of the most common parameter types, there is a special short-form syntax to define them as an array:

* Syntax: `[ <project>, <configType>, <configId>, <property> ]`
* Example: `mz_id: ["project-1", "management-zone", "main", "id"]`

Note that in this case, no `type` is needed, as the type is inferred based on the syntax.

#### Partial references

It's possible to omit some reference fields. In this case, they will be filled with the same value as the current config.

Generally, you might want to use this for simplicity's sake when referencing configuration within the same `project` - simply omit the field.

```
parameters:



mz_id:



type: reference



configType: management-zone



configId: main



property: id
```

While it's possible to omit `configType` and even `configId`, note that you can only leave the upper-most level empty and can't leave a gap.
So if `configType` is omitted, so must `project`.

Below you find a full sample (using shorthand references):

* `infrastructure/management-zone/config.yaml`

  ```
  configs:



  - id: main



  type:



  api: management-zone



  config:



  name: "Main zone"



  template: "zone.json"
  ```
* `development/management-zone/config.yaml`

  ```
  configs:



  - id: development



  type:



  api: management-zone



  config:



  name: "Development zone"



  template: "zone.json"
  ```
* `development/dashboard/config.yaml`

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

#### Compound

The compound parameter is a parameter composed of other parameters of the same config. This parameter requires two properties:

* A `format` string
* A list of `references` to all referenced parameters.

The `format` string can be any string. To use parameters in it, use the syntax `{{ .parameter }}`, where `parameter` is the name of the parameter to be filled in.

For example:

```
parameters:



example:



type: compound



format: "{{ .greeting }} {{ .entity }}!"



references:



- greeting



- entity



greeting: "Hello"



entity: "World"
```

This would produce the value `Hello World!` for `example`. Compound parameters can also be used for more complex values, such as in the following example:

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

This would produce the value `Health: 40%`, for example.

Even though referenced parameters can only be from the same config, by using the reference parameter, it's possible to make a compound parameter with other configs.
This is also true for environment variables.

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



configType: dashboard



configId: dashboard



property: status
```

#### List

Parameters of type `list` allow you to define lists of [value](#value) parameters. When written into a template, these are written as a JSON list surrounded by square brackets and separated by commas.

This type of parameter is generally useful when you require a simple list of things, such as emails or identifiers, that can be filled with any kind of value parameter.

For example:

```
parameters:



recipients:



type: list



values:



- first.last@company.com



- someone.else@company.com



geolocations:



type: list



values: ["GEOLOCATION-1234567", "GEOLOCATION-7654321"]
```

As shown in the example above, you can define the list values either line by line or as an array in YAML.

When using a list parameter value in a JSON template, make sure to just reference the value without any extra brackets.

```
{



"emails": {{ .recipients }}



}
```

This differs from the sometimes-used string list in v1, for which the template required square brackets (for example, `"emails": [ {{ .recipients }} ]`).

#### File

Dynatrace Monaco CLI version 2.14.0+

Parameters of type `file` allow you to load content from a file on disk.

Example:

```
parameters:



comment: "// hello special comment"



myWf:



type: file        # parameter type "file"



path: "myWf.js"   # relative path to the file



references:       # other parameters names referenced in the content of the file



- comment
```

In the given example, the parameter named `myWf` will be dynamically resolved to include the content of the file named `myWf.js`, relative to the current configuration location. This parameter can then be referenced within the JSON template as follows:

```
{



"script" : {{ .myWf }}



}
```

Moreover, you can include references to other parameters within the content of the referenced file. Each reference parameter must be defined as a separate parameter and listed in the references section of the file parameter type.

In the given example, an additional parameter named `comment` can be referenced within the content specified by the file parameter using the notation `{{ .comment }}`.

### OriginObjectID

When using the Dynatrace Monaco CLI to download existing configurations from Dynatrace, the created YAML files contain an `originObjectId` for some configuration types.

This holds the ID of the specific Dynatrace object that was downloaded. It's used when the downloaded configuration is again deployed to the same Dynatrace environment to ensure that the existing object is correctly updated.

For example, an already existing Settings 2.0 object will be extended with [the data used to correctly identify it](/managed/deliver/configuration-as-code/monaco/configuration/special-configuration-types#settings-2-0-objects "Dynatrace Configuration as Code via Monaco - special configuration types.").

Note that `originObjectId` is optional, and you generally don't need to care about it or modify it.

### String escaping of config

In general, all YAML values are escaped before being added to a configuration uploaded to Dynatrace. This ensures that fully filled templates are valid JSON when uploading. Any newlines, special characters such as double quotes, and so on are escaped.

```
parameters:



name: "Dev"



example1: "This is \\n already escaped"



example2: "This will \n be escaped"



example3: This "will" be escaped too



text: |



This will also



be escaped
```

## Override configuration per environment

There are many cases in which a configuration is similar but not the same between environments. Examples:

* An alert is sent to a different Slack channel for staging and production environments
* A service's configuration should be skipped because it's not yet released

To enable this, you can override values of configurations on an environment and environment-group level using the `groupOverrides` and `environmentOverrides` fields.

Both are generally defined in the same way, differing only in whether they're applied to a group or a single environment. You can define the group/environment name to target and any configuration properties to modify.

In the example below, a configuration gets some special configuration applied for two environments, and `skip` ensures that the configuration will not be deployed to the `production-environments` group:

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