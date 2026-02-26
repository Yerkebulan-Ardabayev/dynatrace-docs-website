---
title: Observe Argo CD deployment and application health with Dashboards and SDLC events
source: https://www.dynatrace.com/docs/deliver/pipeline-observability-sdlc-events/tutorials/deployment-observability-use-case-argocd
scraped: 2026-02-26T21:26:19.235012
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