---
title: Red Hat Ansible Automation
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible
scraped: 2026-02-21T21:23:10.090670
---

# Red Hat Ansible Automation

# Red Hat Ansible Automation

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Oct 16, 2025
* Preview

Preview

When you integrate your Dynatrace environment with Red Hat Ansible Automation controller using Red Hat Ansible Connector ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows"), you can automatically start job templates based on your monitoring data.

## Configure the integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Grant permissions to Workflows**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible#permissions "Automate running of Ansible jobs based on your monitoring data and events.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create Red Hat Ansible API key**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible#api-key "Automate running of Ansible jobs based on your monitoring data and events.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure Red Hat Ansible Automation connection**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible#connection "Automate running of Ansible jobs based on your monitoring data and events.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Configure Red Hat Ansible Automation connection**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible#edgeconnect "Automate running of Ansible jobs based on your monitoring data and events.")

### Step 1 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

* `app-settings:objects:read`
* `state:app-states:read`
* `state:app-states:write`
* `state:app-states:delete`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 2 Create Red Hat Ansible API key

To interact with Red Hat Ansible Automation Controller, you need an API key. To learn how to obtain it, see the [Red Hat official documentationï»¿](https://dt-url.net/q60398k).

### Step 3 Configure Red Hat Ansible connection

You need a configured connection for of your Red Hat Automation environments.

To configure a connection for **Red Hat Ansible Automation Controller**

1. Go to **Settings** and select **Connections** > **Connectors** > **Red Hat Ansible**.
2. Select the tab **Automation Controller**.
3. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
4. Provide a meaningful name for your connection.
5. Provide the Red Hat Ansible API URL. For example, `http://your-ansible-host.com/api/v2` (must include the `api/v2`, no trailing slash).
6. Provide your Red Hat Ansible API key.
7. Select **Create**.

### Step 4 optional Configure EdgeConnect

If you connect to a self-hosted Red Hat Ansible Automation Controller or AWX instance, you might require EdgeConnect to establish a connection behind your firewall.

To configure an EdgeConnect connection

1. Go to **Settings** >  **General** > **External Requests** > **EdgeConnect**.
2. Select  **New EdgeConnect**.
3. Enter **Name** for your EdgeConnect.
4. Enter **Host pattern** which is a URL.
5. Select **Create**.

You have a new EdgeConnect connection.

## Available actions

The following workflow actions are available for the Red Hat Ansible Automation integration.
Each action corresponds to an endpoint of the Red Hat Ansible API. For details on endpoints, see the [Ansible Tower API Reference Guideï»¿](https://dt-url.net/0w4392o).

Action

Description

Red Hat Ansible API endpoint

Launch job template

Launch a job template on Red Hat Ansible

`POST /api/v2/job_templates/{id}/launch/`   
Launch a Job Template

List job status

List job status on Red Hat Ansible

`GET /api/v2/jobs/{id}/`   
Retrieve a Job Host Summary

Relaunch job

Relaunch a job on Red Hat Ansible

`POST /api/v2/jobs/{id}/relaunch/`   
Relaunch a Job

## Launch a job template

To launch a job template, you need to provide the information listed below.

| Field | Description | Required |
| --- | --- | --- |
| TemplateId | The ID of the template that you want to launch | Required |
| ExtraVars | Extra variables to be used in the job template | Optional |

For details on the parameters, see the [Ansible Tower API Reference Guideï»¿](https://dt-url.net/0w4392o) (`/api/v2/job_templates/{id}/launch/` "Launch a Job Template").

To create a workflow that launches a job template

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to create a new workflow.
2. In the **Choose trigger** panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. On one of the information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), search for `Ansible`, and select **Launch job template**.
5. On each of the remaining information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") and drag the line to the **Launch job template** action.
6. In the **Launch job template** action, select the [connection](#connection) to your **Red Hat Ansible Automation Controller**.
7. Configure the input fields as needed. To learn how to use the output of information-extracting notes, see [Expression reference](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression").
8. To test your workflow, select **Run**.

## Troubleshooting

The following are solutions to problems some people have.

* [Red Hat Ansible for Workflows: Missing required fields errorï»¿](https://dt-url.net/sq237zw)
* [Red Hat Ansible for Workflows: Insufficient permissions errorï»¿](https://dt-url.net/3e63842)