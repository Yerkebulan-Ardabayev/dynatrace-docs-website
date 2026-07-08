---
title: Migrate configuration from Monaco 1.x to 2.x
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2
---

# Migrate configuration from Monaco 1.x to 2.x

# Migrate configuration from Monaco 1.x to 2.x

* How-to guide
* 9-min read
* Updated on May 08, 2023

The last Monaco version to support the `convert` command is Monaco version `2.19.0`.  
If you want to convert your project using the steps outlined on this page, download and use that version.

If you use Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI) 1.x, this section will guide you through migrating to version 2.x.

## Prerequisites

* Dynatrace Monaco CLI 2.0.0 - Monaco CLI 2.19.0 installed (see [Install Dynatrace Configuration as Code via Monaco](/managed/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.")) and available on your `PATH`.
* An existing Dynatrace Monaco CLI version 1.x project.
* A Dynatrace environment and permission to create access tokens.
* A Dynatrace pre-existing access token, or new access token with the required permissions for your Dynatrace Monaco CLI 1.x configuration.
  For more information on how to create access tokens, see [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
* If your Dynatrace Monaco CLI 1.x project still uses deprecated config types, you should migrate them before conversion: [Migrate deprecated configuration types](/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration "Migrate deprecated 1.x configuration types.")

### Sample project

This guide will help you convert your existing projects.

To illustrate the commands, we convert a project found in the samples in the [GitHub repository﻿](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples).

If you want to follow the exact commands of the guide, clone or download the repo and navigate into the `observability_clinic_sample` folder.

## Convert your project

Migrating existing Monaco 1.x projects is as simple as running the `convert` command.

For this sample, we assume that your existing configuration is located in a folder called `existing_v1_config`.

The content of this sample folder looks like this:

```
existing_v1_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



└── synthetic-monitor/



└── environments.yaml
```

To recap how things work in Monaco 1.x, this folder contains the following:

* A project folder called `project`
* The `project` folder contains configuration folders for `application-web`, `auto-tag`, `slo`, and `synthetic-monitor` configurations.

  + Each of these configuration folders contains a configuration YAML file and one or more JSON templates.
* The `environments.yaml` file defines the environments this configuration project is deployed to.

Linux/macOS

Windows

1. Open your preferred terminal.
2. Navigate to the directory above your configuration folder `/existing_v1_config`.
3. Run `monaco convert` using `environments.yaml` and the `existing_v1_config` folder.

   ```
   monaco convert existing_v1_config/environments.yaml existing_v1_config -o converted_config
   ```

   The `-o` flag allows defining the name of the converted output folder.
4. Inspect the `converted_config` that Monaco has created.

   ```
   ls existing_v1_config-v2
   ```

   It should look like this:

   ```
   converted_config/



   ├── project/



   ├── application-web/



   ├── auto-tag/



   ├── slo/



   └── synthetic-monitor/



   └── manifest.yaml
   ```

1. Open Windows PowerShell.
2. Navigate to the directory above your configuration folder `/existing_v1_config`.
3. Run `monaco convert` using `environments.yaml` and the `existing_v1_config` folder.

   ```
   monaco convert existing_v1_config/environments.yaml existing_v1_config -o converted_config
   ```

   The `-o` flag allows defining the name of the converted output folder .
4. Inspect the `converted_config` that Monaco has created.

   ```
   dir existing_v1_config-v2
   ```

   It should look like this:

   ```
   converted_config/



   ├── project/



   ├── application-web/



   ├── auto-tag/



   ├── slo/



   └── synthetic-monitor/



   └── manifest.yaml
   ```

## Differences between 1.x and 2.x

The main visible differences between versions 1.x and 2.x are the introduction of structured configuration.

Let's take a look at how the project has changed in detail.

### Project folder

On a folder level, your `environments.yaml` is replaced with a `manifest.yaml`.

Version 1.x

Version 2.x

```
existing_v1_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



└── synthetic-monitor/



└── environments.yaml
```

```
converted_config/



├── project/



├── application-web/



├── auto-tag/



├── slo/



└── synthetic-monitor/



└── manifest.yaml
```

### From `environments.yaml` to `manifest.yaml`

* Version 1.x defined projects as folders in the directory where the CLI is executed, while version 2.x introduces manifest files, which define projects (*what* is being deployed) as well as the environments previously defined in environment files (*where* these configurations are to be deployed).
* To indicate that the URL is loaded from an environment variable:

  + In version 1.x, we use the special templating prefix `.Env.`
  + In version 2.x, we use an explicit `type`

For more about manifest files, see [Monaco configuration overview](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").

Version 1.x

Version 2.x

```
environment1:



- name: "Sample Environment"



- env-url: {{ .Env.DEMO_ENV_URL }}



- env-token-name: "DEMO_ENV_ACCESS_TOKEN"
```

```
manifestVersion: "1.0"



projects:



- name: project



environmentGroups:



- name: default



environments:



- name: environment1



url:



type: environment



value: DEMO_ENV_URL



auth:



token:



name: DEMO_ENV_ACCESS_TOKEN
```

### Configuration

* Configuration YAML files in version 2.x change substantially compared to the simple key-value lists of version 1.x.
* JSON payload templates are unchanged between version 1.x and version 2.x.

Version 1.x

Version 2.x

```
config:



- slo: "slo.json"



slo:



- name: "My App's Availability SLO"



- metricName: "my_app_synthetic_availability"



- syntheticId: "/project/synthetic-monitor/AppAvailabilityMonitor.id"



- thresholdTarget: "99.98"



- thresholdWarning: "99.99"
```

Note how the `syntheticId` field defines a reference to a synthetic-monitor's ID in 1.x's string format.

```
configs:



- id: slo



config:



name: My App's Availability SLO



parameters:



metricName: my_app_synthetic_availability



syntheticId:



configId: AppAvailabilityMonitor



configType: synthetic-monitor



property: id



type: reference



thresholdTarget: "99.98"



thresholdWarning: "99.99"



template: slo.json



skip: false



type:



api: slo
```

As you can see, the `slo` configuration has changed substantially.

* There is now a config object with the ID `slo`, which defines all parameters as well as the JSON template file, rather than an initial ID to template pair `slo:slo.json`, followed by key-value pairs defining the configuration's parameters.
* Most significantly, the `syntheticId` field now is a structured field of type `reference`, explicitly defining the ID, type, and property it is referencing.

Note how the conversion has removed the `project` from the reference, which is redundant for references in the same project.

Conversion may include a few small improvements to your input configuration.

Finally, the configuration now has an explicit `type`. In version 2.x, types are defined by this value in the configuration YAML and are no longer based on the name of the file's folder.

#### Environment overrides

Similar to the other configuration changes, version 2.x makes the definition of environment overrides more explicit.

Version 1.x

Version 2.x

```
config:



- slo: "slo.json"



slo:



- name: "My App's Availability SLO"



- thresholdTarget: "99"



slo.dev-env:



- name: "My App's Availability SLO - on DEV stage"



- thresholdTarget: "99.999"
```

```
configs:



- id: slo



type:



api: slo



config:



name: My App's Availability SLO



parameters:



thresholdTarget: "99"



template: slo.json



environmentOverrides:



- environment: dev-env



override:



name: My App's Availability SLO - on DEV stage



parameters:



thresholdTarget: "99.999"
```

## Deploy your converted project

Now we deploy the newly converted project to the same environment already managed by the Dynatrace Monaco CLI.

Linux/macOS

Windows

1. Export your Dynatrace access token to your environment.
   Make sure your access token has the required permissions for your configuration (in this example, **Write configuration** (`WriteConfig`)).

   ```
   export DEMO_ENV_ACCESS_TOKEN=YourAccessTokenValue
   ```

   The environment variable name will be same as in your 1.x `environments.yaml` (for this sample project, it's `DEMO_ENV_ACCESS_TOKEN`).
2. Run `monaco deploy --dry-run` to make sure your configuration is syntactically valid and consistent.

   ```
   monaco  deploy --dry-run converted_config/manifest.yaml
   ```
3. If the dry run is successful, the Dynatrace Monaco CLI returns a message similar to the following:

   ```
   2023/02/09 16:57:13 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 16:57:13 INFO  Projects to be deployed:



   2023/02/09 16:57:13 INFO    - project



   2023/02/09 16:57:13 INFO  Environments to deploy to:



   2023/02/09 16:57:13 INFO    - environment1



   2023/02/09 16:57:13 INFO  Validating configurations for environment `environment1`...



   2023/02/09 16:57:13 INFO    Validating config project:application-web:myApp



   2023/02/09 16:57:13 INFO    Validating config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 16:57:13 INFO    Validating config project:slo:slo



   2023/02/09 16:57:13 INFO    Validating config project:auto-tag:application-tagging



   2023/02/09 16:57:13 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 16:57:13 INFO  Validation finished without errors
   ```
4. Use `monaco deploy` to deploy your converted configuration.

   ```
   monaco  deploy converted_config/manifest.yaml
   ```
5. If the deployment is successful, the Dynatrace Monaco CLI returns a message similar to the following:

   ```
   2023/02/09 17:05:28 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 17:05:28 INFO  Projects to be deployed:



   2023/02/09 17:05:28 INFO    - project



   2023/02/09 17:05:28 INFO  Environments to deploy to:



   2023/02/09 17:05:28 INFO    - environment1



   2023/02/09 17:05:28 INFO  Deploying configurations to environment `environment1`...



   2023/02/09 17:05:28 INFO    Deploying config project:application-web:myApp



   2023/02/09 17:05:29 INFO    Deploying config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 17:05:30 INFO    Deploying config project:slo:slo



   2023/02/09 17:05:30 INFO    Deploying config project:auto-tag:application-tagging



   2023/02/09 17:05:30 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 17:05:31 INFO  Deployment finished without errors
   ```
6. If you open your Dynatrace environment in your browser, you will find your configuration as before.

You are ready to extend your existing configurations using Dynatrace Configuration as Code via Monaco 2.x.

1. Export your Dynatrace access token to your environment.
   Make sure your access token has the required permissions for your configuration (in this example, **Write configuration** (`WriteConfig`)).

   ```
   $env:DEMO_ENV_ACCESS_TOKEN="YourTokenValue"
   ```

   The environment variable name will be the same as in your 1.x `environments.yaml` (for this sample project, it's `DEMO_ENV_ACCESS_TOKEN`).
2. Run `monaco deploy --dry-run` to make sure your configuration is syntactically valid and consistent.

   ```
   monaco  deploy --dry-run converted_config/manifest.yaml
   ```
3. If the dry run is successful, the Dynatrace Monaco CLI returns a message similar to the following:

   ```
   2023/02/09 16:57:13 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 16:57:13 INFO  Projects to be deployed:



   2023/02/09 16:57:13 INFO    - project



   2023/02/09 16:57:13 INFO  Environments to deploy to:



   2023/02/09 16:57:13 INFO    - environment1



   2023/02/09 16:57:13 INFO  Validating configurations for environment `environment1`...



   2023/02/09 16:57:13 INFO    Validating config project:application-web:myApp



   2023/02/09 16:57:13 INFO    Validating config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 16:57:13 INFO    Validating config project:slo:slo



   2023/02/09 16:57:13 INFO    Validating config project:auto-tag:application-tagging



   2023/02/09 16:57:13 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 16:57:13 INFO  Validation finished without errors
   ```
4. Use `monaco deploy` to deploy your converted configuration.

   ```
   monaco  deploy converted_config/manifest.yaml
   ```
5. If the deployment is successful, the Dynatrace Monaco CLI returns a message similar to the following:

   ```
   2023/02/09 17:05:28 INFO  Dynatrace Configuration as Code v2.0.0



   2023/02/09 17:05:28 INFO  Projects to be deployed:



   2023/02/09 17:05:28 INFO    - project



   2023/02/09 17:05:28 INFO  Environments to deploy to:



   2023/02/09 17:05:28 INFO    - environment1



   2023/02/09 17:05:28 INFO  Deploying configurations to environment `environment1`...



   2023/02/09 17:05:28 INFO    Deploying config project:application-web:myApp



   2023/02/09 17:05:29 INFO    Deploying config project:synthetic-monitor:AppAvailabilityMonitor



   2023/02/09 17:05:30 INFO    Deploying config project:slo:slo



   2023/02/09 17:05:30 INFO    Deploying config project:auto-tag:application-tagging



   2023/02/09 17:05:30 WARN  API for "auto-tag" is deprecated! Please consider migrating to "builtin:tags.auto-tagging"!



   2023/02/09 17:05:31 INFO  Deployment finished without errors
   ```
6. If you open your Dynatrace environment in your browser, you will find your configuration as before.

You are ready to extend your existing configurations using Dynatrace Monaco CLI 2.x.

## Related topics

* [Migrate deprecated configuration types](/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration "Migrate deprecated 1.x configuration types.")