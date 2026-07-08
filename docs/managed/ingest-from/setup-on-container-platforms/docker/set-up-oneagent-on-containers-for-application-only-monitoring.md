---
title: Set up OneAgent on containers for application-only monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring
---

# Set up OneAgent on containers for application-only monitoring

# Set up OneAgent on containers for application-only monitoring

* 2-min read
* Published Jun 25, 2021

If you don't have access to underlying hosts, you can deploy OneAgent on containers for application-only monitoring. Follow the steps below to integrate OneAgent into the application image.

## Deploy OneAgent

Required versions

* Docker version 17.05+

1. Sign in to Docker with your Dynatrace environment ID as username.

   ```
   docker login <environmentURL> -u <environmentID>
   ```
2. Enter your <PAAS\_TOKEN> when prompted.
3. Add the following lines of code to the application image, after the last `FROM` command:

   ```
   COPY --from=<environmentURL>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   where:

* `<environmentURL>` is:

  + Environment ActiveGate: `<ActiveGateaddress:9999>`
  + Managed: `{ManagedAddress}`
* `<TECHNOLOGY>` is the OneAgent code module required for your application. Valid options are `all`, `java`, `python`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, and `sdk`. To specify several code modules, separate them by hyphens (for example, use `java-go` to specify `java` and `go`). Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package.

What if my Docker image is based on Alpine Linux?

Dynatrace OneAgent supports Alpine Linux–based environments.  
Use this syntax:

```
COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Valid options here are `all`, `dotnet`, `php`, `java`, `apache`, `nginx`, `nodejs`, and `go`.

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
4. Optional Configure a proxy address

   In case you run an environment with proxy, you need to set the `DT_PROXY` environment variable in the application container to pass the proxy credentials to OneAgent.

   For Alpine Linux-based containers, you might need to update the `wget` shipped with the Alpine image to allow for proxy authentication for the download of OneAgent.

## Update OneAgent

Each time you want to leverage a new version of Dynatrace OneAgent, you must rebuild your local OneAgent code modules and application image. Any newly started pods from this application image will be monitored with the latest version of OneAgent.

If you've specified a default OneAgent installation version for new hosts and applications using [OneAgent update settings](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), your Kubernetes applications will be automatically monitored by the defined default version of Dynatrace OneAgent.

## Uninstall OneAgent

To uninstall OneAgent from application-only monitoring, just remove references from your application or Docker image and then redeploy the application.

### Container build-time injection

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

## Related topics

* [Set up Dynatrace on Docker](/managed/ingest-from/setup-on-container-platforms/docker "Deploy OneAgent on Docker.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")