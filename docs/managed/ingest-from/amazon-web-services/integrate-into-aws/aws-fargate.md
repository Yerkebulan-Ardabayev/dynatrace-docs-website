---
title: Monitor AWS Fargate
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate
---

# Monitor AWS Fargate

# Monitor AWS Fargate

* How-to guide
* 1-min read
* Updated on Oct 02, 2026

To monitor your AWS Fargate workloads, deploy Dynatrace OneAgent as described below.

## Prerequisites

* [Create an API token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment and enable the following permissions:

  + **Access problem and event feed, metrics, and topology** (API v1)
  + **PaaS integration - Installer download**
* Review the list of [supported applications and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Runtime integration

These instructions describe how to integrate Dynatrace OneAgent code modules into your Fargate tasks using an initContainer. The initContainer copies the OneAgent artifacts into a shared ephemeral volume, where environment variables then configure and activate OneAgent.

Dynatrace provides OneAgent code module images on public registries, such as the following:

* [Dynatrace Code Modules Image Tags﻿](https://gallery.ecr.aws/dynatrace/dynatrace-codemodules).

An image can then be used for container services that support initContainers. The `dynatrace-codemodules` image contains the OneAgent artifacts and a small CLI, the `dynatrace-bootstrapper`, that is executed at startup to copy the artifacts into a volume shared with the application container.

### Select an image

The following image tag formats are available:

* **Immutable tags** — contain code modules of a specific release, for example, `1.327.51.20251205-162230`
* **Rolling tags** (major.minor) — for example, `1.327`
* **Technology-specific images** — available with both immutable and rolling tags, for example, `1.327-java`, `1.327-dotnet`

**Rolling tags** (for example, `1.333`) receive patch updates automatically when a container restarts. New tasks pick up the latest patch version without task definition changes. Use rolling tags when automatic hot-fix delivery is the priority.

**Immutable tags** (for example, `1.333.17.20250601-120000`) pin tasks to a specific version, giving you deterministic deployments and a clear rollback path. Use immutable tags when strict version control or compliance requirements apply.

**Technology-specific images** (for example, `1.333-java`, `1.333-dotnet`) contain only the code modules for a single runtime, resulting in a smaller image and faster pull and startup times. Avoid technology-specific images if your container runs multiple runtimes that need to be instrumented simultaneously, for example, PHP served behind NGINX.

### Store credentials securely

Store Dynatrace credentials as secrets and reference them in the `secrets` field of your task definition. Use whichever secrets solution fits your setup, for example, AWS Secrets Manager.

### Configure the task definition

Create a task definition file (for example, `task-definition.json`) with the following structure. The `initoneagent` container runs first, copies OneAgent artifacts into a shared ephemeral volume, and exits. Your application container then starts and loads OneAgent via `LD_PRELOAD`.

Replace `<your-application-image>`, `<your-account-id>`, `<your-region>`, and `<your-secret-name>` with your own values.

```
{



"family": "<your-task-family>",



"requiresCompatibilities": ["FARGATE"],



"networkMode": "awsvpc",



"cpu": "256",



"memory": "512",



"taskRoleArn": "arn:aws:iam::<your-account-id>:role/<your-task-role>",



"executionRoleArn": "arn:aws:iam::<your-account-id>:role/<your-task-execution-role>",



"containerDefinitions": [



{



"name": "initoneagent",



"image": "public.ecr.aws/dynatrace/dynatrace-codemodules:1.333",



"essential": false,



"user": "0:0",



"command": [



"--source=/opt/dynatrace/oneagent",



"--target=/mnt/dynatrace/oneagent",



"--technology=<your-technology>"



],



"environment": [



{ "name": "DT_ONEAGENT_OPTIONS", "value": "flavor=default&include=all" }



],



"secrets": [



{



"name": "DT_API_URL",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_API_URL::"



},



{



"name": "DT_PAAS_TOKEN",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_PAAS_TOKEN::"



}



],



"mountPoints": [



{



"sourceVolume": "oneagent",



"containerPath": "/mnt",



"readOnly": false



}



],



"logConfiguration": {



"logDriver": "awslogs",



"options": {



"awslogs-group": "<your-log-group>",



"awslogs-region": "<your-region>",



"awslogs-stream-prefix": "ecs"



}



}



},



{



"name": "<your-application-container>",



"image": "<your-application-image>",



"essential": true,



"linuxParameters": {



"initProcessEnabled": true



},



"environment": [



{ "name": "LD_PRELOAD", "value": "/mnt/dynatrace/oneagent/agent/lib64/liboneagentproc.so" }



],



"secrets": [



{



"name": "DT_TENANT",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_TENANT::"



},



{



"name": "DT_TENANTTOKEN",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_TENANTTOKEN::"



},



{



"name": "DT_CONNECTION_POINT",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_CONNECTION_POINT::"



}



],



"mountPoints": [



{



"sourceVolume": "oneagent",



"containerPath": "/mnt",



"readOnly": false



}



],



"dependsOn": [



{



"containerName": "initoneagent",



"condition": "COMPLETE"



}



],



"logConfiguration": {



"logDriver": "awslogs",



"options": {



"awslogs-group": "<your-log-group>",



"awslogs-region": "<your-region>",



"awslogs-stream-prefix": "ecs"



}



}



}



],



"volumes": [



{



"name": "oneagent",



"host": {}



}



]



}
```

Replace `<your-technology>` with your application runtime (valid values: `python`, `java`, `dotnet`, `nodejs`, `php`, `go`, `apache`, `nginx`, `all`).

Don't store the OneAgent code modules on network-attached storage, such as Amazon EFS. With Amazon EFS, the OneAgent files might be missing or incomplete when the application container starts. In that case, the application container logs an `LD_PRELOAD` error for `liboneagentproc.so` that ends with `cannot be preloaded (file too short)`, and the task doesn't appear in Dynatrace. Use local storage.

1. Register the task definition:

   ```
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
2. Update your ECS service to use the new revision:

   ```
   aws ecs update-service \



   --cluster <your-cluster-name> \



   --service <your-service-name> \



   --task-definition <your-task-family>
   ```

## Alternative integration paths

* **EKS on Fargate** — you can run on Amazon EKS with the Fargate launch type using application-only injection with Dynatrace Operator. See [Install on EKS Fargate](/managed/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto#fargate "Deploy and configure Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS) environment.").
* **Container build-time injection** — to embed OneAgent into your container image at build time using Docker multi-stage builds, see [Set up OneAgent on containers for application-only monitoring](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

## Optional configuration

After you integrate OneAgent, you can customize its behavior by adding environment variables to your application container.

### Route OneAgent logs to stdout

To route OneAgent diagnostic logs to stdout alongside your application logs, add the following environment variables to your application container:

* `DT_LOGSTREAM=stdout` — routes OneAgent diagnostic output to standard output
* `DT_LOGLEVELCON=INFO` — sets the log verbosity level

When you configure the `awslogs` log driver on your containers (as shown in the task definition example), [CloudWatch Logs](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudwatch-logs "Monitor Amazon CloudWatch Logs and view available metrics.") captures both application and OneAgent diagnostic logs in a single stream.

### Configure network zones

You can configure network zones as an environment variable:

* `DT_NETWORK_ZONE`: equals `your.network.zone`

See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

### Configure custom properties

You can add [custom properties](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") as an environment variable:

* `DT_CUSTOM_PROP`: for example, `AWS_ENVIRONMENT=prod SERVICE_NAME=my-service`

Set `DT_CUSTOM_PROP` and `DT_NETWORK_ZONE` in the application container.

## Rotate the tenant token

The tenant token that your task definition references as `DT_TENANTTOKEN` stays valid until you finish the [tenant token rotation](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token#rotate-tenant-token "Learn what a tenant token is and how to change it."). Before you finish the rotation, update the secret with the new tenant token and redeploy your tasks so that they connect with the new token. After you finish the rotation, the old token is invalid, and tasks that still use it can stop reporting data.

## Monitor consumption

Monitoring consumption depends on your licensing model:

* Dynatrace Platform Subscription (DPS): Consumption is billed in GiB-hours, see [Calculate your consumption of Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring#app-only-gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").
* Dynatrace classic licensing: Consumption is billed in host units, see [Application and Infrastructure Monitoring (Host Units)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Troubleshooting

For OneAgent integration issues, see [Application image OneAgent integration problems﻿](https://dt-url.net/yu23mli).

## Related topics

* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")