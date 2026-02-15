---
title: EdgeConnect parameters for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters
scraped: 2026-02-15T21:22:39.813775
---

# EdgeConnect parameters for Dynatrace Operator

# EdgeConnect parameters for Dynatrace Operator

* Latest Dynatrace
* 7-min read
* Updated on Dec 22, 2025

[EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.") enables Dynatrace apps and workflows to interact securely with your systems. EdgeConnect is available as a Docker container and can run in any container runtime environment. This reference guide provides detailed information on how to configure the EdgeConnect [custom resourceï»¿](https://dt-url.net/b60397m) within your Kubernetes environment.

The following table lists the minimum required Dynatrace Operator versions for each EdgeConnect API version.

| DynaKube API version | Minimum Dynatrace Operator version |
| --- | --- |
| `v1alpha2` | 1.3.0+ |
| `v1alpha1` | All versions |

v1alpha1

v1alpha2

## `.spec`

* The `apiServer` and `oauth` parameters are Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiServer` | Location of the hostname of the Dynatrace API to connect to, including your specific environment UUID. Example: `ENVIRONMENT_ID.live.dynatrace.com` | Not applicable | string |
| `annotations` | Adds annotations to the EdgeConnect Pods. | Not applicable | map[string] string |
| `autoUpdate` | Enables automatic restarts of EdgeConnect Pods when a new version becomes available. | `true` | boolean |
| `customPullSecret` | Pull secret for your private registry. | Not applicable | string |
| `env` | Adds environment variables to the EdgeConnect Pods. | Not applicable | []EnvVar |
| `hostRestrictions` | Restricts outgoing HTTP requests from your internal resources to specified hosts. Comma-separated list. | Not applicable | string |
| `imageRef` | Overrides the default image. | Not applicable | Object |
| `labels` | Adds labels to the EdgeConnect Pods. | Not applicable | map[string]string |
| `nodeSelector` | Node selector to control the selection of nodes for the EdgeConnect Pods. | Not applicable | map[string]string |
| `oauth` | EdgeConnect uses the OAuth client to authenticate itself with the Dynatrace platform. | Not applicable | Object |
| `replicas` | Number of replicas for your EdgeConnect. | 1 | int |
| `resources` | Defines resource requests and limits for single Pods. | Not applicable | ResourceRequirements |
| `tolerations` | Specifies tolerations for your EdgeConnect. | Not applicable | []Toleration |
| `topologySpreadConstraints` | Sets topology spread constraints for the EdgeConnect Pods. | Not applicable | []TopologySpreadConstraint |
| `hostPatterns` | Specifies a list of host patterns for requests to be managed by the EdgeConnect instance. This field mandatory and only used when `.spec.oauth.provisioner` is set to `true`. | empty | []string |
| `caCertsRef` | Adds custom root certificate from a ConfigMap. Ensure the certificate is located under the `certs` directory within your ConfigMap. | empty | string |

## `.spec.oauth`

* `resource`, `endpoint`, `clientSecret` parameters are Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `clientSecret` | Name of the secret containing the OAuth client ID/secret. | Not applicable | string |
| `endpoint` | Token endpoint URL of Dynatrace SSO. | Not applicable | string |
| `resource` | URN identifying your account. The URN is provided when creating the OAuth client. | Not applicable | string |
| `provisioner` | Enables EdgeConnect provisioning. This requires the `.spec.hostPatterns` field to be configured. | `false` | bool |

## `.spec.imageRef`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `repository` | Custom EdgeConnect image repository. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Specifies version of the EdgeConnect image to use. | `latest` | string |

## `.spec.proxy`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `authRef` | Secret name containing the username and password used for authentication with the proxy, using the basic HTTP authentication scheme. | empty | string |
| `host` | Server address (hostname or IP address) of the proxy. | empty | string |
| `noProxy` | Represents the `NO_PROXY` or `no_proxy` environment variable. It specifies a string containing comma-separated values specifying hosts that should be excluded from proxying. | empty | string |
| `port` | Port of the proxy. | empty | integer |

## `.spec`

* The `apiServer` and `oauth` parameters are Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiServer` | Location of the hostname of the Dynatrace API to connect to, including your specific environment UUID. Example: `ENVIRONMENT_ID.live.dynatrace.com` | Not applicable | string |
| `annotations` | Adds annotations to the EdgeConnect Pods. | Not applicable | map[string] string |
| `autoUpdate` | Enables automatic restarts of EdgeConnect Pods when a new version becomes available. | `true` | boolean |
| `customPullSecret` | Pull secret for your private registry. | Not applicable | string |
| `env` | Adds environment variables to the EdgeConnect Pods. | Not applicable | []EnvVar |
| `hostRestrictions` | Restricts outgoing HTTP requests from your internal resources to specified hosts. | Not applicable | []string |
| `imageRef` | Overrides the default image. | Not applicable | Object |
| `labels` | Adds labels to the EdgeConnect Pods. | Not applicable | map[string]string |
| `nodeSelector` | Node selector to control the selection of nodes for the EdgeConnect Pods. | Not applicable | map[string]string |
| `oauth` | EdgeConnect uses the OAuth client to authenticate itself with the Dynatrace platform. | Not applicable | Object |
| `replicas` | Number of replicas for your EdgeConnect. | 1 | int |
| `resources` | Defines resource requests and limits for single Pods. | Not applicable | ResourceRequirements |
| `tolerations` | Specifies tolerations for your EdgeConnect. | Not applicable | []Toleration |
| `topologySpreadConstraints` | Sets topology spread constraints for the EdgeConnect Pods. | Not applicable | []TopologySpreadConstraint |
| `hostPatterns` | Specifies a list of host patterns for requests to be managed by the EdgeConnect instance. This field mandatory and only used when `.spec.oauth.provisioner` is set to `true`. | empty | []string |
| `caCertsRef` | Adds custom root certificate from a ConfigMap. Ensure the certificate is located under the `certs` directory within your ConfigMap. | empty | string |
| `serviceAccountName` | Name of Kubernetes `ServiceAccount` that allows EdgeConnect to access the Kubernetes API. | `dynatrace-edgeconnect` | string |
| `kubernetesAutomation` | Configures Kubernetes Automation. | Not applicable | Object |

## `.spec.oauth`

* `resource`, `endpoint`, `clientSecret` parameters are Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `clientSecret` | Name of the secret containing the OAuth client ID/secret. | Not applicable | string |
| `endpoint` | Token endpoint URL of Dynatrace SSO. | Not applicable | string |
| `resource` | URN identifying your account. The URN is provided when creating the OAuth client. | Not applicable | string |
| `provisioner` | Enables EdgeConnect provisioning. This requires the `.spec.hostPatterns` field to be configured. | `false` | bool |

## `.spec.imageRef`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `repository` | Custom EdgeConnect image repository. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Specifies version of the EdgeConnect image to use. | `latest` | string |

## `.spec.proxy`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `authRef` | Secret name containing the username and password used for authentication with the proxy, using the basic HTTP authentication scheme. | empty | string |
| `host` | Server address (hostname or IP address) of the proxy. | empty | string |
| `noProxy` | Represents the `NO_PROXY` or `no_proxy` environment variable. It specifies a string containing comma-separated values specifying hosts that should be excluded from proxying. | empty | string |
| `port` | Port of the proxy. | empty | integer |

## `.spec.kubernetesApiAutomation`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `enabled` | Enables Kubernetes Automation. | `false` | bool |