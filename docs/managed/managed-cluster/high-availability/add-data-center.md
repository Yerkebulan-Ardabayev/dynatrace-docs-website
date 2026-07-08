---
title: Add a data center
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/add-data-center
---

# Add a data center

# Add a data center

* How-to guide
* 12-min read
* Updated on Jun 15, 2026

To create a globally distributed high availability deployment (Premium High Availability (PHA)), you must add a redundant set of nodes to your original Managed Cluster deployment. Typically, such high availability deployments span across multiple data centers. Dynatrace Managed enables you to add mirrored nodes located in another data center.

In this procedure, the following terms are designated as follows:

* **DC-1** - The data center where the initial Dynatrace Managed Cluster is located.
* **DC-2** - An additional data center designated for PHA deployment.
* **seed node** - Any node within **DC-1** that will be used for performing the installation tasks and distribution of configuration.

The procedure migrates and replicates each Dynatrace Managed component individually to prepare for cross-data center data replication.
See [Overview of Dynatrace Managed components](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

## Before you begin

* **DC-1** cluster must have backup disabled before starting the migration procedure. Create a fresh Managed Cluster backup and disable cluster backup shortly before deploying the additional data center.
* Migration must not take longer than four weeks. If your migration will exceed four weeks, contact a Dynatrace product expert via live chat.
* **DC-1** cluster automatic update must be disabled before starting the migration procedure. The Managed Cluster **must not** be upgraded during migration. See [Automatic update](/managed/managed-cluster/operation/update-cluster#automatic-update-recommended "Learn how to update a Managed cluster and how to schedule an automatic update."). Contact a Dynatrace product expert via live chat if your automatic update option is disabled.
* Make sure machines are prepared for the Managed Cluster in **DC-2**.

  Recommendation

  Since **DC-2** will replicate the data of **DC-1**, designate the same number of nodes with the same hardware, including disk storage.  
  All nodes in **DC-1** and **DC-2** must be time-synchronized. Set up Network Time Protocol (NTP) to time-synchronize all nodes.
* PHA deployment requires at least three nodes in **DC-1** and three corresponding nodes in **DC-2**.
* All nodes in both data centers must be able to communicate with each other. To check if a node in **DC-1** is reachable from a host in **DC-2**, you can run a health-check REST call. For example, run the following command from a host in **DC-2**:

```
curl -k https://<DC-1-node-IP>/rest/health
```

where `<DC-1-node-IP>` is the IP address of any node in **DC-1**. You should receive `"RUNNING"` in a response if the connection can be established successfully.

## Preparation

Ensure that your system meets the specified [hardware and operating system requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").

### Gather information

The commands use these variables in executing the REST API calls. For this, you need the following information:

* `<seed-node-ip>` - The IP address of the **seed node** from **DC-1**.  
  This can be any node running in the existing data center that will be used for performing the installation tasks and distribution of configuration.
* `<nodes-ips>` - The list of IPv4 addresses of new nodes in **DC-2**.  
  Example: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>` - A valid Cluster API token (ServiceProviderAPI scope is required).  
  You can generate it in the Dynatrace Managed Cluster Management Console. See [Cluster API - Authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>` - The directory where Dynatrace Managed is installed on the seed node.  
  The default Dynatrace Managed installation directory is `/opt/dynatrace-managed`
* `<datacenter-1>` - The **DC-1** name must be the same as the **Cassandra DC** name.  
  The default Cassandra DC name is `datacenter1`.

  Get the DC name.

  To get the DC name, run this command on the **seed node** before starting migration:

  ```
  sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status
  ```

  You will get a response that includes the **DC-1** name. Example for a DC named `datacenter1`:

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
* `<datacenter-2>` - The **DC-2** name can be any string that begins and ends with an alphanumeric character and is no longer than 80 characters. Underscores and dashes are allowed within the name. Example: `dc-us-east-2`.

### Set variables

To streamline the numerous REST API calls during the deployment, set environment variables on every node in **DC-1** and **DC-2**.

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=$(echo '[<nodes-ips]')



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

### Check for custom settings

If your Cassandra or Elasticsearch cluster is configured with `custom.settings` that enable rack-awareness, contact a Dynatrace product expert via live chat to apply these custom settings before proceeding with **DC-2** installation.

To check whether custom settings are applied, run on **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

If the `custom.settings` file exists, you use custom settings.

## Review network zone setup

Before you migrate to PHA, review your network zone setup for OneAgents and Environment ActiveGates that use the `default` network zone.

When you migrate and restart a Managed Cluster node, Dynatrace changes the Embedded ActiveGate network zone from `default` to the node's data center name. The network zone reassignment can reroute OneAgent and Environment ActiveGate traffic that currently uses the `default` network zone.

While PHA implements optimizations to reduce traffic between DCs, ActiveGates should send data to both DCs for redundancy. Configure OneAgents and ActiveGates to prefer specific network zones while preserving their ability to fail over to another part of the Managed Cluster during a DC outage. You can also use load balancers for this purpose.

For active-passive application deployments, keep ActiveGates active in the passive portions of the deployment so the Dynatrace infrastructure fails over without reconfiguration or rediscovery.

## Installation

To create a Managed Cluster in a second data center, follow this procedure.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Update Elasticsearch license**](/managed/managed-cluster/high-availability/add-data-center#update-elasticsearch "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Distribute the installer**](/managed/managed-cluster/high-availability/add-data-center#distribute-installer "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create the data center topology**](/managed/managed-cluster/high-availability/add-data-center#create-topology "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Open firewall rules**](/managed/managed-cluster/high-availability/add-data-center#open-firewall-rules "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Install second data center nodes**](/managed/managed-cluster/high-availability/add-data-center#install-nodes "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Replicate Cassandra**](/managed/managed-cluster/high-availability/add-data-center#replicate-cassandra "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Replicate Elasticsearch**](/managed/managed-cluster/high-availability/add-data-center#replicate-elastic "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Migrate the server**](/managed/managed-cluster/high-availability/add-data-center#migrate-server "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Migrate the nodekeeper**](/managed/managed-cluster/high-availability/add-data-center#migrate-nodekeeper "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Enable the new data center**](/managed/managed-cluster/high-availability/add-data-center#enable-data-center "Learn how to replicate Managed Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")

API return codes

Each of the REST API calls returns an HTTP code. Go to the next step only when the returned code is `200`. Expect the following return codes:

`200` - Go to the next step, current step was executed successfully.  
`207` - The request is processing. Repeat the step after a few minutes if there's no response.  
`40x` - Revise your request path and arguments, then repeat the request.  
`5xx` - Contact a Dynatrace product expert via live chat.

### Step 1 Update Elasticsearch license

Fetch the PHA license. Run the following command on each existing **DC-1** node successively:

```
sudo nohup $DT_DIR/installer/reconfigure.sh --only els --premium-ha on &
```

### Step 2 Distribute the installer

In this step, you copy the node installer to every node in **DC-2**.

1. Sign in to your Dynatrace Managed Cluster Management Console.
2. Go to **Home** for the Dynatrace Managed deployment status page.
3. Select **Install cluster node**.
4. Copy the `wget` command line from the **Run this command on the target host** text field.

   Do not run the installer script

   The **Run this installer script with root rights** text field contains a command for the installation script. Ignore this command; **don't run the provided script**.
5. Paste and run only the `wget` command line into your terminal window.

### Step 3 Create the data center topology

In this step, you create a configuration that defines which node belongs to which data center.

Run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$DC2_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Step 4 Open firewall rules

In this step, you add firewall rules that open ports for traffic to the new DC-2 nodes.

#### Open ports

To open ports to traffic from the new **DC-2** nodes, run the following cluster API call only on the **seed node**:

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

To check the firewall rules status, run the following cluster API call only on the **seed node**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

### Step 5 Install second data center nodes

In this step, you install Managed Cluster nodes on all hosts within **DC-2** and, once completed, you check for the presence of a Nodekeeper service. A running Nodekeeper service indicates that all nodes were successfully installed in **DC-2**.

#### Install nodes in DC-2

Run the following command on every node in **DC-2**. Follow the on-screen instructions, as this will be a typical node installation.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $DC2_NAME --seed-auth $API_TOKEN
```

The installation takes 3 to 5 minutes. The expected result is similar to the following:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

#### Check Nodekeeper in DC-2

Run the following cluster API call only on the **seed node** when all nodes in **DC-2** finish installing:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 6 Replicate Cassandra

In this step, you reconfigure Cassandra in **DC-1** and **DC-2** for cross-data center replication, trigger data synchronization, rebuild Cassandra data, and verify the Cassandra state.

Cassandra replication may take minutes to hours, depending on your metric storage size.

1. #### Replication of Cassandra in DC-1

   In this step, you reconfigure Cassandra for cross-data center replication.

   #### Replicate Cassandra in DC-1

   To start Cassandra replication in the **DC-1** data center, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

   ```
   REQ_ID=<replication-old-datacenter-request-id>
   ```

   If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check replication status in DC-1

   To check replication status, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after a few minutes.
2. #### Replication of Cassandra in DC-2

   In this step, you reconfigure Cassandra for cross-data center replication and trigger data synchronization.

   #### Replicate Cassandra in DC-2

   To start replication of Cassandra in the **DC-2** data center, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

   ```
   REQ_ID=<replication-new-datacenter-request-id>
   ```

   If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check replication status in DC-2

   To check the replication status, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after a few minutes.
3. #### Rebuild Cassandra data

   In this step, you rebuild Cassandra and verify the progress by checking the status. Depending on the size of your Cassandra database, this can take several hours.

   ##### Rebuild data

   To rebuild Cassandra data in the **DC-2** data center, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200`. If the status code isn't `200` and the response doesn't suggest the following steps, contact a Dynatrace product expert via live chat within your Dynatrace environment.

   ##### Check the rebuild data status

   To check the rebuild data status, run the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after approximately 15 minutes. Remember that the rebuilding data process can be time-consuming.

   If the response has an error flag set to true, contact a Dynatrace product expert via live chat within your environment.

### Step 7 Replicate Elasticsearch

In this step, you replicate Elasticsearch to the **DC-2** data center and verify the configuration and data replication. Elasticsearch replication may take minutes or hours, depending on your storage size.

#### Replicate Elasticsearch to DC-2

To start replication of Elasticsearch to the **DC-2** data center, run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID that you need to check replication status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<replication-elasticsearch-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

#### Verify progress and status

To check the replication status of Elasticsearch, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

#### Verify data replication

To verify Elasticsearch data replication, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 8 Migrate the server

In this step, you migrate the server, refresh authorization tokens that enable OneAgent connectivity, and start NGINX in the **DC-2** data center. Also, you refresh installers in **DC-1** that are used to add nodes.

#### Migrate server

Launch the Dynatrace Managed Cluster in **DC-2** by running the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID that you need to check cluster readiness. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<replication-server-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

#### Check Managed Cluster readiness

To check if the Managed Cluster is ready, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/server/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Step 9 Migrate the nodekeeper

In this step, you migrate a nodekeeper in **DC-1**.

#### Start migration

Dynatrace Managed version 1.319 and earlier

Run the script below manually on each node in **DC-1** before you start migration.

```
/opt/dynatrace-managed/installer/reconfigure.sh --only ndk
```

To start the nodekeeper migration in **DC-1**, run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

#### Check migration status

To check if the Managed Cluster is migrated, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/currentDc/status?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200`, and the response contains the `Migration completed successfully` message.

### Step 10 Enable the new data center

1. Enable OneAgent traffic.  
   For details, see [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Enable backup in one of the data centers. Your backup is disabled after migration.  
   For details, see [Backup and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").