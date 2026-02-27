---
title: Automate vulnerability remediation with GitHub Copilot and Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/ai-remediation-github-copilot
scraped: 2026-02-27T21:26:46.250668
---

# Automate vulnerability remediation with GitHub Copilot and Dynatrace

# Automate vulnerability remediation with GitHub Copilot and Dynatrace

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026
* Preview

## Overview

Not every code issue needs to be fixed. Dynatrace helps development teams focus on what matters by verifying vulnerabilities with runtime context and streamlining remediation through [GitHub Copilotï»¿](https://docs.github.com/en/copilot).
This use case demonstrates how to prioritize and remediate vulnerabilities that impact production applications. It supports two implementation paths, depending on where you want to triage and trigger fixesâboth powered by Dynatrace and GitHub integrations.

## Challenge

In complex codebases, the number of detected vulnerabilities can be overwhelming. While AI agents like GitHub Copilot can assist with automated remediation, human review and approval are still essential. Code changes may also introduce breaking changes, adding to development overhead. This makes effective prioritization and triaging of vulnerabilitiesâsupported by rich contextâcritical to maintaining velocity and stability.

## Solution

Dynatrace integrates with GitHub by enriching [Dependabot alertsï»¿](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts) with runtime context and [Runtime Vulnerability Analytics (RVA)](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") validation. This enables GitHub Copilot to take targeted action:

* **Confirmed vulnerabilities are automatically fixed**: GitHub Copilot opens a pull request with a secure fix for each vulnerability validated and confirmed by Dynatrace.

  Example

  ![GitHub Copilot coding agent applies fixes](https://dt-cdn.net/images/30603523-539a-49f2-a8ea-bdecf457877f-1056-0f4f097777.png)
* **Unconfirmed vulnerabilities are dismissed with a reason**: If Dynatrace validated a vulnerability at runtime and the vulnerable library isn't loaded or the vulnerable function isn't in use, the vulnerability is not confirmed, and GitHub Copilot dismisses the alert and explains why.

  Example

  ![GitHub Copilot coding agent automatically dismisses unconfirmed vulnerabilities](https://dt-cdn.net/images/5ef668ff-9db4-4027-a740-3c9bbe7cb836-1061-4c1d7cd672.png)

This reduces noise and developer effort by ensuring only relevant vulnerabilities are remediated.

You can implement this solution in two ways, depending on where you want to triage vulnerabilities and trigger remediation:

* [**GitHub-based workflow**](#github-based): Uses the [Dynatrace MCP Server](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp "Learn about the Dynatrace MCP server and how you can connect to it.") integrated with the [GitHub Copilot coding agentï»¿](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) or as a Dynatrace Security [custom agentï»¿](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents), triggered by a [GitHub Actions workflowsï»¿](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows).
* [**Dynatrace-driven workflow**](#dynatrace-driven): Uses [Dynatrace ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") as the trigger and processing engine, with [generative AIï»¿](https://docs.github.com/en/copilot) as the AI-driven analysis tool.

## GitHub-based workflow

This scenario uses GitHub Actions workflow to detect new critical vulnerabilities and trigger GitHub Copilot to fix only those verified by Dynatrace.

### How it works (GitHub-based workflow)

![GitHub-based - how it works](https://dt-cdn.net/images/image-60-2043-f1d3d4c1d0.png)

1. [GitHub Dependabotï»¿](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide) detects vulnerabilities in code dependencies.
2. A GitHub workflow runs on a configured period to check for new critical vulnerabilities.
3. If new vulnerabilities are found, a GitHub issue is created and assigned to GitHub Copilot.
4. GitHub Copilot verifies each vulnerability by querying Dynatrace MCP for runtime context and RVA confirmation.
5. Confirmed vulnerabilities are remediated in a pull request; unconfirmed ones are dismissed in Dependabot with a reason.
6. Developers review and merge the pull request.

### Get started (GitHub-based workflow)



To get started, follow the steps below.

1. Set up Dynatrace

* Set up monitoring with [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") for the production services.
* [Enable Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#start "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* [Create a Dynatrace platform token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") with the proper permissions to both access the MCP server and to query various event types.

  1. List permissions

  + `mcp-gateway:servers:invoke`
  + `mcp-gateway:servers:read`
  + `davis-copilot:conversations:execute`
  + `davis-copilot:nl2dql:execute`
  + `davis-copilot:dql2nl:execute`
  + `davis-copilot:document-search:execute`
  + `storage:entities:read`
  + `storage:smartscape:read`
  + `storage:buckets:read`
  + `storage:bucket-definitions:read`
  + `storage:security.events:read`
* [Request access to Dynatrace MCP Server](/docs/whats-new/preview-releases#mcp-server "Learn about our Preview releases and how you can participate in them.").

2. Prepare your GitHub repository

1. [Enable Dependabotï»¿](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository). This ensures GitHub can detect vulnerabilities in dependencies and raise alerts.
2. [Generate a fine-grained personal access token (PAT)ï»¿](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) with the proper permissions.

   1. List permissions

   * **Read**:

     + `Variables`
     + `Administration`
     + `Dependabot secrets`
     + `Environments`
     + `Metadata`
     + `Webhooks`
     + `Secrets`
   * **Read and write**:

     + `Dependabot alerts`
     + `Actions`
     + `Code scanning alerts`
     + `Custom properties`
     + `Issues`
     + `Pull requests`
     + `Workflows`
     + `Contents`
3. Store the PAT created in step 2 [as a GitHub secret for Copilot environmentï»¿](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment#setting-environment-variables-in-copilots-environment) named `COPILOT_SPONSOR_PAT`. This secret is exposed to the GitHub Copilot coding agent as an environment variable, allowing it to authenticate and perform actions in your repository on your behalf.
4. [Assign a Copilot seat to the sponsor userï»¿](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access).

3. Connect GitHub Copilot to Dynatrace

To connect GitHub Copilot with Dynatrace MCP Server:

1. [Configure Dynatrace MCP Server in your GitHub code repositoryï»¿](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).
2. Store your Dynatrace platform token as a GitHub secret for the Copilot environment named `COPILOT_MCP_DT_API_TOKEN`.
3. In your GitHub repo, go to **Settings** > **Copilot** > **Agents**.
4. Add an MCP server configuration like this:

   ```
   {



   "mcpServers":



   {



   "dynatrace": {



   "type": "http",



   "url": "https://pia1134d.dev.apps.dynatracelabs.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp",



   "headers": {



   "Authorization": "Bearer $COPILOT_MCP_DT_API_TOKEN"



   },



   "tools": ["*"]



   }



   }



   }
   ```

   Make sure to replace `your-tenant-id` with the ID of your Dynatrace environment.

For reference, see [Extending GitHub Copilot coding agent with the Model Context Protocol (MCP)ï»¿](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).

4. Add instructions for GitHub Copilot

To guide the GitHub Copilot coding agent on the verification procedure with Dynatrace, as well as required DQL knowledge for a successful Dynatrace MCP interaction, you have two options:

* **Guide GitHub Copilot coding agent through a global instructions file**: Download the [`copilot-instructions.md`ï»¿](https://dt-url.net/ug032yv) file and add it in `.github/`. For instructions, see [Adding repository custom instructions for GitHub Copilotï»¿](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).
* **Define a Dynatrace custom agent that GitHub Copilot will use to perform the use case**: Download the [`dynatrace-security-agent.md`ï»¿](https://dt-url.net/8r032d2) file and add it in `.github/agents`.

5. Set up the GitHub workflow

Download [`dependabot-alerts-processing.yml`ï»¿](https://dt-url.net/po23283) and add it in `.github/workflows/`. This checks for new critical vulnerabilities and triggers GitHub Copilot to remediate only those confirmed by Dynatrace.

For details, see [Creating your first workflowï»¿](https://docs.github.com/en/actions/get-started/quickstart#creating-your-first-workflow).

Once configured, GitHub Copilot will begin triaging and remediating vulnerabilities as new alerts are detected.

You can [test the workflowï»¿](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow) to ensure that everything is working as expected.

## Dynatrace-driven workflow

This scenario uses Dynatrace to ingest and triage GitHub Advanced Security (GHAS) alerts, then trigger GitHub Copilot to apply fixes only for vulnerabilities confirmed with runtime evidence.

### How it works (Dynatrace-driven workflow)

![Dynatrace-driven - how it works](https://dt-cdn.net/images/image-61-2188-3661817c05.png)

1. GitHub Advanced Security (GHAS) detects vulnerabilities via [Dependabotï»¿](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide).
2. The [Dynatrace integration with GHAS](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.") ingests these alerts using the GitHub Advanced Security extension and stores them in [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") for analysis.
3. A Dynatrace workflow triages alerts using runtime context and Dynatrace Intelligence generative AI workflow action for validation. For more information, see [Dynatrace Intelligence (Preview) app](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/copilot-for-workflows "Learn how to automate Dynatrace Intelligence generative AI actions and responses with workflows.").
4. A GitHub issue is created and assigned to GitHub Copilot, including both confirmed and unconfirmed vulnerabilities.
5. GitHub Copilot coding agent automatically picks up the issue, remediates confirmed vulnerabilities, and dismisses unconfirmed ones.
6. Developers review and merge the pull request with the fixes applied.

### Get started (Dynatrace-driven workflow)



To get started, follow the steps below.

1. Set up Dynatrace

* [Enable Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#start "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* [Request access to Dynatrace MCP Server](/docs/whats-new/preview-releases#mcp-server "Learn about our Preview releases and how you can participate in them.").
* [Create a Dynatrace platform token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") with the proper permissions to both access the MCP server and to query various event types.
* [Install and configure the GitHub Advanced Security integration](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.") in Dynatrace.

2. Prepare your GitHub repository

1. [Enable Dependabotï»¿](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide#enabling-dependabot-for-your-repository) to detect vulnerabilities in dependencies.
2. [Generate a fine-grained personal access token (PAT)ï»¿](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) with the proper permissions.

   1. List permissions

   * **Read**:

     + `Variables`
     + `Administration`
     + `Dependabot secrets`
     + `Environments`
     + `Metadata`
     + `Webhooks`
     + `Secrets`
   * **Read and write**:

     + `Dependabot alerts`
     + `Actions`
     + `Code scanning alerts`
     + `Custom properties`
     + `Issues`
     + `Pull requests`
     + `Workflows`
     + `Contents`
3. Store the PAT created in step 2 [as a GitHub secret for Copilot environmentï»¿](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment#setting-environment-variables-in-copilots-environment) named `COPILOT_SPONSOR_PAT`. This secret is exposed to the GitHub Copilot coding agent as an environment variable, allowing it to authenticate and perform actions in your repository on your behalf.

3. Connect GitHub Copilot to Dynatrace

To connect GitHub Copilot with Dynatrace MCP Server

1. Store your Dynatrace platform token as a GitHub secret named `COPILOT_MCP_DT_API_TOKEN`.
2. In your GitHub repo, go to **Settings** > **Copilot** > **Agents**.
3. Add an MCP server configuration like this:

   ```
   {



   "mcpServers":



   {



   "dynatrace": {



   "type": "http",



   "url": "https://pia1134d.dev.apps.dynatracelabs.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp",



   "headers": {



   "Authorization": "Bearer $COPILOT_MCP_DT_API_TOKEN"



   },



   "tools": ["*"]



   }



   }



   }
   ```

   Make sure to replace `<your-dynatrace-mcp-endpoint>` with your Dynatrace MCP URL.

For reference, see [Extending GitHub Copilot coding agent with the Model Context Protocol (MCP)ï»¿](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp).

4. Add instructions for GitHub Copilot

To help tailor suggestions from the GitHub Copilot coding agent to your coding standards and security policies, you have two options:

* **Guide GitHub Copilot coding agent through a global instructions file**: Download the [`copilot-instructions.md`ï»¿](https://dt-url.net/ug032yv) file and add it in `.github/`. For instructions, see [Adding repository custom instructions for GitHub Copilotï»¿](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions).
* **Define a Dynatrace custom agent that GitHub Copilot will use to perform the use case**: Download the [`dynatrace-security-agent.md`ï»¿](https://dt-url.net/8r032d2) file and add it in `.github/agents`.

Once configured, GitHub Copilot will begin triaging and remediating vulnerabilities as new alerts are detected.

5. Deploy and schedule the Dynatrace triaging workflow

To automate vulnerability triage and issue creation, download the following two Dynatrace workflows for Dependabot alerts and upload them in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**:

1. [GitHub Dependabot alert verification.ymlï»¿](https://dt-url.net/97432ns): This is the parent workflow, which performs the following actions:

   * Queries new GitHub Dependabot critical findings.
   * Verifies them using runtime context.
   * Prepares the issue content and calls the sub-workflow.
2. [GitHub issue creation and Copilot assignment.ymlï»¿](https://dt-url.net/ss632s6): This is the sub-workflow, called by the parent workflow to:

   * Create a GitHub issue with the verification results.
   * Assign the issue to GitHub Copilot for remediation.

   **Before running the workflow**:

   * Store the GitHub personal access token (PAT) created in step 2 (**Prepare your GitHub repository**) in the Dynatrace vault so it can be securely accessed by the workflow.
   * Update the default input configuration of the sub-workflow to specify the owner and repository where the GitHub issue should be created.
   * In the HTTP actions of the sub-workflow, reference the vault-stored credentials to authenticate GitHub API requests.

Once configured, GitHub Copilot will assist with remediating vulnerabilities by suggesting code changes based on new alerts.