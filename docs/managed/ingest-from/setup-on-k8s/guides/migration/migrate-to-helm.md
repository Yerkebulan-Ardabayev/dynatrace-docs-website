---
title: Migrate from manifests to Helm for Dynatrace Operator installation
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm
---

# Migrate from manifests to Helm for Dynatrace Operator installation

# Migrate from manifests to Helm for Dynatrace Operator installation

* 1-min read
* Published Jul 22, 2024

This guide describes the steps required to migrate from using manifests to Helm. This approach simplifies the deployment process and configuration of Dynatrace Operator.

For the successful migration, you need to completely uninstall and reinstall Dynatrace Operator and its components. Proceed with caution as this will remove and redeploy all components managed by Dynatrace Operator.

To ensure a clean migration:

1. Remove all deployed Dynatrace custom resources such as EdgeConnect and DynaKube.

   ```
   kubectl delete edgeconnect --all



   kubectl delete dynakube --all
   ```
2. [Uninstall Dynatrace Operator via manifests](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#manifest-uninstall "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.").

1. Install Dynatrace Operator via Helm. For more information about install instructions, see [Get started with full observability](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed#helm "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes").

   If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version <desired-version> \



   --create-namespace \



   --namespace dynatrace \



   --atomic
   ```

1. Redeploy Dynatrace custom resources.

   ```
   kubectl apply -f edgeconnect.yaml



   kubectl apply -f dynakube.yaml
   ```