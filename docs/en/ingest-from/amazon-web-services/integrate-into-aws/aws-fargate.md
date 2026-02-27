---
title: Monitor AWS Fargate
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate
scraped: 2026-02-27T21:16:36.373894
---

# Monitor AWS Fargate

# Monitor AWS Fargate

* How-to guide
* 1-min read
* Updated on Oct 14, 2025

To deploy OneAgent on AWS Fargate, read the instructions provided below.

## Prerequisites

* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment and enable the following permissions:

  + **Access problem and event feed, metrics, and topology** (API v1)
  + **PaaS integration - Installer download**
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Integrate OneAgent into your application image

There are three ways to integrate OneAgent with AWS Fargate applications.

### Automatic injection EKS

With automatic injection you can manage upgrades and lifecycle.

Kubernetes version 1.20+

On AWS Fargate, only the `applicationMonitoring` deployment without the CSI driver is supported.

Before you start installation, make sure you have a running AWS Fargate cluster. For details, see [Getting started with AWS Fargate using Amazon EKSï»¿](https://dt-url.net/zg034ha).

1. Add a Fargate profile to define the Dynatrace Operator deployment.

   Be sure it matches the `dynatrace` namespace where Dynatrace Operator will be deployed.
2. Create a `dynatrace` namespace.

   ```
   kubectl create namespace dynatrace
   ```
3. Install Dynatrace Operator.

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes.yaml
   ```
4. Create the secret holding the API token for authentication to the Dynatrace cluster.

   Be sure to replace `<API_TOKEN>` with your own value.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<API_TOKEN>"
   ```
5. Download the [preconfigured DynaKube custom resource sample file from GitHubï»¿](https://dt-url.net/dynakube-applicationmonitoring).
6. Review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."), and adapt the DynaKube custom resource according to your requirements.
7. Apply the DynaKube custom resource.

   ```
   kubectl apply -f applicationMonitoring.yaml
   ```

### Build-time injection EKS and ECS

With build-time injection you can embed OneAgent into your container image.

Docker multi-stage image builds

Classic integration

To use this option you need:

* Docker version 17.05+
* OneAgent version 1.155+

1. Sign in to Docker with your Dynatrace environment ID as username and PaaS token as password.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```

* Replace `<your-environment-url>` with the URL or IP address of your environment or of your ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    If you use your own environment ActiveGate, use the `<ip-address>:9999` or `<hostname>:9999` format.
* Add two additional lines of code to the application image, after the last `FROM` command:

  ```
  COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /



  ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
  ```

* Replace `<technology>` with the code module required for your application. Valid options are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `python`, `sdk`, and `go`. You can specify several code modules, separated by hyphen (`-`), for example `java-go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package.

What if my Docker image is based on Alpine Linux?

Dynatrace OneAgent supports Alpine Linux based environments. Use this syntax:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Valid options here are `all`, `go`, `java`, `apache`, `nginx`, `nodejs`, and `python`.

3. Build your application image.

   Build the Docker image from your dockerfile to use it in your Kubernetes environment:

   ```
   docker build -t yourapp .
   ```

   You can monitor your application containers with a different Dynatrace environment. To do this, read the instructions below:

   For OneAgent version 1.139+, if you have an existing application image where you've already added the OneAgent code modules for a specific Dynatrace environment, you can have the OneAgent report to another Dynatrace environment without rebuilding your application image.

   For this you need to make a call to the REST endpoint of your second Dynatrace environment. Make sure to adapt the respective placeholders `<your-environment-id>` and `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   In return, you get a JSON object that covers the required information that needs to be passed as an environment variable to the application container. Make sure you set the environment variables of the application container as described below:

   * `DT_TENANT`: equals `tenantUUID`
   * `DT_TENANTTOKEN`: equals `tenantToken`
   * `DT_CONNECTION_POINT`: semi-colon separated list of `communicationEndpoints`

To utilize distroless images (stripped-down versions of regular Docker images containing the only essentials required to run an application), OneAgent needs to be called in an executable form using the command instruction `CMD`, instead of `ENTRYPOINT`.

1. Set the following environment variables.

   * `DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"`
   * `DT_API_TOKEN="<your-paas-token>"`
   * `ARCH="<x86|arm>"`
   * `DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"`
   * `DT_HOME="/opt/dynatrace/oneagent"`

   Environment variables need to be set:

   * In your current Dockerfile, to integrate OneAgent and activate instrumentation of your application.
     Define variables with optional default values using `ARG` instructions.
     The code block below provides a template to set these environment variables.
   * In the runtime injection container.

   ```
   ARG DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<your-paas-token>"



   ARG ARCH="<x86|arm>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?arch=$ARCH&Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



   CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
   ```

   * The commands above that use `wget` and `unzip` might fail if they aren't provided by the base image.
   * Replace `<your-paas-token>` with your PaaS token.
   * `DT_ONEAGENT_OPTIONS` - this is the flavor (valid options are `default` or `musl` for Alpine images) and the technology (code module).

     + Syntax for `default` is `flavor=default&include=all`.
     + Syntax for `musl` is `flavor=musl&include=all`.

   **What if my Docker image is based on Alpine Linux?**

   Dynatrace OneAgent supports the flavor `musl` for Alpine Linux based environments. Valid options for `flavor=musl` are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.
2. Build your application image.

   Build the Docker image from your dockerfile to use it in your Kubernetes environment:

   ```
   docker build -t yourapp .
   ```

   You can monitor your application containers with a different Dynatrace environment. To do this, read the instructions below:

   For OneAgent version 1.139+, if you have an existing application image where you've already added the OneAgent code modules for a specific Dynatrace environment, you can have the OneAgent report to another Dynatrace environment without rebuilding your application image.

   For this you need to make a call to the REST endpoint of your second Dynatrace environment. Make sure to adapt the respective placeholders `<your-environment-id>` and `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   In return, you get a JSON object that covers the required information that needs to be passed as an environment variable to the application container. Make sure you set the environment variables of the application container as described below:

   * `DT_TENANT`: equals `tenantUUID`
   * `DT_TENANTTOKEN`: equals `tenantToken`
   * `DT_CONNECTION_POINT`: semi-colon separated list of `communicationEndpoints`

### Runtime injection ECS

With runtime injection you can pull OneAgent when the container starts. To install Dynatrace OneAgent at runtime, you must deploy your application using a task with two container definitions. One is for downloading and unzipping the OneAgent to a shared volume, the other is your application container, which must mount the same volume.

For the runtime injection, follow the steps below.

1. Go to **Fargate Task Definition** > **Create New Task Definition** and select **AWS Fargate** in the **Infrastructure requirements > Launch type** section.
2. Name the task, optionally set roles and sizes, and then scroll down to **Storage - optional** > **Volumes** and select **Add volume**. Add a volume of type `Bind Mount` named `oneagent`.

   You must create a volume **before** creating container definitions in order to set the shared volume in each container.
3. Scroll to the bottom of **Container - 1** and select **Add container**.

   * In the **Container details** subsection:

     + Add a container named `install-oneagent`
     + Set the image to Alpine version 3.8+ ("alpine:3")
     + select **No** in the **Essential container** field
   * In the **Resource allocation limits - conditional** subsection:

     + Select the CPU and memory limits.

   There are two types of memory limits: soft and hard. ECS requires that you define the limit for at least one type of memory. We recommend using the default setting (soft limit of 128 MiBs), as it's less restrictive, but you can adjust it as needed.
4. In the **Docker configuration - optional** subsection:

   * In the **Entry point** field, enter `/bin/sh,-c`.
   * In the **Command** field, enter `ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?arch=$ARCH&Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE`.
5. In the **Environment variables** subsection, define:

   * `DT_API_URL` - this is the API URL for your Dynatrace environment.

     + For SaaS: `https://<your-environment-id>.live.dynatrace.com/api`
     + For Managed: `https://<cluster>/e/<your-environment-id>/api`
     + For ActiveGate: `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api`.
   * `DT_ONEAGENT_OPTIONS`- this is the flavor (valid options are `default` or `musl` for Alpine images) and the technology (code module).

     + Syntax for `default` is `flavor=default&include=all`.
     + Syntax for `musl` is `flavor=musl&include=all`.
   * `DT_PAAS_TOKEN` - this is your PaaS token to download the OneAgent code modules.
   * `ARCH` - CPU architecture.

     + for x86\_64: `x86`
     + for arm64: `arm`

       Automatic architecture detection

       Use the following script to detect the CPU architecture on Linux.

       ```
       ARCH=$(uname -p);



       export ARCH;



       if [ "$ARCH" = "arm" ] || [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ]; then



       export ARCH="arm";



       else



       export ARCH="x86";



       fi
       ```
6. Choose **Add container** again, this time to define your application, and complete the fields in the **Standard** subsection according to your application requirements.
7. Scroll to **Environment**, and in **Environment variable**, define `LD_PRELOAD` with the value `/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so`.
8. Scroll to **Startup Dependency Ordering** and enter the container name `install-oneagent` and the condition `Complete`.
9. Scroll to the **Storage - optional** section.

   * Create a new volume and name it `oneagent`
   * Create a mount point:

     + Select **Add mount point**
     + Select `install-oneagent` in the **Container** field
     + Select `oneagent` in the **Source volume** field
     + Set `/opt/dynatrace/oneagent` in the **Container path**
10. Select **Create** at the bottom of the screen to create your task definition and deploy it on your ECS cluster.

Check the **Logs** tab

* For the `install-oneagent` container, you can see the code modules' ZIP file being downloaded by wget and being unzipped.
* For your application workload container, you can see the code module being loaded by the process.

In Dynatrace, your Fargate application workload container will show up in the **Hosts** section. The instrumented process will show up in **Processes** as a typical Docker container.

![Fargate](https://dt-cdn.net/images/fargate-1165-0748c0cf29.png)

The runtime approach requires Fargate version 1.3+. For earlier versions, select the build-time approach.

### Configure network zones Optional

You can configure network zones as an environment variable:

* `DT_NETWORK_ZONE`: equals `your.network.zone`

See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Monitoring consumption

For AWS Fargate, monitoring consumption is based on host units. To learn how host units are calculated for Dynatrace application and infrastructure monitoring, see [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Troubleshooting

* [Application image OneAgent integration problemsï»¿](https://dt-url.net/yu23mli)

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")