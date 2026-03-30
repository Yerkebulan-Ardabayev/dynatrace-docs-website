---
title: Environment API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api
scraped: 2026-03-06T21:20:59.328501
---

# Environment API


* Reference
* Published Apr 01, 2019

## Basics

Authentication

Response codes

Access limit

Preview and Early Adopter releases

Migration guides

[Grail APIsï»¿](https://developer.dynatrace.com/plan/platform-services/grail-service/)

## Endpoints

### ActiveGate

Information

Auto-update configuration

Auto-update jobs

### Anonymization

Anonymization

### Application Security

Vulnerabilities

Davis Security Advisor
Attacks

### Audit logs

Audit logs

![Business Observability](https://cdn.bfldr.com/B686QPH3/at/96c9p97q7f48grj67tqhchz/Business_Analytics.svg?auto=webp&width=72&height=72 "Business Observability")

### Business Events

Business Events

### Cluster information

Cluster information

### Credential vault

Credential vault

### Custom tags

Custom tags of monitored entities

### Deployment

OneAgent

ActiveGate

BOSH tarballs

Orchestration tarballs

### Events

List events

List event types

List event properties

Ingest events

### Extensions 2.0

Extensions 2.0

### Hub capabilities

Hub capabilities

### Log Monitoring

Log Monitoring

### Metrics

#### Version 1

Basics

#### Version 2

List metrics

Get data points

Ingest data points

Metric selector

Metric expressions

### Metric units

List units

View a unit

Convert units

### Monitored entities

Monitored entities

### Network zones

Network zones

### OneAgent on a host

OneAgent on a host

### Problems

Problems v2

### Releases

Releases

### Remote configuration

OneAgent

ActiveGate

### RUM

Geographic regions

User sessions

Real User Monitoring JavaScript

### Settings

Settings

### SLO

Service-Level Objectives

### Synthetic

Monitors

Monitor executions v2

Locations v1

Locations v2

Nodes v1

Nodes v2

Third-party synthetic

### Tokens

Tokens v2

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