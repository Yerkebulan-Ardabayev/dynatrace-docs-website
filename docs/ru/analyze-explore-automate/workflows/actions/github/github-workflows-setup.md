---
title: Set up GitHub Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup
scraped: 2026-02-24T21:31:04.287873
---

# Set up GitHub Connector

# Set up GitHub Connector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on May 07, 2025

Your Dynatrace environment can integrate with GitHub repositories using GitHub Connector ![GitHub](https://dt-cdn.net/images/github-for-workflows-new-lxjn9po-256-94579b3812.png "GitHub"). After this setup, you can start using GitHub Connector actions in your workflow to manage issues and pull requests automatically based on your monitoring data and events.

## Prerequisite

You need the `app-engine:apps:install` permission.

## Steps

### Step 1 Add a New host pattern in External requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

You need to add the `api.github.com` domain name.

### Step 2 Grant permissions to Workflows

Aside from permissions required by Workflows to run actions on your behalf, there are additional permissions required to use GitHub Connector actions.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * `app-settings:objects:read`

For more information on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 3 Authorize connection to GitHub

You need to configure connections for each of your GitHub environments.

To configure a connection

1. Create a personal access token for your GitHub account as described in [Managing your personal access tokensï»¿](https://dt-url.net/icbd0ux9). We only support cloud-based GitHub plans such as GitHub Enterprise Cloud. GitHub Enterprise Server plans aren't supported.
2. Go to **Settings** and select **Connections** > **Connectors** > **GitHub**.
3. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
4. Define your GitHub connection.

   * **Connection name**: Provide a meaningful and unique name for your connection.
   * **GitHub Type**: Select the type of authorization mechanism.
   * **GitHub token**: Provide your GitHub API token.
5. Select **Create**.

Limit your personal access token permissions

We strongly recommend that you limit the permissions of your personal access tokens to the necessary minimum. The necessary permissions for each action can be found on the [GitHub Actions page](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-actions "Integrate Workflows with GitHub services to utilize GitHub Connector actions."). For more information, see [Managing your personal access tokensï»¿](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for information about limiting the access to a certain repository or permissions/scopes. This ensures that your personal access token can be used for accessing and changing only the permitted repositories.

## Related topics

* [Actions for GitHub Connector](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-actions "Integrate Workflows with GitHub services to utilize GitHub Connector actions.")