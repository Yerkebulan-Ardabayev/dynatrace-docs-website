---
title: Migrate from cloud-native full-stack to application monitoring mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring
scraped: 2026-02-15T21:23:44.135577
---

# Migrate from cloud-native full-stack to application monitoring mode

# Migrate from cloud-native full-stack to application monitoring mode

* Latest Dynatrace
* 2-min read
* Published Apr 09, 2024

Dynatrace Operator version 1.0.0+

This guide describes the steps required to migrate your Dynatrace deployment from cloud-native full-stack to the [application monitoring mode](/docs/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.").

## Advantages

To only monitor selected applications on Kubernetes, application monitoring offers a flexible approach with the following benefits:

* The application monitoring mode, similar to the cloud native full stack mode, prevents race conditions that can occur when OneAgent DaemonSet pods and monitored application pods start simultaneously.
* By leveraging Kubernetes concepts such as admission webhooks and CSI driver for Code Module injection, application monitoring mode reduces the required privileges for OneAgent.

### Considerations and implications

* When switching to application monitoring, previously deployed OneAgents will get deactivated and deep monitoring of applications will stop. Consequently, restarting all application pods that require deep monitoring becomes mandatory. Restarting these pods ensures that applications are reinjected, allowing deep monitoring to resume.
* In application monitoring mode, container monitoring rules are ignored. Instead, [label selectors](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") should be employed to precisely manage OneAgent injection.
* Log monitoring requires [additional setup](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.").

## Migrate to application monitoring mode

This section provides all the information needed to perform the migration from cloud-native full-stack to application monitoring mode.

1. Reconfigure (existing) DynaKube for application monitoring mode:

   The following side-by-side comparison outlines how to reconfigure a DynaKube CR from cloud-native full-stack to application monitoring:

   Cloud-native full-stack monitoring

   Application monitoring

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   cloudNativeFullStack:



   args:



   - "--set-host-group=<host-group>"



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   For further information on how to configure DynaKube for application monitoring mode, visit the [deployment guide](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") or [DynaKube parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Alternatively, download the [DynaKube custom resource sampleï»¿](https://dt-url.net/0w036dz) for application monitoring from GitHub and adapt the DynaKube custom resource according to your requirements.
2. Apply the DynaKube custom resource:

   Run the command below to apply the DynaKube custom resource. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f dynakube.yaml
   ```

   This action will lead to the removal of OneAgents in cloud-native full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter.
3. Restart application workloads:

   Restart all application workloads promptly to trigger OneAgent injection and enable deep monitoring minimizing monitoring outages.

## Changes in Kubernetes resources

The migration impacts several Kubernetes resources, altering their functions or introducing new components to support the application monitoring monitoring mode. Key changes include:

Component

cloud-native full-stack

Application monitoring

Dynatrace OneAgent

* Deployed as a DaemonSet
* Collect host metrics on nodes

* Not present

Dynatrace Webhook Server

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

[Dynatrace Operator CSI driver](/docs/ingest-from/setup-on-k8s/how-it-works#csi-driver "In-depth description on how the deployment on Kubernetes works.")

Required

* Deployed as a DaemonSet
* Provides volume storage for OneAgents
* Manages and provides code modules used for pod injection and optimizes storage consumption

Optional

* Deployed as a DaemonSet
* Manages and provides code modules used for pod injection and optimizes storage consumption