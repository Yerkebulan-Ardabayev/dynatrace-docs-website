---
title: Manage Dynatrace deployments using GitOps
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops
scraped: 2026-02-17T04:48:36.842745
---

# Manage Dynatrace deployments using GitOps

# Manage Dynatrace deployments using GitOps

* Latest Dynatrace
* 4-min read
* Published Mar 25, 2024

With many companies today adopting GitOps for streamlined Kubernetes deployments, there's a growing interest in applying these practices to Dynatrace components. This guide focuses on deploying Dynatrace Operator with GitOps tools and setting up monitoring efficiently using the DynaKube custom resource (CR), aligning with modern deployment strategies.

## Using ArgoCD

This section discusses deploying Dynatrace Operator and applying a DynaKube CR using [ArgoCDï»¿](https://dt-url.net/hi037z9). Additionally, it outlines options and tips for flexible integration with ArgoCD.

The following three points describe Dynatrace deployment options outlined by the subsections and combinations of them.

1. Individually [Deploy Dynatrace Operator](#deploy-dynatrace-operator) and [Apply DynaKube CR](#apply-dynakube-custom-resource) via ArgoCD Applications
2. Apply ArgoCD's [App of Apps pattern](#applying-the-app-of-apps-pattern)
3. Use [multiple sources](#using-multiple-sources-for-an-argocd-application-beta-feature) for an ArgoCD Application (beta feature)

This guide was developed and tested with ArgoCD version 2.10.3.

### Deploy Dynatrace Operator

The following ArgoCD Application defines Dynatrace Operator deployment using the OCI-based Helm chart from Amazon ECR:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace-operator



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm: {}
```

For deployment customization via Helm values, please refer to ArgoCD's [Helm user guideï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/).

The Application CR can be applied in the following ways:

* Directly via *kubectl*
* By [applying the App of Apps pattern](#applying-the-app-of-apps-pattern)

#### Multi-cluster deployments via ArgoCD ApplicationSet

To use ApplicationSet CRs for multi-cluster deployments, use the Application CR from above as a template and integrate it into an ApplicationSet CR according to [ArgoCD's official documentationï»¿](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).

### Apply DynaKube custom resource

The following ArgoCD Application references a Git repository holding a DynaKube CR under the specified filepath:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynakube



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: <git-reopository-url>



targetRevision: <revision>



path: <path-to-dynakube-dir>
```

Replace the `repoURL`, `targetRevision`, and `path` source fields with meaningful values before applying the Application CR in either of these ways:

* Directly via *kubectl*
* By [applying the App of Apps pattern](#applying-the-app-of-apps-pattern)

For details on DynaKube CR configuration, see the [deployment modes](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") documentation.

### Apply the App of Apps pattern

ArgoCD's [App Of Apps patternï»¿](https://dt-url.net/s963lbz) describes a very common approach in the ArgoCD community enabling automatic cluster bootstrapping. In combination with [Sync Phases and Wavesï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/), the App of Apps pattern provides sequential control over Application synchronization required for deploying Dynatrace Operator before applying a DynaKube CR [1](#fn-1-1-def).

Add the `argocd.argoproj.io/sync-wave` annotation with the respective value to the Application CRs from the above sections as illustrated in the following snippet:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "0"



name: dynatrace-operator



namespace: argocd



spec:



...



---



apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "10"



name: dynakube



namespace: argocd



spec:



...
```

Both Application CRs are meant to be applied via the App of Apps pattern (which requires a parent Application CR).

1

[Creating Custom Resource Definitions (CRDs)ï»¿](https://dt-url.net/8g23lou) installed via the Helm chart can take several seconds, leading to the possibility that the initial application of the DynaKube CR will fail. To circumvent the given race condition, we recommend [configuring ArgoCD for the use of App of Appsï»¿](https://dt-url.net/ci03l8w) by changing the health assessment logic for Applications. Alternatively, automatic retries of synchronizations can be configured.

### Use multiple sources for an ArgoCD Application (beta feature)

Multiple sources for an Application is an ArgoCD beta feature and is subject to change in backwards-incompatible ways, according ArgoCD documentation.

[Multiple sources for an Applicationï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) enables you to use a single ArgoCD Application for deployment of Dynatrace Operator and DynaKube CR.
Additionally, the feature allows Helm value files to be sources from a Git repository other than the Helm chart itself, which was not possible in ArgoCD before.

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



sources:



- repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm:



valueFiles:



- $values/<path-to-dynatrace-operator-values-file>



- repoURL: <git-repository-url>



targetRevision: HEAD



ref: values



- repoURL: <git-repository-url>



targetRevision: HEAD



path: <path-to-dynakube-dir>



syncPolicy:



retry: # sample retry configuration; for details, see footnote below



limit: 5



...



...
```

Before applying, replace all placeholders with meaningful values and configure automatic retries[2](#fn-2-2-def).

2

[Creating Custom Resource Definitions (CRDs)ï»¿](https://dt-url.net/id43ley) installed via the Helm chart can take several seconds, leading to the possibility of the initial application of the DynaKube resource failing. To ensure successful deployment, you need to configure retries by specifying a sync policy.

## Auto-update for Dynatrace Operator

For configuring automatic updates for Dynatrace Operator, see [Auto-update of Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach."), which explains integrating GitOps with dependency automation tools.

## Related topics

* [Auto-update for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach.")