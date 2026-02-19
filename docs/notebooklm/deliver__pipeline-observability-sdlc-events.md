# Документация Dynatrace: deliver/pipeline-observability-sdlc-events
Язык: Русский (RU)
Сгенерировано: 2026-02-19
Файлов в разделе: 2
---

## deliver/pipeline-observability-sdlc-events/tutorials/deployment-observability-use-case-argocd.md

---
title: Observe Argo CD deployment and application health with Dashboards and SDLC events
source: https://www.dynatrace.com/docs/deliver/pipeline-observability-sdlc-events/tutorials/deployment-observability-use-case-argocd
scraped: 2026-02-17T04:58:38.274560
---

# Observe Argo CD deployment and application health with Dashboards and SDLC events

# Observe Argo CD deployment and application health with Dashboards and SDLC events

* Latest Dynatrace
* Tutorial
* 7-min read
* Updated on Jun 23, 2025
* Preview

In this use case, you'll

* Integrate [Argo CDï»¿](https://argo-cd.readthedocs.io/en/stable) and Dynatrace.
* Use Dashboards to observe Argo CD deployments and application health.
* Use this information to optimize deployments with Argo CD.

Below is an example of what your Argo CD dashboard could look like.

![A screenshot of the Dynatrace ArgoCD Application Lifecycle.](https://dt-cdn.net/images/argocd-sync-deployment-overview-2892-ac512e11e1.png)

## Concepts

Software Development Lifecycle (SDLC) events
:   [SDLC events](/docs/deliver/pipeline-observability-sdlc-events#sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.")

Why were Argo CD notifications changed into SDLC events?
:   The main benefits are data normalization, being tool-agnostic, and not relying on specific tools.
    As a result, Dynatrace Dashboards, Apps, and Workflows can build on [SDLC events](/docs/deliver/pipeline-observability-sdlc-events#sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.") with well-defined properties rather than tool-specific details.

## Target audience

This tutorial is intended for platform engineers who manage the Internal Development Platform (IDP), including Argo CD, in GitOps-based deployments.

## Learning outcome

In this tutorial, you'll learn how to

* Forward Argo CD notifications to Dynatrace.
* Send Prometheus metrics to Dynatrace.
* Normalize the ingested event data.
* Use Dashboards to analyze the data and derive improvements.

If you prefer, you could follow the [Argo CD tutorial directly on GitHubï»¿](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples/blob/main/argocd_observability/README.md).

## Prerequisites

[Install Dynatrace Configuration as Code via Monaco](/docs/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.")

## How-to

1. Setup: Prepare the Monaco configuration

1. [Create an OAuth client for the Dynatrace Monaco CLI](/docs/deliver/configuration-as-code/monaco/guides/create-oauth-client "Create an OAuth client for Dynatrace Configuration as Code via Monaco.") with the following permissions

   * Run apps: `app-engine:apps:run`
   * View OpenPipeline configurations: `openpipeline:configurations:read`
   * Edit OpenPipeline configurations: `openpipeline:configurations:write`
   * Create and edit documents: `document:documents:write`
   * View documents: `document:documents:read`
2. Store the retrieved client ID and secret as separate environment variables.

   Windows

   Linux

   `$env:OAUTH_CLIENT_ID='<YOUR_CLIENT_ID>'`

   `$env:OAUTH_CLIENT_SECRET='<YOUR_CLIENT_SECRET>'`

   `export OAUTH_CLIENT_ID='<YOUR_CLIENT_ID>'`

   `export OAUTH_CLIENT_SECRET='<YOUR_CLIENT_SECRET>'`
3. Clone the [Dynatrace configuration as code sampleï»¿](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples) repository and go to `argocd_observability` directory.

   ```
   git clone https://github.com/Dynatrace/dynatrace-configuration-as-code-samples.git



   cd dynatrace-configuration-as-code-samples/argocd_observability
   ```
4. Edit the `manifest.yaml` by exchanging your environment ID `<YOUR-DT-ENV-ID>` placeholder with your Dynatrace environment ID at the name property and within the URL of the value property.

   ```
   manifestVersion: 1.0



   projects:



   - name: pipeline_observability



   environmentGroups:



   - name: group



   environments:



   - name: <YOUR-DT-ENV-ID>



   url:



   type: value



   value: https://<YOUR-DT-ENV-ID>.apps.dynatrace.com



   auth:



   oAuth:



   clientId:



   name: OAUTH_CLIENT_ID



   clientSecret:



   name: OAUTH_CLIENT_SECRET
   ```

2. Setup: Check the OpenPipeline configuration for SDLC events

These steps modify the OpenPipeline configuration for [SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.").
If your OpenPipeline configuration contains only default/built-in values, you can directly apply the Monaco configuration.
If you have any custom ingest sources, dynamic routes, or pipelines, you'll first need to download your configuration and manually merge it into the Monaco configuration.

Step 3 will indicate if a configuration merge is needed or if you can apply the provided configuration directly.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Events** > **Software development lifecycle**.
2. Check the **Ingest sources**, **Dynamic routing**, and **Pipelines**.

   * Under **Ingest sources**, are there any other sources than **Default API**?
   * Under **Dynamic routing**, are there any other routes than **Default route**?
   * Under **Pipelines**, are there any other pipelines than **events.sdlc**?
3. If the answer to one of those questions is "yes", follow the steps below. Otherwise, skip ahead to step 4.

   * Download the OpenPipeline configuration.

     `monaco download -e <YOUR-DT-ENV-ID> --only-openpipeline`
   * Open the following files:

     + Your downloaded configuration file, `download_<DATE>_<NUMBER>/project/openpipline/events.sdlc.json`.
     + The provided configuration file, `pipeline_observability/openpipline/events.sdlc.argocd.json`.
   * Merge the contents of `events.sdlc.json` into `events.sdlc.argocd.json`, and then save the file.
4. Apply the Monaco configuration.

   The configuration consists of

   * Dashboards to analyze Argo CD activities.
   * OpenPipeline configuration to normalize [Argo CD notificationsï»¿](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/) into [SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.").

   Run this command to apply the provided Monaco configuration:

   `monaco deploy manifest.yaml`

3. Setup: Create an access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

7. Select these scopes:

   * **OpenPipeline - Ingest Software Development Lifecycle Events (Built-in) (`openpipeline.events_sdlc`)**
   * **OpenPipeline - Ingest Software Development Lifecycle Events (Custom) (`openpipeline.events_sdlc.custom`)**

4. Setup: Configure Argo CD notifications

[Argo CD notificationsï»¿](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/) provide a flexible way to alert users about essential changes in the state of their applications managed by Argo CD. To configure the Argo CD notifications, you need to create a notification secret, apply the configuration, and subscribe applications to notifications.

1. Create notification secret.

   1. Update the `argocd-notifications-secret` with:

      ```
      apiVersion: v1



      kind: Secret



      metadata:



      name: argocd-notifications-secret



      stringData:



      dt-base-url: https://{your-environment-id}.live.dynatrace.com



      dt-access-token: <YOUR-ACCESS-TOKEN>
      ```
   2. Apply the configuration.

      `kubectl apply -f <secret_file_name>.yaml -n argocd`
2. Create a notification template and trigger.

   1. If you don't have any notification configurations, create a new configuration map called `argocd-notification-cm` as shown below. Otherwise, extend your config map configuration by adding the example's service, template, and trigger sections.

      ```
      apiVersion: v1



      kind: ConfigMap



      metadata:



      name: argocd-notifications-cm



      data:



      service.webhook.dynatrace-webhook: |



      url: $dt-base-url



      headers:



      - name: "Authorization"



      value: Api-Token $dt-access-token



      - name: "Content-Type"



      value: "application/json; charset=utf-8"



      template.dynatrace-webhook-template: |



      webhook:



      dynatrace-webhook:



      method: POST



      path: /platform/ingest/custom/events.sdlc/argocd



      body: |



      {



      "app": {{toJson .app}}



      }



      trigger.dynatrace-webhook-trigger: |



      - when: app.status.operationState.phase in ['Succeeded'] and app.status.health.status in ['Healthy', 'Degraded']



      send: [dynatrace-webhook-template]



      - when: app.status.operationState.phase in ['Failed', 'Error']



      send: [dynatrace-webhook-template]



      - when: app.status.operationState.phase in ['Running']



      send: [dynatrace-webhook-template]
      ```

      Here is an explanation for the naming in the configuration.

      * `dynatrace-webhook` is the name of the service, `$dt-access-token` refers to the Dynatrace access token, and `$dt-base-url` is a reference to the Dynatrace event ingest endpoint stored in the `argocd-notifications-secret secret`.
      * `dynatrace-webhook-template` is the template's name, and `dynatrace-webhook` refers to the service created above.
      * `dynatrace-webhook-trigger` is the trigger's name, and `dynatrace-webhook-template` refers to the template created above.
   2. Apply the configuration with this command.

      `kubectl apply -f <config_map_file_name>.yaml -n argocd`
   3. Subscribe applications to notifications.

      Modify the annotations of the Argo CD application by using either the Argo CD UI or the [Argo CD application definitionï»¿](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#applications) with the following annotations:

      ```
      apiVersion: argoproj.io/v1alpha1



      kind: Application



      metadata:



      annotations:



      notifications.argoproj.io/subscribe.dynatrace-webhook-trigger.dynatrace-webhook: ""
      ```

      The added `notifications.argoproj.io` notification annotation subscribes the Argo CD application to the notification setup you created above.

5. Setup: Send Argo CD Prometheus metrics to Dynatrace

Argo CD exposes different sets of Prometheus metrics for different services.
Configure your Argo CD services to expose this information so that it can be collected by Dynatrace.
You can use either [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), which is installed on the Kubernetes cluster that hosts Argo CD, or the [Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.").

To use [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")

1. Enable [Prometheus metrics monitoring](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

   1. Go to **Kubernetes** and select the monitored cluster with Argo CD installation.
   2. In the upper-right corner, go to  > **Connection settings**.
   3. Choose **Monitoring Settings**.
   4. Enable **Monitor annotated Prometheus exporters**.
   5. **Save**.
2. In your Argo CD installation namespace, add the following two annotations for each of the services listed in the table below.
   Replace `{METRICS_PORT}` with the corresponding port number.

   ```
   metrics.dynatrace.com/port: {METRICS_PORT}



   metrics.dynatrace.com/scrape: 'true'
   ```

   | Service | Metrics Port |
   | --- | --- |
   | argocd-applicationset-controller | 8080 |
   | argocd-metrics | 8082 |
   | argocd-server-metrics | 8083 |
   | argocd-repo-server | 8084 |
   | argocd-notifications-controller-metrics | 9001 |
   | argocd-dex-server | 5558 |

   View the [histogramï»¿](https://www.dynatrace.com/news/blog/opentelemetry-histograms-reveal-patterns-outliers-and-trends/) data ingest by going to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Metrics** > **Histograms**. The **Ingest complete explicit bucket histograms** setting that you need is automatically turned on.

6. Unlock enhanced deployment insights with Argo CD Dashboards

Now that you've successfully configured Argo CD and Dynatrace, you can use Dashboards and SDLC events to observe your Argo CD deployments.



### Analyze

In Dynatrace, open the **ArgoCD Application Lifecycle** dashboard to

* Investigate running syncs and hotspots of many sync operations.
* Analyze the duration of sync operations.
* See deployment status and application health.

### Optimize

Leverage those insights for the following improvement areas:

* Improved performance: Optimizing syncs can reduce the time it takes to deploy changes, making your deployment process more efficient. Efficient syncs can also help better utilize resources, reducing the load on your infrastructure.
* Enhanced Reliability: Optimizing syncs can minimize the chances of errors during deployment, leading to more stable and reliable releases.
  Ensuring that syncs are optimized can help maintain consistency across different environments.

### Continuous improvements

Regularly review your Argo CD sync operations and adjust the configuration to ensure they're optimized for performance.

In Dynatrace, adjust the timeframe of the **ArgoCD Application Lifecycle** dashboards to monitor the long-term impact of your improvements.

## Call to action

We highly value your insights on Argo CD observability. Your feedback is crucial in helping us enhance our tools and services. Visit the Dynatrace Community page to share your experiences, suggestions, and ideas directly in [Feedback channel for CI/CD Pipeline Observabilityï»¿](https://community.dynatrace.com/t5/Platform-Engineering/Feedback-channel-for-CI-CD-Pipeline-Observability/m-p/269193).

## Further reading

* [Observability throughout the software development lifecycle increases delivery performanceï»¿](https://www.dynatrace.com/news/blog/observability-throughout-the-software-development-lifecycle/)
* [Pipeline observability](/docs/deliver/pipeline-observability-sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.")

## Related topics

* [How to ingest data (events)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")
* [Software development lifecycle (SDLC) events](/docs/semantic-dictionary/model/sdlc-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.")
* [Ingest SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Auto-update for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach.")

---

## deliver/pipeline-observability-sdlc-events/tutorials/pipeline-observability-tutorial-jira.md

---
title: Optimize engineering flow metrics using Jira data
source: https://www.dynatrace.com/docs/deliver/pipeline-observability-sdlc-events/tutorials/pipeline-observability-tutorial-jira
scraped: 2026-02-18T21:30:47.477966
---

# Optimize engineering flow metrics using Jira data

# Optimize engineering flow metrics using Jira data

* Latest Dynatrace
* Tutorial
* 7-min read
* Published Oct 21, 2025
* Preview

In this tutorial, you set up the integration between Jira and Dynatrace to ingest a daily snapshot of your Jira epics into Dynatrace.
You analyze your value delivery system from the highest point of view.
By default, these are epics in Jira.
We provide you with a dashboard that you populate with your Jira data, enabling you to optimize your engineering flow by making data-driven decisions that improve focus, predictability, and value delivery lead times.

Below is a screenshot with highlights from the **Engineering Flow Metrics** dashboard.

![A screenshot with highlights of sections of the Engineering Flow Metrics dashboard.](https://dt-cdn.net/images/20251128-engineering-flow-metrics-dashboard-on-playground-highlights-3065-0660cc0d38.png)

## Concepts

Software Development Lifecycle (SDLC) events
:   [SDLC events](/docs/deliver/pipeline-observability-sdlc-events#sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.") within the Software Development Lifecycle (SDLC) play a pivotal role in achieving effective pipeline observability.
    They represent key actions that occur throughout the lifecycle â such as releasing a new software version, deploying that version, or successfully passing a performance test.
    For more information, see [Semantic Dictionary SDLC events](/docs/semantic-dictionary/model/sdlc-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.")

## Target audience

The **Engineering Flow Metrics** dashboard is intended for:

* Senior leaders and decision-makers who require a high-level view of the value streams to align business objectives with delivery outcomes.
* Development teams, product owners, product managers, agile coaches, and engineering managers who use Jira to get insights about their team's progress.

## Prerequisites

* Access to the Jira Cloud instance.
* You have an [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the `OpenPipeline - Ingest Software Development Lifecycle Events (Built-in)` scope.

## How-to

1. Jira: Configure a quick filter

In Jira, configure a quick filter to get a `<filter-id>` for the scheduled [Jira automationï»¿](https://www.atlassian.com/software/jira/guides/automation/overview#board-vs-project).

1. Go to your Jira instance and [configure a Jira quick filterï»¿](https://support.atlassian.com/jira-software-cloud/docs/configure-quick-filters/).

   To monitor epics in Jira, you can use the following JQL query as an example.

   ```
   type = Epic AND project = <your-project-name> AND (resolved is EMPTY or resolved > -2w)
   ```
2. Select **Copy filter**.
   The **Copy filter** dialog opens.
3. Enter the name of the filter in **Name**.
4. Select who can view in the **Viewers** drop-down list.

   The filter needs to be visible to the actor of the automation.
   To be on the safe side, set the permission so that everybody can see the filter.

   For more information on actors in Jira automation, see [What is a rule actor?ï»¿](https://support.atlassian.com/cloud-automation/docs/what-is-a-rule-actor/).
5. Select **Save**.
6. Get the filter ID from the Jira URL.
   The format is similar to `/issues/?filter=<filter-id>`, for example, `?filter=12345`

2. Dynatrace: Copy Endpoints path

You need the **Endpoints path** to configure the scheduled Jira automation.

To find and copy the **Endpoints path**:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Software development lifecycle**.
2. In the **Ingest sources** tab > **Endpoints path** tab, hover over the **Endpoints path**.
3. From the  dot menu of the source, select  **Copy** to copy the **Endpoints path**.

3. Jira: Set up a trigger for scheduled Jira automation

Data is stored as events in Dynatrace.
Thus, the data is charged as Events powered by Grail.
For more information on the cost of Events powered by Grail, see [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

To populate Dynatrace with Jira data, set up a Jira automation.

1. Go to Jira and open your Jira project.
2. Select **Project settings**.
3. On the left side, select **Automation**.
4. Select **Create rule**.
   Start with an empty Jira automation rule, allowing you to configure the correct fields.
5. Select the **Scheduled** trigger.
   For more information, see [Jira automation triggersï»¿](https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/) and [Jira Automation: Set 'Scheduled' as a trigger and use multiple actionsï»¿](https://confluence.atlassian.com/automationkb/automation-set-scheduled-as-a-trigger-and-use-multiple-actions-1388151419.html).
6. In the **Occurrence** field, to trigger nightly, for example, at 4:00 AM.

   1. In the **Run rule every** field, set the **Scheduled** trigger to `1`.
   2. In the **Run rule every** field, select **Days**.
   3. In the **At** field, set the time to `4:00 AM`.
   4. In the **At** field, select the time zone.
7. Select the **Run a JQL search and execute actions for each work item in the query** checkbox.
8. Required In the **JQL** field, enter the filter you created earlier as `filter=<filter-id>`.
   Replace `<filter-id>` with the ID of the filter that you created earlier.

   Make sure that **Only include work items that have changed since last time** is not selected.
9. Select **Next** to finish the configuration of the scheduled trigger.

4. Jira: Start setting up the Send web request action for Jira automation

As part of the Jira automation, you need to set up a Jira **Send web request** action.
This action sends an HTTP request to the URL specified.

1. Add a [**Send web request** actionï»¿](https://confluence.atlassian.com/automation074/actions-1141481289.html#Actions-sendwebrequest).
2. Enter your **Web request URL** from the [Dynatrace: Copy Endpoints path step](/docs/deliver/pipeline-observability-sdlc-events/tutorials/pipeline-observability-tutorial-jira#copy "Stabilize your value delivery system by making data-driven decisions that improve focus, predictability, and value delivery lead times.").
   The pattern is `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.sdlc`.
3. In the **HTTP method** field, select **POST**.
4. In the **Web request body**, select **Custom data**.
5. In the **Headers** section, set the following **Key** and **Value** pairs:

   1. **Content-Type** to `application/json`.
   2. **Authorization** to `Api-Token <your-API-token>`.
   3. **accept** to `application/json; charset=utf-8`.
6. Replace `<your-API-token>` with your Dynatrace API access token that you generated in the earlier step.

5. Jira: Find Rank and Team Jira field IDs

You need to find the automatically created **Rank** and **Team** Jira field IDs that are specific to your Jira instance so that you can use them for analytics in the next step.

In your browser, to find the Jira fields, make a call to the Jira API on any issue in your project.

1. Enter the following URL `https://<your-endpoint>.atlassian.net/rest/api/2/issue/<your-issue>?expand=names` into your browser.
   Replace `<your-endpoint>` with your URL.
   Replace `<your-issue>` with any of your issue keys.
2. Open the URL.
   This request returns a JSON output to the browser.
3. Search for the custom fields **Rank** and **Team**.
   You can use the custom field ID in the Jira Automation to send the data to your dashboard.

   The field format is `customfield_xxxxx` where `xxxxx` is the field ID.
   The code block below shows an example of the JSON response body, including custom field IDs.

   ```
   {



   "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",



   "id": "10000",



   "self": "https://<your-endpoint>.atlassian.net/rest/api/2/issue/10000",



   "key": "SCRUM-1",



   "names": {



   "customfield_10001": "Team",



   "customfield_10019": "Rank"



   }



   }
   ```

6. Jira: Finish setting up the Send web request action for Jira automation

Add the custom field IDs of the automatically created **Rank** and **Team** Jira fields to the **Custom data** field of your Jira **Send web request** action.

1. Go to your Jira Automation.
2. In the **Custom data** field, enter the following template for generating JSON from JIRA issue data:

   ```
   {



   "specversion": "1.0"



   , "id": "{{issue.key}}"



   , "source": "JIRA"



   , "day": "{{now.jiraDate}}"



   , "version": "1"



   , "key": "{{issue.key}}"



   , "summary": {{issue.summary.asJsonString()}}



   , "type": "{{issue.issuetype.name}}"



   {{#exists(issue.assignee)}}



   , "assignee": "{{issue.assignee.displayName}}"



   {{/}}



   {{#exists(issue.customfield_<your-team-custom-field-id>)}}



   , "team": "{{issue.customfield_<your-team-custom-field-id>.name}}"



   {{/}}



   , "status": "{{issue.status.name}}"



   , "status_category": "{{issue.status.statuscategory.name}}"



   {{#exists(issue.resolution)}}



   , "resolution": "{{issue.resolution.name}}"



   {{/}}



   {{#if(not(issue.labels.isEmpty))}}



   , "labels": [



   {{#issue.labels}}



   "{{.}}" {{^last}},{{/}}



   {{/}}



   ]



   {{/}}



   {{#if(equals(issue.fixVersions.size, 1))}}



   {{#issue.fixVersions}}



   , "fix_version": "{{name}}"



   , "fix_version.release_date": "{{releaseDate.format("yyyy-MM-dd")}}"



   {{/}}



   {{/}}



   , "created": "{{issue.created}}"



   , "status_changed_on": "{{issue.statuscategorychangedate}}"



   , "resolved": "{{issue.resolved}}"



   , "rank": "{{issue.customfield_<your-rank-custom-field-id>}}"



   , "project": "{{issue.project.key}}"



   }
   ```

   This example uses [Jira smart valuesï»¿](https://support.atlassian.com/cloud-automation/docs/smart-values-in-jira-automation/) to extract the required information and ingest it into Dynatrace.  
   `{{#if(equals(issue.fixVersions.size, 1))}}` implies that the Jira epic has only one fix version.
3. Replace `<your-rank-custom-field-id>` with the **Rank** custom field ID.
4. Replace `<your-team-custom-field-id>` with the **Team** custom field ID.
5. Select **Next** to finish the configuration of the **Send web request** action.
6. Select **Turn on rule** to save the automation.
7. Enter the **Name** for the Jira Automation.
8. Select **Turn on rule** to save.

7. Organize data

To organize the data in Dynatrace, set up a [custom Grail bucket](/docs/platform/grail/organize-data#custom-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

1. In Dynatrace, go to **Settings** > **Storage management** > **Bucket storage management**.
2. Select  **Bucket**.
3. In the **New bucket** dialog, enter the **Bucket name** and the **Display name**. Use `jira_events` because the sample dashboard expects this name.
4. Set the **Bucket table type** to **events**.
5. Set the **Retention period** to three years in days which is `1095` days.
6. Select **Create**.

If the data should be restricted, configure the [bucket permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

8. Route data

To route the data into the custom bucket, set up an SDLC pipeline.

1. Go to **Settings** > **Process and contextualize** > **OpenPipeline** > **Software development lifecycle**.
2. Go to the **Pipelines** tab.
3. Select  **Pipeline**.
4. Enter a pipeline **Name**.
5. Go to the **Storage** tab.
6. Select  **Processor** > **Bucket assignment**.
7. Enter a **New Processor** **Name**, for example, `Jira Daily Snapshot`.
8. Set the **Matching condition** to `source == "JIRA"`.
9. In the **Storage** drop-down list, select your bucket from the previous step.
10. Select **Save**.
11. Go to the **Dynamic routing** tab.
12. Select  **Dynamic routing**.
13. In the **Add a new dynamic route** dialog, enter the **Name** of the new dynamic route.
14. In the **Matching condition**, enter `source == "JIRA"`.
15. Select from the **Pipeline** drop-down your custom pipeline.
16. Select **Add**.
17. Select **Save**.

All events created by the Jira automation are added to the bucket.
For more general information, see [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline.").

9. Verify setup

This step is about verifying your Jira and Dynatrace setup.

1. Run the Jira automation manually to verify the automation rule.
2. Query the events via DQL, for example, in **Notebooks**, to verify that your events have been ingested successfully.

   1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
   2. Choose or create a notebook.
   3. Select ![Grail](https://cdn.bfldr.com/B686QPH3/at/kc3c7k476pbx2pb8cphzktf/Grail.svg?auto=webp&width=72&height=72 "Grail") DQL to add a new section with a DQL query input field.
   4. Enter the following DQL query:

      ```
      fetch events



      | filter dt.system.bucket == "jira_events"
      ```

This query returns data after the automation ran successfully.

10. Use the Engineering Flow Metrics dashboard for analysis

We're providing you with a ready-made dashboard.

To find and use the dashboard:

1. Go to the [Engineering Flow Metrics dashboard on Playgroundï»¿](https://dt-url.net/e0032zt).
2. [Download](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-download "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") the dashboard.
3. [Upload](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") the dashboard to your environment.

   You need to adjust the start date of specific queries to match the start of your data ingestion which we explain in detail in the **Hard-Coded Dates** section of the dashboard.

   The sections **Epic Throughput**, **Lead Time**, and **Implementation Aging Chart** are populated immediately after the first data import.

   After the daily snapshot data is available for at least two weeks, you can do the analysis with the help of different sections of the dashboard, for example, **Epic Burndown**, **Cumulative Flow Diagram**, **Work In Progress**, **Backlog Stability**, and **Changes**.

   The dashboard shows:

   * **Epic Throughput**:
     Historical throughput is shown in grey and is based on the **Fix Version**.
     The epics planned in the future are shown in blue, based on the **Fix Version** year quarters.
     The thin green line shows the average of the last four complete quarters.
     The table in the dashboard displays the difference from the average for each quarter.
   * **Epic Burndown**:
     The burndown shows Jira epics per status over time.
     The charts are based on a weekly schedule, using the latest available data point for each week.
   * **Lead Time**:
     Time between creation and resolution of the epic.
     Epics that were closed within a quarter are considered.
   * **Implementation Aging Chart**:
     Time in implementation.
     One month is 30 days.
   * **Cumulative Flow Diagram**:
     Number of Jira epics per status over time.
     Closed epics disappear after two weeks.
   * **Work In Progress**:
     Epics **In Progress**.
   * **Backlog Stability**:
     Shows the top 35 epics in the backlog.
     One line represents one epic.
     A line in the diagram starts when an epic is created, and the line ends as soon as the epic is closed, with the status set to **Closed**.
     Epics below the top 35 are collapsed into one line at the bottom of the chart.
     If lines are crossing each other, priorities have changed.
   * **Changes in the last 2 weeks**:
     Changes to the fields **Status**, **Fix Version**, and **Assignee** are shown.



## Next steps

You now have the dashboard, which allows you to view the metrics and start optimizing your value delivery flow.
The dashboard serves as a starting point; you can extend or refine it based on your specific needs.

Below is a full screenshot of the **Engineering Flow Metrics** dashboard.

![A screenshot of the Engineering Flow Metrics dashboard.](https://dt-cdn.net/images/20251128-engineering-flow-metrics-dashboard-on-playground-3065-68560a9b6d.png)

## Related topics

* [Software development lifecycle (SDLC) events](/docs/semantic-dictionary/model/sdlc-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.")
* [Ingest SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")
* [Analyze SDLC events from your pipeline](/docs/deliver/pipeline-observability-sdlc-events/pipeline-observability-analyze "Analyze your pipeline using data from your software development lifecycle (SDLC) events  using our examples.")

---
