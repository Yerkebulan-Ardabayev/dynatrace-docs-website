---
title: Migrate Dynatrace Operator to a new environment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant
scraped: 2026-02-25T21:33:26.588499
---

# Migrate Dynatrace Operator to a new environment

# Migrate Dynatrace Operator to a new environment

* Latest Dynatrace
* 2-min read
* Updated on Sep 05, 2025

If you're currently monitoring your Kubernetes cluster with a Dynatrace OneAgent rolled out through the Dynatrace Operator and you need to migrate to a different Dynatrace environment, select one of the following options, based on your deployment method.

Kubernetes

OpenShift

1. Delete the existing DynaKube (starting with Dynatrace Operator version 1.3.0, editing `spec.apiUrl` is not allowed).

   ```
   kubectl delete dynakube dynakube -n dynatrace
   ```
2. Delete the existing secret that holds the Dynatrace Operator and Data Ingest tokens for authenticating to the Dynatrace Cluster.

   ```
   kubectl delete secret dynakube -n dynatrace
   ```
3. Create a new secret based on new tokens from your new environment.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the new DynaKube with the updated `spec.apiUrl`.

   ```
   kubectl apply -f dynakube.yaml
   ```
5. Restart your applications.

1. Delete the existing DynaKube (starting with Dynatrace Operator version 1.3.0, editing `spec.apiUrl` is not allowed).

   ```
   oc delete dynakube dynakube -n dynatrace
   ```
2. Delete the existing secret that holds the Dynatrace Operator and Data Ingest tokens for authenticating to the Dynatrace Cluster.

   ```
   oc delete secret dynakube -n dynatrace
   ```
3. Create a new secret based on new tokens from your new environment.

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the new DynaKube with the updated `spec.apiUrl`.

   ```
   oc apply -f dynakube.yaml
   ```
5. Restart your applications.