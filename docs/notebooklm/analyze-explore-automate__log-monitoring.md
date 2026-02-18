# Dynatrace Documentation: analyze-explore-automate/log-monitoring

Generated: 2026-02-18

Files combined: 31

---


## Source: add-log-files-sources-v2.md


---
title: Log sources and storage (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2
scraped: 2026-02-18T05:46:21.776337
---

# Log sources and storage (Logs Classic)

# Log sources and storage (Logs Classic)

* 2-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Starting with OneAgent version 1.243 and Dynatrace Cluster version 1.252, we strongly encourage you to switch to [Log Storage](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.").

With the release of Dynatrace version 1.285 (March 2024), Dynatrace will automatically convert your [log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-files-manually "Learn how to manually add log files for analysis.") and [log storage](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources "Learn how to include and exclude log sources for analysis.") configurations to the latest version.

You can also upgrade to the new configuration by selecting **Upgrade configuration**. All of your current settings will be fully upgraded.

The upgraded configuration (see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.")) defined on the **Custom log source configuration** and **Log sources and storage** pages will give you:

* Greater flexibility in defining log sources (for example, log path, log level, Kubernetes namespace, Kubernetes deployment)
* Flexibility in defining log sources (using environment, host group, and host scopes)
* Granularity in managing log source access rights
* Use of the REST API for managing log sources
* Ability to filter and mask log data at capture

To include or exclude specific log sources from storage

1. Go to **Settings** > **Log Monitoring** > **Log sources and storage**.
2. Select **Include all logs**, **Include the following logs**, or **Exclude the following logs** from the list.
3. Switch between tabs to select logs from **Hosts perspective** or from **Process groups perspective**.

Switching tabs

Only log sources in the currently active (selected) tab will be saved. Log sources marked in the other tab will be ignored.

4. Select **Save changes**.

## Migration to the new storage configuration

After you go to **Settings** > **Log Monitoring** > **Log storage**, automatic migration from the old storage configuration format to the new one takes place. The following changes will occur in your current configuration:

* **Host perspective**  
  All items configured on the **Hosts perspective** are migrated as a set of matchers to the corresponding host scope.
* **Process groups perspective**  
  Only the rules that are applied to a whole process group are migrated to the tenant scope. If a process group is enabled only for a subset of hosts, the relevant rules must be created on the host level.

After your configuration of log sources is successfully migrated, you can use new configuration items and add your matchers.

## FAQ

Is this change reversible?

No. After the change, all old configurations are wiped out, so be sure before you make this change.


---


## Source: cloud-provider-log-forwarding.md


---
title: Cloud provider log forwarding (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding
scraped: 2026-02-17T21:33:13.971092
---

# Cloud provider log forwarding (Logs Classic)

# Cloud provider log forwarding (Logs Classic)

* Overview
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.230+

For the newest Dynatrace version, see [Cloud provider log forwarding](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.").

DDU consumption for Log Monitoring

DDU pricing applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Amazon Web Services

Stream or forward your logs from Amazon CloudWatch, AWS S3 or other AWS sources.

### Stream logs via Amazon Data Firehose

Dynatrace integration with Amazon Data Firehose provides a simple and safe way to ingest AWS logs.

To enable AWS log forwarding,

1. Create Amazon Data Firehose instance.
2. Configure it with your Dynatrace environment as a destination.
3. Connect your CloudWatch log groups by creating a subscription filter or send logs directly to Firehose from services that support it (for example, VPC Flow Logs).
   Firehose and other created cloud resources incur AWS costs according to the standard AWS billing policy.

To learn more, see [Stream logs via Amazon Data Firehose (Logs Classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.").

### Log ingestion from Amazon S3

You can stream logs from AWS S3 to Dynatrace using a serverless architecture.

The log forwarder offers:

* Out of the box parsing of AWS services, see [Supported AWS Servicesï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder#supported-aws-services)
* Processing mechanism for any other use case including 3rd party logs written to s3, see [Log Processingï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_processing.md#log-processing)
* Cross-region support, see [S3 buckets on different AWS Regionsï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-regions)
* Multiple AWS account support, see [S3 buckets on different AWS accountsï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder/blob/main/docs/log_forwarding.md#forward-logs-from-s3-buckets-on-different-aws-accounts)

For detailed instructions on how to set up log ingestion from AWS S3, see [documentation on GitHubï»¿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

### AWS Lambda log collection

You can collect logs directly from your AWS Lambda functions and send them to Dynatrace for analysis. The solution is an alternative to the CloudWatch log forwarder with benefits in terms of cost and latency, and is also easier to set up, particularly if AWS Lambda tracing is already in place. As part of the OneAgent installation process, this feature provides a streamlined solution for collecting logs from your Lambda functions. For more information, see [AWS Lambda documentation page](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Collect logs from AWS Lambda functions").

### AWS log monitoring using log forwarder Deprecated

You can stream logs from Amazon CloudWatch into Dynatrace logs via an ActiveGate.

To enable AWS log forwarding, you need to deploy our special-purpose CloudFormation stack into your AWS account. The stack consists of a Kinesis Firehose instance and a Lambda function. These resources incur AWS costs according to standard AWS billing policy. The same applies to included self-monitoring resources (CloudWatch dashboards and metrics).

For detailed instructions on how to set up AWS log forwarding, see [Log monitoring with AWS log forwarder](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder#prereq "Use AWS log forwarding to ingest AWS logs.").

### Stream logs via Amazon Data Firehose

Dynatrace integration with Amazon Data Firehose provides a simple and safe way to ingest AWS logs.

To enable AWS log forwarding, you need to create Amazon Data Firehose instance and configure it with your Dynatrace environment as a destination. Then you can connect your CloudWatch log groups by creating a Subscription Filter or send logs directly to Firehose from services that support it (e.g. VPC flow logs). Firehose and other created cloud resources incur AWS costs according to the standard AWS billing policy.

## Microsoft Azure

Azure log forwarding allows you to stream Azure logs from Azure Event Hubs into Dynatrace logs via an Azure Function App instance. It supports both Azure resource logs and activity logs.

Azure log forwarding is performed directly through Cluster API. If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.

Deployment of Azure log forwarder results in creating the following resources:

* Storage account (`Microsoft.Storage/storageAccounts`)
* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)
* Azure App Service plan (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Azure log forwarder uses Linux based Azure function by default. Windows based function is not supported.

For details about the resources created, see the [Azure Resource Manager file on GitHubï»¿](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json)

For detailed instruction on how to set up Azure log forwarding see, [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure#prereq "Use Azure log forwarding to ingest Azure logs.").

## Google Cloud

To set up Google Cloud monitoring for metrics and logs, you'll run the deployment script in Google Cloud Shell. During setup, a new Pub/Sub subscription will be created. GKE will run two containers: a metric forwarder and a log forwarder. After installation, you'll get metrics, logs, dashboards, and alerts for your configured services in Dynatrace. Instructions will depend on the location where you want the deployment script to run:

* [On a new GKE Autopilot cluster created automatically](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."). Recommended
* [On an existing GKE standard or GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster").

Depending on where you want log ingestion to be performed, you may need additional resources. For example, for Managed deployments, there is a possibility to use an AG for log ingestion. But you have to do it manually since the installation script does not deploy it.

For all log ingestion options, see [Log ingestion](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#ingestion "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

## Related topics

* [DDUs for Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")


---


## Source: lm-fluent-bit-logs-k8s.md


---
title: Stream Kubernetes logs with Fluent Bit (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-fluent-bit-logs-k8s
scraped: 2026-02-18T05:55:55.565227
---

# Stream Kubernetes logs with Fluent Bit (Logs Classic)

# Stream Kubernetes logs with Fluent Bit (Logs Classic)

* Tutorial
* 5-min read
* Updated on Oct 08, 2025

Log Monitoring Classic

For the newest Dynatrace version, see [Stream Kubernetes logs with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.").

This page provides instructions for deploying and configuring Fluent Bit in your Kubernetes environment for log collection.

## Prerequisites

* Setup [security context constraints (SCC)ï»¿](https://dt-url.net/fb02ljw) properly if you use OpenShift.
* Helm is required. Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).
* Egress traffic must be allowed from the namespace in which Fluent Bit is installed (`dynatrace-fluent-bit`), to Dynatrace.
* For workload enrichment, Dynatrace Operator version 1.1.0+ is required.

## Customize Fluent Bit configuration

Follow the step-by-step guide to prepare the configuration for Fluent Bit.

1. Copy the sample `values.yaml` file and open it with your preferred editor.

   Container logs example (values.yaml)

   ```
   openShift:



   # set to true for OpenShift



   enabled: false



   securityContext:



   capabilities:



   drop:



   - ALL



   readOnlyRootFilesystem: true



   # uncomment the line below for OpenShift



   #privileged: true



   rbac:



   nodeAccess: true



   config:



   inputs: |



   [INPUT]



   Name tail



   Tag kube.*



   Path /var/log/containers/*.log



   DB /fluent-bit/tail/kube.db



   DB.Sync Normal



   multiline.parser cri



   Mem_Buf_Limit 15MB



   Skip_Long_Lines On



   filters: |



   [FILTER]



   Name kubernetes



   Match kube.*



   Merge_Log On



   Keep_Log Off



   K8S-Logging.Parser Off



   K8S-Logging.Exclude Off



   Labels Off



   Annotations On



   Use_Kubelet On



   Kubelet_Host ${NODE_IP}



   tls.verify Off



   Buffer_Size 0



   # Only include logs from pods with the annotation



   #[FILTER]



   #    Name grep



   #    Match kube.*



   #    Regex $kubernetes['annotations']['logs.dynatrace.com/ingest'] ^true$



   # Only include logs from specific namespaces, remove the whole filter section to get all logs



   #[FILTER]



   #    Name grep



   #    Match kube.*



   #    Logical_Op or



   #    Regex $kubernetes['namespace_name'] ^my-namespace-a$



   #    Regex $kubernetes['namespace_name'] ^my-namespace-b$



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under kubernetes



   Add_prefix kubernetes.



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under kubernetes.annotations



   Add_prefix kubernetes.annotations.



   [FILTER]



   Name nest



   Match kube.*



   Operation nest



   Nest_under dt.metadata



   Wildcard kubernetes.annotations.metadata.dynatrace.com/*



   [FILTER]



   Name parser



   Match kube.*



   Key_name kubernetes.annotations.metadata.dynatrace.com



   Parser docker



   Preserve_Key false



   Reserve_Data true



   [FILTER]



   Name nest



   Match kube.*



   Operation lift



   Nested_under dt.metadata



   Remove_prefix kubernetes.annotations.metadata.dynatrace.com/



   [FILTER]



   Name modify



   Match kube.*



   # Map data to Dynatrace log format



   Rename time timestamp



   Rename log content



   Rename kubernetes.host k8s.node.name



   Rename kubernetes.namespace_name k8s.namespace.name



   Rename kubernetes.pod_id k8s.pod.uid



   Rename kubernetes.pod_name k8s.pod.name



   Rename kubernetes.container_name k8s.container.name



   Add k8s.cluster.name ${K8S_CLUSTER_NAME}



   Add k8s.cluster.uid ${K8S_CLUSTER_UID}



   # deprecated, but still in use



   Add dt.kubernetes.cluster.name ${K8S_CLUSTER_NAME}



   Add dt.kubernetes.cluster.id ${K8S_CLUSTER_UID}



   Remove_wildcard kubernetes.



   outputs: |



   # Send data to Dynatrace log ingest API



   [OUTPUT]



   Name http



   Match kube.*



   host ${DT_INGEST_HOST}



   port 443



   tls On



   tls.verify On



   uri /api/v2/logs/ingest



   format json



   allow_duplicated_headers false



   header Authorization Api-Token ${DT_INGEST_TOKEN}



   header Content-Type application/json; charset=utf-8



   json_date_key timestamp



   json_date_format iso8601



   log_response_payload false



   daemonSetVolumes:



   - hostPath:



   path: /var/lib/fluent-bit/



   name: positions



   - hostPath:



   path: /var/log/containers



   name: containers



   - hostPath:



   path: /var/log/pods



   name: pods



   daemonSetVolumeMounts:



   - mountPath: /fluent-bit/tail



   name: positions



   - mountPath: /var/log/containers



   name: containers



   readOnly: true



   - mountPath: /var/log/pods



   name: pods



   readOnly: true



   podAnnotations:



   dynatrace.com/inject: "false"



   #  Uncomment this to collect Fluent Bit Prometheus metrics



   #  metrics.dynatrace.com/path: "/api/v1/metrics/prometheus"



   #  metrics.dynatrace.com/port: "2020"



   #  metrics.dynatrace.com/scrape: "true"



   envWithTpl:



   - name: K8S_CLUSTER_UID



   value: '{{ (lookup "v1" "Namespace" "" "kube-system").metadata.uid }}'



   env:



   - name: K8S_CLUSTER_NAME



   value: "{ENTER_YOUR_CLUSTER_NAME}"



   - name: DT_INGEST_HOST



   value: "{your-environment-id}.live.dynatrace.com"



   - name: DT_INGEST_TOKEN



   value: "{ENTER_YOUR_INGEST_TOKEN}"



   - name: NODE_IP



   valueFrom:



   fieldRef:



   apiVersion: v1



   fieldPath: status.hostIP
   ```
2. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope for the `DT_INGEST_TOKEN` environment variable.
3. Update the `K8S_CLUSTER_NAME`, `DT_INGEST_HOST`, and `DT_INGEST_TOKEN` environment variables in the `values.yaml` file. Use the same cluster name that you have configured in Dynatrace for `K8S_CLUSTER_NAME`, and specify your SaaS or Managed endpoint as `DT_INGEST_HOST`.
4. Optional Adapt the filter section in the `values.yaml` file to target specific namespaces or pods, as described in the [Fluent Bit Filter sectionï»¿](https://dt-url.net/m903n8q) for details.
5. Optional Ensure to remove or mask any sensitive information in the logs.
6. Save the file.

## Install and configure Fluent Bit with Helm

1. Add the fluent repository to your local Helm repositories

   ```
   helm repo add fluent https://fluent.github.io/helm-charts
   ```
2. Update the Fluent Bit repository

   ```
   helm repo update
   ```
3. Install Fluent Bit with the prepared configuration

   ```
   helm install fluent-bit fluent/fluent-bit -f values.yaml --create-namespace --namespace dynatrace-fluent-bit
   ```

## Uninstall Fluent Bit

Uninstall Fluent Bit from your Kubernetes environment using the following command:

```
helm uninstall fluent-bit
```

## View ingested logs

Monitored logs are accessible at the cluster, namespace, workload, and pod levels and can be inspected on the details pages of each entity.

![Pod logs](https://dt-cdn.net/images/podlogsfromfluentbitclassic-1920-32cea17fc9.png)

Alternatively, you can navigate to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**, where filtering can be done in either simple or advanced mode.

![Logs](https://dt-cdn.net/images/view-ingested-logs-1920-4339b9537f.png)

## Limitations

* `GKE Autopilot` is not supported.
* `fluentbit.io/parser` and `fluentbit.io/exclude` annotations are disabled by default.

## Troubleshooting

Visit [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718) in the Dynatrace Community, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

### Check that Fluent Bit pods are running

```
kubectl get pods -n dynatrace-fluent-bit
```

```
NAME               READY   STATUS              RESTARTS    AGE



fluent-bit-5jzlr   0/1     CrashLoopBackOff    1 (7s ago)  11s



fluent-bit-8zfr4   1/1     Running             0           38s



fluent-bit-qxjzh   1/1     Running             0           39s
```

If pods are in an error state, then the helm values file might contain errors. Check logs of the non-running pods for details.

```
kubectl logs fluent-bit-5jzlr -n dynatrace-fluent-bit
```

### Check Fluent Bit health and metrics

[Fluent Bit metricsï»¿](https://dt-url.net/nh43pqz) give you insights into how the logs are being collected (`fluentbit_input_*`), filtered (`fluentbit_filter_*`) and sent to Dynatrace (`fluentbit_output_*`).

1. Find the node on which the pod you are troubleshooting is running.

   ```
   kubectl get pod pod-with-logs -o wide -n dms
   ```

   ```
   NAME            READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   pod-with-logs   1/1     Running   0          31m   10.28.2.41   some-node-782e86b8-mnoz    <none>           <none>
   ```
2. Find the Fluent Bit pod that runs on the same node.

   ```
   kubectl get pods -o wide -n dynatrace-fluent-bit
   ```

   ```
   NAME               READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   fluent-bit-5jzlr   1/1     Running   0          30m   10.28.3.44   some-node-782e86b8-zdb1    <none>           <none>



   fluent-bit-8zfr4   1/1     Running   0          30m   10.28.4.23   some-node-782e86b8-mkjw    <none>           <none>



   fluent-bit-qxjzh   1/1     Running   0          30m   10.28.2.42   some-node-782e86b8-mnoz    <none>           <none>
   ```
3. Set up Fluent Bit pod metrics port forwarding to your localhost.

   ```
   kubectl port-forward fluent-bit-qxjzh 2020:2020 -n dynatrace-fluent-bit
   ```
4. Check the health endpoint.

   ```
   curl http://127.0.0.1:2020/api/v1/health
   ```

   ```
   ok
   ```
5. Examine the metrics.

   * `fluentbit_output_proc_*` metrics indicate how many logs are being ingested
   * `fluentbit_*` metrics give you more insights into what happens before that

   ```
   curl http://127.0.0.1:2020/api/v2/metrics | grep fluentbit_output_proc
   ```

   ```
   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_records_total{name="http.0"} = 767



   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_bytes_total{name="http.0"} = 359630
   ```
6. When `fluentbit_output_errors_total` or `fluentbit_output_retries_failed_total` metrics indicate problems, a potential reason is that you have reached [log monitoring limitsï»¿](https://dt-url.net/vj23poy).

## Related topics

* [Stream logs to Dynatrace with Fluent Bit (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace.")


---


## Source: lm-log-data-transformation.md


---
title: Automatic log enrichment (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation
scraped: 2026-02-18T05:51:45.957891
---

# Automatic log enrichment (Logs Classic)

# Automatic log enrichment (Logs Classic)

* Explanation
* 3-min read
* Updated on Apr 07, 2023

Log Monitoring Classic

For the newest Dynatrace version, see [Automatic log enrichment](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

Dynatrace enables you to transform logs ingested both via OneAgent and API.

## Transform the API-ingested logs

Log ingestion API automatically transforms `status`, `severity`, `level`, and `syslog.severity` severity keys to the `loglevel` attribute.

The input values for the `status`, `severity`, `level`, and `syslog.severity` severity keys are transformed (transformation is not case sensitive) into output values for the `loglevel` attribute based on the mapping below:

Input value

Output value

Example value

Begins with `emerg` or `f`

`EMERGENCY`

`Emergency`, `fail`, `Failure`

Begins with `e` excluding `emerg`

`ERROR`

`Error`, `error`

Begins with `a`

`ALERT`

`alarm`, `Alert`

Begins with `c`

`CRITICAL`

`Critical`, `crucial`

Begins with `s`

`SEVERE`

`Severe`, `serious`

Begins with `w`

`WARN`

`warn`, `Warning`

Begins with `n`

`NOTICE`

`note`, `Notice`

Begins with `i`

`INFO`

`Info`, `information`

Begins with `d` or `trace` or `verbose`

`DEBUG`

`debug`, `TRACE`, `Verbose`

## Transform all types of logs

This transformation applies both to OneAgent-ingested logs and API-ingested logs.

Additionally, for each log event, a `status` attribute is created with a value that is a sum of `loglevel` values based on the following grouping:

Included `loglevel` values

Combined `status` attribute value

`SEVERE`, `ERROR`, `CRITICAL`, `ALERT`, `FATAL`, `EMERGENCY`

`ERROR`

`WARN`

`WARN`

`INFO`, `TRACE`, `DEBUG`, `NOTICE`

`INFO`

`NONE`

`NONE`

For example:
The `level` severity key in the Log ingestion API request parameter contains the value `serious`.

1. The `level` severity key is transformed into the `loglevel` attribute with the `serious` value mapped to `SEVERE` based on the above table.
2. The `loglevel` attribute containing the `SEVERE` value is grouped into `status` attribute. Based on the grouping table above, the `status` attribute will contain the `ERROR` value.
3. For the log event details, the log viewer will report the following:

* **status** - `ERROR`
* **loglevel** - `SEVERE`

## Attributes added during a log ingest via OneAgent

During the log ingestion via OneAgent, the following attributes are added automatically:

### General attributes (via OneAgent)

* `container.name`
* `container.image.name`
* `container.id`
* `dt.host_group.id`
* `dt.kubernetes.cluster.id`
* `dt.kubernetes.cluster.name`
* `dt.kubernetes.node.system_uuid`
* `dt.process.name`
* `event.type`
* `host.name`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.container.name`
* `k8s.deployment.name`
* `log.iostream`
* `loglevel`
* `log.source`
* `process.technology`
* `span_id`
* `status`
* `trace_id`
* `web_server.iis.site_id`
* `web_server.iis.site_name`
* `web_server.iis.application_pool`

### dt entity model attributes (via OneAgent)

* `dt.entity.cloud_application`
* `dt.entity.cloud_application_instance`
* `dt.entity.cloud_application_namespace`
* `dt.entity.container_group`
* `dt.entity.container_group_instance`
* `dt.entity.host`
* `dt.entity.kubernetes_cluster`
* `dt.entity.kubernetes_node`
* `dt.entity.process_group`
* `dt.entity.process_group_instance`
* `dt.source_entity`

## Related topics

* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")


---


## Source: log-data-ingest.md


---
title: Log ingestion API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-data-ingest
scraped: 2026-02-06T16:28:21.884183
---

# Log ingestion API (Logs Classic)

# Log ingestion API (Logs Classic)

* Overview
* 3-min read
* Updated on Jan 22, 2026

Log Monitoring Classic

For the newest Dynatrace version, see [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.").

Dynatrace automatically collects log and event data from a vast array of technologies. With generic log ingestion, you can stream log records to a system and have Dynatrace transform the stream into meaningful log messages.

The Log ingestion API allows you to stream log records to the system. It is available via [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") for JSON and text format or the [OTLP endpoint](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") for OTLP binary protobuf format.

* For Dynatrace SaaS, the Log ingestion endpoint is available in your environment.

* If the Environment ActiveGate is your choice for an endpoint in your local environment, install an ActiveGate instance:

  In Dynatrace Hub, select **ActiveGate** > **Set up**. The Log ingestion API v2 is automatically enabled on ActiveGate is responsible for serving the endpoint, collecting the data, and forwarding it to Dynatrace in batches.

* Saas endpoints:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Environment ActiveGate endpoints:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

Ingest endpoint will collect and attempt to automatically transform any log data containing the following JSON elements:

* Log content
* Timestamp
* Key-Values attributes

To view all predefined key-value attributes, such as the supported semantic attribute keys, check [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

## Log data queue on Environment ActiveGate

You can customize the log data queue properties by editing the `custom.properties` file (see [Configuration properties and parameters of ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) on your ActiveGate to set the following values:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Example

In this example, the API request ingests log data that will create a log event with defined log attributes `content`, `status`, `service.name`, and `service.namespace`.

The API token is passed in the Authorization header.

The response contains response code `204`.

#### Curl

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

#### Request URL

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Response content

```
Success
```

#### Response code

`204`

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related topics

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")


---


## Source: log-monitoring-journald.md


---
title: Log Monitoring from Journald (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-journald
scraped: 2026-02-18T05:48:55.319656
---

# Log Monitoring from Journald (Logs Classic)

# Log Monitoring from Journald (Logs Classic)

* Tutorial
* 4-min read
* Published Apr 22, 2025

Log Monitoring Classic

OneAgent version 1.307+

Log module is capable of reading, processing, and uploading entries from systemd-journald, a Linux-based centralized logging system service. Events/logs are usually stored in files located in the `/var/log/journal/'machine-id'/` directory, where `machine-id` is a long string of digits identifying the machine. These files are kept in a binary, compressed format, maintained by the systemd-journald engine to manage size per file and overall, retention, rotation, etc., according to its settings.

## How Journald works

To avoid the problems of manually tracking the files, such as rotation, decompression, or parsing, Log module uses system API calls to access the entire functionality. This is achieved by opening the system library, `libsystemd.so` and its dependencies, mapping selected functions from the library, and creating a context object, to communicate with the Journald system. This way, Log module becomes a client of Journald and can use a variety of its exposed functions.

At the beginning, Log module opens a handler at the default location of the Journald context. No specific path is used, allowing the handler to open its well-known location. Then the agent reads the entries one by one, keeping track of the current position.

## Enable Journald support

To enable Journald log detection, follow the steps below:

1. Go to **Settings** > **Log Monitoring** > **Log module feature flags**.
2. Select **Enable Journald log detector**.
3. Select **Save changes**.

Enabling the feature flag is required to opt-in. Without it, even with configured ingest rules, Journald logs will not appear in Dynatrace.

## Configure log ingestion from Journald

You can enable log ingestion from Journald by either configuring the default Journald [ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis."), or by configuring the tenant storage upload, for example `kubelet.service` as `Journald.unit` from Journald.

### Enable the default ingestion rule

For new accounts, the default Journald ingest rule is enabled by default, and the configuration described in this section is not needed.

Follow the steps below to configure the default Journald ingest rule:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Enable the **[Built-in] Ingest Journald logs** rule to ingest all Journald logs.
3. Select **Save changes**.

### Create a custom ingestion rule

Follow the steps below to configure the tenat storage upload for `kubelet.service` logs from Journad:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Select **Add matcher**. This is the first matcher to match two specified process groups.
4. From the **Attribute** list, select **Journald Unit**.
5. Select **Add value** and type `kubelet.service`.
6. Select **Add matcher** again to match the specified log data source.
7. From the **Attribute** list, select **Log source**.
8. Select **Add value** and enter **Journald** as the value.
9. Select **Save changes**.

## Attributes selected in journald

Each entry is processed to gain the following attributes:

Semantic attribute name

Description

`Timestamp`

Retrieved by direct API call for timestamp, results in microseconds since epoch converted to agentâs timestamp domain resolution

`Content`

The extracted value of the API call for data with the **MESSAGE** field as a selector

`Journald.unit`

The extracted value of the API call for data with the **UNIT** field as a selector
As an alternative, the ***SYSTEMD\_UNIT*** field is searched. It may happen that none of the fields are found.

`LogEntryLevel`

The extracted value of the API call for data with the **PRIORITY** field as a selector, priority. Consult the table below for the definitions of the priority levels.

## Priority level

Journald priority codes are used to mark the importance of a message. The following table shows how these priorities translate into Dynatrace severity:

Value

Severity

Description

0

Emergency

System is unusable

1

Alert

Should be corrected immediately

2

Critical

Critical conditions

3

Error

Error conditions

4

Warn

May indicate that an error will occur if action is not taken

5

Notice

Events that are unusual, but not error conditions

6

Info

Normal operational messages that require no action

7

Debug

Messages which may need to be enabled first, only useful for debugging


---


## Source: log-monitoring-kubernetes.md


---
title: Log Monitoring in Kubernetes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes
scraped: 2026-02-18T05:48:01.102892
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


---


## Source: log-rotation-patterns.md


---
title: Log rotation patterns (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns
scraped: 2026-02-18T05:57:07.358558
---

# Log rotation patterns (Logs Classic)

# Log rotation patterns (Logs Classic)

* Explanation
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace monitors rotation patterns for log files. This functionality ensures the completeness of the file reading process, even if OneAgent is temporarily switched off or the application crashes. The monitoring process has two dimensions:

* [Rotation tracking based on the file name](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns#filenametracking "Learn about supported log rotation patterns")
* [Rotation tracking based on log generation type](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-rotation-patterns#gennametracking "Learn about supported log rotation patterns")

## Rotation tracking based on the file name

Typically, rotated log files have their specific rotation identifiers embedded into file names. The rotation identifiers can be an appended timestamp or a counter. For example:

* Active log file with no rotation identifier:  
  `/var/log/application.log`
* Rotated/archived log files with appended identifiers as date stamp:  
  `/var/log/application.log.20220509`  
  `/var/log/application.log.20220508`  
  â¦  
  `/var/log/application.log.20220503`
* Rotated/archived log files with appended identifiers as counter:  
  `/var/log/application.log.1`  
  `/var/log/application.log.2`

### Rotation identifier and the log name

Depending on the file type, Dynatrace might replace the rotation identifier with the `#` symbol in the log autodiscovery process.

#### Example of rotation identifier replacement with hashtag

Active log file:
`/var/log/application20220509_060000.log`

Rotated/archived log files:  
`/var/log/application20220509_030000.log`  
`/var/log/application20220508_000000.log`  
`/var/log/application20220508_210000.log`  
â¦  
`/var/log/application20220503_090000.log`

are detected as `/var/log/application#_#.log`

### Supported rotation identifiers

The data types that can be substituted by `#` include:

* Decimal numbers of any length
* Hexadecimal numbers that are at least eight digits long
* Globally unique identifiers (GUIDs), the 128-bit text strings that represent identification (ID)

To be monitored, a rotated log file must contain a rotation identifier preceded **and** followed by one of the predefined separators, including `.` (dot), `-` (hyphen), `_` (underscore), `()`(brackets) or `[]` (square brackets).
In a scenario where a rotation identifier is a decimal number, it is sufficient that it is either preceded **or** followed by a predefined separator.

Apart from explicit rotation identifiers visible under the `#` symbol, Dynatrace implicitly supports monitoring of rotated files that:

* Contain a decimal suffix appended to the end of the log name
* Contain a decimal infix instead of any of the predefined separators (`.`, `-`, `_`, `()`, `[]`)

#### Examples of detected rotated log files with implicit identifiers.

Active log file:
`/var/log/application.log`  
Dynatrace detects a file with the '/var/log/application.log' name and identifies rotated files in all examples below:

`/var/log/application.log.1`  
`/var/log/application.log.2`  
â¦  
`/var/log/application.log.9`  
or  
`/var/log/application.20220509.120000.log`  
`/var/log/application.20220509.060000.log`  
`/var/log/application.20220508.120000.log`  
â¦  
`/var/log/application.20220503.120000.log`  
or  
`/var/log/application.20220509.log.1`  
`/var/log/application.20220509.log.2`  
`/var/log/application.20220508.log.1`  
â¦  
`/var/log/application.20220503.log.1`  
`/var/log/application.20220503.log.2`

## Rotation tracking based on log generation type

Dynatrace supports the main types of log generation, including:

* Rotated log generation based on the **'Index'** rule, where the application opens files one by one and provides them with index numbers.
* Rotated log generation based on the **'Rename and replace'** rule, where the application logs to a file with the same name. If a rotation criterion is met (for example, the required file size is reached), a new file with the same name is opened while the old one is renamed.
* Rotated log generation based on the **'Copy and truncate'** rule, where the application logs to a file with the same name, but the rotation itself is performed by an external process that, after a rotation criterion is met, copies the file's content into another location and truncates the content of the original (active) file. The 'logrotate' process on Linux is an example here.

## Log rotation limits

Scenarios that are not supported in the rotated log monitoring process include:

Type

Description

Rotated log generation with a directory change

The potential consequence is the creation of duplicates and/or incomplete logs.

Rotated log generation with immediate compression

If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed. Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log ingest. There should be at least one uncompressed rotated file.

Rotated log generation with queue logic

The oldest log records are removed whenever new content is added to a file, resulting in a relatively constant log file size. This scenario can be easily replaced with a supported rotation scheme by, for example, starting a new file when the current file reaches a predefined size.


---


## Source: log-storage.md


---
title: Log ingest rules (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage
scraped: 2026-02-18T05:52:01.321423
---

# Log ingest rules (Logs Classic)

# Log ingest rules (Logs Classic)

* Tutorial
* 16-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.252+ OneAgent version 1.243+

For the newest Dynatrace version, see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

If you use a OneAgent version earlier than 1.243 and Dynatrace Cluster version earlier than 1.252, go to [Log Sources and Storage](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources "Learn how to include and exclude log sources for analysis.").

Dynatrace allows you to include and exclude specific log sources for your analysis. Using [Dynatrace identity and access management (IAM) framework](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"), you can control which user can change configurations on which scope.

The configuration is based on rules that use matchers for hierarchy, log path, and process groups. These rules determine which log files among those detected by OneAgent, either automatically or defined as custom log sources, are ingested.

## Log ingest rule

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the name for your configuration.  
   By default, the **Include in storage** button is turned on, indicating that items configured by this rule will be stored in Dynatrace. Alternatively, you can select the **Exclude from storage** rule type.
3. Expand **Details** of your new rule and select **Add matcher** to create a specific match for this rule.  
   Multiple matchers can be included in one rule.

   Other than the **Log source** attribute in Windows (due to file paths being case insensitive), matchers are case-sensitive.
4. Select the matching attribute:

Attribute

Description

Search dropdown logic

**Process group**

Matching is based on the process group ID. The process group is determined by the detection rules described in [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection"). If a process changes its process group, log ingestion for that process may start or stop based on the changes made.

Attributes visible in the last 3 days are listed.

**Log source**

Matching is based on a log path or a Windows event log full name; wildcards are supported in form of an asterisk. Autocompletion for **Log source** is only partial. You can either choose one of the predefined values or enter your log source.

Can be entered manually. No time limit.

**Log source origin**[1](#fn-1-1-def)

Matching is based on the detector used by the log agent to discover the log file. Available options include:

* **Custom log source configuration**: Log source provided by the user through custom configuration.
* **Open log file detector**: Logs discovered automatically by the log module's autodetection mechanism.
* **System log detector**: Includes Windows application log or `/var/log/syslog` for Linux.
* **Container output**: Autodetected Kubernetes or Docker logs.
* **IIS log detector**: Logs detected by the IIS detector.

Can be entered manually. No time limit.

**Log content**

Matching is based on the content of the log; wildcards are supported in form of an asterisk.

Can be entered manually. No time limit.

**Log record level**[2](#fn-1-2-def)[3](#fn-1-3-def)

Matching is based on the level of the log record. It supports the following values: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`.

Can be entered manually. No time limit.

**journald unit**[4](#fn-1-4-def)

Matching is based on any of the selected journald units. Unless you enrich other log sources with a `journald.unit` attribute, you should also add a `log.source` or `log.source.origin` matcher to the ingest rule to boost the Log Module performance.

Can be entered manually. No time limit.

**Host tag**[5](#fn-1-5-def)[6](#fn-1-6-def)

Matching is based on the host tag. The attribute only supports the tags set with the [OneAgent command line tool](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or with the [Remote configuration](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") in a `key=value` pair format. They can be distinguished by the `[Environment]` prefix on the UI, but you should use the value without the prefix.
Multiple tags can be specified in a single matcher, but each tag needs to have the same key, such as `logscope=frontend`, `logscope=backend`.

Can be entered manually. No time limit.

**Kubernetes container name**

Matching is based on the name of the Kubernetes container.

Attributes visible in the last 90 days are listed.

**Kubernetes namespace name**

Matching is based on the name of the Kubernetes namespace.

Attributes visible in the last 90 days are listed.

**Kubernetes deployment name**

Matching is based on any of the selected deployments. It is deprecated for the OneAgent Log Module managed by Dynatrace Operator or when the **Collect all container logs** feature flag is enabled.

Can be entered manually.

**Kubernetes pod annotation**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod annotations. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container** logs feature flag to be enabled.

Can be entered manually.

**Kubernetes pod label**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected pod labels. The correct format is `key=value`. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Kubernetes workload name**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload names. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Attributes visible in the last 90 days are listed.

**Kubernetes workload kind**[4](#fn-1-4-def)[7](#fn-1-7-def)

Matching is based on any of the selected workload kinds. It requires either the OneAgent Log Module managed by Dynatrace Operator or the **Collect all container logs** feature flag to be enabled.

Can be entered manually.

**Docker container name**

Matching is based on the name of the container.

Attributes visible in the last 90 days are listed.

**DT entity container group ID**

Matching is based on any of the selected container groups.

Can be entered manually. No time limit.

**Process technology**

Matching is based on the technology name.

Can be entered manually. No time limit.

**Windows log record event ID**[3](#fn-1-3-def)

Matching is based on any of the selected event ID attribute.

Can be entered manually. No time limit.

**Windows log record source**[3](#fn-1-3-def)

Matching is based on any of the selected source attributes.

Can be entered manually. No time limit.

**Windows log record task category**[3](#fn-1-3-def)

Matching is based on any of the selected task category attributes.

Can be entered manually. No time limit.

**Windows log record operational code**[3](#fn-1-3-def)

Matching is based on any of the selected operational code attribute.

Can be entered manually. No time limit.

**Windows log record user name**[8](#fn-1-8-def)

Matching is based on any of the selected user name attributes.

Can be entered manually. No time limit.

**Windows log record keywords**[8](#fn-1-8-def)

Matching is based on any of the selected keywords attributes.

Can be entered manually. No time limit.

1

OneAgent version 1.295+

2

Log record level attribute, transformed by OneAgent, is different than log `status` attribute transformed by Dynatrace server.

3

OneAgent version 1.273+

4

OneAgent version 1.309+

5

[Manually or automatically applied tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") are not visible to OneAgent.

6

OneAgent version 1.289+

7

Dynatrace Operator version 1.4.2+

8

OneAgent version 1.305+

The wildcard is supported for any attribute value, and might be used multiple times in a single value. However, some attributes, for example Process Group, have a limited, predefined list of possible values that are selected from an auto-complete list.

If no wildcard is used in the value, then the matcher looks for an exact fit to the value. If a wildcard is used, the matcher looks for the exact match. For example, the value `INFO` results in sending only the log data having the exact `INFO` string, but the value `*INFO*` (using the wildcards) matches log data that contain the `INFO` string in its content.

1. Select **Add value** and, from the **Values**, select the detected log data items (log files or process groups that contain log data). Multiple values can be added to the selected attribute. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
2. **Save changes**.

Defined rules can be reordered and are executed in the order in which they appear on the **Log storage** page.

7. To activate your rule, turn on the **Active** toggle.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

## Matching a list of rules to log data

Matching occurs in a predefined hierarchy and rules are executed from top to bottom. This means that if a rule above on the list matches certain log data, then the lower ones will be omitted. Items matched in the higher-level configurations are overwritten in the lower-level configurations if they match the same log data. If no rule is matched, the file is not sent. The matching hierarchy is as follows:

1. Host configuration rules
2. Host group configuration rules
3. Tenant configuration rules

## Configuration scopes

Three hierarchy scopes are supported: host, host group, and tenant. The scope with the least possible set of rules has priority over larger sets.

![Log ingest rules priority](https://dt-cdn.net/images/log-storage-rule-priority-white-1491-d1d8126129.png)

1. Log storage rules configured for a host take precedence over log storage rules configured for a host group.
2. Log storage rules configured for a host group take precedence over log storage rules configured for a tenant.

### Host scope

The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Log ingest rules**.
5. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Log ingest rules**.
7. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### Tenant scope

The tenant scope is available in the settings menu.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Configure storage upload by adding rules with a set of attributes that matches the log data to be stored by Dynatrace.

### List hosts and host groups with overriding rules

The table on **Settings** > **Log Monitoring** > **Log ingest rules** lists all log storage rules that you have set at the tenant level. However, you may want to see where you have set log storage rules for hosts and host groups that override the tenant-level rules.

To list all entities (hosts and host groups) to which more specific log storage rules are applied

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. In the upper-right corner of the **Log ingest rules** page, select **More** (**â¦**) > **Hierarchy and overrides**. A searchable **Hierarchy and overrides** panel lists all entities (hosts and host groups) on which you have set log storage rules that override the tenant-level rules listed on **Settings** > **Log Monitoring** > **Log ingest rules**.
3. Select an entity name to go to that entity's **Log ingest rules** page.

## Example upload

In this example, we configure the tenant storage upload for `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`. The log storage rule consists of two matchers: the first matcher finds the process groups and the second matcher matches only for the defined log source.

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Select **Add matcher**. This is the first matcher to match two specified process groups.
4. From the **Attribute** list, select **Process group**.
5. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
6. Select **Add value** again, type `IIS` and select the second process group from the suggestion list: `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.
7. Select **Add matcher** again. This is the second matcher to match the specified log data source.
8. From the **Attribute** list, select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as the value.
10. Save changes.

## Example exclude

In this example, we configure the tenant storage upload for all log sources except `c:\inetpub\logs\LogFiles\ex_*.log` files in a process group `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

1. Go to **Settings** and select **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Turn off **Send to storage**.
4. Select **Add matcher**. This is the first matcher to match the specified process group.
5. From the **Attribute** list, select `Process group`.
6. Select **Add value** and type IIS, and then, from the suggestion list, select `IIS (PROCESS_GROUP-3D9D854163F8F07A)`.
7. Select **Add matcher** again. This is the second matcher to exclude the specified log data source.
8. From the **Attribute** list select **Log source**.
9. Select **Add value** and enter `c:\inetpub\logs\LogFiles\ex_*.log` as a value.
10. Save changes.

## REST API

You can use the Settings API to manage your log ingest rules:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for log ingest rules, list all available schemas and look for the `builtin:logmonitoring.log-storage-settings` schema identifier.

Log ingest rules can be configured for the following scopes:

* `tenant` â configuration object affects all hosts on a given tenant.
* `host_group` â configuration object affects all hosts assigned to a given host group.
* `host` â configuration object affects only the given host.

To create a log ingest rule using the API:

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The log storage configuration schema identifier (`schemaId`) is `builtin:logmonitoring.log-storage-settings`. Here is an example JSON payload with the log storage configuration:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.log-storage-settings",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "send-to-storage": true,



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

## Examples

The examples that follow show the results of various combinations of rules and matchers.

### Example 1: Multiple rules

In this example, there are two rules:

* Rule 1 is an Exclude rule and has two matchers: the process group attribute is Apache, and the Log source attribute is `access.log`).
* Rule 2 is an Include rule and has one matcher: the process group attribute is Apache.

Results: `access.log` is not sent, `error.log` (of Apache) is sent, and `error.log` (of other PG) is not sent.

* `access.log` written by Apache matches the first rule, which has `send-to-storage: false`, so it is not sent.
* `access.log` not written by Apache doesn't match the first rule (due to incorrect process group), and doesn't match the second rule, so it is not sent.
* `error.log` written by Apache does not match the first rule (due to incorrect source), but it matches the second rule, which has `send-to-storage: true`, so it is sent.
* `error.log` not written by Apache doesn't match the first rule (due to both incorrect process group and log source), and doesn't match the second rule, so it is not sent.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/access.log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 2: Send logs written by Apache and containing 'ERROR'

This task requires setting one rule with two matchers.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 3: Send logs written by Apache or containing 'ERROR'

This task requires setting two rules with one matcher each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 4: Send logs written by Apache, and containing 'ERROR' and 'Customer'

This task requires setting one rule with three matchers, with one value each.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*"



]



},



{



"attribute": "log.content",



"values": [



"*Customer*"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 5: Send logs written by Apache, and containing 'ERROR' or 'Customer'

This task requires setting one rule with two matchers: a matcher with the process group value, and a matcher with two content values.

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "log.content",



"values": [



"*ERROR*", "*Customer*"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Example 6: Send logs written by Apache or MySQL

This task requires setting two rules, or one rule with one matcher having two values.  
Rules with two matchers will not work here.

Setting two rules:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

Setting one rule with one matcher having two values:

```
{



"send-to-storage": true,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



}
```

### Example 7: Send all logs

This task requires setting a rule without any matchers.

```
{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

### Example 8: Send all logs except Apache and MySQL logs

This task requires setting two rules.

* The first rule is an Exclude rule with one matcher having two values.
* The second rule does not contain any matchers.

The rules have to be executed in the order indicated below.

```
{



"send-to-storage": false,



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"send-to-storage": true,



"matchers": [



],



"enabled": true



}
```

## FAQ

Will older OneAgents work with this solution?

OneAgent versions earlier than `1.243` won't send any data; they will get an empty whitelist in response.

Why don't I see any configuration on the global page after migration from the hosts' perspective?

All host perspective configs are migrated to the corresponding host scope.

Are log ingest rules the same as/part of the autodiscovery process?

No. Autodiscovery is a mechanism of OneAgent that detects logs, but it doesn't mean that log files are sent to storage automatically. A configuration page for autodiscovery is planned for a future release. To learn more about autodiscovery, see [Log content autodiscovery (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")

Is the order of configuration items important?

Yes, configuration items are matched from top to bottom, meaning that the top value is the most important.

How long do I need to wait for the configuration to be applied to the host?

It is applied within 90 seconds.

Does adding a content matcher reduce the number of log events sent to Dynatrace?

Yes. A content matcher narrows down the scope of log events (log entries) according to the criteria set (for example, searching only for error logs).

Where is filtering carried out, in Dynatrace and or in OneAgent?

* Filtering (narrowing down the scope according to the criteria set) is carried out in OneAgent.
* Setting limits (for example, the log events per minute limit or the attribute values limit) is conducted in Dynatrace.

Does filtering the content reduce DDU cost and/or network usage?

Yes. Content filtering conducted on OneAgent reduces both DDU costs and network usage. You can calculate the cost and network use reduction by determining your total data consumption and deducting the GB size of data that was filtered out. For details on how DDUs costs are calculated, see:

* [Log Monitoring DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")

* [Log Management and analytics powered by Grail DDU calculation](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.")


---


## Source: logs-classic-ingestion-api.md


---
title: Log ingestion API (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api
scraped: 2026-02-18T05:40:49.470113
---

# Log ingestion API (Logs Classic)

# Log ingestion API (Logs Classic)

* Overview
* 3-min read
* Updated on Jan 30, 2026

Log Monitoring Classic

For the newest Dynatrace version, see [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.").

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system, and have Dynatrace transform the stream into meaningful log messages.

The Log ingestion API allows you to stream log records to the system. It is available via [Ingest JSON and TXT logs (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-ingest-json-txt-logs "Understand how JSON and TXT logs are processed.") or via [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

* For Dynatrace SaaS, the Log ingestion endpoint is available in your environment.

* If the Environment ActiveGate is your choice for an endpoint in your local environment, install an ActiveGate instance:

In Dynatrace Hub, select **ActiveGate** > **Set up**.

The Log ingestion API v2 is automatically enabled on ActiveGate. ActiveGate is responsible for serving the endpoint, collecting the data, and forwarding it to Dynatrace in batches.

* Saas endpoints:

  + `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest`
  + `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

* Environment ActiveGate endpoints:

  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest`
  + `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

## Log data queue on Environment ActiveGate

You can customize the log data queue properties by editing the `custom.properties` file (see [Configuration properties and parameters of ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#generic-ingest "Learn which ActiveGate properties you can configure based on your needs and requirements.")) on your ActiveGate to set the following values:

```
[generic_ingest]



#disk_queue_path=<custom_path> # defaults to temp folder



#disk_queue_max_size_mb=<limit> # defaults to 300 MB
```

503 Usable space limit reached

The log data ingestion API returns a `503 Usable space limit reached` error when the ingested log data exceeds the configured queue size. Typically, this is a temporary situation that occurs only during spikes. If this error persists, increase the value of `disk_queue_max_size_mb` in `custom.properties` to allow log ingestion spikes to be queued.

## Example

In this example, the API request ingests log data that will create a log event with defined log attributes `content`, `status`, `service.name`, and `service.namespace`.

The API token is passed in the Authorization header.

The response contains response code `204`.

#### Curl

```
curl -X POST \



https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest \



-H 'Content-Type: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-d '[



{



"content": "Exception: Custom error log sent via Log ingestion API",



"status": "error",



"service.name": "log-monitoring-tenant",



"service.namespace": "dev-stage-cluster"



}



]'
```

#### Request URL

```
https://environment.activegate.domain.com:9999/e/abc123a/api/v2/logs/ingest
```

#### Response content

```
Success
```

#### Response code

`204`

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Related topics

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")


---


## Source: stream-logs-fluentd-k8s.md


---
title: Stream logs to Dynatrace with Fluentd on Kubernetes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-fluentd-k8s
scraped: 2026-02-18T05:57:30.625839
---

# Stream logs to Dynatrace with Fluentd on Kubernetes (Logs Classic)

# Stream logs to Dynatrace with Fluentd on Kubernetes (Logs Classic)

* Explanation
* 1-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

For the newest Dynatrace version, see [Stream logs to Dynatrace with Fluentd on Kubernetes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.").

The recommended way of streaming logs from Kubernetes nodes and pods to Dynatrace is described at [Log Monitoring in Kubernetes (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.").

Alternatively, you can use the [Dynatrace Fluentd pluginï»¿](https://dt-url.net/gb23475), which is an open-source module, to stream logs.

The architecture is illustrated below.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

## Capabilities

* Supports streaming logs to different Dynatrace environments from the same Kubernetes cluster. For example, you can send application pod logs to a different environment than the Kubernetes node logs.
* Supports streaming logs for [application-only integrations](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* Can be configured to stream logs directly to Dynatrace.

## Limitations

Logs coming from Fluentd aren't linked with the Kubernetes workloads. Consequently, you can't search for logs by Kubernetes workload on the **Log viewer** page in Dynatrace. However, you can still see logs on the corresponding **Kubernetes workloads** pages.

## Deploy integration

For instructions on how to deploy Fluentd integration, see the [documentation on GitHubï»¿](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")


---


## Source: stream-logs-to-dynatrace-with-logstash.md


---
title: Stream logs to Dynatrace with Logstash (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-to-dynatrace-with-logstash
scraped: 2026-02-18T05:50:45.725546
---

# Stream logs to Dynatrace with Logstash (Logs Classic)

# Stream logs to Dynatrace with Logstash (Logs Classic)

* Explanation
* 1-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

For the newest Dynatrace version, see [Stream logs to Dynatrace with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.").

[Dynatrace Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") uses OneAgent DaemonSet, which includes a log module. This is the recommended way of streaming logs from nodes and pods to Dynatrace.

Alternatively, you can use the [Dynatrace Logstash output pluginï»¿](https://github.com/dynatrace-oss/logstash-output-dynatrace), which is an open-source module, to stream logs.

![Logstash pipeline to Dynatrace](https://dt-cdn.net/images/logstash-anna-new-eb3c5ac7a3.svg)

## Capabilities

Supports sending logs to [Dynatrace log ingest API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

The Dynatrace Logstash output plugin also provides the following capabilities:

* Dynatrace API authentication
* Retry failed requests due to temporary network conditions
* Split large payloads into smaller batches ensuring each batch respects Dynatrace API limits (plugin version `0.5.1+`)
* Optional gzip compression (plugin version `0.6.1+`)
* Optional HTTP proxy configuration (plugin version `0.5.0+`)
* Optionally disable SSL verification for use with self-signed certificates

## Deploy integration

For instructions on how to deploy Logstash integration, see the [documentation on GitHubï»¿](https://github.com/dynatrace-oss/logstash-output-dynatrace/blob/main/README.md)

**Example configuration:**

```
output {



dynatrace {



id => "dynatrace_output"



ingest_endpoint_url => "${ACTIVE_GATE_URL}/api/v2/logs/ingest"



api_key => "${API_KEY}"



}



}
```


---


## Source: stream-logs-with-fluent-bit.md


---
title: Stream logs to Dynatrace with Fluent Bit (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit
scraped: 2026-02-17T21:30:49.025094
---

# Stream logs to Dynatrace with Fluent Bit (Logs Classic)

# Stream logs to Dynatrace with Fluent Bit (Logs Classic)

* Tutorial
* 3-min read
* Updated on Jan 22, 2026

Log Monitoring Classic

For the newest Dynatrace version, see [Stream logs to Dynatrace with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace.").

You can send logs to Dynatrace using Fluent Bit. Configure Fluent Bit to send logs to Dynatrace generic ingest API.

## Capabilities

* Fluent Bit is a multiplatform log processor and forwarder that allows you to collect data/logs from different sources, unify and send them to multiple destinations. It is compatible with the Docker and Kubernetes environments.
* Dynatrace can be configured as the target log management and analytics environment for your data thanks to Fluent Bit's configurable `http output`.
* You can use any of Fluent Bit input plugins to get logs and events from your application to Dynatrace.

## Configuration

The Fluent Bit `http output` plugin allows you to forward your logs to the Dynatrace Log ingestion endpoint.

1. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope.
2. [Deploy Fluent Bitï»¿](https://dt-url.net/zd034je).
3. To send logs into the Dynatrace [Log ingestion](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint, configure the [http output pluginï»¿](https://dt-url.net/0z034x4) through the configuration file.
4. In your main Fluent Bit configuration file, append the Output section with the following parameters:

```
[OUTPUT]



name  http



match *



header Content-Type application/json; charset=utf-8



header Authorization Api-Token {your-API-token-here}



allow_duplicated_headers false



host  {your-environment-id}.live.dynatrace.com



Port  443



URI   /api/v2/logs/ingest



Format json



json_date_format iso8601



json_date_key timestamp



tls On



tls.verify On
```

You can place your API token in the header or as `GET` variable in URI (see example below).

* For Dynatrace SaaS, the [Log ingestion](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") endpoint is available in your environment.

* If [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate#agtypes "Understand the basic concepts related to ActiveGate.") is your choice for an endpoint in local environment, install ActiveGate instance.

  In Dynatrace Hub, select **ActiveGate** > **Set up**.
* Log ingestion API v2 is automatically enabled on ActiveGate.

## Example

Fluent Bit is the recommended solution whenever reducing resource consumption is critical.
In the below example, you need to ingest your AWS Fargate logs. FireLens enables you to set up Fluent Bit for this ingestion.

### Ingest AWS Fargate logs with Fluent Bit

When creating a new task definition using the AWS Management Console, the FireLens integration section makes it easy to add a log router container. Follow the steps below to execute your ingest:

1. In the AWS Management Console, go to the Firelens integration section.

![Final log integration page in AWS Management Console](https://dt-cdn.net/images/final-log-route-integration-870-b11a329df9.png)

2. Pick the built-in Fluent Bit image.

3. Edit the container in which your app-generating logs are running.

4. In the **Storage and Logging** section, select **awsfirelens** as the log driver.

![Set AWS Firelens as a log driver](https://dt-cdn.net/images/log-driver-950-0bbba4a0fb.png)

The settings for the log driver should point to the log ingest API of your SaaS tenant. You need to provide two headers for
Fluent Bit: content type and authorization token. As FireLens supports only one header, you can pass the token as part of the
URL. Your configuration for AWS FireLens should have the following:

```
Name: http



TLS: on



Format: json



Header: Content-Type application/json; charset=utf-8



Host: {your-environment-id}.live.dynatrace.com



Port: 443



URI: /api/v2/logs/ingest?api-token={your-API-token-here}



Allow_Duplicated_Headers": "false"



Json_Date_Format": "iso8601"



Json_Date_Key": "timestamp"
```

To avoid publishing the token in plaintext, follow the directions from [AWS Secrets Managerï»¿](https://dt-url.net/r5234z4).
Once your application starts publishing logs, you can view them in the Dynatrace UI.

Refer to [AWS sample repositoryï»¿](https://dt-url.net/3j0348v) for the task definition JSON with Dynatrace configuration.

For more configuration details, see [Amazon ECS Developer Guideï»¿](https://dt-url.net/cf4349a).

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)


---


## Source: syslog.md


---
title: Syslog ingestion with ActiveGate (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog
scraped: 2026-02-17T04:57:39.309248
---

# Syslog ingestion with ActiveGate (Logs Classic)

# Syslog ingestion with ActiveGate (Logs Classic)

* Tutorial
* 4-min read
* Updated on Oct 08, 2025
* Preview

Preview ActiveGate version 1.293+ Log Monitoring Classic

Preview

This is a preview release. Your current configuration is fully compatible with future versions, but you can expect higher resiliency to traffic spikes and better handling of connection disruptions when the feature becomes generally available.

For the newest Dynatrace version, see [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

Syslog, short for system logging protocol, is a logging mechanism that enables system administrators to oversee and control log files from various system components, such as network devices, Linux host syslog, syslog servers, or other syslog producers.

This guide shows you how to configure your Environment ActiveGate on Linux to collect syslog logs in your network and ingest them to Dynatrace.

## Prerequisites

* Environment ActiveGate version 1.293+ on Linux installed to [monitor remote technologies](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").
* Your network devices have the syslog enabled or you have other syslog producers configured in your network. Refer to RFC3164 and RFC5424 for details. Dynatrace supports a wide variety of syslog implementations, including RSysLog, Syslog-NG, NXLog, and others.

## Who is it for?

This guide is intended for network and Dynatrace admins who are tasked to enable the syslog log ingestion into Dynatrace.

## Enable syslog ingestion

Enabling syslog log ingestion requires you to:

* Deploy Environment ActiveAge in a place ensuring the connectivity between ActiveGate and monitored devices.
* Enable syslog ingestion on ActiveGate.
* Optional in some cases, you'll need to adapt the default syslog receiver configuration.

1. **Deploy Environment ActiveGate**.

   See instructions for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux "Learn how to install ActiveGate on Windows, customize installation, and more."). Use the [remote technologies monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") purpose.
2. **Enable syslog ingestion on your ActiveGate**.

   Edit the `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` file and add the following flag:

   ```
   syslogenabled=true
   ```
3. Optional **Edit the syslog receiver configuration**.

   ActiveGate uses an embedded Dynatrace OpenTelemetry Collector instance and stores the receiver configuration in the `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml` file. The Collector is installed by default.

   Use this configuration only for syslog ingestion.

   If your syslog producers use the default ports per supported protocols, your syslog-enabled ActiveGate should receive syslog records right away.

   You only need to modify the configuration if your syslog producers cast events on custom ports.

   Show me the fileâ¦

   ```
   receivers:



   syslog/udp:



   udp:



   listen_address: '0.0.0.0:514'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   syslog/tcp:



   tcp:



   listen_address: '0.0.0.0:601'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   #  syslog/tcp_tls:



   #    tcp:



   #      listen_address: "0.0.0.0:6514"



   #      tls:



   #        cert_file: "/absolute/path/to/server.crt"



   #        key_file: "/absolute/path/to/server.key"



   #    protocol: rfc5424



   #    operators:



   #      - type: syslog_parser



   #        protocol: rfc5424



   #DO.NOT.MODIFY



   exporters:



   otlp_http/syslog: ${file:syslogendpoint.yaml}



   processors:



   batch:



   send_batch_size: 512



   send_batch_max_size: 1024



   transform:



   log_statements:



   - context: log



   statements:



   - set(body, attributes["message"])



   attributes:



   actions:



   - key: net.host.name



   action: delete



   - key: net.peer.name



   action: delete



   - key: net.peer.port



   action: delete



   - key: net.transport



   action: delete



   - key: net.host.ip



   action: delete



   - key: dt.ingest.port



   from_attribute: net.host.port



   action: upsert



   - key: dt.ingest.source.ip



   from_attribute: net.peer.ip



   action: upsert



   - key: net.peer.ip



   action: delete



   - key: net.host.port



   action: delete



   - key: syslog.hostname



   from_attribute: hostname



   action: upsert



   - key: hostname



   action: delete



   - key: syslog.facility



   from_attribute: facility



   action: upsert



   - key: facility



   action: delete



   - key: syslog.priority



   from_attribute: priority



   action: upsert



   - key: priority



   action: delete



   - key: syslog.proc_id



   from_attribute: proc_id



   action: upsert



   - key: proc_id



   action: delete



   - key: syslog.version



   from_attribute: version



   action: upsert



   - key: version



   action: delete



   - key: syslog.appname



   from_attribute: appname



   action: upsert



   - key: appname



   action: delete



   - key: message



   action: delete



   service:



   telemetry:



   metrics:



   level: none



   pipelines:



   logs/udp:



   receivers: [syslog/udp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   logs/tcp:



   receivers: [syslog/tcp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   #    logs/tcp_tls:



   #      receivers: [syslog/tcp_tls]



   #      processors: [transform, attributes, batch]



   #      exporters: [otlp_http/syslog]
   ```

   You can also modify the default configuration if you want to group a set of various devices by configuring them to use a specific port. For example, you can enrich your syslog events cast on specific TCP ports using the configuration as in the example below

   ```
   receivers:



   syslog/f5:



   tcp:



   listen_address: "0.0.0.0:54526"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.dt.ip_addresses



   value: "1xx.xx.xx.xx1"



   - type: add



   field: attributes.instance.name



   value: "ip-1xx-xx-x-xx9.ec2.internal"



   - type: add



   field: attributes.device.type



   value: "f5bigip"



   syslog/host:



   tcp:



   listen_address: "0.0.0.0:54527"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.device.type



   value: "ubuntu-syslog"
   ```

   **Note**: Do NOT modify the exporter configuration. The default configuration points to the embedded Collector.

   For more information on syslog receiver configuration, see [Ingest syslog data with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.").
4. **Verify the syslog ingestion is enabled**.

   After you enable syslog ingestion, check the following log files to verify it:

   Open the newest `ruxit_extensionmodule_*.log` log file in the `extensions` log directory:

   * Linux: `/var/lib/dynatrace/remotepluginmodule/log/extensions`

   It should contain the following line:

   ```
   Otel syslog enabled: true
   ```
5. **Enable syslog on the devices you want to monitor**.

   The way you enable syslog depends on the device and its platform, refer to specific documentation for details.

   **Example**
   Configure Rsyslog on Linux Ubuntu to forward syslog logs to a remote server.

   Add the following line to the syslog daemon configuration file (`/etc/rsyslog.conf`)

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   The `*.*` instructs the daemon to forward all messages to the specified ActiveGate listening on the provided port and IP address. `<ActiveGate host IP>` needs to point to the IP address of a syslog-enabled ActiveGate.

   For more examples, see [Syslog via OpenTelemetry Collectorï»¿](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Verify ActiveGate receives the syslog events**.

   After your syslog producers start to cast log records, open the latest `dynatracesourceotelcollector.*.log` file in `/var/lib/dynatrace/remotepluginmodule/agent/datasources/otelSyslog`.

   If ActiveGate receives the log records you should see entries as in the example below:

   ```
   [otelSyslog][otelSyslog][37448][err]LogRecord #3



   [otelSyslog][oteiSyslog][37448][err]ObservedTimestamp: 2024-05-06 @9:52:10.6748723 +8000 UTC



   [otelSyslog][otelSyslog][37448][err]Timestamp: 2624-05-@6 11:52:16 +90e0 UTC



   [otelSyslog][otelsyslog][37448][err]SeverityText: info



   [otelSyslog][otelSyslog][37443][err]SeverityNumber: Info(9)



   [otelSyslog][otelSyslog][37448][err]Body: Str(<30>May 6 11:52:10 SOME-HOST systemd[1]: Finished    Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Attributes:



   [otelSyslog][otelSyslog][37448][err]    -> priority: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> facility: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> appname: Str(systemd)



   [otelSyslog][otelSyslog][37448][err]    -> proc_id: Str(1)



   [otelSyslog][otelSyslog][37443][err]    -> log: Map({âsource": âsyslog"})



   [otelSyslog][otelSyslog][37443][err]    -> hostname: Str(SOME-HOST)



   [otelSyslog][otelSyslog][37443][err]    -> message: Str(Finished Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Trace ID:



   [otelSyslog][otelSyslog][37448][err]Span ID:



   [otelSyslog][otelSyslog][37443][err]Flags: 0
   ```

For more information on troubleshooting the syslog receiver, see [Collector troubleshootingï»¿](https://opentelemetry.io/docs/collector/troubleshooting/).

## Next steps

After you enable the integration, the syslog-ingested events are enriched with the host-specific attributes and become available for log monitoring and processing.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)


---


## Source: acquire-log-data.md


---
title: Log ingest & process (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data
scraped: 2026-02-16T21:24:12.982633
---

# Log ingest & process (Logs Classic)

# Log ingest & process (Logs Classic)

* Overview
* 2-min read
* Updated on Aug 11, 2023

Log Monitoring Classic

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system and have Dynatrace transform the stream into meaningful log messages.

Dynatrace supports all major third-party platforms and architectures.

## Log autodetection and custom log sources

You can rely on autodiscovered or manually added log sources for OneAgent. See [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

* [Automatically discover log data](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")
* [Manually add log files](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Learn how to manually add log files for analysis.")

![LMC - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lmc-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-c4876fc96b.png)

## Cloud providers

Log Monitoring includes native support for [Red Hat OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes "Extend visibility into Kubernetes/OpenShift events.") and [Kubernetes logs and events](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.") for Kubernetes platforms, workloads, and applications running inside Kubernetes.

Log Monitoring has native support for [multicloud environments](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Learn how to configure AWS, Azure and Google Cloud log forwarding to ingest logs."), including:

* [AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")
* [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

## Syslog

Syslog is a standard protocol for message logging and system logs management. Routers, printers, hosts, switches and other devices across platforms use syslog to log users' activity, system and software lifecycle events, status, or diagnostics.

Syslog logs are ingested via syslog receiver available on the Environment ActiveGate.

For more information, see [Syslog ingestion with ActiveGate (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

## Open source

Dynatrace Log Monitoring supports open-source log data frameworks, including Fluentd and Logstash.

## Log ingestion API

With the Log ingestion API, you can stream log records to Dynatrace and have Dynatrace transform the stream into meaningful log messages. You can also use Log ingestion API to stream log records to Dynatrace using API.

* [Log ingestion API](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

![LMC - Generic log ingestion API](https://dt-cdn.net/images/lmc-generic-log-ingestion-api-2500-e9c0d3ff5f.png)

## Log processing

Dynatrace Log Monitoring incorporates reshaping the incoming log data into the form you may need for better understanding, analysis, or further processing of your log data by Dynatrace. Using Dynatrace Pattern Language (DPL), you can define patterns using matchers and create a set of rules that Log Monitoring applies to ingested log data.

* [Log processing](/docs/analyze-explore-automate/log-monitoring/log-processing "Create log processing rules that reshape your incoming log data for better analysis or further processing.")
* [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

![LMC - Log processing pipeline](https://dt-cdn.net/images/lmc-log-processing-pipeline-2500-60d2c2d7b6.png)


---


## Source: log-custom-attributes.md


---
title: Log custom attributes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes
scraped: 2026-02-17T21:25:45.747786
---

# Log custom attributes (Logs Classic)

# Log custom attributes (Logs Classic)

* Tutorial
* 3-min read
* Updated on Jul 03, 2023

Log Monitoring Classic

Dynatrace [automatically detects attributes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation#autoattributes "Log ingestion API automatically transforms log data into output values for the loglevel attribute.") of ingested log data. **Available attributes** quickly filter the result table data for a specific log data attribute.

You can also define your own custom log data attributes that suits your particular log data format. Similarly to the automatically detected log attributes, your custom log attributes are extracted from the log data during ingestion and become available within Dynatrace.

You can use them as filters in the log viewer (table options and log record detail attributes), as dimensions while creating log metrics, and as properties while creating log events.

These custom attributes must match log attributes in ingested log data or they will be ignored.

Dynatrace version 1.226+

Dynatrace automatically recognizes log attributes that are visible in log details and table options.

## Create a custom log attribute

1. Go to **Settings** > **Log Monitoring** > **Custom attributes**.
2. Select **Add custom attribute**.
3. Select **Log Monitoring** > **Custom attributes** and then select **Add custom attribute**.
4. Toggle on the **Show attribute values in side bar** option. This ensures that the system indexes the attribute values, and searches the logs by them.
5. Enter the **Key**.  
   Rules for keys:

   * A key can contain only alphanumeric characters, underscores ('\_'), hyphens ('-'), dots ('.') and colons (':').
   * It can't begin with a hyphen.
   * All characters must be from the Latin alphabet, with no diacritics; characters such as 'Ã¶' are not allowed.

You can check if the custom attributes you plan to add are part of the [key-values attributes](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api#semantics "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") list for automatic detection. If they are present there, there is no need to add them to the custom list.

Dynatrace Log Monitoring gives you the ability to define custom index log data attributes for log data that is ingested.

## Example

In this example, you will make an API log ingest call with JSON that contains the following log attributes:

```
{



"timestamp": "2021-07-29T10:54:40.962165022Z",



"level": "error",



"source": "Skynet",



"application.id": "PaymentService-Prod",



"message": "PaymentService-Prod failure.",



"data": {}



}
```

Then you will create a custom log attribute and use it for creating a log metric and a log event.

1. Make an API call.
2. Create a custom attribute.

   ![Creating a custom log attribute.](https://dt-cdn.net/images/lm-custom-att-set-custom-att-1129-96179dda7e.png)
3. View the attribute in log viewer. (See [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") for details.)

   * Check **Available attributes**

     Custom attribute shown as available attribute filter in a log viewer

     ![Available attributes-based filter in a log viewer.](https://dt-cdn.net/images/lm-custom-att-lv-facets-r-1493-e08c666d5b.png)
   * Check table options

     Custom attribute shown in table options in the log viewer

     ![Custom attribute shown in table options in the log viewer.](https://dt-cdn.net/images/lm-custom-att-lv-table-options-r-352-1192136876.png)
   * Check log entry/record details

     Custom attribute shown in log record in a log viewer under additional event attributes

     ![Custom attribute shown in log record in a log viewer under additional event attributes.](https://dt-cdn.net/images/lm-custom-att-lv-details-r-1172-19c628f888.png)


---


## Source: log-events.md


---
title: Log events (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events
scraped: 2026-02-18T05:51:57.630104
---

# Log events (Logs Classic)

# Log events (Logs Classic)

* Tutorial
* 5-min read
* Updated on Oct 08, 2025

Log Monitoring Classic

Dynatrace Log Monitoring gives you the ability to create log events based on log data and use them in problem detection.

Log event pricing is based on the Davis data units (DDUs) model. Check [DDUs for custom Davis events](/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.") to find out how you can estimate and track DDU consumption for log events.

When Dynatrace ingests log data, it applies the query specified in the log event definition. Every matched occurrence triggers a log event that can be configured to individually create a problem for each triggered log event or can be merged into one problem.

## Create a log event

1. Go to **Settings** > **Log Monitoring** > **Events extraction** and select **Add log event**.
2. Enter the **Summary**.  
   The summary acts as the display name of the log event configuration. The summary must be unique for all configurations.
3. Enter the **Matcher**.  
   Enter the Log Monitoring query to filter the log data for your log event. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   I switched to Grail

   If you switched to [Dynatrace Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you may begin using the [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") functions in your Log Monitoring queries. For details, see [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
4. Configure the **Event template**.

   * Provide the **Title** of the event to trigger. If this log event triggers a problem, this title will also be the title of the problem.
   * Provide the **Description** of the event. Note that you can have one or more placeholders in the description (see [Placeholders](#placeholders) below for details).
   * Select the **Event Type**. Event types indicate the severity of the event. See [Settings API - Log events schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "View builtin:logmonitoring.log-events settings schema table of your monitoring environment via the Dynatrace API.").
5. Choose whether to **Allow merge**.  
   If two or more events are triggered, Dynatrace could merge these events into a single problem. This option lets you choose to disable this behavior, which can result in more reported problems.

   The `dt.event.allow_davis_merge` property does **not** split problems for the same log event configuration. It only prevents merging with problems from other log event configurations or other problem domains (such as custom alerts).  
   If you want to split problems for the same log event configuration, the `event.unique_identifier` property must be **present in the actual log data**. You can then use a placeholder in your log event configuration to reference this property.  
   For example, to create a separate problem for each log line message, use `event.unique_identifier={content}`.
6. Add **Properties**.
   A property is a key/value pair that is set on every triggered event. You can have one or more placeholders as a value that will be extracted from the log data. For example, a property with **Key** set to `PGI` and a **Value** of placeholder `{dt.entity.process_group_instance}` will extract the process group instance value from log data once the event is triggered. If the placeholder substitution fails, both the key and the value will not be available.  
   To see how to get the full list of properties, go to [Events API v2 - GET all event properties](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API."). The `description` field in the API response body explains how each property works. For [example](/docs/dynatrace-api/environment-api/events-v2/get-event-properties#exampledesc "List all event properties via the Dynatrace API."): In the `dt.event.allow_davis_merge`, the description says :`"Allow Davis AI to merge this event into existing problems (true) or force creating a new problem (false)"`.

### Set a timeout for a log event

Log events have a default timeout of 15 minutes. The timeout defines how frequently the event source must refresh the log event to keep it active. The maximum time allowed for a log event is six hours.

* A log event is kept active if the event source sends a refresh before the event times out (default: `15` minutes).
* An event automatically closes if no refresh is sent within the timeout period.
* You can customize the timeout.

To set a custom timeout

1. When you create or edit a log event, select **Add property**.
2. Set **Key** to `dt.event.timeout`.
3. Set **Value** to the number of minutes (for example, `12`).

To verify that a custom timeout was added for an event triggered on the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host name.
2. Scroll down to **Events** and expand **Details** for the event.

### Placeholders

Placeholders are log entry attributes that can be used to extract the actual value from the log data.

* You can use any attribute listed in the log viewer for a given log entry as a placeholder to extract that attribute value.
* You can use additional log entry attributes in the log viewer as placeholders for the values they represent in the log data. Enclose placeholder values in brackets (for example, `{dt.process.name}`).

Log viewer showing additional log entry attributes

![Additional event attributes in log viewer.](https://dt-cdn.net/images/screenshot-log-viewer-attributes-903-2a2d4d157f.png)

## Example

In this example, we create a log event based on ingested log data. This log event will be triggered when the ingested log entry matches the input from the **Matcher** field. The matcher will search for status `error` on the `555f5555-555a-5dd5-55f555a5b55d` host. We add log event properties (attributes) that will extract values from the log data and include it in the problem summary.

1. Go to **Settings** > **Log Monitoring** > **Events extraction** and select **Add log event**.
2. Set the following:

   * **Summary:** `syslog-agent log event`
   * **Matcher:** `status="error" AND host.name="555f5555-555a-5dd5-55f555a5b55d"`
   * **Event template** - **Title:** `[Log] log events demo`
   * **Event template** - **Description:** `{content}`
   * **Event template** - **Event type:** `Custom alert`
3. Turn off **Allow merge**.
4. For **Properties**, add the following two properties:

   * Key `K8 Id` with value `{dt.kubernetes.config.id}`
   * Key `Process Name` with value `The process name is -> {dt.process.name}`
5. Save your changes and wait for log data to be ingested.

Log events example page

![Settings screen for configuring log events.](https://dt-cdn.net/images/screenshot-log-events-settings-641-583e83f210.png)

Logs can have attributes with long values, up to 32kB. Such attribute can be added as part of the **Event template** section. In such case, the events are created, but those values are trimmed to 4096.

If a match is found, this log event will create a problem with each triggered log event.

![Problem created by defined log events.](https://dt-cdn.net/images/screenshot-log-events-problem-845-dc714350b6.png)

The problem created as a result of a triggered log event will contain the information mapped from your log event configuration. The problem title is the **Event title** and the impact section reflects your **Event type** settings and additional information you configured in the description and properties of the log event.

Note that, in this example, while we have configured two properties (`K8 Id` and `Process Name`), only one appears on the problem page. This is because only the `{dt.process.name}` placeholder had a value in the ingested log data. The `{dt.kubernetes.config.id}` value was not found in that particular log entry and the defined property was ignored.


---


## Source: log-metrics.md


---
title: Log metrics (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics
scraped: 2026-02-18T05:54:47.982647
---

# Log metrics (Logs Classic)

# Log metrics (Logs Classic)

* Tutorial
* 7-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace Log Monitoring gives you the ability not only to view and analyze logs, but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in an analysis, and even create custom alerts.

Log metric pricing is based on the Davis data units (DDUs) model. Check [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") to find out how you can estimate and track DDU consumption for log metrics.

Depending on the options you select during log metric creation, the new metric value can represent:

* **Occurrence of log records** (available in Dynatrace version 1.206+)  
  The metric value will represent a count of occurrences of log records that match the query.
* **Attribute value** (available in Dynatrace version 1.229+)  
  The metric value can represent one of the aggregations that you can specify in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

When Dynatrace ingests log data, it applies the defined query to the log data and, based on your log metric **Measure** selection, the metric value will therefore represent either a count of the log records that match the query or one of the following values for the specified attribute: `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Percentile 10th`, `Percentile 75th`, or `Percentile 90th`. The specified attribute must be of numeric type. Dynatrace will attempt to convert string type attributes to numbers as long as they match the following pattern:  
`123`  
`123.`  
`123.456`  
`.456`  
`-.456`  
`+.456`  
`+123.456`  
`-123.456`  
`123.4e+5`  
`-123.4E-5`  
`1234e+5`  
`1234e5`

Attributes holding more than one value are not converted to attribute-based metrics.

## Creating log metric

All metrics based on a Log Monitoring matcher have a metric key with the `log.` prefix.

Log metric availability in Dynatrace

A created log metric is available only when new log data is ingested, and it matches the input from the **Matcher** field defined during log metric creation. Ensure that new log data has been ingested before utilizing the log metric in other areas of Dynatrace.

The range of a timestamp for accepting data that is used in metric creation is between **1 hour** in the past and **10 minutes** in the future. If no timestamp is provided, the current timestamp of the server is used.

There are two ways to create a metric based on log data:

### Create metric using settings

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Metric key**, append the metric name to the `log.` metric key.
3. In **Matcher**, enter the Log Monitoring query to filter the log data for your metric. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   I switched to Grail

   If you switched to [Dynatrace Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you may begin using the [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") functions in your Log Monitoring queries. For details, see [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
4. Select a **Measure**:

   * **Occurrence of log records**âa count of occurrences of log records that match the query.
   * **Attribute value**âthe collection of measures for the attribute value of log records that match the query. If you select this option, you need to also set **Attribute** to the attribute whose values will be gauged.
5. Optional Select **Add dimension** one or more times to add dimensions for your query result.  
   Adding dimensions allows you to split the log metric occurrences by a specific log data attribute. If the attribute contains more than one value, the first attribute value will act as the metric dimension. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#log-dimensions "Learn how to use Dynatrace log viewer to analyze log data.").
6. Select **Save changes** to create the log metric.

### Create metric using log viewer

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. Create a log viewer query or use log viewer **Available attributes** to extract the log data that interests you. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

Advanced query

In the advanced mode, you can specify more complex criteria for log events by using combinations of keywords, phrases, logical operators, and parentheses. If you use an advanced query and manually modify the query, select **Run query** to update the results table.

3. Select **Create metric**. Your log viewer query is now displayed on the **Log metrics** page.
4. Optionally, add dimensions for your query result.  
   Adding dimensions allows you to split the log metric occurrences according to specific log data attribute.
   For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#log-dimensions "Learn how to use Dynatrace log viewer to analyze log data.").
5. Append the metric name to the metric key `log.` and save changes to create the log metric.

### Unique dimensions limits

If you create metrics with high cardinality (a lot of unique dimensions), you can reach your environment's [cardinality limit](/docs/analyze-explore-automate/metrics/limits "Reference of metrics powered by Grail"). To mitigate these limitations, you can:

* Narrow the query to decrease the number of logs in a metric.
* Lower the cardinality of your dimensions.
* Disable a metric that exceeds the limit.  
  It is recommended to add more filters to reduce the number of unique dimensions first.

## Create metrics from dropped logs

Logs often contain valuable metric data, but you may not want to store the original log data. To get the metric data from logs and discard the original log data, you can create a metric from dropped logs. For example, consider the following log content:

```
2023-06-15T13:02:56Z localhost haproxy[12528]: 10.10.10.10:48064 http-in~ local/local0 3605/0/0/61/3666 HTTP_STATUS 200 138 - - ---- 7416/7413/400/401/0 0/0 {574|||domain.com} {|} "POST /communication HTTP/1.1"
```

You may be interested only in the active session total time from HAPproxy and you would like to discard the rest of the log data.

To do that

1. Ingest the log data via OneAgent and API.

   * [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
   * [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
2. Extract the metric from the ingested log data.

   * [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.")
3. Create the log metric.

   * [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics#log-metrics-create-rule "Create metrics based on log data and use them throughout Dynatrace like any other metric.")

## Editing log metric

To list, enable, disable, delete, or modify metrics created from log data, go to **Settings** > **Log Monitoring** > **Metrics extraction**.

Editing a metric key will generate a new metric. As a result, historical data will be accessible only with the old metric key.

## Example

In this example, we create and chart a log metric, save it to a dashboard, and create an alert.

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** to display the log viewer.
2. Create a query that filters the data that you are interested in. For this example, to filter all log entries for `error`, enter this query: `status="error"`
3. Select **Create metric**.  
   The **Log metrics** page is displayed with **Matcher** set to your query.
4. Type in the metric key (a unique name for the metric). By default, each metric key begins with `log.` prefix. All log metrics based on logs must have a key starting with this prefix.  
   For this example, set key to: `log.error_PGI`
5. Select **Add dimension** and then select the `dt.entityprocess_group_instance` dimension from the list.

   If you saved the metric without adding a dimension, Dynatrace would count errors globally. But in this example, we want to see how the error status is distributed across process group instances. Adding the `dt.entityprocess_group_instance` dimension will make Dynatrace count the number of error statuses for each process group instance. This allows you to view precisely where the error status occurred and to create an alert for a particular dimension.
6. **Save changes**.

Now that you have defined the metric, you can chart it, pin it to a dashboard, and even create an alert based on it.

* **Chart:** Go to **Data Explorer**, set **Select metricâ¦** to `log.error_PGI`, and select **Run query**.
* **Dashboard:** After you create a chart, select **Pin to dashboard** to add the chart to one of your classic dashboards. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
* **Alert:** Go to **Settings** > **Anomaly detection** > **Metric events**, select **Add metric event**, and create a custom event based on `log.error_PGI`.


---


## Source: log-viewer.md


---
title: Log viewer (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer
scraped: 2026-02-16T21:24:25.619729
---

# Log viewer (Logs Classic)

# Log viewer (Logs Classic)

* Explanation
* 9-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

The log viewer enables you to browse logs within a certain timeframe using detected aspects of the log content. You can use **Available attributes** to narrow down your log view and focus on a specific aspect of the log content.

To access the log viewer, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**. The log viewer has four sections:

## Search

In **Filter by**, you can set filters to narrow down the log events that are displayed in the results table. Select **Advanced query** to edit the query manually.

* With **Filter by** displayed (the default), the filter is in autocomplete mode, where you select from a set of detected log data fields to filter the results (limit of 10 different attributes). For filters with the same attributes, only one statement needs to be true. For filters with different attributes, all statements need to be true. While in the auto-complete mode, selected filters and **Available attributes** are synchronized automatically.

  When using a search query in the simple mode:

  + If the searched attribute names are the same, the **OR** operator is applied. The search results include items that match any of the specified attribute names. It provides a broader search, allowing for variations in attribute names.
  + If the searched attribute names differ, the **AND** operator is applied. The search results include only items that simultaneously match **all** of the specified attribute names. It narrows down the search to items that match multiple criteria.
* With **Advanced query** selected, you can specify more complex criteria for log events by using combinations of keywords, phrases, logical operators, and parentheses (limit of 10 different attributes). The Dynatrace search query language provides you with complete flexibility over searches through log content. You can use the query entry to quickly text search the content of the log data. Any string entered in the query text box without specifying the log data attribute will be treated as a simple text search on the log data content.

When filtering over log content, you can only use full tokens. The log content is split into tokens according to rules from the [Unicode Text Segmentationï»¿](https://unicode.org/reports/tr29/). Alternatively, you can use the wildcard \* at the end of the token.

You can turn **Advanced query** on and off to switch between the auto-complete and advanced modes. Dynatrace will transform the auto-complete filters to a query and vice versa provided that the query in the advanced mode can be transformed. Some complex queries with logical operators cannot be converted to auto-complete filters, in which case switching to auto-complete mode becomes unavailable.

In the advanced mode, you can run an empty query to return unfiltered log data.

Dynatrace search query language

Category

Description

Example

Text search

Text searches help you find individual word occurrences. You can search text without any syntax (as long as no special characters or keywords are present, such as `OR` `"` `=` `\` ) In this text search we identify words and ignore any non alphanumeric (whitespaces, interpunction) characters between them.

Spaces are interpreted as AND operators:  
`search words` is equivalent to `content="search" AND content="words"`.

Also, this mode allows you to use double quotes:  
`"search phrase" more` is equivalent to `content="search phrase" AND content="more"`.

Searches are case-sensitive for attribute names, and case-insensitive for attribute values.
`content="SEARCH"` is equivalent to `content="search"`, but `MyAttribute="MyValue"` in NOT equivalent to `myattribute="MyValue"`.

The query has a limit of 20 relations: logical operators (AND, OR) or comparison operators (`=`, `!=`).

```
error



search words



"search phrase" more



content="SEARCH"
```

Attributes

Search for records that have a specified attribute with a specified value.  
Search for records that do not have a specified attribute with a specified value.  
Search for records that do not contain a specified phrase in the content field.  
You can write numbers without quotes, including positive and negative decimals (for example, -123.34)

```
host.name="HOST1"



host.name!="HOST1"



content!="search text"



http.code=123
```

Phrases

A phrase is a group of words surrounded by double quotes. Phrases are treated just like single-word terms in queries. This allows you to search log data for a specified phrase in the content field. It returns only those records in which the entire phrase matches. In this example, the word `search` must be immediately followed by the word `text`.

Keep in mind that using a phrase search for content takes into account only alphanumeric characters in the same manner as the text search described above.

```
content="search text"
```

Boolean operators

Allowed operators are `AND`, `OR` and can be written in either uppercase or lowercase. Log data matches `AND` when it contains both surrounding strings. Log data matches `OR` when it contains at least one of the surrounding strings. The logical operator `AND` is automatically inserted between single-word terms that are not surrounded by parentheses.  
**Precedence**: `AND`, `OR`

```
status="INFO" AND host.name="HOST1"
```

```
status="INFO" OR host.name="HOST1"
```

Grouping

Parentheses `( )` can be used to group clauses into sub-queries.

```
status="INFO" AND



(host.name="HOST1" OR host.name="HOST2")
```

Wildcards

Wildcards can be used to represent a variable or unknown alphanumeric characters in search terms. An asterisk `*` can be used to represent any string composed of alphanumeric characters. The `*` wildcard is only acceptable at the end of the search term. The search term cannot start with the `*` wildcard and the `*` wildcard cannot be used within the search term itself.

```
host.name="host*"
```

Special characters

Escaping special characters in attribute names or attribute values:

For attribute names:  
An attribute can contain any chars but `"=!\` or white space. If an attribute contains any of the special characters or keywords (like `AND` or `OR`), you need to wrap the whole name in backticks (`). Additionally, if an attribute name contains a backtick, you need to escape it with a backslash (\).

For attribute values:  
Special chars: `*` `"` `\` must be escaped with `\`.

For free text search mode:  
Wrap keywords with double quotes.

Values that contain special characters must be wrapped with double quotes and special characters must be escaped with `\`

```
`attri=bute`="\"abc"
```

Entity Selector[1](#fn-1-1-def)

Search for records using entity selector.

For more information, see [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

```
attribute inEntitySelector "$(entitySelector)"
```

```
dt.source_entity inEntitySelector "type(\"HOST\")"
```

1

Not applicable for log events, log metrics, and processing.

## Chart

The log chart is a histogram of log events over time that gives you a quick overview of logs and their severity within the selected timeframe.

## Results table

The results table under the chart displays the log events that match the provided query and filter within the selected timeframe. Each row in the table represents a log record and can be expanded for detailed log data. The first 100 matching records are displayed, but you can view more results by selecting **Show 100 more** at the bottom of the table.

By default, ingested log records are sorted according to timestamp and then according to the order that is maintained in the log source, where a log source is a remote process writing to a REST API endpoint or a remote process on which logs are detected.

By default, the log viewer displays a maximum of 1,000 log events. If you don't see expected results, run a more exact query or narrow down the timeframe to see better focused log data.

To show or hide specific columns in the result table

1. Select **Format table**.  
   This lists Dynatrace generated and reserved log attributes that you can add to the results table for visibility and use as dimensions when creating a log metric. For example, you can use the `dt.entity.process_group` attribute to display the process group instance for which the log event occurred.
2. Select or clear checkboxes to display or hide the corresponding columns in the table.

To export table data

1. Select **Actions**.
2. Select **Download table (JSON)** or **Download table (CSV)**, depending on the format you need.
   While your search query may return more than 1,000 log records, the result table will display only the first 1,000 log records. As a result, the exported table data will contain only the 1,000 log records visible in the table. The exported log records will include complete log data for each record, even if it is not displayed in the table column.

## Available attributes

**Available attributes** (displayed to the left of the table) provide you with an overview and the ability to filter the log data. **Available attributes** are automatically detected attributes of the data presented in the table. You can use them to quickly filter the result table data for a specific log data attribute. Each available attribute displays up to ten most popular values for that attribute. To filter all values for a particular attribute, create and run a query in the log viewer search.

## Log details

Unique log data attributes (high-cardinality attributes) such as `span_id` and `trace_id` generate unnecessarily excessive lists of available attributes that may impact log viewer performance. Because of this, they aren't listed in **Available attributes**. You can still use them in an advanced search query.


---


## Source: management-zones-and-log-monitoring.md


---
title: Management zones and ingested log data (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring
scraped: 2026-02-18T05:55:48.391665
---

# Management zones and ingested log data (Logs Classic)

# Management zones and ingested log data (Logs Classic)

* Explanation
* 2-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Management zones are an information-partitioning mechanism that allow you to focus on specific parts of your topology. You can customize a management zone to include a specific set of monitored entities [via management-zone rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#rule-types "Define rules to limit the entities accessible within a management zone."). Use one of these two methods to analyze logs generated by a management-zone entity.

* Ingest logs via OneAgent, which automatically discovers log files in the topological context.
* Use [log ingestion](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") via API, which requires certain attributes to detect the topological context.

If you use the Log ingestion API via the [Log Monitoring API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2."), you can send an object representing a single event or an array of objects representing multiple events. The object must contain at least one of the following attribute keys, which define the entity types for which log data is ingested.

* `dt.entity.process_group_instance`âProcess group instances
* `dt.entity.custom_device`âCustom devices
* `dt.entity.host`âHosts

Log Monitoring Classic checks, in the order listed above, if the log event attribute value (and, therefore, the corresponding entity) belongs to a given management zone. At the first match, Log Monitoring Classic stops checking and assigns the log data to the management zone that the matched entity belongs to.

If your management zone already provides access to the host through which logs are ingested, you automatically provide access to those logs.

In the [log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data."), select the **Filter** button  in the menu bar to select a management zone. The log viewer displays log data for the entities matching the log-event attribute keys listed above.

Users must have the **View logs** permission on the environment level or management-zone level to be able to view the ingested and automatically assigned log data.

The log viewer displays log data for up to 10,000 monitored entities per management zone. If your management zone contains more than 10,000 monitored entities, and you would like to see log data for all of your monitored entities, you can break your management zone into smaller zones of fewer than 10,000 monitored entities each.

If you need to filter logs by other attributes, you can add a [rule for including log-based dimensional data](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#ui "Define rules to limit the entities accessible within a management zone.") in a management zone. Logs satisfying the conditions of such a rule are then displayed in the log viewer after selecting a management zone using the **Filter** button .

## Related topics

* [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.")
* [Log ingestion API (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")
* [Management-zone rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.")


---


## Source: lmc-ingest-warnings.md


---
title: Log ingestion warnings (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings
scraped: 2026-02-16T09:39:08.859177
---

# Log ingestion warnings (Logs Classic)

# Log ingestion warnings (Logs Classic)

* Overview
* 2-min read
* Published Oct 10, 2023

Log Monitoring Classic

If your ingested logs donât look as expected, you can check if a particular log record contains warnings regarding issues that occurred for that log in the log ingest and processing pipeline. Look for a `dt.ingest.warnings` attribute in log viewer. It lists warnings about issues that affected a particular log record.

Examples of possible warnings:

Warning

Description

content\_trimmed

The content was trimmed after being received bythe API because it exceeded the event content maximum byte size limit.

content\_trimmed\_pipe

The content was trimmed after processing rules were applied because it exceeded the event content maximum byte size limit.

attr\_count\_trimmed

The number of attributes was trimmed after being received by the API because it exceeded the maximum number of attributes in a single event.

attr\_count\_trimmed\_pipe

The number of attributes was trimmed after processing rules were applied because it exceeded the maximum number of attributes in a single event.

attr\_key\_trimmed

At least one attribute key was trimmed because it exceeded the key maximum byte size limit.

attr\_val\_count\_trimmed

At least one multi-value attribute had the number of values trimmed, after being received by the API, because it exceeded the maximum number of attributes in a single event.

attr\_val\_count\_trimmed\_pipe

After applying processing rules, at least one multi-value attribute had its value number trimmed because it exceeded the maximum number of attributes.

attr\_val\_size\_trimmed

At least one attribute value size was trimmed after being received by the API because it exceeded the value maximum byte size limit.

attr\_val\_size\_trimmed\_pipe

At least one attribute value size was trimmed after processing rules were applied because it exceeded the value maximum byte size limit.

timestamp\_corrected

The timestamp was too far in the future and was corrected to the current time.

common\_attr\_corrected

At least one of the following attributes was corrected: `status`, `loglevel`, or `event.type`.

processing\_batch\_timeout

Batch timeout occurred while executing log processing rules.

processing\_transformer\_timeout

Execution timeout occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_error

Execution error occurred in one of the processing transformers while executing log processing rules.

processing\_transformer\_throttled

Execution throttled in one of the processing transformers while executing log processing rules.

processing\_output\_record\_conversion\_error

Output conversion error occurred for some records while executing log processing rules.

processing\_prepare\_input\_error

âPrepare input errorâ occurred in one of the enabled log processing rules.


---


## Source: lmc-troubleshooting.md


---
title: Troubleshooting Log Monitoring (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting
scraped: 2026-02-17T04:58:23.228127
---

# Troubleshooting Log Monitoring (Logs Classic)

# Troubleshooting Log Monitoring (Logs Classic)

* Troubleshooting
* 2-min read
* Updated on Oct 08, 2025

Log Monitoring Classic

## General troubleshooting

If you've encountered an issue related to Log Monitoring, check one of the following pages in the Dynatrace Community.

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [What might prevent logs from appearing on the server?ï»¿](https://dt-url.net/lu23817)
* [I get an ingest warning about an attribute key case mismatchï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-an-ingest-warning-about-an-attribute-key-case-mismatch/ta-p/251188)
* [I get a warning in the Log Viewer about case-sensitive queriesï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-a-warning-in-the-Log-Viewer-about-case-sensitive-queries/ta-p/251189)
* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Technology-specific troubleshooting

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
* [Azure Log Forwarder Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)

## Specific questions

### How much does Log Monitoring cost?

Log Monitoring pricing is based on the Davis data units (DDUs) model. See [DDUs for Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details on how DDU consumption is calculated for Log Monitoring.

### Who can increase the ingestion limit per tenant?

Please contact a Dynatrace product expert via live chat within your environment.


---


## Source: log-enrichment.md


---
title: Connecting log data to traces (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment
scraped: 2026-02-18T05:32:18.855058
---

# Connecting log data to traces (Logs Classic)

# Connecting log data to traces (Logs Classic)

* 9-min read
* Updated on Nov 25, 2025

Log Monitoring Classic

Dynatrace can enrich your ingested log data with additional information that helps Dynatrace to recognize, correlate, and evaluate the data. Log enrichment results in a more refined analysis of your logs.

For the newest Dynatrace version, see [Connect log data to traces](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.").

Log enrichment enables you to:

* Seamlessly switch context and analyze individual spans, transactions, or entire workloads
* Empower development teams by making it easier and faster for them to detect and pinpoint problems

## Enrich logs automatically

You can enable log enrichment for a particular technology used to create log data and let Dynatrace automatically inject additional attributes into every log record received. This method is recommended for structured log data of known technologies.

Limiting log enrichment

Use **Process group override** to limit log enrichment to a specific process group or a process within a process group.

### Enable/disable log enrichment for a specific technology

To enable log enrichment for a specific technology:

Globally

Process group override in OneAgent

Kubernetes namespace

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Filter for **enrichment**.
3. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
4. Select **Save changes** to save your configuration.

1. Open the Process group you are looking for.
2. Select **More** (**â¦**) > **OneAgent features**.
3. Filter for **enrichment**.
4. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
5. Select **Save changes** to save your configuration.

1. Go to **Infrastructure Observability** > **Kubernetes**.
2. Select the **Namespaces** value for your Kubernetes cluster.
3. Select the Kubernetes namespace record that you're interested in.
4. On the top left of the page, go to **More** (**â¦**) > **Settings** > **OneAgent features**.
5. Select **Add override**.
6. Select the log enrichment technology from the **Feature** dropdown list, and make sure that the feature override toggle is turned on.
7. Select **Save and close**.

### What does automatic log enrichment do?

Log enrichment modifies your ingested log data and adds the following information to each detected log record:

* `dt.trace_id`
* `dt.span_id`
* `dt.entity.process_group_instance`

## Supported frameworks

To see the supported frameworks for trace/span log context enrichment, go to [Technology support](/docs/ingest-from/technology-support#web-servers "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Structured log data

For structured log data such as JSON, XML, and well-defined text log formats, Dynatrace adds an attribute field to the log record entry.

### Example of enriched log data in JSON format

Log data in JSON format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `dt.entity.process_group_instance` properties.

```
{



"severity": "error",



"time": 1638957438023,



"pid": 1,



"hostname": "paymentservice-788946fdcd-42lgq",



"name": "paymentservice-charge",



"dt.trace_id": "d04b42bc9f4b6ecdbf6bc9f4b6ecdbc",



"dt.span_id": "9adc716eb808d428",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-27204EFED3D8466E",



"message": "Unsupported card type for cardNumber=************0454"



}
```

### Example of enriched log data in XML format

Log data in XML format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `<dt.entity.process_group_instance>` nodes.

```
<?xml version="1.0" encoding="windows-1252" standalone="no"?>



<record>



<date>2021-08-24T14:41:36.565218700Z</date>



<millis>1629816096565</millis>



<nanos>218700</nanos>



<sequence>0</sequence>



<logger>com.apm.testapp.logging.jul.XMLLoggingSample</logger>



<level>INFO</level>



<class>com.apm.testapp.logging.jul.BaseLoggingSample</class>



<method>info</method>



<thread>1</thread>



<message>Update completed successfully.</message>



<dt.trace_id>513fcd4e9b08792fcd4e9b08792</dt.trace_id>



<dt.span_id>125840e3125840e3</dt.span_id>



<dt.entity.process_group_instance>PROCESS_GROUP_INSTANCE-27204EFED3D8466E</dt.entity.process_group_instance>



</record>
```

## Unstructured log data

Check if Dynatrace log enrichment has an impact on your existing log data pipeline before using automatic log enrichment on unstructured log data.

Unstructured log data is typically made of raw plain text that is sequentially ordered and is designed to be read by people. Dynatrace does not automatically enrich unstructured log data. Dynatrace is able to enrich unstructured log data, but appending additional information to log data may have an impact on third-party tools that consume that same log data.

### Example of enriched log data in raw text format

Log data in raw text is enriched with an additional `[!dt dt.trace_id=$trace_id, dt.span_id=$span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]` string (attributes and their value).

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e,dt.span_id=b93ede8b93ede8, dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-27204EFED3D8466E]
```

## Enrich logs manually

OneAgent version 1.239+

You can manually enrich your Dynatrace ingested log data by defining a log pattern to include the `dt.span_id`, `dt.trace_id`, `dt.trace_sampled`, and `dt.entity.process_group_instance` fields. You can enable manual log enrichment for a specific technology by following the [Log enrichment steps](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment#enableenr "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").

Be sure to follow these rules for the format of the enriched fields in an unstructured log:

* Fields must be encapsulated in square brackets (`[]`) with a `!dt` prefix.  
  For example, `[!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]`
* Fields must be formatted without double quotes.
* Any invalid characters for the field and field value must be escaped.
* Any control characters like `\n` must be excluded from the enrichment definition.

### Example of manually enriching NGINX log data

Suppose you want to manually enrich your NGINX log data with `dt.trace_id`, `dt.span_id` and `dt.trace_sampled`. The NGINX configuration file contains numerous standard NGINX variables, your log format definition must be in the `log_format` section. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled]';



access_log logs/access.log custom;
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=b9e5c9ec08be5fab5071d76f427be7da,dt.span_id=43c5bb9432593963,dt.trace_sampled=true]



127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=01e52950b145d97bf22345e68c5e6c58,dt.span_id=de819d856eecb236,dt.trace_sampled=true]
```

For OneAgent version 1.237 and earlier, the NGINX variables used are different. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$trace_id,dt.span_id=$span_id]'; access_log logs/access.log custom
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=e1c0afeb0b8a91d7748139aa764ee37e,dt.span_id=e5e6748fab93ede8]



127.0.0.1 - [21/Oct/2021:10:33:31 +0200] GET /index.html HTTP/1.1 200 1056 [!dt dt.trace_id=81fe7816ba6c38f7aa09aef3684cd941,dt.span_id=3bdacc466ae073cd]
```

If you use a logging framework and log formatter that allows custom log patterns, you can adapt the pattern in the log formatter and directly access the Dynatrace enrichment attributes.

### Example of manually enriching Log4j log data

In the **Log4j** PatternFormatter, you can specify a pattern like this to include Dynatrace enrichment information:

```
<PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} dt.trace_id=%X{dt.trace_id} dt.span_id=%X{dt.span_id} dt.entity.process_group_instance=%X{dt.entity.process_group_instance} - %msg%n"/>
```

### Example of manually enriching Logstash Logback encoder

Logback is a successor to the log4j project. Logstash Logback is an extension that provides logback encoders, layouts, and appenders to log in JSON and other formats supported by Jackson.

The following is an example of manual enrichment using the Logstash encoder. Note the additional `mdc` property in the configuration file, where you can include MDC variables.

```
<appender name="COMPOSITEJSONENCODER" class="ch.qos.logback.core.FileAppender">



<file>compositejsonencoder.log</file>



<encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">



<providers>



<timestamp>



<fieldName>timestamp</fieldName>



<timeZone>UTC</timeZone>



</timestamp>



<loggerName>



<fieldName>logger</fieldName>



</loggerName>



<logLevel>



<fieldName>level</fieldName>



</logLevel>



<threadName>



<fieldName>thread</fieldName>



</threadName>



<mdc>



<includeMdcKeyName>dt.span_id</includeMdcKeyName>



<includeMdcKeyName>dt.trace_id</includeMdcKeyName>



<includeMdcKeyName>dt.entity.host</includeMdcKeyName>



</mdc>



<stackTrace>



<fieldName>stackTrace</fieldName>



<!-- maxLength - limit the length of the stack trace -->



<throwableConverter class="net.logstash.logback.stacktrace.ShortenedThrowableConverter">



<maxDepthPerThrowable>200</maxDepthPerThrowable>



<maxLength>14000</maxLength>



<rootCauseFirst>true</rootCauseFirst>



</throwableConverter>



</stackTrace>



<message />



<throwableClassName>



<fieldName>exceptionClass</fieldName>



</throwableClassName>



</providers>



</encoder>



</appender>
```

### Example of manually enriching log data for winston (Node.js)

To enable log enrichment for winston, turn on the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Node.js - Trace/span context enrichment for unstructured logs**. You can adapt the winston transport to control the exact location where the enrichment should be added, as in the code example below.

```
const winston = require("winston");



const Transport = require("winston-transport");



class CustomTransport extends Transport {



log(info, next) {



let myLogLine = `MyLogLine: ${info.timestamp} level=${info.level}: ${info.message}`;



// this is important as above line only picks timestamp, level and message but nothing else from metadata



if (info["dt.trace_id"]) {



myLogLine = `[!dt dt.trace_id=${info["dt.trace_id"]},dt.span_id=${info["dt.span_id"]},dt.trace_sampled=${info["dt.trace_sampled"]}] ${myLogLine}`;



}



console.log(myLogLine);



next();



}



}



const logger = winston.createLogger({



level: "info",



format: winston.format.timestamp(),



transports: [



new CustomTransport(),



// this transport includes all metadata (including dynatrace added traceId,..)



new winston.transport.Console({



format: winston.format.simple()



})



]



})
```

## NGINX ingress with Kubernetes

You can enrich your logs using NGINX ingress with Kubernetes in two steps:

1. Execute the [ingress-nginx on Kubernetes](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "Instrument ingress-nginx on Kubernetes") instrumentation instructions.
2. Add the command below to the `configmap.yaml` file for NGINX ingress.

   Adding the `main-snippet` line enables OneAgent ingestion and is optional if you have followed the manual instrumentation instructions already.

```
main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'
```

Example of configmap.yaml file

```
apiVersion: v1



kind: Namespace



metadata:



name: prod-ingress-nginx



labels:



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



---



# Source: ingress-nginx/templates/controller-serviceaccount.yaml



apiVersion: v1



kind: ServiceAccount



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx



namespace: prod-ingress-nginx



automountServiceAccountToken: true



---



# Source: ingress-nginx/templates/controller-configmap.yaml



apiVersion: v1



kind: ConfigMap



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx-controller



namespace: prod-ingress-nginx



data:



allow-snippet-annotations: 'true'



main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'



...
```

## Retrieve span and trace IDs

To have Dynatrace match logs to corresponding traces, you can include the span and trace IDs in your log messages, using the `[!dt]` notation.

The following examples show how to obtain the span and trace IDs with OpenTelemetry or the OneAgent SDK:

Python with OpenTelemetry

JavaScript (Node.js) with OpenTelemetry

Java with OpenTelemetry

Go with the OneAgent SDK

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to the configured log sink associates the log message with the currently active span in the Dynatrace web UI.

```
import logging



from opentelemetry import trace



def dt_log(self, record):



if (not self.disabled) and self.filter(record):



ctx = trace.get_current_span().get_span_context()



if ctx.is_valid:



trace_id = "{0:032X}".format(ctx.trace_id)



span_id = "{0:016X}".format(ctx.span_id)



record.msg = f"[!dt dt.trace_id={trace_id},dt.span_id={span_id}] - {record.msg}"



self.callHandlers(record)



logging.Logger.handle = dt_log



def lambda_handler(event, context):



logger = logging.getLogger()



logger.warning("Hello world")



return {



"statusCode": 200,



"body": "Hello from lambda"



}
```

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to `stdout` associates the log message with the currently active span in the Dynatrace web UI.

```
const opentelemetry = require('@opentelemetry/api');



function dtLog(msg) {



const spanContext = opentelemetry.trace.getSpanContext(opentelemetry.context.active()) ?? opentelemetry.INVALID_SPAN_CONTEXT;



console.log(`[!dt dt.trace_id=${spanContext.traceId},dt.span_id=${spanContext.spanId}] - ${msg}`);



}



exports.handler = function(event, context) {



const msg = "Hello World"



dtLog(msg);



context.succeed({



statusCode: 200,



body: msg



});



};
```

In the example below, a `dtLog` method has been created to enrich a given log message with `TraceId` and `SpanId` information. Printing this enriched message via `System.out` associates the log message with the currently active span in the Dynatrace web UI.

```
package com.amazonaws.lambda.demo;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanContext;



public class HelloJava implements RequestHandler<Object, String> {



private static void dtLog(final String msg) {



SpanContext spanContext = Span.current().getSpanContext();



System.out.printf(



"[!dt dt.trace_id=%s,dt.span_id=%s] - %s%n",



spanContext.getTraceId(),



spanContext.getSpanId(),



msg



);



}



@Override



public String handleRequest(Object input, Context context) {



String msg = "Hello World";



dtLog(msg);



return msg;



}



}
```

In the example below, the HTTP handler uses `Printf()` to log the response to standard output and enriches that information with the trace and span IDs, obtained from `oneagentsdk.GetTraceContextInfo()`. Printing this enriched message associates the log message with the currently active span in the Dynatrace web UI.

```
package main



import (



"fmt"



"log"



"net/http"



"github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



)



func main() {



// Create OneAgent SDK API instance



var oneagentsdk = sdk.CreateInstance()



http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {



// Get TraceContextInfo within the incoming HTTP request



// to obtain Trace ID and Span ID of the active distributed trace context



traceContext := oneagentsdk.GetTraceContextInfo()



msg := "Hello World"



// Log to console



fmt.Printf("[!dt dt.trace_id=%s,dt.span_id=%s] - %s\n", traceContext.GetTraceId(), traceContext.GetSpanId(), msg)



// Write HTTP body



fmt.Fprintf(w, msg)



})



fmt.Println("Starting HTTP server at port 8080...")



log.Fatal(http.ListenAndServe(":8080", nil))



}
```

For details on configuration, see [AWS Lambda logs in context of traces](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Configure log message enrichment with OpenTelemetry on AWS Lambda.").

For instructions on how to source these attributes via OneAgent SDK:

* **Go:** see the [GO documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Go)
* **.NET:** see the [.NET documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet#trace-context)

## Retrieve process group instance ID

You can get the `dt.entity.process_group_instance` field using the OpenTelemetry Python command containing `merged`. The `process_group_instance` is retrieved as one of the attributes delivered in `merged`, as shown in the example below:

With OneAgent, you can simply point to a local endpoint without an authentication token to enable trace ingestion.

```
import json



from opentelemetry import trace as OpenTelemetry



from opentelemetry.exporter.otlp.proto.http.trace_exporter import (



OTLPSpanExporter,



)



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider, sampling



from opentelemetry.sdk.trace.export import (



BatchSpanProcessor,



)



merged = dict()



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json"]:



try:



data = ''



with open(name) as f:



data = json.load(f if name.startswith("/var") else open(f.read()))



merged.update(data)



except:



pass



merged.update({



"service.name": "python-quickstart", #TODO Replace with the name of your application



"service.version": "1.0.1", #TODO Replace with the version of your application



})



resource = Resource.create(merged)



tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



OpenTelemetry.set_tracer_provider(tracer_provider)



tracer_provider.add_span_processor(



BatchSpanProcessor(OTLPSpanExporter(



endpoint="http://localhost:14499/otlp/v1/traces"



)))
```

When using OneAgent, make sure to enable the public [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") in your Dynatrace Settings, otherwise no data will be sent.

Go to **Settings** > **Preferences** > **Extension Execution Controller**. The toggles **Enable Extension Execution Controller** and **Enable local PIPE/HTTP metric and Log Ingest API** should be active.

For details on configuration, see [Instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")

## Related topics

* [Leverage log enrichment for traces to resolve problems](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")


---


## Source: sensitive-data-masking.md


---
title: Sensitive data masking (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking
scraped: 2026-02-18T05:58:19.609944
---

# Sensitive data masking (Logs Classic)

# Sensitive data masking (Logs Classic)

* 11-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace version 1.253+ OneAgent version 1.243+

Your log data contains information that may be considered sensitive. Specific log messages may include user names, email addresses, URL parameters, and other information that you may not want to disclose. Log Monitoring features the ability to mask any information by modifying the configuration file on each OneAgent that handles information you consider to be sensitive.

For the newest Dynatrace version, see [Sensitive data masking in OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

You can select the data that needs to be protected by applying a set of masking rules. Within each rule, you can decide what you need to hide and what to replace your hidden content with. If you need to address only specific attributes, such as predefined containers, log sources or process groups, you can achieve it by adding matchers to your rules.

## Rule hierarchy

Masking rule execution occurs in a predefined hierarchy, from top to bottom. Each consecutive rule is applied to the result of a preceding rule.
The hierarchy is as follows:

1. Host configuration rules
2. Host group configuration rules
3. Environment configuration rules

### Host configuration rules

The host configuration rules can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Sensitive data masking**.
5. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Host group configuration rules

The host group configuration rules can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Sensitive data masking**.
7. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

### Environment configuration rules

The tenant scope is available in the settings menu.

1. Go to **Settings** > **Log Monitoring** > **Sensitive data masking**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## Create rule

You can configure sensitive data masking on the host, host group or environment level.

1. Select **Create new rule** to start configuring your rule.
2. **Name:** The name to display for your configuration.
3. **Search expression:** A regular expression to match the string that you want to mask. Use the regular expression format.
4. **Masking type:** You can replace your data with a string or Secure Hash Algorithm 1 (SHA-1).

   * If you select **replace with string**, set **Replacement** to the string that is meant to replace your sensitive data.
   * If you select **SHA-1**, your data will be replaced by the 40-character hash string.
5. Select **Add matcher** to create a specific match for this rule and narrow down the scope for that rule. You can include multiple matchers in one rule. For example, the masking rule can be applied to logs from a specific container, namespace, or log source.
6. Select the matching attribute.

   Attribute

   Description

   **Container name**

   Matching is based on the name of the container.

   **DT entity container group ID**

   Matching is based on the DT entity container group ID.

   **K8s container name**

   Matching is based on the name of the Kubernetes container.

   **K8s deployment name**

   Matching is based on the name of the Kubernetes deployment.

   **K8s namespace name**

   Matching is based on the name of the Kubernetes namespace.

   **Log source**

   Matching is based on a log path; wildcards are supported in form of an asterisk.

   **Process group**

   Matching is based on the process group ID.

   **Process technology**

   Matching is based on the technology name.
7. Select **Add value** and, from the **Values** list, select the detected log data items (log files or process groups that contain log data). Multiple values can be added to the selected operator. You can have one matcher that indicates log source and matches values **/var/log/syslog** and **Windows Application Log**.
8. Select **Save changes**.

Defined rules can be reordered, and they are executed in the order in which they appear on the **Sensitive data masking** page.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

## REST API

You can use the Settings API to manage your sensitive data masking configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create, edit, or remove configuration object

To check the current schema version for sensitive data masking configuration, list all available schemas and look for the `builtin:logmonitoring.sensitive-data-masking-settings` schema identifier. Sensitive data masking configuration objects are available for configuration on the following scopes:

* `tenant`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a sensitive data masking configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The sensitive data masking configuration schema identifier (`schemaId`) is `builtin:sensitive-data-masking-settings`. Here is an example JSON payload with the sensitive data masking configuration:

```
[



{



"schemaId":"builtin:logmonitoring.sensitive-data-masking-settings",



"scope":"tenant",



"value":{



"config-item-title":"Added from REST API",



"masking":{



"expression":"run (\\d+?)",



"type":"STRING",



"replacement":"testing"



},



"matchers":[



{



"attribute":"log.source",



"operator":"MATCHES",



"values":[



"/var/log/syslog"



]



}



]



}



}



]
```

## SHA-1 examples

You can mask such data as your credit card or phone number, with or without specifying the capturing group.

### Mask credit card number

In this example, you will configure a sensitive data masking rule that targets a credit card number in the following log record:

```
Username: John Doe, CreditCardNumber: 1234-1234-1234-1234
```

The rule is further narrowed to the `c:\inetpub\logs\LogFiles\ex_*.log` files in two process groups: `IIS (PROCESS_GROUP-3D9D854163F8F07A)` and `IIS (PROCESS_GROUP-4A7B47FDB53137AE)`.

Go to **Settings** > **Log Monitoring** > **Sensitive data masking**

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the credit card number, such as `CreditCardNumber: (\d{4}-\d{4}-\d{4}-\d{4})`.
3. Select `SHA-1` for Masking type.
4. Select **Add matcher**.
5. From the **Attribute** list select **Process group**.
6. In the **Value** field, type `IIS`, and select `IIS (PROCESS_GROUP-3D9D854163F8F07A)` from the suggestions list.
7. In the **Value** field, again type `IIS`, and select the second process group from the suggestions list: `PROCESS_GROUP-4A7B47FDB53137AE`.
8. Select **Add matcher** again.
9. Select the matching attribute **Log Source**.
10. Select **Add value** and type `c:\inetpub\logs\LogFiles\ex_*.log`.
11. **Save changes**.

Only content found within a capturing group is masked, and it is transformed to the following:

```
Username: John Doe, CreditCardNumber: 7e938e089861f3975b38cff3a93cc3aa659f7779
```

### Mask phone number

In this example, you will configure a sensitive data masking rule that targets all phone numbers in the following log record for all log files.

```
Username: John Doe, PhoneNumber: +48123010100
```

Go to **Settings** > **Log Monitoring** > **Sensitive data masking**.

1. Select **Create new rule** and provide the name for your configuration.
2. Provide a regular expression for the phone number. For example, `PhoneNumber: [0-9\-\+]{9,15}`.
3. Select `SHA-1` for Masking type.
4. Select **Add matcher**.
5. **Save changes**.

The capturing group is not specified, so the full expression is treated as one capturing group and is masked so that it is transformed into the following in all log files:

```
Username: John Doe, 011897d555c81e88f286cbb74c59f4ad99ec2f8d
```

## Advanced SHA-1 examples

In the examples below, you can see how various combinations of sensitive data can be masked. You can use the listed payload JSON files in the REST API, or enter the listed masking rules, matchers, Regex expressions, and attributes directly when creating your rules via Dynatrace web UI.

### Mask credit card numbers and emails

To mask all credit card numbers and emails in your content, you need to create two separate rules, each with a different matcher:

```
{



"masking": {



"expression": "(\\d{4}-\\d{4}-\\d{4}-\\d{4})",



"type": "STRING",



"replacement": "MaskedCreditCardNumber"



},



"matchers": [



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



],



"enabled": true



}
```

### Mask Apache logs

To mask logs that are written by Apache AND whose log filename is `error.log`, you can create one rule with two matchers:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that are written by Apache OR whose log filename is `error.log`, you need to create two rules with one matcher each:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error.log"



]



}



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that are written by Apache and whose log filename starts with `error` AND ends with `log`, you need to have one rule with three matchers, each matcher having one value.

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*"



]



},



{



"attribute": "log.source",



"values": [



"*log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

To mask logs that are written by Apache and whose log filename starts with `error` OR ends with `log`, you need to have one rule with two matchers, one with the process group value, and the second one with two content values, `/path/to/error*` and `*log`:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "log.source",



"values": [



"/path/to/error*", "*log"



]



},



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

### Mask Apache or MySQL logs

To mask logs that are written by Apache or MySQL, you need to have either two rules or one rule with one matcher that has two values.

The scenario with two rules:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



},



{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID"



]



}



],



"enabled": true



}
```

The scenario with one rule with a matcher that has two values:

```
{



"masking": {



"expression": "email: (.*),",



"type": "SHA1"



},



"matchers": [



{



"attribute": "dt.entity.process_group",



"values": [



"PROCESS_GROUP-APACHEID", "PROCESS_GROUP-MYSQL"



]



}



],



"enabled": true



}
```

## Regex examples

The common regex formats for sensitive data include:

Sensitive data type

ReGEx

IPv4

`\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`

Email address

`\b[\w\-\._]+?@[\w\-\._]+?\.\w{2,10}?\b`

Credit card number

`\b[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}\b`

Phone number

`\+?[0-9]{3}-?[0-9]{6,12}\b`

### Unsupported regular expressions

Data masking occurs within the entire expression or a capturing group. An expression has to match the regular expression engine syntax, and it cannot:

* Be part of more than one capturing group
* Contain the `lookbehind` zero-length assertion in a capturing group
* Contain the `backreference` zero-length assertion in a capturing group
* Contain greedy quantifiers (such as `x?`, `x*`, or `x+`) or possessive quantifiers (such as `x?+`, `x*+`, or `xx++`). Use lazy/reluctant qualifiers (such as `x??` and `x+?`) instead.

## FAQ

Where does sensitive data masking happen?

You can execute sensitive data masking in your environment so that the confidential data does not leave your infrastructure unprotected. If you import your data to Dynatrace via generic ingest, you need to mask the sensitive data on the source level, before ingestion. Alternatively, you can mask sensitive data during [Log Processing](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios."). However, if you choose to mask your data during Log processing, your data will leave your environment as log processing occurs on the Dynatrace side. Therefore, it is safer to mask it within your environment.

How many capturing groups are supported?

One. If none is provided, then the entire scope of the regular expression you provide is treated as one capturing group.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Related topics

* [Data privacy and security](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.")
* [Log Monitoring default limits (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.")


---


## Source: timestamp-configuration.md


---
title: Timestamp/splitting configuration (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration
scraped: 2026-02-18T05:44:31.076939
---

# Timestamp/splitting configuration (Logs Classic)

# Timestamp/splitting configuration (Logs Classic)

* 7-min read
* Updated on Sep 18, 2025

Log Monitoring Classic

Dynatrace allows you to define rules that control log data timestamps.

For the newest Dynatrace version, see [Timestamp/splitting configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

## Timestamp detection

By default, Log Monitoring automatically detects only the most common and unambiguous subset of date formats supported. For details, see [Supported timestamp formats (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.").

### No timestamp detected

When Log Monitoring is unable to determine the time format, it treats each log line as a separate log entry with an automatically assigned timestamp (observation timestamp) using a one-minute time resolution, except for lines starting with whitespaces (space, tab), which are treated as a continuation of an entry.

### Timestamp search limit

Regardless of format, the timestamp typically occurs within the first 64 characters of a log entry. However, the timestamp can occur elsewhere, in which case you can raise this limit on the OneAgent configuration page: **Log Monitoring** > **Timestamp/Splitting patterns**.

### Timestamp rules

Regardless of where it occurs in a log entry, a timestamp may be written in multiple formats. Dynatrace supports some timestamp formats by default, but sometimes multiple formats may fit the incoming log data and match the timestamp to an incorrect timestamp pattern.

Because of this, Log Monitoring also enables you to define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record. These rules contain a timestamp pattern, time zone, and matchers.

* **Pattern**âDefines what should be considered a timestamp in your logline.
* **Timestamp search limit**âspecifies the count of characters in each log line, measured from the beginning of the line, where the timestamp is searched.
* **Timestamps in indented lines**âEnable this option if you don't want to parse timestamps in lines that start with whitespace characters.
* **Time zone**âDefines the timestamp time zone. Optional if your timestamp pattern includes the timezone indicator (`%z`).
* **Matcher**âNarrows down the range for the rule and applies the timestamp pattern only to matched log entries. Because you can't use the `log.content` attribute in the timestamp pattern matchers, the highest granularity is a log source. Granularity is at this level because the timestamp pattern is used to split the contents of a log source into separate log records, so it is used before the `log.content` attribute's value (or any other attributes set on an individual log record's level) is determined.

  + If you create multiple rules matching the same log data, all defined time formats are searched for.
  + If you have at least one rule matching a given log, predefined formats are not applied to it.

### Multiple timestamp patterns in the same log source

When ingesting log entries, OneAgent parses the log entry for a timestamp.
To do this, it uses a list of matcher patterns.

* When the log entry contains one timestamp, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the first pattern in the list. If the entryâs timestamp matches one of the patterns, OneAgent uses that timestamp as the beginning of the log entry.
* When the log entry contains two or more timestamps, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the pattern that was matched in the previous log entry.

Therefore, it is possible that even if the log entryâs first timestamp matches the first pattern in the list of matching patterns, OneAgent will actually match the second timestampâbecause the previous log entry matched the second pattern.
See the code block below for an example.

```
Log entry 1: Pattern 1, Pattern 2



Log entry 2: Pattern 2



Log entry 3: Pattern 1, Pattern 2
```

For log entry 3, even if "Pattern 1" appears first in the list of matcher patterns, OneAgent will actually match "Pattern 2".

To ensure OneAgent evaluates only your desired timestamp patterns, carefully select which patterns are in your matching list. In the example above, to guarantee Pattern 1 is always used, remove Pattern 2 from your list. This may result in messages that only contain Pattern 2 timestamps to be dropped.

For example, if your log file contains both `%FT%T` (2024-01-01T12:30:01) and `%F %T %Z` (2024-01-01 12:30:01 UTC) patterns, and OneAgent successfully matches the first pattern in a line, it will prioritize that pattern for subsequent lines.

## Supported scopes

Three hierarchy scopes are supported: host, host group, and environment.

The hierarchy scopes are merged into one list in the following order:

1. Host rules
2. Host group rules
3. Environment rules

![Diagram showing the rule priority for timestamp configuration rules.](https://dt-cdn.net/images/timestamp-sopes-955-9292323a57.png)

The OneAgent receives the merged list (merged lists from its respective hosts, host groups, and environments) with no indication of which scopes are defined.

### Host scope

The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
5. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
7. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Environment scope

The environment scope is available in the settings menu.

1. Go to **Settings** > **Log Monitoring** > **Timestamp/Splitting patterns**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## Create rule

To add a rule (on the host, host group, or environment level) that interprets the incoming log data timestamps

1. Select **Add rule** to start configuring your rule.
2. **Rule name**

   The name to display for your configuration.
3. **Pattern**

   Enter the pattern to be read as a date from the logs. For details on timestamp formats, see [Supported timestamp formats (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.") and the [Date libraryï»¿](https://dt-url.net/o8034wt).

   You need to specify at least the year, month, day, hours, minutes, and seconds, although you can use alternative formats for them. You can include the time zone indicator (`%z`) or specify the time zone separately in the rule definition.

   Rules without a pattern can override the timezone only for default supported timestamps.
4. **Timestamp search limit**

   Use this field to define the number of characters in every log line where timestamp is searched. If you want to ignore timestamps and split logs using the [default rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-one-agent-log-data-format#plain-text-logs "This topic lists all the log formats supported by Log Management and Analytics"), set this value to `0`. Use this field to overwrite the global [timestamp search limit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration#timestamp-search-limit "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.") (default 64 bytes).
5. **Time zone**

   Select the time zone to apply to this pattern.  
   This setting is not enabled if you have already specified the timezone in the timestamp pattern (`%z`).

   You can select `Local time zone` to use the time zone of the host on which the OneAgent is running.
6. Select **Add matcher** to create a specific match for this rule and narrow down the scope for that rule.

   You can include multiple matchers in one rule. For example, the timestamp configuration rule can be applied to logs from a specific container, namespace, or log source. Multiple matchers with the same attribute use AND logic between matchers, while matchers with multiple values assigned to them use OR logic.

   Matcher attribute

   Matching is based on

   **Process group**

   The process group ID.

   **Log source**

   A log path; wildcards are supported in form of an asterisk.

   **K8s container name**

   The name of the Kubernetes container.

   **K8s namespace name**

   The name of the Kubernetes namespace.

   **K8s deployment name**

   The name of the Kubernetes deployment.

   **Container name**

   The name of the container.

   **DT entity container group ID**

   The DT entity container group ID.

   **Process technology**

   The technology name.
7. Select the matching attribute.
8. Select **Value** and, from the **Value** list, select the detected log data items.

   You can add multiple values to the selected attribute. You can have one matcher that indicates the `Log source` and matches values `/var/log/syslog` and `Windows Application Log`. Use asterisks (`*`) as wildcards to get a partial match.
9. Select **Save changes**.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

Rule reorder propagation delay

When you change the rule order (to change the order in which they are executed), allow for two or three minutes of propagation time between when you save the change and when the change takes effect.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

## REST API

You can use the Settings API to manage your timestamp configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for timestamp configuration, list all available schemas and look for the `builtin:logmonitoring.timestamp-configuration` schema identifier.

Timestamp configuration objects are available for configuration on the following scopes:

* `environment`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a timestamp configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The timestamp configuration schema identifier (`schemaId`) is `builtin:logmonitoring.timestamp-configuration`. Here is an example JSON payload with the timestamp configuration:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.timestamp-configuration",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "date-time-pattern": "%Y-%m-%d %H:%M:%S",



   "timezone": "CET",



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.


---


## Source: timestamp-data-format.md


---
title: Supported timestamp formats (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format
scraped: 2026-02-18T05:45:56.744866
---

# Supported timestamp formats (Logs Classic)

# Supported timestamp formats (Logs Classic)

* 3-min read
* Updated on Sep 18, 2025

Log Monitoring Classic

Timestampâincluding date, time, timezone, and offsetâis searched for in the first 64 characters of the log content (this value is configurable via **Log Monitoring** > **Timestamp/Splitting patterns**). If an offset or timezone is not found, the local timezone of a host is used.

For the newest Dynatrace version, see [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics.").

During log processing, each line where a supported timestamp is detected starts a new log record. A line without a timestamp is considered to be a continuation of an existing log record and appended to a line that contains a timestamp.  
If no timestamp is present in a log file or a timestamp is not recognized due to unsupported format, each line not starting with whitespace characters, such as `space` or `tab`, starts a new log record. Each line starting with whitespace characters, such as `space` or `tab`, is treated as a log record continuation.  
Due to multiple formats of incoming log data, Log Monitoring also enables you to define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record. For more details on defining date format, see [Log timestamp configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

The supported [timestamp formatsï»¿](https://dt-url.net/6e034iy) include:

* ISO 8601 format: `%Y-%m-%d %H:%M:%S`  
  Example: `2022-04-17 11:25:12.345`
* RFC 3339 format: `%Y-%m-%dT%H:%M:%S`  
  Example: `2022-04-17T11:25:12.345`
* Unix Epoch format, providing the number of milliseconds that have elapsed since January 1, 1970
  Example: `1652088888997`
* RFC 3164 format: `%b %d %H:%M:%S`  
  Example: `Apr 17 11:25:12`
* Db2 (IBM database 2) format: `%Y-%m-%d-%H.%M.%S`  
  Example: `2022-05-17-11.25.12.114000-300`
* IIS format: `%m/%d/%Y, %H:%M:%S`  
  Example: `04/17/2022, 11:25:12.345`
* W3C (World Wide Web Consortium) format: `%Y-%m-%d %H:%M:%S`  
  Example: `2022-04-17 11:25:12.345` specified in the UTC timezone
* Klog and Golang/glog format: `[IWEF]%m%d %H:%M:%S`
  Example: `I0408 06:40:02.634162`
* Other common formats:

  + `%d %b %Y %H:%M:%S` (example: `17 Apr 2022 11:25:12.345`)
  + `%Y %b %d %H:%M:%S` (example: `2022 Apr 17 11:25:12.345`)
  + `%d/%b/%Y:%H:%M:%S` (example: `17/Apr/2022:11:25:12.345`)

JSON files are supported for Docker only. If the `log` tag is detected in a JSON file, then the corresponding message is ingested and analyzed. Within the message, the timestamp of one of the supported formats is searched. If no supported file format is found, the `time` tag is searched. For example:

```
{



"log":"2020-11-24 11:01:36,484 CRIT Supervisor running as root (no user in config file)\n",



"stream":"stdout",



"time":"2020-11-24T11:01:36.484996713Z"



}



{



"log":"2020-11-24 11:01:36,500 INFO RPC interface 'supervisor' initialized\n",



"stream":"stdout",



"time":"2020-11-24T11:01:36.50065223Z"



}
```

### Examples of valid log file time formats

Most of the supported timestamp formats are coupled with automatic timezone format detection. The following time zone formats are recognized:

* Offset to UTC zone  
  Examples:

  `2022-04-17 11:25:12.345 +01:00`  
  `2022-04-17 11:25:12.345 +0100`  
  `2022-04-17 11:25:12.345Z -01:00`  
  `2022-04-17 11:25:12.345Z-0100`  
  `2022-04-17 11:25:12.345 UTC-01:00`  
  `2022-04-17 11:25:12.345 GMT-0100`
* Full [IANAï»¿](https://dt-url.net/jq034g6) timezone name.  
  Example:  
  `2022-04-17 11:25:12.345 Europe/Warsaw`
* Timezone name abbreviation  
  Examples:  
  `2022-04-17 11:25:12.345 CEST`  
  `2022-12-17 11:25:12.345 CET`  
  `2022-04-17 11:25:12.345Z`  
  `2022-04-17 11:25:12.345UTC+0100`

If no time zone indicator is found in the log line, the time zone used when parsing a timestamp is by default set to the one configured in
**Settings** > **Log Monitoring** > **Advanced log settings** > **Default timezone for agents**.

### Override the timezone

In case automatic timezone format detection fails, you can add a rule overriding time zone in the [Log timestamp configuration page](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration#createrule "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

## Default used timezone

When processing timestamps, OneAgent follows both local timezone patterns and UTC patterns.

### Local timezone patterns

When no timezone is specified in the log content, the following timestamp formats default to the **local timezone** of the host:

* ISO 8601 (`%Y-%m-%d %H:%M:%S`)
* RFC 3164 (`%b %d %H:%M:%S`)
* IIS (`%m/%d/%Y, %H:%M:%S`)
* Klog and Golang/glog (`[IWEF]%m%d %H:%M:%S`)
* `%d %b %Y %H:%M:%S`
* `%Y %b %d %H:%M:%S`
* `%d/%b/%Y:%H:%M:%S`

### UTC timezone patterns

When no timezone is specified in the log content, the following timestamp formats default to **UTC**:

* RFC 3339 (`%Y-%m-%dT%H:%M:%S`)
* Db2 (`%Y-%m-%d-%H.%M.%S`)
* W3C (`%Y-%m-%d %H:%M:%S`)
* Unix time

To verify which timezone was used for timestamp parsing, search the OneAgent logs (`oneagent-logmon-detailed.log`) for `Diagnostic statistics for LGI`.


---


## Source: log-monitoring-configuration.md


---
title: Log Monitoring configuration (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration
scraped: 2026-02-18T05:43:22.166692
---

# Log Monitoring configuration (Logs Classic)

# Log Monitoring configuration (Logs Classic)

* 5-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

By default, Log Monitoring is activated in your Dynatrace environment. To start ingesting logs, depending on your use case, you need to either configure log storage rules on OneAgents or send logs to ingest APIs.

* [Log ingest rules (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.")
* [Log ingestion API (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")

You can confirm that Log Monitoring is enabled or you can enable it globally or on a host level, but checking the status and enabling or disabling Log Monitoring is optional in most cases. If you plan to use Log Monitoring, you can focus on OneAgent settings that directly affect how Log Monitoring is operating.

* [OneAgent settings](#lm-oneagent-settings).

## Check Log Monitoring status

Optional

You can check if Log Monitoring is enabled in your Dynatrace environment globally (Dynatrace web UI), or you can check if Log Monitoring is enabled on a host level (OneAgent CLI).

* To check if Dynatrace Log Monitoring is enabled globally:

  1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
  2. Find **Log Monitoring** in the list of supported technologies, and select **Edit** (pencil icon).
  3. Check if **Monitor Log Monitoring on every host** option is enabled.
* To check if Dynatrace Log Monitoring is enabled on a host level:  
  Use OneAgent CLI and execute the `oneagentctl` command with the `--get-app-log-content-access` parameter to check whether Log Monitoring is enabled:

  + Linux: `./oneagentctl --get-app-log-content-access`
  + Windows: `.\oneagentctl.exe --get-app-log-content-access`

## Enable or disable Log Monitoring

Optional

Similarly to checking Log Monitoring status, you can enable or disable Log Monitoring in your Dynatrace environment globally (Dynatrace web UI), or on a host level (OneAgent CLI).

* To activate Dynatrace Log Monitoring globally:

  1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
  2. Find **Log Monitoring** in the list of supported technologies, and select **Edit** (pencil icon).
  3. Turn on **Monitor Log Monitoring on every host**.
* To enable or disable Dynatrace Log Monitoring on a host level:  
  Use OneAgent CLI and execute the `oneagentctl` command-line interface to execute the following command at the individual host level.  
  Set the `--set-app-log-content-access` parameter to `true` or `false` to disable or enable Log Monitoring:

  + Linux: `./oneagentctl --set-app-log-content-access=true`
  + Windows: `.\oneagentctl.exe --set-app-log-content-access=true`

  Restart OneAgent service to apply changes.

## OneAgent settings

Dynatrace Log Monitoring uses the [OneAgent log module](/docs/discover-dynatrace/get-started/glossary#glossary-oneagent-log-module "Get acquainted with Dynatrace terminology.") enabled by default with all OneAgent installations. While Log Monitoring does not require any specific configuration, you can modify some of the options available for the OneAgent log module.

You can adjust:

* Enable and disable automatic log detection for different technologies.
* Define default timezone in containers.
* Enable defining the storage configuration by a configuration file on the host.
* Define specific location where the timestamp and severity occur in your incoming log data.
* Define the maximum number of log group instances per entity.

### Global OneAgent settings for Log Monitoring

1. Go to **Settings** > **Log Monitoring** > **OneAgent settings**.
2. Adjust settings and **Save changes**.

### Host-specific OneAgent settings for Log Monitoring

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **Log Monitoring** and **Advanced log settings**.
4. Adjust settings and **Save changes**.

## Default OneAgent settings

Setting

Description

Default

**Detect open log files**

This option automatically detects logs written by important processes.

enabled

**Detect IIS logs**

This option allows the detection of logs and event logs written by the Microsoft IIS server.

enabled

**Detect system logs**

Linux: Detects syslogs, and message logs.
Windows: Detects system, application, and security event logs.

enabled

**Detect logs on network file systems**

This option detects logs stored on the Network File System server. This applies for Linux only

disabled

**Allow OneAgent to monitor OneAgent logs**

This option allows OneAgent to monitor own logs.

disabled

**Detect logs of containerized applications**

This option allows the detection of log messages written to the containerized application's stdout/stderr streams. It also detects Kubernetes pod logs.

enabled

**Set UTC as default timezone in containers**

This sets the default timezone of the containers as UTC.

enabled

**Timestamp search limit**

Set the timestamp search.

`64` bytes

**Severity search chars limit**

Set the severity search characters limit.

`100` bytes

**Severity search lines limit**

Set the severity search lines limit.

`2`

**Maximum of log group instances per entity limit - count**

Set the upper limit for log group instances per entry.

`200`

## Configuration file Optional

The configuration file located on each OneAgent is used to set three options. For security reasons, these options can only be set on the host level and are available only by creating a JSON file in a specific location:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\`

The configuration file name must have the `json` extension; the file name is otherwise unrestricted.

By default, these options are set for the OneAgent log module to operate properly and to auto-detect log files on the specific host. Modifying this configuration file is not required.

### Multiple configuration files

You can have multiple JSON configuration files in the configuration folder. Files are evaluated in alphabetical order. Options from the last evaluated file takes priority.

### Preexisting configuration files

If your OneAgent installation is upgraded, you may find a `_migratedloganalytics.conf.json` file that contains your configuration migrated from the `ruxitagentloganalytics.conf` on your host.

During installation, the OneAgent installer may create `_loganalyticsconf.ctl.json`, which will contain options used during the installation. The same file will be used to store relevant options set by the OneAgentCtl tool.

### Available options

* `AppLogContentAccess`  
  Enables access to the log file content on this host. If set to `false`, the log file will be displayed in the user interface, but the content won't be accessible. Note that the OneAgent will still auto-detect log files unless the flag `AppLogAutoDetection` is set to `false`.
* `AppLogRemoteConfiguration`  
  Enables the manual configuration of logs to be accessed and monitored. If set to `false`, it won't be possible to add logs manually using the settings interface.
* `AppLogAutoDetection`  
  Enables auto-detection of log files on this host. If set to `false`, logs won't be auto-detected.

### Example

```
{



"agent-configuration": [



{



"AppLogRemoteConfiguration": true,



"AppLogContentAccess": true,



"AppLogAutoDetection": true



}



]



}
```


---


## Source: log-monitoring-limits.md


---
title: Log Monitoring default limits (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits
scraped: 2026-02-17T05:06:08.465470
---

# Log Monitoring default limits (Logs Classic)

# Log Monitoring default limits (Logs Classic)

* 1-min read
* Updated on Feb 02, 2026

Log Monitoring Classic

This page lists default limits for the latest version of Dynatrace Log Monitoring.

The current limitations apply to both log file ingestion and generic log ingestion via API.

## Log ingestion limits

The table below summarizes the most important default limits related to log ingest. All presented limits refer to UTF-8 encoded data.

| Type | Limit | Description |
| --- | --- | --- |
| Content | 8 kB | The maximum size of log entry body |
| Attribute key | 100 bytes | The key of an attribute value |
| Attribute value length | 250 bytes | The maximum length of an attribute value |
| Number of log attributes | 50 | The maximum number of attributes a log can contain |
| Log events per minute | 1M/min | The maximum number of log events in a minute |
| Log age | 24 hours | The maximum age of log entries when ingested |
| Logs with future dates | No restriction[1](#fn-1-1-def) | How far into the future log entries can reach |
| Values per attribute | 32 values | The maximum number of individual values an attribute can contain |
| Request size | 10 MB | The maximum size of the payload data |
| Number of log records | 50,000 records | The maximum number of log records per request |
| Nested objects | 5 levels | The maximum number of levels ingested with nested objects |

1

There is no ingestion limitation on log entries with future timestamps, but entries with timestamps further than 10 minutes into the future have their timestamps set to the moment of ingestion.

## Unsupported autodiscovery scenarios

Scenarios that are not supported in the rotated log autodiscovery process include:

* Rotated log generation with a directory change. This process could lead to the creation of numerous non-aggregated and/or incomplete logs, as well as to resource overuse.
* Rotated log generation with immediate compression, where the application addresses a file with the same name. If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed.
  Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log creation.

## Limits for your log autodiscovery when using OneAgent

Log files in OneAgent:

* cannot be deleted earlier than a minute after creation.
* must be appended (old content is not updated).
* must have text content.
* must be opened constantly (not just for short periods of adding log entries).
* must be opened in write mode.
* must not be smaller than the configured size threshold (default: 500 bytes) to be checked for binary content.

The default maximum number of log sources per process group instance is 200. This value is configurable via the **Maximum number of log sources per process group instance** option in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log Monitoring** > **Advanced log settings**.

In standard environments, OneAgent log module supports up to 10,000 files in one directory with logs and 200 MB of new log content per minute. If you have more data, especially a higher level of magnitude, there's a high chance that the OneAgent log module supports it. Contact the Dynatrace support team to review your setup beforehand.

In special cases, such as very poor hardware performance, the OneAgent log module's limitations might be more strict.

## Log rotation limits

Scenarios that are not supported in the rotated log monitoring process include:

Type

Description

Rotated log generation with a directory change

The potential consequence is the creation of duplicates and/or incomplete logs.

Rotated log generation with immediate compression

If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed. Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log ingest. There should be at least one uncompressed rotated file.

Rotated log generation with queue logic

The oldest log records are removed whenever new content is added to a file, resulting in a relatively constant log file size. This scenario can be easily replaced with a supported rotation scheme by, for example, starting a new file when the current file reaches a predefined size.

## Log record accepted time range

The following rules apply to all log event sources, such as OneAgent and the generic log ingestion API.

Log record timestamp

Description

The current time minus 24 hours for log records.

The event is dropped if the log event contains a timestamp before the current time minus 24 hours.
If the record is ingested via the generic Log Ingestion API, it can return the following:

`400` - if all log events in the payload have timestamps earlier than the current time minus 24 hours.
Message in response: `All logs are out of correct time range.`

`200` - in case some of the events in the payload have timestamps earlier than the current time minus 24 hours.
Example message in response: `2 events were not ingested because of timestamp out of correct time range`.

`204` - (No Content) in case of success.

The current time minus two hours for log metrics and events.

The data point is dropped if the log metric data point timestamp is before the current time minus two hours.

Current time plus ten minutes

The time stamp is reset to current time.

## High-cardinality attributes

Unique log data attributes (high-cardinality attributes) such as `span_id` and `trace_id` generate unnecessarily excessive facet lists that may impact log viewer performance. Because of this, they aren't listed in log viewer facets. You can still use them in a log viewer advanced search query.

## Log ingestion API request objects

In addition to generic Dynatrace API limitations ([Dynatrace API - Access limit](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")) the following log ingestion API specific limits apply:

* `LogMessagePlain plain` text object.  
  The length of the message is limited to 8,192 characters. Any content exceeding the limit is trimmed.
* `LogMessageJson` JSON object.  
  The object might contain the following types of keys (the possible key values are listed below):

  + Timestamp. The following formats are supported: UTC milliseconds, RFC3339, and RFC3164. If not set, the current timestamp is used.
  + Severity. If not set, NONE is used.
  + Content. If the content key is not set, the whole JSON is parsed as the content.
  + Semantic attribute. Only values of the String type are supported. Semantic attributes are indexed and can be used in queries. These are also displayed in aggregations (facets). If an unsupported key occurs it is not indexed and cannot be used in indexing and aggregations.

  The length of the value is limited. Any content exceeding the limit is trimmed. Default limits:

  + Content: 8,192 characters.
  + Semantic attribute value: 250 characters.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Active Gate throughput

If you are using the SaaS endpoint, you don't have to worry about the Active Gate throughput. The throughput is the same as for Grail.
If you use Environmental Active Gate, the throughput is 3.3GB/min with RTT <= 200 ms.


---


## Source: log-processing-examples.md


---
title: Log processing examples (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples
scraped: 2026-02-18T05:53:56.617855
---

# Log processing examples (Logs Classic)

# Log processing examples (Logs Classic)

* Tutorial
* 18-min read
* Updated on Sep 22, 2025

Log Monitoring Classic

Depending on the rules that you create, you can customize incoming log data according to your needs. See below for example data processing scenarios.

* [Example 1](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample1 "Example log processing scenarios.") - Fix unrecognized timestamp and loglevel visible in the log viewer based on matched log source.
* [Example 2](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample2 "Example log processing scenarios.") - Define searchable custom attribute using the extracted identifier from a matched phrase in the log content.
* [Example 3](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample3 "Example log processing scenarios.") - Create billed duration metric for AWS service using log data.
* [Example 4](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample4 "Example log processing scenarios.") - Parse out specific fields from JSON content.
* [Example 5](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample5 "Example log processing scenarios.") - Parse out attributes from different formats within a single pattern expression.
* [Example 6](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample6 "Example log processing scenarios.") - Multiple PARSE commands within a single processing rule.
* [Example 7](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample7 "Example log processing scenarios.") - Use specialized matchers.
* [Example 8](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample8 "Example log processing scenarios.") - Manipulate any attribute from log (not only content).
* [Example 9](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample9 "Example log processing scenarios.") - Add a new attribute to the current log event structure.
* [Example 10](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample10 "Example log processing scenarios.") - Basic math on attributes.
* [Example 11](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample11 "Example log processing scenarios.") - Drop a specific attribute from log message.
* [Example 12](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample12 "Example log processing scenarios.") - Drop the whole log event.
* [Example 13](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios.") - Mask any attribute.
* [Example 14](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample14 "Example log processing scenarios.") - Rename attributes.
* [Example 15](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample15 "Example log processing scenarios.") - Input field data types.

### Example 1: Fix unrecognized timestamp and loglevel

You can fix unrecognized timestamp and loglevel visible in the log viewer based on matched log source.
For this example, let's assume that you see a stored event in the log viewer from the `log.source` application that is set to `/var/log/myapp/application.log.#`

You notice a couple of things you want to fix:

* The log contains an unrecognized timestamp format that you want to be treated as a log event timestamp.
* There is no proper logLevel detected.

So you want to transform your log data to contain the proper values in the timestamp and logLevel fields, and you want to add a new `thread.name` attribute containing a properly extracted value.

To create a processing rule

1. Copy the log viewer query to the clipboard (`log.source="/var/log/myapp/application.log.#"`).
2. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
3. Enter the rule name and the copied log query from your clipboard.  
   **Rule name**: `MyApp log processor`  
   **Matcher**: `log.source="/var/log/myapp/application.log.#"`
4. Enter the rule definition to parse out the timestamp, thread name, and log level.  
   **Rule definition**: `PARSE(content, "TIMESTAMP('MMMMM d, yyyy HH:mm:ss'):timestamp ' [' LD:thread.name '] ' UPPER:loglevel")`  
   where:

   * `TIMESTAMP` matcher is used to look for the specific datetime format, and the matched value is set as the existing timestamp log attribute.
   * `LD` (Line Data) matcher is used to match any chars between literals `' ['` and `'] '`.
   * `UPPER` literal is used to match uppercase letters.
   * The remaining part of the content is not matched.
5. Enter the following log data fragment manually in the **Log sample** text box.

   ```
   {



   "event.type":"LOG",



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "status":"NONE",



   "timestamp":"1650889391528",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"NONE"



   }
   ```
6. Select **Test the rule**.  
   The processed log data is displayed. The `timestamp` and the `loglevel` fields have proper values. The additional attribute `thread.name` is also correctly extracted.

   ```
   {



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "timestamp":"1650794392000",



   "event.type":"LOG",



   "status":"NONE",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"INFO",



   "thread.name":"myPool-thread-1"



   }
   ```
7. Save your log processing rule.

As the new log data is ingested, you'll be able to see processed log data in the log viewer.

### Example 2: Define searchable custom attribute

You can define a searchable custom attribute using the extracted identifier from a matched phrase in the log content.

In this example, you see the following log line in the log file (not stored in Dynatrace yet), and you want to extract an identifier from that log line to make it searchable in the log viewer.

`2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`

1. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
2. Enter a rule name and log query. For the log query, use the constant phrase from the log data content (`content="Critical error occurred for product ID"`)  
   **Rule name**: `MyApp product ID with error`  
   **Matcher**: `content="Critical error occurred for product ID"`
3. Enter a rule definition to parse out the ID.  
   **Rule definition**: `PARSE(content, "LD 'product ID:' SPACE? INT:my.product.id")`
4. Assuming that you observed the following log record in the log viewer, you can select **Download a log sample** and automatically populate the **Log sample** text box with your log data.  
   `2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`  
   Alternatively, you can insert the observed log record as log record content manually in the **Log sample** text box:

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet"



   }
   ```
5. Select **Test the rule**.  
   The processed log data is displayed. The processed log data displayed is enriched with the parsed-out product identifier.

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet",



   "timestamp": "1650961124832",



   "my.product.id": "12345678"



   }
   ```
6. Save your log processing rule.
7. Go to **Settings** > **Log Monitoring** > **Custom attributes** and select **Add custom attribute**.
8. Create a custom attribute based on a parsed-out product identifier (`my.product.id`).  
   **Key**: `my.product.id`  
   For details see, [Log custom attributes (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Learn how to create and use custom attributes during log data ingestion.").
9. Save your custom attribute.
10. Now you can search and filter the log data by the `my.product.id` attribute in the log viewer.

### Example 3: Create billed duration metric for AWS service using log data

In this example, you want to monitor the actual billed duration from your AWS services. You want to use the `cloud.provider` attribute with the `aws` value in your log data. In the log viewer, you see a log record containing the following line:

`REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`

Additionally, that log record contains the `cloud.provider` attribute with the `aws` value.

1. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
2. Enter the rule name and the log query. For the log query, use the constant phrase from the log data content for `cloud.provider="aws"` and `content="Billed Duration"`  
   **Rule name**: `AWS services - billed duration`  
   **Matcher**: `cloud.provider="aws" and content="Billed Duration"`
3. Enter a rule definition to parse out the billed duration value.  
   **Rule definition**: `PARSE(content, "LD 'Billed Duration:' SPACE? INT:aws.billed.duration")`
4. Assuming that you observed the following log record the log viewer, you can select **Download a log sample** and automatically populate the **Log sample** text box with your log data.  
   `REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`  
   Alternatively, you can enter the following log data fragment (containing other additional attributes) manually in the **Log sample** text box:

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO"



   }
   ```
5. Select **Test the rule**.  
   The processed log data is displayed. The processed log data displayed is enriched with the new `aws.billed.duration` attribute.

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO",



   "aws.billed.duration": "5034"



   }
   ```
6. Save your log processing rule.
7. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
8. Create a log metric based on the parsed-out product identifier (`aws.billed.duration`).  
   **Key**: `log.aws.billed.duration`  
   **Query**: `cloud.provider="aws" and content="Billed Duration"`  
   **Measure**: `Attribute value`  
   **Attribute**: `aws.billed.duration`  
   For details see, [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.").
9. Save your log metric.
10. The `log.aws.billed.duration` metric is visible in Data Explorer, and you can use it throughout Dynatrace like any other metric. You can add it to your dashboard, include it in analysis, and even use it to create alerts.

    Log metric availability in Dynatrace

    A created log metric is available only when new log data is ingested and it matches the log query defined during log metric creation. Ensure that new log data has been ingested before using the log metric in other areas of Dynatrace.

### Example 4: Parse out specific fields from JSON content

In this example, you see a log line that has the following JSON structure:

`{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }`

The sample log would look like this:

```
{



"content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

* Parsing field from JSON in flat mode.  
  You can use a JSON matcher and configure it to extract desired fields as top-level log attributes. The matcher in flat mode creates attributes automatically and names them exactly the same as the corresponding JSON field names.

  You can then use the `FIELDS_RENAME` command to set the names that fit you.

  Processing rule definition:

  ```
  PARSE(content, "JSON{STRING:stringField}(flat=true)")



  | FIELDS_RENAME(better.name: stringField)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "better.name": "someValue"



  }
  ```
* Parsing nested field from JSON.  
  You can also parse more fields (including nested ones) using a JSON matcher without flat mode. As a result, you get a `VariantObject` that you can process further. For example, you can create a top-level attribute from its inner fields.

  Processing rule definition:

  ```
  PARSE(content, "



  JSON{



  STRING:stringField,



  JSON {STRING:nestedStringField1}:nested



  }:parsedJson")



  | FIELDS_ADD(top_level.attribute1: parsedJson["stringField"], top_level.attribute2: parsedJson["nested"]["nestedStringField1"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "top_level.attribute1": "someValue",



  "top_level.attribute2": "someNestedValue1"



  }
  ```
* Parsing all fields from JSON in auto-discovery mode.  
  Sometimes you're interested in all of the JSON fields. You don't have to list all of the attributes. Instead, a JSON matcher can be used in auto-discovery mode. As a result, you get a `VARIANT_OBJECT` that you can process further. For example, you can create a top-level attribute from its inner fields.

  Processing rule definition:

  ```
  PARSE(content,"JSON:parsedJson")



  | FIELDS_ADD(f1: parsedJson["intField"],



  f2:parsedJson["stringField"],



  f3:parsedJson["nested"]["nestedStringField1"],



  f4:parsedJson["nested"]["nestedStringField2"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "f1": "13",



  "f2": "someValue",



  "f3": "someNestedValue1",



  "f4": "someNestedValue2"



  }
  ```
* Parsing any field from JSON, treating content like plain text.  
  With this approach, you can name the attribute as you lik, but the processing rule is more complex.

  Processing rule definition:

  ```
  PARSE(content, "LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute ")
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "newAttribute": "someValue"



  }
  ```

### Example 5: Parse out attributes from different formats

You can parse out attributes from different formats within a single pattern expression.

In this example, one or more applications is logging a user identifier that you want to extract as a standalone log attribute. The log format is not consistent because it includes various schemes to log the user ID:

* `user ID=`
* `userId=`
* `userId:`
* `user ID =`

With the optional modifier (question `?`) and `Alternative Groups`, you can cover all such cases with a single pattern expression:

```
PARSE(content, "



LD //matches any text within a single line



('user'| 'User') //user or User literal



SPACE? //optional space



('id'|'Id'|'ID') //matches any of these



SPACE? //optional space



PUNCT? //optional punctuation



SPACE? //optional space



INT:my.user.id



")
```

Using such a rule, you can parse out the user identifier from many different notations. For example:

`03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user ID:1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0`

### Example 6: Multiple PARSE commands within a single processing rule

You can handle various formats or perform additional parsing on already parsed-out attributes with multiple `PARSE` commands connected with pipes (`|`).

For example, with the following log:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

First, you can parse out the message field, the user ID, and the error message.

```
PARSE(content, "JSON{STRING:message}(flat=true)") | PARSE(message, "LD 'user ' INT:user.id ': ' LD:error.message")
```

The result is:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



"message": "Error occurred for user 12345: Missing permissions",



"user.id": "12345",



"error.message": "Missing permissions"



}
```

### Example 7: Use specialized matchers

We provide a comprehensive list of matchers that ease pattern building.

For example, you can parse the following sample log event:

```
{



"content":"2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200"



}
```

using the specialized matchers:

```
PARSE(content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code")
```

and the result is:

```
{



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200",



"timestamp": "1652275425000",



"loglevel": "INFO",



"ip": "192.168.33.1",



"request": "GET /api/v2/logs/ingest HTTP/1.0",



"code": "200"



}
```

### Example 8: Manipulate any attribute from log (not only content)

Unless specified otherwise, the processing rule works only on the read-only content field. For it to work on different log event attributes, you need to use the `USING` command.

For example, the following rule declares two input attributes: writable status and read-only content.
Next, it checks whether the status is `WARN` and the content contains the text `error`. If both conditions are true, the rule overwrites `status` with the value `ERROR`.

Processing rule definition:

```
USING(INOUT status:STRING, content)



| FIELDS_ADD(status:IF_THEN(status == 'WARN' AND content CONTAINS('error'), "ERROR"))
```

Log data sample:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "WARN",



"content":"Some error message"



}
```

Result after transformation:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "ERROR",



"content":"Some error message"



}
```

### Example 9: Add a new attribute to the current log event structure

The FIELDS\_ADD command can be used to introduce additional top-level log attributes.
The following script adds two attributes: the first one stores the length and the second one stores the number of words that are in the content field.

Processing rule definition:

```
FIELDS_ADD(content.length: STRLEN(content), content.words: ARRAY_COUNT(SPLIT(content,"' '")))
```

Log data sample:

```
{



"log.source": "new_attributes",



"timestamp": "1656010654603",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

Result after transformation:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"timestamp": "1656010654603",



"log.source": "new_attribute",



"content.length": "62",



"content.words": "9"



}
```

### Example 10: Basic math on attributes

With all of the available functions and operators, it's easy to perform calculations.

In the following example, we parse the values of `total` and `failed`, calculate the percentage that failed, and concatenate the value with the percentage sign. Then we store it in a new attribute called `failed.percentage` and remove the temporary fields.

Processing rule definition:

```
PARSE(content,"LD 'total: ' INT:total '; failed: ' INT:failed")



| FIELDS_ADD(failed.percentage: 100.0 * failed / total + '%')



| FIELDS_REMOVE(total, failed)
```

Log data sample:

```
{



"timestamp": "1656011338522",



"content":"Lorem ipsum total: 1000; failed: 250"



}
```

Result after transformation:

```
{



"content": "Lorem ipsum total: 1000; failed: 250",



"timestamp": "1656011338522",



"failed.percentage": "25.0%"



}
```

### Example 11: Drop a specific attribute from log message

To drop an event attribute that is a part of the original record, we first need to declare it as a writable (`INOUT` option) input field with the `USING` command and then explicitly remove it with the `FIELDS_REMOVE` command so that it is not present in the output of the transformation.

In the following example, we declare `redundant.attribute` as an obligatory writeable attribute of `STRING` type and then we remove it.

Processing rule definition:

```
USING(INOUT redundant.attribute:STRING)



| FIELDS_REMOVE(redundant.attribute)
```

Log data sample:

```
{



"redundant.attribute": "value",



"timestamp": "1656011525708",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

Result after transformation:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus.",



"timestamp": "1656011525708"



}
```

We could use the `?` character to mark the attribute as optional so that the transformation will still run and also succeed if the attribute is not present in the source event.

In this case, the definition would look like this:

```
USING(INOUT redundant.attribute:STRING?)



| FIELDS_REMOVE(redundant.attribute)
```

### Example 12: Drop the whole log event

The whole log event can be dropped with a `FILTER_OUT` command. The event is dropped when the condition passed as the command parameter is fulfilled.

* Prematcher-based dropping
  In most cases, it is enough to drop every event that has been pre-matched.

  For example, if we want to drop all `DEBUG` and `TRACE` events, we could set the matcher query to match either of those statuses and then use the `FILTER_OUT` command to catch everything.

  Matcher:

  ```
  status="DEBUG" or status="TRACE"
  ```

  Processing rule definition:

  ```
  FILTER_OUT(true)
  ```

  Log data sample:

  ```
  {



  "status": "DEBUG",



  "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



  }
  ```

  This way, all logs with status `DEBUG` or `TRACE` are dropped.
* Advanced dropping condition
  It's also possible to have some extra logic and not drop all the events that are pre-matched.

  In the following example, we drop incoming events where the execution time is below 100 ms.

  Log data sample:

  ```
  {



  "content":"2022-06-23 06:52:35.280 UTC INFO My monitored service call took 97ms"



  }
  ```

  Processing rule definition:

  ```
  PARSE(content, "LD 'My monitored service call took ' INT:took 'ms'")



  | FILTER_OUT(took < 100)



  | FIELDS_REMOVE(took)
  ```

### Example 13: Mask any attribute

Whenever the content or any other attribute is to be changed, it has to be declared as `INOUT` (writable) with the `USING` command. The `REPLACE_PATTERN` is a very powerful function that can be useful when we want to mask some part of the attribute.

* In the following example, we mask the IP address, setting value 0 to the last octet.

  Processing rule definition:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: IPADDR(ip) & 0xFFFFFF00l)
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.0"



  }
  ```
* In the following example, we mask the IP address, setting value `xxx` to the last octet.

  Processing rule definition:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: REPLACE_PATTERN(ip, "(INT'.'INT'.'INT'.'):not_masked INT", "${not_masked}xxx"))
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.xxx"



  }
  ```
* In the following example, we mask the entire email address using `sha1` (Secured Hash Algorithm)

  Processing rule definition:

  ```
  USING(INOUT email)



  | FIELDS_ADD(email: REPLACE_PATTERN(email, "LD:email_to_be_masked", "${email_to_be_masked|sha1}"))
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "john.doe@dynatrace.com"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "9940e79e41cbf7cc452b137d49fab61e386c602d"



  }
  ```
* In the following example, we mask the IP address, email address, and credit card number from the content field.

  Processing rule definition:

  ```
  USING(INOUT content)



  | FIELDS_ADD(content: REPLACE_PATTERN(content, "



  (LD 'ip: '):p1                                   // Lorem ipsum ip:



  (INT'.'INT'.'INT'.'):ip_not_masked               // 192.168.0.



  INT                                              // 12



  ' email: ':p2                                    //  email:



  LD:email_name '@' LD:email_domain                // john.doe@dynatrace.com



  ' card number: ': p3                             //  card number:



  CREDITCARD:card                                  // 4012888888881881



  ", "${p1}${ip_not_masked}xxx${p2}${email_name|md5}@${email_domain}${p3}${card|sha1}"))
  ```

  Log data sample:

  ```
  {



  "timestamp": "1656010291511",



  "content": "Lorem ipsum ip: 192.168.0.12 email: john.doe@dynatrace.com card number: 4012888888881881 dolor sit amet"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum ip: 192.168.0.xxx email: abba0b6ff456806bab66baed93e6d9c4@dynatrace.com card number: 62163a017b168ad4a229c64ae1bed6ffd5e8fb2d dolor sit amet",



  "timestamp": "1656010291511"



  }
  ```

### Example 14: Rename attributes

With the `FIELDS_RENAME` command, we can rename attributes that were a part of an original log event and attributes created within the processor.
Whenever we want to change any attribute from the original event, we need to declare it as `INOUT` (writeable).

In the following example, we rename an existing attribute. Furthermore, we parse out the field from JSON in flat mode and rename the new attribute that has been created automatically with the JSON field name.

Processing rule definition:

```
USING(INOUT to_be_renamed, content)



| FIELDS_RENAME(better_name: to_be_renamed)



| PARSE(content,"JSON{STRING:json_field_to_be_renamed}(flat=true)")



| FIELDS_RENAME(another_better_name: json_field_to_be_renamed)
```

Log data sample:

```
{



"timestamp": "1656061626073",



"content":"{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"to_be_renamed": "Lorem ipsum"



}
```

Result after transformation:

```
{



"content": "{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"timestamp": "1656061626073",



"better_name": "Lorem ipsum",



"another_better_name": "dolor sit amet"



}
```

### Example 15: Input field data types

The script in a processor definition operates with strongly typed data: the functions and operators accept only declared types of data. The type is assigned to all input fields defined in the `USING` command as well as to variables created while parsing or using casting functions.

Processing rule definition:

```
USING(number:INTEGER, avg:DOUBLE, addr:IPADDR, arr:INTEGER[],bool:BOOLEAN, ts:TIMESTAMP)



| FIELDS_ADD(multi:number*10)



| FIELDS_ADD(avgPlus1:avg+1)



| FIELDS_ADD(isIP: IS_IPV6(addr))



| FIELDS_ADD(arrAvg: ARRAY_AVG(arr))



| FIELDS_ADD(negation: NOT(bool))



| FIELDS_ADD(tsAddYear: TIME_ADD_YEAR(ts,1))
```

Log data sample:

```
{



"content":"Lorem ipsum",



"number":"5",



"avg":"123.5",



"addr":"2a00:1450:4010:c05::69",



"arr": ["1","2"],



"bool":"false",



"ts":"1984-11-30 22:19:59.789 +0000"



}
```

Result after transformation:

```
{



"content": "Lorem ipsum",



"number": "5",



"avg": "123.5",



"addr": "2a00:1450:4010:c05::69",



"arr": [



"1",



"2"



],



"bool": "false",



"ts": "1984-11-30 22:19:59.789 +0000",



"tsAddYear": "1985-11-30T22:19:59.789000000 +0000",



"negation": "true",



"arrAvg": "1.5",



"isIP": "true",



"avgPlus1": "124.5",



"multi": "50"



}
```


---


## Source: log-processing.md


---
title: Log processing (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-processing
scraped: 2026-02-18T05:54:06.626853
---

# Log processing (Logs Classic)

# Log processing (Logs Classic)

* Explanation
* 3-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Dynatrace Log Monitoring can reshape incoming log data for better understanding, analysis, or further processing based on log processing rules that you create.

Information can be logged in a very wide variety of formats depending on the application or process, operating system or other factors. Log processing offers a central and flexible way of extracting value from those raw log lines.

For example, you can extract numerical values from log line via log processing, turn these into metrics on Dynatrace Platform, and include them in dashboards and problem detection.

Log processing does not affect [DDU](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") consumption of log ingest.

## Log processing rules

Go to **Settings** > **Log Monitoring** > **Processing** to view log processing rules that are in effect, reorder the existing rules, and create new rules. Rules are executed in the order in which they're listed, from top to bottom. This order is critical because a preceding rule may impact the log data that a subsequent rule uses in its definition.

Expand **Details** to examine a rule definition. A log processing rule consists of the following:

* **Rule name**
* **Matcher**
* **Rule definition**

You can turn any rule on or off in the **Active** column.

## Built-in rules

By default, log processing includes many enabled built-in rules responsible for cleaning up or normalizing log data. The name of every built-in rule starts with `[Built-in]`.

You cannot modify these rules directly, but you have the ability to turn them off, copy their definitions, and create new rules with your modifications.

## Add a log processing rule

To create a log processing rule

1. Go to **Settings** > **Log Monitoring** > **Processing**.
2. Select **Add rule**.
3. Provide the name for the log processing rule.
4. Provide a log query in the **Matcher** section.  
   A log search query narrows down the available log data for executing this specific rule. This is the same search query that you have been using in the [log viewer search query](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   Matching based on previous rules is not supported

   The matcher operates on the initial data set before applying any processing rules. Matching records modified by preceding rules is not supported. For example, the modified field in rule 1 and used for matching in rule 2 will contain the original value for that field and will not use the modified field in rule 1.
5. Provide the processing rule definition.  
   The processing rule definition is a log processing instruction about how Dynatrace should transform or modify your log data narrowed down by the **Log query**.

   The rule definition is created using log processing [commands](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-commands "Use log processing commands that reshape your incoming log data for better analysis or further processing."), [functions](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-functions "Use log processing data types that reshape your incoming log data for better analysis or further processing."), and pattern matching that allows you to add, transform, or remove incoming log records. This gives you total control over how your log data is presented to Dynatrace Log Monitoring.
6. Test the log processing rule.  
   You can test the rule definition by either downloading the sample log or providing a fragment of the sample log manually in the **Log sample** text box.

   1. Select a log sample.

      * If you choose to download the sample log, the data used for testing the rule is the matched result of the **Log query**.
      * If you choose to provide a fragment of the log data manually, make sure it's in JSON format. Any textual log data should be inserted into the `content` field of the JSON.
   2. Run the test.

      Select **Test the rule**, and view the result in the **Test result** text box.
7. Select **Save changes**.


---


## Source: lmc-logs-upgrade-to-lma.md


---
title: Upgrade to Log Management and Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma
scraped: 2026-02-18T05:35:37.755560
---

# Upgrade to Log Management and Analytics

# Upgrade to Log Management and Analytics

* How-to guide
* 6-min read
* Updated on Jul 07, 2023

Log Management and Analytics is the latest Dynatrace log monitoring solution. With the introduction of Dynatrace Platform and [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), we encourage you to upgrade to the latest log monitoring offer. If you use Dynatrace SaaS on AWS, your environment will be enabled for Log Management and Analytics powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") with a phased rollout.

For more information about the phased rollout, please reach out to one of your Dynatrace Account team members. You can also reach out directly to Dynatrace product experts via live chat within your Dynatrace environment. Our product experts will get you in touch with your account team members and help with answers to any other questions you might have.

### How can I upgrade from Log Monitoring Classic to Log Management and Analytics?

Once your environment is enabled for activation:

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. In the banner message, select **Go to activation page** and select **Activate Logs powered by Grail**.
3. On the **Activate Grail for log and events** page you can select:

   * **Activate now**
   * **Wait 7 days**
4. Select **Confirm** to verify your choice.

* Only administrative users can activate Log Management and Analytics for the environment.
* Activating Log Management and Analytics is not reversible.

### Upgrade with existing data

You can choose to upgrade with your existing log data.

* If you choose **Wait 7 days** on the **Activate Grail for log and events** page, Grail activation will be postponed for 7 days.
  During that timeframe, your log data will be ingested into both Log Monitoring Classic and Grail. After the 7 day period ends, Grail will be activated automatically and you will begin using Log Management and Analytics with 7 days of existing data.
* If you require log data for a longer period before upgrading, contact a Dynatrace product expert via live chat and request the longer wait time.
* If upgrading with existing data is not important for you, choose **Activate now** on the **Activate Grail for log and events** page and Logs powered by Grail will become active in about 30 seconds.

### What changes after activation

After activating Log Management and Analytics, the following changes take place:

* Ingested log data

  + Ingested log data is saved in the [Grail database](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.").
  + Ingested log data can be routed to buckets with different [retention periods](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.").
* DDU consumption

  + When you activate Log Management and Analytics, you begin consuming DDUs under a [new model with three dimensions: Ingest & Process, Retain, Query](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.").
  + If you choose **Wait 7 days**, you'll still start consuming DDUs for ingestion and retention under the new model immediately and for querying after you run your first DQL query.
* API

  + The [log export API](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs "Fetch log records via the Log Monitoring API v2.") will not be available. We recommend that you stop using [Log GET search](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs "Fetch log records via the Log Monitoring API v2.") and [Log GET aggregate](/docs/dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs "Fetch the aggregated log records via the Log Monitoring API v2."). If you continue using them, they require an [OAuth2 token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.") with the `storage:logs:read` and `storage:buckets:read` scopes.
  + We recommend that you switch from existing APIs to the [Grail Query APIï»¿](https://developer.dynatrace.com/platform-services/services/storage/).
* No support for Management Zones

  + Management Zones configuration will not work with Grail. You have to use buckets and policies for access control. Please check the **User access** section below.

### What does not change after activation

After activating Log Management and Analytics, the following will not change:

* Ingestion configuration, including [OneAgent configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.") and [generic API ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.").
* Log processing, including [processing rules](/docs/analyze-explore-automate/logs/lma-classic-log-processing#lmc-log-processing-rules "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.") with matchers based on the LQL syntax.
* Log metrics, including [metric queries](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.") based on the LQL syntax.
* Log events, including [event queries](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.") based on the LQL syntax.

However we recommend to [convert your LQL matchers](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.") for log processing, metrics and events to highly performing [DQL matcher](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher "Examine specific DQL functions and logical operators for log processing.").

### User access

The user access granting process depends on whether you are a new or existing user.

Management Zones configuration will not work with Grail. You have to use buckets and policies for access control.

* Assign policy to existing users  
  After activating Log Management and Analytics, all users who already had access to log data are assigned a new policy to access the log data in Grail.
* Assign policy to new users

  There are two options for configuring access policies for Grail:

  Assign policy using Account Admin

  In Dynatrace SaaS, only admin users can manage policies (users with account permission `Manage users`).  
  You need to have two policies, **Storage Events Read** and **Storage Logs Read** assigned, bound to a group.

  To check if your policies are assigned

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Go to **Identity & access management** > **Policy management**.
  3. Check if Storage Events Read and Storage Logs Read are present on the policy list.

  If **Storage Events Read** and **Storage Logs Read** are not present on you policy list, you need to add them manually:

  + **Storage Events Read**:  
    **Policy name**: Storage Events Read  
    **Policy description**: Enables reading events from GRAIL  
    **Policy statements**: `ALLOW storage:events:read`
  + **Storage Logs Read**:  
    **Policy name**: Storage Logs Read  
    **Policy description**: Enables reading logs from GRAIL  
    **Policy statements**: `ALLOW storage:logs:read`  
    For details, see [Manage IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt#create "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.").

  To make a policy effective, you need to [bind it to a group](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies#add-or-remove "Working with policies").

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/).
  2. Select **Identity & access management** > **Group management**.  
     For details, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").
  3. Edit the group to which you want to bind the policy (for example, Logs and events). Make sure the users who need to use the Logs and events have this group assigned to their names.
  4. Select the **Policies** tab.

  Assign policy via API

  1. Obtain an [OAuth](/docs/manage/account-management/identity-access-management/oauth "Manage authentication and user permissions for the Account Management API.") token
     Make a POST call with form parameters to SSO.

     + client\_id = [client\_id]
     + client\_secret = [secret]
     + grant\_type = client\_credentials
     + scope = `iam:policies:write iam:policies:read`

     In response, you get an authorization token

     ```
     {



     "scope": "iam:policies:read iam:policies:write",



     "token_type": "Bearer",



     "expires_in": 300,



     "access_token": "123(...)ABC"



     }
     ```
  2. Create a storage events read policy
     Make a POST call to [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")

     Body payload for the policy is:

     ```
     {



     "name": "Storage Events Read",



     "description": "Storage Events Read",



     "tags": [



     ],



     "statementQuery": "ALLOW storage:events:read;"
     ```
  3. Create a storage logs read policy
     Make a POST call to [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")

     Body payload for the policy is:

     ```
     {



     "name": "Storage Logs Read",



     "description": "Storage Logs Read",



     "tags": [



     ]  ,



     "statementQuery": "ALLOW storage:logs:read;"



     }
     ```

  Your newly created policies will be visible on the account level. To check it, go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management** > **Edit Storage Events Read**.


---
