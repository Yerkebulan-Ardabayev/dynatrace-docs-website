---
title: Set up GitLab Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-setup
scraped: 2026-02-16T21:24:21.515039
---

# Set up GitLab Connector

# Set up GitLab Connector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 07, 2025

Use GitLab Connector ![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows") to integrate your Dynatrace environment with GitLab repositories. This integration enables you to use GitLab Connector actions in your workflow to manage issues and merge requests automatically based on your monitoring data and events.

## Steps

### Step 1 Add a New host pattern in External requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

You need to add the `*.gitlab.com` domain name.

### Step 2 Grant permissions to Workflows

Aside from permissions required by Workflows to run actions on your behalf, there are additional permissions required to use GitLab Connector actions.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permission besides the general Workflows permission:

* `app-settings:objects:read`

To learn more about Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 3 Authorize connection to GitLab

You need a configured connection for each of your GitLab environments.

To configure a connection

1. Go to **Settings** and select **Connections** > **Connectors** > **GitLab**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
3. Define your GitLab connection.

   * **Connection name**: Provide a meaningful name for your connection.
   * **GitLab URL**: Add the URL of your GitLab environment.
   * **GitLab token**: Provide your GitLab API token.
4. Select **Create**.

The GitLab token needs the scopes `api`, `read_repository`, `read_user`, and `write_repository`.
Scopes can be skipped if related actions are not used.
Refer to the GitLab documentation for details on which scope is needed for which action.

## Related topics

* [Actions for GitLab Connector](/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-actions "List of available actions in GitLab Connector.")
* [GitLab Connector](/docs/analyze-explore-automate/workflows/actions/gitlab "Integrate Workflows with GitLab.")