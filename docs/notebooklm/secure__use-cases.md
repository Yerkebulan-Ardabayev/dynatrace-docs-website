# Dynatrace Documentation: secure/use-cases

Generated: 2026-02-17

Files combined: 17

---


## Source: ai-remediation-github-copilot.md


---
title: Automate vulnerability remediation with GitHub Copilot and Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/ai-remediation-github-copilot
scraped: 2026-02-17T04:58:48.943181
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


---


## Source: ai-remediation-kiro-cli.md


---
title: Automate cloud misconfiguration triaging and remediation with Kiro CLI and Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/ai-remediation-kiro-cli
scraped: 2026-02-16T21:32:52.821154
---

# Automate cloud misconfiguration triaging and remediation with Kiro CLI and Dynatrace

# Automate cloud misconfiguration triaging and remediation with Kiro CLI and Dynatrace

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026
* Preview

## Overview

Not every cloud misconfiguration needs to be fixed. Dynatrace helps SREs focus on what matters by verifying cloud misconfigurations with runtime context and streamlining remediation with [Kiro CLIï»¿](https://kiro.dev/cli/). This use case demonstrates how to prioritize and remediate cloud misconfigurations that impact production applications. It supports two implementation paths, depending on where and how you want to triage the issuesâboth powered by Dynatrace and Kiro CLI integrations.

## Challenge

In complex cloud environments, the number of high and critical findings that need to be handled is very high. SREs cannot handle all of them, and they need an effective way to remediate those misconfigurations that risk their environments and introduce compliance issues. Cloud misconfiguration might not have a direct impact on production applications. An additional validation and context is needed for more effective triage and remediation efforts.

## Solution

Dynatrace integrates with AWS products, such as [AWS Security Hubï»¿](https://aws.amazon.com/de/security-hub/), to enrich their findings with additional runtime context and verify them for production impact.

* Confirmed findings require an immediate fix, which can be automated with the Kiro CLI.
* Unconfirmed findings can be suppressed to remove them from the list of active issues.

This reduces noise and SRE effort by ensuring only relevant misconfigurations are remediated.

You can implement this solution in two ways, depending on where you want to triage cloud misconfigurations:

* [**Kiro CLI-based triaging**](#kiro-cli-triaging): Uses Kiro CLI as the main engagement point, connected to Dynatrace and (natively) AWS MCP servers. Users interact with Kiro CLI to first get the top cloud misconfigurations, contextualize and prioritize with Dynatrace context, and finally, remediate them.
* [**Dynatrace-driven triaging**](#dynatrace-triaging): Uses ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** as the main triaging engine with Dynatrace Intelligence generative AI workflow action to summarize the outcomes into a Jira ticket. The rest of the flow takes place in the Kiro CLI as in the first scenario.

## Prerequisites

See below for the [AWS](#aws) and [Dynatrace](#dt) requirements.

### AWS

* Enable AWS Security Hub to monitor your AWS environment.
* Install [Kiro CLIï»¿](https://kiro.dev/cli/) and authenticate it with AWS.

### Dynatrace

* [Set up Dynatrace AWS monitoring](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.") for the desired AWS environment.

* [Set up Dynatrace integration with AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace.").
* [Request access to Dynatrace MCP Server](/docs/whats-new/preview-releases#mcp-server "Learn about our Preview releases and how you can participate in them.").
* [Create a Dynatrace platform token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") with the proper permissions to both access the MCP server and to query various event types.

## Kiro CLI-based triaging

In this scenario, an SRE interacts with Kiro CLI to perform validation and remediation actions with the help of Dynatrace MCP.

### How it works (Kiro CLI-based triaging)

![Kiro CLI-based triaging](https://dt-cdn.net/images/dd7782f2-aaa7-47db-a2ba-be0d9701e734-1920-c3a5adeea6.png)

1. Detection

AWS Security Hub identifies cloud misconfigurations.

2. Verification

* An SRE interacts with the Kiro CLI to extract top findings.
* The Dynatrace agent, invoked by the Kiro CLI, utilizes the Dynatrace MCP server to verify whether these findings impact production applications.

3. Remediation

* SRE remediates confirmed findings via Kiro CLI; others are suppressed.
* Findings are resolved and verified in AWS Security Hub.

### Get started (Kiro CLI-based triaging)

To get started, follow the steps below.

1. Download the [`dynatrace-security-agent.json` fileï»¿](https://dt-url.net/ov0301d) and place it in `.kiro/agents/`. It contains the Dynatrace MCP configuration with the proper Dynatrace API Platform Token, and the reference to an instructions file.
   Make sure to replace:

   * `<DYNATRACE_TENANT>` with your environment, for example `mytenant.apps.dynatrace.com`.
   * `<DYNATRACE_PLATFORM_TOKEN>` with the Dynatrace token generated in [prerequisites](#dt).
2. Download the [`instructions.md` fileï»¿](https://dt-url.net/cp2300s) and place it in the same `.kiro/agents/` directory, next to the agent configuration file.

## Dynatrace-driven triaging

In this scenario, initial validation and triage are automated in Dynatrace Workflows, and the SRE then acts on the Jira tickets to perform assisted remediation using the Kiro CLI.

### How it works (Dynatrace-driven triaging)

![Dynatrace-driven triaging](https://dt-cdn.net/images/kiro-cli-2-2088-7ca80c5d12.png)

1. Detection

AWS Security Hub identifies cloud misconfigurations.

2. Verification

* AWS Security Hub integration ingests findings into Dynatrace.
* A Dynatrace workflow analyzes new critical/high-risk findings and performs the automated verification using the Dynatrace Intelligence generative AI workflow action.

3. Remediation

* A Jira ticket is created automatically with the summary of the verification results.
* An SRE uses Kiro CLI to act on the Jira findings. Confirmed findings are remediated, while the unconfirmed findings can be suppressed.
* Findings are resolved in AWS Security Hub and are no longer in the top findings dashboard in Dynatrace.

### Get started (Dynatrace-driven triaging)

To get started, follow the steps below.

1. Download the [`dynatrace-security-agent.json` fileï»¿](https://dt-url.net/ov0301d) and place it in `.kiro/agents/`. It contains the Dynatrace MCP configuration with the proper Dynatrace API Platform Token, and the reference to an instructions file.
   Make sure to replace:

   * `<DYNATRACE_TENANT>` with your environment, for example `mytenant.apps.dynatrace.com`.
   * `<DYNATRACE_PLATFORM_TOKEN>` with the Dynatrace token generated in [prerequisites](#dt).
2. Download the [`instructions.md` fileï»¿](https://dt-url.net/cp2300s) and place it in the same `.kiro/agents/` directory, next to the agent configuration file.
3. Optional Configure the Jira remote MCP as part of the Dynatrace agent or as a global Kiro setting (`.kiro/settings/mcp.json`). For details, see [Model context protocol (MCP)ï»¿](https://kiro.dev/docs/cli/mcp/).
4. Deploy the [Dynatrace triaging workflow for AWS Security Hub findingsï»¿](https://dt-url.net/a9032pe).

* Edit the configuration to set the desired values for Jira parameters (such as project key, issue type, assignee, reporter, and labels), which will be used by the Jira ticket creation action.
* Schedule the workflow to run periodically.


---


## Source: analyze-aws-api-gateway-access-logs-with-security-investigator.md


---
title: Analyze Amazon API Gateway access logs with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator
scraped: 2026-02-16T09:27:21.832273
---

# Analyze Amazon API Gateway access logs with Investigations

# Analyze Amazon API Gateway access logs with Investigations

* Latest Dynatrace
* Tutorial
* Published Jan 29, 2025

[Amazon API Gatewayï»¿](https://dt-url.net/dm03wn5) is a powerful service that enables you to build serverless web APIs using Lambda functions or to add "bolt-on security" for existing services. It can range from straightforward actions such as [applying TLS encryptionï»¿](https://dt-url.net/q823w6q) or [cachingï»¿](https://dt-url.net/bj43w6c) to more advanced measures such as [Access controlï»¿](https://dt-url.net/iq63wsn), [API throttlingï»¿](https://dt-url.net/km83wry), or [security loggingï»¿](https://dt-url.net/vqa3w97). API Gateway provides an extra layer of security that can be applied to your services quickly without modifying your underlying code.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you monitor and identify errors in your Amazon API Gateway access logs.

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in maintaining and securing cloud applications in AWS. It shows you how to make the most of the Amazon API Gateway logs ingested to Dynatrace to detect security issues.

## Prerequisites

* Create an [Amazon CloudWatch log groupï»¿](https://dt-url.net/r8c3wk1) for the Amazon API Gateway access logs
* [Set up Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.") for the log group to send the logs to Dynatrace
* Knowledge of

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

## Before you begin

Enable logging and ensure that the logs are saved to the CloudWatch log group (in this example, `/aws/apigateway/my-gateway-demo`) and sent to your Dynatrace environment.

1. Enable Amazon API Gateway logging

1. In AWS, go to the **API Gateway** service page.
2. Select your **API Gateway API** from the API list.

   In this example, an HTTP API has been used (API Gateway supports multiple API types and logging configurations are different for each of them).
3. In the sidebar menu, select **Monitor** > **Logging**.
4. Select **Choose a stage** to configure logging, then select **Edit**.
5. Turn on **Access logging**.
6. For **Log destination**, enter the ARN of the `/aws/apigateway/my-gateway-demo` log group.
7. For **Log format**, select `JSON` to simplify log record parsing.
8. In **Additional fields**, customize the log format, then select **Save**.

   For a list of available fields, see [Customize HTTP API access logsï»¿](https://dt-url.net/hk03wez).

   This example uses the following log format:

   ```
   {



   "requestId": "$context.requestId",



   "ip": "$context.identity.sourceIp",



   "requestTime": "$context.requestTime",



   "httpMethod": "$context.httpMethod",



   "routeKey": "$context.routeKey",



   "path": "$context.path",



   "status": "$context.status",



   "protocol": "$context.protocol",



   "responseLength": "$context.responseLength",



   "responseLatency": "$context.responseLatency",



   "integrationLatency": "$context.integrationLatency",



   "integrationStatus": "$context.integrationStatus",



   "errorMessage": "$context.error.message",



   "integrationErrorMessage": "$context.integrationErrorMessage"



   }
   ```

2. Verify that the API Gateway requests are logged

1. In Dynatrace, open ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** and select  **Investigation** to create a new investigation scenario.
2. To verify that the logs from the Amazon CloudWatch log group are reaching your Dynatrace environment, run the following query:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```

   Example result:

   ![fetch logs](https://dt-cdn.net/images/2025-01-27-11-45-07-1546-309fa661f3.png)

   If no logs are displayed, check your CloudWatch subscription filter and Data Firehose settings (including performance metrics, tenant and buffer settings).

## Get started

Analyze your Amazon API Gateway logs with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

1. Discover backend issues using latency metrics

1. How to decide which metrics to use

API Gateway logs contain a lot of helpful information that can be used to debug your backend applications. One standard metric to monitor from an API Gateway is latency. Two types of latencies can be monitored from API Gateway logs:

* **Integration latency**: The time between when API Gateway relays a request to the backend and when it receives a response from the backend.
* **Response latency**: The time between when API Gateway receives a request from a client and when it returns a response to the client. It includes the integration latency and other API Gateway overhead.

Deciding which metric to use for performance monitoring depends on your use case. Since this example focuses on the backend performance, not the whole request cycle, the integration latency will be used.

Follow the steps below to analyze and discover the services with the highest latency.

1. Fetch your API Gateway logs from Grail:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```
2. In the query results table, right-click on a field and select **View field details** to [view the log record in the original format](/docs/secure/investigations/enhance-results#view-details "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

   Example JSON-formatted log record:

   ```
   {



   "requestId": "Dzfa6gNrrks42Tw=",



   "ip": "14.21.74.45",



   "requestTime": "03/Jan/2025:09:22:13 +0000",



   "httpMethod": "GET",



   "routeKey": "ANY /",



   "path": "/getStuff",



   "status": "200",



   "protocol": "HTTP/1.1",



   "responseLength": "33",



   "responseLatency": "1671",



   "integrationLatency": "1665",



   "integrationStatus": "200",



   "errorMessage": "-",



   "integrationErrorMessage": "-"



   }
   ```
3. Add the following [parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands") to the DQL query to extract the `path` and `integrationLatency` properties from the JSON record.

   ```
   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"
   ```

   This example uses [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") and the [JSON matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.") to extract [selected matchers](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object#parse-selected "Explore DPL syntax for handling JSON Objects.") to separate fields.

   DPL pattern used:

   ```
   JSON{



   STRING:path,



   INT:integrationLatency



   }(flat=true)
   ```

   After running the query, you can see two new columns called **path** and **integrationLatency** in the results table.
4. To simplify viewing the results, add the following [`makeTimeseries` command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to the DQL query to create a metric from the API Gateway logs. The metric should have the path as a dimension and average latency per minute as the metric values.

   ```
   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   },



   by: { path },



   interval:1m
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"



   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   }, by: { path }, interval:1m
   ```

   Example result viewed as a chart:

   ![chart1](https://dt-cdn.net/images/2025-01-27-15-02-11-1530-a85e8ff3a0.png)

   It turns out you're experiencing some periodical latency issues for both service endpoints.

2. Identify latency issues and troubleshoot response codes

Follow the steps below to dig deeper into the response codes.

1. Extract the response codes as an additional column with an [INT matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-numeric#int "Explore DPL syntax for handling numeric data."), as you're expecting to get an integer value from the field.

   DPL pattern used:

   ```
   JSON{ STRING:path, INT:status, INT:integrationLatency }(flat=true)
   ```

   You can see that the response code is called `status`.
2. To add the status as one of the dimensions for your metric, add the `status` field to the `by` parameter of your `maketimeseries` command.

   ```
   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   },



   by: { path, status },



   interval:1m
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status INT:integrationLatency }(flat=true)"



   | makeTimeseries {



   latency = avg(integrationLatency, default:0)



   }, by: { path, status }, interval:1m
   ```

   Example result viewed as a chart:

   ![chart 2](https://dt-cdn.net/images/2025-01-27-15-07-19-1529-0f585fe086.png)

   It turns out that no successful responses are returned: requests take longer, and all responses return a "Server Error" (HTTP/500).

3. Debug integration errors

Follow the steps below to continue debugging integration errors.

1. To analyze the error messages, extract an additional **integrationErrorMessage** field from the log record with a string matcher.

   DPL pattern used:

   ```
   JSON{



   STRING:path,



   INT:status,



   INT:integrationLatency,



   STRING:integrationErrorMessage



   }(flat=true)
   ```
2. Add the following snippet to the DQL query to aggregate the error messages and sort them by count:

   ```
   | summarize count(), by: { integrationErrorMessage }



   | sort `count()` desc
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



   | summarize count(), by: { integrationErrorMessage }



   | sort `count()` desc
   ```

   A distinct timeout error message stands out from results: `The Lambda function returned the following error: RequestId: 01fe3839-4974-40d5-960a-173fcb5ec786 Error: Task timed out after 5.00 seconds. Check your Lambda function code and try again.`
3. Extract the `Error` portion from the log record without the request ID to compare this error message with the others.

   DPL pattern used:

   ```
   LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error
   ```

   You now have two fields (**error** and **integrationErrorMessage**) that can contain the error message.
4. Add the following snippet to the DQL query to merge the two fields into one column with the `if` function and summarize based on that.

   ```
   | fields error = if(isnull(error), integrationErrorMessage, else: error)



   | summarize count(), by: { error }
   ```

   Your DQL query should look like this:

   ```
   fetch logs



   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



   | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"



   | fields error = if(isnull(error), integrationErrorMessage, else: error)



   | summarize count(), by: { error }
   ```

   Example results:

   ![results](https://dt-cdn.net/images/2025-01-27-15-55-59-1538-7994d7382c.png)

   It turns out that timeout errors are the most frequent.
5. To see how the error messages distribute over the same period, create a metric based on the timeout errors as follows:

* Add a [`filterOut` command](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filterOut "DQL filter and search commands") to remove the successful events
* Add the `timestamp` field to the [`fields` command](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands#fields "DQL selection and modification commands")
* Construct the `makeTimeseries` command to aggregate errors by count in one-minute interval.

  Your final query should look like this:

  ```
  fetch logs



  | filter aws.log_group == "/aws/apigateway/my-gateway-demo"



  | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"



  | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"



  | fields timestamp, error = if(isnull(error), integrationErrorMessage, else: error)



  | filterOut error == "-"



  | makeTimeseries count(default: 0), by: { error }, interval: 1m
  ```

  Example result viewed as a chart:

  ![chart 3](https://dt-cdn.net/images/2025-01-27-15-50-54-1509-00bad2a7dc.png)

  It turns out you're experiencing Lambda timeout problems, which are creating latency and server error issues in your API Gateway logs.

  To investigate this further, you'd have to look into the Lambda function and see why you're experiencing this behavior precisely at those times. It can be that certain scheduled jobs are running, resources are locked or overloaded, or some other dependencies are causing these issues.

## Related topics

* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")


---


## Source: analyze-aws-cloudtrail-logs-with-security-investigator.md


---
title: Analyze AWS CloudTrail logs with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator
scraped: 2026-02-16T09:29:14.631559
---

# Analyze AWS CloudTrail logs with Investigations

# Analyze AWS CloudTrail logs with Investigations

* Latest Dynatrace
* Tutorial
* Published Nov 26, 2024

[AWS CloudTrailï»¿](https://dt-url.net/ax63uwp) is an AWS service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service in an Amazon AWS environment are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you

* [Monitor sign-in failures to AWS console](#sign-in)
* [Create metrics for unauthorized API calls](#metrics)
* [Monitor AWS API throttling](#monitor)
* [Detect externally generated keys in AWS KMS](#keys)

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in maintaining and securing cloud applications in AWS.

## Prerequisites

* Store your CloudTrail logs to an S3 bucket or [CloudWatchï»¿](https://dt-url.net/mr03u6p).
* Send CloudTrail logs to Dynatrace. There are two options to stream logs:

  + [Amazon S3ï»¿](https://dt-url.net/c703wc8) Recommended
  + [Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Knowledge of

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

## Before you begin

Follow the steps below to fetch the AWS CloudTrail logs from Grail using ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** and prepare them for analysis.

1. Fetch AWS CloudTrail logs from Grail

Once your CloudTrail logs are ingested into Dynatrace, follow these steps to fetch the logs.

1. Open [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation** to create an investigation scenario.
3. In the query input section, insert the DQL query below.

   ```
   fetch logs, from: -30min



   | filter aws.service == "cloudtrail"
   ```
4. Select ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") **Run** to display results.

   The query will search for logs from the last 30 minutes, which have been forwarded from an AWS log group that contains the word `cloudtrail`.

   If you know in which Grail bucket the CloudTrail logs are stored, use filters to specify the bucket to improve the query performance.

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"
   ```

   For details, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

   The results table will be populated with the JSON-formatted events.
5. Right-click on an event and select **View field details** to see the JSON-formatted event in a structured way. This enables investigators to grasp the content of the event much faster.

   ![results table](https://dt-cdn.net/images/image-20241109-145818-3100-3e65568b52.png)
6. Navigate between events in the results table via the keyboard arrow keys or the navigation buttons in the upper part of the **View field details** window.

   ![field details](https://dt-cdn.net/images/image-20241106-153049-1-2040-9f9e875bf6.png)

2. Prepare the data for analysis

Follow the steps below to simplify log analysis, speed up investigations, and maintain the required precision for analytical tasks.

1. Add to your DQL query the [parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands") to extract the required data from the log records into separate fields.
2. Add the [JSON matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.") to extract the JSON-formatted log content as a JSON object into a separate field called `event`.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"
   ```
3. Double-click on any record in the results table to view the object in the **Record details** view. Expand the JSON elements to navigate through the object faster and add filters based on its content.

   ![Record details](https://dt-cdn.net/images/image-20241106-155245-1-2288-9851882d34.png)

## Get started

The following are use cases demonstrating how to build the above query to analyze AWS CloudTrail logs with Dynatrace.

1. Monitor sign-in failures to AWS console

Failures in authentication logs can be an indication for a potential attack towards your infrastructure. A malicious user could try to enumerate usernames or passwords to gain access to your AWS environment and take control of your business.

To monitor sign-in failures to the AWS console using CloudTrail logs

1. Add a filter statement to fetch only results with `signin.amazonaws.com` as the event source and `ConsoleLogin` as the event name.
2. Add a filter command for the `responseElements.ConsoleLogin` sub-element in the JSON object with the value `Failure` to see only failed login attempts.

   You can use the DQL snippet below.

   ```
   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName] == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"
   ```
3. Add the `summarize` command with your chosen fields to have an aggregated overview of the events.

   You can use the DQL snippet below.

   ```
   | summarize event_count = count(), by: {



   source  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

   Your final DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"



   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName]   == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"



   | summarize count(), by: {



   ipAddr  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

2. Create metrics for unauthorized API calls

Unauthorized API calls can indicate a hacking attempt or a system malfunction. These kinds of anomalies should be investigated to prevent unexpected costs or system takeovers by malicious users.

To identify the "top targets" from the API list

1. Create a filter to fetch only events, with an `AccessDenied` or `UnauthorizedOperation` error code.
2. Add the [makeTimeseries command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to convert your log results to metrics.
3. Add the `event[eventName]` value from the logs as a metrics dimension.
4. Sort the results to see only the top 10 APIs and limit the results to 10 records.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter in(event[errorCode], { "AccessDenied", "UnauthorizedOperation" })



   | makeTimeseries event_count = count(), by: { eventName = event[eventName] }



   | sort arrayAvg(event_count) desc



   | limit 10
   ```

   For more granularity, you can add more dimensions to the `makeTimeseries` command.

   For example, to see API call charts based on the user and the API endpoint, the summarization command would be as follows.

   ```
   | makeTimeseries count(), by: {



   user      = event[userIdentity][arn],



   eventName = event[eventName]



   }
   ```

   Example results visualized as a line chart:

   ![ results visualized to a line-chart ](https://dt-cdn.net/images/image-20241108-135013-2334-7d17f90671.png)

3. Monitor AWS API throttling

Monitoring request counts towards APIs is important from the availability, cost, and security perspectives. A throttling API might indicate either a brute-force attack, a denial-of-service attack, or an ongoing data exfiltration by a malicious actor.

To monitor AWS API throttling from AWS CloudTrail logs in Dynatrace

1. Create a filter to fetch only events with an error code `Client.RequestLimitExceeded`.
2. Add the [makeTimeseries command](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") to convert your log results to metrics.
3. Add the `event[eventName]` value from the logs as a metrics dimension.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[errorCode] == "Client.RequestLimitExceeded"



   | makeTimeseries count(), by: { eventName = event[eventName] }
   ```

4. Detect externally generated keys in AWS KMS

When creating a new key in [AWS Key Management Service (KMS)ï»¿](https://dt-url.net/4g23uoc), you can choose the key material origin for the key: whether the keys are kept under AWS control or handled externally.

By default, key origin material is `AWS_KMS`, which means that KMS creates the key material.

When keys are handled externally, thereâs an increased risk that the keys might leak, thus endangering the data which is protected with the key: the key could leak from elsewhere and its location could be unknown.

To detect such key creations, where external key material was used

1. Create a filter to fetch only events with the name `CreateKey`.
2. Add a statement to the filter to exclude all origins that begin with `AWS_`.

   Currently there are two options (`AWS_KMS` and `EXTERNAL`) so you could filter by `External` origin, but having the filtering out could be be more future-proof.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "CreateKey"



   | filterOut startsWith(event[requestParameters][origin], "AWS_")



   | fields {



   eventName = event[eventName],



   origin    = event[requestParameters][origin],



   keyUsage  = event[responseElements][keyMetadata][keyUsage],



   region    = event[awsRegion],



   userARN   = event[userIdentity][arn],



   keyId     = event[responseElements][keyMetadata][keyId]



   }
   ```

As a result, you get a table that contains the following information:

* **eventName**: CreateKey
* **origin**: EXTERNAL
* **keyUsage**: ENCRYPT\_DECRYPT
* **region**: us-east-1
* **userARN**: username
* **keyId**: 123acb

## Summary

These are some of the use cases that can be solved using CloudTrail logs and Dynatrace ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**. These logs are an endless source of information that enables Security and DevOps Engineers to conduct different investigations on their AWS infrastructure.

## Related topics

* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")


---


## Source: automate-and-orchestrate-security-findings.md


---
title: Automate and orchestrate security findings
source: https://www.dynatrace.com/docs/secure/use-cases/automate-and-orchestrate-security-findings
scraped: 2026-02-17T05:05:58.835235
---

# Automate and orchestrate security findings

# Automate and orchestrate security findings

* Latest Dynatrace
* Tutorial
* Published Aug 30, 2024

Prioritization and remediation of security findings require a lot of manual effort. With so many different security tools, efficiently orchestrating the findings and focusing on the critical ones becomes impossible.

While siloed products can provide localized automation, they often generate excessive noise. This means dev teams ultimately ignore alerts and tickets, and the security posture degrades.

In this context, you can

* [Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from various tools and map them to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).
* Automate and orchestrate security findings across products and tools with our workflow automation samples, which you can further customize with the robust [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") capabilities for your organization's orchestration processes.

## Target audience

Security architects and managers who aim to streamline remediation processes and direct the development teamsâ efforts towards effective remediation.

Key use cases include:

* Ticket creation for remediation of the discovered critical issues
* Notification of the relevant stakeholders on the critical findings
* Email reporting on the top findings

## Prerequisites

[Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from your third-party product.

## Get started

1. Download our [sample workflow from GitHubï»¿](https://dt-url.net/l403xh0).

   * For vulnerability findings, download these sample workflows instead:

     + [Slack workflow sampleï»¿](https://dt-url.net/ko43qsm)
     + [Jira workflow sampleï»¿](https://dt-url.net/od23qa1)
   * For container vulnerability findings, download these sample workflows instead:

     + [Slack workflow sampleï»¿](https://dt-url.net/a643qqd)
     + [Jira workflow sampleï»¿](https://dt-url.net/l103p3t)

   For some integrations, such as [Amazon ECR](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.") or [AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace."), workflow samples are available in the app in the **Try our templates** section (go to **Settings (new)** > **Connections** and select the app).
2. Open [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.

Example result:

![email notification example](https://dt-cdn.net/images/image-54-1103-3883848f65.png)


---


## Source: automated-threat-alert-triaging.md


---
title: Automated threat-alert triaging
source: https://www.dynatrace.com/docs/secure/use-cases/automated-threat-alert-triaging
scraped: 2026-02-17T05:08:40.300182
---

# Automated threat-alert triaging

# Automated threat-alert triaging

* Latest Dynatrace
* Tutorial
* Updated on Jun 26, 2025

Security teams face the challenge of sifting through massive amounts of security data to identify and respond to potential threats, prioritize alerts, and assess the severity of events. Lacking context in place, analysts spend valuable time sorting through the noise, switching between tools, and risking overlooking important information, which leads to delayed responses and inefficiencies in security operations.

The Dynatrace platform addresses this issue by providing security contextualization capabilities, such as threat intelligence enrichment. Various security findings in the Dynatrace platform contain observables, such as IP addresses. Those observables can now be enriched with reputation and other threat contexts, enabling you to

* Classify and prioritize alerts
* Reduce the noise
* Respond to threat alerts fast

## Target audience

This article is intended for incident response teams that want to automate the triage of new detections supported by threat intelligence.

## Scenario

* A new security detection finding from [Amazon GuardDutyï»¿](https://aws.amazon.com/guardduty/) is ingested into the Dynatrace platform.
* The security team wants to be notified in Slack only about new critical detections from an actor whose IP address is classified as malicious by the [AbuseIPDBï»¿](https://www.abuseipdb.com/) threat intelligence source.

The same scenario can be applied to other supported integrations for enrichment and security data ingest.

## Prerequisites

* [Install and configure Amazon GuardDuty integration](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.") (or any other [supported data ingest integration](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")).
* [Install and configure the AbuseIPDB enrichment](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.") (or any other [supported enrichment integration](/docs/secure/threat-observability/security-events-ingest#enrich "Ingest external security data into Grail.")).
* Users must have the `security-intelligence:enrichments:run` permission to run enrichments.

## Get started

1. Import workflow

Import the sample workflow available as a template in the **AbuseIPDB** app.

1. In Dynatrace, open **Settings** > **AbuseIPDB**.
2. In **Templates**, select and import the sample workflow.

2. Enable enrichment

To run the enrichment workflow action, you need to enable the `security-intelligence:enrichments:run` permission.

1. Go to the settings menu  in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.
2. In **Secondary permissions**, search for and select the `security-intelligence:enrichments:run` permission.
3. Select **Save**.

3. Customize workflow

Customize the DQL query action or the Slack notification message to your needs.

![customize workflow](https://dt-cdn.net/images/image-20250602-114203-2544-00ee8d9d9a.png)

4. Test workflow

Run the workflow to test it.

Example notification:

![test workflow](https://dt-cdn.net/images/image-20250602-115603-977-1c24ffce39.png)

5. Save workflow

Schedule and save the workflow to be triggered automatically.


---


## Source: detect-threats-against-aws-secrets-with-security-investigator.md


---
title: Detect threats against your AWS Secrets with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator
scraped: 2026-02-17T05:05:05.016229
---

# Detect threats against your AWS Secrets with Investigations

# Detect threats against your AWS Secrets with Investigations

* Latest Dynatrace
* Tutorial
* Published Nov 26, 2024

In today's digital landscape, protecting your cryptographic secrets in a cloud environment is more critical than ever. Secrets such as API keys, passwords, and encryption keys used in your applications are vital parts of your applications that, when leaked, could jeopardize your whole business. That's why analyzing threats against secrets is essential to ensure your data's integrity, confidentiality, and availability.

In the following, you'll learn how [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") can help you

* [Detect externally generated keys in AWS KMS](#keys)
* [Detect unprivileged requests trying to read Secrets](#requests)
* [Detect requesting non-existing secrets](#secrets)

## Target audience

This article is intended for security engineers and site reliability engineers who are involved in the maintenance and security of cloud applications in AWS.

## Prerequisites

* Store your CloudTrail logs to an S3 bucket or [CloudWatchï»¿](https://dt-url.net/mr03u6p).
* Send CloudTrail logs to Dynatrace. There are two options to stream logs:

  + [Amazon S3ï»¿](https://dt-url.net/c703wc8) Recommended
  + [Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Knowledge of

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

## Before you begin

Follow the steps below to fetch the AWS CloudTrail logs from Grail using ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** and prepare them for analysis.

1. Fetch AWS CloudTrail logs from Grail

Once your CloudTrail logs are ingested into Dynatrace, follow these steps to fetch the logs.

1. Open [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation** to create an investigation scenario.
3. In the query input section, insert the DQL query below.

   ```
   fetch logs, from: -30min



   | filter aws.service == "cloudtrail"
   ```
4. Select ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") **Run** to display results.

   The query will search for logs from the last 30 minutes, which have been forwarded from an AWS log group that contains the word `cloudtrail`.

   If you know in which Grail bucket the CloudTrail logs are stored, use filters to specify the bucket to improve the query performance.

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"
   ```

   For details, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

   The results table will be populated with the JSON-formatted events.
5. Right-click on an event and select **View field details** to see the JSON-formatted event in a structured way. This enables investigators to grasp the content of the event much faster.

   ![results table](https://dt-cdn.net/images/image-20241109-145818-3100-3e65568b52.png)
6. Navigate between events in the results table via the keyboard arrow keys or the navigation buttons in the upper part of the **View field details** window.

   ![field details](https://dt-cdn.net/images/image-20241106-153049-1-2040-9f9e875bf6.png)

2. Prepare the data for analysis

Follow the steps below to simplify log analysis, speed up investigations, and maintain the required precision for analytical tasks.

1. Add to your DQL query the [parse command](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "DQL extraction commands") to extract the required data from the log records into separate fields.
2. Add the [JSON matcher](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Explore DPL syntax for handling JSON Objects.") to extract the JSON-formatted log content as a JSON object into a separate field called `event`.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"
   ```
3. Double-click on any record in the results table to view the object in the **Record details** view. Expand the JSON elements to navigate through the object faster and add filters based on its content.

   ![Record details](https://dt-cdn.net/images/image-20241106-155245-1-2288-9851882d34.png)

## Get started

The following are use cases demonstrating how to build the above query to analyze AWS Secrets with Dynatrace.

1. Detect externally generated keys in AWS KMS

When creating a new key in [AWS Key Management Service (KMS)ï»¿](https://dt-url.net/4g23uoc), you can choose the key material origin for the key: whether the keys are kept under AWS control or handled externally.

By default, key origin material is `AWS_KMS`, which means that KMS creates the key material.

When keys are handled externally, thereâs an increased risk that the keys might leak, thus endangering the data that is protected with the key: the key could leak from elsewhere and its location could be unknown.

To detect key creations where external key material was used

1. Create a filter to fetch only events with the name `CreateKey`.
2. Add a statement to the filter to exclude all origins that begin with `AWS_`.

   Currently, there are two options (`AWS_KMS` and `EXTERNAL`), so you could filter by `External` origin, but having the filtering out could be be more future-proof.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "CreateKey"



   | filterOut startsWith(event[requestParameters][origin], "AWS_")



   | fields {



   eventName = event[eventName],



   origin    = event[requestParameters][origin],



   keyUsage  = event[responseElements][keyMetadata][keyUsage],



   region    = event[awsRegion],



   userARN   = event[userIdentity][arn],



   keyId     = event[responseElements][keyMetadata][keyId]



   }
   ```

As a result, you get a table that contains the following information:

* **eventName**: CreateKey
* **origin**: EXTERNAL
* **keyUsage**: ENCRYPT\_DECRYPT
* **region**: us-east-1
* **userARN**: username
* **keyId**: 123acb

2. Detect unprivileged requests trying to read Secrets

Unauthorized requests to read secrets is an indication of either a hacking attempt or a system misconfiguration. Unauthorized requests might mean that an attacker has compromised credentials from your system and is now trying to extract Secrets from your AWS account (but luckily without success).

In this use-case, we go through two scenarios that target different unprivileged access attempts to your secrets: [requesting secrets without KMS privileges](#no-kms-privilege) and [requesting unauthorized secrets](#unauthorized-secret).

#### Requests without KMS privileges

In case of missing KMS privileges, you can assume these accounts were not supposed to access any secrets in your environments. If this still happens, this is (either malicious or accidental) credential misuse or misconfiguration. Either way, this requires your attention.

To see if someone is trying to access such events in your CloudTrail logs

1. Create a filter to fetch only `GetSecretValue` events and with an `AccessDenied` error code.
2. Add a new filtering condition to see only errors with an `Access to KMS is not allowed` message.
3. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `ARN` of the user of the unauthorized attempts.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   and event[errorMessage] == "Access to KMS is not allowed"



   | summarize event_count = count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn]



   }
   ```

If your query returns any results, they would look like this:

| **sourceIPAddress** | **region** | **arn** | **event\_count** |
| --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 3 |

#### Unauthorized Secret requests

In this case, the account is trying to load privileges to which it doesnât have access. The secret configuration might be incorrect, or the account might be being used for secrets it wasnât meant to be used for. The last possibility introduces a potential security threat if the intent is malicious.

To see if such events occur in your CloudTrail logs

1. Create a filter to fetch only `GetSecretValue` events and with an `AccessDenied` error code.
2. If the requested secret doesn't exist or the user doesn't have access to it, the secret's ARN is mentioned in the error message. Parse out the `secretID` from the error message.
3. Show only the events where `secretID` is present.
4. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `userARN` of the user of the unauthorized attempts.

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   | parse event[errorMessage], "LD ':secret:' STRING:secretId"



   | filter isNotNull(secretId)



   | summarize count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn],



   secretId



   }
   ```

If your query returns any results, they would look like this:

| **sourceIPAddress** | **awsRegion** | **arn** | **secretId** | **event\_count** |
| --- | --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 123abc | 3 |

3. Detect requesting non-existing secrets

Requesting secrets that don't exist might indicate a security issue (for example, when someone is trying to enumerate your secrets to extract them and tries all kinds of secrets that might not exist) or an operational issue (secrets used by the service are no longer available, thus creating service issues).

To see if such events are present in your CloudTrail logs

1. Create a filter to fetch the `GetSecretValue` events.
2. Append the filter conditions to fetch only events with a `ResourceNotFoundException` error message.
3. Aggregate the results by `sourceIPAddress`, `awsRegion`, and the `userARN` and collect the number of events and distinct secrets fetched by this user in the respective AWS region from the specific IP address.

   If you see a large number of distinct secrets being fetched from a single `userARN`, it might be a secret enumeration. If the number of different secrets is low, something has probably happened to the secret (a wrong set of privileges, the secret has been removed, or similar).

   Your DQL query should look like this:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "ResourceNotFoundException"



   | summarize {



   event_count = count(),



   distinct_secrets = countDistinct(event[requestParameters][secretId])



   }, by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN   = event[userIdentity][arn]



   }



   | sort distinct_secrets desc
   ```

## Related topics

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")


---


## Source: detect-threats-cloud-native-workflows.md


---
title: Detect threats in cloud-native environments using workflows
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-cloud-native-workflows
scraped: 2026-02-17T05:08:09.825265
---

# Detect threats in cloud-native environments using workflows

# Detect threats in cloud-native environments using workflows

* Latest Dynatrace
* Tutorial
* Updated on Sep 10, 2025

In this tutorial, you'll learn how to

* Continuously detect and respond to active threats within your cloud-native environment
* Find attackers trying to exploit your applications before they can negatively affect your business
* Easily and flexibly search through huge amounts of data to find signs of suspicious behavior

## Target audience

This article is intended for

* DevOps, CloudOps, and SREs responsible for protecting workloads
* Security analysts responsible for cloud-native environments

## Prerequisites

* Set up ingestion of Kubernetes audit logs, for example, through [Amazon Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput."). Firehose can be used to ship logs from Amazon Elastic Kubernetes Service (EKS), but the provided template is compatible with any Kubernetes distribution.
* Generate an access token with the `openpipeline.events_security` scope to allow us to ingest detection findings. To later access the token securely from within a workflow, store the token in the [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault."). For details, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Get started

After setting up log ingestion, you can start detecting threats.

1. Set up scheduled DQL queries

Use ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** to execute DQL queries regularly and look for suspicious behavior in your data.

1. Import our [workflow templateï»¿](https://dt-url.net/s9030m9).
2. For the **execute\_query** step, adapt the DQL query to your needs.

   The template query aims to find possibly compromised service accounts within our Kubernetes cluster.

   * You can tune it, adjust its logic or modify it completely to detect other potential threats.
   * You can find additional examples in the [Dynatrace blogï»¿](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/).
3. For the **ingest\_findings** step, go to **Input** > **Authentication** and select the token previously stored in the credential vault.

2. Test the workflow

To trigger a detection finding based on the query provided, execute the following commands in a Dynatrace-monitored Kubernetes cluster:

1. Create a test service account:

   ```
   kubectl create serviceaccount test-sa -n default
   ```
2. Attempt unauthorized access (should trigger detection):

   ```
   kubectl --as=system:serviceaccount:default:test-sa get secret -A
   ```

3. Tune detection

You can define exceptions to the rule by adding allowlisting criteria to the **apply\_allowlist** step in the workflow.

A detection finding event will not be created if all attributes of an entry match those of any single allowlisted entry.

* Attribute comparison follows `AND` logic within an entry.
* Allowlist evaluation uses `OR` logic across entries.

4. Triage and investigate

Use [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.") to examine and prioritize the detection findings created. The rich observability context provided in the detection finding enables fast analysis and confident assessment of the situation.

**Sample result**

![sample result in threats and exploits app](https://dt-cdn.net/images/image-58-1667-0a98717d9c.png)

## Sample workflows for threat response

Dynatrace provides ready-to-use workflow templates that automatically trigger on new Kubernetes threat detection findings and send notifications via [Slack](/docs/analyze-explore-automate/workflows/actions/slack#workflow "Send messages to Slack Workspaces"), [Microsoft Teams](/docs/analyze-explore-automate/workflows/actions/microsoft-teams#use "Send messages to Microsoft Teams"), or [Email](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
Use these as starting points to build your own automated response workflows:

* [Instant notification for critical Kubernetes detection findingsï»¿](https://dt-url.net/l9430ds): Triggers on high or critical findings and alerts the responsible team.
* [Threat detection notification senderï»¿](https://dt-url.net/hs2301e): A reusable sub-workflow for centralized notification delivery.

These templates show how to enrich findings with [ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") context and integrate real-time alerting into your response workflows.

## Conclusion

Workflows enable precise threat detection and response aligned with your environmentâs context. Features like flexible scheduling, DQL-based filtering, allowlisting, ownership tagging, and notification integration allow for rapid, low-noise detection. The included blueprint offers a modular starting point that can be fine-tuned or extended to meet specific operational needs.


---


## Source: discover-coverage-gaps-in-security-scans.md


---
title: Discover coverage gaps in security findings
source: https://www.dynatrace.com/docs/secure/use-cases/discover-coverage-gaps-in-security-scans
scraped: 2026-02-17T05:02:03.008320
---

# Discover coverage gaps in security findings

# Discover coverage gaps in security findings

* Latest Dynatrace
* Tutorial
* Updated on Sep 30, 2025

During the Software Development Lifecycle (SDLC), multiple tools scan various artifacts as they progress through the development stages. An artifact like a container image reaches the deployment stage and eventually represents your running applications. At this point, you want to be sure the artifacts went through the proper security scanning procedures and didn't skip any essential validation.

Gaining complete visibility of the validation cycle isn't easy, as the scanning products used by different teams silo.

In this context, you can

* Aggregate the security scans for the deployed and running artifacts.
* Gain complete visibility into the security validations those artifacts went through before reaching your production environment.
* Discover gaps in your security procedures and remediate them before they become a real risk.
* Visualize security findings across the products and tools with our dashboard samples, which can also be a good foundation for tailoring further visual customization to meet your organization's posture analysis and reporting requirements.

## Target audience

Security architects and managers responsible for keeping the security scan procedures aligned with the security standards.

Key use cases include:

* Gaining an overview of the performed security assessments
* Identifying coverage gaps
* Identifying top contributing products and their ROI

## Prerequisites

[Ingest security findings](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") from your third-party product.

## Get started

1. Visualize

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Security product coverage** for the desired integration.

Example result:

![dashboard sample result](https://dt-cdn.net/images/2025-05-07-13-27-38-1905-24ee0d41ed.png)

2. Analyze

Open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to [query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") security findings, using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

For a better understanding of how to build your queries, see [DQL query examples for ingested events](/docs/secure/threat-observability/dql-examples#ingested "DQL examples for security data powered by Grail.").


---


## Source: ingest-and-process-custom-security-findings.md


---
title: Ingest and process custom security findings
source: https://www.dynatrace.com/docs/secure/use-cases/ingest-and-process-custom-security-findings
scraped: 2026-02-16T21:21:57.999124
---

# Ingest and process custom security findings

# Ingest and process custom security findings

* Latest Dynatrace
* Tutorial
* Updated on Jun 17, 2025

In the following, you'll learn how to ingest and process custom security data while pushing the data from a third-party tool to Dynatrace, using the OpenPipeline ingest API for security events.

## Target audience

Security practitioners aiming to analyze, visualize, and automate custom security data with Dynatrace.

## Scenario

You're a security architect who uses Dynatrace to monitor the health of applications and services. As part of Software Development Lifecycle (SDLC) security practices, you need to ensure that developers scan container images before deploying them into production.

To achieve this, you want to

1. Ingest your container scan findings to Dynatrace continuously.
2. Connect the findings to the monitored production containers.
3. Create automatic Jira tickets to the dev-owners of the containers if there are missing security scans for the corresponding container images.

This article covers the first part: ingesting custom security findings and mapping them to Dynatrace Semantic Dictionary for security vulnerability findings.

Sample input for security findings - Trivy JSON scan report

```
{



"SchemaVersion": 2,



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



"ArtifactType": "container_image",



"Metadata": {



"OS": {



"Family": "alpine",



"Name": "3.9.4",



"EOSL": true



},



"ImageID": "sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



"DiffIDs": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



],



"ImageConfig": {



"architecture": "amd64",



"container": "c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f",



"created": "2019-05-11T00:07:03.510395965Z",



"docker_version": "18.06.1-ce",



"history": [



{



"created": "2019-05-11T00:07:03.358250803Z",



"created_by": "/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / "



},



{



"created": "2019-05-11T00:07:03.510395965Z",



"created_by": "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]",



"empty_layer": true



}



],



"os": "linux",



"rootfs": {



"type": "layers",



"diff_ids": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



]



},



"config": {



"Cmd": [



"/bin/sh"



],



"Env": [



"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"



],



"Image": "sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a",



"ArgsEscaped": true



}



}



},



"Results": [



{



"Target": "testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)",



"Class": "os-pkgs",



"Type": "alpine",



"Vulnerabilities": [



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl@1.1.20-r4",



"PkgName": "musl",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "d6abd271e71d3ce2"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



},



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl-utils@1.1.20-r4",



"PkgName": "musl-utils",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl-utils@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "8c341199f4077fc8"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



}



]



}



]



}
```

## Prerequisites

* Your [containers are deployed in Kubernetes and monitored by Dynatrace](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")
* Corresponding container images are scanned by a third-party tool (in this case, Trivy)

### Permissions

To add new sources and pipeline processing to OpenPipeline, you need both permissions below.

* `openpipeline:configurations:read`
* `openpipeline:configurations:write`

To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Get started

For instructions on ingesting any type of event, see [How to ingest data (events)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.").

1. Configure endpoint in Dynatrace

1. Open **OpenPipeline**.
2. Go to **Events** > **Security events** > **Ingest sources**.
3. You have two ingest options:

   * Recommended Option 1 - Use the builtin security events endpoint Copy the URL of the builtin security events endpoint.

     ![copy URL of builtin security events endpoint](https://dt-cdn.net/images/2024-08-28-19-48-19-1855-96c02de135.png)
   * Option 2 - Create a custom endpoint Select  **Source** to [create a custom ingest source](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#ingest "Configure ingest sources, routes, and processing for your data in OpenPipeline."), then copy its URL.

   For more information about the ingest options, see [Security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
4. Generate an [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.") with the required scope according to your ingest option selected in step 3.

   For details on the required scopes, see [Get started](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data#start "Ingest security events from custom third-party products via API.").

2. Feed data into Grail

Use the ingest endpoint URL and access token generated previously to configure the third-party product.

To work granularly later with the security findings ingested to Grail, aggregated reports should be broken into and ingested as individual findings.

In this case, we modified events before ingestion to include only a single container image, vulnerability, and vulnerable library.

Sample ingested event with a single vulnerability finding

```
{



"SchemaVersion": 2,



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



"ArtifactType": "container_image",



"Metadata": {



"OS": {



"Family": "alpine",



"Name": "3.9.4",



"EOSL": true



},



"ImageID": "sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



"DiffIDs": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



],



"ImageConfig": {



"architecture": "amd64",



"container": "c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f",



"created": "2019-05-11T00:07:03.510395965Z",



"docker_version": "18.06.1-ce",



"history": [



{



"created": "2019-05-11T00:07:03.358250803Z",



"created_by": "/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / "



},



{



"created": "2019-05-11T00:07:03.510395965Z",



"created_by": "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]",



"empty_layer": true



}



],



"os": "linux",



"rootfs": {



"type": "layers",



"diff_ids": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



]



},



"config": {



"Cmd": [



"/bin/sh"



],



"Env": [



"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"



],



"Image": "sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a",



"ArgsEscaped": true



}



}



},



"Results": [



{



"Target": "testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)",



"Class": "os-pkgs",



"Type": "alpine",



"Vulnerabilities": [



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl@1.1.20-r4",



"PkgName": "musl",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "d6abd271e71d3ce2"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



}



]



}



]



}
```

3. Validate data in Notebooks

To validate data, open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and query the security events.

Sample DQL query:

This query has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
fetch security.events



| filter dt.system.bucket == "default_securityevents"



| sort timestamp desc
```

To clearly distinguish ingested data from other ingested events, you can add filters for the attributes you expect there.

Example:

```
| filter SchemaVersion == 2 AND ArtifactType == "container_image"
```

The query result should include the ingested event in the original format with a few enriched fields, such as `timestamp` and `event.kind`.

Sample query result

```
{



// enriched fields



"timestamp": "2024-08-02T14:38:53.854000000Z",



"event.kind": "SECURITY_EVENT",



// original fields



"SchemaVersion": 2,



"Results": [



"{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\",\"Class\":\"os-pkgs\",\"Type\":\"alpine\",\"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\",\"PkgID\":\"musl@1.1.20-r4\",\"PkgName\":\"musl\",\"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\",\"UID\":\"d6abd271e71d3ce2\"},\"InstalledVersion\":\"1.1.20-r4\",\"FixedVersion\":\"1.1.20-r5\",\"Status\":\"fixed\",\"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\",\"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"},\"SeveritySource\":\"nvd\",\"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\",\"DataSource\":{\"ID\":\"alpine\",\"Name\":\"Alpine Secdb\",\"URL\":\"https://secdb.alpinelinux.org/\"},\"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.\",\"Severity\":\"CRITICAL\",\"CweIDs\":[\"CWE-787\"],\"VendorSeverity\":{\"nvd\":4},\"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\",\"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\",\"V2Score\":7.5,\"V3Score\":9.8}},\"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\",\"https://security.gentoo.org/glsa/202003-13\",\"https://www.openwall.com/lists/musl/2019/08/06/1\"],\"PublishedDate\":\"2019-08-06T16:15:00Z\",\"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}"



],



"ArtifactType": "container_image",



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"Metadata": "{\"OS\":{\"Family\":\"alpine\",\"Name\":\"3.9.4\",\"EOSL\":true},\"ImageID\":\"sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1\",\"DiffIDs\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"],\"ImageConfig\":{\"architecture\":\"amd64\",\"container\":\"c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f\",\"created\":\"2019-05-11T00:07:03.510395965Z\",\"docker_version\":\"18.06.1-ce\",\"history\":[{\"created\":\"2019-05-11T00:07:03.358250803Z\",\"created_by\":\"/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / \"},{\"created\":\"2019-05-11T00:07:03.510395965Z\",\"created_by\":\"/bin/sh -c #(nop)  CMD [\\\"/bin/sh\\\"]\",\"empty_layer\":true}],\"os\":\"linux\",\"rootfs\":{\"type\":\"layers\",\"diff_ids\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"]},\"config\":{\"Cmd\":[\"/bin/sh\"],\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"],\"Image\":\"sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a\",\"ArgsEscaped\":true}}}",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz"



}
```

In the current case, format isn't supported and data isn't mapped. If Dynatrace supports the format, it automatically maps it to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

4. Map data to Dynatrace Semantic Dictionary

In simple cases, you can work with ingested events in their original format. However, this becomes difficult in more complex cases, as

* There are many nested fields
* You can't access findings from various tools and products uniformly
* Some fields are added to classify the findings correctly, and others are mapped to the conventions

In such complex cases, you need to manually map the ingested data to the Dynatrace Semantic Dictionary. When data is mapped, the original data persists alongside the mapped one, which allows you to benefit from the vendor-specific data in your analysis and automation or as an additional context.

1. In **OpenPipeline**, select **Pipelines** >  **Pipeline** to [create a custom pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline."), and name it, for example, "Custom security findings".
2. Add a [processor](/docs/platform/openpipeline/concepts/processing#processor "Learn the core concepts of Dynatrace OpenPipeline processing.") of type **DQL** to your pipeline and configure it to parse the fields required by the [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0) (in our case, we want to map the vulnerability findings' basic fields and, as an extension, container image details). Enter the following data:

   * Processor name: For example, "Map Trivy fields"
   * Matching condition: `SchemaVersion == 2 AND ArtifactType == "container_image"` (this way, the mapping will be attempted only for the relevant events)
   * DQL processor definition (in the mapping, we assume that the result and vulnerability arrays already include single items):

   Sample DQL processor definition

   ```
   fieldsAdd event.type="VULNERABILITY_FINDING",



   event.provider="Trivy"



   | parse Results[0], """json:result"""



   | fieldsAdd vulnerability=result[Vulnerabilities][0]



   | parse vulnerability, """json:vulnerability"""



   | parse Metadata, """json:metadata"""



   | fieldsAdd



   finding.id=concat(ArtifactName,"/",metadata[ImageID],"/",vulnerability[PkgID]),



   finding.time.created=toTimestamp(CreatedAt),



   finding.severity=vulnerability[Severity]



   | fieldsAdd



   dt.security.risk.level=if(vulnerability[Severity]=="UNKNOWN","NOT_AVAILABLE",else:vulnerability[Severity]),



   dt.security.risk.score=if(vulnerability[Severity]=="CRITICAL",10,else:



   if(vulnerability[Severity]=="HIGH",8,else:



   if(vulnerability[Severity]=="MEDIUM",6,else:



   if(vulnerability[Severity]=="LOW",3,else:0))))



   | fieldsAdd



   object.id=concat(ArtifactName,"/",metadata[ImageID]),



   object.type="CONTAINER_IMAGE",



   object.name=ArtifactName



   | fieldsAdd



   vulnerability.id=vulnerability[VulnerabilityID],



   vulnerability.description=coalesce(vulnerability[Description],vulnerability[VulnerabilityID]),



   vulnerability.title=coalesce(vulnerability[Title],vulnerability[VulnerabilityID])



   | fieldsAdd



   component.name=vulnerability[PkgName],



   component.version=vulnerability[InstalledVersion]



   | fieldsAdd



   container_image.digest=vulnerability[Layer][Digest]



   | fieldsAdd artifact=splitString(ArtifactName,":")



   | fieldsAdd container_image.repository=artifact[0],



   container_image.tags=artifact[1]



   | fieldsRemove vulnerability, Metadata, artifact
   ```

   ![config dql processor](https://dt-cdn.net/images/2024-11-01-10-41-25-1694-e7c83279aa.png)

   Sample mapped result

   ```
   "timestamp": "2024-10-31T09:58:21.141000000Z",



   "event.provider": "Trivy",



   "event.type": "VULNERABILITY_FINDING",



   "dt.security.risk.score": 10,



   "dt.security.risk.level": "CRITICAL",



   "finding.id": "testdata/fixtures/images/alpine-39.tar.gz/sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1/musl@1.1.20-r4",



   "finding.time.created": "2021-08-25T12:20:30.000000005Z",



   "finding.severity": "CRITICAL",



   "object.id": "testdata/fixtures/images/alpine-39.tar.gz/sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



   "object.type": "CONTAINER_IMAGE",



   "object.name": "testdata/fixtures/images/alpine-39.tar.gz",



   "vulnerability.id": "CVE-2019-14697",



   "vulnerability.title": "CVE-2019-14697",



   "vulnerability.description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code."



   "component.name": "musl",



   "component.version": "1.1.20-r4",



   "container_image.digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



   "container_image.tags": null,



   "container_image.repository": "testdata/fixtures/images/alpine-39.tar.gz",



   "metadata": "{\"OS\":{\"Family\":\"alpine\", \"Name\":\"3.9.4\", \"EOSL\":true}, \"ImageID\":\"sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1\", \"DiffIDs\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"], \"ImageConfig\":{\"architecture\":\"amd64\", \"container\":\"c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f\", \"created\":\"2019-05-11T00:07:03.510395965Z\", \"docker_version\":\"18.06.1-ce\", \"history\":[{\"created\":\"2019-05-11T00:07:03.358250803Z\", \"created_by\":\"/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / \"}, {\"created\":\"2019-05-11T00:07:03.510395965Z\", \"created_by\":\"/bin/sh -c #(nop)  CMD [\\\"/bin/sh\\\"]\", \"empty_layer\":true}], \"os\":\"linux\", \"rootfs\":{\"type\":\"layers\", \"diff_ids\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"]}, \"config\":{\"Cmd\":[\"/bin/sh\"], \"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"], \"Image\":\"sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a\", \"ArgsEscaped\":true}}}",



   "CreatedAt": "2021-08-25T12:20:30.000000005Z",



   "result": "{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\", \"Class\":\"os-pkgs\", \"Type\":\"alpine\", \"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\", \"PkgID\":\"musl@1.1.20-r4\", \"PkgName\":\"musl\", \"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\", \"UID\":\"d6abd271e71d3ce2\"}, \"InstalledVersion\":\"1.1.20-r4\", \"FixedVersion\":\"1.1.20-r5\", \"Status\":\"fixed\", \"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\", \"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"}, \"SeveritySource\":\"nvd\", \"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\", \"DataSource\":{\"ID\":\"alpine\", \"Name\":\"Alpine Secdb\", \"URL\":\"https://secdb.alpinelinux.org/\"}, \"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application\\'s source code.\", \"Severity\":\"CRITICAL\", \"CweIDs\":[\"CWE-787\"], \"VendorSeverity\":{\"nvd\":4}, \"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\", \"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\", \"V2Score\":7.5, \"V3Score\":9.8}}, \"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\", \"https://security.gentoo.org/glsa/202003-13\", \"https://www.openwall.com/lists/musl/2019/08/06/1\"], \"PublishedDate\":\"2019-08-06T16:15:00Z\", \"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}",



   "SchemaVersion": 2,



   "ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



   "Results": [



   "{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\",\"Class\":\"os-pkgs\",\"Type\":\"alpine\",\"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\",\"PkgID\":\"musl@1.1.20-r4\",\"PkgName\":\"musl\",\"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\",\"UID\":\"d6abd271e71d3ce2\"},\"InstalledVersion\":\"1.1.20-r4\",\"FixedVersion\":\"1.1.20-r5\",\"Status\":\"fixed\",\"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\",\"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"},\"SeveritySource\":\"nvd\",\"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\",\"DataSource\":{\"ID\":\"alpine\",\"Name\":\"Alpine Secdb\",\"URL\":\"https://secdb.alpinelinux.org/\"},\"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.\",\"Severity\":\"CRITICAL\",\"CweIDs\":[\"CWE-787\"],\"VendorSeverity\":{\"nvd\":4},\"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\",\"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\",\"V2Score\":7.5,\"V3Score\":9.8}},\"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\",\"https://security.gentoo.org/glsa/202003-13\",\"https://www.openwall.com/lists/musl/2019/08/06/1\"],\"PublishedDate\":\"2019-08-06T16:15:00Z\",\"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}"



   ],



   "ArtifactType": "container_image"
   ```
3. Select **Dynamic routing** >  **Dynamic route** to [add a dynamic routing](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.") to the new pipeline. Enter the following data:

   * Dynamic route name: For example, "Custom event"
   * Matching condition: `SchemaVersion == 2 AND ArtifactType == "container_image"`
   * Select the pipeline to which the dynamic routing will apply (in our case, `Custom security findings`)

   ![add dynamic routing](https://dt-cdn.net/images/2024-08-28-23-04-46-576-9e042f6845.png)

   For details on dynamic routing, see [Routing](/docs/platform/openpipeline/concepts/data-flow#routing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.").

## Next steps

Now you can use the data to

* [Visualize container vulnerability findings with a sample dashboard](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate Jira ticket creation and Slack notifications with sample workflows](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")


---


## Source: instant-intrusion-response.md


---
title: Instant Intrusion Response
source: https://www.dynatrace.com/docs/secure/use-cases/instant-intrusion-response
scraped: 2026-02-16T21:31:22.722941
---

# Instant Intrusion Response

# Instant Intrusion Response

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

Time is crucial when dealing with security incidents. This page shows how you can use Dynatrace to speed up your incident response in two phases:

* When an attack is detected, Dynatrace can automate the notification and analysis for you, so that the right teams are informed and receive actionable information to start working on the issue.
* When investigating an issue, each new discovery guides the next steps in the incident response. Through Grailâs schemaless queries, Dynatrace allows you to remain flexible in this time-critical process.

## Target audience

This page is intended for Security teams analyzing security incidents, such as the Incident Response team.

## Scenario

In the following, we address a scenario in which identifying an attack, researching the scope, determining the responsible entity owners, and remediating the attack takes hours, sometimes even days.

* Tools like AWS GuardDuty trigger events on suspicious activity independently.
* Handling the incoming load while increasing security strength is impossible.
* All correlation and collaboration are manual, resulting in frustration about the silos.
* Several internal integration tools, hard to manage, have been built; they are helpful, but aren't providing solid and safe automation.
* A typical suspicious incident takes days to escalate and qualify.

### Request

The team wants to quickly

* Identify when a possible attack is happening.
* Research the scope and determine what is affected: for example, whether the attack affects only a single isolated, non-production system or threatens a critical part of the environment.
* Determine the responsible entity owners.
* Remediate the attack.

### Goals

* **Efficiency**: The team should be able to respond much faster to attacks.
* **Flexibility**: The team should have more flexibility in their response to security incidents.

### Result

Combining the Dynatrace automation capabilities with insights into security-related data, our solution helps security teams react and respond faster to attacks. The team automatically scans all ingested logs for patterns that might indicate possible attacks. Because each attack is different, they make use of schemaless queries with instant responses to quickly identify the scope of an attack, thus reducing the required time from days to minutes.

## How it works

### Context

Logs from your [Dynatrace-monitored environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") are ingested into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") via [log ingestion](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace."). When an attack is detected, a Dynatrace problem is created.

### 1. Intrusion notification automation

A workflow is automatically triggered by this type of problem. The workflow collects, processes, and enriches the data with context, and converts the resulting information into notifications on your desired channels.

For an example of how you can set up an attack notification automation, see [Intrusion notification automation](#workflow).

### 2. Instant queries

Based on the information received, you can immediately respond to discoveries and perform further investigations by running a sequence of DQL queries in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** tailored to the attack type.

For details, see [Instant queries](#notebook).

## Prerequisites

* Dynatrace version 1.283+
* [Set up log ingestion](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") (ingests security incidents into Grail).
* [Set up ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") (allows the workflow to assign security incidents based on ownership of the affected entity).
* [Set up Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.") (allows the workflow to convert resulting findings into Jira tickets).
* [Set up Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces") (allows the workflow to send resulting findings to Slack channels).

  While the current scenario uses Slack and Jira as notification channels, other integrations are also available. For details, see [Workflows integrations](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").
* Basic knowledge of how to

  + [Use Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
  + [Create workflows](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.")
* Make sure the following permissions are enabled.

  + **Grail**: `storage:logs:read`. For instructions, see [Assign permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
  + ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**: Permissions to access, view, write, and execute workflows. For details, see [Authorization](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

    To access permissions, go to the **Settings** menu in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.

## 1. Intrusion notification automation

The following example illustrates how you can implement an attack notification automation using [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."). You can customize the workflow according to your needs.

1. Set the trigger

The automation needs to be triggered whenever an attack occurs.

In the **Select trigger** section, select and configure **Davis Problem trigger**. For details, see [Create workflows in Dynatrace Workflows: Trigger](/docs/analyze-explore-automate/workflows/building#trigger "Create and edit workflows in Dynatrace Workflows.").

Show me the relevant workflow task sequence

![Set the trigger](https://dt-cdn.net/images/trigger-1700-3001e4f912.png)

2. Determine ownership

Route notifications to the team responsible for the affected entities.

Select the **Get owners** action to create and configure this task. For details, see [Ownership app: **`get_owners`**](/docs/deliver/ownership-app#get-owners "It provides custom actions to define workflows integrating entity owners and their contact information.").

Show me the relevant workflow task sequence

![Set ownership](https://dt-cdn.net/images/set-owners-1700-f719d66bac.png)

3. Set up notification variables

Configure variables such as default values for Slack and Jira fields, that will be used in later steps in the notification process.

Select the **Run JavaScript** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequences

![Define notification channels](https://dt-cdn.net/images/channels-1700-83943a78ba.png)

4. Collect data and enrich with context

* Query third-party services. For example:

  + Perform a WHOIS lookup to find details about the attacker's IP address.
  + Verify the IP reputation using a third-party service such as AbuseIPDB.

  Select the **HTTP Request** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").
* Query Dynatrace. For example:

  + Determine whether there were any successful logins from the attacker's IP address.
  + Find out additional traffic information from the attacker's IP address.

  Select the **Execute DQL Query** action to create and configure these tasks. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequences

![Collect and enrich data](https://dt-cdn.net/images/collect-data-1700-2cf1aad6c7.png)

5. Extract successful requests

Extract the successful requests from the total requests collected.

Select the **Run JavaScript** action to create and configure this task. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequence

![Extract successful requests](https://dt-cdn.net/images/extract-successful-1700-7d72549785.png)

6. Replay against target

Replay the successful requests against the target entity to look for indicators of compromise. Custom code steps allow you to automate complex logic that you want to run for each detected attack. Depending on the detected attack and the affected systems, you might want to replay the attacks for more detailed analysis.

Select the **Run JavaScript** action to create and configure this task. For details, see [Introduction to workflows: Action](/docs/analyze-explore-automate/workflows#concept-action "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

Show me the relevant workflow task sequence

![Replay against target](https://dt-cdn.net/images/replay-against-target-1700-dca61b334e.png)

7. Send notifications

* Notify the responsible team on Slack.

  Select the **Send message** action to create and configure this task. For details, see [Use Workflows with Slack](/docs/analyze-explore-automate/workflows/actions/slack#workflow "Send messages to Slack Workspaces").
* Create a Jira ticket for the entity owner containing the collected information.

  Select the **Create issue** action to create and configure this task. For details, see [Create Jira issues with workflows](/docs/analyze-explore-automate/workflows/actions/jira#workflow "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.").

Show me the relevant workflow task sequences

![Send notifications](https://dt-cdn.net/images/send-notifications-1700-52548fa8bb.png)

## 2. Instant queries

After receiving the notification, the security team can immediately respond to discoveries and instantly run additional DQL queries in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") without knowing beforehand where the information they're looking for is. In an emergency situation, this is crucial, as a speedy response can ensure that the attack can be contained.

The following are some examples of how you can query Grail in case of a web attack.

### Logs from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP ADDRESS>>"



| sort timestamp desc
```

### Successful web requests from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP Address>>"



| filter http.status_code == "200"



| sort timestamp desc
```

### Status codes and response codes overview

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| filter net.peer.ip == "<<IP Address>>"



| summarize requests=count(), by:{http.status_code, http.user_agent}



| sort http.status_code
```

### Payloads used by the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



// Successful requests only



| filter http.status_code == "200"



| filter net.peer.ip == "<<IP Address>>"



| summarize requests=count(), by:{http.target}



| sort requests DESC
```

### Successful requests from a given IP address sorted by response size

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| fields timestamp, net.peer.ip, http.target, http.status_code, http.response_content_length, http.user_agent



| filter http.status_code == "200"



// Filter for a specific IP address



| filter net.peer.ip == "<<IP Address>>"



| sort toLong(http.response_content_length) DESC
```

### Payloads in access logs (both successful and not successful)

Query example:

```
fetch logs, scanLimitGBytes:-1



| filter log.source == "/var/log/nginx/access.log"



| fields payload = "<<PAYLOAD>>", timestamp, net.peer.ip, http.method, http.target, http.status_code, http.request.header.referrer, http.response_content_length, http.user_agent, content



| filter contains(content, payload)
```

### Successful SSO logins from the attacker IP address

Query example:

```
fetch logs, scanLimitGBytes: -1



// Search for logins



| filter log.source == "/var/log/sso.log"



// Search for successful logins from a given IP address



| filter contains(content, "user login successful") and contains(content, "<<IP address>>")



| sort timestamp desc
```

### Which environments the attacker has logged into

Query example:

```
fetch logs, scanLimitGBytes: -1



// Search for logins



| filter log.source == "/var/log/sso.log"



// Search for logins from a given account id



| filter contains(content, "<<Account ID>>") and contains(content, "tenant: ")



| sort timestamp desc
```

## Stay ahead of threats

You can use the above instructions as building blocks to automate common steps in your incidents process. These can help you respond faster to security incidents, thus reducing their impact.

## Further reading

[Log on Grail examples](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")

[Dynatrace Intelligence DQL examples](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")

[DQL examples for security-related data](/docs/secure/threat-observability/dql-examples "DQL examples for security data powered by Grail.")


---


## Source: monitor-sign-in-activity.md


---
title: Monitor suspicious sign-in activity with Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/monitor-sign-in-activity
scraped: 2026-02-16T21:21:54.858021
---

# Monitor suspicious sign-in activity with Dynatrace

# Monitor suspicious sign-in activity with Dynatrace

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

As organizations embrace cloud technologies, monitoring sign-in logs is crucial for detecting anomalies, investigating suspicious activities, and ensuring regulatory compliance. Real-time visibility into login behavior helps rapidly address security risks, protect user identities, and safeguard critical resources. It also provides actionable insights into compromised accounts, malicious insiders, and user behavior patterns, aiding strategic decisions on access management, device policies, and application usage.

While the following scenario focuses on Microsoft Entra ID logs as an example, the described approach is universally applicable to any cloud, access, or identity provider integrated with Dynatrace. This is made possible through Semantic Dictionary and the standardized data mapping to the defined [semantic model](/docs/semantic-dictionary/model/log "Get to know the Semantic Dictionary models related to Log Analytics.").

As long as sign-in logs from a supported identity provider are ingested into Dynatrace, you can follow the steps outlined below to monitor these logs effectively.

## Target audience

Security administrators and security teams responsible for safeguarding their organizationâs cloud environment and user activity.

## Scenario

Your organization relies on Microsoft Entra ID as a centralized identity provider, granting users single-sign-on (SSO) access to various company applications and services.
Microsoft Entra ID sign-in logs are forwarded to Dynatrace and stored in Grail to gain deeper visibility into user activity, creating a unified data hub for monitoring and analysis.

As a security administrator, your responsibility is to

* Safeguard user identities belonging to your organization
* Monitor user access and track patterns to spot unusual behavior quickly
* Identify and investigate potential threats or anomalous sign-in events
* Start incident response activities promptly to minimize damage if a user account gets compromised

### Goals

* Achieve comprehensive visibility over the cloud environment and user activity through a single pane of glass.
* Demonstrate how to monitor Microsoft Entra ID sign-in logs and user activity to detect potential security issues and anomalous behaviors.

## Prerequisites

* Knowledge of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.").
* Send Microsoft Entra ID sign-in logs to Dynatrace. There are two options to stream logs:

  + [Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")
  + [Azure Log Forwarder](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* Follow the instructions in [Create a pipeline for processing](/docs/platform/openpipeline/use-cases/tutorial-technology-processor#pipeline "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.") to configure the OpenPipeline environment. Select **Azure Entra ID Audit Logs** as the built-in processor.

## Get started

1. Import dashboard

Use our sample dashboard to view user sign-in activities within your cloud environments.

1. Download the [sample dashboard from GitHubï»¿](https://dt-url.net/ur03wvb).
2. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.

2. Set up filters

1. In **Product**, filter for `Azure` to display Microsoft Entra ID sign-in logs coming from the connected Azure environment.
2. Use the timeframe selector to narrow down your investigation to relevant incidents, identify trends or anomalies within that window, and efficiently monitor user activities or suspicious behavior during critical times.

   ![filtering](https://dt-cdn.net/images/2025-03-26-18-28-55-1865-3328587bcd.png)
3. To fine-tune your investigation, consider setting up additional filters. For example:

   * **User**, to analyze individual sign-in trends, devices, and locations for specific users, helping you to identify unusual access patterns or targeted attacks.
   * **User IP address**, to investigate activities from particular IP addresses, detecting repeated failed sign-ins or unusual access origins.
   * **Device OS**, to track the operating systems used during sign-ins, helping you to spot outdated or unauthorized devices.
   * **Country**, to examine sign-ins by geographic location to detect access from unexpected or restricted regions.
   * **Target service**, to identify which services or applications are being accessed, useful for monitoring sensitive resources.
   * **Result code**, to review the outcomes of sign-in attempts to detect anomalies, such as excessive failed attempts indicating potential brute-force attacks.
   * **Client application**, to determine which applications are being used to sign in, useful for identifying unauthorized or suspicious app usage.

3. Review activity and trends

In the **Sign-in activity monitoring** section, you can

* Analyze sign-in trends
* Identify peak activity periods
* Investigate access patterns by location or IP address

This enables you to gain a clear understanding of user distribution and quickly spot irregular activities from unexpected regions, helping you enhance security and respond to potential risks effectively.

![An overview dashboard example](https://dt-cdn.net/images/image-50-2540-6620ffd45d.png)

Run query

You can reproduce the **Sign-in activity outcomes over time** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| makeTimeseries {



Success = countIf(audit.result=="Succeeded", default:0),



Failure = countIf(audit.result!="Succeeded", default:0)



}, time:audit.time
```

4. Drill down

In the **Top sign-in activity breakdown** section, you can explore detailed insights into user and IP-based sign-in activities.

**Example 1**: In **Top 10 sign-in users**, you can identify

* Anomalies such as account lockouts or potential brute-force attacks
* Users with the highest number of sign-in attempts, categorized by successful and failed attempts
* Users with the most failed attempts, with associated IP addresses and client applications

![sign-in users](https://dt-cdn.net/images/2025-03-26-14-46-19-1359-17c6e4d12e.png)

Run query

Top 10 sign-in users

Top 10 users by failed sign-in attempts

You can reproduce the **Top 10 sign-in users** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded", by:{User=audit.identity



}



| sort Success+Failure desc



| limit 10
```

You can reproduce the **Top 10 users by failed sign-in attempts** table in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(),



`Client applications` = collectDistinct(client.app.name),



`IPs` = collectDistinct(client.ip)



}, by:{User=audit.identity}



| sort Failures desc



| limit 10
```

**Example 2**: In **Top 10 sign-in IPs**, you can

* Uncover unusual patterns which may indicate malicious activity, such as repeated failed attempts from a single IP or multiple users accessing from the same IP
* View rankings of IP addresses with the most sign-in attempts, along with those linked to multiple users or services

![sign-in-ip](https://dt-cdn.net/images/2025-03-26-17-26-56-1644-34f2135bb6.png)

Run query

Top 10 sign-in IPs

Top 10 addresses by failed sign-in attempts

You can reproduce the **Top 10 sign-in IPs** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded")



}, by:{IP=client.ip}



| sort Success+Failure desc



| limit 10
```

You can reproduce the **Top 10 addresses by failed sign-in attempts** table in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(), Users = collectDistinct(audit.identity),



`Target services` = collectDistinct(client.app.name)



}, by:{`Client IP`=client.ip, City=actor.geo.city.name}



| sort Failures desc



| limit 10
```

5. Analyze data

Dynatrace Intelligence automatically identifies anomalous trends and deviations in sign-in logs, significantly enhancing your organization's ability to detect potential threats swiftly. Dynatrace Intelligence continuously analyzes user sign-in patterns, providing proactive alerts when anomalies are detected.

To detect anomalous peaks within the observed sign-in logs with Davis

1. Select any of the time-based charts, then select **Open with**.

   ![davis02](https://dt-cdn.net/images/sssssss-1102-25711b87e5.png)
2. Select **Notebooks**.
3. In the notebook document that opens, select **Options**.
4. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
5. Select an analyzer and configure its parameters.
6. Select **Run analysis**.

For example, you can select an auto-adaptive threshold to apply a dynamic approach based on the past sign-in trends.

![An example of AI data analysis in the Notebooks app.](https://dt-cdn.net/images/2025-03-27-12-52-08-1920-d8b53c4e4a-1444-3573714c33.png)

## Summary

Monitoring sign-in activities in cloud environments is essential for detecting anomalies, protecting critical resources, and ensuring compliance. Integrating sign-in logs into the Dynatrace platform centralizes visibility into user access patterns. By analyzing metrics like top users, IP addresses, client applications, and locations, security teams can swiftly identify suspicious behavior and address potential threats. The dashboardâs filtering options allow targeted investigations, enhancing threat detection and accelerating incident response.


---


## Source: notification-automation.md


---
title: CSPM Notification Automation
source: https://www.dynatrace.com/docs/secure/use-cases/notification-automation
scraped: 2026-02-16T21:21:53.475448
---

# CSPM Notification Automation

# CSPM Notification Automation

* Latest Dynatrace
* Tutorial
* Updated on Jan 31, 2024

Early Adopter

Hyperscalers provide offerings such as [AWS Security Hubï»¿](https://dt-url.net/5l239zz), through which security-related events give insights into potential threats. These events must be triaged, analyzed, and remediated by the owners of the affected resources, and reaching hundreds of thousands of such alerts is common.

* The volume of these events currently means that not all can get the attention they deserve.
* Because ownership of resources is distributed, significant coordination and administrative effort is required to ensure that all events are acted upon.

Dynatrace addresses these concerns and improves your cloud security posture management (CSPM) by introducing an automation workflow that filters security findings stored in Grail and triggers alerts only for the events that matter.

## Target audience

This page is intended for Security teams analyzing security findings.

## Scenario

In the following, we address a scenario in which 400,000 AWS alerts are issued daily.

Manually dealing with all of them is simply infeasible. The Security team therefore has to focus only on high-priority events and has built custom tooling to partially automate Jira ticket creation.

* Within a year, nearly 1,100 security tickets have been manually created from those events.
* Investigating those tickets has involved about 300 people gathering additional information to analyze the situation.

Effort is sometimes invested in vain, and alerts turn out to be irrelevant, but the resource owner must always cross-check the resolution with the Security team. Ensuring that all are followed up on requires a significant coordination effort, leaving less time for actual security work.

### Request

* The team wants to be able to explore all data but receive notifications (tickets) only for critical or high events and only for certain relevant AWS accounts.
* Notifications should include the alert type, full context, relevant details, and remediation advice to enable understanding, actionability, and operationalization.
* Only the account owner should be informed of the issue (tickets should be automatically assigned to him).
* The team doesn't want to be spammed with multiple notifications for the same issue, so there shouldn't be any duplicate tickets.

### Goal

**Efficiency**: The team should be able to act on everything that matters immediately.

### Result

**Dynatrace CSPM Notification Automation** is a tool designed to answer the Security team's pain and improve their efficiency significantly. It allows the team to continue monitoring events without being burdened with alerts; they can now focus only on what matters and requires their security expertise.

More concretely, from a total of 400,000 alerts per day, of which just 40,000 are relevant, with Dynatrace CSPM Notification Automation, only a couple of Jira tickets are now created daily, just for the relevant issues.

## How it works

Dynatrace CSPM Notification Automation consists of two stages.

1. (Prerequisite) AWS security findings from [AWS Security Hubï»¿](https://dt-url.net/5l239zz)
   are ingested into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") by means of [Dynatrace log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.").
2. (Actual automation) A predefined [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") orchestrates the processes of querying, filtering, and grouping data and converts the resulting findings into Jira tickets for remediation. See [Get started](#start) for the workflow steps.

![How CSPM automation works](https://dt-cdn.net/images/2024-01-31-15-04-14-470-834fcfc1a2.png)

## Prerequisites

See below for the [AWS](#aws) and [Dynatrace](#dt) requirements.

### AWS requirements

* [Set up AWS accountsï»¿](https://dt-url.net/ng439wv) for which you want to receive notifications.
* [Set up AWS Security Hubï»¿](https://dt-url.net/uh639rl) (collects AWS security findings).

### Dynatrace requirements

* Dynatrace version 1.276+
* [Set up log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") (ingests AWS security findings into Grail).
* [Set up Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira#setup "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.") (allows the workflow to convert resulting findings into Jira tickets).
* Make sure the following permissions are enabled.

  + **Grail**: `storage:logs:read`. For instructions, see [Assign permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
  + ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**: Permissions to access, view, write, and execute workflows. For details, see [Authorization](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

    To access permissions, go to the **Settings** menu in the upper-right corner of ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** and select **Authorization settings**.

## Get started

Once your AWS security findings are ingested into Grail (see [Prerequisites](#prerequisites)), you can set up the CSPM Notification Automation workflow.

The workflow consists of several steps you can adapt according to your needs. To configure it, you can start by importing a prefilled workflow into your environment.

1. Import workflow

1. Copy and save the JSON file below.

   ```
   {



   "id": "dcce961d-26a9-46e6-a9e4-14a0f7f2185c",



   "title": "CSPM Notification Automation",



   "description": "",



   "tasks": {



   "count_all_new_findings": {



   "name": "count_all_new_findings",



   "description": "Executes query to count all recently created AWS findings",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| fields timestamp\n| filter timestamp > now() - 24h                                                                        // Only filter created since last successful run         \n| summarize { count=count() }"



   },



   "position": {



   "x": -1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "log_new_findings_count": {



   "name": "log_new_findings_count",



   "description": "Logs total number of recently created AWS findings",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n\n  const ex = await execution(executionId);\n  const countResult = await ex.result(\"count_all_new_findings\");\n\n  console.log('======================================================================')\n  console.log('Total findings added since last run: ')\n  console.log(countResult.records[0].count)\n  console.log('')\n}"



   },



   "position": {



   "x": -1,



   "y": 3



   },



   "predecessors": [



   "count_all_new_findings"



   ],



   "conditions": {



   "states": {



   "count_all_new_findings": "OK"



   }



   }



   },



   "log_tickets_by_account": {



   "name": "log_tickets_by_account",



   "description": "Logs potentially created Jira issues for findings by account",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n  const ex = await execution(executionId);\n  const by_control_id = await ex.result(\"fetch_findings_by_account\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by accounts, ${by_control_id.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_control_id.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.controlId} - AWS account ${finding.awsAccountId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your account via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.awsAccountId}`)\n    console.log('')\n    console.log('Vulnerability:')\n    console.log(`${finding.controlId} - ${finding.title}`)\n    console.log(finding.severity)\n    console.log(finding.description)\n    console.log(finding.remediation[0].Recommendation.Url)\n    console.log('')\n    console.log('Affected resources:')\n    for(let resource of finding.resources) {\n      console.log(resource)\n    }\n    console.log('')          \n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_control_id.records;\n}"



   },



   "position": {



   "x": 0,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_account"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_account": "OK"



   }



   }



   },



   "workflow_config_params": {



   "name": "workflow_config_params",



   "description": "Sets configuration parameters for the workflow run",



   "action": "dynatrace.automations:run-javascript",



   "input": {



   "script": "// This step sets up some configurational parameters for the workflow run \n// (e.g. which accounts, which finding types we are filtering for)\nexport default async function () {\n\n  // AWS accounts to filter for\n  const awsAccountIds = [\n    // add your AWS account ids here, e.g.\n    // \"1234567890\"\n  ]\n\n  // Findings that should be grouped by AWS account\n  const securityControlIdsToGroupByAccount = [\n    // add you control IDs here, e.g.\n    // \"S3.1\" // S3 Block Public Access setting should be enabled\n  ]\n\n  // Findings that should be grouped by AWS Resource\n  const securityControlIdsToGroupByResource = [\n    // add you control IDs here, e.g.\n    // \"EC2.13\" // Security groups should not allow ingress from 0.0.0.0/0 to port 22\n  ]\n  \n  return { awsAccountIds, securityControlIdsToGroupByAccount, securityControlIdsToGroupByResource }\n}"



   },



   "position": {



   "x": 0,



   "y": 1



   },



   "predecessors": []



   },



   "log_tickets_by_resource": {



   "name": "log_tickets_by_resource",



   "description": "Logs potentially created Jira issues for findings by resource",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n  const ex = await execution(executionId);\n  const by_resource = await ex.result(\"fetch_findings_by_resource\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by resource, ${by_resource.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_resource.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.resource.resourceId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your resource via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.aws.accountId}`)\n    console.log('')\n    console.log('Resource details:')\n    console.log(finding.resource.resourceType)\n    console.log(finding.resource.resourceId)\n    console.log('')\n    console.log('Vulnerabilities:')\n    for(let vulnerability of finding.vulnerabilities) {\n      console.log(`${vulnerability.controlId} - ${vulnerability.title}`)\n      console.log(vulnerability.severity)\n      console.log(vulnerability.description)\n      console.log(vulnerability.remediation[0].Recommendation.Url)      \n    }\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_resource.records;\n}"



   },



   "position": {



   "x": 1,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_resource"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_resource": "OK"



   }



   }



   },



   "create_issue_for_account": {



   "name": "create_issue_for_account",



   "description": "Creates new Jira issue or the vulnerable AWS account",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 0,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_account": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_account\")}}"



   },



   "create_issue_for_resource": {



   "name": "create_issue_for_resource",



   "description": "Creates new issue for the vulnerable AWS resource",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 1,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_resource": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_resource\")}}"



   },



   "fetch_findings_by_account": {



   "name": "fetch_findings_by_account",



   "description": "Executes query to get relevant security findings grouped by AWS account",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resource = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByAccount | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus),\n              resources = collectDistinct(resource),\n              title = takeAny(title),\n              description = takeAny(description),\n              severity = takeAny(severity),\n              awsRegion = collectArray(awsRegion)\n            },\n            by:{\n              controlId, \n              awsAccountId\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields awsAccountId, entity.name\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n"



   },



   "position": {



   "x": 0,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "fetch_findings_by_resource": {



   "name": "fetch_findings_by_resource",



   "description": "Executes query to get relevant security findings grouped by AWS resource",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resourceId = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByResource | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus)\n            },\n            by:{\n              alertType, \n              resourceType, \n              controlId, \n              title,\n              description, \n              severity, \n              resourceId, \n              awsAccountId,\n              created,\n              awsRegion\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields id, awsAccountId, entity.name, tags, awsNameTag\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n| fields aws = record(\n            accountId = awsAccountId,\n            name = aws.account.entity.name,\n            entity = aws.account.id\n         ), \n         resource = record(\n           resourceId = resourceId,\n           resourceType = resourceType\n         ),\n         region = awsRegion,\n         alert = record(controlId = controlId, \n           severity = severity, \n           complianceStatus = complianceStatus,\n           title = title,\n           description = description,\n           remediation = remediation\n         )\n| summarize {\n        count=count(),\n        vulnerabilities = collectDistinct(alert)\n      },\n      by:{\n        aws,\n        resource,\n        region\n      }"



   },



   "position": {



   "x": 1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "prepare_tickets_by_account": {



   "name": "prepare_tickets_by_account",



   "description": "Prepares payload of Jira tickets for vulnerable AWS accounts",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n    const ex = await execution(executionId);\n    const records = await ex.result(\"log_tickets_by_account\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const resourcesList = finding.resources\n          .map( resource => `|${resource}|` )\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.controlId} - AWS Account ${finding.awsAccountId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.awsAccountId}|\\n\\n`\n              + '*Vulnerability*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + `|{noformat}${finding.controlId}{noformat}|{noformat}${finding.severity}{noformat}|${finding.title}|${finding.description}|[${finding.remediation[0].Recommendation.Url}]|\\n\\n`\n              + '*Affected Resources*:\\n'\n              + '||Resource Id||\\n'\n              + resourcesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 0,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_account": "OK"



   }



   }



   },



   "prepare_tickets_by_resource": {



   "name": "prepare_tickets_by_resource",



   "description": "Prepares payload of Jira tickets for vulnerable AWS resources",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function ({ executionId }) {\n    const ex = await execution(executionId);\n    const records = await ex.result(\"log_tickets_by_resource\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const vulnerabilitiesList = finding.vulnerabilities\n          .map( vuln => \n            `|{noformat}${vuln.controlId}{noformat}|{noformat}${vuln.severity}{noformat}|${vuln.title}|${vuln.description}|[${vuln.remediation[0].Recommendation.Url}]|`)\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.resource.resourceId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.aws.accountId}|\\n\\n`\n              + '*Resource Details*:\\n'\n              + '||Resource Type||Resource Id||\\n'\n              + `|${finding.resource.resourceType}|${finding.resource.resourceId}|\\n\\n`\n              + '*Vulnerabilities*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + vulnerabilitiesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 1,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_resource": "OK"



   }



   }



   }



   },



   "ownerType": "USER",



   "isPrivate": false,



   "trigger": {



   "schedule": {



   "rule": null,



   "trigger": {



   "type": "time",



   "time": "09:00"



   },



   "timezone": "Europe/Berlin",



   "isActive": true,



   "isFaulty": false,



   "nextExecution": "2023-10-03T07:00:00.000Z",



   "filterParameters": {



   "earliestStart": "2023-09-25"



   },



   "inputs": {}



   }



   },



   "schemaVersion": 3



   }
   ```
2. In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, select **Upload** and upload the file.

2. Set the time

**Fixed time trigger**: Sets the time when you want the workflow to run (in the current case, the workflow runs every day at 9:00 AM). See [Schedule workflows](/docs/analyze-explore-automate/workflows/trigger/schedules "Guide to creating workflow automation schedule triggers in Dynatrace Workflows.") for more information on scheduling a workflow.

Show me the relevant workflow task

![Set the time in CSPM workflow ](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-79b6452375.png)

3. Define parameters

**Workflow config params**: Determines what findings you want to filter for. In the current scenario, the team wants to

* Receive notifications only about findings from important AWS accounts while discarding those from other accounts, such as environments that aren't in production.

  + Under `awsAccountIds`, select which AWS accounts you want to get findings for.
* Group findings for specific [security control IDsï»¿](https://dt-url.net/nx8393z) into one ticket per AWS account.

  + Under `securityControlIdsToGroupByAccount`, select which security control IDs you want to group by AWS account.
* Group findings for specific security control IDs into one ticket per AWS resource.

  + Under `securityControlIdsToGroupByResource`, select which security control IDs you want to group by AWS resource.

Show me the relevant workflow task

![Define parameters in CSMP workflow](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-711174cd7e.png)

4. Orchestrate findings

By AWS account

By AWS resource

The following task sequence orchestrates grouping and converting the resulting findings into one ticket per AWS account.

1. **Fetch findings by account**: Executes the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") that fetches the findings. Some of the information fetched for the current case, to be displayed in Jira, includes

   * Number of findings for the respective account
   * Issue title, including the security control IDs and the AWS account name
   * Short description of the vulnerabilities
   * Link to AWS for how to remediate the vulnerabilities
   * List of affected AWS resources
2. **Log tickets by account**: Shows a ticket's potential content before one is automatically created. This step ensures that your configuration is correct. For details, see [Plot statistics before creating tickets](#test).
3. **Prepare tickets by account**: Configures the payload for the Jira ticket.
4. **Create issues for account**: Integrates with your Jira connection. In **Input**, select your Jira connection created in [Prerequisites](#dt) and enter the desired parameters of the Jira ticket.

Show me the relevant workflow task sequence

![Group findings by AWS account](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e9069605d2.png)

The following task sequence orchestrates grouping and converting the resulting findings into one ticket per AWS resource.

1. **Fetch findings by resource**: Executes the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") that fetches the findings. Some of the information fetched for the current case, to be displayed in Jira, includes

   * Number of findings for the respective resource
   * Issue title, including the security control IDs and the AWS resource name
   * AWS account name of the respective resource
   * Resource details
   * Short description of the vulnerabilities
   * Link to AWS for how to remediate the vulnerabilities
2. **Log tickets by resource**: Shows a ticket's potential content before one is automatically created. This step ensures that your configuration is correct. For details, see [Plot statistics before creating tickets](#test).
3. **Prepare tickets by resource**: Configures the payload for the Jira ticket.
4. **Create issues for resource**: Integrates with your Jira connection. In **Input**, select your Jira connection created in [Prerequisites](#dt) and enter the desired parameters of the Jira ticket.

Show me the relevant workflow task sequence

![Group findings by AWS resource](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e30cc64df3.png)

5. Display statistics

The following task sequence displays a count of the new findings since the last workflow run.

1. **Count all new findings**: Executes the DQL query that fetches the number of findings created by AWS Security Hub in the last 24 hours.
2. **Log new findings count**: Displays the query result.

Show me the relevant workflow task sequence

![Display stats in CSPM workflow](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ac3fc24771.png)

Once you're done configuring the workflow, select **Save**.

### Plot statistics before creating tickets

To test your configuration before sending Jira tickets

1. Disable the **Prepare tickets by account/resource** and **Create issues for account/resource** tasks.

Show me the relevant workflow task sequences

![Disable tasks for creating notifications ](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ef757cb613.png)

For instructions on disabling a task, see [Disable or enable a task](/docs/analyze-explore-automate/workflows/building#disable-enable "Create and edit workflows in Dynatrace Workflows.").

2. Run the workflow or execute individual tasks for which you want to check the output. For instructions, see [Run and monitor workflows](/docs/analyze-explore-automate/workflows/running "Run and monitor workflows created in Dynatrace Workflows.").

## Smart security

Congratulations! Youâve now set up an automation that empowers your security team. With Dynatrace CSPM Notification Automation, critical events are streamlined, alert fatigue is minimized, and cloud security is enhanced. Efficiency unleashed!

## Further resources

The following is a tutorial by the internal customer of Dynatrace CSPM Notification Automation.

CSPM Notification Automation with Dynatrace


---


## Source: runtime-contextualization-of-container-findings.md


---
title: Runtime contextualization of container findings
source: https://www.dynatrace.com/docs/secure/use-cases/runtime-contextualization-of-container-findings
scraped: 2026-02-17T04:59:04.504947
---

# Runtime contextualization of container findings

# Runtime contextualization of container findings

* Latest Dynatrace
* Tutorial
* Updated on Sep 30, 2025

Container image scanning is usually performed in artifact repositories, such as [AWS Elastic Container Registry (ECR)ï»¿](https://dt-url.net/mu03pcw), [GCP Artifact Registryï»¿](https://dt-url.net/9g03udo), and [Microsoft Azure Container Registryï»¿](https://dt-url.net/mn23u20). After the images are deployed in production, continuous reassessing of the container images is essential to ensure they're not affected by emerging critical vulnerabilities.

The number of vulnerability findings grows with the number of stored container images, and the development team might become overwhelmed by the number of critical findings. Some of the container images will never be deployed to your production environment. They might be part of your test environments or become obsolete and lay in the repository as a legacy.

In this context, Dynatrace helps you

* Reduce alert fatigue
* Focus remediation efforts on the critical vulnerability findings that significantly impact your production applications

![overview of vulnerability alert reduction](https://dt-cdn.net/images/final-final-v3-last-final-teo-500-f2e05b1ca1.png)

## Target audience

Site reliability engineers (SREs) and application owners who want to maintain the security hygiene and health of their applications.

## Scenario

* The development team stores container images in Amazon ECR. Later on, those images are deployed into staging and production environments running on Kubernetes.
* You monitor the health of your applications with Dynatrace OneAgent in Kubernetes.
* Several new critical vulnerabilities have been discovered recently by Amazon ECR in the container images.

### Request

* Triage critical vulnerabilities and assess the situation automatically.
* Automatically create tickets and notifications for emerging critical vulnerabilities that threaten your production application.

### Goal

Avoid critical vulnerability exposure in production applications on containers with vulnerable container images.

### Result

Our solution allows you to

* Filter for critical findings in production applications on containers with vulnerable container images
* Create notification automation workflows based on those findings

## Prerequisites

* [Set up Kubernetes observability with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* [Ingest Amazon ECR vulnerability findings and scan events](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Use Dynatrace release product/stage tags](/docs/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies") for your containers

## Get started

1. Visualize

To view the summarized and unified list of recent vulnerability findings ingested from Amazon ECR

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Container Vulnerability Findings** for the Amazon ECR integration.

Example dashboard:

![dashboard sample for container vulnerabilities](https://dt-cdn.net/images/new-dashboard-4308-b95f9d6ec2.png)

2. Filter

1. Filter for `RuntimeStatus` to display contextualized findings affecting your runtime containers.

   ![runtime status filter](https://dt-cdn.net/images/2024-11-04-10-10-45-1835-6e0d130070.png)
2. Filter for `ProductStage` to display contextualized findings affecting your production services and applications.

   ![product stage filter](https://dt-cdn.net/images/2024-11-04-10-12-42-1829-24210337bc.png)

3. Automate

You can adjust our automation workflow samples to enrich and filter external container image vulnerability findings for runtime context. For details, see [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.").

Example query to get new critical container image vulnerabilities with a list of the affected container images and running containers:

This query has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
// The query has a rolling window of 7 days and the last 24hrs.



// Vulnerability finding events which have already been reported



// before the current 24hr window will not be reported again.



fetch security.events, from: now() - 7d



| filter dt.system.bucket == "default_securityevents"



AND object.type == "CONTAINER_IMAGE"



AND event.type == "VULNERABILITY_FINDING"



AND dt.security.risk.level == "CRITICAL"



// now enrich the runtime context



| join [



fetch dt.entity.container_group_instance, from:now()-3h



| fieldsAdd entity.name, containerImageDigest, containerImageName, workloadName, containerStatus, processes=contains[dt.entity.process_group_instance]



| expand dt.entity.process=processes



| fieldsRemove processes



| join [



fetch dt.entity.process_group_instance, from:now()-3h



], on:{left[dt.entity.process]==right[id]}, kind:leftOuter, fields:{releasesProduct, releasesStage}



], on:{left[container_image.digest]==right[containerImageDigest]}, kind:leftOuter,



fields:{container_instance.id=id, container_instance.name=entity.name, container_image.name=containerImageName,



releasesProduct, releasesStage, containerStatus}



// summarize and filter



| dedup {object.id, vulnerability.id, component.name, component.version,



container_image.registry, container_image.repository}, sort: {timestamp desc}



| parse containerStatus, """LD* "state=" LD:containerStatus ("}" | ",")"""



| fieldsAdd containerStatus=if(isNull(containerStatus),"not running",else:containerStatus)



| fieldsAdd releasesStage=if(isNull(releasesStage), "None", else:releasesStage)



| filter containerStatus=="running" AND releasesStage=="production"



// Aggregate vulnerability findings per vulnerability, repository,



// component and component version.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



record(



object.id = object.id,



event.provider = event.provider,



container_image.registry = container_image.registry,



container_image.repository = container_image.repository,



component.version = component.version,



component.name = component.name,



dt.security.risk.level = dt.security.risk.level,



ingest_time = timestamp



)



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



// Filter out, if this vulnerability for the repository and the component



// and version was already reported before the last 24 hours.



// For example, if the same vulnerability was reported multiple times



// during the last 7 days, don't report it again.



| filterOut iAny(vulnerability_finding_events[][ingest_time] < now() - 24h)



// Expand and deduplicate for repetitive findings if they



// were reported more than once in the last 24 hours.



| expand vulnerability_finding_events



| dedup { vulnerability.id, vulnerability.title, vulnerability_finding_events[object.id], vulnerability_finding_events[component.name], vulnerability_finding_events[component.version] }



// Aggregate again to count the unique affected images within each repository.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



vulnerability_finding_events



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



| sort vulnerability_finding_events[][ingest_time] desc
```

Example result:

![Example result](https://dt-cdn.net/images/2024-11-04-09-48-57-1764-c397b99b5c.png)

4. Track alert reduction

To track the alert reduction process based on the progressive filtering in [step 2](#filter)

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Container image alert reduction** for the Amazon ECR integration.

Example result:

![funnel dashboard showing alert reduction](https://dt-cdn.net/images/funnel-dashboard-4308-16c82e5aa3.png)


---


## Source: stay-compliant.md


---
title: Stay compliant with Security Posture Management
source: https://www.dynatrace.com/docs/secure/use-cases/stay-compliant
scraped: 2026-02-17T05:07:16.757027
---

# Stay compliant with Security Posture Management

# Stay compliant with Security Posture Management

* Latest Dynatrace
* Tutorial
* Published Dec 02, 2024

Early Adopter

In this tutorial you will learn how [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") can help you stay compliant with the [security hardening guidelines and regulatory compliance standards](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

## Target audience

This tutorial is dedicated to Security Ops Engineers, DevOps, DevSecOps, and Site Reliability Engineers (SREs).

## Scenario

* Your organization requires following Industry best practices or regulatory requirements.
* New workloads are constantly added or removed from your environment.

## Goal

* Gain immediate insight into the overall security posture of your monitored environment.
* Detect and address security issues and misconfigurations easily.
* Ensure your environment is configured securely and efficiently.
* Enhance the overall system reliability.
* Stay compliant with security standards.

## Result

* Kubernetes clusters are actively assessed through Kubernetes Security Posture Management against regulatory compliance standards and security best practices.
* Misconfigurations and violations against standards are continuously discovered.

## Prerequisites

* [Deploy Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")
* Install ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**

  1. Show me how

  1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
  2. Look for ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and select **Install**.

## Get started

1. Review results

Open [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.") ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") and review

* The [Assessment results](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.")
* The compliance status

  + [For the whole environment](/docs/secure/xspm/assess-coverage#standards "Review the Security Posture Management coverage of your systems at a glance.")
  + [For specific systems](/docs/secure/xspm/assess-coverage#systems "Review the Security Posture Management coverage of your systems at a glance.")

2. Search for relevant information

Use the [filtering and sorting](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.") options to gather insights about problems in your environment.

3. Gather insights

Define which rules are relevant [based on contextual insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").

4. Define compliance strategy

1. Fix configuration issues for [rules with the highest priority](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") in a narrow context (for example, on a single cluster).
2. Monitor compliance and operation for a while.
3. If everything works fine, roll out the fix to other environments.

5. Define monitoring for compliance

There are two ways:

In the app

Via DQL queries

Use ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** to monitor that

1. The [compliance standard percentage](/docs/secure/xspm/assess-coverage#standards "Review the Security Posture Management coverage of your systems at a glance.") is increasing.
2. The total number of assessed resources with the `Passed` result is increasing.

For easy management and to compare results, you can [download results as a CSV file](/docs/secure/xspm/share-findings#dwld "Interact with other apps for further insights and share results with stakeholders.").

Use [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to monitor

1. The history of results per standard or rule, per cluster or environment.
2. That the resource assessment result for a specific set of rules remains `Passed`.

   For a list of DQL examples based on compliance events that you can use, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

6. Create notifications

[Create a workflow](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.") to send an alert on your desired channel if the previously `Passed` rule turns into `Failed`.

## Further resources

[Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.")

[Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")

## Related topics

* [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.")


---


## Source: threat-hunting.md


---
title: Threat hunting and forensics
source: https://www.dynatrace.com/docs/secure/use-cases/threat-hunting
scraped: 2026-02-16T09:34:45.595381
---

# Threat hunting and forensics

# Threat hunting and forensics

* Latest Dynatrace
* Tutorial
* Published Mar 14, 2024

When threat hunting, time and precision are crucial. You need to be as fast and accurate as possible to find and act upon information. As a security analyst investigating security incidents or threat hunting, you often need to

* Navigate between multiple executed queries and their results
* Manage the evidence gathered during investigations and reuse it when building additional queries
* Ensure that

  + The investigation is maintained in context.
  + The tools for such activities support quick query creation and a detailed overview of the results.

In the following, we demonstrate how you can achieve these goals using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

## Target audience

This page is intended for Security teams performing threat hunting or analyzing security incidents, such as the Incident Response team or Security Analysts.

## Scenario

In the following, we address a scenario in which you get a notification from an external source about a suspiciously high number of unauthorized requests towards our Kubernetes control plane between `2024-02-13 16:00:00` and `2024-02-13 18:59:59`. Your Kubernetes cluster has been set up to AWS EKS cluster, and logs are forwarded to Dynatrace.

As a security analyst, you want to understand if this is related to malicious activities or if it may be an indication of a cyber security incident. During this investigation, you will follow the trail of your findings to illustrate the nature of threat hunting and incident solving.

## Prerequisites

* [Set up Kubernetes observability with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* Set up AWS logging to CloudWatch:

  + [Set up EKS Cluster loggingï»¿](https://dt-url.net/va038gi)
  + [Set up VPC Flow loggingï»¿](https://dt-url.net/ya238ol)
  + [Set up K8S DNS logging](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks/k8s-dns-logs "Learn how to ingest Kubernetes-related DNS logs from AWS to Dynatrace.")
* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Basic knowledge of

  + [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
  + [Dynatrace Pattern Language (DPL)](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")
  + How DNS name resolving works in Kubernetes clusters

## Investigation path 1: Analyze Kubernetes audit logs

First, you want to understand which activities caused the notification about the high number of unauthorized requests in your Kubernetes audit logs.
Open [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") and create a new investigation.

1. Set the timeframe

In the [timeframe section](/docs/secure/investigations/define-timeframes#selector "Adjust time ranges for data analysis and event correlation in Investigations."), set the timeframe from `2024-02-13 16:00:00` to `2024-02-13 18:59:59`, when the unauthorized requests occurred.

![set the timeframe](https://dt-cdn.net/images/2024-03-06-08-15-45-1914-2f0de669a4.png)

2. Fetch Kubernetes cluster audit logs

1. Kubernetes audit logs are forwarded to Dynatrace with `aws.log_group` and `log_stream` values attached. To fetch all the unique AWS CloudWatch log groups that are ingested to Dynatrace, copy-paste the following [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") in the query input.

   ```
   fetch logs



   | summarize count(), by: aws.log_group
   ```
2. Select **Run** to execute the query.

   ![fetch kubernetes cluster audit logs](https://dt-cdn.net/images/2024-03-06-08-45-30-1910-d1342717df.png)

   At this point, you notice a circle has appeared in the **Query tree** section in the upper right. This is called a root node and marks the starting point of your investigation. From here on, every time you modify and execute a query, a new node will be added in the query tree, allowing you to navigate among queries while keeping the history of your investigation intact. For details, see [query tree](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis.").

3. Filter by log group name

1. In the query results, find the record with the log group collecting the EKS control plane logs (in our example, `/aws/eks/unguard-secla-demo/cluster`) and [add it as a filter](/docs/secure/investigations#fields "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to your DQL query.

   ![Add a filter for the log group name](https://dt-cdn.net/images/2024-03-06-09-01-16-1530-51987a9960.png)
2. To view only the control plane audit events, modify the `filter` command in the query input by adding the [`and` operator](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") and the [`contains` string function](/docs/platform/grail/dynatrace-query-language/functions/string-functions#contains "A list of DQL string functions.") as follows:

   ```
   | filter aws.log_group == "/aws/eks/unguard-secla-demo/cluster" and contains(aws.log_stream, "audit")
   ```
3. In the query input, remove the `summarize` command and select **Run** to execute the query.

   ![view only the control plane audit events](https://dt-cdn.net/images/2024-03-06-09-19-12-1919-c2f0267459.png)

4. Inspect the content

In the query results table, right-click on any cell in the **content** field and select **View field details** to view the raw content of the field. For details, see [Explore data in the original format](/docs/secure/investigations/enhance-results#view-details "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

![Inspect the content](https://dt-cdn.net/images/2024-03-07-16-43-25-1546-aa18860a77.png)

5. Extract fields from JSON

1. In the query results table, right-click on any cell in the **Content** field and select [**Extract fields**](/docs/secure/investigations/extract-fields#field "Pull specific data points from logs in Investigations.") to navigate to [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.").
2. Select **Saved patterns**.
3. In **Dynatrace patterns**, select **k8s** > **audit**.

   ![extract field](https://dt-cdn.net/images/2024-03-06-18-41-50-1547-0df2e723b3.png)

   When extracting fields from a JSON structure, you can define only a partial schema for the fields that are relevant for your use case. To continue your investigation, you need to select only the relevant fields.
4. In the query input of DPL Architect, replace the pattern as follows:

   ```
   JSON{



   STRING:verb,



   JSON{string:username}(flat=true):user,



   JSON_ARRAY{ipaddr}(typed=true):sourceIPs,



   JSON{string+:resource}(flat=true):objectRef,



   JSON{int:code}(flat=true):responseStatus



   }(flat=true)
   ```
5. Select **Results** for an overview of the fields that will be extracted from the [match preview dataset](/docs/platform/grail/dynatrace-pattern-language/dpl-architect#match-preview "Extract fields with Dynatrace Pattern Language Architect.").

   ![display results](https://dt-cdn.net/images/2024-03-06-14-28-54-816-6ec66c1606.png)
6. Select **Insert pattern** to append the pattern to your DQL query.

   ![Insert pattern in DPL Architect](https://dt-cdn.net/images/2024-03-11-08-59-35-613-d01beb3deb.png)
7. Select **Run** to execute the query.

6. Filter events

To find out which IPs have unauthorized activity, you need to

* [Expand](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#expand "DQL structuring commands") the source IP array
* [Summarize](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") the results with the relevant fields extracted previously
* [Filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") the results to view only unauthorized requests (`401`) and forbidden requests (`403`)

1. In the query input, add the following DQL snippet, then select **Run** to execute the query.

   ```
   | expand sourceIPs



   | summarize count(), by: {sourceIPs, username, verb, resource=objectRef, responseStatus}



   | filter in(responseStatus, {401, 403})
   ```
2. In the results table menu, sort results by count to see which IP addresses had the most connections.

   ![filter the relevant events](https://dt-cdn.net/images/2024-03-07-08-11-17-1448-777bfa0c1e.png)

It looks like you found the origin of your security notification:

* An unauthorized external IP address is trying to fetch secrets from your control plane (in our example, `198.51.100.2`, with `401` response code and 122 connections). This is not surprising, since security scanners are attempting this daily from the internet.
* A private IP address is trying to enumerate pods repeatedly (in our example, `172.31.29.138`, with `403` response code and 2090 connections). It seems to be one of the pods in your Kubernetes cluster, and such behavior might indicate a compromised pod!

7. Add IPs as evidence

Both IP addresses need to be analyzed further, but the one with a `403` response and 2090 attempts is more critical and requires special attention.

To save the IPs as [evidence](/docs/secure/investigations/manage-evidence "Collect and preserve investigation artifacts in Investigations."), you can add the first IP (`198.51.100.2`) to a preset evidence list and the second one (`172.31.29.138`) to a new customized evidence list:

1. Right-click on `198.51.100.2`, then select **Add to evidence list** > **Suspicious IPs**.
2. Right-click on `172.31.29.138`, select **Add to evidence list** > **New evidence list** and enter a name, for example, "Suspicious pod".

   ![add to IP collections](https://dt-cdn.net/images/2024-03-07-08-32-32-357-51a8b2b145.png)

## Investigation path 2: Investigate potential target

To understand what the pod did and which other service logs you need for your investigation, you can start with the network logs. For AWS, the best place to start is the [VPC network flow logsï»¿](https://dt-url.net/6c0385l).

1. Fetch VPC flow logs

1. Using the [query tree](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis.") created during your investigation, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step.
2. In the query results, find the record with the log group that contains your VPC flow logs (in our example, `/aws/vpc/unguard-secla-demo/vpc-flow-logs`), and add it as a filter to the DQL query.

   ![VPC flow logs](https://dt-cdn.net/images/2024-03-06-16-11-40-1905-ed76689a2c.png)

   The node in the query tree has changed its icon, which means youâre in the middle of editing the query. You can either revert to the original query to update the results table or execute the modified query. When you run the modified query, a new node is created with the respective query and its results. You can [give the node a distinctive name and color](/docs/secure/investigations/query-tree "Visualize and structure complex queries in Investigations.") to recognize it later.
3. In the query input, remove the `summarize` command, then select **Run** to execute the modified query.

   ![execute modified query](https://dt-cdn.net/images/2024-03-07-18-21-06-1913-6f988f1771.png)

   This creates a second branch in the query tree. A branch is the visual representation of an investigation path. Let's see where this new path takes us.

2. Extract fields

For more accurate results, you need to extract fields from the log records with DPL Architect.

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **aws** > **vpc-flow-full**.
4. Select **Insert pattern**.
5. Select **Run** to execute the query.

3. Filter results

Since youâre interested only in the results from the suspicious pod, you can add a filter to your DQL query based on the evidence created in the [Add evidence for later use](#evidence) step.

1. Go to **Evidence lists** and select the evidence menu for the `Suspicious pod` list to see the filtering options and the suitable field names that match the `IPADDR` type.
2. Select **Filter for** > **Filter within field `pkt_srcaddr`**. This appends the filter to your DQL query.

   ![Filter by evidence](https://dt-cdn.net/images/2024-03-07-08-51-47-790-18cc53cc6c.png)
3. To get a better overview about the network connections, append the following command to the DQL query in the query input:

   ```
   | summarize count(), by: { pkt_dstaddr, protocol, action, dstport}



   | sort `count()` desc
   ```
4. Select **Run** to execute the query.

You can see that the suspicious pod has most often connected to the cluster's DNS service via UDP port 53.

![Better overview of network connections](https://dt-cdn.net/images/2024-03-07-09-20-38-1421-bf0a76a211.png)

There could be an application misconfiguration or something suspicious might be happening with that pod.

## Investigation path 3: Identify what data the pod sent out

To look for the DNS names resolved by a pod you need to check the CoreDNS logs. If configured properly, the query logs are visible in the CoreDNS container logs.

1. Fetch coreDNS logs

1. To fetch CoreDNS container logs, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step and modify the query in the query input as follows:

   ```
   fetch logs



   | filter k8s.container.name == "coredns"
   ```
2. Select **Run** to execute the query. This creates a third branch in the query tree.

   ![Fetch coreDNS logs](https://dt-cdn.net/images/2024-03-07-19-14-29-1919-bdcb4fef59.png)

2. Extract fields

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **k8s** > **coredns-query**.
4. Select **Insert pattern**.
5. Select **Run** to execute the query.

3. Filter results

To view only records containing the DNS requests originating from your suspicious pod, select the **source\_ip** column header, then select **Filter for** > **Suspicious pod**.

![Filter the source_ip field by the suspicious pod](https://dt-cdn.net/images/2024-03-07-09-52-47-539-9ece6d7f6f.png)

4. Extract domain name

There could be quite a lot of DNS requests in the results table. For a better understanding of the resolved hostnames, you need to extract the domain name portion from the name field and summarize results based on it.

1. In the query input, add the following snippet to the DQL query:

   ```
   | parse name, "ld* '.'? ( (ld '.' ld):domain '.' eos)"



   | summarize count = count(), by: {domain}
   ```
2. Select **Run** to execute the query.

   You notice that, besides internal or local domains, one suspicious domain (`tiitha-maliciousdomain.com`) is being resolved quite a lot!

   ![suspicious domain identified](https://dt-cdn.net/images/2024-03-07-10-01-49-503-598f18f1d7.png)

5. Add domain as evidence

1. In the query results table, right-click on the suspicious domain name, then select **Add to evidence list** > **New evidence list**.
2. Enter a name for your new evidence list, for example, **Attacker domain**.

   ![Add attacker domain as evidence](https://dt-cdn.net/images/2024-03-07-18-32-15-488-857db7fc3a.png)

6. Filter by attacker domain

1. In the query results table, select the cell with the suspicious domain, then select **Filter for** to add a filter to the query that fetches only requests that include the attacker domain.

   ![Filter for the malicious domain](https://dt-cdn.net/images/2024-03-07-10-17-10-1039-fc84720720.png)
2. In the query input, remove the `summarize` command and select **Run** to execute the query.

   It looks like there's some kind of data movement between the suspicious pod and the attacker domain. Looking at the query names and considering the number of queries, data appears to be extracted via DNS tunneling.

   ![data is being extracted via DNS tunnelling](https://dt-cdn.net/images/2024-03-07-10-24-01-1450-8d1cdc2027.png)

7. Analyze DNS requests

As there are thousands of DNS requests towards that particular domain, you may want to aggregate the data to determine how to proceed further.

1. In the query results, select the **type** column header, then select [**Summarize**](/docs/secure/investigations/enhance-results#aggregate "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").
2. Select **Run** to execute the query.

   ![Summarize by type](https://dt-cdn.net/images/2024-03-07-10-40-41-399-c7c4bf8285.png)

   You notice many A, AAAA, and TXT requests from the pod. You start investigating the A requests.
3. In the query results table, right-click on an **A** cell and select **Filter for** to add a filter to the DQL query.
4. In the query input, remove the `summarize` command and select **Run** to execute the query.

   To determine what is being sent out, you need to extract the subdomain portion of the domain. For this, you need to analyze one of the DNS queries that is resolving the attacker domain.
5. Double-click on any cell in the query results table.
6. In the **Details (â¦)** window, check the data in the **name** field.

   It seems that the DNS name is structured by an ID followed by the payload portion encoded in hex, and these parts are delimited by `.`.

   ![Inspect the name](https://dt-cdn.net/images/2024-03-07-11-09-13-997-28d0d5a17a.png)
7. To parse and decode the payload, add the following DQL snippet to the DQL query:

   ```
   | parse name, """ld:id '.' ld:payload '.tiitha-maliciousdomain'"""



   | fieldsAdd payload=replaceString(payload,".","")



   | fields timestamp, id, payload=decodeBase16ToString(payload)



   | sort timestamp, id
   ```

   The result proves that data from your pod is definitely being extracted and sent out!

   ![data from pod is extracted and sent out](https://dt-cdn.net/images/2024-03-07-11-11-40-1106-e7433155ee.png)

## Investigation path 4: Find out how the commands were sent to the pod

You know for sure the pod is sending information to an external DNS server, but you havenât figured out how it gets the commands. Since TXT-type DNS queries enable larger responses and are sometimes used for malicious transactions as well, you need to take a look at those requests. Since CoreDNS records don't contain the response payload, you turn to Route53 logs.

1. Analyze TXT records

1. Using the query tree, navigate to the [Fetch Kubernetes cluster audit logs](#fetch-k8s-logs) step.
2. In the query results, find the record with your Route53 log group (in our example, `/aws/route53/unguard-secla-demo/resolver-logs`) and add it as a filter to your DQL query.
3. In the query input, remove the `summarize` command and select **Run** to execute the query. This creates a fourth branch in the query tree.

   ![Analyze TXT records](https://dt-cdn.net/images/2024-03-07-18-55-59-1919-a0b7fff314.png)

2. Extract fields from log records

1. In the query results table, right-click on any cell in the **content** field and select **Extract fields**.
2. In DPL Architect, select **Saved patterns**.
3. In **Dynatrace patterns**, select **aws** > **route53-query**.
4. You need to extract the `query_name`, `query_type`, `srcaddr`, and `answers` values from the log record. In the query input, you can replace the pattern as follows:

   ```
   json{



   string:query_name,



   string:query_type,



   json_array:answers,



   ipaddr:srcaddr



   }(flat=true)
   ```
5. Select **Insert pattern**.
6. Select **Run** to execute the query.

3. Filter data

1. In the query results, select the `query_name` column header, then select **Filter for** > **Attacker domain**.
2. Select **Run** to execute the query.

   You only care about the queries with the TXT type, so you can append the filter with the appropriate expression. Since the answers portion is an array, expand the field so that each value in the array is a separate record. The only fields you need are `srcaddr`, `query_name`, and the `Rdata` element from the answer object.
3. In the query input, modify the `filter` command by adding the following snippet:

   ```
   | filter endsWith(query_name, "tiitha-maliciousdomain.com.") and query_type == "TXT"



   | expand answers



   | fields srcaddr, uery_name, answer=answers[Rdata]
   ```
4. Select **Run** to execute the query.

   Your hypothesis is correct: the TXT DNS queries were used to fetch the commands. The executed commands (including the Kubernetes control plane requests as curl commands) show up as responses in your DNS logs!

   ![Correct hypothesis: TXT DNS queries were used to fetch the commands](https://dt-cdn.net/images/2024-03-07-19-02-39-1919-08659833f4.png)

## Conclusion

You've found out what happened but haven't figured out what else the pod has done, what process or activity is triggering the DNS requests, who controls the data extraction, how and when the pod was infected, and other relevant aspects of a security incident.

From here on, the complexity of the investigation will only grow, and the ability to navigate between different stages of an investigation is even more crucial. All these questions might trigger a new branch in the query tree, if not a separate investigation. Our investigation introduces many additional questions that require answers.

## Related topics

* [Analyze AWS CloudTrail logs with Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Analyze Amazon API Gateway access logs with Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Detect threats against your AWS Secrets with Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Resolve incidents faster with Investigations templates](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")
* [Operationalize DQL query results with Investigations](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")


---


## Source: visualize-and-analyze-security-findings.md


---
title: Visualize and analyze security findings
source: https://www.dynatrace.com/docs/secure/use-cases/visualize-and-analyze-security-findings
scraped: 2026-02-16T21:21:56.163251
---

# Visualize and analyze security findings

# Visualize and analyze security findings

* Latest Dynatrace
* Tutorial
* Updated on Oct 07, 2025

Organizations use multiple security products and tools that generate security findings in various data formats. Accessing the data in a siloed approach makes the life of security analysts hard, as they must spend a lot of manual effort generating a combined security posture picture.

In this context, you can

* Ingest security findings from your security tools (see [Security integrations](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.")) or vulnerability finding events from Dynatrace-monitored processes (see [Third-party library events](/docs/secure/vulnerabilities/concepts#tpv-events "Concepts that are specific to the Dynatrace Vulnerabilities app.")) and map them to the [Dynatrace Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0), which makes events from different tools uniformly accessible with DQL.
* View and analyze security findings across products and tools with our dashboards, which can also be a good foundation for tailoring further visual customization to meet your organization's posture analysis and reporting requirements.
* [Query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") ingested data in our dedicated apps.

## Target audience

Security analysts and managers responsible for analyzing and reporting the organization's security posture.

Key use cases include:

* Gaining a unified view of all the security findings
* Prioritizing security findings across products
* Identifying top affected assets

## Prerequisites

Depending on the ingestion source, follow the appropriate setup:

* **Third-party security products**: [Set up a supported integration](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
* **Dynatrace-monitored environments**: [Enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to ingest vulnerability finding events from third-party libraries.

## Get started

1. Visualize

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.

   Ready-made dashboards are available for third-party tool integrations. Vulnerability finding events from Dynatrace-monitored environments are accessible via DQL but aren't currently included in those dashboards.
2. Search for and select **Security findings** for the desired integration.

Example result:

![dashboard sample result](https://dt-cdn.net/images/2025-05-07-15-06-056-1903-93aa46287c.png)

2. Analyze

Open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to [query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") ingested data, using the data format in [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0).

For a better understanding of how to build your queries, see [DQL query examples for ingested events](/docs/secure/threat-observability/dql-examples#ingested "DQL examples for security data powered by Grail.").


---
