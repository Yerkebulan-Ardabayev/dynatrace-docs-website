---
title: "Cluster API v2"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2
updated: 2026-02-09
---

# Cluster API v2

# Cluster API v2

* Published Feb 10, 2020

Dynatrace Managed exposes cluster-wide functionality via REST endpoints. This interactive documentation also acts as a REST client you can use to interact with Dynatrace Managed clusters.

To access the Cluster API

1. Open the Cluster Management Console.
2. Open the User menu by clicking the User icon in the upper-right corner.
3. Select **Cluster API v2**.

### Environments

[List all existing environments](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/list-managed-environments "Use the Dynatrace API to get a list of all existing environments.")

[Create a new environment](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/create-managed-environment "Use the Dynatrace API to create a new environment.")

[List properties for specific environment](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/list-specific-managed-environment "Use the Dynatrace API to get the properties of a specified environment.")

[Update specific environment](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/update-specific-managed-environment "Use the Dynatrace API to update a specific environment.")

[Delete specific environment](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/delete-specific-managed-environment "Use the Dynatrace API to delete a specific environment.")

### Synthetic locations and nodes

[List all cluster private Synthetic locations](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations "List all synthetic locations via the Synthetic v2 API on Dynatrace Managed.")

[Create new private Synthetic locations](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location "Create a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.")

[Get properties of specified cluster locations](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location "Retrieve parameters of a Synthetic location via the Synthetic API v2 in Dynatrace Managed.")

[Update specified private Synthetic cluster location](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Update a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.")

[Delete specified private Synthetic cluster location](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/delete-a-location "Delete a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.")

[List all Synthetic cluster nodes](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all "List all Synthetic nodes via the Synthetic API v2 in Dynatrace Managed.")

[List properties of specified Synthetic cluster nodes](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-node "Retrieve parameters of a Synthetic node via the Synthetic API v2 in Dynatrace Managed.")

### Tokens

[List available cluster tokens](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-tokens "Learn how to use the Dynatrace API to get a list of available Dynatrace Cluster API authentication tokens.")

[Create new cluster token](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens "Learn how to create new Dynatrace Cluster token using API.")

[Update cluster token](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/update-cluster-token "Learn how to update Dynatrace Cluster token using API.")

[Delete cluster token](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/delete-cluster-token "Learn how to delete Dynatrace Cluster token using API.")

[List cluster token metadata with request](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-req "Learn how to list token metadata using token value in request and API.")

[List cluster token metadata with ID](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-para "Learn how to list token metadata using token ID and API.")

### User management

[Get cluster user sessions configuration](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions-configuration "Learn how to get user sessions configuration via Cluster API.")

[Update cluster user sessions configuration](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration "Learn how to update Dynatrace Cluster user sessions configuration using API.")

[Get cluster user sessions](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions "Learn how to get user sessions via Cluster API.")

[Delete user sessions of a given user](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/delete-cluster-user-session "Learn how to delete Dynatrace Cluster user sessions of a given user using API.")

### Remote access

[Get all cluster access requests](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-all-cluster-access-requests "Learn how to get all cluster access requests.")

[Grant remote access permission](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/post-remote-access-permission "Learn how to grant permission for remote access using the Cluster API v2.")

[Get Cluster access request](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-cluster-access-request "Learn how to get cluster access request.")

[Change state of access request](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/put-change-access-request-state "Learn how to change the state of an access request using the Cluster API v2.")

### License

[Export license data](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/export-license-data/get-export-license-data "Learn how to export aggregated hourly license usage as a ZIP file.")

### Log Monitoring

[Get Log Monitoring status](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/get-log-monitoring-status "Learn how to get Log Monitoring status in Managed deployments using API.")

[Update log events per cluster for Log Monitoring](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring "Learn how to update the total log events per cluster limit based on the cluster resources size using API.")
