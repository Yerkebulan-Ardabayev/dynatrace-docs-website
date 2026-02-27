---
title: PagerDuty
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/pagerduty
scraped: 2026-02-27T21:31:38.521293
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