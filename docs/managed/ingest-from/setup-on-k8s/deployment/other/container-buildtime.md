---
title: Application observability via container build-time injection
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime
scraped: 2026-05-12T11:52:45.250678
---

# Application observability via container build-time injection

# Application observability via container build-time injection

* 5-min read
* Updated on Oct 17, 2025

Inject Dynatrace code modules into a container during its build process.

This method of application instrumentation has limitations in linking Kubernetes workloads with monitored containers/processes. To achieve proper relationships and linking, consider using [automatic application-only injection](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").

## Prerequisites

* Review the list of [supported applications and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* [Create an access token with `PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope.
* Storage requirements:

  + ~325 MB for glibc
  + ~290 MB for musl
  + ~650 MB for glibc and musl combined
* For ARM architecture, ensure `wget` and `unzip` are installed.

Container buildtime injection and cgroup v2

If Container buildtime injection is used with [cgroup v2ï»¿](https://kubernetes.io/docs/concepts/architecture/cgroups/), the `builtin:containers.*` metrics are reported to Dynatrace only if all the following conditions are respected:

* The **Kubernetes API** is accessible (see [Grant viewer role to service accounts](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment."))
* The pod runs a **single container**

## Deploy

To integrate OneAgent into the application image, follow the steps below.

Kubernetes/OpenShift v4.0

OpenShift v3.11

ARM

1. Sign in to Docker with your Dynatrace environment ID as username and access token as password.

   ```
   docker login -u <environmentID> -p <accessToken> <environmentURL>
   ```
2. Add the following lines of code to the application image, after the last `FROM` command:

   ```
   COPY --from=<environment>/linux/oneagent-codemodules:<technology> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   * `<technology>`âOneAgent code module required for your application. Available options are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, and `sdk`. You can specify several code modules, separated by hyphen (`-`), for example `java-go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package.

What if my Docker image is based on Alpine Linux?

Dynatrace OneAgent supports Alpine Linux based environments.

```
COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Valid options here are: `all`, `dotnet`, `php`, `java`, `apache`, `nginx`, `nodejs`, and `go`.

3. Build your application image.

   Build the Docker image from your Dockerfile to use it in your Kubernetes environment.

   ```
   docker build -t yourapp .
   ```

You can monitor your application containers with a different Dynatrace environment.

For OneAgent version 1.139+, if you have an existing application image where you've already added the OneAgent code modules for a specific Dynatrace environment, you can have the OneAgent report to another Dynatrace environment without rebuilding your application image.  
For this, you need to make a call to the REST endpoint of your second Dynatrace environment. Don't forget to adapt the respective placeholders `<environmentID>` and `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

In return, you get a JSON object that covers the required information that needs to be passed as an environment variable to the application container.  
Make sure you set the environment variables of the application container as described below:

* `DT_TENANT`: equals `tenantUUID`
* `DT_TENANTTOKEN`: equals `tenantToken`
* `DT_CONNECTION_POINT`: semi-colon separated list of `communicationEndpoints`

4. Optional Configure network zones

You can configure network zones as an environment variable:

* `DT_NETWORK_ZONE`: equals `your.network.zone`

See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

5. Optional Configure a proxy address

   In case you run an environment with proxy, you need to set the `DT_PROXY` environment variable in the application container to pass the proxy credentials to OneAgent.

   For Alpine Linux-based containers, you might need to update the `wget` shipped with the Alpine image to allow for proxy authentication for the download of OneAgent.

1. Define variables with optional default values using `ARG` instructions, as shown below.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_PAAS_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"
   ```

   * You can override the default values within the OpenShift `BuildConfig`. Replace `<environmentID>` with your Dynatrace environment ID. If youâre using Dynatrace Managed, you need to provide your Dynatrace Server URL (`https://<YourDynatraceServerURL>/e/<environmentID>/api`). Replace `<token>` with the PaaS token mentioned above.
   * Technology support is enabled via `include` parameters. Valid options for `flavor=default` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, and `sdk`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package.

   What if my Docker image is based on Alpine Linux?

   OneAgent supports the flavor `musl` for Alpine Linux based environments. Valid options for `flavor=musl` are `all`, `java`, `apache`, `nginx`, and `nodejs`.
2. Add the following commands to your current Dockerfile to integrate OneAgent and activate instrumentation of your application.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENV LD_PRELOAD="/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so"
   ```

   The commands above that use `wget` and `unzip` might fail if they aren't provided by the base image.
3. Build your application image.

   In an OpenShift context the above Dockerfile could be used for binary builds as follows:

   ```
   oc new-build --binary --strategy=docker --allow-missing-images yourapp



   oc patch bc/yourapp --type=json --patch='[{"op":"remove","path":"/spec/strategy/dockerStrategy/from"}]'



   oc start-build yourapp --from-dir=. --follow
   ```

You can monitor your application containers with a different Dynatrace environment.

For OneAgent version 1.139+, if you have an existing application image where you've already added the OneAgent code modules for a specific Dynatrace environment, you can have the OneAgent report to another Dynatrace environment without rebuilding your application image.  
For this, you need to make a call to the REST endpoint of your second Dynatrace environment. Don't forget to adapt the respective placeholders `<environmentID>` and `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

In return, you get a JSON object that covers the required information that needs to be passed as an environment variable to the application container.  
Make sure you set the environment variables of the application container as described below:

* `DT_TENANT`: equals `tenantUUID`
* `DT_TENANTTOKEN`: equals `tenantToken`
* `DT_CONNECTION_POINT`: semi-colon separated list of `communicationEndpoints`

4. Optional Configure network zones

You can configure network zones as an environment variable:

* `DT_NETWORK_ZONE`: equals `your.network.zone`

See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

5. Optional Configure a proxy address

   In case you run an environment with proxy, you need to set the `DT_PROXY` environment variable in the application container to pass the proxy credentials to OneAgent.

   For Alpine Linux-based containers, you might need to update the `wget` shipped with the Alpine image to allow for proxy authentication for the download of OneAgent.

1. Set the following build-time variables:

   * `$DT_API_URL` (The API URL of your Dynatrace environment)
   * `$DT_PAAS_TOKEN` (The PaaS token to download the code modules)
   * `$DT_ONEAGENT_TECHNOLOGY` (The module that is downloaded, for example `php`)
2. Add the following commands to the Dockerfile:

   ```
   RUN mkdir -p /opt/dynatrace/oneagent && ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&flavor=default&arch=arm&include=$DT_ONEAGENT_TECHNOLOGY" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

## Update

You need to manually update OneAgent by rebuilding the container image every time a new version of a code module is needed.

## Uninstall

To uninstall OneAgent from application monitoring

Docker multi-stage image builds

Classic integration

1. Remove the two lines of code from the application image.

   ```
   COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
2. Rebuild the application image.

   ```
   docker build -t yourapp .
   ```

1. Remove the following commands from your Dockerfile.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



   CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
   ```
2. Rebuild the application image.

   ```
   docker build -t yourapp .
   ```