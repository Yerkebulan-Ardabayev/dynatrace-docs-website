---
title: Work with Dynatrace Monaco CLI commands for Latest Dynatrace
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/reference/commands-saas
scraped: 2026-02-17T21:29:03.337056
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