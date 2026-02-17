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