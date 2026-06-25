---
title: Dynatrace Monaco CLI command reference
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/reference/commands
scraped: 2026-05-12T12:35:01.236249
---

# Dynatrace Monaco CLI command reference

# Dynatrace Monaco CLI command reference

* Reference
* 23-min read
* Updated on Nov 13, 2025

This command cheat sheet for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI) describes the basic commands for managing your configuration files.

## Deploy command

The `deploy` command deploys configurations to environments defined in a given [deployment manifest](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") file.

### Usage

`monaco deploy graph <manifest.yaml> [flags]`

#### Example

The most straightforward way to use `deploy` is to run it without any flags (command options) and pass the file name of your deployment manifest. This way, all configurations in the `project` section of the deployment manifest file are applied to all environments defined in the `environments` section of the file.

```
monaco deploy manifest.yaml
```

### Positional Arguments Required

| Argument | Description |
| --- | --- |
| `<manifest.yaml>` | The manifest file defining projects to deploy and the environments to deploy them to. |

### Flags Optional

| Flag | Description |
| --- | --- |
| `--continue-on-error`  or  `-c` | Proceed with deployment even if an error is encountered.  This can be used to ensure that all valid configurations are applied to your environments, even if other configurations are invalid or failed to deploy.  Using this flag might lead to follow-up errors for configurations that depend on each other. |
| `--dry-run`  or  `-d` | Validate configuration file structure without deploying them.  With this flag set, `monaco deploy` checks whether your templates are valid JSON and whether your configuration YAML files can be parsed and used.  A `dry-run` doesn't connect to Dynatrace and can't validate the content of JSON sent to Dynatrace. A deployment may still fail with HTTP 400 Bad Request errors after a successful `dry-run` if the content of a JSON template is incorrect. |
| `--environment <name>`  or  `-e <name>` | Apply your configurations to specific environments within your deployment manifest file. To set multiple environments, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--group`.  * If this flag is specified, configurations are deployed to each specified environment. * If neither `--group` nor `--environment` is present, all environments are used. |
| `--group <name>`  or  `-g <name>` | Apply your configurations to specific [environment groups](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") within your deployment manifest file. To set multiple groups, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--environment`.  * If this flag is specified, configurations are deployed to each environment within the specified groups. * If neither `--group` nor `--environment` is present, all environments are used. |
| `--project <name>`  or  `-p <name>` | Specify one or more projects to be deployed. To set multiple projects, either repeat this flag or separate them using a comma (`,`).  * If this flag is specified, configurations from the specified projects are deployed. * Without this flag, configurations from all projects defined in the manifest are deployed. |

### Proxy

In environments where access to Dynatrace API endpoints is only possible or allowed via a proxy server, the Dynatrace Monaco CLI provides an option to specify the address of your proxy server when running a command:

Linux/macOS

Windows

```
HTTPS_PROXY=localhost:5000 monaco deploy example.yaml
```

```
$env:HTTPS_PROXY="localhost:5000"



monaco deploy example.yaml
```

## Download command

The `download` command lets you download configurations from a Dynatrace environment as Dynatrace Monaco CLI files. Use this feature to avoid starting from scratch when using the Dynatrace Monaco CLI.

### Usage

There are two ways to define the connection to the Dynatrace environment to download from - either by using a manifest file, or by defining the required values to connect directly using CLI flags.

`monaco download [connection flags] [flags]`

Help

Use the `--help` flag to view all options:

```
monaco download --help
```

#### Using the manifest

1. [Create a manifest file](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") if you don't have one already.
2. Run the Dynatrace Monaco CLI using the `download` command:

   ```
   monaco download --manifest your-manifest.yaml --environment environment-name
   ```

   If you named your manifest file the default `manifest.yaml`, you can omit the `manifest` flag:

   ```
   monaco download --environment environment-name
   ```

##### Connection Flags Required

| Flag | Description |
| --- | --- |
| `--manifest <filepath>`  or  `-m <filepath>` | Path to the manifest file to use for connection information.  Default: `manifest.yaml` in the current folder. |
| `--environment <name>`  or  `-e <name>` | Specify an environment defined in the manifest to download configurations from. |

#### Direct download

You can use command flags to download an environment directly without using a manifest.

Authentication

Authentication secrets are always loaded from environment variables, so you need to supply the name of a variable, not the actual secrets, when using the `--token` flag.

In the example, the environment variable is named `ACCESS_TOKEN_ENV_VAR`.

The same variable name will be used for the manifest that downloading will create for you.

The `monaco download --url https://env.dynatrace.com --token ACCESS_TOKEN_ENV_VAR` command will get you started and create a manifest.

After a direct download, you have everything you need to `deploy` your downloaded configuration.

##### Connection Flags Required

| Flag | Description |
| --- | --- |
| `--url <url>` | URL of the Dynatrace environment from which to download the configuration.  To be able to connect to any Dynatrace environment, an access token needs to be provided using `--token`.  This flag is mutually exclusive with `--manifest` or `--environment`. |
| `--token <environment variable name>` | Access token environment variable. Required when using the flag `--url` |

### Flags Optional

In addition to the connection flags described above, several options exist that apply to both manifest-based and direct downloads.

| Flag | Description |
| --- | --- |
| `--output-folder <filepath>`  or  `-o <filepath>` | Specify the name of the output folder in which downloaded configurations will be stored.  Default: a new folder will be created with the name 'download' and the current timestamp |
| `--project <name>`  or  `-p <name>` | The name of the project that will be generated containing all downloaded configurations.  Default: `project` |
| `--api <name>`  or  `-a <name>` | Download one or more classic configuration APIs, including deprecated ones. (Repeat flag or use comma-separated values) |
| `--settings-schema <name>`  or  `-s <name>` | Download settings 2.0 objects of one or more settings 2.0 schemas. (Repeat flag or use comma-separated values) |
| `--only-apis` | Download only classic configuration APIs. Deprecated configuration APIs will not be included. |
| `--only-settings` | Download only Settings 2.0 configuration objects. Classic configuration APIs will not be included. |
| `--force`  or  `-f` | Force overwrite any existing `manifest.yaml`, rather than creating an additional manifest\_{timestamp}.yaml.  In case of [manifest-based download](/managed/deliver/configuration-as-code/monaco/reference/commands#dowload-manifest "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)"): Never append the source environment name to the project folder name. |

### Filtering

The `download` command filters out several configurations by default.

Filtering possibilities range from excluding a configuration type completely to just excluding specific configuration objects.

Some types are excluded because the Dynatrace API does not return full information from them.
Generally, these types contain secrets that can never be exported after creation:

* `aws-credentials`
* `azure-credentials`
* `kubernetes-credentials`
* `credential-vault`
* `extension`

Specific configuration objects are filtered out if they are read-only configurations that can't be modified.

#### Deactivate filters

Dynatrace Monaco CLI version 2.2.0+

It's possible to deactivate filtering if you want to `download` everything. Keep in mind that such a `download` results in a project that can't be `deployed` directly and that requires manual post-processing.

Filters can be controlled by the following environment variable flags:

| Environment variable | Description |
| --- | --- |
| `MONACO_FEAT_DOWNLOAD_FILTER` | Controls all download filtering. If set to `false`, no filters are applied. This supersedes all other filtering flags. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS` | Controls Settings 2.0 download filtering. If set to `false`, all settings are downloaded without filtering. This supersedes the `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE` flag. |
| `MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE` | Controls Settings 2.0 download filtering. If set to `false`, settings that are marked as `unmodifiable` by the API are downloaded. |
| `MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS` | Controls classic [Config API type](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco") download filtering. If set to `false`, all Config API configurations are downloaded without filtering. |

For example, assume we want to `download` all classic Config API types without filtering and also include unmodifiable Settings 2.0 objects.
We can do this by setting two environment variables:

Linux/macOS

Windows

```
export MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS=false



export MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE=false



monaco download [flags]
```

```
$env:MONACO_FEAT_DOWNLOAD_FILTER_CLASSIC_CONFIGS=false



$env:MONACO_FEAT_DOWNLOAD_FILTER_SETTINGS_UNMODIFIABLE=false



monaco download [flags]
```

### Concurrent downloads

To ensure that large configuration sets are downloaded as quickly as possible, the `download` command makes several simultaneous API calls to Dynatrace.

You can set a `MONACO_CONCURRENT_REQUESTS` environment variable to configure various values for concurrent requests:

Linux/macOS

Windows

```
MONACO_CONCURRENT_REQUESTS=15 monaco download [flags]
```

```
$env:MONACO_CONCURRENT_REQUESTS=15



monaco download [flags]
```

By default, no more than five concurrent requests to Dynatrace are made. If you need faster downloads and your environment or network setup allows it, you can increase the number of concurrent requests.

If you notice problems with downloading configurationsâfor example, if the internal network setup is throttling and dropping requestsâreduce the number of concurrent requests.

### Dependency resolution

When downloading, the Dynatrace Monaco CLI resolves references between configurations to ensure that they can be re-uploaded in the correct order. To achieve this, all downloaded JSON templates are parsed and searched for the identifiers of all configurations.

The default version of dependency resolution is CPU intensive and can be slow if run on hardware or containers with limited CPU resources.

Monaco CLI version 2.0.2+ A fast resolver is available to speed this up, which trades off CPU requirements for an increased memory need. To activate it:

1. Make sure the machine has at least 16â32 GB of RAM and several hundred GB of storage available as swap space.
2. Set the `MONACO_FEAT_FAST_DEPENDENCY_RESOLVER` environment variable to `true`.

   Linux/macOS

   Windows

   ```
   MONACO_FEAT_FAST_DEPENDENCY_RESOLVER=true monaco download [flags]
   ```

   ```
   $env:MONACO_FEAT_FAST_DEPENDENCY_RESOLVER=true



   monaco download [flags]
   ```

## Delete command

The `delete` command is a convenient way to remove configurations from Dynatrace environments.

Ideally, you will not want to delete long-lived configurations in your production environments, but sometimes it's necessary.

The Dynatrace Monaco CLI is also sometimes used to manage ephemeral configurations in development environments, in which case you can easily use Monaco to clean up those temporary configurations.

### Usage

`monaco delete [--manifest manifest.yaml] [--file delete.yaml] [FLAGS]`

The delete command requires two YAML files:

* A manifest file that contains the list of Dynatrace environments from which to remove configuration
* A delete file that defines which configurations are to be removed

If you don't specify file names, the command tries to find a `manifest.yaml` and a `delete.yaml` file in the current folder.

#### Example

Suppose we have a [deployment manifest](/managed/deliver/configuration-as-code/monaco/configuration#deployment-manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") file called `deployment-file.yaml` with the structure below:

```
projects:



- name: infrastructure



path: infrastructure



environments:



- group: development



entries:



- name: development



url:



type: value



value: "https://mytenant.live.dynatrace.com"



auth:



token:



name: "TestIt"
```

And we have a `delete.yaml` file with the following structure:

```
delete:



- type: java-service



name: my-java-service-config
```

The following delete command will remove the `my-java-service-config` configuration within the `infrastructure` project from the development environment:

```
monaco delete --manifest deployment-file.yaml --file delete.yaml
```

### Flags Optional

| Flag | Description |
| --- | --- |
| `--manifest <filepath>`  or  `-m <filepath>` | Delete configurations from environments defined in a specific manifest file.  Default: `manifest.yaml` in the current folder. |
| `--file <filepath>` | Delete configurations defined in a specific [delete file](/managed/deliver/configuration-as-code/monaco/reference/commands#delete-yaml "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)").  Default: `delete.yaml` in the current folder. |
| `--environment <name>`  or  `-e <name>` | Specify one or more environments that configurations are deleted from. To set multiple environments, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--group`.  * If neither `--group` nor `--environment` is present, all environments are used. |
| `--group <name>`  or  `-g <name>` | Specify one or more [environment groups](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") that configurations are deleted from. To set multiple groups, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--environment`.  * If neither `--group` nor `--environment` is present, all environments are used. |

### Delete file `delete.yaml`

A delete file, by default named `delete.yaml`, is a YAML document that lists the configurations that to be deleted by the delete command.

Each entry can reference a configuration **directly** via its Dynatrace object ID, or **indirectly** via coordinates.

Only objects created by or onboarded to Monaco can be deleted by indirectly referencing them via coordinates.

If you have downloaded existing configurations and you want to delete them using this method, you need to first deploy the downloaded project at least once to make sure these objects can be found for deletion.

A delete file may not contain entries for `dashboard-share-settings` or `openpipeline` configurations. These configurations can't be deleted.

#### Direct reference entry

To reference directly, `type` and `objectId` must be defined, where `type` specifies the type of the config, and `objectId` is the ID of the configuration from Dynatrace.

```
- type: management-zone



objectId: origin-object-ID
```

#### Indirect reference entry

Depending on the [type of configuration](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type "Learn how to set up your Monaco YAML configuration."), the indirect reference differs slightly.

* [Type API](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-config-api "Learn how to set up your Monaco YAML configuration.")

  To create an API entry define the following:

  + `name`: the name of the configuration
  + `type`: one of [supported API types](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco")

  ```
  - name: my-mz



  type: management-zone
  ```
* [Type Settings](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-setting "Learn how to set up your Monaco YAML configuration.")

  To create a Settings entry, define the following:

  + `project`: the project name of the configuration
  + `id`: the ID of the configuration entry inside the `config.yaml` file
  + `type`: one of the [Settings 2.0 schema](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#settings "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco") IDs

  ```
  - project:  my-project



  id:       my-auto-tag



  type:     builtin:auto.tagging
  ```
* [Type Automation](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-automation "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI version 2.6.0+

  To create an Automation entry, define the following:

  + `project`: the project name of the configuration
  + `type`: one of the following values: `workflow`, `scheduling-rule` or `business-calendar`
  + `id`: the ID of the config entry inside the `config.yaml`file

  ```
  - project: my-project



  type:    workflow



  id:      my-workflow
  ```
* [Type Bucket](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-bucket "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI version 2.9.0+

  To create a Bucket entry, define the following:

  + `project`: the project name of the configuration
  + `type`: is set to `bucket`
  + `id`: the ID of the config entry inside the `config.yaml`file

  ```
  - project: my-project



  type:    bucket



  id:      my-bucket
  ```
* [Type Document](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-document "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI version 2.15.0+

  To create a Document entry, define the following:

  + `project`: the project name of the configuration
  + `type`: is set to `document`
  + `id`: the ID of the config entry inside the `config.yaml`file

  ```
  - project: my-project



  type: document



  id: monaco-config-id
  ```

* Using an indirect reference entry, Monaco can only delete documents originally created by it. Use a direct reference entry to delete documents created through other means.

* [Type Segment](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-segment "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI version 2.19.0+

  To create a Segment entry, define the following:

  + `project`: the project name of the configuration
  + `type`: is set to `segment`
  + `id`: the ID of the config entry inside the `config.yaml`file

  ```
  - project: my-project



  type:    segment



  id:      my-segment
  ```
* [Type Service-Level Objective (SLO)](/managed/deliver/configuration-as-code/monaco/configuration/yaml-configuration#type-service-level-objective-slo "Learn how to set up your Monaco YAML configuration.")

  Dynatrace Monaco CLI version 2.22.0+

  To create a Service-Level Objective (SLO) entry, define the following:

  + `project`: the project name of the configuration
  + `type`: is set to `slo-v2`
  + `id`: the ID of the config entry inside the `config.yaml`file

  ```
  - project: my-project



  type:    slo-v2



  id:      my-slo
  ```

#### Deprecated shorthand syntax Deprecated

Monaco currently still supports an alternate syntax for delete file entries:

```
delete:



- <api/name> OR <schema/config-id>



- â¦
```

However, be aware that this syntax is deprecated and will no longer be supported in future releases. We recommend that you use the more structured format above.

## Generate commands

The `monaco generate` command offers several sub-commands that allow you to generate auxiliary files from your configuration.

### Generate delete file

Dynatrace Monaco CLI version 2.6.0+

The `monaco generate deletefile` command creates a delete configuration file for use with the [delete command](/managed/deliver/configuration-as-code/monaco/reference/commands#delete "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)").

#### Usage

`monaco generate deletefile <manifest.yaml> [flags]`

##### Example

```
monaco generate deletefile my_manifest.yaml -o deletefiles --file my-projects-delete-file.yaml -p my_project
```

#### Positional Arguments Required

| Argument | Description |
| --- | --- |
| `<manifest.yaml>` | The manifest file for which a delete file is generated. An entry will be generated for each configuration defined in the manifest's projects. |

#### Flags Optional

| Flag | Description |
| --- | --- |
| `--file <filepath>` | Specify the name of the generated delete file. If a file of this name already exists, a timestamp is appended (default: `delete.yaml`). |
| `--output-folder <filepath>`  or  `-o <filepath>` | Specify the name of the output folder in which the delete file will be generated.  Default: the file is generated in the directory in which you run the command. |
| `--project <name>`  or  `-p <name>` | Specify one or more projects for which to generate delete file entries. If not defined, all projects in the manifest are used. |

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

**Workaround:** Create the delete file manually or update the generated file to set the configuration name without references. See the [delete file format](/managed/deliver/configuration-as-code/monaco/reference/commands#delete-yaml "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)") for the correct syntax.

### Generate dependency graph DOT file

Dynatrace Monaco CLI version 2.6.0+

The `monaco generate graph` command creates DOT representations of the dependencies between configurations defined in a given manifest's projects.

The [DOT formatï»¿](https://dt-url.net/oo0365m) is a standardized text-based format for representing graphs. You can create visual representations with tools such as [Graphvizï»¿](https://dt-url.net/zg2369w).

#### Usage

`monaco generate graph <manifest.yaml> [flags]`

##### Example

```
monaco generate graph manifest.yaml -e dev-environment -o mygraphs_folder
```

#### Positional Arguments Required

| Argument | Description |
| --- | --- |
| `<manifest.yaml>` | The manifest file for which dependency graphs are generated. One DOT file is generated per environment for all configurations defined in the manifest's project. |

#### Flags Optional

| Flag | Description |
| --- | --- |
| `--output-folder <filepath>`  or  `-o <filepath>` | Specify the name of the output folder in which to generate the DOT graph files.  Default: the file is generated in the directory in which you run the command. |
| `--environment <name>`  or  `-e <name>` | Specify one or more environments that should be used for creating dependency graphs. To set multiple environments, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--group`.  * If this flag is specified, a dependency graph is generated for each specified environment. * If neither `--group` nor `--environment` is present, all environments are used. |
| `--group <name>`  or  `-g <name>` | Specify one or more [environment groups](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") to use for creating dependency graphs. To set multiple groups, either repeat this flag or separate them using a comma (`,`).  This flag is mutually exclusive with `--environment`.  * If this flag is specified, a dependency graph is generated for each environment within the specified groups. * If neither `--group` nor `--environment` is present, all environments are used. |
| `--id-encoding [default,json]` | Dynatrace Monaco CLI version 2.12.0+  Set to `json` to generate a DOT file encoding each node's coordinate as JSON, instead of the `default` string representation.  JSON encoding can be useful when processing generated DOT files automatically. |

### Generate JSON schemas for YAML files

Dynatrace Monaco CLI version 2.10.0+

The `monaco generate schemas` command creates [JSON schemaï»¿](https://json-schema.org/) files for Monaco's YAML files such as the manifest, configuration, and delete files.

These schema files can be integrated with most common IDEs and advanced editors directly or by using free plugins.

#### Usage

`monaco generate schemas [flags]`

##### Example

```
monaco generate schemas -o monaco_schema_folder
```

#### Using generated schema files with Visual Studio Code

Below we describe one recommended usage example using [Visual Studio Codeï»¿](https://code.visualstudio.com/).

If you're using a different editor or IDE, follow the respective documentation for registering JSON schemas in your tool of choice.

Prerequisites:

* Monaco JSON schema files are generated, and the file paths are known
* The latest version of [Visual Studio Codeï»¿](https://code.visualstudio.com/) for your operating system is installed
* The [YAML extensionï»¿](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) is installed in Visual Studio Code

Once the YAML extension is installed, you can associate specific schemas with Monaco files.

For general information on configuring the YAML extension, see the [extension documentationï»¿](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml#associating-schemas).

We recommend the following configuration entry in your Visual Studio Code `settings.json`:

```
"yaml.schemas": {



"file:///<path-to-your-schema-folder>/monaco-config.schema.json": "**/*config*.yaml",



"file:///<path-to-your-schema-folder>/monaco-manifest.schema.json": "**/*manifest*.yaml",



"file:///<path-to-your-schema-folder>/monaco-delete-file.schema.json": "**/*delete*.yaml"



}
```

In the example configuration above:

* You need to replace `<path-to-your-schema-folder>` with the path to the generated folder. We recommend using absolute paths.
* We assume you follow the naming patterns that are used in this documentation and the generated files. If you use different naming patterns for your manifest, config, or delete YAML files, you need to adapt the configuration accordingly.

Update the schemas

Because the format of manifest or configuration files may change between versions, regenerate the schema definitions with the current version of Monaco.

#### Flags Optional

| Flag | Description |
| --- | --- |
| `--output-folder <filepath>`  or  `-o <filepath>` | Specify the name of the output folder in which to generate the JSON schema files.  Default: the files are generated in a `schemas/` directory under the directory in which you run the command. |

## Global Flags Optional

The following optional flags can be used with all commands.

| Flags | Description |
| --- | --- |
| `--support-archive` | Create a [support archive](/managed/deliver/configuration-as-code/monaco/reference/logging#support-archive "Logging reference for Dynatrace Configuration as Code via Monaco"). |
| `--verbose`  or  `-v` | Enable [verbose debug logs](/managed/deliver/configuration-as-code/monaco/reference/logging#timestamps "Logging reference for Dynatrace Configuration as Code via Monaco"). |