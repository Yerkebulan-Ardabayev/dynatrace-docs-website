---
title: Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api
scraped: 2026-03-06T21:16:34.990823
---

# Dynatrace API


* Reference
* Updated on Feb 26, 2026

Use the Dynatrace API to automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools. API communication ensures safety by using secured communication via the HTTPS protocol.

## Basics

[Authentication](dynatrace-api/basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.")

[Response codes](dynatrace-api/basics/dynatrace-api-response-codes.md "Find out which HTTP response codes are used in the Dynatrace API.")

[Access limit](dynatrace-api/basics/access-limit.md "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Preview and Early Adopter releases](dynatrace-api/basics/preview-early-access.md "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Migration guides](dynatrace-api/basics/deprecation-migration-guides.md "Migrate your automation to newer endpoints of the Dynatrace API.")

[Grail APIsï»¿](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Endpoints

Environment

Configuration

Account Management

### ActiveGate

[Information](dynatrace-api/environment-api/activegates/activegate-info.md "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Auto-update configuration](dynatrace-api/environment-api/activegates/auto-update-config.md "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Auto-update jobs](dynatrace-api/environment-api/activegates/auto-update-jobs.md "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Anonymization

[Anonymization](dynatrace-api/environment-api/anonymization.md "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Application Security

[Vulnerabilities](dynatrace-api/environment-api/application-security/vulnerabilities.md "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](dynatrace-api/environment-api/application-security/davis-security-advice.md "View the Davis Security Advisor recommendations via Dynatrace API.")
[Attacks](dynatrace-api/environment-api/application-security/attacks.md "Find out what the Dynatrace Attacks API offers.")

### Audit logs

[Audit logs](dynatrace-api/environment-api/audit-logs.md "Read Dynatrace audit logs via Dynatrace API.")

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Business Events

[Business Events](dynatrace-api/environment-api/business-analytics-v2.md "Find out how you can ingest a business event with the Dynatrace Business Events API v2.")

### Cluster information

[Cluster information](dynatrace-api/environment-api/cluster-information.md "Find out how to check the cluster version and time with Dynatrace API.")

### Credential vault

[Credential vault](dynatrace-api/environment-api/credential-vault.md "Learn what the Dynatrace API for credentials offers.")

### Custom tags

[Custom tags of monitored entities](dynatrace-api/environment-api/custom-tags.md "Manage custom tags of the monitored entities via the Dynatrace API.")

### Deployment

[OneAgent](dynatrace-api/environment-api/deployment/oneagent.md "Download OneAgent installers via Dynatrace API.")

[ActiveGate](dynatrace-api/environment-api/deployment/activegate.md "Download ActiveGate installers via Dynatrace API.")

[BOSH tarballs](dynatrace-api/environment-api/deployment/bosh.md "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Orchestration tarballs](dynatrace-api/environment-api/deployment/orchestration.md "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### Events

[List events](dynatrace-api/environment-api/events-v2/get-events.md "List events of your monitoring environment via the Dynatrace API.")

[List event types](dynatrace-api/environment-api/events-v2/get-event-types.md "List event types via the Dynatrace API.")

[List event properties](dynatrace-api/environment-api/events-v2/get-event-properties.md "List all event properties via the Dynatrace API.")

[Ingest events](dynatrace-api/environment-api/events-v2/post-event.md "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](dynatrace-api/environment-api/extensions-20.md "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Hub capabilities

[Hub capabilities](dynatrace-api/environment-api/hub.md "Learn how to access Dynatrace Hub features via the Hub items API.")

### Log Monitoring

[Log Monitoring](dynatrace-api/environment-api/log-monitoring-v2.md "Find out what you can do with the Log Monitoring API v2.")

### Metrics

#### Version 1

[Basics](dynatrace-api/environment-api/metric-v1.md "Retrieve metric information via Timeseries v1 API.")

#### Version 2

[List metrics](dynatrace-api/environment-api/metric-v2/get-all-metrics.md "List all metrics available in your monitoring environment via Metrics v2 API.")

[Get data points](dynatrace-api/environment-api/metric-v2/get-data-points.md "Read data points of one or multiple metrics via Metrics v2 API.")

[Ingest data points](dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Metric selector](dynatrace-api/environment-api/metric-v2/metric-selector.md "Configure the metric selector for the Metric v2 API.")

[Metric expressions](dynatrace-api/environment-api/metric-v2/metric-expressions.md "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Metric units

[List units](dynatrace-api/environment-api/metrics-units/get-all-units.md "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[View a unit](dynatrace-api/environment-api/metrics-units/get-unit.md "View metadata of a metric unit via the Dynatrace API.")

[Convert units](dynatrace-api/environment-api/metrics-units/get-unit-convert.md "Convert a metric value from one unit into another via the Dynatrace API.")

### Monitored entities

[Monitored entities](dynatrace-api/environment-api/entity-v2.md "Learn about the Dynatrace Monitored entities API.")

### Network zones

[Network zones](dynatrace-api/environment-api/network-zones.md "Manage network zones via the Dynatrace API.")

### OneAgent on a host

[OneAgent on a host](dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Problems

[Problems v2](dynatrace-api/environment-api/problems-v2.md "Find out what the Dynatrace Problems v2 API offers.")

### Releases

[Releases](dynatrace-api/environment-api/releaseapi.md "Find out what the Dynatrace Releases API offers.")

### Remote configuration

[OneAgent](dynatrace-api/environment-api/remote-configuration/oneagent.md "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](dynatrace-api/environment-api/remote-configuration/activegate.md "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Geographic regions](dynatrace-api/environment-api/rum/geographic-regions.md "View requests available through the Dynatrace Geographic regions API.")

[User sessions](dynatrace-api/environment-api/rum/user-sessions.md "Learn what the Dynatrace User Sessions Query language API offers.")

[Real User Monitoring JavaScript](dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code.md "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Settings

[Settings](dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.")

### SLO

[Service-Level Objectives](dynatrace-api/environment-api/service-level-objectives.md "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

### Synthetic

[Monitors](dynatrace-api/environment-api/synthetic/synthetic-monitors.md "Manage synthetic monitors via the Synthetic v1 API.")

[Monitor executions v2](dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution.md "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Locations v1](dynatrace-api/environment-api/synthetic/synthetic-locations.md "Manage synthetic locations via the Synthetic v1 API.")

[Locations v2](dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2.md "Manage synthetic locations via the Synthetic v2 API.")

[Nodes v1](dynatrace-api/environment-api/synthetic/synthetic-nodes.md "Get synthetic nodes information via the Synthetic v1 API.")

[Nodes v2](dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2.md "Manage synthetic nodes via the Synthetic v2 API.")

[Third-party synthetic](dynatrace-api/environment-api/synthetic/third-party-synthetic.md "Push third-party synthetic data to Dynatrace via API.")

### Tokens

[Tokens v2](dynatrace-api/environment-api/tokens-v2.md "Manage Dynatrace access tokens via Dynatrace API.")

### Anomaly detection

[Applications](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications.md "Learn what the Dynatrace Anomaly detection API for applications offers.")

[AWS](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws.md "Learn what the Dynatrace Anomaly detection API for AWS offers.")

[Database services](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database.md "Learn what the Dynatrace Anomaly detection API for database services offers.")

[Disk events](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events.md "Learn what the Dynatrace Anomaly detection API for disk events offers.")

[Hosts](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts.md "Learn what the Dynatrace Anomaly detection API for hosts offers.")

[Process groups](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups.md "Learn what the Dynatrace Anomaly detection API for process groups offers.")

[Services](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services.md "Learn what the Dynatrace Anomaly detection API for services offers.")

[VMware](dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware.md "Learn what the Dynatrace Anomaly detection API for VMware offers.")

### AWS

[AWS credentials](dynatrace-api/configuration-api/aws-credentials-api.md "Learn what the Dynatrace AWS credentials config API offers.")

[AWS PrivateLink](dynatrace-api/configuration-api/aws-privatelink.md "Learn what the Dynatrace AWS PrivateLink config API offers.")

[AWS supported services](dynatrace-api/configuration-api/aws-supported-services.md "Fetch a list of AWS supported services via the Dynatrace API.")

### Azure

[Azure credentials](dynatrace-api/configuration-api/azure-credentials-api.md "Learn what the Dynatrace Azure credentials config API offers.")

[Azure supported services](dynatrace-api/configuration-api/azure-supported-services.md "Fetch a list of Azure supported services via the Dynatrace API.")

### Calculated metrics

[Mobile app metrics](dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics.md "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")

[Service metrics](dynatrace-api/configuration-api/calculated-metrics/service-metrics.md "Manage calculated service metrics via the Dynatrace configuration API.")

[Synthetic metrics](dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics.md "Manage calculated synthetic metrics via the Dynatrace configuration API.")

[Web application metrics](dynatrace-api/configuration-api/calculated-metrics/rum-metrics.md "Manage calculated web application metrics via the Dynatrace configuration API.")

### Conditional naming

[Conditional naming](dynatrace-api/configuration-api/conditional-naming.md "Learn what the Dynatrace configuration API for conditional naming offers.")

### Data privacy

[Data privacy](dynatrace-api/configuration-api/data-privacy-api.md "Learn what the Dynatrace data privacy config API offers.")

### Dashboards

[Dashboards](dynatrace-api/configuration-api/dashboards-api.md "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

### Extensions

[Extensions](dynatrace-api/configuration-api/extensions-api.md "Learn what the Dynatrace Extension API offers.")

[Plugins](dynatrace-api/configuration-api/plugins-api.md "Find out how to manage plugins via Dynatrace configuration API.")

### Mobile

[Mobile and custom app configuration](dynatrace-api/configuration-api/rum/mobile-custom-app-configuration.md "Learn what the Dynatrace mobile and custom app config API offers.")

[Mobile symbolication](dynatrace-api/configuration-api/mobile-symbolication-api.md "Manage mobile symbol files via the Dynatrace API.")

### OneAgent

[OneAgent on a host](dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host.md "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")

[OneAgent in a host group](dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group.md "Manage the configuration of OneAgent instances in your host groups via the Dynatrace API.")

[Environment-wide configuration](dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide.md "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

### Remote environments

[Remote environments](dynatrace-api/configuration-api/remote-environments.md "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

### Reports

[Reports](dynatrace-api/configuration-api/reports-api.md "Manage reports via the Dynatrace configuration API.")

### RUM

[Allowed beacon origins for CORS](dynatrace-api/configuration-api/rum/allowed-beacon-cors.md "Learn what the Dynatrace configuration API for allowed beacon origins for Cross Origin Resource Sharing offers.")

[Applications detection configuration](dynatrace-api/configuration-api/rum/application-detection-configuration.md "Learn what the Dynatrace application detection API offers.")

[Calculated web application metrics](dynatrace-api/configuration-api/calculated-metrics/rum-metrics.md "Manage calculated web application metrics via the Dynatrace configuration API.")

[Content resources](dynatrace-api/configuration-api/rum/content-resources.md "Learn what the Dynatrace configuration API for content resources offers.")

[Geographic regions - IP address mapping rules](dynatrace-api/configuration-api/rum/geographic-regions-ip-address.md "Learn what the Dynatrace configuration API for IP address mapping rules offers.")

[Geographic regions - IP mapping headers](dynatrace-api/configuration-api/rum/geographic-regions-ip-header.md "Learn what the Dynatrace configuration API for IP mapping headers offers.")

[Mobile and custom app configuration](dynatrace-api/configuration-api/rum/mobile-custom-app-configuration.md "Learn what the Dynatrace mobile and custom app config API offers.")

[Web application configuration](dynatrace-api/configuration-api/rum/web-application-configuration-api.md "Learn what the Dynatrace web application config API offers.")

### Services

[Calculated service metrics](dynatrace-api/configuration-api/calculated-metrics/service-metrics.md "Manage calculated service metrics via the Dynatrace configuration API.")

[Custom services](dynatrace-api/configuration-api/service-api/custom-services-api.md "Learn what the Dynatrace custom services config API offers.")

[Failure detection](dynatrace-api/configuration-api/service-api/failure-detection.md "Learn what the Dynatrace failure detection config API offers.")

[Request attributes](dynatrace-api/configuration-api/service-api/request-attributes-api.md "Learn what the Dynatrace request attribute config API offers.")

[Request naming](dynatrace-api/configuration-api/service-api/request-naming-api.md "Learn what the Dynatrace request naming config API offers.")

[Service detection rules](dynatrace-api/configuration-api/service-api/detection-rules.md "Learn what the Dynatrace service detection rules config API offers.")

[### User management

View and manage Dynatrace users in your account.](dynatrace-api/account-management-api/user-management-api.md "View and manage users in your Dynatrace account via the User management API.")[### Group management

View and manage user groups in your account.](dynatrace-api/account-management-api/group-management-api.md "Create and manage user groups in your Dynatrace account via the Group management API.")[### Permission management

Manage user permissions in your account.](dynatrace-api/account-management-api/permission-management-api.md "Manage permissions of user groups in your Dynatrace account via the Permission management API.")[### Policy management

Manage access policies in your account.](dynatrace-api/account-management-api/policy-management-api/policies.md "Manage access policies in your Dynatrace account via the Policy management API.")[### Account limits

View account limits of your account.](dynatrace-api/account-management-api/account-limits-api.md "View assigned account limits in your Dynatrace account via the Dynatrace API.")[### Service user management

Manage service users in your account.](dynatrace-api/account-management-api/service-user-management-api.md "Create and manage service users in your Dynatrace account via the Dynatrace API.")[### Platform tokens

Manage platform tokens of your account.](dynatrace-api/account-management-api/platform-tokens-api.md "Create and manage platform tokens in your Dynatrace account via the Dynatrace API.")[### Environment management

View monitoring environments of your Dynatrace account.](dynatrace-api/account-management-api/environment-management-api/environment-management-api.md "View monitoring environments of your Dynatrace account via Environment management API.")[### Dynatrace Platform Subscription

View your Dynatrace Platform Subscription and how it is used.](dynatrace-api/account-management-api/dynatrace-platform-subscription-api.md "Query the data about your Dynatrace Platform Subscription via the Account Management API.")[![Notifications](https://dt-cdn.net/images/account-management-icon-notifications-8f074dc2ad.svg "Notifications")

### Notifications

List notifications for your account.](dynatrace-api/account-management-api/post-notifications.md "List notifications for your account.")[### Reference data

View the reference info about your account.](dynatrace-api/account-management-api/reference-data.md "Check the reference info of your account via the Reference data API.")

## API Explorer

Environment

Configuration

Account Management

You can access all Dynatrace API endpoints using the API Explorer.

* Latest Dynatrace Go to **Access Tokens** and then select the **Dynatrace API Explorer** link.
* Previous DynatraceFrom the [user menu](discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Navigate the latest Dynatrace"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.

You can access all Dynatrace API endpoints using the API Explorer.

* Latest Dynatrace Go to **Access Tokens** and then select the **Dynatrace API Explorer** link.
* Previous DynatraceFrom the [user menu](discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Navigate the latest Dynatrace"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.

You can access all Dynatrace API endpoints using the API Explorer.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. On the top navigation bar, go to **Identity & access management** > **OAuth clients**.
3. In the upper-right corner of the page, select **Account Management API**.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.