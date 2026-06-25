---
title: Premium HA - Data center disaster recovery from backup
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup
scraped: 2026-05-12T12:06:57.040997
---

# Premium HA - Data center disaster recovery from backup

# Premium HA - Data center disaster recovery from backup

* Updated on Jan 13, 2026

Premium High Availability

Dynatrace Premium High Availability (Premium HA) is a self-contained, out-of-the-box solution that provides near-zero downtime and allows monitoring to continue without data loss in failover scenarios. This solution requires additional licensing for your deployment.

In this recovery procedure, the following terms are designated as follows:

* **Source-DC** - Source (surviving) data center where the Managed cluster is located.
* **Target-DC** - Target (lost) data center designated for recovery.
* **seed node** - Any node within **Source-DC** that will be used for performing the installation tasks and distribution of configuration.

The procedure involves migration and replication of Dynatrace Managed components separately so they are prepared for data replication across two data centers.
See [Overview of Dynatrace Managed components](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Uninstall Dynatrace Managed on all running nodes**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-1 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Restore data center from backup**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-2 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Remove lost data center from configuration**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-3 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Distribute the installer**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-4 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Prepare cluster data for a replication**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-5 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Create the data center topology**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-6 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Open firewall rules**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-7 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Install second data center nodes**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-8 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Migrate Cassandra**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-9 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Migrate Elasticsearch**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#anchor_pha_migrate_elastic "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Step 11")

**Migrate the server**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-11 "Learn how to recover lost data center from backup in a multiple data center deployment.")[![Step 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Step 12")

**Enable the new data center**](/managed/managed-cluster/high-availability/data-center-disaster-recovery-from-backup#step-12 "Learn how to recover lost data center from backup in a multiple data center deployment.")

### Gather information

The commands will use these variables in executing the REST API calls. For this, you will need the following information:

* `<seed-node-ip>` - The IP address of the **seed node** from **Source-DC**.  
  This can be any node running in existing data center that will be used for performing the installation tasks and distribution of configuration.
* `<nodes-ips>` - The list of IPV4 addresses of new nodes in **Target-DC**.  
  Example: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>` - A valid Cluster API token (ServiceProviderAPI scope is required).  
  You can generate it in the Dynatrace Managed Cluster Management Console. See [Cluster API - Authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>` - The directory where Dynatrace Managed is installed on the seed node.  
  The default Dynatrace Managed installation directory is `/opt/dynatrace-managed`
* `<datacenter-1>` - The **Source-DC** name must be the same as the **Cassandra DC** name.  
  The default Cassandra DC name is `datacenter1`.

  Get the DC name.

  To get the DC name, execute this command on the **seed node** before starting migration:

  `sudo <dynatrace-directory>/utils/cassandra-nodetool.sh status`

  You will get a response that includes the **Source-DC** name. Example for a DC named `datacenter1`:

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
* `<datacenter-2>` - The **Target-DC** name must remain unchanged. Example: `dc-us-east-2`.

Lost data center name

You must use the same name of the lost data center during the recovery to **Target-DC**.

### Set variables

Set the following environment variables on **seed node** in **Source-DC** and EACH NODE in **Target-DC**:

```
SEED_IP=<seed-ip>



DT_DIR=<dynatrace-directory>



NODES_IPS=$(echo '[<nodes-ips]')



API_TOKEN=<api-token>



SDC_NAME=<datacenter-1>



TDC_NAME=<datacenter-2>
```

For example:

```
SEED_IP=10.176.37.201



DT_DIR=/opt/dynatrace-managed



NODES_IPS=$(echo '["10.176.37.218", "10.176.37.227", "10.176.37.120"]')



API_TOKEN=R_SZOpV4RTOmjr9fFmK4x



SDC_NAME=datacenter1



TDC_NAME=dc-us-east-2
```

### Check for custom settings

If your Cassandra or Elasticsearch cluster is configured with `custom.settings` that enable rack-awareness, contact a Dynatrace product expert via live chat to apply these custom settings before proceeding with **Target-DC** installation.

To check whether custom settings are applied, execute on **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

If the `custom.settings` file exists, you are using custom settings.

API return codes

Each of the REST API calls will return the HTTP code. Go to the next step only when the returned code is `200`. Expect the following return codes:

`200` - Go to the next step, current step was executed successfully.  
`207` - The request is being processed, repeat a step after few minutes.  
`40x` - Revise your request path and arguments and repeat the request.  
`5xx` - Contact support.

### Step 1 Uninstall Dynatrace Managed on all running nodes

Follow the official procedure to remove a cluster node using either the command prompt or the Cluster Management Console. See [Remove a cluster node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.").

### Step 2 Restore data center from backup

Follow the official procedure to restore the data center from the backup. See [Back up and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.").

### Step 3 Remove lost data center from configuration

Execute the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

If the status code is not `200` and the response does not suggest next steps, contact a Dynatrace product expert via live chat.

### Step 4 Distribute the installer

In this step, you will copy the node installer to every node in **Target-DC**.

1. Log into your Dynatrace Managed Cluster Management Console.
2. Go to **Home** for the Dynatrace Managed deployment status page.
3. Click **Add new cluster node**.
4. Copy the `wget` command line from the **Run this command on the target host** text box.

   Do not run the installer script

   The **Run this installer script with root rights** text box contains a command for the installation script. Ignore this command; **do not execute the provided script**.
5. Paste and execute only the `wget` command line into every node in Target-DC terminal window.

### Step 5 Prepare cluster data for a replication

In this step, you will prepare data indexes for replication.

#### Prepare cluster data

Execute the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

If the status code is not `200` and the response does not suggest next steps, contact a Dynatrace product expert via live chat.

#### Check cluster preparation status

Execute the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

If the status code from this call is not `200`, try again after a few minutes.

### Step 6 Create the data center topology

In this step, you will create configuration that maintains which nodes belong to which data center.

Execute the following cluster API call only on the **seed node**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code is not `200` and the response does not suggest next steps, contact a Dynatrace product expert via live chat.

### Step 7 Open firewall rules

In this step, you will add firewall rules that open ports to traffic from the **Target-DC** nodes.

#### Open ports

To open ports to traffic from the new **Target-DC** nodes, execute the following cluster API call only on the **seed node**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, status code will be `200` and the response body will contain a request ID you need to check the firewall rules status.

If the status code is not `200` and the response does not suggest next steps, contact a Dynatrace product expert via live chat.

#### Verify firewall rules

Set the request ID environment variable on **seed node** only. The request ID is from the response in the previous API call.

```
REQ_ID=<topology-configuration-request-id>
```

To check the firewall rules status, execute the following cluster API call only on the **seed node**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code from this call is not `200`, try again after a few minutes.

### Step 8 Install second data center nodes

In this step, you will install managed nodes on all hosts within **Target-DC** and once completed, you will check for the presence of a Nodekeeper service. This will indicate if all nodes were successfully installed in **Target-DC**.

#### Install nodes in Target-DC

Execute the following command on every node in **Target-DC**. Follow the on-screen instructions as this will be a typical node installation.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

This operation should take about 3-5 minutes and the expected result should be similar to this:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

#### Check Nodekeeper in Target-DC

Execute the following cluster API call only on the **seed node** when all nodes in **Target-DC** finish installing:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code is not `200`, try again after a few minutes.

### Step 9 Migrate Cassandra

In this step, you will reconfigure Cassandra in **Source-DC** and **Target-DC** for cross data center replication, trigger data synchronization, rebuild Cassandra data and verify Cassandra state.

It may take minutes to hours depending on your metric storage size.

1. #### Migration of Cassandra in Target-DC

   In this step, you will reconfigure Cassandra for cross data center replication and trigger data synchronization.

   #### Migrate Cassandra

   To start migration of Cassandra in the **Target-DC** data center, execute the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, status code will be `200` and the response body will contain a request ID which you need to check migration status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

   ```
   REQ_ID=<migration-new-datacenter-request-id>
   ```

   If status code is not `200` and response does not suggest next steps, contact a Dynatrace product expert via live chat.

   #### Check migration status

   To check the migration status, execute the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code is not `200`, try again after few minutes.
2. #### Rebuild Cassandra data

   Rebuild Cassandra data and Verify Cassandra state for Dynatrace release 254 and earlier.

   In this step, you will rebuild Cassandra, verify the progress by checking the status. Depending on the size of your Cassandra database, can take several hours.

   ##### Rebuild data

   To rebuild Cassandra, run the following command on each new **Target-DC** node successively. Use the `nohup` command to prevent interruption of script execution (such as session disconnect) during important operations.

   ```
   sudo nohup $DT_DIR/utils/cassandra-nodetool.sh rebuild -- $SDC_NAME &
   ```

   ##### Verify progress and status

   To verify the progress and status, execute the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuildStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If the status code is not `200`, try again after approximately 15 minutes. Remember that the rebuild process can be time-consuming.

   #### Verify Cassandra state

   To verify Cassandra cluster state, execute the `cassandra-nodetool.sh` with the `status` parameter only on the **seed node**:

   ```
   sudo $DT_DIR/utils/cassandra-nodetool.sh status
   ```

   The result should look similar to this:

   ```
   Datacenter: dc1



   ===============



   Status=Up/Down



   |/ State=Normal/Leaving/Joining/Moving



   --  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



   UN  10.176.41.167  18.82 GB   256          100.0%            3af25127-4f99-4f43-afc3-216d7a2c10f8  rack1



   UN  10.176.41.154  19.44 GB   256          100.0%            5a618559-3a73-42ec-83f0-32d28e08beec  rack1



   UN  10.176.41.43   19.58 GB   256          100.0%            191f3b30-949a-4cf2-b620-68a40eebf31e  rack1



   Datacenter: dc2



   ===============



   Status=Up/Down



   |/ State=Normal/Leaving/Joining/Moving



   --  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



   UN  10.176.42.54   19.18 GB   256          100.0%            852ce236-a430-400a-92a6-daeed99acf68  rack1



   UN  10.176.42.104  19.12 GB   256          100.0%            84479219-b64d-442c-a807-a832db9aae18  rack1



   UN  10.176.42.234  19.4 GB    256          100.0%            507b377c-5bfc-4667-b251-a9b7c453ed22  rack1
   ```

   The **Load** value should not differ significantly between the nodes and **Status** should be `UN` on all nodes.

   In this step, you will rebuild Cassandra and verify the progress by checking the status. Depending on the size of your Cassandra database, this can take several hours.

   ##### Rebuild data

   To rebuild Cassandra data in the **Target-DC** data center, execute the following cluster API call only on the seed node:

   ```
   curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
   ```

   If successful, the status code will be `200`. If the status code is not `200` and the response does not suggest the following steps, contact a Dynatrace product expert via live chat within your Dynatrace environment.

   ##### Check the rebuild data status

   To check the rebuild data status, execute the following cluster API call only on the **seed node**:

   ```
   curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
   ```

   If the status code is not `200`, try again after approximately 15 minutes. Remember that the rebuilding data process can be time consuming.

   If the response has an error flag set to `true`, contact a Dynatrace product expert via live chat within your environment.

### Step 10 Migrate Elasticsearch

In this step, you will migrate Elasticsearch to the **Target-DC** data center, verify the configuration and data migration. This step may take minutes or hours depending on your Elasticsearch storage.

#### Migrate Elasticsearch to Target-DC

Start Elasticsearch. Execute the following command successively on every node in **Target-DC** only:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

To start migration of Elasticsearch to the **Target-DC** data center, execute the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, status code will be 200.

#### Verify progress and status

To check the migration status of Elasticsearch, execute the following cluster API call only on the seed node:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code is not `200`, try again after a few minutes.

#### Verify data migration

To verify migration Elasticsearch data migration, execute the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code is not `200`, try again after a few minutes.

### Step 11 Migrate the server

In this step, you will migrate the server, refresh authorization tokens that enable OneAgent connectivity, and start NGINX in the **Target-DC** data center. Also, you will refresh installers in **Source-DC** that are used to add nodes.

#### Migrate server

Launch the Dynatrace Managed cluster in the **Target-DC** by executing the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, status code will be `200` and the response body will contain a request ID which you need to check cluster readiness. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<migration-server-request-id>
```

If status code is not `200` and response does not suggest next steps, contact a Dynatrace product expert via live chat.

#### Check cluster readiness

To check if the cluster is ready, execute the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code is not `200`, try again after a few minutes.

### Step 12 Enable the new data center

1. Enable OneAgent traffic.  
   For details, see [Enable/Disable a cluster node](/managed/managed-cluster/configuration/cluster-node-capabilities "Find out how to enable/disable a cluster node via the Web UI or API call").
2. Enable backup in one of the data centers. Your backup is disabled after migration.  
   For details, see [Back up and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").