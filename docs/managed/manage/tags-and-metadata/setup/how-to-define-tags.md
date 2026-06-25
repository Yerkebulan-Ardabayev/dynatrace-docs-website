---
title: Define and apply tags
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata/setup/how-to-define-tags
scraped: 2026-05-12T11:11:27.945893
---

# Define and apply tags

# Define and apply tags

* How-to guide
* 14-min read
* Published Jul 19, 2017

Use tags to organize monitoring data and analysis based on related entities in all environments. Tags simplify searches for related services, process groups, and hosts. They also facilitate the collection of related metrics into meaningful groups for analysis. Tags can also be used for all types of entities across your environment for the purpose of alerting, charting and window maintenance. For more details on defining maintenance windows via tags, see [How to define a maintenance window](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows/define-maintenance-window "Create maintenance windows and define their scope.").

You can apply tags manually or automatically.

* Manual tagging is great for small-scale efforts where it isn't worth your effort to create tagging rules when you need to tag just a few static items.
* Automatic, rule-based tagging is great for dynamic or large-scale environments, where manual tagging can be impractical. Rule definition for automatic tagging requires some up-front effort on your part, but it's much easier and more reliable than trying to manually keep up with tags on thousands of entities in a changing environment.

## Manual tagging

In smaller environments, tags can be set up manually by following the steps listed below.

### View all manually applied tags

To list all tags manually applied to any entities

1. Go to **Settings** and select **Tags** > **Manually applied tags**.
2. Optional In the **Filter by name** box, enter a filter string to list all manually applied tags that match your search string:

   * Enter a partial string to match all tags that start with, end with, or contain the string (`bc` matches `bcd`, `abc`, and `abcd`)
   * Use a colon to find a key:value combination
   * In a large environment, you may need to use filtering to limit the list to a manageable size or use rule-based [automatic tagging](#automatic).

To list all tags manually applied to a certain entity (such as an application, browser monitor, HTTP monitor, service, host, or process)

1. Open the entity-specific page (such as a host details page).
2. Tags applied to that entity are listed under the page title.

   * You can view, add, and delete manually applied tags directly from the entity-specific page.
   * Automatically applied tags are also listed, but you can't add or delete them directly; they are applied based on tagging rules that you define for [automatic tagging](#automatic).

### Manually apply or clear a tag

You can manually apply and clear tags:

* From the **Manually applied tags** pageâbest for manually applying or clearing tags on multiple entities
* From the entity pageâhandy for when you're working with a specific entity such as a single host

#### Manual tagging of multiple entities

To manually apply or clear a tag for multiple entities

1. Go to **Settings** and select **Tags** > **Manually applied tags**.
2. Find and select an existing tag, or create a new tag.

   To find and select an existing tag

   1. In the **Filter by name** box, enter a filter string to list all manually applied tags that match your search string:

      * Enter a partial string to match all tags that start with, end with, or contain the string (`bc` matches `bcd`, `abc`, and `abcd`)
      * Use a colon to find a key:value combination
   2. When you find the tag, select its name. This displays a table of manually taggable components.

   To create a new tag

   1. In the **Key (required)** box, enter the name of the new tag.
   2. Optional In the **Value** box, enter a value (to create a key:value pair)
   3. Select **Add**. This creates your tag and optional value, and then displays a table of components to which you can apply the new tag.
3. By default, the table displays applications.

   * If you are applying an existing tag, `Tagged` is selected and the selected check boxes indicate applications to which the tag has already been applied
   * If you are creating a new tag, `Untagged` is selected and no check boxes are selected (because the tag doesn't exist yet)
4. Optional Change `Applications` to `All types` or another specific component type, depending on the type of component to which you want to apply the tag.

   Component types that you can manually tag

   * Applications
   * Browser monitors
   * HTTP monitors
   * Services
   * Hosts
   * ESXi
   * AWS
   * Azure Scale sets
   * Processes
   * Process groups
   * Custom devices
   * Custom device groups
5. Optional Change `Tagged` to `All` or `Untagged`.

   All/Tagged/Untagged options

   * Allâlist all components of the selected type, regardless of whether the selected tag has been applied to them
   * Taggedâlist all components of the selected type to which the selected tag has already been applied
   * Untaggedâall components of the selected type to which the selected tag has NOT already been applied
6. Optional Enter a value in the edit box.

   Value

   This is a value for a key:value pair.
7. Select or clear the check box for each component for which you want to apply or clear the selected tag.

   * Select the **Tag component** check box to apply the tag to all matching components
   * Clear the **Tag component** check box remove the tag from all matching components

#### Manual tagging of a single entity

To manually apply or clear a tag for a single entity (such as an application, browser monitor, HTTP monitor, service, host, or process), it may be easier to start from the entity page.

For example, to tag a single host manually

1. Go to **Hosts**.
2. Select the host that you want to tag.
3. Expand the **Properties and tags** section under the page title to list all tags applied to that host manually or automatically.

   * **Manually** applied tags have a delete button, indicating that you can delete them manually.
   * **Automatically** applied tags have no delete button. When you hover over an automatically applied tag, a tooltip displays the tag key and value followed by the phrase `(applied by tagging rule)`.
4. Select **Add tag**.
5. In the pop-up window, enter the required **Key**, optionally enter a **Value**, and select **Add**.

   * If you decide that you instead want to tag multiple entities (such as hosts), select **Tag settings** in the pop-up window to open the **Manually applied tags** page, and then follow the [Manual tagging of multiple entities](#manual-multiple) instructions above.

## Automatic tagging

Automatic tagging is rule based:

* Tags are applied automatically to new entities that match rules you've defined.
* Automatically applied tags canât be removed manually from individual services, process groups, process group instances, applications, or hosts.

You can also set up automated tagging of the entities in your environment using:

* [Topology and Smartscape API](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.")
* [Environment variables](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.")
* [Host autotag configuration file](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") (for hosts only)

### How to define an automatically applied tag

To automatically apply a tag

1. Go to **Settings** and select **Tags** > **Automatically applied tags**.
2. Select **Create tag**.
3. Type a name for the new tag in the **Tag name** field.
4. Select **Add new rule**.
5. Specify an **Optional tag value**. This value will appear next to the tag name after a `:` and is used to provide more precise information. This value can be a property of the entity (for example, a service or a process group) where the tag is applied to. If the selected property is not available, the tag value will remain empty. Please note, that optional tag value placeholders do not work for entity selector based rules.
6. From the **Rule applies to** list, choose the type of entity you want to apply the rule to (such as `Services`, `Process groups`, or `Hosts`).
7. Optional Restrict the rule to specific entities by setting the provided properties using the respective lists.
8. You can directly define a condition that the entity must meet before the tag is applied. If you want to define more conditions, select **Add condition**. Conditions check for specific values of any property that is available within the **Conditions** drop list on the left. A rule example for a tag named `ocp-project` is shown in the image below.

   ![Page showing how to create rule for a new tag.](https://dt-cdn.net/images/tagging-rules-689-87fc41a18f.png)

   Page showing how to create rule for a new tag.
9. You can also propagate a rule to the underlying entities (such as process groups and hosts in the case of services, or hosts in the case of process groups) by selecting the corresponding check boxes at the bottom of the rule (see image above).
10. Select the **Preview** button to verify the results returned by the specific rule. Note that to be tagged, an entity must meet all the specified conditions of a rule.
11. Select **Create rule**. You can define multiple rules for each tag. Rules are executed in order. You can edit or delete a defined rule or activate/deactivate a rule at any time via the **Disable/Enable** switch.
12. To save your tag, select **Save changes** at the bottom right corner of the page.

When you select a tag, you can see the rules currently defined for the tag as well as the entities that match all the defined rules in the **Matching entities** area. Automatically applied tags are applied to all existing and newly detected entities (services, process groups, and others). Note that it can take up to a minute before your new tag is applied. Once a tag is applied to an entity, the tag is listed on that entity's page. For example, with services, each new tag is listed on the service's overview page within the **Properties and tags** section. The tag named `ocp-project`, for instance, that was defined in the example above, appears on the overview page of `ocp AuthenticationService` within **Properties and tags** extended with the tag value `demo-live-1` (see image below).

![Tagging example](https://dt-cdn.net/images/image-1-1821-6dd922ad5b.png)

Tagging example

Each tagging rule is self-contained and evaluated independently of any other existing rules.

#### Regular expressions

You can create conditions for your automatically applied tags based on [regular expressions](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace."). In step 8 above, select the property you want from the **Conditions** drop list on the left. Then select **contains regex** from the next drop list and type the regular expression in the text field.

Automatically applied tags cannot be used in conditions for automated rule-based tagging.

### Service and process group properties available for tagging

The service and process group properties available for tagging vary based on technology type.

To find out which properties a service provides:

1. Go to **Services**.
2. Select the service that you want to tag.
3. Select **Properties and tags** to display the available properties.

To find out which properties a process group provides

1. Go to **Hosts**.
2. Select the host that includes the process group you want to tag.
3. Select **Properties and tags** to display the available properties.

#### Properties supported by Dynatrace for automated tagging

Service properties

* Custom service class name
* Database name
* Database topology
* Database vendor
* Detected service name
* Endpoint path
* Public domain name
* Service name
* Service port
* Service tags
* Web application ID
* Web context root
* Web server host
* Web server name
* Web service name
* Web service namespace

Process properties

* Apache Spark master IP address
* Apache configuration path
* Azure host name of process
* Azure site name of process
* Catalina base
* Catalina home
* Cloud Foundry application
* Cloud Foundry instance index
* Cloud Foundry space
* Cloud Foundry space ID
* ColdFusion JVM configuration file
* ColdFusion service name
* Detected group name
* Detected process name
* Docker container name
* Docker image name
* Dotnet command
* Dynatrace custom cluster ID
* Dynatrace custom node ID
* Elasticsearch cluster name
* Elasticsearch node name
* EXE name
* EXE path
* GlassFish domain name
* GlassFish instance name
* IIS application pool
* IIS role name
* JBoss home
* JBoss mode
* JBoss server name
* Java JAR file
* Java JAR path
* Java main class
* Kubernetes base pod name
* Kubernetes container name
* Kubernetes full pod name
* Kubernetes namespace
* Kubernetes pod uid
* Listen port
* Node.js application name
* Node.js script name
* Process group name
* Process name
* Ruby application root path
* Ruby script path
* Varnish instance name
* WebLogic home
* WebLogic name
* WebSphere cell name
* WebSphere cluster name
* WebSphere node name
* WebSphere server name

Host properties

* AWS availability zone
* Azure SKU
* Azure compute mode
* Azure web application host name
* Azure web application site name
* Cloud type
* Detected AWS Availability Zone
* Detected host name
* EC2 Instance ID
* Host IP address
* Host group name
* Host name
* Host tags
* Hypervisor type
* Local EC2 host name
* OS type
* OS version
* PaaS type
* Public EC2 host name

### Rule examples for defining automatically applied tags

The image below shows two rules. The first rule filters services that are of type **Web service**, running on **Tomcat**, that include the string `BB` in their **process group** names. The second rule returns services that run on **Tomcat** and whose **Web application ID** contains the word `frontend`.

![Tagging example](https://dt-cdn.net/images/servicetagging-example1-758-969cddd35d.png)

Tagging example

The rule example below matches all services that are built on **Java**-based service technologies, run in a Cloud Foundry space called `development`, have the PaaS setup type `cloud foundry`, and include the string `spring` within their detected process group name.

![Tagging example](https://dt-cdn.net/images/servicetagging-example2-1074-7416af5a06.png)

Tagging example

The example below shows a rule that applies a tag to all **Azure websites** services on process groups where the **Detected group name** does not begin with `IIS app pool ~`.

![Service tagging example](https://dt-cdn.net/images/service-tagging-example-927-7099a6a46d.png)

Service tagging example

The image below shows a rule that tags specific process groups through the selection of the check boxâthereby additionally applying the tag to the underlying hosts.

![Page showing tagging rule editor.](https://dt-cdn.net/images/image-2-2834-50b14ed53f-2834-54a273c2f0.png)

Page showing tagging rule editor.

The **Infrastructure** tab includes the hosts to which the tag has been propagated (see image below).

![Tagging example](https://dt-cdn.net/images/image-3-2712-ef1391cd8d.png)

Tagging example

## Examples of how to use tags

Service, process group, and host tags can be leveraged in a number of ways. Two examples are detailed below.

### Narrow down your analysis

You can use tags to narrow the focus of your analysis to a specific set of services.

1. Go to **Services**.
2. In the **Filtered by** box, select `Tag` and then type and select a tag name. Repeat this for each tag you want to filter the table by.

Once you've selected a tagged group of related services, it's easy to focus your analysis on those services. For example:

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

1. Filter the **Services** page by one or more tags.
2. Select the **Pin to dashboard** button to add a health monitoring tile to a dashboard for the services matching the selected tags.
3. From the dashboard, you can now:

   * Watch the tile to monitor the selected services at a glance
   * Select the tile to drill down to the **Services** page filtered by the tags you selected in step 1.

### Ensure efficient routing of problem notifications

You can also use tags for efficient routing of problem notifications to responsible team members.

For example, assuming that you've defined a tag, `TeamBoston`, to tag all entities that this team is in charge of. To make sure the team members receive problem notifications

1. Use this tag to define an [alerting profile](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
2. Go to **Settings** and select **Integration** > **Problem notifications**.
3. Select **Set up notifications**.
4. Select the appropriate incident-management system or team-collaboration channel.
5. Select the alerting profile (from step 1) from the **Alerting profile** list.

The next time a problem notification is sent out, Dynatrace will check to see if any affected services carry properties that you've defined in your service tags. When critical parts of your environment are affected by a detected problem, the related notification will be delivered to the appropriate teams.

## Related topics

* [Filter tiles](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/filter-charts "Learn how to use powerful filtering options to set up dashboards in support of the unique monitoring needs of each of your organization's teams.")