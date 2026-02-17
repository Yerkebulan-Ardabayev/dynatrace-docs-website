---
title: Enrich ingested data with Dynatrace-specific dimensions
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-data
scraped: 2026-02-17T21:27:37.623248
---

# Enrich ingested data with Dynatrace-specific dimensions

# Enrich ingested data with Dynatrace-specific dimensions

* Latest Dynatrace
* 4-min read
* Published Apr 26, 2021

Unlike automatic ingestion using OneAgent, data sent directly to an ActiveGate (for example, ingest APIs) is not automatically enriched with host-related information. This may incur additional charges, as it would not take into account possibly included [DDU quotas](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

The different Dynatrace deployment options provide several Java-style properties and JSON files with sets of attributes that you can use to enrich your requests to Dynatrace and ensure Dynatrace can map the data to your infrastructure.

## Enrichment directory

Dynatrace uses the following directories to provide `.json` and `.properties` files with enrichment data:

* On Unix: `/var/lib/dynatrace/enrichment`
* On Windows: `%ProgramData%\dynatrace\enrichment`

## Dynatrace OneAgent

A standard OneAgent setup provides the following files with host-specific details in the [enrichment directory](#enrichment-directory):

* `dt_host_metadata.json`
* `dt_host_metadata.properties`

Both files contain the same collection of host-level resource attributes that OneAgent uses to enrich monitoring artifacts for a given host. This also includes key-value tags and properties set via [oneagentctl](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or through [Remote configuration management](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.").

If you supply telemetry data via different channels than OneAgent (for example, using OpenTelemetry), it is important you enrich your telemetry data manually with these attributes to ensure the proper host association.

For more information, see [Host-level resource attributes](/docs/platform/oneagent/resource-attributes#host-level-resource-attributes "Any signal that uses a given resource, such as host or process group, is enriched with certain attributes coming from the resource.").

For an example of how to load the JSON file, see the [Python example](#python-example) below.

## Dynatrace Kubernetes Operator

The following files are available in the [enrichment directory](#enrichment-directory) when metadata enrichment is enabled.

* `dt_metadata.json`
* `dt_metadata.properties`

Both files contain the same data in different formats. For an example of how to load the JSON file, see the [Python example](#python-example) below.

Please visit the [Configure enrichment directory](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") guide for configuration instructions.

To learn how to enrich all [telemetry data originating from Kubernetes workloads with Kubernetes labels and annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes").

## OneAgent virtual files

When OneAgent is monitoring your application, your application is also able to access the following virtual files:

* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

These files are not specific to the enrichment directory and do not physically exists in your file system, but are provided by the OneAgent instrumentation. Both files return the same data and the file extension (`.json`/`.properties`) only determines the output format.

In the context of the [Kubernetes Operator](#dynatrace-kubernetes-operator), the virtual file also contains the attributes of the `dt_metadata.{json,properties}` files.

### How to access the virtual files

1. Use the standard file read function of your language platform to open and read one of these files:

   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

   The file extension you choose is relevant for step 4. Only use the filename and do not specify an additional path.
2. The content of the file is a single text line with an absolute file path (consider it an ephemeral value and do not store, persist, or cache that path for later use).
3. Open the file at the path location obtained in the previous step and read its entire content.
4. The content format received from the previous read will match the file extension you chose in step 1 (Java-style properties or JSON).

If step 1 returns a file-not-found error, verify that your application is instrumented by OneAgent.

### Limitations

* Supported for full-stack and application-only deep-monitored processes.
* The `stat` and other `if (exists)` checks fail for these files. These checks are not required for the mechanism to work.
* `syscalls` used directly for file access aren't supported. This also means that the Go-based applications used for metric ingestion aren't supported unless you use the OneAgent SDK as explained in [Instrument your Go application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/go "Learn how to instrument your Go application using OpenTelemetry and Dynatrace.").

## Python example

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