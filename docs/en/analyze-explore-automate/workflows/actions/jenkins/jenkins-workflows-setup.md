---
title: Set up Jenkins Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/jenkins/jenkins-workflows-setup
scraped: 2026-02-26T21:21:04.042185
---

# Set up Jenkins Connector

# Set up Jenkins Connector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 07, 2025

### Step 1 Add a New host pattern in External requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

### Step 2 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf.
Other permissions are required by actions that come bundled with Jenkins Connector itself.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

* Permissions needed for Jenkins workflow actions:

  + `app-settings:objects:read`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 3 Configure Jenkins connection

You need a configured connection for each of your Jenkins environments.

To configure a connection

1. Open ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** and go to **Connections** > **Jenkins**.
2. Select  **Connection**.
3. Describe your Jenkins connection.

   * **Connection name**: Provide a meaningful name for your connection.
   * **Jenkins URL**: Add the URL of your Jenkins environment.
   * **Username**: Provide your Jenkins username.
   * **Password**: Provide your Jenkins password.
4. Select **Create**.