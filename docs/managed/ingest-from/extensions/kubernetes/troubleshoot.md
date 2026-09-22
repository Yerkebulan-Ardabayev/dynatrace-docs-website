---
title: Troubleshoot SQL extensions on Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes/troubleshoot
---

# Troubleshoot SQL extensions on Kubernetes

# Troubleshoot SQL extensions on Kubernetes

* Reference
* 3-min read
* Published Aug 25, 2026

## Extension stuck in the Pending state

* In ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, verify that at least one Kubernetes cluster name matches the `clusterNamePatterns` configuration.
* Check logs for components in the Kubernetes cluster.

## Extension Execution Controller

The controller pod name is `<dynakube-name>-extension-controller-<pod-num>`.

The following table lists common entries found in controller logs, what they mean, and possible remediation steps.

| Log contains | Explanation | Possible remediation steps |
| --- | --- | --- |
| HttpSession::onRead: async\_read failed: end of stream | No communication with ActiveGate | Check if the ActiveGate service matches the controller pod environment variable `ServerUrl`. Also check whether the ActiveGate pod was recently restarting. These logs are typically temporary and clear once the pod stabilizes. |
| HttpSession::onRead. Request failed HTTP/1.1 503 Service Unavailable | Communication with ActiveGate is established, but is actively refused | Check the health status of ActiveGate |
| Task assignment revision | Communication with Dynatrace Cluster works properly | N/A - connectivity log |
| K8sApiClient: | Logs that show if creating a client to communicate with Kubernetes worked | Check if pod Service Account exists and is attached to cluster RBAC |
| K8sApi: | Logs that show if querying the Kubernetes API for pods worked properly | Check if pod Service Account is configured properly and has proper access rights |

## SQL Extension Executor

The SQL Extension Executor pod name is `<dynakube-name>-executor-<deployment-id>-<pod-id>`.

The following table lists common entries found in SQL Extension Executor logs, what they mean, and possible remediation steps.

| Log contains | Explanation | Possible remediation steps |
| --- | --- | --- |
| Parameters: url=SERVICE\_URL, podid=POD\_UID, idtoken=TOKEN\_PATH, userdata=USERDATA\_PATH | Regular log that shows startup parameters | Check if SERVICE\_URL exists and points to the SQL Extension Executor, POD\_UID is set correctly, and token is properly mounted |
| Error in polling loop .\*: | Unable to connect to controller | Check connectivity between the SQL Extension Executor and the controller |
| New task .\* detected | Executor properly picks up the task from the controller | If the connection to the controller works, check if the SQL Extension Executor pod UID matches the UID from the task reassignment log of the controller |

For issues related to DynaKube configuration and pod startup, see [SQL database extensions troubleshooting](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/sql-database-extensions#troubleshooting "Enable SQL database monitoring in Kubernetes by configuring Dynatrace Operator to deploy SQL Extension Executor pods that collect metrics from SQL databases inside or outside your cluster.").