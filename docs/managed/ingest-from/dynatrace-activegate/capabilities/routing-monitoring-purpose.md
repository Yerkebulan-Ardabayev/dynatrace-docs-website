---
title: Route OneAgent traffic to Dynatrace, monitor cloud environments and remote technologies using extensions
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose
scraped: 2026-05-12T11:36:18.837695
---

# Route OneAgent traffic to Dynatrace, monitor cloud environments and remote technologies using extensions

# Route OneAgent traffic to Dynatrace, monitor cloud environments and remote technologies using extensions

* 6-min read
* Published Nov 09, 2018

The functionality offered by these types of ActiveGates depends on the functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") that are currently installed or configured.

## Route OneAgent traffic

A Dynatrace ActiveGate establishes Dynatrace presenceâa Dynatrace componentâin your local network. In this way Dynatrace ActiveGate allows you to reduce your interaction with Dynatrace to one single pointâavailable locally.
Besides convenience, this solution also optimizes traffic volume and reduces the complexity of network connections, and consequently reduces cost. It also ensures the security of sealed networks.

### Message routing functionality and modules

#### Message Routing

(module: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
ActiveGate knows about the runtime structure of your Dynatrace environment and routes messages from OneAgent instances to the correct server endpoints.

#### Buffering and compression

(module: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
ActiveGate collects messages from OneAgent instances and builds bulks, which are then sent in compressed form to Dynatrace Servers. This can reduce network overhead considerably, depending on the number of OneAgent instances communicating with the ActiveGate and on the amount of data transferred by them.

#### Authentication

(module: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
ActiveGate authenticates OneAgent requests (SSL handshake and environment ID authentication).

#### Accessing sealed networks

(module: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
In case OneAgents don't have access to the internet, you should install an ActiveGate to serve as a single access point, rather than opening the firewall for multiple hosts running OneAgents. This approach greatly reduces the effort of managing and maintaining firewall and/or proxy configuration settings.

### Memory dumps

Memory dumps come from OneAgents and thus can be considered a part of the routing functionality of ActiveGate.

#### Memory dumps

(module: [Memory dumps](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#mem_dump_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Dynatrace supports both automatic and manual capture and analysis of [memory dumps](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.") on monitored hosts. Memory dumps need to be stored in a centralized location for download and analysis. Since such dumps are often large and can contain sensitive data, Dynatrace doesn't allow you to upload dumps to the Dynatrace cluster in the cloud. Instead you should set up an ActiveGate and configure it to serve as a host for memory dumps. The Dynatrace UI provides you with download URLs for the ActiveGate REST API that serves the dumps.

## Monitor cloud environments and remote technologies

#### AWS monitoring

(module: [AWS](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#aws-monitoring "Learn which ActiveGate properties you can configure based on your needs and requirements."))
[AWS service monitoring](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Monitor AWS with Dynatrace") is a resource-intensive task. Therefore, to monitor more than 2,000 AWS resources, you must install an ActiveGate and configure AWS monitoring.

#### Cloud Foundry monitoring

(module: [Cloud Foundry](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#cf_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
To connect your Cloud Foundry foundations to Dynatrace, you're required to install an ActiveGate instance to complement Cloud Foundry process- and host-level metrics collected by Dynatrace OneAgent with additional metadata and metrics pulled from the Cloud Foundry API. This integration allows you to use the [Cloud Foundry overview page](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Available metrics for monitoring your Cloud Foundry clusters with Dynatrace") as well as the automatic detection of your Cloud Foundry organizations in addition to other Cloud Foundry process properties like `space`, `space ID`, `application`, `application ID`, and `instance index`.

#### Kubernetes/OpenShift monitoring

Environment ActiveGates only

(module: [Kubernetes](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#k8s_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
To connect your Kubernetes/OpenShift clusters to Dynatrace to take advantage of the dedicated [Kubernetes/OpenShift overview page](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes "Monitor the health and utilization of your Kubernetes/OpenShift cluster resources."), you need to run an ActiveGate in your environment.

#### Azure monitoring

(module: [Azure](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
To integrate [Azure monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") data, a dedicated ActiveGate is required to poll metadata and metrics from Azure APIs. This integration enables monitoring of Azure Services (especially for cloud services where we can't install OneAgent) and also monitoring through the Dynatrace UI.

#### Monitoring using an ActiveGate extension

Environment ActiveGates only

(module: [Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))  
With [ActiveGate extensions](/managed/ingest-from/extend-dynatrace "Learn what extension mechanisms are offered by Dynatrace."), you can extend Dynatrace monitoring to any remote technology that exposes an interface, where OneAgent installation is not an option. For example, PaaS technologies, network devices, or cloud technologies. ActiveGate extensions (aka remote plugins) are executed on ActiveGates and can acquire metrics and topology information from remote sources, thereby fully integrating remote technology monitoring into Dynatrace Smartscape and problem detection.

#### Oracle database insights

(module: [Database insights](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#oracle_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
[Database insights](/managed/observe/infrastructure-observability/databases/database-services-classic/database-insights "Learn how to extend your database monitoring to the database infrastructure layer.") adds an infrastructure perspective to your database monitoring. With additional data fetched from the database layer, you are able to resolve performance problems that are rooted deep in the database.

#### Monitoring virtualized infrastructure

(module: [VMware](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#vmware "Learn which ActiveGate properties you can configure based on your needs and requirements."))
An ActiveGate can poll your [vCenter or standalone ESXi hosts](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.") to obtain information about all important resources that ESXi servers provision to your virtual machines (for example, CPU usage, memory consumption, and data-store related activity on your VMware platform). To acquire this information, Dynatrace needs a component installed in your environment that has access to the vCenter API.

## Dynatrace API

Dynatrace ActiveGate provides endpoints for accessing [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API."). The types of API calls listed below are handled or pre-processed on the ActiveGate, before involving the Dynatrace Cluster. Other API calls are forwarded directly to the Dynatrace Cluster.  
ActiveGate supports calls to all the endpoints of the v1 as well as v2 versions of the Dynatrace Configuration and Environment APIs.

#### Log Monitoring

(module: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."))
With [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") as a part of the Dynatrace platform, you gain direct access to the log content of all your mission-critical processes. You can create custom log metrics for smarter and faster troubleshooting. You will be able to understand log data in the context of your full stack, including real user impacts.

#### Metric ingestion

(module: [HTTP Metric API](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#metric_api_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
[Metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") provides you a with a simple way to push any custom metrics to Dynatrace. You can further refine your metrics into categories.

#### OpenTelemetry trace ingestion

(module: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
You can send [OpenTelemetry trace data](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (traces and spans) in OTLP format to Dynatrace via an API available on Dynatrace ActiveGate. The ingested spans are integrated into PurePathÂ® distributed traces.

#### OpenTelemetry metric ingestion

(module: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
You can send [OpenTelemetry metric data](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") in OTLP format to Dynatrace via an API available on Dynatrace ActiveGate.

#### OpenTelemetry log ingestion

(module: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."))
You can send [OpenTelemetry log data](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") in OTLP format to Dynatrace via an API available on Dynatrace ActiveGate.

#### Real User Monitoring

(module: [Beacon forwarder](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#bf_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Dynatrace infrastructure can be used as the default [beacon endpoint for the agentless monitoring of your applications](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Auto-injected applications send the beacon back to the customer's web server, bypassing the need for a third-party domain. However, when required, such applications can also use the Dynatrace infrastructure as an endpoint for RUM monitoring signals.