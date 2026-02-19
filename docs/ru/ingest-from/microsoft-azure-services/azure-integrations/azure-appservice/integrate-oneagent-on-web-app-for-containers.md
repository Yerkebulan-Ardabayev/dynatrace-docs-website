---
title: Integrate OneAgent on Azure App Service for Linux and containers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers
scraped: 2026-02-19T21:21:37.774500
---

# Integrate OneAgent on Azure App Service for Linux and containers

# Integrate OneAgent on Azure App Service for Linux and containers

* Latest Dynatrace
* How-to guide
* 11-min read
* Updated on Dec 17, 2025

Linux only

App Service on Linux supports two scenarios.

* **Bring your own code**

  In the code scenario, App Service provides a base container that is maintained by the platform.

  This container targets:

  + A development framework, such as .NET Core, PHP, or Node.js.
  + A version of that framework, such as .NET Core 3.0 or .NET Core 3.1.

  Follow the procedure on the **Built-in image** tab.
* **Bring your own container**

  In the container scenario, App Service provides a host where a custom container provided by the customer can execute.

  For details on the differences between the two scenarios, see [Things you should know: Web Apps on Linuxï»¿](https://dt-url.net/jm039gu).

  To monitor App Services on Linux, you need to integrate OneAgent within your containerized application.

  Follow the procedure on the **Custom image** tab.

Built-in image

Custom image

## Integrate Dynatrace on built-in image

Azure App Service for Linux allows you to customize its base container at runtime using a [startup script or script commandï»¿](https://dt-url.net/z2234qa) that must be executed in a bash shell or [Azure Cloud Shellï»¿](https://dt-url.net/at034yy). The script can be configured in multiple ways.

### Set startup script command/file at creation time using Azure CLI

```
az webapp create -n <my-app> -g <my-resourcegroup> -p <my-appservice-plan> --runtime <runtime-tag> --startup-file <startup-script/command>
```

### Set script command/file at creation time for an existing App Service

```
az webapp config set -n <my-app> -g <my-resourcegroup> --startup-file <startup-script/command>
```

### Set script command/file using ARM template

Use the [appCommandLineï»¿](https://docs.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-web?pivots=deployment-language-arm-template#siteconfig-1) property of your ARM template to set the startup script/command.

```
{



"acrUseManagedIdentityCreds": false,



"acrUserManagedIdentityId": null,



"alwaysOn": false,



"apiDefinition": null,



"apiManagementConfig": null,



"appCommandLine": "<startup-script/command>",



"appSettings": null,



"autoHealEnabled": false,



"autoHealRules": null,



"autoSwapSlotName": null,



...
```

### Set startup script command/file in the Azure portal

![AppService Linux Portal Startup](https://dt-cdn.net/images/screenshot-2022-12-13-at-13-42-44-1109-8955530cdd.png)

### Script or command?

A startup script is the same as a startup command: it's a command that executes the script (remember to use the path of the script). However, this requires that you package the script along with your application. If you don't want to have this dependency, use startup commands.

The script/command is executed within the container init script, which is implemented differently on each technology stack.

For details on startup commands, see the Azure App Service for Linux documentation on [What are the expected values for the Startup File section when I configure the runtime stack?ï»¿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

### Integrate Dynatrace using a startup script/command

To integrate Dynatrace, the startup script/command needs to have access to a few variables.

Parameter

Description

`$DT_ENDPOINT`

Your Dynatrace API server endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

`$DT_API_TOKEN`

API Token to access the Dynatrace REST APIâ[create an API Token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the **InstallerDownload** scope.

`$DT_INCLUDE`

Configure required code modules, depending on the used technology stack.

* `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
* Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

For details, see [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").

`$START_APP_CMD`

The command to start your application

[What are the expected values for the Startup File section when I configure the runtime stack?ï»¿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

If you use a shell other than bash, make sure to adapt the script appropriately to the shell's character escape requirements.

You can do this in two ways.

* App service settings Recommended
* Setting the values inline

#### Monitoring PHP on NGINX

To monitor both PHP-FPM and NGINX

1. Set `DT_INCLUDE` to `all`.
2. Use the startup script with two additional commands at the end.

   ```
   echo '/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so' >> /etc/ld.so.preload



   /etc/init.d/nginx restart
   ```

#### App service settings

Set the values of the above parameters using [App Settingsï»¿](https://dt-url.net/da239ts)âthis is equivalent to setting environment variablesâand then run this command.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && sh /tmp/installer-wrapper.sh
```

Java Runtime stack

For apps running on the Java Runtime stack in Azure App Service, this installation method may not work as expected in some cases. For example, customers have reported issues with Alpine-based images, where the above command was interpreted as a single string rather than executed as a shell command. This caused the `&&` operator to be treated as part of the `wget` input instead of chaining commands.

If you encounter this behavior, consider using an alternative approach to execute the script (such as a custom startup script or modifying a [custom image](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#install--custom-image "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")).

Alternatively, you can use the calling-only script below, which works for all Linux images.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



sh $installerWrapperInstallationPath
```

#### Setting the values inline

You can set the needed variables only for the command that runs the OneAgent installer.

To do this, you need to set the values before the command as shown below.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh
```

Alternatively, you can use the startup file as shown below.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh $installerWrapperInstallationPath
```

### Example: Integrate into a node.js application using Azure CLI within a bash shell



[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configure the startup command**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-1 "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Restart the web application twice**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-2 "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

#### Step 1 Configure the startup command

```
RESOURCE_GROUP="my-appservice-test"



APPSVC="my-linux-webapp"



DT_ENDPOINT="https://XXXXXX.live.dynatrace.com"



DT_API_TOKEN="XXXXXX"



DT_INCLUDE="nodejs"



START_APP_CMD="pm2 start index.js --no-daemon"



STARTUP_CMD="wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh"



az webapp config set --resource-group $RESOURCE_GROUP --name $APPSVC --startup-file "$STARTUP_CMD"
```

#### Step 2 Restart the web application twice

After you configure the startup command, restart the web application **twice**.

* Restart once to initialize OneAgent installation.
* Restart again to start OneAgent instrumenting your application.

## Integrate Dynatrace on custom image

To integrate OneAgent with the application image, you have two options:

* [Integrate the OneAgent image layer provided by Dynatrace](#layer)
* [Download OneAgent artifacts at image build-time from Dynatrace REST API](#api)

### Option 1: Integrate using Dynatrace offered OneAgent image layer

This option requires that you have Docker v17.05+ installed on your computer.

1. Sign in to Docker with your Dynatrace environment ID as the username and your PaaS token as the password.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Add the following lines to your application image Dockerfile, after the last `FROM` command.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Replace the following placeholders in the template.

   Parameter

   Description

   `<ADDRESS>`

   Your Dynatrace registry endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

   `<TECHNOLOGY>`

   Configure required code modules, depending on the used technology stack.

   * `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
   * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

   For details, see the [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").

   **What if my Docker image is based on Alpine Linux?**

   Dynatrace OneAgent supports Alpine Linuxâbased environments. To use an Alpine Linux compatible OneAgent, use image name `oneagent-codemodules-musl` (as shown in the adapted template below) instead of `oneagent-codemodules`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
3. Build your application image.

   Build the Docker image from your Dockerfile to use it in your Kubernetes environment.

   ```
   docker build -t yourapp .
   ```
4. Restart the web application **twice**.

   * Restart once to initialize the OneAgent install script.
   * Restart again to start OneAgent on the host.

### Option 2: Integrate using installer script from Dynatrace REST API

1. Add the following two lines to your Dockerfile.

   ```
   RUN wget -O /tmp/installer.sh -q "<DT_ENDPOINT>/api/v1/deployment/installer/agent/unix/paas-sh/latest?Api-Token=<DT_API_TOKEN>&flavor=<DT_FLAVOR>&include=<DT_INCLUDE>" && sh /tmp/installer.sh



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Replace the following parameters in the template above.

   Parameter

   Description

   `<DT_ENDPOINT>`

   Your Dynatrace API endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

   `<DT_API_TOKEN>`

   API Token to access the Dynatrace REST APIâ[create an API Token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the **InstallerDownload** scope.

   `<DT_FLAVOR>`

   Configure the required architecture.

   * `default` for standard, glibc-based Linux images
   * `musl` for Alpine Linuxâbased images

   `<DT_INCLUDE>`

   Configure required code modules, depending on the used technology stack.

   * `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
   * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

   For details, see the [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").
2. Build your application image.

   Build the Docker image from your Dockerfile to use it in your Kubernetes environment.

   ```
   docker build -t yourapp .
   ```
3. Restart the web application **twice**.

   * Restart once to initialize the OneAgent install script.
   * Restart again to start OneAgent on the host.

## Additional configuration Optional

Use additional environment variables to configure OneAgent for troubleshooting or advanced networking. You can either set them via your App Service Application settings or, when using a custom container image, configure them within your application image Dockerfile.

### Networking variables

Parameter

Description

`DT_NETWORK_ZONE`

Specifies to use a network zone. For more information, see [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

`DT_PROXY`

When using a proxy, use this environment variable to pass proxy credentials. For more information, see [Set up OneAgent on containers for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

### Additional metadata for process grouping and service detection

When listing multiple tags, you need to put them in double quotes, for example: DT\_TAGS="Tag1=Value1 Tag2=Value2".

Parameter

Description

`DT_LOCALTOVIRTUALHOSTNAME`

Multiple containers are sometimes detected as a single instance (localhost), leading to various problems in, for example, service detection or availability alerts. Use this environment variable to define a unique name for your container instance. For details, see [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Find out how Dynatrace Service Detection v1 detects and names different types of services.")

`DT_APPLICATIONID`

Some technologies don't provide unique application names. In such cases, use this environment variable to provide a unique name. For more information, see [Web server naming issues](/docs/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Find out how Dynatrace Service Detection v1 detects and names different types of services.").

`DT_TAGS`

Applies [custom tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") to your process group.

`DT_CUSTOM_PROP`

Applies [custom metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") to your process group.

`DT_CLUSTER_ID`

If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use case, use this environment variable to **group all processes with the same value**.

`DT_NODE_ID`

If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use case, use this environment variable to **separate process group instances**.

### Validating variables



Parameter

Description

`DT_LOGSTREAM`

Set this variable with `stdout` to configure the OneAgent to log errors to the console. To see additional OneAgent logs, set the log level with `DT_LOGLEVELCON` as follows.

`DT_LOGLEVELCON`

Use this environment variable to define the console log level. Valid options are: `NONE`, `SEVERE`, and `INFO`.

`DT_AGENTACTIVE`

Set to `true` or `false` to enable or disable OneAgent.

## Update OneAgent

Built-in image

Custom image

When an update is available, restart your application to update OneAgent.

Each time you want to leverage a new version of Dynatrace OneAgent, you need to rebuild your local OneAgent code modules and application image. Any newly started pods from this application image will be monitored with the latest version of OneAgent.

If you've specified a default OneAgent installation version for new hosts and applications using [OneAgent update settings](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), your web apps will be automatically monitored by the defined default version of OneAgent.

## Uninstall OneAgent

Built-in image

Custom image

To uninstall OneAgent

1. In Azure portal, go to your web application > **Configuration** > **General settings**.
2. Remove your startup command (leave **Startup Command** empty).
3. Select **Save**.

To uninstall OneAgent, remove references from above described Dynatrace integration from your application image and redeploy the application.

## Potential conflict with Application Insights

OneAgent may conflict with Azure Application Insights agents already instrumenting the application. If you don't see any monitoring data coming in, check if you have turned on Application Insights and re-try with Application Insights turned off.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")