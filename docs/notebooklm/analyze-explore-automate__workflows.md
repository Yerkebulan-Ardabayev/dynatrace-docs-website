# Dynatrace Documentation: analyze-explore-automate/workflows

Generated: 2026-02-16

Files combined: 20

---


## Source: email.md


---
title: Email
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/email
scraped: 2026-02-15T21:30:29.145746
---

# Email

# Email

* Latest Dynatrace
* 3-min read
* Updated on Feb 05, 2026

You can automate sending out-of-the-box emails using Email ![Email for Workflows](https://dt-cdn.net/images/email-for-workflows-new-256-f6c0e2d343.png "Email for Workflows") based on the events and schedules defined by your [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

## Grant permissions to Workflows

Workflows require certain permissions to run actions on your behalf. Other permissions are required by actions that come bundled with Email.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and go to **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * Permissions needed for **Send email** actions

     + `email:emails:send`

For more on general Workflows user permissions, see [Expression reference](/docs/analyze-explore-automate/workflows/reference#user-permission "Get to know the workflows expression").

Trial environments are prohibited to send emails with **Email**.

## Send an email with workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select **![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") Workflow** to create a new workflow.
2. Select the **Trigger** to choose the right trigger for your needs.
3. In the side panel, select one of the triggers.
4. On the trigger node, select **Add task** ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
5. In the side panel, search the actions for **Email** and select **Send email**.
6. In **To** field, enter the email addresses of the recipients. The **Cc**, **Bcc** fields, are also available. For **To**, **Cc**, and **Bcc** fields the number of email addresses is restricted to 10 per field.
7. In **Subject** and **Message** fields, enter a meaningful text.
8. Select **Run**.

Email sends emails from `no-reply@apps.dynatrace.com` email address. We recommend whitelisting the domain to avoid emails being redirected to the junk folder.

## Format email

To format the body of an email

1. Select **Message**.
2. Enter your text.

   When you select, for example, the bold style, your text is rendered as bold in the sent email.
   You won't be able to preview it without the formatting symbols.
   However, when you send an email, the recipient will see the properly formatted text, and the formatting symbols won't be visible.

   You can use the toolbar to insert common elements like a heading, bold text, or a link.

   Attaching an image or inserting JavaScript code into the email body is impossible. It's just shown as plain text.

   ![Screenshot of a workflow with an email action where the email body text can be formatted.](https://dt-cdn.net/images/umsaywsjuo-dev-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-new-view-draft-task-send-email-3754-473a3b4d5b.png)

## Format syntax

### Italics

Wrap text in single asterisks (`*like this*`) to get italics *like this*.

### Bold

Wrap text in double asterisks (`**like this**`) to get bold text **like this**.

### Strikethrough

Wrap text in double tildes (~~like this~~) to get strikethrough (crossed out) text ~~like this~~.

### Code

* Wrap text in backticks (`like this`) to get bold text `like this`.
* Wrap text in triple backticks (```like this```) to show a code block (multiple lines of `code text`).

### Headings

To add a heading, start the line with the `#` character like this: `# This is your heading text`.

### Horizontal line

To visually separate sections of your annotation, add a horizontal line with three dashes (`---`):

### Lists

Each line of an unordered (bulleted) list starts with an asterisk (`*`):

```
* Line 1



* Line 2
```

Alternatively, you can use a dash (`-`):

```
- Line 1



- Line 2
```

An ordered (numbered) list starts with a number and a period (`1.`) followed by a space and then your text:

```
1. The first line of my procedure.



2. The second line of my procedure.



3. The third line of my procedure.
```

### Tables

To add a table, define the headers, the column formatting row, and then the rows of data you want to display

```
| Header 1 | Header2



--- | ---



content2 | content2
```

| Header 1 | Header2 |
| --- | --- |
| content2 | content2 |

### Links

To link to a website, use this format:

`[Example text label](https://www.example.com)`

```
Here's a link to the [Dynatrace website](www.dynatrace.com).
```

When using markdown links in email messages, only certain protocols are supported and are transformed to HTML links:

* `http`
* `https`
* `ftp`
* `ftps`
* `mailto`
* `tel`
* `sms`

Unsupported link protocols

Links using unsupported protocols (such as `file://`) aren't transformed from markdown to HTML links and remain plain text. Depending on your email client, these links might still be highlighted or rendered as clickable links by the client itself.

### Line break

To add a single line break and a new line, select **Enter** in the **Message** field of the Connector.

No HTML support

This Connector only allows formatting of the message body using the listed formatting options. It doesn't offer support for HTML.

Email formatting is disabled for messages with a size greater than or equal to 256 KiB.

## Inputs

| Field | Description | Required |
| --- | --- | --- |
| **To** | The recipients of the email. | Required |
| **Cc** | The cc recipients of the email. | Required |
| **Bcc** | The bcc recipients of the email. | Required |
| **Subject** | The subject of the email. | Required |
| **Content** | The content of the email. | Required |

You must enter at least one and a maximum of ten recipients in one of the fields (to, cc, bcc).
If you are using [expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") for the recipients, the expressions must be evaluated as a list of email addresses, for example, `["user1@domain.com", "user2@domain.com"]`.

## Action result

The **Send email** action provides the following result.

Property

Description

`requestId`

A unique identifier to trace successfully accepted email send requests.

`clientRequestId`

A unique identifier to trace successfully accepted email send requests. For sending emails, this is identical to `requestId`.

## Expected behavior 'Failed to send email. Status code 403.'

Failed to send email. Status code 403.

This message is related to missing permissions or a trial environment as described above in [Grant permissions to Workflows](#permissions).

### Sending JSON payloads as message content

When sending an object or non-string data as message content, ensure it is properly formatted as a string.
The recommended approach is to wrap your input in an expression and convert it to a JSON string using the `to_json` filter:

```
{{ result("run_javascript_1") | to_json }}
```

This approach ensures your data is properly formatted for transmission. For more information, see [Expression reference](/docs/analyze-explore-automate/workflows/reference#any-object "Get to know the workflows expression").

The message size is limited to 256 KiB. Larger payloads will result in an action failure.

## Related topics

* [Send email notifications for problems](/docs/analyze-explore-automate/workflows/use-cases/workflows-tutorial-problems-email "Learn how to send email notifications for problems using a simple workflow.")


---


## Source: github-workflows-actions.md


---
title: Actions for GitHub Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/github/github-workflows-actions
scraped: 2026-02-15T09:09:19.331883
---

# Actions for GitHub Connector

# Actions for GitHub Connector

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jan 27, 2025

This page contains Github workflow actions that are available for the GitHub Connector ![GitHub](https://dt-cdn.net/images/github-for-workflows-new-lxjn9po-256-94579b3812.png "GitHub") integration.

### Required token permissions to run all GitHub actions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Contents > Read and write.

Select Repository permissions > Pull requests > Read and write.

Select Repository permissions > Workflows > Read and write.

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Actions > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Contents > Read and write.

Select Repository permissions > Pull requests > Read and write.

Select Repository permissions > Workflows > Read and write.

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Actions > Read and write.

**Token (classic)**

public

Select scopes > repo > public\_repo.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Get content

The **Get content** action returns the content of an existing file in the repository.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **File path** | The file path to a single, existing file. A directory path is not supported. | Required |
| **Reference** | The name of the commit, branch or tag. If not set, the repository's default branch is used. | Optional |

### Output

The action returns the `content` property that contains the plain text content of an existing file in the repository.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

No additional permissions are required.

**Fine-grained personal access token**

private

Select Repository permissions > Contents > Read only.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Create or replace file

The **Create or replace file** action creates a new file with the specified content or replaces an existing one. Next, it commits the change to a newly created branch using the specified source branch or the specified existing branch.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Create new branch** | Select this option if you want the change to be made in a new branch. | Optional |
| **Commit to an existing branch** | Select this option if you're going to use an existing branch for the change. | Optional |
| **Source branch** | The source branch on which the new branch is based. For example: `main`. | Optional |
| **Branch** | The new or existing branch you want to commit to. | Required |
| **File path** | The relative path to the file. A directory path is not supported. Existing files will be overwritten. | Required |
| **File content** | The full content of the file. Existing files will be overwritten. | Required |
| **Commit message** | The git commit message for the change. | Required |

### Output

The action returns the `fileMetadata` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Contents > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Contents > Read and write.

Select Repository permissions > Workflows > Read and write. (required to modify GitHub workflow files)

**Token (classic)**

public

Select scopes > repo > public\_repo.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Delete file

The **Delete file** action deletes an existing file in the repository and commits the change to either a newly created branch using the specified source branch as a basis or uses the specified existing branch.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Create new branch** | Select this option if you want the file deletion to be made in a new branch. | Optional |
| **Commit to an existing branch** | Select this option if you're going to use an existing branch for the change. | Optional |
| **Source branch** | The source branch on which the new branch is based, for instance, "main". | Optional |
| **Branch** | The new or existing branch you want to commit to. | Required |
| **File path** | The relative path to the file to be deleted. A directory path is not supported. | Required |
| **Commit message** | The git commit message for the change. | Required |

### Output

The action returns the `fileMetadata` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Contents > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Contents > Read and write.

**Token (classic)**

public

Select scopes > repo > public\_repo.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Create pull request

The **Create pull request** action creates a pull request for an existing branch and the specified target branch. For example: `main`.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the .git extension. The name is not case-sensitive. | Required |
| **Source branch** | The source branch where the changes are implemented. | Required |
| **Target branch** | The target branch you want the changes to be pulled into. | Required |
| **Pull request title** | The title of the pull request. | Required |
| **Pull request description** | The description of the pull request. | Optional |

### Output

The action returns the `pullRequest` property that contains the full response of the corresponding GitHub API endpoint.

### Required permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Pull requests > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Pull requests > Read and write.

**Token (classic)**

public

Select scopes > repo > public\_repo.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Get pull request

The **Get pull request** action returns details about the specified pull request.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Pull request number** | The number that identifies the pull request. | Required |

### Output

The action returns the `pullRequest` property that contains the full response of the corresponding GitHub API endpoint.

### Required permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

No additional permissions are required.

**Fine-grained personal access token**

private

Select Repository permissions > Pull requests > Read-only.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control) of private repositories.

## List pull requests

The **List pull requests** action returns a list of pull requests that match the specified criteria. The limit of 30 pull requests applies.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **State** | The state of pull requests you're interested in (open, closed, all). | Optional |

### Output

The action returns the `pullRequest` property that contains the full response of the corresponding GitHub API endpoint.

### Required permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

No additional permissions are required.

**Fine-grained personal access token**

private

Select Repository permissions > Pull requests > Read-only.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Merge pull request

The **Merge pull request** action merges the specified pull request.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Pull request number** | The number that identifies the pull request. | Required |
| **Merge Method** | The merge method to use. | Optional |

### Output

The action returns the `mergeStatus` property that contains the full response of the corresponding GitHub API endpoint.

### Required permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Contents > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Contents > Read and write.

**Token (classic)**

public

Select scopes > repo > public\_repo.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Create issue

The **Create issue** action creates a new issue in a specified repository.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Issue Title** | The title of the issue to be created. | Required |
| **Description** | The description or body of the issue. | Optional |
| **Assignees** | A list of usernames to assign to the issue. | Optional |
| **Labels** | A list of labels to associate with the issue. | Optional |

### Output

The action returns the `issue` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Issues > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Issues > Read and write.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Update issue

The **Update issue** action updates an existing issue in a specified repository. Use the **Add Field** option to specify fields for updates.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Issue Number** | The number of the issue to be updated. | Required |
| **Title** | The new title of the issue. Displayed only after the field is added. Leaving the added field empty updates it with an empty value. | Optional |
| **Description** | The new description or body of the issue. Displayed only after the field is added. Leaving the added field empty updates it with an empty value. | Optional |
| **State** | The new state of the issue. Displayed only after the field is added. Leaving the added field empty updates it with an empty value. | Optional |
| **Assignees** | The new list of usernames to assign to the issue. Displayed only after the field is added. Leaving the added field empty updates it with an empty value. | Optional |
| **Labels** | The new list of labels to associate with the issue. Displayed only after the field is added. Leaving the added field empty updates it with an empty value. | Optional |

### Output

The action returns the `issue` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Pull requests > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Pull requests > Read and write.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Create comment

The **Create comment** action creates a new comment on an issue or pull request in a specified repository.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Issue or pull request ID** | The ID of the issue or pull request to which the comment will be added. | Required |
| **Content** | The content of the comment to be created. | Required |

### Output

The action returns the `comment` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Pull requests > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Issues > Read and write.

Select Repository permissions > Pull requests > Read and write.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Trigger workflow run

The **Trigger workflow run** action triggers a workflow in a specified repository. The workflow must be configured to run on the `workflow_dispatch` event. If the workflow calls reuseable workflows from other private repositories, you can make them accessible in **Settings** > **Actions** > **General** > **Access** on GitHub.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Workflow** | The ID of the workflow or the workflow file name including the `.yml` or `.yaml` extension. | Required |
| **Reference** | The name of the branch or tag for the workflow. For example: `main`. | Required |
| **Inputs** | Key-value pairs of input parameters to pass to the workflow in JSON format. | Optional |

### Output

The action returns no result.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Actions > Read and write.

**Fine-grained personal access token**

private

Select Repository permissions > Actions > Read and write.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Get latest workflow run

The **Get latest workflow run** action retrieves data from the latest run workflow in a specified repository.

### Input

| Field | Description | Required |
| --- | --- | --- |
| **Connection** | [Connection](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup#connection "Learn how to set up GitHub Connector.") to your GitHub environment. | Required |
| **Owner** | Account owner of the repository (private user or organization). | Required |
| **Repository** | The name of the repository without the `.git` extension. The name is not case-sensitive. | Required |
| **Workflow** | The ID of the workflow or the workflow file name including the `.yml` or `.yaml` extension. | Required |
| **Branch** | The name of the branch or tag. For example: `main`. | Optional |

### Output

The action returns the `workflowRun` property that contains the full response of the corresponding GitHub API endpoint.

### Required token permissions

Token type

Repository type

Permissions

**Fine-grained personal access token**

public

Select Repository permissions > Actions > Read.

**Fine-grained personal access token**

private

Select Repository permissions > Actions > Read.

**Token (classic)**

public

No additional permissions are required.

**Token (classic)**

private

Select scopes > repo (Full control of private repositories).

## Related topics

* [Set up GitHub Connector](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup "Learn how to set up GitHub Connector.")


---


## Source: github-workflows-setup.md


---
title: Set up GitHub Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup
scraped: 2026-02-15T21:26:55.238458
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


---


## Source: gitlab-workflows-setup.md


---
title: Set up GitLab Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-setup
scraped: 2026-02-15T09:11:50.139815
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


---


## Source: gitlab.md


---
title: GitLab Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/gitlab
scraped: 2026-02-15T21:26:21.861314
---

# GitLab Connector

# GitLab Connector

* Latest Dynatrace
* Overview
* 1-min read
* Published Aug 23, 2024

GitLab Connector ![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows") enables your Dynatrace environment to integrate with GitLab projects. With this integration, you can automate issues and merge requests based on monitoring data and events defined in a dedicated [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

[![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows")

### Set up GitLab Connector

Set up and configure GitLab.](/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-setup "Set up GitLab Connector.")[![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows")

### Actions in GitLab Connector

Learn about available actions used by GitLab Connector integration for automating issues and merge requests on your monitoring data and events.](/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-actions "List of available actions in GitLab Connector.")


---


## Source: jira.md


---
title: Jira Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/jira
scraped: 2026-02-15T21:28:18.766756
---

# Jira Connector

# Jira Connector

* Latest Dynatrace
* Overview
* 1-min read
* Updated on Feb 13, 2025

Your Dynatrace environment can integrate with a Jira Cloud or Server instance using Jira Connector ![Jira for Workflows](https://dt-cdn.net/images/jira-for-workflows-lm8hkkp-257-bfed74a746.png "Jira for Workflows"). With this integration, you can automate creating, commenting, and assigning Jira issues on the events and schedules defined for your [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

[![Jira for Workflows](https://dt-cdn.net/images/jira-for-workflows-lm8hkkp-257-bfed74a746.png "Jira for Workflows")

### Jira Connector Get Started

Get started with our Quick Start Guide for Jira Connector.](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-get-started "Learn how to get started with Jira Connector actions.")[![Jira for Workflows](https://dt-cdn.net/images/jira-for-workflows-lm8hkkp-257-bfed74a746.png "Jira for Workflows")

### Set up Jira Connector

Set up and configure Jira Connector.](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-setup "Learn how to set up Jira Connector.")[![Jira for Workflows](https://dt-cdn.net/images/jira-for-workflows-lm8hkkp-257-bfed74a746.png "Jira for Workflows")

### Jira Connector actions

Learn about available actions used by Jira Connector integration for automating issue creation.](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-actions "Integrate with the Jira instance to utilize a wide range of Jira Connector actions.")

## Troubleshooting

The following are solutions to problems some people had with Jira Connector actions.

* [Invalid connection error in Jira Connectorï»¿](https://dt-url.net/86238jw)
* [Insufficient permissions error in Jira Connectorï»¿](https://dt-url.net/ix2388q)
* [Why does Jira ticket creation fail for Jira Connector?ï»¿](https://dt-url.net/ru038v6)

## Related topics

* [Set up Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-setup "Learn how to set up Jira Connector.")
* [Get started with Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-get-started "Learn how to get started with Jira Connector actions.")
* [Actions for Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira/automation-workflows-jira-actions "Integrate with the Jira instance to utilize a wide range of Jira Connector actions.")


---


## Source: microsoft-entra-id.md


---
title: Microsoft Entra ID Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id
scraped: 2026-02-15T21:23:18.603511
---

# Microsoft Entra ID Connector

# Microsoft Entra ID Connector

* Latest Dynatrace
* 5-min read
* Updated on Jun 18, 2025

Your Dynatrace environment can integrate with Microsoft Entra ID (formerly Azure Active Directory) in automation [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").
Microsoft Entra ID Connector ![Azure Connector](https://dt-cdn.net/images/azure-for-workflows-lcgzeur-256-0e765fdb69.png "Azure Connector") enables you to use prebuilt actions in Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") to automate importing teams from Entra ID (based on various triggers) for defining entity ownership and other use cases in Dynatrace.
Microsoft Entra ID Connector connects to the Azure Cloud via the [Microsoft Graph APIï»¿](https://developer.microsoft.com/en-us/graph).

## Setup

1. Allow External Requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

You need to add these domain names `login.microsoftonline.com` and `graph.microsoft.com`.

2. Grant permissions to Workflows

Workflows requires some permissions to run actions on your behalf. Actions that come bundled with the Connector require other permissions.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and go to **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * `app-settings:objects:read`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

3. Set up integration with Dynatrace

Configure your Microsoft Azure tenant to establish a connection with your Dynatrace environment.

1. Open `portal.azure.com` to access your Microsoft Azure tenant.
2. Navigate to **App registrations** to set up a new application.

   For the necessary setup steps, see [Register a client application in Azure Active Directoryï»¿](https://dt-url.net/3w239qt).
3. Grant your newly created Azure application the `Group.Read.All` permission.

   For more information, see [API Permissionsï»¿](https://dt-url.net/v8439p2) and [Introduction to permissions and consentï»¿](https://dt-url.net/7g639wa).
4. After registering the app, create a new client secret. For details, see [Certificates & secretsï»¿](https://dt-url.net/bt839gp).

   * To create a client secret, make sure that you either have admin permissions or are part of the app owners.
   * Make sure you store the client secret **Value** (not the **Secret ID**) after creation for establishing the connection to your Dynatrace environment later.

4. Authorize connection

Microsoft Entra ID Connector requires a client secret from Microsoft Azure for authorization.

1. Get the following credentials from your application registration in your Microsoft Azure tenant on `portal.azure.com`.

   * Directory (tenant) ID: Available in the **Overview** menu
   * Application (client) ID: Available in the **Overview** menu
   * Client secret: The **Value** (not the **Secret ID**) of the client secret from the preceding [Set up Microsoft Azure for integration with Dynatrace](#set-up-azure) section
2. Return to Dynatrace, go to **Settings** ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") > **Connections** > **Microsoft Entra ID**.
3. Select **Add item** and provide the following information.

   * **Connection name**: Needs to be unique. It will be listed and selectable in the connection field in Microsoft Entra ID Connector.
   * **Directory (tenant) ID**
   * **Application (client) ID**
   * **Type**: `Client secret`
   * **Client Secret**: This is the **Value** of the client secret from the [Set up Microsoft Azure for integration with Dynatrace](#set-up-azure) section.
4. Select **Create**.

#### Additional notes

* To add connection settings, you need the following permissions.

  ```
  ALLOW settings:objects:read, settings:objects:write, settings:schemas:read WHERE settings:schemaId = "app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection"
  ```

  For details, see [Permissions and access](/docs/manage/settings/settings-20#permissions-and-access "Introduction to the Settings 2.0 framework").

## Get groups from Entra ID in automation workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow** in the upper-right corner of the page.
2. In the side panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. In the **Choose action** side panel, search for **Microsoft Entra ID** and select **Get groups**.
5. In the action **Input**, you can target specific groups in **$filter** if you wish to filter your results. Likewise, in **$select**, specify which fields you wish to get from Entra ID. The syntax is based on [Entra ID API documentationï»¿](https://dt-url.net/azure-api-docs).

   Important for importing Entra ID groups as [ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership."):

   * You always need to include `id` and `displayName` in `$select`; these fields are mapped to the imported ownership team's **Team identifier** and **Team name**, respectively.
   * We recommend that you always include the `mailNickname` parameter in `get_groups`. This field has unique values in Entra ID and is set as a unique, human-readable **Supplementary Identifier** for your imported ownership team within Dynatrace.
   * The **Object Id** from Entra ID, imported via the `id` parameter, is set as the unique **Team identifier** as well as the **External ID** of the imported ownership team.
   * The `mail` parameter is set as the **Email** of the imported ownership team.

   ![Get groups input fields](https://dt-cdn.net/images/azure-connector-get-groups-input-698-0609c7d9dc.webp)
6. Optionally, insert the **Import teams** action (provided by the [Ownership app](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information.") ![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership")) to store Entra ID group information as [ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") within Dynatrace **Settings**. You can then [assign these imported teams as owners](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") to any monitored entity in Dynatrace.
7. To test your workflow, select **Run**.

### Action result

The result of `get_groups` is a JSON array with each record consisting of a single user group. If **$count** is set to `true` when configuring the action, the **Results** panel shows a count of imported groups.

The `directory_id` displayed in the results is the Azure tenant ID.

The log of a successful run is shown below.

```
[INFO]    Successfully retrieved connection settings.



[INFO]    Successfully fetched authentication token.



[INFO]    Calling Entra-ID groups endpoint with the following query params: $filter=startswith(displayName, 'team-deco')&$select=id,displayName,description,mail,mailNickname&$count=true&$top=999



[INFO]    Successfully fetched Groups from Entra-ID.
```


---


## Source: pagerduty.md


---
title: PagerDuty
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/pagerduty
scraped: 2026-02-15T21:22:46.035361
---

# PagerDuty

# PagerDuty

* Latest Dynatrace
* 5-min read
* Updated on May 07, 2025

Your Dynatrace environment can integrate with a PagerDuty environment using PagerDuty Connector ![PagerDuty](https://dt-cdn.net/images/pagerduty-for-workflows-257-0cd4ce0d3a.png "PagerDuty"), enabling you to create incidents, based on your monitoring data automatically.

## Configure the integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Grant permissions to Workflows**](/docs/analyze-explore-automate/workflows/actions/pagerduty#permissions "Automate creation of incidents in PagerDuty based on your monitoring data and events.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create PagerDuty API key**](/docs/analyze-explore-automate/workflows/actions/pagerduty#api-key "Automate creation of incidents in PagerDuty based on your monitoring data and events.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure PagerDuty connection**](/docs/analyze-explore-automate/workflows/actions/pagerduty#connection "Automate creation of incidents in PagerDuty based on your monitoring data and events.")

### Step 1 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf. Other permissions are required by actions that come bundled with PagerDuty Connector itself.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * `app-settings:objects:read`
   * `state:app-states:read`
   * `state:app-states:write`
   * `state:app-states:delete`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 2 Create PagerDuty API key

To interact with PagerDuty, you need an API key. To learn how to obtain it, refer to the [PagerDuty official documentationï»¿](https://dt-url.net/jo03j4l).

### Step 3 Configure PagerDuty connection

You need a configured connection for each of your PagerDuty environments.

To configure a connection

1. Go to **Settings** and select **Connections** > **Connectors** > **PagerDuty**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
3. Provide a meaningful name for your connection.
4. If needed, adapt the URL of the PagerDuty API.
5. Provide your PagerDuty API key.
6. Select **Create**.

## Available actions

The following workflow actions are available for the PagerDuty integration. Each action corresponds to an endpoint of the PagerDuty API.

Action

Description

PagerDuty API endpoint

Create an incident

Creates an incident in your PagerDuty environment. An incident represents a problem or an issue that needs to be addressed and resolved.

Use other actions to obtain the necessary input.

[Create an incidentï»¿](https://dt-url.net/b723jjs)

List all of the on-calls

Lists all PagerDuty users who are on call duty.

[List all of the on-callsï»¿](https://dt-url.net/4t43jm9)

List escalation policies

Lists PagerDuty escalation policies. An escalation policy defines who to notify (and how) in case of an incident.

[List escalation policiesï»¿](https://dt-url.net/qo63j74)

List priorities

Lists PagerDuty priorities. A priority defines the importance of an incident. The list is ordered from the most to the least severe.

[List prioritiesï»¿](https://dt-url.net/ow83jrh)

List services

Lists PagerDuty services. A service represents an application, component, or team to which you want to map the incident.

[List servicesï»¿](https://dt-url.net/0b03jpm)

List users

List all users of your PagerDuty environment.

[List usersï»¿](https://dt-url.net/ee23j45)

## Create a PagerDuty incident

To create an incident, you need to provide the information listed below. You can hard-code them in the **Create an incident** action or extract them from PagerDuty via an appropriate action.

| Field | Description | Required |
| --- | --- | --- |
| From | The ID of the user who creates the incident | Required |
| Title | The incident title | Required |
| Service ID | The ID of the service in your PagerDuty environment | Required |
| Urgency | The urgency of the incident | Optional |
| Additional incident details | A description of the incident | Optional |
| Assignee ID | The ID of the incident assignee | Optional |
| Escalation policy ID | The ID of the escalation policy | Optional |
| Conference number | The phone number of the conference call for the conference bridge | Optional |
| Conference URL | The URL for the conference bridge, such as a link to a web conference or Slack channel | Optional |
| Incident key | A unique identifier for this incident. For most use cases this is the Dynatrace event ID. | Optional |

For more details on each parameter, refer to [Create an incidentï»¿](https://dt-url.net/b723jjs) in the PagerDuty official documentation.

To create a workflow that raises a PagerDuty incident

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to create a new workflow.
2. In the **Choose trigger** panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. Optional In the **Choose action** panel, search for `PagerDuty` and select one of the information-extracting actions.
5. Optional If needed, add more information-extracting actions. Be sure to put them in parallel.
6. On one of the information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), search for `PagerDuty`, and select **Create an incident**.
7. On each of the remaining information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") and drag the line to the **Create an incident** action.
8. In the **Create an incident** action, select the [connection](#connection) to your PagerDuty environment.
9. Configure the input fields as needed. To learn how to use the output of information-extracting notes, see [Expression reference](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression").
10. To test your workflow, select **Run**.

## Troubleshooting

The following are solutions to problems some people have.

* [PagerDuty: Missing required fields errorï»¿](https://dt-url.net/gt038mx)
* [PagerDuty: Insufficient permissions errorï»¿](https://dt-url.net/2e23837)


---


## Source: service-now.md


---
title: ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/service-now
scraped: 2026-02-15T21:18:23.623731
---

# ServiceNow

# ServiceNow

* Latest Dynatrace
* 7-min read
* Updated on Nov 18, 2025

Your Dynatrace environment can integrate with a ServiceNow environment using ServiceNow Connector ![ServiceNow for Workflows](https://dt-cdn.net/images/servicenow-for-workflows-257-9349ea0329.png "ServiceNow for Workflows"), enabling you to create incidents based on your monitoring data and events automatically.
Furthermore, you can retrieve groups from ServiceNow and import them as [Ownership teams](/docs/deliver/ownership/ownership-teams#import-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

## Configure the integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Grant permissions to Workflows**](/docs/analyze-explore-automate/workflows/actions/service-now#permissions "Automate creation of incidents in ServiceNow based on your monitoring data and events.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create ServiceNow authentication credentials**](/docs/analyze-explore-automate/workflows/actions/service-now#authentication "Automate creation of incidents in ServiceNow based on your monitoring data and events.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure ServiceNow connection**](/docs/analyze-explore-automate/workflows/actions/service-now#connection "Automate creation of incidents in ServiceNow based on your monitoring data and events.")

### Step 1 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf. Other permissions are required by actions that come bundled with ServiceNow Connector itself.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * Permissions needed for ServiceNow workflow actions:

     + `app-settings:objects:read`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 2 Create ServiceNow authentication credentials

Sign in to your ServiceNow instance and create basic authentication credentials with the following permissions. You will need these credentials in the next step.

ServiceNow user permissions:

* Search, create and update incidents (table incident)
* Read categories (table sys\_choice, element category)
* Read subcategories (table sys\_choice, element subcategory)
* Read assignment groups (table sys\_user\_group)
* Read resolution codes (table sys\_choice, element close\_code)

### Step 3 Configure ServiceNow connection

You need a configured connection for each of your ServiceNow environments.

To configure a connection

1. Go to **Settings** and select **Connections** > **Connectors** > **ServiceNow**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**
3. Describe your ServiceNow connection.

   * **Connection name**: Provide a meaningful name for your connection.
   * **ServiceNow Instance URL**: Add the URL of your ServiceNow environment.
   * **Type** Either use basic authentication or client credentials.

     + For **Basic Authentication**, provide your username and password.
     + For **Client Credentials**, provide your client id and client secret.
4. Select **Create**.

## Available actions

The following workflow actions are available for the ServiceNow integration. Each action corresponds to an endpoint of the ServiceNow API.

Action

Description

ServiceNow API endpoint

**Create Incident**

Creates an incident in your ServiceNow environment. An incident represents a problem or an issue that needs to be addressed and resolved.

`POST /api/now/v2/table/incident`

**Create a vulnerability item**

Creates a vulnerability item in your ServiceNow environment.

`POST /api/now/v2/table/sn_vul_vulnerable_item`

**Get Groups**

Get groups from your ServiceNow environment.

`GET /api/now/v2/table/sys_user_group`

**Comment**

Create a comment on an entry in your ServiceNow environment.

`PUT /api/now/v2/table/${tableName}/${sysId}`

**Comment on an incident**

Add a new comment to a ServiceNow incident record.

`PUT /api/now/v2/table/incident/${sys_id}`

**Search**

Generic search action that allows searching your ServiceNow environment.

`GET /api/now/v2/table/${tableName}`

**Search incidents**

Query ServiceNow to retrieve a list of incidents matching specified criteria.

`GET /api/now/v2/table/incident`

**Resolve incident**

Update a ServiceNow incident to mark it as resolved.

`PUT /api/now/v2/table/incident/${sys_id}`

**Create record**

Create a new record in a specified ServiceNow table.

`POST /api/now/v2/table/${tableName}`

**Update record**

Update an existing record in a specified ServiceNow table.

`PUT /api/now/v2/table/${tableName}/${sys_id}`

## Create a ServiceNow incident

To raise a ServiceNow incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Incident**.
2. In the **Create Incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Correlation ID** | Unique identifier (in most cases, this is the Dynatrace event ID). | Optional |
   | **Caller** | The user who reports the incident. | Optional |
   | **Category** | The category of the incident. Category options are derived by querying the `sys_choice` table with `sysparm_query: 'name=incident^element=category^inactive=false'`. | Required |
   | **Subcategory** | The subcategory of the incident. Subcategory options are derived by querying the `sys_choice` table with `sysparm_query: 'name=incident^element=subcategory^inactive=false^dependent_value=${category}'`. | Required |
   | **Impact** | The impact of the incident. | Required |
   | **Urgency** | The urgency of the incident. | Required |
   | **Assignment Group** | The group that will work on the incident. Assignment groups options are derived by querying the `sys_user_group` table with `sysparm_display_value: 'all'`. | Required |
   | **Configuration item** | The affected entity. | Optional |
   | **Short description** | A brief description of the incident. | Optional |
   | **Description** | A detailed description of the incident. | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create a vulnerability item in ServiceNow

To create a ServiceNow vulnerability item in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create a vulnerability item**.
2. In the **Create a vulnerability item** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **External ID** | ID which is associated with the vulnerable item | Optional |
   | **Description** | A detailed description of the vulnerability item | Optional |
   | **Short description** | A brief description of the vulnerability item | Optional |
   | **Risk score** | The risk score of the vulnerability item | Optional |
   | **Risk rating** | The risk rating of the vulnerability item | Optional |
   | **Source** | The source which detected the vulnerable item | Optional |
   | **Source risk score** | The risk score in the source system of the vulnerability item | Optional |
   | **Configuration item** | The affected entity | Optional |
   | **First found** | The date of the detection | Optional |
   | **Priority** | The priority of the vulnerability item | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Get Groups from ServiceNow

To fetch groups from ServiceNow in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Get Groups**.
2. In the **Get Group** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create comment in ServiceNow

To create a comment on an entry in a ServiceNow table in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Comment**.
2. In the **Create Comment** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The table name of the entry to comment on | Required |
   | **Unique record identifier (sys\_id)** | The sys\_id of the entry to comment on | Required |
   | **Comment** | The comment that will be created | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Comment on an incident in ServiceNow

To comment on an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Comment on an incident**.
2. In the **Comment on an incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to comment on | Required |
   | **Comment** | The comment that will be created | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search in ServiceNow

To search ServiceNow in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search**.
2. In the **Search** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | Select the table in which to search | Required |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Query category** | Category to filter search results. | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |
   | **Offset** | Records to skip (Default: 0) | Optional |
   | **Order by asc** | Field name to sort results in ascending order | Optional |
   | **Order by desc** | Field name to sort results in descending order | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search incidents in ServiceNow

To search for incidents in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search incidents**.
2. In the **Search incidents** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Resolve incident in ServiceNow

To resolve an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Resolve incident**.
2. In the **Resolve incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to resolve | Required |
   | **Resolution Notes** | Add notes for the resolution of the incident | Required |
   | **Resolution Code** | The close code for the resolution | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create record

To create a record in a ServiceNow Table from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Record**.
2. In the **Create Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Update record

To update a record in ServiceNow from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Update Record**.
2. In the **Update Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Unique record identifier (sys\_id)** | The sys\_id of the entry to comment on | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Troubleshooting

The following is a solution to a problem some people have.

* [ServiceNow for Workflows: Insufficient permissions errorï»¿](https://dt-url.net/hj637wm)


---


## Source: slack.md


---
title: Slack Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/slack
scraped: 2026-02-15T09:06:37.953372
---

# Slack Connector

# Slack Connector

* Latest Dynatrace
* 5-min read
* Updated on Jan 23, 2026

Your Dynatrace environment can integrate with a Slack workspace using Slack Connector ![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector"). You can automate sending messages to Slack based on the events and schedules defined for your [workflow](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

## Set up Slack integration

### Step 1 Allow External Requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

### Step 2 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf. Other permissions are required by actions that come bundled with **Slack** Connector itself.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * `app-settings:objects:read`
   * `app-settings:objects:write`
   * `state:app-states:read`
   * `state:app-states:write`
   * `state:app-states:delete`
   * `state:user-app-states:read`
   * `state:user-app-states:write`
   * `state:user-app-states:delete`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 3 Create Slack app

For Slack Connector workflow actions to interact with your Slack workspace, you first need to create a Slack App for Dynatrace and authorize its connection to Slack.

1. Go to [Slack APIï»¿](https://api.slack.com/apps) and select **Create an App**.
2. In the **Create an app** window, select **From an app manifest**.
3. In the **Pick a workspace to develop your app** window, select the Slack workspace you want to connect to and select **Next**.
4. In the **Enter app manifest below** window, paste the manifest YAML provided below into the YAML tab.
   Replace `<app-name>` and `<bot-name>` with values of your choice (for example, `Dynatrace`). For more information on the manifest YAML, see [Slack documentationï»¿](https://api.slack.com/reference/manifests).

   ```
   display_information:



   name: <app-name>



   features:



   bot_user:



   display_name: <bot-name>



   always_online: false



   oauth_config:



   scopes:



   bot:



   - channels:join



   - channels:read



   - chat:write



   - chat:write.public



   - files:read



   - files:write



   - groups:read



   - im:read



   - mpim:read



   - reactions:read



   - reactions:write



   settings:



   org_deploy_enabled: false



   socket_mode_enabled: false



   token_rotation_enabled: false
   ```

### Step 4 Authorize connection to Slack

Your Dynatrace Slack Connector requires an OAuth token to authorize sending messages to Slack.

1. Go to [Slack APIï»¿](https://api.slack.com/apps/), select **Your Apps** in the upper-right corner, and select the app you just created.
2. Go to **Features** > **OAuth & Permissions**.
   If you're a workspace admin, you'll be able to copy the OAuth token for your workspace. Otherwise, you'll need to **Request to Install** it. After your app is enabled by your admin, you'll get access to the OAuth token as well.
3. Copy the OAuth token.
4. Return to Dynatrace, go to **Settings** and select **Connections** > **Connectors** > **Slack**.
5. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**, give your Slack connection a name and paste the OAuth token in **Bot token**.
6. Select **Create**.

### Input examples

The workflow action can be used to send Markdown-formatted messages or [Block Kit-basedï»¿](https://app.slack.com/block-kit-builder/) interactive messages in Slack.

* **Connection**: select any connection from the dropdown list, for example, `dynatrace-notifications-sandbox`.
* **Message**: see the examples in the following table.

  Input type

  Sample input

  Markdown

  ```
  *Hello World*



  This is Markdown-formatted text!
  ```

  Block Kit Builder

  ```
  {



  "blocks": [



  {



  "type": "section",



  "text": {



  "type": "mrkdwn",



  "text": "*This is a section block with a button.*"



  },



  "accessory": {



  "type": "button",



  "text": {



  "type": "plain_text",



  "text": "Click Me"



  },



  "value": "click_me_123",



  "action_id": "button-action"



  }



  }



  ]



  }
  ```

  Automation expression

  ```
  {{ result("workflow_action_script_result") }}
  ```
* **Interactions**

  Select **Run** to send your message to your Slack channel.

  + **Output**:

    Sample result

    threadTs

    ```
    123456789.01234
    ```

    channelID

    ```
    ABCDEF012345
    ```

    messageTs

    ```
    123456789.01234
    ```

    permalink

    ```
    https://your-environment.slack.com/archives/ABCDEFG/p12345679890
    ```
* **Log output examples**

  + **Successful**:

    ```
    [INFO] POST https://slack.com/api/chat.postMessage called successfully



    [INFO] Message has been posted successfully
    ```
  + **Error**:

    ```
    [ERROR] Slack API error while calling 'chat.postMessage': 'no_text'
    ```

#### Example 1: Block Kit Builder JSON

You can use Block Kit Builder to create richly formatted messages for Slack.
For text formatting options, see [Slack's Markdownï»¿](https://docs.slack.dev/messaging/formatting-message-text/#basic-formatting) reference.
After designing your message, copy the JSON output and adapt it to your needs
in Dynatrace Workflows using workflow expressions.

```
{



"blocks": [



{



"type": "header",



"text": {



"type": "plain_text",



"text": "ð¨ Dynatrace Alert: High CPU Usage Detected",



"emoji": true



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "*Alert Details:*\nâ¢ *Entity*: `Host-1234`\nâ¢ *Metric*: CPU Usage\nâ¢ *Threshold*: > 90%\nâ¢ *Current Value*: 95%"



}



},



{



"type": "divider"



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "ð¡ *Recommended Actions:*"



}



},



{



"type": "actions",



"elements": [



{



"type": "button",



"text": {



"type": "plain_text",



"text": "Acknowledge Alert"



},



"style": "primary",



"value": "acknowledge_alert"



},



{



"type": "button",



"text": {



"type": "plain_text",



"text": "View in Dynatrace"



},



"url": "https://dynatrace.example.com/alert/1234",



"style": "danger"



}



]



},



{



"type": "context",



"elements": [



{



"type": "mrkdwn",



"text": "Triggered at: 2026-01-08 14:30 UTC"



}



]



}



]



}
```

Slack doesn't have a built-in templating language.
Use our templating functionality.
For more information, see [Dynatrace expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression").
Expressions will be resolved at execution time, creating a static card payload that will be sent.

#### Example 2: Dynamic messages with Expressions

If you want to create a structured message with multiple data fields, you can use The Slack Block Kit to develop such a message. See the following example:

```
{



"blocks": [



{



"type": "header",



"text": {



"type": "plain_text",



"text": "production-payment-service",



"emoji": true



}



},



{



"type": "section",



"text": {



"type": "plain_text",



"emoji": true,



"text": "2024-01-09T11:30:00+01:00"



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "```Error: Connection timeout after 5000ms\n  at PaymentGateway.connect (gateway.js:45)\n  at processPayment (service.js:123)```"



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "DT App function: `processPayment`"



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "DT entity service: `SERVICE-A1B2C3D4E5F6G7H8`"



}



}



]



}
```

To replicate this behavior, you can use expressions instead. The same example above can be created with the following snippet:

```
{%- set data = [



{



"dt_app_id": "production-payment-service",



"instance": "2024-01-09T10:30:00Z",



"error": "Error: Connection timeout after 5000ms\n  at PaymentGateway.connect (gateway.js:45)\n  at processPayment (service.js:123)",



"dt_app_function": "processPayment",



"dt_entity_service": "SERVICE-A1B2C3D4E5F6G7H8"



}



]



-%}



{



"blocks": [



{% for item in data %}



{



"type": "header",



"text": {



"type": "plain_text",



"text": "{{ item.dt_app_id }}",



"emoji": true



}



},



{



"type": "section",



"text": {



"type": "plain_text",



"emoji": true,



"text": "{{ item.instance | to_datetime(timezone='Europe/Vienna') }}"



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": {{ ("```" ~ item.error ~ "```") | to_json }}



}



},



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "DT App function: `{{ item.dt_app_function }}`"



}



},



{% if 'dt_entity_service' in item %}



{



"type": "section",



"text": {



"type": "mrkdwn",



"text": "DT entity service: `{{ item.dt_entity_service }}`"



}



}



{% endif %}



{% if not loop.last %},{% endif %}



{% endfor %}



]



}
```

#### Key techniques used in this example:

* `{% set data = [...] %}` - Define data inline or use `result("task_name")` to reference workflow task results.
* `{{ item.field }}` - Access object properties.
* `| to_datetime(timezone='...')` - Format timestamps.
* `| to_json` - Escape special characters for JSON compatibility.
* `{% if condition %}` - Conditional blocks.
* `{% for item in data %}` - Iterate over arrays.

For more expression capabilities, see [Expression reference](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression").

## Use Workflows with Slack

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to create a new workflow.
2. In the **Choose trigger** panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. In the **Choose action** panel, search for `slack` and select **Send message**.
5. Select a pre-configured Slack connection.
6. Select a channel to send your message to.

   Use Slack channel ID

   We recommend using the Slack channel ID. You can also use a Slack channel name or Slack channel ID; however, not all features of the **Send Message** action will be available.
7. Provide a message body.
   Format your message using [Slack Markdownï»¿](https://api.slack.com/reference/surfaces/formatting#basics). It is also possible to use [workflow expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") as input.
8. To test your workflow, select **Run**.

## Troubleshooting

The following are solutions to problems some people had with Slack integration.

* [Invalid connection error for Slackï»¿](https://dt-url.net/2503800)
* [Missing required fields error in Slackï»¿](https://dt-url.net/596382w)
* [Slack channel not shown in list of available channels (Slack)ï»¿](https://dt-url.net/tq038te)
* [Insufficient permissions error in Slackï»¿](https://dt-url.net/09438li)
* [Text file attachment shown as a binary fileï»¿](https://dt-url.net/z423x5i)

## Related topics

* [Send Slack notifications for problems](/docs/analyze-explore-automate/workflows/use-cases/workflows-tutorial-problems-slack "Learn how to send Slack notifications for problems using a simple workflow.")


---


## Source: automation-workflows-text-processing-actions.md


---
title: Actions for Text Processing Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/text-processing/automation-workflows-text-processing-actions
scraped: 2026-02-15T09:11:03.187591
---

# Actions for Text Processing Connector

# Actions for Text Processing Connector

* Latest Dynatrace
* Reference
* 5-min read
* Published Oct 08, 2025

Below is a list of workflow actions available for Text Processing.

## Path syntax details

* Dot notation: Use a `.` dot to navigate through nested objects or arrays.
* Array indexing: Use `.[index]` to access specific elements in an array.
* Escaping special characters: Use square brackets and quotes for property names with spaces or special characters, for example, `.["some property"]`.
* Update entire content: Use `.` to modify the entire content. To be able to update the entire content is useful if the JSON or YAML is a simple string or integer instead of an object, for example, "simple-string".

### Escaping templating syntax

You may encounter double curly braces templating syntax when dealing with JSON or YAML files.

[workflow expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") also use double curly bracket notation.

It is possible to escape `{{` and `}}` with `{{ '{{' }}` and `{{ '}}' }}` respectively, however; actions provided by Text Processing only support valid JSON or YAML syntax.
Should the expression evaluation result yield an action input that is not considered valid in respect to [JSONï»¿](https://www.json.org/json-en.html) or [YAMLï»¿](https://yaml.org/spec/1.2.2/), the workflow execution state is [`Error`](/docs/analyze-explore-automate/workflows/running#workflow-execution-states "Run and monitor workflows created in Dynatrace Workflows.").

In the official Jinja documentation, read more about [escape mechanismsï»¿](https://jinja.palletsprojects.com/en/stable/templates/#escaping).

## Set JSON value

Configures a JSON file.

### Inputs

Field

Description

Required

Example syntax

**JSON content**

The full content of the JSON.

Required

```
{ "obj1": { "innerObj1": { "array": [ { "theObjectInsideTheArray": "value1" }, { "theObjectInsideTheArray": "value2" } ] } } }
```

**Path**

The path to the property that is added or changed.

Required

* Nested object: `.obj1.innerObj1`
* Array element: `.obj1.innerObj1.array[2].theObjectInsideTheArray`
* Property with spaces: `.["some property"]`
* Top-level array: `.[0].someObjectInTheToplevelArray`
* Entire content: `.`

**Value**

The new value for the property path.

Required

`{"new-key": "new-value"}`

### Results

```
{



"json": "<updated json content>"



}
```

### Example

This is an example input for the **Set JSON value** action where we change the value of `name` from "Max" to "Michael".

* **JSON content**

  ```
  {



  "persons": [



  {



  "name": "Max"



  },



  {



  "name": "John"



  }



  ]



  }
  ```
* **Path**: `.persons[0].name`
* **Value**: "Michael"

### Example result

This is the result of running the **Set JSON value** action as part of a workflow.
The first name was changed to Michael.

```
{



"persons": [



{



"name": "Michael"



},



{



"name": "John"



}



]



}
```

## Set YAML value

Manipulates a YAML.
Supports multi-document YAML files.

### Inputs

Field

Description

Required

Example syntax

**YAML content**

The full content of the YAML.

Required

```
obj1:



innerObj1:



array:



- theObjectInsideTheArray: value1



- theObjectInsideTheArray: value2
```

**Path**

The path to the property that is added or changed.

Required

* Nested object: `.obj1.innerObj1`
* Array element: `.obj1.innerObj1.array[0].theObjectInsideTheArray`
* Property with spaces: `.["some property"]`
* Top-level array: `.[0].someObjectInTheTopLevelArray`
* Entire content: `.`

**Value**

The new value for the property path.

Required

`'new-value'`

**Document index**

Relevant only for YAML files containing multiple documents. Index starts at `0`.

Optional

```
obj1:



key: value1



---



obj2:



key: value2
```

To modify the second document, set `documentIndex` to `1`.

### Results

```
{



âyamlâ: â<updated yaml content>â



}
```

### Example

This is an example input for the **Set YAML value** action where we change the value of `name` from "Max" to "Michael".

* **YAML content**

  ```
  ---



  persons:



  - name: John



  - name: Sarah



  ---



  persons:



  - name: Max



  - name: Jeff
  ```
* **Path**
  `.persons[0]`
* **Document index**
  1
* **Value**
  `{ name: "Michael" }`

### Example result

This is the result of running the **Set JSON value** action as part of a workflow. The name was changed to Michael.

```
persons:



- name: John



- name: Sarah



---



persons:



- name: Michael



- name: Jeff
```

## Get JSON value

Retrieves a value from a JSON file.

| Field | Description | Required |
| --- | --- | --- |
| **JSON content** | The full content of the JSON. | Required |
| **Path** | The path to the property that is retrieved. | Required |

### Result

* **JSON content**

  ```
  {



  "person": {



  "name": "John Doe"



  "age": 30,



  }



  }
  ```
* **Path**: `.person`

  ```
  {



  "json": {



  "name": "John Doe",



  "age": 30



  }



  }
  ```

## Get YAML value

Retrieves a value from a YAML file.
Supports multi-document YAML files.

| Field | Description | Required |
| --- | --- | --- |
| **YAML content** | The full content of the YAML. | Required |
| **Document index** | Relevant only for YAML files containing multiple documents. Index starts at `0`. | Optional |
| **Path** | The path to the property that is retrieved. | Required |

### Result

* **YAML content**

  ```
  person:



  name: "John doe"



  age: 30
  ```
* **Path**: `.person`

  ```
  {



  "yaml": "name: \"John Doe\"\nage: 30"



  }
  ```


---


## Source: actions.md


---
title: Workflows Connectors
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions
scraped: 2026-02-15T21:18:22.166064
---

# Workflows Connectors

# Workflows Connectors

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Feb 05, 2026

You can select Workflows Connectors from the Dynatrace Platform catalog. The Workflows Connectors have various actions you can use in your workflow task. For example, you can use actions to create Jira tasks, send Slack notifications, and direct them based on extracted entity ownership information.

## Third-party integrations

[![Kubernetes connector](https://dt-cdn.net/images/kubernetes-for-workflows-256-bcc87a8239.webp "Kubernetes connector")

### Kubernetes Connector

Query and manipulate any Kubernetes resources such as pods, deployments, and services.](/docs/analyze-explore-automate/workflows/actions/kubernetes-automation "Integrate with Kubernetes for controlling your cluster.")[![AWS Connector](https://dt-cdn.net/images/aws-for-workflows3-256-5f6d52e0fa.png "AWS Connector")

### AWS Connector

The **AWS** Connector actions enable your Dynatrace environment to integrate with an AWS environment.](/docs/analyze-explore-automate/workflows/actions/aws "The AWS Connector integration provides powerful actions for various Amazon Web Services such as EC2, Autoscaling and S3.")[![Slack Connector](https://dt-cdn.net/images/slack-for-workflows1-257-4ad7b09fd3.png "Slack Connector")

### Slack Connector

Slack workflow actions come bundled with **Slack** Connector, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces")[![GitHub](https://dt-cdn.net/images/github-for-workflows-new-lxjn9po-256-94579b3812.png "GitHub")

### GitHub Connector

GitHub workflow actions come bundled with **GitHub Connector**, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/github "Integrate Workflows with GitHub for handling common developer tasks.")[![Jira for Workflows](https://dt-cdn.net/images/jira-for-workflows-lm8hkkp-257-bfed74a746.png "Jira for Workflows")

### Jira Connector

Jira workflow actions come bundled with **Jira Connector**, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/jira "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.")[![Microsoft 365 for Workflows](https://dt-cdn.net/images/microsoft-365-for-workflows-sztyvk4-257-484266710c.png "Microsoft 365 for Workflows")

### Microsoft 365 Connector

Microsoft 365 workflow actions come bundled with **Microsoft 365 Connector**, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/microsoft365 "Automate sending emails via Microsoft 365 based on the events and schedules defined for your workflows.")[![Microsoft Teams Connector](https://dt-cdn.net/images/ms-teams-for-workflows1-ybzab76-257-b1a35402d5.png "Microsoft Teams Connector")

### Microsoft Teams Connector

Microsoft Teams workflow actions come bundled with **Microsoft Teams** Connector, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/microsoft-teams "Send messages to Microsoft Teams")[![PagerDuty](https://dt-cdn.net/images/pagerduty-for-workflows-257-0cd4ce0d3a.png "PagerDuty")

### PagerDuty Connector

PagerDuty workflow actions come bundled with **PagerDuty** Connector, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/pagerduty "Automate creation of incidents in PagerDuty based on your monitoring data and events.")[![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows")

### Red Hat Ansible Connector

Red Hat Ansible workflow actions come bundled with **Red Hat Ansible** Connector, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible "Automate running of Ansible jobs based on your monitoring data and events.")[![Azure Connector](https://dt-cdn.net/images/azure-for-workflows-lcgzeur-256-0e765fdb69.png "Azure Connector")

### Azure Connector

Workflow actions come bundled with **Azure Connector**, which you can install in your environment via Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")[![ServiceNow for Workflows](https://dt-cdn.net/images/servicenow-for-workflows-257-9349ea0329.png "ServiceNow for Workflows")

### ServiceNow Connector

Automate the creation of incidents in ServiceNow based on your monitoring data and events.](/docs/analyze-explore-automate/workflows/actions/service-now "Automate creation of incidents in ServiceNow based on your monitoring data and events.")[![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows")

### GitLab Connector

GitLab workflow actions can be bundled with **GitLab** Connector, which you can install in your environment through Dynatrace Hub.](/docs/analyze-explore-automate/workflows/actions/gitlab "Integrate Workflows with GitLab.")[![Snowflake](https://dt-cdn.net/images/snowflake-for-workflows-256-3d9ba2057b.png "Snowflake")

### Snowflake for Workflows

Query and ingest data from Snowflake for Workflows.](/docs/analyze-explore-automate/workflows/actions/snowflake "Query and ingest data from Snowflake for Workflows.")[![Jenkins for Workflows](https://dt-cdn.net/images/jenkins-for-workflows-257-799b6950a2.png "Jenkins for Workflows")

### Jenkins Connector

Integrate with Jenkins to trigger builds and query the status of build jobs.](/docs/analyze-explore-automate/workflows/actions/jenkins "Automate pipelines in Jenkins.")

## Dynatrace integrations

[![Email for Workflows](https://dt-cdn.net/images/email-for-workflows-new-256-f6c0e2d343.png "Email for Workflows")

### Email

Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.")[![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership")

### Ownership

Ownership workflow actions are available directly within Workflows after you install the **Ownership** app. Ownership actions enable you to extract entity ownership contact information and use it in workflows for notifications and task assignments.](/docs/deliver/ownership-app "It provides custom actions to define workflows integrating entity owners and their contact information.")[![Site Reliability Guardian](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Site Reliability Guardian")

### Site Reliability Guardian

Site Reliability Guardian workflow action is available directly within Workflows after you install the **Site Reliability Guardian** app. It enables you to execute a guardian directly in workflows.](/docs/deliver/site-reliability-guardian#automation "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.")[### Dynatrace Intelligence (Preview)

Automate AI analysis such as to forecast and remediate capacity shortages.](/docs/dynatrace-intelligence/use-cases/davis-for-workflows "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic")

### Synthetic for Workflows

Enhance your automation capabilities with Synthetic Monitoring. **Synthetic for Workflows** allows you to execute synthetic monitors on demand at selected locations within your workflows.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows "Enhance your automation capabilities with Synthetic Monitoring.")[### Business Observability

Generate business events from automated tasks to connect monitoring and observability data with business information.](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.")[![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

### Text Processing

Text Processing provides a set of `set` and `get` actions for manipulating content in JSON and YAML file types.](/docs/analyze-explore-automate/workflows/actions/text-processing "Automate text processing in JSON and YAML files for your workflows.")


---


## Source: http-request-workflow-action.md


---
title: HTTP request action for Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/default-workflow-actions/http-request-workflow-action
scraped: 2026-02-15T21:27:06.384993
---

# HTTP request action for Workflows

# HTTP request action for Workflows

* Latest Dynatrace
* Reference
* 1-min read
* Published Apr 02, 2024

The **HTTP Request** action for Workflows enables you to issue an HTTP request to any API.

## HTTP Request action security

* All HTTP calls are validated against the global allowlist.

We strictly advise against providing any static Authorization header and therefore, leak a secret. Use the credential vault to store your credentials for **Basic** or **Token** authentication, or a Run JavaScript action to implement any other authentication.

## Input

* **Method**: the HTTP request method to use.
* **ULR**: the url the request should target.
* **Authentication**: the HTTP Request action supports to use credentials of the credential vault for Basic and Token authentication.
  Make sure the credential configuration [allows access](/docs/manage/credential-vault#access-cv "Store and manage credentials in the credential vault.") for the workflow actor (credential scope: `AppEngine`, app access: `Workflows app`, Owner access or actor as selected user).
* **Payload**: the payload of the HTTP request.
  Set an appropriate content-type header.
* **Headers**: the HTTP request headers with their name and value.
  Be aware that any header value is accessible in the workflow monitor to everyone with access to the workflow. Thus it is strictly advised to not expose any secret, but use the authentication configuration via credential vault.
* **Error handling**: the HTTP response codes that let the task fail.
  Depending on the use case, issuing the HTTP request independently of the response should be successful.
  Therefore, turn the option to fail on certain HTTP response codes off or define the HTTP response codes that shall fail the task.

## Result

The result of the HTTP request action is a JSON structure that includes

* **status\_code**: the HTTP response status code.
* **body**: the raw HTTP response body.
* **headers**: the HTTP response header as objects consisting of header name and value.
* **json**: the HTTP response as a JSON document. Only JSON response payloads are supported.


---


## Source: run-javascript-workflow-action.md


---
title: Run JavaScript action for Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/default-workflow-actions/run-javascript-workflow-action
scraped: 2026-02-15T21:23:56.968382
---

# Run JavaScript action for Workflows

# Run JavaScript action for Workflows

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jun 25, 2025

The **Run JavaScript** action for Workflows enables you to build a custom task running JavaScript code in a workflow.

The Dynatrace Platform provides a [JavaScript runtimeï»¿](https://dt-url.net/mf03qa8) for custom scripts in Workflows.

Custom JavaScript tasks in workflows are provided with an `executionId`, `actionExecutionId`, and `loopItemValue` that, in conjunction with the [automation SDKsï»¿](https://dt-url.net/vq23qax), give you access to task results, workflow execution, and loop item parameters, directly as JavaScript objects without using Jinja expressions.

To use the automation SDKs, import them into the custom script task. Then, they can be initialized with the execution context.

We offer both a [client automation SDKï»¿](https://dt-url.net/j343q5k), which gives full access to the Automation API, and a convenience-focused [automation utils SDKï»¿](https://dt-url.net/0n63qgu).

Executing the Run JavaScript for Workflows action is similar to running the code in the [Function executorï»¿](https://dt-url.net/cp83qh8). You can find the results in the **Result** tab of the **Execution** that you could use in subsequent tasks.

## Run JavaScript action security

* The **Run JavaScript** action does not support [expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") in its input to avoid the possibility of code injection.
* All HTTP calls are validated against the global allowlist.
* If you import [third-party libraries](#third-party) for your JavaScript action, the allowlisted CDN domains provide access to the entire package portfolio. Dynatrace JavaScript runtime is robust against certain attack vectors, but you might accidentally allow malicious code. Make sure to mirror dependencies that you rely on in your internal infrastructure and monitor their security implications with [Dynatrace Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") or third-party tools like Snyk.

We strictly advise against returning any secret as part of the result. Every result is accessible in the executions to anyone with read access to the workflow.

## Run JavaScript action requirements

* See [JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/) for Node and Web API compatibility of the Dynatrace JavaScript runtime.
  The JavaScript runtime times out after 120 seconds.
  Thus, any Run JavaScript action also times out after 120 seconds.
  Please remember that this timeout isn't extendable by setting a higher timeout value in task options.
* The JavaScript runtime provides up to 256 MB RAM.
* The JavaScript runtime and thus Run Javascript actions can't return a binary result. A workaround would be to serialize the payload into an object.
* The script of a Run JavaScript action size is limited to about 5 MB. Additional context information implicitly sent by the AutomationEngine on action invocation, for example, workflow and action execution identifier, also account for this limit.
* The result of Run JavaScript action is limited to 6 MB.
* There is a limit on concurrent requests to the underlying infrastructure (Function executor) that executes the JavaScript runtime. In case your Run JavaScript tasks run into such issue, you can use the task options retry functionality to mitigate the problem.

## Task result

Your JavaScript actions can retrieve the result of a previous task and use it for further processing.

### Example using the automation-utils SDK to access the result

```
// import of sdk modules



import { result } from '@dynatrace-sdk/automation-utils';



export default async function () {



// get the result of task 'my_task'. 'my_task' must be a predecessor.



var myResult = await result('my_task');



// log the result object



console.log('The whole result object: ', myResult);



console.log('only one variable: ', myResult.myVariable)



}
```

### Example using the client-automation SDK to access the result

```
// import of sdk modules



import { executionsClient } from '@dynatrace-sdk/client-automation';



export default async function ({ executionId }) {



// load the execution object using the current executionId



var config = {executionId, id: 'my_task'}



var myResult = await executionsClient.getTaskExecutionResult(config)



// log the result object



console.log('My task result: ', myResult)



console.log('only one variable: ', myResult.myVariable)



}
```

## Available execution context

The following execution context is available out of the box and can be accessed for any use case that demand for it.

```
export default async function ({ executionId, actionExecutionId }) {



//log available execution context ids



console.log('Workflow execution id: ', executionId);



console.log('Action execution id: ', actionExecutionId)



}
```

For loop item context, please see the [Task loop](#task-loop) section below.
Various workflow context information is also available in the Dynatrace JavaScript Runtime itself.

## Task loop

When using the option to loop a task, you might want to access the value of the current loop item. You can use the `loopItemValue` parameter to access the value of the item for the current iteration.

### Example using `loopItemValue`

```
export default async function ({ loopItemValue }) {



// log the current value of the loop item



console.log(loopItemValue)



}
```

## AutomationEngine context information

The `@dynatrace-sdk/automation-utils` package available to run JavaScript tasks provides access to the following information:

* `workflowId` - the executed workflow's ID.
* `executionId` - the ID of the related workflow execution.
* `actionExecutionId` - the ID of the current action execution.
* `taskName` - the task's name in the workflow execution to which the action execution is related.

```
// optional import of sdk modules



import { actionExecutionId, executionId, taskName, workflowId } from '@dynatrace-sdk/automation-utils';



export default async function () {



console.log(`Running action execution '${actionExecutionId}' for task '${taskName}' of workflow '${workflowId}' in workflow execution '${executionId}'`)



}
```

## Import third-party libraries

If you need a certain functionality in your JavaScript action that is provided by third-party libraries, you can load the library via a URL import.

Restrictions apply:

* The JavaScript modules need to be valid [ECMAScript modulesï»¿](https://tc39.es/ecma262/#sec-modules)
* They run within the [context of the Dynatrace JavaScript runtimeï»¿](https://developer.dynatracelabs.com/reference/javascript-runtime/), and its respective compatibility.
* Only modules from allowlisted URLs can be loaded. You need to add them to the **External requests**.

  External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Select  **New host pattern**.
  3. Add the domain names.
  4. Select **Add**.

  This way you can granularly control the web services your functions can connect to.
* Imports may not exceed 6MB in size (combined).

### Example - use XMLJSON library to parse XML input

Let's say your backend produces legacy XML output, but you need to process data as JSON. In such a case, you can let the generic XML2JSON Library to parse the content rather than writing your own code do it.

1. Add the XMLJSON library URL to allowed **External requests**.

   External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
   2. Select  **New host pattern**.
   3. Add the domain names.
   4. Select **Add**.

   This way you can granularly control the web services your functions can connect to.
2. Add a snippet like below to your JavaScript action to parse the XML, convert it to JSON and use as input for your action.

```
// Load the XML parser from ESM



import xml2js from "https://esm.sh/xml2js@0.6.2";



export default async function() {



// Dummy XML, can be fetched from your back-end



const xml = "<root><list><item>Hello</item><item>World</item></list></root>";



const parser = new xml2js.Parser();



const json = await parser.parseStringPromise(xml);



return json;



}
```

Package CDNs like [esm.shï»¿](https://esm.sh), [unpkgï»¿](https://unpkg.com/), [JSRï»¿](https://jsr.io/), [JSDELIVERï»¿](https://www.jsdelivr.com/), or [Denoï»¿](https://deno.com/) offer compatible packages.

Note that some of those libraries either depend on Node.js internals or Deno internals, which the Dynatrace JavaScript runtime does not provide. See [JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/) for Node and Web API compatibility of the Dynatrace JavaScript runtime.

## Intentionally fail task

If you need to fail a run JavaScript task by intention, you throw an unhandled exception.

Here is an example that will always fail the execution of the task.

```
export default async function() {



throw new Error()



}
```

## Access event trigger payload

For workflows triggered by an event, you might want to access the event payload for the business logic you want to implement.

Here is an example to retrieve event context from the workflow execution for event triggered workflows

```
import { execution } from '@dynatrace-sdk/automation-utils';



export default async function ({ executionId }) {



const ex = await execution(executionId);



console.log( ex.params.event);



// your code goes here



}
```


---


## Source: workflows-access-management.md


---
title: Access workflow management functionality
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/manage-workflows/workflows-access-management
scraped: 2026-02-15T21:28:28.263568
---

# Access workflow management functionality

# Access workflow management functionality

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 15, 2025

To access various workflow management commands:

1. Find the workflow and select .
2. Select a command. The list of commands available to you depends on your permissions.

   * **Edit workflow**âsee [Create workflows in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/building "Create and edit workflows in Dynatrace Workflows.")
   * **Run workflow**âsee [Run and monitor workflows created in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/running "Run and monitor workflows created in Dynatrace Workflows.")
   * **View execution history**âlists executions of the workflow
   * **Duplicate workflow**âmakes a copy of the selected workflow
   * **Make public** and  **Make private**âtoggle sharing on and off. Any user with permissions can access a public workflow.
   * **Transfer ownership**âsee [Change ownership of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-change-owner "Change ownership of your workflow.")
   * **Version history**âsee [Compare and restore versions of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-versioning "Compare and restore every version of your workflow.")
   * **Workflow**âsee [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download#download-workflow "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
   * **Template**âsee [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download#download-workflow-template "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
   * **Delete workflow**âdeletes the selected workflow and any **Draft** available.
   * **Delete draft**âsee [deletes only the workflow draft](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-manage-live-mode "Undeploy your workflow or download as Workflow or as a template.").

## Related topics

* [Upload a workflow or a workflow template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-upload "Upload your workflow or your template.")
* [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
* [Change ownership of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-change-owner "Change ownership of your workflow.")
* [Manage live or draft workflows](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-manage-live-mode "Undeploy your workflow or download as Workflow or as a template.")
* [Get notified about workflow changes](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-notifications "Get workflow notifications about changes to your workflow, such as edits, deletions, and failures.")
* [Compare and restore versions of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-versioning "Compare and restore every version of your workflow.")


---


## Source: workflows-manage-live-mode.md


---
title: Manage live or draft workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/manage-workflows/workflows-manage-live-mode
scraped: 2026-02-15T09:09:33.290038
---

# Manage live or draft workflows

# Manage live or draft workflows

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 23, 2025

To access various **Live** or **Draft** workflow management commands

1. Go to ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
2. Find the workflow.
3. Select either **Edit in draft** or **Switch to live**.
4. Next to the **Switch to live** button, open to the  menu.
5. Select a command.

   * **Workflow**âsee [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download#download-workflow "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
   * **Template**âsee [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download#download-workflow-template "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
   * **Compare draft changes**âcompare the **Draft**to any the **Live** version of the workflow.
   * **Undeploy workflow**âthe workflow becomes draft only, any existing **Draft** will be replaced. It won't be triggered automatically anymore.
   * **Delete draft**âdeletes only the **Draft** of the workflow.

## Related topics

* [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
* [Manage workflows](/docs/analyze-explore-automate/workflows/manage-workflows "Manage your workflows")


---


## Source: workflows-notifications.md


---
title: Get notified about workflow changes
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/manage-workflows/workflows-notifications
scraped: 2026-02-15T09:06:29.574632
---

# Get notified about workflow changes

# Get notified about workflow changes

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 07, 2025

Get notifications about changes to your workflow, such as edits, deletions, execution failures, and throttle limits.

## Turn on notifications

Notifications are not turned on by default.

To turn on notifications for a workflow navigate to the relevant workflow.

1. Select .
2. Select **Turn on notifications**.

   ![Screenshot of a workflow with notification.](https://dt-cdn.net/images/umsaywsjuo-dev-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-send-email-1-view-draft-1968-27572da6b3.png)

## Details

When you turn on notifications, you receive email notifications for the following scenarios:

* Workflow edits or deletions
* Workflow failures
* Hourly execution throttle limit

### Workflow edits or deletions

Notifications are sent when a workflow is edited or deleted, provided the following conditions are met:

Notifications are sent when:

* Someone else edited a live workflow.
* Someone else deleted a workflow.

### Workflow failures

A notification is sent when a workflow execution fails if that workflow has already had at least one successful execution.

### Hourly execution throttle limit

A notification is sent when a workflow hits its hourly execution throttle limit.
This ensures awareness about potential interruptions in workflow execution.

## Turn off notifications

To turn off notifications for workflow, select  > **Turn off notifications**.

## Related topics

* [Workflows quick start guide](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.")
* [Create workflows in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/building "Create and edit workflows in Dynatrace Workflows.")
* [Manage workflows](/docs/analyze-explore-automate/workflows/manage-workflows "Manage your workflows")
* [Upload a workflow or a workflow template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-upload "Upload your workflow or your template.")
* [Download a workflow or template](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-download "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
* [Change ownership of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-change-owner "Change ownership of your workflow.")
* [Manage live or draft workflows](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-manage-live-mode "Undeploy your workflow or download as Workflow or as a template.")
* [Compare and restore versions of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-versioning "Compare and restore every version of your workflow.")


---


## Source: security.md


---
title: User permissions for workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/security
scraped: 2026-02-15T21:22:44.842187
---

# User permissions for workflows

# User permissions for workflows

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 17, 2025

## Workflows and AutomationEngine API permissions

The Workflows app, which is the frontend for the AutomationEngine, enables you to edit, manage, and run workflows in Dynatrace.

* To use Workflows, you need some general AppEngine permissions and some AutomationEngine-specific permissions.
* Permissions are configured in account administration and require account admin access.
* If you are missing any required permissions, reach out to your account administrator.

We recommend that administrators differentiate between regular users and administrators as follows.

### AutomationEngine authorization settings

If the required permission for a workflow task is missing, an attempt to execute this task results in a 403 Forbidden error.

Always make sure:

* You have the required permissions granted in [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.").
* You granted all required permissions for the workflows to run in the authorization settings.

To enable or edit the AutomationEngine authorization settings

1. In the **Workflows** app, go to **Settings** > **Authorization settings**.
2. Enable the required permissions from **Primary permissions** and **Secondary permissions** lists.

### Workflows user

A Workflows user creates, edits, runs, and monitors workflows.

To access the **Workflows** and view workflows, you need at least the following permissions.

Permission

Grants access to

`app-engine:apps:run`

List all apps and read the app bundles.

`automation:workflows:read`

View workflows.

`storage:system:read`

optional `storage:event.provider = "AUTOMATION_ENGINE"` [1](#fn-1-1-def)

`storage:buckets:read`

optional `storage:table-name = "dt.system.events"` [1](#fn-1-1-def)

View the execution history of workflows.

1

The conditions listed represent the most restrictive way to apply the permissions while still allowing access to the execution history. Any less restrictive application of these permissions will also provide the necessary access.

To write and execute workflows, the following additional permissions are required.

| Permission | Grants access to |
| --- | --- |
| `app-engine:functions:run` | Use the function executor. |
| `automation:workflows:run` | Run workflows manually via the user interface or API. |
| `automation:workflows:write` | Write workflows. It includes creating, updating, and deleting a workflow. It also includes the workflow configuration with active schedule or event trigger configurations. Thus, the workflow is run based on these configurations. |

You can grant users the `automation:workflows:write` permission where the `automation:workflow-type = "SIMPLE"` is specified. This means that they can create workflows with a single trigger and task. Since simple workflows don't consume workflow hours, this is a convenient way to give a broader user base access to workflows without the cost implication.

These permissions grant access to workflows themselves. To successfully run workflow tasks, the [actor](#workflow-actor) might need additional permissions.

### Workflows administrator

A Workflows administrator can:

* Access all workflows and executions in an environment.
* Manage workflows and executions where the owner is unavailable.
* Import or edit workflows, preserving the [actor](#workflow-actor) and [owner](#workflow-access) of the workflow, which is most of the time desired when transporting workflows between environments.

To administer workflows, you need the following permission on top of all [user permissions](#user-permission).

| Permission | Grants access to |
| --- | --- |
| `automation:workflows:admin` | Administer workflows. |

To turn on **Workflow admin** mode in Workflows

1. Verify that you have `automation:workflows:admin` permission in addition to all regular user permissions.
2. Select **Settings** in the upper-right corner of the **Workflows** app.
3. Turn on the **Workflow admin** mode.

To exit the **Workflow admin** mode and use Workflows as a regular user, turn off the **Workflow admin** toggle.

## Workflow owner

The initial owner of a workflow is the user who creates it. Right after a workflow is created, only the owner can view, manage, and execute the workflow. This is a private workflow.

To let others access a workflow, the owner has the following options:

* Make the workflow public. A public workflow is visible to every user with `automation:workflows:*` permissions.
* Transfer ownership to another user. For details, see [Change ownership of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-change-owner "Change ownership of your workflow.").
* Transfer ownership to a group, in which case all members of the group can access the workflow, depending on their permissions.

### Execution access and ownership

Access to an execution depends on the workflow ownership and private/public configuration when the execution was started.

* Execution access is always evaluated at the start of an execution.
* A change to workflow ownership or visibility doesn't impact past executions; it affects only future executions.

### Administrator

An administrator has access to all workflows and executions in an environment.

* An administrator can manage all workflows and executions.
* No restriction of visibility or ownership applies to an administrator.

## Workflow actor

Every execution of a workflow task is performed in the context of a user.

To figure out the actor of a workflow

1. Open a workflow in the workflow editor.
2. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Settings**.
3. Check the details pane where you'll find the actor information.

* This user is called the actor.
* The actor is configured per workflow.
* By default, the actor is the creator of the workflow.

When you run a workflow in an environment for the first time, Dynatrace asks to allow the AutomationEngine to run workflows for you.

* You need to consent to the range of permissions the AutomationEngine might exercise when running workflows with you as the actor.
* These permissions are tied to the permissions you already have and can never exceed them.

### Actor updates

A user who updates a workflow is set as the actor automatically. This prevents exploits where a user changes a workflow to achieve something in another user's context.

* The actor remains unchanged if either the workflow update happens by a user in **Workflow admin** mode, or the actor is set to a service user.
* You can only use service users which are granted to you.

### Service users

By default, the workflow actor is the user who created the workflow. However, there is the option to select a non-interactive service user as the actor of a workflow. This makes the workflow independent of the status of the user who maintains it.

We highly recommend using service users as actors for all workflows that are worked on collaboratively and serve a production grade use case.

Service users and their permissions are managed by admins through [Identity and Access Management](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users"). We highly recommend granting a service user only the permissions that are required for the intended usage scenario.

To set the workflow actor to a service user

1. Open the workflow in the workflow editor.
2. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Settings**.
3. Select the service user from the **Actor** list.
4. Save your changes.

The user editing a workflow needs the `iam:service-users:use` permission to use a service user as an actor. You can create a policy as follows to allow specific service users.

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("<SERVICE_USER_1_EMAIL>", "<SERVICE_USER_2_EMAIL>");
```

For more information, see [Service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users")


---


## Source: event-trigger.md


---
title: Event triggers for workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/trigger/event-trigger
scraped: 2026-02-15T21:24:09.997342
---

# Event triggers for workflows

# Event triggers for workflows

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 02, 2026

Event triggers are a group of triggers that you can configure to match events in the ingest pipeline to trigger a workflow.

There are three event trigger types

* **Event trigger**
* **Davis problem trigger**
* **Davis event trigger**

## Event trigger

The **Event trigger** allows you to specify a custom event filter with the help of a [DQL matcher](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline .") expression to define which events will trigger a workflow execution.

The following configuration parameters are available to define the triggering behavior of the **Event trigger**.

* **Event type**

  + **events** are created by Dynatrace and your monitoring and platform configuration.
  + **bizevents** are business events. An external application sends the **bizevents**. For more information, see the [`/bizevents/ingest` endpoint](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.").
  + **dt.system.events** are generated by Dynatrace system services. Not all system events are eligible to trigger workflows. To find the events that can be used, look for those with the `dt.openpipeline.pipelines` property set using filter `isNotNull(dt.openpipeline.pipelines)` in a notebook.
  + **security.events** are generated by Dynatrace Application Security, ingested via the [`v1/security.events` endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.") or ingested via [`custom/security.events/<custom-endpoint-name>` endpoints](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API."). For more information, see [security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.") in the Semantic Dictionary.
* In **Filter query**, you can define how to narrow down the events. The filter definition is provided in [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") syntax.

Optional Select **Query past events** to estimate the volume of matching events in your environment.

Single events

All events are evaluated in the ingest pipeline against the DQL matcher expression, event by event. A DQL matcher expression, therefore, doesn't allow the use of any aggregation or querying over a set of events.

## Davis problem trigger

Davis problems are created by [Dynatrace Intelligence](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.") based on monitoring data. The **Davis problem trigger** allows selectively triggering a workflow in response. The trigger will happen once, when a Davis problem becomes active (on open and re-open), and optionally once when a problem is closed.

The following configuration parameters are available to define the triggering behavior of the **Davis problem trigger**.

* **Problem state**

  + **active** means that the Davis problem is not closed yet.
  + **active or closed** means that the Davis problem can be both active or closed.
* **Event category** definitions are in [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.").
* Select **Affected entities** based on their tags. For more information on tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

  + **Include all entities**
  + **Include entities with all defined tags below**
  + **Include entities with any defined tag below**
* Define **Additional custom filter query** by adding any [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") expression to the above definition.

## Davis event trigger

Davis events are created by [Dynatrace Intelligence](/docs/dynatrace-intelligence/root-cause-analysis "How Dynatrace analyzes problems to determine their root cause.") based on monitoring data. The **Davis event trigger** allows selectively triggering a workflow in response.

The following configuration parameters are available to define the triggering behavior on Davis Problem events

* **Problem state**

  + **active** means that the Davis event is not closed yet.
  + **active or closed** means that the Davis event can be active or closed.
* **Davis event name**

  + **equals** means there's a match if the Davis event name exactly matches the event name string.
  + **contains** means there's a match if the Davis event name contains the event name string.
* Select the **Affected entities** based on their tags. For more information on tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

  + **Include all entities**
  + **Include entities with all defined tags below**
  + **Include entities with any defined tag below**
* Define **Additional custom filter query** by adding any [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") expression to the above definition.

## Permissions

The actor on a workflow with event trigger requires access to the event, thus the following permissions must be granted accordingly.

* [storage:events:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-events-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") - in case of generic event trigger of type events, as well as Davis problem or event trigger
* [storage:security.events:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-security-events-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") - in case of event trigger of type security.events
* [storage:bizevents:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-bizevents-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") - in case of generic event trigger of type bizevents
* [storage:system:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-system-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") - in case of generic event trigger of type dt.system.events
* [storage:buckets:read](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-buckets-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") - its recommended to restrict the permission to the bucket related to the event only

These permissions must be granted for any kind of user selected as an actor. In the case of an interactive user (nonsystem user), make sure that these permissions are also chosen in the authorization settings by this user. For more details, see (permission documentation for Workflows](workflows-security).

## Limits

Because event triggers can occur frequently, each workflow is limited to a maximum of 1,000 event triggers per hour, per workflow.

* If an event trigger exceeds this limit, no further event triggers for this workflow will run for up to an hour.
* If an event trigger reaches the limit three times within seven days, the event trigger is disabled.

In either case, the limit is flagged in the Workflows overview and can be filtered for.

To remedy this situation, we recommend adjusting the event trigger configuration and reenabling the trigger.

## Hints on working with workflows and event triggers

* To access the event payload to parameterize tasks in your workflow, use the `event()` [expression](/docs/analyze-explore-automate/workflows/reference#event "Get to know the workflows expression").
* For an event trigger, Workflows will prompt the event context of the last successful execution for manually triggered workflow runs. The Workflows prompt allows you to adjust the event context for manual runs during workflow development iterations.
* With **Query past events** in the event trigger definition, you can quickly see how many matching events were observed in the past in your environment.
* Use [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to explore the events in your environment and determine which events you want to leverage.
* Be aware that event filter expressions only support [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") syntax, which is a subset of DQL.


---


## Source: workflows-tutorial-problems-email.md


---
title: Send email notifications for problems
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/use-cases/workflows-tutorial-problems-email
scraped: 2026-02-15T21:23:06.031543
---

# Send email notifications for problems

# Send email notifications for problems

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Oct 19, 2025

Problems are automatically opened by Dynatrace when anomalies or alert conditions are detected in your environment.
In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, build a  simple workflow that listens to problems and automatically sends ![Email for Workflows](https://dt-cdn.net/images/email-for-workflows-new-256-f6c0e2d343.png "Email for Workflows") email alerts.
This guide shows you how.

![Screenshot of a workflow to learn how to send email notifications for Davis problems using a simple workflow.](https://dt-cdn.net/images/umsaywsjuo-dev-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-e45c4e16-ae41-422d-b6d6-0f8d2aa3d015-view-live-3728-0fad43a67d.png)

## What will you learn

In this tutorial, you'll learn how to alert your team in real time by emailing the details of a new problem to a specific email recipient.

At a short glance, you will:

1. [Create a simple workflow](/docs/analyze-explore-automate/workflows/simple-workflow#create-simple-workflow "Build and run a simple workflow.").
2. Add an [event trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") for  [Davis problems](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").
3. Add an [email notification](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
4. Save and run the  workflow to get email notifications.
5. Verify your  workflow is working as expected.

## Prerequisites

* You should have permission to configure and run a  simple workflow.
  For example, the permission granted with the default policy is for a [standard user](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference").
* You should select the necessary permissions in [authorization settings](/docs/analyze-explore-automate/workflows/security#authorization-settings "Guide on security aspects of workflow automation in Dynatrace Workflows").

  + You should allow the required permissions to

    - Access ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
    - Write and execute a workflow.
      For more information, see [authorization settings](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

## Steps

1. [Create a simple workflow](/docs/analyze-explore-automate/workflows/simple-workflow#create-simple-workflow "Build and run a simple workflow.").

   1. Go to ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
   2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow** in the upper-right corner of the page.
   3. Select the workflow title.
      By default, it is `Untitled workflow`, and enter a meaningful name.
      The workflow type is set to  simple workflow by default.
2. Add an [event trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") for  [Davis problems](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").

   1. In the **Select trigger** section, select a  [Davis problem trigger](/docs/analyze-explore-automate/workflows/trigger/event-trigger#davis-problem-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.").
   2. Set the **Problem state** to **active or closed**.
      This option means that the problem can be both active or closed.
      This setting causes the workflow to trigger twice, once when the problem becomes active and again when it is closed.
   3. In the **Event category** drop-down list, select **Select all**.
   4. Optional Select **Query past events** to see the most recent problem events that would have triggered this workflow.
   5. Optional Enter **Entity tags** or **Additional custom filter query** to only trigger the workflow on the relevant problems.
3. Add an [email notification](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").

   1. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add task** on the trigger node.
   2. In the **Choose action** section, select **Send email** action type.
      Give the action type a meaningful title.
   3. Enter the recipient's email address in the **To** field.
   4. In the **Subject** field, enter the following:

      ```
      {{ event()["event.status"] }} Problem {{ event()["display_id"] }}: {{ event()["event.category"] }} {{ event()["event.name"] }}
      ```
   5. In the **Message** field, enter the following:

      ```
      {{ event()["event.description"] }}



      Go to problem: {{ environment().url }}/ui/apps/dynatrace.davis.problems/problem/{{ event()["event.id"] }}
      ```

   This configuration uses event context placeholders to dynamically populate the email with relevant problem details .

   The Davis problems trigger returns the problem record.
   You can use any field from the problem record, stored in `dt.davis.problems`, in the email notification.
4. Save and run the  workflow to get email notifications.

   1. Select  **Create draft**.
   2. Select **Deploy**.
   3. Select **Run** to see the selected problem event that will be used for the workflow.
5. Verify that your  workflow is working as expected:

   1. Go to your workflow.
   2. Select **Run**.
   3. Select **Run** again to execute the workflow.

      After the workflow has executed, you should see a **Success** state at the top of the workflow editor.
      Execution logs aren't available for a simple workflow.
      If an error occurs, you can find the error details on the right in the task details pane.

      ![Screenshot of a successfully run email notification workflow. ](https://dt-cdn.net/images/umsaywsjuo-dev-apps-dynatracelabs-com-ui-apps-dynatrace-automations-executions-ced3847e-34b5-4a04-9312-a79f423e32a2-3718-dfc1a7d8c5.png)

## Conclusion

Youâve created a  simple workflow that sends email notifications when problems are opened or closed.
This setup helps to ensure that your team is immediately informed about critical issues in your environment.

You can extend this workflow by

* Adding conditions to handle specific problem categories or severities.
* Adding auto remediation steps to your workflow.

This workflow is a great starting point for automating incident response and improving operational awareness.

## Related topics

* [Create a simple workflow in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/simple-workflow "Build and run a simple workflow.")
* [Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Email](/docs/analyze-explore-automate/workflows/actions/email "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.")


---
