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