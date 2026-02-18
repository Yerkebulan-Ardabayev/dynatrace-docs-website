---
title: Slack Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/slack
scraped: 2026-02-18T05:54:04.949649
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