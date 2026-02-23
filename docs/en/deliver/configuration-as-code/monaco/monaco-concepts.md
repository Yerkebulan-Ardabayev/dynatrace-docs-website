---
title: Monaco concepts
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-concepts
scraped: 2026-02-23T21:31:40.505304
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