---
title: Deploy Dynatrace alongside Istio
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment
scraped: 2026-02-17T04:49:19.800029
---

# Deploy Dynatrace alongside Istio

# Deploy Dynatrace alongside Istio

* Latest Dynatrace
* 10-min read
* Updated on Oct 22, 2025

This guide explains how Dynatrace components can be deployed alongside Istio. A Dynatrace deployment on Kubernetes contains several components that need to communicate with each other, with the Dynatrace cluster and other external resources.

For more information on communication of Dynatrace Operator and its managed components, see the [network traffic](/docs/ingest-from/setup-on-k8s/reference/network "Network traffic requirements for the Dynatrace Operator components in a Kubernetes cluster.") reference page.

## Limitations

* Istio injection into the Dynatrace Operator namespace is not supported.
* Istio spin-offs are currently not supported (for example, Maistra or OpenShift Service Mesh).
* Istio East-West (sidecar combined with ambient) deployment is not supported.

## Setup considerations

This guide covers two predefined configurations of Istio, chosen for their simplicity and common use cases. While Istio offers extensive customization options, these configurations serve as a starting point. This section explains the configuration scenarios and provides guidance on selecting the right Dynatrace setup that best suits your needs. Note that Dynatrace does not impose any limitations on how you configure Istio.

* **Default Istio configuration** Recommended  
  This represents the default deployment of Istio, meaning no special mesh configuration. It's basically the result of following the official [Istio installation guideï»¿](https://dt-url.net/hm03u3r).
  This means Istio is installed either via Helm or `istioctl` in sidecar mode with the CNI node agent.

  Follow the [setup guide for the default Istio configuration](#setup-guide-for-default-istio-configuration) if Istio is deployed accordingly.
* **Secure Istio configuration**  
  This represents a "secure" configuration of Istio. However, this does not mean that we consider this the best practice for security configuration in Istio or that this should be seen as a guide for securing Istio. This setup is based on settings that are most likely to influence the deployed Dynatrace components and their connections. This scenario assumes that Istio is deployed with strict mTLS and `outboundTrafficPolicy` set to `REGISTRY_ONLY`. These options severely limit the incoming and outgoing connections for workloads in the mesh.

  Choose this configuration if any point below applies:

  + If you have enabled mTLS in strict mode.
  + If you have an `outboundTrafficPolicy` set to `REGISTRY_ONLY`.

  If none of the points above apply, choose [Default Istio configuration](#setup-guide-for-default-istio-configuration).  
  Follow the [setup guide for the secure Istio configuration](#setup-guide-for-secure-istio-configuration) if Istio is deployed accordingly.

### Other deployment considerations

Disable injection of CNI pods

#### Disable injection of CNI pods

This is relevant to you if all of the following applies to your deployment:

* Not supported Dynatrace Operator is deployed inside the mesh.
* Istio is deployed using sidecars.
* Istio is configured to use the CNI component.
* You have not configured any namespace selector in the DynaKube that would exclude the `istio-system` namespace.

In all scenarios, you should exclude the Istio CNI pods from being injected by the Dynatrace Operator. Otherwise, when adding a new node to the cluster, it is possible that a deadlock situation will occur.

Both the CSI driver and Istio's CNI agent are DeamonSets, and will therefore be deployed on any (new) node in the cluster.

* The CSI driver pod will be injected by Istio with an init container that waits for the correct setup of the redirection rules needed for the proxy sidecar to work.
* The CNI pod will be injected by Dynatrace to include the required OneAgent binaries for instrumentation that are provided via a volume provisioned by the CSI driver on that Node.

This leads to a situation where both pods cannot start:

* The CNI pod is waiting for the CSI driver to become ready to provide the volume.
* The CSI pod is waiting for the CNI agent to provide the redirections for the proxy.

Also all other workloads that are target of either the Istio or Dynatrace injection and get scheduled on that Node will be affected and won't be able to start.

The easiest way to exclude the CNI pods from the injection by the Dynatrace Operator is to add the annotation `oneagent.dynatrace.com/inject: "false"`. For example, for a Helm deployment of Istio, add the following to the values of the `cni` chart:

```
cni:



podAnnotations:



oneagent.dynatrace.com/inject: "false"
```

Native sidecar support

#### Native sidecar support

Istio 1.28 deployed on a compatible Kubernetes cluster (>=1.29) will use native sidecar containers. This new type of sidecar container is currently not supported by Dynatrace Operator. Disable native sidecars in your Istio deployment by adding the following environment variable to the pilot deployment.

Example values for the Istio helm chart:

```
pilot:



...



env:



ENABLE_NATIVE_SIDECARS: false



...
```

## Setup guide for default Istio configuration

Because Dynatrace supports Istio in the default configuration, you only need to enable the `enableIstio` parameter in the [DynaKube](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."). However, you don't need to set this parameter if you don't plan to use a restrictive `outboundTrafficPolicy`.

When this parameter is enabled, Dynatrace Operator will deploy `ServiceEntries` and `VirtualServices` to enable communication from inside the mesh to all relevant Dynatrace components and the Dynatrace environment. The `ServiceEntries` and `VirtualServices` work regardless of whether Dynatrace Operator's namespace itself is part of the mesh (if no `discoveryfilter` is set in Istio).

This enables all workloads and OneAgents to connect to the ActiveGate instance and all required connections to the Dynatrace environment. Therefore, all Dynatrace features are expected to work.

`ServiceEntries` result in additional DNS queries executed by each sidecar proxy. This can put additional load on your DNS server.

To minimize the number of URLs, and therefore DNS queries, make sure the network zones in your Dynatrace environment are configured correctly. For a detailed setup description, see [Kubernetes network zone docs](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones#kubernetes-cluster-with-restricted-egress "Set up and use network zones in Kubernetes environments with the Dynatrace Operator.").

If this is not possible or sufficient in your environment, see [Istio DNS proxyingï»¿](https://dt-url.net/ab23uvy) for another possible mitigation.

### How `enableIstio` works

The `enableIstio` attribute is a convenience feature that automatically creates `ServiceEntries` and `VirtualServices` for connection endpoints required by:

* Dynatrace Operator: Uses `apiUrl` defined in DynaKube.
* ActiveGate: Uses the `/v1/deployment/installer/gateway/connectioninfo` endpoint.
* OneAgent injected into user containers: Uses the `/v1/deployment/installer/agent/connectioninfo`, which respects the `networkZone` attribute for routing.

Note that `enableIstio` attribute will not consider pre-existing `ServiceEntries` and `VirtualServices`. Using this attribute prematurely might lead to conflicts in Istio configurations. In complex setups, manual configuration may yield better outcomes.

Changes to the `enableIstio` attribute require you to remove and reapply your DynaKube for the update to take effect.

Manual configuration

Manual configuration of `ServiceEntries` and `VirtualServices` may be required in the following cases:

#### ActiveGate

* **Requirement**: Necessary if the ActiveGate pod is part of the mesh.
* **Configuration**: Manually configure `ServiceEntries` and `VirtualServices` based on the output of the `/v1/deployment/installer/gateway/connectioninfo` endpoint.

#### `cloudNativeFullstack` and `applicationMonitoring`

* **Requirement**: Necessary if injected user applications are part of the mesh.
* **Configuration**: Manually configure `ServiceEntries` and `VirtualServices` based on the output of the `/v1/deployment/installer/agent/connectioninfo` endpoint.

## Setup guide for secure Istio configuration

In such a restricted environment, and depending on your required Dynatrace features and other considerations, it might be necessary to create a few additional configuration rules for Istio. There are a few things to consider regarding the Dynatrace components when deciding how to deploy Dynatrace Operator.

* Even if routing is enabled on the ActiveGate, OneAgents will fall back to directly connecting to the Dynatrace environment if the ActiveGate is not reachable (for example because it's inside the mesh). That means no monitoring data is lost if some OneAgents can't connect to the ActiveGate because of the chosen deployment strategy.
* The monitoring modes `classicFullStack` or `cloudNativeFullStack` create pods with host networking enabled. That means those pods can never be part of the mesh, as Istio does not support pods with host networking. For `classicFullStack`, those pods handle all application metrics, while for `cloudNativeFullStack`, only host monitoring is affected.
* Some features of the ActiveGate might require direct connections to pods (for example, metric scraping). With mTLS enabled in Istio, direct connections to pod IPs are not possible. For a workaround for metric scraping, see [Istio metric merging](#metric-scraping-using-istio-metric-merging).

### Deployment outside the mesh

In this scenario, the least complex deployment is outside the mesh. You still have to enable the `enableIstio` parameter in the DynaKube. The possible downsides of this deployment might include:

* Communication from inside the mesh to the ActiveGate will not be secured by mTLS. However, the communication is still encrypted via HTTPS.
* The ActiveGate is not able to connect to any pod or service inside the mesh. If metric scraping is your only concern, see the [Metric scraping using Istio metric merging](#metric-scraping-using-istio-metric-merging) workaround (not applicable for Istio ambient).

Depending on whether most of your monitored workloads are part of the mesh or most of your targets for metric scraping are inside the mesh, deploying only the ActiveGate inside the mesh can be a more suitable option.

### ActiveGate deployment inside the mesh

The most compatible deployment option is to deploy only the ActiveGate inside the mesh. This deployment option makes the most sense if most of your monitored workloads are also part of the mesh or if you need the ActiveGate to directly connect to pods inside the mesh (for example, for Prometheus scraping).

1. Make sure that the Dynatrace Operator namespace is not labeled for Istio injection (`istio-injection` or `istio.io/dataplane-mode` label is not set).
2. Label the ActiveGate pods for Istio by adding the following to your DynaKube:

   Sidecar

   Ambient

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: your-dynakube-name



   spec:



   enableIstio: true



   activeGate:



   labels:



   sidecar.istio.io/inject: "true"
   ```

   Restart your ActiveGate pods to trigger the injection.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: your-dynakube-name



   spec:



   enableIstio: true



   activeGate:



   labels:



   istio.io/dataplane-mode: "ambient"
   ```
3. Optional You can enable communication from OneAgents outside the mesh to the ActiveGate by deploying the following `PeerAuthentication` resource:

   ```
   apiVersion: security.istio.io/v1



   kind: PeerAuthentication



   metadata:



   name: ag-no-mtls # <yourname>



   namespace: dynatrace-operator # <operator namespace>



   spec:



   mtls:



   mode: PERMISSIVE



   selector:



   matchLabels:



   app.kubernetes.io/managed-by: dynatrace-operator



   app.kubernetes.io/name: activegate
   ```

All communication to the ActiveGate will still be encrypted using HTTPS.

Configure Dynatrace Operator CSI driver with Istio in registry-only mode and custom codeModulesImage

### Configure Dynatrace Operator CSI driver with Istio in registry-only mode

When using Istio configured to `REGISTRY_ONLY` mode with the `codeModulesImage` field for CSI driver, you need to apply additional configuration to ensure proper communication with the image registry.

#### Prerequisites

* Istio is installed and configured in `REGISTRY_ONLY` mode.
* Not supported Dynatrace Operator CSI driver is injected with Istio.
* `codeModulesImage` field is specified in the CSI driver configuration.

#### Configure `ServiceEntry` for CSI driver

1. Create a `ServiceEntry`.

   The `ServiceEntry` configuration allows the Dynatrace Operator CSI driver to communicate with the specified image registry. Without this configuration, the image pull process will fail. See an example of `ServiceEntry` for `docker.io` below.

   ```
   apiVersion: networking.istio.io/v1



   kind: ServiceEntry



   metadata:



   name: codemodules-docker-io



   namespace: dynatrace



   spec:



   hosts:



   - index.docker.io



   - auth.docker.io



   - production.cloudflare.docker.com



   location: MESH_EXTERNAL



   ports:



   - name: https-443



   number: 443



   protocol: HTTPS



   resolution: DNS
   ```
2. Apply the `ServiceEntry`.

   Save and apply the above configuration to a file.

   ```
   kubectl apply -f serviceentry.yaml
   ```

## Metric scraping using Istio metric merging

[Dynatrace metric scraping](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.") is done via the ActiveGate and configured via annotations. This results in the ActiveGate connecting directly to the pods on the configured endpoint to scrape the metrics. As stated earlier, this direct connection does not work with strict mTLS.

Istio ambient mode does not support metric merging as it requires a sidecar proxy. However, in ambient mode it's possible for the ActiveGate to directly connect to the pod IPs and scrape the configured targets. Depending on your mTLS policy, this might only be possible for pods inside the mesh if the ActiveGate is also part of the mesh.

Istio provides a feature called [metric mergingï»¿](https://dt-url.net/5y43ufx) that uses the (widely adopted) `prometheus.io/...` annotations to configure an additional endpoint in the sidecar proxy that serves Istio and Envoy metrics as well as the application metrics defined by the annotations. This newly created endpoint is excepted from mTLS and therefore reachable from outside the mesh despite having mTLS in strict mode.

You can now point the Dynatrace annotations to this endpoint to scrape metrics of Istio and the application. If you don't want to scrape the additional Istio and Envoy metrics, you can exclude them by using the `metrics.dynatrace.com/filter` annotation and excluding `istio_*` and `envoy_*` metrics.

This way, an ActiveGate outside (or inside) the mesh can scrape the metrics from pods inside the mesh.

Example of all required annotations:

```
apiVersion: v1



kind: Pod



metadata:



annotations:



...



metrics.dynatrace.com/path: /stats/prometheus # Endpoint created by Istio



metrics.dynatrace.com/port: "15020" # Port of the Envoy sidecar



metrics.dynatrace.com/scrape: "true"



prometheus.io/path: /metrics # Metric endpoint of the application



prometheus.io/port: "8080" # Metric port of the application



prometheus.io/scrape: "true"



...
```

Keep in mind that Istio will rewrite the `prometheus.io/...` annotations to the generated endpoint and port when applying the above pod. That means that the resulting pod in the cluster will not match the applied YAML.

## Troubleshooting

Istio service registry

You can get all services known to Istio (a service registry) by executing the following command inside the `pilot` container of the `istiod` pod.

```
curl localhost:8080/debug/registryz
```

This dumps all known services as JSON. It should contain entries for the Dynatrace tenant and ActiveGate in the cluster.

If not, check if `enableIstio` is set to `true` in the DynaKube.

## Related topics

* [Configure OpenTelemetry tracing with Istio](/docs/ingest-from/opentelemetry/integrations/istio "Learn how to configure Istio on Kubernetes to deploy pre-configured proxy services for OpenTelemetry tracing.")