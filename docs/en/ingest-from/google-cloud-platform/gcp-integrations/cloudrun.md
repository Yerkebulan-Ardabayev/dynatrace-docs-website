---
title: Monitor Google Cloud Run managed
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun
scraped: 2026-02-16T21:14:07.528109
---

# Monitor Google Cloud Run managed

# Monitor Google Cloud Run managed

* Latest Dynatrace
* How-to guide
* 11-min read
* Published Sep 09, 2022

Google [Cloud Runï»¿](https://cloud.google.com/run) managed is a compute platform for running containers in a serverless environment. To monitor services running on Google Cloud Run managed using Dynatrace, you need to integrate OneAgent within your containerized application.

Support for Cloud Run managed in the [first generation and second generationï»¿](https://cloud.google.com/run/docs/about-execution-environments) execution environments is currently limited to **Java** and **Node.js**.

## Integrate Dynatrace into your containers

There are several ways to build and deploy containers to Cloud Run, such as with [Cloud Buildï»¿](https://cloud.google.com/build).

While the instructions to integrate Dynatrace may differ depending on the technology stack used to build and deploy, the integration of Dynatrace independently follows the same approach:

1. Add necessary OneAgent binaries to your container image (for example, by either downloading from REST API or copying from the OneAgent image layer).
2. Configure OneAgent with the necessary connection parameters and additional options such as custom tags.
3. Enable process injection for automatic instrumentation of your workloads.

### Prerequisites

Before you begin, you need to take care of the following:

* Get an **access token** to download the Dynatrace OneAgent with `InstallerDownload` scope. For details on access tokens, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

  In the procedures that follow, replace `<DT_TOKEN>` with your actual access token.
* Get the **environment ID**. For details on environment IDs, see [What is a monitoring environment?](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

  In the procedures that follow, replace `<DT_ENV_ID>` with your actual environment ID.
* Get your Dynatrace API endpoint as defined by your [Environment URL](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or alternatively an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

  In the procedures that follow, replace `<DT_ENV_FQDN>` with the actual Dynatrace API endpoint.
* Install [gcloud CLIï»¿](https://cloud.google.com/sdk/docs/install)

After you have completed the above prerequisites, follow one of these procedures (select a tab) to integrate Dynatrace into your containers.

Cloud build with cloudbuild.yaml

Cloud Build without cloudbuild.yaml

Jib

### Integrate into cloud built with `cloudbuild.yaml`

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OneAgent installer**](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#add-oneagent-installer-option-1 "Monitor Java application deployed on Google Cloud Run managed.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure Cloud Build**](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#configure-cloud-build-option-1 "Monitor Java application deployed on Google Cloud Run managed.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Build and deploy**](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#build-and-deploy-option-1 "Monitor Java application deployed on Google Cloud Run managed.")

#### Step 1 Add the OneAgent installer to a Docker image

Requires Docker version 17.05+

Open your Dockerfile and add the following lines to the application image **after** the last `FROM` and **before** your container entrypoint.

```
# FROM ...



ARG DT_API_URL="<DT_ENV_FQDN>/api"



ARG DT_API_TOKEN="<DT_TOKEN>"



ARG DT_ONEAGENT_OPTIONS="flavor=<DT_FLAVOR&include=<DT_TECHNOLOGY>"



ENV DT_HOME="/opt/dynatrace/oneagent"



RUN apt-get update && \



apt-get install -y wget && \



apt-get install unzip && \



mkdir -p "$DT_HOME" && \



wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



rm "$DT_HOME/oneagent.zip"



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



# Run the web service on container startup.



# ENTRYPOINT ...
```

Make sure to substitute the placeholders with your actual values.

* `<DT_ENV_FQDN>` is your actual Dynatrace API endpoint as described in the [Prerequisites](#prerequisites).
* `<DT_TOKEN>` is your actual token as described in the [Prerequisites](#prerequisites).
* `<DT_TECHNOLOGY>` is your OneAgent artefact specific to your images technology-stack like either `java` or `nodejs`.
* `<DT_FLAVOR>` For Alpine Linux based images, choose `musl`, otherwise `default`

The `wget` and `unzip` commands above might fail if they aren't provided by the base image.

Example

A sample Dockerfile as provided by Google via the Getting Started guide on Google Cloud Run with Java, adapted with the instructions provided above.

```
# Use the official maven/Java 11 image to create a build artifact.



# https://hub.docker.com/_/maven



FROM maven:3-jdk-11-slim AS build-env



# Set the working directory to /app



WORKDIR /app



# Copy the pom.xml file to download dependencies



COPY pom.xml .



# Copy local code to the container image.



COPY src ./src



# Download dependencies and build a release artifact.



RUN mvn package -DskipTests



# Use OpenJDK for base image.



# https://hub.docker.com/_/openjdk



# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds



FROM openjdk:11-jre-slim



# Copy the jar to the production image from the builder stage.



COPY --from=build-env /app/target/hello-world-*.jar /hello-world.jar



# Get and enable Dynatrace



ARG DT_API_URL="<DT_ENV_FQDN>/api"



ARG DT_API_TOKEN="<DT_TOKEN>"



ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"



ENV DT_HOME="/opt/dynatrace/oneagent"



RUN apt-get update && \



apt-get install -y wget && \



apt-get install unzip && \



mkdir -p "$DT_HOME" && \



wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



rm "$DT_HOME/oneagent.zip"



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



# Run the web service on container startup.



ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

#### Step 2 Adjust your Google Cloud Build configuration file

Open your [cloudbuild.yamlï»¿](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run#continuous_deployment) file and add the following environment variables and bash commands to the build step:

```
# Build the container image



- name: 'gcr.io/cloud-builders/docker'



args: ['build', '-t', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>', '.']



# Push the container image to Container Registry



- name: 'gcr.io/cloud-builders/docker'



args: ['push', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>']
```

Add the following lines to your args in your deploy step:

```
# Deploy container image to Cloud Run



- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'



entrypoint: gcloud



args:



- beta



- run



- deploy



- $_SERVICE_NAME



- --allow-unauthenticated



- --image=gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>



- --region=$_GCP_REGION



- --execution-environment=<ENVIRONMENT>



- --project=$_PROJECT



- --set-env-vars=



DT_TAGS=$_SERVICE_NAME,



DT_LOGLEVELCON=INFO
```

Make sure to substitute the placeholders with your actual values.

* `<GCP_PROJECT_ID>` is the name of your [Google Cloud projectï»¿](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` is the name and the tag of your image to be built
* `<ENVIRONMENT>` is the execution environment you want to use. Valid options are `gen1` for first generation and `gen2` for second generation.

You can change the `DT_TAGS` environment variable to another value as needed.

#### Step 3 Build and deploy your Cloud Run Service

Edit and run this command:

```
gcloud builds submit \



<SAMPLE_NAME> \



--project <GCP_PROJECT_ID> \



--substitutions \



"_API_KEY=<DT_TOKEN>,\



_TENANT_NAME=<DT_ENV_ID>,\



_TENANT_FQDN=<DT_ENV_FQDN>,\



_IMAGE_NAME_AND_TAG=<YOUR_IMAGE_NAME_AND_TAG>,\



_SERVICE_NAME=<YOUR_SERVICE_NAME>,\



_PROJECT=<GCP_PROJECT_ID>,\



_GCP_REGION=<GCP_REGION>,\" \



--config cloudbuild.yaml
```

Make sure to substitute the placeholders with your actual values.

* `<SAMPLE_NAME>`is the name of your Cloud Run Service
* `<GCP_PROJECT_ID>` is the name of your [Google Cloud projectï»¿](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` is the name and the tag of your image to be built

### Integrate into cloud built without `cloudbuild.yaml`

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OneAgent installer**](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#add-oneagent-installer-option-2 "Monitor Java application deployed on Google Cloud Run managed.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Build and deploy**](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#build-and-deploy-option-2 "Monitor Java application deployed on Google Cloud Run managed.")

#### Step 1 Add the OneAgent installer to a Docker image

Requires Docker version 17.05+

Open your Dockerfile and add the following sample to the application image **after** the last `FROM`.

```
ARG DT_API_URL="<DT_ENV_FQDN>/api"



ARG DT_API_TOKEN="<DT_TOKEN>"



ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"



ENV DT_HOME="/opt/dynatrace/oneagent"



RUN apt-get update && \



apt-get install -y wget && \



apt-get install unzip && \



mkdir -p "$DT_HOME" && \



wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



rm "$DT_HOME/oneagent.zip"



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



# Run the web service on container startup.



ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

Make sure to substitute the placeholders with your actual values.

* `<DT_ENV_FQDN>` is your actual Dynatrace API endpoint as described in the [Prerequisites](#prerequisites).
* `<DT_TOKEN>` is your actual token as described in the [Prerequisites](#prerequisites).

* Technology support is enabled via `include` parameters. For Alpine Linuxâbased environments, use `flavor=musl&include=java`.
* The `wget` and `unzip` commands above might fail if they aren't provided by the base image.

Example

This is a sample Dockerfile as provided by Google via the Getting Started guide on Google Cloud Run with Java, adapted with the instructions provided above.

```
# Use the official maven/Java 11 image to create a build artifact.



# https://hub.docker.com/_/maven



FROM maven:3-jdk-11-slim AS build-env



# Set the working directory to /app



WORKDIR /app



# Copy the pom.xml file to download dependencies



COPY pom.xml .



# Copy local code to the container image.



COPY src ./src



# Download dependencies and build a release artifact.



RUN mvn package -DskipTests



# Use OpenJDK for base image.



# https://hub.docker.com/_/openjdk



# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds



FROM openjdk:11-jre-slim



# Copy the jar to the production image from the builder stage.



COPY --from=build-env /app/target/hello-world-*.jar /hello-world.jar



# Get and enable Dynatrace



ARG DT_API_URL="<DT_ENV_FQDN>/api"



ARG DT_API_TOKEN="<DT_TOKEN>"



ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"



ENV DT_HOME="/opt/dynatrace/oneagent"



RUN apt-get update && \



apt-get install -y wget && \



apt-get install unzip && \



mkdir -p "$DT_HOME" && \



wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



rm "$DT_HOME/oneagent.zip"



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



# Run the web service on container startup.



ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

#### Step 2 Build and deploy your Cloud Run Service

To build your Cloud Run Service, edit and run the following command within your project directory:

```
gcloud builds submit --region=<GCP_REGION> --tag gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

To deploy your Cloud Run Service, edit and run the following command:

```
gcloud run deploy <YOUR_SERVICE_NAME> --image gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

Make sure to substitute the placeholders with your actual values.

* `<GCP_REGION>` is the name of the [Google Cloud regionï»¿](https://cloud.google.com/compute/docs/regions-zones) you deploy
* `<GCP_PROJECT_ID>` is the name of your [Google Cloud projectï»¿](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` is the name and the tag of your image to be built
* `<YOUR_SERVICE_NAME>` is the name of the service that will be displayed in Dynatrace

### Integrate using Jib container tool

Google's [Jibï»¿](https://github.com/GoogleContainerTools/jib) container tool builds optimized Docker and OCI images for your Java applications without a Docker daemonâand without requiring deep mastery of Docker best practices. It is available as plugins for Maven and Gradle and as a Java library.

In the GitHub repository for Jib, you can find a [sample integration for the Google StackDriver Java agentï»¿](https://github.com/GoogleContainerTools/jib/blob/master/examples/java-agent/build.gradle) that follows the same pattern as the Dynatrace integration (Download, Configure, and Inject). You can adapt this blueprint to your needs for integrating Dynatrace using jib.

## Additional configuration

You can use additional environment variables to configure, for example, troubleshooting or advanced networking settings.

| Name | Description |
| --- | --- |
| **Networking** |  |
| `DT_NETWORK_ZONE` | Specifies to use a network zone. For details, see [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace."). |
| `DT_PROXY` | When using a proxy, use this environment variable to pass proxy credentials. For details, see [Set up OneAgent on containers for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.") |
| **Additional metadata for Process Grouping / Service Detection** |  |
| `DT_LOCALTOVIRTUALHOSTNAME` | Multiple containers are sometimes detected as a single instance (localhost), leading to various problems in, for example, service detection or availability alerts. Use this environment variable to define a unique name for your container instance. For details, see [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Find out how Dynatrace Service Detection v1 detects and names different types of services.") |
| `DT_APPLICATIONID` | Some technologies don't provide unique application names. In such cases, use this environment variable to provide a unique name. For details, see [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Find out how Dynatrace Service Detection v1 detects and names different types of services.") |
| `DT_TAGS` | Applies [custom tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") to your process group |
| `DT_CUSTOM_PROP` | Applies [custom metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") to your process group |
| `DT_CLUSTER_ID` | If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use-case, use this environment variable to **group all processes with the same value**. |
| `DT_NODE_ID` | If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use-case, use this environment variable to **separate process group instances** |
| **Troubleshooting** |  |
| `DT_LOGSTREAM` | Set this variable with `stdout` to configure agent to log errors into console. To see additional agent logs set the log level with DT\_LOGLEVELCON as below. |
| `DT_LOGLEVELCON` | Use this environment variable to define the console log level. Valid options are `NONE`, `INFO`, `WARNING`, `SEVERE` in order to increase log level. |
| `DT_AGENTACTIVE` | `true` or `false` to enable or disable OneAgent. |

## Verify that the integration was successful

After the build and deploy, you should start seeing your Cloud Run service in Dynatrace.

### Verify via service overview

Check your service's overview within Dynatrace for your instrumented application.

The service will show up in Dynatrace after running the newly built version and calling it at least once via, for example, a webrequest.

### Verify via host overview

You can filter for containers in the host overview to filter by **Monitoring Mode** with `Standalone/PaaS`.

## Known limitations

* **No host metrics for Gen1**

  The first generation of the GCR execution environment, also referred to as Gen1, comes with intentionally increased security limitations. As a consequence, some OneAgent functionalities cannot work in this runtime and are not available. For example, metrics on the **Hosts** page such as `CPU Usage` and `Memory Usage` are not available.
* **GCR instances detected as hosts**

  GCR execution environments are currently displayed on the **Hosts** page, with proper detection of GCP properties and the memory limit of each of these runtime (container) instances, not on the [**Container groups** page](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring"). Container metrics are not available.
* **Possible startup overhead**

  Because each revision of Google Cloud Run scales automatically to the number of container instances needed to handle incoming requests, such cold starts might appear more often than on other environments, thus increasing overall startup overhead.

## Update OneAgent

Each time you want to leverage a new version of Dynatrace OneAgent, you must rebuild and redeploy.

If you've specified a default OneAgent installation version for new hosts and applications using [OneAgent update settings](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), your application will be automatically monitored by the defined default version of OneAgent.

## Uninstall OneAgent

To uninstall OneAgent from application-only monitoring, remove references from your application or Docker image and redeploy the application.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")