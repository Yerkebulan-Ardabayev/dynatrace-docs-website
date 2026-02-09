---
title: "Configuration API"
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api
updated: 2026-02-09
---

# Configuration API

# Configuration API

* Reference
* Published Oct 18, 2018

Automation is the key to successful IT operations. Automation is also the key to successful monitoring and how you set up your monitoring environment or software intelligence platform.

Managing your configuration is critically importantâyou probably wouldnât let anybody change the configuration of your production monitoring environment without proper staging tests.

Keeping track of all the changes within your configurations is another important aspect of what is commonly known as *configuration as code*.

Configuration as code introduces a strategy for managing your Dynatrace monitoring configurations just as you manage your source code. Managing your configurations should follow the same principles and rules that you apply to your critical, production source code. Configurations must be validated, tested, deployed, and versioned in a controlled and reproducible manner.

Without such rules, configuring your environments can result in chaos, with losses in flexibility, speed, and stability.

Dynatrace configuration API helps you keep track of your Dynatrace monitoring environment configurations. It provides the endpoints listed in the **Endpoints** section below.

## Basics

[Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

[Response codes](/managed/dynatrace-api/basics/dynatrace-api-response-codes "Find out which HTTP response codes are used in the Dynatrace API.")

[Access limit](/managed/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")

[Preview and Early Adopter releases](/managed/dynatrace-api/basics/preview-early-access "How Preview and Early Adopter releases of Dynatrace API endpoints work")

[Migration guides](/managed/dynatrace-api/basics/deprecation-migration-guides "Migrate your automation to newer endpoints of the Dynatrace API.")

## Endpoints

### Anomaly detection

[Applications](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-applications "Learn what the Dynatrace Anomaly detection API for applications offers.")

[AWS](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws "Learn what the Dynatrace Anomaly detection API for AWS offers.")

[Database services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-database "Learn what the Dynatrace Anomaly detection API for database services offers.")

[Disk events](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events "Learn what the Dynatrace Anomaly detection API for disk events offers.")

[Hosts](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts "Learn what the Dynatrace Anomaly detection API for hosts offers.")

[Process groups](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-process-groups "Learn what the Dynatrace Anomaly detection API for process groups offers.")

[Services](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-services "Learn what the Dynatrace Anomaly detection API for services offers.")

[VMware](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware "Learn what the Dynatrace Anomaly detection API for VMware offers.")

### AWS

[AWS credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api "Learn what the Dynatrace AWS credentials config API offers.")

[AWS PrivateLink](/managed/dynatrace-api/configuration-api/aws-privatelink "Learn what the Dynatrace AWS PrivateLink config API offers.")

[AWS supported services](/managed/dynatrace-api/configuration-api/aws-supported-services "Fetch a list of AWS supported services via the Dynatrace API.")

### Azure

[Azure credentials](/managed/dynatrace-api/configuration-api/azure-credentials-api "Learn what the Dynatrace Azure credentials config API offers.")

[Azure supported services](/managed/dynatrace-api/configuration-api/azure-supported-services "Fetch a list of Azure supported services via the Dynatrace API.")

### Calculated metrics

[Mobile app metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")

[Service metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Synthetic metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Manage calculated synthetic metrics via the Dynatrace configuration API.")

[Web application metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

### Conditional naming

[Conditional naming](/managed/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

### Data privacy

[Data privacy](/managed/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

### Dashboards

[Dashboards](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

### Extensions

[Extensions](/managed/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

[Plugins](/managed/dynatrace-api/configuration-api/plugins-api "Find out how to manage plugins via Dynatrace configuration API.")

### Mobile

[Mobile and custom app configuration](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Mobile symbolication](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.")

### OneAgent

[OneAgent on a host](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host "Manage the configuration of OneAgent instances on your hosts via the Dynatrace API.")

[OneAgent in a host group](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group "Manage the configuration of OneAgent instances in your host groups via the Dynatrace API.")

[Environment-wide configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

### Remote environments

[Remote environments](/managed/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")

### Reports

[Reports](/managed/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")

### RUM

[Allowed beacon origins for CORS](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors "Learn what the Dynatrace configuration API for allowed beacon origins for Cross Origin Resource Sharing offers.")

[Applications detection configuration](/managed/dynatrace-api/configuration-api/rum/application-detection-configuration "Learn what the Dynatrace application detection API offers.")

[Calculated web application metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics "Manage calculated web application metrics via the Dynatrace configuration API.")

[Content resources](/managed/dynatrace-api/configuration-api/rum/content-resources "Learn what the Dynatrace configuration API for content resources offers.")

[Geographic regions - IP address mapping rules](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Learn what the Dynatrace configuration API for IP address mapping rules offers.")

[Geographic regions - IP mapping headers](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header "Learn what the Dynatrace configuration API for IP mapping headers offers.")

[Mobile and custom app configuration](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.")

[Web application configuration](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.")

### Services

[Calculated service metrics](/managed/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")

[Custom services](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Learn what the Dynatrace custom services config API offers.")

[Failure detection](/managed/dynatrace-api/configuration-api/service-api/failure-detection "Learn what the Dynatrace failure detection config API offers.")

[Request attributes](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.")

[Request naming](/managed/dynatrace-api/configuration-api/service-api/request-naming-api "Learn what the Dynatrace request naming config API offers.")

[Service detection rules](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace services detection rules config API offers.")

## API Explorer

You can access all Dynatrace API endpoints using the API Explorer. From the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.
