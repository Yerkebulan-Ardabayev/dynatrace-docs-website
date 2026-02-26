---
title: Work with Dynatrace Monaco CLI commands for Latest Dynatrace
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/reference/commands-saas
scraped: 2026-02-26T21:32:02.164148
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

### Options

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

#### Arguments to download via URL

These arguments are used when you want to download via the Dynatrace environment URL.

#### Options

These options can be used with either download method (whether via manifest or URL).

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

### Options

The available options depend on the specific argument that is used.

#### deletefile

These options are used with the `monaco generate deletefile` command.

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

#### schema

These options are used with the `monaco generate schema` command.

## Account

The `account` command is used for operations that affect Account Management resources.

### Usage

```
monaco account [ARGS] [OPTIONS]
```

### Arguments

### Options

The available options depend on the specific argument that is used.

#### deploy

These options are used with the `monaco account deploy` command.

#### download

These options are used with the `monaco account download` command.

##### Options to download via manifest

These options are used when you want to download via a manifest YAML file.

##### Options to download via UUID

These options are used when you want to download via a Dynatrace account UUID

##### Additional options

These options can be used with either download method (whether via manifest or UUID).

#### delete

These options are used with the `monaco account delete` command.

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