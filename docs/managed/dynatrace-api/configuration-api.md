---
title: "Configuration API"
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api
updated: 2026-02-09
---

Automation is the key to successful IT operations. Automation is also the key to successful monitoring and how you set up your monitoring environment or software intelligence platform.

Managing your configuration is critically importantâyou probably wouldnât let anybody change the configuration of your production monitoring environment without proper staging tests.

Keeping track of all the changes within your configurations is another important aspect of what is commonly known as *configuration as code*.

Configuration as code introduces a strategy for managing your Dynatrace monitoring configurations just as you manage your source code. Managing your configurations should follow the same principles and rules that you apply to your critical, production source code. Configurations must be validated, tested, deployed, and versioned in a controlled and reproducible manner.

Without such rules, configuring your environments can result in chaos, with losses in flexibility, speed, and stability.

Dynatrace configuration API helps you keep track of your Dynatrace monitoring environment configurations. It provides the endpoints listed in the **Endpoints** section below.

## Basics

Authentication

Response codes

Access limit

Preview and Early Adopter releases

Migration guides

## Endpoints

### Anomaly detection

Applications

AWS

Database services

Disk events

Hosts

Process groups

Services

VMware

### AWS

AWS credentials

AWS PrivateLink

AWS supported services

### Azure

Azure credentials

Azure supported services

### Calculated metrics

Mobile app metrics

Service metrics

Synthetic metrics

Web application metrics

### Conditional naming

Conditional naming

### Data privacy

Data privacy

### Dashboards

Dashboards

### Extensions

Extensions

Plugins

### Mobile

Mobile and custom app configuration

Mobile symbolication

### OneAgent

OneAgent on a host

OneAgent in a host group

Environment-wide configuration

### Remote environments

Remote environments

### Reports

Reports

### RUM

Allowed beacon origins for CORS

Applications detection configuration

Calculated web application metrics

Content resources

Geographic regions - IP address mapping rules

Geographic regions - IP mapping headers

Mobile and custom app configuration

Web application configuration

### Services

Calculated service metrics

Custom services

Failure detection

Request attributes

Request naming

Service detection rules

## API Explorer

You can access all Dynatrace API endpoints using the API Explorer. From the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform"), scroll down to **Dynatrace API** and select the API section you're interested in.

Alternatively, you can access the API Explorer via the direct link `https://{your-domain}/e/{your-environment-id}/rest-api-doc/`.

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

### Try out an API call

Once you've entered your OAuth 2.0 token, you can directly execute API calls within the API explorer. Just select **Try it out** to open the parameter section of the selected API endpoint, where you can enter additional parameters and modify the request payload before executing it by selecting **Execute**.
