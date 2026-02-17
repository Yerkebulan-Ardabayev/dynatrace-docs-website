---
title: Monitor Elastic Container Service (ECS) with EC2 launch type
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs
scraped: 2026-02-17T05:10:15.329885
---

# Monitor Elastic Container Service (ECS) with EC2 launch type

# Monitor Elastic Container Service (ECS) with EC2 launch type

* How-to guide
* 3-min read
* Published May 18, 2020

To deploy OneAgent on **AWS Elastic Container Service** (ECS) clusters with EC2 launch type, follow the instructions below.

## Prerequisites

* Create a [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* ECS cluster with **Linux-based container instances**.
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Create the `ecsinstanceRole` IAM role in the ECS console.

## Deploy OneAgent as a daemon service

This approach describes the installation of OneAgent as a daemon service in its own container. ECS orchestrates the execution of the OneAgent task on each container instance that is part of the cluster.

1. On the ECS console, go to **Task Definitions** > **Create new Task Definition**. Select **EC2** and then **Next step**.
2. In **Configure task and container definitions**, enter the following values:

   * **Task Definition Name**: `oneagent`
   * **Network Mode**: `host`
3. Scroll down to **Volumes**. Click **Add volume** and enter the following values:

   * **Name**: `oneagent`
   * **Volume type**: `Bind Mount`
   * **Source path**: `/`

   Click **Add** to add the volume.
4. Scroll to **Container Definitions** and click **Add container**. In the **Standard** section, enter the following values:

   * **Container name**: `oneagent`
   * **Image**: `dynatrace/oneagent`
   * **Memory limits**: as needed

   There are two types of memory limits: soft and hard. ECS requires that you define the limit for at least one type of memory. We recommend using the default setting (soft limit of 256 MiBs), as it's less restrictive, but you can adjust this setting as needed.
5. In the **Advanced container configuration** section, go to **Environment**. Make sure that **Essential** is selected.

   In **Environment variables**, define `ONEAGENT_INSTALLER_SCRIPT_URL` depending on how you connect to Dynatrace:

   * For SaaS: `https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * For Managed: `https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * For ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   If you connect via an ActiveGate, you can skip the certificate check by adding the `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` key with the value `true`.
6. Optional Add OneAgent installer parameters.

   While still in **Environment variables**, you can [customize your OneAgent installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") by adding several OneAgent installer parameters in the command text box. Make sure to separate each parameter by a space. For example, `--set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Set the `--set-network-zone=<your.network.zone>` parameter if you want to configure network zones. See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.
7. Go to **Storage and logging** and enter the following values in **Mount point**:

   * **Source volume**: `oneagent`
   * **Container path**: `/mnt/root`
8. Scroll down to **Security** and set the container to run in **Privileged** mode.
9. Click **Add** to add the container definition.
10. While still in the task definition, go back to **Volumes** and click **Configure via JSON**. Add the following two parameters at the root level (for example, before the `"tags"`):

    ```
    "ipcMode": "host",



    "pidMode": "host",
    ```

    Click **Save** to save the JSON configuration.
11. Click **Create** to save your task definition.
12. In the **Task definitions** menu, select the newly created OneAgent task and then click **Actions** > **Create service**. This will create a service to run your task.
13. In **Configure service**, enter the following values:

    * **Launch type**: `EC2`
    * **Task Definition**: `oneagent`
    * **Service type**: `DAEMON`
    * **Service name**: give a name to the service.

    Leave the rest of the settings set as they are by default. Follow the remaining steps until you reach and select **Create service**.

    Once the service is created, the associated tasks will be executed. The `oneagent` service creates a task to deploy OneAgent on each container instance of your cluster.

    You can see the container instances displayed on the ECS cluster dashboard, and the corresponding hosts in your Dynatrace monitoring environment.

    ![ECS hosts](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)
14. After deploying OneAgent, restart the running application tasks to get service-level visibility.

## Security implications

See [Docker security implications](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#security "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Limitations

See [Docker limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Monitoring consumption

For Elastic Container Service, monitoring consumption is based on hosts units. See [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") for details.

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")