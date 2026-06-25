---
title: Update dashboard owners in SaaS Upgrade Assistant
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant/sua-update-dashboard-owners
scraped: 2026-05-12T12:16:23.057827
---

# Update dashboard owners in SaaS Upgrade Assistant

# Update dashboard owners in SaaS Upgrade Assistant

* Published Dec 19, 2024

Latest Dynatrace

Each dashboard must have an owner, and dashboard owners are configured in Managed with the user ID. However, a user ID in Managed will not necessarily be a valid user ID in the SaaS account. To ensure that you can see your dashboards after the migration, ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** assists with the dashboard ownership update process by doing the following.

* Checks which dashboard owners donât exist in the SaaS account and marks those dashboards, and then visualizes the results on a bar chart and creates warnings to track occurrences.
* Automatically updates dashboard owners by changing user IDs to email addresses set in the Managed cluster. If some users miss an email address, you can define an email domain to append to the user ID.
* Gives you the possibility to opt out of unwanted functionalities in the **Dashboard ownership** section in ![Edit](https://dt-cdn.net/images/share-settings-1859c5a34c.svg "Edit") **Settings**.

## Deployment

On the  **Home** page, select an environment to go to the **Upgrade overview** page, and then select the deployment type for this environment. If there's at least one dashboard within the configurations included in the deployment that's missing an owner for the SaaS account, a new step called **Update dashboard owners** will appear in the deployment procedure with:

* Information about current settings
* A chart section with information on how many

  + Dashboard owners are missing from the SaaS account.
  + Dashboards are affected by the issue of missing owners.

  This section is hidden if creating warnings in ![Edit](https://dt-cdn.net/images/share-settings-1859c5a34c.svg "Edit") **Settings** is turned off.
* **Automatic adjustments** tells you what changes will be applied during the deployment automatically and where you can

  + Check the number of changes to be applied.
  + Preview all user adjustments and apply them immediately if needed.
  + Check the number of users in the mapping who donât have an email address configured. Use the link to go to Settings and define an email domain that can be automatically appended to the user ID.

  This section is hidden if the automatic update of dashboard owners is turned off.
* **Manual adjustments** shows the number of users who wonât be automatically updated.

  + Select **Show users without replacement suggestions** to see the list of users.
  + Select a user from the list to open an automatically filled-in property bulk edit form to facilitate manual edits.

  When do you need manual adjustments?

  + When a user doesn't have an email address, and no email domain is configured.
  + The automatic update of dashboard owners is turned off.
  + Some users are missing from the mapping, which means they have dashboards but no longer exist in the Managed cluster. This often applies to users who have left the company. You can either reassign such dashboards to other users or exclude them from the deployment.

  This section is hidden if no manual adjustments are needed.

## Preview dashboard owner adjustments

Select **Preview dashboard owner adjustments** to open a pop-up window with suggested adjustments. Within that table, you can

* Browse through all dashboard owner adjustments.
* Find adjustments by the previous or new values.
* Preview changes in dashboards that contain a selected owner.
* Apply all changes immediately.

Select **Confirm** to apply all listed changes automatically during the deployment operation or select **Apply all now** to apply all changes instantly.

## Warnings

![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** checks if dashboard owners exist in the SaaS account and produces warnings in several places to guide users during the owner update process.

You might see warnings in the following:

* **Review errors** tabâone warning is produced for each dashboard. You can review them and navigate to configuration details.
* **Upgrade details: configuration** tabâa warning icon  next to the `dashboard` config type indicates that some action is required in one or more dashboards. The same icon is displayed next to the affected dashboard configurations names.

Select an affected configuration and go to the **Errors** tab within that configuration to see a warning message with instructions.

Missing dashboard owners are marked with a warning icon  inside the **Edit properties** tab.

## Suggestions

If you donât want to update all dashboard owners automatically, ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** can also display suggestions based on the mapping of email addresses exported from the Managed cluster. The suggestions are essentially the adjustments that would be automatically applied, but you can use them individually; you donât have to turn on the automatic update of dashboard owners for that.

To apply suggestions, select **Use value** in either

* The property bulk edit form
* A single configuration's **Edit properties** tab

## Dashboard ownership settings

You can also configure the automatic update of dashboard owner in the ![Edit](https://dt-cdn.net/images/share-settings-1859c5a34c.svg "Edit") **Settings** > **Dashboard ownership** section, which provides the following.

* **Automatically update dashboard owners** toggleâturned on by default. When turned off, dashboard owners wonât be updated during the deployment.
* **Create a warning if dashboard ownership is set to a user that doesnât exist in your SaaS account** toggleâturned on by default. When turned off, ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** won't check whether an owner exists. It wonât show any warnings or the chart of affected dashboards.
* Email domain inputâempty by default. As long as the configured domain is correct, itâll be appended to the user IDs of existing users without an email address. This option can prove most helpful when you're using LDAP integration (user IDs such as: `firstname.lastname` and no email addresses in the LDAP server). By appending the companyâs domain to the first and last name, ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** can produce a valid email address for SaaS users.

  The email domain wonât be appended to the missing dashboard owners from the Managed cluster's user mapping.

## Possible scenarios

### One-click deployment with default settings

#### Assumptions

* You haven't changed any settings.
* You uploaded a correct configurations archive and navigated to the source environment.
* All valid users had email addresses configured in Managed.

#### Steps

1. Select deployment step **Deploy all configurations** and **Next**.
2. In the **Update dashboard owners** step, select **Next**.
3. In the **Prepare authorization token** step, select **Generate token for 24 hours** if necessary, then select **Next**.
4. In the **Run deployment** step, select **Run full deploymentâ and confirm**.
5. In the **Upgrade results** section, wait for the deployment to finish and check the results.
   **Note:** After the deployment is finished, you might need to refresh the page to update user properties and related warnings.

Troubleshoot

* If you don't see the changes in the **Update dashboard owners** step, refresh the page.
* If you updated the owners but still see warnings, invite Managed users to the SaaS account using their Managed email as a login.
* If you invited all active users, but some warnings are still there, it might be caused by old dashboards of removed users. To solve this, you can

  + Go back to the **Update dashboard owners** step and select **Show users without replacement suggestions**. For each displayed invalid dashboard owner, select the link and edit the value in the bulk edit form. You should use an existing user's email in the **Replace with** input. After making all changes, run selective deployment with the edited dashboards.
  + Find all affected dashboards and remove them manually from your SaaS environment.

### Correcting dashboards before deployment

#### Assumptions

* You haven't changed any settings.
* You uploaded a correct configurations archive and navigated to the source environment.
* All valid users had email addresses configured in Managed.

#### Steps

1. In the **Select deployment type** step, select **Deploy all configurations**, then **Next**.
2. In the **Update dashboard owners** step

   1. In **Automatic adjustments**, select **Preview dashboard owner adjustments**.
   2. In the **Preview dashboard owner adjustments** pop-up window, review changes and select **Apply all now**.

      The following success message should appear instead of the **Preview** button.

      `All existing automatic owner replacement suggestions have already been applied.`
   3. If the number of warnings doesnât go down after the update, ensure you have invited Managed users to the SaaS account using their Managed email as a login.
   4. In **Manual adjustments**, select **Show users without replacement suggestions** and correct all those users.
   5. Select **Next** if the step is still visible. If not, go directly to the next step.
3. In the **Prepare authorization token** step, select **Generate token for 24 hours**, if necessary, then **Next**.
4. In the **Run deployment step** step, select **Run full deployment** and confirm.
5. In the **Upgrade results** section, wait for the deployment to finish.
6. Expected result: All warnings were resolved before the deployment.

### Selective deployment

1. In the **Select deployment** step, select **Choose configurations to deploy**, then **Next**.
2. Choose configurations to include in the deployment step.

   1. Go to the **Upgrade details: configuration** tab and include some dashboards in the next deployment.
   2. Select **Next**.
3. In the **Update dashboard owners** step, review adjustments and select **Next**.
4. In the **Prepare authorization token** step, select **Generate token for 24 hours**, if necessary, then **Next**.
5. In the **Run deployment** step, select **Run selective deployment** and confirm.
6. In the **Upgrade results** section, wait for the deployment to finish.
7. Expected result: Only selected configurations were modified and deployed. Other dashboards were not changed. Owners of other dashboards were also not changed unless they owned some of the selected dashboards.
8. Optional If you want to migrate more configurations, select **More configurations** and run a selective deployment a few more times. Each time, dashboard owners will be automatically updated only for the dashboards included in the deployment.

### Managed users have no email addresses

#### Assumptions

* You had LDAP integration on your Managed cluster and no email addresses in the LDAP server, so now all users are missing email addresses, but they have an easily identifiable user ID: `firstname.lastname`.
* You haven't changed any settings.
* You uploaded a correct configurations archive and navigated to the source environment.

#### Steps

1. In the **Select deployment** step, select **Deploy all configurations**, then **Next**.
2. In the **Update dashboard owners** step

   1. In **Automatic adjustments**, select **Settings**.
   2. Go to the **Dashboard ownership** section, set an email domain, and **Save**.
   3. Navigate back to the source environment.
   4. Review adjustments and select **Next**.
3. In the **Prepare authorization token** step, select **Generate token for 24 hours**, if necessary, then **Next**.
4. In the **Run deployment** step, select **Run full deployment** and confirm.
5. In the **Upgrade results** section, wait for the deployment to finish.
6. Expected result: Dashboard owners are now represented by correct emails. Warnings may still be present, and you may need to invite users to the SaaS account or correct some emails like in the basic scenario.

Email domain wasnât added to some owners.

There are two possible reasons:

* The user has been removed from the Managed cluster and is missing from the mapping.
* The user ID contains invalid characters, so appending the email domain doesnât form a correct email address.

In either case, you need to adjust such owners manually.

### Fully manual update of owners

#### Assumptions

* You turned off **Automatically update dashboard owners** and want to manually review and edit configurations.
* You uploaded a correct configurations archive and navigated to the source environment.

#### Steps

1. In the **Select deployment** step, select **Choose configurations to deploy**, then **Next**.
2. Choose configurations to include in the deployment step.

   1. Go to the **Upgrade details: configuration** tab and select **Include all**.
   2. Review configurations and exclude the ones you donât want.

      1. When reviewing dashboards, note the warning icon  and the error generated for each dashboard. If this happens for a dashboard you want to include, select the username in the error message.
      2. Select **Use value** or manually enter the correct user email.
      3. Select **Preview changes** > **Save**. If a `Changed properties were found in other configs` message appears, select **Preview changes** and **Save** again, then **Done**.
   3. Go back to the **Overview** tab and select **Next**.
3. In the **Prepare authorization token** step, select **Generate token for 24 hours** if necessary, then select **Next**.
4. In the **Run deployment** step, select **Run selective deployment** and confirm.
5. In the **Upgrade results** section, wait for the deployment to finish.

If you want to deploy other dashboards in the future and correct all owners

1. Go to **Upgrade details: configuration** > **Bulk edit**.
2. Select `Dashboard owner` as the property group.
3. The **Find** dropdown will contain all owners. Select the owners you want to edit.
4. Optional If you want to use suggestions, select **Use value**.

## FAQ

What happens if there is no user mapping?

Automatic update of dashboard owners is not possible without a user mapping. This mapping was added to Managed clusters in version 1.298. The app will display a warning if you use an old configuration package without a user mapping.

We recommend exporting the package again using an updated Managed cluster.

The user mapping is the `users.ndjson` file located in the configuration export package.

What if I donât see the Update dashboard owners step?

This could mean that all your dashboard owners are already valid SaaS users. If thatâs not the case, then make sure you have selected the deployment type. If you plan to run a selective deployment, include at least one dashboard for the step to appear.

What if the owners were automatically updated, but warnings still say theyâre missing?

Adjusting dashboard owners according to automatic suggestions doesnât guarantee that all users will be able to see their dashboards. If you encounter this issue:

* Make sure the affected userâs email address in the Managed cluster is correct.
* Create the user in your SaaS account using the correct email.