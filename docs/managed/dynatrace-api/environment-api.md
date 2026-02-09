---
title: "Environment API"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api
updated: 2026-02-09
---

# Environment API

# Environment API

* Reference
* Published Apr 01, 2019

## Basics

[Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

[Response codes](/managed/dynatrace-api/basics/dynatrace-api-response-codes "Find out which HTTP response codes are used in the Dynatrace API.")

[Access limit](/managed/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Preview and Early Adopter releases](/managed/dynatrace-api/basics/preview-early-access "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Migration guides](/managed/dynatrace-api/basics/deprecation-migration-guides "Migrate your automation to newer endpoints of the Dynatrace API.")

## Endpoints

### ActiveGate

[Information](/managed/dynatrace-api/environment-api/activegates/activegate-info "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Auto-update configuration](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Auto-update jobs](/managed/dynatrace-api/environment-api/activegates/auto-update-jobs "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Anonymization

[Anonymization](/managed/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Application Security

[Vulnerabilities](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
[Attacks](/managed/dynatrace-api/environment-api/application-security/attacks "Find out what the Dynatrace Attacks API offers.")

### Audit logs

[Audit logs](/managed/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")

### Cluster information

[Cluster information](/managed/dynatrace-api/environment-api/cluster-information "Find out how to check the cluster version and time with Dynatrace API.")

### Credential vault

[Credential vault](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

### Custom tags

[Custom tags of monitored entities](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")

### Deployment

[OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate "Download ActiveGate installers via Dynatrace API.")

[BOSH tarballs](/managed/dynatrace-api/environment-api/deployment/bosh "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Orchestration tarballs](/managed/dynatrace-api/environment-api/deployment/orchestration "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### Events

[List events](/managed/dynatrace-api/environment-api/events-v2/get-events "List events of your monitoring environment via the Dynatrace API.")

[List event types](/managed/dynatrace-api/environment-api/events-v2/get-event-types "List event types via the Dynatrace API.")

[List event properties](/managed/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API.")

[Ingest events](/managed/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Hub capabilities

[Hub capabilities](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.")

### Log Monitoring

[Log Monitoring](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

### Metrics

#### Version 1

[Basics](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.")

#### Version 2

[List metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.")

[Get data points](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.")

[Ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Metric selector](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")

[Metric expressions](/managed/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Metric units

[List units](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[View a unit](/managed/dynatrace-api/environment-api/metrics-units/get-unit "View metadata of a metric unit via the Dynatrace API.")

[Convert units](/managed/dynatrace-api/environment-api/metrics-units/get-unit-convert "Convert a metric value from one unit into another via the Dynatrace API.")

### Monitored entities

[Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")

### Network zones

[Network zones](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

### OneAgent on a host

[OneAgent on a host](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Problems

[Problems v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")

### Releases

[Releases](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.")

### Remote configuration

[OneAgent](/managed/dynatrace-api/environment-api/remote-configuration/oneagent "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](/managed/dynatrace-api/environment-api/remote-configuration/activegate "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Geographic regions](/managed/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.")

[User sessions](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.")

[Real User Monitoring JavaScript](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Settings

[Settings](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

### SLO

[Service-Level Objectives Classic](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.")

### Synthetic

[Monitors](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")

[Monitor executions v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Locations v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations "Manage synthetic locations via the Synthetic v1 API.")

[Locations v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.")

[Nodes v1](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes "Get synthetic nodes information via the Synthetic v1 API.")

[Nodes v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.")

[Third-party synthetic](/managed/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic data to Dynatrace via API.")

### Tokens

[Tokens v2](/managed/dynatrace-api/environment-api/tokens-v2 "Manage Dynatrace access tokens via Dynatrace API.")

## API Explorer

You can access all Dynatrace API endpoints using the API Explorer. From the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.
