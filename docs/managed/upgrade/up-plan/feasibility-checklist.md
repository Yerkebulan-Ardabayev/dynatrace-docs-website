---
title: Pre-upgrade assessment
source: https://docs.dynatrace.com/managed/upgrade/up-plan/feasibility-checklist
---

# Pre-upgrade assessment

# Pre-upgrade assessment

* Published Apr 24, 2023

Before executing the upgrade of your Dynatrace Managed environments to SaaS, use the following section to collect and assess the necessary information to plan your upgrade. Go through all of the questions, taking into consideration all the environments that you plan to upgrade. In the end, solve all the issues by following recommended actions.

### Upgrade assistance approach

* #### Do you plan to leverage Dynatrace ACE Services engagement, or do you already have an active engagement?

  No

  Yes

  Prepare a good plan for your upgrade, and remember, you can always talk to a Dynatrace product expert via live chat within your Dynatrace environment.

  Reach out to your Dynatrace Sales representative contact to get further guidance.

### Data residency and redundancy

* #### Does your Dynatrace platform have to be hosted in a specific country? Which one?

  No

  Yes

  No action is required.

  Check available regions where your monitored data is stored. Contact Dynatrace Sales representative to receive planned timelines if a region is unavailable.
* #### Do you plan to merge or split environments?

  No

  Yes

  No action is required. Proceed with a one-to-one environment migration.

  Plan your environment consolidation strategy.

### Environment constraints and features

* #### What's the maximum count of monitored hosts planned in one environment?

  To find this information, in your environment, go to **Hosts** and use the quick filter to get the count for **Infrastructure only** and **Full stack**. The sum of these hosts is the maximum count of monitored hosts in the selected environment.

  Less than 3,000

  between 3,000 and 10,000

  10,000 or more

  No action is required.

  You can continue your migration. Additionally, contact the Dynatrace Sales representative to ensure the best environment instance.

  Before migration, contact the Dynatrace Sales representative so we set up the right environment limits.

* #### How many custom IP mappings do you use?

  To find this information, in your environment, go to **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations** and count the number of IP address mapping rules.

  Less than 5,000

  More than 5,000

  No action is required.

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.
* #### How many user actions per minute do you plan to monitor?

  To find this information, in your environment, go to **Data Explorer** and create a graph containing **Action count** metrics for web, mobile and custom. The highest value for these metrics is the maximum number of user actions per minute that you currently monitor.

  Less than 50,000

  Between 50,000 and 240,000

  More than 240,000

  No action is required.

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.

  Before migration, contact the Dynatrace Sales representative so that we can evaluate your environment size.
* #### How many key user actions per application do you plan to monitor?

  To find this information, in your environment, go to **Frontend**, count the number of configured key user actions for each application, and take the highest value.

  Less than 100

  More than 100

  No action is required.

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.
* #### How many key user actions in one environment do you plan to monitor?

  To find this information, in your environment, go to **Frontend**, count the number of configured key user actions for each application, and sum them up.

  Less than 500

  More than 500

  No action is required.

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.

### Data retention

* #### What's the required retention of distributed traces, code-level insights, and errors?

  To find this information, in the Cluster Management Console (CMC), go to **Environments**, select an environment, scroll to the **Storage settings** section and check the value for **Distributed traces, code insights, and errors**.

  Less than 10 days

  Between 10 and 30 days

  30 or more days

  No action is required

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.

  Before migration, contact the Dynatrace Sales representative so that we can evaluate your environment size.
* #### What's the required retention of services: Requests and request attributes?

  To find this information, in the Cluster Management Console (CMC), go to **Environments**, select an environment, scroll to the **Storage settings** section and check the value for **Services: Requests and request attributes retention**.

  Less than 35 days

  Between 35 days and 1 year

  1 year or more

  No action is required

  Contact a Dynatrace product expert via live chat so we can adjust the limit for you.

  Before migration, contact the Dynatrace Sales representative to evaluate your environment size.

Questions?

Visit the [Upgrade to SaaS forum﻿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.