---
title: Cost & Carbon Optimization
source: https://www.dynatrace.com/docs/observe/business-observability/cost-and-carbon-optimization
scraped: 2026-02-16T21:22:45.316020
---

# Cost & Carbon Optimization

# Cost & Carbon Optimization

* Latest Dynatrace
* App
* 8-min read
* Updated on Dec 21, 2025

About the app

* Calculates your IT carbon footprint at the data center, host, and Kubernetes infrastructure levels for multi hybrid-cloud infrastructure.
* Calculates your IT cost based on public price list from cloud vendors for each region and at host level.
* Translates utilization metricsâincluding CPU, memory, disk, and network I/Oâinto energy consumption in kWh and CO2 equivalents (CO2e).
* Reports energy consumption, carbon dioxide emissions, and list price costs in a single interfaceâwith drill-downs into physical hosts and Kubernetes infrastructure.
* Identifies opportunities to reduce costs and carbon emissions.

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

app-engine:apps:run

Run the Cost & Carbon Optimization app

state:app-states:delete

Delete workflow execution metadata

app-engine:functions:run

Run the Cost & Carbon Optimization data calculation and ingest

storage:events:write

Store Cost & Carbon Optimization events in GRAIL

storage:entities:read

Read entities from GRAIL

state:app-states:read

Read configuration and workflow metadata from app-states

state:app-states:write

Writes configuration and workflow metadata to app-states

automation:workflows:read

Read Cost & Carbon Optimization data ingest automation related data

automation:workflows:write

Creates/edits the Cost & Carbon Optimization data ingest automation

storage:bizevents:read

Read Cost & Carbon Optimization events from GRAIL

10

rows per page

Page

1

of 1

### Grant permissions to Workflows

Check if [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") has the required permissions to run automations: open ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, select **Settings** > **Authorization settings** in the upper-right corner, and ensure that the following settings are enabled.

* `app-engine:apps:run`
* `app-engine:functions:run`
* `app-settings:objects:read`
* `app-settings:objects:write`
* `automation:workflows:read`
* `automation:workflows:write`
* `environment-api:entities:read`
* `iam:bindings:read`
* `state:app-states:read`
* `state:app-states:write`
* `state:app-states:delete`
* `storage:bizevents:read`
* `storage:buckets:read`
* `storage:entities:read`
* `storage:events:write`
* `storage:metrics:read`

For more information, see [Manage user permissions with IAM policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") and [Workflow authorization settings](/docs/analyze-explore-automate/workflows/running "Run and monitor workflows created in Dynatrace Workflows.").

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

For carbon emissions calculation

Carbon dioxide emissions and energy consumption are calculated for hosts that are set up and monitored with OneAgent. Energy calculations are based on observed infrastructure metrics.

1. In ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization**, go to the **Hosts** tab.
2. Check that you have at least one host instrumented.

For public pricing costs calculations

* The data generation of carbon emissions must be active to allow generating public pricing cloud costs. You can activate it in the app's  settings.
* You need instrumented hosts with OneAgent and cloud vendor monitoring configured.
  The calculation of public price list costs requires the collection of metadata from a host as the cloud provider, cloud region, and the type of instance configured in the cloud vendor. This information is provided by configuring the cloud vendor monitoring for the hosts to be monitored with OneAgent. For more information, see [Ingest data](/docs/ingest-from "Learn how to install and configure ActiveGate and OneAgent on various platforms.").
* Enable **External requests** to the cloud vendors where the hosts are running to collect public price lists into Grail.

  External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Select  **New host pattern**.
  3. Add the domain names.
  4. Select **Add**.

  This way you can granularly control the web services your functions can connect to.

  You need to add the following domain names

  + For AWS, add `*.amazonaws.com`
  + For Azure, add `azure.microsoft.com`
  + For Google Cloud, add `cloudbilling.googleapis.com`

Get started

Concepts

Use cases

Dynatrace ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** enables you to calculate and monitor your IT cost (public list price) and carbon footprint.

It tracks, reports, and helps you optimize the costs from your cloud infrastructure and reduce your carbon emissions resulting from your cloud and on-premises infrastructure electricity consumption.

## Landing page

The **Overview** tab provides an at-a-glance view of your IT carbon footprint.

![Cost & Carbon Optimization overview page summarizes carbon emissions, energy consumption, cloud costs, and optimization targets.](https://cdn.hub.central.dynatrace.com/hub/overview-page.png)

1 of 1Cost & Carbon Optimization overview page summarizes carbon emissions, energy consumption, cloud costs, and optimization targets.

* The **Carbon & Energy Footprint** summary reports total CO2e emissions for the selected and preceding timeframes for quick interval-based comparisons.
* Wasted energy summary is also reported with the selected and preceding timeframe.
* Publicly listed **cloud costs** report the sum of cloud costs for Dynatrace-monitored hosts for the user-selected timeframe, using publicly available list prices from each cloud provider. Costs are displayed for the selected and preceding timeframes.

* **Optimization recommendations** reports idle hosts and underutilized hosts with their cost and wasted energy measured.

  To adjust thresholds influencing these calculations to your needs, navigate to the upper-right corner and select  to open the app's settings.
* The **Accumulated carbon footprint over time** chart shows the accumulated carbon footprint and energy consumption over time.
* With the **Carbon versus business KPI** chart, you can [compare carbon emissions over time with a business key performance indicator (KPI) of your choice](#business-health), derived from any of your captured business events.
* If cloud costs are calculated, two more charts display **Accumulated cloud cost over time** and **Cloud cost versus business KPI** defined.
* Carbon/energy data is measured for all hosts monitored by Dynatrace OneAgent, or by Dynatrace Kubernetes monitoring.

## Hosts

This tab allows you to view energy, carbon emissions, costs, and utilization information for OneAgent-monitored hosts.

![Host page displays host-level carbon, energy, cloud costs and optimization status](https://dt-cdn.net/images/hosts-page-1920-f2f5c2e743.png)

* The table includes all hosts with carbon/cost information for the user-selected timeframe, and displays metadata, energy consumption, CO2 equivalent, and cloud costs (cloud hosts only).
* Use the information from this table to identify and optimize hosts with low utilization and high energy consumption, high carbon emissions, and high costs.
* The table allows you to search for specific hosts, filter by data center, or filter by optimization state (`Idling`, `Scaling`, `Normal`âthresholds are defined in the app's  settings).
* Expand a host to see if average CPU, memory and network traffic utilization for the user-selected timeframe.
* The page includes an intent that allows you to query the underlying data using DQL in a notebook or dashboard and combine the carbon and energy data with other information in Dynatrace. This can be useful to customize optimization information using DQL. Tabular information can be downloaded to a CSV file by selecting the download link.
* This view includes only hosts that are monitored by Dynatrace OneAgent. Kubernetes infrastructure is shown in the **Kubernetes** tab. Cloud hosts not monitored by Dynatrace OneAgent are not displayed here.

## Kubernetes

![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** works only for Kubernetes monitoring on Grail; classic Kubernetes monitoring is not supported.

This tab allows you to view energy, carbon emissions, and utilization information for Kubernetes infrastructure monitored by Dynatrace.

![Kubernetes clusters GA](https://dt-cdn.net/images/kubernetes-clusters-ga-1920-e487b9d40c.png)![Kubernetes Namespaces GA](https://dt-cdn.net/images/kubernetes-namespaces-ga-1920-43a911839b.png)

1 of 2

Use the **Kubernetes** view to explore the energy consumption and carbon emissions of Kubernetes clusters, namespaces, and nodes by selecting the relevant link at the top of the page. Each view provides you with:

* A textual summary of carbon emissions and energy consumption
* Charts of the carbon emissions and energy consumption over the user-selected timeframe.
* A table of carbon emissions, energy consumption, and the relevant metadata for each Kubernetes entity.

Clusters

Namespaces

Provides a breakdown of carbon emissions and energy consumption for each monitored cluster, with an average count of nodes, namespaces, and workloads seen during the user-selected timeframe.

You can filter the table by cluster deployment type (for example, EKS, AKS, GKE) and search for a specific cluster names.

See [Average vs. actual values](#average-actual-value) for additional information on the use of average and actual counts.

This table provides a breakdown of carbon emissions and energy consumption for each namespace, with an average count of pods and workloads seen during the user-selected timeframe.

You can filter the table by cluster name and search for specific namespaces.

See [Average vs. actual values](#average-actual-value) for additional information on the use of average and actual counts.

The **Clusters** and **Namespaces** views

* Provide contextual navigation to the Kubernetes entity in ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** by selecting the cluster, namespace, or node link in the table.
* List the average CPU and memory allocatable to help understand each entity's hardware resources.
* Include an intent that allows you to query the underlying data using DQL in a notebook or dashboard and combine the carbon and energy data with other information in Dynatrace. Tabular information can be downloaded to a CSV file by selecting the download link.
* The % metric change is also shown in each view, enabling you to quickly determine whether the scope or emissions of a Kubernetes entity have increased/decreased for the selected timeframe.

Use this information to

* Identify Kubernetes clusters and namespaces with the highest energy consumption and carbon emissions, and correlate this with Dynatrace ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** information on CPU and memory slack to identify the most costly and underutilized Kubernetes resources.
  Leverage this information with your application teams to reconsider optimizing their requests/limits to reduce slack and optimize carbon and costs.

  One-click navigation between ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** and ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** allows you to quickly drill down into more information about the Kubernetes resources to inspect resource requests and limits, quotas, or idle workloads/jobs that reserve resources but run infrequently.
* Track energy and carbon at the Kubernetes cluster and namespace over time and identify anomalies that need further investigation to understand what changed in the environment and whether the change was intentional and warranted. A large spike (increase) in energy and carbon could be a normal side effect of increased usage, but it could signal an issue or change with automatic scaling or resource provisioning.
  Examples: Changes to the type of node instances being used, or an unnecessary increase in associated storage.
* Measure and compare carbon emissions from single-use servers to Kubernetes infrastructure to ensure that migration efforts are meeting the desired sustainability goals.
  Organizations may even consider gamifying this and challenging their engineering teams to develop solutions that delight end-users and the environment.

### Average vs. actual values

Kubernetes is a dynamic environment, and the number of nodes and pods changes continuously.

When reporting on carbon and energy over longer timeframes, counts can be derived using the average count of nodes, pods, and other entities observed during the user-selected timeframe, or a more in-depth query can be made to the Kubernetes data in Grail to get actual distinct counts of each entity.

In a large Kubernetes environment, an actual count of distinct entities can take several seconds, whereas the average count typically takes milliseconds, and is sufficient for most use cases.

This selector may account for differences between ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** and ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

The query time for the actual data is dependent on the size of your Kubernetes infrastructure and the timeframe being analyzed.

* Using actual data over a 7-day period could take minutes, not seconds.
* Querying namespace actual data is significantly heavier than clusters or nodes, and we recommend using a short timeframe (1-2d) when using actual data within the **Namespaces** tab.

When using the deployment mode **Kubernetes platform monitoring + Application observability**, nodes and namespaces can be excluded from monitoring using the `namespaceSelector` (and `nodeSelector`).

As ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** only reports on the energy/carbon of namespaces/nodes that are monitored, energy and carbon emissions shown may be lower than expected when infrastructure is excluded from monitoring. Excluded namespaces will be displayed in the **Namespaces** table but will show no carbon/energy measurements.

In addition, internal workloads (such as `coredns`, `traefik`, and more) may be running that are not monitored by Dynatrace and energy/carbon data will not be included in the measurements.

## Learning modules

Go through the following process to learn using ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization**:

[01Set up Cost & Carbon Optimization

* How-to guide
* Install and set up Cost & Carbon Optimization.](/docs/observe/business-observability/cost-and-carbon-optimization/install-cost-and-carbon-optimization)[02Advanced analytics with Notebooks

* Reference
* Use Notebooks to analyze your carbon footprint data.](/docs/observe/business-observability/cost-and-carbon-optimization/advanced-analytics-with-notebooks)

### Methodology to estimate electricity consumption

Electricity consumption and carbon dioxide emission are calculated based on guidelines from the Sustainable Digital Infrastructure Alliance ([SDIAï»¿](https://dt-url.net/rga3uql)) with some contributions from the [Cloud Carbon Footprintï»¿](https://dt-url.net/0ic3u5z) project and internal research from Dynatrace. All of the methodology is aligned with the [GHG Protocolï»¿](https://dt-url.net/1re3uzm).

Energy is estimated based on the utilization metrics captured by Dynatrace OneAgent (in all modes for hosts) for CPU, memory, storage IO, and network. This estimation is performed every hour for each instrumented host through an automation.

The formula to estimate energy draw includes several parameters from external data sources and some assumptions.

The deviation from the measured power cannot be reliably determined due to the large variety of devices in the market and lack of statistical analysis.

### External data sources

* Random Access Memory energy usage data source

  + [How much power does memory use?ï»¿](https://dt-url.net/yt03uaw)
* CPU architecture sources (TDP, core, thread count) used in calculations

  + [Intel Product Specificationsï»¿](https://dt-url.net/ld23uvj)
  + [AMD Processor Specificationsï»¿](https://dt-url.net/nj83uae)
  + CPUs not officially listed are manually added through research, and the sources vary
* Storage energy usage

  + United States Data Center Energy Usage Reportâ[Energy Technologies Areaï»¿](https://dt-url.net/jl63u1r)
* Networking energy usage

  + Methodologyâ[Cloud Carbon Footprintï»¿](https://dt-url.net/cw83ura)

### Assumptions for electricity consumption

* CPU energy measurement:

  + Over a long period of time, a CPU running at 100% utilization will consume its TDP in power draw.
  + The base power draw of a CPU is 1/3 of its TDP
    It is known that true idle for CPUs is much lower, but CPU utilization hovers around a constant 10-20% for server applications, so true idle can never be reached.
  + One cloud vCPU equals one CPU thread
* Memory energy measurement:

  + Random Access Memory uses a constant of 3 W of power per 8 GB regardless of utilization.
* Storage energy measurement:

  + The power draw of a terabye of SSD storage is 1.2 W
  + All storage is assumed to be on an SSD
  + Storage power draw is constant
  + Cloud storage is replicated twice (or more)
* Network energy measurement:

  + 1 GB of networking (upload or download) consumes 1 W if sent outside of the local network.
  + 1 GB of networking (upload or download) consumes 0.12 W if remaining within a local network.

### Power Usage Effectiveness (PUE)

The final result of the formula includes the energy consumed by hardware and cooling. Cooling is included in a standard metric, Power Usage Effectiveness (PUEânot displayed directly in ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** but available in the raw data generated). This metric, used to measure the energy efficiency of a data center, is a ratio between the total power consumption of a data centerâincluding cooling, lighting, and support equipment energy useâand the power consumed by the IT infrastructure. It describes how much energy IT equipment uses compared to other electrical devices.

The Power Usage Effectiveness varies depending on a data center, but its predefined values for the main cloud providers are publicly available. The ones used in the calculation are:

* AWS and Azureâ[MethodologyâCloud Carbon Footprintï»¿](https://dt-url.net/cw83ura)
* Googleâ[EfficiencyâData Centersï»¿](https://dt-url.net/t5g3uwt)
* Rest of the worldâ[Global PUEsï»¿](https://dt-url.net/0ai3utu)

### Wasted energy calculation

Wasted Energy calculation is based on the assumption that every CPU cycle that is not utilized wastes about 1/3\*TDP (Thermal Design Power). The proportion of unutilized CPU cycles is roughly 100% - CPU usage %. With those assumptions, the Wasted Energy (WE) is calculated as WE = Wp \* 1/3 \* TDP, where Wp is 0 for 100% CPU utilization and 1 when the CPU utilization is equal to the idle threshold.

### Carbon emissions calculation

Carbon emissions are estimated in CO2 equivalent grams. The calculation is multiplying carbon intensity factors by total energy consumed calculated with previous methodology.

### Assumptions for carbon emissions

* A data centerâs carbon intensity is equal to the average carbon intensity of the country where it is located. This means that for large countries the national differences are not considered.
* Carbon intensity values used on calculations are an annual average.

### Carbon intensity data sources

* European Union (EU)â[Greenhouse gas emission intensity of electricity generationï»¿](https://dt-url.net/lm23uco)
* Rest of the worldâ[Carbon intensity of electricity generationï»¿](https://dt-url.net/1103ubu)

### Public price list costs calculation

![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** can collect public price list data from cloud providers available data on a daily basis, limited to the regions where OneAgents are deployed and cloud extensions are configured.

Every hour, the same workflow that generates the data for energy and emissions also calculates the hourly cost of a host based on the public price list matched with its cloud vendor, region, and instance type.

Both business events follow the Dynatrace Semantic Dictionary schema.

### Data centers and hosts

The **Data center emissions** table on the landing page shows costs, energy, and CO2e consumption per data center. Select a data center name to view details of its hosts.

The **Hosts** tab details cost, energy, and CO2e consumption per host. You can narrow your search using filters. For example, you can view underutilized hosts in a specific data center or top CO2e emitters.

Expand a hostname to see key infrastructure metrics: **CPU in use**, **Memory in use**, and **Receiving network traffic**. Select a host name to view the host details page in [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.").

![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** is automatically connected to Dynatrace SmartscapeÂ® topology modeling, so it's easy to see the host details or use [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for ad hoc analysis with DQL.

### Measure the energy of Dynatrace Kubernetes platform monitoring

Use ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** to measure energy and carbon emissions of your Kubernetes infrastructure.

![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** calculates the energy consumed (in Watt-hours) and carbon emissions (in grams of carbon dioxide emissions) of Kubernetes clusters and namespaces, and nodes, monitored by Dynatrace. All Dynatrace Kubernetes monitoring modes are supported, and data is calculated hourly and stored as [carbon Kubernetes events](/docs/semantic-dictionary/model/business-analytics#carbon-kubernetes-cluster-events "Get to know the Semantic Dictionary models related to Business Observability.").

Organizations using Kubernetes today, or looking to migrate workloads to Kubernetes, should consider using ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** in addition to the Dynatrace Kubernetes monitoring for the following reasons:

Energy use is a direct driver of cost
:   Cloud infrastructure costs are largely driven by energy consumption. CPU, memory, storage, and networking all consume power, and cloud providers factor this into pricing. By measuring energy usage, you're essentially tracking the underlying metric that influences cost.

Carbon footprint adds environmental context
:   Carbon footprint translates energy consumption into environmental impact. This is especially valuable for organizations with sustainability goals or ESG (Environmental, Social, and Governance) reporting requirements.

Optimization opportunities align
:   Inefficient clusters, namespaces, and nodes that consume more energy (and thus emit more carbon) are often the ones driving up cloud costs. Identifying high-carbon workloads can highlight areas for cost and environmental optimization.

The app will generate carbon Kubernetes bizevents in addition to regular carbon bizevents when the **Enable energy and emission data generation** option is enabled within the app's  settings.

You can report on Kubernetes infrastructure energy and carbon emissions using custom DQL and dashboards.

### Cluster calculations

Each Kubernetes node within the cluster is identified as a host, and ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** uses the host processor, and utilization information to calculate energy and carbon every hour using the **Cost & Carbon Optimization Calculation** workflow. The carbon and energy metrics of all nodes are summed and stored as a bizevent using: `type="carbon.measurement.k8s.cluster"`.

### Namespace calculations

Namespace carbon and energy values are derived by determining the % utilization of each namespace across the Kubernetes nodes it runs on, proportionally allocating energy and carbon from each node to the namespace. The carbon and energy metrics of all nodes are summed and stored as a bizevent using: `type="carbon.measurement.k8s.namespace"`.

Bear in mind the following:

* CPU processor information is only available when using **Kubernetes platform monitoring + Full-Stack observability**. Other monitoring modes provide only instance type. Dynatrace maintains a lookup table of cloud instance type to CPU and will fall back to a Dynatrace-derived Kubernetes median value of 240w TDP and 64 threads.
* For AWS Fargate, energy calculations assume a Graviton1 processor type (TDP 110w, 16 threads).

## Use cases

* Cost reporting and allocation
* Carbon reporting and allocation
* Carbon reduction
* Usage optimization
* Kubernetes infrastructure carbon optimization
* Cost anomaly management

## Troubleshooting

"An error occurred while loading the data. Please make sure you have the required user permissions."

This popup error message will list the permissions needed to use ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization**.

Ensure that a Dynatrace IAM administrator adds these policies to your user/group.

"Try adjusting the timeframe or columns"

* There's no data to display, potentially due to the timeframe selected, or due to carbon data not being generated correctly.
* If you enabled ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization** recently, please wait for up to 1-2 hours for the workflow to execute and start generating carbon data.
* You can check whether carbon or carbon Kubernetes data is being generated by running the following DQL in a notebook. Select the  icon on the page, right above any table in the **Hosts** or **Kubernetes** tabs, to **Open with** the underlying DQL in a notebook:

  ```
  fetch bizevents



  filter event.type == "carbon.measurement" or event.type == "carbon.measurement.k8s.cluster"
  ```

  Run in Playground
* Ensure that the Cost & Carbon Optimization workflow has the required authorization settings to function.

  Open ![Cost & Carbon Optimization](https://dt-cdn.net/images/cost-and-carbon-1024-4f5a603752.webp "Cost & Carbon Optimization") **Cost & Carbon Optimization**  settings page. If this is the problem, an error message with missing authorization settings will be displayed theres.
* Ensure that the Cost & Carbon Optimization workflow is scheduled to run every hour, that all steps within the workflow are enabled (not disabled), and that no errors are generated by the workflow.

  Review any workflow errors for further troubleshooting or contact our customer support.

"We encountered an unexpected issue. Please try again later."

* A platform issue is preventing the app from executing queries to report on carbon Kubernetes data.

  The issue may be temporary and will resolve itself shortly, or please reach out to our customer support.
* Kubernetes monitoring may not be set up or functioning correctly.

  Please check ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** to ensure that your Kubernetes infrastructure is being monitored correctly.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Track and reduce your site infrastructure's carbon footprint.](https://www.dynatrace.com/hub/detail/carbon-impact/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [Analyze energy consumption and carbon emissions in hybrid cloud infrastructureï»¿](https://www.dynatrace.com/news/blog/analyze-energy-consumption-and-carbon-emissions-in-hybrid-cloud-infrastructure/)