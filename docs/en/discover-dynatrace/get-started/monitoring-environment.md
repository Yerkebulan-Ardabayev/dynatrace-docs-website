---
title: What is a monitoring environment?
source: https://www.dynatrace.com/docs/discover-dynatrace/get-started/monitoring-environment
scraped: 2026-02-16T21:10:55.296821
---

# What is a monitoring environment?

# What is a monitoring environment?

* Latest Dynatrace
* 4-min read
* Published Dec 05, 2017

Your Dynatrace monitoring environment is where all your Dynatrace performance analysis takes place. [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") sends all captured monitoring data to your monitoring environment for analysis. A monitoring environment is analogous to an analysis server that provides all Dynatrace application-performance analysis functionality, including all dashboards, charts, reports and other tools.

![Dynatrace architecture](https://dt-cdn.net/images/dynatrace-architecture-1743-fab92236e8.png)

## Monitoring environment location

Your monitoring environment location depends on your deployment type.

| Deployment type | Monitoring environment location |
| --- | --- |
| Standard SaaS | In the Dynatrace cloud |
| On-premises | In your own data center |
| Dynatrace for Government | In the cloud with FedRAMP moderate authorization |

## Environment ID

All external access to your Dynatrace monitoring environment relies on two credential types: an *environment ID* and an [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").

Each environment that you monitor with Dynatrace is identified with a unique character stringâthe environment ID. The Dynatrace API relies heavily on environment IDs to ensure that it pulls monitoring data from and pushes relevant external events to the correct Dynatrace environments.

* In Dynatrace SaaS, your environment ID is the first part of your Dynatrace environment's URL:

  ```
  https://{your-environment-id}.live.dynatrace.com/
  ```

  For example, for the Dynatrace environment `https://abc123a.dynatrace.com`, the environment ID is `abc123a`.

  You can also find your environment ID in [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.").

  1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
  2. Select **Settings** > **Environments**.

     You can find the environment ID in the **Environment** column.

For example, for the URL address `https://managed-cluster/e/abc123a`, the environment ID is `abc123a`.

## Multiple monitoring environments

You can set up and monitor separate Dynatrace monitoring environments with a single Dynatrace account.

When you set up multiple monitoring environments:

* Each monitoring environment shares the same user base and other account settings.
* The data collected from each monitoring environment is kept separate.
* It's easy to switch between monitoring views for separate environments to track the performance and availability of each environment.

### Use cases

There are several reasons people choose to create separate monitoring environments.

For example:

* You may want to monitor your organization's development, staging, and production environments separately.
* You may want to maintain a separate monitoring environment for each of your organization's data centers.

### Set up multiple monitoring environments

How you set up different monitoring environments depends on whether you use Dynatrace SaaS, Dynatrace Managed, or Dynatrace for Government.

| Deployment type | How set up different monitoring environments |
| --- | --- |
| SaaS | Contact a Dynatrace product expert via live chat within your Dynatrace environment; the product expert will make sure you get the assistance you need. |
| Managed | You can use the Cluster Management Console. For details, see [Managed - managed-monitoring-environmentï»¿](https://docs.dynatrace.com/managed/shortlink/managed-monitoring-environment). |
| Dynatrace for Government | Contact your Dynatrace representative. |

### Connect my multiple environments

With multiple environments, monitoring data is strictly separated by design. Environments do not automatically receive information one from another.

In some scenarios, however, you might need to connect your environments. For example:

* To trace calls between services monitored in different Dynatrace environments, you can configure cross-environment tracing. For details, see [Set up cross-environment tracing](/docs/observe/application-observability/distributed-traces/analysis/connect-environments "Analyze requests across environment boundaries.").
* To display metrics from remote environments on your local environment's dashboards, you can set up cross-environment dashboard tiles. For details, see [Create remote/multi-environment Dynatrace dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.").