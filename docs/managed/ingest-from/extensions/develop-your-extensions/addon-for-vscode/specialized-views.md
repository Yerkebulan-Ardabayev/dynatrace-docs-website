---
title: Specialized views
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views
scraped: 2026-05-12T12:35:07.310859
---

# Specialized views

# Specialized views

* Reference
* 2-min read
* Published Jun 16, 2025

**Dynatrace Extensions** creates its entry in the VS Code activity bar. This entry provides two specialized views to help you manage Extension projects at scale and become more efficient.

## Extension 2.0 workspaces

This view is intended to help you keep track of all Extension 2.0 projects and their workspaces, no matter where they're stored on your filesystem. Each registered workspace is shown by its root folder name, and your currently opened workspace is shown in green, whereas others are in blue.

In this view, you can do the following:

* Use the plus button to register a new workspace.
* Use the refresh button to update the list.

Top-level items in this list represent your Extension projects. For each one, you can do the following:

* Use the folder button to open the associated workspace in the VS Code editor.
* Use the bin button to un-register the project. It'll not delete the workspace from your filesystem.
* Select the label to see the extension's name within that workspace, along with its version.

  + Use the file button to open the extension's manifest for a quick look. It'll open in the same window.

This view lets you easily update some Dynatrace Extensions behavior settings associated with each workspace. You can do this by right-clicking on any registered workspace label.

## Environments

As its name implies, this view is focused on Dynatrace environments and your deployed extensions. Your currently connected Dynatrace environment is shown in green, while others are in blue.

In this view, you can do the following:

* Use the plus button to register a new environment.
* Use the refresh button to update the list.

Top-level items in this list are your registered Dynatrace environments. For each one, you can do the following:

* Use the pen button to change any details.
* Use the bin button to remove this environment.
* Select the label to expand a list of deployed extensions.

Children items to an environment are its deployed extensions. Select any extension to expand the list further and show the extension's monitoring configurations (the status is indicated next to its name). You can do the following:

* Use the plus button to create a new monitoring configuration.
* Use the pen button to make changes to a configuration.
* Use the bin button to delete the configuration.
* Use the file button to save this configuration to a file. It'll be saved in your workspace's `./config` folder.