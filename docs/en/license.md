---
title: License Dynatrace
source: https://www.dynatrace.com/docs/license
scraped: 2026-02-15T08:54:49.691960
---

# License Dynatrace

# License Dynatrace

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Sep 03, 2025

Learn how Dynatrace monitoring consumption is calculated using the Dynatrace Platform Subscription model.

Not yet using Dynatrace?

To get started using Dynatrace, [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/).

## Overview

The Dynatrace Platform Subscription (DPS) is more than a licensing modelâit's a strategic enabler for modern observability.
DPS empowers organizations to consume any Dynatrace capability, at any volume, at any time, under a single, transparent commitment.
Itâs designed to eliminate friction, simplify operations, and scale effortlessly with your business.

DPS is the licensing foundation for Dynatraceâs latest platform innovations, including [AI observability](/docs/observe/dynatrace-for-ai-observability "Learn about AI and LLM observability, what AI observability is, how Dynatrace observes Generative AI (LLM) models and AI SaaS services, and much more."), [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data."), [AppEngine](/docs/platform/appengine "Develop feature-rich Dynatrace apps for you and the world!"), and [AutomationEngine](/docs/platform/automationengine "Combine observability, security, and business data with causal AI to easily automate BizDevSecOps workflows at enterprise scale.").

Feature

Benefit

Simplicity

One contract, one rate card, one platform. No SKU juggling. No surprises.

Scalability

DPS scales with your needsâacross modules, teams, and geographies.

Frictionless use

No pre-allocation. No per-user costs. No overage penalties. Just use what you need, when you need it.

Transparency

Real-time usage and cost visibility via Account Management and DPS APIs.

Flexibility

Supports all deployments, trials, and evolving pricing models.

Dynatrace meters usage based on Coordinated Universal Time (UTC).
All references to time and date are therefore to be understood as UTC+00:00.

Prerequisites

* Unless otherwise stated, the consumption details explained here apply to the current Dynatrace Platform Subscription.

  + If you had early access to DPS licensing (prior to April 2023), please refer to the [earlier version of DPS documentation](/docs/license/subscription-and-license/subscription-and-license-dps "View license and subscription usage and consumption history Dynatrace Platform subscription licenses that were signed prior to April, 2023.").
  + If you have a Dynatrace classic licensing agreement, please refer to [classic licensing documentation](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

* Certain features of DPS, especially those related to **Account Management**, require specific [DPS permissions](/docs/license/dps-permissions "How permissions are set with the Dynatrace Platform Subscription.").

Get started

Concepts

The following pages give you an overview of how to get started with DPS, from planning your commitment through to managing and reporting budgets and spends.

[01Understanding DPS capabilities

* Explanation
* How different DPS capabilities work and how consumption is calculated and billed.](/docs/license/capabilities)[02Your license lifecycle

* Explanation
* Understand your Dynatrace DPS or Classic license lifecycle, and how it affects your consumption of Dynatrace services.](/docs/license/license-lifecycle)[03Access your DPS cost overview

* How-to guide
* View license and subscription usage and consumption history for Dynatrace SaaS, Dynatrace Managed, and the Dynatrace platform subscription model.](/docs/license/cost-overview)[04Allocate your DPS costs

* How-to guide
* Learn how to allocate costs to cost centers and products.](/docs/license/cost-allocation)[05Set budget alerts

* How-to guide
* Learn how to configure budgets in Dynatrace.](/docs/license/budget-alerts)[06Customize cost alerts

* How-to guide
* Learn how to use the Cost Monitors feature to make forecasts and cost events.](/docs/license/cost-monitors)[07Billing report

* Explanation
* View your billing to see details about accrued costs per booking date. Use this view to determine which Dynatrace monitoring costs were recognized and booked on which day.](/docs/license/billing-reports)

Account Management
:   Account Management provides forecasting, alerting, drill-downs and real-time insights into your usage patterns. You can also manage Dynatrace license and subscriptions, Dynatrace users, SSO access, and monitor Dynatrace platform adoption and environment health.

Annual commitment
:   An annual commitment is the minimum amount of money a customer agrees to spend each year as part of their DPS contract. A Dynatrace Platform Subscription agreement is typically signed for 1â3 years, with a minimum annual commitment.

Billing usage events
:   The usage of Dynatrace capabilities are recorded as Billing Usage Events (BUEs) in Grail. Further usage details are stored there as BUE attributes. You can access those via Account Management, or by building your own dashboards that have DQL queries.

Capability
:   Dynatrace licensing costs are calculated based on an environment's consumption of Dynatrace capabilities. For example, the Application & Infrastructure Observability category includes four capabilities: Full-Stack Monitoring, Infrastructure Monitoring, Mainframe Monitoring, and Foundation & Discovery. You can find them on your rate card.

Consumption
:   The use of Dynatrace leads to consumption of capabilities, which we measure in different units of measurement.

Costs
:   All usage is collected and rated using the subscriptionâs rate card. As a result, usage is transferred into costs, expressed as a monetary value. Cost is the result of usage multiplied by the price point on your rate card of the respective Dynatrace capability.

Forecast
:   Your Dynatrace Platform Subscription provides a budget summary that forecasts costs through the end of the subscription period. The algorithms use seasonal forecasting techniques, looking at past usage and predicting future usage based on repeating usage patterns and costs.

Metered usage
:   Usage is metered each time that a Dynatrace capability is used. Usage counts the amount of units the customer consumes for a specific Dynatrace capability. Each capability has a different unit of measurement, for example, "memory-Gibibyte-hours" for Full-Stack Monitoring.

On-demand usage
:   On-demand usage occurs after the minimum annual commit is reached. Dynatrace never charges penalty-style overages. Instead, customers who consume more than their minimum annual spend commitment can continue to use the platform on an on-demand basis, billed monthly at the same rates as pre-paid consumption.

Rate card
:   The rate card is a structured pricing list that outlines the cost per capabilities under the DPS model. Your individual rate card is part of your purchase order and is accessible in the Account Management portal. Each platform capability has a price point defined in the rate card.

Subscription term
:   A Dynatrace Platform Subscription agreement is typically signed for 1â3 years, with a minimum annual commitment. Each platform capability has a price point defined in the rate card that's included with your agreement.

## FAQ

### How can I manage my consumption and control my costs?

You get complete transparency into your usage through a suite of tools in the Dynatrace Account Management.
In addition to raw data, the tools provide forecasting, alerting, and drill-downs that give real-time insights into your usage patterns.

### I get access to all platform capabilities in a Dynatrace Platform Subscription contract?

Yes, the Dynatrace Platform Subscription gives you access to all platform capabilities when you sign the order form.
You can find them on your rate card.

### When does Dynatrace charge for overages?

A: Dynatrace never charges penalty-style overages.
Instead, customers who consume more than their minimum annual spend commitment can continue to use the platform on an on-demand basis, billed monthly at the same rates as pre-paid consumption.
Customers can alternatively increase their commitment spend to attain a higher discount.

### How is monitoring consumption calculated when capabilities are used for less than an hour?

When Dynatrace capabilities are used for a fraction of an hour, we round up to the nearest 15 minutes for billing purposes (for example, one minute of usage is billed as 15 minutes; an hour and three minutes of usage is billed as 1.25 hours).
This billing model is intended to be advantageous in cloud native environments where hosts and services are rapidly spun up and destroyed.

### How can I manage who can access consumption information?

This is simple to manage via permissions.
Dynatrace permissions are structured across three levels, giving flexibility and transparency on access rights across the organization.