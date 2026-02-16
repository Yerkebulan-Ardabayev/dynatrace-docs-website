# Dynatrace Documentation: manage/tags-and-metadata

Generated: 2026-02-16

Files combined: 2

---


## Source: best-practice-tagging-at-scale.md


---
title: Best practices for scaling tagging and management-zone rules
source: https://www.dynatrace.com/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale
scraped: 2026-02-16T09:29:23.014404
---

# Best practices for scaling tagging and management-zone rules

# Best practices for scaling tagging and management-zone rules

* Explanation
* 8-min read
* Published May 19, 2021

Automatic [tag](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") and [management zone](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") assignment helps keep your monitoring environment organized and directs the focus of individual teams to the infrastructure they're responsible for.

Dynatrace offers powerful filters and conditional processing to select which parts of your monitored topology should display a certain tag or be assigned to a management zone. These filters are the conditions you specify when creating an automatic tagging or management-zone rule. While Dynatrace has some stability limits in place, the administrator of each monitoring environment is responsible for the performance of tagging and [management-zone rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.").

Overly complex rule filters run slower than simple filters, and the total number of rule filters defines the speed of automatic tagging and management-zone assignment in your monitoring environment. For reference, it takes approximately one minute to complete a tagging run with a small number of tagging filters (say, 100); it can take several hours to complete a tagging run with thousands of complex tagging filters.

As many filters contain some hidden topology traversal as well as other "expensive," time-intensive operations, this topic aims to help you optimize tagging speed in your environment. The sections below deliver some advice on best practices to speed up the time taken to assign tags and management zones within your monitoring environments.

## Keep the number of rules low

Keeping the number of automatic tagging rules and management-zone rules low is the most effective way of guaranteeing fast assignment. You can have multiple rules within a single tagging or management-zone configuration, but it's the total number of those individual rules across all your tagging and management-zone configurations that impacts the assignment of tags as well as management zones.

Management zones can be derived from tagged entities, so the assignment of management zones might depend on automatic tagging rules. This also means that the tagging worker process needs to evaluate tags and management zones sequentially, which slows the assignment of management zones depending on the number of automatic tagging rules configured.

Any delay in a tagging run primarily depends on the number of rules combined with the number of monitored entities within your environment. While thousands of complex tagging rules might work out well in smaller environments with hundreds of monitored hosts, you can experience long tagging delays in environments with thousands of monitored hosts.

Per monitoring environment, you can set up:

* Any number of automatic tags.
* 300 UI-based automatic tagging rules for entities (150 for Dynatrace versions 1.323 and earlier).
* 300 text-based entity selector rules for automatic tagging (150 for Dynatrace versions 1.323 and earlier).
* 100,000 conditions for all automatic tagging rules taken together (does not apply to entity selector rules).
* A maximum of 1000 manual tags and 1000 automatic tags per individual entity.

Additionally, per monitoring environment, you can set up:

* 5,000 management zones by default. For any questions, contact a Dynatrace product expert via live chat.
* 300 UI-based management-zone rules for entities (150 for Dynatrace versions 1.323 and earlier).
* 300 UI-based management-zone rules for dimensional data (150 for Dynatrace versions 1.323 and earlier).
* 300 text-based entity selector rules for management zones (150 for Dynatrace versions 1.323 and earlier).
* 100,000 conditions for all management-zone rules taken together (does not apply to [entity selector rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#text "Define rules to limit the entities accessible within a management zone.")).
* Any individual entity to a maximum of 200 management zones (run the [GET an entity](/docs/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") API call to see an entity's management zones).

## Topology queries are slow

Filters that perform topology queries use a parent entity property in order to filter for a list of child entities. For example, you can use a host property to filter for all process group instances running on that host or filter for all services running on that host.

No matter how useful they are, such topology queries are expensive and slow because each filter has to traverse the topology, through multiple steps in some cases, to assign a tag or extract a value for a given entity. Topology traversal is expensive especially in large-scale environments where each such filter adds a significant lag to overall tag and management-zone assignment.

If you really need to propagate values from one entity type to another (for example, from host to services), keep only a very small number of such complex rules.

## Avoid value extraction wherever possible

Assigning a single tag is fast. Extracting values from the property of a given entity is slow. If you can reduce a value-extraction rule to a single tag assignment by using a static rule instead, this will speed up the overall tagging performance.

In cases where the number of values is a limited static set, several single static rules can replace an automatic value-extraction rule.

For example, if you run a handful of Kubernetes clusters, you might use an extraction filter for assigning the K8S cluster ID as a value in a rule. This can easily be replaced by a single rule for each of your Kubernetes clusters. This might not be as flexible as an extraction rule, but it's much faster.

## Use multilevel filters to narrow down search results

If an "expensive" filter condition such as a regex is inevitable, you can also configure a "cheap" pre-filter that reduces the overall number of entities to check.

An example of a cheap filter is a "name begins with" filter that first reduces the number of entities to a much smaller set, after which an expensive regex filter can be safely applied.

The order in which you specify filters within a single rule configuration doesn't matter, as Dynatrace filter execution always chooses the cheapest filter first in order to reduce the result set before applying expensive filters.

## Avoid regex or "contains" queries

While regular expressions are tremendously powerful, they have a major tradeoff in that they're significantly slower to evaluate than simple "begins with" or "equals" filters. The same is true of "contains" queries, where the entire string must be checked for the existence of a given substring.

"Begins with" or "equals" queries are much more efficient than "contains" or regex-based queries.

One of the most powerful ways to organize your data and topology is to use a common naming scheme that uses a hierarchical structure, as this provides the most efficient way to construct queries that use "begins with" filters.

Here's an example of an efficient hierarchical naming pattern where the hierarchy is defined from the most general to the most specific from left to right.

Entity naming scheme: `<stage>.<app>.<cluster>.<entityname>`

## Use manual, bulk, or environment tags

Besides the use of automatic tagging rules, there are alternative ways of tagging entities that come with certain performance benefits.

### Manual tagging

One alternative to automatic tagging is to tag entities manually. This might not be possible for a large set of entities but it works for a small set of stable entities.

As manual tags can be used by an automatic management-zone rule, this shortcut can improve the overall performance of tag and management-zone assignment.

### Custom tags API

When there are too many entities to perform manual tagging efficiently, Dynatrace offers the Custom tags API to conveniently [assign a tag to a large group of entities within a single API call](/docs/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API."). What makes this approach powerful is the standardized [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")âa powerful and flexible tool for selecting entities.

The entity selector can also contain a topology query, such as a query for all disks of a given set of hosts that can be filtered by any kind of entity attribute. See some examples of using the entity selector below.

Use this entity selector string to pick all services where the service name starts with `book`:

```
type(SERVICE),entityName.startsWith("Book")
```

Use this entity selector string to pick all container-group instances of a given Kubernetes cluster:

```
type(CONTAINER_GROUP_INSTANCE),fromRelationship.isCgiOfCluster(type(KUBERNETES_CLUSTER) AND entityName.equals(my-prod-cluster-name))
```

The API call is executed immediately, which is a major benefit over auto-tagging rules that are scheduled via the Dynatrace tagging process. This helps you speed up execution time where complex tagging rules are necessary.

The tradeoff of this approach is that it's a one-time tagging action, and newly detected entities that fit the rule will not be tagged automatically. You can easily address this with a regular API request (for example, triggered by an external cron job).

### Environment tags

OneAgent provides a convenient way of reading and [assigning tags from local system environment variables](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables."). Using environment tags over automatic tagging rules significantly improves tagging performance, as each OneAgent instance is responsible for assigning such tags in a highly distributed fashion. Moreover, this approach is fast and doesn't slow down the execution of server-side tagging rules at all.

As most modern automatic deployment systems use deployment scripts and receipts anyway, such receipts can also be used to define Dynatrace tags through system environment variables.

By using environment variables to create and assign tags, your own deployment receipt is in control of tag assignment, and you don't have to rely on an expensive tagging rule.

## Use cheap attributes in place of expensive ones

Large parts of the Dynatrace Smartscape topology model are indexed in memory to guarantee fast query execution. Dynatrace keeps an index of most entity attributes that are stable, while an index of highly volatile information is avoided.

This means that tagging and management-zone rules that are defined on indexed entity attributes are much cheaper than rules that query for attributes that are not available in our topology index.

The following list of entity attributes should be avoided, as they are not available through the topology index.

* Docker container name
* Docker full image name
* Service topology
* Software technology
* Software technology version
* Docker image version
* Docker stripped image name
* Kubernetes labels
* Cloud application labels
* Cloud application namespace labels
* Instance type of OpenStack VM
* Public IP addresses of GCE
* IP addresses of host
* IP addresses of custom device
* PaaS memory limit
* Synthetic engine type
* Synthetic engine name
* Security groups of EC2
* Frontend ports of ELB


---


## Source: define-tags-based-on-environment-variables.md


---
title: Define tags based on environment variables
source: https://www.dynatrace.com/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables
scraped: 2026-02-15T21:19:08.432361
---

# Define tags based on environment variables

# Define tags based on environment variables

* How-to guide
* 2-min read
* Updated on Aug 07, 2023

Dynatrace provides the ability to define tags as in environment variables for processes and process groups.

## Recommendation

Defining tags in the environment itself has its uses. However it's not recommended as a general purpose solution, as it is rather cumbersome and requires a lot of preplanning. It also makes it hard to make changes later. Therefore, you will have to use it with caution.

We recommend that you define additional metadata at the deployed system. Typically, you should think about additional metadata and standard metadata and not about tags (that is, labels).

Use the environment variable [`DT_CUSTOM_PROP`](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") to define your metadata. This enables you to use [automated tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and are applied almost immediately without any change to the monitored environment or applications.

## Define tags as environment variables

You can define an environment variable called `DT_TAGS` on the process or host level. The format of the variable is simple. The variable can contain simple strings or key/value pairs (for example, `DT_TAGS=MikesStuff easyTravel=Mike`). As you can see in the Windows process example below, you can define multiple tags. Spaces are used to separate tag values.

To customize the process group of IIS, you need to define an environment variable that you can use within the scope of a rule. To set up an environment variable in IIS version 10 or later, see [Environment variablesï»¿](https://www.iis.net/configreference/system.applicationhost/applicationpools/add/environmentvariables).

How to define an environment variable for IIS earlier than version 10

#### Set up an environment variable for IIS versions earlier than 10

To set up an environment variable in IIS versions earlier than 10, follow the instructions below.

1. Configure the **Advanced Settings** for Application Pool.

   ![Environment variable IIS](https://dt-cdn.net/images/env1-1578-6d669915ad.png)
2. Set the **Load User Profile** as **True**.

   ![Environment variable IIS](https://dt-cdn.net/images/env2-1563-c1584fc0f2.png)
3. Restart IIS.  
   At the command prompt with admin rights, enter `iisreset`.
4. Open the Registry and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`

   ![Environment variable IIS](https://dt-cdn.net/images/env4-1571-60d8f6ab63.png)
5. Launch the application to initialize the AppPool (or set the **AppPool Start Mode** to **Always Running**), refresh `hivelist` and look for the new entries.

   ![Environment variable IIS](https://dt-cdn.net/images/env5-1580-7e22193123.png)
6. Check `C:\Users` for the name of the user who runs the AppPool.

   ![Environment variable IIS](https://dt-cdn.net/images/env7-557-1acbf9ee8c.png)
7. In the registry navigate to the ID of the user under `HKEY_USERS` and add a **String Value** named `DT_CUSTOM_PROP`.

   ![Environment variable IIS](https://dt-cdn.net/images/env8-1590-c013dd318f.png)
8. Add the value you want with spaces between the key/value pairs.

   ![Environment variable IIS](https://dt-cdn.net/images/env9-949-0ec6aad7a9.png)
9. Restart IIS one more time and check Dynatrace process for environmental metadata.

   ![Environment variable IIS](https://dt-cdn.net/images/env10-1361-e92e945f44.png)

How to define an environment variable for Windows

To customize process grouping for Windows services, open **Registry Editor** on your local machine and create a key called **Environment** of type `REG_MULTI_SZ` in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<servicename>`. The variable name should start with the `DT_CUSTOM_PROP` string, for example, `DT_CUSTOM_PROP=NAME_A=valueA`. The key may contain multiple entries.

Example:

![pg-vars](https://dt-cdn.net/images/2022-02-18-9-49-57-459-fb9fe355b4.png)

Applying [tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") to hosts (instead of thoughtfully setting up environment variables as explained here) isn't recommended. The same applies to applications and processes. For details on setting up the `DT_CUSTOM_PROP` environment variable for Tomcat or WebSphere application metadata, Kubernetes annotations for Kubernetes-based deployments, or AWS tagging, see [Application metadata & tagging](/docs/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging#application-metadata-and-tagging "Learn when it's recommended to use tags that leverage auto-detected metadata, as well as best practices for enriching Dynatrace monitoring with additional metadata.").

![Env tagging 1](https://dt-cdn.net/images/env-tagging1-433-ef2e38dad8.png)

## Filter entities based on environment variables

In the Dynatrace UI, the example environment variable shown above results in new filters being displayed on the related process overview page (see below). Process group overview pages display the sum of all the tags of all processes in the group.

![Env tagging 2](https://dt-cdn.net/images/env-tagging2-1414-289c172a71.png)

![Env tagging 3](https://dt-cdn.net/images/env-tagging3-1272-0d740c7cb8.png)

![Env tagging 4](https://dt-cdn.net/images/env-tagging4-1113-971391db79.png)

This feature is currently only available for processes that are deep monitored via OneAgent (Java, Apache Webserver, NGINX, .NET, Node.js, PHP, Go, and IIS).


---
