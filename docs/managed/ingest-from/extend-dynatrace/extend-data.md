---
title: Enrich ingested data with Dynatrace-specific fields
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-data
---

# Enrich ingested data with Dynatrace-specific fields

# Enrich ingested data with Dynatrace-specific fields

* Reference
* 5-min read
* Updated on Oct 02, 2026

Unlike automatic ingestion using OneAgent, data sent directly to an ActiveGate (for example, ingest APIs) is not automatically enriched with host-related information. This may incur additional charges, as it would not take into account possibly included [DDU quotas](/managed/license/classic-licensing/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

The different Dynatrace deployment options provide several Java-style properties and JSON files with sets of attributes that you can use to enrich your requests to Dynatrace and ensure Dynatrace can map the data to your infrastructure.

## Enrichment directory

Dynatrace uses the following directories to provide `.json` and `.properties` files with enrichment data:

* On Unix: `/var/lib/dynatrace/enrichment`
* On Windows: `%ProgramData%\dynatrace\enrichment`

## Dynatrace OneAgent

A standard OneAgent setup provides the following files with host-specific details in the [enrichment directory](#enrichment-directory):

* `dt_host_metadata.json`
* `dt_host_metadata.properties`

Both files contain the same collection of host-level resource attributes that OneAgent uses to enrich monitoring artifacts for a given host. This also includes key-value tags and properties set via [oneagentctl](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Automate host tags and metadata with oneagentctl or configuration files, and use the resulting properties in auto-tagging and management-zone rules.") or through [Remote configuration management](/managed/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.").

If you supply telemetry data via different channels than OneAgent (for example, using OpenTelemetry), it is important you enrich your telemetry data manually with these attributes to ensure the proper host association.

For more information, see [Host-level resource attributes](/managed/ingest-from/dynatrace-oneagent/resource-attributes "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

For an example of how to load the JSON file, see the [Python example](#python-example) below.

### OneAgent virtual files

When OneAgent is monitoring your application, your application is also able to access the following virtual files:

* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

These files are not specific to the enrichment directory and do not physically exists in your file system, but are provided by the OneAgent instrumentation. Both files return the same data and the file extension (`.json`/`.properties`) only determines the output format.

In the context of [Dynatrace Operator](#operator-enrichment-directory), the virtual file also contains the attributes of the `dt_metadata.{json,properties}` files.

#### How to access the virtual files

1. Use the standard file read function of your language platform to open and read one of these files:

   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

   The file extension you choose is relevant for step 4. Only use the filename and do not specify an additional path.
2. The content of the file is a single text line with an absolute file path (consider it an ephemeral value and do not store, persist, or cache that path for later use).
3. Open the file at the path location obtained in the previous step and read its entire content.
4. The content format received from the previous read will match the file extension you chose in step 1 (Java-style properties or JSON).

If step 1 returns a file-not-found error, verify that your application is instrumented by OneAgent.

#### Limitations

* Supported for full-stack and application-only deep-monitored processes.
* The `stat` and other `if (exists)` checks fail for these files. These checks are not required for the mechanism to work.
* `syscalls` used directly for file access aren't supported. This also means that the Go-based applications used for metric ingestion aren't supported unless you use the OneAgent SDK as explained in [Instrument your Go application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/go "Learn how to instrument your Go application using OpenTelemetry and Dynatrace.").

### Python example

The following example shows how to load the enrichment information as JSON in Python on Unix.

```
# Initialize dictionary variable



enrich_attrs = dict()



# Iterate over the potential data files and try reading them



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json", "/var/lib/dynatrace/enrichment/dt_host_metadata.json"]:



try:



data = ''



with open(name) as f:



data = json.load(f if name.startswith("/var") else open(f.read()))



enrich_attrs.update(data)



except:



pass # An exception indicates the file was not available



# Use enrich_attrs here to enrich your requests to Dynatrace.



# For example, when instrumenting with OpenTelemetry, add the data as resource attributes.
```

The example code initializes an empty dictionary for the imported attributes. It then iterates over an array of `.json` filenames and loads the content of each file as JSON document, adding the keys to the dictionary. File exceptions indicate the particular file is not available and are ignored.

## Dynatrace Operator

When `metadataEnrichment` is enabled in your DynaKube, the Dynatrace Operator injects the following files into the [enrichment directory](#enrichment-directory) of each pod:

* `dt_metadata.json`
* `dt_metadata.properties`

Both files contain the same Kubernetes metadata in different formats. For an example of how to load the JSON file, see the [Python example](#python-example) above. With OneAgent enabled, these files are applied automatically; without OneAgent, load and apply them manually.

The resource attributes you declare in your DynaKube also land in these files. See [Set resource attributes in the DynaKube](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment#resource-attributes "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.").

`metadataEnrichment` is automatically enabled — no explicit DynaKube configuration required — when using [OneAgent injection](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") (`cloudNativeFullStack` or `applicationMonitoring`) or [OTLP exporter auto-configuration](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

Enable metadataEnrichment in your DynaKube

Add `metadataEnrichment` to your DynaKube spec:

```
spec:



metadataEnrichment:



enabled: true
```

To limit enrichment to specific namespaces, add a `namespaceSelector`:

```
spec:



metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



team: finance
```

Enrichment file contents

Both files expose the following attributes:

```
{



"k8s.cluster.name": "<cluster-name>",



"k8s.cluster.uid": "<cluster-uid>",



"k8s.namespace.name": "<namespace-name>",



"k8s.node.name": "<node-name>",



"k8s.pod.name": "<pod-name>",



"k8s.pod.uid": "<pod-uid>",



"k8s.container.name": "<container-name>",



"k8s.workload.kind": "<workload-kind>",



"k8s.workload.name": "<workload-name>",



"dt.entity.kubernetes_cluster": "<kubernetes-cluster-id>",



"dt.kubernetes.cluster.id": "<cluster-id>",



"dt.kubernetes.workload.kind": "<workload-kind>",



"dt.kubernetes.workload.name": "<workload-name>"



}
```

Confirm enrichment is working by inspecting `/var/lib/dynatrace/enrichment` inside an injected pod and verifying both files are present.

## Resource attributes in the enrichment files

The `dt_host_metadata.json` and `dt_host_metadata.properties` files contain the host-level resource attributes that OneAgent reports for the host entity. The `dt_metadata.json` and `dt_metadata.properties` files are a separate set, reported for the processes and containers on the host and propagated up to their process groups and container groups. The two sets don't mix: an attribute in the host files isn't reported for a process, and the other way around. You can filter entities by most of what you read from these files, using the [resource attributes criterion](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#resourceattributes "Learn the Environment API v2 entity selector syntax for filtering monitored entities by type, name, tag, management zone, and health state.") of the Environment API v2 entity selector. You can also match those values in [management-zone rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules#resource-attribute-conditions "Define management-zone rules to control access to monitored entities, logs, and metrics using entity conditions, dimensional data, and entity selectors.") and in [automatically applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#resource-attribute-conditions "Define and apply tags manually or automatically to organize Dynatrace entities, using rule conditions based on entity properties and regular expressions.").

Two kinds of entry in these files are an exception, because Dynatrace doesn't store them on the entity: keys that start with `dt.`, and any attributes beyond the number Dynatrace stores per entity. See [Resource attribute limits and excluded keys](/managed/ingest-from/dynatrace-oneagent/resource-attributes#ra-limits "Understand the resource attributes stored on Dynatrace Managed hosts, processes, and containers, including configuration, filtering, and storage limits.").

Dynatrace writes these files, and you read them—they aren't a configuration input. Editing them has no effect, because Dynatrace overwrites them.

To add your own resource attributes, use one of these routes instead:

* On a host, set host tags whose keys use the `primary_tags.` prefix, with `oneagentctl`. See [Custom resource attributes](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#custom-resource-attributes "Automate host tags and metadata with oneagentctl or configuration files, and use the resulting properties in auto-tagging and management-zone rules.").
* In Kubernetes, declare the attributes in your DynaKube, or annotate your pods and namespaces. See [Set resource attributes in the DynaKube](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment#resource-attributes "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.").