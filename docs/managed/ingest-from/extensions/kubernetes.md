---
title: Run SQL extensions on Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes
---

# Run SQL extensions on Kubernetes

# Run SQL extensions on Kubernetes

* How-to guide
* 5-min read
* Updated on Sep 18, 2026

Create a configuration for your SQL based extension executing on Kubernetes.

## Supported extensions

The following database types are supported, both as official Dynatrace Hub extensions and as custom extensions:

* Oracle
* Microsoft SQL Server
* PostgreSQL
* MySQL / MariaDB
* SAP HANA
* IBM Db2
* Generic JDBC

## Prerequisites

* A DynaKube with SQL extensions enabled (`.spec.extensions.databases`) and all pods in a healthy state. For setup instructions, see [Enable Dynatrace SQL database extensions](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/sql-database-extensions "Enable SQL database monitoring in Kubernetes by configuring Dynatrace Operator to deploy SQL Extension Executor pods that collect metrics from SQL databases inside or outside your cluster.").
* Dynatrace version 1.346+.
* [SQL Extension Executor﻿](https://gallery.ecr.aws/dynatrace/dynatrace-sql-extension-executor) 1.345+.
* [Extension Execution Controller﻿](https://gallery.ecr.aws/dynatrace/dynatrace-eec) 1.345+.
* If you deploy a custom extension signed with your own certificate, configure the signing certificate in DynaKube before deploying the extension.  
  See [Custom extension signing certificates](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/sql-database-extensions#custom-extension-certs "Enable SQL database monitoring in Kubernetes by configuring Dynatrace Operator to deploy SQL Extension Executor pods that collect metrics from SQL databases inside or outside your cluster.") and [`customExtensionCertificates`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extension-execution-controller-template "List the available parameters for setting up Dynatrace Operator on Kubernetes.") in the DynaKube parameters reference.

## Create monitoring configuration

### Via API

Use the [Extensions API](/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/post-monitoring-configuration "Create a monitoring configuration of an extension via the Dynatrace Extensions 2.0 API.") to create a monitoring configuration programmatically.

The following example creates a PostgreSQL monitoring configuration targeting your SQL Extension Executor on Kubernetes:

Single cluster

Cluster name pattern

```
[



{



"scope": "kubernetes",



"value": {



...



"activationContext": "CONTAINER",



"isSingleClusterConfiguration": true,



"kubernetesClusterId": "<cluster-id>",



"executorId": "default",



"sqlPostgresContainer": {



"endpoints": [ ... ]



}



}



}



]
```

```
[



{



"scope": "kubernetes",



"value": {



...



"activationContext": "CONTAINER",



"isSingleClusterConfiguration": false,



"clusterNamePatterns": [



"<cluster-name-pattern>"



],



"executorId": "default",



"sqlPostgresContainer": {



"endpoints": [ ... ]



}



}



}



]
```

The request body fields for Kubernetes monitoring configurations:

| Field | Description |
| --- | --- |
| `scope` | Must be `"kubernetes"` to target an SQL Extension Executor deployment in Kubernetes. |
| `activationContext` | Must be `"CONTAINER"` to run the extension inside an SQL Extension Executor pod. |
| `isSingleClusterConfiguration` | `true` to target one cluster by ID; `false` to match clusters by name pattern. |
| `kubernetesClusterId` | ID of the Kubernetes cluster to monitor. Required when `isSingleClusterConfiguration` is `true`. |
| `clusterNamePatterns` | List of name patterns. All Kubernetes clusters whose name matches any of the provided patterns will be targeted by this configuration. Required when `isSingleClusterConfiguration` is `false`. Use `*` as a wildcard (for example, `*production*`). |
| `executorId` | The executor group ID as defined in `.spec.extensions.databases[].id` in your DynaKube. |
| `sql*Container.endpoints` | Database connection endpoints and authentication parameters. The field name is vendor-specific: `sqlOracleContainer`, `sqlServerContainer`, `sqlPostgresContainer`, `sqlMySqlContainer`, `sqlHanaContainer`, `sqlDb2Container`, or `jdbcContainer` for generic JDBC. |

The full content of the activation JSON varies based on the SQL vendor, extension version, enabled features, and other conditions. To get the most up-to-date schema with all supported fields, use one of the following options:

* Use the [GET extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint to retrieve the full schema for a specific extension version programmatically.
* If you already have a monitoring configuration in your environment, retrieve its payload using the [GET monitoring configuration](/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/get-monitoring-configuration "View the monitoring configuration of an extension via the Dynatrace Extensions 2.0 API.") endpoint.

## Next steps

[#### Kubernetes resource planning

Size the Extension Execution Controller and SQL Extension Executor pods on Kubernetes using recommended resource profiles and scaling strategies.

* Reference

Read this reference](/managed/ingest-from/extensions/kubernetes/resource-planning)[#### Custom JDBC drivers

Provide custom JDBC driver JARs to SQL Extension Executor pods on Kubernetes using a custom container image or a mounted volume.

* How-to guide

Read this guide](/managed/ingest-from/extensions/kubernetes/jdbc-drivers)[#### Configure custom TLS certificates for SQL Extension Executor pods

Provide TLS certificates to SQL Extension Executor pods on Kubernetes by mounting individual certificate files or a pre-built PKCS12 truststore.

* How-to guide

Read this guide](/managed/ingest-from/extensions/kubernetes/tls-certificates)[#### Set up file-based endpoints and credentials

Configure SQL Extension Executor pods to use mounted files for credentials, keeping sensitive data out of Dynatrace and enabling zero-downtime updates.

* How-to guide

Read this guide](/managed/ingest-from/extensions/kubernetes/file-based-config)[#### Monitored pod Kubernetes metadata enrichment

Learn how the Extension Execution Controller enriches extension signals with Kubernetes pod metadata based on the target endpoint's IP address.

* Explanation

Read this explanation](/managed/ingest-from/extensions/kubernetes/pod-metadata-enrichment)[#### Troubleshoot SQL extensions on Kubernetes

Diagnose and resolve common issues with SQL Extension Executor and Extension Execution Controller pods running on Kubernetes.

* Reference

Read this reference](/managed/ingest-from/extensions/kubernetes/troubleshoot)