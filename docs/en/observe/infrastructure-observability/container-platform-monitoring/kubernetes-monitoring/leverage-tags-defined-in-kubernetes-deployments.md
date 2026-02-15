---
title: Organize Kubernetes/OpenShift deployments by tags
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments
scraped: 2026-02-15T09:05:33.866229
---

# Organize Kubernetes/OpenShift deployments by tags

# Organize Kubernetes/OpenShift deployments by tags

* How-to guide
* 6-min read
* Updated on Nov 09, 2023

Dynatrace automatically derives tags from your Kubernetes/OpenShift labels. This enables you to automatically organize and filter all your monitored Kubernetes/OpenShift application components.

## Recommendations

We recommend that you define additional metadata at the deployed system. For Kubernetes-based applications, you can simply use [Kubernetes annotationsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/). Dynatrace automatically detects and retrieves all Kubernetes and OpenShift annotations for pods that are monitored with a OneAgent code module. This enables you to use [automated tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and will apply almost immediately without any change to the monitored environment or applications.

In Dynatrace, you can specify [entity ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") for different Kubernetes objects such as Deployments, Pods, Services, or namespaces. We recommend providing ownership information via Kubernetes labels or annotations (you can use either labels or annotations to attach metadata to Kubernetes objects). This ensures that Kubernetes objects have adequate ownership coverage, which is especially important for short-lived entities like Pods. See [Assign ownership teams to monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") for more on the correct format and examples of providing ownership information in key-value pairs in the deployment specification file.

We recommend defining ownership for the Deployment and all other objects for which you want ownership coverage. See also [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage"). You can assign more than one team to a Kubernetes object, provided that the keys in the key-value pairs are unique.

While you can also use tags (manual, automated, and via API) to apply ownership information to Kubernetes objects, this approach has its limitationsâread more in [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

## Automatic detection of Kubernetes properties and annotations

Dynatrace detects Kubernetes properties and annotations. Such [properties and annotations](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") can be used when specifying [automated rule-based tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

Additionally Dynatrace detects the following properties that can be used for [automated rule-based tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") and [property-based process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection#detection-rules "Ways to customize process-group detection").

* Kubernetes base pod name: User-provided name of the pod the container belongs to.
* Kubernetes container: Name of the container that runs the process.
* Kubernetes full pod name: Full name of the pod the container belongs to.
* Kubernetes namespace: Namespace to which the containerized process is assigned.
* Kubernetes pod UID: Unique ID of the related pod.

## Leverage Kubernetes labels in Dynatrace

Kubernetes-based tags are searchable via Dynatrace search. This allows you to easily find and inspect the monitoring results of related processes running in your Kubernetes or OpenShift environment. You can also leverage Kubernetes tags to set up fine-grained [problem alerting profiles](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles."). Kubernetes tags also integrate perfectly with [Dynatrace filters](/docs/observe/application-observability/services-classic/service-flow/service-flow-filtering "Understand how service filtering works and how it can be exploited.").

## Import your labels and annotations

Requirements

For OneAgent to detect Kubernetes annotations and properties, make sure that

* Pods are monitored with a code module
* `automountServiceAccountToken: false` isn't set in your pod's `spec`

Kubernetes

OpenShift

You can specify [Kubernetes labelsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) in the [deployment definitionï»¿](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment) of your application or you can update the labels of your Kubernetes resources using the command `kubectl label`.

You can specify [OpenShift labelsï»¿](https://docs.openshift.com/enterprise/3.0/architecture/core_concepts/pods_and_services.html#labels) in the [Pod object definitionï»¿](https://docs.openshift.com/container-platform/3.10/architecture/core_concepts/pods_and_services.html) of your application or you can update the labels of your OpenShift resources using the command [oc labelï»¿](https://docs.openshift.com/enterprise/3.0/cli_reference/basic_cli_operations.html#application-modification-cli-operations).

Dynatrace automatically detects all labels attached to pods at application deployment time. All you have to do is grant sufficient privileges to the pods that allow for reading the metadata from the Kubernetes REST API endpoint. This way, the OneAgent code modules can read these labels directly from the pod.

### Grant viewer role to service accounts

Kubernetes

OpenShift

In Kubernetes, every pod is associated with a service account which is used to authenticate the pod's requests to the Kubernetes API. If not otherwise specified the pod uses the `default` service account of its namespace.

Every namespace has its own set of service accounts and thus also its own namespace-scoped `default` service account. The labels of each pod for which the service account has view permissions will be imported into Dynatrace automatically.

The following steps show you how to add view privileges to the `default` service account in the `namespace1` namespace. You need to repeat these steps for all service accounts and namespaces you want to enable for Dynatrace.

Create the following `Role` and `RoleBinding`, which allow the `default` service account to view the necessary metadata about your namespace `namespace1` via the Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: namespace1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]



---



kind: RoleBinding



apiVersion: rbac.authorization.k8s.io/v1



metadata:



name: dynatrace-oneagent-metadata-viewer-binding



namespace: namespace1



subjects:



- kind: ServiceAccount



name: default



apiGroup: ""



roleRef:



kind: Role



name: dynatrace-oneagent-metadata-viewer



apiGroup: ""
```

```
kubectl -n namespace1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

In OpenShift, every pod is associated with a service account that's used to authenticate the pod's requests to the Kubernetes API. If not otherwise specified, the pod uses the `default` service account of its OpenShift project.

Each OpenShift project has its own set of service accounts and thus also its own project-scoped `default` service account. The labels of every pod whose service account has view permissions will be imported to Dynatrace automatically.

The following steps show you how to add view privileges to the `default` service account in the `project1` project. You need to repeat these steps for all service accounts and projects you want to enable for Dynatrace.

Create the following `Role`, which will allow a service account to view the necessary metadata about your namespace `project1` via the Kubernetes REST API:

```
# dynatrace-oneagent-metadata-viewer.yaml



kind: Role



apiVersion: rbac.authorization.k8s.io/v1



metadata:



namespace: project1



name: dynatrace-oneagent-metadata-viewer



rules:



- apiGroups: [""]



resources: ["pods"]



verbs: ["get"]
```

```
oc -n project1 create -f dynatrace-oneagent-metadata-viewer.yaml
```

Bind the `Role` to the `default` service account for the `Role` to take effect:

```
oc -n project1 policy add-role-to-user dynatrace-oneagent-metadata-viewer --role-namespace="project1" -z default
```

Alternatively, OpenShift also allows you to bind the `Role` to all service accounts in a project.

```
oc -n project1 policy add-role-to-group dynatrace-oneagent-metadata-viewer --role-namespace="project1" system:serviceaccounts:project1
```

As a result, Kubernetes [processes](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") monitored in your Dynatrace environment will have Kubernetes labels attached as Kubernetes tags. For namespaces, pods, and workloads, Kubernetes tags are not evaluated.

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Assign ownership teams to monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")