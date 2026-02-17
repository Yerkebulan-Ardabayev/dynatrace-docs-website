# Dynatrace Documentation: ingest-from/google-cloud-platform

Generated: 2026-02-17

Files combined: 57

---


## Source: cloud-run-monitoring.md


---
title: Google Cloud Run monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring
scraped: 2026-02-17T05:06:30.054553
---

# Google Cloud Run monitoring

# Google Cloud Run monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Run.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_run\_revision/default\_metrics | Billable Instance Time | Second | run.googleapis.com/container/billable\_instance\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Allocation | Second | run.googleapis.com/container/cpu/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Utilization | Percent | run.googleapis.com/container/cpu/utilizations |
| cloud\_run\_revision/default\_metrics | Instance Count | Count | run.googleapis.com/container/instance\_count |
| cloud\_run\_revision/default\_metrics | Max Concurrent Requests | Count | run.googleapis.com/container/max\_request\_concurrencies |
| cloud\_run\_revision/default\_metrics | Container Memory Allocation | GibiByte | run.googleapis.com/container/memory/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container Memory Utilization | Percent | run.googleapis.com/container/memory/utilizations |
| cloud\_run\_revision/default\_metrics | Received Bytes | Byte | run.googleapis.com/container/network/received\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Sent Bytes | Byte | run.googleapis.com/container/network/sent\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Request Count | Count | run.googleapis.com/request\_count |
| cloud\_run\_revision/default\_metrics | Request Latency | MilliSecond | run.googleapis.com/request\_latencies |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: cloudrun.md


---
title: Monitor Google Cloud Run managed
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun
scraped: 2026-02-17T21:19:35.952979
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


---


## Source: cloud-functions-monitoring.md


---
title: Google Cloud Functions monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring
scraped: 2026-02-17T21:25:00.053481
---

# Google Cloud Functions monitoring

# Google Cloud Functions monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Functions.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_function/default\_metrics | Active instances | Count | cloudfunctions.googleapis.com/function/active\_instances |
| cloud\_function/default\_metrics | Executions | Count | cloudfunctions.googleapis.com/function/execution\_count |
| cloud\_function/default\_metrics | Execution times | NanoSecond | cloudfunctions.googleapis.com/function/execution\_times |
| cloud\_function/default\_metrics | Network egress | Byte | cloudfunctions.googleapis.com/function/network\_egress |
| cloud\_function/default\_metrics | Memory usage | Byte | cloudfunctions.googleapis.com/function/user\_memory\_bytes |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: opentelemetry-on-gcf-dotnet.md


---
title: Integrate on Google Cloud Functions .NET
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet
scraped: 2026-02-17T04:56:13.328814
---

# Integrate on Google Cloud Functions .NET

# Integrate on Google Cloud Functions .NET

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jul 25, 2023

The `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` NuGet package provides APIs for tracing server-side .NET Google Cloud Function (GCF) invocations.

## Prerequisites

* [Set up OpenTelemetry monitoring for Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").
* Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions version 1.273+
* Cloud Functions product versions: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry .NET integration on Google Cloud Functions, run the command below in the root directory of your Google Cloud Function project.

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions
```

This adds the latest version of the `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` NuGet package as a dependency on your project.

## Trace export

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Initialize tracing**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#initialize "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Instrument a handler function**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#instrument "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")

## Step 1 Initialize tracing

The initialization code for GCF tracing in your `Function.cs` file could look as follows (where `Function` is the configured GCF handler class):

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions;



using Google.Cloud.Functions.Framework;



using Microsoft.AspNetCore.Http;



using OpenTelemetry;



using OpenTelemetry.Trace;



namespace Examples.GcfFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



static Function()



{



DynatraceSetup.InitializeLogging();



TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



.AddGoogleCloudFunctionsInstrumentation()



.Build();



}



}



}
```

## Step 2 Instrument a handler function

Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions version 1.273 Only tracing of incoming calls for HTTP-triggered functions is supported.

To instrument an HTTP-triggered function to trace incoming calls, in addition to the [initialization code above](#initialization), wrap the GCF function handler method using either `GoogleCloudFunctionsWrapper.Trace` or `GoogleCloudFunctionsWrapper.TraceAsync` as shown in the following example.

```
public Task HandleAsync(HttpContext context)



{



return GoogleCloudFunctionsWrapper.TraceAsync(



TracerProvider,



() => HandleInternalAsync(context), context);



}



private Task HandleInternalAsync(HttpContext context)



{



// This is just an example of function handler and should be replaced by actual code.



return Task.CompletedTask;



}
```

## Cold start

When the function handler is invoked for the first time after a [cold startï»¿](https://cloud.google.com/functions/docs/concepts/exec#cold_starts), the instrumentation initialization method `AddGoogleCloudFunctionsInstrumentation`
makes additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://cloud.google.com/compute/docs/metadata/overview). This metadata is used to set the required attributes for Dynatrace to process
the span ("Activity" in .NET terminology).

### Limitations

The additional HTTP requests from `AddGoogleCloudFunctionsInstrumentation` method might cause unhandled exceptions during the initialization phase (for example, `HttpRequestException` in the case of a broken network connection). If your code is set to avoid monitoring when startup fails, exceptions will still be caught.

## Span flush

By default, all wrapping `Trace/TraceAsync` methods automatically perform a flush operation before the end of function invocation to ensure that all spans are exported properly. Because span flushing becomes part of the function's execution logic, it might result in a longer execution time.

To disable flushing after every invocation, you can provide a configuration parameter with the flag `ForceFlushAfterEachInvocation` set to `false` in the `AddGoogleCloudFunctionsInstrumentation` method. Spans will still be periodically exported in the background.

```
TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



// Setting ForceFlushAfterEachInvocation to false disables the flushing after every function invocation.



.AddGoogleCloudFunctionsInstrumentation(c => c.ForceFlushAfterEachInvocation = false)



.Build();
```

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: opentelemetry-on-gcf-nodejs.md


---
title: Integrate on Google Cloud Functions Node.js
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs
scraped: 2026-02-17T21:27:01.706196
---

# Integrate on Google Cloud Functions Node.js

# Integrate on Google Cloud Functions Node.js

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Sep 26, 2025

The [`@dynatrace/opentelemetry-gcf`ï»¿](https://dt-url.net/zm03ye8) module provides APIs for tracing Node.js on Google Cloud Functions (GCF).

## Prerequisites

Make sure you have followed the instructions on how to [integrate OpenTelemetry on Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").

* So far, only [HTTP triggersï»¿](https://dt-url.net/os23yfz) are supported.
* Cloud Function product version: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry Node.js integration on Google Cloud Functions, run the command below in the root directory of your Google Cloud Function project.

```
npm install --save @dynatrace/opentelemetry-gcf
```

This will install the latest version of the [`@dynatrace/opentelemetry-gcf`ï»¿](https://dt-url.net/zm03ye8) module from NPM. Note that this library by itself is not enough to start tracing your Google Cloud Functions.
See the [Usage](#usage) section below for the remaining required steps.

## Usage

To export traces to Dynatrace

1. Select one of the two ways below to initialize tracing.

   * `NodeTracerProvider` used to initialize tracing is more lightweight than `NodeSDK`.
   * `NodeSDK` is typically used if you're interested in additional OpenTelemetry signals such as metrics.

   Using NodeTracerProvider (recommended)

   Using NodeSDK

   Install the required OpenTelemetry packages with the command below.

   ```
   npm install --save @opentelemetry/sdk-trace-node @opentelemetry/semantic-conventions
   ```

   After you install the packages, initialize tracing using the following snippet as an example.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



   const processor = new DtSpanProcessor(new DtSpanExporter());



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource",



   }),



   sampler: new DtSampler(),



   // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



   spanProcessors: [processor]



   // ...other configurations



   });



   provider.register({



   propagator: new DtTextMapPropagator(),



   // ...other configurations



   });
   ```

   Install the required OpenTelemetry packages with the command below.

   ```
   npm install --save @opentelemetry/sdk-node @opentelemetry/semantic-conventions
   ```

   After you install the packages, initialize tracing using the following snippet as an example.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeSDK } = require('@opentelemetry/sdk-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



   const sdk = new NodeSDK({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   spanProcessor: new DtSpanProcessor(new DtSpanExporter()),



   textMapPropagator: new DtTextMapPropagator(),



   // ...other configurations



   });



   sdk.start().then(() => {



   // Resources have been detected and SDK is started



   });
   ```
2. Start the root Google Cloud Function server span, using one of the two general patterns in OpenTelemetry below.

   Start an active span (recommended)

   Start the span and activate it later

   Example that starts and immediately activates a span inside a Google Cloud Function:

   ```
   const { startActiveHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   await startActiveHttpSpan(req, async (span) => {



   let error;



   try {



   // do something



   } catch (e) {



   error = e;



   }



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   });



   }
   ```

   Example that starts a span inside a Google Cloud Function and later activates it within the same function.

   ```
   const { context, trace, ROOT_CONTEXT } = require('@opentelemetry/api');



   const { startHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   const span = await startHttpSpan(req);



   let error;



   await context.with(trace.setSpan(ROOT_CONTEXT, span), async () => {



   try {



   // do something



   } catch (e) {



   error = e;



   }



   });



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   }
   ```

## Compatibility

| OneAgent version | OpenTelemetry API | OpenTelemetry SDK |
| --- | --- | --- |
| 1.243 - 1.255 | 1.x.y | 1.0.x |
| 1.257+ | 1.x.y | 1.0.x - 1.7.x |
| 1.259+ | 1.x.y | 1.0.x - 1.8.x |
| 1.261+ | 1.x.y | 1.0.x - 1.9.x |
| 1.265+ | 1.x.y | 1.0.x - 1.10.x |
| 1.273+ | 1.x.y | 1.0.x - 1.15.x |
| 1.279+ | 1.x.y | 1.0.x - 1.17.x |
| 1.283+ | 1.x.y | 1.0.x - 1.18.x |
| 1.285+ | 1.x.y | 1.0.x - 1.20.x |
| 1.289+ | 1.x.y | 1.0.x - 1.22.x |
| 1.293+ | 1.x.y | 1.0.x - 1.24.x |
| 1.297+ | 1.x.y | 1.0.x - 1.25.x |
| 1.303+ | 1.x.y | 1.0.x - 1.26.x |
| 1.307+ | 1.x.y | 1.0.x - 1.29.x |
| 1.313+ | 1.x.y | 1.0.x - 1.30.x |
| 1.327+ | 1.x.y | 1.0.x - 2.0.x |
| 1.331+ | 1.x.y | 1.0.x - 2.2.x |

Dynatrace version 1.327+ The `@dynatrace/opentelemetry-gcf` module supports OpenTelemetry SDK V2. To use V2 (instead of V1), override the version of `@dynatrace/opentelemetry-core` module (required by `@dynatrace/opentelemetry-gcf`) with a version that supports OpenTelemetry SDK V2.

1. From the table above, choose a version that supports OpenTelemetry SDK V2.
2. In your `package.json` file, adding the `overrides` section and specify one of the versions of the `@dynatrace/opentelemetry-core` module to enforce.
3. Run `npm install` to apply the changes.

Example:

```
{



"dependencies": {



"@dynatrace/opentelemetry-gcf": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Once `@dynatrace/opentelemetry-gcf` is changed to use OpenTelemetry SDK V2 by default, this override won't be needed anymore.

## Cold start

Starting a Google Cloud Function span during [cold startsï»¿](https://dt-url.net/j543yr9) produces additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://dt-url.net/jc83y1m) and set the attributes required for Dynatrace to process the spans.

## Span flush

To ensure that spans are exported properly, you need to flush the spans before a function's response is sent to the client. For details on this limitation, see [Signalling function terminationï»¿](https://dt-url.net/5ta3ywp).

You can use `endHttpSpan()` and `flushSpans()` separately instead of `endHttpSpanAndFlush()` when needed.

Flushing spans in the function's code results in longer execution times, as this operation becomes part of the function's execution logic. To avoid this, you can omit the flush operation. Spans will still be periodically exported in the background.

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Caveats

You need to pay special attention to cases like unhandled exceptions or function timeouts. If not handled properly, they could lead to a non-ended, and therefore non-exported, span.

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: opentelemetry-on-gcf-python.md


---
title: Integrate on Google Cloud Functions Python
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python
scraped: 2026-02-17T04:56:03.508136
---

# Integrate on Google Cloud Functions Python

# Integrate on Google Cloud Functions Python

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 16, 2023

The `dynatrace-opentelemetry-gcf` [packageï»¿](https://pypi.org/project/dynatrace-opentelemetry-gcf) provides APIs for tracing Python Google Cloud Functions (GCF).

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.") before using the packages below.

* dynatrace-opentelemetry-gcf version 1.247+
* Cloud Functions product version: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry Python integration on Google Cloud Functions, add the following line to the `requirements.txt` file of your function:

```
dynatrace-opentelemetry-gcf
```

This adds the latest version of the `dynatrace-opentelemetry-gcf` package as a dependency to your function. For more information about managing dependencies, consult the [GCF documentation for Pythonï»¿](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).

## Trace export

To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler function](#instrument).

### Initialize tracing

Select one of the following ways to initialize tracing:

* `configure_dynatrace` functionâThis is the recommended option unless you need to manually set up tracing components.

  Example with `configure_dynatrace` (recommended)

  ```
  from opentelemetry.sdk.resources import Resource



  from opentelemetry.semconv.resource import ResourceAttributes



  from dynatrace.opentelemetry.tracing.api import configure_dynatrace



  tracer_provider = configure_dynatrace(



  resource=Resource.create({"my.resource.attribute": "My Resource"})



  )
  ```
* Manual tracing setupâThis allows for a more fine-grained setup of tracing components.

  Example with manual tracing setup

  ```
  from opentelemetry.propagate import set_global_textmap



  from opentelemetry.sdk.resources import Resource



  from opentelemetry.sdk.trace import TracerProvider



  from opentelemetry.semconv.resource import ResourceAttributes



  from opentelemetry.trace import set_tracer_provider



  from dynatrace.opentelemetry.tracing.api import (



  DtSampler,



  DtSpanProcessor,



  DtTextMapPropagator,



  )



  span_processor = DtSpanProcessor()



  tracer_provider = TracerProvider(



  sampler=DtSampler(),



  resource=Resource.create({"my.resource.attribute": "My Resource"}),



  )



  tracer_provider.add_span_processor(span_processor)



  set_global_textmap(DtTextMapPropagator())



  set_tracer_provider(tracer_provider)
  ```

The tracing setup code should be implemented to set up tracing only once before any other third-party module is imported. If you use `isort` to sort your imports, we suggest that you [deactivate itï»¿](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) while importing the tracing setup module, as shown in the following example:

```
# isort: off



import setup_tracing  # import the module containing your setup code



# isort: on



# import other modules
```

### Instrument a handler function

Use the `wrap_handler` decorator to instrument your handler function as shown in the following example:

```
import flask



from dynatrace.opentelemetry.gcf import wrap_handler



@wrap_handler



def handler(request: flask.Request) -> flask.Response:



# From here the created span is available in the OpenTelemetry context as the current span.



# do something ...



return flask.Response("Hello World", 200)
```

## Cold start

When the wrapped handler is invoked for the first time after [cold startï»¿](https://cloud.google.com/functions/docs/concepts/exec#cold_starts), the decorator will make additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://cloud.google.com/compute/docs/metadata/overview). This metadata is used to set the required attributes for Dynatrace to process the span.

## Span flush

By default, the `wrap_handler` decorator automatically performs a flush operation when the decorated function exits to ensure that spans are exported properly. However, flushing spans results in longer execution time, because this operation becomes part of the function's execution logic.

By providing an additional parameter to the decorator, `@wrap_handler(flush_on_exit=False)`, you can disable the flushing after every invocation. Spans will still be periodically exported in the background.

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Limitations

* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: opentelemetry-on-gcf.md


---
title: Set up OpenTelemetry monitoring for Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf
scraped: 2026-02-17T04:56:46.223584
---

# Set up OpenTelemetry monitoring for Google Cloud Functions

# Set up OpenTelemetry monitoring for Google Cloud Functions

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Mar 31, 2025

Dynatrace uses [OpenTelemetryï»¿](https://dt-url.net/y903u4j) to monitor Google Cloud Functions invocations.

For that purpose, Dynatrace provides language-specific packagesâsuch as [`@dynatrace/opentelemetry-gcf` for Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace."), [`dynatrace-opentelemetry-gcf` for Python](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Monitor Google Cloud Functions with OpenTelemetry for Python and Dynatrace."), and [`Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` for .NET](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")âthat can be used in combination with default OpenTelemetry SDKs and APIs.

## Prerequisites

* Dynatrace version 1.240+
* OneAgent version 1.193+ for all OneAgents participating in a trace
* Go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.

## Installation

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Select a configuration method**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#choose-config-method "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Specify a Dynatrace API endpoint**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#specify-endpoint "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Apply the configuration to your Google Cloud function**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#apply-config "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument the function code**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#instrument-code "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")

## Step 1 Select a configuration method

1. In Dynatrace,  **Search** for **Deploy OneAgent** app and select it.
2. Under **Download Dynatrace OneAgent**, select **Set up** > **Google Cloud Functions**.
3. On the **Enable Monitoring for Google Cloud Functions** page, under **How will you configure your Google Cloud Functions?**, select your preferred method from the dropdown menu. Make sure you set all properties for the selected method before copying the generated configuration snippets.

## Step 2 optional Specify a Dynatrace API endpoint Optional

If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.

To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the Google Cloud function that you want to monitor.

### Step 3 Apply the configuration to your Google Cloud function

Configure with JSON file

Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your Google Cloud Functions deployment.

Configure with environment variables

On **Enable Monitoring for Google Cloud Functions**, under **Use the following values to configure your monitored Google Cloud Functions**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your Google Cloud function configuration. For details, see [Using environment variablesï»¿](https://cloud.google.com/functions/docs/configuring/env-var).

## Step 4 Instrument the function code

Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution:

* **Node.js:** [Integrate on Google Cloud Functions Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")
* **Python:** [Integrate on Google Cloud Functions Python](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Monitor Google Cloud Functions with OpenTelemetry for Python and Dynatrace.")
* **Go:** [Integrate on Google Cloud Functions GoLang](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Monitor Google Cloud Functions with OpenTelemetry for Go and Dynatrace.")
* **.NET:** [Integrate on Google Cloud Functions .NET](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")

## Known limitations

The Dynatrace Google Cloud Functions integration doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace OneAgent, this results in **unmonitored hosts**.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: otel-gcf-go.md


---
title: Trace Google Cloud Functions in Go with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go
scraped: 2026-02-17T21:25:44.502384
---

# Trace Google Cloud Functions in Go with OpenTelemetry

# Trace Google Cloud Functions in Go with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 9-min read
* Updated on Nov 13, 2023

This guide shows how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace. To learn more about how Dynatrace works with OpenTelemetry, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

To learn about how to monitor Google Cloud Functions with Dynatrace-enhanced OpenTelemetry traces, see [Integrate on Google Cloud Functions GoLang](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Monitor Google Cloud Functions with OpenTelemetry for Go and Dynatrace.").

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.
* Cloud Functions Go Runtime 1.16+

## Instrument Google Cloud Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Google Cloud Functions.

To instrument your Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OpenTelemetry dependencies**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-dependencies "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OpenTelemetry**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-setup "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument the function entry point**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#instrument-handler "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument outgoing requests**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#outgoing-instrument "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")

### Step 1 Add OpenTelemetry dependencies

Use the following commands to add the required OpenTelemetry dependencies to your function:

```
go get go.opentelemetry.io/otel



go get go.opentelemetry.io/otel/sdk



go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```

### Step 2 Set up OpenTelemetry

To make sure traces are collected, linked, and exported to Dynatrace, you need to set up and configure OpenTelemetry accordingly. For this, the Dynatrace endpoint and an authentication token are required.

To determine the endpoint

1. Open Dynatrace.
2. Check the address line of your browser. The URL will match one of the following patterns:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Replace the `...` part with `api/v2/otlp` to get the URL you will need to configure the OpenTelemetry exporter.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

To create an authentication token

1. Go to **Access Tokens** > **Generate new token**.
2. Provide a **Token name**.
3. In the **Search scopes** box, search for `Ingest OpenTelemetry traces` and select the checkbox.
4. Select **Generate token**.
5. Select **Copy** to copy the token to your clipboard.
6. Save the token in a safe place; you can't display it again, and you will need it to configure the OpenTelemetry exporter.

Here is how to set up the OpenTelemetry tracing pipeline:

```
package otelsetup



import (



"context"



"log"



"go.opentelemetry.io/otel"



"go.opentelemetry.io/otel/exporters/otlp/otlptrace"



"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"



"go.opentelemetry.io/otel/propagation"



"go.opentelemetry.io/otel/sdk/resource"



sdk "go.opentelemetry.io/otel/sdk/trace"



semconv "go.opentelemetry.io/otel/semconv/v1.7.0"



)



func InitTracing(serviceName string, serviceVersion string) *sdk.TracerProvider {



client := otlptracehttp.NewClient()



exporter, err := otlptrace.New(context.Background(), client)



if err != nil {



log.Fatal(err)



}



// create resource



r, err := resource.Merge(



resource.Default(),



resource.NewWithAttributes(



// customizable resource attributes



semconv.SchemaURL,



semconv.ServiceNameKey.String(serviceName),



semconv.ServiceVersionKey.String(serviceVersion),



),



)



tracerProvider := sdk.NewTracerProvider(



sdk.WithBatcher(exporter),



sdk.WithResource(r),



)



otel.SetTracerProvider(tracerProvider)



// setup W3C trace context as global propagator



otel.SetTextMapPropagator(propagation.TraceContext{})



return tracerProvider



}
```

To configure the exporter to your tenant, add the following environment variables when deploying your Google Cloud function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: set it to the previously determined endpoint.
* `OTEL_EXPORTER_OTLP_HEADERS`: set it to `Authorization=Api-Token <TOKEN>`, where `<TOKEN>` is the previously created authentication token.

Alternatively, the endpoint and authentication token can be configured in code by providing them as options to `otlptracehttp.NewClient`.

### Step 3 Instrument the function entry point

To instrument invocations to a Google Cloud Function with OpenTelemetry, you need to

1. Create a span around the entry point of the function to trace invocations.
2. Extract and link the parent span from the propagated context. (To learn about W3C Trace Context, see our [W3C Trace Contextï»¿](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/) introduction.)

For certain libraries, OpenTelemetry Go already provides [instrumentationsï»¿](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation) that you can use to take care of these things.

The following sections show you how to instrument certain types of Google Cloud Functions:

* [Instrument an HTTP Google Cloud Function](#instrument-http-handler)
* [Instrument a Pub/Sub Google Cloud Function](#instrument-pubsub-handler)

#### Instrument an HTTP Google Cloud Function

The entry point of an HTTP Google Cloud Function mostly matches the standard `http.Handler` interface. OpenTelemetry Go already provides an instrumentation for this interface. To add it as a dependency to your function, use the following command:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Because this instrumentation works with an `http.Handler` interface, it requires your entry point function to have the name `ServeHTTP`. Also, because the Go Runtime might terminate right after a function invocation, spans must be exported to Dynatrace beforehand.

To take care of this, create a wrapper function that instruments your actual handler and flushes the spans after invocation:

```
package instrumentor



import (



"context"



"net/http"



"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



semconv "go.opentelemetry.io/otel/semconv/v1.7.0"



"go.opentelemetry.io/otel/trace"



)



type Flush interface {



ForceFlush(context.Context) error



}



type HttpHandler = func(w http.ResponseWriter, r *http.Request)



func InstrumentedHandler(functionName string, function HttpHandler, flusher Flush) HttpHandler {



opts := []trace.SpanStartOption{



// customizable span attributes



trace.WithAttributes(semconv.FaaSTriggerHTTP),



}



// create instrumented handler



handler := otelhttp.NewHandler(



http.HandlerFunc(function), functionName, otelhttp.WithSpanOptions(opts...),



)



return func(w http.ResponseWriter, r *http.Request) {



// call the actual handler



handler.ServeHTTP(w, r)



// flush spans



flusher.ForceFlush(r.Context())



}



}
```

Putting everything together, here is how you use it in your function:

```
package myfunction



import (



"net/http"



"instrumentor"



"otelsetup"



)



var InstrumentedHandler instrumentor.HttpHandler



func init() {



tracerProvider := otelsetup.InitTracing("my-service", "1.0.0")



InstrumentedHandler = instrumentor.InstrumentedHandler("my-function", Handler, tracerProvider)



}



func Handler(w http.ResponseWriter, r *http.Request) {



// Your code goes here



}
```

When deploying your function to GCP, make sure to use `InstrumentedHandler` as the entry point to your Google Cloud Function.

#### Instrument a Pub/Sub Google Cloud Function

A Pub/Sub Google Cloud Function is triggered by the [Pub/Sub messageï»¿](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) event. The event is unmarshalled by GCP into a message object that matches the type you defined in the entry point of your function. This type usually looks similar to the following:

```
type PubSubMessage struct {



Data        []byte            `json:"data"`



Attributes  map[string]string `json:"attributes"`



MessageId   string            `json:"messageId"`



PublishTime string            `json:"publishTime"`



OrderingKey string            `json:"orderingKey"`



}
```

OpenTelemetry currently does not provide an instrumentation for Pub/Sub, so instrumenting a Pub/Sub Google Cloud Function requires a little more work.

In the following snippet, you can see how to create a wrapper function that instruments invocations to your Pub/Sub handler. This wrapper creates the corresponding span and uses the `Attributes` map on the `PubSubMessage` to extract and link to the parent span from the propagated context.

```
package instrumentor



import (



"context"



"fmt"



"go.opentelemetry.io/otel"



"go.opentelemetry.io/otel/codes"



"go.opentelemetry.io/otel/propagation"



semconv "go.opentelemetry.io/otel/semconv/v1.7.0"



"go.opentelemetry.io/otel/trace"



)



const (



instrumentationName = "my.company.com/my-pubsub-handler-instrumentation-name"



instrumentationVer  = "0.1.0"



)



type PubSubHandler = func(context.Context, PubSubMessage) error



type Flush interface {



ForceFlush(context.Context) error



}



func InstrumentedHandler(topicID string, handler PubSubHandler, flush Flush) PubSubHandler {



return func(ctx context.Context, msg PubSubMessage) error {



// create span



ctx, span := beforePubSubHandlerInvoke(ctx, topicID, msg)



defer span.End()



// call actual handler function



err := handler(ctx, msg)



// update span with handler result



afterPubSubHandlerInvoke(span, err)



// flush spans



flush.ForceFlush(ctx)



return err



}



}



func beforePubSubHandlerInvoke(ctx context.Context, topicID string, msg PubSubMessage) (context.Context, trace.Span) {



if msg.Attributes != nil {



// extract propagated span



propagator := otel.GetTextMapPropagator()



ctx = propagator.Extract(ctx, propagation.MapCarrier(msg.Attributes))



}



opts := []trace.SpanStartOption{



trace.WithSpanKind(trace.SpanKindConsumer),



trace.WithAttributes(



//customizable attributes



semconv.FaaSTriggerPubsub,



semconv.MessagingSystemKey.String("pubsub"),



semconv.MessagingDestinationKey.String(topicID),



semconv.MessagingDestinationKindTopic,



semconv.MessagingOperationProcess,



semconv.MessagingMessageIDKey.String(msg.MessageId),



),



}



tracer := otel.GetTracerProvider().Tracer(



instrumentationName, trace.WithInstrumentationVersion(instrumentationVer),



)



return tracer.Start(ctx, fmt.Sprintf("%s process", topicID), opts...)



}



func afterPubSubHandlerInvoke(span trace.Span, err error) {



if err != nil {



span.RecordError(err)



span.SetStatus(codes.Error, err.Error())



}



}
```

Putting everything together, here is how to use the instrumented handler in your function:

```
package myfunction



import (



"context"



"instrumentor"



"otelsetup"



)



var InstrumentedHandler instrumentor.PubSubHandler



func init() {



tracerProvider := otelsetup.InitTracing("my-service", "1.0.0")



InstrumentedHandler = instrumentor.InstrumentedHandler("my-topic", Handler, tracerProvider)



}



func Handler(ctx context.Context, msg PubSubMessage) error {



// Your code goes here



return nil



}
```

When deploying your function to GCP, make sure to use `InstrumentedHandler` as the entry point to your Google Cloud Function.

### Step 4 Instrument outgoing requests

To achieve end-to-end tracing, it is important to also make sure your outgoing requests are instrumented.

The following sections show how to instrument certain outgoing requests:

* [Instrument outgoing HTTP requests](#outgoing-http-instrument)
* [Instrument Pub/Sub publish requests](#pubsub-publish-instrument)

OpenTelemetry Go uses `context.Context` to link a newly created span to its parent, so when using an instrumentation or creating a span manually, make sure to pass it the `context.Context` instance that was passed to your Google Cloud Function (or an instance derived from it). Otherwise, your trace will not be linked properly.

#### Instrument outgoing HTTP requests

OpenTelemetry Go provides an instrumentation for tracing outgoing HTTP calls. Add it as a dependency to your function by using the following command:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Here is how you can use this instrumentation in your code:

```
import (



"context"



"net/http"



"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



)



func makeHttpRequest(ctx context.Context, url string) {



// create an instrumented HTTP client



client := http.Client{Transport: otelhttp.NewTransport(http.DefaultTransport)}



req, err := http.NewRequestWithContext(ctx, "GET", url, nil)



if err != nil {



// error handling



return



}



res, err := client.Do(req)



if err != nil {



// error handling



return



}



defer res.Body.Close()



// response handling code goes here



}
```

* Do not use convenience functions such as `GET` or `POST` on the standard `http.Client`, because they do not accept a `context.Context` object. To make sure that your HTTP request is properly linked, either create a request with a context object as in the sample above, or use one of the convenience functions (such as `otelhttp.Get` or `otelhttp.Put`) of the HTTP instrumentation.
* Make sure to close or fully read the response body. Otherwise, the outgoing request will not be instrumented properly.

#### Instrument Pub/Sub publish request

For the Pub/Sub client, there is currently no instrumentation in OpenTelemetry Go. Check out the following snippet to see how you can use the OpenTelemetry Go API to instrument Pub/Sub publish operations:

```
import (



"context"



"fmt"



"cloud.google.com/go/pubsub"



"go.opentelemetry.io/otel"



"go.opentelemetry.io/otel/codes"



"go.opentelemetry.io/otel/propagation"



semconv "go.opentelemetry.io/otel/semconv/v1.7.0"



"go.opentelemetry.io/otel/trace"



)



const (



instrumentationName = "my.company.com/my-pubsub-instrumentation-lib"



instrumentationVer  = "0.1.0"



)



func PublishMessage(ctx context.Context, client *pubsub.Client, msg *pubsub.Message, topicID string) (string, error) {



// create span



ctx, span := beforePublishMessage(ctx, topicID, msg)



defer span.End()



// Send Pub/Sub message



messageID, err := client.Topic(topicID).Publish(ctx, msg).Get(ctx)



// enrich span with publish result



afterPublishMessage(span, messageID, err)



return messageID, err



}



func beforePublishMessage(ctx context.Context, topicID string, msg *pubsub.Message) (context.Context, trace.Span) {



opts := []trace.SpanStartOption{



trace.WithSpanKind(trace.SpanKindProducer),



trace.WithAttributes(



// customizable span attributes



semconv.MessagingSystemKey.String("pubsub"),



semconv.MessagingDestinationKey.String(topicID),



semconv.MessagingDestinationKindTopic,



),



}



tracer := otel.Tracer(



instrumentationName, trace.WithInstrumentationVersion(instrumentationVer),



)



ctx, span := tracer.Start(ctx, fmt.Sprintf("%s send", topicID), opts...)



if msg.Attributes == nil {



msg.Attributes = make(map[string]string)



}



// propagate Span across process boundaries



otel.GetTextMapPropagator().Inject(ctx, propagation.MapCarrier(msg.Attributes))



return ctx, span



}



func afterPublishMessage(span trace.Span, messageID string, err error) {



if err != nil {



span.RecordError(err)



span.SetStatus(codes.Error, err.Error())



} else {



span.SetAttributes(semconv.MessagingMessageIDKey.String(messageID))



}



}
```

The above snippet propagates the outgoing span by injecting it into the `Attributes` field on the Pub/Sub message. An [instrumented Pub/Sub function](#instrument-pubsub-handler) will extract this propagated span to link the trace together.

## Verify that the traces are ingested into Dynatrace

A few minutes after invoking your Google Cloud Functions, look for your spans:

* Go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab.
* Your spans will be part of an existing PurePath distributed trace if the root of your call is already being monitored by the OneAgent.

If your Google Cloud Function is not getting any traffic, there will be no traces.

## (Optional) Configure data capture to meet privacy requirements

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").


---


## Source: otel-gcf-nodejs.md


---
title: Trace Google Cloud Functions with OpenTelemetry JavaScript
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs
scraped: 2026-02-17T21:25:31.459004
---

# Trace Google Cloud Functions with OpenTelemetry JavaScript

# Trace Google Cloud Functions with OpenTelemetry JavaScript

* Latest Dynatrace
* How-to guide
* 8-min read
* Updated on Nov 13, 2023

This guide shows how to instrument Google Cloud Functions with [OpenTelemetry JSï»¿](https://github.com/open-telemetry/opentelemetry-js) and export the traces to Dynatrace. To learn more about how Dynatrace works with OpenTelemetry, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Instrument Google Cloud Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Google Cloud Functions.

To instrument your Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OpenTelemetry dependencies**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#otel-dependencies "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OpenTelemetry**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#otel-setup "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument the function entry point**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#instrument-handler "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument outgoing requests**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#outgoing-instrument "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")

### Step 1 Add OpenTelemetry dependencies

Add the following required OpenTelemetry dependencies to `package.json` file (your version numbers may vary):

```
"dependencies": {



"@opentelemetry/api": "^1.0.4",



"@opentelemetry/core": "^1.0.1",



"@opentelemetry/exporter-trace-otlp-proto": "^0.27.0",



"@opentelemetry/instrumentation": "^0.27.0",



"@opentelemetry/instrumentation-http": "^0.27.0",



"@opentelemetry/sdk-trace-node": "^1.0.1",



"@opentelemetry/semantic-conventions": "^1.0.1"



}
```

### Step 2 Set up OpenTelemetry

To make sure traces are collected, linked, and exported to Dynatrace, you need to set up and configure OpenTelemetry accordingly. For this, the Dynatrace endpoint and an authentication token are required.

To determine the endpoint

1. Open Dynatrace.
2. Check the address line of your browser. The URL will match one of the following patterns:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Replace the `...` part with `api/v2/otlp` to get the URL you will need to configure the OpenTelemetry exporter.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

To create an authentication token

1. Go to **Access Tokens** and select **Generate new token**.
2. Provide a **Token name**.
3. In the **Search scopes** box, search for `Ingest OpenTelemetry traces` and select the checkbox.
4. Select **Generate token**.
5. Select **Copy** to copy the token to your clipboard.
6. Save the token in a safe place; you can't display it again, and you will need it to configure the OpenTelemetry exporter.

Here is how to setup the OpenTelemetry tracing pipeline:

```
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');



const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



const { Resource } = require("@opentelemetry/resources");



const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");



diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);



function setupOtel(functionName) {



// create tracer provider



const provider = new NodeTracerProvider({



resource: new Resource({



[SemanticResourceAttributes.SERVICE_NAME]: functionName,



}),



sampler: new AlwaysOnSampler()



});



// add proto exporter



const exporter = new OTLPTraceExporter();



provider.addSpanProcessor(new BatchSpanProcessor(exporter));



// register globally



provider.register({



propagator: new W3CTraceContextPropagator()



});



// add http automatic instrumentation



registerInstrumentations({



instrumentations: [



new HttpInstrumentation()



],



});



return provider;



}
```

To configure the exporter to your tenant add, the following environment variables when deploying your Google Cloud function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: set it to the previously determined endpoint
* `OTEL_EXPORTER_OTLP_HEADERS`: set it to `Authorization=Api-Token <TOKEN>`, where `<TOKEN>` is the previously created authentication token.

### Step 3 Instrument the function entry point

To instrument invocations to a Google Cloud Function with OpenTelemetry, there are basically two things to do:

1. Create a span around the entry point of the function to trace invocations.
2. Extract and link the parent span from the propagated context (learn more about [W3C Trace Contextï»¿](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/)).

For certain libraries OpenTelemetry JS already provides [instrumentationsï»¿](https://github.com/open-telemetry/opentelemetry-js-contrib) that you can use to take care of these things.

The following section shows how to instrument an HTTP (`Trigger: HTTP`) Google Cloud Function.

#### Instrument an HTTP Google Cloud Function

The entry point of a newly created HTTP Google Cloud Function looks like this:

```
/**



* Responds to any HTTP request.



*



* @param {!express:Request} req HTTP request context.



* @param {!express:Response} res HTTP response context.



*/



exports.helloWorld = (req, res) => {



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

OpenTelemetry JS already provides an [instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) for this. In order to make sure that an incoming HTTP request is instrumented
and spans are captured, a few code code snippets must be added to the function's code.

Add this as your first `require` statement:

```
const { trace, context } = require("@opentelemetry/api");
```

Then add this helper function, which calls the `setupOtel` function we defined above and applies a user-defined name (`funcName`) to the automatically created span.

```
function instrumentHandler(handler, funcName) {



setupOtel(funcName);



return (req, res) => {



const span = trace.getSpan(context.active());



if (span != null) {



span.updateName(funcName);



}



handler(req, res);



};



}
```

Next, we move the function's actual "business" logic into the `myHandler` function.

```
async function myHandler(req, res) {



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

Finally, we make sure to set the now instrumented `myHandler` function as the entry point and `require` the `http(s)` modules.

Without requiring the `http(s)` modules, no spans will be created and the function's trace will not show up in Dynatrace.

```
exports.helloWorld = instrumentHandler(myHandler, "helloWorld");



// make sure the http(s) library is patched before the first call



require("http");



require("https");
```

### Step 4 Instrument outgoing requests

To achieve end-to-end tracing, it is important that outgoing requests are also instrumented.

The following section shows how to instrument outgoing HTTP(S) requests.

#### Instrument outgoing HTTP requests

OpenTelemetry JS provides an [instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) for tracing outgoing HTTP calls (which we already used in the code snippets above for tracing the incoming HTTP call).

The following helper function `httpGet` wraps outgoing HTTP(S) calls in a `Promise` object so that the result of the call can be `await`ed in the main function.

```
async function httpGet(url) {



return new Promise((resolve, reject) => {



const isHttps = url.startsWith("https://");



const httpLib = isHttps ? https : http;



const request = httpLib.get(url, (res) => {



console.log(`${url} status code - ${res.statusCode}`);



const responseData = [];



res.on("error", (error) => {



console.error(`${url} reponse error - ${error}`);



reject(error);



});



res.on("data", (chunk) => {



responseData.push(chunk);



});



res.on("end", () => {



resolve({ statusCode: res.statusCode, data: responseData });



});



});



request.on("error", error => {



console.error(`${url} request error - ${error}`);



reject(error);



});



request.end();



});



}
```

The main function can then perform outgoing HTTP(S) calls, making use of this helper function `httpGet`, which is automatically instrumented by OpenTelemetry.

```
async function myHandler(req, res) {



await httpGet('https://example.com');



await httpGet('http://example.net');



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

Putting everything together, here is the full sample code for tracing a Node.js Google Cloud Function that is invoked via HTTP and that performs outgoing HTTP(S) calls.

```
const { trace, context } = require("@opentelemetry/api");



const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');



const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



const { Resource } = require("@opentelemetry/resources");



const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");



const http = require("http");



const https = require("https");



diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);



function setupOtel(functionName) {



// create tracer provider



const provider = new NodeTracerProvider({



resource: new Resource({



[SemanticResourceAttributes.SERVICE_NAME]: functionName,



}),



sampler: new AlwaysOnSampler()



});



// add proto exporter



const exporter = new OTLPTraceExporter();



provider.addSpanProcessor(new BatchSpanProcessor(exporter));



// register globally



provider.register({



propagator: new W3CTraceContextPropagator()



});



// add http automatic instrumentation



registerInstrumentations({



instrumentations: [



new HttpInstrumentation()



],



});



return provider;



}



async function httpGet(url) {



return new Promise((resolve, reject) => {



const isHttps = url.startsWith("https://");



const httpLib = isHttps ? https : http;



const request = httpLib.get(url, (res) => {



console.log(`${url} status code - ${res.statusCode}`);



const responseData = [];



res.on("error", (error) => {



console.error(`${url} reponse error - ${error}`);



reject(error);



});



res.on("data", (chunk) => {



responseData.push(chunk);



});



res.on("end", () => {



resolve({ statusCode: res.statusCode, data: responseData });



});



});



request.on("error", error => {



console.error(`${url} request error - ${error}`);



reject(error);



});



request.end();



});



}



// The function's custom logic goes in here.



async function myHandler(req, res) {



// Perform 2 outgoing HTTP calls.



await httpGet('https://example.com');



await httpGet('http://example.net');



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};



function instrumentHandler(handler, funcName) {



setupOtel(funcName);



return (req, res) => {



const span = trace.getSpan(context.active());



if (span != null) {



span.updateName(funcName);



}



handler(req, res);



};



}



// This is the function'S entrypoint.



exports.helloWorld = instrumentHandler(myHandler, "helloWorld");



// make sure the http(s) library is patched before the first call



require("http");



require("https");
```

These are the resulting *Distributed traces* as they show up in Dynatrace.

![The OpenTelemetry JS GCF traces in Dynatrace](https://dt-cdn.net/images/otel-gcf-nodejs-1578-425c527e3f.png)

## Verify that the traces are ingested into Dynatrace

A few minutes after invoking your Google Cloud Functions, look for your spans:

* Go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab.
* Your spans will be part of an existing PurePath distributed trace if the root of your call is already being monitored by the OneAgent.
  If your Google Cloud Function is not getting any traffic, there will be no traces.

## (Optional) Configure data capture to meet privacy requirements

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").


---


## Source: gcp-functions.md


---
title: Google Cloud Functions monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions
scraped: 2026-02-17T21:20:06.717486
---

# Google Cloud Functions monitoring

# Google Cloud Functions monitoring

* Latest Dynatrace
* Overview
* 1-min read
* Updated on Jul 19, 2023

Google Cloud Functions lets you run your code without provisioning or managing servers. This deployment model is sometimes referred to as "serverless" or "Function as a Service" (FaaS).

* A Google Cloud Function runs in an application on a container managed by Google. This lets you focus on writing code without worrying about the underlying application or infrastructure.
* Google Cloud Functions are ephemeral. This means that the underlying container can be suspended or recycled when there's no request pending.

## Integration

* [Integrate on Google Cloud Functions Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")
* [Integrate on Google Cloud Functions Python](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Monitor Google Cloud Functions with OpenTelemetry for Python and Dynatrace.")
* [Integrate on Google Cloud Functions GoLang](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Monitor Google Cloud Functions with OpenTelemetry for Go and Dynatrace.")
* [Integrate on Google Cloud Functions .NET](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")
* [Google Cloud Functions monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")

## Monitoring consumption

For Google Cloud Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: deploy-k8.md


---
title: Set up the Dynatrace GCP metric and log integration on a new GKE Autopilot cluster
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8
scraped: 2026-02-17T21:29:26.983282
---

# Set up the Dynatrace GCP metric and log integration on a new GKE Autopilot cluster

# Set up the Dynatrace GCP metric and log integration on a new GKE Autopilot cluster

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

Follow the instructions below to set up Google Cloud monitoring for metrics and logs on a new GKE Autopilot cluster, using Google Cloud Shell. During setup, a new Pub/Sub subscription will be created. GKE will run two containers: a metric forwarder and a log forwarder. After installation, you'll get metrics, logs, dashboards, and alerts for your configured services in Dynatrace.

If you prefer to run the deployment script on an existing standard GKE or GKE Autopilot cluster, see [Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster").

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to install version 1.0 of the GCP integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace GCP log integration supports up to 8 GB of data processing per hour (with base resourcesâwithout scaling). With bigger loads, messages will start to be retained in the PubSub Subscription. To measure latency, look for these metrics: `Oldest unacked message age` and `Unacked messages`. For scaling recommendations, see the [scaling guide](#scalingguide) below.

Dynatrace GCP metric integration supports up to 50 GCP projects with the standard deployment. To monitor larger environments, you need to enable metrics scope. See [Monitor multiple GCP projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

## Prerequisites

To deploy the integration, you need to make sure the following requirements are met on the machine where you are running the installation.

* Linux OS only
* Internet access
* GKE Cluster access
* Dynatrace environment access

  You need to configure the Dynatrace endpoint (environment, cluster or ActiveGate URL) to which the GKE cluster should send metrics and logs. Make sure that you have direct network access or, if there is a proxy or any other component present in between, that communication is not affected.

### Tools

You can deploy the Dynatrace GCP integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [kubectlï»¿](https://kubernetes.io/docs/tasks/tools/)
* [helmï»¿](https://helm.sh/docs/intro/install/)
* [jq (version 1.6)ï»¿](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (version 4.9.x+)ï»¿](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### GCP permissions

Running the deployment script requires a list of permissions. You can create a custom role (see below) and use it to deploy `dynatrace-gcp-monitor`.

1. Create a YAML file named `dynatrace-gcp-monitor-helm-deployment-role.yaml` with the following content:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Each group of permissions is used to handle the different resources included in the integration. Creation and access are for new resources, update is for reusing existing resources, and deletion is for uninstalling.

* container.configMaps: for mapping secrets and other variables used by the containers.
* container.deployments: for the K8s' deployment within the cluster (which includes the pods, containers, etc.).
* container.namespaces: for the K8s namespace in which we are deploying the resources.
* container.pods: for the K8s pods.
* container.secrets: for the K8s secrets in which to store the data-sensitive variables.
* container.serviceAccounts: for the SA to be taken in the K8s context.
* iam.roles: for the necessary permissions for data collection.
* iam.serviceAccounts: for the general context SA.
* resourcemanager.projects: for handling the project in which we are deploying our integration.
* serviceusage.services: for handling the services' APIs.
* pubsub.subscriptions: for the PubSub subscription we are using to collect and ingest logs.
* pubsub.topics: for the PubSub topic we are using to collect and ingest logs.

2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace GCP integration.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Be sure to add this role to your GCP user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Configure log export

1. Run the following shell script in the GCP project you've selected for deployment.

Be sure to replace `<your-subscription-name>` and `<your-topic-name>` with your own values.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Configure [log exportï»¿](https://dt-url.net/4743r02) to send the desired logs to the GCP Pub/Sub topic created above.

### Dynatrace permissions

You need to create a token with a set of permissions.

1. Go to **Access tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Under **Template**, select `GCP Services Monitoring`.
5. Select **Generate**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

Alternatively, you can create the token and add permissions manually.

Add manually

[Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permissions](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extensions monitoring configuration**
  + **Write extensions monitoring configuration**
  + **Read extensions environment configuration**
  + **Write extensions environment configuration**
  + **Ingest logs**
  + **Manage metadata of Hub items**
  + **Read Hub related data**
  + **Install and update Hub items**

To monitor logs from multiple projects, you need to create **Log Routing Sinks** in each source project selecting as a destination for your main project (in which you also deployed the integration and the PubSub Topic and Subscription).
For more information, see [Route logs to supported destinationsï»¿](https://dt-url.net/cl038gj).

### Log ingestion

* Determine where log ingestion will be performed, according to your deployment. This distinction is important when configuring the [parameters](#param) for this integration.

  + **For SaaS deployments:** SaaS log ingest, where log ingestion is performed directly through the Cluster API. Recommended
  + **For Managed deployments:** You can use an existing ActiveGate for log ingestion. For information on how to deploy it, see [ActiveGate installation](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

Because of GCP's implementation of Cloud Function 2nd gen, logs from those resources will be linked to the underlying Cloud Run instances. Both extensions will have to be enabled.

To learn more, visit [Google Cloud Functions version comparisonï»¿](https://dt-url.net/b6038q5).

## Install

Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#dwld "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#param "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#script "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

1. The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor` and edit the `values.yaml` file, setting the required and optional parameter values as follows.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

   **Parameter name**

   **Description**

   **Default value**

   `parallelProcesses`

   Optional Number of parallel processes to run the whole log monitoring loop

   `1`

   `numberOfConcurrentLogForwardingLoops`

   Optional Number of workers pulling logs from pubsub concurrently and pushing them to Dynatrace

   `5`

   `numberOfConcurrentMessagePullCoroutines`

   Optional Number of concurrent coroutines to pull messages from pub/sub

   `10`

   `numberOfConcurrentPushCoroutines`

   Optional Number of concurrent coroutines to push messages to Dynatrace

   `5`

   `gcpProjectId`

   Required The ID of the GCP project you've selected for deployment.

   Your current project ID

   `deploymentType`

   Required Leave to `all`.

   `all`

   `dynatraceAccessKey`

   Required Your [Dynatrace API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the [required permissions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

   `dynatraceUrl`

   RequiredFor SaaS log/metric ingestion, it's your environment URL (`https://<your-environment-id>.live.dynatrace.com`).

   `logsSubscriptionId`

   Required The ID of your log Sink Pub/Sub subscription. For details, see [Configure log export](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

   `dynatraceLogIngestUrl`

   Optional You can set it if you want to ingest logs separately from metrics.For SaaS log ingestion, it's your environment URL (`https://<your_environment_ID>.live.dynatrace.com`).

   `dynatraceAccessKeySecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceAccessKey`.

   `dynatraceUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceUrl`.

   `dynatraceLogIngestUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceLogIngestUrl`.

   `dtSecurityContext`

   Optional Assign the attribute value used for data segmentation, analysis, and permission mapping within the Dynatrace platform. Refer to [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") for more information. If left empty, the value of `gcpProjectId` will be assigned automatically.

   Value of `gcpProjectId`

   `requireValidCertificate`

   Optional If set to `true`, Dynatrace requires the SSL certificate of your Dynatrace environment.For SaaS log ingestion, we recommend leaving the default value.

   `true`

   `selfMonitoringEnabled`

   Optional Send custom metrics to GCP to quickly diagnose if `dynatrace-gcp-monitor` processes and sends metrics/logs to Dynatrace properly. For details, see [Self-monitoring metrics for the Dynatrace GCP integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

   `false`

   `serviceAccount`

   Optional Name of the service account to be created

   `dockerImage`

   OptionalDynatrace GCP Monitor docker image. We recommend using the default value, but you can adapt it if needed.

   `dynatrace/dynatrace-gcp-monitor:v1-latest`

   `logIngestContentMaxLength`

   Optional The maximum content length of a log event. Should be less than or equal to the setting on your Dynatrace environment.

   `8192`

   `logIngestAttributeValueMaxLength`

   Optional The maximum length of the log event attribute value. If it exceeds the server limit, content will be truncated.

   `250`

   `logIngestRequestMaxEvents`

   Optional The maximum number of log events in a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `5000`

   `logIngestRequestMaxSize`

   Optional The maximum size in bytes of a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `1048576`

   `logIngestEventMaxAgeSeconds`

   Optional Determines the maximum age of a forwarded log event. Should be less than or equal to the setting on your Dynatrace environment.

   `86400`

   `printMetricIngestInput`

   Optional If set to `true`, the GCP Monitor outputs the lines of metrics to stdout.

   `false`

   `serviceUsageBooking`

   Optional Service usage booking is used for metrics and determines a caller-specified project for quota and billing purposes. If set to `source`, monitoring API calls are booked in the project where the Kubernetes container is running. If set to `destination`, monitoring API calls are booked in the project that is monitored. For details, see [Monitor multiple GCP projects - Standard environments - Step 4](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `source`

   `useProxy`

   Optional Depending on the value you set for this flag, the GCP Monitor will use the following proxy settings: Dynatrace (set to `DT_ONLY`), GCP API (set to `GCP_ONLY`), or both (set to `ALL`).

   By default, proxy settings are not used.

   `httpProxy`

   Optional The proxy HTTP address; use this flag in conjunction with `USE_PROXY`.

   `httpsProxy`

   Optional The proxy HTTPS address; use this flag in conjunction with `USE_PROXY`.

   `gcpServicesYaml`

   Optional Configuration file for GCP services.

   `queryInterval`

   Optional Metrics polling interval in minutes. Allowed values: `1` - `6`

   `3`

   `vpcNetwork`

   Optional Existing VPC Network where the autopilot cluster will be deployed. Shared VPC is not supported.

   `default`

   `useCustomSubnet`

   Optional Set to `true` only if you want to use a custom mode VPC network.If set to `true`, you'll need to pass the `customSubnetName` parameter.

   `false`

   `customSubnetName`

   Required Only if `useCustomSubnet` is set to `true`.  
   Set this value to the subnet name you want to deploy the Google Cloud Monitor in.

   `""`

   `scopingProjectSupportEnabled`

   Optional Set to `true` when metrics scope is configured, so metrics will be collected from all projects added to the metrics scope. For details, see [Monitor multiple GCP projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `false`

   `excludedProjects`

   Optional Comma-separated list of projects to be excluded from monitoring (for example, `<project_A>,<project_B>`)

   `excludedMetricsAndDimensions`

   Optional Yaml formatted list of metrics and their dimensions to be excluded for monitoring.

   `metricAutodiscovery`

   Optional If set to `true`, the GCP Monitor will run metric auto-discovery mode, expanding your options for selecting metrics to monitor. For more information, see [Monitor GCP projects using auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.").

   `false`

   `clusterIpv4Cidr`

   Optional Set the IP address range for the pods in this cluster in CIDR notation, if you want to use a custom range.

   `servicesIpv4Cidr`

   Optional Set the IP range for the services IPs. It can be specified as a netmask size or as in the CIDR notion.

   `useCustomMasterCidr`

   Optional If set to `true`, you can specify the IPv4 CIDR range to use for the master network.

   `false`

   `masterIpv4Cidr`

   Optional IPv4 CIDR range requires the `useCustomMasterCidr` value to be `true` in order to use for the master network.
2. Choose which services you want Dynatrace to monitor.

   By default, the Dynatrace GCP integration starts monitoring a set of selected services. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Run the deployment script

The deployment script will automatically create the new GKE Autopilot cluster named `dynatrace-gcp-monitor` and deploy the installation to it. The latest versions of GCP extensions will be uploaded.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

To set a different name for the new cluster, run the command below instead, making sure to replace the placeholder (`<name-of-new-cluster>`) with your preferred name.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Verify installation

To check whether installation was successful

1. Check if the container is running.

   After the installation, it may take couple of minutes until the container is up and running.

   ```
   kubectl -n dynatrace get pods
   ```
2. Check the container logs for errors or exceptions. You have two options:

   In the Kubernetes CLI

   In your GCP console

   Run the following commands.

   ```
   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics



   kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
   ```

   To check the container logs for errors in your GCP console

   1. Go to **Logs explorer**.
   2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (for metric ingest logs)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (for log ingest logs)
3. Check if dashboards are imported.

   Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Choose services for metrics monitoring

### Services enabled by default

Monitoring of following services will be enabled during deployment of GCP Monitor:

* [Google APIs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")
* [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")
* [Google BigQuery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")
* [Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")
* [Google Cloud Run](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")
* [Google Cloud Storage](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")
* [Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")
* [Google Firestore in Datastore mode](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")
* [Google Filestore](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")
* [Google Kubernetes Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")
* [Google Cloud Load Balancing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")
* [Google Cloud Pub/Sub](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")
* [Google Cloud Pub/Sub Lite](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")
* [Google Cloud SQL](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

There are more service integrations available, but need to be enabled. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services. The next section describes how to manage them. For an alternative approach, consider leveraging [auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.") to extend your metric coverage.

### Manage enabled services

You can manage enabled services via Dynatrace Hub.

Filter for "gcp"âyou'll find annotations in the results for items that are already available in your environment.

To enable a new service, select it in Hub and then install it.

You can also disable a service via Dynatrace Hub.

To see if the services need updating, open them in Hub and check release notes. The updates can include new metrics, new assets like dashboards, or other changes.

All changes to enabled services are applied to GCP Monitor within few minutes.

#### Feature sets & available metrics

To see what metrics are included for specific service, check [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics."). By default, only `defaultMetrics` feature set is enabled. To enable additional feature sets, you have to uncomment them in `values.yaml` file and redeploy whole GCP Monitor.

Current configuration of feature sets can be found in cluster's ConfigMap named `dynatrace-gcp-function-config`.

#### Advanced scope management

To further refine monitoring scope, you can use `filter_conditions` field in `values.yaml` file. This requires GCP Monitor to be redeployed. See [GCP Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US) for syntax.

Example:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for GCP alerts and turn on **On/Off** for the alerts you want to activate.

## View metrics and logs

After deploying the integration, you can:

* See metrics from monitored services: go to **Metrics** and filter by `gcp`.
* View and analyze GCP logs: go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and, to look for GCP logs, filter by `cloud.provider: gcp`.

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Run the command below, making sure to replace `<your-helm-release>` with value from previous step.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

For details, see [Helm upgradeï»¿](https://helm.sh/docs/helm/helm_upgrade/).

### Change deployment type

To change the deployment type (`all`, `metrics`, or `logs`)

1. Find out what helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<your-helm-release>` with the release name from the previous output.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Edit `deploymentType` in `values.yaml` with the new value and save the file.
4. Run the deployment command again. For details, see [Run the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check container logs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Scaling guide for logs

The default container with 1.25vCPU and 1Gi (with default configuration) can handle 8 GB of log throughput per hour. Achieving more throughput requires allocating more resources to the container (scale up), increasing the number of container replicas (scale out), and changing configuration numbers to use allocated resources efficiently. All config variables can be found and changed in `dynatrace-gcp-monitor-config`.

The following table presents tested configuration and achieved throughput with scaled up&out containers:

Achieved throughput

Machine resources

Replica sets

Config variable values

~8MB/s => ~480MB/min

4vCPU 4Gi RAM

1

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~25MB/s => ~1.5GB/min => ~2TB/day

4vCPU 4Gi RAM

4

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~46MB/s => ~2.7GB/min => ~4TB/day

4vCPU 4Gi RAM

6

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

## Autoscaling guide for logs

Autoscaling works only for `logs` type of deployment, not `all`.

We recommend manually scaling the container to have a 4vCPU 4Gi machine and then enabling autoscaling.

GCP provides autoscaling of containers in both directions: **horizontal** and **vertical**. However, Dynatrace recommends only **horizontal** scaling.

If you have a 4vCPU 4Gi machine, you can enable autoscaling **horizontally**. However, we **don't** recommend scaling horizontally with the base resources of the container (1.25vCPU, 1Gi). It hasn't been proven to be efficient during testing. One 4vCPU machine does better than four 1vCPU machines. To enable autoscaling horizontally, use the horizontal autoscaling command:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Autoscaling is recommended only when you have a minimum of 450 MB/min throughput and can provide a 4vCPU 4Gi RAM machine. Autoscaling is only scaling out, not scaling the machine up.

We **don't** recommend scaling **vertically** because every time a machine is scaled up, an environment variable needs to be changed to create more processes corresponding to machine cores.

## Uninstall

1. Find out what Helm release version you're using.

```
helm ls -n dynatrace
```

2. Uninstall the release.

Be sure to replace `<your-helm-release>` with the release name from the previous output.

```
helm uninstall <your-helm-release> -n dynatrace
```

Alternatively, you can delete the namespace.

```
kubectl delete namespace dynatrace
```

3. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all GCP extensions.

You can find and delete relevant extensions via Dynatrace Hub.

Make sure to uninstall the following resources manually:

* The initial Role created and attached to the Service Account that you used to deploy the integration.
* The PubSub Topic.
* The PubSub Subscription.
* The LogRoute Sink.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)


---


## Source: deploy-with-google-cloud-function.md


---
title: Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function
scraped: 2026-02-17T21:28:41.571915
---

# Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions

# Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Sep 06, 2022
* Deprecated

Dynatrace version 1.230+

Dynatrace Google Cloud metric integration in Google Cloud Functions is **not** supported anymore.

If you're using this kind of deployment, you should switch to k8s-based Google Cloud integration as soon as possible.
See [Migrate from Google Cloud Functions 1.0 to Google Cloud k8s 1.0](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function-1-to-k8s-1 "Migrate from Google Cloud Functions v1.0 to Google Cloud k8s v1.0.").

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), that provides Google Cloud monitoring for both metrics and logs, and where the deployment takes place in a GKE cluster, you can choose to set up monitoring for metrics only, in Google Cloud Cloud Function. Note that the Google Cloud Cloud Function deployment isn't recommended for large environments and doesn't support log forwarding.
In this scenario, you will be able run the deployment script either in Google Cloud Shell or in bash. After installation, you'll get metrics, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to deploy version 1.0 of the Dynatrace Google Cloud integration in Google Cloud Cloud Function.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy "Set up monitoring for Google Cloud services using a Google Cloud Function.") of the Google Cloud Monitor installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Prerequisites

### Tools

You can deploy the Dynatrace Google Cloud integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role and use it to deploy `dynatrace-gcp-monitor`.

To create a custom role

1. Create a YAML file named `dynatrace-gcp-monitor-cloud-function-deployment-role.yaml` with the following content:

   dynatrace-gcp-monitor-cloud-function-deployment-role.yaml

   ```
   title: Dynatrace GCP Monitor cloud function deployment role



   description: Role for Dynatrace GCP Monitor cloud function deployment



   stage: GA



   includedPermissions:



   - appengine.applications.get



   - appengine.applications.create



   - cloudfunctions.functions.create



   - cloudfunctions.functions.get



   - cloudfunctions.functions.list



   - cloudfunctions.functions.sourceCodeSet



   - cloudfunctions.functions.update



   - cloudfunctions.functions.getIamPolicy



   - cloudfunctions.operations.get



   - cloudfunctions.operations.list



   - cloudscheduler.locations.list



   - cloudscheduler.jobs.list



   - cloudscheduler.jobs.create



   - cloudscheduler.jobs.get



   - cloudscheduler.jobs.delete



   - pubsub.topics.list



   - pubsub.topics.create



   - pubsub.topics.update



   - secretmanager.secrets.list



   - secretmanager.versions.add



   - secretmanager.secrets.create



   - secretmanager.versions.list



   - secretmanager.secrets.getIamPolicy



   - secretmanager.secrets.setIamPolicy



   - resourcemanager.projects.get



   - resourcemanager.projects.getIamPolicy



   - resourcemanager.projects.setIamPolicy



   - serviceusage.services.enable



   - iam.serviceAccounts.actAs



   - iam.serviceAccounts.list



   - iam.serviceAccounts.create



   - iam.serviceAccounts.getIamPolicy



   - iam.serviceAccounts.setIamPolicy



   - iam.roles.list



   - iam.roles.create



   - iam.roles.update



   - monitoring.dashboards.list



   - monitoring.dashboards.create
   ```
2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

   ```
   gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
   ```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Dynatrace permissions

[Create an API tokenï»¿](https://dt-url.net/be03q3a) and [enable the following permissionsï»¿](https://dt-url.net/c023q1m):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extension monitoring configurations**
  + **Write extension monitoring configurations**
  + **Read extension environment configurations**
  + **Write extension environment configurations**

### Dynatrace URL

Determine the URL for your environment.

* For Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
* For Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

To determine `<your-environment-id>`, see [environment IDï»¿](https://dt-url.net/ej43qge).

## Install

You can deploy the Dynatrace Google Cloud integration in Google Cloud Shell or in bash. To set up integration, follow the instructions below.

For bash deployment, be sure to restart the console and [initialize Cloud SDKï»¿](https://dt-url.net/ac43q0f) before you start installation.

To initialize Cloud SDK, run

```
gcloud init
```

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the deployment package**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#dwld "Set up monitoring for Google Cloud services in Google Cloud Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#configure-deployment "Set up monitoring for Google Cloud services in Google Cloud Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#script "Set up monitoring for Google Cloud services in Google Cloud Functions.")

### Step 1 Download the deployment package

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/tag/release-1.1.8/download/function-deployment-package.zip" -O function-deployment-package.zip; unzip function-deployment-package.zip; chmod a+x *.sh
```

### Step 2 Configure deployment

1. Adjust the parameters in the `activation-config.yaml` file from the deployment package.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.
2. Choose which services you want Dynatrace to monitor.

By default, the Google Cloud integration starts monitoring a series of selected services. Uncomment any additional services you want Dynatrace to monitor in the `activation-config.yaml` file.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Run the deployment script

Version upgrade of extensions is done by default. To keep the versions of existing extensions, run the script with the `--without-extensions-upgrade` parameter.

```
./setup.sh
```

The script may ask you for confirmations during deployment. For CI/CD purposes, you can add the `-d` option to make the script noninteractive.

After deploying the integration, you can see metrics from monitored services. If you want to change the monitoring scope (services & featureSets) or update the Google Cloud integration, see [Change deployment settings](#manage) below.

## Verify installation

To check whether installation was successful

1. In your Google Cloud console, go to Cloud Functions and make sure that `dynatrace-gcp-monitor` is there.
2. Select the newly deployed Google Cloud Monitor function and go to **Logs** to make sure there are no error messages.

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable custom events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for GCP alerts and turn on **On/Off** for the alerts you want to activate.

## View enabled services

To find the list of currently enabled services, go to Cloud Function in your Google Cloud console, and check the `ACTIVATION_CONFIG` environment variable.

## Update services

Adding, removing and updating versions of existing services is done by modyfing the corresponding list of services and redeploying.

1. Apply your changes to `activation-config.yaml` by commenting or uncommenting configuration blocks corresponding to specific services.
   Terminology within the file includes:

   * `service`: represents Google Cloud service name you want to monitor. Services are grouped by extensions, but you can decide what you need to monitor on a lower level (`featureSets`)
   * `featureSet`: a set of metrics for a given service. `default_metrics` is a default `featureSet` with a recommended set of metrics to be monitored. In more specific use cases, you can consider monitoring such sets as `istio featureSet` for `gae_instance service`
   * `filter_conditions`: a service-level filter that enables you to narrow the monitoring scope. It is based on the [Google Cloud Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).  
     Example:

     ```
     filter_conditions:



     resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
     ```
2. Update monitored services by running the script below.

   Version upgrade of extensions is done by default. To keep the versions of existing extensions, run the script with the `--without-extensions-upgrade` parameter.

   ```
   ./setup.sh
   ```
3. If you removed services from monitoring, find the relevant extensions in Dynatrace Hub and delete them to remove service-specific assets (such as dashboards and alerts).

### Example

In the following example

* The `gae_instance` service is disabled.
* For the `gce_instance` service, only two feature sets are enabled: `default_metrics` and `istio`.

```
# Google App Engine Instance



#- service: gae_instance



#  featureSets:



#    - default_metrics



#  vars:



#    filter_conditions: ""



# Google VM Instance



- service: gce_instance



featureSets:



- default_metrics



#    - agent



#    - firewallinsights



- istio



#    - uptime_check



vars:



filter_conditions: ""
```

For a complete list of the Google Cloud supported services, see [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new#services "Monitor Google Cloud services with Dynatrace and view available metrics.").

## Change deployment settings

To add or remove services, or to update parameters, you need to redeploy the integration.

1. Apply your changes to `activation-config.yaml`.

   Be sure to use the same value for the `FUNCTION_NAME` parameter as before.
2. [Rerun the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check function logs](#verify).

## Uninstall

1. Go to your installation directory and run the command below.

```
./uninstall.sh
```

2. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

## Monitoring consumption

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")


---


## Source: migrate-gcp-function.md


---
title: Migrate to Google Cloud integration version 1.0
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function
scraped: 2026-02-17T21:31:00.451969
---

# Migrate to Google Cloud integration version 1.0

# Migrate to Google Cloud integration version 1.0

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Jan 17, 2022

Dynatrace version 1.230+

The new version of the Google Cloud integration (v.1.0) uses [Extensions 2.0](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and introduces [custom topology](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology "Learn how to create a custom topology model that's suited to your telemetry data.") for a number of Google Cloud services.

List of services with custom topology

* Google Compute Engine
* Google Cloud Storage
* Google Cloud Functions
* Google Cloud Run
* Google App Engine
* Google Cloud Tasks
* Google Cloud SQL
* Google Cloud Datastore
* Google Load Balancing
* Google Cloud NAT Gateway
* Google Filestore
* Google Kubernetes Engine
* Google Pub/Sub
* Google Pub/Sub Lite
* Google Memorystore
* Google Spanner

Note that your existing metric dimension names will change when you switch to Google Cloud integration using Dynatrace Extensions 2.0. Dimension name changes affect all configured managements zones, custom alerts, and custom dashboards in your environment. To restore proper functionality for these entities, please follow the instructions below.

Upgrading existing `dynatrace-gcp-monitor` installations from earlier versions is not supported. You need to first delete your existing deployment and then install the Google Cloud integration v.1.0. For instructions, see below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Delete existing deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#delete-deployment "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Remove dashboards and/or alerts**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#remove-dashboards "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Install new Google Cloud deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#install-deployment "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Update dimensions**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function#update-dimensions "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.")

## Step 1 Delete existing deployment

For Kubernetes container deployment

For GC Function deployment

1. Find out what release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<release-name>` with the release name from the previous output.

   ```
   helm uninstall <release-name> -n dynatrace
   ```

1. Uninstall the release.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/uninstall.sh -O uninstall.sh ; chmod a+x uninstall.sh ; ./uninstall.sh
```

2. Remove the `activation-config.yaml` service configuration file.

## Step 2 Remove dashboards and/or alerts

You need to manually remove any dashboards or alerts created manually during the previous installation.

## Step 3 Install new Google Cloud deployment

To install the new Google Cloud deployment, see [Set up the Dynatrace Google Cloud metric and log integration (v.1.0) on a new GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

## Step 4 Update dimensions

If you created your own dashboards, alerts, or management zones based on Google Cloud metrics, you need to manually update the dimensions according to the list below in order to get links for entities.

### List of dimension changes

| Old dimension name | New dimension name |
| --- | --- |
| `project_id` | `gcp.project.id` |
| `region` | `gcp.region` |
| `zone` | `gcp.region` |
| `instance_id` | `gcp.instance.id` |
| `autoscaler_id` | `gcp.instance.id` |
| `model_id` | `gcp.instance.id` |
| `queue_id` | `gcp.instance.id` |
| `device_registry_id` | `gcp.instance.id` |
| `job_id` | `gcp.instance.id` |
| `version_id` | `gcp.instance.id` |
| `database_id` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `router_id` | `gcp.instance.id` |
| `instance_group_id` | `gcp.instance.id` |
| `interconnect` | `gcp.instance.id` |
| `attachment` | `gcp.instance.id` |
| `volume_id` | `gcp.instance.id` |
| `snapshot_id` | `gcp.instance.id` |
| `subscription_id` | `gcp.instance.id` |
| `topic_id` | `gcp.instance.id` |
| `key_id` | `gcp.instance.id` |
| `worker_id` | `gcp.instance.id` |
| `agent_id` | `gcp.instance.id` |
| `gateway_id` | `gcp.instance.id` |
| `name` | `gcp.instance.name` |
| `autoscaler_name` | `gcp.instance.name` |
| `environment_name` | `gcp.instance.name` |
| `cluster_name gcp.instance.name` | `gcp.instance.name` |
| `function_name gcp.instance.name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `job_name` | `gcp.instance.name` |
| `instance_name` | `gcp.instance.name` |
| `domain_name` | `gcp.instance.name` |
| `table_name` | `gcp.instance.name` |
| `firewall_name` | `gcp.instance.name` |
| `bucket_name` | `gcp.instance.name` |
| `container_name` | `gcp.instance.name` |
| `url_map_name` | `gcp.instance.name` |
| `instance_group_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `canonical_service_name` | `gcp.instance.name` |
| `node_name` | `gcp.instance.name` |
| `pod_name` | `gcp.instance.name` |
| `broker_name` | `gcp.instance.name` |
| `revision_name` | `gcp.instance.name` |
| `trigger_name` | `gcp.instance.name` |
| `fqdn` | `gcp.instance.name` |
| `target_domain_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |
| `policy_name` | `gcp.instance.name` |
| `proxy_name` | `gcp.instance.name` |
| `load_balancer_name` | `gcp.instance.name` |
| `backend_target_name` | `gcp.instance.name` |
| `connector_name` | `gcp.instance.name` |
| `gateway_name` | `gcp.instance.name` |

* To update dimensions for dashboards

  1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. Select the dashboard for which you want to update dimensions, and then select **More** (**â¦**) > **Configure**.
  3. Select **Dashboard JSON**.
  4. In the `"splitBy"` section, replace the old dimensions with the new values as determined from the [list of dimension changes](#dimension).
  5. Select **Save changes**.

Alternatively, you can replace the dimensions by configuring each dashboard tile of a selected dashboard in Data Explorer.

* To update dimensions for alerts

  1. Go to **Settings**.
  2. Select **Anomaly detection** > **Metric events**.
  3. Select the event for which you want to update dimensions.
  4. In the **Add dimension filter** field, select the new dimension keys and enter the corresponding dimension values as determined from the [list of dimension changes](#dimension).
  5. Select **Save changes**.
* To update dimensions for management zones

  1. Go to **Settings**.
  2. Select **Preferences** > **Management zones**.
  3. Select **Edit** for the management zone for which you want to update dimensions.
  4. Select **Edit** to edit an existing rule.
  5. In **Conditions**, edit the `DIMENSION` value according to the [List of dimension changes](#dimension).
  6. Select **Save changes**.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")


---


## Source: set-up-gcp-integration-logs-only.md


---
title: Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only
scraped: 2026-02-17T05:09:22.263449
---

# Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)

# Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)

* Latest Dynatrace
* How-to guide
* 12-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), that provides Google Cloud monitoring for both metrics and logs, you can choose to set up monitoring for logs only. In this scenario, you'll run the deployment script in Google Cloud Shell. Instructions will depend on the location where you want the deployment script to run:

* On a new GKE Autopilot cluster created automatically Recommended
* On an existing GKE standard or GKE Autopilot cluster

During setup, a new Pub/Sub subscription will be created. GKE will run a log forwarder container. After installation, you'll get logs, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to install version 1.0 of the Google Cloud integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace Google Cloud log integration supports up to 8 GB of data processing per hour (with base resourcesâwithout scaling). With bigger loads, messages will start to be retained in the PubSub Subscription. To measure latency, look for these metrics: `Oldest unacked message age` and `Unacked messages`. For scaling recommendations, see the [scaling guide](#scalingguide) below.

## Prerequisites

To deploy the integration, you need to make sure the following requirements are met on the machine where you are running the installation.

* Linux OS only
* Internet access
* GKE Cluster access
* Dynatrace environment access

  You need to configure the Dynatrace endpoint (environment, cluster or ActiveGate URL) to which the GKE cluster should send metrics and logs. Make sure that you have direct network access or, if there is a proxy or any other component present in between, that communication is not affected.

### Tools

You can deploy the Dynatrace GCP integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [kubectlï»¿](https://kubernetes.io/docs/tasks/tools/)
* [helmï»¿](https://helm.sh/docs/intro/install/)
* [jq (version 1.6)ï»¿](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (version 4.9.x+)ï»¿](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role (see below) and use it to deploy `dynatrace-gcp-monitor`.

1. Create a YAML file named `dynatrace-gcp-monitor-helm-deployment-role.yaml` with the following content:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Each group of permissions is used to handle the different resources included in the integration. Creation and access are for new resources, update is for reusing existing resources, and deletion is for uninstalling.

* container.configMaps: for mapping secrets and other variables used by the containers.
* container.deployments: for the K8s' deployment within the cluster (which includes the pods, containers, etc.).
* container.namespaces: for the K8s namespace in which we are deploying the resources.
* container.pods: for the K8s pods.
* container.secrets: for the K8s secrets in which to store the data-sensitive variables.
* container.serviceAccounts: for the SA to be taken in the K8s context.
* iam.roles: for the necessary permissions for data collection.
* iam.serviceAccounts: for the general context SA.
* resourcemanager.projects: for handling the project in which we are deploying our integration.
* serviceusage.services: for handling the services' APIs.
* pubsub.subscriptions: for the PubSub subscription we are using to collect and ingest logs.
* pubsub.topics: for the PubSub topic we are using to collect and ingest logs.

2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Configure log export

1. Run the following shell script in the Google Cloud project you've selected for deployment.

Be sure to replace `<your-subscription-name>` and `<your-topic-name>` with your own values.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Configure [log exportï»¿](https://dt-url.net/4743r02) to send the desired logs to the Google Cloud Pub/Sub topic created above.

To monitor logs from multiple projects, you need to create **Log Routing Sinks** in each source project selecting as a destination for your main project (in which you also deployed the integration and the PubSub Topic and Subscription).
For more information, see [Route logs to supported destinationsï»¿](https://dt-url.net/cl038gj).

### Dynatrace permissions

* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permission](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."): **Ingest logs** (API v2).

### Log ingestion

* Determine where log ingestion will be performed, according to your deployment. This distinction is important when configuring the [parameters](#param) for this integration.

  + **For SaaS deployments:** SaaS log ingest, where log ingestion is performed directly through the Cluster API. Recommended
  + **For Managed deployments:** You can use an existing ActiveGate for log ingestion. For information on how to deploy it, see [ActiveGate installation](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

Because of GCP's implementation of Cloud Function 2nd gen, logs from those resources will be linked to the underlying Cloud Run instances. Both extensions will have to be enabled.

To learn more, visit [Google Cloud Functions version comparisonï»¿](https://dt-url.net/b6038q5).

## Install

Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#dwld "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#param "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect your Kubernetes cluster**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#connect "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#script "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor`and edit the `values.yaml` file, setting the required and optional parameter values as follows.

You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

**Parameter name**

**Description**

**Default value**

`gcpProjectId`

Required The ID of the Google Cloud project you've selected for deployment.

Your current project ID

`deploymentType`

Required Set to `logs`.

`all`

`dynatraceAccessKey`

Required Your [Dynatrace API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the [required permissions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

`dynatraceAccessKeySecretName`

Optional You can specify the key to fetch the endpoint from Google Cloud Secret Manager, instead of using `dynatraceAccessKey`.

`dynatraceUrlSecretName`

Optional You can specify the key to fetch the endpoint from Google Cloud Secret Manager, instead of using `dynatraceUrl`.

`dtSecurityContext`

Optional Assign the attribute value used for data segmentation, analysis, and permission mapping within the Dynatrace platform. Refer to [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") for more information. If left empty, the value of `gcpProjectId` will be assigned automatically.

Value of `gcpProjectId`

`dynatraceUrl`

Required For SaaS log ingestion, it's your environment URL (`https://<your-environment-id>.live.dynatrace.com`).

`logsSubscriptionId`

Required The ID of your log Sink Pub/Sub subscription. For details, see [Configure log export](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

`requireValidCertificate`

Optional If set to `true`, Dynatrace requires the SSL certificate of your Dynatrace environment.  
For SaaS log ingestion, we recommend leaving the default value.

`true`

`selfMonitoringEnabled`

Optional Send custom metrics to Google Cloud to quickly diagnose if `dynatrace-gcp-monitor` processes and sends logs to Dynatrace properly.For details, see [Self-monitoring metrics for the Dynatrace Google Cloud integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

`false`

`serviceAccount`

Optional Name of the service account to be created.

`dockerImage`

OptionalDynatrace Google Cloud Monitor Docker image. We recommend using the default value, but you can adapt it if needed.

`dynatrace/dynatrace-gcp-monitor:v1-latest`

`logIngestContentMaxLength`

Optional The maximum content length of a log event. Should be less than or equal to the setting on your Dynatrace environment.

`8192`

`logIngestAttributeValueMaxLength`

Optional The maximum length of the log event attribute value. If it exceeds the server limit, content will be truncated.

`250`

`logIngestRequestMaxEvents`

Optional The maximum number of log events in a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

`5000`

`logIngestRequestMaxSize`

Optional The maximum size in bytes of a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

`1048576`

`logIngestEventMaxAgeSeconds`

Optional Determines the maximum age of a forwarded log event. Should be less than or equal to the setting on your Dynatrace environment.

`86400`

`clusterIpv4Cidr`

Optional Set the IP address range for the pods in this cluster in CIDR notation, if you want to use a custom range.

`servicesIpv4Cidr`

Optional Set the IP range for the services IPs. It can be specified as a netmask size or as in the CIDR notion.

`useCustomMasterCidr`

Optional If set to `true`, you can specify the IPv4 CIDR range to use for the master network.

`false`

`masterIpv4Cidr`

Optional IPv4 CIDR range to use for the master network. Requires the `useCustomMasterCidr` value to be true.

For DDU consumptiom information, see [Monitoring consumption](#ddu).

### Step 3 Connect your Kubernetes cluster

* If you want to have a new GKE Autopilot cluster created by the deployment script, add `--create-autopilot-cluster` to the script. Setting up the connection to the cluster will happen automatically in this case and you can proceed to [step 4](#script).
* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, you can connect to your cluster from the Google Cloud console or via terminal. Follow the instructions below.

From the Google Cloud console

Via terminal

1. In your Google Cloud console, go to your Kubernetes Engine.
2. Select **Clusters**, and then select **Connect**.
3. Select **Run in Cloud Shell**.

Run the command below, making sure to replace

* `<cluster>` with your cluster name
* `<region>` with the region where your cluster is running
* `<project>` with the project ID where your cluster is running

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

For details, see [Configuring cluster access for kubectlï»¿](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Step 4 Run the deployment script

* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, the deployment script will create an IAM service account with the necessary roles and deploy `dynatrace-gcp-monitor` to your Kubernetes cluster.
* If you run the deployment script with the `--create-autopilot-cluster` option, the deployment script will automatically create the new GKE Autopilot cluster and deploy `dynatrace-gcp-monitor` to it.

To run the deployment script, follow the instructions below.

Run on existing cluster

Run on new cluster

The latest versions of Google Cloud extensions will be uploaded. You have two options:

* Run the deployment script without parameters if you want to use the default values provided (`dynatrace-gcp-monitor-sa` for the IAM service account name and `dynatrace_monitor` for the IAM role name prefix):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Run the deployment script with parameters if you want to set your own values (be sure to replace the placeholders with your desired values):

```
cd helm-deployment-package



./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --without-extensions-upgrade
```

Run the command below. The latest versions of extensions will be uploaded.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

To set a different name for the new cluster, run the command below instead, making sure to replace the placeholder (`<name-of-new-cluster>`) with your preferred name.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Verify installation

To check whether installation was successful

1. Check if the container is running.

   After the installation, it may take couple of minutes until the container is up and running.

   ```
   kubectl -n dynatrace get pods
   ```
2. Check the container logs for errors or exceptions. You have two options:

In the Kubernetes CLI

In your Google Cloud console

Run the following command.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

To check the container logs for errors in your Google Cloud console

1. Go to **Logs explorer**.
2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"`

3. Check if dashboards are imported.

   In Dynatrace, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for Google Cloud alerts and turn on **On/Off** for the alerts you want to activate.

## View logs

After deploying the integration, you can view and analyze Google Cloud logs in Dynatrace if you go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and filter by `cloud.provider: gcp`.

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Run the command below, making sure to replace `<your-helm-release>` with the value from the previous step.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

For details, see [Helm upgradeï»¿](https://helm.sh/docs/helm/helm_upgrade/).

### Change deployment type

To change the deployment type (`all`, `metrics`, or `logs`)

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<your-helm-release>` with the release name from the previous output.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Edit `deploymentType` in `values.yaml` with the new value and save the file.
4. Run the deployment command again. For details, see [Run the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check container logs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Scaling guide for logs

The default container with 1.25vCPU and 1Gi (with default configuration) can handle 8 GB of log throughput per hour. Achieving more throughput requires allocating more resources to the container (scale up), increasing the number of container replicas (scale out), and changing configuration numbers to use allocated resources efficiently. All config variables can be found and changed in `dynatrace-gcp-monitor-config`.

The following table presents tested configuration and achieved throughput with scaled up&out containers:

Achieved throughput

Machine resources

Replica sets

Config variable values

~8MB/s => ~480MB/min

4vCPU 4Gi RAM

1

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~25MB/s => ~1.5GB/min => ~2TB/day

4vCPU 4Gi RAM

4

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~46MB/s => ~2.7GB/min => ~4TB/day

4vCPU 4Gi RAM

6

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

## Autoscaling guide for logs

Autoscaling works only for `logs` type of deployment, not `all`.

We recommend manually scaling the container to have a 4vCPU 4Gi machine and then enabling autoscaling.

GCP provides autoscaling of containers in both directions: **horizontal** and **vertical**. However, Dynatrace recommends only **horizontal** scaling.

If you have a 4vCPU 4Gi machine, you can enable autoscaling **horizontally**. However, we **don't** recommend scaling horizontally with the base resources of the container (1.25vCPU, 1Gi). It hasn't been proven to be efficient during testing. One 4vCPU machine does better than four 1vCPU machines. To enable autoscaling horizontally, use the horizontal autoscaling command:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Autoscaling is recommended only when you have a minimum of 450 MB/min throughput and can provide a 4vCPU 4Gi RAM machine. Autoscaling is only scaling out, not scaling the machine up.

We **don't** recommend scaling **vertically** because every time a machine is scaled up, an environment variable needs to be changed to create more processes corresponding to machine cores.

## Uninstall

1. Find out what Helm release version you're using.

```
helm ls -n dynatrace
```

2. Uninstall the release.

Be sure to replace `<your-helm-release>` with the release name from the previous output.

```
helm uninstall <your-helm-release> -n dynatrace
```

Alternatively, you can delete the namespace.

```
kubectl delete namespace dynatrace
```

3. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

Make sure to uninstall the following resources manually:

* The initial Role created and attached to the Service Account that you used to deploy the integration.
* The PubSub Topic.
* The PubSub Subscription.
* The LogRoute Sink.

## Monitoring consumption

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)


---


## Source: set-up-gcp-integration-metrics-only.md


---
title: Set up the Dynatrace Google Cloud metric integration on a GKE cluster
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only
scraped: 2026-02-17T05:06:58.000813
---

# Set up the Dynatrace Google Cloud metric integration on a GKE cluster

# Set up the Dynatrace Google Cloud metric integration on a GKE cluster

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), that provides Google Cloud monitoring for both metrics and logs, you can choose to set up monitoring for metrics only. In this scenario, you'll run the deployment script in Google Cloud Shell. Instructions will depend on the location where you want the deployment script to run:

* On a new GKE Autopilot cluster created automatically Recommended
* On an existing GKE standard or GKE Autopilot cluster

During setup, GKE will run a metric forwarder container. After installation, you'll get metrics, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to install version 1.0 of the Google Cloud integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace Google Cloud metric integration supports up to 50 Google Cloud projects with the standard deployment. To monitor larger environments, you need to enable metrics scope. See [Monitor multiple Google Cloud projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

## Prerequisites

To deploy the integration, you need to make sure the following requirements are met on the machine where you are running the installation.

* Linux OS only
* Internet access
* GKE Cluster access
* Dynatrace environment access

  You need to configure the Dynatrace endpoint (environment, cluster or ActiveGate URL) to which the GKE cluster should send metrics and logs. Make sure that you have direct network access or, if there is a proxy or any other component present in between, that communication is not affected.

### Tools

You can deploy the Dynatrace GCP integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [kubectlï»¿](https://kubernetes.io/docs/tasks/tools/)
* [helmï»¿](https://helm.sh/docs/intro/install/)
* [jq (version 1.6)ï»¿](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (version 4.9.x+)ï»¿](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role (see below) and use it to deploy `dynatrace-gcp-monitor`.

1. Create a YAML file named `dynatrace-gcp-monitor-helm-deployment-role.yaml` with the following content:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Each group of permissions is used to handle the different resources included in the integration. Creation and access are for new resources, update is for reusing existing resources, and deletion is for uninstalling.

* container.configMaps: for mapping secrets and other variables used by the containers.
* container.deployments: for the K8s' deployment within the cluster (which includes the pods, containers, etc.).
* container.namespaces: for the K8s namespace in which we are deploying the resources.
* container.pods: for the K8s pods.
* container.secrets: for the K8s secrets in which to store the data-sensitive variables.
* container.serviceAccounts: for the SA to be taken in the K8s context.
* iam.roles: for the necessary permissions for metrics collection.
* iam.serviceAccounts: for the general context SA.
* resourcemanager.projects: for handling the project in which we are deploying our integration.
* serviceusage.services: for handling the services' APIs.

2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Google Cloud settings

The location where you deploy the integration determines whether you need to change additional settings.

#### Deploy on a GKE Autopilot cluster

If you deploy the integration on an existing GKE Autopilot cluster or on a new Autopilot cluster that will be automatically created by the deployment script, you don't need to make any additional settings.

#### Deploy on a GKE standard cluster

If you deploy the integration on an existing GKE standard cluster, you need to:

* [Enable Workload Identity on a cluster.ï»¿](https://dt-url.net/2j23qqv)
* [Enable `GKE_METADATA` on the GKE node pools.ï»¿](https://dt-url.net/an43q2s)

### Dynatrace permissions

You need to create a token with a set of permissions.

1. Go to **Access tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Under **Template**, select `GCP Services Monitoring`.
5. Select **Generate**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

Alternatively, you can create the token and add permissions manually.

Add manually

[Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permissions](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extensions monitoring configuration**
  + **Write extensions monitoring configuration**
  + **Read extensions environment configuration**
  + **Write extensions environment configuration**
  + **Manage metadata of Hub items**
  + **Read Hub related data**
  + **Install and update Hub items**

## Install

Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#dwld "Set up metric monitoring for Google Cloud services on a GKE cluster.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#params "Set up metric monitoring for Google Cloud services on a GKE cluster.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect your Kubernetes cluster**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#connect "Set up metric monitoring for Google Cloud services on a GKE cluster.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only#script "Set up metric monitoring for Google Cloud services on a GKE cluster.")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

1. The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor`and edit the `values.yaml` file, setting the required and optional parameter values as follows.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

   **Parameter name**

   **Description**

   **Default value**

   `gcpProjectId`

   Required The ID of the Google Cloud project you've selected for deployment.

   Your current project ID

   `deploymentType`

   Required Set to `metrics`.

   `all`

   `dynatraceAccessKey`

   Required Your [Dynatrace API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the [required permissions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

   `dynatraceAccessKeySecretName`

   Optional You can specify the key to fetch the endpoint from Google Cloud Secret Manager, instead of using `dynatraceAccessKey`.

   `dynatraceUrlSecretName`

   Optional You can specify the key to fetch the endpoint from Google Cloud Secret Manager, instead of using `dynatraceUrl`.

   `dtSecurityContext`

   Optional Assign the attribute value used for data segmentation, analysis, and permission mapping within the Dynatrace platform. Refer to [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") for more information. If left empty, the value of `gcpProjectId` will be assigned automatically.

   Value of `gcpProjectId`

   `dynatraceUrl`

   Required For SaaS log ingestion, it's your environment URL (`https://<your-environment-id>.live.dynatrace.com`).

   `requireValidCertificate`

   Optional If set to `true`, Dynatrace requires the SSL certificate of your Dynatrace environment.  
   For SaaS log ingestion, we recommend leaving the default value.

   `true`

   `selfMonitoringEnabled`

   Optional Send custom metrics to Google Cloud to quickly diagnose if `dynatrace-gcp-monitor` processes and sends logs to Dynatrace properly.For details, see [Self-monitoring metrics for the Dynatrace Google Cloud integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

   `false`

   `serviceAccount`

   Optional Name of the service account to be created.

   `dockerImage`

   OptionalDynatrace Google Cloud Monitor Docker image. We recommend using the default value, but you can adapt it if needed.

   `dynatrace/dynatrace-gcp-monitor:v1-latest`

   `printMetricIngestInput`

   Optional If set to `true`, the Google Cloud Monitor outputs the lines of metrics to stdout.

   `false`

   `serviceUsageBooking`

   Optional Service usage booking is used for metrics and determines a caller-specified project for quota and billing purposes.If set to `source`, monitoring API calls are booked in the project where the Kubernetes container is running.If set to `destination`, monitoring API calls are booked in the project that is monitored.For details, see [Monitor multiple Google Cloud projects - Standard environments - Step 4](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `source`

   `useProxy`

   Optional Depending on the value you set for this flag, the Google Cloud Monitor will use the following proxy settings: Dynatrace (set to `DT_ONLY`), Google Cloud API (set to `GCP_ONLY`), or both (set to `ALL`).

   By default, proxy settings are not used.

   `httpProxy`

   Optional The proxy HTTP address; use this flag in conjunction with `USE_PROXY`.

   `httpsProxy`

   Optional The proxy HTTPS address; use this flag in conjunction with `USE_PROXY`.

   `gcpServicesYaml`

   Optional Configuration file for Google Cloud services.

   `queryInterval`

   Optional Metrics polling interval in minutes. Allowed values: `1` - `6`

   `3`

   `scopingProjectSupportEnabled`

   Optional Set to `true` when metrics scope is configured, so metrics will be collected from all projects added to the metrics scope. For details, see [Monitor multiple Google Cloud projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `false`

   `excludedProjects`

   Optional Comma-separated list of projects to be excluded from monitoring (for example, `<project_A>,<project_B>`)

   `excludedMetricsAndDimensions`

   Optional Yaml formatted list of metrics and their dimensions to be excluded for monitoring.

   `metricAutodiscovery`

   Optional If set to `true`, the Google Cloud Monitor will run in metric auto-discovery mode, expanding your options for selecting metrics to monitor. For more information, see [Monitor Google Cloud projects using auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.").

   `clusterIpv4Cidr`

   Optional Set the IP address range for the pods in this cluster in CIDR notation, if you want to use a custom range.

   `servicesIpv4Cidr`

   Optional Set the IP range for the services IPs. It can be specified as a netmask size or as in the CIDR notion.

   `useCustomMasterCidr`

   Optional If set to `true`, you can specify the IPv4 CIDR range to use for the master network.

   `false`

   `masterIpv4Cidr`

   Optional IPv4 CIDR range to use for the master network requires the `useCustomMasterCidr` value to be true.
2. Choose which services you want Dynatrace to monitor.

   By default, the Dynatrace Google Cloud integration starts monitoring a set of selected services. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Connect your Kubernetes cluster

* If you want to have a new GKE Autopilot cluster created by the deployment script, add `--create-autopilot-cluster` to the script. Setting up a connection to the cluster will happen automatically in this case and you can proceed to [step 4](#script).
* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, you can connect to your cluster from the Google Cloud console or via terminal. Follow the instructions below.

From the Google Cloud console

Via terminal

1. In your Google Cloud console, go to your Kubernetes Engine.
2. Select **Clusters**, and then select **Connect**.
3. Select **Run in Cloud Shell**.

Run the command below, making sure to replace

* `<cluster>` with your cluster name
* `<region>` with the region where your cluster is running
* `<project>` with the project ID where your cluster is running

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

For details, see [Configuring cluster access for kubectlï»¿](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Step 4 Run the deployment script

* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, the deployment script will create an IAM service account with the necessary roles and deploy `dynatrace-gcp-monitor` to your Kubernetes cluster.
* If you run the deployment script with the `--create-autopilot-cluster` option, the deployment script will automatically create the new GKE Autopilot cluster and deploy `dynatrace-gcp-monitor` to it.

To run the deployment script, follow the instructions below.

Run on existing cluster

Run on new cluster

The latest versions of Google Cloud extensions will be uploaded. You have two options:

* Run the deployment script without parameters if you want to use the default values provided (`dynatrace-gcp-monitor-sa` for the IAM service account name and `dynatrace_monitor` for the IAM role name prefix):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Run the deployment script with parameters if you want to set your own values (be sure to replace the placeholders with your desired values):

```
cd helm-deployment-package



./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --without-extensions-upgrade
```

Run the command below. The latest versions of extensions will be uploaded.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

To set a different name for the new cluster, run the command below instead, making sure to replace the placeholder (`<name-of-new-cluster>`) with your preferred name.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
```

## Verify installation

To check whether installation was successful

1. Check if the container is running.

   After the installation, it may take a couple of minutes before the container is up and running.

   ```
   kubectl -n dynatrace get pods
   ```
2. Check the container logs for errors or exceptions. You have two options:

In the Kubernetes CLI

In your Google Cloud console

Run the following command.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics
```

To check the container logs for errors in your Google Cloud console

1. Go to **Logs explorer**.
2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"`

3. Check if dashboards are imported.

   Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Choose services for metrics monitoring

### Services enabled by default

Monitoring of following services will be enabled during deployment of Google Cloud Monitor:

* [Google APIs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")
* [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")
* [Google BigQuery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")
* [Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")
* [Google Cloud Run](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")
* [Google Cloud Storage](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")
* [Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")
* [Google Firestore in Datastore mode](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")
* [Google Filestore](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")
* [Google Kubernetes Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")
* [Google Cloud Load Balancing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")
* [Google Cloud Pub/Sub](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")
* [Google Cloud Pub/Sub Lite](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")
* [Google Cloud SQL](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

There are more service integrations available, but need to be enabled. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services. The next section describes how to manage them. For an alternative approach, consider leveraging [auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.") to extend your metric coverage.

### Manage enabled services

You can manage enabled services via Dynatrace Hub.

Filter for "gcp"âyou'll find annotations in the results for items that are already available in your environment.

To enable a new service, select it in Hub and then install it.

You can also disable a service via Dynatrace Hub.

To see if the services need updating, open them in Hub and check release notes. The updates can include new metrics, new assets like dashboards, or other changes.

All changes to enabled services are applied to Google Cloud Monitor within few minutes.

#### Feature sets & available metrics

To see what metrics are included for specific service, check [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics."). By default, only `defaultMetrics` feature set is enabled. To enable additional feature sets, you have to uncomment them in `values.yaml` file and redeploy whole Google Cloud Monitor.

Current configuration of feature sets can be found in cluster's ConfigMap named `dynatrace-gcp-function-config`.

#### Advanced scope management

To further refine monitoring scope, you can use `filter_conditions` field in `values.yaml` file. This requires Google Cloud Monitor to be redeployed. See [Google Cloud Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US) for syntax.

Example:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for Google Cloud alerts and turn on **On/Off** for the alerts you want to activate.

## View metrics

After deploying the integration, you can see metrics from monitored services (go to **Metrics** and filter by `gcp`).

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Run the command below, making sure to replace `<your-helm-release>` with the value from the previous step.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

For details, see [Helm upgradeï»¿](https://helm.sh/docs/helm/helm_upgrade/).

### Change deployment type

To change the deployment type (`all`, `metrics`, or `logs`)

1. Find out what helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<your-helm-release>` with the release name from the previous output.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Edit `deploymentType` in `values.yaml` with the new value and save the file.
4. Run the deployment command again. For details, see [Run the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check container logs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Uninstall

1. Find out what Helm release version you're using.

```
helm ls -n dynatrace
```

2. Uninstall the release.

Be sure to replace `<your-helm-release>` with the release name from the previous output.

```
helm uninstall <your-helm-release> -n dynatrace
```

Alternatively, you can delete the namespace.

```
kubectl delete namespace dynatrace
```

3. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

Make sure to uninstall the initial Role created and attached to the Service Account that you used to deploy the integration.

## Monitoring consumption

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)


---


## Source: set-up-gcp-integration-on-existing-cluster.md


---
title: Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster
scraped: 2026-02-17T05:06:32.095074
---

# Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster

# Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), where the deployment script runs in a new automatically created GKE Autopilot cluster, you can choose to run the deployment script on an existing standard GKE or GKE Autopilot cluster. In this scenario, you will set up Google Cloud monitoring for metrics and logs in Google Cloud Shell. During setup, a new Pub/Sub subscription will be created. GKE will run two containers: a metric forwarder and a log forwarder. After installation, you'll get metrics, logs, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

Dynatrace version 1.230+

This page describes how to install version 1.0 of the Google Cloud integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace Google Cloud log integration supports up to 8 GB of data processing per hour (with base resourcesâwithout scaling). With bigger loads, messages will start to be retained in the PubSub Subscription. To measure latency, look for these metrics: `Oldest unacked message age` and `Unacked messages`. For scaling recommendations, see the [scaling guide](#scalingguide) below.

Dynatrace Google Cloud metric integration supports up to 50 Google Cloud projects with the standard deployment. To monitor larger environments, you need to enable metrics scope. See [Monitor multiple Google Cloud projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

## Prerequisites

To deploy the integration, you need to make sure the following requirements are met on the machine where you are running the installation.

* Linux OS only
* Internet access
* GKE Cluster access
* Dynatrace environment access

  You need to configure the Dynatrace endpoint (environment, cluster or ActiveGate URL) to which the GKE cluster should send metrics and logs. Make sure that you have direct network access or, if there is a proxy or any other component present in between, that communication is not affected.

### Tools

You can deploy the Dynatrace GCP integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [kubectlï»¿](https://kubernetes.io/docs/tasks/tools/)
* [helmï»¿](https://helm.sh/docs/intro/install/)
* [jq (version 1.6)ï»¿](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (version 4.9.x+)ï»¿](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role (see below) and use it to deploy `dynatrace-gcp-monitor`.

1. Create a YAML file named `dynatrace-gcp-monitor-helm-deployment-role.yaml` with the following content:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Each group of permissions is used to handle the different resources included in the integration. Creation and access are for new resources, update is for reusing existing resources, and deletion is for uninstalling.

* container.configMaps: for mapping secrets and other variables used by the containers.
* container.deployments: for the K8s' deployment within the cluster (which includes the pods, containers, etc.).
* container.namespaces: for the K8s namespace in which we are deploying the resources.
* container.pods: for the K8s pods.
* container.secrets: for the K8s secrets in which to store the data-sensitive variables.
* container.serviceAccounts: for the SA to be taken in the K8s context.
* iam.roles: for the necessary permissions for data collection.
* iam.serviceAccounts: for the general context SA.
* resourcemanager.projects: for handling the project in which we are deploying our integration.
* serviceusage.services: for handling the services' APIs.
* pubsub.subscriptions: for the PubSub subscription we are using to collect and ingest logs.
* pubsub.topics: for the PubSub topic we are using to collect and ingest logs.

2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Google Cloud settings

The location where you deploy the integration determines whether you need make any additional settings.

#### Deploy on an existing GKE Autopilot cluster

If you deploy the integration on an existing GKE Autopilot cluster, you don't need to make any additional settings.

#### Deploy on an existing GKE standard cluster

If you deploy the integration on an existing GKE standard cluster, you need to

* [Enable Workload Identity on a clusterï»¿](https://dt-url.net/2j23qqv)
* [Enable `GKE_METADATA` on the GKE node poolsï»¿](https://dt-url.net/an43q2s)

### Configure log export

1. Run the following shell script in the Google Cloud project you've selected for deployment.

Be sure to replace `<your-subscription-name>` and `<your-topic-name>` with your own values.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Configure [log exportï»¿](https://dt-url.net/4743r02) to send the desired logs to the Google Cloud Pub/Sub topic created above.

### Dynatrace permissions

You need to create a token with a set of permissions.

1. Go to **Access tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Under **Template**, select `GCP Services Monitoring`.
5. Select **Generate**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

Alternatively, you can create the token and add permissions manually.

Add manually

[Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permissions](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extensions monitoring configuration**
  + **Write extensions monitoring configuration**
  + **Read extensions environment configuration**
  + **Write extensions environment configuration**
  + **Ingest logs**
  + **Manage metadata of Hub items**
  + **Read Hub related data**
  + **Install and update Hub items**

To monitor logs from multiple projects, you need to create **Log Routing Sinks** in each source project selecting as a destination for your main project (in which you also deployed the integration and the PubSub Topic and Subscription).
For more information, see [Route logs to supported destinationsï»¿](https://dt-url.net/cl038gj).

### Log ingestion

* Determine where log ingestion will be performed, according to your deployment. This distinction is important when configuring the [parameters](#param) for this integration.

  + **For SaaS deployments:** SaaS log ingest, where log ingestion is performed directly through the Cluster API. Recommended
  + **For Managed deployments:** You can use an existing ActiveGate for log ingestion. For information on how to deploy it, see [ActiveGate installation](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

Because of GCP's implementation of Cloud Function 2nd gen, logs from those resources will be linked to the underlying Cloud Run instances. Both extensions will have to be enabled.

To learn more, visit [Google Cloud Functions version comparisonï»¿](https://dt-url.net/b6038q5).

## Install

Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#dwld "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#param "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect your Kubernetes cluster**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#connect "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#script "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

1. The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor`and edit the `values.yaml` file, setting the required and optional parameter values as follows.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

   **Parameter name**

   **Description**

   **Default value**

   `parallelProcesses`

   Optional Number of parallel processes to run the whole log monitoring loop

   `1`

   `numberOfConcurrentLogForwardingLoops`

   Optional Number of workers pulling logs from pubsub concurrently and pushing them to Dynatrace

   `5`

   `numberOfConcurrentMessagePullCoroutines`

   Optional Number of concurrent coroutines to pull messages from pub/sub

   `10`

   `numberOfConcurrentPushCoroutines`

   Optional Number of concurrent coroutines to push messages to Dynatrace

   `5`

   `gcpProjectId`

   Required The ID of the GCP project you've selected for deployment.

   Your current project ID

   `deploymentType`

   Required Leave to `all`.

   `all`

   `dynatraceAccessKey`

   Required Your [Dynatrace API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the [required permissions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

   `dynatraceUrl`

   Required For SaaS log/metric ingestion, it's your environment URL (`https://<your-environment-id>.live.dynatrace.com`).

   `logsSubscriptionId`

   Required The ID of your log Sink Pub/Sub subscription. For details, see [Configure log export](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

   `dynatraceLogIngestUrl`

   Optional You can set it if you want to ingest logs separately from metrics.For SaaS log ingestion, it's your environment URL (`https://<your_environment_ID>.live.dynatrace.com`).

   `dynatraceAccessKeySecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceAccessKey`.

   `dynatraceUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceUrl`.

   `dtSecurityContext`

   Optional Assign the attribute value used for data segmentation, analysis, and permission mapping within the Dynatrace platform. Refer to [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") for more information. If left empty, the value of `gcpProjectId` will be assigned automatically.

   Value of `gcpProjectId`

   `dynatraceLogIngestUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceLogIngestUrl`.

   `requireValidCertificate`

   Optional If set to `true`, Dynatrace requires the SSL certificate of your Dynatrace environment.For SaaS log ingestion, we recommend leaving the default value.

   `true`

   `selfMonitoringEnabled`

   Optional Send custom metrics to GCP to quickly diagnose if `dynatrace-gcp-monitor` processes and sends metrics/logs to Dynatrace properly.For details, see [Self-monitoring metrics for the Dynatrace GCP integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

   `false`

   `serviceAccount`

   Optional Name of the service account to be created.

   `dockerImage`

   OptionalDynatrace GCP Monitor docker image. We recommend using the default value, but you can adapt it if needed.

   `dynatrace/dynatrace-gcp-monitor:v1-latest`

   `logIngestContentMaxLength`

   Optional The maximum content length of a log event. Should be less than or equal to the setting on your Dynatrace environment.

   `8192`

   `logIngestAttributeValueMaxLength`

   Optional The maximum length of the log event attribute value. If it exceeds the server limit, content will be truncated.

   `250`

   `logIngestRequestMaxEvents`

   Optional The maximum number of log events in a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `5000`

   `logIngestRequestMaxSize`

   Optional The maximum size in bytes of a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `1048576`

   `logIngestEventMaxAgeSeconds`

   Optional Determines the maximum age of a forwarded log event. Should be less than or equal to the setting on your Dynatrace environment.

   `86400`

   `printMetricIngestInput`

   Optional If set to `true`, the GCP Monitor outputs the lines of metrics to stdout.

   `false`

   `serviceUsageBooking`

   Optional Service usage booking is used for metrics and determines a caller-specified project for quota and billing purposes. If set to `source`, monitoring API calls are booked in the project where the Kubernetes container is running. If set to `destination`, monitoring API calls are booked in the project that is monitored. For details, see [Monitor multiple GCP projects - Standard environments - Step 4](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `source`

   `useProxy`

   Optional Depending on the value you set for this flag, the GCP Monitor will use the following proxy settings: Dynatrace (set to `DT_ONLY`), GCP API (set to `GCP_ONLY`), or both (set to `ALL`).

   By default, proxy settings are not used.

   `httpProxy`

   Optional The proxy HTTP address; use this flag in conjunction with `USE_PROXY`.

   `httpsProxy`

   Optional The proxy HTTPS address; use this flag in conjunction with `USE_PROXY`.

   `gcpServicesYaml`

   Optional Configuration file for GCP services.

   `queryInterval`

   Optional Metrics polling interval in minutes. Allowed values: `1` - `6`

   `3`

   `scopingProjectSupportEnabled`

   Optional Set to `true` when metrics scope is configured, so metrics will be collected from all projects added to the metrics scope.For details, see [Monitor multiple GCP projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `false`

   `excludedProjects`

   Optional Comma-separated list of projects to be excluded from monitoring (for example, `<project_A>,<project_B>`)

   `excludedMetricsAndDimensions`

   Optional Yaml formatted list of metrics and their dimensions to be excluded for monitoring.

   `metricAutodiscovery`

   Optional If set to `true`, the GCP Monitor will run metric auto-discovery mode, expanding your options for selecting metrics to monitor. For more information, see [Monitor GCP projects using auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.").

   `false`
2. Choose which services you want Dynatrace to monitor.

   By default, the Dynatrace Google Cloud integration starts monitoring a set of selected services. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Connect your Kubernetes cluster

To connect to your existing GKE standard cluster or existing GKE Autopilot cluster, run the command below, making sure to replace

* `<cluster>` with your cluster name
* `<region>` with the region where your cluster is running
* `<project>` with the project ID where your cluster is running

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

For details, see [Configuring cluster access for kubectlï»¿](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Step 4 Run the deployment script

The deployment script will create an IAM service account with the necessary roles and deploy `dynatrace-gcp-monitor` to your GKE cluster. The latest versions of Google Cloud extensions will be uploaded.

You have two options:

* Run the deployment script without parameters if you want to use the default values provided (`dynatrace-gcp-monitor-sa` for the IAM service account name and `dynatrace_monitor` for the IAM role name prefix):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Run the deployment script with parameters if you want to set your own values (be sure to replace the placeholders with your desired values):

```
cd helm-deployment-package



./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --without-extensions-upgrade
```

## Verify installation

To check whether installation was successful

1. Check if the container is running.

   After the installation, it may take couple of minutes until the container is up and running.

   ```
   kubectl -n dynatrace get pods
   ```
2. Check the container logs for errors or exceptions. You have two options:

In the Kubernetes CLI

In your Google Cloud console

Run the following commands.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics



kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

To check the container logs for errors in your Google Cloud console

1. Go to **Logs explorer**.
2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (for metric ingest logs)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (for log ingest logs)

3. Check if dashboards are imported.

   Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Choose services for metrics monitoring

### Services enabled by default

Monitoring of following services will be enabled during deployment of Google Cloud Monitor:

* [Google APIs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")
* [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")
* [Google BigQuery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")
* [Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")
* [Google Cloud Run](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")
* [Google Cloud Storage](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")
* [Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")
* [Google Firestore in Datastore mode](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")
* [Google Filestore](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")
* [Google Kubernetes Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")
* [Google Cloud Load Balancing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")
* [Google Cloud Pub/Sub](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")
* [Google Cloud Pub/Sub Lite](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")
* [Google Cloud SQL](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

There are more service integrations available, but need to be enabled. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services. Next section describes how to manage them. For an alternative approach, consider leveraging [auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.") to extend your metric coverage.

### Manage enabled services

You can manage enabled services via Dynatrace Hub.

Filter for "gcp"âyou'll find annotations in the results for items that are already available in your environment.

To enable a new service, select it in Hub and then install it.

You can also disable a service via Dynatrace Hub.

To see if the services need updating, open them in Hub and check release notes. The updates can include new metrics, new assets like dashboards, or other changes.

All changes to enabled services are applied to Google Cloud Monitor within few minutes.

#### Feature sets & available metrics

To see what metrics are included for specific service, check [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics."). By default, only `defaultMetrics` feature set is enabled. To enable additional feature sets, you have to uncomment them in `values.yaml` file and redeploy whole Google Cloud Monitor.

Current configuration of feature sets can be found in cluster's ConfigMap named `dynatrace-gcp-function-config`.

#### Advanced scope management

To further refine monitoring scope, you can use `filter_conditions` field in `values.yaml` file. This requires Google Cloud Monitor to be redeployed. See [Google Cloud Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US) for syntax.

Example:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. Select **Anomaly detection** > **Metric events**.
3. Filter for Google Cloud alerts and turn on **On/Off** for the alerts you want to activate.

## View metrics and logs

After deploying the integration, depending on your deployment type, you can:

* See metrics from monitored services: go to **Metrics** and filter by `gcp`.
* View and analyze Google Cloud logs: in Dynatrace, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and, to look for Google Cloud logs, filter by `cloud.provider: gcp`.

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Run the command below, making sure to replace `<your-helm-release>` with the value from the previous step.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

For details, see [Helm upgradeï»¿](https://helm.sh/docs/helm/helm_upgrade/).

### Change deployment type

To change the deployment type (`all`, `metrics`, or `logs`)

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<your-helm-release>` with the release name from the previous output.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Edit `deploymentType` in `values.yaml` with the new value and save the file.
4. Run the deployment command again. For details, see [Run the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check container logs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Scaling guide for logs

The default container with 1.25vCPU and 1Gi (with default configuration) can handle 8 GB of log throughput per hour. Achieving more throughput requires allocating more resources to the container (scale up), increasing the number of container replicas (scale out), and changing configuration numbers to use allocated resources efficiently. All config variables can be found and changed in `dynatrace-gcp-monitor-config`.

The following table presents tested configuration and achieved throughput with scaled up&out containers:

Achieved throughput

Machine resources

Replica sets

Config variable values

~8MB/s => ~480MB/min

4vCPU 4Gi RAM

1

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~25MB/s => ~1.5GB/min => ~2TB/day

4vCPU 4Gi RAM

4

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~46MB/s => ~2.7GB/min => ~4TB/day

4vCPU 4Gi RAM

6

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

## Autoscaling guide for logs

Autoscaling works only for `logs` type of deployment, not `all`.

We recommend manually scaling the container to have a 4vCPU 4Gi machine and then enabling autoscaling.

GCP provides autoscaling of containers in both directions: **horizontal** and **vertical**. However, Dynatrace recommends only **horizontal** scaling.

If you have a 4vCPU 4Gi machine, you can enable autoscaling **horizontally**. However, we **don't** recommend scaling horizontally with the base resources of the container (1.25vCPU, 1Gi). It hasn't been proven to be efficient during testing. One 4vCPU machine does better than four 1vCPU machines. To enable autoscaling horizontally, use the horizontal autoscaling command:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Autoscaling is recommended only when you have a minimum of 450 MB/min throughput and can provide a 4vCPU 4Gi RAM machine. Autoscaling is only scaling out, not scaling the machine up.

We **don't** recommend scaling **vertically** because every time a machine is scaled up, an environment variable needs to be changed to create more processes corresponding to machine cores.

## Uninstall

1. Find out what Helm release version you're using.

```
helm ls -n dynatrace
```

2. Uninstall the release.

Be sure to replace `<your-helm-release>` with the release name from the previous output.

```
helm uninstall <your-helm-release> -n dynatrace
```

Alternatively, you can delete the namespace.

```
kubectl delete namespace dynatrace
```

3. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

Make sure to uninstall the following resources manually:

* The initial Role created and attached to the Service Account that you used to deploy the integration.
* The PubSub Topic.
* The PubSub Subscription.
* The LogRoute Sink.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)


---


## Source: gcp-guide.md


---
title: End-to-end guide for monitoring Google Cloud services integrating Operations Suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide
scraped: 2026-02-17T21:31:05.475320
---

# End-to-end guide for monitoring Google Cloud services integrating Operations Suite

# End-to-end guide for monitoring Google Cloud services integrating Operations Suite

* Latest Dynatrace
* Overview
* 2-min read
* Published Jan 17, 2022

Dynatrace perfectly integrates with Google Cloud to provide deep visibility into the workloads that are running on this platform.

## Google Cloud supported services

Dynatrace can analyze metrics from all services available in Google Operations API. To learn about monitoring the Google Cloud supported services, capabilities and configuration options, see [Google Cloud supported service metrics](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").

## Google Cloud overview

Dynatrace provides the Google Cloud overview page. It includes views per Google Cloud project and lists of instances for VMs, SQLs, Cloud Functions, and Kubernetes.

If you are already monitoring Google Cloud and the overview is not available, you need to update the Google Cloud integration you have.

## Set up metric and log ingest

To start analyzing metrics and logs from all services available in the Google Operations API, see [Set up the Dynatrace Google Cloud metric and log integration on a new GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") Recommended.

For other deployment options, see

* [Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")
* [Set up the Dynatrace Google Cloud metric integration on a GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only "Set up metric monitoring for Google Cloud services on a GKE cluster.")
* [Set up the Dynatrace Google Cloud log integration on a GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")
* [Deploy the Dynatrace Google Cloud metric integration in Google Cloud Function](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Set up monitoring for Google Cloud services in Google Cloud Functions.")

The [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") describes how to install version 1.0 of the Google Cloud integration on a GKE cluster. If you already have earlier versions installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

After deploying the integration, [you can push metrics to Dynatrace from multiple Google Cloud projects](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

To check if your monitoring function processes and sends logs to Dynatrace properly, see [Self-monitoring for the Dynatrace Google Cloud integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")


---


## Source: gcp-apigee-monitoring.md


---
title: Google Cloud Apigee monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring
scraped: 2026-02-17T21:26:14.132652
---

# Google Cloud Apigee monitoring

# Google Cloud Apigee monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Apigee.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| apigee\_googleapis\_com\_Environment/default\_metrics | Apigee anomaly event count | Count | apigee.googleapis.com/environment/anomaly\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee policy response latencies | MilliSecond | apigee.googleapis.com/policy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response latencies | MilliSecond | apigee.googleapis.com/proxy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy request cumulative count | Count | apigee.googleapis.com/proxy/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response cumulative count | Count | apigee.googleapis.com/proxy/response\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response latencies | MilliSecond | apigee.googleapis.com/target/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target request cumulative count | Count | apigee.googleapis.com/target/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response cumulative count | Count | apigee.googleapis.com/target/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee policy response latencies | MilliSecond | apigee.googleapis.com/policyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee proxy response latencies | MilliSecond | apigee.googleapis.com/proxyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy request cumulative count | Count | apigee.googleapis.com/proxyv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy response cumulative count | Count | apigee.googleapis.com/proxyv2/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target request cumulative count | Count | apigee.googleapis.com/targetv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target response cumulative count | Count | apigee.googleapis.com/targetv2/response\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-apis-monitoring.md


---
title: Google Cloud APIs monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring
scraped: 2026-02-17T05:07:39.337816
---

# Google Cloud APIs monitoring

# Google Cloud APIs monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud APIs.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| api/default\_metrics | Request count | Count | serviceruntime.googleapis.com/api/request\_count |
| api/default\_metrics | Request latencies | Second | serviceruntime.googleapis.com/api/request\_latencies |
| api/default\_metrics | Request backend latencies | Second | serviceruntime.googleapis.com/api/request\_latencies\_backend |
| api/default\_metrics | Request overhead latencies | Second | serviceruntime.googleapis.com/api/request\_latencies\_overhead |
| consumer\_quota/default\_metrics | Allocation quota usage | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| consumer\_quota/default\_metrics | Quota exceeded error | Count | serviceruntime.googleapis.com/quota/exceeded |
| consumer\_quota/default\_metrics | Quota limit | Count | serviceruntime.googleapis.com/quota/limit |
| consumer\_quota/default\_metrics | Rate quota usage | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |
| consumed\_api/default\_metrics | Request count | Count | serviceruntime.googleapis.com/api/request\_count |
| consumed\_api/default\_metrics | Request latencies | Second | serviceruntime.googleapis.com/api/request\_latencies |
| consumed\_api/default\_metrics | Request sizes | Byte | serviceruntime.googleapis.com/api/request\_sizes |
| consumed\_api/default\_metrics | Response sizes | Byte | serviceruntime.googleapis.com/api/response\_sizes |
| producer\_quota/default\_metrics | Allocation quota usage | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| producer\_quota/default\_metrics | Quota limit | Count | serviceruntime.googleapis.com/quota/limit |
| producer\_quota/default\_metrics | Rate quota usage | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-assistant-smart-home-monitoring.md


---
title: Google Cloud Assistant Smart Home monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring
scraped: 2026-02-17T05:07:21.711342
---

# Google Cloud Assistant Smart Home monitoring

# Google Cloud Assistant Smart Home monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Assistant Smart Home.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| assistant\_action\_project/default\_metrics | Daily active users | Count | actions.googleapis.com/smarthome\_action/num\_active\_users |
| assistant\_action\_project/default\_metrics | Request count | Count | actions.googleapis.com/smarthome\_action/request\_count |
| assistant\_action\_project/default\_metrics | Request latencies | MilliSecond | actions.googleapis.com/smarthome\_action/request\_latencies |
| assistant\_action\_project/default\_metrics | 7 day active users | Count | actions.googleapis.com/smarthome\_action/seven\_day\_active\_users |
| assistant\_action\_project/default\_metrics | 28 day active users | Count | actions.googleapis.com/smarthome\_action/twenty\_eight\_day\_active\_users |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-bigtable-monitoring.md


---
title: Google Cloud Bigtable monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring
scraped: 2026-02-17T05:11:39.005589
---

# Google Cloud Bigtable monitoring

# Google Cloud Bigtable monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Bigtable.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| bigtable\_cluster/default\_metrics | CPU load | Count | bigtable.googleapis.com/cluster/cpu\_load |
| bigtable\_cluster/default\_metrics | CPU load (hottest node) | Count | bigtable.googleapis.com/cluster/cpu\_load\_hottest\_node |
| bigtable\_cluster/default\_metrics | Disk load | Count | bigtable.googleapis.com/cluster/disk\_load |
| bigtable\_cluster/default\_metrics | Nodes | Count | bigtable.googleapis.com/cluster/node\_count |
| bigtable\_cluster/default\_metrics | Storage utilization | Count | bigtable.googleapis.com/cluster/storage\_utilization |
| bigtable\_cluster/default\_metrics | Data stored | Byte | bigtable.googleapis.com/disk/bytes\_used |
| bigtable\_cluster/default\_metrics | Storage capacity per node | Byte | bigtable.googleapis.com/disk/per\_node\_storage\_capacity |
| bigtable\_cluster/default\_metrics | Storage capacity | Byte | bigtable.googleapis.com/disk/storage\_capacity |
| bigtable\_table/default\_metrics | Replication latencies | MilliSecond | bigtable.googleapis.com/replication/latency |
| bigtable\_table/default\_metrics | Replication maximum delay | Second | bigtable.googleapis.com/replication/max\_delay |
| bigtable\_table/default\_metrics | Error count | Count | bigtable.googleapis.com/server/error\_count |
| bigtable\_table/default\_metrics | Server Latencies | MilliSecond | bigtable.googleapis.com/server/latencies |
| bigtable\_table/default\_metrics | Modified rows | Count | bigtable.googleapis.com/server/modified\_rows\_count |
| bigtable\_table/default\_metrics | Multi-cluster failovers | Count | bigtable.googleapis.com/server/multi\_cluster\_failovers\_count |
| bigtable\_table/default\_metrics | Received bytes | Byte | bigtable.googleapis.com/server/received\_bytes\_count |
| bigtable\_table/default\_metrics | Request count | Count | bigtable.googleapis.com/server/request\_count |
| bigtable\_table/default\_metrics | Returned rows | Count | bigtable.googleapis.com/server/returned\_rows\_count |
| bigtable\_table/default\_metrics | Sent bytes | Byte | bigtable.googleapis.com/server/sent\_bytes\_count |
| bigtable\_table/default\_metrics | Data stored | Byte | bigtable.googleapis.com/table/bytes\_used |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-composer-monitoring.md


---
title: Google Cloud Composer monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring
scraped: 2026-02-16T09:39:20.654753
---

# Google Cloud Composer monitoring

# Google Cloud Composer monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Composer.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_composer\_environment/default\_metrics | API Requests | Count | composer.googleapis.com/environment/api/request\_count |
| cloud\_composer\_environment/default\_metrics | API Latency | MilliSecond | composer.googleapis.com/environment/api/request\_latencies |
| cloud\_composer\_environment/default\_metrics | Parse Error Count | Count | composer.googleapis.com/environment/dag\_processing/parse\_error\_count |
| cloud\_composer\_environment/default\_metrics | DAG parsing processes | Count | composer.googleapis.com/environment/dag\_processing/processes |
| cloud\_composer\_environment/default\_metrics | Processors Timeout Count | Count | composer.googleapis.com/environment/dag\_processing/processor\_timeout\_count |
| cloud\_composer\_environment/default\_metrics | Total Parse Time | Second | composer.googleapis.com/environment/dag\_processing/total\_parse\_time |
| cloud\_composer\_environment/default\_metrics | Dag Bag Size | Count | composer.googleapis.com/environment/dagbag\_size |
| cloud\_composer\_environment/default\_metrics | Database Healthy | Unspecified | composer.googleapis.com/environment/database\_health |
| cloud\_composer\_environment/default\_metrics | Executor Open Slots | Count | composer.googleapis.com/environment/executor/open\_slots |
| cloud\_composer\_environment/default\_metrics | Executor Running Tasks | Count | composer.googleapis.com/environment/executor/running\_tasks |
| cloud\_composer\_environment/default\_metrics | Task Instance Count | Count | composer.googleapis.com/environment/finished\_task\_instance\_count |
| cloud\_composer\_environment/default\_metrics | Healthy | Unspecified | composer.googleapis.com/environment/healthy |
| cloud\_composer\_environment/default\_metrics | Celery Workers | Count | composer.googleapis.com/environment/num\_celery\_workers |
| cloud\_composer\_environment/default\_metrics | Scheduler Heartbeats | Count | composer.googleapis.com/environment/scheduler\_heartbeat\_count |
| cloud\_composer\_environment/default\_metrics | Task Queue Length | Count | composer.googleapis.com/environment/task\_queue\_length |
| cloud\_composer\_environment/default\_metrics | Worker Pod Eviction Count | Count | composer.googleapis.com/environment/worker/pod\_eviction\_count |
| cloud\_composer\_environment/default\_metrics | Zombie Tasks Killed | Count | composer.googleapis.com/environment/zombie\_task\_killed\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-data-loss-prevention-monitoring.md


---
title: Google Cloud Data Loss Prevention monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring
scraped: 2026-02-16T09:36:47.557826
---

# Google Cloud Data Loss Prevention monitoring

# Google Cloud Data Loss Prevention monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Data Loss Prevention.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_dlp\_project/default\_metrics | Content bytes inspected | Byte | dlp.googleapis.com/content\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Content bytes transformed | Byte | dlp.googleapis.com/content\_bytes\_transformed\_count |
| cloud\_dlp\_project/default\_metrics | Findings | Count | dlp.googleapis.com/finding\_count |
| cloud\_dlp\_project/default\_metrics | Job results | Count | dlp.googleapis.com/job\_result\_count |
| cloud\_dlp\_project/default\_metrics | Job trigger runs | Count | dlp.googleapis.com/job\_trigger\_run\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes inspected | Byte | dlp.googleapis.com/storage\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes transformed | Byte | dlp.googleapis.com/storage\_bytes\_transformed\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-dns-monitoring.md


---
title: Google Cloud DNS monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-dns-monitoring
scraped: 2026-02-17T21:32:01.549615
---

# Google Cloud DNS monitoring

# Google Cloud DNS monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud DNS.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| dns\_query/default\_metrics | DNS response counts | Unspecified | dns.googleapis.com/query/response\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-firestore-monitoring.md


---
title: Google Cloud Firestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring
scraped: 2026-02-17T05:10:51.376490
---

# Google Cloud Firestore monitoring

# Google Cloud Firestore monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Firestore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| firestore\_instance/default\_metrics | Document Deletes | Count | firestore.googleapis.com/document/delete\_count |
| firestore\_instance/default\_metrics | Document Reads | Count | firestore.googleapis.com/document/read\_count |
| firestore\_instance/default\_metrics | Document Writes | Count | firestore.googleapis.com/document/write\_count |
| firestore\_instance/default\_metrics | Connected Clients | Count | firestore.googleapis.com/network/active\_connections |
| firestore\_instance/default\_metrics | Snapshot Listeners | Count | firestore.googleapis.com/network/snapshot\_listeners |
| firestore\_instance/default\_metrics | Rule Evaluations | Count | firestore.googleapis.com/rules/evaluation\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-iot-core-monitoring.md


---
title: Google Cloud IoT Core monitoring (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring
scraped: 2026-02-17T21:26:50.127180
---

# Google Cloud IoT Core monitoring (deprecated)

# Google Cloud IoT Core monitoring (deprecated)

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud IoT Core.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloudiot\_device\_registry/default\_metrics | Active devices | Count | cloudiot.googleapis.com/device/active\_devices |
| cloudiot\_device\_registry/default\_metrics | Billable bytes transferred | Byte | cloudiot.googleapis.com/device/billing\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Errors communicating with devices | Count | cloudiot.googleapis.com/device/error\_count |
| cloudiot\_device\_registry/default\_metrics | Operations | Count | cloudiot.googleapis.com/device/operation\_count |
| cloudiot\_device\_registry/default\_metrics | Bytes received by devices | Byte | cloudiot.googleapis.com/device/received\_bytes\_count |
| cloudiot\_device\_registry/default\_metrics | Bytes sent to devices | Byte | cloudiot.googleapis.com/device/sent\_bytes\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-load-balancing-monitoring.md


---
title: Google Cloud Load Balancing monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring
scraped: 2026-02-16T09:35:45.918996
---

# Google Cloud Load Balancing monitoring

# Google Cloud Load Balancing monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Load Balancing.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| https\_lb\_rule/default\_metrics | Backend latency | MilliSecond | loadbalancing.googleapis.com/https/backend\_latencies |
| https\_lb\_rule/default\_metrics | Backend Request Bytes | Byte | loadbalancing.googleapis.com/https/backend\_request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Backend Request Count | Count | loadbalancing.googleapis.com/https/backend\_request\_count |
| https\_lb\_rule/default\_metrics | Backend Response Bytes | Byte | loadbalancing.googleapis.com/https/backend\_response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Frontend RTT | MilliSecond | loadbalancing.googleapis.com/https/frontend\_tcp\_rtt |
| https\_lb\_rule/default\_metrics | Request bytes | Byte | loadbalancing.googleapis.com/https/request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Request count | Count | loadbalancing.googleapis.com/https/request\_count |
| https\_lb\_rule/default\_metrics | Response bytes | Byte | loadbalancing.googleapis.com/https/response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Total latency | MilliSecond | loadbalancing.googleapis.com/https/total\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Backend latencies | MilliSecond | loadbalancing.googleapis.com/https/internal/backend\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Request bytes | Byte | loadbalancing.googleapis.com/https/internal/request\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Request count | Count | loadbalancing.googleapis.com/https/internal/request\_count |
| internal\_http\_lb\_rule/default\_metrics | Response bytes | Byte | loadbalancing.googleapis.com/https/internal/response\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Total latencies | MilliSecond | loadbalancing.googleapis.com/https/internal/total\_latencies |
| internal\_tcp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | RTT latencies | MilliSecond | loadbalancing.googleapis.com/l3/internal/rtt\_latencies |
| internal\_udp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | RTT latencies | MilliSecond | loadbalancing.googleapis.com/l3/external/rtt\_latencies |
| udp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| udp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Closed connections | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/closed\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/egress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Frontend RTT | MilliSecond | loadbalancing.googleapis.com/tcp\_ssl\_proxy/frontend\_tcp\_rtt |
| tcp\_ssl\_proxy\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/ingress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | New connections opened | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/new\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Open Connections | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/open\_connections |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-sql.md


---
title: Google Cloud SQL monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql
scraped: 2026-02-17T21:33:59.423391
---

# Google Cloud SQL monitoring

# Google Cloud SQL monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud SQL.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloudsql\_database/default\_metrics | Auto-failover Requests | Count | cloudsql.googleapis.com/database/auto\_failover\_request\_count |
| cloudsql\_database/default\_metrics | Available for failover | Count | cloudsql.googleapis.com/database/available\_for\_failover |
| cloudsql\_database/default\_metrics | CPU reserved cores | Count | cloudsql.googleapis.com/database/cpu/reserved\_cores |
| cloudsql\_database/default\_metrics | CPU usage | Second | cloudsql.googleapis.com/database/cpu/usage\_time |
| cloudsql\_database/default\_metrics | CPU utilization | Percent | cloudsql.googleapis.com/database/cpu/utilization |
| cloudsql\_database/default\_metrics | Bytes used | Byte | cloudsql.googleapis.com/database/disk/bytes\_used |
| cloudsql\_database/default\_metrics | Disk quota | Byte | cloudsql.googleapis.com/database/disk/quota |
| cloudsql\_database/default\_metrics | Disk read IO | Count | cloudsql.googleapis.com/database/disk/read\_ops\_count |
| cloudsql\_database/default\_metrics | Disk utilization | Count | cloudsql.googleapis.com/database/disk/utilization |
| cloudsql\_database/default\_metrics | Disk write IO | Count | cloudsql.googleapis.com/database/disk/write\_ops\_count |
| cloudsql\_database/default\_metrics | Instance state | Unspecified | cloudsql.googleapis.com/database/instance\_state |
| cloudsql\_database/default\_metrics | Memory quota | Byte | cloudsql.googleapis.com/database/memory/quota |
| cloudsql\_database/default\_metrics | Total memory usage | Byte | cloudsql.googleapis.com/database/memory/total\_usage |
| cloudsql\_database/default\_metrics | Memory usage | Byte | cloudsql.googleapis.com/database/memory/usage |
| cloudsql\_database/default\_metrics | Memory utilization | Count | cloudsql.googleapis.com/database/memory/utilization |
| cloudsql\_database/default\_metrics | InnoDB dirty pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_dirty |
| cloudsql\_database/default\_metrics | InnoDB free pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_free |
| cloudsql\_database/default\_metrics | InnoDB total pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_total |
| cloudsql\_database/default\_metrics | InnoDB fsync calls | Count | cloudsql.googleapis.com/database/mysql/innodb\_data\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB log fsync calls | Count | cloudsql.googleapis.com/database/mysql/innodb\_os\_log\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB pages read | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_read |
| cloudsql\_database/default\_metrics | InnoDB pages written | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_written |
| cloudsql\_database/default\_metrics | Queries | Count | cloudsql.googleapis.com/database/mysql/queries |
| cloudsql\_database/default\_metrics | Questions | Count | cloudsql.googleapis.com/database/mysql/questions |
| cloudsql\_database/default\_metrics | Network bytes received by MySQL | Byte | cloudsql.googleapis.com/database/mysql/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Available for failover (Deprecated) | Count | cloudsql.googleapis.com/database/mysql/replication/available\_for\_failover |
| cloudsql\_database/default\_metrics | Last I/O thread error number | Count | cloudsql.googleapis.com/database/mysql/replication/last\_io\_errno |
| cloudsql\_database/default\_metrics | Last SQL thread error number | Count | cloudsql.googleapis.com/database/mysql/replication/last\_sql\_errno |
| cloudsql\_database/default\_metrics | Replica lag | Second | cloudsql.googleapis.com/database/mysql/replication/seconds\_behind\_master |
| cloudsql\_database/default\_metrics | Slave I/O thread running state | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_io\_running\_state |
| cloudsql\_database/default\_metrics | Slave SQL thread running state | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_sql\_running\_state |
| cloudsql\_database/default\_metrics | Network bytes sent by MySQL | Byte | cloudsql.googleapis.com/database/mysql/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Cloud SQL Connections | Count | cloudsql.googleapis.com/database/network/connections |
| cloudsql\_database/default\_metrics | Received bytes | Byte | cloudsql.googleapis.com/database/network/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Sent bytes | Byte | cloudsql.googleapis.com/database/network/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Execution time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/execution\_time |
| cloudsql\_database/default\_metrics | IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/io\_time |
| cloudsql\_database/default\_metrics | Latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/latencies |
| cloudsql\_database/default\_metrics | Aggregated lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/lock\_time |
| cloudsql\_database/default\_metrics | Affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/row\_count |
| cloudsql\_database/default\_metrics | Shared blocks cache access | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per query execution times | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/execution\_time |
| cloudsql\_database/default\_metrics | Per query IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/io\_time |
| cloudsql\_database/default\_metrics | Per query latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/latencies |
| cloudsql\_database/default\_metrics | Per query lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/lock\_time |
| cloudsql\_database/default\_metrics | Per query affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/row\_count |
| cloudsql\_database/default\_metrics | Per query Shared blocks cache access | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per tag execution time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/execution\_time |
| cloudsql\_database/default\_metrics | Per tag IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/io\_time |
| cloudsql\_database/default\_metrics | Per tag latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/latencies |
| cloudsql\_database/default\_metrics | Per tag lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/lock\_time |
| cloudsql\_database/default\_metrics | Per tag affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/row\_count |
| cloudsql\_database/default\_metrics | Per tag shared blocks cache accessed | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | PostgreSQL Connections | Count | cloudsql.googleapis.com/database/postgresql/num\_backends |
| cloudsql\_database/default\_metrics | Lag bytes | Byte | cloudsql.googleapis.com/database/postgresql/replication/replica\_byte\_lag |
| cloudsql\_database/default\_metrics | Number of transactions | Count | cloudsql.googleapis.com/database/postgresql/transaction\_count |
| cloudsql\_database/default\_metrics | Replica lag | Second | cloudsql.googleapis.com/database/replication/replica\_lag |
| cloudsql\_database/default\_metrics | Server up | Count | cloudsql.googleapis.com/database/up |
| cloudsql\_database/default\_metrics | Uptime | Second | cloudsql.googleapis.com/database/uptime |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-storage-monitoring.md


---
title: Google Cloud Storage monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring
scraped: 2026-02-17T21:31:07.932454
---

# Google Cloud Storage monitoring

# Google Cloud Storage monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Storage.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gcs\_bucket/default\_metrics | Rule evaluations | Count | firebasestorage.googleapis.com/rules/evaluation\_count |
| gcs\_bucket/default\_metrics | Request count | Count | storage.googleapis.com/api/request\_count |
| gcs\_bucket/default\_metrics | Authentication count | Count | storage.googleapis.com/authn/authentication\_count |
| gcs\_bucket/default\_metrics | Object-ACL based access count | Count | storage.googleapis.com/authz/acl\_based\_object\_access\_count |
| gcs\_bucket/default\_metrics | ACLs usage | Count | storage.googleapis.com/authz/acl\_operations\_count |
| gcs\_bucket/default\_metrics | Object ACL changes | Count | storage.googleapis.com/authz/object\_specific\_acl\_mutation\_count |
| gcs\_bucket/default\_metrics | Received bytes | Byte | storage.googleapis.com/network/received\_bytes\_count |
| gcs\_bucket/default\_metrics | Sent bytes | Byte | storage.googleapis.com/network/sent\_bytes\_count |
| gcs\_bucket/default\_metrics | Object count | Count | storage.googleapis.com/storage/object\_count |
| gcs\_bucket/default\_metrics | Total byte seconds | Byte | storage.googleapis.com/storage/total\_byte\_seconds |
| gcs\_bucket/default\_metrics | Total bytes | Byte | storage.googleapis.com/storage/total\_bytes |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-cloud-tasks-monitoring.md


---
title: Google Cloud Tasks monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-tasks-monitoring
scraped: 2026-02-17T05:07:33.759196
---

# Google Cloud Tasks monitoring

# Google Cloud Tasks monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Tasks.

| Feature Set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_tasks\_queue/default\_metrics | API requests | Count | cloudtasks.googleapis.com/api/request\_count |
| cloud\_tasks\_queue/default\_metrics | Queue depth | Count | cloudtasks.googleapis.com/queue/depth |
| cloud\_tasks\_queue/default\_metrics | Task attempt count | Count | cloudtasks.googleapis.com/queue/task\_attempt\_count |
| cloud\_tasks\_queue/default\_metrics | Task attempt delays | MilliSecond | cloudtasks.googleapis.com/queue/task\_attempt\_delays |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-dataflow-monitoring.md


---
title: Google Cloud Dataflow monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring
scraped: 2026-02-17T05:06:40.360545
---

# Google Cloud Dataflow monitoring

# Google Cloud Dataflow monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Dataflow.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| dataflow\_job/default\_metrics | Billable shuffle data processed | Byte | dataflow.googleapis.com/job/billable\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Current number of vCPUs in use | Count | dataflow.googleapis.com/job/current\_num\_vcpus |
| dataflow\_job/default\_metrics | Current shuffle slots in use | Count | dataflow.googleapis.com/job/current\_shuffle\_slots |
| dataflow\_job/default\_metrics | Data watermark lag | Second | dataflow.googleapis.com/job/data\_watermark\_age |
| dataflow\_job/default\_metrics | Elapsed time | Second | dataflow.googleapis.com/job/elapsed\_time |
| dataflow\_job/default\_metrics | Element count | Count | dataflow.googleapis.com/job/element\_count |
| dataflow\_job/default\_metrics | Elements Produced | Count | dataflow.googleapis.com/job/elements\_produced\_count |
| dataflow\_job/default\_metrics | Estimated byte count | Byte | dataflow.googleapis.com/job/estimated\_byte\_count |
| dataflow\_job/default\_metrics | Estimated Bytes Produced | Count | dataflow.googleapis.com/job/estimated\_bytes\_produced\_count |
| dataflow\_job/default\_metrics | Failed | Count | dataflow.googleapis.com/job/is\_failed |
| dataflow\_job/default\_metrics | Per-stage data watermark lag | Second | dataflow.googleapis.com/job/per\_stage\_data\_watermark\_age |
| dataflow\_job/default\_metrics | Per-stage system lag | Second | dataflow.googleapis.com/job/per\_stage\_system\_lag |
| dataflow\_job/default\_metrics | PubsubIO.Read requests from Dataflow jobs | Count | dataflow.googleapis.com/job/pubsub/read\_count |
| dataflow\_job/default\_metrics | Pub/Sub Pull Request Latencies | MilliSecond | dataflow.googleapis.com/job/pubsub/read\_latencies |
| dataflow\_job/default\_metrics | Pub/Sub Publish Requests | Count | dataflow.googleapis.com/job/pubsub/write\_count |
| dataflow\_job/default\_metrics | Pub/Sub Publish Request Latencies | MilliSecond | dataflow.googleapis.com/job/pubsub/write\_latencies |
| dataflow\_job/default\_metrics |  |  | dataflow.googleapis.com/job/status |
| dataflow\_job/default\_metrics | System lag | Second | dataflow.googleapis.com/job/system\_lag |
| dataflow\_job/default\_metrics | Total memory usage time | GigaByte | dataflow.googleapis.com/job/total\_memory\_usage\_time |
| dataflow\_job/default\_metrics | Total PD usage time | GigaByte | dataflow.googleapis.com/job/total\_pd\_usage\_time |
| dataflow\_job/default\_metrics | Total shuffle data processed | Byte | dataflow.googleapis.com/job/total\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Total streaming data processed | Byte | dataflow.googleapis.com/job/total\_streaming\_data\_processed |
| dataflow\_job/default\_metrics | Total vCPU time | Second | dataflow.googleapis.com/job/total\_vcpu\_time |
| dataflow\_job/default\_metrics | User Counter | Count | dataflow.googleapis.com/job/user\_counter |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-dataproc-monitoring.md


---
title: Google Cloud Dataproc monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring
scraped: 2026-02-17T21:34:01.868118
---

# Google Cloud Dataproc monitoring

# Google Cloud Dataproc monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Dataproc.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_dataproc\_cluster/default\_metrics | HDFS DataNodes | Count | dataproc.googleapis.com/cluster/hdfs/datanodes |
| cloud\_dataproc\_cluster/default\_metrics | HDFS capacity | GibiByte | dataproc.googleapis.com/cluster/hdfs/storage\_capacity |
| cloud\_dataproc\_cluster/default\_metrics | HDFS storage utilization | Count | dataproc.googleapis.com/cluster/hdfs/storage\_utilization |
| cloud\_dataproc\_cluster/default\_metrics | Unhealthy HDFS blocks by status | Count | dataproc.googleapis.com/cluster/hdfs/unhealthy\_blocks |
| cloud\_dataproc\_cluster/default\_metrics | Job duration | Second | dataproc.googleapis.com/cluster/job/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Job state duration | Second | dataproc.googleapis.com/cluster/job/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed jobs | Count | dataproc.googleapis.com/cluster/job/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running jobs | Count | dataproc.googleapis.com/cluster/job/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted jobs | Count | dataproc.googleapis.com/cluster/job/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Operation duration | Second | dataproc.googleapis.com/cluster/operation/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Operation state duration | Second | dataproc.googleapis.com/cluster/operation/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed operations | Count | dataproc.googleapis.com/cluster/operation/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running operations | Count | dataproc.googleapis.com/cluster/operation/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted operations | Count | dataproc.googleapis.com/cluster/operation/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | YARN allocated memory percentage | Count | dataproc.googleapis.com/cluster/yarn/allocated\_memory\_percentage |
| cloud\_dataproc\_cluster/default\_metrics | YARN active applications | Count | dataproc.googleapis.com/cluster/yarn/apps |
| cloud\_dataproc\_cluster/default\_metrics | YARN containers | Count | dataproc.googleapis.com/cluster/yarn/containers |
| cloud\_dataproc\_cluster/default\_metrics | YARN memory size | GibiByte | dataproc.googleapis.com/cluster/yarn/memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN NodeManagers | Count | dataproc.googleapis.com/cluster/yarn/nodemanagers |
| cloud\_dataproc\_cluster/default\_metrics | YARN pending memory size | GibiByte | dataproc.googleapis.com/cluster/yarn/pending\_memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN virtual cores | Count | dataproc.googleapis.com/cluster/yarn/virtual\_cores |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-filestore-in-datastore-mode-monitoring.md


---
title: Google Cloud Firestore in Datastore mode monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring
scraped: 2026-02-15T21:29:55.455182
---

# Google Cloud Firestore in Datastore mode monitoring

# Google Cloud Firestore in Datastore mode monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Firestore in Datastore mode.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| datastore\_request/default\_metrics | Requests | Count | datastore.googleapis.com/api/request\_count |
| datastore\_request/default\_metrics | Sizes of read entities | Byte | datastore.googleapis.com/entity/read\_sizes |
| datastore\_request/default\_metrics | Sizes of written entities | Byte | datastore.googleapis.com/entity/write\_sizes |
| datastore\_request/default\_metrics | Index writes | Count | datastore.googleapis.com/index/write\_count |
| datastore\_request/default\_metrics | Requests | Count | firestore.googleapis.com/api/request\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-filestore-monitoring.md


---
title: Google Cloud Filestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring
scraped: 2026-02-17T21:32:00.310070
---

# Google Cloud Filestore monitoring

# Google Cloud Filestore monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Filestore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| filestore\_instance/default\_metrics | Average read latency | MilliSecond | file.googleapis.com/nfs/server/average\_read\_latency |
| filestore\_instance/default\_metrics | Average write latency | MilliSecond | file.googleapis.com/nfs/server/average\_write\_latency |
| filestore\_instance/default\_metrics | Free disk bytes | Byte | file.googleapis.com/nfs/server/free\_bytes |
| filestore\_instance/default\_metrics | Free disk space percent | Percent | file.googleapis.com/nfs/server/free\_bytes\_percent |
| filestore\_instance/default\_metrics | Metadata operation count | Count | file.googleapis.com/nfs/server/metadata\_ops\_count |
| filestore\_instance/default\_metrics | Procedure call count | Count | file.googleapis.com/nfs/server/procedure\_call\_count |
| filestore\_instance/default\_metrics | Bytes read | Byte | file.googleapis.com/nfs/server/read\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on read operations | MilliSecond | file.googleapis.com/nfs/server/read\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk read operation count | Count | file.googleapis.com/nfs/server/read\_ops\_count |
| filestore\_instance/default\_metrics | Used disk bytes | Byte | file.googleapis.com/nfs/server/used\_bytes |
| filestore\_instance/default\_metrics | Used disk space percent | Percent | file.googleapis.com/nfs/server/used\_bytes\_percent |
| filestore\_instance/default\_metrics | Bytes written | Byte | file.googleapis.com/nfs/server/write\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on write operations | MilliSecond | file.googleapis.com/nfs/server/write\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk write operation count | Count | file.googleapis.com/nfs/server/write\_ops\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-firebase-monitoring.md


---
title: Google Cloud Firebase monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring
scraped: 2026-02-16T21:29:14.614721
---

# Google Cloud Firebase monitoring

# Google Cloud Firebase monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Firebase.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| firebase\_domain/default\_metrics | Bytes stored limit | Byte | firebasehosting.googleapis.com/storage/limit |
| firebase\_domain/default\_metrics | Bytes stored | Byte | firebasehosting.googleapis.com/storage/total\_bytes |
| firebase\_namespace/default\_metrics | Database Load | Count | firebasedatabase.googleapis.com/io/database\_load |
| firebase\_namespace/default\_metrics | Saved Bytes | Byte | firebasedatabase.googleapis.com/io/persisted\_bytes\_count |
| firebase\_namespace/default\_metrics | Responses sent | Count | firebasedatabase.googleapis.com/io/sent\_responses\_count |
| firebase\_namespace/default\_metrics | I/O utilization | Count | firebasedatabase.googleapis.com/io/utilization |
| firebase\_namespace/default\_metrics | Connections | Count | firebasedatabase.googleapis.com/network/active\_connections |
| firebase\_namespace/default\_metrics | API Hits | Count | firebasedatabase.googleapis.com/network/api\_hits\_count |
| firebase\_namespace/default\_metrics | Broadcast Load | Count | firebasedatabase.googleapis.com/network/broadcast\_load |
| firebase\_namespace/default\_metrics | Disabled for network | Unspecified | firebasedatabase.googleapis.com/network/disabled\_for\_overages |
| firebase\_namespace/default\_metrics | HTTPS Requests Received | Count | firebasedatabase.googleapis.com/network/https\_requests\_count |
| firebase\_namespace/default\_metrics | Bytes sent monthly | Byte | firebasedatabase.googleapis.com/network/monthly\_sent |
| firebase\_namespace/default\_metrics | Bytes sent limit | Byte | firebasedatabase.googleapis.com/network/monthly\_sent\_limit |
| firebase\_namespace/default\_metrics | Total billed bytes | Byte | firebasedatabase.googleapis.com/network/sent\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload and Protocol Bytes sent | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_and\_protocol\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload Bytes Sent | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_bytes\_count |
| firebase\_namespace/default\_metrics | Rule evaluations | Count | firebasedatabase.googleapis.com/rules/evaluation\_count |
| firebase\_namespace/default\_metrics | Bytes stored limit | Byte | firebasedatabase.googleapis.com/storage/limit |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-hybrid-connectivity-monitoring.md


---
title: Google Cloud Hybrid Connectivity monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring
scraped: 2026-02-16T09:35:31.017264
---

# Google Cloud Hybrid Connectivity monitoring

# Google Cloud Hybrid Connectivity monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Hybrid Connectivity.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gce\_router/default\_metrics | Received routes count | Count | router.googleapis.com/best\_received\_routes\_count |
| gce\_router/default\_metrics | BFD control packets receive intervals | MilliSecond | router.googleapis.com/bfd/control/receive\_intervals |
| gce\_router/default\_metrics | Control packets received | Count | router.googleapis.com/bfd/control/received\_packets\_count |
| gce\_router/default\_metrics | Control packets rejected | Count | router.googleapis.com/bfd/control/rejected\_packets\_count |
| gce\_router/default\_metrics | BFD control packets transmit intervals | MilliSecond | router.googleapis.com/bfd/control/transmit\_intervals |
| gce\_router/default\_metrics | Control packets transmitted | Count | router.googleapis.com/bfd/control/transmitted\_packets\_count |
| gce\_router/default\_metrics | BFD session status | Count | router.googleapis.com/bfd/session\_up |
| gce\_router/default\_metrics | BGP received routes count | Count | router.googleapis.com/bgp/received\_routes\_count |
| gce\_router/default\_metrics | BGP sent routes count | Count | router.googleapis.com/bgp/sent\_routes\_count |
| gce\_router/default\_metrics | BGP session status | Count | router.googleapis.com/bgp/session\_up |
| gce\_router/default\_metrics | BGP sessions down count | Count | router.googleapis.com/bgp\_sessions\_down\_count |
| gce\_router/default\_metrics | BGP sessions up count | Count | router.googleapis.com/bgp\_sessions\_up\_count |
| gce\_router/default\_metrics | Router status | Count | router.googleapis.com/router\_up |
| gce\_router/default\_metrics | Sent routes count | Count | router.googleapis.com/sent\_routes\_count |
| interconnect/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/interconnect/capacity |
| interconnect/default\_metrics | Dropped Packets | Unspecified | interconnect.googleapis.com/network/interconnect/dropped\_packets\_count |
| interconnect/default\_metrics | Circuit Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/link/operational |
| interconnect/default\_metrics | Circuit Receive Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/rx\_power |
| interconnect/default\_metrics | Circuit Transmit Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/tx\_power |
| interconnect/default\_metrics | Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/operational |
| interconnect/default\_metrics | Ingress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/receive\_errors\_count |
| interconnect/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/interconnect/received\_bytes\_count |
| interconnect/default\_metrics | Ingress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/received\_unicast\_packets\_count |
| interconnect/default\_metrics | Egress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/send\_errors\_count |
| interconnect/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/interconnect/sent\_bytes\_count |
| interconnect/default\_metrics | Egress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/sent\_unicast\_packets\_count |
| vpn\_gateway/default\_metrics | Number of connections | Count | vpn.googleapis.com/gateway/connections |
| vpn\_gateway/default\_metrics | Incoming packets dropped | Count | vpn.googleapis.com/network/dropped\_received\_packets\_count |
| vpn\_gateway/default\_metrics | Outgoing packets dropped | Count | vpn.googleapis.com/network/dropped\_sent\_packets\_count |
| vpn\_gateway/default\_metrics | Received bytes | Byte | vpn.googleapis.com/network/received\_bytes\_count |
| vpn\_gateway/default\_metrics | Received packets | Unspecified | vpn.googleapis.com/network/received\_packets\_count |
| vpn\_gateway/default\_metrics | Sent bytes | Byte | vpn.googleapis.com/network/sent\_bytes\_count |
| vpn\_gateway/default\_metrics | Sent packets | Unspecified | vpn.googleapis.com/network/sent\_packets\_count |
| vpn\_gateway/default\_metrics | Tunnel established | Count | vpn.googleapis.com/tunnel\_established |
| interconnect\_attachment/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/attachment/capacity |
| interconnect\_attachment/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/attachment/received\_bytes\_count |
| interconnect\_attachment/default\_metrics | Ingress Packets | Unspecified | interconnect.googleapis.com/network/attachment/received\_packets\_count |
| interconnect\_attachment/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/attachment/sent\_bytes\_count |
| interconnect\_attachment/default\_metrics | Egress Packets | Unspecified | interconnect.googleapis.com/network/attachment/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-memorystore-monitoring.md


---
title: Google Cloud Memorystore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring
scraped: 2026-02-16T09:27:36.220790
---

# Google Cloud Memorystore monitoring

# Google Cloud Memorystore monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Memorystore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| redis\_instance/default\_metrics | Blocked Clients | Count | redis.googleapis.com/clients/blocked |
| redis\_instance/default\_metrics | Connected Clients | Count | redis.googleapis.com/clients/connected |
| redis\_instance/default\_metrics | Calls | Count | redis.googleapis.com/commands/calls |
| redis\_instance/default\_metrics | Total Time of Calls | MicroSecond | redis.googleapis.com/commands/total\_time |
| redis\_instance/default\_metrics | Time per Call | Count | redis.googleapis.com/commands/usec\_per\_call |
| redis\_instance/default\_metrics | Average TTL | MilliSecond | redis.googleapis.com/keyspace/avg\_ttl |
| redis\_instance/default\_metrics | Keys | Count | redis.googleapis.com/keyspace/keys |
| redis\_instance/default\_metrics | Expirable Keys | Count | redis.googleapis.com/keyspace/keys\_with\_expiration |
| redis\_instance/default\_metrics | Persisting RDB | Count | redis.googleapis.com/persistence/rdb/bgsave\_in\_progress |
| redis\_instance/default\_metrics | Bytes lagging | Byte | redis.googleapis.com/replication/master/slaves/lag |
| redis\_instance/default\_metrics | Replication byte offset (Replica) | Byte | redis.googleapis.com/replication/master/slaves/offset |
| redis\_instance/default\_metrics | Replication byte offset (Master) | Byte | redis.googleapis.com/replication/master\_repl\_offset |
| redis\_instance/default\_metrics | Bytes pending replication | Byte | redis.googleapis.com/replication/offset\_diff |
| redis\_instance/default\_metrics | Node Role | Count | redis.googleapis.com/replication/role |
| redis\_instance/default\_metrics | Uptime | Second | redis.googleapis.com/server/uptime |
| redis\_instance/default\_metrics | Cache Hit ratio | Count | redis.googleapis.com/stats/cache\_hit\_ratio |
| redis\_instance/default\_metrics | Total Connections Received | Count | redis.googleapis.com/stats/connections/total |
| redis\_instance/default\_metrics | CPU seconds | Second | redis.googleapis.com/stats/cpu\_utilization |
| redis\_instance/default\_metrics | Evicted Keys | Count | redis.googleapis.com/stats/evicted\_keys |
| redis\_instance/default\_metrics | Expired Keys | Count | redis.googleapis.com/stats/expired\_keys |
| redis\_instance/default\_metrics | Hits | Count | redis.googleapis.com/stats/keyspace\_hits |
| redis\_instance/default\_metrics | Misses | Count | redis.googleapis.com/stats/keyspace\_misses |
| redis\_instance/default\_metrics | Maximum Memory | Byte | redis.googleapis.com/stats/memory/maxmemory |
| redis\_instance/default\_metrics | Time in system memory overload | MicroSecond | redis.googleapis.com/stats/memory/system\_memory\_overload\_duration |
| redis\_instance/default\_metrics | System Memory Usage Ratio | Count | redis.googleapis.com/stats/memory/system\_memory\_usage\_ratio |
| redis\_instance/default\_metrics | Used Memory | Byte | redis.googleapis.com/stats/memory/usage |
| redis\_instance/default\_metrics | Memory Usage Ratio | Count | redis.googleapis.com/stats/memory/usage\_ratio |
| redis\_instance/default\_metrics | Total traffic to Redis | Byte | redis.googleapis.com/stats/network\_traffic |
| redis\_instance/default\_metrics | Pubsub Channels | Count | redis.googleapis.com/stats/pubsub/channels |
| redis\_instance/default\_metrics | Pubsub Patterns | Count | redis.googleapis.com/stats/pubsub/patterns |
| redis\_instance/default\_metrics | Rejected Connections | Count | redis.googleapis.com/stats/reject\_connections\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-netapp-monitoring.md


---
title: NetApp on Google Cloud monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring
scraped: 2026-02-17T21:29:05.886160
---

# NetApp on Google Cloud monitoring

# NetApp on Google Cloud monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for NetApp on Google Cloud.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| netapp\_cloud\_volume/default\_metrics | Volume inode allocation | Unspecified | netapp.com/cloudvolume/inode\_allocation |
| netapp\_cloud\_volume/default\_metrics | Volume inode usage | Unspecified | netapp.com/cloudvolume/inode\_usage |
| netapp\_cloud\_volume/default\_metrics | Operations count | Count | netapp.com/cloudvolume/operation\_count |
| netapp\_cloud\_volume/default\_metrics | Bytes read | Byte | netapp.com/cloudvolume/read\_bytes\_count |
| netapp\_cloud\_volume/default\_metrics | Volume IO operation latency | MilliSecond | netapp.com/cloudvolume/request\_latencies |
| netapp\_cloud\_volume/default\_metrics | Volume space allocation | Byte | netapp.com/cloudvolume/volume\_size |
| netapp\_cloud\_volume/default\_metrics | Volume space usage | Byte | netapp.com/cloudvolume/volume\_usage |
| netapp\_cloud\_volume/default\_metrics | Bytes written | Byte | netapp.com/cloudvolume/write\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Logical Bytes Backed Up | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/logical\_bytes\_backed\_up |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Operation Count | Count | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/operation\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Read Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/read\_bytes\_count |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Request Latencies | MilliSecond | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/request\_latencies |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Size | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_size |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Volume Usage | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/volume\_usage |
| cloudvolumesgcp\_api\_netapp\_com\_NetAppCloudVolumeSO/default\_metrics | NetApp CVS-SO Write Bytes Count | Byte | cloudvolumesgcp-api.netapp.com/cloudvolume\_so/write\_bytes\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-network-security-monitoring.md


---
title: Google Cloud Network Security monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-security-monitoring
scraped: 2026-02-17T05:05:53.846435
---

# Google Cloud Network Security monitoring

# Google Cloud Network Security monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Network Security.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| network\_security\_policy/default\_metrics | Previewed request count | Count | networksecurity.googleapis.com/https/previewed\_request\_count |
| network\_security\_policy/default\_metrics | Request count | Count | networksecurity.googleapis.com/https/request\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-network-topology-monitoring.md


---
title: Google Cloud Network Topology monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-topology-monitoring
scraped: 2026-02-17T04:59:18.957886
---

# Google Cloud Network Topology monitoring

# Google Cloud Network Topology monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Network Topology.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gce\_zone\_network\_health/default\_metrics | Number of probes | Count | networking.googleapis.com/cloud\_netslo/active\_probing/probe\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-operations-cloud-monitoring-and-logging.md


---
title: Operations: Cloud Monitoring & Logging
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging
scraped: 2026-02-17T05:04:37.557018
---

# Operations: Cloud Monitoring & Logging

# Operations: Cloud Monitoring & Logging

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Operations suite.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| uptime\_url/default\_metrics | Check passed | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| uptime\_url/default\_metrics | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| uptime\_url/default\_metrics | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| uptime\_url/default\_metrics | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gce\_instance/uptime\_check | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gce\_instance/uptime\_check | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gce\_instance/uptime\_check | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gae\_app\_uptime\_check/default\_metrics | Check passed | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| gae\_app\_uptime\_check/default\_metrics | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gae\_app\_uptime\_check/default\_metrics | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gae\_app\_uptime\_check/default\_metrics | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| logging\_sink/default\_metrics | Exported log bytes | Byte | logging.googleapis.com/exports/byte\_count |
| logging\_sink/default\_metrics | Exported log entries failures | Count | logging.googleapis.com/exports/error\_count |
| logging\_sink/default\_metrics | Exported log entries | Count | logging.googleapis.com/exports/log\_entry\_count |
| cloudtrace\_googleapis\_com\_CloudtraceProject/default\_metrics | Spans Exported to BigQuery | Count | cloudtrace.googleapis.com/bigquery\_export/exported\_span\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-pub-sub-lite-monitoring.md


---
title: Google Cloud Pub/Sub Lite monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring
scraped: 2026-02-17T05:04:52.359513
---

# Google Cloud Pub/Sub Lite monitoring

# Google Cloud Pub/Sub Lite monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Pub/Sub Lite.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| pubsublite\_topic\_partition/default\_metrics | Oldest retained message age | Second | pubsublite.googleapis.com/topic/oldest\_retained\_message\_age |
| pubsublite\_topic\_partition/default\_metrics | Publish message count | Count | pubsublite.googleapis.com/topic/publish\_message\_count |
| pubsublite\_topic\_partition/default\_metrics | Publish quota byte limit | Byte | pubsublite.googleapis.com/topic/publish\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Publish quota bytes | Byte | pubsublite.googleapis.com/topic/publish\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Publish quota utilization ratio | Percent | pubsublite.googleapis.com/topic/publish\_quota\_utilization |
| pubsublite\_topic\_partition/default\_metrics | Publish raw bytes | Byte | pubsublite.googleapis.com/topic/publish\_raw\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Publish request count | Count | pubsublite.googleapis.com/topic/publish\_request\_count |
| pubsublite\_topic\_partition/default\_metrics | Topic sent quota bytes | Byte | pubsublite.googleapis.com/topic/sent\_quota\_bytes |
| pubsublite\_topic\_partition/default\_metrics | Storage quota byte limit | Byte | pubsublite.googleapis.com/topic/storage\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Subscribe quota byte limit | Byte | pubsublite.googleapis.com/topic/subscribe\_quota\_byte\_limit |
| pubsublite\_topic\_partition/default\_metrics | Subscribe quota utilization ratio | Percent | pubsublite.googleapis.com/topic/subscribe\_quota\_utilization |
| pubsublite\_subscription\_partition/default\_metrics | Backlog message count | Count | pubsublite.googleapis.com/subscription/backlog\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Backlog quota bytes | Byte | pubsublite.googleapis.com/subscription/backlog\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Oldest unacked message age | Second | pubsublite.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent message count | Count | pubsublite.googleapis.com/subscription/sent\_message\_count |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent quota bytes | Byte | pubsublite.googleapis.com/subscription/sent\_quota\_bytes |
| pubsublite\_subscription\_partition/default\_metrics | Subscription sent raw bytes | Byte | pubsublite.googleapis.com/subscription/sent\_raw\_bytes |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-pub-sub-monitoring.md


---
title: Google Cloud Pub/Sub monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring
scraped: 2026-02-17T21:28:03.096139
---

# Google Cloud Pub/Sub monitoring

# Google Cloud Pub/Sub monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Pub/Sub.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes by region | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes\_by\_region |
| pubsub\_snapshot/default\_metrics | Snapshot updates | Count | pubsub.googleapis.com/snapshot/config\_updates\_count |
| pubsub\_snapshot/default\_metrics | Snapshot messages | Count | pubsub.googleapis.com/snapshot/num\_messages |
| pubsub\_snapshot/default\_metrics | Snapshot messages by region | Count | pubsub.googleapis.com/snapshot/num\_messages\_by\_region |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age by region | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Ack message count | Count | pubsub.googleapis.com/subscription/ack\_message\_count |
| pubsub\_subscription/default\_metrics | Backlog size | Byte | pubsub.googleapis.com/subscription/backlog\_bytes |
| pubsub\_subscription/default\_metrics | Subscription byte cost | Byte | pubsub.googleapis.com/subscription/byte\_cost |
| pubsub\_subscription/default\_metrics | Subscription updates | Count | pubsub.googleapis.com/subscription/config\_updates\_count |
| pubsub\_subscription/default\_metrics | Dead letter message count | Count | pubsub.googleapis.com/subscription/dead\_letter\_message\_count |
| pubsub\_subscription/default\_metrics | Mod ack deadline message count | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Outstanding push messages | Count | pubsub.googleapis.com/subscription/num\_outstanding\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/subscription/num\_unacked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages | Count | pubsub.googleapis.com/subscription/num\_undelivered\_messages |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Oldest unacked message age | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Acknowledge message operations | Count | pubsub.googleapis.com/subscription/pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Acknowledge requests | Count | pubsub.googleapis.com/subscription/pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Pull operations | Count | pubsub.googleapis.com/subscription/pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Pull requests | Count | pubsub.googleapis.com/subscription/pull\_request\_count |
| pubsub\_subscription/default\_metrics | Push requests | Count | pubsub.googleapis.com/subscription/push\_request\_count |
| pubsub\_subscription/default\_metrics | Push latency | MicroSecond | pubsub.googleapis.com/subscription/push\_request\_latencies |
| pubsub\_subscription/default\_metrics | Retained acked bytes | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes |
| pubsub\_subscription/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes\_by\_region |
| pubsub\_subscription/default\_metrics | Seek requests | Count | pubsub.googleapis.com/subscription/seek\_request\_count |
| pubsub\_subscription/default\_metrics | Sent message count | Count | pubsub.googleapis.com/subscription/sent\_message\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull responses | Count | pubsub.googleapis.com/subscription/streaming\_pull\_response\_count |
| pubsub\_subscription/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/subscription/unacked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Topic byte cost | Byte | pubsub.googleapis.com/topic/byte\_cost |
| pubsub\_topic/default\_metrics | Topic updates | Count | pubsub.googleapis.com/topic/config\_updates\_count |
| pubsub\_topic/default\_metrics | Publish message size | Byte | pubsub.googleapis.com/topic/message\_sizes |
| pubsub\_topic/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/topic/num\_retained\_acked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/topic/num\_unacked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/topic/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/topic/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/topic/retained\_acked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Publish message operations | Count | pubsub.googleapis.com/topic/send\_message\_operation\_count |
| pubsub\_topic/default\_metrics | Publish requests | Count | pubsub.googleapis.com/topic/send\_request\_count |
| pubsub\_topic/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/topic/unacked\_bytes\_by\_region |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-recaptcha-enterprise-monitoring.md


---
title: Google Cloud reCAPTCHA Enterprise monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-recaptcha-enterprise-monitoring
scraped: 2026-02-17T21:26:09.135285
---

# Google Cloud reCAPTCHA Enterprise monitoring

# Google Cloud reCAPTCHA Enterprise monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud reCAPTCHA Enterprise.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| recaptchaenterprise\_googleapis\_com\_Key/default\_metrics | Score counts | Count | recaptchaenterprise.googleapis.com/score\_counts |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-router-monitoring.md


---
title: Google Cloud Router monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring
scraped: 2026-02-17T05:12:27.013198
---

# Google Cloud Router monitoring

# Google Cloud Router monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Router.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| nat\_gateway/default\_metrics | Allocated ports | Unspecified | router.googleapis.com/nat/allocated\_ports |
| nat\_gateway/default\_metrics | Closed connections count | Unspecified | router.googleapis.com/nat/closed\_connections\_count |
| nat\_gateway/default\_metrics | Received packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_received\_packets\_count |
| nat\_gateway/default\_metrics | Sent packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_sent\_packets\_count |
| nat\_gateway/default\_metrics | NAT allocation failed | Unspecified | router.googleapis.com/nat/nat\_allocation\_failed |
| nat\_gateway/default\_metrics | New connections count | Unspecified | router.googleapis.com/nat/new\_connections\_count |
| nat\_gateway/default\_metrics | Open connections | Unspecified | router.googleapis.com/nat/open\_connections |
| nat\_gateway/default\_metrics | Port usage | Unspecified | router.googleapis.com/nat/port\_usage |
| nat\_gateway/default\_metrics | Received bytes count | Byte | router.googleapis.com/nat/received\_bytes\_count |
| nat\_gateway/default\_metrics | Received packets count | Unspecified | router.googleapis.com/nat/received\_packets\_count |
| nat\_gateway/default\_metrics | Sent bytes count | Byte | router.googleapis.com/nat/sent\_bytes\_count |
| nat\_gateway/default\_metrics | Sent packets count | Unspecified | router.googleapis.com/nat/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-spanner-monitoring.md


---
title: Google Cloud Spanner monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring
scraped: 2026-02-16T21:31:50.549496
---

# Google Cloud Spanner monitoring

# Google Cloud Spanner monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Spanner.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| spanner\_instance/default\_metrics | API requests | Count | spanner.googleapis.com/api/api\_request\_count |
| spanner\_instance/default\_metrics | Bytes received by Cloud Spanner. | Byte | spanner.googleapis.com/api/received\_bytes\_count |
| spanner\_instance/default\_metrics | API request rate | PerSecond | spanner.googleapis.com/api/request\_count |
| spanner\_instance/default\_metrics | Request latencies | Second | spanner.googleapis.com/api/request\_latencies |
| spanner\_instance/default\_metrics | Bytes sent by Cloud Spanner. | Byte | spanner.googleapis.com/api/sent\_bytes\_count |
| spanner\_instance/default\_metrics | Backup storage used. | Byte | spanner.googleapis.com/instance/backup/used\_bytes |
| spanner\_instance/default\_metrics | Smoothed CPU utilization | Percent | spanner.googleapis.com/instance/cpu/smoothed\_utilization |
| spanner\_instance/default\_metrics | CPU utilization | Percent | spanner.googleapis.com/instance/cpu/utilization |
| spanner\_instance/default\_metrics | CPU utilization by priority | Percent | spanner.googleapis.com/instance/cpu/utilization\_by\_priority |
| spanner\_instance/default\_metrics | Nodes | Count | spanner.googleapis.com/instance/node\_count |
| spanner\_instance/default\_metrics | Sessions | Count | spanner.googleapis.com/instance/session\_count |
| spanner\_instance/default\_metrics | Storage limit | Byte | spanner.googleapis.com/instance/storage/limit\_bytes |
| spanner\_instance/default\_metrics | Storage used. | Byte | spanner.googleapis.com/instance/storage/used\_bytes |
| spanner\_instance/default\_metrics | Storage utilization | Percent | spanner.googleapis.com/instance/storage/utilization |
| spanner\_instance/default\_metrics | Count of queries | Count | spanner.googleapis.com/query\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-storage-transfer-service-monitoring.md


---
title: Google Cloud Storage Transfer Service monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-storage-transfer-service-monitoring
scraped: 2026-02-17T05:07:20.112015
---

# Google Cloud Storage Transfer Service monitoring

# Google Cloud Storage Transfer Service monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Storage Transfer Service.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| transfer\_service\_agent/default\_metrics | Agent connected status | Unspecified | storagetransfer.googleapis.com/agent/connected |
| transfer\_service\_agent/default\_metrics | Agent transfer delta | Byte | storagetransfer.googleapis.com/agent/transferred\_bytes\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-virtual-private-cloud-monitoring.md


---
title: Google Cloud Virtual Private Cloud (VPC) monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring
scraped: 2026-02-16T09:35:22.855723
---

# Google Cloud Virtual Private Cloud (VPC) monitoring

# Google Cloud Virtual Private Cloud (VPC) monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud VPC.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| vpc\_access\_connector/default\_metrics | CPU Utilizations | Percent | vpcaccess.googleapis.com/connector/cpu/utilizations |
| vpc\_access\_connector/default\_metrics | Active instances | Count | vpcaccess.googleapis.com/connector/instances |
| vpc\_access\_connector/default\_metrics | Bytes received delta | Byte | vpcaccess.googleapis.com/connector/received\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Packets received delta | Unspecified | vpcaccess.googleapis.com/connector/received\_packets\_count |
| vpc\_access\_connector/default\_metrics | Bytes sent delta | Byte | vpcaccess.googleapis.com/connector/sent\_bytes\_count |
| vpc\_access\_connector/default\_metrics | Packets sent delta | Unspecified | vpcaccess.googleapis.com/connector/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: gcp-supported-service-metrics-new.md


---
title: Google Cloud supported services
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new
scraped: 2026-02-17T21:20:03.940818
---

# Google Cloud supported services

# Google Cloud supported services

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Sep 23, 2024

Dynatrace version 1.230+

This section refers to Google Cloud service metrics that are available with Google Cloud version 1.0 integration.

* For Google Cloud service metrics that are available with earlier versions of the Google Cloud integration, see [Google Cloud supported service metrics (legacy)](/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Supported GCP service metrics, metrics configuration, DDU consumption, and preset dashboard availability").

## Prerequisites

[Deploy Dynatrace integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Supported services for metrics

After deploying the Dynatrace integration, you can get insights into Google Cloud services metrics collected from the Google Operations API to ensure health of your cloud infrastructure.

Below, see the list of Google Cloud supported services.

Services

Supported entities[1](#fn-1-1-def)

Supported logs

Logs entities

[Google Cloud AI Platform monitoring (deprecated)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring "Monitor Google Cloud AI Platform and view available metrics.")

cloudml\_job, cloudml\_model\_version

yes

cloudml\_job, cloudml\_model\_version

[Google Cloud AlloyDB monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-alloydb-monitoring "Monitor Google Cloud AlloyDB and view available metrics.")

alloydb\_database, alloydb\_instance

yes

alloydb\_database, alloydb\_instance

[Google Cloud APIs monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")

no

[Google Cloud Apigee monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring "Monitor Google Cloud Apigee and view available metrics.")

apigee\_environment, apigee\_proxy, apigee\_target

no

[Google App Engine with Operations suite metrics monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")

gae\_app

yes

gae\_app

[Google Cloud Assistant Smart Home monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-assistant-smart-home-monitoring "Monitor Google Cloud Assistant Smart Home and view available metrics.")

no

[Google BigQuery monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")

bigquery\_bigengine\_model

no

[Google Cloud Bigtable monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring "Monitor Google Cloud Bigtable and view available metrics.")

bigtable\_cluster, bigtable\_table

no

[Google Cloud DNS monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-dns-monitoring "Monitor Google Cloud DNS and view available metrics.")

no

[Google Cloud Functions monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")

cloud\_function

yes

cloud\_function

[Google Cloud IoT Core monitoring (deprecated)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-iot-core-monitoring "Monitor Google Cloud IoT Core and view available metrics.")

no

[Google Cloud Router monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring "Monitor Google Cloud Router and view available metrics.")

nat\_gateway

yes

nat\_gateway

[Google Cloud Run monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")

cloud\_function, cloud\_run\_revision

yes

cloud\_run\_revision

[Google Cloud Storage monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")

gcs\_bucket

yes

gcs\_bucket

[Google Cloud Tasks monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-tasks-monitoring "Monitor Google Cloud Tasks and view available metrics.")

cloud\_tasks\_queue

yes

cloud\_tasks\_queue

[Google Cloud Composer monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring "Monitor Google Cloud Composer and view available metrics.")

cloud\_composer\_environment

yes

cloud\_composer\_environment

[Google Compute Engine with Operations suite metrics monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")

autoscaler, gce\_instance, instance\_group, tpu\_worker

yes

autoscaler, gce\_autoscaler, gce\_instance\_group, gce\_instance, tpu\_worker

[Google Cloud Data Loss Prevention monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring "Monitor Google Cloud Data Loss Prevention (now part of Sensitive Data Protection) and view available metrics.")

no

[Google Cloud Storage Transfer Service monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-storage-transfer-service-monitoring "Monitor Google Cloud Storage Transfer Service and view available metrics.")

storage\_transfer\_job, transfer\_service\_agent

yes

storage\_transfer\_job

[Google Cloud Dataflow monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring "Monitor Google Cloud Dataflow and view available metrics.")

no

[Google Cloud Dataproc monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring "Monitor Google Cloud Dataproc and view available metrics.")

cloud\_dataproc\_cluster

yes

cloud\_dataproc\_cluster

[Google Cloud Firestore in Datastore mode monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")

no

[Google Cloud Filestore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")

filestore\_instance

no

[Google Cloud Firebase monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring "Monitor Google Cloud Firebase and view available metrics.")

no

[Google Cloud Firestore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring "Monitor Google Cloud Firestore and view available metrics.")

firestore\_database

no

[Google Cloud Hybrid Connectivity monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring "Monitor Google Cloud Hybrid Connectivity and view available metrics.")

interconnect, interconnect\_attachment, gce\_router, vpn\_gateway

yes

gce\_router, vpn\_gateway

[Google Kubernetes Engine monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")

k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod

yes

k8s\_cluster, k8s\_container, k8s\_node, k8s\_pod

[Google Cloud Load Balancing monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")

https\_lb, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule

yes

http\_load\_balancer, internal\_http\_lb\_rule, internal\_network\_lb\_rule, network\_lb\_rule, tcp\_ssl\_proxy\_rule

[Google Managed Microsoft AD monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-managed-microsoft-ad-monitoring "Monitor Google Managed Microsoft AD and view available metrics.")

microsoft\_ad\_domain

no

[Google Cloud Memorystore monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-memorystore-monitoring "Monitor Google Cloud Memorystore and view available metrics.")

redis\_instance

yes

redis\_instance

[NetApp on Google Cloud monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-netapp-monitoring "Monitor NetApp on Google Cloud and view available metrics.")

netapp\_volumes\_replication, netapp\_volumes\_storage\_pool, netapp\_volumes\_volume

no

[Google Cloud Network Security monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-security-monitoring "Monitor Google Cloud Network Security and view available metrics.")

network\_security\_policy

yes

network\_security\_policy

[Operations: Cloud Monitoring & Logging](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging "Monitor Google Cloud's operations suite and view available metrics.")

uptime\_url

yes

uptime\_url

[Google Cloud Pub/Sub monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")

pubsub\_snapshot, pubsub\_subscription, pubsub\_topic

yes

pubsub\_snapshot, pubsub\_subscription, pubsub\_topic

[Google Cloud Pub/Sub Lite monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")

subscription\_partition, topic\_partition

no

[Google Cloud Spanner monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring "Monitor Google Cloud Spanner and view available metrics.")

spanner\_instance

yes

spanner\_instance

[Google Cloud SQL monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

cloudsql\_database

yes

cloudsql\_database

[Google Cloud Virtual Private Cloud (VPC) monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-virtual-private-cloud-monitoring "Monitor Google Cloud Virtual Private Cloud (VPC) and view available metrics.")

vpc\_access\_connector

yes

vpc\_access\_connector

[Google Cloud Network Topology monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-network-topology-monitoring "Monitor Google Cloud Network Topology and view available metrics.")

no

[Google Vertex AI monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-vertex-ai "Monitor Google Cloud Vertex AI and view available metrics.")

vertex\_ai\_deployment\_resource\_pool,  
vertex\_ai\_endpoint,  
vertex\_ai\_feature\_online\_store,  
vertex\_ai\_feature\_store,  
vertex\_ai\_pipeline\_job,  
vertex\_ai\_index, vertex\_ai\_index\_endpoint,  
vertex\_ai\_publisher\_model,  
vision\_ai\_instance,  
vision\_ai\_stream

yes

vertex\_ai\_deployment\_resource\_pool,  
vertex\_ai\_endpoint,  
vertex\_ai\_feature\_store,  
vertex\_ai\_pipeline\_job,  
vertex\_ai\_index\_endpoint

1

Services might have one entity, several entities, or none. For each entity, you can see metrics, properties, logs, errors, and many more in Dynatrace [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.").

## Check available metrics

To check available metrics for a service, you need to

1. Find the extension in the [Hubï»¿](https://www.dynatrace.com/hub/?query=google&filter=all) and select it to open the overview page. See example: [Google Cloud Functionsï»¿](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).
2. Scroll down to the bottom of the overview page of the extension to find the **Feature sets** section.
3. In the table, select the **default\_metrics** dropdown.
4. Now, you can check all available metrics for the chosen service.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: app-engine-monitoring.md


---
title: Google App Engine with Operations suite metrics monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring
scraped: 2026-02-17T04:59:27.198830
---

# Google App Engine with Operations suite metrics monitoring

# Google App Engine with Operations suite metrics monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google App Engine.

| Feature Set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gae\_app/default\_metrics | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| gae\_app/default\_metrics | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| gae\_app/default\_metrics | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gae\_app/default\_metrics | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| gae\_app/default\_metrics | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gae\_app/default\_metrics | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| gae\_app/default\_metrics | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| gae\_app/default\_metrics | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gae\_app/default\_metrics | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| gae\_app/default\_metrics | Autoscaling Metrics Utilization Capacity | Count | appengine.googleapis.com/flex/autoscaler/capacity |
| gae\_app/default\_metrics | Autoscaling Metrics Current Utilization | Count | appengine.googleapis.com/flex/autoscaler/current\_utilization |
| gae\_app/default\_metrics | Connections | Count | appengine.googleapis.com/flex/connections/current |
| gae\_app/default\_metrics | Reserved cores | Count | appengine.googleapis.com/flex/cpu/reserved\_cores |
| gae\_app/default\_metrics | CPU utilization | Percent | appengine.googleapis.com/flex/cpu/utilization |
| gae\_app/default\_metrics | Disk bytes read | Byte | appengine.googleapis.com/flex/disk/read\_bytes\_count |
| gae\_app/default\_metrics | Disk bytes written | Byte | appengine.googleapis.com/flex/disk/write\_bytes\_count |
| gae\_app/default\_metrics | Network bytes received. | Byte | appengine.googleapis.com/flex/network/received\_bytes\_count |
| gae\_app/default\_metrics | Network bytes sent. | Byte | appengine.googleapis.com/flex/network/sent\_bytes\_count |
| gae\_app/default\_metrics | Interception count | Count | appengine.googleapis.com/http/server/dos\_intercept\_count |
| gae\_app/default\_metrics | Quota denial count | Count | appengine.googleapis.com/http/server/quota\_denial\_count |
| gae\_app/default\_metrics | Response count | Count | appengine.googleapis.com/http/server/response\_count |
| gae\_app/default\_metrics | Response latency | MilliSecond | appengine.googleapis.com/http/server/response\_latencies |
| gae\_app/default\_metrics | Response count by style | Count | appengine.googleapis.com/http/server/response\_style\_count |
| gae\_app/default\_metrics | Memcache utilization | Count | appengine.googleapis.com/memcache/centi\_mcu\_count |
| gae\_app/default\_metrics | Hit ratio | Count | appengine.googleapis.com/memcache/hit\_ratio |
| gae\_app/default\_metrics | Memcache operations | Count | appengine.googleapis.com/memcache/operation\_count |
| gae\_app/default\_metrics | Memcache received bytes | Byte | appengine.googleapis.com/memcache/received\_bytes\_count |
| gae\_app/default\_metrics | Memcache sent bytes | Byte | appengine.googleapis.com/memcache/sent\_bytes\_count |
| gae\_app/default\_metrics | Used Cache Size | Byte | appengine.googleapis.com/memcache/used\_cache\_size |
| gae\_app/default\_metrics | Estimated instance count | Count | appengine.googleapis.com/system/billed\_instance\_estimate\_count |
| gae\_app/default\_metrics | CPU megacycles | Count | appengine.googleapis.com/system/cpu/usage |
| gae\_app/default\_metrics | Instance count | Count | appengine.googleapis.com/system/instance\_count |
| gae\_app/default\_metrics | Memory usage | Byte | appengine.googleapis.com/system/memory/usage |
| gae\_app/default\_metrics | Received bytes | Byte | appengine.googleapis.com/system/network/received\_bytes\_count |
| gae\_app/default\_metrics | Sent bytes | Byte | appengine.googleapis.com/system/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Connections | Count | appengine.googleapis.com/flex/instance/connections/current |
| gae\_instance/default\_metrics | CPU Utilization | Percent | appengine.googleapis.com/flex/instance/cpu/utilization |
| gae\_instance/default\_metrics | Network bytes received | Byte | appengine.googleapis.com/flex/instance/network/received\_bytes\_count |
| gae\_instance/default\_metrics | Network bytes sent | Byte | appengine.googleapis.com/flex/instance/network/sent\_bytes\_count |
| gae\_instance/default\_metrics | Websocket average duration | Second | appengine.googleapis.com/flex/instance/ws/avg\_duration |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: google-app-engine.md


---
title: Monitor Google App Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine
scraped: 2026-02-06T16:24:08.961664
---

# Monitor Google App Engine

# Monitor Google App Engine

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 23, 2020

The Google App Engine standard environment type supports applications that run on Java, .NET, Node.js, Golang, and more. For custom Docker images, Google App Engine provides flexible environment support.

## Prerequisites

* Create a [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Integrate OneAgent into the application image

To integrate OneAgent into a container deployment with a Dockerfile in Google App Engine flexible environment and activate instrumentation of your application, add the commands below to your current Dockerfile, making sure to enter your own values for the `DT_API_URL`, `DT_API_TOKEN`, and `DT_ONEAGENT_OPTIONS` arguments.

* `<environmentID>` should be replaced with your Dynatrace environment ID. If youâre using Dynatrace Managed, you need to provide your Dynatrace Server URL (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).
* `<token>`should be replaced with the PaaS token mentioned in the prerequisites.
* Technology support is enabled via `include` parameters. Valid options for `flavor=default` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` and `go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package. For Alpine Linux based environments, Dynatrace OneAgent supports the flavor `musl`. Valid options for `flavor=musl` are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.

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

The `wget` and `unzip` commands above might fail if they aren't provided by the base image.

## Deploy the application image

After integrating the OneAgent into the application Docker file, deploy the application. In order to do this, switch to the directory of the application that contains the `Dockerfile` and the `app.yaml` file, and run the following command in the `gcloud` CLI.

```
gcloud app deploy
```

Google App Engine will take care of building the Docker image based on the Docker file provided, and thereby of downloading and installing the OneAgent code-modules into the application image.

## Update OneAgent

Every time you want to update your version of Dynatrace OneAgent, you must redeploy your application. Google App Engine thus rebuilds the application image with the latest OneAgent components. Any newly started containers from this application image is then monitored with the latest version of OneAgent.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: compute-engine-monitoring.md


---
title: Google Compute Engine with Operations suite metrics monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring
scraped: 2026-02-17T05:00:44.606903
---

# Google Compute Engine with Operations suite metrics monitoring

# Google Compute Engine with Operations suite metrics monitoring

* Latest Dynatrace
* How-to guide
* 18-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Compute Engine.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gce\_instance/default\_metrics | Dropped bytes | Byte | compute.googleapis.com/firewall/dropped\_bytes\_count |
| gce\_instance/default\_metrics | Dropped packets | Count | compute.googleapis.com/firewall/dropped\_packets\_count |
| gce\_instance/default\_metrics | Runnable task count. | Count | compute.googleapis.com/guest/cpu/runnable\_task\_count |
| gce\_instance/default\_metrics | CPU usage | Second | compute.googleapis.com/guest/cpu/usage\_time |
| gce\_instance/default\_metrics | Disk usage in Bytes | Byte | compute.googleapis.com/guest/disk/bytes\_used |
| gce\_instance/default\_metrics | IO Time | MilliSecond | compute.googleapis.com/guest/disk/io\_time |
| gce\_instance/default\_metrics | Merged disk operations | Count | compute.googleapis.com/guest/disk/merged\_operation\_count |
| gce\_instance/default\_metrics | Disk bytes transferred | Byte | compute.googleapis.com/guest/disk/operation\_bytes\_count |
| gce\_instance/default\_metrics | Disk operations | Count | compute.googleapis.com/guest/disk/operation\_count |
| gce\_instance/default\_metrics | Disk operation time | MilliSecond | compute.googleapis.com/guest/disk/operation\_time |
| gce\_instance/default\_metrics | Queue Length | Count | compute.googleapis.com/guest/disk/queue\_length |
| gce\_instance/default\_metrics | IO Time | MilliSecond | compute.googleapis.com/guest/disk/weighted\_io\_time |
| gce\_instance/default\_metrics | Anonymous memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/anonymous\_used |
| gce\_instance/default\_metrics | Memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/bytes\_used |
| gce\_instance/default\_metrics | Dirty pages usage in Bytes. | Byte | compute.googleapis.com/guest/memory/dirty\_used |
| gce\_instance/default\_metrics | Page cache memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/page\_cache\_used |
| gce\_instance/default\_metrics | Unevictable memory usage in Bytes | Byte | compute.googleapis.com/guest/memory/unevictable\_used |
| gce\_instance/default\_metrics | Problem Count | Count | compute.googleapis.com/guest/system/problem\_count |
| gce\_instance/default\_metrics | Problem State | Count | compute.googleapis.com/guest/system/problem\_state |
| gce\_instance/default\_metrics | Uptime | Second | compute.googleapis.com/guest/system/uptime |
| gce\_instance/default\_metrics | Reserved vCPUs | Count | compute.googleapis.com/instance/cpu/reserved\_cores |
| gce\_instance/default\_metrics | Scheduler Wait Time | Second | compute.googleapis.com/instance/cpu/scheduler\_wait\_time |
| gce\_instance/default\_metrics | CPU usage | Second | compute.googleapis.com/instance/cpu/usage\_time |
| gce\_instance/default\_metrics | CPU utilization | Percent | compute.googleapis.com/instance/cpu/utilization |
| gce\_instance/default\_metrics | Peak disk read bytes | Byte | compute.googleapis.com/instance/disk/max\_read\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk read ops | Count | compute.googleapis.com/instance/disk/max\_read\_ops\_count |
| gce\_instance/default\_metrics | Peak disk write bytes | Byte | compute.googleapis.com/instance/disk/max\_write\_bytes\_count |
| gce\_instance/default\_metrics | Peak disk write ops | Count | compute.googleapis.com/instance/disk/max\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk read bytes | Byte | compute.googleapis.com/instance/disk/read\_bytes\_count |
| gce\_instance/default\_metrics | Disk read operations | Count | compute.googleapis.com/instance/disk/read\_ops\_count |
| gce\_instance/default\_metrics | Throttled read bytes | Byte | compute.googleapis.com/instance/disk/throttled\_read\_bytes\_count |
| gce\_instance/default\_metrics | Throttled read operations | Count | compute.googleapis.com/instance/disk/throttled\_read\_ops\_count |
| gce\_instance/default\_metrics | Throttled write bytes | Byte | compute.googleapis.com/instance/disk/throttled\_write\_bytes\_count |
| gce\_instance/default\_metrics | Throttled write operations | Count | compute.googleapis.com/instance/disk/throttled\_write\_ops\_count |
| gce\_instance/default\_metrics | Disk write bytes | Byte | compute.googleapis.com/instance/disk/write\_bytes\_count |
| gce\_instance/default\_metrics | Disk write operations | Count | compute.googleapis.com/instance/disk/write\_ops\_count |
| gce\_instance/default\_metrics | Early Boot Validation | Count | compute.googleapis.com/instance/integrity/early\_boot\_validation\_status |
| gce\_instance/default\_metrics | Late Boot Validation | Count | compute.googleapis.com/instance/integrity/late\_boot\_validation\_status |
| gce\_instance/default\_metrics | VM Memory Total | Byte | compute.googleapis.com/instance/memory/balloon/ram\_size |
| gce\_instance/default\_metrics | VM Memory Used | Byte | compute.googleapis.com/instance/memory/balloon/ram\_used |
| gce\_instance/default\_metrics | VM Swap In | Byte | compute.googleapis.com/instance/memory/balloon/swap\_in\_bytes\_count |
| gce\_instance/default\_metrics | VM Swap Out | Byte | compute.googleapis.com/instance/memory/balloon/swap\_out\_bytes\_count |
| gce\_instance/default\_metrics | Received bytes | Byte | compute.googleapis.com/instance/network/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets | Count | compute.googleapis.com/instance/network/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes | Byte | compute.googleapis.com/instance/network/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets | Count | compute.googleapis.com/instance/network/sent\_packets\_count |
| gce\_instance/default\_metrics | Uptime | Second | compute.googleapis.com/instance/uptime |
| gce\_instance/default\_metrics | Uptime Total | Second | compute.googleapis.com/instance/uptime\_total |
| gce\_instance/default\_metrics | Dropped packets | Count | compute.googleapis.com/mirroring/dropped\_packets\_count |
| gce\_instance/default\_metrics | Mirrored bytes | Byte | compute.googleapis.com/mirroring/mirrored\_bytes\_count |
| gce\_instance/default\_metrics | Mirrored packets | Count | compute.googleapis.com/mirroring/mirrored\_packets\_count |
| gce\_instance/default\_metrics | Allocated ports | Unspecified | compute.googleapis.com/nat/allocated\_ports |
| gce\_instance/default\_metrics | Closed connections count | Unspecified | compute.googleapis.com/nat/closed\_connections\_count |
| gce\_instance/default\_metrics | Received packets dropped count | Unspecified | compute.googleapis.com/nat/dropped\_received\_packets\_count |
| gce\_instance/default\_metrics | Sent packets dropped count | Unspecified | compute.googleapis.com/nat/dropped\_sent\_packets\_count |
| gce\_instance/default\_metrics | New connections count | Unspecified | compute.googleapis.com/nat/new\_connections\_count |
| gce\_instance/default\_metrics | Open connections | Unspecified | compute.googleapis.com/nat/open\_connections |
| gce\_instance/default\_metrics | Port usage | Unspecified | compute.googleapis.com/nat/port\_usage |
| gce\_instance/default\_metrics | Received bytes count | Byte | compute.googleapis.com/nat/received\_bytes\_count |
| gce\_instance/default\_metrics | Received packets count | Unspecified | compute.googleapis.com/nat/received\_packets\_count |
| gce\_instance/default\_metrics | Sent bytes count | Byte | compute.googleapis.com/nat/sent\_bytes\_count |
| gce\_instance/default\_metrics | Sent packets count | Unspecified | compute.googleapis.com/nat/sent\_packets\_count |
| gce\_instance/agent | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| gce\_instance/agent | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| gce\_instance/agent | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| gce\_instance/agent | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| gce\_instance/agent | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| gce\_instance/agent | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| gce\_instance/agent | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| gce\_instance/agent | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| gce\_instance/agent | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/apache/connections |
| gce\_instance/agent | Idle workers | Count | agent.googleapis.com/apache/idle\_workers |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/apache/request\_count |
| gce\_instance/agent | Scoreboard | Count | agent.googleapis.com/apache/scoreboard |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/apache/traffic |
| gce\_instance/agent | Hit count | Count | agent.googleapis.com/cassandra/cache/hits |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/50p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/95p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/99p |
| gce\_instance/agent | Read latency | MicroSecond | agent.googleapis.com/cassandra/client\_request/latency/max |
| gce\_instance/agent | Compression ratio | Count | agent.googleapis.com/cassandra/column\_family/compression\_ratio |
| gce\_instance/agent | Max row size | Byte | agent.googleapis.com/cassandra/column\_family/max\_row\_size |
| gce\_instance/agent | Commit log size | Byte | agent.googleapis.com/cassandra/commitlog\_total\_size |
| gce\_instance/agent | Completed tasks | Count | agent.googleapis.com/cassandra/completed\_tasks |
| gce\_instance/agent | Tasks | Count | agent.googleapis.com/cassandra/current\_tasks |
| gce\_instance/agent | Dropped messages | Count | agent.googleapis.com/cassandra/dropped\_message/dropped\_count |
| gce\_instance/agent | Exceptions | Count | agent.googleapis.com/cassandra/storage\_service\_exception\_count |
| gce\_instance/agent | Storage load | Byte | agent.googleapis.com/cassandra/storage\_service\_load |
| gce\_instance/agent | Request latency | MilliSecond | agent.googleapis.com/couchdb/average\_request\_time |
| gce\_instance/agent | Bulk requests | Count | agent.googleapis.com/couchdb/httpd/bulk\_request\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/couchdb/httpd/request\_count |
| gce\_instance/agent | Request methods | Count | agent.googleapis.com/couchdb/httpd/request\_method\_count |
| gce\_instance/agent | Response codes | Count | agent.googleapis.com/couchdb/httpd/response\_code\_count |
| gce\_instance/agent | Temp view reads | Count | agent.googleapis.com/couchdb/httpd/temporary\_view\_read\_count |
| gce\_instance/agent | View reads | Count | agent.googleapis.com/couchdb/httpd/view\_read\_count |
| gce\_instance/agent | Open databases | Count | agent.googleapis.com/couchdb/open\_databases |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/couchdb/open\_files |
| gce\_instance/agent | Reads | Count | agent.googleapis.com/couchdb/read\_count |
| gce\_instance/agent | Writes | Count | agent.googleapis.com/couchdb/write\_count |
| gce\_instance/agent | CPU load (15m) | Count | agent.googleapis.com/cpu/load\_15m |
| gce\_instance/agent | CPU load (1m) | Count | agent.googleapis.com/cpu/load\_1m |
| gce\_instance/agent | CPU load (5m) | Count | agent.googleapis.com/cpu/load\_5m |
| gce\_instance/agent | CPU usage | Second | agent.googleapis.com/cpu/usage\_time |
| gce\_instance/agent | CPU utilization | Percent | agent.googleapis.com/cpu/utilization |
| gce\_instance/agent | Disk usage | Byte | agent.googleapis.com/disk/bytes\_used |
| gce\_instance/agent | Disk I/O time | MilliSecond | agent.googleapis.com/disk/io\_time |
| gce\_instance/agent | Disk merged operations | Count | agent.googleapis.com/disk/merged\_operations |
| gce\_instance/agent | Disk operations | Count | agent.googleapis.com/disk/operation\_count |
| gce\_instance/agent | Disk operation time | MilliSecond | agent.googleapis.com/disk/operation\_time |
| gce\_instance/agent | Disk pending operations | Count | agent.googleapis.com/disk/pending\_operations |
| gce\_instance/agent | Disk utilization | Percent | agent.googleapis.com/disk/percent\_used |
| gce\_instance/agent | Disk bytes read | Byte | agent.googleapis.com/disk/read\_bytes\_count |
| gce\_instance/agent | Disk weighted I/O time | MilliSecond | agent.googleapis.com/disk/weighted\_io\_time |
| gce\_instance/agent | Disk bytes written | Byte | agent.googleapis.com/disk/write\_bytes\_count |
| gce\_instance/agent | Cache size | Byte | agent.googleapis.com/elasticsearch/cache\_memory\_usage |
| gce\_instance/agent | Field evictions | Count | agent.googleapis.com/elasticsearch/field\_eviction\_count |
| gce\_instance/agent | Filter evictions | Count | agent.googleapis.com/elasticsearch/filter\_cache\_eviction\_count |
| gce\_instance/agent | GC count | Count | agent.googleapis.com/elasticsearch/gc\_collection\_count |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/elasticsearch/memory\_usage |
| gce\_instance/agent | Network traffic | Byte | agent.googleapis.com/elasticsearch/network |
| gce\_instance/agent | Documents | Count | agent.googleapis.com/elasticsearch/num\_current\_documents |
| gce\_instance/agent | Data nodes | Count | agent.googleapis.com/elasticsearch/num\_data\_nodes |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/elasticsearch/num\_http\_connections |
| gce\_instance/agent | Nodes | Count | agent.googleapis.com/elasticsearch/num\_nodes |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/elasticsearch/num\_open\_files |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/elasticsearch/num\_server\_connections |
| gce\_instance/agent | Shards | Count | agent.googleapis.com/elasticsearch/num\_shards |
| gce\_instance/agent | Completed operations | Count | agent.googleapis.com/elasticsearch/operation\_count |
| gce\_instance/agent | Operation time | MilliSecond | agent.googleapis.com/elasticsearch/operation\_time |
| gce\_instance/agent | Max threads | Count | agent.googleapis.com/elasticsearch/peak\_threads |
| gce\_instance/agent | Storage size | Byte | agent.googleapis.com/elasticsearch/storage\_size |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/elasticsearch/threads |
| gce\_instance/agent | IPC connections | Count | agent.googleapis.com/hbase/ipc/connections |
| gce\_instance/agent | IPC queue size | Count | agent.googleapis.com/hbase/ipc/queue\_length |
| gce\_instance/agent | IPC traffic | Byte | agent.googleapis.com/hbase/ipc/traffic\_count |
| gce\_instance/agent | Load | Count | agent.googleapis.com/hbase/master/average\_load |
| gce\_instance/agent | Dead region servers | Count | agent.googleapis.com/hbase/master/dead\_region\_servers |
| gce\_instance/agent | Live region servers | Count | agent.googleapis.com/hbase/master/live\_region\_servers |
| gce\_instance/agent | Block cache accesses | Count | agent.googleapis.com/hbase/regionserver/block\_cache/access\_count |
| gce\_instance/agent | Evicted block count | Count | agent.googleapis.com/hbase/regionserver/block\_cache/evicted\_blocks\_count |
| gce\_instance/agent | Block cache hit ratio | Percent | agent.googleapis.com/hbase/regionserver/block\_cache/hit\_ratio\_percent |
| gce\_instance/agent | Block cache size | Byte | agent.googleapis.com/hbase/regionserver/block\_cache/memory |
| gce\_instance/agent | Block count | Count | agent.googleapis.com/hbase/regionserver/block\_cache/num\_items |
| gce\_instance/agent | Call queue size | Count | agent.googleapis.com/hbase/regionserver/call\_queue/length |
| gce\_instance/agent | Compaction queue size | Count | agent.googleapis.com/hbase/regionserver/compaction\_queue/length |
| gce\_instance/agent | Flush queue size | Count | agent.googleapis.com/hbase/regionserver/flush\_queue/length |
| gce\_instance/agent | Heap usage | Byte | agent.googleapis.com/hbase/regionserver/memory/heap\_usage |
| gce\_instance/agent | Memstore files | Count | agent.googleapis.com/hbase/regionserver/memstore/files |
| gce\_instance/agent | Memstore index size | Byte | agent.googleapis.com/hbase/regionserver/memstore/index\_size |
| gce\_instance/agent | Memstore open stores | Count | agent.googleapis.com/hbase/regionserver/memstore/open\_stores |
| gce\_instance/agent | Memstore size | Byte | agent.googleapis.com/hbase/regionserver/memstore/size |
| gce\_instance/agent | Online regions | Count | agent.googleapis.com/hbase/regionserver/online\_regions |
| gce\_instance/agent | Request count | Count | agent.googleapis.com/hbase/regionserver/request\_count |
| gce\_instance/agent | RPC request rate | PerSecond | agent.googleapis.com/hbase/regionserver/requests/total\_rate |
| gce\_instance/agent | Slow operations | Count | agent.googleapis.com/hbase/regionserver/slow\_operation\_count |
| gce\_instance/agent | Thrift average batch latency | NanoSecond | agent.googleapis.com/hbase/thrift/batch\_latency/average |
| gce\_instance/agent | Thrift average call latency | NanoSecond | agent.googleapis.com/hbase/thrift/call\_latency/average |
| gce\_instance/agent | Thrift call queue size | Count | agent.googleapis.com/hbase/thrift/call\_queue/length |
| gce\_instance/agent | Thrift average slow call latency | NanoSecond | agent.googleapis.com/hbase/thrift/slow\_call\_latency/average |
| gce\_instance/agent | Thrift average time in queue | NanoSecond | agent.googleapis.com/hbase/thrift/time\_in\_queue/average |
| gce\_instance/agent | IIS open connections | Count | agent.googleapis.com/iis/current\_connections |
| gce\_instance/agent | IIS transferred bytes | Byte | agent.googleapis.com/iis/network/transferred\_bytes\_count |
| gce\_instance/agent | IIS connections | Count | agent.googleapis.com/iis/new\_connection\_count |
| gce\_instance/agent | IIS requests | Count | agent.googleapis.com/iis/request\_count |
| gce\_instance/agent | Network errors | Count | agent.googleapis.com/interface/errors |
| gce\_instance/agent | Network packets | Count | agent.googleapis.com/interface/packets |
| gce\_instance/agent | Network traffic | Byte | agent.googleapis.com/interface/traffic |
| gce\_instance/agent | GC count | Count | agent.googleapis.com/jvm/gc/count |
| gce\_instance/agent | GC time | MilliSecond | agent.googleapis.com/jvm/gc/time |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/jvm/memory/usage |
| gce\_instance/agent | CPU time | NanoSecond | agent.googleapis.com/jvm/os/cpu\_time |
| gce\_instance/agent | Open files | Count | agent.googleapis.com/jvm/os/open\_files |
| gce\_instance/agent | Daemon threads | Count | agent.googleapis.com/jvm/thread/num\_daemon |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/jvm/thread/num\_live |
| gce\_instance/agent | Max threads | Count | agent.googleapis.com/jvm/thread/peak |
| gce\_instance/agent | Uptime | MilliSecond | agent.googleapis.com/jvm/uptime |
| gce\_instance/agent | Failed requests | Count | agent.googleapis.com/kafka/broker/topics/failed\_request\_count |
| gce\_instance/agent | Incoming messages | Count | agent.googleapis.com/kafka/broker/topics/incoming\_message\_count |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/kafka/broker/topics/traffic |
| gce\_instance/agent | Active controllers | Count | agent.googleapis.com/kafka/controller/kafka/active |
| gce\_instance/agent | Offline partitions | Count | agent.googleapis.com/kafka/controller/kafka/offline\_partitions |
| gce\_instance/agent | Leader elections | Count | agent.googleapis.com/kafka/controller/leader\_elections/election\_count |
| gce\_instance/agent | Stale leader elections | Count | agent.googleapis.com/kafka/controller/leader\_elections/unclean\_count |
| gce\_instance/agent | Flushes | Count | agent.googleapis.com/kafka/log/flush\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/kafka/network/request\_count |
| gce\_instance/agent | Delayed purgatory requests | Count | agent.googleapis.com/kafka/purgatory/num\_delayed\_requests |
| gce\_instance/agent | Purgatory requests | Count | agent.googleapis.com/kafka/purgatory/size |
| gce\_instance/agent | Maximum lag | Count | agent.googleapis.com/kafka/replica\_fetcher/max\_lag |
| gce\_instance/agent | Minimum fetch rate | PerSecond | agent.googleapis.com/kafka/replica\_fetcher/min\_fetch\_rate |
| gce\_instance/agent | Gaining replicas | Count | agent.googleapis.com/kafka/replica\_manager/isr/expand\_count |
| gce\_instance/agent | Lagging replicas | Count | agent.googleapis.com/kafka/replica\_manager/isr/shrink\_count |
| gce\_instance/agent | Leaders | Count | agent.googleapis.com/kafka/replica\_manager/leaders |
| gce\_instance/agent | Partitions | Count | agent.googleapis.com/kafka/replica\_manager/partitions |
| gce\_instance/agent | Unreliable partitions | Count | agent.googleapis.com/kafka/replica\_manager/under\_replicated\_partitions |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/memcached/command\_count |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/memcached/current\_connections |
| gce\_instance/agent | Items | Count | agent.googleapis.com/memcached/current\_items |
| gce\_instance/agent | Evictions | Count | agent.googleapis.com/memcached/eviction\_count |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/memcached/memory |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/memcached/network |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/memcached/operation\_count |
| gce\_instance/agent | Hit ratio | Percent | agent.googleapis.com/memcached/operation\_hitratio |
| gce\_instance/agent | CPU time | Second | agent.googleapis.com/memcached/rusage |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/memcached/threads |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/memory/bytes\_used |
| gce\_instance/agent | Memory utilization | Percent | agent.googleapis.com/memory/percent\_used |
| gce\_instance/agent | Cache hits | Count | agent.googleapis.com/mongodb/cache/hits |
| gce\_instance/agent | Cache misses | Count | agent.googleapis.com/mongodb/cache/misses |
| gce\_instance/agent | Collections | Count | agent.googleapis.com/mongodb/collections |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/mongodb/connections |
| gce\_instance/agent | Data size | Byte | agent.googleapis.com/mongodb/data\_size |
| gce\_instance/agent | Extents | Count | agent.googleapis.com/mongodb/extents |
| gce\_instance/agent | Global lock time | MilliSecond | agent.googleapis.com/mongodb/global\_lock\_hold\_time |
| gce\_instance/agent | Index size | Byte | agent.googleapis.com/mongodb/index\_size |
| gce\_instance/agent | Indexes | Count | agent.googleapis.com/mongodb/indexes |
| gce\_instance/agent | Memory usage | MebiByte | agent.googleapis.com/mongodb/memory\_usage |
| gce\_instance/agent | Objects | Count | agent.googleapis.com/mongodb/objects |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/mongodb/operation\_count |
| gce\_instance/agent | Storage size | Byte | agent.googleapis.com/mongodb/storage\_size |
| gce\_instance/agent | SQL Server open connections | Count | agent.googleapis.com/mssql/connections/user |
| gce\_instance/agent | SQL Server transaction rate | PerSecond | agent.googleapis.com/mssql/transaction\_rate |
| gce\_instance/agent | SQL Server write transaction rate | PerSecond | agent.googleapis.com/mssql/write\_transaction\_rate |
| gce\_instance/agent | Buffer pool pages | Count | agent.googleapis.com/mysql/buffer\_pool/num\_pages |
| gce\_instance/agent | Buffer pool operations | Count | agent.googleapis.com/mysql/buffer\_pool/operation\_count |
| gce\_instance/agent | Buffer pool size | Byte | agent.googleapis.com/mysql/buffer\_pool\_size |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/mysql/command\_count |
| gce\_instance/agent | Handlers | Count | agent.googleapis.com/mysql/handler\_count |
| gce\_instance/agent | InnoDB doublewrite buffers | Count | agent.googleapis.com/mysql/innodb/doublewrite\_count |
| gce\_instance/agent | InnoDB log operations | Count | agent.googleapis.com/mysql/innodb/log\_operation\_count |
| gce\_instance/agent | InnoDB operations | Count | agent.googleapis.com/mysql/innodb/operation\_count |
| gce\_instance/agent | InnoDB page operations | Count | agent.googleapis.com/mysql/innodb/page\_operation\_count |
| gce\_instance/agent | InnoDB locks | Count | agent.googleapis.com/mysql/innodb/row\_lock\_count |
| gce\_instance/agent | InnoDB row operations | Count | agent.googleapis.com/mysql/innodb/row\_operation\_count |
| gce\_instance/agent | Locks | Count | agent.googleapis.com/mysql/lock\_count |
| gce\_instance/agent | QCache operations | Count | agent.googleapis.com/mysql/qcache/operation\_count |
| gce\_instance/agent | QCache queries | Count | agent.googleapis.com/mysql/qcache/query\_count |
| gce\_instance/agent | Replica lag | Second | agent.googleapis.com/mysql/slave\_replication\_lag |
| gce\_instance/agent | Sorts | Count | agent.googleapis.com/mysql/sort\_count |
| gce\_instance/agent | Threads | Count | agent.googleapis.com/mysql/thread\_count |
| gce\_instance/agent | TCP connections | Count | agent.googleapis.com/network/tcp\_connections |
| gce\_instance/agent | Accepted connections | Count | agent.googleapis.com/nginx/connections/accepted\_count |
| gce\_instance/agent | Active connections | Count | agent.googleapis.com/nginx/connections/current |
| gce\_instance/agent | Handled connections | Count | agent.googleapis.com/nginx/connections/handled\_count |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/nginx/request\_count |
| gce\_instance/agent | Pagefile utilization | Percent | agent.googleapis.com/pagefile/percent\_used |
| gce\_instance/agent | Blocks read | Count | agent.googleapis.com/postgresql/blocks\_read\_count |
| gce\_instance/agent | Commits | Count | agent.googleapis.com/postgresql/commit\_count |
| gce\_instance/agent | DB size | Byte | agent.googleapis.com/postgresql/db\_size |
| gce\_instance/agent | Backends | Count | agent.googleapis.com/postgresql/num\_backends |
| gce\_instance/agent | DB rows | Count | agent.googleapis.com/postgresql/num\_tuples |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/postgresql/operation\_count |
| gce\_instance/agent | Rollbacks | Count | agent.googleapis.com/postgresql/rollback\_count |
| gce\_instance/agent | Processes | Count | agent.googleapis.com/processes/count\_by\_state |
| gce\_instance/agent | Process CPU | Second | agent.googleapis.com/processes/cpu\_time |
| gce\_instance/agent | Process disk read I/O | Byte | agent.googleapis.com/processes/disk/read\_bytes\_count |
| gce\_instance/agent | Process disk write I/O | Byte | agent.googleapis.com/processes/disk/write\_bytes\_count |
| gce\_instance/agent | Fork count | Count | agent.googleapis.com/processes/fork\_count |
| gce\_instance/agent | Process resident memory | Byte | agent.googleapis.com/processes/rss\_usage |
| gce\_instance/agent | Process virtual memory | Byte | agent.googleapis.com/processes/vm\_usage |
| gce\_instance/agent | Consumers | Count | agent.googleapis.com/rabbitmq/consumers |
| gce\_instance/agent | Delivery rate | PerSecond | agent.googleapis.com/rabbitmq/delivery\_rate |
| gce\_instance/agent | Messages | Count | agent.googleapis.com/rabbitmq/num\_messages |
| gce\_instance/agent | Publish rate | PerSecond | agent.googleapis.com/rabbitmq/publish\_rate |
| gce\_instance/agent | Unsaved changes | Count | agent.googleapis.com/redis/changes\_since\_last\_save |
| gce\_instance/agent | Blocked clients | Count | agent.googleapis.com/redis/clients/blocked |
| gce\_instance/agent | Connected clients | Count | agent.googleapis.com/redis/clients/connected |
| gce\_instance/agent | Commands | Count | agent.googleapis.com/redis/commands\_processed |
| gce\_instance/agent | Slave connections | Count | agent.googleapis.com/redis/connections/slaves |
| gce\_instance/agent | Connections | Count | agent.googleapis.com/redis/connections/total |
| gce\_instance/agent | Expired keys | Count | agent.googleapis.com/redis/expired\_keys |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/redis/memory/usage |
| gce\_instance/agent | Lua memory usage | Byte | agent.googleapis.com/redis/memory/usage\_lua |
| gce\_instance/agent | PubSub channels | Count | agent.googleapis.com/redis/pubsub/channels |
| gce\_instance/agent | PubSub patterns | Count | agent.googleapis.com/redis/pubsub/patterns |
| gce\_instance/agent | Uptime | Second | agent.googleapis.com/redis/uptime |
| gce\_instance/agent | 95% latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/95th\_percentile |
| gce\_instance/agent | Average latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/average |
| gce\_instance/agent | Maximum latency (1m) | MicroSecond | agent.googleapis.com/riak/latency/maximum |
| gce\_instance/agent | Memory usage | Byte | agent.googleapis.com/riak/memory\_usage |
| gce\_instance/agent | 95% siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/95th\_percentile |
| gce\_instance/agent | Average siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/average |
| gce\_instance/agent | Maximum siblings (1m) | Count | agent.googleapis.com/riak/num\_siblings/maximum |
| gce\_instance/agent | 95% object size (1m) | Byte | agent.googleapis.com/riak/object\_size/95th\_percentile |
| gce\_instance/agent | Average object size (1m) | Byte | agent.googleapis.com/riak/object\_size/average |
| gce\_instance/agent | Maximum object size (1m) | Byte | agent.googleapis.com/riak/object\_size/maximum |
| gce\_instance/agent | Operations | Count | agent.googleapis.com/riak/operation\_count |
| gce\_instance/agent | Swap usage | Byte | agent.googleapis.com/swap/bytes\_used |
| gce\_instance/agent | Swap I/O operations | Count | agent.googleapis.com/swap/io |
| gce\_instance/agent | Swap utilization | Percent | agent.googleapis.com/swap/percent\_used |
| gce\_instance/agent | Sessions | Count | agent.googleapis.com/tomcat/manager/sessions |
| gce\_instance/agent | Errors | Count | agent.googleapis.com/tomcat/request\_processor/error\_count |
| gce\_instance/agent | Processing time | MilliSecond | agent.googleapis.com/tomcat/request\_processor/processing\_time |
| gce\_instance/agent | Requests | Count | agent.googleapis.com/tomcat/request\_processor/request\_count |
| gce\_instance/agent | Traffic | Byte | agent.googleapis.com/tomcat/request\_processor/traffic\_count |
| gce\_instance/agent | Busy threads | Count | agent.googleapis.com/tomcat/threads/busy |
| gce\_instance/agent | Current threads | Count | agent.googleapis.com/tomcat/threads/current |
| gce\_instance/agent | Backend connection successes | Count | agent.googleapis.com/varnish/backend\_connection\_count |
| gce\_instance/agent | Cache operations | Count | agent.googleapis.com/varnish/cache\_operation\_count |
| gce\_instance/agent | Client connections | Count | agent.googleapis.com/varnish/client\_connection\_count |
| gce\_instance/agent | Open connections | Count | agent.googleapis.com/zookeeper/connections\_count |
| gce\_instance/agent | Data size | Byte | agent.googleapis.com/zookeeper/data\_size |
| gce\_instance/agent | Followers | Count | agent.googleapis.com/zookeeper/followers/count |
| gce\_instance/agent | Synced followers | Count | agent.googleapis.com/zookeeper/followers/synced\_count |
| gce\_instance/agent | Packets received | Count | agent.googleapis.com/zookeeper/network/received\_packets\_count |
| gce\_instance/agent | Packets sent | Count | agent.googleapis.com/zookeeper/network/sent\_packets\_count |
| gce\_instance/agent | Nodes | Count | agent.googleapis.com/zookeeper/nodes/count |
| gce\_instance/agent | Ephemeral nodes | Count | agent.googleapis.com/zookeeper/nodes/ephemeral\_count |
| gce\_instance/agent | Watches | Count | agent.googleapis.com/zookeeper/nodes/watches\_count |
| gce\_instance/agent | Average request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/average |
| gce\_instance/agent | Maximum request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/maximum |
| gce\_instance/agent | Minimum request latency | MilliSecond | agent.googleapis.com/zookeeper/requests/latency/minimum |
| gce\_instance/agent | Outstanding requests | Count | agent.googleapis.com/zookeeper/requests/outstanding\_count |
| gce\_instance/agent | Pending syncs | Count | agent.googleapis.com/zookeeper/sync\_operations/pending\_count |
| gce\_instance/firewallinsights | VM Firewall Hit Counts | Count | firewallinsights.googleapis.com/vm/firewall\_hit\_count |
| gce\_instance/firewallinsights | VM Firewall Last Used Timestamp | Count | firewallinsights.googleapis.com/vm/firewall\_last\_used\_timestamp |
| gce\_instance/istio | Client Connection Close Count | Byte | istio.io/service/client/connection\_close\_count |
| gce\_instance/istio | Client Connection Open Count | Byte | istio.io/service/client/connection\_open\_count |
| gce\_instance/istio | Client Received Bytes Count | Byte | istio.io/service/client/received\_bytes\_count |
| gce\_instance/istio | Client Request Bytes | Byte | istio.io/service/client/request\_bytes |
| gce\_instance/istio | Client Request Count | Count | istio.io/service/client/request\_count |
| gce\_instance/istio | Client Response Bytes | Byte | istio.io/service/client/response\_bytes |
| gce\_instance/istio | Client Roundtrip Latencies | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| gce\_instance/istio | Client Sent Bytes Count | Byte | istio.io/service/client/sent\_bytes\_count |
| gce\_instance/istio | Server Connection Close Count | Byte | istio.io/service/server/connection\_close\_count |
| gce\_instance/istio | Server Connection Open Count | Byte | istio.io/service/server/connection\_open\_count |
| gce\_instance/istio | Server Received Bytes Count | Byte | istio.io/service/server/received\_bytes\_count |
| gce\_instance/istio | Server Request Bytes | Byte | istio.io/service/server/request\_bytes |
| gce\_instance/istio | Server Request Count | Count | istio.io/service/server/request\_count |
| gce\_instance/istio | Server Response Bytes | Byte | istio.io/service/server/response\_bytes |
| gce\_instance/istio | Server Response Latencies | MilliSecond | istio.io/service/server/response\_latencies |
| gce\_instance/istio | Server Sent Bytes Count | Byte | istio.io/service/server/sent\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Egress bytes | Byte | networking.googleapis.com/vm\_flow/egress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | Ingress bytes | Byte | networking.googleapis.com/vm\_flow/ingress\_bytes\_count |
| gce\_instance\_vm\_flow/default\_metrics | RTT latencies | MilliSecond | networking.googleapis.com/vm\_flow/rtt |
| instance\_group/default\_metrics | Instance group size | Count | compute.googleapis.com/instance\_group/size |
| autoscaler/default\_metrics | Serving capacity | Count | autoscaler.googleapis.com/capacity |
| autoscaler/default\_metrics | Current Autoscaler utilization | Count | autoscaler.googleapis.com/current\_utilization |
| tpu\_worker/default\_metrics | Container CPU utilization | Percent | tpu.googleapis.com/container/cpu/utilization |
| tpu\_worker/default\_metrics | Container memory usage | Byte | tpu.googleapis.com/container/memory/usage |
| tpu\_worker/default\_metrics | CPU utilization | Percent | tpu.googleapis.com/cpu/utilization |
| tpu\_worker/default\_metrics | Memory usage | Byte | tpu.googleapis.com/memory/usage |
| tpu\_worker/default\_metrics | Network bytes received | Byte | tpu.googleapis.com/network/received\_bytes\_count |
| tpu\_worker/default\_metrics | Network bytes sent | Byte | tpu.googleapis.com/network/sent\_bytes\_count |
| tpu\_worker/default\_metrics | MXU utilization | Percent | tpu.googleapis.com/tpu/mxu/utilization |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: google-compute-engine.md


---
title: Monitor Google Compute Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine
scraped: 2026-02-17T21:19:37.160171
---

# Monitor Google Compute Engine

# Monitor Google Compute Engine

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 03, 2018

## Deploy OneAgent

Monitoring Google Compute Engine instances works out-of-the-box by just running the regular [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.") and [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.") OneAgent installers. Youâll get full-stack visibility, from hosts to processes and services layer.

## Update OneAgent

You can update OneAgent by running regular [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.") and [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.") OneAgent update.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: google-kubernetes-engine-monitoring.md


---
title: Google Kubernetes Engine monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring
scraped: 2026-02-17T21:26:43.389269
---

# Google Kubernetes Engine monitoring

# Google Kubernetes Engine monitoring

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Kubernetes Engine.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| k8s\_cluster/default\_metrics | Log entries | Count | logging.googleapis.com/log\_entry\_count |
| k8s\_node/default\_metrics | Allocatable cores | Unspecified | kubernetes.io/node/cpu/allocatable\_cores |
| k8s\_node/default\_metrics | CPU allocatable utilization | Count | kubernetes.io/node/cpu/allocatable\_utilization |
| k8s\_node/default\_metrics | CPU usage time | Second | kubernetes.io/node/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Total cores | Unspecified | kubernetes.io/node/cpu/total\_cores |
| k8s\_node/default\_metrics | Allocatable ephemeral storage | Byte | kubernetes.io/node/ephemeral\_storage/allocatable\_bytes |
| k8s\_node/default\_metrics | Free inodes | Count | kubernetes.io/node/ephemeral\_storage/inodes\_free |
| k8s\_node/default\_metrics | Total inodes | Count | kubernetes.io/node/ephemeral\_storage/inodes\_total |
| k8s\_node/default\_metrics | Total ephemeral storage | Byte | kubernetes.io/node/ephemeral\_storage/total\_bytes |
| k8s\_node/default\_metrics | Ephemeral storage usage | Byte | kubernetes.io/node/ephemeral\_storage/used\_bytes |
| k8s\_node/default\_metrics | Allocatable memory | Byte | kubernetes.io/node/memory/allocatable\_bytes |
| k8s\_node/default\_metrics | Memory allocatable utilization | Count | kubernetes.io/node/memory/allocatable\_utilization |
| k8s\_node/default\_metrics | Total memory | Byte | kubernetes.io/node/memory/total\_bytes |
| k8s\_node/default\_metrics | Memory usage | Byte | kubernetes.io/node/memory/used\_bytes |
| k8s\_node/default\_metrics | Bytes received | Byte | kubernetes.io/node/network/received\_bytes\_count |
| k8s\_node/default\_metrics | Bytes transmitted | Byte | kubernetes.io/node/network/sent\_bytes\_count |
| k8s\_node/default\_metrics | PID capacity | Count | kubernetes.io/node/pid\_limit |
| k8s\_node/default\_metrics | PID usage | Count | kubernetes.io/node/pid\_used |
| k8s\_node/default\_metrics | CPU usage time | Second | kubernetes.io/node\_daemon/cpu/core\_usage\_time |
| k8s\_node/default\_metrics | Memory usage | Byte | kubernetes.io/node\_daemon/memory/used\_bytes |
| k8s\_pod/default\_metrics | Bytes received | Byte | kubernetes.io/pod/network/received\_bytes\_count |
| k8s\_pod/default\_metrics | Bytes transmitted | Byte | kubernetes.io/pod/network/sent\_bytes\_count |
| k8s\_pod/default\_metrics | Volume capacity | Byte | kubernetes.io/pod/volume/total\_bytes |
| k8s\_pod/default\_metrics | Volume usage | Byte | kubernetes.io/pod/volume/used\_bytes |
| k8s\_pod/default\_metrics | Volume utilization | Count | kubernetes.io/pod/volume/utilization |
| k8s\_pod/istio | Client Connection Close Count | Byte | istio.io/service/client/connection\_close\_count |
| k8s\_pod/istio | Client Connection Open Count | Byte | istio.io/service/client/connection\_open\_count |
| k8s\_pod/istio | Client Received Bytes Count | Byte | istio.io/service/client/received\_bytes\_count |
| k8s\_pod/istio | Client Request Bytes | Byte | istio.io/service/client/request\_bytes |
| k8s\_pod/istio | Client Request Count | Count | istio.io/service/client/request\_count |
| k8s\_pod/istio | Client Response Bytes | Byte | istio.io/service/client/response\_bytes |
| k8s\_pod/istio | Client Roundtrip Latencies | MilliSecond | istio.io/service/client/roundtrip\_latencies |
| k8s\_pod/istio | Client Sent Bytes Count | Byte | istio.io/service/client/sent\_bytes\_count |
| k8s\_container/default\_metrics | CPU usage time | Second | kubernetes.io/container/cpu/core\_usage\_time |
| k8s\_container/default\_metrics | Limit cores | Unspecified | kubernetes.io/container/cpu/limit\_cores |
| k8s\_container/default\_metrics | CPU limit utilization | Count | kubernetes.io/container/cpu/limit\_utilization |
| k8s\_container/default\_metrics | Request cores | Unspecified | kubernetes.io/container/cpu/request\_cores |
| k8s\_container/default\_metrics | CPU request utilization | Count | kubernetes.io/container/cpu/request\_utilization |
| k8s\_container/default\_metrics | Ephemeral storage limit | Byte | kubernetes.io/container/ephemeral\_storage/limit\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage request | Byte | kubernetes.io/container/ephemeral\_storage/request\_bytes |
| k8s\_container/default\_metrics | Ephemeral storage usage | Byte | kubernetes.io/container/ephemeral\_storage/used\_bytes |
| k8s\_container/default\_metrics | Memory limit | Byte | kubernetes.io/container/memory/limit\_bytes |
| k8s\_container/default\_metrics | Memory limit utilization | Count | kubernetes.io/container/memory/limit\_utilization |
| k8s\_container/default\_metrics | Page faults | Count | kubernetes.io/container/memory/page\_fault\_count |
| k8s\_container/default\_metrics | Memory request | Byte | kubernetes.io/container/memory/request\_bytes |
| k8s\_container/default\_metrics | Memory request utilization | Count | kubernetes.io/container/memory/request\_utilization |
| k8s\_container/default\_metrics | Memory usage | Byte | kubernetes.io/container/memory/used\_bytes |
| k8s\_container/default\_metrics | Restart count | Count | kubernetes.io/container/restart\_count |
| k8s\_container/default\_metrics | Uptime | Second | kubernetes.io/container/uptime |
| k8s\_container/agent | Monitoring Agent API Request Count | Count | agent.googleapis.com/agent/api\_request\_count |
| k8s\_container/agent | Logging Agent Log Entry Count | Count | agent.googleapis.com/agent/log\_entry\_count |
| k8s\_container/agent | Logging Agent Retried Log Entry Writes Count | Count | agent.googleapis.com/agent/log\_entry\_retry\_count |
| k8s\_container/agent | Monitoring Agent Memory Usage | Byte | agent.googleapis.com/agent/memory\_usage |
| k8s\_container/agent | Monitoring Agent Metric Point Count | Count | agent.googleapis.com/agent/monitoring/point\_count |
| k8s\_container/agent | Logging Agent API Request Count | Count | agent.googleapis.com/agent/request\_count |
| k8s\_container/agent | Monitoring Agent Process Labels Size | Byte | agent.googleapis.com/agent/streamspace\_size |
| k8s\_container/agent | Monitoring Agent is Throttling Processes | Count | agent.googleapis.com/agent/streamspace\_size\_throttling |
| k8s\_container/agent | Monitoring/Logging Agent Uptime | Second | agent.googleapis.com/agent/uptime |
| k8s\_container/apigee | Apigee Cassandra client request latency | Count | apigee.googleapis.com/cassandra/clientrequest\_latency |
| k8s\_container/apigee | Apigee Cassandra pending compaction tasks | Count | apigee.googleapis.com/cassandra/compaction\_pendingtasks |
| k8s\_container/apigee | Apigee Cassandra bytes committed per area | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial memory bytes | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra max bytes of memory | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra used JVM memory bytes | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra bytes committed per memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_committed |
| k8s\_container/apigee | Apigee Cassandra initial bytes of JVM memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_init |
| k8s\_container/apigee | Apigee Cassandra JVM memory pool bytes max | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_max |
| k8s\_container/apigee | Apigee Cassandra bytes per memory pool | Byte | apigee.googleapis.com/cassandra/jvm\_memory\_pool\_bytes\_used |
| k8s\_container/apigee | Apigee Cassandra user and system CPU in seconds | Second | apigee.googleapis.com/cassandra/process\_cpu\_seconds\_total |
| k8s\_container/apigee | Apigee Cassandra process max file descriptors | Count | apigee.googleapis.com/cassandra/process\_max\_fds |
| k8s\_container/apigee | Apigee Cassandra process open file descriptors | Count | apigee.googleapis.com/cassandra/process\_open\_fds |
| k8s\_container/apigee | Apigee server fault count | Count | apigee.googleapis.com/server/fault\_count |
| k8s\_container/apigee | Apigee server latencies | MilliSecond | apigee.googleapis.com/server/latencies |
| k8s\_container/apigee | Apigee server nio | Count | apigee.googleapis.com/server/nio |
| k8s\_container/apigee | Apigee server thread count | Count | apigee.googleapis.com/server/num\_threads |
| k8s\_container/apigee | Apigee server request count | Count | apigee.googleapis.com/server/request\_count |
| k8s\_container/apigee | Apigee server response count | Count | apigee.googleapis.com/server/response\_count |
| k8s\_container/apigee | Apigee UDCA disk used bytes | Byte | apigee.googleapis.com/udca/disk/used\_bytes |
| k8s\_container/apigee | Apigee UDCA server local file count | Count | apigee.googleapis.com/udca/server/local\_file\_count |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and latest file | Second | apigee.googleapis.com/udca/server/local\_file\_latest\_ts |
| k8s\_container/apigee | Apigee UDCA server timestamp difference between current time and oldest file | Second | apigee.googleapis.com/udca/server/local\_file\_oldest\_ts |
| k8s\_container/apigee | Apigee UDCA pruned file count | Count | apigee.googleapis.com/udca/server/pruned\_file\_count |
| k8s\_container/apigee | Apigee UDCA outstanding number of entries in retry cache | Count | apigee.googleapis.com/udca/server/retry\_cache\_size |
| k8s\_container/apigee | Apigee UDCA server total latencies | Second | apigee.googleapis.com/udca/server/total\_latencies |
| k8s\_container/apigee | Apigee UDCA server upload latencies | Second | apigee.googleapis.com/udca/server/upload\_latencies |
| k8s\_container/apigee | Apigee UDCA server HTTP error count | Count | apigee.googleapis.com/udca/upstream/http\_error\_count |
| k8s\_container/apigee | Apigee UDCA server HTTP latencies | Second | apigee.googleapis.com/udca/upstream/http\_latencies |
| k8s\_container/apigee | Apigee UDCA uploaded file count | Count | apigee.googleapis.com/udca/upstream/uploaded\_file\_count |
| k8s\_container/apigee | Apigee UDCA uploaded file size distribution | Byte | apigee.googleapis.com/udca/upstream/uploaded\_file\_sizes |
| k8s\_container/apigee | Apigee upstream latencies | MilliSecond | apigee.googleapis.com/upstream/latencies |
| k8s\_container/apigee | Apigee upstream request count | Count | apigee.googleapis.com/upstream/request\_count |
| k8s\_container/apigee | Apigee upstream response count | Count | apigee.googleapis.com/upstream/response\_count |
| k8s\_container/istio | Config Convergence Latencies | MilliSecond | istio.io/control/config\_convergence\_latencies |
| k8s\_container/istio | Config Event Count | Count | istio.io/control/config\_event\_count |
| k8s\_container/istio | Config Push Count | Count | istio.io/control/config\_push\_count |
| k8s\_container/istio | Config Validation Count | Count | istio.io/control/config\_validation\_count |
| k8s\_container/istio | Proxy Clients | Count | istio.io/control/proxy\_clients |
| k8s\_container/istio | Rejected Config Count | Count | istio.io/control/rejected\_config\_count |
| k8s\_container/istio | Sidecar Injection Count | Count | istio.io/control/sidecar\_injection\_count |
| k8s\_container/istio | Server Connection Close Count | Byte | istio.io/service/server/connection\_close\_count |
| k8s\_container/istio | Server Connection Open Count | Byte | istio.io/service/server/connection\_open\_count |
| k8s\_container/istio | Server Received Bytes Count | Byte | istio.io/service/server/received\_bytes\_count |
| k8s\_container/istio | Server Request Bytes | Byte | istio.io/service/server/request\_bytes |
| k8s\_container/istio | Server Request Count | Count | istio.io/service/server/request\_count |
| k8s\_container/istio | Server Response Bytes | Byte | istio.io/service/server/response\_bytes |
| k8s\_container/istio | Server Response Latencies | MilliSecond | istio.io/service/server/response\_latencies |
| k8s\_container/istio | Server Sent Bytes Count | Byte | istio.io/service/server/sent\_bytes\_count |
| k8s\_container/nginx | Nginx connections\_accepted | Unspecified | kubernetes.io/nginx/connections\_accepted |
| k8s\_container/nginx | Nginx connections\_active | Unspecified | kubernetes.io/nginx/connections\_active |
| k8s\_container/nginx | Nginx connections\_handled | Unspecified | kubernetes.io/nginx/connections\_handled |
| k8s\_container/nginx | Nginx connections\_reading | Unspecified | kubernetes.io/nginx/connections\_reading |
| k8s\_container/nginx | Nginx connections\_waiting | Unspecified | kubernetes.io/nginx/connections\_waiting |
| k8s\_container/nginx | Nginx connections\_writing | Unspecified | kubernetes.io/nginx/connections\_writing |
| k8s\_container/nginx | Nginx http\_requests\_total | Unspecified | kubernetes.io/nginx/http\_requests\_total |
| k8s\_container/nginx | Nginx nginxexporter\_build\_info | Count | kubernetes.io/nginx/nginxexporter\_build\_info |
| k8s\_container/nginx | Nginx up | Count | kubernetes.io/nginx/up |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---


## Source: google-gke.md


---
title: Monitor Google Kubernetes Engine (GKE)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke
scraped: 2026-02-17T21:19:52.550776
---

# Monitor Google Kubernetes Engine (GKE)

# Monitor Google Kubernetes Engine (GKE)

* Latest Dynatrace
* Overview
* 1-min read
* Published Sep 26, 2018

Dynatrace OneAgent provides extensive monitoring of Google Kubernetes Engine pods, nodes, and clusters. The OneAgent deployment process is consistent with other distributions.

## Integration

[Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")

Refer to the [Google Marketplaceï»¿](https://www.dynatrace.com/news/blog/60-seconds-to-self-upgrading-observability-on-google-kubernetes-engine/) for the OneAgent integration with Google Console.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")


---


## Source: gcp-integrations.md


---
title: Google Cloud integrations
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations
scraped: 2026-02-17T04:51:50.084654
---

# Google Cloud integrations

# Google Cloud integrations

* Latest Dynatrace
* Overview
* 1-min read
* Published Aug 12, 2021

Dynatrace OneAgent provides full-stack monitoring on Google Compute Engine and Google Kubernetes Engine, but also monitoring on container and application level. Dynatrace supports Google App Engine with the application-only approach.

## Integrations

[Monitor Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke "Google GKE")

[Google Cloud Functions monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.")

[Monitor Google Cloud Run managed](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun "Monitor Java application deployed on Google Cloud Run managed.")

[Monitor Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.")

[Monitor Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine "Install OneAgent on Google Compute Engine.")

[End-to-end guide for monitoring Google Cloud services integrating Operations Suite](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services")

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)


---


## Source: gcp-supported-service-metrics-legacy.md


---
title: Google Cloud supported service metrics (legacy)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy
scraped: 2026-02-17T21:26:55.224380
---

# Google Cloud supported service metrics (legacy)

# Google Cloud supported service metrics (legacy)

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Apr 12, 2021
* Deprecated

This page refers to the GCP supported service metrics for version 0.1 of the GCP integration, which is scheduled for deprecation.
For a list of supported services and their metrics for version 1.0 of the GCP integration, see [Google Cloud service metrics (new)](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").

Dynatrace supports all metrics available in the Google Operations API.

## Prerequisites

Deploy Dynatrace integration [as a GCP function](/docs/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy "Set up monitoring for Google Cloud services using a Google Cloud Function.") or [in a Kubernetes container](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.").

## Supported services

After deploying the Dynatrace integration, you can start monitoring the GCP supported services. The table below shows available metrics configurations[1](#fn-1-1-def) per service, including [Davis data units (DDUs)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") consumption[2](#fn-1-2-def) per instance per minute.

1

**Metrics configuration** refers to groups of metrics that can be ingested. Use the **Configuration ID** when adjusting the monitoring scope of your setup.

2

**DDU consumption** is an estimation that may vary depending on characteristics of your environment. We recommend that you check your weekly DDU consumptions for more accurate budgeting.

| Service name | Preset dashboard | Configuration name | Configuration ID | DDUs per minute per instance |
| --- | --- | --- | --- | --- |
| Google Cloud Function | Applicable |  | cloud\_function/default | 0.073 DDU |
| Cloud SQL | Applicable | Database | cloudsql\_database/default | 0.066 DDU |
| Google Cloud APIs | Applicable |  | api/default | 0.086 DDU |
| Google Cloud Pub/Sub | Applicable | Snapshot | pubsub\_snapshot/default | 0.021 DDU |
|  |  | Subscription | pubsub\_subscription/default | 0.166 DDU |
|  |  | Topic | pubsub\_topic/default | 0.049 DDU |
| Google Pub/Sub Lite |  | Subscription Partition | pubsublite\_subscription\_partition/default | 0.006 DDU |
|  |  | Topic Partition | pubsublite\_topic\_partition/default | 0.013 DDU |
| Cloud Load Balancing | Applicable | Google Internal HTTP/S Load Balancing Rule | internal\_http\_lb\_rule/default | 0.405 DDU |
|  |  | Google Internal TCP Load Balancer Rule | internal\_tcp\_lb\_rule/default | 0.135 DDU |
|  |  | Google Internal UDP Load Balancer Rule | internal\_udp\_lb\_rule/default | 0.108 DDU |
|  |  | Google Cloud Network UDP Load Balancer Rule | udp\_lb\_rule/default | 0.036 DDU |
|  |  | Google Cloud HTTP/S Load Balancing Rule | https\_lb\_rule/default | 3.897 DDU |
|  |  | Google Cloud Network TCP Load Balancer Rule | tcp\_lb\_rule/default | 0.045 DDU |
|  |  | Google Cloud TCP/SSL Proxy Rule | tcp\_ssl\_proxy\_rule/default | 0.054 DDU |
| Google Kubernetes Engine | Applicable | Container Agent | k8s\_container/agent | 0.021 DDU |
|  |  | Container Apigee | k8s\_container/apigee | 0.268 DDU |
|  |  | Container NGINX | k8s\_container/nginx | 0.017 DDU |
|  |  | Container | k8s\_container/default | 0.024 DDU |
|  |  | Container | gke\_container/default | 0.109 DDU |
|  |  | Cluster | k8s\_cluster/default | 0.009 DDU |
|  |  | Node | k8s\_node/default | 0.039 DDU |
| Google Cloud Datastore | Applicable |  | datastore\_request/default | 0.025 DDU |
| Google Filestore | Applicable | Instance | filestore\_instance/default | 0.048 DDU |
| Google Cloud Storage | Applicable | bucket | gcs\_bucket/default | 0.185 DDU |
| Google VM Instance |  |  | gce\_instance/appenginee | 0.108 DDU |
|  |  | Instance | gce\_instance/default | 2.828 DDU |
|  |  | Agent | gce\_instance/agent | 2.794 DDU |
|  |  | Firewall Insights | gce\_instance/firewallinsights | 0.18 DDU |
|  |  | Google Cloud Router | gce\_router/default | 0.032 DDU |
|  |  | Google Zone Network Health | gce\_zone\_network\_health/default | 0.243 DDU |
|  |  | Uptime Checks | gce\_instance/uptime\_check | 2.187 DDU |
| Google Cloud Spanner |  | Instance | spanner\_instance/default | 0.223 DDU |
| Google Cloud BigQuery |  | BI Engine Model | bigquery\_biengine\_model/default | 0.055 DDU |
|  |  | Dataset | bigquery\_dataset/default | 0.147 DDU |
|  |  | Project | bigquery\_project/default | 0.085 DDU |
| Google Interconnect |  | Default | interconnect/default | 0.03 DDU |
|  |  | Attachment | interconnect\_attachment/default | 0.005 DDU |
| Google Cloud Memorystore |  | Instance | redis\_instance/default | 0.169 DDU |
| Google Apigee |  | Proxy (v2) | apigee.googleapis.com/ProxyV2/default | 0.246 DDU |
|  |  | Environment | apigee.googleapis.com/Environment/default | 0.027 DDU |
|  |  | Proxy | apigee.googleapis.com/Proxy/default | 0.207 DDU |
| Google Consumer Quota |  |  | consumer\_quota/default | 0.021 DDU |
| Google Cloud NAT Gateway |  |  | nat\_gateway/default | 0.04 DDU |
| Google Transfer Service Agent |  |  | transfer\_service\_agent/default | 0.002 DDU |
| Google Cloud DNS Query |  |  | dns\_query/default | 0.003 DDU |
| Google Cloud Run for Anthos Trigger |  |  | knative\_trigger/default | 0.57 DDU |
|  |  | Google Cloud Run for Anthos Broker | knative\_broker/default | 0.27 DDU |
|  |  | Google Cloud Run for Anthos Revision | knative\_revision/default | 0.547 DDU |
| Google Instance Group |  |  | instance\_group/default | 0.001 DDU |
| Google App Engine |  | Application - Uptime Checks | gae\_app\_uptime\_check/default | 2.916 DDU |
|  |  | Application | gae\_app/default | 0.101 DDU |
|  |  | Instance | gae\_instance/default | 0.005 DDU |
| Google Compute Engine Autoscaler |  | Google Autoscaler | autoscaler/default | 0.006 DDU |
| Google Dataflow |  | Job | dataflow\_job/default | 3.397 DDU |
| Google Network Security Policy |  |  | network\_security\_policy/default | 0.018 DDU |
| Google Cloud Logging |  | export sink | logging\_sink/default | 0.003 DDU |
| Google VPC Access Connector |  |  | vpc\_access\_connector/default | 0.004 DDU |
| Google Cloud ML |  | Job | cloudml\_job/default | 0.162 DDU |
|  |  | Model Version | cloudml\_model\_version/default | 0.038 DDU |
| Google Cloud Bigtable |  | Cluster | bigtable\_cluster/default | 0.018 DDU |
|  |  | Table | bigtable\_table/default | 0.111 DDU |
| Google Cloud Amazon EC2 Instance (via GCP) |  |  | cloud\_tasks\_queue/default | 0.014 DDU |
| Google Cloud Composer |  | Environment | cloud\_composer\_environment/default | 0.129 DDU |
| Google Cloud Data Loss Prevention |  | Project | cloud\_dlp\_project/default | 0.019 DDU |
| Google Cloud Dataproc |  | Cluster | cloud\_dataproc\_cluster/default | 0.081 DDU |
| Google Cloud Run Revision |  |  | cloud\_run\_revision/default | 0.059 DDU |
| Google Cloud Trace |  |  | cloudtrace.googleapis.com/CloudtraceProject/default | 0.003 DDU |
| Google Cloud TPU |  | Worker | tpu\_worker/default | 0.013 DDU |
| Google reCAPTCHA |  | Key | recaptchaenterprise.googleapis.com/Key/default | 0.003 DDU |
| Google Firestore |  | Instance | firestore\_instance/default | 0.324 DDU |
| Google NetApp CVS-SO |  |  | cloudvolumesgcp-api.netapp.com/NetAppCloudVolumeSO/default | 0.013 DDU |
| Google NetApp Cloud Volume |  |  | netapp\_cloud\_volume/default | 0.032 DDU |
| Google Assistant Smart Home |  | Google Assistant Action Project | assistant\_action\_project/default | 0.567 DDU |
| Google Firebase Hosting |  | Google Firebase Realtime Database | firebase\_namespace/default | 0.104 DDU |
|  |  | Site Domain | firebase\_domain/default | 1.921 DDU |
| Google Cloud IoT Registry |  |  | cloudiot\_device\_registry/default | 0.026 DDU |
| Google Consumed API |  |  | consumed\_api/default | 0.084 DDU |
| Google Cloud Microsoft Active Directory Domain |  |  | microsoft\_ad\_domain/default | 0.028 DDU |
| Google IAM Service Account |  |  | iam\_service\_account/default | 0.04 DDU |
| Google Producer Quota |  |  | producer\_quota/default | 0.012 DDU |
| Google Uptime Check URL |  |  | uptime\_url/default | 2.916 DDU |
| Google Cloud VPN Tunnel |  |  | vpn\_gatewayv/ | 0.09 DDU |

## View GCP service metrics

Dynatrace provides preset dashboards for a number of GCP services. You can see which GCP services have preset dashboards in the list of GCP supported services above.  
After deploying the Dynatrace integration, you can view these preset dashboards in ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.

**Example preset dashboard:**

![GCP dash](https://dt-cdn.net/images/gcp-api-dashboard-2744-cef7a39830.png)

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")


---
