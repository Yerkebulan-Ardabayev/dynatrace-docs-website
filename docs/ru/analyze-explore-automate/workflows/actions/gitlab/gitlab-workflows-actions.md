---
title: Actions for GitLab Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-actions
scraped: 2026-02-19T21:23:54.475554
---

# Actions for GitLab Connector

# Actions for GitLab Connector

* Latest Dynatrace
* Reference
* 9-min read
* Updated on Jan 14, 2025

The following workflow actions are available for the GitLab Connector ![GitLab for Workflows](https://dt-cdn.net/images/gitlab-for-workflows-3a1edba03e.svg "GitLab for Workflows") integration. Each action corresponds to an endpoint of the GitLab Connector API.

For details on creating workflows, refer to [Create workflows in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/building#create "Create and edit workflows in Dynatrace Workflows.").

The actions are listed under the following categories:

* [Repository files APIs](#create-file)
* [Merge requests APIs](#create-merge-request)
* [Issues APIs](#create-new-issue)
* [Jobs APIs](#get-pipeline-status)

## Create file

Creates a new file in a new branch based on the specified base branch.

The action can only act on one file, resulting in the creation of a new branch. The GitLab API doesn't allow the reuse of existing branches. Any attempt to do so results in the GitLab API throwing an error.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Start branch** | The starting branch to base the new branch on. | Required |
| **Branch** | The name of the new branch. | Required |
| **File path** | The relative path to the file to be created. | Required |
| **File content** | The content of the new file. | Required |
| **Commit message** | The commit message for the new file. | Required |
| **Author name** | The name of the author of the resulting commit. | Optional |

### Output

Returns fields as described in the [Repository files API - Create new file in repositoryï»¿](https://dt-url.net/7o43w88) GitLab documentation.

## Get file

Gets a file from a repository.

This action should only be used to retrieve the contents of a plain-text file.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **File path** | The relative path of the file. | Required |
| **Ref** | The reference from which to retrieve the file. It can be a branch name or a commit hash. | Required |

### Output

Returns fields as described in the [Repository files API - Get file from repositoryï»¿](https://dt-url.net/l863wwz) GitLab documentation.

## Update file

Updates a file in your GitLab repository. This action creates a new branch based on the specified base branch.

The action can only act on one file, resulting in the creation of a new branch. The GitLab API doesn't allow the reuse of existing branches. Any attempt to do so results in the GitLab API throwing an error.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Start branch** | The starting branch to base the new branch on. | Optional |
| **Branch** | The name of the new branch. | Required |
| **File path** | The relative path to the file to be updated. | Required |
| **File content** | The updated content of the file. | Required |
| **Commit message** | The commit message for the edit. | Required |
| **Author name** | The name of the author of the resulting commit. | Optional |

### Output

Returns fields as described in the [Repository files API - Update existing file in repositoryï»¿](https://dt-url.net/6o83wg0) GitLab documentation.

## Delete file

Deletes a file in your GitLab repository. This action creates a new branch based on the specified base branch.

The action can only act on one file, resulting in the creation of a new branch. The GitLab API doesn't allow the reuse of existing branches. Any attempt to do so results in the GitLab API throwing an error.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Start branch** | The starting branch to base the new branch on. | Required |
| **Branch** | The name of the new branch. | Required |
| **File path** | The relative path to the file to be deleted. | Required |
| **Commit message** | The commit message for the deletion. | Required |
| **Author name** | The name of the author of the resulting commit. | Optional |

### Output

Returns fields as described in the [Repository files API - Delete existing file in repositoryï»¿](https://dt-url.net/xfa3w6o) GitLab documentation.

## Create merge request

Creates a merge request in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Source Branch** | The name of the source branch. | Required |
| **Target Branch** | The name of the target branch. | Required |
| **Title** | The title of the new merge request. | Required |
| **Description** | The description of this merge request. | Optional |

### Output

Returns fields as described in the [Merge requests API - Create MRï»¿](https://dt-url.net/uyc3wjd) GitLab documentation.

## Get merge request

Gets a single merge request in GitLab.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Internal ID** | The GitLab internal identifier of the merge request. | Required |
| **Commits behind the target branch** | Toggle the switch on to include the commits behind the target branch. | Optional |
| **Rebase operation in progress** | Toggle the switch on to include any rebase operation in progress. | Optional |

### Output

Returns fields as described in the [Merge requests API - Get single MRï»¿](https://dt-url.net/u8e3wkb) GitLab documentation.

## List merge requests

Gets a list of merge requests in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Author** | The name of the user who authored the merge requests. | Optional |
| **State** | The status of merge requests you're interested in. | Optional |

### Output

Returns fields as described in the [Merge requests API - List merge requestsï»¿](https://dt-url.net/42g3w9v) GitLab documentation.

## Merge a merge request

Merges a merge request in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Merge request** | The merge request to merge. | Required |
| **SHA** | The hash of the presumptive last commit in the merge request. If the actual last commit differs, the action fails. | Optional |
| **Enable squash merge** | Toggle the switch on to use the squash merge strategy or off to use the merge commit strategy. | Optional |

### Output

Returns fields as described in the [Merge requests API - Merge a merge requestï»¿](https://dt-url.net/myi3wx9) GitLab documentation.

## Update merge request

Updates an existing merge request in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Merge request** | The merge request to be updated. | Required |
| **Branch** | The name of the target branch. | Required |
| **Title** | The new title of the merge request. | Optional |
| **Description** | The description of this merge request. | Optional |

### Output

Returns fields as described in the [Merge requests API - Update MRï»¿](https://dt-url.net/b7k3wms) GitLab documentation.

## Create merge request note

Creates a new note for a single merge request in GitLab.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Merge request** | The merge request to which the note will be posted. | Required |
| **Content of the note** | The content of the note. | Required |
| **SHA** | The hash of the presumptive last commit in the merge request. If the actual last commit differs, the action fails. | Optional |

### Output

Returns fields as described in the [Merge requests API - Create MR Noteï»¿](https://dt-url.net/f903w51) GitLab documentation.

## Create new issue

Creates a new issue in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Title** | The title of the new issue. | Required |
| **Labels** | A comma-separated list of labels to add to the issue. | Optional |
| **Issue type** | The type of the issue. | Optional |
| **Description** | The description of the issue. | Optional |
| **Assignees** | The user to assign this issue. If not set, the issue will be unassigned. | Optional |

### Output

Returns fields as described in the [Issues API - New issueï»¿](https://dt-url.net/n1m3wi7) GitLab documentation.

## Edit issue

Edits an issue in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Title** | The new title of the issue. | Optional |
| **Labels** | A comma-separated list of labels to apply to the issue. | Optional |
| **Issue type** | The type of the issue. | Optional |
| **Description** | The description of the issue. | Optional |
| **Close/Reopen** | Select to change the issue status. | Optional |

### Output

Returns fields as described in the [Issues API - Edit an issueï»¿](https://dt-url.net/fuo3was) GitLab documentation.

## List issues

Gets a list of issues from your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Issue Ids** | Show only issues with the specified, comma-separated list of IDs. | Optional |
| **Title or Description** | Show only issues that contain the specified text in their title or description. | Optional |
| **Issue type** | Show only issues of the specified type. | Optional |
| **Labels** | Show only issues with all of the comma-separated labels assigned to them. | Optional |
| **State** | Set whether you want to retrieve a list of open or closed issues. | Optional |

### Output

Returns fields as described in the [Issues API - List issuesï»¿](https://dt-url.net/kqq3wj6) GitLab documentation.

## Get pipeline status

Gets the status of a pipeline running in your GitLab repository.

### Inputs



| Field | Description | Required |
| --- | --- | --- |
| **Branch** | The name of the branch. | Required |
| **Pipeline** | The GitLab internal identifier of the pipeline. | Required |

### Output

Returns fields as described in the [Jobs API - Get a single jobï»¿](https://dt-url.net/vss3wqf) GitLab documentation.

## Trigger a new pipeline

Triggers a new run of a pipeline in your GitLab repository.

### Inputs

| Field | Description | Required |
| --- | --- | --- |
| **Branch** | The name of the branch for which the pipeline should be triggered. | Required |

You can also set any number of build parameters.

### Output

Returns fields as described in the [Jobs API - Run a jobï»¿](https://dt-url.net/leu3wbq) GitLab documentation.

## Related topics

* [GitLab Connector](/docs/analyze-explore-automate/workflows/actions/gitlab "Integrate Workflows with GitLab.")
* [Set up GitLab Connector](/docs/analyze-explore-automate/workflows/actions/gitlab/gitlab-workflows-setup "Set up GitLab Connector.")