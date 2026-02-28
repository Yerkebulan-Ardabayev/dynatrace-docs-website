---
title: Red Hat Event-Driven Ansible
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-even-driven-ansible
scraped: 2026-02-28T21:25:57.883348
---

# Red Hat Event-Driven Ansible

# Red Hat Event-Driven Ansible

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on May 06, 2025
* Preview

Preview

When you integrate your Dynatrace environment with Red Hat Event-Driven Ansible controller using Red Hat Ansible Connector ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows"),
you can automatically send events to the Event-Driven Ansible Controller by using the dt\_webhook event source plugin.

## Configure the integration

To use Red Hat Ansible workflow actions, you first need to install Red Hat Ansible Connector ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows") from Dynatrace Hub.

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select **Red Hat Ansible**.
2. Select **Install** and then follow the process below to set up your Event-Driven Ansible environment, grant permissions, and configure the connection.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Set up Event-Driven Ansible controller for integration with Dynatrace**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-even-driven-ansible#setup-eda "Send events to Red Hat Event-Driven Ansible")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Grant permissions to Workflows**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-even-driven-ansible#permissions "Send events to Red Hat Event-Driven Ansible")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure Red Hat Event-Driven Ansible connection**](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-even-driven-ansible#connection "Send events to Red Hat Event-Driven Ansible")

### Step 1 Configuration of Event-Driven Ansible controller

For more information on the Event-Driven Ansible Controller, see [Event-Driven Ansible controller user guideï»¿](https://dt-url.net/7xg3n92).

#### Project configuration

For more information on how to configure a project, see [Event-Driven Ansible controller user guideï»¿](https://dt-url.net/p1i3n2u).

#### Event-Driven Ansible with simplified event routing (event streams)

##### Prerequisites

* Red Hat Ansible Automation Platform 2.5+

#### Setting up a decision environment

When using event streams, you can use the standard decision environment provided by Red Hat, for example, the [Ansible-rulebook default-deï»¿](https://dt-url.net/oq03zp2).
You don't need to build a custom decision environment when using event streams.

##### Credential configuration

Before creating the event stream, you need to set up the credentials for token authentication.

1. In the Ansible Automation Platform Dashboard navigation panel, select **Automation Decisions** > **Infrastructure** > **Credentials**.
2. Select **Create credential**.
3. Enter the following credential details.

For more information on how to set up a credential, see [Setting up a credentialï»¿](https://dt-url.net/6c23znj) in the Red Hat documentation.

##### Event stream configuration

After the credential is configured, you can create an event stream.

1. In the Ansible Automation Platform navigation panel, select **Automation Decisions** > **Event streams**.
2. Select **Create event stream**.
3. Enter the following event stream details.

For more information on how to set up an event stream, see [Simplified event routingï»¿](https://dt-url.net/sv63zyi) in the Red Hat documentation.

##### Rulebook activation

The final step is to attach the created event stream to a rulebook activation.

1. From the navigation panel on your Event-Driven Ansible Controller, select **Rulebook Activations**.
2. Select **Create rulebook activation** and enter the required fields.
3. Select the event stream:

   1. Select the gear icon and select `_SOURCE_1` from the list.
   2. Select the event stream you created in the step before and save it.

   For more information on attaching an event stream to a rulebook activation, see [Attaching event streams to activationsï»¿](https://dt-url.net/tka3z5c) in the Red Hat documentation.

When the rulebook activation is enabled, events can be sent from the workflow action to the Event-Driven Ansible Controller.

For more information on configuring a rulebook activation on the Event-Driven Ansible controller, see [Setting up a rulebook activationï»¿](https://dt-url.net/ev63nil) in the Red Hat documentation.

#### Event-Driven Ansible without simplified event routing (event streams)

#### Prerequisites

The collection [dynatrace.event\_driven\_ansibleï»¿](https://dt-url.net/9le3nc2) that contains **dt\_webhook** must be installed within a decision environment on the Event-Driven Ansible Controller.

#### Setting up a decision environment

For more information on how to set up a new decision environment, see [Event-Driven Ansible controller user guideï»¿](https://dt-url.net/p603rfl).

#### Event source plugin and rulebook configuration

A rulebook activation is used to enable an event source. Hence, it is necessary to set up a rulebook.

The rulebook should be located in the configured project repository in the directory `/rulebooks`. For more information, see [Event-Driven Ansible rulebook exampleï»¿](https://dt-url.net/qr03nps).

The first part of the rulebook is the configuration of the event source (source plugin). The second part of the rulebook configuration contains the actual rules. A rule includes conditions and actions.

**Example rulebook for dt\_webhook**

To use the [dt\_webhookï»¿](https://dt-url.net/5w23n6c) plugin, you need to configure it as a source in your rulebook. The following arguments must be set.

* `host`

  + This can be, for example, a localhost or 0.0.0.0.
* `port`

  + Configure the port which will be used from the source plugin to listen for events.
  + Hints:

    - The API URL in **Red Hat Event-Driven Ansible Connection** has the same `port` as defined here.
    - [Prerequisiteï»¿](https://dt-url.net/fu43nbr) for the port configuration.
* `token`

  + Define a variable name for the token here, for example `dt_webhook_token`.
  + Hints:

    - This token variable will be set in the rulebook activation later on the Red Hat Event-Driven Ansible Controller.
    - `dt_webhook_token` is just an example name for the token variable. It could be also another name but the name must be the same in the rulebook activation and rulebook configuration.

  ```
  ---



  - name: Listen for events on dt_webhook



  hosts: all



  sources:



  - dynatrace.event_driven_ansible.dt_webhook:



  host: 0.0.0.0



  port: 5000



  token: '{{ dt_webhook_token }}'



  rules:



  - name: API Endpoint not available



  condition: event.payload.eventData["event.name"] is match ("Monitoring not available")



  action:



  run_job_template:



  name: "Trigger test playbook"



  organization: "Default"
  ```

When the rulebook configuration is done, ensure your project repository is synchronized to the Event-Driven Ansible Controller by selecting **Sync project** in the project list.

![Sync projects](https://dt-cdn.net/images/eda-project-sync-1917-a8723ab2bc.webp)

The next step then is to configure the rulebook activation. Select **Rulebook Activations** from the navigation panel on your Event-Driven Ansible Controller.
Select **Create rulebook activation** and fill in the required fields.

In the field **Variables** you define the token by setting your token variable from the **Rulebook configuration**. The rulebook variables are in a JSON/YAML format.

Ensure the variable name is identical in the rulebook activation and rulebook configuration.

![Configure a rulebook activation](https://dt-cdn.net/images/eda-rulebook-activation-1918-d3fc9c9876.webp)

For more information on configuring a rulebook activation on the Event-Driven Ansible controller, see [Setting up a rulebook activationï»¿](https://dt-url.net/ev63nil).

When the rulebook activation is enabled, events can be sent from the workflow action to the Event-Driven Ansible Controller.

### Step 2 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

* `app-settings:objects:read`
* `state:app-states:read`
* `state:app-states:write`
* `state:app-states:delete`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 3 Configure Red Hat Ansible connection



You need a configured connection for your Red Hat Event-Driven Ansible environments.

This connection connects to the dt\_webhook plugin within Red Hat Event-Driven Ansible. Open a specific port on your firewall to ensure the plugin is accessible for these connections.
If this is impossible, you can use [EdgeConnectï»¿](https://dt-url.net/at03rhn) to tunnel the traffic and make the environment accessible.

To configure a connection for the **Red Hat Event-Driven Ansible Controller**

1. Go to **Settings** and select **Connections** > **Connectors** > **Red Hat Ansible**.
2. Select the tab **Event-Driven Ansible**.
3. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**.
4. Provide a meaningful name for your connection.
5. Select if you would like to use event stream
6. Provide your Red Hat Event-Driven-Ansible Controller URL,

   * when not using event stream, `http://your-eda-controller.redhat.com:your-port` (must include the `port`, which is configured in the Ansible Rulebook).
   * when using event stream, `http://your-aap.redhat.com/eda-event-streams/api/eda/v1/external_event_stream/a-uuid/post`.
7. Provide your token of the Red Hat Event-Driven Ansible source plugin.
8. Select **Create**.

## Available action

The following workflow action is available for the Red Hat Event-Driven Ansible controller.

## Send event to Event-Driven Ansible

To send an event to Event-Driven Ansible in your workflow, you need to provide the information listed below.

| Field | Description | Required |
| --- | --- | --- |
| Event data | The event data to be sent as valid JSON | Optional |

To create a workflow that sends an event to Event-Driven Ansible

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to create a new workflow.
2. In the **Choose trigger** panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. On one of the information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add"), search for `Ansible`, and select **Send event to Event-Driven Ansible**.
5. On each of the remaining information-extracting nodes, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") and drag the line to the **Send event to Event-Driven Ansible** action.
6. In the **Send event to Event-Driven Ansible** action, select the [connection](#connection) to your **Red Hat Event-Driven Ansible Controller**.
7. Configure the event data field as needed. To learn how to use the output of information-extracting notes, see [Expression reference](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression").

   The event data must be valid JSON.
8. To test your workflow, select **Run**.