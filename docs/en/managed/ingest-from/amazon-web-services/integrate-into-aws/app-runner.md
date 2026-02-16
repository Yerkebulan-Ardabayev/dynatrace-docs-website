---
title: Monitor AWS App Runner
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner
scraped: 2026-02-16T21:14:30.705294
---

# Monitor AWS App Runner

# Monitor AWS App Runner

* How-to guide
* 3-min read
* Published Jan 16, 2023

To deploy OneAgent on App Runner, read the instructions provided below.

## Prerequisites

* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment and enable the following permissions:

  + **Access problem and event feed, metrics, and topology** (`DataExport`) (API v1)
  + **PaaS integration - Installer download** (`InstallerDownload`)
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Integrate OneAgent into your application image

### Build-time injection EKS, ECS, and App Runner

If you're using ECS, EKS, and App Runner, you can use build-time injection to embed OneAgent into your container image.

Docker multi-stage image builds

Classic integration

To use this option you need:

* Docker version 17.05+
* OneAgent version 1.155+

1. Sign in to Docker with your Dynatrace environment ID as username and your PaaS token as password.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Add two additional lines of code to the application image after the last `FROM` command:

   ```
   COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

* Replace `<your-environment-url>` with the URL or IP address of your environment or your ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    If you use your own environment ActiveGate, use the `<ip-address>:9999` or `<hostname>:9999` format.
* Replace `<technology>` with the code module required for your application. Valid options are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `sdk`, and `go`. You can specify several code modules, separated by hyphen (`-`), for example `java-go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package.

What if my Docker image is based on Alpine Linux?

Dynatrace OneAgent supports Alpine Linux-based environments. Use this syntax:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Valid options here are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.

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

1. Add the following commands to your current Dockerfile to integrate OneAgent and activate instrumentation of your application. Define variables with optional default values using `ARG` instructions.

   ```
   ARG DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<your-paas-token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



   CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
   ```

   * The commands above that use `wget` and `unzip` might fail if they aren't provided by the base image.
   * Replace `<your-environment-id>` with your Dynatrace environment ID. If you're using Dynatrace Managed, you need to provide your Dynatrace Cluster URL (`https://<YourDynatraceServerURL>/e/<your-environment-id>/api`).
   * Replace `<your-paas-token>` with your PaaS token.
   * `DT_ONEAGENT_OPTIONS` - this is the flavor (valid options are `default` or `musl` for Alpine images) and the technology (code module).

     + Syntax for `default` is `flavor=default&include=all`.
     + Syntax for `musl` is `flavor=musl&include=all`.

   **What if my Docker image is based on Alpine Linux?**

   Dynatrace OneAgent supports the flavor `musl` for Alpine Linuxâbased environments. Valid options for `flavor=musl` are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.
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

### Configure network zones Optional

You can configure network zones as an environment variable:

* `DT_NETWORK_ZONE`: equals `your.network.zone`

See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Monitoring Consumption

For AWS App Runner, monitoring consumption is based on host units. See [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") for details.

## Troubleshoot

* [Application image OneAgent integration problemsï»¿](https://dt-url.net/yu23mli)

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")