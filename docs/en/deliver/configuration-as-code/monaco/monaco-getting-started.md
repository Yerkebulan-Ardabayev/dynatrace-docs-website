---
title: Manage configurations with Monaco
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-getting-started
scraped: 2026-03-01T21:27:07.229444
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