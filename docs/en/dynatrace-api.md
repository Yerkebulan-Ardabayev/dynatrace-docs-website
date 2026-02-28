---
title: Dynatrace API
source: https://www.dynatrace.com/docs/dynatrace-api
scraped: 2026-02-28T21:14:22.240128
---

# Dynatrace API

# Dynatrace API

* Reference
* Updated on Feb 26, 2026

Use the Dynatrace API to automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools. API communication ensures safety by using secured communication via the HTTPS protocol.

## Basics

[Authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

[Response codes](/docs/dynatrace-api/basics/dynatrace-api-response-codes "Find out which HTTP response codes are used in the Dynatrace API.")

[Access limit](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Preview and Early Adopter releases](/docs/dynatrace-api/basics/preview-early-access "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Migration guides](/docs/dynatrace-api/basics/deprecation-migration-guides "Migrate your automation to newer endpoints of the Dynatrace API.")

[Grail APIsï»¿](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Endpoints

Environment

Configuration

Account Management

### ActiveGate

[Information](/docs/dynatrace-api/environment-api/activegates/activegate-info "List all ActiveGates currently or recently connected to the environment via the Dynatrace API.")

[Auto-update configuration](/docs/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.")

[Auto-update jobs](/docs/dynatrace-api/environment-api/activegates/auto-update-jobs "Manage auto-update jobs of your ActiveGates via the Dynatrace API.")

### Anonymization

[Anonymization](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

### Application Security

[Vulnerabilities](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")

[Davis Security Advisor](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
[Attacks](/docs/dynatrace-api/environment-api/application-security/attacks "Find out what the Dynatrace Attacks API offers.")

### Audit logs

[Audit logs](/docs/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Business Events

[Business Events](/docs/dynatrace-api/environment-api/business-analytics-v2 "Find out how you can ingest a business event with the Dynatrace Business Events API v2.")

### Cluster information

[Cluster information](/docs/dynatrace-api/environment-api/cluster-information "Find out how to check the cluster version and time with Dynatrace API.")

### Credential vault

[Credential vault](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.")

### Custom tags

[Custom tags of monitored entities](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")

### Deployment

[OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate "Download ActiveGate installers via Dynatrace API.")

[BOSH tarballs](/docs/dynatrace-api/environment-api/deployment/bosh "Download OneAgent installers as BOSH tarballs via Dynatrace API.")

[Orchestration tarballs](/docs/dynatrace-api/environment-api/deployment/orchestration "Download OneAgent installers as orchestration tarballs via Dynatrace API.")

### Events

[List events](/docs/dynatrace-api/environment-api/events-v2/get-events "List events of your monitoring environment via the Dynatrace API.")

[List event types](/docs/dynatrace-api/environment-api/events-v2/get-event-types "List event types via the Dynatrace API.")

[List event properties](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API.")

[Ingest events](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.")

### Extensions 2.0

[Extensions 2.0](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.")

### Hub capabilities

[Hub capabilities](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.")

### Log Monitoring

[Log Monitoring](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

### Metrics

#### Version 1

[Basics](/docs/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.")

#### Version 2

[List metrics](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.")

[Get data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.")

[Ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.")

[Metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")

[Metric expressions](/docs/dynatrace-api/environment-api/metric-v2/metric-expressions "Use metric expressions to apply arithmetic operations in a data points query via the Metrics API v2.")

### Metric units

[List units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.")

[View a unit](/docs/dynatrace-api/environment-api/metrics-units/get-unit "View metadata of a metric unit via the Dynatrace API.")

[Convert units](/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert "Convert a metric value from one unit into another via the Dynatrace API.")

### Monitored entities

[Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")

### Network zones

[Network zones](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

### OneAgent on a host

[OneAgent on a host](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.")

### Problems

[Problems v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.")

### Releases

[Releases](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.")

### Remote configuration

[OneAgent](/docs/dynatrace-api/environment-api/remote-configuration/oneagent "Manage the configuration of OneAgents remotely at scale using the Dynatrace API.")

[ActiveGate](/docs/dynatrace-api/environment-api/remote-configuration/activegate "Manage the configuration of ActiveGates remotely at scale using the Dynatrace API.")

### RUM

[Geographic regions](/docs/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.")

[User sessions](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.")

[Real User Monitoring JavaScript](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.")

### Settings

[Settings](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

### SLO

[Service-Level Objectives](/docs/dynatrace-api/environment-api/service-level-objectives "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

### Synthetic

[Monitors](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")

[Monitor executions v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API.")

[Locations v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations "Manage synthetic locations via the Synthetic v1 API.")

[Locations v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.")

[Nodes v1](/docs/dynatrace-api/environment-api/synthetic/synthetic-nodes "Get synthetic nodes information via the Synthetic v1 API.")

[Nodes v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.")

[Third-party synthetic](/docs/dynatrace-api/environment-api/synthetic/third-party-synthetic "Push third-party synthetic data to Dynatrace via API.")

### Tokens

[Tokens v2](/docs/dynatrace-api/environment-api/tokens-v2 "Manage Dynatrace access tokens via Dynatrace API.")

### Anomaly detection

[Applications](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Learn what the Dynatrace Anomaly detection API for applications offers.")

[AWS](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Learn what the Dynatrace Anomaly detection API for AWS offers.")

[Database services](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Learn what the Dynatrace Anomaly detection API for database services offers.")

[Disk events](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Learn what the Dynatrace Anomaly detection API for disk events offers.")

[Hosts](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Learn what the Dynatrace Anomaly detection API for hosts offers.")

[Process groups](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Learn what the Dynatrace Anomaly detection API for process groups offers.")

[Services](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Learn what the Dynatrace Anomaly detection API for services offers.")

[VMware](/docs/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Learn what the Dynatrace Anomaly detection API for VMware offers.")

### AWS

[AWS credentials](/docs/dynatrace-api/configuration-api/aws-credentials-api "Learn what the Dynatrace AWS credentials config API offers.")

[AWS PrivateLink](/docs/dynatrace-api/configuration-api/aws-privatelink "Learn what the Dynatrace AWS PrivateLink config API offers.")

[AWS supported services](/docs/dynatrace-api/configuration-api/aws-supported-services "Fetch a list of AWS supported services via the Dynatrace API.")

### Azure

[Azure credentials](/docs/dynatrace-api/configuration-api/azure-credentials-api "Learn what the Dynatrace Azure credentials config API offers.")

[Azure supported services](/docs/dynatrace-api/configuration-api/azure-supported-services "Fetch a list of Azure supported services via the Dynatrace API.")

### Calculated metrics

[Mobile app metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")

[Service metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Synthetic metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Manage calculated synthetic metrics via the Dynatrace configuration API.")

[Web application metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

### Conditional naming

[Conditional naming](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

### Data privacy

[Data privacy](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

### Dashboards

[Dashboards](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

### Extensions

[Extensions](/docs/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

[Plugins](/docs/dynatrace-api/configuration-api/plugins-api "Find out how to manage plugins via Dynatrace configuration API.")

### Mobile

[Mobile and custom app configuration](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Mobile symbolication](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.")

### OneAgent

[OneAgent on a host](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")

[OneAgent in a host group](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Manage the configuration of OneAgent instances in your host groups via the Dynatrace API.")

[Environment-wide configuration](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

### Remote environments

[Remote environments](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

### Reports

[Reports](/docs/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")

### RUM

[Allowed beacon origins for CORS](/docs/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Learn what the Dynatrace configuration API for allowed beacon origins for Cross Origin Resource Sharing offers.")

[Applications detection configuration](/docs/dynatrace-api/configuration-api/rum/application-detection-configuration "Learn what the Dynatrace application detection API offers.")

[Calculated web application metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

[Content resources](/docs/dynatrace-api/configuration-api/rum/content-resources "Learn what the Dynatrace configuration API for content resources offers.")

[Geographic regions - IP address mapping rules](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Learn what the Dynatrace configuration API for IP address mapping rules offers.")

[Geographic regions - IP mapping headers](/docs/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Learn what the Dynatrace configuration API for IP mapping headers offers.")

[Mobile and custom app configuration](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Web application configuration](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.")

### Services

[Calculated service metrics](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Custom services](/docs/dynatrace-api/configuration-api/service-api/custom-services-api "Learn what the Dynatrace custom services config API offers.")

[Failure detection](/docs/dynatrace-api/configuration-api/service-api/failure-detection "Learn what the Dynatrace failure detection config API offers.")

[Request attributes](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")

[Request naming](/docs/dynatrace-api/configuration-api/service-api/request-naming-api "Learn what the Dynatrace request naming config API offers.")

[Service detection rules](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")

[### User management

View and manage Dynatrace users in your account.](/docs/dynatrace-api/account-management-api/user-management-api "View and manage users in your Dynatrace account via the User management API.")[### Group management

View and manage user groups in your account.](/docs/dynatrace-api/account-management-api/group-management-api "Create and manage user groups in your Dynatrace account via the Group management API.")[### Permission management

Manage user permissions in your account.](/docs/dynatrace-api/account-management-api/permission-management-api "Manage permissions of user groups in your Dynatrace account via the Permission management API.")[### Policy management

Manage access policies in your account.](/docs/dynatrace-api/account-management-api/policy-management-api/policies "Manage access policies in your Dynatrace account via the Policy management API.")[### Account limits

View account limits of your account.](/docs/dynatrace-api/account-management-api/account-limits-api "View assigned account limits in your Dynatrace account via the Dynatrace API.")[### Service user management

Manage service users in your account.](/docs/dynatrace-api/account-management-api/service-user-management-api "Create and manage service users in your Dynatrace account via the Dynatrace API.")[### Platform tokens

Manage platform tokens of your account.](/docs/dynatrace-api/account-management-api/platform-tokens-api "Create and manage platform tokens in your Dynatrace account via the Dynatrace API.")[### Environment management

View monitoring environments of your Dynatrace account.](/docs/dynatrace-api/account-management-api/environment-management-api/environment-management-api "View monitoring environments of your Dynatrace account via Environment management API.")[### Dynatrace Platform Subscription

View your Dynatrace Platform Subscription and how it is used.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api "Query the data about your Dynatrace Platform Subscription via the Account Management API.")[### Reference data

View the reference info about your account.](/docs/dynatrace-api/account-management-api/reference-data "Check the reference info of your account via the Reference data API.")

## API Explorer

Environment

Configuration

Account Management

You can access all Dynatrace API endpoints using the API Explorer.

* Latest Dynatrace Go to **Access Tokens** and then select the **Dynatrace API Explorer** link.
* Previous DynatraceFrom the [user menu](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.

You can access all Dynatrace API endpoints using the API Explorer.

* Latest Dynatrace Go to **Access Tokens** and then select the **Dynatrace API Explorer** link.
* Previous DynatraceFrom the [user menu](/docs/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the latest Dynatrace"), scroll down to **Dynatrace API** and select the API section you're interested in.

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