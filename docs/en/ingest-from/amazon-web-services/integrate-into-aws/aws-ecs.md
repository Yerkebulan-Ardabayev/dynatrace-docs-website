---
title: Monitor Amazon Elastic Container Service (ECS)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs
scraped: 2026-02-15T08:57:00.237770
---

# Monitor Amazon Elastic Container Service (ECS)

# Monitor Amazon Elastic Container Service (ECS)

* How-to guide
* 1-min read
* Published Jan 16, 2023

To deploy OneAgent on AWS Elastic Container Service (ECS) clusters with EC2 launch type, follow the instructions below.

## Prerequisites

* Create a [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* ECS cluster with **Linux-based container instances**.
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* An IAM role for your container instances should attach the `AmazonEC2ContainerServiceforEC2Role` managed policy. Instructions for creating this role, named `ecsInstanceRole`, are provided in the [AWS documentationï»¿](https://dt-url.net/y923usz).

## Deploy OneAgent as a daemon service

This approach describes the installation of OneAgent as a daemon service in its own container. ECS orchestrates the execution of the OneAgent task on each container instance that is part of the cluster.

Privileged mode and volume parameters are prerequisites for this deployment method. As a result, this can only be done using JSON revisions. Consider using [build-time injection](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#buildtime "Install OneAgent on AWS Fargate.") instead.

1. On the ECS console, go to **Task Definitions** > **Create new task definition** > **Create new task definition with JSON**.
2. Edit the task definition JSON:

   * Set `requiresCompatibilities` to `["EC2"]`
   * Set `family` to a unique name of your choice for the task definition, such as `oneagent`
   * Add `ipcMode` and set to `host`
   * Add `pidMode` and set to `host`
   * Set `containerDefinitions[0]` to

     ```
     {



     "name": "oneagent",



     "image": "dynatrace/oneagent",



     "essential": true,



     "privileged": true



     }
     ```
   * Create a new dictionary in the `volumes` array:

     ```
     {



     "name": "oneagent"



     }
     ```
3. Select **Create**.
4. Select **Create new revision** > **Create new revision**.
5. In **Infrastructure requirements**, go to **Network Mode** and select `host`.
6. Scroll to **Container - 1**, go to **Resource allocation limits** and set the memory limits as needed

   There are two types of memory limits: soft and hard. ECS requires that you define the limit for at least one type of memory. We recommend using the default setting (soft limit of 256 MiBs), as it's less restrictive, but you can adjust this setting as needed.
7. In the **Environment variables** section, go to **Add individually** and define `ONEAGENT_INSTALLER_SCRIPT_URL` depending on how you connect to Dynatrace:

   * For Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`
   * For ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   If you connect via an ActiveGate, you can skip the certificate check by adding the `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` key with the value `true`.
8. Optional Add OneAgent installer parameters.

   While still in **Environment variables**, you can [customize your OneAgent installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") by adding several OneAgent installer parameters in the command text box. Make sure to separate each parameter by a space. For example, `--set-monitoring-mode=infra-only --set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Set the `--set-network-zone=<your.network.zone>` parameter if you want to configure network zones. See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.
9. Scroll down to **Storage** > **Volume - 1** and set **Source path** to `/`
10. Go to **Container mount points**, select **Add mount point** and enter the following values:

    * **Container**: `oneagent`
    * **Source volume**: `oneagent`
    * **Container path**: `/mnt/root`
11. Select **Create** to save your task definition.
12. In the **Task definitions** menu, select the newly created OneAgent task and then select **Deploy** > **Create service**. This will create a service to run your task.
13. In **Compute configuration**, select **Launch type** and for **Launch type** select `EC2`.
14. In **Deployment configuration**, perform the following actions:

    * **Service name**: Name the service.
    * **Service type**: Select `Daemon`.

    Leave the rest of the settings set as they are by default. Follow the remaining steps until you reach and select **Create**.

    Once the service is created, the associated tasks will be executed. The `oneagent` service creates a task to deploy OneAgent on each container instance of your cluster.

    You can see the container instances displayed on the ECS cluster dashboard, and the corresponding hosts in your Dynatrace monitoring environment.

    ![ECS hosts](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)
15. After deploying OneAgent, restart the running application tasks to get service-level visibility.

## Security implications

See [Docker security implications](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#security "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Limitations

See [Docker limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Monitoring consumption

For Elastic Container Service, monitoring consumption is based on host units. See [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") for details.

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")