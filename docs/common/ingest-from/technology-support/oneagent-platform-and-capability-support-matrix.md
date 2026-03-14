---
title: "OneAgent platform and capability support matrix"
source: https://docs.dynatrace.com/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix
updated: 2026-02-09
---

# OneAgent platform and capability support matrix


* Latest Dynatrace
* 13-min read
* Updated on Oct 15, 2025

This page describes which capabilities are supported by OneAgent on different operating systems and platforms.

|  |  |
| --- | --- |
| **GA** | Generally available and fully supported. |
| **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |
| **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |
| **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |
| n/a | Not applicable |

## Operating systems

The tables below contain information about the supported OneAgent capabilities for various supported operating systems. Note that Alpine Linux is supported in containers only, see [Alpine Linux (musl libc) based containers](#musl).

### Code modules

| Code module | [Windows](../technology-support.md#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](../../../ru/ingest-from/technology-support/mainframe-technology-support.md "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](../../../ru/ingest-from/technology-support/application-software/java.md "Learn about all aspects of Dynatrace support for Java application monitoring.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  |  |
| [.NET and .NET Core](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [.NET Framework](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| [Node.js](../../../ru/ingest-from/technology-support/application-software/nodejs.md "Read about Dynatrace support for Node.js applications.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| Python | n/a |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| PHP |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [Go](../../../ru/ingest-from/technology-support/application-software/go.md "Read an overview of Dynatrace support for Go applications.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Apache, IHS |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| NGINX |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Microsoft IIS |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

1

[Classic full-stack mode](../../../ru/ingest-from/setup-on-k8s/how-it-works.md#classic "In-depth description on how the deployment on Kubernetes works.") is not supported for [Alpine Linux (musl libc) based containers](#musl). Please [migrate](../../../ru/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native.md "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") to the [Cloud-native full-stack](../../../ru/ingest-from/setup-on-k8s/how-it-works.md#cloud-native "In-depth description on how the deployment on Kubernetes works.").

2

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### IBM technologies

| Code module | [Windows](../technology-support.md#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](../../../ru/ingest-from/technology-support/mainframe-technology-support.md "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IBM App Connect Enterprise |  |  | n/a | n/a |  |  |  |  |  |
| IBM Integration Bus |  |  | n/a | n/a |  |  |  |  |  |
| IBM CICS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |
| IBM IMS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |

### OneAgent SDK

| OneAgent SDK | [Windows](../technology-support.md#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](../../../ru/ingest-from/technology-support/mainframe-technology-support.md "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) |  |  |  |  |
| OneAgent SDK for Java |  |  |  |  |  |  |  |  |  |
| OneAgent SDK for .NET |  |  |  |  | n/a | n/a | n/a | n/a | n/a |
| OneAgent SDK for Node.js |  |  |  |  |  |  |  | n/a | n/a |
| OneAgent SDK for Python |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | n/a | n/a |

1

We added support for Python, C++, and other runtimes via [OpenTelemetry](../../../ru/ingest-from/opentelemetry.md "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") instead of the Dynatrace SDK (which is Dynatrace-proprietary). This is available on any platform.

### Other modules

| Module | [Windows](../technology-support.md#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](../../../ru/ingest-from/technology-support/mainframe-technology-support.md "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OS module[1](#fn-3-1-def) |  |  | n/a |  |  |  |  |  |  |
| Network module |  |  | n/a |  |  |  |  |  |  |
| Log module |  |  | n/a |  | [2](#fn-3-2-def) |  |  |  |  |
| JMX extensions |  |  |  |  |  |  |  |  |  |
| Extensions |  |  |  |  |  |  |  |  |  |
| Live Debugger [3](#fn-3-3-def) |  |  |  |  |  |  |  |  | n/a |

1

OS module is required for out-of-the-box infrastructure alerting capabilities.

2

Log module support is limited to custom log sources, no log auto-detection is performed.

3

Supported for Java versions 8-23. Node.js version 22 is supported starting OneAgent version 1.313+.

### Features

| Feature | [Windows](../technology-support.md#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](../technology-support.md#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](../../../ru/ingest-from/technology-support/mainframe-technology-support.md "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Auto-update of all modules |  |  | n/a |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) of code modules |  |  |  |  | n/a[1](#fn-4-1-def) |  |  |  |  |
| [Universal injection](#universal-injection) of code modules |  |  |  |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) for containers |  |  | n/a |  |  |  |  |  |  |
| Non-privileged |  |  | n/a |  |  |  |  |  | n/a |

1

Global auto-injection isn't possible for AIX. Instead, use the [universal injection](#universal-injection) approach, as described on the [AIX OneAgent installation page](../../../ru/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix.md "Learn how to download and install Dynatrace OneAgent on AIX.").

## Enterprise cloud platforms

The tables below contain information about the supported OneAgent capabilities for various supported Cloud platforms.

Cloud Foundry application-only also applies to [SAP Cloud](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring.md "Install OneAgent on SAP Business Technology Platform.").

OneAgent deployment via container (OneAgent Operator) on OpenShift and Kubernetes has some [limitations](#agent-container) compared to standard OneAgent installation.

### Code modules

| Code module[1](#fn-5-1-def) | [Cloud Foundry](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.") | [OpenShift](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](../../../ru/ingest-from/technology-support/application-software/java.md "Learn about all aspects of Dynatrace support for Java application monitoring.") |  |  |  |  |  |  |  |
| [.NET and .NET Core](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) | [1](#fn-5-1-def) |
| [.NET Framework](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  | n/a | n/a | n/a | n/a | n/a |  |
| [Node.js](../../../ru/ingest-from/technology-support/application-software/nodejs.md "Read about Dynatrace support for Node.js applications.") |  |  |  |  |  |  |  |
| [Python](application-software/python.md "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.") | n/a | n/a |  |  |  |  | n/a |
| PHP |  |  |  |  |  |  |  |
| [Go](../../../ru/ingest-from/technology-support/application-software/go.md "Read an overview of Dynatrace support for Go applications.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) |  |
| Apache, IHS |  |  |  |  |  |  | [2](#fn-5-2-def) |
| NGINX |  |  |  |  |  |  | [2](#fn-5-2-def) |

1

Out-of-the-box infrastructure alerting capabilities are not supported for application-only code modules.

2

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### OneAgent SDK

| OneAgent SDK | [Cloud Foundry](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.") | [OpenShift](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  |  |  |  |  |
| OneAgent SDK for Python |  |  |  |  |  |  |  |

### Other modules

| Module | [Cloud Foundry](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.") | [OpenShift](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OS module |  | n/a |  | n/a |  | n/a |  |
| Network module |  | n/a |  | n/a |  | n/a |  |
| Log module |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  |
| Extension module |  | n/a | n/a | n/a | n/a | n/a |  |
| Live Debugger |  |  |  |  |  |  |  |

1

This is supported via the [FluentD integration](../../../ru/analyze-explore-automate/log-monitoring/acquire-log-data.md "Learn how to acquire log data in Dynatrace Log Monitoring.") available in Dynatrace

### Features

| Feature | [Cloud Foundry](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.") | [OpenShift](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](../setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Auto-update of all modules |  | n/a |  | n/a |  | n/a |  |
| [Auto-injection](#auto-injection) of code modules |  | n/a |  | n/a |  | n/a |  |
| [Universal injection](#universal-injection) of code modules |  |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) for containers |  | n/a |  | n/a |  | n/a |  |
| Non-privileged | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Cloud application platforms

The tables below contain information about the supported OneAgent capabilities for supported Cloud application platforms.

### Code modules

| Code module | AWS Lambda | [Azure Functions](../../../ru/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions.md "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | [Azure Spring Apps](../../../ru/ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md "Learn how to configure OneAgent for monitoring Azure Spring Apps.") | [Azure App services](../../../ru/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring.md "Monitor Azure with Dynatrace") | [Heroku](../setup-on-container-platforms/heroku.md "Install OneAgent to monitor applications running on Heroku.") | [Google App Engine](../../../ru/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md "Install OneAgent on Google App Engine clusters for application-only monitoring.") | [AWS Fargate](../../../ru/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md "Install OneAgent on AWS Fargate.") | [Google Cloud Run Managed](../../../ru/ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md "Monitor Java application deployed on Google Cloud Run managed.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](../../../ru/ingest-from/technology-support/application-software/java.md "Learn about all aspects of Dynatrace support for Java application monitoring.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| [.NET and .NET Core](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  |  |  | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| [.NET Framework](../../../ru/ingest-from/technology-support/application-software/dotnet.md "Learn about all aspects of Dynatrace support for .NET application monitoring.") | n/a |  |  |  | n/a | n/a | n/a |  |
| [Node.js](../../../ru/ingest-from/technology-support/application-software/nodejs.md "Read about Dynatrace support for Node.js applications.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| Python | [1](#fn-7-1-def) |  |  |  |  |  |  |  |
| PHP |  |  |  |  |  |  |  |  |
| [Go](../../../ru/ingest-from/technology-support/application-software/go.md "Read an overview of Dynatrace support for Go applications.") |  | n/a |  | n/a | [3](#fn-7-3-def) | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| Microsoft IIS | n/a | n/a |  |  |  |  |  |  |

1

Both 64-bit ARM ([AWS Graviton2 processorsï»¿](https://aws.amazon.com/ec2/graviton/)) and 64-bit x86 architectures are supported.

2

Both Google Cloud Run execution environments are supported, with some restrictions.

3

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### Features

| Feature | AWS Lambda | [Azure Functions](../../../ru/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions.md "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | [Azure Spring Apps](../../../ru/ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md "Learn how to configure OneAgent for monitoring Azure Spring Apps.") | [Azure App services](../../../ru/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring.md "Monitor Azure with Dynatrace") | [Heroku](../setup-on-container-platforms/heroku.md "Install OneAgent to monitor applications running on Heroku.") | [Google App Engine](../../../ru/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md "Install OneAgent on Google App Engine clusters for application-only monitoring.") | [AWS Fargate](../../../ru/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md "Install OneAgent on AWS Fargate.") |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Universal injection](#universal-injection) of code modules | n/a |  | n/a |  |  |  |  |

## Auto-injection of code modules

Auto-injection automatically injects code modules into monitored applications in a completely transparent and automatic fashion that requires no manual configuration or intervention. This approach to deep monitoring is supported for Windows (Docker only) and Linux. Among other things, auto-injection also automatically injects code modules into Docker, containerd, CRI-O, and Cloud Foundry Garden containers. This means that you don't have to change any container images on monitored platforms to gain full insights.

## Universal injection of code modules

Universal injection allows Dynatrace to inject code modules into applications in a unified way across multiple platforms, in situations where auto-injection isn't available. This applies to AIX and Solaris as well as to Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate, and AWS App Runner.

The feature is described on the [AIX](../../../ru/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix.md "Learn how to download and install Dynatrace OneAgent on AIX.")/[Solaris](../../../ru/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris.md "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") OneAgent installation page. It is also part of the [OpenShift application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")/[Kubernetes application-only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integration and the container platforms [Google App Engine](../../../ru/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md "Install OneAgent on Google App Engine clusters for application-only monitoring.") and [AWS Fargate](../../../ru/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md "Install OneAgent on AWS Fargate.").

Outside of these specific use cases, this feature isn't to be used directly!

The [Cloud Foundry buildpack](../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.") integrations and [Dynatrace Heroku](../setup-on-container-platforms/heroku.md "Install OneAgent to monitor applications running on Heroku.") buildpack use this transparently under the hood without any need for manual intervention or configuration.

Any form of undocumented injection (for example, older forms of manual injection) aren't supported.

## Alpine Linux (musl libc) based containers

Dynatrace supports [Alpine Linux (musl libc) based containers](../technology-support.md#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") on monitored Linux x86\_64 hosts. This includes OpenShift, Kubernetes and Cloud Foundry installations and all forms of Docker environments. In these environments Dynatrace OneAgent [automatically injects](#auto-injection) the code modules into the applications running inside the container.

Alpine Linux is also supported in [OpenShift application only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") and [Kubernetes application only](../../../ru/ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integrations as well as when pushing Docker images to Cloud Foundry and Heroku. This happens via the [universal injection](#universal-injection).

Dynatrace OneAgent doesn't support direct installation in Alpine based Linux systems.

Dynatrace OneAgent doesn't support monitoring binaries built against GNU C Library (glibc) running on Alpine based Linux systems using a GNU C Library (glibc) compatibility package like gcompat (GNU C Library compatibility layer for musl) or libc6-compat (compatibility libraries for glibc).

## OneAgent deployment via Dynatrace Operator

Dynatrace Operator deploys the OneAgent to Kubernetes or OpenShift clusters through a containerized approach. There are some [limitations](../setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md "Install and update Dynatrace OneAgent as a Docker container.") associated with deploying OneAgent via Dynatrace Operator. These include:

* The auto-update mechanism of modules is disabled for container rollouts. However, Dynatrace Operator ensures the restart of OneAgent pods to receive OneAgent updates.
* Auto-injection of code-modules is disabled for native (i.e., non-containerized) processes.
* JMX extensions aren't supported for technologies outside of containers

For a detailed overview of limitations, see [Set up Dynatrace OneAgent as a Docker container](../setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md "Install and update Dynatrace OneAgent as a Docker container.").

## Related topics

* [Technology support](../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](../../../ru/ingest-from/technology-support/known-solutions-and-workarounds.md "Check the solutions for reported problems regarding various technologies.")
