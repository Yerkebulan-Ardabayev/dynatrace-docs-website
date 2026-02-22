---
title: Leverage enhanced endpoints for SDv1
source: https://www.dynatrace.com/docs/observe/application-observability/services/enhanced-endpoints-sdv1
scraped: 2026-02-22T21:10:47.377709
---

# Leverage enhanced endpoints for SDv1

# Leverage enhanced endpoints for SDv1

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Jan 19, 2026

With the **Enhanced endpoints for Service Detection v1 (SDv1)** feature, you can get full endpoint visibility for SDv1 services. When this feature is turned on, all endpoints are shown in [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") without requiring you to configure [key requests](/docs/observe/application-observability/services/services-concepts#key-requests "Understand application observability, services, and distributed tracing concepts."). This is consistent with the behavior already in place for [SDv2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") services.

The **Enhanced endpoints for SDv1** feature is turned on by default for the environments created in Dynatrace version 1.330+. For existing environments, the feature is available in Dynatrace version 1.333+.

No endpoints are created for [external services](/docs/discover-dynatrace/get-started/glossary#glossary-externalservice "Get acquainted with Dynatrace terminology.") and for the following SDv1 service types: [Background activity services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#background-activity-services "Understand the different types of services that can be detected and monitored in your environment."), [Queue listener services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#queue-listener-services "Understand the different types of services that can be detected and monitored in your environment."), and Key value store.

## Benefits

* **Complete endpoint visibility in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services****: Gain a complete list of endpoints for SDv1 services in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

  If you don't enable the **Enhanced endpoints for SDv1** feature, the **Endpoints** section in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** either remains empty or only shows key requests.
* **Improved service insights**: The list of endpoints enhances visibility into the service's behavior, enabling quick identification and resolution of issues.
* **Dedicated metrics for endpoints**: Detected endpoints feature [dedicated metrics](#metrics), which you can add to [dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and analyze for long-term endpoint history.

## Endpoint metrics

When the **Enhanced endpoints for SDv1** feature is turned on, Dynatrace starts collecting metrics for all detected endpoints of an SDv1 service in Grail.

The following metrics are collected for each endpoint:

* Failure rate
* Response time
* Throughput

These endpoint metrics are available not only in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** but also in other Dynatrace apps, such as [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

## Enable enhanced endpoints for SDv1

You can activate the **Enhanced endpoints for SDv1** feature for the entire environment or for a specific host group, Kubernetes namespace, and cluster.

Environment

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services**.
2. Under **Service detection v1**, select **Enhanced endpoints for SDv1**.
3. Turn on **Enable enhanced endpoints for SDv1**.

Host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. Close the overlay with the host group settings.
6. Go to **Process and contextualize** > **Services** > **Enhanced endpoints for SDv1**.
7. Turn on **Enable enhanced endpoints for SDv1**.

Kubernetes namespace or cluster

1. Go to ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Select the required namespace or cluster.
3. In the upper-right corner of the namespace or cluster details pane, select  (**Actions menu**) > **Service detection settings**.
4. Go to **Process and contextualize** > **Services** > **Enhanced endpoints for SDv1**.
5. Turn on **Enable enhanced endpoints for SDv1**.

Endpoint names are changed

Enabling the **Enhanced endpoints for SDv1** feature changes some request names and their associated endpoint names. For this reason, your existing API metric queries, dashboards, and configured alerts for the changed endpoints might be impacted, so you should reconfigure them. See [Changes to endpoint names](#changes-to-endpoint-names) for the details.

## View service endpoints

Service endpoints as well as the [related metrics](#metrics) are displayed in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, in the **Endpoints** section.

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** > **Explorer**.
2. Find and select the service for which you want to explore the endpoints.
3. On the **Overview** tab, scroll down to the **Endpoints** section.

From there, you can view the service endpoints, check the related endpoint metrics, view traces for each endpoint, and more. Select  (**Actions menu**) for the endpoint to view the available options.

![Services app showing the Endpoints section with four different endpoints and their metrics](https://dt-cdn.net/images/service-app-endpoints-section-3840-6f62930eb6.png)

## Changes to endpoint names

Enabling the **Enhanced endpoints for SDv1** feature changes some request names and their associated endpoint names. Check the flowchart and textual description below for the details.

Pre-existing key requests and request naming rules remain in effect

For all service types, the already existing [key requests](/docs/observe/application-observability/services-classic/monitor-key-requests "Discover how to closely monitor requests that are critical to your business.") and [request naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") continue to apply.

If you have set up key requests, the associated endpoints have the same names as their key requests. If you have configured request naming rules, they are also applied to the related endpoint names.

![Diagram - Changes to endpoint names](https://dt-cdn.net/images/enhanced-endpoints-sdv1-changes-to-endpoint-names-6993-563d8740fc.png)

When the **Enhanced endpoints for SDv1** feature is on, some endpoint names for [web request services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types#web-request-service "Understand the different types of services that can be detected and monitored in your environment.") and other service types are changed. This depends on whether there's an associated [request naming rule](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") and whether [volatile placeholder attributes](#volatile-placeholder-attributes) are used in these rules.

Endpoint names for web request services

Endpoint names for all other service types

**No request naming rule**

The following built-in rules are used for the endpoint names:[1](#fn-1-1-def)

1. `{http.request.method} {http.route}`
2. `{http.request.method} /*`

No change. The original request name is kept as the endpoint name.

**Request naming rule has no volatile placeholder attributes**

The placeholders are replaced with the corresponding values, and the template is fully applied.[2](#fn-1-2-def)

The placeholders are replaced with the corresponding values, and the template is fully applied.[2](#fn-1-2-def)

**Request naming rule contains volatile placeholder attributes**

The placeholder is not replaced, and the placeholder name is used in the endpoint name as is.[3](#fn-1-3-def)

The placeholder is not replaced, and the placeholder name is used in the endpoint name as is.[3](#fn-1-3-def)

1

For example, if the spans have no `{http.route}`, the endpoint name is `GET /*`.

2

For example, the `{HTTP-Method} - {Request:IsKeyRequest} - user authentication endpoint` template results in the `GET - yes - user authentication endpoint` endpoint name. Note that both `{HTTP-Method}` and `{Request:IsKeyRequest}` are replaced with their corresponding values (that is, `GET` and `yes`), as these are non-volatile placeholder attributes.

3

For example, the `{HTTP-Method} - {URL} - user authentication endpoint` template results in the `GET - {URL} - user authentication endpoint` endpoint name. Note that `{HTTP-Method}` (non-volatile placeholder attribute) is replaced with `GET` , while `{URL}` (volatile placeholder attribute) is not replaced and is used as is.

You can modify endpoint names by creating [custom naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#create-request-naming-rule "Adjust request naming and define the operations your services offer.").

### Volatile placeholder attributes

The volatile placeholder attributes are as follows:

* `{OneAgentAttribute:}` except `http.route`
* `{Relative-URL}`
* `{URL:Path}`
* `{URL:Query}`
* `{URL}`
* Customer-defined patterns based on one of the above-stated patterns

### Required actions

As some request names and their associated endpoint names change after you enable the **Enhanced endpoints for SDv1** feature, your existing API metric queries, dashboards, and configured alerts for the changed endpoints might be impacted. For this reason, you should reconfigure the affected entities.

## Static resource requests

Static resource requests include `Image`, `Binary`, `CSS`, and `JavaScript`.

When the **Enhanced endpoints for SDv1** feature is turned on, all static resource requests are unmuted and grouped into a single **Static resources** endpoint that has the same [metrics](#metrics) as other regular endpoints.

However, you can mute your static resource requests.

Whether the **Static resources** endpoint is muted or not, you can always go to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") to view and analyze spans like CSS, images, or binary.

### Mute static resource requests

To mute static resource requests, follow the steps described in [Mute monitoring of service requests](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.").

After you mute your static resource requests, the **Static resources** endpoint is not displayed in the endpoint list in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, and these requests don't count toward the overall service metrics.

### Manage resource request detection

You can add or edit filename extensions that count towards the **Static resources** endpoint. For details, see [Configure resource request detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#resource-request-detection "Adjust request naming and define the operations your services offer.").

Your existing configuration for resource request detection is still applicable, so if you have already added additional filename extensions, the corresponding requests should also become a part of the **Static resources** endpoint.