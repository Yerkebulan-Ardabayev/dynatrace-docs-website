---
title: Monaco resources
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/monaco-manage-resources
scraped: 2026-02-21T21:19:04.381121
---

# Monaco resources

# Monaco resources

* Latest Dynatrace
* Reference
* 8-min read
* Published Jul 22, 2025

To run Monaco, you need to define the [deployment manifest](/docs/deliver/configuration-as-code/monaco/monaco-concepts#deploy-manifest "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration."), [project directories](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration."), and [resource configuration](/docs/deliver/configuration-as-code/monaco/monaco-concepts#resource-configuration "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration.") so that you can manage the resources.

## Deployment manifest

The [deployment manifest](/docs/deliver/configuration-as-code/monaco/monaco-concepts#deploy-manifest "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration.") file has three top-level keys: `manifestVersion`, `projects`, and `environmentGroups`.

### Sample manifest.yaml

An example of a manifest.yaml:

```
manifestVersion: 1.0



projects:



- name: infra



path: shared/infrastructure



- name: general



path: general



type: grouping



environmentGroups:



- name: dev



environments:



- name: test-env-1



url:



value: https://<YOUR-DT-DEV-ENV-ID>.apps.dynatrace.com



auth:



token:



name: DEV_TOKEN



oAuth:



clientId:



name: DEV_CLIENT_ID



clientSecret:



name: DEV_CLIENT_SECRET



- name: test-env-2



url:



value: https://<YOUR-DT-SPRINT-ENV-ID>.apps.dynatrace.com



auth:



token:



name: SPRINT_TOKEN



oAuth:



clientId:



name: SPRINT_CLIENT_ID



clientSecret:



name: SPRINT_CLIENT_SECRET



- name: prod



environments:



- name: prod-env-1



url:



type: environment



value: https://<YOUR-DT-PROD-ENV-ID>.apps.dynatrace.com



auth:



token:



name: PROD_TOKEN



oAuth:



clientId:



name: PROD_CLIENT_ID



clientSecret:



name: PROD_CLIENT_SECRET
```

### manifestVersion

A manifest must contain a `manifestVersion` as a top-level key.
This is a simple string that is used to validate if the currently used version of Monaco can correctly parse the manifest.

Currently, the supported manifest version is `1.0`.
The release notes will contain details if the manifest is extended, of if newer versions are released.

### projects

All entries under [`projects`](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration.") specify the projects to deploy by Monaco.
To specify a project's:

* Name, provide the `name` key.
* Path, provide the `path`.
* Type, provide the `type` key.

Give these keys a value.

There are two project types: `simple` and `grouping`.

#### simple projects (default type)

A simple project represents the default type and is defined by two properties:

* Required `name`: can't contain any slash characters (`/` or `\`). For example, `/ or DynatraceÂ® Software Intelligence Platform`, is to be distinguished from file system paths.

* Optional `path`: if not stated, the `name` will be used as the path.
  It must always use a forward slash (/) as a separator, regardless of your operating system (Linux, Windows, Mac).

#### grouping projects

A grouping project loads all subfolders of a given path as simple projects.
A grouping project offers a simplified way of grouping multiple projects together.

* Required `name`: used as a prefix for the resulting simple project.
* A dot (`.`) will be used as separator of `<project.name>.<subfolder_name>`.

  A given file structure

  With the following project definition

  Yields two projects

  general/  
  âââ infrastructure/  
  âââ zones/

  ```
  projects:



  - name: general



  path: general



  type: grouping
  ```

  `general.infrastructure`

  `general.zones`

### environmentGroups



An environment is a Dynatrace environment.
You can group these environments together in single environment group using the `environmentGroups` type.
You can apply a configuration to an `environmentGroup`, which implicitly applies it to all environments within the group.
Grouping pre-production and production environments can be helpful, as shown in the initial [`manifest.yaml`](#sample-manifest) example above.

#### environment

An `environment` type consists of `name`, `url`, and `auth` sections.

* `name`: A Monaco-internal name for the given Dynatrace environment.
  The name can be any globally unique string.
  It must be unique.
* `url`: The URL of the Dynatrace environment.

  The environment `url` definition consists of

  + `type`
  + `value`

  The environment's `url` can be defined directly in the manifest or referenced via an environment variable.

  + Defined directly

  ```
  url:



  type: value



  value: "https://<YOUR-ENV-ID>.apps.dynatrace.com"
  ```

  + Via environment variable

  ```
  url:



  type: environment



  value: YOUR_URL_ENV_VAR
  ```
* `auth`: The Dynatrace API authentication method.
  It defines all the information required for authenticated use of the Dynatrace API.

Because these configurations are sensitive, the Dynatrace Monaco CLI doesn't allow you to define them directly, but always loads them from the environment variables.
Make these secrets available as environment variables by following the instructions for your operating system or CI/CD tool.

Always define a `token` specifying the access token for general configuration and settings, including the latest Dynatrace Platform.

Access tokens for the Dynatrace Monaco CLI always require at least the "Access problem and event feed, metrics, and topology (`DataExport`)âAPI v1" permission to query general information about your environment.

You need to configure each available configuration type with specific permissions. For more detailed information, see [Monaco API support and access permission handling](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling "This is a list of the Monaco API support and access permission handling.").

In most cases, you require a token with at least these permissions:

* "Access problem and event feed, metrics, and topology (`DataExport`)âAPI v1"
* "Read configuration (`ReadConfig`)âAPI v2"
* "Write configuration (`WriteConfig`)âAPI v2"
* "Read settings (`settings.read`)âAPI v2"
* "Write settings (`settings.write`)âAPI v2"

For general information on access token authentication, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

You need an OAuth section specifying the OAuth client credentials.

Generally, OAuth client credentials for the Dynatrace Monaco CLI should have at least these scopes:

* Run apps (`app-engine:apps:run`) - This permission is required to access Dynatrace metadata endpoints.
* View settings objects for schema (`settings:objects:read`)
* Create settings objects for schema (`settings:objects:write`)
* View settings schemas (`settings:schemas:read`)

#### projects

The [`projects`](/docs/deliver/configuration-as-code/monaco/monaco-concepts#projects "This is a list of Monaco concepts such as deployment manifest, projects, and resource configuration.") are directories used to logically group API configurations together.
An example of a project could be a service where all configurations regarding this service are present in the folder.
Projects can consist of multiple files and directories.

A project folder contains specifically named subfolders that represent the APIs.
The single API folders further contain another layer of folders, defining the configurations.
The configuration folders finally contain the YAML files specifying what resources get deployed.

#### Configuration files

The configuration files consist of

* [configs YAML file](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas "The Monaco configuration YAML file is structure."), defining parameters, dependencies, name, and template
* JSON template file

config.yaml

slo-cpu-usage.json

```
configs:



- id: newCpuUsageSLO



config:



parameters:



target: 95



title: myNewSLO



entityScope: HOST-#######



template: slo-cpu-usage.json



skip: false



type: slo-v2
```

```
{



"name": "{{ .title }}",



"description": "test SLO for template test",



"tags": [],



"customSli": {



"filterSegments": [],



"indicator": "timeseries sli=avg(dt.host.cpu.usage)\n, by: { \"{{ .entityScope }}\" } \n  , filter: in(dt.entity.host, { $hosts })\n  | fieldsAdd entityName(dt.entity.host)"



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

The Dynatrace Monaco CLI uses Go templates, which allow you to define more complex templates. Still, we recommend keeping templates simpleâreferencing variables via `{{ .PARAMETER_NAME }}` should be sufficient.

##### Important additional information for creating new templates

The JSON files that can be uploaded with Monaco are the JSON objects that the respective Dynatrace APIs accept/return.
Adding a new configuration is generally done via the Dynatrace UI unless you know the configuration JSON structures well enough to prefer writing them.
You can download the configurations via the respective GET endpoint defined in the Dynatrace Configuration API, and they should be cleaned up for auto-deployment.

* A checked-in configuration should not include the entity's `id`.
  The entity can be created or updated if one with the same name exists.
  The `name` must be defined as a variable.
* Avoid hardcoded values for environment information, such as references to other auto-deployed entities, tags, and management zones.
  Reference these as variables.
* Empty/null values that are optional when creating an object.
  Most API GET endpoints return more data than is needed to create an object.
  Many fields are empty or null and can be omitted, such as **tileFilters** on a dashboard.

The special requirements for JSON templates

Some configuration types have special requirements for their JSON payloads and might need manual modification to be used with Configuration as Code.