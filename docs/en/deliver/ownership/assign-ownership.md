---
title: Assign ownership teams to monitored entities
source: https://www.dynatrace.com/docs/deliver/ownership/assign-ownership
scraped: 2026-02-26T21:33:18.745570
---

# Assign ownership teams to monitored entities

# Assign ownership teams to monitored entities

* How-to guide
* 9-min read
* Updated on Sep 16, 2025

You can assign [team owners](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") to **any monitored entity** in Dynatrace using the main team identifier or supplementary identifiers (defined when [setting up a team](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.")). This makes it easier to find the responsible team instantly and contact them if any issue arises with an entity, for example, if the entity is affected by a vulnerability.

You can apply ownership using several methods such as Kubernetes labels and annotations, host metadata, environment variables, and tags (including via the Dynatrace [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")).

## Supported methods of applying ownership

The following methods for applying ownership and entity types are supported.

* **Deployment or configuration metadata** Recommended

  | Method | Entity types |
  | --- | --- |
  | Kubernetes labels and annotations | All Kubernetes objects |
  | Host metadata via `oneagentctl` or `hostcustomproperties.conf` | Hosts |
  | Environment variables | Processes |
* **Tags** (manual, automated, and via API)âall monitored entities

We highly recommend that you use the preferred method for applying ownership based on entity type, as described in the sections that follow.

* [Kubernetes labels and annotations for Kubernetes objects](#kubernetes)
* [Metadata for hosts](#host-metadata)
* [Environment variables for processes](#process-env-variables)
* [Tags (manual, automated, and via API) for all other entities](#tags)

Our recommendations are based on the most efficient methods to ensure that entities have adequate ownership coverage. See [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage") for more information.

## Format for applying ownership information

Regardless of the method used, ownership information is applied to entities in **key-value pairs**. The default keys `owner` and `dt.owner` are available in every monitoring environmentâsee **Settings** > **Ownership** > **Configuration**. You can, however, change or delete the default keys and [define your own](#custom-keys).

The value is always the unique team identifier specified when creating a team. You can also use supplementary identifiers. (See [Create and manage teams for entity ownership](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") for more information on defining these values.)

An entity can have more than one ownership team. You can effect this by applying multiple key-value pairs, as shown in the sections that follow.

### Custom keys for ownership information

You can define up to a maximum of five keys for applying ownership information.

1. Go to **Settings** > **Ownership** > **Configure**.
2. Select **Add key**.
3. Enter the key (**Enabled** by default).
4. **Save changes**.

![Custom keys for ownership](https://dt-cdn.net/images/ownership-custom-keys-1482-1a7f6383f7.png)

When you **disable or delete a key**, entities assigned to teams via such keys will no longer display or hold ownership metadata. However, such keys will appear as regular tags applied to the entities.

### Additional requirements for ownership keys

* You can define a maximum of five and a minimum of one key.
* You can use any of your defined keys as a prefix in key-value pairs. For example, for the keys `owner` and `dt.owner`, you can use `owner-1` and `dt.owner-test`.

## Kubernetes labels and annotations

You can specify team ownership for different Kubernetes objects such as Deployments, Pods, Services, or namespaces. To ensure that Kubernetes objects have adequate ownership coverage, which is especially important for short-lived entities like Pods, provide ownership information as Kubernetes labels or annotations with [key-value pairs](#format) in the deployment specification file, for example, `deployment.yaml`.

We recommend defining ownership for the Deployment and all other objects for which you want ownership coverage. See also [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

* Setting a team identifier as a label or annotation for the Deployment, CronJob, Job, DaemonSet, or StatefulSet provides team ownership information for the respective `CLOUD_APPLICATION` entities. Note that this ownership is not propagated to the `CLOUD_APPLICATION_INSTANCE`.

  In this example, dual ownership is set via two labels for the Deployment. Each label has a unique key. **Unique keys are a requirement in Kubernetes labels and annotations**.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  labels:



  dt.owner-1: my-team-1 # Dual team ownership defined for the Deployment



  dt.owner-2: my-team-2



  spec:
  ```

  The sample code below shows an annotation for ownership at the Deployment level.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  annotations:



  dt.owner: my-team # Ownership defined for the Deployment
  ```
* Set labels for Pods to specify ownership for the respective `CLOUD_APPLICATION_INSTANCE` entity. Specify ownership for each Pod.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  spec:



  replicas: 3



  selector:



  matchLabels:



  app: demo



  template:



  metadata:



  labels:



  app: demo



  dt.owner: my-team # Ownership defined for the Pod



  spec:
  ```

  The sample code below shows the manifest for a Pod that has the annotation `dt.owner: myTeam`.

  ```
  apiVersion: v1



  kind: Pod



  metadata:



  name: annotations-demo



  annotations:



  imageregistry: "https://hub.docker.com/"



  dt.owner: my-team



  spec:



  containers:



  - name: nginx



  image: nginx:1.14.2



  ports:



  - containerPort: 80
  ```
* For a **process**, specify ownership using key-value pairs with the `DT_CUSTOM_PROP` **environment variable**, which is defined for the container.

  In environment variables, you can provide multiple values for the same key. In this example, dual ownership is defined using the key `owner`.

  ```
  apiVersion: apps/v1



  kind: Deployment



  metadata:



  name: demo



  spec:



  replicas: 3



  selector:



  matchLabels:



  app: demo



  template:



  spec:



  containers:



  - name: demo



  image: demo:1.0.0



  env:



  - name: DT_CUSTOM_PROP ## Environment variable



  value: "owner=team-automation owner=team-dev" # Dual ownership for the process; team IDs are team-automation and team-dev.
  ```
* Kubernetes labels for a Service

  ```
  apiVersion: v1



  kind: Service



  metadata:



  name: my-service



  labels:



  dt.owner: team-a # Ownership defined for the Service



  spec:



  selector:



  app.kubernetes.io/name: MyApp



  ports:



  - protocol: TCP



  port: 80



  targetPort: 9376
  ```
* Kubernetes labels for a namespace

  ```
  apiVersion: v1



  kind: Namespace



  metadata:



  name: my-namespace



  labels:



  dt.owner: team-a # Ownership defined for the namespace
  ```

## Host metadata

For hosts, we recommend using [host metadata](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.") as the primary method of applying ownership.

Read more about [defining tags and metadata for hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") and the [OneAgent `oneagentctl` command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

You can also apply ownership to hosts using [tags](#tags).

### Via `oneagentctl`

OneAgent version 1.189+ For hosts with OneAgent version 1.189+, use the `oneagenctl` command-line interface after installation to set a metadata property for an individual host. Run `oneagentctl` with administrator or root privileges from these default locations.

* Windows: `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`
* All Unix-like systems: `/opt/dynatrace/oneagent/agent/tools`

This example for Unix-like systems uses `--set-host-property` to set ownership with the [key-value pair](#format) `owner-1=team-automation`, where `team-automation` is the [main team identifier or a supplementary identifier](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

```
./oneagentctl --set-host-property owner-1=team-automation
```

### Via `hostcustomproperties.conf`

OneAgent version 1.187 and earlier For hosts on OneAgent 1.187 and earlier, create or edit the `hostcustomproperties.conf` OneAgent configuration file at these locations.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* All Unix-like systems: `/var/lib/dynatrace/oneagent/agent/config`

This example for Unix-like systems sets host ownership with the [key-value pair](#format) `dt.owner-1=team-automation`, where `team-automation` is the [main team identifier or a supplementary identifier](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

```
cat hostcustomproperties.conf dt.owner-1=team-automation
```

## Process environment variables

For processes, we recommend specifying ownership in key-value pairs via the `DT_CUSTOM_PROP` environment variable.

We **do not recommend** using tags to apply ownership to processes or process groups.

Read more about [defining process group metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment."), for example, setting up the `DT_CUSTOM_PROP` environment variable for [IIS](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#iis "Configure your own process-related metadata based on the unique needs of your organization or environment.") and [Windows](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#windows "Configure your own process-related metadata based on the unique needs of your organization or environment.").

```
export DT_CUSTOM_PROP dt.owner=DemoTeam
```

See [Format for applying ownership information](#format) on all existing key-value options or to create your own.

## Tags

**Use tags to apply ownership only for entities that aren't covered by the methods described above**. These are typically entities like frontend applications that are stable and fewer in number.

### Tagging methods

You can use tags to apply ownership in [key-value pairs](#format) to any monitored entityâread more about [tagging](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.").

![Ownership via a manual tag](https://dt-cdn.net/images/ownership-manual-tag-1004-f7c90a9b42.png)

* [Manual tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags#manual "Find out how to define and apply tags manually and automatically.") using the defined keys or key prefixes (like `owner` and `dt.owner`) are simple to apply via the web UI.
* You can also set up [automatic tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") via the web UI.
* We recommend using the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") over automatic tagging rules to apply ownership to entities. The Custom tags API enables you to conveniently apply tags to a large group of entities within a single API call, executed immediately.

Note that manually applied tags can be removed manually. Automatically applied tags canât be removed manually from individual services, process groups, process group instances, applications, or hosts.

See [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage") for more information on the benefits and limitations of tagging for assigning owners to entities. See also [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").

### Permissions

You require **all** the following permissions to add, change, or remove ownership via the Custom tags API.

* The `entities.write` [token permission](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")
* The `settings.read` token permission or the [IAM policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") `ALLOW settings:objects:read WHERE settings:schemaId = "builtin:ownership.teams";`

For adding, changing, or deleting tags via the web UI, you need the **Manage monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment or management-zone level.

## View ownership information in the web UI

Ownership information is only available for [unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.").

For hosts and all Kubernetes entities, select **Owners** on the entity details page to view ownership information.

This example shows a Kubernetes workload mapping to the `CLOUD_APPLICATION` entity. Expand a team name to view its details. Select ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in the **Ownership** card to [edit team details](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") in **Settings**.

![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

This example shows ownership information for a Kubernetes Pod.

![Owner of a Kubernetes Pod](https://dt-cdn.net/images/ownership-k8s-pod-2214-e55133496a.png)

On the **Hosts** page, you can search for hosts with ownershipâfilter by **Tags** with the key prefixes you have defined, for example, `owner` and `dt-owner`. Note that [ownership key-value pairs](#format) must be applied to at least one host for the key to be available in the **Tags** filter. This method of searching for ownership is available on all entity group pages that can be filtered by tags.

![Filter by ownership tags on entity group pages](https://dt-cdn.net/images/ownership-hosts-page-2190-8b47f48119.png)

In the example host details page below, the host has three team owners. One of the owners is marked **Unknown team identifier**. This is because even though the team identifier has been applied to the host (for example, via [oneagentctl](#oneagentctl) or a [manual tag](#tags)) in a key-value pair, the team doesn't exist. **Invalid team identifier** means that the team or supplementary ID was applied to the host in the wrong [format](#format).

Select **Properties and tags** to view all tags applied to the host.

![Owners of a host](https://dt-cdn.net/images/ownership-host-2199-95873a776f.png)

Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") next to the unknown team and then select **Add team** to define team information in **Settings**. The entity is then automatically updated with the team definition.

![Unknown team](https://dt-cdn.net/images/ownership-unknown-team-909-590ed7fbc0.png)

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Define tags and metadata for hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")
* [Define your own process group metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")
* [Tags and metadata](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.")
* [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
* [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")
* [Kubernetes labelsï»¿](https://dt-url.net/g442yn5 "Official Kubernetes documentation on labels")
* [Kubernetes annotationsï»¿](https://dt-url.net/bz62yto "Official Kubernetes documentation on annotations")
* [Unified analysis pages](/docs/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.")