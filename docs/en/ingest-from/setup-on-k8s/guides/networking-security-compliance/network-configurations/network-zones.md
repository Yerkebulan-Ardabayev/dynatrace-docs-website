---
title: Using network zones in Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones
scraped: 2026-02-21T21:22:56.556371
---

# Using network zones in Kubernetes

# Using network zones in Kubernetes

* Latest Dynatrace
* 5-min read
* Published Mar 25, 2024

This page describes how to effectively use network zones within Kubernetes environments, emphasizing their configuration through DynaKube.

To ensure a seamless setup process, we strongly advise you to thoroughly review this guide before making any configuration efforts. By doing so, network admins can gain a solid understanding of the prerequisites and steps involved, ensuring a successful deployment.

We assume a foundational understanding of network zones. See the following links for background information:

* [Network zones introduction](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") and [basic information](/docs/manage/network-zones/network-zones-basic-info#activate "Learn how to get started with network zones.")
* [OneAgent](/docs/manage/network-zones/oneagent-connectivity "Find out how network zones prioritize ActiveGates for OneAgent connectivity.") and [ActiveGate](/docs/manage/network-zones/activegate-connectivity "Find out how network zones prioritize ActiveGates for Environment ActiveGate connectivity.") connectivity

## Network zones in Kubernetes environments

Network zones are instrumental in managing and directing traffic flow among Dynatrace components, ensuring efficient communication within the network, whether in Kubernetes environments or traditional setups. By leveraging network zones, network admins can optimize traffic flow and accommodate environments with stringent network restrictions, such as limited egress capabilities.

Network zones for Dynatrace components deployed on Kubernetes can easily be configured via the DynaKube custom resource, enabling tailored and effective network management.

## Set up network zones

This section categorizes setups into two distinct scenarios based on their characteristics:

* [Kubernetes cluster with non-restricted egress](#kubernetes-cluster-with-non-restricted-egress)
* [Kubernetes cluster with restricted egress](#kubernetes-cluster-with-restricted-egress)

### Kubernetes cluster with non-restricted egress

In Kubernetes clusters without egress restrictions, the main purposes of network zones are to:

* Efficiently direct traffic to prevent unnecessary global routing
* Filter unreachable endpoints

The adoption of network zones is therefore widely recommended for optimal traffic management of Dynatrace components.

1. Configure a network zone by setting the `networkZone` field and make sure an ActiveGate is rolled out as part of the DynaKube configuration. The specified network zone will be automatically applied to rolled out ActiveGates and OneAgents by the Dynatrace Operator.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   ...



   spec:



   ...



   networkZone: my-networkzone # Configures network zone



   oneAgent:



   ...



   activeGate: # Ensures ActiveGate rollout



   capabilities:



   - routing



   - kubernetes-monitoring



   ...
   ```
2. Apply the DynaKube CR to the Kubernetes API.

   ```
   kubectl apply -f dynakube.yaml
   ```

   After applying, the Dynatrace Operator will roll out Dynatrace components according the DynaKube configuration. As part of the rollout, ActiveGates and OneAgents receive available endpoints according to the specified network zone (with fallback mode *Any ActiveGate*) and can start communicating independently of each other's rollout status.

   In this scenario, it is not required to manually create the network zone before applying the DynaKube custom resource, as network egress is not restricted. Creation of the network zone happens implicitly when the ActiveGate registers itself with the Dynatrace cluster, with *Any ActiveGate* configured as [fallback mode](/docs/manage/network-zones/network-zones-basic-info#fallback-mode "Learn how to get started with network zones.").

### Kubernetes cluster with restricted egress

In Kubernetes clusters that enforce restricted egress, typically, only whitelisted components are permitted to interact with external networks. For Dynatrace, the ActiveGate is designed for this use case and serves as this crucial gateway component able to centralize all outbound communications towards the Dynatrace Cluster.

Given that all Dynatrace components must communicate exclusively through the whitelisted ActiveGate, it is imperative that the network zone is configured to support this requirement. Hence, the network zone needs to ensure that only ActiveGates within the specified network zone are provided for communication, without resorting to any fallback options. To achieve that, the network zone must be created upfront with *None* as the fallback mode to prevent a lockdown of Dynatrace monitoring components.

Dynatrace Operator version 0.14.0+ postpones OneAgent rollout and injection until at least one ActiveGate becomes available. Once an ActiveGate is available, OneAgents are deployed and OneAgent injection is performed. Application pods that have not been injected due to the postponement need to be manually restarted.

Additionally, it may be necessary to also [configure a proxy](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#configure-proxy "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.") to facilitate controlled network access in Kubernetes clusters with restricted egress.

1. Run the following command to create a network zone in fallback mode *None* using the [Dynatrace API](/docs/dynatrace-api/environment-api/network-zones/put-network-zone "Update a network zone via the Dynatrace API.").

   ```
   curl -X PUT https://<environment-fqdn>/api/v2/networkZones/<network-zone-name> \



   -H "Authorization: Api-Token <api-token>" \



   -H "Content-Type: application/json" \



   -d "{ \"fallbackMode\": \"NONE\" }"
   ```

   The API token must have the `networkZones.write` permission assigned.
2. Configure a network zone by setting the `networkZone` field and make sure an ActiveGate is rolled out as part of the DynaKube configuration.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   ...



   spec:



   ...



   networkZone: my-networkzone # Configures network zone



   oneAgent:



   ...



   activeGate: # Ensures ActiveGate rollout



   capabilities:



   - routing



   - kubernetes-monitoring



   ...
   ```
3. Apply the DynaKube CR to the Kubernetes API.

   ```
   kubectl apply -f dynakube.yaml
   ```

   After deploying, Dynatrace Operator performs the following steps.

   1. Deploy ActiveGates.

   2. Poll Dynatrace cluster for available ActiveGates in a certain interval until an ActiveGate becomes available.
   3. Deploy OneAgents with available communication endpoints.
   4. Perform OneAgent injection into application pods.

   Application pods that have not been injected due to the postponement need to be manually restarted.

   Troubleshooting OneAgent injection of application pods

   If application pods start before an ActiveGate becomes available, Dynatrace Operator skips OneAgent injection. This way, startup of applications won't be delayed, but applications will not be deeply monitored.

   The following reasons can lead to skipped OneAgent injection:

   * ActiveGates are still starting and none is yet registered with the Dynatrace cluster.
   * ActiveGates are crashing due to misconfiguration.

   Dynatrace Operator adds the following annotations to every pod in case of skipped OneAgent injection:

   ```
   oneagent.dynatrace.com/injected: "false"



   oneagent.dynatrace.com/reason: "EmptyConnectionInfo"
   ```

   Alternatively, Dynatrace Operator logs can be analyzed for skipped OneAgent injections.

## Related topics

* [Get started with network zones](/docs/manage/network-zones/network-zones-basic-info "Learn how to get started with network zones.")
* [Network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.")