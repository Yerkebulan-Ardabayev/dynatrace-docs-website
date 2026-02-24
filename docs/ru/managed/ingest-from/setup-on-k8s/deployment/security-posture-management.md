---
title: Kubernetes Security Posture Management
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/security-posture-management
scraped: 2026-02-24T21:31:35.341439
---

# Kubernetes Security Posture Management

# Kubernetes Security Posture Management

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 03, 2025

Dynatrace Kubernetes Security Posture Management enables you to detect, analyze, and monitor misconfigurations, security hardening guidelines, and potential compliance violations across your Kubernetes deployment.

How it works

Dynatrace ingests configuration data from your clusters and workloads into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data."), where it's formatted into [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") according to the [Semantic Dictionary](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.") conventions.

The mechanism is described below.

![Diagram showing how Security Posture Management works on Kubernetes](https://dt-cdn.net/images/kspm-how-it-works-v3-1027-60596036f8.png)

1. KSPM is configured by Dynatrace Operator to collect data

Once you enable Dynatrace Kubernetes Node Configuration Collector in Dynatrace Operator, it's deployed as a DaemonSet on your monitored cluster's nodes to collect cluster and workload configuration data.

2. Data is collected

* Node Configuration Collector collects data from the cluster nodes.

  + Frequency: every minute
* ActiveGate collects data from the Kubernetes API.

  + Frequency: every hour

3. Data is sent to the Dynatrace Cluster

ActiveGate processes all data received from the nodes and Kubernetes API and sends it to the Dynatrace Cluster.

4. Data is mapped

This section has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

The cluster and workload configuration data is mapped as [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") according to the [Semantic Dictionary](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.") and stored in the `default_securityevents_builtin` bucket (for details, see [Built-in Grail buckets](/docs/platform/grail/organize-data#built-in-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.")).

5. Compliance results are ready to use

Once data is ingested into Grail, you can analyze your clusters' security posture and evaluate your compliance with industry standards. For details, see [What's next](#next).

## Prerequisites

Dynatrace version 1.305+ Dynatrace Operator version 1.5.0+ ActiveGate version 1.321+

* [Security Posture Management](/docs/secure/application-security/spm "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") is licensed based on the consumption of [host-hours](/docs/license/capabilities/application-security/security-posture-management "Learn how your consumption of the Dynatrace Security Posture Management (SPM) DPS capability is billed and charged.") and requires the [Dynatrace Platform Subscription (DPS) licensing model](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

  If you're using [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."), or if you're on DPS but don't see the SPM capability enabled in your DPS rate card, please contact a Dynatrace product expert via live chat.
* Review the [Supported compliance standards and technologies](/docs/secure/application-security/spm#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").
* [Set up Kubernetes monitoring](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes").

* Support is limited to compatibility with upstream Kubernetes and available for x86-64 CPU architectures only.
* Amount of replicas of ActiveGate Pods needs to be set to 1 (default).
* If you're using a Dynatrace Operator version earlier than 1.4.0, you need to [upgrade](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#helm "Upgrade and uninstallation procedures for Dynatrace Operator") before you can continue.

## Deploy

See below how to [set up](#setup) and [enable](#enable) Kubernetes Security Posture Management.

### Set up Dynatrace Kubernetes Node Configuration Collector



1. Create secret

If you already created a secret with a token in a previous deployment of Dynatrace Operator, you can skip this step.

1. Create a Dynatrace Operator token.

   For instructions, see [Access tokens and permissions](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
2. Create a secret to hold the access token that will be used by Dynatrace Operator to communicate with the Dynatrace environment.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```

2. Configure DynaKube

1. Create your DynaKube custom resource (minimum `apiVersion: dynatrace.com/v1beta4` is required), making sure to enable the following:

   * Kubernetes Security Posture Management:

     + `spec.kspm: {}`: Enables the KSPM Node Configuration Collector DaemonSet (for details, see [How it works](/docs/secure/application-security/spm#mechanism "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards."))

     KSPM mounts the hosts root filesystem by default. If you want to limit that to specific paths, you can use the field `spec.kspm.mappedHostPaths`. The `spec.kspm.mappedHostPaths` field defines the host paths that are mounted to the container. For a list of suggested paths, see the [Dynatrace Operator repository sampleï»¿](https://dt-url.net/ky03zzm).
   * ActiveGate with Kubernetes monitoring and additional configuration:

     + `spec.activeGate.capabilites`: Must contain `kubernetes-monitoring`

       1. Configuration for ActiveGate versions earlier than 1.311

       For ActiveGate versions earlier than 1.311, make sure to enable the following:

       - `spec.activeGate.capabilites`: Must contain `kubernetes-monitoring`
       - `spec.activeGate.customProperties`: Must contain the following:

         ```
         [kubernetes_monitoring]



         kubernetes_configuration_dataset_pipeline_enabled = true



         kubernetes_configuration_dataset_pipeline_include_node_config = true
         ```
   * Templates with Kubernetes Security Posture Management image:

     ```
     spec:



     ...



     templates:



     kspmNodeConfigurationCollector:



     imageRef:



     repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



     tag: <tag>
     ```

     For more information on tags, visit the [public registry repositoryï»¿](https://dt-url.net/4p03ueu).
   * Tolerations to deploy Node Configuration Collector to the control plane and master nodes

     + `.spec.templates.kspmNodeConfigurationCollector.tolerations`

   For guidelines on how to set properties, see [Add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file").

   For a list of all available parameters, see [DynaKube parameters for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

   **Example DynaKube**:

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   tokens: <secret-token>



   kspm:



   mappedHostPaths:



   - /boot



   - /etc



   - /proc/sys/kernel



   - /sys/fs



   - /sys/kernel/security/apparmor



   - /usr/lib/systemd/system



   - /var/lib



   activeGate:



   capabilities:



   - kubernetes-monitoring



   templates:



   kspmNodeConfigurationCollector:



   imageRef:



   repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



   tag: <tag>



   tolerations:



   - effect: NoSchedule



   key: node-role.kubernetes.io/master



   operator: Exists



   - effect: NoSchedule



   key: node-role.kubernetes.io/control-plane



   operator: Exists
   ```

   1. Example DynaKube for ActiveGate versions earlier than 1.311

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   kspm:



   mappedHostPaths:



   - /boot



   - /etc



   - /proc/sys/kernel



   - /sys/fs



   - /sys/kernel/security/apparmor



   - /usr/lib/systemd/system



   - /var/lib



   activeGate:



   capabilities:



   - kubernetes-monitoring



   customProperties:



   value: |



   [kubernetes_monitoring]



   kubernetes_configuration_dataset_pipeline_enabled = true



   kubernetes_configuration_dataset_pipeline_include_node_config = true



   templates:



   kspmNodeConfigurationCollector:



   imageRef:



   repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



   tag: <tag>
   ```
2. Apply the DynaKube custom resource.

   ```
   kubectl apply -f dynakube.yaml
   ```

3. Verify configuration

1. Check the status of your DynaKube custom resource.

   ```
   kubectl get dks -n dynatrace
   ```

   1. Expected result

   DynaKube status is `Running`.

   ```
   NAME       APIURL                  STATUS    AGE



   dynakube   <environment-api-url>   Running   3m48s
   ```
2. Check the deployment status of the Node Configuration Collector DaemonSet.

   ```
   kubectl get daemonset -n dynatrace -l app.kubernetes.io/component=kspm
   ```

   1. Expected result

   All Pods are in `READY` mode.

   ```
   NAME                             DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE



   dynakube-node-config-collector   3         3         3       3            3           <none>          11m
   ```
3. Check the deployment status of the ActiveGate StatefulSet.

   ```
   kubectl get statefulset -n dynatrace -l app.kubernetes.io/component=activegate
   ```

   1. Expected result

   ActiveGate is in `READY` mode.

   ```
   NAME                  READY   AGE



   dynakube-activegate   1/1     14m
   ```

### Enable Kubernetes Security Posture Management

You can enable Kubernetes Security Posture Management in **Settings** per environment or per cluster. See below for instructions.

Enable KSPM per environment

Enable KSPM per cluster

To enable Kubernetes Security Posture Management for all your monitored clusters

1. Go to **Settings Classic** and select **Application Security** > **Security Posture Management**.
2. Under **Kubernetes**, select **Enable Security Posture Management**.

To enable Kubernetes Security Posture Management for a specific monitored cluster

1. Open **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)").
2. Go to **Clusters** and select the cluster for which you want to enable Security Posture Management.
3. In the upper-right, select , then select **Settings**.
4. In the **Open with** menu, select **Settings Classic**.
5. Select **Security Posture Management**, then select **Enable Security Posture Management**.
6. To verify your configuration, select **Test configuration**.

## What's next

Once you set up Kubernetes Security Posture Management, you can use

* [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.") to analyze your clusters' security posture and evaluate your compliance with industry standards
* [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") for further insights
* [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to share finding reports with stakeholders

## Limitations

Up to 100 nodes and 3,000 pods per Kubernetes cluster can be covered by Kubernetes Security Posture Management.

## Further resources

* For a use case scenario, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").
* For a list of frequently asked questions on Kubernetes Security Posture Management, see [FAQ](/docs/secure/application-security/spm#faq "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").
* For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").
* For an overview of security data usage, see [Security data on Grail](/docs/secure/threat-observability/concepts#security-data "Basic concepts related to Threat Observability").

## Related topics

* [Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")