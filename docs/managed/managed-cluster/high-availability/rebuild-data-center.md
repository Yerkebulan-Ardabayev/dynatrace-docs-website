---
title: Rebuild a data center
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rebuild-data-center
---

# Rebuild a data center

# Rebuild a data center

* How-to guide
* 10-min read
* Updated on Jul 07, 2026

To rebuild a lost data center (DC) in a Premium High Availability deployment, follow the steps below. The procedure migrates and replicates Dynatrace Managed components so they can replicate data across two data centers.

The procedure uses the following terms:

* **Source-DC**: Surviving data center that contains the Managed Cluster.
* **Target-DC**: Lost data center designated for recovery.
* **seed node**: Node in **Source-DC** that performs installation tasks and distributes configuration.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Gather information**](/managed/managed-cluster/high-availability/rebuild-data-center#gather-information "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set variables and check for custom settings**](/managed/managed-cluster/high-availability/rebuild-data-center#set-variables "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Terminate unavailable data center**](/managed/managed-cluster/high-availability/rebuild-data-center#terminate-unavailable-dc "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Remove nodes**](/managed/managed-cluster/high-availability/rebuild-data-center#remove-nodes "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Remove lost data center from configuration**](/managed/managed-cluster/high-availability/rebuild-data-center#remove-lost-dc "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Distribute the installer**](/managed/managed-cluster/high-availability/rebuild-data-center#distribute-installer "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Prepare Managed Cluster data for replication**](/managed/managed-cluster/high-availability/rebuild-data-center#prepare-cluster-data "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Create the data center topology**](/managed/managed-cluster/high-availability/rebuild-data-center#create-topology "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Open firewall rules**](/managed/managed-cluster/high-availability/rebuild-data-center#open-firewall-rules "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Install second data center nodes**](/managed/managed-cluster/high-availability/rebuild-data-center#install-nodes "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Step 11")

**Migrate Cassandra**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-cassandra "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Step 12")

**Migrate Elasticsearch**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-elastic "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 13](https://dt-cdn.net/images/number-step-gray-13-51a01d2a99.svg "Step 13")

**Migrate the server**](/managed/managed-cluster/high-availability/rebuild-data-center#migrate-server "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")[![Step 14](https://dt-cdn.net/images/number-step-gray-14-75a70c82df.svg "Step 14")

**Restore traffic and backup**](/managed/managed-cluster/high-availability/rebuild-data-center#restore-traffic-backup "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.")

API return codes

Steps 3–14 use Dynatrace Cluster API calls. Each call returns an HTTP code. Go to the next step only when the returned code is `200`. Expect the following return codes:

`200`: Go to the next step. The current step succeeded.  
`207`: The request is still processing. Repeat the step after a few minutes.  
`40x`: Revise your request path and arguments, and repeat the request.  
`5xx`: Contact support.

## Step 1 Gather information

The commands use these variables in Cluster API calls. Gather the following information:

* `<seed-node-ip>`: The IP address of the **seed node** from **Source-DC**.  
  Use any node that runs in the existing data center and can perform installation tasks and distribute configuration.
* `<nodes-ips>`: The list of IPv4 addresses of new nodes in **Target-DC**.  
  Example: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>`: A valid Cluster API token. The token requires the ServiceProviderAPI scope.  
  You can generate it in the Cluster Management Console (CMC). See [Cluster API authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>`: The directory where Dynatrace Managed runs on the seed node.  
  The default Dynatrace Managed installation directory is `/opt/dynatrace-managed`.
* `<datacenter-1>`: The **Source-DC** name must be the same as the **Cassandra DC** name.  
  The default Cassandra DC name is `datacenter1`.

  Get the DC name

  To get the DC name, run this command on the **seed node** before you start migration:

  ```
  sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status
  ```

  The response includes the **Source-DC** name. The example shows a DC named `datacenter1`:

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
* `<datacenter-2>`: The **Target-DC** name must remain unchanged. Example: `dc-us-east-2`.

Lost data center name

During recovery to **Target-DC**, use the same name as the lost data center.

## Step 2 Set variables and check for custom settings

Set the following environment variables on the **seed node** in **Source-DC** and on every node in **Target-DC**:

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=echo '[<nodes-ips]'



API_TOKEN=<api-token>



SDC_NAME=<datacenter-1>



TDC_NAME=<datacenter-2>
```

For example:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]'



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



SDC_NAME=datacenter1



TDC_NAME=dc-us-east-2
```

If your Cassandra or Elasticsearch cluster uses `custom.settings` to turn on rack-awareness, contact a Dynatrace product expert via live chat. The Dynatrace product expert must apply these custom settings before you proceed with **Target-DC** recovery.

To check whether custom settings exist, run this command on the **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

If the `custom.settings` file exists, the Managed Cluster uses custom settings.

## Step 3 Terminate unavailable data center

Stop all required Dynatrace Managed services in the recommended order. See [Start, stop, or restart a node](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").

## Step 4 Remove nodes

1. Go to the **CMC**.
2. For each node in the unavailable data center, go to the **Node details** page and remove the node.

For more information on other ways to remove a node, see [Remove a Managed Cluster node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.").

## Step 5 Remove lost data center from configuration

Run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

## Step 6 Distribute the installer

In this step, copy the node installer to every node in **Target-DC**.

1. Sign in to the CMC.
2. Go to **Home** for the Dynatrace Managed deployment status page.
3. Open **Add new cluster node**.
4. Copy only the `wget` command line from **Run this command on the target host**. Ignore the command in **Run this installer script with root rights** and don't run the installer script.
5. Paste and run only the `wget` command line in your terminal window.

## Step 7 Prepare Managed Cluster data for replication

In this step, prepare data indexes for replication.

### Prepare Managed Cluster data

Run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Check Managed Cluster preparation status

Run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

## Step 8 Create the data center topology

In this step, create configuration that identifies which nodes belong to each data center.

Run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

## Step 9 Open firewall rules

In this step, add firewall rules that open ports to traffic from the **Target-DC** nodes.

### Open ports

To open ports to traffic from the new **Target-DC** nodes, run the following Cluster API call only on the **seed node**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID. Use this ID to check the firewall rules status.

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Verify firewall rules

Set the request ID environment variable only on the **seed node**. Use the request ID from the response in the previous API call.

```
REQ_ID=<topology-configuration-request-id>
```

To check the firewall rules status, run the following Cluster API call only on the **seed node**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

## Step 10 Install second data center nodes

In this step, install Managed Cluster nodes on all hosts in **Target-DC**. Then check for the Nodekeeper service to verify that all nodes installed successfully in **Target-DC**.

### Install nodes in the target data center

Run the following command on every node in **Target-DC**. Follow the prompts for a typical node installation.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

The node installation takes about 3–5 minutes. The expected output is:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

### Check Nodekeeper in the target data center

Run the following Cluster API call only on the **seed node** when all nodes in **Target-DC** finish installing:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 11 Migrate Cassandra

In this step, reconfigure Cassandra in **Source-DC** and **Target-DC** for cross data center replication. Then trigger data synchronization, rebuild Cassandra data, and verify Cassandra state.

The Cassandra migration may take minutes to hours depending on your metric storage size.

1. ### Trigger migration

   To start migration of Cassandra in the **Target-DC** data center, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200` and the response body contains a request ID. Use this ID to check the migration status. Set the request ID environment variable only on the **seed node**.

   ```
   REQ_ID=<migration-new-datacenter-request-id>
   ```

   If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   ### Check migration status

   To check the migration status, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after a few minutes.
2. ### Rebuild Cassandra data

   Depending on the size of your Cassandra database, this can take several hours.

   #### Rebuild data

   To rebuild Cassandra data in the **Target-DC** data center, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code is `200`. If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check the rebuild data status

   To check the rebuild data status, run the following Cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code isn't `200`, try again after approximately 15 minutes. The rebuild process can take several hours.

   If the response has an error flag set to true, contact a Dynatrace product expert via live chat.

## Step 12 Migrate Elasticsearch

In this step, migrate Elasticsearch to the **Target-DC** data center. Then verify the configuration and data migration. The Elasticsearch migration can take minutes or hours depending on your Elasticsearch storage.

### Migrate Elasticsearch to the target data center

Start Elasticsearch. Run the following command on every node in **Target-DC** in sequence:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

To start migration of Elasticsearch to the **Target-DC** data center, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200`.

### Verify progress and status

To check the migration status of Elasticsearch, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Verify data migration

To verify the Elasticsearch data migration, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 13 Migrate the server

In this step, migrate the server, refresh authorization tokens for OneAgent connectivity, and start NGINX in the **Target-DC** data center. Also, refresh installers in **Source-DC** for adding nodes.

### Migrate the server

Launch the Managed Cluster in the **Target-DC** by running the following Cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body contains a request ID. Use this ID to check Managed Cluster readiness. Set the request ID environment variable only on the **seed node**.

```
REQ_ID=<migration-server-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Check Managed Cluster readiness

To check whether the Managed Cluster is ready, run the following Cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 14 Restore traffic and backup

1. Restore OneAgent traffic.  
   For details, see [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Turn on backup in one of the data centers. Migration turns off backup.  
   For details, see [Back up and restore a Managed Cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").