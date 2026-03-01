---
title: Auto-update for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update
scraped: 2026-03-01T21:22:13.309318
---

# Auto-update for Dynatrace Operator

# Auto-update for Dynatrace Operator

* Latest Dynatrace
* 2-min read
* Published Mar 25, 2024

Dynatrace Operator manages and auto-updates the components it deploys. To achieve a similar effect for Dynatrace Operator itself, we recommend using GitOps and open-source tools.

## Recommended setup

* Keep the Dynatrace Operator configuration in a Git repository.
* Use [ArgoCDï»¿](https://dt-url.net/hi037z9) to deploy the configuration from the Git repository into the Kubernetes environment.
* Implement [Renovateï»¿](https://dt-url.net/vn237h6) to automatically update the Git repository with the latest Dynatrace Operator configurations.

## Automated update workflow

The workflow outlined below is a direct result of the recommended setup, ensuring that Dynatrace Operator is automatically kept up to date in your Kubernetes environment.

1. ArgoCD deploys the configuration from the Git repository into the Kubernetes environment.
2. Renovate detects a new release of Dynatrace Operator and updates the version in the Git repository.
3. ArgoCD notices the change in the Git repository and updates Dynatrace Operator in the Kubernetes environment accordingly.

### Deploy with ArgoCD

[Argoï»¿](https://dt-url.net/wt4379d) offers a suite of open-source tools for Kubernetes app deployment and management. ArgoCD, a continuous delivery tool, is used to keep the Dynatrace Operator configuration in sync with the Kubernetes cluster.

After you set up ArgoCD in your cluster, create an `ApplicationSet` YAML that specifies the source Helm chart for Dynatrace Operator, the version you want to deploy, and the target environment for the deployment.

ArgoCD ApplicationSet example

```
# For exact syntax refer to the official ArgoCD documentation



apiVersion: argoproj.io/v1alpha1



kind: ApplicationSet



metadata:



name: dynatrace-operator



spec:



generators:



...



template:



...



spec:



...



source:



repoURL: https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable



chart: dynatrace-operator



targetRevision: <version>
```

### Automate updates with Renovate

Renovate automates the updating of dependencies in Git repositories. Integrating Renovate into your workflow ensures that the Dynatrace Operator version specified in your `ApplicationSet` is always up to date. Use the [Renovate guideï»¿](https://dt-url.net/67637gq) for instructions on updating ArgoCD configurations.

## Related topics

* [Manage Dynatrace deployments using GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "How to deploy Dynatrace Operator and DynaKube using GitOps.")