---
title: Update configuration via editable properties
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant/sua-update-editable-properties
---

# Update configuration via editable properties

# Update configuration via editable properties

* Published Dec 07, 2023

Latest Dynatrace

There are two edit modes available in ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**: single and bulk (multiple).

## Update a single configuration

To update a single configuration

1. In the Dynatrace Launcher, select ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**.
2. [**Start upgrade with SaaS Upgrade Assistant**](/managed/upgrade/saas-upgrade-assistant/sua-get-started "Upload configuration and deploy with SaaS Upgrade Assistant.")
3. Select the **Upgrade details: configuration** tab.
4. Filter configurations with **Config type** selector and type configuration name or ID.
5. Select a configuration object from the left panel.
6. Select the **Edit properties** tab.
7. Type a new value in the input box.
8. Select **Preview changes**.
9. Review the change and confirm by selecting **Save**.

## Update multiple configurations

To update multiple configurations at once

1. In the Dynatrace Launcher, select ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**.
2. [**Start upgrade with SaaS Upgrade Assistant**](/managed/upgrade/saas-upgrade-assistant/sua-get-started "Upload configuration and deploy with SaaS Upgrade Assistant.")
3. Select the **Configuration** tab.
4. Filter configurations with the **Config type** selector and/or type configuration name or ID.
5. Select **Bulk edit**. The number in parentheses indicates the number of editable properties.
6. Select **Property group**.
7. Choose a value to find from the selector.
8. Type a new value in the **Replace with** input box.
9. Select **Preview changes**.
10. Review the change and confirm by selecting **Save**.

## Example: Private Synthetic location

This example serves as a best practice for successful configuration migration.

You can run your Dynatrace synthetic monitors from a [private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."), a location in your private network infrastructure where you install one or more Synthetic-enabled ActiveGate instances. A private Synthetic location is bound to ActiveGate by the ActiveGate ID. To migrate that configuration, install a new ActiveGate for your SaaS environment and obtain its ID from the **Deployment status** page. Then use ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** to update private Synthetic location configuration:

1. Select **Configuration** tab.
2. In **Config type** select `Synthetic location`.
3. Select a private Synthetic location's configuration object from the left panel.
4. Select **Edit** ![Edit](https://dt-cdn.net/images/dashboards-app-dashboard-rename-a2875a87a2.svg "Edit") button.
5. Paste the new ActiveGate ID.
6. Select **Preview changes** button.
7. Review the change and confirm by selecting **Save** button.
8. Select **Overview** navigation tab.
9. Select **Start upgrade** to deploy your changes.