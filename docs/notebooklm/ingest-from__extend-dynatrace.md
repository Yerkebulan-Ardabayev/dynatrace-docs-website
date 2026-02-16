# Dynatrace Documentation: ingest-from/extend-dynatrace

Generated: 2026-02-16

Files combined: 22

---


## Source: extend-data.md


---
title: Enrich ingested data with Dynatrace-specific dimensions
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-data
scraped: 2026-02-15T09:10:54.008075
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


---


## Source: jmx-extensions.md


---
title: JMX extensions
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions
scraped: 2026-02-15T21:11:52.603515
---

# JMX extensions

# JMX extensions

* Latest Dynatrace
* 7-min read
* Published Jul 19, 2017

JMX ([Java Management Extensionsï»¿](https://www.oracle.com/technetwork/java/javase/tech/javamanagement-140525.html)) is ideal for monitoring applications built using Java. With Dynatrace, you can monitor any metric in your JVM that is exposed via an MBean.

## Infrastructure Monitoring mode

JMX and PMI extensions are also available in [Infrastructure Monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") You can use them to monitor any infrastructure component and backing service written in Java and have all the collected metrics reported by Dynatrace.

## Create a JMX extension

Dynatrace version 1.162 and later

Dynatrace version 1.161 and earlier

1. Sign in to Dynatrace and go to **Settings** > **Monitoring** > **Monitored technologies** and click **Add new technology monitoring**. Of the four available options, one is **Monitor Java or WebSphere based technologies**. Click **Add JMX/PMI extension**.
2. Click **Use JMX/PMI extensions editor**.
3. Type the extension name. You can only use letters `A-Z, a-z`, numbers `0-9`, or `-/_`.
4. Add the metrics source.

* Select one of the available technologies.
* Based on your selection, the editor will suggest the Java process as a source for your metrics. This narrows the list of available MBeans or PMI modules you will use in the next step. The technology behind the process determines whether you'll browse JMX MBeans or PMI modules. Click **Add metrics source** to use a suggested source. Click ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to select a different process. When selecting it, you can narrow the list of available processes by choosing a particular host or Management Zone.

Selecting the process, host, or Management Zone doesn't limit the extension monitoring scope. JMX/PMI extensions monitor all Java processes accessible to OneAgent. The metric defined for the same MBean and attribute will be also available in other Java processes across your application, which can quickly exhaust your custom metric limit.

You can also select individual hosts on which to run your new JMX extension, instead of running it globally across your whole environment.

1. Immediately after you add your JMX extension, go to **Settings**> **Monitored technologies** > **Custom extensions** tab and disable it globally.
2. Navigate to individual host pages, open the host settings, find your JMX extension and enable it.

5. When the metrics list is downloaded, click the **Add metric** button to start creating your extension.

   #### Domain

   Select the domain.

   #### Select key properties

   Key properties filter the list of available MBeans. Note that property values can contain wildcards. Select **Exact match** to filter MBeans list only to the entries matching the exact key property values.

   #### Select MBean

   Select one MBean from the list or leave **All matching MBeans** option. If more than one MBean is matched, this will cause the aggregation of attributes from all matching MBeans into one metric. You will define the aggregation type below.

   #### Select attribute

   The attributes available in the list are only the numeric ones. To see other attributes, for example attributes of the `String` type, select **Include non-numeric attributes**. Note that selected attributes must be parsable to double, or boolean type. Otherwise, Dynatrace OneAgent will not collect any data from such a metric.

   #### Display name

   You can define a custom display name for the metric.

   #### Unit

   Select the metric unit.

   #### Aggregation

   Select the aggregation method if you're pulling an attribute from a number of matching Mbeans.

   #### Calculation

   **Delta** calculates the change in values of the given attribute. **Rate** calculates the rate of changes per seconds. When you select both, you can convert an absolute attribute (eg. Request Count) to a rate (eg. Requests per Second). Value = attribute / query interval.

## Creating the PMI extension

Creating the PMI extension is very similar to the JMX extension. PMI Module translates to JMX Mbean and statistics to attributes. All other settings behave accordingly.

## Saving the extension

After you add the metric, you can still edit or delete its definition. You must click the **Save** button to register the extension and start collecting data from all Java processes that contain defined MBeans. After you save the extension, you cannot edit or delete the metrics, as this way we're able to maintain the continuity of your data. You can still add the new metrics. This time however, you won't be able to select the base Java process, because you will use a process where the extension is already deployed.

## Customizing your extension

The Dynatrace JMX extensions are highly customizable beyond the capabilities of the editor. You can download your extension and edit its JSON file that describes your JMX metrics and how you want to display them. For reference and examples, see [Customizing JMX Plugins](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions/customize-jmx-extensions "Learn how to further customize your JMX extensions.").

You need to create a JSON file that describes your JMX metrics and how you want to display them. For reference and examples, see [Customizing JMX Plugins](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions/customize-jmx-extensions "Learn how to further customize your JMX extensions.").

## Upload a JMX extension

1. To add a JMX extension to Dynatrace, go to **Settings** > **Monitored technologies > Custom extensions** and click **Upload extension**.
2. Select the `plugin.json` file of your JMX extension.  
   Once successfully uploaded, your extension is listed on the **Custom extensions** page. You don't need to restart your JVM to enable JMX extensions or make changes effective.

   If in the future you make changes to your extension, remember to upload the updated `plugin.json` file to Dynatrace.

## Viewing JMX metrics in Dynatrace

JMX metrics are available for all Java-based processes monitored by OneAgent.

Once your extension is uploaded, Dynatrace automatically begins querying the defined metrics for all Java processes. To find the metrics, go to a relevant process page and click **Further details**.

![JMX metrics](https://dt-cdn.net/images/jmxeditor-1-600-91b2c04b73.png)

For example, for a extension named `HornetQ`, go to the process you selected when creating the extension, click **Further details** and then select the **HornetQ** tab named automatically after the extension name. You'll find all the defined metrics there.

![JMX metrics](https://dt-cdn.net/images/jmxeditor-2-1211-ca87466d9e.png)

Not seeing a certain metric?

JMX monitoring is highly dynamic. If a particular metric doesnât exist in your JVM, it's not an errorâthe metric simply isn't available.

## JMX/PMI extension custom metrics

You may notice that the number of metrics in the `plugin.json` file of your JMX/PMI extension differs from the number of billed custom metrics. This is because JMX/PMI extensions provide "splittings" which can be used to define additional dimensions for reported metrics. For each value of a selected property, a separate timeseries metric is created at runtime. The actual number of timeseries metrics depends on the number of distinct values for the selected property.

The following sample shows how to define a metric that provides multiple timeseries with a single metric:

```
"metrics": [



{



"timeseries": {



"key": "XY.Size",



"unit": "Count",



"displayname": "Queue Consumer Count",



"dimensions": [



"rx_pid",



"name"



]



}



"source": {



"domain": "com.sample",



"keyProperties": {



"type": "XY",



"name": "*"



},



"attribute": "Size",



"splitting": {



"name": "name",



"type": "keyProperty",



"keyProperty": "name"



}



}



}



]
```

In this example, MBeans `com.sample:type=XY,name=A` and `com.sample:type=XY,name=B` will result in two timeseries metrics (`A` and `B`).

Since such values typically aren't known in advance, and are subject to change, this can lead to an unexpectedly high number of [consumed custom metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). If the values of the property are known in advance, or if only some of the values are of interest, we recommend that you specify one metric for each value and not use splitting.

## Metrics limit per JMX extension

There can be no more than `5,000` metrics per JMX extension. This limit is necessary to prevent underperforming or metric-heavy extensions from overwhelming the monitoring system.

## Monitoring consumption

The JMX extension listed below initially consume each monitored host's quota of included metrics. Once the included metrics quota is exhausted, DDU consumption begins. The figures in the table below represent the expected consumption per process for each technology type that an extension monitors. The **Custom metrics** count reflects the default set of metrics that are generated by each extension.

| Technology | Type | Custom metrics |
| --- | --- | --- |
| ActiveMQ JMX | JMX Monitoring | 15 |
| Apache Hadoop HDFS | JMX Monitoring | 43 |
| Apache Hadoop YARN | JMX Monitoring | 48 |
| Apache Spark | JMX Monitoring | 17 |
| Cassandra JMX | JMX Monitoring | 28 |
| HornetQ JMX | JMX Monitoring | 5 |
| JBoss Connection Pools | JMX Monitoring | 14 |
| Jetty JMX | JMX Monitoring | 7 |
| Kafka JMX | JMX Monitoring | 42 |
| Solr JMX | JMX Monitoring | 24 |
| Tomcat Connection Pools | JMX Monitoring |  |
| WebLogic Connection Pools | JMX Monitoring | 12 |
| WebSphere Liberty Connection Pools | JMX Monitoring | 5 |
| WSO2 API Manager | JMX Monitoring | 27 |


---


## Source: micrometer.md


---
title: Send Micrometer metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer
scraped: 2026-02-15T21:11:34.553740
---

# Send Micrometer metrics to Dynatrace

# Send Micrometer metrics to Dynatrace

* Latest Dynatrace
* 7-min read
* Updated on Jan 28, 2026

[Micrometerï»¿](https://dt-url.net/7u039ck) is an open source instrumentation framework for JVM-based application metrics. It's used by [Spring Bootï»¿](https://dt-url.net/ba239ye) to record a wide range of metrics. You can ingest Micrometer and Spring Boot metrics and analyze them with Dynatrace Intelligence end-to-end in the context of your trace, log, and diagnostics data. With Dynatrace, you get intelligent AI-based observability and automatic root cause analysis for Spring Boot, 15+ pre-instrumented JVM-based frameworks and servers, and custom metrics.

You can use Micrometer in Dynatrace to:

* Ingest pre-instrumented metrics from Spring Boot applications
* Ingest pre-instrumented metrics from JVM-based frameworks, servers, and cache systems
* Define and ingest custom metrics

Metrics ingested from Micrometer consume [DDUs for custom metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

There are two ways of using Micrometer:

* [As part of Spring Boot](#micrometer-with-spring-boot)
* [As a metrics facade used directly in your code](#directly)

## Prerequisites

* Micrometer version 1.8.0+
* Optional Spring Boot version 2.6.0+
* The registry dependency must be added to your project:

  Micrometer standalone

  Spring Boot

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace:latest.release'
  ```

  Maven

  Replace `{micrometer.version}` with the latest version of Micrometer or a specific version that you want to use.
  A list of released versions is available on [Maven Centralï»¿](https://dt-url.net/ay439b4).
  We recommend that you use the latest version.

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-dynatrace</artifactId>



  <version>{micrometer.version}</version>



  </dependency>
  ```

  The Spring Boot BOM specifies a Micrometer version that has been tested with the respective version of Spring Boot.
  It's therefore enough to specify the name of the dependency without specifying the version.
  This will result in the correct, matching version being pulled by Gradle or Maven.

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace'
  ```

  Maven

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-dynatrace</artifactId>



  </dependency>
  ```

## Ingestion channels

You can use one of the following ingestion channels to send your Micrometer metrics:

* [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")âneeds OneAgent installed on the monitored host.
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Dynatrace Micrometer registry

Micrometer uses the concept of a registry to export metrics to monitoring systems.

* For Micrometer version 1.8.0 or later, [Dynatrace Registry v2ï»¿](https://micrometer.io/docs/registry/dynatrace) is available. It exports metrics via the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). All new integrations of Micrometer and Dynatrace must use this version.
* For Micrometer version 1.8.0 or earlier, the legacy Dynatrace Micrometer registry v1 is available. For instructions, see [Dynatrace Micrometer registry v1 (legacy)](#registry-v1) below.

## Ingest metrics from Spring Boot apps

Micrometer can be configured via a `.properties` or `.yaml` file used for Spring Boot configuration.
Spring Boot automatically binds properties with the `management.dynatrace.metrics.export` prefix to the [Dynatrace configuration object](#dt-configuration-properties).

All configuration should be made through the property files. Manually creating a Micrometer `MeterRegistry` breaks the auto-configuration.

Property names for binding attributes from Spring Boot have changed in Spring Boot version 3.0.0. If you use a Spring Boot version before 3.0.0, use `management.metrics.export.dynatrace` instead of `management.dynatrace.metrics.export`.

With OneAgent (recommended)

With Dynatrace Operator for Kubernetes

Without OneAgent

OneAgent on Kubernetes nodes does not support the ingestion of Micrometer metrics directly. See [Sending Metrics from Kubernetes](#k8s-metrics) for more details. If you're using Dynatrace on Kubernetes, we recommend using Dynatrace Operator, which provides autoconfiguration.

For hosts that are monitored by OneAgent, automatic configuration is available. You don't need to specify the API endpoint to ingest the metricâif the **uri** parameter is not set in the configuration, the metric will be ingested via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

YAML

```
management.dynatrace.metrics.export:



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

Dynatrace Operator configures Dynatrace Micrometer registry by providing ingest URL, credentials and Kubernetes metadata. For configuration examples, see our [Dynakube examplesï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
For more information about metadata enrichment, see [the documentation on enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

* This feature is available when using Dynatrace Micrometer registry versions 1.9.0 and above.
* An app using the Dynatrace Micrometer registry and running in Kubernetes with a Dynatrace Operator does not require any explicit configuration. Dynatrace Operator and the registry will work together and automatically export Micrometer metrics to Dynatrace.
* Explicitly specifying the `management.dynatrace.metrics.export.uri` will overwrite automatic configuration and should be avoided when used with Dynatrace Operator.

YAML

```
management.dynatrace.metrics.export:



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

To ingest metrics from hosts where OneAgent is not installed, such as serverless deployments (for example, AWS ECS) or other non-Kubernetes environments, you need to use the [ingest endpoint of the Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API."). To learn how to use the endpoint, see the [POST ingest data points example](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API."). The Micrometer Dynatrace registry exports to this API when the URI and token are set.

Ensure that the URI is explicitly configured, as leaving it unset will default to `localhost`, and the OneAgent local ingest is not available in these environments.

HTTP clients connecting to the non-public ActiveGate REST endpoint must trust provided certificates. For details, see [Add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.").

You can use the Spring placeholder notation (for example, `api-token: ${YOUR_METRICS_INGEST_API_TOKEN}`), which will automatically read the environment variable and supply it to the Micrometer configuration.

YAML

```
management.dynatrace.metrics.export:



uri: "https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest"



# Read the environment variable YOUR_METRICS_INGEST_API_TOKEN and supply the value of the env var instead.



api-token: ${YOUR_METRICS_INGEST_API_TOKEN}



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.uri=https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest



management.dynatrace.metrics.export.api-token=${YOUR_METRICS_INGEST_API_TOKEN}



management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

## Ingest metrics directly from Micrometer

With OneAgent (recommended)

With Dynatrace Operator for Kubernetes

Without OneAgent

For hosts that are monitored by OneAgent, automatic configuration is available. You don't need to specify the API endpoint to ingest the metricâif the **uri** parameter is not set in the configuration, the metric will be ingested via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

View auto-configuration code

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

Dynatrace Operator configures Dynatrace Micrometer registry by providing ingest URL, credentials and Kubernetes metadata. For configuration examples, see our [Dynakube examplesï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
For more information about metadata enrichment, see [the documentation on enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

* This feature is available when using Dynatrace Micrometer registry versions 1.9.0 and above.
* An app using the Dynatrace Micrometer registry and running in Kubernetes with a Dynatrace Operator does not require any explicit configuration. Dynatrace Operator and the registry will work together and automatically export Micrometer metrics to Dynatrace.
* Explicitly specifying the `management.dynatrace.metrics.export.uri` will overwrite automatic configuration and should be avoided when used with Dynatrace Operator.

View auto-configuration code

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

To ingest metrics from hosts where OneAgent is not installed, such as serverless deployments (for example, AWS ECS) or other non-Kubernetes environments, you need to use the [ingest endpoint of the Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API."). To learn how to use the endpoint, see the [POST ingest data points example](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API."). The Micrometer Dynatrace registry exports to this API when the URI and token are set.

Ensure that the URI is explicitly configured, as leaving it unset will default to `localhost`, and the OneAgent local ingest is not available in these environments.

HTTP clients connecting to the non-public ActiveGate REST endpoint must trust provided certificates. For details, see [Add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.").

View manual configuration code

In this example, the metrics ingest URL and access token are read from environment variables `YOUR_METRICS_INGEST_URL` and `YOUR_METRICS_INGEST_TOKEN`. You should never store secrets in the code directly, but read them from a secure source.

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



public DynatraceApiVersion apiVersion() {



// Not strictly required, but makes the code more clear/explicit



return DynatraceApiVersion.V2;



}



@Override



public String uri() {



// The endpoint of the Dynatrace Metrics API v2 including path:



// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");



return endpoint != null ? endpoint : DynatraceConfig.super.uri();



}



@Override



public String apiToken() {



// Should be read from a secure source



String token = System.getenv("YOUR_METRICS_INGEST_TOKEN");



return token != null ? token : "";



}



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(dynatraceConfig).build();
```

## Verify the metrics

After you have sent your metrics, verify the data in the [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [query them in Grail](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands").

## Configuration properties

To set up the Dynatrace Micrometer registry, you can use the Dynatrace configuration object (`DynatraceConfig`). The object contains the parameters of metric ingestion and is used to construct the Dynatrace registry (`DynatraceMeterRegistry`), which is registered with Micrometer to ingest metrics to Dynatrace. You can set the following parameters:

Spring Boot

Directly in Micrometer

When using Spring Boot, entries in your `application.properties` or `application.yaml` files will be mapped to the `DynatraceConfig` object automatically.

Property

Description

Required

api-version

The version of the Dynatrace API to ingest data to Dynatrace:

* `V2` (default): [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").
* `V1`: [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.")

Optional

uri

The ingestion endpoint of the API.

Optional

metric-key-prefix

The prefix to be added to all ingested metric keys (for example, a namespace).

Optional

enrich-with-dynatrace-metadata

[Enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") (`true`) or do not enrich (`false`) ingested metrics with additional metadata.

If not set, `true` is used.

Optional

default-dimensions

A list of dimensions to be added to the ingested metrics.

Dimensions are defined as key-value pairs.

Optional

use-dynatrace-summary-instruments

Micrometer versions 1.9.x+ Ignore the Dynatrace-specific implementation for summary instruments (`Timer` and `DistributionSummary`).

The default (`true`) uses the new Instruments. Use `false` to fall back to 1.8.x behavior.

Optional

export-meter-metadata

Micrometer versions 1.12.x+ Turn meter metadata export (unit & description) on or off.

The default (`true`) configures the registry to export meter metadata. Use `false` to turn off metadata exporting.

Optional

Property

Description

Required

apiVersion

The version of the Dynatrace API to ingest data to Dynatrace:

* `V2` (default): [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").
* `V1`: [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.")

Optional

uri

The ingestion endpoint of the API.

Optional

metricKeyPrefix

The prefix to be added to all ingested metric keys (for example, a namespace).

Optional

enrichWithDynatraceMetadata

[Enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") (`true`) or do not enrich (`false`) ingested metrics with additional metadata.

If not set, `true` is used.

Optional

defaultDimensions

A list of dimensions to be added to the ingested metrics.

Dimensions are defined as key-value pairs.

Optional

useDynatraceSummaryInstruments

Micrometer versions 1.9.x+ Ignore the Dynatrace-specific implementation for summary instruments (`Timer` and `DistributionSummary`).

The default (`true`) uses the new Instruments. Use `false` to fall back to 1.8.x behavior.

Optional

exportMeterMetadata

Micrometer versions 1.12.x+ Turn meter metadata export (unit & description) on or off.

The default (`true`) configures the registry to export meter metadata. Use `false` to turn off metadata exporting.

Optional

Code snippet to set properties

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



public DynatraceApiVersion apiVersion() {



// Defaults to V2 if not set explicitly.



return DynatraceApiVersion.V2;



}



@Override



public String uri() {



// The endpoint of the Dynatrace Metrics API v2 including path. For example:



// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest".



String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");



return endpoint != null ? endpoint : DynatraceConfig.super.uri();



}



@Override



public String apiToken() {



// Should be read from a secure source



String token = System.getenv("YOUR_METRICS_INGEST_API_TOKEN");



return token != null ? token : "";



}



@Override



public String metricKeyPrefix() {



// Will be prepended to all metric keys



return "service.component";



}



@Override



public boolean enrichWithDynatraceMetadata() {



// On by default, but can be turned off explicitly.



return true;



}



@Override



public Map<String, String> defaultDimensions() {



// Create and return a map containing the desired key-value pairs.



Map<String, String> dims = new HashMap<>();



dims.put("dimensionKey", "dimensionValue");



return dims;



}



// Only available in Micrometer 1.9.0 and above.



@Override



public boolean useDynatraceSummaryInstruments() {



return false;



}



// Only available in Micrometer 1.12.0 and above.



@Override



public boolean exportMeterMetadata() {



return false;



}



@Override



@Nullable



public String get(String k) {



return null; // Accept the rest of the defaults



}



};
```

## Additional information

### Metric types

All metrics are transformed to follow the [Metric ingestion protocol types](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.") used by Dynatrace.

Micrometer instrument

Dynatrace metric type

Gauge

`gauge,X`

Counter

`count,delta=X`

Timer

`gauge,min=X,max=Y,sum=Z,count=N`

DistributionSummary

`gauge,min=X,max=Y,sum=Z,count=N`

LongTaskTimer

`gauge,min=X,max=Y,sum=Z,count=N`

TimeGauge

`gauge,X`

FunctionCounter

`count,delta=X`

FunctionTimer

`gauge,min=X,max=Y,sum=Z,count=N`

Note that the `count` for LongTaskTimers can be misleading as it is likely to double-count depending on the export frequency. In case you require the current number of active tasks, exporting a separate Gauge is more reliable.

### Meter metadata

Starting with version 1.12.0 of the Dynatrace Micrometer registry, meter metadata (unit and description) is automatically exported to Dynatrace.
No code changes are required to start exporting metadata.
To turn off metadata export, use the following configuration:

Spring Boot

Directly in Micrometer

YAML

```
management:



metrics:



export:



dynatrace:



v2:



export-meter-metadata: false  # default: true
```

.properties

```
management.dynatrace.metrics.export.v2.export-meter-metadata=false
```

Meter metadata was introduced with Micrometer 1.12.0, which was first included in Spring Boot 3.2.0.
The toggles described above are therefore available from Spring Boot 3.2.0.

Code snippet to set properties

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



// Only available in Micrometer 1.12.0 and above.



@Override



public boolean exportMeterMetadata() {



return false;



}



@Override



@Nullable



public String get(String k) {



return null; // Accept the rest of the defaults



}



};
```

For previous versions of Micrometer, metadata needs to be specified manually using either the Dynatrace API or web UI.
For more information, see [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.").

### Sending metrics from Kubernetes

OneAgent cannot be used for Micrometer metric ingestion on Kubernetes nodes. You can configure your Micrometer setup to push metrics directly to Dynatrace using the [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

### Capture JVM metrics in Micrometer

By default, JVM metrics are turned off when running Micrometer without Spring Boot. To learn how to enable them, see the [Micrometer documentationï»¿](https://docs.micrometer.io/micrometer/reference/reference/jvm.html). After they are enabled and registered with the Dynatrace registry (`DynatraceMeterRegistry`), JVM metrics are recorded and sent to Dynatrace automatically.

On hosts that are monitored by OneAgent, these metrics might already be captured by OneAgent.

### Restrict ingestion of specific metrics

Spring Boot

Directly in Micrometer

When running Micrometer in Spring Boot, [many metricsï»¿](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.metrics.supported) are automatically created and sent to Dynatrace, including JVM, process, and disk metrics.

To see all metrics created by your Spring Boot application, navigate to the [actuator endpoint on your Spring Boot appï»¿](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.enabling) (`/actuator/metrics`). Some of these metrics might already be captured by OneAgent.

### Disable metrics with Spring properties

Metrics can be disabled based on their prefix in the Spring Boot configuration. To find out which metrics can be excluded, check your Spring Boot applications actuator endpoint. Be sure to **exclude** your custom metric key prefix (if any, see [`metric-key-prefix`](#dt-configuration-properties)) when using this feature.

YAML

```
management.metrics.enable:



# disable jvm.memory metrics



jvm.memory: false



# disable all jvm metrics:



jvm: false
```

.properties

```
# disable jvm.memory metrics



management.metrics.enable.jvm.memory=false



# disable all jvm metrics



management.metrics.enable.jvm=false
```

It is also possible to disable all metrics first and then only re-enable the desired ones:

YAML

```
management.metrics.enable:



# disable all metrics



all: false



# re-enable only jvm.* metrics



jvm: true
```

.properties

```
# disable all metrics



management.metrics.enable.all=false



# re-enable jvm.* metrics



management.metrics.enable.jvm=true
```

### Disable metrics in code

Micrometer provides [meter filtersï»¿](https://docs.micrometer.io/micrometer/reference/concepts/meter-filters.html) to disable metrics based on a variety of conditions. Meter filters can also be configured via Spring Boot with the `@Configuration` annotation.

Show code snippet

```
@Configuration(proxyBeanMethods = false)



public class MyMeterRegistryConfiguration {



@Bean



public MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {



return registry -> registry.config()



.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));



}



}
```

The metric prefix configured for the Dynatrace registry will be applied after filtering, so properties to enable or disable metrics have to be specified using the original metric key without this prefix.

Register MeterFilters before creating or [turning on additional metrics](#add-automatically-created-metrics), as the `MeterFilter` will only be evaluated when the metric is added to the `MeterRegistry`.

You can configure the registry to filter out specific metrics by name and/or tags (for example, metrics that are already captured by OneAgent). To achieve that, use Micrometer's [meter filtersï»¿](https://micrometer.io/docs/concepts#_meter_filters). You need to add meter filters before you enable [capture of JVM metrics](#add-automatically-created-metrics), otherwise filters will be overridden.

The metric prefix configured for the Dynatrace registry will be applied after filtering, so `meterFilters` have to be specified using the original metric key without this prefix.

Disable metrics in code

```
// Disable all metrics with metric names starting with jvm.gc



registry.config()



.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));
```

### Troubleshooting with logs

Spring Boot

Directly in Micrometer

Spring handles the logging when using Micrometer in the Spring Boot context. The log level for the Micrometer Dynatrace registry can be set via configuration properties.

YAML

```
logging.level.io.micrometer.dynatrace: DEBUG
```

.properties

```
logging.level.io.micrometer.dynatrace=DEBUG
```

Micrometer and the Dynatrace Micrometer registry use [slf4jï»¿](https://www.slf4j.org/) internally to log events, such as the lines that are sent to Dynatrace.
If you want to get this information, set up your project with the logging framework of your choice (for example, [logbackï»¿](https://logback.qos.ch/manual/configuration.html#automaticConf)) and set the log level to `debug`.

Debug logging with logback

When using the default logback implementation, debug logging to the console is enabled by default. In order to add logback to your project and log debug information, add the following dependency:

```
implementation 'ch.qos.logback:logback-classic:latest.release'
```

### Dynatrace summary instruments

Starting with Micrometer version 1.9.x, specialized instruments are used in the Dynatrace meter registry for certain summary instruments (`DynatraceTimer` and `DynatraceDistributionSummary`). Their purpose is to get around a peculiarity in how Micrometer records metrics, which, in some cases, led to metrics being rejected by Dynatrace for having an invalid format. The specialized instruments, tailored to Dynatrace metrics ingestion, prevent the creation of invalid metrics.

* They are available from version 1.9.0 and are used as a drop-in replacement by default. No action is needed from users upgrading to 1.9.0.
* If there's a discrepancy in the observed metrics, it's possible to return to the previous behavior by setting the `useDynatraceSummaryInstruments` toggle to `false`.

## Dynatrace Micrometer registry v1 (legacy)

If the **apiVersion** property is set to `V1`, the registry sends data via the [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API."). For backward compatibility, it defaults to `V1` if a **deviceId** is specified, because this property is required in `V1` and is not used in `V2`.

Existing setups will continue to work when updating to newer versions of Micrometer. The reported metrics will be assigned to custom devices in Dynatrace.

For the `V1` API, you only need to specify the base URL of your environment (for example, `https://mySampleEnv.live.dynatrace.com`).

Spring Boot

```
management.dynatrace.metrics.export:



# For v1 export, do not append a path to the endpoint URL. For example:



# For SaaS: https://{your-environment-id}.live.dynatrace.com



# For Managed deployments: https://{your-domain}/e/{your-environment-id}



uri: https://{your-environment-id}.live.dynatrace.com



# Should be read from a secure source



api-token: MY_TOKEN



# When setting the device id, metrics will be exported to the v1 timeseries endpoint



# Using just device-id (without the v1 prefix) is deprecated, but will work to maintain backwards compatibility.



v1:



device-id: sample



# To disable Dynatrace publishing (for example, in a local development profile), use:



# enabled: false



# The interval at which metrics are sent to Dynatrace. The default is 1 minute.



step: 1m
```

Directly in Micrometer

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



public String uri() {



// The Dynatrace environment URI without any path. For example:



// https://{your-environment-id}.live.dynatrace.com



return MY_DYNATRACE_URI;



}



@Override



public String apiToken() {



// Should be read from a secure source



return MY_TOKEN;



}



@Override



public String deviceId() {



return MY_DEVICE_ID;



}



@Override



@Nullable



public String get(String k) {



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();



// Add the Dynatrace registry to Micrometers global registry.



Metrics.addRegistry(registry);
```


---


## Source: oneagent-metric-api.md


---
title: OneAgent metric API
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api
scraped: 2026-02-15T21:11:46.394170
---

# OneAgent metric API

# OneAgent metric API

* Latest Dynatrace
* 2-min read
* Updated on Jan 28, 2026

You can use the local `http://localhost:<port>/metrics/ingest` API endpoint to push locally retrieved metrics to Dynatrace over a secure and authenticated channel. This endpoint is available only to local clients and cannot be reached from remote hosts.

If you can't push metrics using a local API endpoint, you can also use the public [Metric API v2](#api) endpoint.

## Enable the OneAgent metric API

ActiveGate version 1.243+

OneAgent version 1.243+

The OneAgent metric API comes with OneAgent version 1.201 by default. You only need to enable the OneAgent metric API at the environment or host level. Note that the host-level configuration overrides the environment configuration.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

If you want to change your limits for EEC resource consumption, see [Performance profile](/docs/ingest-from/extensions/concepts#performance-profile "Learn more about the concept of Dynatrace Extensions.").

## Topology awareness

Using the local API endpoint, the host ID and host name context are automatically added to each metric as dimensions. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

The request consumes a `text/plain` payload with the `charset=utf-8` character set. The payload is limited to `1,000` lines.

## Example

With this `curl` command, you'll ingest the `cpu.temperature` metric assigned to the `cpu=1` dimension. The metric will be automatically assigned to a respective host ID and host name.

```
curl --data "cpu.temperature,cpu=1 55" http://localhost:14499/metrics/ingest \



-H "Content-Type: text/plain; charset=utf-8"
```

Successful response:

```
{



"error": null,



"linesValid": 1,



"linesInvalid": 0



}
```

## Communication port

Starting with OneAgent version 1.267+, AIX systems also support metric ingestion.

The default metric ingestion port is `14499`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the port. Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

### Check the ingestion port

Use the `--get-extensions-ingest-port` parameter to show the current local ingestion port, `14499` by default.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Set a custom ingestion port

Use the `--set-extensions-ingest-port=<arg>` parameter to set a custom local ingestion port.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Configure proxy

Configure your host proxy to allow localhost traffic going to the metric ingestion port, `14499` by default.

Note that changing the port for the OneAgent metric API also affects scripting integration and Telegraf.

## Metrics API v2

Unlike the local ingestion interface, which adds the topology context automatically (each metric is assigned to a respective host), metrics pushed through the public [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") v2 are flat by default. This is especially beneficial for business-related metrics that don't have any relation to the topology entities in your environment.

However, to have events raised for a selected host and have Dynatrace Intelligence perform causation analysis based on your metrics, you can configure your app to add the `dt.entity.host` dimension. To automatically enrich process group identifier with the metric, provide `dt.process.pid` dimension. For more information, see [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: oneagent-pipe.md


---
title: Metric scripting integration
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe
scraped: 2026-02-15T21:11:31.743541
---

# Metric scripting integration

# Metric scripting integration

* Latest Dynatrace
* 2-min read
* Published Oct 15, 2020

You can use the `dynatrace_ingest` tool to push locally retrieved metrics to Dynatrace over a secure and authenticated channel. The tool is available to local clients only and cannot be reached from remote hosts.

## Enable scripting integration

Scripting integration comes with OneAgent version 1.201+ by default. You only need to enable scripting integration at the environment or local host level. Note that the host-level configuration overrides the environment configuration.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

## Binary location

The tool location depends on whether or not you've customized the OneAgent installation using the `<INSTALL_PATH>` parameter:

* **Linux**:  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`
* **Docker-based deployment**  
  `<INSTALL_PATH>/agent/tools`, by default `/opt/dynatrace/oneagent/agent/tools`  
  Note that this path will differ for a volume-based deployment.
* **Windows**:  
  `<INSTALL_PATH>\agent\tools`, by default `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`

## Topology awareness

Using the `dynatrace_ingest` based scripting integration, the host ID and host name context are added to each metric as dimensions automatically. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

## Usage

The basic usage is:

```
dynatrace_ingest [Options] [Metrics]
```

Both `[Options]` and `[Metrics]` are optional. The syntax of metrics passed to the `[Metrics]` arguments must comply with the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

There two basic ways to pass metrics with `dynatrace_ingest`: (1) by piping another process output to `dynatrace_ingest`, or (2) using the call arguments.

### Piping process output

When metrics are omitted, `dynatrace_ingest` expects them to be passed via standard input. Each line is treated as one metric. This enables you to pipe metrics to `dynatrace_ingest` from the output of other processes. For example:

```
echo host.process_count `ps aux | wc -l` | dynatrace_ingest
```

### Call arguments

When using call arguments instead of standard input to pass metrics, pass each metric as a separate argument. For example, to pass two metrics using a single command:

```
dynatrace_ingest 'cpu.temperature,cpu=1 55'  'cpu.temperature,cpu=2 45'
```

### Command line options

`-v [ --verbose ]`  
Prints logs to standard output

`-p [ --port ] arg (=14499)`  
Sets custom port for communication with the OneAgent Extensions Execution Controller (EEC) module. If you change the default EEC port (`14499`), you must instruct `dynatrace_ingest` to use the new port. For more information on setting a custom EEC port, see [Communication port](#communication-port)

`-h [ --help ]`  
Prints help message and quit

## Communication port

Starting with OneAgent version 1.267+, AIX systems also support metric ingestion.

The default metric ingestion port is `14499`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the port. Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

### Check the ingestion port

Use the `--get-extensions-ingest-port` parameter to show the current local ingestion port, `14499` by default.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Set a custom ingestion port

Use the `--set-extensions-ingest-port=<arg>` parameter to set a custom local ingestion port.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Configure proxy

Configure your host proxy to allow localhost traffic going to the metric ingestion port, `14499` by default.

Note that changing the port for scripting integration also affects OneAgent REST API and Telegraf.


---


## Source: prometheus-extensions.md


---
title: Manage Prometheus extensions
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions
scraped: 2026-02-15T09:12:00.693990
---

# Manage Prometheus extensions

# Manage Prometheus extensions

* Latest Dynatrace
* 4-min read
* Published Feb 01, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from a Prometheus endpoint. With it, you can bring the Prometheus data into Dynatrace at scale and in context with all other data.

* To take full advantage of the Dynatrace Prometheus extension, you need a OneAgent on the monitored box, but it can also work in an agentless manner.
* Check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=prometheus) to see if your technology is already covered by an existing extension. If this is not the case, you can easily build your own [Dynatrace Prometheus extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.").

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Before you begin**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#before-you-begin "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add extension to environment**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#add-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Define monitoring source**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#define-monitoring-source "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Advanced properties**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#advanced-properties "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Autodiscovery**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#autodiscovery "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Activate extension**](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#activate-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")

## Step 1 Before you begin

Decide which of your hosts will provide the Prometheus data for the extension.

Prometheus extensions can run locally on a OneAgent (recommended) or remotely on an ActiveGate.

* When run locally, the extension connects to the Prometheus interface automatically. Make sure the Extension Execution Controller (EEC) is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
* When monitored remotely, the ActiveGates belonging to an ActiveGate group that you'll designate for remote monitoring need to be able to connect to the host where Prometheus metrics originate.

Required permission: **Change monitoring settings**

## Step 2 Add extension to environment

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Prometheus data into your Dynatrace environment.

1. In Dynatrace Hub, search for a Prometheus extension. You can use the "Prometheus" keyword to filter results.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

## Step 3 Define monitoring source

Decide how you want to monitor your host: local or remote.

### Local monitoring

1. Select the host, host group or management zone for which you will run the extension, or choose to monitor the whole environment. The host needs to be running a OneAgent that is [enabled to run extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
2. Select **Next step**.
3. Select **Add endpoint**.
4. Define the Prometheus endpoint providing metrics and authentication details. For more information on supported authentication schemes, see [Authentication](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#authentication "Learn about Prometheus extensions in the Extensions framework."). Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Remote monitoring

1. Select **Monitor remotely**.
2. Define the Prometheus endpoint providing metrics and authentication details. For more information on supported authentication schemes, see [Authentication](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#authentication "Learn about Prometheus extensions in the Extensions framework.")
3. Select **Next step**.
4. Select the ActiveGate group to determine which ActiveGates will run the extension. When done, select **Next step**.

## Step 4 Advanced properties

Select **Define** to configure optional advanced properties:

* **Timeout in seconds**: The maximum time (in seconds) to wait to return data. Default = 10 seconds.
* **Retries**: The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). Default = 0 retries.

## Step 5 Autodiscovery

Autodiscovery is a feature that automatically resolves the DNS endpoints. If autodiscovery is defined, the URL becomes the DNS name.

Select **Define** to configure DNS endpoints:

* **Auto discovery type**: Only the `DNS` type available.
* **DNS type**: The type of DNS query to perform. Only the `A` type is available, which corresponds to IPv4 addresses.
* **DNS port**: Specifies the port assigned to all IPs resolved by the DNS.
* **DNS refresh interval (s)**: Sets interval time in seconds to the frequently changing IP addresses.

## Step 6 Activate extension

Provide final configuration details.

* Description
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* Feature sets
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension. For more information, see [Prometheus data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions/prometheus-schema-reference#featureset "Learn about Prometheus extensions in the Extensions framework.").

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")


---


## Source: prometheus.md


---
title: Prometheus
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus
scraped: 2026-02-15T21:11:41.173600
---

# Prometheus

# Prometheus

* Latest Dynatrace
* 1-min read
* Published Feb 01, 2022

Prometheus is an open-source monitoring and alerting toolkit that is popular in the Kubernetes community. Prometheus scrapes metrics from a number of HTTP(s) endpoints that expose metrics in the OpenMetrics format.

Dynatrace provides you with a framework to easily ingest data provided by Prometheus into Dynatrace at scale and in the context to all other data.

To get started, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/) to see if your technology is already covered by an existing extension.

If there's no extension covering your needs, Dynatrace currently provides three approaches to acquiring Prometheus data, depending on the environment.

* Prometheus in Kubernetes
* Prometheus outside of Kubernetes
* Prometheus via OpenTelemetry Collector

Dynatrace integrates gauge and counter metrics from Prometheus exporters and servers. These metrics are then available for charting, alerting, and analysis within Dynatrace. See the list of available Prometheus exporters in the [Prometheus documentationï»¿](https://prometheus.io/docs/instrumenting/exporters/) or in the [list maintained by the communityï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations).

## Prometheus in Kubernetes

In Kubernetes, Dynatrace supports scraping of any HTTP(s) endpoint offering metrics in OpenMetrics format (for example, Prometheus exporters). Using Dynatrace-specific annotations, you can specify which pods or services to scrape.

* Learn how to collect [Prometheus metrics in Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

## Prometheus outside of Kubernetes

Dynatrace provides a scalable means to ingest Prometheus metrics directly from the source, without Kubernetes. This works fully automatically and works best if OneAgent is installed on the box where the Prometheus metrics originate, but it can also be done in a fully agentless manner when OneAgent can't be installed on the box.

* Learn how to collect Prometheus metrics without Kubernetes using [Extensions 2.0 Prometheus data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.").

## Prometheus via OpenTelemetry Collector

For environments that require greater customization, Dynatrace allows the ingestion of Prometheus metrics using the OpenTelemetry Collector. To get started, see [Scrape data from Prometheus](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.").


---


## Source: statsd.md


---
title: Send StatsD metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd
scraped: 2026-02-15T21:11:51.315142
---

# Send StatsD metrics to Dynatrace

# Send StatsD metrics to Dynatrace

* Latest Dynatrace
* 5-min read
* Updated on Jun 18, 2025

StatsD is an industry standard for communicating arbitrary statistics and other metrics in a vendor-independent way via UDP. We recommend that you use Dynatrace OneAgent to ingest your metrics, as OneAgent comes with a StatsD daemon out of the box. This means that any application or library that supports StatsD can send metrics to Dynatrace. You only need to install OneAgent and make sure that your StatsD client uses the right port (`18125` by default).

Supported OneAgent

StatsD daemon is only available on OneAgent installed on the VM or host that you want to monitor. OneAgent deployed on Kubernetes, for example using Dynatrace Operator, isn't supported. For Kubernetes environments, we recommend [remote StatsD monitoring](#remote) using an environment ActiveGate.

If you can't install OneAgent on a host with your StatsD metrics, however, you can use an ActiveGate to act as a remote listener.

## Choose your StatsD ingestion method

OneAgent

ActiveGate

OpenTelemetry Collector

Use OneAgent for direct installation on the host with StatsD. For more details, go to [OneAgent listener](#oneagent-listener).

If OneAgent cannot be installed on the host, use ActiveGate as a remote listener to collect StatsD metrics. For more details, go to [Remote StatsD](#remote-statsd).

For distributed environments or when using Kubernetes, OpenTelemetry Collector provides a solution to ingest StatsD metrics into Dynatrace. For more details, see [Ingest data from StatsD](/docs/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.").

## Enable DynatraceStatsD

The DynatraceStatsD listener comes with OneAgent version 1.201+. You only need to enable DynatraceStatsD metric ingestion at the environment, host, or host group level. Note that the host-level and host group-level configurations override the environment configuration.

Enable at the environment level

To enable DynatraceStatsD metric ingestion at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable Dynatrace StatsD**.

Enable at the host group level

To enable DynatraceStatsD metric ingestion at the host group level

1. Go to **Settings** and select **Monitoring overview** > **Hosts**.
2. Select the host group name for a chosen host.
3. On the **Host group settings** page, select **Extension Execution Controller**.
4. Turn on **Enable Dynatrace StatsD**.

Enable for a single host

To enable DynatraceStatsD metric ingestion only for selected hosts

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.
6. Turn on **Enable Dynatrace StatsD**.

Enable remote StatsD

ActiveGate version 1.227+

If you can't use OneAgent to ingest StatsD metrics, you can use an Environment ActiveGate as your DynatraceStatsD ingestion point. Your ActiveGate needs to be able to connect to your StatsD client over UDP.

DynatraceStatsD metric ingestion is disabled by default on an ActiveGate.

To enable DynatraceStatsD metric ingestion

1. Edit the `extensionsuser.conf` file in the following directory

   * Linux
     `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
   * Windows
     `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
2. Set the `statsdenabled` parameter to `true`:

   ```
   statsdenabled=true
   ```
3. Restart the Extension Execution Controller service.

   * Linux
     Run the following commands:

     + for systems with SystemV:

       ```
       service extensionsmodule stop



       service extensionsmodule start
       ```
     + for systems with systemd:

       ```
       systemctl stop extensionsmodule



       systemctl start extensionsmodule
       ```
   * Windows
     Use **Task Manager** and restart the `Dynatrace Extensions Controller` service or run the following commands:

     ```
     net stop "Dynatrace Extensions Controller"



     net start "Dynatrace Extensions Controller"
     ```

Note that the default port for remote StatsD is different than for the OneAgent DynatraceStatsD listener (`18126`). See [Remote StatsD](#remote-statsd).

This file is not modified during ActiveGate updates.

Make sure that your ActiveGate can connect to your StatsD client. For example, you should configure the DNS name for your ActiveGate and make sure that it works after a new IP address is assigned from DHCP.

## Communication port

### OneAgent listener

The default DynatraceStatsD UDP listening port for the OneAgent listener is `18125`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the metric ingestion port. Changing the port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

#### Check the ingestion port

Use the `--get-extensions-statsd-port` parameter to show the current DynatraceStatsd UDP listening port (default = `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Set a custom ingestion port

Use the `--set-extensions-statsd-port=<arg>` parameter to set a custom DynatraceStatsd UDP listening port.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Remote StatsD

The default DynatraceStatsD UDP listening port for a remote listener is `18126`.

To change the default `18126` listening port, modify the `StatsdPort` parameter in the ActiveGate `extensionsuser.conf` file:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Topology awareness

Using DynatraceStatsD with OneAgent, the host ID and host name context are added as dimensions to each metric automatically. For more information, see [Metric ingestion](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."). Note that we're already working on more automatic metric enrichments. For remote ingestion, no extra enrichment is added. If you want to add context to your metrics, you'll need to add dimensions of your choice to your StatsD metrics.

## Security

The DynatraceStatsD OneAgent listener only accepts input from localhost addresses. This means that only processes that are running on the same host as OneAgent can leverage the interface. This ensures that no unauthorized programs are sending data to your Dynatrace environment.

## StatsD metric format

DynatraceStatsD accepts the following metrics in the [native StatsD formatï»¿](https://github.com/statsd/statsd/blob/master/docs/metric_types.md):

* `count`

  ```
  <metric name>:<value>|c
  ```
* `gauge`

  ```
  <metric name>:<value>|g
  ```
* `time`

  ```
  <metric name>:<value>|ms
  ```
* `histogram`

  ```
  <metric name>:<value>|h
  ```
* `set` OneAgent version 1.303+

  ```
  <metric name>:<value>|s
  ```
* `distribution`

  ```
  <metric name>:<value>|d
  ```

DynatraceStatsD extends the original protocol to enable you to also send dimensions. Use the following format:

```
<metric name>:<value>|g|#<Dimension1>:<value>,<Dimension2>:<value>
```

## Datasource limits and performance

The limits are based on the test that deploys a Linux machine in the AWS cloud. The purpose of this test is to determine how much StatsD load the infrastructure framework can handle.

### Hardware specification

OneAgent and ActiveGate are installed in a Linux-based VM in Amazon EC2 [c5.largeï»¿](https://dt-url.net/rv031ec) instance type.

* CPU: x2
* RAM: 4 GiB
* Storage: EBS
* Network bandwidth: up to 10 GBPS

|  | Total records | Packets | Lines per packet | Connections | Metrics |
| --- | --- | --- | --- | --- | --- |
| StatsD on OneAgent | 290,000 | 11,600 | 25 | 1 | 1 |
| StatsD on ActiveGate | 345,000 | 13,800 | 25 | 1 | 1 |


---


## Source: telegraf.md


---
title: Send Telegraf metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf
scraped: 2026-02-06T16:28:34.508791
---

# Send Telegraf metrics to Dynatrace

# Send Telegraf metrics to Dynatrace

* Latest Dynatrace
* 2-min read
* Published Oct 15, 2020

[Telegrafï»¿](https://github.com/influxdata/telegraf) is a plugin-driven server agent for collecting, processing, aggregating, and writing metrics. Telegraf comes with the Dynatrace Output Plugin that enables you to easily send Telegraf metrics to Dynatrace.

## Enable Telegraf ingestion

Telegraf metric ingestion comes with OneAgent version 1.201+. The easiest configuration scenario is to install Telegraf and OneAgent on the same host. Then you only need to enable the Dynatrace Output Plugin in your Telegraf configuration (Telegraf version 1.16+) and enable Telegraf metric ingestion at the environment or host level in your Dynatrace configuration. Note that the host-level configuration overrides the environment-level configuration.

Enable the Dynatrace Output Plugin in Telegraf configuration

### Telegraf and OneAgent on the same host

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.16/administration/configuration/).
2. Uncomment the `[[outputs.dynatrace]]` line.
3. Optional Uncomment the `prefix = "telegraf."` line and set the prefix to easily find the Telegraf ingested metrics. The prefix will also be visible in the Dynatrace metric key.
4. Save the file.

```
# # Send telegraf metrics to a Dynatrace environment



[[outputs.dynatrace]]



#   ## For usage with the Dynatrace OneAgent you can omit any configuration,



#   ## the only requirement is that the OneAgent is running on the same host.



#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.



#   ##



#   ## Your Dynatrace environment URL.



#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)



#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"



#   url = ""



#



#   ## Your Dynatrace API token.



#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API



#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.



#   api_token = ""



#



#   ## Optional prefix for metric names (e.g.: "telegraf.")



prefix = "telegraf."



#



#   ## Optional TLS Config



#   # tls_ca = "/etc/telegraf/ca.pem"



#   # tls_cert = "/etc/telegraf/cert.pem"



#   # tls_key = "/etc/telegraf/key.pem"



#



#   ## Optional flag for ignoring tls certificate check



#   # insecure_skip_verify = false



#



#



#   ## Connection timeout, defaults to "5s" if not set.



#   timeout = "5s"
```

### No OneAgent on the host

If you can't install OneAgent on the Telegraf-monitored host, you can configure the Dynatrace Output Plugin to push metrics directly to your Dynatrace environment through [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

#### Prerequisites

* [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the **Ingest metrics data points** scope.
* Your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Uncomment the `# [[outputs.dynatrace]]` line.
3. Optional Uncomment the `# prefix = "telegraf."` line and set the prefix to easily find the Telegraf ingested metrics. The prefix will also be visible in the Dynatrace metric key.
4. Uncomment the `# api_token = ""` line and add your API token, for example `api_token = "abcdefjhij1234567890"`
5. Uncomment the `# url = ""` line and add your Dynatrace metric API endpoint. For example,

   * Dynatrace SaaS `url = "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"`
   * Dynatrace Managed `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest`
6. Save the file.

```
# # Send telegraf metrics to a Dynatrace environment



[[outputs.dynatrace]]



#   ## For usage with the Dynatrace OneAgent you can omit any configuration,



#   ## the only requirement is that the OneAgent is running on the same host.



#   ## Only setup environment url and token if you want to monitor a Host without the OneAgent present.



#   ##



#   ## Your Dynatrace environment URL.



#   ## For Dynatrace OneAgent you can leave this empty or set it to "http://127.0.0.1:14499/metrics/ingest" (default)



#   ## For Dynatrace SaaS environments the URL scheme is "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



#   ## For Dynatrace Managed environments the URL scheme is "https://{your-domain}/e/{your-environment-id}/api/v2/metrics/ingest"



#   url = "https://abd12345.live.dynatrace.com/api/v2/metrics/ingest"



#



#   ## Your Dynatrace API token.



#   ## Create an API token within your Dynatrace environment, by navigating to Settings > Integration > Dynatrace API



#   ## The API token needs data ingest scope permission. When using OneAgent, no API token is required.



api_token = "abcdefjhij1234567890"



#



#   ## Optional prefix for metric names (e.g.: "telegraf.")



prefix = "telegraf."



#



#   ## Optional TLS Config



#   # tls_ca = "/etc/telegraf/ca.pem"



#   # tls_cert = "/etc/telegraf/cert.pem"



#   # tls_key = "/etc/telegraf/key.pem"



#



#   ## Optional flag for ignoring tls certificate check



#   # insecure_skip_verify = false



#



#



#   ## Connection timeout, defaults to "5s" if not set.



#   timeout = "5s"
```

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a single host

1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

## Topology awareness

When OneAgent and Telegraf are installed on the same host, the host ID and host name context are automatically added to each metric as dimensions. Learn how to [enrich your metrics with other Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") and apply Dynatrace-AI causation details to your ingested data.

## Metric format

Provided data points must follow the [Metrics ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

## Communication port

The Telegraf Dynatrace Output Plugin sends metrics to the [OneAgent metric API](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") endpoint.

The default metric ingestion port is `14499`. If necessary, you can use the [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") command to check or change the port. Changing the metric ingestion port requires restart of OneAgent. Add [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to the command to restart OneAgent automatically.

### Check the ingestion port

Use the `--get-extensions-ingest-port` parameter to show the current local ingestion port, `14499` by default.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Set a custom ingestion port

Use the `--set-extensions-ingest-port=<arg>` parameter to set a custom local ingestion port.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Configure proxy

Configure your host proxy to allow localhost traffic going to the metric ingestion port, `14499` by default.

If you change the default OneAgent communication port, make sure you also update the Telegraf configuration.

1. Edit `telegraf.conf`, the [Telegraf configuration fileï»¿](https://docs.influxdata.com/telegraf/v1.15/administration/configuration/).
2. Set the `url` property to `url = "http://127.0.0.1:<your-custom-port>/metrics/ingest"`.
3. Save the file.

Note that changing the port for Telegraf ingested metrics also affects OneAgent REST API and Scripting integration.


---


## Source: custom-metric-metadata.md


---
title: Custom metric metadata
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata
scraped: 2026-02-15T21:27:33.958849
---

# Custom metric metadata

# Custom metric metadata

* Latest Dynatrace
* 1-min read
* Updated on Nov 25, 2025

To add more context to data points and their dimensions, your custom metric can carry additional useful information, such as the unit of measurement, display name, and value ranges.

You can provide such information via custom metric metadata. Metadata is stored independently from data points and tied together by the metric key. You can push data points and set metadata in any order.

You cannot provide metadata for built-in or calculated metrics; metadata is supported only for custom ingested metrics.

## Available parameters

The following parameters are available for metric metadata.

Parameters

Example JSON

Parameter

Type

Description

displayName

string

The name of the metric in the user interface.

description

string

A short description of the metric.

unit

string

The unit of the metric.

Find the possible values in the description of the **unit** field for [built-in metrics](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.").

sourceEntityType

string

The entity type of the metric. Used for management zone filtering.

For details, see [Metric entity type](/docs/analyze-explore-automate/metrics-classic/metrics-mz#entity-based-rules "How to filter metrics by management zone and related security considerations").

tags

string[]

A list of tags applied to the metric.

metricProperties

[MetricProperties](#properties)

A list of the metric's properties.

dimensions

[MetricDimensions](#dimensions)[]

A list of the metric's dimensions.

#### The `MetricProperties` object

Properties of a metric.

Parameter

Type

Description

minValue

integer

The minimum allowed value of the metric.

maxValue

integer

The maximum allowed value of the metric.

rootCauseRelevant

boolean

Whether (`true` or `false`) the metric is related to a root cause of a problem.

A root-cause relevant metric represents a strong indicator for a faulty component.

impactRelevant

boolean

Whether (`true` or `false`) the metric is relevant to a problem's impact.

An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.

valueType

string

The type of the metric's value. You have these options:

* `score`: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.
* `error`: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count.

latency

integer

The reporting delay of the metrics, in minutes.

The delay caused by constraints of cloud vendors or other third-party data sources that leads to a latency in data ingest on the Dynatrace side.

#### The `MetricDimensions` object

A dimension of the metric.

Parameter

Type

Description

key

string

The key of the dimension to be used in the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

displayName

string

The name of the dimension in the user interface.

```
{



"displayName": "Total revenue",



"description": "Total store revenue by region, city, and store",



"unit": "Unspecified",



"sourceEntityType": "string",



"tags": ["KPI", "Business"],



"metricProperties": {



"maxValue": 1000000,



"minValue": 0,



"rootCauseRelevant": false,



"impactRelevant": true,



"valueType": "score",



"latency": 1



},



"dimensions": [



{



"key": "city",



"displayName": "City name"



},



{



"key": "country",



"displayName": "Country name"



},



{



"key": "region",



"displayName": "Sales region"



},



{



"key": "store",



"displayName": "Store #"



}



]



}
```

## Set metric metadata

Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") call of the Settings API to provide metadata for your metric. Use the following parameters in the payload:

| Field | Value |
| --- | --- |
| scope | metric-{your-metric-key} |
| schemaId | builtin:metric.metadata |
| value | The desired set of metadata. See the available fields above. |

Example payload

```
[



{



"scope": "metric-business.shop.revenue",



"schemaId": "builtin:metric.metadata",



"value": {



"displayName": "Total revenue",



"description": "Total store revenue by region, city, and store",



"unit": "Unspecified",



"sourceEntityType": "string",



"tags": ["KPI", "Business"],



"metricProperties": {



"maxValue": 1000000,



"minValue": 0,



"rootCauseRelevant": false,



"impactRelevant": true,



"valueType": "score",



"latency": 1



},



"dimensions": [



{



"key": "city",



"displayName": "City name"



},



{



"key": "country",



"displayName": "Country name"



},



{



"key": "region",



"displayName": "Sales region"



},



{



"key": "store",



"displayName": "Store #"



}



]



}



}



]
```

Alternatively, you can:

* Send metadata via the [ingestion protocol](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metadata "Learn how the data ingestion protocol for Dynatrace Metrics API works.").
* Configure a metric's metadata in [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

## View metric metadata

You can retrieve the metadata of a metric via the [GET metric descriptor](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") call of the Metrics v2 API or via the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

## Related topics

* [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")


---


## Source: metric-ingestion-protocol.md


---
title: Metric ingestion protocol
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol
scraped: 2026-02-15T21:23:24.222038
---

# Metric ingestion protocol

# Metric ingestion protocol

* Latest Dynatrace
* 6-min read
* Updated on Jul 08, 2025

This page describes the protocol for metric ingestion in Dynatrace.

## Syntax

The general syntax of metric ingestion is the following:

```
metric.key,dimensions payload
```

### Metric key Required

The key of the metric you're submitting. It consists of sections, separated by dots, for example `first.second.third`.

Allowed characters are lowercase and uppercase letters, numbers, hyphens (`-`), and underscores (`_`). The following restrictions apply:

* Non-latin letters (like `Ã¶`) are not allowed.
* Metric keys cannot start with a number or a hyphen (`-`).
* Sections cannot start with a hyphen (`-`).
* The length of the key must be in range from 3 to 255 characters.

The metric key ends either at the first comma (if you're specifying dimensions) or at the first whitespace (if you omit dimensions).

Your provided key may be suffixed automatically depending on the payload. For details, see [Payload](#payload).

Avoid sections with non-alphabetical characters. You will need to escape these characters in the [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") when you [query your metric](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

### Dimension Optional

If you want to omit dimensions, provide the payload right after the metric key, separated by a whitespace.

Dimensions are specified as `key="value"` pairs. You can specify up to 50 dimensions, separated by commas (`,`).

Allowed characters for the key are lowercase letters, numbers, hyphens (`-`), periods (`.`), colons (`:`) and underscores (`_`). Special letters (like `Ã¶`) are not allowed. The key can be in the `key.key-section` format.

Pass the dimension value as a quoted string. If you want to pass quotes (`"`) and/or backslashes (`\`) in a dimension value, make sure you escape them with a backslash (`\`). For example:

```
workHours,team="devops\\bugfixing",project="\"product\"_improvement" 1000
```

Currently we support only one dimension value per dimension key. If the same dimension key is specified multiple times in a single payload (for example, `ipaddress="192.168.100.1",ipaddress="10.0.0.1"`) the payload is valid, but only one value is accepted.

#### Dynatrace reserved dimensions

The `dt.entity.<entity_type>` key is a Dynatrace reserved dimension key that relates the metric to the monitored entity provided as dimension value (for example, the `dt.entity.host=HOST-06F288EE2A930951` dimension maps the data points to the host with the ID of **HOST-06F288EE2A930951**).

### Payload Required

The general format of the payload is the following:

```
format,dataPoint timestamp
```

#### Format Optional

You can specify a payload in two formats: gauge (`gauge`) or count value (`count`). Specify the format before you specify data points and separate it from data points with a comma (for example `gauge,80.6`).

A metric key can only refer to one payload type with Classic metrics. Thus, your provided metric key is automatically suffixed with `.count` for the payload type `count` unless the key already ends with `.count`. Vice versa, if the key of a metric with type gauge ends with `.count`, it is suffixed with `.gauge`.

Grail metrics do not apply the `.count` and `.gauge` suffixes.

gauge

count

For the gauge format, you can specify the following statistic summaries:

* `min`
* `max`
* `sum`
* `count`âthe number of measurements included in the data point.

You can omit the format if you're using a single value gauge payload. In that case, the provided value is used for all summaries and the count is set to `1`.

For example, a payload of `80.6` equals `gauge,min=80.6,max=80.6,sum=80.6,count=1`.

Usage of the count format will automatically create a new metric with the `your-metric-key.count` key. To specify the count value, you must provide the delta field: `count,delta=500`.

Data points of the `count` type are **deltas** between the previous and current data points. For example, if the initial data point has the value of `500` and the second data point has the value of `1,000`, the actual stored value at the timestamp of the second data point is `1,500`.

#### Data point Required

A data point might include one or, in the case of the gauge format, several measures. For several measures, provide them with statistic summaries. You must specify all the summaries.

A data point of the `count` type is the **delta** between the previous and current data points.

#### Timestamp Optional

The format of the timestamp is UTC milliseconds. The allowed range is between **1 hour** into the past and **10 minutes** into the future from now. Data points with timestamps outside of this range are rejected.

If no timestamp is provided, **the current timestamp of the server** is used.

### Metadata Optional

You can provide custom metric metadata via the ingestion protocol. The ingestion protocol supports only creation of metadata. If metadata for the same metric is specified several times in the payload, only the first occurrence is used. To view or update metadata, use either [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") or the Settings API (to learn how to compose an API payload, see [Set metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata#create "Provide metadata for your custom metric.")).

```
#metric.key <payload-format> dt.meta.<property>="<value>"
```

Set either `gauge` or `count` in place of `<payload-format>`. Usage of the count format will automatically create a new metric with the `metric-key.count` key.

The following properties are available. To specify several properties, separate them with a comma (`,`).

Key

Type

Description

dt.meta.displayName

string

The name of the metric in the user interface.

dt.meta.description

string

A short description of the metric.

dt.meta.unit

string

The unit of the metric. Find the possible unit values in the [Dynatrace Developerï»¿](https://developer.dynatrace.com/reference/units/) documentation.

## Examples

The general syntax of metric ingestion is the following:

```
metric.key,dimensions payload



#metric.key <payload-format> dt.meta.<property1>="<value>", dt.meta.<property2>="<value>"
```

### Dimensions

Here's an example of a metric using multiple dimensions, `team` and `businessapp` that describe the reported datapoints.

```
mymetric,team=teamA,businessapp=hr 1000
```

Here's the same example with the timestamp of the data point.

```
mymetric,team=teamA,businessapp=hr 1000 1609459200000
```

### GAUGE metric

Gauge is the default data, so you can keep the data type optional in case you want to send gauge values:

```
cpu.temperature,hostname=hostA,cpu=1 55



cpu.temperature,hostname=hostA,cpu=2 45
```

Here's an example with the `gauge` data type used nonetheless.

```
cpu.temperature,hostname=hostA,cpu=1 gauge,45
```

You can also provide consolidated information about multiple datapoints recorded on the client side before sending it to Dynatrace. In the example below, 2 datapoints are summarized and the minimum, maximum, sum value and number of datapoints are sent in a single line.

```
cpu.temperature,hostname=hostA,cpu=1 gauge,min=17.1,max=17.3,sum=34.4,count=2
```

You can also relate measurements to existing host entities by making use of the `dt.entity.host` reserved dimension key.

```
cpu.temperature,dt.entity.host=HOST-4587AE40F95AD90D,cpu=1 gauge,min=17.1,max=17.3,sum=34.4,count=2
```

You don't need to specify the `dt.entity.host` dimension when using local ingestion methods via OneAgent, that is [dynatrace\_ingest](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") and [local API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), because for this ingestion methods, the host context is added automatically.

### COUNT metric

For a count type of metric, the delta is calculated and provided by the client that sends the metric to Dynatrace, which in the case below represents new users reported by region.

```
new_user_count,region=EAST count,delta=50



new_user_count,region=WEST count,delta=150
```

### Create metadata

Here's an example of providing metadata for a `cpu.temperature` metric.

```
#cpu.temperature gauge dt.meta.unit=count,dt.meta.description="The temperature of the CPU",dt.meta.displayname="CPU temperature"
```

### API call

See [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API.") for an example API call.

## Related topics

* [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")


---


## Source: events-entity-extraction.md


---
title: Event topology extraction and mapping
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/events-entity-extraction
scraped: 2026-02-15T21:30:16.664254
---

# Event topology extraction and mapping

# Event topology extraction and mapping

* Latest Dynatrace
* 4-min read
* Updated on Jan 28, 2026

Every event stored in Dynatrace is mapped to a monitored entity that it impacts. Dynatrace Intelligence uses this topological knowledge in its automated root cause analysis. An example of a topological context is a CPU usage spike that is mapped to the host where it was observed. However, once you start ingestion of your own data sources into Dynatrace, out-of-the-box topological mapping might not be sufficient anymore: you might need to map events to your custom entities.

The [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") enables you to include metadata in events you're ingesting into Dynatrace. With such enrichment, you can include topological context in the event itself. Dynatrace can extract this information and map an incoming event to the entity it belongs to.

## Map to predefined entity types

To map an event to an entity of a predefined type, specify it in the **entitySelector** field. Note that you can map an event only to entities that have been active within the last 24 hours. If no entity matches your selector or the selector is omitted altogether, the event is mapped to the environment level. No additional configuration is needed. To learn the entity selector syntax, see [Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Map to generic entity types

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define custom entity type**](#define-type)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Provide event metadata**](#configure-event-metadata)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Define extraction rules**](#extract-map)

### Step 1 Define custom entity type

You can map events only to entities of an existing custom-defined generic type. If you don't have the required type defined yet, create it. To learn how, see [**Define new entity type**](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology#define-new-entity-type "Learn how to create a custom topology model that's suited to your telemetry data.").

You can't extract entities of predefined types and re-map events to them.

### Step 2 Provide event metadata

To be able to extract generic entities from events, you need to provide the relevant information in the event configuration. The following elements of event properties control the feature. You can find descriptions on all event configuration fields in [**POST an event**](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Name

ID

Description

Allow entity remapping

`dt.event.allow_entity_remapping`

Defines whether the remapping is allowed. Set to `"true"` to allow remapping to extracted entities.

If set to `"false"`, no remapping will happen, even if there's a matching extraction rule. However, if there **is** a matching rule, the extracted entity will still be created/updated. You can use such incoming events to keep your custom entities up-to-date.

Note that the values of the property must be of the `String` type.

Preferred entity type for remapping

`dt.event.preferred_entity_type`

Defines the generic entity type to which the event should be mapped. Use this property if your event metadata contains multiple entities of different types. If no entity of the specified type is extracted, no remapping is applied. If not set, Dynatrace Intelligence automatically decides on the appropriate entity type.

Entity identification

User-defined

Defines the ID of your entity. Since generic entities are user-defined, so is the ID of this property. As an illustration, for our [Easy Shipping LTD logistics example](/docs/ingest-from/extend-dynatrace/extend-topology#custom-topology-model-in-action "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to."), this property could use the key **trucknr**.

Show an example JSON

```
{



"eventType": "CUSTOM_ALERT",



"title": "Truck fuel low",



"timeout": 5,



"properties": {



"trucknr": "13",



"dt.event.allow_entity_remapping": "true",



"dt.event.preferred_entity_type": "logistics:truck"



}



}
```

### Step 3 Define extraction rules

To assign an extraction rule to a generic entity type

1. Go to **Settings** > **Topology model** > **Generic types**.
2. Expand the generic type to which you want to map your events.
3. Select **Add extraction rule**.
4. In the **Extracted ID pattern** field, specify the placeholder of the event property that holds the entity ID. For our Easy Shipping example, that would be `{trucknr}`.
5. Optional In the **Instance name pattern**, provide the human-friendly pattern for names of extracted entities. Use placeholders to automatically create unique names. For our Easy Shipping example, that could be `Truck {trucknr}`.
6. Select **Add source**.
7. Select **Events** as the data source type.
8. In the condition field, use the `$eq()` condition with the event type value. For our Easy Shipping example, that would be `$eq(CUSTOM_ALERT)`.
9. Save your changes.

## Troubleshooting

If the remapping fails, you can retrieve the diagnostic information on an event overview page or via the [**GET an event**](/docs/dynatrace-api/environment-api/events-v2/get-event "View parameters of an event via the Events API v2.") request. Look for the **Entity remapping failure information** (`dt.event.entity_remapping_failure_info`) field.

## Related topics

* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.")


---


## Source: network-topology.md


---
title: Generic network topology
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology/network-topology
scraped: 2026-02-15T21:18:15.556965
---

# Generic network topology

# Generic network topology

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jan 29, 2025

The [SNMP Autodiscoveryï»¿](https://www.dynatrace.com/hub/detail/snmp-autodiscovery) extension scans through subnets and helps users discover their full inventory of SNMP-enabled network devices. In addition, this extension also includes a topology model that aims to be generic enough that most sources for data relating to network devices can be expressed through a simple set of common entities: network device, network port, and network interface.

We've started applying this model to some of our most popular SNMP extensions for technologies like Cisco, F5, Palo Alto, and Juniper. This has allowed us to unify all network entities, simplify our queries, and show relevant network data regardless of the monitoring source.

To see how the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app visualizes this data, see [Supercharge your end-to-end infrastructure and operations observability experienceï»¿](https://dt-url.net/vm03xd1) (Dynatrace blog).

## Scenario

This guide walks you through the concepts that tie this topology together, and explain how youâas an extension developer or data integratorâcan leverage the same model.

As this is a technical guide, we will take a complete example based on a trimmed-down version of the F5 BIG-IP extension.

Three extension manifests are attached to this guide:

* `1_initial.yaml` is the unmodified extension.

  It monitors an F5 load balancer, sending data to Dynatrace, but without any awareness of the model.
* `2_basic.yaml` showcases basic usage.

  Dynatrace now knows that the F5 load balancer is a network device with interfaces and ports. Other apps will show it too.
* `3_advanced.yaml` showcases advanced usage.

  The network device and interface now have access to more data. The network device has also been given additional attributes and charts to display.

See the [Manifest files](#manifest-files) section below to learn more about these files.

You can use an online tool like [diffcheckerï»¿](https://www.diffchecker.com/text-compare/) to better focus on the changes between the three manifests.

## Step 1 Key concepts

It's important to understand that the topology model is defined largely by the SNMP Autodiscovery extension. Other extensions and integrations only need to ensure the right data is sent to Dynatrace and optionally define any additional charts to display as part of the web UI.

Let's have a look at the topology entities and relationships.

### Network device

(`network:device`)

* A network device is like a physical device on the network. This is the core entity that hosts the OS and runs the technology required to deliver network communications and other capabilities.
* A network device is identified by its management IP address and labeled by the system name.

### Network port

(`network:port`)

* A network port is like a physical hardware network port on a network device.
* A network port is identified and labeled by its MAC address.

### Network interface

(`network:interface`)

* A network interface is like a physical or virtual network interface (NIC). This is typically the first point of reference in device-to-device network communications.
* A network interface is identified by a combination of MAC address and interface name, and labeled by its name.

### Relationships

These entity types are tied together by the following relationships:

* `network:port` `-runsOn->` `network:device`
* `network:interface` `-runsOn->` `network:device`
* `network:interface` `-isChildOf->` `network:port`

## Step 2 Basic usage

As mentioned earlier, other extensions and integrations only need to send the data in the correct format to leverage this topology. Mandatory dimensions must be present on all metrics, whereas optional dimensions can be added to a single metric to reduce unnecessary data splitting.

### Dimensions and metrics for network devices

The following metrics and dimensions are available for network devices.

* **Mandatory dimensions**:

  + Key: `device.address`

    Usage: identifies each device and decides when new entity instances should be created
  + Key: `monitoring.mode`

    Usage: must have fixed value "Extension". This affects the UI and tell Dynatrace this entity is monitored.
  + Key: `sys.name`

    Usage: labels the device, giving the entity its name.
  + Key: `device.type`

    Usage: a string to represent the type of device. Can be the name of a technology, make/model, or simply a label like "L3 Switch". Will populate the `devType` attribute of the entity.
* **Optional (recommended) dimensions**:

  + Key: `device.port`

    Usage: registers a listening port on the device. No additional entities are created, but the `dt.listen\ports` attribute will be populated from it.
  + Key: `sys.description`

    Usage: registers the deviceâs description against the devDescription attribute. Can be manufacturer information or any descriptive text.
* **Metrics**:

  + Key: `com.dynatrace.extension.network_device.sysuptime`

    Description: The time, in system ticks (1/100 second), since the last system reboot.
  + Key: `com.dynatrace.extension.network_device.cpu_usage`

    Description: The system's CPU usage expressed as a percentage
  + Key: `com.dynatrace.extension.network_device.cpu_ratio`

    Description: The system's CPU usage expressed as a ratio
  + Key: `com.dynatrace.extension.network_device.memory_used`

    Description: The amount of memory, in kilobytes, used by the device
  + Key: `com.dynatrace.extension.network_device.memory_free`

    Description: The amount of memory, in kilobytes, currently free on the device
  + Key: `com.dynatrace.extension.network_device.memory_total`

    Description: The total (used and free) amount of memory, in kilobytes, available on the device
  + Key: `com.dynatrace.extension.network_device.memory_usage`

    Description: The current memory used by the device, expressed as a percentage of total memory

### Dimensions and metrics for network interfaces

The following are metrics and dimensions available for network interfaces.

* **Mandatory dimensions**:

  + Key: `mac.address`

    Usage: in combination with the name, identifies each interface and when to create new entity instances. Separately, it also identifies network ports and when to create new instances.
  + Key: `if.name`

    Usage: in combination with the MAC address, identifies each interface. It also gives each interface entity a name.
* **Metrics**:

  + Key: `com.dynatrace.extension.network_device.if.status`

    Description: A state metric representing a network interface, whose value is always 1 and its dimensions indicate its state details.

    Additional dimensions (extracted as entity attributes):
  + Key: `oper.status`

    Usage: The operational state of the interface (up/down/etc.).
  + Key: `admin.status`

    Usage: The admin state of the interface (up/down/etc.).
  + Key: `if.speed`

    Usage: The speed/bandwidth of the interface.
  + Key: `com.dynatrace.extension.network_device.if.bytes_in.count`

    Description: The volume of traffic, in bytes, inboud to the network interface.
  + Key: `com.dynatrace.extension.network_device.if.bytes_out.count`

    Description: The volume of traffic, in bytes, outbound from the network interface.

### What can be expected at this stage?

This should guarantee that network device, network port, and network interface entities are created correctly from your data. At this point, you can leverage either the (Classic) Technologies or ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app to visualize these devices.

* In the (Classic) Technologies app, navigate to `../ui/apps/dynatrace.classic.technologies/ui/entity/list/network:interface`

  ![Network devices](https://dt-cdn.net/images/network-devices-classic-1105-6a410f8f74.png)
* In the ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") Infrastructure & Operations app, select the **Network Devices** tab

  ![Network devices](https://dt-cdn.net/images/389541815-e685532f-7ddc-40c5-9b08-0d40e494e4af-1177-f87f6dc4be.png)

## Step 3 Advanced usage

Building on top of the previous changes, this section focuses on how to extend the network model with additional metrics, relationships to existing entities, and UI customizations.

In many cases, you probably already have an extension or integration that sends specialized data about a particular type of network device. In these situations, the model can be used to draw some âsame asâ relationships from your existing entities to the generic ones, effectively attaching new metrics to them, customizing their attributes, and injecting some of your existing charts into their UI.

Once you implemented the proposed changes, follow these additional steps:

1. Attach your existing data to the network device:

   * Create a new entry in `topology.types` as follows:

     ```
     - name: network:device



     enabled: true



     displayName: Network device



     rules: [] # You will populate this at the next step
     ```
   * Add rules to attach your data to the entity (replace `[]`)

     Note: You can identify an existing entity type that resembles a network device and copy all the rules from its definition

     Ensure that every rule defines the following:

     ```
     - idPattern: network_device_{device.address}



     instanceNamePattern: "{sys.name}"



     role: default
     ```

     Note: `device.address` and `sys.name` are placeholders that can hold any other dimension, but they must identify a management IP address and a device name.
2. Attach your existing data to the network interface:

   * Create a new entry in `topology.types` as follows:

     ```
     - name: network:interface



     enabled: true



     displayName: Network interface



     rules: [] # You will populate this in the next step
     ```
   * Add rules to attach your data to the entity (replace the above `[]`).

     Note: You can identify an existing type that resembles a network interface and copy all the rules from its definition.

     Ensure that every rule defines the following:

     ```
     - idPattern: network_interface_{mac.address}_{if.name}



     instanceNamePattern: "{if.name}"



     role: default
     ```

     Note: `mac.address` and `if.name` are placeholders that can hold any other dimension, but they must identify a MAC address and an interface name.
3. Draw the "same as" relationships:

   * Create two entries in `topology.relationships`. Each should be based on data similar to what you used in the previous steps.

     ```
     - fromType: ""  # Add your existing entity type that resembles a network device



     typeOfRelation: SAME_AS



     toType: `network:device`



     sources:



     - sourceType: Metrics



     condition: ""  # Match any of the metrics that you used for the network:device entity rule



     - fromType: ""  # Add your existing entity type that resembles a network interface



     typeOfRelation: SAME_AS



     toType: `network:interface`



     sources:



     - sourceType: Metrics



     condition: ""  # Match any of the metrics that you used for the network:interface entity rule
     ```
4. Customize the UI:

   * Create a new entry in `screens` for the network device:

     ```
     screens:



     - entityType: network:device
     ```
   * Display a drilldown link to the specialized entity:

     Add a `RELATION` type property to the `propertiesCard` pointing to your existing entity

     ```
     propertiesCard:



     properties:



     - type: RELATION



     relation:



     # replace your_type with your existing entity type



     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))



     displayName: Linked entity



     conditions:



     # Replace your_type with your existing entity type



     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension
     ```
   * Display your existing charts on the Network Device screen:

     The easiest way is to inject them by reference from your existing entity's screen.

     **Note:** Never define anything in `detailsSettings`, always in `detailsInjections`.

     ```
     detailsInjections:



     - type: CHART_GROUP



     key: my-custom-chart



     # replace your_type with your existing entity type



     entitySelectorTemplate: type(your_type),fromRelationships.isSameAs($(entityConditions))



     conditions:



     # Replace your_type with your existing entity type



     - relatedEntity|entitySelectorTemplate=type(your_type),fromRelationships.isSameAs($(entityConditions))



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension
     ```
   * Define new charts for the network device:

     ```
     detailsInjections:



     - type: CHART_GROUP



     key: my-custom-chart



     conditions:



     # Ensures it only appears on monitored devices



     - entityAttribute|devMonitoringMode=Extension



     chartsCards:



     - key: my-custom-chart



     type: CHART_GROUP



     # Rest of definition goes here...
     ```

### What can be expected at this stage?

The network device entity is associated with an extended set of metrics (coming from the specialized extension), reports additional attributes, displays some of the specialized extension's data on its details page, and retains a drilldown link to the specialized entity.

![Network device overview](https://dt-cdn.net/images/network-device-overview-1473-e9624340d5.png)

## Manifest files

### `1_initial.yaml`

This is the unmodified extension.

It monitors an F5 load balancer, sending data to Dynatrace, but without any awareness of the model.

Show me the `1_initial.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.0.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



topology:



types:



- name: f5lb:instance



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



screens:



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

### `2_basic.yaml`

This showcases basic usage.

Dynatrace now knows that the F5 load balancer is a network device with interfaces and ports. Other apps will show it too.

Show me the `2_basic.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.1.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



# In this example, we add the basic metrics & dimensions for the network model.



# We chose to spread them in-between the existing metrics where possible, but



# they could just as well be extracted into separate groups & subgroups.



snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



# Adding the mandatory dimensions here ensures they appear everywhere



- key: monitoring.mode



value: const:Extension



- key: sys.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.type



value: const:F5 Load balancer



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- key: com.dynatrace.extension.network_device.sysuptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: if.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- key: com.dynatrace.extension.network_device.if.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: com.dynatrace.extension.network_device.if.bytes_in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: com.dynatrace.extension.network_device.if.bytes_out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: com.dynatrace.extension.network_device.cpu_usage



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



- key: com.dynatrace.extension.network_device.memory_used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0



- key: com.dynatrace.extension.network_device.memory_total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0



topology:



types:



- name: f5lb:instance



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



screens:



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

### `3_advanced.yaml`

This showcases advanced usage.

The network device and interface now have access to more data. The network device has also been given additional attributes and charts to display.

Show me the `3_advanced.yaml` manifest file

```
name: custom:f5-load-balancer



version: 1.2.0



minDynatraceVersion: 1.289.0



author:



name: Dynatrace



# In this example, we add topology rules for customizing the network model.



# And modify the screens to customize the UI of the network device.



# All other changes done so far stay the same.



snmp:



- group: f5



interval:



minutes: 1



dimensions:



- key: instance.name



value: oid:1.3.6.1.2.1.1.5.0



- key: failover.state



value: oid:1.3.6.1.4.1.3375.2.1.14.3.1.0



- key: sync.state



value: oid:1.3.6.1.4.1.3375.2.1.14.1.1.0



# Adding the mandatory dimensions here ensures they appear everywhere



- key: monitoring.mode



value: const:Extension



- key: sys.name



value: oid:1.3.6.1.2.1.1.5.0



- key: device.type



value: const:F5 Load balancer



subgroups:



- subgroup: f5-instance-details



table: false



dimensions:



- key: instance.systemname



value: oid:1.3.6.1.4.1.3375.2.1.6.1.0



- key: instance.systemrelease



value: oid:1.3.6.1.4.1.3375.2.1.6.3.0



- key: instance.systemarch



value: oid:1.3.6.1.4.1.3375.2.1.6.5.0



- key: instance.productversion



value: oid:1.3.6.1.4.1.3375.2.1.4.2.0



metrics:



- key: f5.lb.sys.uptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- key: com.dynatrace.extension.network_device.sysuptime



value: oid:1.3.6.1.4.1.3375.2.1.6.6.0



- subgroup: f5-interface-details



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: if.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.1



- key: interface.enabled



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.8



- key: interface.status



value: oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.17



- key: mac.address



value: $networkFormat(const:macAddress, oid:1.3.6.1.4.1.3375.2.1.2.4.1.2.1.6)



metrics:



- key: f5.lb.sys.interface.status



value: const:1



- key: com.dynatrace.extension.network_device.if.status



value: const:1



- subgroup: f5-interface-metrics



featureSet: interface



table: true



dimensions:



- key: interface.name



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.1



metrics:



- key: f5.lb.sys.interface.stat.bytes.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: f5.lb.sys.interface.stat.bytes.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: com.dynatrace.extension.network_device.if.bytes_in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.3



type: count



- key: com.dynatrace.extension.network_device.if.bytes_out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.5



type: count



- key: f5.lb.sys.interface.stat.pkts.in.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.2



type: count



- key: f5.lb.sys.interface.stat.pkts.out.count



value: oid:1.3.6.1.4.1.3375.2.1.2.4.4.3.1.4



type: count



- subgroup: f5-cpu



table: false



featureSet: instance-cpu



metrics:



- key: com.dynatrace.extension.network_device.cpu_usage



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.29.0



- key: f5.lb.sys.global.host.cpu.idle1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.25.0



- key: f5.lb.sys.global.host.cpu.iowait1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.28.0



- key: f5.lb.sys.global.host.cpu.irq1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.26.0



- key: f5.lb.sys.global.host.cpu.softirq1min



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.27.0



- key: f5.lb.sys.global.host.cpu.stolen1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.40.0



- key: f5.lb.sys.global.host.cpu.system1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.24.0



- key: f5.lb.sys.global.host.cpu.user1m



value: oid:1.3.6.1.4.1.3375.2.1.1.2.20.22.0



- subgroup: f5-memory



table: false



featureSet: instance-memory



metrics:



- key: f5.lb.sys.host.memory.total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.1.0



- key: f5.lb.sys.host.memory.used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.2.0



- key: com.dynatrace.extension.network_device.memory_used



value: oid:1.3.6.1.4.1.3375.2.1.7.1.4.0



- key: com.dynatrace.extension.network_device.memory_total



value: oid:1.3.6.1.4.1.3375.2.1.7.1.3.0



topology:



types:



# These are already existing rules which we can copy & adjust



- name: f5lb:instance # Closely resembles a network device



displayName: F5 BIG-IP Instance



rules:



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime)



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: f5_instance_{instance.name}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: f5lb:interface # Closely resembles a network interface



displayName: F5 BIG-IP Interface



rules:



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status)



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: Status



displayName: Status



pattern: '{interface.status}'



role: default



- idPattern: f5_interface_{instance.name}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



# These are new rules added to customize the model



- name: network:device



enabled: true



displayName: Network device



rules:



- idPattern: network_device_{device.address} # must follow `network_device_{...}` pattern



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.uptime) # It's important to target specialized metrics, not the generic ones



attributes:



- key: dt.ip_addresses



displayName: IP Address



pattern: '{device.address}'



- key: dt.dns_names



displayName: DNS Name



pattern: '{instance.name}'



- key: OSRelease



displayName: OS release



pattern: '{instance.systemrelease}'



- key: OSArchitecture



displayName: OS architecture



pattern: '{instance.systemarch}'



- key: OSName



displayName: OS name



pattern: '{instance.systemname}'



- key: ProductVersion



displayName: Product version



pattern: '{instance.productversion}'



- key: FailoverStatus



pattern: '{failover.state}'



displayName: Failover status



- key: SyncStatus



pattern: '{sync.state}'



displayName: Config sync status



role: default



- idPattern: network_device_{device.address}



instanceNamePattern: '{instance.name}'



iconPattern: f5



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



requiredDimensions: []



attributes: []



role: default



- name: network:interface



enabled: true



displayName: Network interface



rules:



- idPattern: network_interface_{mac.address}_{interface.name} # must follow `network_interface_{...}_{...}` pattern



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $eq(f5.lb.sys.interface.status) # Again, we target specialized metrics, not generic ones



attributes:



- key: EnabledState



displayName: Enabled State



pattern: '{interface.enabled}'



- key: MacAddress



displayName: MAC Address



pattern: '{mac.address}'



- key: ifOperStatus



displayName: Operational status



pattern: '{interface.status}'



role: default



- idPattern: network_interface_{mac.address}_{interface.name}



instanceNamePattern: '{interface.name}'



iconPattern: network-interfaces



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



requiredDimensions: []



attributes: []



role: default



relationships:



- fromType: f5lb:interface



typeOfRelation: RUNS_ON



toType: f5lb:instance



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



# Adding the same as relationships



- fromType: f5lb:interface



typeOfRelation: SAME_AS



toType: network:interface



sources:



- sourceType: Metrics



condition: $prefix(f5.lb.sys.interface)



- fromType: f5lb:instance



typeOfRelation: SAME_AS



toType: network:device



sources:



- sourceType: Metrics



condition: $prefix(f5.lb)



screens:



# Customizing the screen for the network device



- entityType: network:device



propertiesCard:



properties:



# Show a link to the specialized entity



- type: RELATION



relation:



entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



displayName: F5 Load balancer



conditions:



# Apply only to devices that have a same as relation, who are monitored by Extension



# These 2 conditions are used althroughout the screen definition



- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



- entityAttribute|devMonitoringMode=Extension



# Must define everything in `detailsInjections` and not `detailsSettings`!



detailsInjections:



# This card is injected by reference, meaning we don't have to duplicate the definition again



- type: CHART_GROUP



key: f5_instance-charts-cpu



# When using `entitySelectorTemplate`, the card is understood to be defined as part of the



# resolved entity's screen definition, and not the current screen definition.



entitySelectorTemplate: type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



conditions:



- relatedEntity|entitySelectorTemplate=type(f5lb:instance),fromRelationships.isSameAs($(entityConditions))



- entityAttribute|devMonitoringMode=Extension



# Of course, full definitions are still supported



- type: CHART_GROUP



key: network-interfaces-list



chartsCards:



- key: network-interfaces-list



mode: NORMAL



target: BOTH # Use CLASSIC for Managed, PLATFORM for SaaS, or BOTH for both



displayName: Traffic



numberOfVisibleCharts: 1



conditions:



# Even if your card is generic, you should still apply this condition so that only



# monitored devices display the card.



- entityAttribute|devMonitoringMode=Extension



charts:



- displayName: Traffic in/out



visualizationType: GRAPH_CHART



graphChartConfig:



metrics:



# metricSelector is required for Managed



- metricSelector: com.dynatrace.extension.network_device.if.bytes_in.count:splitBy("dt.entity.network:device)



# dqlQuery is required for SaaS



dqlQuery: timeseries bytesIn=avg(com.dynatrace.extension.network_device.if.bytes_in.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}



visualization:



displayName: Bytes In



- metricSelector: com.dynatrace.extension.network_device.if.bytes_out.count:splitBy("dt.entity.network:device")



dqlQuery: timeseries bytesOut=avg(com.dynatrace.extension.network_device.if.bytes_out.count),by:{`dt.entity.network:device`},filter:{`dt.entity.network:device`==$(entityId)}



visualization:



displayName: Bytes Out



- entityType: f5lb:instance



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



target: BOTH



layout:



autoGenerate: false



cards:



- key: f5_instance-charts-cpu



type: CHART_GROUP



- key: f5_instance-charts-memory



type: CHART_GROUP



chartsCards:



- key: f5_instance-charts-cpu



target: BOTH



mode: NORMAL



displayName: CPU



numberOfVisibleCharts: 4



chartsInRow: 4



charts:



- displayName: CPU Breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



stacked: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: Idle



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: System



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



displayName: User



visualization:



themeColor: DEFAULT



seriesType: AREA



- displayName: System CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.system1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries system1m=avg(f5.lb.sys.global.host.cpu.system1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: User CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.user1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries user1m=avg(f5.lb.sys.global.host.cpu.user1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- displayName: Idle CPU



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



metrics:



- metricSelector: f5.lb.sys.global.host.cpu.idle1m:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries idle1m=avg(f5.lb.sys.global.host.cpu.idle1m),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



visualization:



themeColor: BLUE



seriesType: LINE



- key: f5_instance-charts-memory



target: BOTH



mode: NORMAL



displayName: Memory



numberOfVisibleCharts: 4



hideEmptyCharts: true



charts:



- displayName: Memory breakdown



visualizationType: GRAPH_CHART



graphChartConfig:



connectGaps: true



yAxes:



- key: y-absolute



position: LEFT



visible: true



- key: y-relative



position: RIGHT



visible: true



min: '0'



max: '100'



metrics:



- metricSelector: f5.lb.sys.host.memory.total:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries total=avg(f5.lb.sys.host.memory.total),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: BLUE



seriesType: AREA



displayName: Total



- metricSelector: f5.lb.sys.host.memory.used:splitBy("dt.entity.f5lb:instance")



dqlQuery: timeseries used=avg(f5.lb.sys.host.memory.used),by:{`dt.entity.f5lb:instance`},filter:{`dt.entity.f5lb:instance`==$(entityId)}



yAxisKey: y-absolute



visualization:



themeColor: ORANGE



seriesType: AREA



displayName: Used
```

## FAQ

### Where does `device.address` come from?

You may have noticed there's no special OID-based capturing of the `device.address` dimension in the shared manifests. This is because the example given is based on the SNMP data source, which automatically adds these dimensions to every collected metric.

### Can this guide be used for any extension data source?

Yes. SNMP was given as an example as it is focused on network devices, but any extension can leverage this topology model so long as it sends the same metrics and dimensions described in this guide.

### Is it possible to extend the details UI within the Infrastructure & Operations Infrastructure & Operations app?

Not yet, but this capability is expected to be available soon, at which point this guide will be updated to include the additional usage details.


---


## Source: extend-topology.md


---
title: Custom topology model
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-topology
scraped: 2026-02-15T21:11:29.256774
---

# Custom topology model

# Custom topology model

* Latest Dynatrace
* 4-min read
* Updated on Jan 28, 2026

The Dynatrace software platform and Dynatrace Intelligence depend on context-rich, high-quality data that is provided by OneAgent, cloud integrations, or technology monitoring extensions.

## Context-rich observability

Context-rich observability means that each incoming observation (metric, trace, log, or event) is stored with a reference to the monitored entity that it belongs to. Simple examples here are a CPU metric measurement that was observed on a given host, or a response time that was observed on a given service trace.

## Built-in topology model

Using all these observations and the related entities, Dynatrace can extract and visualize the huge topological graph that we call [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").

Each OneAgent that is deployed within your IT landscape sends in its own observations. Dynatrace then extracts and auto-discovers all context-relevant topology information. As a result, your Smartscape topology visualization grows in size and detail.

Smartscape, the Dynatrace built-in topological model, is entirely focused on entity types that are relevant for IT operations management, such as hosts, compute nodes, processes, web services, and more.

## Topology examples

You can find examples of topological models all over Dynatrace, for example, the service deployment stack shown in Smartscape.

Smartscape example

![Smartscape example](https://dt-cdn.net/images/smartscape-services-1621-d595e2d107.png)

Another topological view is shown within [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment."), which shows the real-time call relationships of services extracted from all incoming transactions and traces.

Service flow example

![Service flow example](https://dt-cdn.net/images/serviceflow2-1910-d07d5c5e14.png)

The built-in topology model automatically detects more than a hundred entity types and their relationships, but is limited to well-known IT and software related types.

## Custom topology model

Once you start to send in your own data sourcesâsuch as Telegraf metric streams, StatsD application measurements, or your own business metricsâthrough the metric ingest channel, you might be interested in extending the built-in model by adding your own domain-related types and relationships.

The extensibility of the topological model is especially interesting for IoT use cases, where you want to model your own device types (such as `cars`, `ships`, or `vending machines`) and connect them via well-defined relationships.

See the topology-related step in the [WMI extension tutorial](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Learn about WMI extensions in the Extensions framework.") to learn more about extending the Dynatrace topology.

## Custom topology model in action

Let's look at a simple example from the logistics domain that we want to model within Dynatrace.

Easy Shipping LTD

Suppose we have a company, Easy Shipping LTD, that provides transport services. Easy Shipping LTD operates smart containers mounted on trucks that carry the containers from loading dock to loading dock.

* Each truck continuously sends basic telemetry data, such as fuel consumption, operation hours, and error logs.
* Each smart container is able to report the truck number to which it's currently mounted and its container temperature.

With the above example, the company can ingest a continuous stream of observations in the form of truck and container telemetry.

### Truck telemetry data

Easy Shipping LTD trucks send a continuous data stream on fuel (`truck.fuel.total` and `truck.fuel.usage`) and operation hours (`operation.hours`). Each measurement is sent in the context of the individual truck (`trucknr`) and its model (`model`). For example:

```
truck.fuel.total,trucknr=99,model=mac-granite 10234



truck.fuel.usage,trucknr=99,model=mac-granite 17



truck.operation.hours,trucknr=99,model=mac-granite 23766



truck.fuel.total,trucknr=12,model=mac-anthem 234



truck.fuel.usage,trucknr=12,model=mac-anthem 10



truck.operation.hours,trucknr=12,model=mac-anthem 13766
```

### Container telemetry data

Smart containers carried by the company trucks send a continuous data stream on the currently measured temperature (`container.temperature`). Each measurement is sent in the context of the individual container (`containernr`) and the truck it is carried on (`trucknr`):

```
container.temperature,containernr=234321,trucknr=99 40



container.temperature.dev,containernr=234321,trucknr=99 0
```

```
container.temperature,containernr=111111,trucknr=12 39



container.temperature.dev,containernr=111111,trucknr=12 2,5
```

and so on.

Instances of the types `truck` and `container` and their relationship can be extracted automatically from the continuous data stream.

## Benefits of custom topology

The benefit of having a domain model on top of your telemetry data is:

* **Dynatrace-wide monitoring**  
  Domain-specific terminology is used for your entity types and their relationships within all parts of the monitoring platform, such as charting, dashboard, and alerting.
* **Information in context**  
  Analytics can be performed on top of the given domain model, such as to check on which truck a container was mounted over time. Slicing and dicing of telemetry data as well as on logs and events is offered on top of your own domain model.
* **Single pane view**  
  Observed telemetry data no longer represents an isolated view but begins to shape a complete picture of your own domain topology.

See [Define custom topology](/docs/ingest-from/extend-dynatrace/extend-topology/custom-topology "Learn how to create a custom topology model that's suited to your telemetry data.") to learn how to create a custom topology suited to your telemetry data.


---


## Source: oneagent-sdk.md


---
title: OneAgent SDK
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk
scraped: 2026-02-15T21:11:37.446326
---

# OneAgent SDK

# OneAgent SDK

* Latest Dynatrace
* 2-min read
* Published Mar 01, 2018

Dynatrace provides extensive monitoring capabilities for nearly all popular languages and technologies, including Java, .NET, Node.js, PHP, and Golang. See our [our supported technologies page](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details about all supported technologies.

The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module available yet. With the SDK, you get full access to all analysis and monitoring functionality, including auto-baselining and AI-based root cause analysis.

The Dynatrace OneAgent SDK is available in GitHub. Feedback and feature requests can be filed directly in GitHub.

## What you can do with Dynatrace OneAgent SDK

With the Dynatrace OneAgent SDK, you can:

* Trace incoming and outgoing remote calls
* Trace database requests
* Trace incoming and outgoing web requests
* Trace in-process asynchronous execution
* Trace queues and messages
* Capture request attributes

More functionality will be added to the OneAgent SDK over time. The feature sets differ slightly with each language implementation.

## What you can't do with Dynatrace OneAgent SDK

With the Dynatrace OneAgent SDK, you can't:

* Create user sessions and user actions: This functionality is provided by [Dynatrace OpenKit](/docs/ingest-from/extend-dynatrace/openkit "Learn how you can instrument your application using OpenKit, how you can use Dynatrace OpenKit API methods, and more.")

## How to use the Dynatrace OneAgent SDK

As the OneAgent SDK works hand-in-hand with Dynatrace OneAgent, no additional configuration is required.

The main requirements for using the OneAgent SDK are:

* Access to the source code of the application (and willingness to change the code)
* As the OneAgent SDK communicates directly with OneAgent, OneAgent (minimum required OneAgent version depends on the SDK version) needs to be installed and running on the host that runs the application. Container environments are supported.
* OneAgent in full-stack monitoring mode.

OneAgent automatically detects that your application is instrumented with the OneAgent SDK and immediately begins monitoring it. A restart of the application is required following OneAgent installation on the host.

## OneAgent SDK on GitHub

The Dynatrace OneAgent SDK is published directly to GitHub together with the technical documentation. To get a detailed overview of the current features of the OneAgent SDK, check out the following links:

* [Language independent documentation of the SDK's APIs and conceptsï»¿](https://github.com/Dynatrace/OneAgent-SDK)
* [OneAgent SDK for Javaï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Java)
* [OneAgent SDK for C/C++ï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-C)
* [OneAgent SDK for Node.jsï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs)
* [OneAgent SDK for .NETï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet)
* [OneAgent SDK for Pythonï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Python)
* [OneAgent SDK for PHPï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-PHP)

## Further reading

* [Blog: Extend AI-based root cause analysis with OneAgent SDKï»¿](https://www.dynatrace.com/news/blog/extend-ai-based-root-cause-analysis-with-oneagent-sdk)

## Related topics

* [Instrumentation via OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* [OneAgent SDK for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.")
* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")


---


## Source: opentracing.md


---
title: OpenTracing
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing
scraped: 2026-02-15T21:11:53.985605
---

# OpenTracing

# OpenTracing

* Latest Dynatrace
* 2-min read
* Updated on Sep 23, 2022

Early Adopter

OpenTracing is an open source project that provides APIs and instrumentation for distributed tracing. Although OpenTracing and OpenCensus merged in 2019 to form OpenTelemetry, OpenTracing instrumentations are still used by many popular frameworks, libraries, and projects.

Dynatrace OneAgent for Java automatically collects OpenTracing span data and integrates it into end-to-end PurePathÂ® distributed traces.
OpenTracing with OneAgent enables you to:

* Gain insights into Java third-party libraries or frameworks that arenât natively covered by OneAgent but come with OpenTracing pre-instrumentation.
* Enrich monitoring data with project-specific additions (for example, custom instrumentation that adds business data or the capture of developer-specific diagnostics points).
* Stitch together independent, unrelated transactions to extend end-to-end distributed traces (for instance, by adding vendor-neutral custom instrumentation to gain business-process-specific or domain-specific end-to-end transactional insights).

![OpenTracing support in OneAgent](https://dt-cdn.net/images/oneagent-opentracing-support-2596-85407ecec3.png)

The quality of the OpenTracing spans captured by OneAgent depends on the quality of instrumentation provided by the third-party library.

## Prerequisites

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracingï»¿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

## Enable OpenTracing integration

To enable support for capturing span data

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Filter for **OpenTracing**.
3. You can enable OneAgent to:

   * Automatically register Dynatrace as the `GlobalTracer` and thereby override other tracers that are registered in the application. Select this setting only if you're sure that you want to override the other tracers (for example, Jaeger) in your tracing system.
   * Automatically register Dynatrace as the `GlobalTracer` when no other tracer is registered in the application. Do this if you don't want to interfere with any other tracers in your tracing system.
4. In your application code, use the return value from `GlobalTracer.get()` to create spans.
   The following sample shows how to manually create spans with OpenTracing:

   ```
   // Make sure to use the correct Tracer.



   Tracer tracer = GlobalTracer.get();



   SpanBuilder spanBuilder = tracer.buildSpan("hello");



   spanBuilder.withTag("foo", "bar");



   Span span = spanBuilder.start();



   // Make sure to close every created Scope.



   // It is recommended to use a try-with-resource statement for that.



   try (Scope scope = tracer.activateSpan(span)) {



   // Do actual operation.



   } finally {



   // Make sure to finish every started Span.



   span.finish();



   }
   ```

   The following sample shows how to use an existing instrumentation scope/library to create spans with OpenTracing:

   ```
   HazelcastInstance untraced = HazelcastClient.newHazelcastClient();



   // This operation will not be visible in Dynatrace.



   untraced.getMap("map").put("key", "value");



   // TracingHazelcastInstance implements the same interface (HazelcastInstance)



   // but automatially creates span for every operation.



   // It internally calls GlobalTracer.get().



   // Available as a separate instrumentation scope/library:



   // https://github.com/opentracing-contrib/java-hazelcast



   HazelcastInstance traced = new TracingHazelcastInstance(



   HazelcastClient.newHazelcastClient(),



   false // traceWithActiveSpanOnly



   );



   // This operation will be visible in Dynatrace.



   traced.getMap("map").put("key", "value");
   ```

See [Span settings](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.") for all configuration options.

## Limitations

* [Span default service](/docs/observe/application-observability/services/service-detection/service-detection-v1#span-service "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* When both OneAgent and OpenTracing instrumentation are present for the same technology (for example, incoming web requests via the Servlet API), you may experience the following limitations:

  + Duplicate nodes in PurePathÂ® distributed traces
  + Additional overhead
  + For JDBC, such double instrumentation may break service detection
    Be extra cautious when enabling OneAgent OpenTracing Java support for OneAgent out-of-the-box [supported technologies](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Integrating traces from OpenTracing Spring framework instrumentation currently is not supported.
* The OpenTracing Java sensor doesn't capture `array`-type attributes.

## Supported technologies

Dynatrace integrates traces from any OpenTracing instrumentations. We have positively tested the instrumentation of the following libraries and frameworks:

* Hazelcast for OpenTracing Java
* Couchbase starting with [java-client version 3.1.3ï»¿](https://github.com/couchbase/couchbase-jvm-clients) for OpenTracing Java


---


## Source: span-settings.md


---
title: Span settings
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings
scraped: 2026-02-15T21:08:51.447692
---

# Span settings

# Span settings

* Latest Dynatrace
* 4-min read
* Updated on Dec 20, 2023

OneAgent version 1.215+ Dynatrace version 1.216+

Dynatrace automatically captures all OpenTracing and OpenTelemetry spans, but you can control and adapt how OpenTelemetry and OpenTracing spans are combined with OneAgent data into PurePathÂ® distributed traces.

The span settings are available at **Settings** > **Server-side service monitoring**. You can define rules to:

* Store and mask only specific attributesâ**Attribute capturing**
* Exclude specific spansâ**Span capturing**
* Define spans that should be considered as entry pointsâ**Span entry points**
* Enable context propagation for certain spansâ**Span context propagation**

For details, see the sections that follow.

## Attributes

The OneAgent code module's OpenTelemetry Span Sensor automatically captures all OpenTelemetry attributes.
If you want to prevent the accidental storage of personal data, you can exclude specific attribute keys for which the values must not be persisted.
By omitting attributes containing personal data, you can meet your organization's privacy requirements and control the scope of stored monitoring data.

To configure attribute storage and masking settings for your environment

1. Go to the appropriate configuration page:

   * In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * In Dynatrace Classic, go to **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Select **Server-side service monitoring** > **Attribute capturing**.
3. optional To change the default OpenTelemetry attribute persistence, go to **Preferences**.

   * To store all attributes except the ones in the **Blocked attributes** list, select **Allow all attributes**
   * To block all attributes except the ones in the **Allowed attributes** list, select **Block all attributes**

   Only one setting preference is possible.
4. Add an attribute name to the attribute list.

   1. On the **Attribute capturing** page, select **Blocked attributes** or **Allowed attributes**.

      Allowed attributes list Dynatrace recommends a few basic attributes to generally be included, such as `service.name` or `service.version`. For ease of use, Dynatrace comes with a default configuration that can be adjusted.
   2. Select **Add item** to add a new key to the attribute list and enter the key.
   3. Select **Save changes**.
5. Perform the following actions to mask a stored attribute value.

   1. On the **Attribute capturing** page, select **Attribute data masking**.
   2. Select **Add item** to add a new key to the masked attributed list.
   3. Enter a stored value key and select an option from the **Masking** dropdown list. To learn more about masking options, see [OpenTelemetry traces](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#otel-traces "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").
   4. Select **Save changes**.

You can then find the attribute key on the **Distributed traces** page on the [**Summary** tab](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#summary-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

## Span capture

All detected OpenTelemetry and OpenTracing spans are captured by default. This means that every detected span is added to distributed traces. This gives code-level visibility along with span attributes, even for technologies not supported by OneAgent out of the box.

You can create [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") based on spans to segment the distributed traces.

We recommend that you exclude spans for technologies supported out of the box by OneAgent for [Java](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Go](/docs/ingest-from/technology-support#go "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To control your span capturing

1. Go to **Settings** > **Server-side service monitoring** > **Span capturing**.
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, decide whether you want to **Ignore** or **Capture** spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span capturing based on the value of the following sources:

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Enter the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.

## Span entry points

By default:

* OpenTelemetry/OpenTracing span kinds `server` and `consumer` start new distributed traces automatically. This means that all OneAgent sensors contribute to that distributed trace and a default service is created for the distributed trace.
* OpenTelemetry/OpenTracing span kinds `client`, `internal`, and `producer` don't start new distributed trace automatically.

You can choose to start distributed traces based on `client`, `internal`, and `producer` span kinds, and to opt out for `server` and `consumer` span kinds, based on various span details.

To control your span entry points

1. Go **Settings** > **Server-side service monitoring** > **Span entry points**
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, specify **Create entry point** or **Do not create entry point** for spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span entry points based on the value of the following sources:

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Enter the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.

## Span context propagation

Context propagation enables you to connect distributed traces through OpenTelemetry/OpenTracing. You can connect distributed traces through any protocol and propagate the inject and extract usage to the Dynatrace PurePathÂ® distributed traces context.

To reduce the risk of context propagation conflicts with built-in sensors, context propagation is disabled by default and is limited to spans matching the criteria of your choice.

To define rules to enable context propagation for specific spans

1. Go **Settings** > **Server-side service monitoring** > **Span context propagation**
2. Select **Add item**.
3. Enter a **Rule name**.
4. In the **Rule action** list, specify **Propagate** or **Do not propagate** span context for spans matching the criteria you're about to define.
5. Select **Add item**.
6. You can control span context propagation based on the value of the following sources

   * **Attribute**
   * **Instrumentation scope name**, `OpenTelemetry`
   * **Instrumentation scope version**
   * **Span kind**âfor example, `server`
   * **Span name**
7. Select the **Comparison type**âfor example, **Contains** or **Equals**.
8. Add the value for the source you specified earlier.
9. By default, the search for key and value is not case sensitive. Turn on **Case sensitive** if you want your rule to consider key and value case.
10. Select **Save changes**.


---


## Source: extend-tracing.md


---
title: Extend distributed tracing
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing
scraped: 2026-02-15T21:09:01.169129
---

# Extend distributed tracing

# Extend distributed tracing

* Latest Dynatrace
* 1-min read
* Published Feb 04, 2022

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Learn how to extend distributed tracing observability with OpenTelemetry tracing.](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")[![Opentracing](https://dt-cdn.net/images/techn-icon-opentracing-936f2ba1cd.svg "Opentracing")

### OpenTracing

Learn how to extend distributed tracing observability in Dynatrace with OpenTracing.](/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace.")[### OneAgent SDK

Learn how to extend distributed tracing observability in Dynatrace with the OneAgent SDK.](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.")


---


## Source: extend-unified-analysis-pages.md


---
title: Extend built-in unified analysis pages
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages
scraped: 2026-02-15T21:27:19.923959
---

# Extend built-in unified analysis pages

# Extend built-in unified analysis pages

* Reference
* 2-min read
* Published May 19, 2022

If your extension supplies additional data for a default entity with its own unified analysis page, you can extend the page using card injections. Examples of built-in unified analysis pages are the [host overview page](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") or any unified analysis Kubernetes page. Card injections are available since Dynatrace version 1.233.

## Define card injection

The configuration of a card injection is similar to the configuration of the page layout itself with one significant modification: injected cards are ordered alphabetically by their key, which should use a well-specified key prefix. This ensures that unrelated data supplied by different extensions won't be mixed on a unified analysis page. Injections can be added under the `detailsInjections` and `listInjections` sections of the screen configuration.

```
detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE
```

The following options are available for a card supplied by your extension:

* `type`: Card type available to be supplied to a unified analysis page. Supported types include `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS`, and `MESSAGE`.
* `key`: Unique card key used to reference the desired card configuration. Use a well-specified key prefix to ensure that related cards are placed properly on a page. Cards are sorted alphabetically based on key.
* `entitySelectorTemplate`: An entity selector that is used to reference cards from another monitored entity type. For more information, see [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

  Details

  It can serve multiple purposesâselecting the entity where the chart will be displayed and filtering them based on certain rules or relating entities. It is used in conjunction with `entityType` to further refine which entities are applicable for the card. For example, if `entityType` is `HOST`, you can use `entitySelectorTemplate` to show the card only for hosts using a certain operating system.

  `$entityConditions` acts as a dynamic placeholder, adapting to the context in which the card appears. For example, when the card is displayed on a page dedicated to a specific host, `$entityConditions` will automatically adjust to conditions applicable to that host.

  For example, when the card with the following configuration is displayed on the host page.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))"
  ```

  The `$(entityConditions)` placeholder will be automatically replaced to point to the specific host entity.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))"
  ```
* `width`: Determines how wide that card is in relation to the page width. Supported values are `HALF_SIZE` and `FULL_SIZE`.
* `conditions`: A list of conditions that need to be fulfilled for the card to be visible.

## Reference card injection

As a final step, you need to reference the card to be injected on a built-in unified analysis page with an Extensions 2.0 package and place it in your `extension.yaml` file in the `screens` section. In this example, we extend the built-in host overview page (`entityType: HOST`).

```
name: custom:com.ua.example.extension



version: 1.0.0



minDynatraceVersion: 1.233.0



author:



name: StackEnterprise



# Here comes your usual extension YAML content: data source, declarative metrics, topology, etc.



screens:



- entityType: HOST



detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE



chartsCards:



- key: my-host-feature-windows-only-chart



...



- key: my-host-feature-chart1



...



- key: my-host-feature-chart2



...



- entityType: PROCESS_GROUP_INSTANCE



chartsCards:



- key: my-host-feature-process-chart



...
```


---


## Source: unified-analysis.md


---
title: Unified analysis pages
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis
scraped: 2026-02-15T09:13:23.222313
---

# Unified analysis pages

# Unified analysis pages

* Overview
* 4-min read
* Published Mar 09, 2023

Dynatrace unified analysis pages bring all observability data and relevant analytical tools for effective analysis and troubleshooting into context. When exploring metrics, events, logs, and metadata for a problematic, domain-specific entity, you can find every observability signal related to this entity on one page.

The [host overview page](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") is an example of a unified analysis page available in most environments.

## Page types

There are two types of unified analysis pages:

* **List screen**  
  The list screen is automatically generated and enables you to browse all instances of a specific entity type. You can find the available customizations in [List settings](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-settings "Learn about unified analysis syntax").
* **Details screen**  
  The entity details screen brings all observability signals attached to an entity into context. Like the list screen, a details screen is automatically generated for every entity in your environment. You can find the available customizations in [Details settings](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-settings "Learn about unified analysis syntax").

## Cards

On the entity page, you can define various types of cards.

### Chart group

Use the chart group component to group configured charts in a grid. For configuration details, see [Chart group cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#chart-group-cards "Learn about unified analysis syntax").

### Chart type

You can use the following chart types (controlled by the `visualizationType` field).

* **Graph chart:**

  ![Chart group example](https://dt-cdn.net/images/chart-group-1169-76d6ed5a9e.png)
* **Pie chart:**

  ![Pie chart](https://dt-cdn.net/images/pie-chart-519-7780ea60ce.png)
* **Single value:**

  ![Single value](https://dt-cdn.net/images/single-value-550-35129a06f1.png)

### Entity list

Use the entity list card to show entities of the same type, their attributes, and related entities in one table.

For configuration details, see [Entities list cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#entities-list-cards "Learn about unified analysis syntax").

![Entity list example](https://dt-cdn.net/images/a84b28ad-48ba-40b6-b83e-c2962c2d2f86-1423-5c0e42d7a4.png)

### Metric table

Use the metric table card to show multiple metric data in one table.

For configuration details, see [Metric table cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#metric-table-cards "Learn about unified analysis syntax").

![Metric table card](https://dt-cdn.net/images/7dc47e10-5c1f-494d-bb1c-865fec747246-1598-1442ff2964.png)

### Properties

Use the properties card to show attributes and tags. By default, it displays all attributes coming from the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API."). For more information, see [Notifications bar](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#notifications-bar "Monitor hosts with Dynatrace.").

See [Properties cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#properties-cards "Learn about unified analysis syntax") for configuration details.

![Properties card example](https://dt-cdn.net/images/properties-528-184d1764f0-528-10fef21345.png)

### Logs

Use the logs cardâwhich has the same functionalities as the [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")âto display a bar chart representing different log occurrences within the selected timeframe and a detailed table where each log is an entry with additional properties such as timestamp, status, and content.

See [Logs cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#logs-cards "Learn about unified analysis syntax") for configuration details.

![logs-card](https://dt-cdn.net/images/screenshot-2023-03-14-at-10-16-08-624-bf7cf1200b.png)

### Messages

Use the message card to show information when a certain condition is satisfied. For configuration details, see [Message cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#message-cards "Learn about unified analysis syntax"). There are two types of message card visualization:

* **Message**âa card that just displays text information.
* **Card**âa card with a title, description, and available actions.

For example, display the message card if OneAgent is not deployed:

![Message card example](https://dt-cdn.net/images/screenshot-from-2022-02-02-11-45-21-2531-4541e56bf6.png)

### Events

Use the events card to display events related to the specified entities.

See [Events cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#events-cards "Learn about unified analysis syntax") for configuration details.

![Events card example](https://dt-cdn.net/images/screenshot-2023-03-14-at-14-12-35-571-7d4521137a.png)

### Health

Use the health card to display specific metrics in a visual format. By default, it provides a quick overview of up to six distinct tiles, each representing a unique metric or data point.

Single tile reacts to certain events on connected metrics and may take different colors:

* greenâthere is data on at least one connected metric
* redâthere is an open problem related to at least one connected metric
* grayâthere is a closed problem related to at least one connected metric
* whiteâthere is no data for this tile in current timeframe

See [Health cards](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#health-cards "Learn about unified analysis syntax") for configuration details.

![Health card](https://dt-cdn.net/images/dee80e89-6646-420a-810d-0e7e2566677b-1640-4b6291895b.png)

## Concepts

### Actions

Actions define what happens after selecting one of the available options available from the **More** (**â¦**) menu in the upper-right corner of every card.

See [Actions](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#actions "Learn about unified analysis syntax") for configuration details.

### Filtering

Unified analysis supports filtering entities by indexed entity attributes. You can enable filtering for the list screen and in the context of specific cards. Entity filtering can be configured at two levels:

* At the page level, where filtering affects all cards on the screen. There are separate configurations for the [details screen](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-filters "Learn about unified analysis syntax") and [list screen](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-filters "Learn about unified analysis syntax").
* In the entity list level, where filtering affects only a single list.

### Injections

If you want to display the cards on the page without modifying their layout, see [Extend built-in unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages "Extend the built-in unified analysis page with additional data ingested by your extension.").

### Exploratory analysis

The exploratory analysis analyzes only the metrics from the graph charts that are in the chart groups, entities lists, and metric tables. For more information, see [DavisÂ® causal correlation analysis](/docs/dynatrace-intelligence/reference/ai-models/causal-correlation-analysis "Learn how Dynatrace Intelligence causal correlation analysis finds related metrics across your environment.").

**Next step**: [Unified analysis tutorial](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial "Learn how to upload sample data to your Dynatrace environment and create a simple unified analysis extension.")


---


## Source: extend-ui.md


---
title: Extend Dynatrace with domain-specific web UI
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui
scraped: 2026-02-15T21:11:47.629525
---

# Extend Dynatrace with domain-specific web UI

# Extend Dynatrace with domain-specific web UI

* Overview
* 1-min read
* Updated on May 16, 2022

The Dynatrace Extensions 2.0 framework enables you to tailor the Dynatrace web UI to the specific needs of the data ingested by your extension. You can define customized dashboards, create specialized unified analysis pages, and extend built-in unified analysis pages with data provided by your extension.

[### Create specialized unified analysis pages

Extend the Dynatrace web UI using entity-tailored unified analysis pages.](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")[### Extend built-in unified analysis pages

Extend the built-in unified analysis page with additional data ingested by your extension.](/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages "Extend the built-in unified analysis page with additional data ingested by your extension.")[### Distribute custom dashboards

Extend the Dynatrace web UI using your data-tailored dashboards.](/docs/ingest-from/extensions/advanced-configuration/custom-dashboards "Extend the Dynatrace web UI using your data-tailored dashboards.")


---


## Source: openkit.md


---
title: Extend user experience and behavior data
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/openkit
scraped: 2026-02-15T21:11:42.420060
---

# Extend user experience and behavior data

# Extend user experience and behavior data

* Latest Dynatrace
* 2-min read
* Updated on May 30, 2022

There are many ways your business can interact with your customers in the digital world. Monitoring user experience and behavior in your web and mobile applications is a great way to get started with digital experience monitoring; Dynatrace easily detects and automatically monitors all application touchpoints using OneAgent. However, your business likely has many other digital touchpoints outside of your applications where your customers interact with your brand that are also key to the success of your business. With Dynatrace OpenKit, you get a set of open source libraries that enable you to instrument all other digital touchpoints in your environment, whether or not theyâre traditional rich client applications, smart IoT applications, or even Alexa skills.

Dynatrace OpenKit is a set of open source libraries that provides an easy, lightweight means of instrumenting the source code of your custom applications so that you can monitor their performance with Dynatrace. Dynatrace OpenKit is best suited for client/server applications that communicate via HTTPâfor example, rich client applications, embedded devices, and terminals.

The main advantages of OpenKit are:

* Ease of use
* No OneAgent library dependencies
* Ease of portability to other languages and platforms

With Dynatrace OpenKit, you can:

* Track [user sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") and [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")
* Report events, errors, and crashes
* Trace web requests to [server-side distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")
* Tag user sessions with user tags
* Maintain compatibility with Dynatrace

With Dynatrace OpenKit, you can't:

* Create server-side distributed traces. This functionality is provided by the Dynatrace OneAgent SDK.
* Create metrics. However, you can use the [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.") and [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") to report metrics.

As of April 2022, Dynatrace no longer supports TLS 1.0 and TLS 1.1 for Dynatrace SaaS Real User Monitoring (RUM) data. Now Dynatrace SaaS only supports TLS 1.2+. For this reason, using a .NET Framework version lower than 4.7 might require [additional configurationï»¿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls#if-your-app-targets-a-net-framework-version-earlier-than-47).


---
