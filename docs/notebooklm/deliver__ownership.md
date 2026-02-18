# Dynatrace Documentation: deliver/ownership

Generated: 2026-02-18

Files combined: 3

---


## Source: assign-ownership.md


---
title: Assign ownership teams to monitored entities
source: https://www.dynatrace.com/docs/deliver/ownership/assign-ownership
scraped: 2026-02-17T21:25:11.822782
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


---


## Source: best-practices.md


---
title: Best practices for entity ownership
source: https://www.dynatrace.com/docs/deliver/ownership/best-practices
scraped: 2026-02-17T05:08:43.800611
---

# Best practices for entity ownership

# Best practices for entity ownership

* 5-min read
* Updated on Apr 25, 2023

These best practices and tips for ownership are designed to help you:

* Capture ownership for short-lived entities such as process group instances and Kubernetes Pods.
* Minimize the time taken for tagging runs.
* Scale the assignment of ownership effectively for large, complex environments.
* Provide ownership coverage for entities by assigning teams at the time of deployment.
* Maintain adequate team information for routing and display.

## Ownership assignment

We recommend that you **assign owners to critical entities**. These are entities that experience a high number of outages or security issues, have high throughput, are business critical, or are customer facing.

**Use these recommended methods for applying ownership based on entity type**; while you can use tags to apply ownership to any monitored entity, these recommended methods are the most efficient ways to assign entities to owners.

* [Kubernetes labels for Kubernetes objects](/docs/deliver/ownership/assign-ownership#kubernetes "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Metadata for hosts](/docs/deliver/ownership/assign-ownership#host-metadata "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Environment variables for processes](/docs/deliver/ownership/assign-ownership#process-env-variables "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Tags (manual, automated, and via API) for all other entities](/docs/deliver/ownership/assign-ownership#tags "Assign owners to entities using entity metadata like labels, environment variables, and tags.")

### Kubernetes

For [Kubernetes objects](/docs/deliver/ownership/assign-ownership#kubernetes "Assign owners to entities using entity metadata like labels, environment variables, and tags."), **define ownership simultaneously for all desired Kubernetes objects**. This ensures that all your Kubernetes objects have adequate ownership coverage at the time of deployment.

* Always apply labels for the **Deployment**.
* We recommend specifying ownership for at least the `CLOUD_APPLICATION` (for example, the Deployment, Job, CronJob, or DaemonSet) and the `CLOUD_APPLICATION_INSTANCE` (Pods) entities.
* Unique keys are a requirement in [key-value pairs](/docs/deliver/ownership/assign-ownership#format "Assign owners to entities using entity metadata like labels, environment variables, and tags.") in Kubernetes labels. Keys must begin with the [custom key names you define for ownership information](/docs/deliver/ownership/assign-ownership#custom-keys "Assign owners to entities using entity metadata like labels, environment variables, and tags."). For example, you can use `owner` and `dt.owner` as prefixes to create unique keys.

Sample Kubernetes deployment file with ownership defined for Deployment, Pod, and process

```
apiVersion: apps/v1



kind: Deployment



metadata:



name: demo



labels:



dt.owner-1: my-team-1 # Dual team ownership defined for the Deployment



dt.owner-2: my-team-2



spec:



replicas: 1



selector:



matchLabels:



app: demo



template:



metadata:



labels:



app: demo



dt.owner-1: my-team-1 # Ownership defined for the Pod



spec:



containers:



- name: demo



image: demo:1.0.0



ports:



- containerPort: 8888



env:



- name: DT_CUSTOM_PROP # Environment variable



value: 'dt.owner-1=my-team-1' # Ownership defined for the process
```

### Tags

**Use [tags to apply ownership](/docs/deliver/ownership/assign-ownership#tags "Assign owners to entities using entity metadata like labels, environment variables, and tags.") only for entities that aren't covered by other methods**.

#### Advantages and uses of tags

* Tags are appropriate for assigning a **few stable entities** (for example, an application and the synthetic monitors running against it) to specific ownership teams.
* [Manual tagging](/docs/manage/tags-and-metadata/setup/how-to-define-tags#manual "Find out how to define and apply tags manually and automatically.") or the [Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") are effective in applying ownership to **existing (already deployed) entities**.
* [Automatic tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") have the advantage of capturing **new entities** that match your tagging rules. Automatically applied tags also can't be removed manually from individual services, process groups, process group instances, applications, or hosts.
* While the Custom tags API and automatic tagging rules both use the powerful and flexible [**entity selector**](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") for selecting entities, the **Custom tags API call is executed immediately**. This is a [major advantage over automatic tagging rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale#custom-tags-api "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") that are scheduled via the Dynatrace tagging process. This helps you speed up execution time when complex tagging rules are necessary.

#### Important considerations when using tags for ownership

* **Manual tagging** doesn't **scale** adequately for assigning ownership in large, dynamic monitoring environments. Manual tags can also be removed manually.
* While (web UIâbased) **automatic tagging rules** are designed for complexity, automatic tagging runs can take a **long time** to be completed, depending on the complexity of your rules and the size of your environment. Meanwhile, a critical entity experiencing an issue could miss being tagged with ownership. Read more about optimizing tagging in [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").
* While the **Custom tags API call** is executed immediately, the tradeoff is that it's a **one-time operation**. Depending on the frequency of your tagging runs, new or short-lived entities could miss being tagged with ownership information entirely, making it difficult to find owners in case of vulnerabilities or outages.
* We **do not recommend** using tags to apply ownership to processes or process groups.

## Team information

While only the **Team name** and **Team identifier** fields are required for creating an [ownership team](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership."), here are some suggestions and best uses of other fields.

* When defining [custom keys](/docs/deliver/ownership/assign-ownership#custom-keys "Assign owners to entities using entity metadata like labels, environment variables, and tags.") for ownership identifiers, use specific, easily understandable names that are not likely to be used for other tagging needs.
* Always add a team **Description**âthis is displayed along with the team name on the **Ownership teams** settings page and helps to differentiate teams at a glance. Teams with no description or a poor name (team 1) offer no clues as to their role in your organization. Teams with descriptions (2 and 3) are more identifiable.

  ![Team definitions](https://dt-cdn.net/images/ownership-team-definitions-1888-78e12327f8.png)
* **Supplementary identifiers**âyou can define up to three per teamâare especially useful when:

  + Your team name changesâyou can add a supplementary identifier to reflect the name change while leaving the main team identifier unchanged. (Once created, the main team identifier cannot be edited or changed.)
  + You want to define sub-teams. Create a supplementary ID for each sub-teamâyou can use the main team ID as a prefix. For example, for the main team ID `team1`, create the supplementary IDs `team1-taskforce` and `team1-planning`.

  Supplementary identifiers give you more flexibility.

  + Whether you apply a team's main ID or supplementary ID to an entity, it's marked as belonging to the same named team.
  + Supplementary IDs may be changed and deleted.
  + A supplementary identifier can be the same as the main or supplementary identifier of another team. In such a case, both teams are marked as owners when the supplementary identifier is applied to an entity.
* Always select team **Responsibilities**, even though they aren't required. Responsibilities are displayed prominently along with team descriptions on an entity's **Ownership** card. These pieces of team information are key indicators for adding contact information for message routing and escalations.

  ![Ownership card](https://dt-cdn.net/images/ownership-card-responsibilities-905-94c952fe00.png)
* Define at least one email or Slack channel per team in **Contact details** so you can create an automated workflow with a targeted notification or simply extract any monitored entity's contact information when you need to.
* For **Additional information**, while you can define custom key-value pairs ad hoc, we recommend rationalizing the keys across teams so they can be reused for the same kinds of information. For example, use the same or related keys to define cost center information and another set of keys across your organization to define team hierarchies and relationships.

## Related topics

* [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")


---


## Source: ownership-teams.md


---
title: Create and manage teams for entity ownership
source: https://www.dynatrace.com/docs/deliver/ownership/ownership-teams
scraped: 2026-02-18T05:53:30.335737
---

# Create and manage teams for entity ownership

# Create and manage teams for entity ownership

* How-to guide
* 8-min read
* Updated on Nov 07, 2023

Ownership for monitored entities is defined within **teams**. You can set up ownership teams in the web UI, via API, and using [Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform."). Each team has a **unique identifier** that is the basis for [applying ownership to entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") by different methods (Kubernetes labels and annotations, host metadata, environment variables, or tags). Additionally, team definitions consist of names, descriptions, important routing information for notifications (via Microsoft Teams, Slack, Jira, and email), responsibilities (such as operations or security), and additional helpful links.

Team settings are based on the [Settings 2.0 framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework"), which defines each team configuration as a settings object based on the ownership schema, whether you use API, Configuration as Code, imported data from third-party databases, or the web UI at **Settings** > **Ownership**.

Ownership information attached to monitored entities aids in mapping your Dynatrace environment to the right teams for collaboration, issue resolution, and vulnerability escalation.

## Permissions

You need **any** of the following permissions to create, edit, or delete a team via API.

* The `settings.write` [token permission](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")
* The [IAM policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") `ALLOW settings:objects:write, settings:schemas:read WHERE settings:schemaId = "builtin:ownership.teams";`

You need the **Manage monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment or management-zone level to create teams via the web UI.

## Create a team via web UI

To create a team via the Dynatrace web UI

1. Go to **Settings** > **Ownership** > **Teams**.

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)
2. Select **Add team**.
3. Required Start by providing a **Team name**.

In ownership team data [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), the `displayName` import parameter from `get_groups` is set as the **Team name**.

4. Required The **Team identifier** is auto-populated based on the team name. Use the default identifier or provide your own.

   **Requirements**

   Team identifiers are the basis of [applying ownership to entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags."), regardless of the method. Main team identifiers must be unique across your environment. However, you may reuse the identifier of a previously deleted team.

   * Identifiers must be unique; no two main team identifiers can be the same.
   * Identifiers must be between 1 and 100 characters long.
   * They must begin and end with a letter (`[a-zA-Z]`).
   * They can contain hyphens (`-`), underscores (`_`), and alphanumerics between the opening and closing characters. Blank spaces and other special characters are not supported.
   * Once created, a main **team identifier cannot be edited or changed**.

   In team information [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), this field is set to the corresponding group's **Object Id** in Entra ID and cannot be edited. The **External ID** of the imported ownership team in Dynatrace is also set to this value.
5. Add a **Description** that aids in differentiating the team, for example, by entities managed or by responsibility. This description is appended to the team name for display on the **Ownership teams** page.
6. Optionally, specify **Supplementary identifiers**. Select **Add supplementary identifier** to provide up to three additional identifiers, for example, to identify sub-teams. When assigning ownership to entities, you can use the main team identifier or any of the supplementary identifiers to assign an entity to the named team.

   * Supplementary identifiers must meet the same character requirements as the main team ID.
   * A supplementary identifier cannot be the same as the main identifier of the same team.
   * Within a team, supplementary identifiers must be unique.
   * A supplementary identifier can be the same as the main or supplementary identifier of another team.
   * Unlike the main team identifier, supplementary identifiers **may be edited and deleted**.

   In ownership team data [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), the `mailNickname` import parameter from `get_groups` is set as a unique, human-readable **Supplementary Identifier**.
7. Select all **Responsibilities** that apply to the team. Although optional, these toggles provide critical metadata at a glance and help you specify the appropriate contact details.

   * **Development**âTeams responsible for developing and maintaining the underlying software code
   * **Security**âTeams tasked with assessing the impact and priority of vulnerabilities and responding to them
   * **Operations**âTeams that deploy and manage software, with a focus on performance and availability
   * **Infrastructure**âTeams responsible for installing and maintaining IT hardware
   * **Line of business**âTeams responsible for meeting customer and business goals
8. Add all **Contact details** that apply to the team. You can provide specific routing information for targeted notifications via email, Jira, Microsoft Teams, and Slack.

   You can add as many entries as required. Create a separate entry for each email address, Slack channel, Microsoft team, or Jira project you want to add.

   1. Select **Add contact information**.
   2. Select an **Integration type**.
   3. Provide details as follows:

      * **Email**âProvide a single **Email** address.
      * **Jira**âEnter the Jira **Project** name, **Default assignee** Required, and project **URL**.
      * **MS Teams**âProvide the **Team** name and **URL** (you can provide the link to a team channel from MS Teams).
      * **Slack**âProvide the **Channel** name and **URL**.
9. Provide any other **Links** describing the team or its responsibilities.
10. Select **Add link**.
11. Select the link **Type**, for example, **Documentation** or **Wiki**.
12. Provide the **URL**.

    You can add as many entries as required. Create a separate entry for each link you want to add.
13. Select **Add additional information** to provide additional key-value pairs in the **Name** and **Value** fields, for example, cost center names or organizational hierarchy information. You can also provide an optional **URL**.

    Keys for additional information:

    * Must be 1â100 characters long.
    * Can contain letters, numbers, special characters, and spaces.
14. Provide an **External ID** to be used only for automation purposes such as importing or updating team information. For example, use this field to store the unique ID assigned to a team in an external system such as Active Directory.

    * An external ID can only be specified during team creation.
    * Once created, an external ID **cannot be modified**.
    * This string can begin and end with and contain special characters, blank spaces, numbers, and letters.

    * External IDs cannot be used to apply ownership information to entities in key-value pairs; use the main team ID and supplementary IDs to assign entities to team owners.

    * In team information [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), this field is set to the corresponding group's **Object Id** from Entra ID and cannot be edited. The **Team identifier** of the imported ownership team is also set to this value.
15. **Save changes**.

See [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage") for more information about setting up teams optimally.

## Create a team via API and Configuration as Code

Team creation via the [**Settings API**](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") requires the ownership configuration [JSON schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") (`builtin:ownership.config`) provided by Dynatrace. You can retrieve the schema using the Settings API. Provide team configuration as a JSON payload.

[Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") enables you to use JSON templates and YAML files for team creation for one or multiple teams at the same time.

## Import teams via Workflows Workflows

You can import user groups from **Microsoft Entra ID** and **ServiceNow** as ownership teams within Dynatrace.
Therefore, see how to use the [`import_teams`](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information.") action and workflows for importing teams.

## Manage teams

You can manage (create, delete, edit) ownership teams via **Settings** > **Ownership** > **Teams** as well as the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

The **Ownership teams** settings page lists all teams (and their descriptions) in your environment, whether created via web UI or the API. Use the **Filter** field  to narrow this list by any string in a team name or description.

You can **Delete** a team from this view and expand **Details** to view and edit team information. You cannot, however, edit or delete the main team identifier.

### Revision history

Select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") in the upper-right corner of the **Ownership teams** page and then select **Revision history** for details of changes, including team creation, modification and deletion. Revisions are listed with **Timestamp**, the **Source** of the change (**Web UI** or **API**), and the **User** making the change.

![History of ownership teams](https://dt-cdn.net/images/ownership-teams-revisions-1462-e55719add4.png)

Expand to view the **Details** of any revision. Changes are color coded to show the **Original value** and any **New value**. The image below shows a deleted supplementary identifier.

![Revision simple view](https://dt-cdn.net/images/ownership-teams-revision1-1849-055f7f5d2e.png)

**Switch to advanced mode** and select **Show diff** to view the same changes as JSON objects. The **Key** displayed in advanced mode is a unique setting ID assigned to each team. Select the key to view the corresponding team's details.

![Revision YAML view](https://dt-cdn.net/images/ownership-teams-revision2-1848-06b3770890.png)

You can also filter revision history for a specific teamâpaste any setting ID **Key** into the **Filter** field .

### Additional team management

There are additional conveniences for team-specific management within each team.

1. Expand team details on the **Ownership teams** page.
2. Select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") in the upper-right corner of team details to access team-specific [**Revision history**](#revision-history), helpful **API** snippets for team management, and the ability to **Duplicate** team details as the basis for creating a new team.

   ![Team-management links](https://dt-cdn.net/images/ownership-team-specific-links-1462-4d8ea5d2df.png)

The API snippets for reading, creating, updating, and deleting teams are available for both Windows and Linux command line interfaces. While API snippets are team specific, you can modify them, for example, by removing the team identifier to create a new team. Be sure to provide your access token.

![Team-management API snippets](https://dt-cdn.net/images/ownership-teams-api-snippets-763-e9a0f5eb88.png)

## Related topics

* [Dynatrace settings framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Configuration as Code overview](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.")


---
