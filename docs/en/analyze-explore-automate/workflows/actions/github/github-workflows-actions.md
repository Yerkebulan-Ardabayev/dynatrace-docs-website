---
title: Actions for GitHub Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/github/github-workflows-actions
scraped: 2026-02-25T21:33:42.069840
---

# Actions for GitHub Connector

# Actions for GitHub Connector

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jan 27, 2025

This page contains Github workflow actions that are available for the GitHub Connector ![GitHub](https://dt-cdn.net/images/github-for-workflows-new-lxjn9po-256-94579b3812.png "GitHub") integration.

### Required token permissions to run all GitHub actions

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

## Related topics

* [Set up GitHub Connector](/docs/analyze-explore-automate/workflows/actions/github/github-workflows-setup "Learn how to set up GitHub Connector.")