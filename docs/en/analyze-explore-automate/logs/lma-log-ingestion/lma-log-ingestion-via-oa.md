---
title: Log ingestion via OneAgent
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa
scraped: 2026-02-25T21:27:05.811424
---

# Log ingestion via OneAgent

# Log ingestion via OneAgent

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Jan 30, 2026

## Ingest via OneAgent

Recommended

OneAgent is a recommended, powerful tool that automatically finds log sources from a wide range of technologies on many different platforms, container orchestration and operating systems. Refer to [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") to see the supported operating systems.

![log-oneagents](https://dt-cdn.net/images/log-oneagents-1980-8ae52ce287.png)

See the [OneAgent for logs ingestion](/docs/analyze-explore-automate/logs/lma-use-cases/lma-oa-logs-ingest "Set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.") use case to learn how to set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.

We recommend using OneAgent for logs, as it provides the following advantages:

* Simplified instrumentation for hosts, processes, and Kubernetes clusters.

  + Seamless installation on hosts, and Operator for Kubernetes ensures a first-class experience with built-in logs observability.
  + Out-of-the-box log enrichment with contextual information such as topology and Kubernetes metadata.
  + One-click opt-in for trace context inclusion in logs, enhancing traceability.
* Automatic detection of critical logs coupled with flexible custom log source configuration, ensuring comprehensive observability.
* Advanced log management capabilities at scale, offering configurations for log formats, sensitive data masking, and capture and processing filtering.

Check out the OneAgent platform and capability [support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") and deploy OneAgent to your environment.

## Log data autodiscovery

OneAgent automatically detects log files, ensuring that relevant logs are collected and analyzed for all monitored processes. OneAgent scans the file system and applications running on the host to detect log files and sources and identifies log files. Access the [Log content autodiscovery](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-autodiscovery "Dynatrace automatically discovers all new log files that meet specific requirements.") page to learn about the autodiscovery process.

Once log sources are detected, OneAgent applies relevant log ingestion rules. These rules define how the logs should be collected, parsed, and forwarded to the Dynatrace monitoring platform. The autodetection includes [log rotation patterns](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-rotation-patterns "Dynatrace monitors rotation patterns for log files and ensures the completeness of the file reading process, even if OneAgent is temporarily switched off or the log source is unavailable.").

OneAgent autodetects logs from hosts, and collects logs from [Kubernetes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") container orchestration systems and from [Docker](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-in-docker "Dynatrace supports the collection of log data from non-orchestrated Docker environments via OneAgent.") containers.

A OneAgent starts ingesting logs as soon as its log module reads a log file for the first time. The actual start time may be affected by ingestion intervals and how long it takes to propagate the configuration from the environment to the log module.

### OneAgent for host logs

OneAgent simplifies log management by automatically decorating logs based on infrastructure and log source context, and enabling one-click trace enrichment for enhanced troubleshooting. Installation and central log ingestion rules setup in Dynatrace are all it takes to start monitoring logs. OneAgent also offers advanced features for scalable log management, including filtering, masking sensitive data, custom log source definition, log rotation pattern detection, and centralized configuration for easier lifecycle management.
Learn more by accessing the [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.").

Find below an example of ingested logs attributes.

```
"timestamp": "2024-05-23T15:46:23.000000000+02:00",



"content": "2024-05-23 15:46:23 WebLaunche ERROR [HeadlessVisitRunnable] DriverEntry shutDown. [com.dynatrace.diagnostics.uemload.headless.DriverEntry@647129f3  useCnt: [4] drv: [ChromeDriver: chrome on LINUX (01b4aedd5176375e9712d60df153d6a2) http://localhost:17828] proxy: [org.littleshoot.proxy.impl.DefaultHttpProxyServer@4598e617 /127.0.0.1:45875] chrome_driver: [http://localhost:17828] debug port: [33787] ip: [91.172.93.134] healthy: [true]]",



"dt.entity.host": "HOST-9A17CDBA8FF4FCBB",



"dt.source_entity": "HOST-9A17CDBA8FF4FCBB",



"event.type": "LOG",



"host.name": "demodev-master",



"log.source": "/home/labuser/.dynaTrace/easyTravel 2.0.0/easyTravel/log/WebLauncher.log",



"loglevel": "ERROR",



"process.technology": [



"Apache Tomcat",



"Java"



],



"status": "ERROR",



"date_ingested": "2024-05-22T22:14:42.079000000Z"
```

### Kubernetes logs via OneAgent

Read more about configuring log ingest from Kubernetes by accessing the [Stream Kubernetes logs with Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") page.

Find below an example of ingested logs attributes.

```
{



"timestamp": "2024-05-23T15:55:23.000000000+02:00",



"content": "2024/05/23 13:55:23 Failed to export to Stackdriver: rpc error: code = PermissionDenied desc = The caller does not have permission",



"dt.entity.cloud_application": "CLOUD_APPLICATION-63AACD91ADBAB15F",



"dt.entity.cloud_application_instance": "CLOUD_APPLICATION_INSTANCE-F731124830922265",



"dt.entity.cloud_application_namespace": "CLOUD_APPLICATION_NAMESPACE-0A4EA744229201C9",



"dt.entity.container_group": "CONTAINER_GROUP-4F1B012F9B098D9F",



"dt.entity.container_group_instance": "CONTAINER_GROUP_INSTANCE-D8EF90CDA84B35F2",



"dt.entity.gcp_zone": "GCP_ZONE-4E0474C4AFCCC79A",



"dt.entity.host": "HOST-C4E8984646B39EBE",



"dt.entity.kubernetes_cluster": "KUBERNETES_CLUSTER-324E5954D86018E3",



"dt.entity.kubernetes_node": "KUBERNETES_NODE-4B5BC37280D9BFD6",



"dt.entity.process_group": "PROCESS_GROUP-B6AA568F4AD316D7",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-8E2A55B6CF37CF42",



"dt.kubernetes.cluster.name": "gke",



"dt.kubernetes.node.system_uuid": "592f7b67-a340-e136-a9a2-488969f9fe34",



"dt.process.name": "server frontend-*",



"dt.source_entity": "PROCESS_GROUP_INSTANCE-8E2A55B6CF37CF42",



"event.type": "LOG",



"gcp.instance.id": "7994835647533846587",



"gcp.project.id": "dynatrace-demoability",



"gcp.region": "us-central1",



"host.name": "gke-keptn-demo1-e2-custom-4-8192-08f6a08a-1xvo.c.dynatrace-demoability.internal",



"k8s.container.name": "server",



"k8s.deployment.name": "frontend-*",



"k8s.namespace.name": "online-boutique",



"k8s.pod.name": "frontend-7cc5676659-j2n5l",



"k8s.pod.uid": "776226ff-4a33-4ea5-807e-2c930759d6eb",



"log.source": "Container Output",



"loglevel": "ERROR",



"process.technology": [



"C-Library",



"Containerd",



"Go"



],



"status": "ERROR",



"OperatorVersion": "v1.1.0",



"gcp.zone": "us-central1-c",



"k8s.cluster.uid": "74d7702f-11bf-445f-8fbc-2998804007ab",



"k8s.node.name": "gke-keptn-demo1-e2-custom-4-8192-08f6a08a-1xvo",



"log.iostream": "stderr"



},
```

## Custom log sources

Many applications generate logs in formats or locations not covered by the default autodiscovery mechanism. You can add custom log sources when automatic detection does not recognize specific log files or when you need to monitor logs from applications not covered by default settings. Configure custom log sources if you encounter challenges with the rotation pattern or when the log file does not meet the detector's requirements. To learn more, see [Custom log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source "Configure custom log sources to manually add log data sources that have not been autodetected.").

## OneAgent log configuration flow

The only required step after OneAgent installation is to review default ingest rules or create custom log ingest rules to ensure the logs are ingested to the Dynatrace tenant. For further configurations, you can use the options listed in the diagram below:

![LMA - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lma-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-66c4cfd087.png)

### Log ingest rules

Required

Setting up the log ingest rules is the most important step in the configuration process. The rules allow you to specify which automatically discovered and custom logs are ingested, filtered, and stored. The log ingest rules allow customization according to specified matchers, such as process group or log source file. This ensures that the logs ingested from various sources are properly managed and integrated into the Dynatrace log monitoring system. (includes automatically discovered and custom logs).

You can review log sources detected by OneAgent on the **Host** or **Process** page in Dynatrace. For new tenants, some built-in rules are enabled by default. Learn more by accessing the [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") page.

The log ingest rules apply exclusively to OneAgent. These rules do not extend to other log collection mechanisms.

### Sensitive data

You can set up OneAgent to mask any information that you consider to be sensitive so it doesn't reach Dynatrace in plain text. To learn about this configuration, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

### Timestamps

Learn how OneAgent supports [timestamps](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics."), or you can optionally [configure a custom timestamp pattern](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.") specific to your case.

## OneAgent settings

Dynatrace Log Monitoring uses the [OneAgent log module](/docs/discover-dynatrace/get-started/glossary#glossary-oneagent-log-module "Get acquainted with Dynatrace terminology.") enabled by default with all OneAgent installations. While Log Monitoring does not require any specific configuration, you can modify some of the options available for the OneAgent log module.

### Enable Log Monitoring with `oneagentctl`

To enable Log Monitoring on a OneAgent, use `oneagentctl` with the option `--set-app-log-content-access=true`.
For more information, see [Log Monitoring configuration](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#log-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Global OneAgent settings for Log Monitoring

1. Go to **Settings** > **Log Monitoring** > **Advanced log settings**.
2. Adjust settings and **Save changes**.

### Host-specific OneAgent settings for Log Monitoring

1. Go to **Hosts** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **Log Monitoring** and **Advanced log settings**.
4. Adjust settings and **Save changes**.

### Default OneAgent settings

## Confirm that log monitoring is enabled

**Dynatrace Log Monitoring** is enabled by default but only controls the OneAgent log module capability. To actually ingest and view logs, you must also configure log ingest rules. If you experience issues with log collection, verify that this setting hasn't been disabled.

Follow the steps below in your Dynatrace environment to check if **Dynatrace Log Monitoring** is enabled:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. From there, go to **Collect and capture** > **General monitoring settings** > **Monitored technologies**.
3. Find **Log Monitoring** in the list of supported technologies, and select  **Edit**.
4. Check if the **Enable Log Monitoring across all OneAgent in your environment** toggle switch is on, and enable it, if it's not.

If this setting is disabled at the global level, you can enable **Dynatrace Log Monitoring** at the host level:

1. Go to **Infrastructure & Operations** > **Hosts**.
2. Select a host record.
3. Go to  > **Host Settings** > **General**.
4. Find **Log Monitoring** in the list of supported technologies.
5. Turn on **Enable on this host**.

## Log enrichment

As an out of the box feature, OneAgent automatically decorates logs by adding topology context, maintaining trace information, and identifying severity levels. To learn more, see [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

## Alternative to ingestion via OneAgent

You can use the following alternatives to OneAgent for monitoring your log data:

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages."): Collect logs via API when unable to install OneAgent.
* [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."): Use customizable add-ons to ingest logs and extend observability.
* [Syslog](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages."): Stream, oversee and control log files from various system components.

## Recent past logs ingestion when enabling the log module

When log monitoring is enabled, the Dynatrace log module ingests a limited amount of recent past data from the log files.

* If the log module can detect a supported timestamp format, it ingests the last 15 minutes of logs.
* If the timestamp format can't be detected, the log module ingests the last 10 MiB of the file.

Recent past logs ingestion begins when the log module attempts to read the log file for the first time. This means that the starting point can vary for different log modules in your environment. Additionally, log module ingestion intervals and configuration propagation time (from the environment to the log module) impact the actual start time. This is a built-in feature and no configuration is required.

## Log files with outdated modifications

Log files whose last modification time is older than 7 days are not tracked by OneAgent. This has the following implications:

* No log data from these files is ingested.
* When additional content is appended, the file is treated as new. If the content doesn't contain timestamps, OneAgent ingests the last 10 MiB of the file, which may include data that was previously ingested. This can result in duplicate entries.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-troubleshooting "Fix issues related to the setup and configuration of Log Management and Analytics.").

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)

## Related topics

* [OneAgent for logs ingestion](/docs/analyze-explore-automate/logs/lma-use-cases/lma-oa-logs-ingest "Set up log monitoring using OneAgent to automatically discover and ingest logs from your hosts.")