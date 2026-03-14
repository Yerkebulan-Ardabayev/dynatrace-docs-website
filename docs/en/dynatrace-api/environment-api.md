---
title: Environment API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api
scraped: 2026-03-06T21:20:59.328501
---

# Environment API


* Reference
* Published Apr 01, 2019

## Basics

[Authentication](basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.")

[Response codes](basics/dynatrace-api-response-codes.md "Find out which HTTP response codes are used in the Dynatrace API.")

[Access limit](basics/access-limit.md "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Preview and Early Adopter releases](basics/preview-early-access.md "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Migration guides](basics/deprecation-migration-guides.md "Migrate your automation to newer endpoints of the Dynatrace API.")

[Grail APIsï»¿](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Endpoints

### ActiveGate

[Information](environment-api/activegates/activegate-info.md "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Auto-update configuration](environment-api/activegates/auto-update-config.md "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Auto-update jobs](environment-api/activegates/auto-update-jobs.md "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Anonymization

[Anonymization](environment-api/anonymization.md "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Application Security

[Vulnerabilities](environment-api/application-security/vulnerabilities.md "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](environment-api/application-security/davis-security-advice.md "View the Davis Security Advisor recommendations via Dynatrace API.")
[Attacks](environment-api/application-security/attacks.md "Find out what the Dynatrace Attacks API offers.")

### Audit logs

[Audit logs](environment-api/audit-logs.md "Read Dynatrace audit logs via Dynatrace API.")

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Business Events

[Business Events](environment-api/business-analytics-v2.md "Find out how you can ingest a business event with the Dynatrace Business Events API v2.")

### Cluster information

[Cluster information](environment-api/cluster-information.md "Find out how to check the cluster version and time with Dynatrace API.")

### Credential vault

[Credential vault](environment-api/credential-vault.md "Learn what the Dynatrace API for credentials offers.")

### Custom tags

[Custom tags of monitored entities](environment-api/custom-tags.md "Manage custom tags of the monitored entities via the Dynatrace API.")

### Deployment

[OneAgent](environment-api/deployment/oneagent.md "Download OneAgent installers via Dynatrace API.")

[ActiveGate](environment-api/deployment/activegate.md "Download ActiveGate installers via Dynatrace API.")

[BOSH tarballs](environment-api/deployment/bosh.md "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Orchestration tarballs](environment-api/deployment/orchestration.md "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### Events

[List events](environment-api/events-v2/get-events.md "List events of your monitoring environment via the Dynatrace API.")

[List event types](environment-api/events-v2/get-event-types.md "List event types via the Dynatrace API.")

[List event properties](environment-api/events-v2/get-event-properties.md "List all event properties via the Dynatrace API.")

[Ingest events](environment-api/events-v2/post-event.md "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](environment-api/extensions-20.md "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Hub capabilities

[Hub capabilities](environment-api/hub.md "Learn how to access Dynatrace Hub features via the Hub items API.")

### Log Monitoring

[Log Monitoring](environment-api/log-monitoring-v2.md "Find out what you can do with the Log Monitoring API v2.")

### Metrics

#### Version 1

[Basics](environment-api/metric-v1.md "Retrieve metric information via Timeseries v1 API.")

#### Version 2

[List metrics](environment-api/metric-v2/get-all-metrics.md "List all metrics available in your monitoring environment via Metrics v2 API.")

[Get data points](environment-api/metric-v2/get-data-points.md "Read data points of one or multiple metrics via Metrics v2 API.")

[Ingest data points](environment-api/metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Metric selector](environment-api/metric-v2/metric-selector.md "Configure the metric selector for the Metric v2 API.")

[Metric expressions](environment-api/metric-v2/metric-expressions.md "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Metric units

[List units](environment-api/metrics-units/get-all-units.md "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[View a unit](environment-api/metrics-units/get-unit.md "View metadata of a metric unit via the Dynatrace API.")

[Convert units](environment-api/metrics-units/get-unit-convert.md "Convert a metric value from one unit into another via the Dynatrace API.")

### Monitored entities

[Monitored entities](environment-api/entity-v2.md "Learn about the Dynatrace Monitored entities API.")

### Network zones

[Network zones](environment-api/network-zones.md "Manage network zones via the Dynatrace API.")

### OneAgent on a host

[OneAgent on a host](environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Problems

[Problems v2](environment-api/problems-v2.md "Find out what the Dynatrace Problems v2 API offers.")

### Releases

[Releases](environment-api/releaseapi.md "Find out what the Dynatrace Releases API offers.")

### Remote configuration

[OneAgent](environment-api/remote-configuration/oneagent.md "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](environment-api/remote-configuration/activegate.md "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Geographic regions](environment-api/rum/geographic-regions.md "View requests available through the Dynatrace Geographic regions API.")

[User sessions](environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.")

[Real User Monitoring JavaScript](environment-api/rum/real-user-monitoring-javascript-code.md "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Settings

[Settings](environment-api/settings.md "Find out what the Dynatrace Settings API offers.")

### SLO

[Service-Level Objectives](environment-api/service-level-objectives.md "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

### Synthetic

[Monitors](environment-api/synthetic/synthetic-monitors.md "Manage synthetic monitors via the Synthetic v1 API.")

[Monitor executions v2](environment-api/synthetic-v2/synthetic-monitor-execution.md "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Locations v1](environment-api/synthetic/synthetic-locations.md "Manage synthetic locations via the Synthetic v1 API.")

[Locations v2](environment-api/synthetic-v2/synthetic-locations-v2.md "Manage synthetic locations via the Synthetic v2 API.")

[Nodes v1](environment-api/synthetic/synthetic-nodes.md "Get synthetic nodes information via the Synthetic v1 API.")

[Nodes v2](environment-api/synthetic-v2/synthetic-nodes-v2.md "Manage synthetic nodes via the Synthetic v2 API.")

[Third-party synthetic](environment-api/synthetic/third-party-synthetic.md "Push third-party synthetic data to Dynatrace via API.")

### Tokens

[Tokens v2](environment-api/tokens-v2.md "Manage Dynatrace access tokens via Dynatrace API.")

## API Explorer

You can access all Dynatrace API endpoints using the API Explorer.

* Latest Dynatrace Go to **Access Tokens** and then select the **Dynatrace API Explorer** link.
* Previous DynatraceFrom the [user menu](../discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Navigate the latest Dynatrace"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.