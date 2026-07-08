---
title: Import Kubernetes API certificates
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/api-certificates
---

# Import Kubernetes API certificates

# Import Kubernetes API certificates

* 1-min read
* Published Jul 28, 2023

Kubernetes API certificates are automatically imported for certification validation checks. Kubernetes automatically creates a `kube-root-ca.crt` configmap in every namespace. This certificate is automatically mounted into every container to `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` and merged into the ActiveGate truststore file using an `initContainer`.
To get this feature, be sure to [update Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#update "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.") if you're using an earlier version.