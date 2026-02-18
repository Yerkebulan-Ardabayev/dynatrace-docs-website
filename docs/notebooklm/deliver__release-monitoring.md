# Документация Dynatrace: deliver/release-monitoring
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 4
---

## deliver/release-monitoring/issue-tracking-integration.md

---
title: Issue-tracking integration
source: https://www.dynatrace.com/docs/deliver/release-monitoring/issue-tracking-integration
scraped: 2026-02-16T21:27:22.845700
---

# Issue-tracking integration

# Issue-tracking integration

* How-to guide
* 2-min read
* Published Sep 14, 2020

To get statistics about release issues for your monitored entities and configure dynamic queries, you can integrate your issue-tracking system with Dynatrace.

## Supported integrations

Dynatrace currently supports integration with

* Jira on-premises
* Jira cloud
* GitHub
* GitLab
* ServiceNow

## Integrate your issue-tracking system

To integrate your issue-tracking system

1. Go to **Settings Classic** > **Cloud Automation** > **Issue-tracking for releases**.
2. Select **Add issue-tracking query**.
3. Enter the information required (**Issue label**, [**Issue query**](#query), **Issue type**, **Issue-tracking system**, **Target URL**[1](#fn-1-1-def), [**Username**, and **Password** or **Token**](#credentials)).
4. If there are configuration errors, an error message will be displayed at the bottom of the page (`Please resolve errors before saving...`). Select **Show errors** to view the configuration errors (marked in red).
5. Optional Select **Check configuration** to check connectivity between Dynatrace and the issue-tracking system.
6. Select **Save changes** to save your configuration.

1

For GitLab, to define queries to multiple projects, you can enter the `/groups` API endpoint.

Example configuration

![Add tracker](https://dt-cdn.net/images/2021-04-26-08-06-21-1478-2c90218945.png)

### Issue query

In the **Issue query** field, you can specify queries with placeholders that are resolved at runtime (for dynamic filtering).  
Examples:

* **Jira on-premises/Jira cloud:** `issueType = Bug and component in ({PRODUCT}) and affectedVersion in ({VERSION})`
* **GitHub:** `is:issue is:open label:{PRODUCT} label:{VERSION}`
* **GitLab:** `search={PRODUCT} {VERSION}&state=opened&scope=issues`

#### Exception

For **ServiceNow**, placeholders aren't supported. You can query incidents by incident attribute values using the format `<col_name><operator><value>`.  
Example: `correlation_displayLIKEDYNATRACE^active=true`. In this case, filtering will apply for records that contain `DYNATRACE` within the `correlation_display` column and that are currently active.  
For other operators, consult the [ServiceNow API documentationï»¿](https://dt-url.net/0w03qc9).

Any query that can be written as a `sysparm_query` request parameter is supported.

### Credentials

The **Username**, **Password**, and **Token** fields are required as follows:

* For **GitHub**, enter a username and an OAuthToken
* For **GitLab**, enter an API token with read permissions
* For **Jira on-premises**, enter a username and a password
* For **Jira cloud**, enter a username and an OAuthToken
* For **ServiceNow**, enter a username and a password

Once you add your issue tracker to Dynatrace, you can see issue statistics related to the monitored entities in the **Release inventory** on the **Releases** page. For example, if the release inventory shows entries for the application **Cassandra** with version `3.11`, the issue-tracking integration will provide the count of bugs for Cassandra version 3.11.

Example issue tracker integration

![Example integration](https://dt-cdn.net/images/2021-04-26-08-20-46-1549-374692d0dd.png)

## Limitations

You can create a maximum of 20 issue-tracking configurations.

## Troubleshooting

The following is a solution to a problem some people had with [Automated release monitoring issue-tracking integration: no query results matching the filterï»¿](https://dt-url.net/5o038bi).

---

## deliver/release-monitoring/monitor-releases-with-dynatrace.md

---
title: Monitor releases with Dynatrace
source: https://www.dynatrace.com/docs/deliver/release-monitoring/monitor-releases-with-dynatrace
scraped: 2026-02-18T21:30:39.396726
---

# Monitor releases with Dynatrace

# Monitor releases with Dynatrace

* How-to guide
* 4-min read
* Updated on Aug 11, 2025

Once you [configure environment variables for version detection](/docs/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies") and, optionally, [integrate your issue-tracking system and configure dynamic queries](/docs/deliver/release-monitoring/issue-tracking-integration "Integrate your issue tracker into Dynatrace to pull statistics for monitored entities."), you can start analyzing data related to each release version of your software.

## List releases

To list the software releases in your environment, go to **Releases**.

Example Releases page

![Release list](https://dt-cdn.net/images/2021-05-25-12-02-34-1641-8ea61fbf08.png)

**Release version** sorting uses lexicographic (string) sorting rather than semantic version sorting. In lexicographic sorting, numbers are treated as individual characters, and the ordering is determined based on these characters' ASCII or Unicode values. **Release version** sorting uses lexicographic sorting because there's no pattern for the release versions, and users can enter any value.

The **Releases** page displays the following information about the listed releases:

### Release inventory

Shows all detected releases. Each entry represents processes, process group instances, grouped by release and build versions, stage, and product to which they logically belong.

### Release events

Shows all events corresponding to the releases, such as process restart and deployment events.

### Tracked issues

Shows issues from the external issue trackers related to the releases.

## Filters

* To set simple filters, use the quick filters on the left side of the page.
* To set more detailed filters, use the filter bar above the table.  
  For example, you can use the `tag` filter to search by the tag of a process group instance.
* To see only releases that are impacted by problems, select **Apply filter** above the **Release inventory** table.

  + Filtering for a specific release shows an overview of stages and product contexts in which the release is deployed.
  + Filtering for a stage shows an overview of all releases deployed at that stage.

## List release details

To see details about a release, select a link in the **Name** column of the **Releases** page.

Example Release details page

![Release details](https://dt-cdn.net/images/2021-05-25-12-41-08-1636-73e6cdccd9.png)

The **Release details** page displays the following information about the selected release:

### Release name

Shows a summary of captured metadata (process group name, version, stage, product, technologies, instances, throughput, problems, and third-party vulnerabilities) and links to the process group where the release is deployed.

* **Instances** shows the number of deployments of this release in a specific stage in the context of a specific product.
* **Throughput** shows how much traffic is routed to the selected release.
* **Problems** shows the number of open impacted problems related to the process group instance of the release.

  If Dynatrace detects problems in the release, **Problems** is displayed in red. Select it to display the **Problems** page and gather more information. See [Problem overview](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") for details.
* **Third-party vulnerabilities** shows the number of third-party vulnerabilities related to the selected release. This helps you check if, for example, a new release would introduce a known vulnerability and, based on this, decide on its impact on and relevance to your release schedule.

  If Dynatrace detects vulnerabilities in the release, **Third-party vulnerabilities** is displayed in red. Select it to display the **Security** page and gather more information. See [Application Security monitoring](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") for details.

### Process details

Shows hosts with basic metrics where the release is deployed and links to the host page for further analysis.

### Release events

Shows all events corresponding to the selected release, such as process restart and deployment events.

### Tracked issues

Shows issues from the external issue trackers related to the selected release.

### Release validation

To optimize the release inventory table, when no Cloud Automation instance is provisioned, the column to display a release validation result is not shown.

Lists release validations detected within the global timeframe.

* You can sort the list by score and evaluation end time.
* Select any release validation in the list to navigate to the heatmap of the corresponding evaluation on your Cloud Automation instance.

In addition, a graph displays the latest 20 release validation results:

* The y-axis displays the score
* The x-axis displays the end time of each quality gate evaluation
* The bar color indicates the quality gate status (`Failed`, `Warning`, or `Passed`)

---

## deliver/release-monitoring/version-detection-strategies.md

---
title: Version detection strategies for deep-monitored processes
source: https://www.dynatrace.com/docs/deliver/release-monitoring/version-detection-strategies
scraped: 2026-02-17T04:59:25.534551
---

# Version detection strategies for deep-monitored processes

# Version detection strategies for deep-monitored processes

* How-to guide
* 3-min read
* Updated on Aug 11, 2025

Dynatrace supports multiple strategies to detect and ingest release version information.
These strategies help enrich observability data with release context, enabling better traceability, filtering, and analysis.
Version detection can be influenced by environment variables, Kubernetes labels, event ingestion, and resource attributes from OpenTelemetry.

## Environment variables

Use environment variables to provide release metadata directly to Dynatrace OneAgent.

* `DT_RELEASE_VERSION` for **Version**
* `DT_RELEASE_STAGE` for **Stage**
* `DT_RELEASE_PRODUCT` for **Product**
* `DT_RELEASE_BUILD_VERSION` for **Build version**

### Example

1. Set an environment variable, making sure to replace `<YOUR_VERSION>` with your version information.

Windows

Linux

`$env:DT_RELEASE_VERSION='<YOUR_VERSION>'`

`export DT_RELEASE_VERSION='<YOUR_VERSION>'`

2. Start the process. After a short time, the version of this process appears in Dynatrace.

## Kubernetes labels

Best practice

We recommend that you propagate Kubernetes labels to environment variables in the deployment configuration.

### Example

![K8s best practice](https://dt-cdn.net/images/k8s-labels-env-1-662-06080041a8.png)

Starting with Dynatrace Operator version 0.10.0+, you can configure release label propagation by setting the `feature.dynatrace.com/label-version-detection=true` feature flag in the DynaKube custom resource. For details, see [Configure build label propagation](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

You can use:

* Kubernetes pod labels to provide metadata for:

  + Stage information (label: `dynatrace-release-stage`)
* [Kubernetes recommended labelsï»¿](https://dt-url.net/e103qse) for deployed pods to provide metadata for:

  + Versions information (label: `app.kubernetes.io/version`)
  + A related product (label: `app.kubernetes.io/part-of`) Optional

Be sure to use only pod labels, not the Kubernetes workload labels.

Kubernetes recommended labels mapped to release metadata:

![Recommended labels](https://dt-cdn.net/images/k8s-recommended-labels-1982-5e4ca55659.png)

Dynatrace OneAgent with [viewer permissions on the namespace](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.") can automatically detect labels attached to the Kubernetes pods.

* **Version** and **Product** show up in the release inventory.
* Kubernetes namespaces or configured Dynatrace host-group names show up as **Stages** in the release inventory.

If you need to update version information, update the deployment configuration to include the updated label and redeploy the pods. This ensures that `DT_RELEASE_VERSION` environment variable is correctly set when the pod starts. For more information, see [Configure build label propagation](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation "Configure build label propagation").

The command below will not propagate the updated label to the `DT_RELEASE_VERSION` environment variable used by OneAgent.

```
kubectl label --overwrite pod yourPodId -n yourNamespace app.kubernetes.io/version=42
```

## Events ingestion

Use the Dynatrace Events API to send [custom deployment events](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/info-events "Learn more about informational events and the logic behind raising them.") with release metadata.

* Version information sent via events can't be used to filter traces or metrics.
  Always set environment variables to reflect the currently deployed version to ensure accurate filtering and analysis.
  Ensure that environment variables always indicate the currently deployed version.

  + Because processes are matched using tags, a separate event is emitted for each process.
    As a result, any [workflow](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.") subscribed to these events may be triggered multiple times.
    To avoid redundant executions, we recommend sending a dedicated event to the workflow instead.

The example JSON below shows how to send custom deployment events to the [event ingestion API](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

For a release to be discovered, the following requirements must be fulfilled:

* `eventType` is set to `CUSTOM_DEPLOYMENT`
* `entitySelector` is mandatory and should point to a process group instance or a list of process group instances
* `dt.event.deployment.version` is mandatory

### Example

```
{



"eventType": "CUSTOM_DEPLOYMENT",



"title": "Easytravel 1.1",



"entitySelector": "type(PROCESS_GROUP_INSTANCE),tag(easytravel)",



"properties": {



"dt.event.deployment.name":"Easytravel 1.1",



"dt.event.deployment.version": "1.1",



"dt.event.deployment.release_stage": "production" ,



"dt.event.deployment.release_product": "frontend",



"dt.event.deployment.release_build_version": "123",



"approver": "Jason Miller",



"dt.event.deployment.ci_back_link": "https://pipelines/easytravel/123",



"gitcommit": "e5a6baac7eb",



"change-request": "CR-42",



"dt.event.deployment.remediation_action_link": "https://url.com",



"dt.event.is_rootcause_relevant": true



}



}
```

## OpenTelemetry Resource Attributes

Dynatrace supports ingesting release metadata via OpenTelemetry resource attributes, allowing you to propagate version information through telemetry data.

To use this method, define the `OTEL_RESOURCE_ATTRIBUTES` environment variable in your application and set key-value pairs that represent release metadata.
Refer to the [Semantic Dictionary](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") for the complete list of supported [attributes](/docs/semantic-dictionary/fields#deployment-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), called deployment attributes.
While Dynatrace enriches telemetry data with these attributes, they're not propagated to process group instance entities.
As a result, releases defined via OpenTelemetry resource attributes won't appear in the [release inventory](/docs/deliver/release-monitoring/monitor-releases-with-dynatrace#release-inventory "Analyze data related to each release version of your software.").

### Example

1. Create or extend the `OTEL_RESOURCE_ATTRIBUTES` environment variable with release metadata.

   Windows

   Linux

   `$env:OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`

   `export OTEL_RESOURCE_ATTRIBUTES=deployment.release_version='<YOUR_VERSION>',deployment.release_stage='<YOUR_STAGE_NAME>'`
2. Once the environment variable is set, Dynatrace automatically detects the resource attributes and enriches traces and logs with the provided release metadata.

---

## deliver/release-monitoring.md

---
title: Release monitoring Classic
source: https://www.dynatrace.com/docs/deliver/release-monitoring
scraped: 2026-02-18T21:29:53.158842
---

# Release monitoring Classic

# Release monitoring Classic

* Overview
* 1-min read
* Published Sep 14, 2020

The software product lifecycle of a release requires careful management of release risks. Also, as more and more components and versions are deployed, the frequency of releases in your organization increases, and manually collecting release-relevant data can easily become a bottleneck in your release automation pipeline and automated software lifecycle.

Dynatrace offers a built-in release-analysis solution that helps you determine:

* Which versions are deployed across your deployment stages and production environments based on multiple version-detection strategies.
* The release stages of the deployed versions.
* The changelog for a new version.
* Known bugs and whether they're release blockers.
* Risks related to specific versions.
* Which version has an excessive load (for example, if you're temporarily redirecting the load with a canary deployment).
* How the new version is behaving compared to previous versions.
* Issue statistics related to the monitored entities.

## Configure

* Learn how to [configure environment variables for version detection](/docs/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies").
* Optionally, you can [integrate your issue-tracking systems and configure dynamic queries](/docs/deliver/release-monitoring/issue-tracking-integration "Integrate your issue tracker into Dynatrace to pull statistics for monitored entities.").

## Analyze

Once you configure your software/issue tracker, you can [analyze the software product lifecycle of your releases](/docs/deliver/release-monitoring/monitor-releases-with-dynatrace "Analyze data related to each release version of your software.").

---
