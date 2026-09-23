---
title: Combine Premium High Availability with rack awareness
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/pha-rack-aware
---

# Combine Premium High Availability with rack awareness

# Combine Premium High Availability with rack awareness

* How-to guide
* 10-min read
* Published Sep 18, 2026

To run Premium High Availability (PHA) and rack awareness together, so each of your two data centers holds three racks, follow the steps below.

This procedure uses these terms:

* **DC-1**: Data center that holds the initial Managed Cluster
* **DC-2**: Additional data center for the PHA deployment
* **rack**: Fault domain within a data center

Before a data center uses rack awareness, it has one rack, `rack1`, and replicas sit on other nodes inside it. Converting to rack awareness creates the additional racks, `rack2` and `rack3`, and only then does that layout become visible.

The starting point for this procedure depends on what you have today:

| Starting point | Recommended path |
| --- | --- |
| No Managed Cluster yet | Install DC-1 rack-aware from the start, then add DC-2 |
| An existing Managed Cluster, not yet PHA | Convert DC-1 to rack awareness, then add DC-2 |
| An existing PHA deployment | Convert DC-1 to rack awareness, then rebuild DC-2 |

Dynatrace recommends making both data centers rack-aware. A rack-aware DC-2 alongside a non-rack-aware DC-1 works, but once more than one rack name exists in the Managed Cluster, every node you later add to either data center must pass `--rack-name`, or the join is rejected. Only one node operation runs at a time across the whole Managed Cluster, so plan the two data centers sequentially—DC-1 first is the usual order, but not a requirement.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Plan the target topology**](/managed/managed-cluster/high-availability/pha-rack-aware#plan-topology "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Check the combined prerequisites**](/managed/managed-cluster/high-availability/pha-rack-aware#check-prerequisites "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Make DC-1 rack-aware**](/managed/managed-cluster/high-availability/pha-rack-aware#rack-aware-dc-1 "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Confirm DC-1 is stable**](/managed/managed-cluster/high-availability/pha-rack-aware#confirm-dc-1 "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Bring DC-2 into the topology**](/managed/managed-cluster/high-availability/pha-rack-aware#rack-aware-dc-2 "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Verify the deployment**](/managed/managed-cluster/high-availability/pha-rack-aware#verify "Combine Premium High Availability with rack awareness so each data center holds three racks and the cluster spans six independent fault domains.")

## Step 1 Plan the target topology

Each data center holds exactly three racks, matching the replication factor of Dynatrace data storage. Dynatrace doesn't enforce a specific number of nodes per rack, but the number you choose determines how much protection rack awareness adds.

| Nodes per rack | Nodes per DC | Total nodes | Use this when |
| --- | --- | --- | --- |
| 1 | 3 | 6 | Not recommended—rack awareness adds no failover tolerance |
| 2 | 6 | 12 | Limited failover tolerance |
| 3 | 9 | 18 | **Recommended for production** |
| 4 | 12 | 24 | Scale for capacity |
| 5 | 15 | 30 | Maximum—15 nodes per DC |

Six nodes meets the PHA minimum, but it leaves one node per rack, where rack awareness gains no failover tolerance. Dynatrace recommends three nodes per rack for production deployments—nine nodes per DC, eighteen total.

### Why three nodes per rack

With one node per rack, the rack is the node, so a rack failing is the same as a node failing, which a standard high-availability deployment already tolerates. A second failure then always falls in a different rack, which Dynatrace treats the same way it would treat a second failed node. Rack awareness buys nothing in that layout, yet still costs the same as a real one: you still owe the 10 ms inter-rack latency and physical-placement prerequisites for three racks, and each single-node rack holds a full replica—100% `Owns (effective)` instead of 33.3% at three nodes per rack—tripling per-node disk usage.

With three nodes per rack, a whole rack failing counts as multiple nodes failing in the same rack, which Dynatrace still considers the data center healthy. That's rack awareness working as intended.

Both DCs may use the same rack names—`rack1`, `rack2`, and `rack3` in each. Dynatrace scopes rack names per data center, not globally, so reusing the same three names in DC-2 is expected. Matching names across the two data centers also keeps `cassandra-nodetool.sh status` output easier to compare, since the same three names appear under each data center's section.

Always supply `--rack-dc` and `--rack-name` together, and set `--rack-dc` to the same value as `--datacenter`—the installer refuses to proceed otherwise. With rack names repeating across data centers, `--rack-dc` is the only thing that tells Dynatrace which data center's rack a node belongs to.

Once the Managed Cluster holds more than one rack name, a joining node that omits `--rack-name` is rejected instead of defaulting to `rack1`, so you can't accidentally forget the rack parameters on a node you add later.

Dynatrace doesn't enforce the number of racks or the number of nodes per rack, so meeting the [rack awareness requirements](/managed/managed-cluster/high-availability/rack-awareness#rack-awareness-requirements "Learn how rack awareness groups Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.") is your responsibility.

At nine nodes per DC, not every node serves web UI traffic by default. Use the [Cluster REST API](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.") to set which nodes serve the UI.

## Step 2 Check the combined prerequisites

Before you begin, confirm your deployment meets the prerequisites from both features.

### From Premium High Availability

Review the [PHA requirements and limitations](/managed/managed-cluster/high-availability/multi-data-centers#requirements-and-limitations "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers."), including the license model, network latency, and node count bounds.

### From rack awareness

Review the [rack awareness requirements](/managed/managed-cluster/high-availability/rack-awareness#rack-awareness-requirements "Learn how rack awareness groups Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss."), including the low-latency network requirement between racks.

### Only from the combination

* Ensure your system meets the [hardware and operating system requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") for [multi-node installations](/managed/managed-cluster/installation/managed-hardware-requirements#multi-node-install "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure."), and review the [storage requirements](/managed/managed-cluster/installation/managed-hardware-requirements#storage "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") for eighteen nodes rather than six.
* Ensure your operating system meets the [operating system requirements](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") for every node in both data centers.

## Step 3 Make DC-1 rack-aware

New Managed Cluster

Existing Managed Cluster, not yet PHA

Existing PHA deployment

If you don't have a Managed Cluster yet, install DC-1 rack-aware from the start. Follow [Install Dynatrace Managed](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") and append the rack parameters to the installation command, cycling the rack name across the three racks you want DC-1 to have:

```
dynatrace-managed.sh --rack-dc <dc-1-name> --rack-name <rack>
```

Replace `<dc-1-name>` with the name of DC-1, and `<rack>` with `rack1`, `rack2`, or `rack3` depending on which rack the node belongs to.

If you already have a single Managed Cluster that isn't yet rack-aware, convert it before you add DC-2.

Choose a conversion method based on your metric storage size:

* Use [rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") for a Managed Cluster where one node can contain a full replica.
* Use [rack-aware conversion using restore](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Managed Cluster to a rack-aware deployment using the restore method, including preparation and installer parameters.") when your metric storage per node exceeds the replication method's limit.

If DC-1 is already part of a PHA deployment, use the [rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") method only. The restore method isn't supported on a PHA cluster. It stops every node in the Managed Cluster at once and reinstalls from a single node list, and in a PHA deployment that list spans both data centers, leaving nothing running to serve traffic while the restore completes.

The replication method converts DC-1 one node at a time, so DC-1 keeps serving traffic throughout. Each node operation still blocks all other cluster operations across the whole Managed Cluster, including DC-2, for one to two days at a time, and a removed host needs 72 hours before you can reattach it.

Add nodes to DC-1 using [Add a Managed Cluster node](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress."), with the rack parameters plus the parameters that place the node in DC-1:

```
dynatrace-managed-installer.sh --seed-auth <api-token> --premium-ha on --datacenter <dc-1-name> --datacenter-topology <dc-1-name>,<dc-2-name> --rack-name <rack> --rack-dc <dc-1-name>
```

Replace `<api-token>` with the authentication token from the seed node, `<dc-1-name>` and `<dc-2-name>` with the two data center names, and `<rack>` with the rack the node joins. The installer enforces four rules here: `--rack-dc` must carry the same value as `--datacenter`; `--datacenter` requires `--premium-ha on`; `--datacenter` requires `--datacenter-topology`; and the data center must appear in that topology list.

Don't use the plain `--rack-dc`/`--rack-name` command shown on [Rack-aware conversion using replication](/managed/managed-cluster/high-availability/rack-aware-replication#extend-racks "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") to add a node to a PHA cluster. Without `--datacenter` and `--datacenter-topology`, the node joins with no data center assigned, which breaks Elasticsearch discovery, skips Elasticsearch cross-cluster replication, and can cancel the installation outright if data center-scoped backup is on.

When DC-1 is converted, continue to step 5 to rebuild DC-2. Don't convert DC-2 in place—DC-2 is rebuilt instead, in step 5.

## Step 4 Confirm DC-1 is stable

While DC-1 has three racks and DC-2 has fewer, Dynatrace evaluates DC-2's health node by node instead of rack by rack, so DC-2 is briefly less fault-tolerant than a fully racked data center. This is expected and not a cause for concern: the [DC-health rules](/managed/managed-cluster/high-availability/failover#rack-awareness "The Premium High Availability failover mechanism detects node outages exceeding 15 minutes and transfers server responsibility to a healthy data center.") still apply throughout, and if DC-1 has a problem, DC-2 is still there to take over.

Confirm DC-1 is fully converted and healthy before you continue to DC-2. Dynatrace Managed blocks all other cluster operations while a node operation is in progress, so you can't work on DC-1 and DC-2 at the same time.

Converting a nine-node data center by replication means six to twelve serialized node operations at one to two days each, so plan for roughly one to three weeks, plus a possible multi-day wait for the first node's Cassandra bootstrap. Six of those operations are additions, to populate `rack2` and `rack3`. The rest are removals of the `rack1` nodes whose capacity moved to the new racks and are no longer needed. A data center that started at three nodes needs no removals, while one that started at nine needs six removals and briefly reaches fifteen nodes before settling back at nine. Because DC-1 and DC-2 can't be converted in parallel, their durations add together.

## Step 5 Bring DC-2 into the topology

Whether DC-2 doesn't exist yet or you're rebuilding an existing one, the underlying command is the same—only the surrounding procedure differs:

```
sudo /bin/sh ./managed-installer.sh --install-new-dc --premium-ha on --datacenter <dc-2-name> --seed-auth <api-token> --rack-dc <dc-2-name> --rack-name <rack>
```

This is the command from the install-nodes step of whichever procedure you follow below, with the rack parameters added. `--rack-dc` takes the same value as `--datacenter`. Cycle `<rack>` across `rack1`, `rack2`, and `rack3` for DC-2's nodes so the three racks end up with equal node counts—reusing DC-1's rack names is expected. The two procedures below name the `<dc-2-name>` variable differently, so use whichever your procedure defines.

DC-2 doesn't exist

DC-2 already exists

Follow [Add a data center](/managed/managed-cluster/high-availability/add-data-center "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication."), and add the rack parameters to the command in [Install second data center nodes](/managed/managed-cluster/high-availability/add-data-center#install-nodes "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.").

Install all three racks. Dynatrace ignores racks in a data center that has only one or two.

This is the supported way to make an existing DC-2 rack-aware: follow [Rebuild a data center](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers."), and add the rack parameters to the command in [Install second data center nodes](/managed/managed-cluster/high-availability/rebuild-data-center#install-nodes "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.").

That procedure is written for a lost data center, and its early steps terminate DC-2's nodes and remove DC-2 from the cluster configuration. Here, you perform those same steps on purpose, against a healthy DC-2, to rebuild it rack-aware. Its Source-DC is DC-1 and its Target-DC is DC-2.

Nothing in Dynatrace Managed or Mission Control checks whether DC-2 is unhealthy before you remove it, and nothing notifies Dynatrace that a rebuild is underway. Between removing DC-2 and completing its reinstallation, your Managed Cluster runs on DC-1 alone, with no second data center to fail over to.

Backup stays disabled for the whole rebuild, not only while DC-2 is down, and automatic outage detection has nothing to evaluate during this window, because it requires two data centers. Make sure DC-2's nodes are fully removed before you continue: the data center topology step fails if any of them are still cluster members.

## Step 6 Verify the deployment

Run `cassandra-nodetool.sh status` on the seed node, and confirm the output shows:

* Two `Datacenter:` sections, one for each data center
* Three distinct rack values within each section
* Every node showing status `UN`
* Equal node counts across the three racks in each data center

Example output

```
Datacenter: datacenter1



=======================



Status=Up/Down



|/ State=Normal/Leaving/Joining/Moving



--  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



UN  10.176.41.10   19.12 GB   256          33.3%             3af25127-4f99-4f43-afc3-216d7a2c10f8  rack1



UN  10.176.41.11   19.18 GB   256          33.3%             5a618559-3a73-42ec-83f0-32d28e08beec  rack1



UN  10.176.41.12   19.44 GB   256          33.3%             191f3b30-949a-4cf2-b620-68a40eebf31e  rack1



UN  10.176.41.20   19.08 GB   256          33.3%             852ce236-a430-400a-92a6-daeed99acf68  rack2



UN  10.176.41.21   19.31 GB   256          33.3%             84479219-b64d-442c-a807-a832db9aae18  rack2



UN  10.176.41.22   19.27 GB   256          33.3%             507b377c-5bfc-4667-b251-a9b7c453ed22  rack2



UN  10.176.41.30   19.15 GB   256          33.3%             48543bca-41f5-26d3-b2fd-6cfdf5c0f3b2  rack3



UN  10.176.41.31   19.02 GB   256          33.3%             2aa7e790-a423-9273-88f9-45bcd158dd6e  rack3



UN  10.176.41.32   19.36 GB   256          33.3%             f053dd8d-ecf3-7834-b099-68542439817b  rack3



Datacenter: dc-us-east-2



========================



Status=Up/Down



|/ State=Normal/Leaving/Joining/Moving



--  Address        Load       Tokens       Owns (effective)  Host ID                               Rack



UN  10.176.42.10   19.21 GB   256          33.3%             a1b2c3d4-4f99-4f43-afc3-216d7a2c10f8  rack1



UN  10.176.42.11   19.09 GB   256          33.3%             b2c3d4e5-3a73-42ec-83f0-32d28e08beec  rack1



UN  10.176.42.12   19.33 GB   256          33.3%             c3d4e5f6-949a-4cf2-b620-68a40eebf31e  rack1



UN  10.176.42.20   19.17 GB   256          33.3%             d4e5f6a7-a430-400a-92a6-daeed99acf68  rack2



UN  10.176.42.21   19.24 GB   256          33.3%             e5f6a7b8-b64d-442c-a807-a832db9aae18  rack2



UN  10.176.42.22   19.11 GB   256          33.3%             f6a7b8c9-5bfc-4667-b251-a9b7c453ed22  rack2



UN  10.176.42.30   19.29 GB   256          33.3%             a7b8c9d0-f41f-26d3-b2fd-6cfdf5c0f3b2  rack3



UN  10.176.42.31   19.06 GB   256          33.3%             b8c9d0e1-a423-9273-88f9-45bcd158dd6e  rack3



UN  10.176.42.32   19.38 GB   256          33.3%             c9d0e1f2-ecf3-7834-b099-68542439817b  rack3
```

## Related topics

* [Rack awareness](/managed/managed-cluster/high-availability/rack-awareness "Learn how rack awareness groups Cluster nodes into three fault domains to ensure resilience against a full rack outage and data loss.")
* [Multi-data center high availability](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.")
* [Add a data center](/managed/managed-cluster/high-availability/add-data-center "Learn how to replicate Cluster nodes across two data centers to set up a Premium High Availability deployment with cross-data center replication.")
* [Multi-data center failover](/managed/managed-cluster/high-availability/failover "The Premium High Availability failover mechanism detects node outages exceeding 15 minutes and transfers server responsibility to a healthy data center.")