---
title: Recover from a backup
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/recover-from-backup
---

# Recover from a backup

# Recover from a backup

* How-to guide
* 10-min read
* Updated on Jul 07, 2026

To restore a lost data center (DC) from backup in a Premium High Availability deployment, follow these steps.

This procedure uses the following terms:

* **Source-DC** - Source (surviving) DC where the Managed Cluster is located.
* **Target-DC** - Target (lost) DC designated for recovery.
* **seed node** - Any node within **Source-DC** used to perform the installation tasks and distribute configuration.

The procedure migrates and replicates Dynatrace Managed components individually to prepare them for data replication across two DCs.
See [Managed components](/managed/managed-cluster/basics/managed-components "Understand the Dynatrace Managed architecture, including the Managed Cluster, the Cluster Management Console, and Mission Control.").

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Uninstall Dynatrace Managed on all running nodes**](/managed/managed-cluster/high-availability/recover-from-backup#step-1 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Restore data center from backup**](/managed/managed-cluster/high-availability/recover-from-backup#step-2 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Remove lost data center from configuration**](/managed/managed-cluster/high-availability/recover-from-backup#step-3 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Distribute the installer**](/managed/managed-cluster/high-availability/recover-from-backup#step-4 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Prepare cluster data for replication**](/managed/managed-cluster/high-availability/recover-from-backup#step-5 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Create the data center topology**](/managed/managed-cluster/high-availability/recover-from-backup#step-6 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Open firewall rules**](/managed/managed-cluster/high-availability/recover-from-backup#step-7 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Step 8")

**Install second data center nodes**](/managed/managed-cluster/high-availability/recover-from-backup#step-8 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 9](https://dt-cdn.net/images/step-9-caa5a7bd32.svg "Step 9")

**Migrate Cassandra**](/managed/managed-cluster/high-availability/recover-from-backup#step-9 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 10](https://dt-cdn.net/images/step-10-f1909063b2.svg "Step 10")

**Migrate Elasticsearch**](/managed/managed-cluster/high-availability/recover-from-backup#anchor_pha_migrate_elastic "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 11](https://dt-cdn.net/images/number-step-gray-11-5cb9304947.svg "Step 11")

**Migrate the server**](/managed/managed-cluster/high-availability/recover-from-backup#step-11 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")[![Step 12](https://dt-cdn.net/images/number-step-gray-12-0eaef2f87b.svg "Step 12")

**Enable the new data center**](/managed/managed-cluster/high-availability/recover-from-backup#step-12 "Learn how to restore a Premium High Availability data center from backup in a Dynatrace Managed multi-DC deployment after a data center loss.")

## Gather information

Collect the following information before running the API calls:

* `<seed-node-ip>` - The IP address of the **seed node** from **Source-DC**.  
  The seed node can be any node running in an existing DC, used for performing the installation tasks and distributing configuration.
* `<nodes-ips>` - The list of IPv4 addresses of new nodes in **Target-DC**.  
  Example: `"176.16.0.5", "176.16.0.6", "176.16.0.7"`
* `<api-token>` - A valid Cluster API token (ServiceProviderAPI scope is required).  
  You can generate it in the Dynatrace Managed Cluster Management Console (CMC). See [Cluster API - Authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* `<dynatrace-directory>` - The directory where Dynatrace Managed is installed on the seed node.  
  The default Dynatrace Managed installation directory is `/opt/dynatrace-managed`
* `<datacenter-1>` - The **Source-DC** name must be the same as the **Cassandra DC** name.  
  The default Cassandra DC name is `datacenter1`.

  Get the DC name.

  To get the DC name, run this command on the **seed node** before starting migration:

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

You must use the same name of the lost DC during the recovery to **Target-DC**.

## Set variables

Set the following environment variables on the **seed node** in **Source-DC** and on every node in **Target-DC**:

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

## Check for custom settings

If your Cassandra or Elasticsearch cluster is configured with `custom.settings` that enable rack-awareness, contact a Dynatrace product expert via live chat. Apply the custom settings before proceeding with **Target-DC** installation.

To check whether custom settings are applied, run on **seed node**:

```
ls $DT_DIR/installer/custom.settings
```

If the `custom.settings` file exists, you're using custom settings.

API return codes

Each of the REST API calls will return the HTTP code. Go to the next step only when the returned code is `200`. Expect the following return codes:

`200` - The step completed successfully. Go to the next step.  
`207` - The request is in process. Retry after a few minutes.  
`40x` - Revise your request path and arguments and repeat the request.  
`5xx` - Contact support.

## Step 1 Uninstall Dynatrace Managed on all running nodes

Follow the official procedure to remove a Managed Cluster node using either the command prompt or the CMC. See [Remove a cluster node](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console.").

## Step 2 Restore data center from backup

Follow the official procedure to restore the DC from the backup. See [Back up and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster#cluster-restore "Understand the steps and commands required to restore a Dynatrace Managed cluster.").

## Step 3 Remove lost data center from configuration

Run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/lostDatacenterCleanUp?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

## Step 4 Distribute the installer

1. Sign in to the CMC.
2. Go to **Home** for the Dynatrace Managed deployment status page.
3. Select **Add new cluster node**.
4. Copy the `wget` command line from the **Run this command on the target host** text field.

   Do not run the installer script

   The **Run this installer script with root rights** text field contains a command for the installation script. Ignore this command. Don't run the provided script.
5. Paste and run only the `wget` command line on every node in the **Target-DC** terminal window.

## Step 5 Prepare cluster data for replication

### Prepare cluster data

Run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Check cluster preparation status

Run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterReplicationPreparation?Api-Token=$API_TOKEN -H  "accept: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

## Step 6 Create the data center topology

Run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST -d "{\"newDatacenterName\" : \"$TDC_NAME\", \"nodesIp\" :$NODES_IPS}" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/datacenterTopology?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

## Step 7 Open firewall rules

### Open ports

To open ports to traffic from the new **Target-DC** nodes, run the following cluster API call only on the **seed node**:

```
curl --noproxy '*' -ikS -X POST -d "$NODES_IPS" https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body will contain a request ID you need to check the firewall rules status.

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Verify firewall rules

Set the request ID environment variable on **seed node** only. The request ID is from the response in the previous API call.

```
REQ_ID=<topology-configuration-request-id>
```

To check the firewall rules status, run the following cluster API call only on the **seed node**:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/clusterNodes/currentDc/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code from this call isn't `200`, try again after a few minutes.

## Step 8 Install second data center nodes

### Install nodes in Target-DC

Run the following command on every node in **Target-DC**. Follow the installation prompts as this will be a typical node installation.

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter $TDC_NAME --seed-auth $API_TOKEN
```

The installation takes from 3 through 5 minutes. The expected result is similar to this:

```
Installation in new data center completed successfully after 2 minutes 51 seconds.
```

### Check Nodekeeper in Target-DC

Run the following cluster API call only on the **seed node** when all nodes in **Target-DC** finish installing:

```
curl -ikS https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/nodekeeper/healthCheck?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 9 Migrate Cassandra

Cassandra migration may take minutes to hours depending on your metric storage size.

### Migrate Cassandra

To start migration of Cassandra in **Target-DC**, run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body will contain a request ID which you need to check migration status. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<migration-new-datacenter-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Check migration status

To check the migration status, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/newDc/$REQ_ID?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Rebuild Cassandra data

Rebuild Cassandra data and Verify Cassandra state for Dynatrace release 254 and earlier.

Depending on the size of your Cassandra database, this process can take several hours.

#### Rebuild data

To rebuild Cassandra, run the following command on each new **Target-DC** node successively. Use the `nohup` command to prevent interruption of script execution (such as session disconnect) during important operations.

```
sudo nohup $DT_DIR/utils/cassandra-nodetool.sh rebuild -- $SDC_NAME &
```

#### Verify progress and status

To verify the progress and status, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuildStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after approximately 15 minutes. Remember that the rebuild process can be time-consuming.

### Verify Cassandra state

To verify Cassandra cluster state, run the `cassandra-nodetool.sh` with the `status` parameter only on the **seed node**:

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

The **Load** value shouldn't differ significantly between the nodes and **Status** should be `UN` on all nodes.

Depending on the size of your Cassandra database, this can take several hours.

### Rebuild data

To rebuild Cassandra data in **Target-DC**, run the following cluster API call only on the seed node:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200`. If the status code isn't `200` and the response doesn't suggest the following steps, contact a Dynatrace product expert via live chat within your Dynatrace environment.

### Check the rebuild data status

To check the rebuild data status, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/cassandra/rebuild?Api-Token=$API_TOKEN -H  "accept: application/json" -H  "Content-Type: application/json"
```

If the status code isn't `200`, try again after approximately 15 minutes. Remember that the rebuilding data process can be time-consuming.

If the response has an error flag set to `true`, contact a Dynatrace product expert via live chat within your environment.

## Step 10 Migrate Elasticsearch

Elasticsearch migration may take minutes or hours depending on your Elasticsearch storage.

### Migrate Elasticsearch to Target-DC

Start Elasticsearch. Run the following command successively on every node in **Target-DC** only:

```
sudo $DT_DIR/launcher/elasticsearch.sh start
```

To start migration of Elasticsearch to **Target-DC**, run the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200`.

### Verify progress and status

To check the migration status of Elasticsearch, run the following cluster API call only on the seed node:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/elasticsearch/recover?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

### Verify data migration

To verify Elasticsearch data migration, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/migration/elasticsearch/indexMigrationStatus?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 11 Migrate the server

### Migrate server

Launch the **Managed Cluster** in **Target-DC** by running the following cluster API call only on the **seed node**:

```
curl -ikS -X POST https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If successful, the status code is `200` and the response body will contain a request ID which you need to check cluster readiness. Set the request ID environment variable only on the **seed node**. The request ID is from the response in the previous API call.

```
REQ_ID=<migration-server-request-id>
```

If the status code isn't `200` and the response doesn't suggest next steps, contact a Dynatrace product expert via live chat.

### Check cluster readiness

To check if the Managed Cluster is ready, run the following cluster API call only on the **seed node**:

```
curl -ikS -X GET https://$SEED_IP/api/v1.0/onpremise/multiDc/restore/server/recovery/$REQ_ID?Api-Token=$API_TOKEN -H "accept: application/json" -H "Content-Type: application/json"
```

If the status code isn't `200`, try again after a few minutes.

## Step 12 Enable the new data center

1. Turn on OneAgent traffic.  
   For details, see [Cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").
2. Turn on backup in one of the DCs. Migration turns off backup.  
   For details, see [Back up and restore a cluster](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").