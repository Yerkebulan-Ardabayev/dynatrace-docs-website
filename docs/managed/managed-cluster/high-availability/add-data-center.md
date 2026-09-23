---
title: Add a data center
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/add-data-center
---

# Add a data center

# Add a data center

* How-to guide
* 12-min read
* Updated on Sep 18, 2026

To extend your Managed Cluster into a second data center for a Premium High Availability (PHA) deployment, follow the steps below.

A PHA deployment is globally distributed. You add a redundant set of nodes that mirrors your original Managed Cluster, and the two node sets typically sit in different data centers.

This procedure uses these terms:

* **DC-1**: Data center that holds the initial Managed Cluster
* **DC-2**: Additional data center for the PHA deployment
* **seed node**: Any node in **DC-1** that you use to run the installation tasks and distribute the configuration

The procedure migrates and replicates each Dynatrace Managed component individually to prepare for cross-data center data replication.
See [Overview of Dynatrace Managed components](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

## Before you begin

* The **DC-1** Managed Cluster must have backup turned off before you start the migration procedure. Create a fresh Managed Cluster backup, then turn off backup shortly before you deploy the additional data center.
* The **DC-1** Managed Cluster must have automatic update turned off before you start the migration procedure. Do not upgrade the Managed Cluster during migration. See [Automatic update](/managed/managed-cluster/operation/update-cluster#automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update."). Contact a Dynatrace product expert via live chat if the automatic update option is turned off.
* Make sure the machines for the **DC-2** Managed Cluster are ready.

Recommendation

**DC-2** replicates the data of **DC-1**, so designate the same number of nodes with the same hardware, including disk storage. Set up Network Time Protocol on every node in **DC-1** and **DC-2**, so all nodes stay time-synchronized.

* PHA deployment requires at least three nodes in **DC-1** and three corresponding nodes in **DC-2**.
* All nodes in both data centers must be able to communicate with each other.

To check whether a node in **DC-1** is reachable from **DC-2**, run this health-check REST call from a host in **DC-2**:

```
curl -k https://<DC-1-node-IP>/rest/health
```

Replace `<DC-1-node-IP>` with the IP address of any node in **DC-1**. The response contains `"RUNNING"` when the connection succeeds.

## Prepare for the migration

Ensure that your system meets the specified [hardware and operating system requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

### Gather information

The REST API calls in this procedure use variables. Collect this information before you start:

* `<seed-node-ip>`: IP address of the **seed node** in **DC-1**
* `<nodes-ips>`: List of IPv4 addresses of the new nodes in **DC-2**.  
  Example: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>`: Valid Cluster API token, which requires the ServiceProviderAPI scope.  
  Generate it in the **Cluster Management Console**. See [Cluster API - Authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>`: Directory where Dynatrace Managed is installed on the seed node.  
  The default installation directory is `/opt/dynatrace-managed`.
* `<datacenter-1>`: **DC-1** name, which must match the **Cassandra DC** name.  
  The default Cassandra DC name is `datacenter1`.

Get the DC name

To get the DC name, run this command on the **seed node** before you start migration:

```
sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status
```

The response includes the **DC-1** name. The example shows a DC named `datacenter1`:

```
Datacenter: datacenter1



=======================



Status=Up/Down



|/ State=Normal/Leaving/Joining/Moving



--  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



UN  10.176.42.20   65.54 GB   256          100.0%            f053dd8d-ecf3-7834-b099-68542439817b  rack1



UN  10.176.42.244  65.47 GB   256          100.0%            2aa7e790-a423-9273-88f9-45bcd158dd6e  rack1



UN  10.176.42.168  65.47 GB   256          100.0%            48543bca-41f5-26d3-b2fd-6cfdf5c0f3b2  rack1
```

* `<datacenter-2>`: **DC-2** name, which can be any string that begins and ends with an alphanumeric character and is no longer than 80 characters. Underscores and dashes are allowed within the name. Example: `dc-us-east-2`.

### Set variables

To streamline the numerous REST API calls during the deployment, set environment variables on every node in **DC-1** and **DC-2**.

```
SEED_IP=<seed-node-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=$(echo '[<nodes-ips>]')



API_TOKEN=<api-token>



DC1_NAME=<datacenter-1>



DC2_NAME=<datacenter-2>
```

For example:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=$(echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]')



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



DC1_NAME=datacenter1



DC2_NAME=dc-us-east-2
```

## Review network zone setup

Before you migrate to PHA, review your network zone setup for OneAgents and Environment ActiveGates that use the `default` network zone.

When you migrate and restart a Cluster node, Dynatrace changes the Embedded ActiveGate network zone from `default` to the node's data center name. The network zone reassignment can reroute OneAgent and Environment ActiveGate traffic that currently uses the `default` network zone.

Although PHA optimizes traffic between the data centers, ActiveGates should send data to both data centers for redundancy. Configure OneAgents and ActiveGates to prefer specific network zones without losing their ability to fail over to another part of the Managed Cluster during a data center outage. You can also use load balancers for this purpose.

For active-passive application deployments, keep ActiveGates active in the passive portions of the deployment so the Dynatrace infrastructure fails over without reconfiguration or rediscovery.

## Install the second data center

Complete these steps in order.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Update Elasticsearch license**](/managed/managed-cluster/high-availability/add-data-center#update-elasticsearch "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Distribute the installer**](/managed/managed-cluster/high-availability/add-data-center#distribute-installer "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create the data center topology**](/managed/managed-cluster/high-availability/add-data-center#create-topology "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Open firewall rules**](/managed/managed-cluster/high-availability/add-data-center#open-firewall-rules "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Install second data center nodes**](/managed/managed-cluster/high-availability/add-data-center#install-nodes "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Replicate Cassandra**](/managed/managed-cluster/high-availability/add-data-center#replicate-cassandra "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Replicate Elasticsearch**](/managed/managed-cluster/high-availability/add-data-center#replicate-elastic "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Migrate the server**](/managed/managed-cluster/high-availability/add-data-center#migrate-server "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Migrate the Nodekeeper**](/managed/managed-cluster/high-availability/add-data-center#migrate-nodekeeper "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Enable the new data center**](/managed/managed-cluster/high-availability/add-data-center#enable-data-center "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")

API return codes

Each REST API call in this procedure returns an HTTP code. Go to the next step only when the call returns `200`.

| Return code | What to do |
| --- | --- |
| `200` | The step succeeded. Go to the next step. |
| `207` | The request is in progress. Repeat the step after a few minutes if there is no response. |
| `40x` | Revise your request path and arguments, then repeat the request. |
| `5xx` | Contact a Dynatrace product expert via live chat. |

### Step 1 Update Elasticsearch license

Fetch the PHA license. Run the following command on each existing **DC-1** node successively:

```
sudo nohup $DT_DIR/installer/reconfigure.sh --only els --premium-ha on &
```

### Step 2 Distribute the installer

In this step, you copy the node installer to every node in **DC-2**.

1. Sign in to the **Cluster Management Console**.
2. Go to **Home** for the Dynatrace Managed deployment status page.
3. Select **Install cluster node**.

Do not run the installer script

The **Run this installer script with root rights** text field contains a command for the installation script. Ignore this command, and do not run the provided script.

1. Copy the `wget` command line from the **Run this command on the target host** text field.
2. Paste and run only the `wget` command line into your terminal window.

### Step 3 Create the data center topology

In this step, you create a configuration that defines which node belongs to which data center.

Run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$DC2_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Step 4 Open firewall rules

In this step, you add firewall rules that open ports for traffic to the new DC-2 nodes.

#### Open ports

To open ports to traffic from the new **DC-2** nodes, run the following Cluster API call only on the **seed node**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID you need to check the firewall rules status.

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

#### Verify firewall rules

Set the request ID environment variable on **seed node** only. The request ID is from the response in the previous API call.

```
REQ_ID=<topology-configuration-request-id>
```

To check the firewall rules status, run the following Cluster API call only on the **seed node**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

### Step 5 Install second data center nodes

In this step, you install Cluster nodes on all hosts within **DC-2** and, once completed, you check for the presence of a Nodekeeper service. A running Nodekeeper service indicates that all nodes were successfully installed in **DC-2**.

#### Install nodes in DC-2

Run this command on every node in **DC-2**, then follow the installer prompts. The installation follows the standard Cluster node procedure.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $DC2_NAME --seed-auth $API_TOKEN
```

For rack-aware deployments, also add the `--rack-dc <data-center>` and `--rack-name <rack>` parameters. For the full procedure, go to [Combine Premium High Availability with rack awareness](/managed/managed-cluster/high-availability/pha-rack-aware "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.").

The installation takes three to five minutes. The expected result is similar to the following:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

#### Check Nodekeeper in DC-2

Run the following Cluster API call only on the **seed node** when all nodes in **DC-2** finish installing:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 6 Replicate Cassandra

In this step, you reconfigure Cassandra in **DC-1** and **DC-2** for cross-data center replication, trigger data synchronization, rebuild Cassandra data, and verify the Cassandra state.

Cassandra replication can take minutes to hours, depending on your metric storage size.

1. #### Replicate Cassandra in DC-1

   Reconfigure Cassandra in **DC-1** for cross-data center replication. Run this Cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

   ```
   REQ_ID=<replication-old-datacenter-request-id>
   ```

   If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check replication status in DC-1

   To check replication status, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after a few minutes.
2. #### Replicate Cassandra in DC-2

   Reconfigure Cassandra in **DC-2** for cross-data center replication and trigger data synchronization. Run this Cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

   ```
   REQ_ID=<replication-new-datacenter-request-id>
   ```

   If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check replication status in DC-2

   To check the replication status, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after a few minutes.
3. #### Rebuild Cassandra data

   In this step, you rebuild Cassandra and verify the progress by checking the status. Depending on the size of your Cassandra database, this can take several hours.

   ##### Rebuild data

   To rebuild Cassandra data in the **DC-2** data center, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200`. If the status code isn't `200` and the response doesn't suggest the following steps, contact a Dynatrace product expert via live chat within your Dynatrace environment.

   ##### Check the rebuild data status

   To check the rebuild data status, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after approximately 15 minutes. Remember that the rebuilding data process can be time-consuming.

   If the response has an error flag set to true, contact a Dynatrace product expert via live chat within your environment.

### Step 7 Replicate Elasticsearch

In this step, you replicate Elasticsearch to the **DC-2** data center and verify the configuration and data replication. Elasticsearch replication can take minutes or hours, depending on your storage size.

#### Replicate Elasticsearch to DC-2

To start replication of Elasticsearch to the **DC-2** data center, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<replication-elasticsearch-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

#### Verify progress and status

To check the replication status of Elasticsearch, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

#### Verify data replication

To verify Elasticsearch data replication, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 8 Migrate the server

In this step, you migrate the server, refresh authorization tokens that enable OneAgent connectivity, and start NGINX in the **DC-2** data center. Also, you refresh installers in **DC-1** that are used to add nodes.

#### Migrate server

Start the Managed Cluster in **DC-2**. Run this Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID that you need to check cluster readiness. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<replication-server-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

#### Check Managed Cluster readiness

To check if the Managed Cluster is ready, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 9 Migrate the Nodekeeper

In this step, you migrate the Nodekeeper service in **DC-1**.

#### Start migration

Dynatrace Managed version 1.319 and earlier

Run the script below manually on each node in **DC-1** before you start migration.

```
/opt/dynatrace-managed/installer/reconfigure.sh --only ndk
```

To start the Nodekeeper migration in **DC-1**, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

#### Check migration status

To check if the Managed Cluster is migrated, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc/status?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200`, and the response contains the `Migration completed successfully` message.

### Step 10 Enable the new data center

1. Enable OneAgent traffic.  
   For details, see [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Enable backup in one of the data centers. Your backup is disabled after migration.  
   For details, see [Backup and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").

Go to the **Deployment status** page in the Cluster Management Console and confirm that it lists both data centers with all nodes healthy.

## Related topics

* [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")
* [Multi-data center failover](/managed/managed-cluster/high-availability/failover "The Premium High Availability failover mechanism detects node outages exceeding 15 minutes and transfers server responsibility to a healthy data center.")