---
title: Monaco configuration overview
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration
---

# Monaco configuration overview

# Monaco configuration overview

* Overview
* 5-min read
* Updated on Feb 19, 2026

Configuration as Code via Monaco is made up of a set of projects and a deployment manifest.

## projects

Projects are directories (folders) used to logically group API configurations together. An example of a project could be a service where all configurations regarding this service are present in the folder. Projects can consist of multiple files and directories. For more information, see [Manage a Monaco project](/managed/deliver/configuration-as-code/monaco/configuration/projects "Manage a project folder with Dynatrace Configuration as Code via Monaco.").

## Deployment manifest

Deployment manifests are YAML files that tell the Dynatrace Monaco CLI what projects to deploy and exactly where they should be deployed. For the Dynatrace Monaco CLI to know what to deploy, there has to be a manifest file present.

This file provides details on what to deploy and where to deploy it.

The manifest is saved as a YAML file. It has three top-level keys: `manifestVersion`, `projects`, and `environmentGroups`.

A sample `manifest.yaml` might look like this:

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



- name: test-env-2



url:



value: https://<YOUR-DT-SPRINT-ENV-ID>.apps.dynatrace.com



auth:



token:



name: SPRINT_TOKEN



- name: prod



environments:



- name: prod-env-1



url:



type: environment



value: https://<YOUR-DT-PROD-ENV-ID>.apps.dynatrace.com



auth:



token:



name: PROD_TOKEN
```

The following sections describe each configuration key in detail.

### Version

A manifest must contain a `manifestVersion` as a top-level key. This is a simple string that is used to validate if the currently used version of Monaco can correctly parse the manifest.

Currently, the supported manifest version is `1.0`. The release notes will contain details if the manifest is extended and newer versions are released.

### Project definitions

All entries under the `projects` top-level key specify projects to deploy by Monaco. To specify the `type` of a project, provide the `type` key in the project item. There are currently two project types:

* `simple`
* `grouping`

#### Simple projects

This is the default type. All you need to provide is the `name` and `path` properties. If no `path` property is provided, the `name` will be used as the `path`.

* A `name` can not contain any slash character (`/` or `\`). This explicitly distinguishes it from filesystem paths.
* A `path` must always use a forward slash (`/`) as a separator, regardless of the operating system you use (Linux, Windows, Mac). For example:

```
projects:



- name: infra



path: shared/infrastructure
```

#### Grouping projects

Grouping projects offer a simplified way of grouping multiple projects together. The difference between a grouping project and a simple project is that a grouping project will load all sub-folders of a given path as simple projects. You have to specify a name, which will then be used as a prefix for the resulting simple projects. A dot (`.`) will be used as separator.

For example, given the following file structure:

```
general/



├── infrastructure/



└── zones/
```

The following project definition:

```
projects:



- name: general



path: general



type: grouping
```

will yield two projects:

* `general.infrastructure`
* `general.zones`

### Environment groups

If projects are the *what*, environments are the *where* configuration for the Dynatrace Monaco CLI.
[Consider this sample manifest.yaml example](/managed/deliver/configuration-as-code/monaco/configuration#manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").
As you can see, every environment has to be part of a group and can only be present in one group.

Environment groups are a mechanism allowing you to target specific environments together when deploying or to overwrite configuration properties for several environments with one override rather than one per environment.

It can be helpful to group and differentiate pre-production and production environments, as shown in the example.

### Environment definition

An environment definition consists of three parts: `name`, `url`, and `auth`.

* The `name` identifies the environment for monaco. It's a freeform string, but it must be unique.
* The `url` section specifies the URL of the Dynatrace environment.
* The `auth` section specifies how to authenticate against the Dynatrace API.

#### Environment URL

The `url` definition consists of a `type` and a `value` field.

You can either specify the environment's URL directly in the manifest as a value:

```
url:



type: value



value: https://{environment-specific-domain}
```

or as an environment variable to load the URL from:

```
url:



type: environment



value: YOUR_URL_ENV_VAR
```

##### Access token authentication

Access tokens for the Dynatrace Monaco CLI always require at least the following permission to query general information about your environment:

* **Access problem and event feed, metrics, and topology** (`DataExport`)—API v1

In most cases, you will require an access token with at least these permissions:

* **Access problem and event feed, metrics, and topology** (`DataExport`)—API v1
* **Read configuration** (`ReadConfig`)—API v1
* **Write configuration** (`WriteConfig`)—API v1
* **Read settings** (`settings.read`)—API v2
* **Write settings** (`settings.write`)—API v2

For general information on access token authentication, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").