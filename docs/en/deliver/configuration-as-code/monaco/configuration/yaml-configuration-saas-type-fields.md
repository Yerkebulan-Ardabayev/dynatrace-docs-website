---
title: Monaco configuration YAML file - list of type fields
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields
scraped: 2026-02-17T05:10:53.325344
---

# Monaco configuration YAML file - list of type fields

# Monaco configuration YAML file - list of type fields

* Latest Dynatrace
* Reference
* 11-min read
* Updated on Jan 15, 2026

The [`type` field](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas#type-field "The Monaco configuration YAML file is structure.") in the `configs` YAML file defines the Dynatrace configuration type.

The list of `type` fields

* [`api`](#API-type-field)
* [`Settings`](#settings-type-field)
* [`Automation`](#automation-type-field)
* [`Bucket`](#bucket-type-field)
* [`Document`](#document-type-field)
* [`OpenPipeline`](#openpipeline-type-field)
* [`Segment`](#segment-type-field)
* [`SLO` (Service-level objective)](#slo-v2-type-field)
* [`Account configuration`](#accounts-type-field)

## api type field

The `type` field `api` can be defined as follows.

```
configs:



id: [...]



type:



api: synthetic-monitor



config:



[...]
```

or

```
configs:



id: [...]



type: synthetic-monitor



config:



[...]
```

For more information, see [supported API types](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling#supported-api-types "This is a list of the Monaco API support and access permission handling.").

Some of the `api` `type` configuration have a parent-child relationship with another configuration.
Such a configuration requires a scope field that points to the parent configuration.
Define `scope` as `value`, `reference`, or `environment`.

Because such configurations are made in the scope of their parent API, referencing the parent configuration's `id` is a useful way of configuring entities after they've been created via the Dynatrace Monaco CLI.

In the example below, a mobile application and related key-user actions are configured, and the `configs` `id` references the mobile application.

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



config:



name: myKeyUserAction



template: kua.json



skip: false



type:



api:



name: key-user-actions-mobile



scope:



type: reference



configType: application-mobile



configId: mobile-application-id



property: id
```

## settings type field

The [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") are defined by their `schema`, `scope`, and an optional `schemaVersion`.

The `type` field `settings` can be defined as follows.

```
configs:



id: [...]



type:



settings:



schema: builtin:davis.anomaly-detectors



schemaVersion: 1.0.2



scope: environment



config:



[...]
```

You can define the `scope` parameter as `value`, `reference`, or `environment`.
Setting the scope to `environment` allows the creation of a settings configuration for the entire Dynatrace environment.

A Dynatrace entity has many `settings` made, so referencing another `configs` `id` is a useful way of configuring entities after you've created them via the Dynatrace Monaco CLI.

In the example below, a web application is configured, and then the `settings` for this application are made.
The `rum.web.enablement` `settings` scope references the web application `MyApp`.

```
configs:



- id: MyAppId



type:



api: application-web



config:



name: My Sample Web Application



template: application.json



skip: false



- id: MyApp_RUMSettingsId



type:



settings:



schema: builtin:rum.web.enablement



scope:



type: reference



configType: application-web



configId: MyAppId



property: id



config:



name: MyApp_RUMSettings



template: rum-settings.json



skip: false
```

Another useful parameter is `insertAfter`.
This parameter enforces a specific ordering of single Settings 2.0 objects.

In the example below, if the `insertAfter` is set, Dynatrace Monaco ensures the settings object is deployed:

* For Dynatrace Monaco CLI version 2.14.0+ after the referenced one using the reference parameter.

  ```
  - id: mySecondAppDetectionRuleId



  config:



  parameters:



  [...]



  template: wed-detect-rule.json



  skip: false



  type:



  settings:



  schema: builtin:rum.web.app-detection



  schemaVersion: 2.1.1



  scope: environment



  insertAfter:



  configId: myFirstAppDetectionRuleId  # Monaco config id



  property: id                         # must be âidâ



  type: reference                      # must be âreferenceâ
  ```
* For Dynatrace Monaco CLI version 2.21.0+ after a specified configuration via a hardcoded ID using the value parameter

  ```
  type:



  settings:



  schema: builtin:rum.web.app-detection



  schemaVersion: 2.1.1



  scope: environment



  insertAfter:



  value: myFirstAppDetectionRuleId     # hardcoded config id



  type: value                          # must be âvalueâ
  ```
* For Dynatrace Monaco CLI version 2.21.0+ at the top or bottom of the list using the values front or back.

  ```
  type:



  settings:



  schema: builtin:rum.web.app-detection



  schemaVersion: 2.1.1



  scope: environment



  insertAfter: front       # âfrontâ puts the config on top of the list, âbackâ puts it at the bottom
  ```

* If multiple Monaco configurations or projects define front or back, it is not guaranteed which configuration is the first or last.
* Since Dynatrace Monaco deploys `configs` in parallel, we recommend that you add the `insertAfter` parameter to all `configs` to ensure that one config is placed at the top or bottom of the list.

Since Dynatrace Monaco CLI version 2.23.0+ specific Settings 2.0 objects allow the definition of a more granular permission scope to specify read or write access to single settings objects, using the `permissions` parameter.

The `permissions` parameter supports the `allUsers` field:

* `none`: only the owner (creator) of the settings object has full access to it, while other users have no access.
* `read`: owner (creator) has full access to the settings object, while other users, who have generic `settings:objects:read` permissions, only have read-only access.
* `write`: every user who has `settings:objects:read` and `settings:objects:write` permissions has full access, read and write, to the settings object.

An example is shown below.

```
configs:



- id: security-jira-connection



config:



name: 'Security: Jira Connection'



template: jira-connection.json



skip: false



parameters:



[â¦]



type:



settings:



schema: app:dynatrace.jira:connection



scope: environment



permissions:



allUsers: read
```

## automation type field

Since Dynatrace Monaco CLI version 2.6.0+, the `automation` type is supported.
The `automation` type configurations represent [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") related resources.

The `type` field `automation` can be defined as follows.

```
type:



automation:



resource: workflow # or business-calendar, or scheduling-rule
```

The `resource` field specifies the desired automation resource. Each resource requires distinct OAuth permissions.
For more information, see [Monaco API support and access permission handling](/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling#supported-api-types "This is a list of the Monaco API support and access permission handling.").

An example is shown below.

```
configs:



- id: myRemediationWorkflow



config:



name:



value: âHigh Prio Incident Remediationâ



parameters:



[...]



template: remediationWorkflow.json



skip: false



type:



automation:



resource: workflow
```

The automation API supports an `adminAccess` query parameter to fetch all available workflow resources on a given tenant.
If not used, only workflow resources are bound to the permissions of the user who created the OAuth client.

To use this parameter, the OAuth client needs to have the scope `automation:workflows:admin configured`.

To get the scope `automation:workflows:admin configured`

1. Create a custom policy that grants the `automation:workflows:admin` permissions using the following policy statement `ALLOW automation:workflows:admin`.
2. Bind it to a group.
3. Assign the user to that group.

By default, the Dynatrace Monaco CLI uses this flag when accessing the API.
If it fails, the operation is repeated without the flag, but you can only access the workflow created by your own user.

## bucket type field

Since Dynatrace Monaco CLI version 2.9.0+, the `bucket` type is supported, and it represents the configurations of the [data storage management in Grail with custom Grail buckets](/docs/platform/grail/organize-data#creating-new-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

The `type` field `bucket` can be defined as follows.

```
type: bucket
```

It does not require any additional fields.

In addition to defining and creating a new storage bucket, you need an additional bucket rule [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to specify what data is stored in it.

An example is shown below.

```
configs:



# this is the new custom bucket



- id: my-bucket-id



config:



name: My awesome bucket



template: bucket.json



parameters:



retention_days: 372



type: bucket



# this is a new setting to define the rule what data shall be stored in the previously defined custom Grail bucket



- id: log-bucket-rule



type:



settings:



schema: builtin:logmonitoring.log-buckets-rules



scope: environment



config:



name: My custom rule



template: log-bucket-rule.json



parameters:



phrase: My phrase to look for



bucket:



type: reference



configType: bucket



configId: my-bucket-id



property: id
```

### Bucket naming

If the `originObjectId` is set in the bucket configuration, it is used as the bucket name.
Otherwise, the bucket name is automatically generated from the project name and `config` `id` using the pattern `project_configId`.
This name serves as both the bucket name and its identifier.

By default, the bucket name is sanitized to ensure compatibility with Dynatrace naming requirements.

## document type field

Since Dynatrace Monaco CLI version 2.15.0+, the `document` type is supported, and it represents the [API for Dashboards and Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/document-api "Manage Dynatrace documents (such as dashboards and notebooks) via API.").

Since Dynatrace Monaco CLI version 2.18.0+, the `document` type also represents the `launchpad`.

Since Dynatrace Monaco CLI version 2.28.0+, the `document` type also supports an `id` field for user-defined IDs.

The `type` field `document` can be defined as follows.

```
type:



document:



kind: dashboard # other possible types: ânotebookâ or âlaunchpadâ



private: true # optional field specifying the visibility of the document



id: custom-document-id # optional field specifying a user-defined document ID
```

The optional field `private` specifies whether a document is not visible.
If not specified otherwise, the `document` is public by default, which means everyone with access permissions can see it.

The optional field `id` allows you to set a custom ID for the document.
If this field is set, a direct reference via `objectId` is needed
in the [deletefile](/docs/deliver/configuration-as-code/monaco/configuration#file-structure-for-direct-reference "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."), should you want to delete the document later.

If not specified, Monaco generates a custom ID. In both cases, user-defined and Monaco-generated, the custom ID is used to populate the `id` field on download.

Monaco does not download [Ready-made documents](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Use ready-made documents right out of the box.").

Depending on the userâs credentials, Monaco may not be able to redeploy all downloaded documents in certain situations.
This situation happens when documents are publicly accessible, but the Monaco user does not have ownership rights. In other words, the Monaco user does not own the document.
For more information on sharing documents or changing their owner, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."), or [Launchpads](/docs/discover-dynatrace/get-started/dynatrace-ui/launchpads "Build and manage custom start pages with launchpads.").

For more information, see [Configuration as code sample repoï»¿](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples)

## openpipeline type field

Deprecated

Since Dynatrace Monaco CLI version 2.15.0+, the `openpipeline` type is supported.
`openpipeline` configuration manages the data ingestion and processing of data from different sources.

The `type` field `openpipeline` can be defined as follows.

```
type:



openpipeline:



kind: bizevents # id of openpipeline configuration (for example, "bizevents", "events", "logs", "spans", or "metrics")
```

Deploying an `openpipeline` configuration overwrites the existing one of the same kind, causing any manual changes made in the web UI or other configurations managed by Monaco or Terraform to be lost.
To prevent data loss, ensure all configurations are defined within a single Monaco or Terraform configuration.

This resource is deprecated and has been moved to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**. For more information, see [OpenPipeline API](/docs/platform/openpipeline/reference/openpipeline-api "Configure OpenPipeline capabilities of ingest source, routing, and processing via API.").

The `kind` field specifies the `id` of a pre-existing `openpipeline` configuration.
Monaco can retrieve and update configurations, but can't create or delete new ones.

## segment type field

Since Dynatrace Monaco CLI version 2.19.0+, the `segment` type is supported.
[Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") are used to structure and filter data for tailored views in Dynatrace.

The `type` field `segment` can be defined as follows.

```
type: segment
```

It does not require further fields, but can be referenced in other configurations to filter visualized data accordingly.

An example is shown below.

```
configs:



- id: segment                # configures the desired segment



type: segment



config:



template: segment.json



- id: dashboard              # creates a dashboard that references a segment



type:



document:



kind: dashboard



private: true



config:



name: Log Dashboard with Dynatrace Segment



parameters:



segment_id:            # references the previously created segment within a dashboard



configId: segment



configType: segment



property: id



type: reference



template: dashboard.json
```

## `slo-v2` (Service-level objective) type field

Since Dynatrace Monaco CLI version 2.22.0+, the `slo-v2` type is supported.

[Configure and monitor service-level objectives with Dynatrace](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo "Create, configure, and monitor service-level objectives with Dynatrace."), based on Grail and utilizing DQL are managed via the `type` `slo-v2`.

The `slo-v2` configuration type is distinct from the existing `slo` type and represents SLOs leveraging Grail, as described in the [Configure and monitor service-level objectives with Dynatrace](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo "Create, configure, and monitor service-level objectives with Dynatrace.") overview.
These two configuration types are incompatible, and deploying a `slo` configuration as a `slo-v2` or vice versa results in the API rejecting the request.

The `type` field `slo-v2` can be defined as follows.

```
type: slo-v2
```

This type does not require additional fields.

An example is shown below.

```
configs:



- id: custom-sli          # An SLO based using a custom DQL query as SLI



type: slo-v2



config:



name: custom-sli



template: custom-sli.json



- id: sli-reference       # another SLO using an out-of-the-box template (aka reference)



type: slo-v2



config:



name: sli-reference



template: sli-reference.json
```

## accounts

To define the `accounts` for which Monaco configures Account Management resources, you need to create an accounts section in the configuration file.

The following example defines a single `accounts` object containing account-related information.
The `name` property specifies the account name, my-account, which can be referenced using the Monaco CLI command's `--account` flag.

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

### Account resources

Using Monaco, you can define `users`, `service users`, `groups`, and `policies` as dedicated types.

Unlike the usual environment-level configurations, no JSON template files are needed.
Monaco builds the required API data directly from your YAML configuration.

Account-level configuration is usually distinct from environment-level configuration.
It changes less frequently; existing commands like `monaco deploy` ignore any account configuration that may be defined in a manifest file.

A dedicated `monaco account deploy` command needs to be used instead.

The example shows how Monaco represents account management resources locally, with examples defining users, service users, groups, and policies.

```
users: # users define one or more users bound to different groups



- email: monaco@dynatrace.com



groups:



- Log viewer # default group



- type: reference



id: my-group



# id: specifies a custom group. The ID must match a group defined in groups. Custom groups need to be referenced (vs. default groups)



serviceUsers:     # supported with Monaco CLI v2.23.0+



- name: Monaco service user # name: must be unique. Otherwise, an originObjectId is needed



description: Description of service user



originObjectId: 3037325d-6475-4adf-a14d-93d1c862f9e9 # (optional) only needed if the userâs name is not unique



groups:



- Log viewer # default group



- type: reference # custom group my-group needs to be referenced



id: my-group



groups:



- name: My Group



id: my-group



description: This is my group



account: # specifies permissions and policies to which the group is bound on the account level.



permissions:



- account-viewer



policies:



- policy: Environment role - Access environment



environments: # specify the permissions and policies to which the group is bound on the environment/tenant level.



- environment: abc12345



permissions:



- tenant-viewer



policies:



- policy: Environment role - Replay session data without masking



- type: reference



id: my-policy



managementZones: # classic Dynatrace only



- environment: abc12345



managementZone: Management Zone 2000



permissions:



- tenant-viewer



policies: # defines one or more policies for the selected group



- name: My Policy



id: my-policy



level:



type: account



description: abcde



policy: |- # contains any policy rules of this particular policy.



ALLOW automation:workflows:read;
```

While this sample shows users, service users, policies, and groups defined in a single file, you can define them in individual files and structure your account resource projects and files as needed.

## Related topics

* [Monaco configuration YAML file structure](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas "The Monaco configuration YAML file is structure.")