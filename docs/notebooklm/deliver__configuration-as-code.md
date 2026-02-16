# Dynatrace Documentation: deliver/configuration-as-code

Generated: 2026-02-16

Files combined: 12

---


## Source: account-configuration.md


---
title: Account configuration for Monaco account management
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/account-configuration
scraped: 2026-02-16T09:30:22.332747
---

# Account configuration for Monaco account management

# Account configuration for Monaco account management

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Jan 15, 2026

To define the accounts for which Monaco will configure the account management resources, you need to create an `accounts` section in a [manifest file](/docs/deliver/configuration-as-code/monaco/configuration#manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").

In the following example, we define a single account object containing account-related information. The **name** property specifies the account name (in this example, `my-account`) that can be referenced using the Monaco CLI commands `--account` flag.

```
accounts:



- name: my-account



accountUUID: 12345678-1234-5678-1234-123456789012



oAuth:



clientId:



name: OAUTH_CLIENT_ID



clientSecret:



name: OAUTH_CLIENT_SECRET
```

Account management requires OAuth credentials.
Platform tokens and API tokens are not supported.
The OAuth client must have the appropriate scopes configured for the account resources you want to manage.
Ensure your OAuth credentials include the required permissions for users, groups, policies, boundaries, or service users before deploying configurations.

Other than the `accounts` section, a `manifest.yaml` defined for account resources is the same as for environment configurations, requiring [`projects`](/docs/deliver/configuration-as-code/monaco/configuration#project-definitions "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") of account resource configuration files.

## Account resources

Using Monaco, you can define [users](/docs/manage/identity-access-management/user-and-group-management/access-user-management "User management"), [service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users"), [groups](/docs/manage/identity-access-management/user-and-group-management/access-group-management "Manage Dynatrace groups and their permissions."), [policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"), and [boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") as dedicated types in YAML configuration files.

Unlike the usual environment-level configurations, no JSON template files are needed. Monaco builds the required API data directly from your YAML configuration.

### Example account management resources representation

This example shows how Monaco represents account management resources locally, with examples defining users, service users, groups, policies, and boundaries.

The following sections will describe each configuration in detail.

```
users:



- email: monaco@dynatrace.com



groups:



- Log viewer



- type: reference



id: my-group



serviceUsers:



- name: Monaco service user



description: Description of service user



groups:



- Log viewer



- type: reference



id: my-group



groups:



- name: My Group



id: my-group



description: This is my group



account:



permissions:



- account-viewer



policies:



- policy: Environment role - Access environment



environments:



- environment: abc12345



permissions:



- tenant-viewer



policies:



- policy: Environment role - Replay session data without masking



- policy:



type: reference



id: my-policy



boundaries:



- type: reference



id: workflow-simple-boundary



- MyExistingBoundary # If you want to reference by name directly



managementZones:



- environment: abc12345



managementZone: Management Zone 2000



permissions:



- tenant-viewer



policies:



- name: My Policy



id: my-policy



level:



type: account



description: My policy description.



policy: |-



ALLOW automation:workflows:read;



boundaries:



- id: workflow-simple-boundary



name: Workflow Simple boundary



query: automation:workflow-type = "SIMPLE";
```

While this sample shows users, service users, groups, policies, and boundaries defined in a single file, you can define them in individual files and structure your account resource projects and files as needed.

### Users

```
users:



- email: my-user@example.com



groups:



- Log viewer



- type: reference



id: my-group
```

In this example, we define these objects.

* **users** define one or more users bound to different groups.

  + **email** address
  + **groups** specifies the groups to which the user belongs. In the example, the user belongs to the default `Log viewer` group.

    - **type**
    - **id** specifies a custom group, for example, `my-group`. This **id** must match a group defined under the **groups** field.

### Service users

Dynatrace Monaco CLI version 2.23.0+

```
serviceUsers:



- name: Monaco service user



description: Description of the service user.



originObjectId: 123e4567-e89b-12d3-a456-426614174000



groups:



- Log viewer



- type: reference



id: my-group
```

In this example, we define these objects.

* **serviceUsers** define one or more service users bound to different groups.

  + **name** is the name of the service user. If not unique within an account, an **originObjectId** must be provided.
  + **description** is an optional description of the service user.
  + **originObjectId** is an optional Dynatrace ID of an existing service user to update, used to differentiate between service users if more than one has the same name.
  + **groups** specifies the groups to which the service user belongs. In the example, the service user belongs to the default `Log viewer` group and to `my-group` defined under the **groups** field. As the latter is a reference, **type** must be set to `reference` and **id** must match that of a group defined under the **groups** field.

### Groups

```
groups:



- name: My Group



id: my-group



description: This is my group



account:



permissions:



- account-viewer



policies:



- policy: Environment role - Access environment



environments:



- environment: abc12345



permissions:



- tenant-viewer



policies:



- policy: Environment role - Replay session data without masking



- policy:



type: reference



id: my-policy



boundaries:



- type: reference



id: my-boundary



- MyExistingBoundary # If you want to reference by name directly



managementZones:



- environment: abc12345



managementZone: Management Zone 2000



permissions:



- tenant-viewer
```

In this example, we define these objects.

* **groups** defines one or more groups that are bound to different policies or permissions.

  + **name**: The name of the group.
  + **id**: A monaco-internal unique identifier for the group, which users and service users can reference.
  + **description**: A description of the group.
  + **account** specifies permissions and policies to which the group is bound on the account level.
  + **environments** specify the permissions and policies to which the group is bound on the environment level.

    - **name**: The environment-id.
    - **permissions**: A list of permissions assigned to the group for this environment.
    - **policies**
    - **policy** can be referenced by name if a default policy is available.

      * **type** must be set to `reference` when referencing a custom policy.
      * **id** references a custom policy. The **id** must match a policy defined in the **policies**.
    - **boundaries** can be referenced by name if it's available.

      * **id** references a custom boundary. The **id** must match a boundary defined in the **boundaries**.
      * **type** must be set to `reference` when referencing a custom boundary.
  + **managementZones**: specifies the permissions assigned to the group on the management zone level.

    - **environment**: The environment-id.
    - **managementZone**: The name of the environment zone, for example, `Management Zone 2000`.
    - **permissions**: A list of permissions assigned to the group for this management zone.

### Policies

```
policies:



- name: My policy



id: my-policy



level:



type: account



description: My policy is defined for the account.



policy: |-



ALLOW automation:workflows:read;



- name: My other policy.



id: my-other-policy



level:



type: environment



environment: abc12345



description: My policy is defined for a specific environment.



policy: |-



ALLOW automation:workflows:read;
```

In this example, we define these objects.

* **policies** defines one or more policies.

  + **name**: The name of the policy.
  + **id**: A monaco-internal unique identifier for the policy, which can be referenced by groups.
  + **level**: Specifies the level of the policy.

    - **type**: This can be `account` or `environment`.
    - **environment**: If the type is `environment`, specify the environment ID for which this policy applies.
  + **description**: A description of the policy.
  + **policy** contains any policy rules of this particular policy.

### Boundaries

```
boundaries:



- id: workflow-simple-boundary



name: Workflow Simple boundary



query: automation:workflow-type = "SIMPLE";
```

In this example, we define these objects.

* **boundaries** defines one or more boundaries.

  + **id**
  + **name**
  + **query** contains one or more policy statements separated by `;`.

## Commands

Because account-level configuration is usually distinct from environment-level configuration and changes less frequently, existing commands like `monaco deploy` ignore any account configuration that may be defined in a manifest file.

Dedicated commands exist for account resources: [Account](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#account "How to use the Monaco CLI application, including arguments and options.").


---


## Source: monaco-manage-resources.md


---
title: Monaco resources
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/monaco-manage-resources
scraped: 2026-02-16T09:36:39.396028
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


---


## Source: special-configuration-types-saas.md


---
title: Monaco configuration YAML file - list of special configuration types
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas
scraped: 2026-02-16T21:29:59.595544
---

# Monaco configuration YAML file - list of special configuration types

# Monaco configuration YAML file - list of special configuration types

* Latest Dynatrace
* Reference
* 6-min read
* Published Sep 14, 2025

This section describes how only one, single configuration end point should be present. It also describes the configuration types with non-standard behavior and specific constraints when working with the related APIs.
For more information, see [supported Configuration API types](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling#supported-api-types "This is a list of the Monaco API support and access permission handling.").

## Single configuration endpoint

These configurations are global to a Dynatrace environment and a one-off.
Unlike other configurations, there is usually some default configuration that you can update.

Be aware that only one such configuration should be present in your configuration.
Having multiple configurations, for example, in several projects deployed in one run, results in the last applied configuration being active on the Dynatrace environment.

## Non-unique name

Monaco assumes a unique configuration name and uses it as the identifier when creating or updating a configuration.
This is true for most configurations created in the Dynatrace web UI or via API calls.

Some configurations can have the same names, which causes issues for the Dynatrace Monaco CLI.
For example, there can be several dashboards named `MyDashboard`.
If more than one name configuration is present, the Dynatrace Monaco CLI can't ensure that the correct one is updated when searching by name. Similar problems are present when downloading.

Dynatrace Monaco CLI specially handles these configuration APIs to ensure the following:

* They receive a known identifier when originating from the Dynatrace Monaco CLI.
* They are stored with their Dynatrace identifier rather than their name when downloading.

## Calculated metrics

Calculated metric type names should be globally unique.
Otherwise, Monaco may return `duplicate config name` errors.

Generally, calculated metrics behave as non-unique name types but use a `metricKey` that you can define as an identifier, so the automated handling described above is impossible.

While the API and web UI allow you to create several configurations with the same `name`, the Dynatrace Monaco CLI can't uniquely identify these configurations.
After a [download](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#download "How to use the Monaco CLI application, including arguments and options."), you may see `duplicate config name` errors for calculated metric types.

The `calculated-metrics-log` type, which allows configuring the metrics for the deprecated Logs v1, needs further special handling. For more information, see [calculated log metrics JSON](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#log-metrics-json "This is a list of Monaco special configuration types.") below.

## Settings 2.0 objects

The handling of Settings 2.0 objects differs from classic configurations.
Unlike the latter, which are typically identified by name, Settings 2.0 objects might not have a unique name or any name at all.
Instead, they are assigned an external identifier called `externalId` that enables them to be uniquely identified.

The `externalId` consists of the prefix `monaco:` followed by an identifier generated by the Dynatrace Monaco CLI on deployment.

To ensure that the existing Settings 2.0 objects are reliably updated, the Dynatrace Monaco CLI records the original Dynatrace object IDs when downloading and includes them in the YAML configuration field `originObjectId`.

Settings objects also have special requirements for their JSON templates. For more details, see [Settings JSON](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#settings-json "This is a list of Monaco special configuration types.") below.

## Special requirements for JSON templates

Some types of configuration have special requirements for their JSON payloads and may need manual attention.

### Dashboard JSON

When you create a dashboard, it's private by default.
All the dashboards defined via Configuration as Code need to be shared publicly with other users; otherwise, only the owner of the access token used to deploy can view them.
You can change this in the dashboard's **Settings** or by changing your checked-in `json` file.

We recommend the following values for the `dashboardMetadata`:

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

This configuration does the following:

* References the name of the dashboard as a [variable](#configuration-yaml-structure)
* Shares the dashboard with other users
* Sets a management zone filter on the entire dashboard, again as a variable, typically [referenced from another configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas#reference "The Monaco configuration YAML file is structure.") TODO

Filtering the whole dashboard by management zone ensures that only data that is meant to be displayed is picked up by the dashboard tiles, and it eliminates the possible need to define filters for individual tiles.

* Dynatrace Monaco CLI version 1.208+ A dashboard configuration must have a property owner. The property owner in `dashboardMetadata` is mandatory and must contain a non-null value.
* Dynatrace Monaco CLI version 1.208+ The property `sharingDetails` in `dashboardMetadata` is no longer present.

### Calculated log metrics JSON

The calculated log metrics API requires the following specific naming conventions.
To ensure Dynatrace Monaco considers these configurations, the log metric's `metricKey` must be reused as the configuration's `name`.

If you experience failing configuration deployments, consider setting the same value for `metricKey` and `displayName`.

You need to reference at least the `metricKey` of the log metric, as `{{ .name }}` in the JSON file as shown here:

```
configs:



- id: some-log-metric-config



config:



name:  "cal.log:this-is-some-metric"



[...]
```

And in the corresponding JSON:

```
{



"metricKey": "{{ .name }}",



"active": true,



"displayName": "{{ .name }}",



[...]



}
```

### Conditional naming JSON

The conditional naming API does not provide a `name` parameter.
Since Dynatrace Monaco CLI requires a name property in the `config.yaml`, it needs to be mapped to the `displayName` field in the JSON template.

The `PROCESS_GROUP` type:

```
{



"type": "PROCESS_GROUP",



"nameFormat": "Test naming PG for {Host:DetectedName}",



"displayName": "{{ .name }}",



[...]



}
```

The `HOST` type:

```
{



"type": "HOST",



"nameFormat": "Test - {Host:DetectedName}",



"displayName": "{{ .name }}",



[...]



}
```

The `SERVICE` type:

```
{



"type": "SERVICE",



"nameFormat": "{ProcessGroup:KubernetesNamespace} - {Service:DetectedName}",



"displayName": "{{ .name }}",



...



}
```

### Settings 2.0 JSON

The [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") has additional properties unrelated to the specific schemas.
This requires Dynatrace Monaco CLI to set further parameters.

The JSON templates for Settings should only include the actual configuration `value`.

For example, while the API response for a custom alert config (`builtin:davis.anomaly-detectors`) is:

```
{



"items": [



{



"objectId": "XYZ",



"value": {



"enabled": false,



"title": "Error when adding item to cart",



"description": "",



"source": "Anomaly Detection",



"executionSettings": {



"queryOffset": 3



},



"analyzer": {



"name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",



"input": [



{



"key": "query",



"value": "timeseries cartFailedToAddItem=sum(log.cartFailedToAddItem)"



},



{



"key": "slidingWindow",



"value": "3"



},



{



"key": "violatingSamples",



"value": "1"



},



{



"key": "dealertingSamples",



"value": "3"



},



{



"key": "alertCondition",



"value": "ABOVE"



},



{



"key": "alertOnMissingData",



"value": "false"



},



{



"key": "threshold",



"value": "0"



}



]



},



"eventTemplate": {



"properties": [



{



"key": "event.name",



"value": "Cart Failure increase"



},



{



"key": "event.description",



"value": "The {metricname} value was {alert_condition} normal behavior."



},



{



"key": "event.type",



"value": "ERROR_EVENT"



},



{



"key": "dt.event.allow_davis_merge",



"value": "true"



}



]



}



}



}



]



"totalCount": 89,



"pageSize": 1,



"nextPageKey": "XY"



}
```

The Dynatrace Monaco JSON template only requires the `value` content:

```
{



"enabled": false,



"title": "Error when adding item to cart",



"description": "",



"source": "Anomaly Detection",



"executionSettings": {



"queryOffset": 3



},



"analyzer": {



"name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",



"input": [



{



"key": "query",



"value": "timeseries cartFailedToAddItem=sum(log.cartFailedToAddItem)"



},



{



"key": "slidingWindow",



"value": "3"



},



{



"key": "violatingSamples",



"value": "1"



},



{



"key": "dealertingSamples",



"value": "3"



},



{



"key": "alertCondition",



"value": "ABOVE"



},



{



"key": "alertOnMissingData",



"value": "false"



},



{



"key": "threshold",



"value": "0"



}



]



},



"eventTemplate": {



"properties": [



{



"key": "event.name",



"value": "Cart Failure increase"



},



{



"key": "event.description",



"value": "The {metricname} value was {alert_condition} normal behavior."



},



{



"key": "event.type",



"value": "ERROR_EVENT"



},



{



"key": "dt.event.allow_davis_merge",



"value": "true"



}



]



}



}
```

When using the [download command](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#download "How to use the Monaco CLI application, including arguments and options."), this happens automatically.


---


## Source: yaml-configuration-saas.md


---
title: Monaco configuration YAML file structure
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas
scraped: 2026-02-16T21:30:31.097027
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


---


## Source: monaco-api-support-and-access-handling.md


---
title: Monaco API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling
scraped: 2026-02-15T21:25:17.814798
---

# Monaco API support and access permission handling

# Monaco API support and access permission handling

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 27, 2025

Dynatrace offers different options to authenticate API calls. Dynatrace Monaco supports the following authentication options:

* Platform tokens
* OAuth clients

For details about Dynatrace Identity and Access Management (including platform tokens,API tokens, and OAuth clients), see [Tokens and OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Create a platform token for the Dynatrace Monaco CLI

To create a platform token, follow the steps described in [Create a platform token for the Dynatrace Monaco CLI](/docs/deliver/configuration-as-code/monaco/guides/create-platform-token "Create a platform token for Dynatrace Configuration as Code via Monaco.").
Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Create an OAuth client for the Dynatrace Monaco CLI

To create an OAuth client, follow the steps described in [Create an OAuth2 client](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-an-oauth2-client "Manage authentication and user permissions using OAuth clients.").

Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To use the `automation:workflows:admin` scope, you need to do the following before creating the OAuth client.

1. Create a custom policy granting that scope.
2. Bind a group to it.
3. Assign your user to that group.

For detailed information on managing policies, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To manage OpenPipeline configurations, ensure that the user belongs to a group with the policy **Data Processing and Storage** assigned to it.
Do this before creating the OAuth client.

In addition to the scopes available to the OAuth client, permissions can be further limited via policies applied to the user's groups.

When working with a service user, ensure the service user's permissions match the OAuth scopes for all environments.
For details on how permissions can be controlled, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

To use your OAuth client:

1. Follow the instructions for your operating system or CI/CD tool on how to make the client ID and secret available as environment variables.
2. Reference the environment variables you have created in the OAuth section of your manifest file
3. Dynatrace Monaco CLI will request OAuth access tokens using your client credentials to make authenticated API calls.

## API coverage

Dynatrace Monaco supports the following configuration types:

* Settings 2.0
* Configuration APIs
* Platform APIs

The specific configuration types are defined in the Monaco configuration YAML file.

### Settings 2.0

Settings 2.0 resources require a classic Dynatrace API access token or OAuth credentials.

The Dynatrace Monaco CLI provides general support for any Settings 2.0 schema available in your environment.
For information about schemas, see [Settings 2.0 - Available schemas](/docs/dynatrace-api/environment-api/settings/schemas "View the entire settings schemas table of your monitoring environment via the Dynatrace API.").

For latest Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings:objects:read`, `settings:objects:write` |
| View Settings 2.0 schemas | `settings:schemas:read` |

For classic Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings.read`, `settings.write` |

### Supported platform API types

The Dynatrace platform provides a collection of [platform servicesï»¿](https://developer.dynatrace.com/plan/platform-services/), each with a specific area of responsibility.
OAuth credentials are required to target platform APIs.

The Dynatrace Monaco CLI provides support for Dynatrace platform API types as described in the table below.

Platform service

Configuration type

Endpoint

OAuth client permissions

Monaco CLI version

Automation

`business-calendars`

`/platform/automation/v1/business-calendars`

`automation:calendars:read`, `automation:calendars:write`

2.6.0+

Automation

`scheduling-rules`

`/platform/automation/v1/scheduling-rules`

`automation:rules:read`, `automation:rules:write`

2.6.0+

Automation

`workflows`

`/platform/automation/v1/workflow`

`automation:workflows:read`, `automation:workflows:write`

2.6.0+

Grailâ-storage management

`buckets`

`/platform/storage/management/v1/bucket-definitions`

`storage:bucket-definitions:read`, `storage:bucket-definitions:write`, `storage:bucket-definitions:delete`

2.9.0+

Documents (Dashboards, Notebooks, Launchpads)

`documents`

`/platform/document/v1/documents`

`document:documents:write`, `document:documents:read`, `document:documents:delete`, `document:trash.documents:delete`

2.15.0+

OpenPipeline

`openpipelines`

`/platform/openpipeline/v1/configurations`

`openpipeline:configurations:read`, `openpipeline:configurations:write`

2.15.0+

Grail

`segment`

`/platform/storage/filter-segments/v1/filter-segments`

`storage:filter-segments:read`, `storage:filter-segments:write`, `storage:filter-segments:delete`, `storage:filter-segments:admin`

2.19.0+

SLOs

`slo-v2`

`/platform/slo/v1/slos`

`slo:slos:read`, `slo:slos:write`, `slo:objective-templates:read`

2.22.0+

### Account Management permissions

To manage account resources, such as user management or policy handling, OAuth credentials require the following permissions:

* `account-idm-read`
* `account-idm-write`
* `account-env-read`
* `account-env-write`
* `iam-policies-management`
* `iam:policies:write`
* `iam:policies:read`
* `iam:bindings:write`
* `iam:bindings:read`
* `iam:boundaries:read`
* `iam:boundaries:write`

### Supported Configuration API types

Configuration via the [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.") requires an API access token.
Dynatrace Monaco CLI provides support for most Configuration APIs, as described in the table below.
This table provides:

* The supported configuration types.
* Their API endpoints.
* The access token permissions that are required to interact with any endpoint.

Note that most Configuration APIs are deprecated in favor of Settings 2.0, see [Settings 2.0](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Configuration type

Constraints

Endpoint and access permission

**alerting-profile**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Problem alerting profiles schema: `builtin:alerting.profile`

RUM: **allowed-beacon-origins**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**anomaly-detection-applications**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-aws**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-database-services**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-disks**

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-hosts**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-metrics**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Metric events schema:
`builtin:anomaly-detection.metric-events`

**anomaly-detection-services**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-vmware**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**app-detection-rule**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**app-detection-rule-host**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**application-web**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**application-mobile**

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**auto-tag**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Automatically applied tags schema: `builtin:tags.auto-tagging`

**aws-credentials**

It can't be downloaded.

[AWS credentials API](/docs/dynatrace-api/configuration-api/aws-credentials-api "Learn what the Dynatrace AWS credentials config API offers.")

**azure-credentials**

It can't be downloaded.

[Azure credentials API](/docs/dynatrace-api/configuration-api/azure-credentials-api "Learn what the Dynatrace Azure credentials config API offers.")

**calculated-metrics-application-mobile**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-application-web**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-log**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with SchemaID `builtin:logmonitoring.schemaless-log-metric`.

**calculated-metrics-service**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-synthetic**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**conditional-naming-host**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**conditional-naming-processgroup**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**conditional-naming-service**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**content-resources**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**credential-vault**

It can't be downloaded.

[Credential vault API](/docs/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers.")

**custom-service-java**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-dotnet**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-go**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-nodejs**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-php**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

Dashboard Classic

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

dashboard-share-settings classic

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.") and [Scoped configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#API-type-field "This is a list of Monaco special configuration types.")

[Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

**data-privacy**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Data privacy API](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

**extension**

It can't be downloaded.

[Extensions API](/docs/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

**extension-elasticsearch**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Extensions API](/docs/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

**failure-detection-parametersets**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**failure-detection-rules**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**frequent-issue-detection**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with `builtin:anomaly-detection.frequent-issues` schema

**geo-ip-address-mappings**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**geo-ip-detection-headers**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**hosts-auto-update**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[OneAgent environment-wide configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

**key-user-actions-mobile**

[Scoped configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**key-user-actions-web**

[Scoped Configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**kubernetes-credentials**

It can't be downloaded.

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with [Settings API - Connection settings schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") `builtin:cloud.kubernetes` and [Settings API - Monitoring settings schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.") `builtin:cloud.kubernetes.monitoring` schemas

**maintenance-window**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the Maintenance windows `builtin:alerting.maintenance-window` schema

**management-zone**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the Problem notifications `builtin:problem.notifications` schema

network-zone Dynatrace Monaco CLI version 2.10.0+

[Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

**notification**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with Problem notifications `builtin:problem.notifications` schema

**reports**

[Reports API](/docs/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")

**request-attributes**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**request-naming-service**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**slo classic**

[Service-level Objectives API classic](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.")

**service-detection-full-web-request**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-full-web-service**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-opaque-web-request**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-opaque-web-service**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-resource-naming**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.") `/api/config/v1/service/resourceNaming`

**synthetic-location**

[Synthetic API v1](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.")

**synthetic-monitor**

[Synthetic API v2](/docs/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers.")

**user-action-and-session-properties-mobile**

[Scoped Configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

## Related topics

* [Monaco configuration YAML file - list of special configuration types](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas "This is a list of Monaco special configuration types.")


---


## Source: monaco-concepts.md


---
title: Monaco concepts
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-concepts
scraped: 2026-02-16T21:26:25.397736
---

# Monaco concepts

# Monaco concepts

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Oct 07, 2025

Monaco was designed within Dynatrace to allow configuring Dynatrace environments at scale and in a reliable and secure way.
It represents a lightweight CLI tool that uses native JSON to describe Dynatrace configuration resources.

Monaco is a Dynatrace proprietary solution that can operate standalone; hence, no additional third-party tool is required to use it.

## Advantages of using Dynatrace Monaco

* No manual edits in production needed.
* Scale configs via teams and stages.
* Keep configs or environments in sync.
* Recreate configs (e.g., for purposes of disaster recovery).

## Monaco concepts

Deployment manifest
:   The deployment manifest defines the projects and configuration files folder you deploy to the specified target environment.
    Deployment manifests are YAML files that tell the Dynatrace Monaco CLI what projects to deploy and exactly where they should be deployed.
    For the Dynatrace Monaco CLI to know what to deploy, a manifest file has to be present.
    This file provides details on what to deploy and where to deploy it.
    The manifest is saved as a YAML file.

Projects
:   Monaco projects are directories (folders) that logically group API configurations. An example of a project could be a service where all configurations regarding this service are present in the folder. Projects can consist of multiple files and directories. For more information, see [Manage a Monaco project](/docs/deliver/configuration-as-code/monaco/configuration/projects "Manage a project folder with Dynatrace Configuration as Code via Monaco.").

    The projects directories group configuration files that are deployed to the same target environment.

Dynatrace resource configuration
:   The Dynatrace resource configuration consists of a couple of elements.

    * The YAML file with the defining parameters, dependencies, name, and related JSON template.
    * The JSON template file holds the needed API payload, including the placeholders for parameters of the YAML file.

    The configuration YAML file contains basic information about the configuration to deploy.

    The basic information includes the configuration's name, the location of the template file, and the parameters usable in the template file.
    Parameters can be overwritten based on which group or environment is currently deployed.

    The JSON template file contains the payload that will be uploaded to the Dynatrace API endpoints. It allows you to reference all defined configuration parameters via `{{ .PARAMETER_NAME }}` syntax.


---


## Source: monaco-getting-started.md


---
title: Manage configurations with Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-getting-started
scraped: 2026-02-16T09:29:08.031533
---

# Manage configurations with Monaco

# Manage configurations with Monaco

* Latest Dynatrace
* Explanation
* 6-min read
* Published Jul 22, 2025

To get you started with managing configurations, this section will guide you through a simple example of how to use Monaco to create, deploy, and delete a configuration.

## Prerequisites

* [Install Monaco](/docs/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.") and make the executable available in your `PATH`.
* Create a [platform token or OAuth client](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling "This is a list of the Monaco API support and access permission handling.") with the correct access permissions.
  The correct permissions depend on which APIs you use.

  For more info, see the API documentation or [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

In this example, we will make use of the SLO configuration, which requires the following permissions:

* `slo:slos:read`
* `slo:slos:write`
* `slo:objective-templates:read`

## Create a new configuration with Monaco

To create a new Dynatrace configuration, follow the steps below.

1. Set up the project directory.
   Run the following commands.

   ```
   mkdir -p monaco-getting-started/project-example/slo



   cd monaco-getting-started/project-example/slo
   ```
2. Create two files.
   Run the following commands.

   ```
   # Linux



   touch slo.json slo.yaml



   # Windows



   New-Item slo.json



   New-Item slo.yaml
   ```
3. Populate `slo.json`.
   Open the JSON configuration file in your text editor and paste the contents of the code block below.
   Save the file.

   ```
   {



   "name": "{{ .name }}",



   "description": "Measures the proportion of successful service requests over time.",



   "tags": {{ .tags }},



   "criteria": [



   {



   "target": 95,



   "timeframeFrom": "now-7d",



   "timeframeTo": "now"



   }



   ],



   "customSli": {



   "filterSegments": [],



   "indicator": "timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }\n  , by: { dt.entity.service }\n  | fieldsAdd sli=(((total[]-failures[])/total[])*(100))\n | fieldsRemove total, failures"



   }



   }
   ```

   The name and tags used in this configuration are specified as variables.
   Their values will be given in the YAML configuration.
4. Populate `slo.yaml`.
   Open the YAML configuration file in your text editor and paste the contents of the code block below.
   Save the file.

   ```
   configs:



   - id: my-sample-slo



   config:



   name: mySampleSLO



   parameters:



   tags:



   type: list



   values: ["service:myService",



   "dt.owner:myTeam"]



   template: slo.json



   skip: false



   type: slo-v2
   ```

   The values of `name` and `tags` will be propagated to the related placeholders in the `slo.json` file.
5. Create a deployment manifest in the configuration directory.
   Run the following commands.

   ```
   # Linux



   cd ../..



   touch manifest.yaml



   # Windows



   cd ../..



   New-Item manifest.yaml
   ```
6. Populate `manifest.yaml`.
   Open the YAML configuration file in your text editor and paste the contents of the code block below.
   Save the file.

   ```
   manifestVersion: 1.0



   projects:



   - name: my-slo-project



   path: project-example



   environmentGroups:



   - name: development



   environments:



   - name: development-environment



   url:



   type: environment



   value: DT_ENV_URL



   auth:



   platformToken:



   type: environment



   name: PLATFORM_TOKEN
   ```
7. Specify the following environment variables.
   Run the commands below.

   ```
   # Linux



   export DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"



   export PLATFORM_TOKEN="YourPlatformTokenValue"



   # Windows



   $env:DT_ENV_URL="https://<your-dynatrace-environment>.apps.dynatrace.com"



   $env:PLATFORM_TOKEN="YourTokenValue"
   ```
8. Run Monaco to check if the configuration is syntactically valid and consistent.

   ```
   monaco deploy --dry-run manifest.yaml
   ```

   A successful run will return output similar to that shown in the code block below.

   ```
   time=2025-09-01T09:06:23.506+02:00 level=INFO msg="Monaco version 2.24.0"



   time=2025-09-01T09:06:23.507+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"



   time=2025-09-01T09:06:23.535+02:00 level=INFO msg="Projects to be deployed (1):"



   time=2025-09-01T09:06:23.536+02:00 level=INFO msg="  - my-slo-project"



   time=2025-09-01T09:06:23.536+02:00 level=INFO msg="Environments to deploy to (1):"



   time=2025-09-01T09:06:23.537+02:00 level=INFO msg="  - development-environment"



   time=2025-09-01T09:06:23.537+02:00 level=INFO msg="Deploying configurations to environment \"development-environment\"..." environment.name=default environment.group=group



   time=2025-09-01T09:06:23.556+02:00 level=INFO msg="Deploying config" deploymentStatus=deploying environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0



   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Deployment successful" deploymentStatus=deployed environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0



   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Deployment successful for environment 'development-environment'" environment.group=group environment.name=development-environment environment.name=development-environment environment.group=group



   time=2025-09-01T09:06:23.557+02:00 level=INFO msg="Validation finished without errors"
   ```

You have now created valid Dynatrace configuration files to be used with Dynatrace Monaco CLI.

## Deploy a new configuration with Monaco

Now that you have created the configuration, you need to deploy it to your Dynatrace environment.

Apply your configuration with the name of the deployment file provided as an argument.
Run the following command.

```
monaco deploy manifest.yaml
```

A successful deployment will return output similar to that shown in the code block below.

```
time=2025-09-01T09:08:23.506+02:00 level=INFO msg="Monaco version 2.24.0"



time=2025-09-01T09:08:23.507+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"



time=2025-09-01T09:08:23.535+02:00 level=INFO msg="Projects to be deployed (1):"



time=2025-09-01T09:08:23.536+02:00 level=INFO msg="  - my-slo-project"



time=2025-09-01T09:08:23.536+02:00 level=INFO msg="Environments to deploy to (1):"



time=2025-09-01T09:08:23.537+02:00 level=INFO msg="  - development-environment"



time=2025-09-01T09:08:23.537+02:00 level=INFO msg="Deploying configurations to environment \"development-environment\"..." environment.name=default environment.group=group



time=2025-09-01T09:08:23.556+02:00 level=INFO msg="Deploying config" deploymentStatus=deploying environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo-v2:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0



time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment successful" deploymentStatus=deployed environment.name=development-environment environment.group=group coordinate.reference=my-slo-project:slo:my-sample-slo coordinate.project=my-slo-project coordinate.type=slo-v2 coordinate.configId=my-sample-slo gid=0



time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment successful for environment 'development-environment'" environment.group=group environment.name=development-environment environment.name=development-environment environment.group=group



time=2025-09-01T09:08:23.557+02:00 level=INFO msg="Deployment finished without errors"
```

If your configuration fails to deploy, refer to the output error description.
Your files may have syntax errors or your platform token may require more permissions.

To verify that your Dynatrace config has been created in your Dynatrace environment:

1. Log in to your Dynatrace environment.
2. Go to **Settings** > **Analyze and alert** > **Site reliability** > **Service-level objectives (SLOs)**.
3. Search for `mySampleSLO`.

## Delete a configuration with Monaco

Now that your configuration is deployed, you can delete it from your local filesystem.

1. To delete the previously created SLO, create a delete file.
   Run the following command.

   ```
   # Linux



   touch delete.yaml



   # Windows



   New-Item delete.yaml
   ```
2. Open the file in your text editor and paste the following configuration.
   Save the file.

   ```
   delete:



   - project: my-slo-project



   type: slo-v2



   id: my-sample-slo
   ```
3. Run Monaco to delete the configuration, specifying the delete file and the manifest.
   This specifies in which environments the configuration should be deleted.
   Run the following command.

   ```
   monaco delete --manifest manifest.yaml --file delete.yaml -e development-environment
   ```

   A successful deletion will return output similar to that shown in the code block below.

   ```
   time=2025-09-01T09:10:23.506+02:00 level=INFO msg="Monaco version 2.24.0"



   time=2025-09-01T09:10:23.751+02:00 level=INFO msg="Loading manifest \"{your full path to the file}\manifest.yaml\". Restrictions: groups=[], environments=[]" manifestPath="{your full path to the file}\manifest.yaml"



   time=2025-09-01T09:11:24.140+02:00 level=INFO msg="Deleting configs for environment \"development-environment\"..." environment.name=development-environment environment.group=group



   time=2025-09-01T09:11:24.140+02:00 level=INFO msg="Deleting 1 config(s) of type \"slo-v2\"..." type=slo-v2 environment.name=development-environment environment.group=group
   ```

Verify that your Dynatrace config has been deleted from your Dynatrace environment.

1. Log in to your Dynatrace environment.
2. Go to **Settings** > **Analyze and alert** > **Site reliability** > **Service-level objectives (SLOs)**.
3. Search for `mySampleSLO`.

## Related topics

* [Install Dynatrace Configuration as Code via Monaco](/docs/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.")
* [Monaco API support and access permission handling](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling "This is a list of the Monaco API support and access permission handling.")


---


## Source: commands-saas.md


---
title: Work with Dynatrace Monaco CLI commands for Latest Dynatrace
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/reference/commands-saas
scraped: 2026-02-16T21:30:32.702727
---

# Work with Dynatrace Monaco CLI commands for Latest Dynatrace

# Work with Dynatrace Monaco CLI commands for Latest Dynatrace

* Latest Dynatrace
* Reference
* Updated on Jan 26, 2026

The Dynatrace Monaco CLI offers several native commands that can be used to manage Dynatrace configuration files.

* `deploy`: Deploy configurations to a Dynatrace environment.
* `download`: Download configurations from a Dynatrace environment.
* `delete`: Remove configurations from a Dynatrace environment and exclude them from subsequent deployments.
* `generate`: Generate file skeletons based on a given configuration.
* `account`: Operations involving Account Management resources.
* Global flags: modify the commands.

## Deploy

The `deploy` command deploys configurations to environments defined in a selected deployment manifest file.

### Usage

```
monaco deploy [ARGS] [OPTIONS]
```

The most straightforward way to use deploy is to run it without any flags and pass the file name of your deployment manifest.
This way, all configurations in the project section of the deployment manifest file are applied to all environments defined in the environments section of the file.

### Arguments

Argument

Description

Required

`<manifest.yaml>`

The manifest file defining projects to deploy and the environments to deploy them to.

Required

### Options

Option

Description

Required

`--continue-on-error`, `-c`

Proceed with deployment even if an error is encountered.

This can be used to ensure that all valid configurations are applied to your environments, even if other configurations are invalid or failed to deploy.

Using this flag might lead to follow-up errors for configurations that depend on each other.

Optional

`--dry-run`, `-d`

Validate the configuration file structure without deploying it.

With this flag set, `monaco deploy` checks whether your templates are valid JSON and whether your configuration YAML files can be parsed and used.

A `dry-run` doesn't connect to Dynatrace and can't validate the content of the JSON sent to Dynatrace.
A deployment may still fail with `HTTP 400 Bad Request` errors after a successful `dry-run` if the content of a JSON template is incorrect.

Optional

`--environment <name>`, `-e <name>`

Apply your configurations to specific environments within your deployment manifest file.
To set multiple environments, either repeat this flag or separate them using a comma (`,`).

This flag is mutually exclusive with `--group`:

* If this flag is specified, configurations are deployed to each specified environment.
* If neither `--group` nor `--environment` is present, all environments are used.

Optional

`--group <name>`, `-g <name>`

Apply your configurations to specific [environment groups](/docs/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") within your deployment manifest file.
To set multiple groups, either repeat this flag or separate them using a comma (`,`).

This flag is mutually exclusive with `--environment`:

* If this flag is specified, configurations are deployed to each environment within the specified groups.
* If neither `--group` nor `--environment` is present, all environments are used.

Optional

`--project <name>`, `-p <name>`

Specify one or more projects to be deployed.
To set multiple projects, either repeat this flag or separate them using a comma (`,`).

* If this flag is specified, configurations from the specified projects are deployed.
* Without this flag, configurations from all projects defined in the manifest are deployed.

Optional

### Additional configuration via environment variables

You can use environment variables to set additional configuration options.

#### Specify proxy server

In environments where access to Dynatrace API endpoints is only possible or allowed via a proxy server, the Dynatrace Monaco CLI provides an option to specify the address of your proxy server when running a command:

To do this, set the `HTTPS_PROXY` environment variable to the address of your proxy server.

```
# Linux or Mac OS



HTTPS_PROXY=localhost:5000



monaco deploy example.yaml



# Windows



$env:HTTPS_PROXY="localhost:5000"



monaco deploy example.yaml
```

## Download

The `download` command lets you download configurations from a Dynatrace environment as Dynatrace Monaco CLI files.

This command lets you:

* Back up existing Dynatrace configurations.
* Share (download and) Dynatrace configurations from one environment to another.
* Create blueprints/templates of Dynatrace configuration files from existing (UI-created) configurations.

Monaco can either:

* Download via a local manifest YAML file, in which the environment is specified.
* Download directly from a Dynatrace environment URL.

### Usage

```
monaco download [ARGS] [OPTIONS]
```

### Options

The available options depend on the download method.

#### Arguments to download via manifest

These arguments are used when you want to download via a manifest YAML file.

Argument

Description

Required

`--manifest <filepath>`, `-m <filepath>`

The path to the manifest file to use for connection information.

If not specified, Monaco searches for a file named `manifest.yaml` in the current directory.

Required

`--environment <name>`, `-e <name>`

Specify an environment defined in the manifest from which the configuration is to be downloaded.

Required

`--force`, `-f`

Used in combination with `--manifest`.
Force overwrites any existing `manifest.yaml` file.

Never append the source environment name to the project folder name.

Optional

#### Arguments to download via URL

These arguments are used when you want to download via the Dynatrace environment URL.

Argument

Description

Required

`--url <url>`

The URL of the Dynatrace environment from which to download the configuration.

This flag is mutually exclusive with `--manifest` or `--environment`.

Required

`--platform-token <environment variable name>`

The name of the environment variable that contains the Dynatrace platform token.

This is mutually exclusive with `--oauth-client-id` and `--oauth-client-secret`.

Required

`--token <environment variable name>`

The name of the environment variable that contains the API token (classic Dynatrace only).

Required

`--oauth-client-id <environment variable name>`

The name of the environment variable that contains the OAuth client ID.

This must be used together with `--oauth-client-secret`.
This is mutually exclusive with `--platform-token`.

Required

`--oauth-client-secret <environment-variable-name>`

The name of the environment variable that contains the OAuth client secret.

This must be used together with `--oauth-client-id`.
This is mutually exclusive with `--platform-token`.

Required

#### Options

These options can be used with either download method (whether via manifest or URL).

Option

Description

Required

`--output-folder <filepath>`, `-o <filepath>`

Specifies the name of the output folder in which downloaded configurations will be stored.

By default, the folder name will be `download` with the current timestamp appended.

Optional

`--project <name>`, `-p <name>`

The name of the project (which contains all downloaded configurations) that will be generated.

By default, the project name is `project`.

Optional

`--api <name>`, `-a <name>`

Download one or more classic Configuration APIs, including deprecated ones.
You can specify multiple APIs by repeating the flag, or by using comma-separated values.

Optional

`--settings-schema <name>`, `-s <name>`

Download Settings 2.0 objects for one or more Settings 2.0 schemas.
You can specify multiple APIs by repeating the flag, or by using comma-separated values.

Optional

`--only-apis`

Download only [classic Configuration APIs](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#API-type-field "This is a list of type fields in the Monaco configuration YAML file.").
Deprecated configuration APIs will not be included.

Optional

`--only-automation`

Download only [automation](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#automation-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

`--only-settings`

Download only [Settings 2.0](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.") configuration objects.

Optional

`--only-buckets`

Download only [bucket](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#bucket-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

`--only-documents`

Download only [document](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#document-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

`--only-openpipeline` Deprecated

Download only [openpipeline](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#openpipeline-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

`--only-segments`

Download only [segment](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#segment-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

`--only-slo-v2`

Download only [slo-v2](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#slo-v2-type-field "This is a list of type fields in the Monaco configuration YAML file.") configurations.

Optional

You can combine multiple `--only-<type>` flags in a single `monaco download` command to download several types at once.

### Additional configuration via environment variables

You can use environment variables to set additional configuration options.

#### Filtering of downloaded files

By default, certain configuration types or configuration objects are not included in a download.
This is because the Dynatrace API does not return full information from these configuration types.

* Typically, these types contain secrets that must not be exported, such as:

  + `aws-credentials`
  + `azure-credentials`
  + `kubernetes-credentials`
  + `credential-vault`
  + `extension`
* Read-only configurations are also excluded.

With Dynatrace Monaco CLI version 2.2.0+, you can deactivate this filtering.
To do so, set one of the environment variables as described in the table below.
Then, use `monaco download` to download the settings configuration.

| Environment variable | Description |
| --- | --- |
| `MONACO_FEAT_DOWNLOAD_FILTER` | Controls all download filtering. If set to `false`, no filters are applied, and all settings are downloaded. This supersedes all other environment variables. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS` | Controls Settings 2.0 download filtering. If set to `false`, all Settings 2.0 settings are downloaded without filtering. This supersedes the `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE` environment variables. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE` | Controls Settings 2.0 download filtering. If set to `false`, read-only settings are also downloaded. |
| `MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS` | Controls classic Configuration API type download filtering. If set to `false`, all classic Configuration API configurations are downloaded without filtering. |

While this lets you download a project, you won't be able to deploy it automatically.
Some manual post-processing will be needed.

```
# Linux or macOS



MONACO_FEAT_DOWNLOAD_FILTER=false



# MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS=false



# MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE=false



# MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS=false



monaco download



# Windows



$env:MONACO_FEAT_DOWNLOAD_FILTER="false"



# $env:MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS="false"



# $env:MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE="false"



# $env:MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS="false"



monaco download
```

#### Concurrent downloads

When downloading a configuration, Monaco makes multiple simultaneous API calls to ensure that large configuration sets are downloaded as quickly as possible.
By default, up to five concurrent requests are made.

If you need faster downloads, and your environment or network allows it, you can configure Monaco to make additional concurrent requests.
To do this, use the `MONACO_CONCURRENT_REQUESTS` environment variable set to the number of concurrent requests that you want to set.
For example, `MONACO_CONCURRENT_REQUESTS=15` enables up to 15 concurrent requests.

```
# Linux or Mac OS



MONACO_CONCURRENT_REQUESTS=15



monaco download



# Windows



$env:MONACO_CONCURRENT_REQUESTS="15"



monaco download
```

If you notice problems with downloading configurations, for example, if the internal network setup is throttling and dropping requests, reduce the number of concurrent requests.

#### Dependency resolution

A Dynatrace configuration may contain dependencies on other configurations.
Monaco resolves these dependencies automatically:

* The default resolver is run automatically as part of `monaco download`.
* A faster resolver is available with Monaco CLI version 2.0.2+.
  This speeds up the `monaco download` execution, but is resource intensive: it requires 16+ GB of RAM and several hundred GB of storage available as swap space.

To activate the fast resolver, set the environment variable `MONACO_FEAT_FAST_DEPENDENCY_RESOLVER` to `true`.

```
# Linux or Mac OS



MONACO_FEAT_FAST_DEPENDENCY_RESOLVER=true



monaco download



# Windows



$env:MONACO_FEAT_FAST_DEPENDENCY_RESOLVER="true"



monaco download
```

## Delete

The `delete` command is a convenient way to remove configurations from Dynatrace environments.

* Deleting long-lived configurations in production environments is not ideal, but sometimes it's necessary
* Clean up temporary configurations in development environments.

As input, the `delete` command requires two YAML files:

* The [manifest file](/docs/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") that specifies the relevant Dynatrace environments.
* The [deletefile](/docs/deliver/configuration-as-code/monaco/configuration#file-structure-for-direct-reference "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") that specifies the relevant configurations.

The deletefile itself is generated with `monaco generate deletefile`, see [Generate](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#generate-deletefile "How to use the Monaco CLI application, including arguments and options.").

### Usage

```
monaco delete [--manifest <file>] [--file <file>] [OPTIONS]
```

### Arguments

Argument

Description

Required

`--manifest <file>`, `-m <file>`

The manifest file that specifies the relevant Dynatrace environments.

If not specified, Monaco will look for the file named `manifest.yaml`.

Optional

`--file <file>`

The delete file that specifies the relevant configurations.

If not specified, Monaco will look for the file named `delete.yaml`.

Optional

Option

Description

Required

`--environment <name>`, `-e <name>`

The environment(s) from which the configurations should be deleted.
To delete from multiple environments in a single call, either repeat this flag or use comma-separated variables.

This flag is mutually exclusive with `--group`.
If neither `--group` nor `--environment` is present, all environments are used.

Optional

`--group <name>`, `-g <name>`

The environment group(s) from which the configurations should be deleted.
To delete from multiple groups in a single call, either repeat this flag or use comma-separated variables.

This flag is mutually exclusive with `--environment`.
If neither `--group` nor `--environment` is present, all environments are used.

Optional

## Generate

The `monaco generate` command lets you generate various auxiliary files, based on your configuration:

* Deletefile
* DOT graph
* JSON schema files

### Usage

```
monaco generate [ARGS] [OPTIONS]
```

### Arguments

Argument

Description

Supported from version

Required

`deletefile`

Generates a deletefile.

Dynatrace Monaco 2.6.0

Optional

`graph`

Generates a DOT representation of the dependencies between configurations defined in a manifest's projects.

The [DOT formatï»¿](https://graphviz.org/doc/info/lang.html) is a standardized text-based format for representing graphs.
You can create visual representations with tools such as Graphviz.

Dynatrace Monaco 2.6.0

Optional

`schema`

Creates JSON schema files for Monaco's YAML files, such as the manifest, configuration, and delete files.

Dynatrace Monaco 2.10.0

Optional

### Options

The available options depend on the specific argument that is used.

#### deletefile

These options are used with the `monaco generate deletefile` command.

Option

Description

Required

`--file <file>`

Specify the name of the generated delete file.
If a file of this name already exists, a timestamp is appended.
By default, the file is named `delete.yaml`.

Optional

`--output-folder <path>`, `-o <path>`

Specify the path/name of the output folder where the deletefile will be saved.

If not specified, the file is generated in the directory from which you run the command.

Optional

`--project <name>`, `-p <name>`

Specify the project(s) for which deletefile entries are generated.

If not specified, all projects in the manifest are used.

Optional

The `generate deletefile` command can't process configurations that contain references in their name field and will fail when encountering such configurations.

**Example of a problematic configuration:**

```
configs:



- id: appRule



config:



name:



configId: application



configType: application-web



property: name



type: reference



template: rule.json



skip: false



type:



api: app-detection-rule
```

**Workaround:** Create the delete file manually or update the generated file to set the configuration name without references. See the [delete file format](/docs/deliver/configuration-as-code/monaco/configuration#file-structure-for-direct-reference "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") for the correct syntax.

#### graph

These options are used with the `monaco generate graph` command.

Option

Description

Required

`--output-folder <path>`, `-o <path>`

Specify the path/name of the output folder where the graph will be saved.

If not specified, the file is generated in the directory from which you run the command.

Optional

`--environment <name>`, `-e <name>`

Generate dependency graphs for one or more environment(s) within your deployment manifest file.
To set multiple environments, either repeat this flag or separate them using a comma (`,`).

This flag is mutually exclusive with `--group`:

* If this flag is specified, graphs are generated for each specified environment.
* If neither `--group` nor `--environment` is present, all environments are used.

Optional

`--group <name>`, `-g <name>`

Generate dependency graphs for one or more specific [environment groups](/docs/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") within your deployment manifest file.
To set multiple groups, either repeat this flag or separate them using a comma (`,`).

This flag is mutually exclusive with `--environment`:

* If this flag is specified, graphs are generated for each environment within the specified groups.
* If neither `--group` nor `--environment` is present, all environments are used.

Optional

`--id-encoding [default,json]`

Starting with Dynatrace Monaco 2.12.0, you can choose the encoding format:

* The default string representation.
* JSON.

JSON encoding can be useful when processing generated DOT files automatically.

Optional

#### schema

These options are used with the `monaco generate schema` command.

Option

Description

Required

`--output-folder <filepath>`, `-o <filepath>`

Specifies the name of the output folder in which the JSON schema files will be saved.

If not specified, the files will be saved in a `./schemas/` directory, which is within the directory where you ran the command.

Optional

## Account

The `account` command is used for operations that affect Account Management resources.

### Usage

```
monaco account [ARGS] [OPTIONS]
```

### Arguments

Argument

Description

Required

`deploy`

Deploy Account Management resources.

Optional

`download`

Download Account Management resources.

Optional

`delete`

Delete Account Management resources.

Optional

### Options

The available options depend on the specific argument that is used.

#### deploy

These options are used with the `monaco account deploy` command.

Option

Description

Required

`--account <name>`, `-a <name>`

The account name to deploy to, as specified in the manifest file.

Optional

`--dry-run`, `-d`

Validate the structure of your manifest, projects, and configurations.
A dry run resolves all configuration parameters, but it can't verify if the Dynatrace APIs will accept the content.

Optional

`--manifest <file>`, `-m <file>`

The name of the manifest file.

If not specified, Monaco searches for the `./manifest.yaml` file in the folder where the command is executed from.

Optional

`--project <name>`, `-p <name>`

Specify one or more projects to be deployed.
To set multiple projects, either repeat this flag or separate them using a comma (`,`).

* If this flag is specified, configurations from the specified projects are deployed.
* Without this flag, configurations from all projects defined in the manifest are deployed.

Optional

#### download

These options are used with the `monaco account download` command.

##### Options to download via manifest

These options are used when you want to download via a manifest YAML file.

Option

Description

Required

`--manifest <file>`, `-m <file>`

The name of the manifest file.

If the file name is not specified, Monaco searches for the `./manifest.yaml` file in the folder where the command is executed from.

Optional

`--account <name>`, `-a <name>`

The account name(s) to download from, as specified in the manifest file.
To set multiple accounts, either repeat this flag or separate them using a comma (`,`).

* If this flag is specified, configurations from the specified accounts are downloaded.
* Without this flag, configurations from all projects defined in the manifest are downloaded.

Optional

`--force`, `-f`

Used in combination with `--manifest`.
Force overwrites any existing `manifest.yaml` file.

Optional

##### Options to download via UUID

These options are used when you want to download via a Dynatrace account UUID

Option

Description

Required

`--oauth-client-id <environment variable name>`

The name of the environment variable that contains the OAuth client ID.

Required

`--oauth-client-secret <environment-variable-name>`

The name of the environment variable that contains the OAuth client secret.

Required

`--uuid <account UUID>`, `-u <account UUID>`

Account UUID from which the account management resources should be downloaded.

You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client.

Required

##### Additional options

These options can be used with either download method (whether via manifest or UUID).

Option

Description

Required

`--output-folder <filepath>`, `-o <filepath>`

Specifies the name of the output folder in which downloaded configurations will be stored.

By default, the folder name will be `download` with the current timestamp appended.

Optional

#### delete

These options are used with the `monaco account delete` command.

Option

Description

Required

`--account <name>`, `-a <name>`

The account name(s) account whose resources should be deleted, as specified in the manifest file.
To set multiple accounts, either repeat this flag or separate them using a comma (`,`).

* If this flag is specified, configurations from the specified accounts are deleted.
* Without this flag, configurations from all projects defined in the manifest are deleted.

Optional

`--file <file>`

The delete file that specifies the relevant configurations.

If not specified, Monaco will look for the file named `delete.yaml`.

Optional

`--manifest <file>`, `-m <file>`

The manifest file that specifies the relevant Dynatrace environments.

If not specified, Monaco will look for the file named `manifest.yaml`.

Optional

##### Example

In this example, we delete a user, service user, group, policy, and boundary using respective entries in a `delete.yaml` file.

```
delete:



- type: user



email: the.user@dynatrace.com



- type: serviceUser



name: Monaco service user



- type: group



name: My Group



- type: policy



name: My Policy



level:



type: account



- type: boundary



name: My Boundary
```

## Global options

These options can be used with any `monaco` argument.
They are useful for troubleshooting any errors that you might encounter.

Option

Description

Required

`--support-archive`

Create a [support archive for troubleshooting](/docs/deliver/configuration-as-code/monaco/reference/logging#support-archive "Logging reference for Dynatrace Configuration as Code via Monaco").

Optional

`--verbose`, `-v`

Enable [verbose debugging logs](/docs/deliver/configuration-as-code/monaco/reference/logging "Logging reference for Dynatrace Configuration as Code via Monaco").

Optional


---


## Source: terraform-api-support-access-permission-handling.md


---
title: Terraform API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling
scraped: 2026-02-16T21:26:05.486160
---

# Terraform API support and access permission handling

# Terraform API support and access permission handling

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Nov 20, 2025

Dynatrace offers different options to authenticate API calls. The Dynatrace Terraform Provider supports the following authentication options.

* Platform tokens
* OAuth clients
* Access tokens (classic)

For more information about Identity and Access Management (IAM), including platform tokens, OAuth clients, and API tokens / access tokens classic, see [Tokens and OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Create platform tokens

[Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") can be used to authenticate API calls against Dynatrace.
These platform tokens are long-lived access tokens.
For the full list of supported platform token services, see [Available services for platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#available-services "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

The following code blocks show you how to define environment variables for your environment URL and platform token for Windows and Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_PLATFORM_TOKEN=<YOUR_PLATFORM_TOKEN>
```

## Create OAuth client

To create an OAuth client, follow the steps described in [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-oauth-client "Manage authentication and user permissions using OAuth clients.").

To ensure the OAuth client works as intended, verify that the service user's groups grant the same scopes as the OAuth client you have created for all environments you want to use it with.
For more details on controlling permissions, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

The Dynatrace Terraform Provider requests OAuth access tokens using your client credentials to make authenticated API calls.

The following code blocks show you how to define environment variables for your environment URL, authentication client, and secret for Windows and Linux.

Windows

Linux

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



set DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_CLIENT_ID=<YOUR_CLIENT_ID>



export DYNATRACE_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
```

## Create API access token

Use access tokens to authenticate Dynatrace Classic API calls.
For more information on how to use a Dynatrace API token, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

The following code blocks show you how to define environment variables for your environment URL and API token for Windows and Linux.

Windows SaaS Classic Dynatrace

Linux SaaS Classic Dynatrace

```
set DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



set DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

```
export DYNATRACE_ENV_URL=https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



export DYNATRACE_API_TOKEN=<YOUR_API_TOKEN>
```

## API coverage

The Dynatrace Terraform Provider contains most Dynatrace APIs. All supported resources are listed in the Dynatrace Terraform Provider documentation in the [Terraform Registryï»¿](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs).

Always consider the correct permission scopes that are needed for the selected API resources.
Information can be found at [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") and [the Dynatrace Terraform provider GitHub repositoryï»¿](https://github.com/dynatrace-oss/terraform-provider-dynatrace/blob/main/documentation/supported-resources.md).


---


## Source: terraform-cli-commands.md


---
title: Terraform CLI commands
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-cli-commands
scraped: 2026-02-16T21:24:36.897092
---

# Terraform CLI commands

# Terraform CLI commands

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Nov 10, 2025

Terraform CLI offers a wide variety of commands to manage your resources. In this section, we provide a high-level outline of the main commands. As these commands are not Terraform-related and not specifically for the Dynatrace Terraform provider, you can find details in the [Terraform documentationï»¿](https://developer.hashicorp.com/terraform/docs).

## Main Terraform commands

You can use the following native commands with the Dynatrace Terraform provider:

* `init`: Prepares your working directory for other commands.
* `validate`: Checks whether the configuration is valid.
* `plan`: Shows changes required by the current configuration.
* `apply`: Creates or updates the infrastructure.
* `destroy`: Destroys the previously created infrastructure.

Additionally, Dynatrace implements the following command specifically for the Dynatrace Terraform provider:

* `export`: Exports the existing Dynatrace resources from a given Dynatrace environment.
  [Terraform CLI examples](/docs/deliver/configuration-as-code/terraform/terraform-cli-commands#terraform-cli-examples "This is a list of Terraform CLI commands.") provides examples of how to use the `export` command.

## Export configuration from a Dynatrace environment using the Dynatrace Terraform Provider

In addition to Terraform's out-of-the-box functionality, the Dynatrace Terraform Provider can be executed as a standalone executable to export an existing configuration from a Dynatrace environment. This functionality provides an alternative to manually creating a Terraform configuration and an easy way to create templates based on an existing configuration.

When exporting resources, consider appropriate permission scopes for fetching the desired configuration items.

### Prerequisites

* [Install Terraform CLI and set up Configuration as Code via Terraform](/docs/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.") and make it available in your `PATH`.
* Create a [platform token or OAuth client](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.") with the correct access permissions.
  The correct permissions depends on which APIs you use.
  For more info, see the API documentation or [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Using the export utility

1. Define the environment variables to identify the Dynatrace tenant for configuration retrieval, according to the [API support and access permission handling](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").

   Optionally, set the environment variable `DYNATRACE_TARGET_FOLDER` to designate an output directory (export folder). If not set, the default directory `.configuration` is used.
2. Go to the Terraform Dynatrace Provider executable in the terminal. This executable isn't generic, such as `terraform.exe` or `./terraform`.

   Typically, you can find it in the `.terraform/providers/registry.terraform.io/dynatrace-oss/dynatrace/{provider_version}/{os_version}/terraform-provider-dynatrace_x.y.z/` directory.
3. Directly invoke the executable with the options you need. The export is an additional functionality; invoking the plugin directly is OK, and you can ignore the warning.

   Windows

   Linux

   ```
   terraform-provider-dynatrace.exe -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]'
   ```

   ```
   ./terraform-provider-dynatrace -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]'
   ```

### Commands

The `list-exclusions` command provides an overview of resources that won't get exported unless explicitly specified.
This does not perform an export.
It isn't intended to be used in conjunction with other options.

Windows

Linux

```
terraform-provider-dynatrace.exe -export -list-exclusions
```

```
./terraform-provider-dynatrace -export -list-exclusions
```

By default, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (`dynatrace_json_dashboard`) and other resources are excluded from the export unless the resource is directly specified. Use the `-list-exclusions` command for a complete list of the excluded resources.

### Options and flags

* `-ref`: Enable resources with data sources and dependencies.
* `-migrate`: Enable resources with dependencies, excluding data sources.
* `-import-state`: Initialize Terraform modules and import resources into the state.
* `-id`: Display commented id output in resource files.
* `-flat`: Store all resources directly within the target folder without a module structure.
* `-exclude`: Exclude specified resources from export.

## Example usage

The table below describes various use cases for the Dynatrace-specific `export` command, as well example commands to achieve the desired outcome.
For simplicity, only Linux examples are provided.

Use case

Example

Export all configurations without data sources/dependencies.

```
./terraform-provider-dynatrace -export
```

Export all configurations with data sources/dependencies and include commented IDs.

```
./terraform-provider-dynatrace -export -ref -id
```

Export all configurations with data sources/dependencies including specified resources in the exclusion list.

```
./terraform-provider-dynatrace -export -ref * dynatrace_document dynatrace_platform_slo
```

Export specific configuration.

```
./terraform-provider-dynatrace -export dynatrace_document dynatrace_platform_slo
```

Export specific configurations and their dependencies.

```
./terraform-provider-dynatrace -export -ref dynatrace_platform_slo dynatrace_automation_workflow
```

Export specific alerting profiles by their IDs.

```
./terraform-provider-dynatrace -export -ref dynatrace_automation_workflow=4f5942d4-3450-40a8-818f-c5faeb3563d0 dynatrace_automation_workflow=9c4b75f1-9a64-4b44-a8e4-149154fd5325
```

Export multiple resources including dependencies.

```
./terraform-provider-dynatrace -export -ref dynatrace_document dynatrace_automation_workflow=4f5942d4-3450-40a8-818f-c5faeb3563d0
```

Export all configurations and import them into the state.

```
./terraform-provider-dynatrace -export -import-state
```

Export all service-level objectives and import them into the state.

```
./terraform-provider-dynatrace -export -import-state dynatrace_platform_slo
```

Export all configurations except specified resources.

```
./terraform-provider-dynatrace -export -ref -exclude dynatrace_platform_slo dynatrace_automation_workflow
```

## Additional information

During a Terraform export, it's possible that certain files cannot be processed correctly.
These files are moved to the following directories in the export folder, see [Using the export utility](/docs/deliver/configuration-as-code/terraform/terraform-cli-commands#export "This is a list of Terraform CLI commands.").
The reasons are added as comments at the beginning of each file.

* `.flawed`: The files in this directory are either deprecated or require modifications.
* `.required_attention`: The files in this directory lack essential information for a Terraform to be applied.
  This may be due to sensitive data or instances where the files require additional attention.
  (For example, `dynatrace_credentials` confidential strings are not available via the API.)


---


## Source: terraform-tutorial-set-up-automated-notification.md


---
title: Configure automated notifications using Terraform and Configuration as Code
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/tutorials/terraform-tutorial-set-up-automated-notification
scraped: 2026-02-16T21:27:45.110164
---

# Configure automated notifications using Terraform and Configuration as Code

# Configure automated notifications using Terraform and Configuration as Code

* Latest Dynatrace
* Tutorial
* 2-min read
* Updated on Nov 05, 2025

This tutorial explains how to configure an event notification with the latest Dynatrace.

The notification consists of

* A [custom alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") configuration, which raises an alerting event if a certain conditions is met.
* A simple workflow that automatically sends an email when the alerting event is active.

## Prerequisites

* Terraform CLI with the Dynatrace provider installed and available under PATH.
  For more information, see [Install Terraform CLI and set up Configuration as Code via Terraform](/docs/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.").
* OAuth client or platform token with the following permissions.
  For more information, see [Create API access token](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling#terraform-api-setup "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").

  + View settings objects for schema (`settings:objects:read`)
  + Create settings objects for schema (`settings:objects:write`)
  + View workflows (`automation:workflows:read`)
  + Create and edit workflows (`automation:workflows:write`)

  The Terraform user needs to have all required permissions to run the run automated configurations such as custom alerts or workflows.
  Missing or wrong permission can lead to an unexpected behavior.

## What will you learn

You'll learn how to configure a [custom alert](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.") and a [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") with an email action.

## Steps

### Build Terraform configuration

To build a configuration for raising an event and a simple workflow for sending an email in case of a raised event

1. Inside your working directory, create a `main.tf` file with the content for selected resources.

   Show me the code to build a custom alert configuration and a workflow

   ```
   locals {



   event_name = "Authentication Service: High Response Time"



   }



   resource "dynatrace_davis_anomaly_detectors" "Authentication_Service_High_Response_Time" {



   enabled     = true



   source      = "Anomaly Detection"



   title       = "Authentication Service: High Response Time"



   description = "Raises an event if my service response time performance decreases"



   analyzer {



   name = "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer"



   input {



   analyzer_input_field {



   key   = "query"



   value =<<-EOT



   timeseries avg(dt.service.request.response_time), by:{dt.entity.service}



   | fieldsAdd name=entityName(dt.entity.service)



   | filter in(name, "AuthenticationService")



   EOT



   }



   analyzer_input_field {



   key   = "threshold"



   value = "3000000"



   }



   analyzer_input_field {



   key   = "alertCondition"



   value = "ABOVE"



   }



   analyzer_input_field {



   key   = "alertOnMissingData"



   value = "false"



   }



   analyzer_input_field {



   key   = "violatingSamples"



   value = "3"



   }



   analyzer_input_field {



   key   = "slidingWindow"



   value = "30"



   }



   analyzer_input_field {



   key   = "dealertingSamples"



   value = "15"



   }



   }



   }



   event_template {



   properties {



   property {



   key   = "dt.source_entity"



   value = "{dims:dt.entity.service}"



   }



   property {



   key   = "event.type"



   value = "PERFORMANCE_EVENT"



   }



   property {



   key   = "event.description"



   value =<<-EOT



   **Alert description** An anomaly was detected:



   An anomaly was detected on {metricname}. Within the sliding window, {violating_samples} violation samples were detected that were {alert_condition} the threshold of {threshold}.



   EOT



   }



   property {



   key   = "event.name"



   value = local.event_name



   }



   property {



   key   = "dt.owner"



   value = "myTeam"



   }



   }



   }



   execution_settings {



   }



   }



   resource "dynatrace_automation_workflow" "Authentication_Service_Email_Notification" {



   type          = "SIMPLE"



   private       = false



   title         = "Authentication Service: Email Notification"



   tasks {



   task {



   name        = "send_email"



   description = "Send email"



   action      = "dynatrace.email:send-email"



   input       = jsonencode({



   "bcc": [],



   "cc": [



   "otherteam@mycompany.com"



   ],



   "content": "{{event()[\"event.description\"]}}\nAn alert has been raised, impacting the service: \n\nDetails:\nStatus:             {{event()[\"event.status\"]}}\nId:                 {{event()[\"event.id\"]}}\nTime:               {{event()[\"timestamp\"]}}\nCategory:           {{event()[\"event.category\"]}}\nImpacted service:   {{event()[\"dt.entity.service.name\"]}}\nResponsible team:   {{event()[\"dt.owner\"]}},\n",



   "environmentUrl": "{{ environment().url }}",



   "executionId": "{{ execution().id }}",



   "subject": "Dynatrace Alert",



   "taskId": "{{ task().id }}",



   "to": [



   "myteam@mycompany.com"



   ]



   })



   position {



   x = 0



   y = 1



   }



   }



   }



   trigger {



   event {



   active = true



   config {



   davis_event {



   entity_tags_match = "all"



   names {



   name {



   name = local.event_name



   match = "equals"



   }



   }



   }



   }



   }



   }



   }
   ```

   This file contains the Terraform configurationâa set of resource blocks that define the configuration.

   If you want to try other resources, consider using the export utility to export existing configurations from your selected environment.
2. Open a terminal and set the environment variables for your environment URL and authentication credentials.
   The environment variable identifies which tenant you'll be pushing configurations to.
   For more information, see [Terraform API support and access permission handling](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").
3. In your working directory, run the `terraform plan` to generate an execution plan that provides a preview of the changes Terraform intends to make.

   Show me preview example

   ```
   Terraform used the selected providers to generate the following execution



   plan. Resource actions are indicated with the following symbols:



   + create



   Terraform will perform the following actions:



   # dynatrace_automation_workflow.Authentication_Service_Email_Notification will be created



   + resource "dynatrace_automation_workflow" "Authentication_Service_Email_Notification" {



   + id      = (known after apply)



   + private = false



   + title   = "Authentication Service: Email Notification"



   + type    = "SIMPLE"



   + tasks {



   + task {



   + action      = "dynatrace.email:send-email"



   + active      = true



   + description = "Send email"



   + input       = jsonencode(



   {



   + bcc            = []



   + cc             = [



   + "otherteam@mycompany.com",



   ]



   + content        = <<-EOT



   {{event()["event.description"]}}



   An alert has been raised, impacting the service:



   Details:



   Status:             {{event()["event.status"]}}



   Id:                 {{event()["event.id"]}}



   Time:               {{event()["timestamp"]}}



   Category:           {{event()["event.category"]}}



   Impacted service:   {{event()["dt.entity.service.name"]}}



   Responsible team:   {{event()["dt.owner"]}},



   EOT



   + environmentUrl = "{{ environment().url }}"



   + executionId    = "{{ execution().id }}"



   + subject        = "Dynatrace Alert"



   + taskId         = "{{ task().id }}"



   + to             = [



   + "myteam@mycompany.com",



   ]



   }



   )



   + name        = "send_email"



   # (4 unchanged attributes hidden)



   + position {



   + x = 0



   + y = 1



   }



   }



   }



   + trigger {



   + event {



   + active = true



   + config {



   + davis_event {



   + entity_tags_match = "all"



   + on_problem_close  = false



   + names {



   + name {



   + match = "equals"



   + name  = "Authentication Service: High Response Time"



   }



   }



   }



   }



   }



   }



   }



   # dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time will be created



   + resource "dynatrace_davis_anomaly_detectors" "Authentication_Service_High_Response_Time" {



   + description = "Raises an event if my service response time performance decreases"



   + enabled     = true



   + id          = (known after apply)



   + source      = "Anomaly Detection"



   + title       = "Authentication Service: High Response Time"



   + analyzer {



   + name = "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer"



   + input {



   + analyzer_input_field {



   + key   = "alertCondition"



   + value = "ABOVE"



   }



   + analyzer_input_field {



   + key   = "alertOnMissingData"



   + value = "false"



   }



   + analyzer_input_field {



   + key   = "dealertingSamples"



   + value = "15"



   }



   + analyzer_input_field {



   + key   = "query"



   + value = <<-EOT



   timeseries avg(dt.service.request.response_time), by:{dt.entity.service}



   | fieldsAdd name=entityName(dt.entity.service)



   | filter in(name, "AuthenticationService")



   EOT



   }



   + analyzer_input_field {



   + key   = "slidingWindow"



   + value = "30"



   }



   + analyzer_input_field {



   + key   = "threshold"



   + value = "3000000"



   }



   + analyzer_input_field {



   + key   = "violatingSamples"



   + value = "3"



   }



   }



   }



   + event_template {



   + properties {



   + property {



   + key   = "dt.source_entity"



   + value = "{dims:dt.entity.service}"



   }



   + property {



   + key   = "event.type"



   + value = "PERFORMANCE_EVENT"



   }



   + property {



   + key   = "event.description"



   + value = <<-EOT



   **Alert description** An anomaly was detected:



   An anomaly was detected on {metricname}. Within the sliding window, {violating_samples} violation samples were detected that were {alert_condition} the threshold of {threshold}.



   EOT



   }



   + property {



   + key   = "event.name"



   + value = "Authentication Service: High Response Time"



   }



   + property {



   + key   = "dt.owner"



   + value = "myTeam"



   }



   }



   }



   + execution_settings {}



   }



   Plan: 2 to add, 0 to change, 0 to destroy.
   ```
4. After verifying the plan, execute `terraform apply` to implement the proposed changes.

   Show me an example of completion

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creating...



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creating...



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Creation complete after 2s [id=************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Creation complete after 5s [id=************]



   Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
   ```

   A Terraform `terraform.tfstate` state file is automatically generated. It keeps track of the resources that Terraform manages.
   It's crucial for subsequent Terraform operations.

### Modify Terraform configuration

To modify the Terraform configuration

1. Execute the `terraform plan`, which should indicate that no changes are needed.

   Show me the execution log

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To make a change, edit the `main.tf file`. For instance, you can modify the email notification recipient by modifying the `to` attribute in the `dynatrace_davis_anomaly_detectors` resource.
3. After making your changes, execute terraform apply that will update the management zone configuration in Dynatrace and adjust the Terraform state file accordingly.

   Show me preview example

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifying... [id=************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Modifications complete after 3s [id=************]



   Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
   ```

### Delete your configuration

1. To remove a configuration, run `terraform plan` to confirm no pending changes.

   Show me the execution log

   ```
   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Refreshing state... [id=************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Refreshing state... [id=************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To permanently delete the selected configuration, execute `terraform destroy`.

   Show me the execution log

   ```
   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destroying... [id= ************]



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destroying... [id= ************]



   dynatrace_davis_anomaly_detectors.Authentication_Service_High_Response_Time: Destruction complete after 0s



   dynatrace_automation_workflow.Authentication_Service_Email_Notification: Destruction complete after 1s



   Destroy complete! Resources: 2 destroyed.
   ```

   The previously created configurations in the Dynatrace environment have been destroyed. Confirm that your Terraform state `terraform.tfstate` file is empty.


---


## Source: tutorials.md


---
title: Terraform tutorials overview
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/tutorials
scraped: 2026-02-15T21:28:13.613733
---

# Terraform tutorials overview

# Terraform tutorials overview

* Latest Dynatrace
* Explanation
* 1-min read
* Published Nov 03, 2025

Terraform is an extensive tool that you can combine with Configuration as Code to achieve great results.

We provide a tutorial to help you [Configure automated notifications using Terraform and Configuration as Code](/docs/deliver/configuration-as-code/terraform/tutorials/terraform-tutorial-set-up-automated-notification "Configure automated notifications using Terraform and Configuration as Code.").


---
