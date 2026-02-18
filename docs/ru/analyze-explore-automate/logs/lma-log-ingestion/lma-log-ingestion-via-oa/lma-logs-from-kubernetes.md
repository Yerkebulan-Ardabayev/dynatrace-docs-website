---
title: Stream Kubernetes logs with Dynatrace Log Module
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes
scraped: 2026-02-18T05:46:18.356272
---

# Stream Kubernetes logs with Dynatrace Log Module

# Stream Kubernetes logs with Dynatrace Log Module

* Latest Dynatrace
* Tutorial
* 13-min read
* Updated on Oct 08, 2025

Dynatrace provides integrated Log management and analytics for your Kubernetes environments. We recommend collecting logs in Kubernetes using our fully managed [Dynatrace Log module](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace."), either integrated in the OneAgent deployed on the node (OneAgent Log module) or without OneAgent as a standalone deployment (Kubernetes Log module). Dynatrace Operator configures and manages the Dynatrace Log module for both approaches. Alternatively, you can stream logs to Dynatrace using log collectors such as [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace."), [Dynatrace OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), or [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.").

On this page you learn advanced configuration of our OneAgent Log module and Kubernetes Log module to ingest logs from Kubernetes. To learn about the different **deployment options, supported platforms, and runtimes**, see the [Kubernetes log monitoring](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.") page.

## Auto-discovery of Kubernetes container logs

The Dynatrace Log module automatically discovers logs written to the **stdout/stderr** streams through containerized applications running in pods. Under the covers, these log streams are stored as files on the Kubernetes nodes, where the Dynatrace Log module can pick those files up and stream them to Dynatrace. The `log source` attribute for these logs in Dynatrace is set to `Container Output`. The attribute `log.iostream` defines the log stream the log entries were written to, for example, stdout or stderr.

The Dynatrace Log module does not discover logs written to the container filesystem (as opposed to stdout/stderr). In this case, you can use a log shipper to read the logs from the container filesystem and write them to stdout/stderr for the Dynatrace Log module to pick them up.

For the OneAgent Log module, we recommend to review the [Collect all containers logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-feature-flags#collect-all-container-logs "Enable or disable specific functionalities of the OneAgent log module and the Dynatrace log module for Kubernetes.") feature flag within your settings to ensure best coverage of your logs within Kubernetes. The Kubernetes Log module always collects all container logs.

## Log enrichment with Kubernetes metadata

Dynatrace Log module decorates the ingested logs with the following Kubernetes metadata: `k8s.cluster.name`, `k8s.cluster.uid`, `k8s.namespace.name`, `k8s.workload.name`, `k8s.workload.kind`, `dt.entity.kubernetes_cluster`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `dt.entity.kubernetes_node`.

Also, any pod annotations starting with the `metadata.dynatrace.com/` prefix are added to the log records.

Additionally, you can use existing Kubernetes annotations and labels to enrich your logs. See [metadata enrichment for Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes") to learn more.

## Control log ingest with Kubernetes metadata

You can control logs from Kubernetes ingestion with log ingest rules in Dynatrace. You can configure these rules at the Kubernetes cluster level to allow cluster-specific log ingestion. The rules use matchers for Kubernetes metadata and other common log entry attributes to determine which logs are to be ingested.
Standard log processing features from OneAgent, including [sensitive data masking](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics."), [timestamp configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record."), [log boundary definition](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-entry-boundary "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record."), and [automatic enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") of log records, are also available and enabled here.

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

Log record level attribute, transformed by Dynatrace Log Module, is different than the log `status` attribute transformed by the Dynatrace server. Learn more by accessing the [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") page.

### Log ingest rule hierarchy

Log ingest rules can be defined on environment scope but also on more fine-grained level like Kubernetes cluster. The matching hierarchy is as follows:

1. Host configuration rules;
2. Kubernetes cluster configuration rules;
3. Host group configuration rules;
4. Environment configuration rules.

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent.

To prevent the unintended ingestion of all logs due to the **Ingest all** rule enabled at the environment level, we recommend adding an **Exclude everything** rule at the end of the cluster scope configuration. This ensures that any unmatched logs are explicitly excluded. Without this, the log ingest rules defined at the environment scope will be further evaluated by the Dynatrace Log module, and logs will be ingested if the conditions are matched.

Consult the [Configuration scopes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#configuration-scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") for the three scopes of the configuration hierarchy.

## Use cases



Explore the following use cases for log ingestion from Kubernetes environments using Dynatrace. By configuring log ingestion with different matchers, you can control which logs are captured in the system. The use cases below offer guidance on configuring Dynatrace to capture logs based on your specific monitoring needs, whether it's from a particular namespace, container, or other criteria.

For detailed instructions on how to configure log ingestion, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

### Ingest all logs from a specific namespace

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest logs from a specific namespace and container

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Select the namespace from the dropdown inside the **Value** field, and select **Add matcher**.
6. Add a new matcher, this time, select **K8s container name**, and input the container name in the **Value** field. You can add multiple container names in this configuration step.
7. Select **Save changes**.

You can now analyze the logs in the log viewer or notebooks after fitering the proper namespace and container. You can also find the logs in context in the Kubernetes application by selecting the **Logs** tab.

### Ingest all Kubernetes logs excluding specific namespaces

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
3. Select **Add condition**.
4. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
5. Insert asterisk (\*) in the **Value** field, as a placeholder for all available namespaces of the cluster.
6. Select **Add matcher**.
7. Select **Save changes**.
8. Back in the **Log ingest** rules screen, add one more rule, and select the **Exclude from storage** option.
9. In the **Value** field, add the namespaces that you want to exclude when ingesting Kubernetes logs.
10. Select **Add matcher**.
11. Select **Save changes**.

### Ingest error logs from a given Kubernetes cluster and namespace

1. Go to the **Kubernetes** application and select **Clusters**.
2. Select the cluster that you'd like to configure.
3. Go to  > **Connection settings** > **Log Monitoring** > **Log ingest rules**.
4. Select **Add rule** and provide the name for your configuration in the **Rule name** field.  
   Make sure that the **Include in storage** button is turned on, so logs matching this configuration will be stored in Dynatrace.
5. Select **Add condition**.
6. From the **Matcher attribute** dropdown, select **Kubernetes namespace name**.
7. Select one or multiple namespaces from the dropdown inside the **Value** field. You can input an asterisk (\*) in as a placeholder for all available namespaces of the cluster.
8. Select **Add matcher**.
9. Add one more matcher, and set the **Matcher attribute** as **Log record level**.
10. From the **Value** field dropdown, select **Error**.
11. Select **Add matcher**.
12. Select **Save changes**.

On the **Log ingest rules** screen, arrange the configured rules to prioritize the excluded namespaces rule at the top and the rule including all namespaces at the bottom.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema;
* List stored configuration objects;
* View single configuration object;
* Create new, edit, or remove existing configuration object.

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rule objects can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given environment.
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

To learn more about log ingestion please consult the [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#faq "Include and exclude specific log sources already known to OneAgent for storage and analysis.") page.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)