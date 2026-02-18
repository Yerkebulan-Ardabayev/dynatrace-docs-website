---
title: Log Monitoring in Kubernetes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes
scraped: 2026-02-18T21:34:10.252601
---

# Log Monitoring in Kubernetes (Logs Classic)

# Log Monitoring in Kubernetes (Logs Classic)

* Tutorial
* 10-min read
* Updated on Oct 08, 2025

Log Monitoring Classic

For the newest Dynatrace version, see [Stream Kubernetes logs with Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.").

Dynatrace Log Monitoring supports collecting logs from Kubernetes container orchestration systems via OneAgent.

As an alternative to OneAgent-based log collection, you can stream logs to Dynatrace via the [logs ingest API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.") with an integration such as [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), or [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.").

## Supported features

Dynatrace Log Monitoring supports various Kubernetes-based container platforms like Upstream Kubernetes or Red Hat OpenShift using **containerd**, or **CRI-O** as container runtime.

**Docker** isnât compliant with CRI, the Container Runtime Interface. For this reason, Kubernetes setups using **Docker** are only partially supported. Kubernetes deprecated **Docker** as a container runtime after v1.20.

For more details regarding supported versions of Kubernetes, check [Dynatrace Operator support and known issues](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

## Auto-discovery of Kubernetes logs

OneAgent autodiscovers logs written by the containerized application to its **stdout**/**stderr** streams. Kubernetes Engine saves these log streams to a file on the Kubernetes node. OneAgent autodiscovers these log files, and reports the container logs under the `Container Output` log source.

Logs written directly to the pods filesystem are not discovered by OneAgent. In this case, use a log shipper integration, such as Fluent Bit.

## Log enrichment with Kubernetes metadata

OneAgent Log module decorates the ingested logs with the following Kubernetes metadata: `k8s.cluster.name`, `k8s.cluster.uid`, `k8s.namespace.name`, `k8s.workload.name`, `k8s.workload.kind`, `dt.entity.kubernetes_cluster`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `dt.entity.kubernetes_node`. This metadata is used to map the logs to the entity model of Kubernetes clusters, namespaces, workloads, and pods.

Also, any pod annotations starting with the `metadata.dynatrace.com/` prefix are added to the log records.

See [metadata enrichment for Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes") to learn more.

### Control log ingest with Kubernetes metadata

You can control logs from Kubernetes ingestion with log ingest rules in Dynatrace. You can configure these rules at the Kubernetes cluster level to allow cluster-specific log ingestion. The rules use matchers for Kubernetes metadata and other common log entry attributes to determine which logs are to be ingested.
Standard log processing features from OneAgent, including [sensitive data masking](/docs/analyze-explore-automate/log-monitoring/methods-of-masking-sensitive-data "Choose the optimal method to mask your sensitive data."), [timestamp configuration](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration "Define log monitoring rules that control log data timestamps."), and [automatic enrichment](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") of log records, are also available and enabled here.

Use the following recommended matching attributes when configuring log ingestion from Kubernetes.

Attribute

Description

Search dropdown logic

**Kubernetes namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**Kubernetes container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**Kubernetes deployment name**

Matching is based on the name of the Kubernetes workload.[1](#fn-1-1-def)

Attributes visible in the last 90 days are listed.

**Kubernetes pod annotation**

Matching is based on any of the selected pod annotations. The correct format is `key=value`.

Can be entered manually.

**Kubernetes pod label**

Matching is based on any of the selected pod labels. The correct format is `key=value`.

Can be entered manually.

**Kubernetes workload name**

Matching is based on any of the selected workload names.

Can be entered manually.

**Kubernetes workload kind**

Matching is based on any of the selected workload kinds.

Can be entered manually.

**Log content**

Matching is based on the content of the log; wildcards are supported in the form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[2](#fn-1-2-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**Log source origin**

Matching is based on the detector was used by OneAgent to discover the log file.

Can be entered manually. No time limit.

**Process group**

Matching is based on the process group ID. It also requires running a OneAgent on the node.

Entities visible in the last 3 days are listed.

**Process technology**

Matching is based on the technology name. It also requires running a OneAgent on the node.

Can be entered manually. No time limit.

**DT entity container group ID**

Matching is based on any of the selected container groups. It also requires running a OneAgent on the node.

Can be entered manually. No time limit.

1

Subject to change in the future versions of OneAgent. Separate matchers for each workload kind would be available. We recommend using the Kubernetes workload name and Kubernetes workload kind instead.

2

Log record level attribute, transformed by OneAgent Log Module, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

## Configure log ingest from Kubernetes



Ingesting logs from Kubernetes requires log ingest rules definition. The configuration is based on a hierarchy of rules that use matchers for Kubernetes and other common log entry attributes. These rules determine which log files, among those detected by OneAgent are ingested.

Use the following recommended matching attributes when configuring log ingestion from Kubernetes.

Attribute

Description

Search dropdown logic

**K8s namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**K8s container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**K8s deployment name**

Matching is based on the name of the Kubernetes pod.

Subject to change in the future versions of log agent. Separate matchers for each workload kind would be available. We recommend using the K8s container name instead.

Attributes visible in the last 90 days are listed.

**Log content**

Matching is based on the content of the log; wildcards are supported in the form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[1](#fn-2-1-def)[2](#fn-2-2-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

1

Log record level attribute, transformed by OneAgent, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

2

The minimum required OneAgent version is 1.273.

You can also use the following general matching attributes when configuring log ingestion from Kubernetes.

Attribute

Description

Search dropdown logic

**Container name**

Matching is based on the name of the container. It is used for non-orchestrated container environments, for example Docker.

Attributes visible in the last 90 days are listed.

**Log source**

Matching is based on a **Log source** attribute. In case of Kubernetes logs, it is always set to **Container Output**; wildcards are supported in form of an asterisk.

Can be entered manually. No time limit.

**Process group**

Matching is based on the process group ID.

Entities visible in the last 3 days are listed.

**Process technology**

Matching is based on the technology name.

Can be entered manually. No time limit.

### Log ingest rule hierarchy

Log ingest rules can be defined on environment scope but also on host or host group. The matching hierarchy is as follows:

1. Host configuration rules;
2. Host group configuration rules;
3. Tenant configuration rules.

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent.

Consult the [Configuration scopes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#configuration-scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") for the four scopes of the configuration hierarchy.

## Use cases

Explore the following use cases for log ingestion from Kubernetes environments using Dynatrace. By configuring log ingestion with different matchers, you can control which logs are captured in the system. The use cases below offer guidance on configuring Dynatrace to capture logs based on your specific monitoring needs, whether it's from a particular namespace, container, or other criteria.

### Ingest all logs from a specific namespace

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **K8s namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest logs from a specific namespace and container

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **K8s namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Add a new matcher, this time, select **K8s container name**, and input the container name in the **Value** field. You can add multiple container names in this configuration step.
7. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace and container. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest all Kubernetes logs excluding specific namespaces

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **K8s namespace name**.
5. Insert asterisk (\*) in the **Value** field, as a placeholder for all available namespaces of the cluster.
6. Select **Add matcher**.
7. Select **Save changes**.
8. Back in the **Log ingest** rules screen, add one more rule, and select the **Exclude from storage** option.
9. In the **Value** field, add the namespaces that you want to exclude when ingesting Kubernetes logs.
10. Select **Add matcher**.
11. Select **Save changes**.

On the **Log ingest rules** screen, arrange the configured rules to prioritize the excluded namespaces rule at the top and the rule including all namespaces at the bottom.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema;
* List stored configuration objects;
* View single configuration object;
* Create new, edit, or remove existing configuration object.

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rule objects can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given tenant.
* `host_group` â configuration object affects all hosts assigned to a given host group.
* `host` â configuration object affects only the given host.

To create a log ingest rule using the API:

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) scopes.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The log ingest rules schema identifier (`schemaId`) is `builtin:logmonitoring.log-storage-settings`. Here is an example JSON payload with the log ingest rules:

   ```
   {



   "items": [



   {



   "objectId": "vu9U3hXa3q0AAAABACpidWlsdGluOmxvZ21vbml0b3JpbmcubG9nLXN0b3JhZ2Utc2V0dGluZ3MABEhPU1QAEEFEMDVFRDZGQUUxNjQ2MjMAJDZkZGU3YzY5LTMzZjEtMzNiZC05ZTAwLWZlNDFmMjUxNzUzY77vVN4V2t6t",



   "value": {



   "enabled": true,



   "config-item-title": "Send kube-system logs",



   "send-to-storage": true,



   "matchers": [



   {



   "attribute": "k8s.container.name",



   "operator": "MATCHES",



   "values": [



   "kubedns",



   "kube-proxy"



   ]



   },



   {



   "attribute": "k8s.namespace.name",



   "operator": "MATCHES",



   "values": [



   "kube-system"



   ]



   }



   ]



   }



   }



   ],



   "totalCount": 1,



   "pageSize": 100



   }
   ```

## Examples

The examples that follow show the results of various combinations of rules and matchers.

### Example 1: Ingest all logs from a specific namespace

This task requires setting one rule with one matcher.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "tenant",



"value": {



"enabled": true,



"config-item-title": "All logs from kube-system namespace",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



}



]



}



}]
```

### Example 2: Send logs from a specific namespace and containers with content containing 'ERROR'



This task requires setting one rule with three matchers.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "tenant",



"value": {



"enabled": true,



"config-item-title": "Error logs from kube-proxy and kube-dns containers",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



},



{



"attribute": "k8s.container.name",



"operator": "MATCHES",



"values": [



"kubedns",



"kube-proxy"



]



},



{



"attribute": "log.content",



"operator": "MATCHES",



"values": [



"*ERROR*"



]



}



]



}



}]
```

### Example 3: Ingest all Kubernetes logs excluding specific namespaces on a specific host group scope

This task requires setting two rules.

```
[{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "HOST_GROUP-1D91E46493049D07",



"value": {



"enabled": true,



"config-item-title": "Exclude logs from kube-system namespace",



"send-to-storage": false,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"kube-system"



]



}



]



}



},{



"schemaId": "builtin:logmonitoring.log-storage-settings",



"scope": "HOST_GROUP-1D91E46493049D07",



"value": {



"enabled": true,



"config-item-title": "All Kubernetes logs",



"send-to-storage": true,



"matchers": [



{



"attribute": "k8s.namespace.name",



"operator": "MATCHES",



"values": [



"*"



]



}



]



}



}]
```

## FAQ

What are prerequisites for autodiscovery and ingestion of Kubernetes logs via OneAgent?

The requirements for autodiscovery and ingestion of Kubernetes logs are the following:

* The **containerd**, or **CRI-O** container runtime is used;
* The process running in the container is an [important process](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.");
* Logs are written to the container's **stdout**/**stderr** streams;
* The log file on the Kubernetes node exists for a minimum of one minute after container execution is finished.

Is it possible to decorate logs with Kubernetes labels and annotations?

No, OneAgent doesn't offer such a functionality yet, although it is planned in future releases.

For more ingest related FAQ, please consult the [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#faq "Include and exclude specific log sources already known to OneAgent for storage and analysis.") page.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)