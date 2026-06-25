---
title: Dynatrace glossary
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/glossary
scraped: 2026-05-12T12:26:06.600705
---

# Dynatrace glossary

# Dynatrace glossary

* 26-min read
* Updated on Jan 28, 2026

Gain a deeper understanding of Dynatrace terminology and concepts.

## A

Adaptive Traffic Management (ATM)

Dynatrace intelligent trace sampling mechanism for Full-Stack Monitoring.

For details, see [Adaptive Traffic Management for Dynatrace Managed](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").

Apdex

A performance-measurement standard that shows the relationship between recorded performance measurements and real-user satisfaction. Apdex offers a uniform means of measuring how well performance meets user expectations. For full details on the Apdex standard, please visit [Apdex.orgï»¿](https://www.apdex.org/). In the context of Dynatrace, Apdex is used to give you a quick and easy rating that you can use to evaluate the satisfaction of your application's end users. Apdex ratings in Dynatrace are based on application-specific thresholds. An Apdex measurement rating of `1` equates to perfect performance. An Apdex rating below `0.5` equates to poor performance. For more details about how Apdex is applied in Dynatrace, see [Apdex ratings](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")

application

A web application consists of web pages that are served by web servers and web containers, for example Tomcat. A web or mobile application is built upon services that process requests like web requests, web service calls, and messaging. Within Dynatrace, the term application refers to the frontend part that you can access via a browser or a mobile app.

Dynatrace monitors all of your application's services, processes, and infrastructure. By evaluating all components collectively, Dynatrace pinpoints exactly how each service contributes to the performance of your application. For example, in Java monitoring, the host, JVM, and processes are seen as a whole.

Dynatrace monitors all the individual components that applications are built upon: web requests, database requests, processes, services, and more. It's these individual components working together that collectively deliver what your end users view as a complete application. Dynatrace identifies and tracks each of these individual application components at a highly granular level. Dynatrace doesn't simply identify that a service is running on a server in a process but rather identifies all the details of these components. For example, Dynatrace can show you which of your web services is running on your Tomcat application server and how your Tomcat server's performance is affected by its host, or even your VMware vCenter server. In this way, Dynatrace gives you insight into the performance of your unique application stack, including all its components and connections.

Application Security

A Dynatrace feature that enables you to detect, visualize, analyze, monitor, and remediate open-source and third-party vulnerabilities in production and pre-production environments at runtime.

Application Security unit

A means of licensing [Dynatrace Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities."). The number of Application Security units that an environment consumes is based on the amount of RAM that a monitored server has and the number of hours that those Application Security units are monitored.

## B

browser clickpath

A simulated user visit that monitors your applicationâs business critical workflows. Use the Dynatrace recorder to record an exact sequence of clicks and user input that you're interested in monitoring for availability and performance. Once youâve captured the mouse clicks and additional user actions that you want your [browser clickpath](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") to include, your synthetic monitor runs automatically at regular intervals to test your siteâs availability and functionality.

browser monitor

The equivalent of a simulated user visiting your application using a modern web browser. [Synthetic single-URL browser monitors](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") can be configured to run from any of our global or private locations at a frequency of up to once every five minutes. Browser monitors alert you when your application is inaccessible from the Internet or when baseline performance degrades significantly.

bucket

Bucket is a cross-content term used to describe a certain scope of data that is retained for a defined period. Within a bucket, you need to define what is retained (a scope), using the [matcher-specific DQL queries](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). You also need to specify for how long your data needs to be retained. This is a concept common to Grail-based solutions such as [Log Management and Analytics powered by Grailï»¿](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics) and [Business Observabilityï»¿](https://docs.dynatrace.com/docs/shortlink/business-observability-hub).

## C

candidate

See [monitoring candidates](#glossary-monitoring-candidates)

Cluster ActiveGate

A Dynatrace component that provides secure and reliable communication with cloud-based Dynatrace cluster nodes. It is [downloaded from your Dynatrace Managed cluster and installed](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") within your infrastructure. Similar to a proxy, ActiveGate reduces bandwidth requirements by encrypting and compressing network communication. It also provides monitoring of virtual infrastructure. Stopping or disabling ActiveGate reduces the monitoring capabilities of hosts that use a Cluster ActiveGate to communicate with Dynatrace clusters.

Cluster Management Console (CMC)

The web-based user interface that manages a single Dynatrace Managed cluster. The CMC allows you to:

* View the deployment status and configure your Dynatrace Managed cluster.
* Manage cluster nodes and ActiveGates.
* Manage your monitoring environments.
* Create user accounts and groups.
* View licensing information and consumption status.
* View audit log and cluster events.

crash analysis

Determining the root causes of a process crash. Dynatrace accelerates crash analysis by providing a process crash entry for each affected process and monitored host. Details available for crash analysis may include a native core dump, a Java core dump, or an abnormal program exit due to exceptions. Dynatrace also provides access to additional crash artifacts, such as `hs_err_pid` files for Java crashes, text files providing Linux and Windows core dump analysis, and files containing the `.NET`, `Java`, or `Node.js` exceptions that are potentially responsible for crashes.

credential vault

A centralized location for securely storing and managing [credentials](/managed/manage/credential-vault "Store and manage credentials in the credential vault.") used for authentication and authorization in [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types."). Supported credential types are username/password pairs, certificates, and tokens. Credentials are stored in Advanced Encryption Standardâencrypted form (AES-256). Access to the data is encrypted using TLS 1.2.

The credential vault is accessible at **Settings** > **Web and mobile monitoring** > **Credential vault**.

## D

data center

From the perspective of Dynatrace Smartscape environment-topology mapping, a data center is either:

* A grouping of virtual machines running in an Amazon cloud instance. Dynatrace maps Availability Zones to your data center.
* Or a set of vCenter-based virtual hosts that transmit data to Dynatrace via a single ActiveGate. You may have multiple vCenter servers or standalone ESXi hosts associated with a single data center.

Each virtual host within a data center must have Dynatrace OneAgent installed on it. You'll see at least one data center in Smartscape view if you have an ActiveGate installed. If you don't have an ActiveGate in your environment, Smartscape can't create a data center for your topology map.

Note that Dynatrace provides real-world geographic location details for data centersâlook for data center location details in Smartscape and on **Host** pages (in the **Properties** pane).

Davis

Dynatrace AI causation engine that analyzes all the relationships and dependencies within complex IT environments to provide answers, not just data. Davis tells you when there is a problem, the business impact of the problem, and the root cause of the problem so that you can fix it quickly, including automated remediation through integration with your CI/CD tools.

Davis data units (DDUs)

Certain Dynatrace capabilities (for example, custom metric-ingestion, Log Monitoring, and event ingestion) are licensed and consumed based on a type of "currency" called [Davis data units](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). You license a certain volume of DDUs and your available quota is consumed over time based on the amount of monitoring that your environment consumes.

Digital Experience Monitoring

[Digital Experience Monitoring (DEM)ï»¿](https://www.dynatrace.com/platform/digital-experience-monitoring/) extends Application Performance Monitoring (APM) by including the outside-in perspective to ensure applications and services are available, functional, and performant across all channels of the digital customer experience in real time. Monitoring tools combine application performance data, real user behavior, synthetic monitoring, and deeper experience insights like session replays, to pinpoint digital experience issues and understand the precise impact to business KPIs.

DEM units

Dynatrace Synthetic Monitoring, Real User Monitoring, and Session Replay capabilities are licensed and consumed based on [Digital Experience Monitoring units](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units."), otherwise known as DEM units. The amount of DEM units you need depends on how many Synthetic monitors you want to run and how many user sessions you need to monitor.

Dynatrace Cluster

A "cluster" is a group of connected computers that work together to perform tasks. A Dynatrace Cluster contains one or more cluster nodes that are set up using the Dynatrace Managed installer. After successful installation, each Dynatrace Managed cluster node runs a Dynatrace Server, an ActiveGate, and one instance of Cassandra, Elasticsearch, and NGINX. Each Dynatrace Cluster also provides a web-based management interface called a [Cluster Management Console](#glossary-cmc).

## E

endpoint

A service API is defined by endpoints that provide insights into what operations are exposed by services.

* Every call to a service happens on a single endpoint.
* Dynatrace automatically derives endpoints from individual [service calls](#request), based on [endpoint detection built-in rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service#endpoint-detection "Define services on observability signals ingested via Trace ingest APIs.").

environment

See [monitoring environment](#glossary-monitoring-environment)

Environment ActiveGate

An ActiveGate that is bound to your environment, and thus only handles traffic from OneAgent instances that belong to the same environment as the ActiveGate. An Environment ActiveGate is [downloaded from your Dynatrace environment](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") and installed within your infrastructure.

An Environment ActiveGate only handles traffic from OneAgent, not from other ActiveGates. An Environment ActiveGate can communicate to a Dynatrace server either directly or via a Cluster ActiveGate.

environment topology

A Smartscape visualization of the hosts, processes, services, applications, and data centers in your Dynatrace monitoring environment and the relationships between those entities.

With no manual configuration, [Smartscapeï»¿](https://www.dynatrace.com/platform/application-topology-discovery/smartscape/) auto-discovers all the components and dependencies of your entire technology stack end-to-end and visualizes them in an easy to understand environment topology map.

event

A manual action performed on a server in your environment. Events are reported by Dynatrace and, where applicable, correlated with detected problems. Examples of events include machine reboots, system shutdowns, process restarts, and new code deployments. Any manual action you perform on a server is an event, even if it's a regularly scheduled event.

external service

Any service called by your application or another service that isn't directly monitored by Dynatrace OneAgent is considered to be an external service. Dynatrace maintains awareness of external services when they send or receive requests from your monitored services and applications. Dynatrace doesn't however receive performance data related to external services. An exception to this rule is database services. If you have Dynatrace OneAgent installed on a machine from which JDBC calls are sent to your database, Dynatrace will provide a full spectrum of performance analysis related to the called database service (even when Dynatrace OneAgent isn't installed on the database server machine itself).

## H

host unit

The size of a host for licensing purposes (based on the amount of RAM provided by a host). We use the amount of RAM on a monitored server as a measuring stick to determine the size of a host (i.e., how many host units it comprises). The advantage of this approach is its simplicityâwe donât take technology-specific factors into consideration (for example, the number of JVMs or the number of microservices that are hosted on a server). It doesn't matter if a host is .NET-based, Java-based, or something else. You can have 10 JVMs or 1,000 JVMs; such factors don't affect the amount of monitoring that an environment consumes.

For full details, see [How to calculate monitoring consumption](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

host unit hours

Represents the consumption of a host unit over a time period. **1 host unit hour equates to 1 host unit being consumed for 1 hour**. A host with 16 GB of RAM (i.e., 1 host unit) running for a full day consumes 24 host unit hours.

For full details, see [How to calculate monitoring consumption](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

HTTP monitor

A type of synthetic monitor comprising simple HTTP requests to check the availability of your API endpoints or perform simple HTTP checks for single-resource availability. As with browser monitors, [HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site.") run automatically at regular intervals from our global public or private locations. HTTP monitors executed by an [ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") from a private Synthetic location can be used to check the availability of your internal resources that are inaccessible from outside your network.

Hyperlyzer

This Dynatrace multidimensional visual interface lets you analyze multiple dimensions of the top three findings of your application's usage. With Hyperlyzer, you can see details on where your users are located, what browser versions they're using, their operating systems, and the number of different user actions your application has received. The Hyperlyzer wheel interface enables you to quickly focus on specific dimensions of interest.

Hyperlyzer data is based on detection rules, which can be configured separately for each application.

## K

key request

*Key requests* are requests that need special attention, either because they're a critical measure of the success of your business (for example, a login request or a shopping-cart checkout request) or because they provide vital technical functionality that your application relies on.

For more information, see [Monitor key requests](/managed/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.").

key performance metric

[Key performance metrics](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.") enable you to define performance goals that best fit the variable needs of each application you monitor via [RUM](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") or [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."). For RUM web applications and Synthetic browser monitors, you can select a different key performance metric for load actions, XHR actions, and any custom actions. **Visually complete** is set as the default key performance metric for load and XHR actions.

For situations where you want to tailor the key performance metric used for different features in one web application, you can select a different key performance metric for the application's different key user actions.

## L

Log Monitoring

The intelligent evaluation of data-logging records that are produced by network devices, operating systems, applications, and other intelligent or programmable devices.

Dynatrace Log Monitoring provides direct access to the log content of all your system's mission-critical processes and enables you to quickly search for specific log messages. You can filter log content [based on keywords](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") or analysis timeframe, and even analyze multiple log files simultaneouslyâeven when log files are stored across multiple hosts.

Most significantly, Dynatrace artificial intelligence automatically correlates relevant log messages with any problems that are detected in your environment. Any relevant log messages associated with a problem are factored into that problem's root-cause analysis.

log record

In Dynatrace Log Monitoring, a log record is a single log entry that contains a valid timestamp. A log record can contain multiple lines of log data. The number of log records plays an important role in DDU consumption for Log Monitoring.

## M

management zone

[Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") are a powerful information-partitioning mechanism that promote collaboration and the sharing of relevant data in your Dynatrace environment while simultaneously ensuring secure access control.

Each customizable management zone comprises a set of monitored entities or dimensional data (such as metrics) in your environment defined by [rules](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.") based on the Dynatrace tagging engine and other criteria. Access to a management zone is controlled by [user and group permissions](/managed/manage/identity-access-management/user-and-group-management "User and group management").

Management zones may overlap, just as team responsibilities often overlap. Users may be granted access to entire environments, a specific management zone, or a subset of related management zones.

merged services

A merged service is a service that aggregates multiple [web-request services](/managed/observe/application-observability/services/service-detection/service-detection-v1#web-request-service "Find out how Dynatrace Service Detection v1 detects and names different types of services.") of the same process group that perform identical functions across separate cluster nodes. These web-request services are effectively identical from a performance-monitoring perspective. A merged service appears in Dynatrace as a single service that contains all the data of all aggregated services.

Say you have an Apache web server with several virtual host definitions (for example, `dynatrace.com`, `dynatrace.at`, and `dynatrace.pl`). From the Apache perspective, these are independent virtual hosts. Dynatrace therefore detects them as separate services. For your monitoring purposes however, you might want to view these services as a single merged service called `Dynatrace web page`.

Dynatrace automatically identifies mergeable services for you and displays them on the **Merged service monitoring** page (**Settings** > **Server-side service monitoring** > **Merged service monitoring**). Only services included in this list can be merged.

For more information, see [Merged services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.").

Million Service Units (MSUs)

A measurement of the amount of processing work a computer can perform in one hour. Monitoring of OneAgent code modules that run on IBM z/OS (CICS, IMS, and Java) is based on the [licensing and consumption of MSUs](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units."), not host units.

Mission Control

The proactive support for Dynatrace Managed that automatically solves many common maintenance and support challenges for you. Mission Control's proactive support provides fully automated management capabilities that keep Dynatrace Server secure, reliable, and up-to-dateâall while saving you from administrative tasks like upgrades and troubleshooting.

A dedicated 24x7 support team proactively handles health checks, scaling verification, upgrades, and any troubleshooting when you run into problems. This includes:

* Analyzing hardware utilization and alerting you if you need more resources.
* Addressing problems or incompatibilities with your Dynatrace Serverâso you donât need to track and react to system events.
* Optimizing your Dynatrace Managed settings to ensure optimum performance and stability.
* Collecting the required log files for problem resolution.

See [How does Mission Control pro-active support work?](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") for more information.

monitoring candidate

A host that communicates with monitored hosts in your environment, but doesn't itself have Dynatrace OneAgent installed on it. It's recommended that you install Dynatrace OneAgent on all monitoring candidates to gain full visibility and complete monitoring capabilities.

In Smartscape, a candidate is visualized with dashed circles and a generic host icon. Candidates are shown linked to relevant data centers. Each monitoring candidate is also listed on the **Hosts** page, within the **Unmonitored** category.

Any inactive monitoring candidates (those that haven't communicated with a host for more than two hours) aren't included in Smartscape or listed on the **Hosts** page.

monitoring environment

Includes all the dashboards, charts, reports, and other tools that Dynatrace makes available for the analysis of your application or applications. A monitoring environment is analogous to an analysis server that provides all your Dynatrace application-performance analysis functionality.

You can set up multiple monitoring environments to group related entities for discrete analysis. For example, you might set up one monitoring environment to monitor and analyze the performance of your production clusters. You might set up a second environment that's dedicated to the performance of your developers' machines and a third environment for your staging servers. How you segment your monitoring environments is entirely up to you.

multidimensional baselining

There are a number of variables (or dimensions) that affect application performanceâmost notably, geographic region, OS, browser, connection type, and user actions. These are the five dimensions that Dynatrace uses to evaluate application health. Each subset of cohorts is subject to a unique set of these variables so Dynatrace measures the health of and reports on each of these user segments separately.

multidimensional analysis

The **Multidimensional analysis** view enables you to analyze web requests of your services with fine-tuned filtering, so you can focus your analysis on the dimensions that matter most. This view is easily configurable and serves as a convenient entry point for in-depth analysis of your services.

For more information, see [Multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.").

## O

OneAgent

Dynatrace OneAgent monitors the performance of the hosts in your application-deployment environment, along with all related processes. Based on your environment settings, Dynatrace OneAgent enables detailed performance monitoring and real user monitoring of your applications and their services. Changes to your applications, as well as infrastructure and performance problems, are reported to Dynatrace for performance monitoring.

OneAgent DaemonSet

With OneAgent DaemonSet, you can set up OneAgent on Kubernetes manually. DaemonSet is a feature that ensures that if a copy of a pod on a node dies, the copy is recreated, and if nodes are added to the cluster, copies of the pod are added as well.

OneAgent log module

With OneAgent log module ([OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")), you can set up OneAgent to [ingest](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.") and [process](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.") log data. Once enabled, OneAgent log module collects log data and streams it to Dynatrace to be analyzed by Dynatrace [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") feature. You can use a command line ([OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#log-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")) to see if the log monitoring module is enabled on your OneAgent.

OneAgent for Android

Dynatrace mobile app support for Android. Use the [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") to set up user experience monitoring for your Android application project, which automatically adds OneAgent to your app and auto-instruments it without modifying the source code. OneAgent for Android lets you track visitors, actions, and PurePathÂ® distributed traces that are triggered by your Android app.

OneAgent for iOS

Mobile app support for iOS in Dynatrace lets you track user behavior on mobile web pages. OneAgent for iOS helps you identify mobile user experience problems before they affect your users. It also lets you receive business analytics data like the geographic distribution of your web page visitors and average session duration.

Dynatrace lets you set up OneAgent for iOS with CocoaPods or Swift Package Manager, or you can set it up manually through Dynatrace to [enable UEM monitoring for iOS apps](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.").

oneagentmon device

"oneagentmon device" appears in your Windows system during Dynatrace OneAgent installation. It's used by Dynatrace for deep process monitoring. It works like a monitoring driver and allows Dynatrace OneAgent to add its own library between the operating system and the processes it's monitoring.

oneagentmon driver

A special device that appears in your Windows system during Dynatrace OneAgent installation. It's indispensable for deep monitoring purposes, as it allows Dynatrace OneAgent to add its own library between the system and the monitored processes.

opaque service

A service detected on the calling side by Dynatrace for which code-level visibility isn't available.

Dynatrace can detect requests of opaque services and identify which processes they're processed by, but Dynatrace can't monitor opaque services directly.

## P

prediction-based anomaly detection

Evaluating traffic and load anomalies carries different assumptions than evaluating performance anomalies. Dynatrace uses a range of measures and methodologies to identify performance anomalies that affect customer experience and therefore require your attention. However, traffic and load anomalies are based on daily, seasonal, and business-cycle related patterns driven by an application's business model, related marketing efforts, and sociological factors. These are fairly predictable cycles that impact traffic and load as customers use your application. Examples of predictable cycles include weekends/workweeks, workday/evening hours, and customer activity occurring on an annual cycle, such as Black Friday. Because of this, Dynatrace uses a prediction-based methodology approach to detect abnormalities in application traffic and service load.

problem

A logical grouping of information in Dynatrace that includes the AI-driven analysis, environmental context, root cause analysis, and other details provided for one or more incidents in your environment. Problems can express themselves in your environment as performance degradations, improper functionality, or lack of availability. A problem can be the result of a single "event" or multiple events.

process

A process is an instance of an executed computer program. Processes serve as containers that host services. When you look at processes you see topology information, whereas services give you code-level insight. For example, you might have a Tomcat process that hosts a web application in the form of a server-side service. While processes are host-centricâassociated with a single machine in your environmentâservices are request-centric and therefore typically span across multiple machines in a data center.

PurePathÂ® distributed traces

A distributed trace is a complete multidimensional trace of a transaction in your monitoring environmentâwith code-level visibility, topology information, and metadata to provide the highest level of data granularity and fidelity.

PurePathÂ® technology tailors the data captured by OneAgent in various tiers of your environment into a single trace, providing comprehensive visibility beginning with each monitored user action and extending to every component of your application.

process group

A logical cluster of processes that belong to the same application or deployment unit and perform the same function across multiple hosts. Process groups are key building blocks of most modern web-based applications.

process group instance

A single instance of a process group running on a specific host. Each process group instance is identified and monitored individually, allowing Dynatrace to provide detailed insights into the performance and behavior of each instance within the broader context of the process group.

process responsiveness

An assessment of process health based on response-time metrics that measure how long it takes to react to requests from other processes or clients (regardless of resource consumption).

Dynatrace measures process responsiveness on the TCP level, so a process responsiveness metric is available for any process that accepts TCP requests (for example, listening on an open port) and responds to TCP requests. Typical examples are web server processes, proxy server processes, and SQL server processes. This metric is always measurable. No process restarts or special instrumentation are required.

## R

Real User Monitoring

Dynatrace Real User Monitoring analyzes the experience that your customers have while interacting with your application. Real User Monitoring is a combination of web analytics and performance measurements that build a picture of how well your customer-facing components perform.

request

A request is a call from one service to another on a single endpoint (service call). Requests produce metrics for the called service, such as response time, throughput, and failure rate. Dynatrace identifies the following request types:

Dynamic request
:   A request is dynamic when the server compiles or modifies the information after receiving it. Examples of dynamic requests are requests served via PHP scripts (`index.php`), Java Servlets or Node.js express handlers.

Resource (static) request
:   A request is static when thereâs no additional action from the server once itâs delivered (such as requests fetching JavaScript, image, or CSS resources).

Full-service call
:   A request is a full-service call when the underlying application or process is fully monitored by Dynatrace. Full-service calls are, for example, requests to web request services. Dynatrace has complete insights into the request, and can produce server, internal, and client spans.

External service call
:   A request is an external (or opaque) service call if it goes to an external resource (for example, `https://MyDomainName.my.salesforce.com/`) or to an opaque service that does not ingest distributed traces into Dynatrace (for example, a request to a Redis process). Dynatrace can see only the calling side of the request and not what is happening inside the request.

response time

The time it takes for a service to execute and complete a task.

root cause analysis

The Dynatrace AI-driven process for understanding why detected problems occurred, along with guidance for resolving the underlying causes of problems.

Dynatrace identifies performance problems before your customers are affected by them and prioritizes problems based on customer impact, providing instant insight into problem severity and user experience impact. When Dynatrace discovers performance problems, it provides you with a single problem notification that identifies the root cause of the problem so you donât have to manually interpret dozens of data sources to figure out what needs to be fixed.

Because performance problems are seldom isolated events (they're usually symptoms of larger issues), Dynatrace artificial intelligence can analyze up to billions of events that occur within your IT environment to help you address the causes of problems, not the symptoms. Dynatrace root cause analysis also streamlines bug fixing through deep-dive analysis into source code and database statements, letting you cut down mean time to repair by 90% or more.

## S

server-side service

Web and mobile applications are built upon services that process requests like web requests, web service calls, and messaging. For example, the web requests that are sent to a specific Tomcat server are an example of a server-side service. Such services can take the form of web services, web containers, database requests, custom services, and more. Services may in turn call other services such as web services, remote services, and databases services.

Processes are essentially containers that host services. When you look at processes you are looking at topology information, whereas services can provide code-level insights. For example, you might have a Tomcat process that hosts a web application in the form of a server-side service. While processes are host-centricâassociated with a single machine in your environmentâservices are request-centric and therefore typically span across multiple machines in a data center.

service

Server-side code executed within a process group.

service backtrace

A visualization of all the services that send requests to a specific backend service. More than just showing which services directly call a specific backend service, Service backtrace shows you the sequence of service calls that leads up to each request, all the way back up to the browser click that triggered the sequence of calls.

Session Replay

Dynatrace [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") is a powerful tool that you can use to capture and visually replay user sessions. You can record all interactions that customers have with your application and replay each click and action in a movie-like experience, allowing you to recapture the complete digital experience of every user and understand the exact user actions that led to errors, resolve complaints, and conduct usability analysis.

Session Replay settings enable you to protect confidential user data by leveraging [data masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.") and permission controls for playing back recorded user sessions.

Smartscape

Using proprietary Smartscape technology, Dynatrace is able to automatically discover your entire application stack, from the data centers, hosts, and processes that comprise your infrastructure and network, through the services that comprise your applications, and extending all the way up to your applications. Dynatrace even discovers and maps all of the dependencies of these components, in real time. Dynatrace then presents its findings to you in an interactive Smartscape topology map. You can click anywhere within a Smartscape visualization to view performance statistics for each discovered entity in your environment.

Synthetic location

A [public](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") or [private location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") from which [Synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") are executed.

Dynatrace global cloud-based public Synthetic Monitoring locations support both [browser](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") and [HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Learn how to set up an HTTP monitor to check the performance and availability of your site."). You can also create private Synthetic locations within your own network infrastructure hosted on Synthetic-enabled ActiveGates. Private Synthetic locations support browser and HTTP monitors and enable you to monitor internal as well as external resources.

Synthetic Monitoring

Application availability and performance can be experienced differently by different customers around the world at any given time. [Dynatrace Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") makes it easy for you to monitor application availability and performance as your customers experience it, around the world and around the clock. Synthetic monitoring proactively simulates user visits even when no users are currently visiting your site. Synthetic monitoring provides 24x7 global visibility into your web applications by driving real web browser sessions with full HTML5/Ajax support.

## T

timeframe selector

The analysis timeframe selection tool that's in the upper-right corner of all Dynatrace pages and views. The timeframe selector enables you to filter monitoring data down to a specific time range. **Previous** and **Next** buttons enable you to move forward and backward in time based on pre-defined increments (`30 minutes`, `1 hour`, `1 day`, `1 week`, etc.). Selected timeframes remain persistent even when you move between pages and views.

## U

user action

Actions your customers perform within your application. User actions equate to common user activities such as performing a search, viewing an account balance, viewing items in a shopping cart, or ordering a product. User actions vary based on the features of your application.

From the Dynatrace perspective, each user action contains all client activity that occurs during the transition from one state to another. Each user action contains at least one web request because when a user navigates to a page, the browser downloads multiple resources and calls the JavaScript onload handler, which in turn may perform XHR requests and more.

The duration of a user action is called **action duration**. This represents the time that the user must wait before they can proceed. So a low action duration is better than a high action duration. For more details, see [What are user actions?](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.").

user session

A user session, also known as a "visit," "journey," or "clickpath," is a sequence of [user actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") that are performed by the same user in your application during a limited period of time. A single session typically includes multiple page or view loads, third-party content requests, service requests, and user actions such as clicks or taps. Each user session includes at least one user action.

For more information, see [User sessions](/managed/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").