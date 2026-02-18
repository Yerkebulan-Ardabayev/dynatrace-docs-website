# Документация Dynatrace: deliver/site-reliability-guardian
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 4
---

## deliver/site-reliability-guardian/event-structure.md

---
title: Site Reliability guardian event structure
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/event-structure
scraped: 2026-02-16T21:29:05.232559
---

# Site Reliability guardian event structure

# Site Reliability guardian event structure

* Latest Dynatrace
* Reference
* 4-min read
* Published Oct 24, 2025

Depending on the type of [guardian](/docs/deliver/site-reliability-guardian#guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") â [Lifecycle guardian](/docs/deliver/site-reliability-guardian#lifecycle-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") or [Business guardian](/docs/deliver/site-reliability-guardian#business-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") â you use, the underlying event structure is different.
The number of events written by the Site Reliability guardian is the same, no matter the type.
For each validation, one **started** event, one **finished** event, and `n` **objective** event, one for each objective of the respective guardian, are written.

## Lifecycle guardian (SDLC events)

To query [Lifecycle guardian](/docs/deliver/site-reliability-guardian#lifecycle-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") events with DQL, use the following query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"
```

There are two different types of events: `validation` and `validation.objective`.
For `validation` event types, there are two additional subtypes based on the event status `started` and `finished`.

validation started

validation finished

validation.objective

To query Lifecycle guardian `validation` `started` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation"



| filter event.status == "started"
```

To query Lifecycle guardian `validation` `finished` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation"



| filter event.status == "finished"
```

To query Lifecycle guardian `validation.objective` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation.objective"
```

The above lifecycle events share several common fields.
Any data that is related to guardian internals is stored with a prefix of `dt.srg.`.
The structure of the other event fields aligns with the [Semantic Dictionary for Software Development Lifecycle Validation Events](/docs/semantic-dictionary/model/sdlc-events#sdlc-validation-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.").

### Lifecycle guardian event fields

When you want to integrate Lifecycle guardian validation results with a [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or other tooling that you have created, the event fields below is a good starting point for your queries.

**Field name**

**Description**

**Event type / status**

`validation.result`

A text indicating the result of the validation. Any value of `pass`, `warning`, `fail`, `error`, or `info` is possible.

`validation`, `finished`

`dt.srg.id`

The ID of the guardian. It could be used to filter for specific guardian events or as part of a backlink to the guardian.

all

`dt.srg.tags`

All the tags that have been defined for a guardian. It could be used to filter for specific guardian events.

all

`task.id`

The ID of the guardian validation. It could be used as part of a backlink to the analysis page of the guardian.

all

## Business guardian (Business events)

To query business guardian events with DQL, use the following query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"
```

You can see three different types of events: `guardian.validation.started`, `guardian.validation.finished`, and `guardian.validation.objective`.

guardian.validation.started

guardian.validation.finished

guardian.validation.objective

To query Business `guardian.validation.started` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.started"
```

To query Business `guardian.validation.finished` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.finished"
```

To query Business `guardian.validation.objective` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.objective"
```

The above business events share several common fields.

### Business guardian event fields

When you want to integrate business guardian validation results with a [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or other tooling that you have created, the event fields below is a good starting point for your queries.

**Field name**

**Description**

**Event type / status**

`validation.status`

A text indicating the status of the validation. Any value of `pass`, `warning`, `fail`, `error`, or `info` is possible.

`guardian.validation.finished`

`guardian.id`

The ID of the guardian. It could be used to filter for specific guardian events or as part of a backlink to the guardian.

all

`guardian.tags`

All the tags that have been defined for a guardian. It could be used to filter for specific guardian events.

all

`validation.id`

The ID of the guardian validation. It could be used as part of a backlink to the analysis page of the guardian.

all

---

## deliver/site-reliability-guardian/execution-context.md

---
title: Guardian execution context
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/execution-context
scraped: 2026-02-17T05:11:33.815602
---

# Guardian execution context

# Guardian execution context

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 29, 2023

Your Continuous Integration (CI) tool, for example, Jenkins, can [send business events to Dynatrace](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API."). These events can then trigger Site Reliability Guardian validations in a workflow.

Disclaimer

The following steps use business events to integrate into a CI/CD pipeline and fetch validation results. This approach is valid for now, but we plan a new event kind for events occurring during the software development lifecycle of a software component. This new event kind will replace business events in the future.

If you want to filter the Site Reliability Guardian validation events based on the source trigger, the created business events must contain context information from the external tool. The context information can be carried by an externalId, a version number, a build number, or any parameter that lets you identify the tool.

## Context propagation

To propagate the execution context, the event triggering a workflow execution must contain the `execution_context` field, as in the example below.

```
{



"timeframe.to": "2023-03-08T06:29:08.809Z",



"timeframe.from": "2023-03-08T05:29:08.809Z",



"errors": "[]",



"status": "fail",



"event.id": "d08a70d8-f6de-4d0d-bd34-5d416a20ba6a",



"timestamp": 1678256963078000000,



"event.kind": "BIZ_EVENT",



"event.type": "guardian.validation.triggered",



"tag.stage": "hardening",



"tag.service": "carts",



"event.provider": "Jenkins",



"dt.system.bucket": "default_bizevents_short"



"execution_context": {



"buildId": "4711",



"version": "0.1.0"



}



}
```

The context execution is propagated to the guardian validation business event. The `guardian.validation.started`, `guardian.validation.finished`, and `guardian.validation.objective` events contain the propagated `execution_context` field.

## Query your guardian data using execution context

This DQL shows you the first `guardian.validation.objective` business event with a specific guardian ID and parses the execution context field to extract a specific value from the event JSON.

```
fetch bizevents |



filter event.type == "guardian.validation.objective" AND guardian.id == "vu9U3hXa3q0AAAABADFhcHA6ZHluYXRyYWNlLnNpdGUucmVsaWFiaWxpdHkuZ3VhcmRpYW46Z3VhcmRpYW5zAAZ0ZW5hbnQABnRlbmFudAAkMWNiZDVkYWYtZThhNi0zMDkxLWFkOGQtMmU5NDNmNWJmZWJmvu9U3hXa3q0" |



limit 1 |



parse execution_context, "JSON:parsed_execution_context"
```

This DQL shows you all `guardian.validation.finished` business events where the execution context is defined by `buildid` equal to `4711`.

```
fetch bizevents



| filter event.type == "guardian.validation.finished"



| parse execution_context, "JSON:parsed_execution_context"



| filter parsed_execution_context[buildId] == "4711"
```

---

## deliver/site-reliability-guardian/guardian-list.md

---
title: List and work with your guardians
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/guardian-list
scraped: 2026-02-17T05:11:27.358442
---

# List and work with your guardians

# List and work with your guardians

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 09, 2025

The validation view, which is called the "All guardians" page, gives you an overview of all your guardians.
You can compare or bulk delete your guardians in the  **Table**.

### List

To list all your guardians

1. Search for ![Site Reliability Guardian](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Site Reliability Guardian") Site Reliability Guardian.
2. Select ![Site Reliability Guardian](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Site Reliability Guardian") Site Reliability Guardian.

   The **All guardians** page opens, showing a list of all your guardians.
   By default, the guardians are displayed in the  **Grid** view.

   ![Screenshot is showing a list of guardians in a grid view.](https://dt-cdn.net/images/gmg80500-dev-apps-dynatracelabs-com-ui-apps-dynatrace-site-reliability-guardian-2-3434-8a52040e6d.png)

### Work with guardians

To with your guardians

1. Go to the window's top-right, just below the  **New guardian**  button.
2. If you're in the  **Grid** view, switch to the  **Table** view.

   In this view, you can quickly compare and delete the guardians.
   If you used the **Table** view the last time, this view is shown by default.

   ![Screenshot is showing a list of guardians in a table view.](https://dt-cdn.net/images/gmg80500-dev-apps-dynatracelabs-com-ui-apps-dynatrace-site-reliability-guardian-1-3414-1e523a8817.png)

### View older results

You can view older results by opening a guardian and selecting a different timeframe.

---

## deliver/site-reliability-guardian.md

---
title: Site Reliability Guardian
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian
scraped: 2026-02-17T04:58:01.403715
---

# Site Reliability Guardian

# Site Reliability Guardian

* Latest Dynatrace
* App
* 15-min read
* Updated on Jan 28, 2026

In this tutorial

* Create and use guardians
* Use guardians at scale with Site Reliability Guardian as code

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

app-settings:objects:read

Read guardian configurations

app-settings:objects:write

Write guardian configurations

storage:buckets:read

Enables reading all system data stored in Grail

storage:logs:read

Read logs during validations

storage:metrics:read

Read metrics during validations

storage:bizevents:read

Read business events during validations

storage:events:write

Write business events during validations

storage:events:read

Read events during validations

storage:spans:read

Read spans during validations

storage:entities:read

Read entities during validations

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

The Site Reliability Guardian is a Dynatrace app that automates change impact analysis to validate service availability, performance, and capacity objectives across various systems. It enables DevOps platform engineers to make the right release decisions and empowers SREs to apply Service-Level Objectives (SLOs) for their critical services.

![Guardians overview](https://dt-cdn.net/images/overview-screen-light-1920-fkjm7jk-1920-9ee2115a3a.png)![The details of a Guardian in a failure state](https://dt-cdn.net/images/screenshot-2023-09-19-150559-1915-0a8661d7f2.png)![Get started quickly by using predefined templates to guard your critical services.](https://dt-cdn.net/images/1-3-0-templates-light-1920-zvwdsns-1920-cbc918b08d.png)

1 of 3

## Learning modules

Go through the following process to learn using Site Reliability Guardian:

[01Create a Site Reliability guardian

* How-to guide
* Create a guardian manually or from a predefined template.](/docs/deliver/site-reliability-guardian/create-srg)[02List and work with your guardians

* How-to guide
* List your guardians to view, compare, or delete them in bulk.](/docs/deliver/site-reliability-guardian/guardian-list)[03Add Site Reliability Guardian objective

* Reference
* Add a new Site Reliability Guardian objective.](/docs/deliver/site-reliability-guardian/reference)[04Guardian execution context

* How-to guide
* Filter Site Reliability Guardian validation events triggered by an external tool using the context information provided by the tool.](/docs/deliver/site-reliability-guardian/execution-context)[05Site Reliability Guardian as code

* How-to guide
* See configuration as code examples for a guardian and its workflow.](/docs/deliver/site-reliability-guardian/config-as-code-srg)[06Site Reliability Guardian Role Permissions

* Reference
* Configure role permissions to use the Site Reliability Guardian.](/docs/deliver/site-reliability-guardian/role-permissions)[07Site Reliability guardian event structure

* Reference
* Details about the event structure of the Site Reliability Guardian.](/docs/deliver/site-reliability-guardian/event-structure)[08Validate a Site Reliability guardian

* Tutorial
* Trigger a guardian validation either manually or automatically using a workflow to evaluate service reliability.](/docs/deliver/site-reliability-guardian/trigger-srg)

## Site Reliability Guardian concepts

Site Reliability Guardian is based on the following concepts:

### 1. Guardian

A guardian is the grouping of objectives. It is built around a set of entities reflecting a service or application you want to safeguard.

A guardian provides you with a default [automation workflow](#automation) that performs the objective [validation](#validation). As a result, a guardian always represents the latest validation result derived from the objectives.

We support two types of guardians.
While these two types don't differ from a conceptual point of view, there are technical and semantic differences that distinguish them.

### Lifecycle guardian (SDLC events)

* Reads and writes [SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.") as validation results.
* It is aligned with the [validation events specification in the Semantic Dictionary](/docs/semantic-dictionary/model/sdlc-events#sdlc-validation-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.").
* It is intended to be used in the context of the Software Development Lifecycle.

  + As a quality gate in progressive delivery scenarios
  + As a performance indicator after load testing
  + As a continuous health monitor for services and components

### Business guardian (Business events)

* Reads and writes [Business events](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.") as validation results
* It is intended for business-level usage and insights into application behavior

As these two types of guardians have different data sources (`bizevents` vs. `events`) and different event data structures, you need to adapt your DQL queries that target guardian validation events in Notebooks or Dashboards when switching from one type to the other.
For more details on the structural differences, see [Site Reliability guardian event structure](/docs/deliver/site-reliability-guardian/event-structure "Details about the event structure of the Site Reliability Guardian.").

You can create a maximum of 1000 guardians.

### 2. Objective

Objectives are means for measuring the performance, availability, capacity, and security of your services. Objectives are measured by indicators. You can define an objective for your guardian that is validated on demand or automatically.

You can create a maximum of 50 objectives for each guardian.

### 3. Indicator

An indicator is a value against which the warning and failure thresholds are checked using a comparison operator. To retrieve an indicator value, use [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

### 4. Static thresholds

The [static warning and failure thresholdsï»¿](https://dt-url.net/ta5s0pxa) determine whether the measured value of the indicator meets the objective, is close to violating the objective, or violates the objective.

Warning and failure are optional; objective validation can vary:

* If both the warning and failure thresholds are set, the objective validation can return warning, failure, or pass.
* If just the warning threshold is set, the objective validation can return warning or pass.
* If no threshold is set, the objective validation does not return a status but is used for informational purposes.

### 5. Auto-adaptive thresholds

[Auto-adaptive thresholdsï»¿](https://dt-url.net/c55q0p1u) are dynamic limits that adjust over time based on previous validations. If an objective changes its behavior, the threshold adapts automatically.

* Auto-adaptive thresholds are only available for fetching data via DQL.
  The Dynatrace Intelligence threshold analyzer requires a minimum of 5 validations for auto-adaptive thresholds to take effect. During this learning phase, the objective validation returns an info state. All subsequent validations will then use the auto-adapted thresholds, impacting the overall validation.
* Switching from static to auto-adaptive is supported.

### 6. Operator

The comparison operator defines whether the objective is met: the indicator is less than or equal to (A lower value is good for my result), or it is greater than or equal to (A higher value is good for my result), the warning and failure threshold.

### 7. Tags

To organize your guardians, you can assign tags to them. Tags use the `key:value` format, with the value being optional.

To assign a tag to your guardian, either specify it in the **Add tags to your guardian** section during guardian creation or add the tag later in edit mode.

To filter the list of all guardians by a tag, type the tag in the **Search by name or tag** fieldâthe page automatically updates to show only guardians with matching tags.

This DQL shows you the first `guardian.validation.objective` business event with a specific guardian ID and parses the guardian tags field to extract a specific tag value from the event JSON.

```
fetch bizevents |



filter event.type == "guardian.validation.objective" AND guardian.id == "vu9U3hXa3q0AAAABADFhcHA6ZHluYXRyYWNlLnNpdGUucmVsaWFiaWxpdHkuZ3VhcmRpYW46Z3VhcmRpYW5zAAZ0ZW5hbnQABnRlbmFudAAkMWNiZDVkYWYtZThhNi0zMDkxLWFkOGQtMmU5NDNmNWJmZWJmvu9U3hXa3q0" |



limit 1 |



parse guardian.tags, "JSON:parsed_guardian_tags"
```

This DQL shows you all `guardian.validation.finished` business events from guardians tagged as `tagkey:my-tagged-guardian`.

```
fetch bizevents



| filter event.type == "guardian.validation.finished"



| expand guardian.tags



| filter contains(guardian.tags, "my-tagged-guardian")
```

### 8. Guardian workflow action

You can automate the execution of a guardian via [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."), tying guardian execution to [an event](/docs/analyze-explore-automate/workflows/trigger/event-trigger#event-trigger "Guide to creating workflow automation event triggers in Dynatrace Workflows.") or [an API call](/docs/analyze-explore-automate/workflows/trigger#on-demand-trigger "Introduction to workflow automation triggers for workflows.").



### Add a guardian action to an existing workflow or create a new workflow

The same final steps apply, whether you add a guardian to an existing workflow or create a new workflow.

#### Edit an existing workflow

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and open your workflow.
2. Go to the last task, which should be the predecessor of the guardian validation action, and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.

#### Create a new workflow

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow**.
2. Select a [trigger](/docs/analyze-explore-automate/workflows/trigger "Introduction to workflow automation triggers for workflows.").
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.

#### Set up a guardian validation action

1. Find `Site Reliability Guardian` in the **Choose action** panel.
2. On the **Input** tab, you have two options to select the required guardian:

* Select the guardian from the list.
* Use an [expression](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") to extract the guardian from the triggering event or a previous workflow action.
* Configure the validation timeframe.

For more details, see also [Validate a Site Reliability guardian](/docs/deliver/site-reliability-guardian/trigger-srg "Trigger a guardian validation either manually or automatically using a workflow to evaluate service reliability."), [Automate release validation](/docs/deliver/release-validation-automated "Learn how to automatically validate your business-critical service release using this hands-on tutorial."), [Test pipeline observability](/docs/deliver/test-pipeline-observability "Utilize Dynatrace to observe and analyze test pipelines effectively")

### Create a workflow from the All guardians page

You can trigger your guardian automatically using a workflow.

To create a workflow for this guardian, follow these steps:

1. Go to your guardian.
2. To automate the trigger for your guardian, on the **All guardians** page, hover over your guardian or open it, and then select **Automate**. **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") opens in a new browser tab. You can also access **Automate** from the validation details.

   This step creates a new workflow for your guardian with an even trigger and a **run validation** action.

   When you create a workflow in this manner, the following parameters are configured; however, ensure that you adapt them as needed.

You can create a new workflow by selecting ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Automate**. When you create a workflow this way, the following parameters are configured, but be sure to adapt them as needed.

* A new workflow with an event trigger and a **run validation action** is created.
* Depending on the type of guardian - Lifecycle or Business - the **event type** and the **filter query** are set accordingly.

  + For **Lifecycle guardians** (SDLC events) the **event type** is set to `events` and the **filter query** defaults to `event.type == "validation.triggered" AND event.kind == "SDLC_EVENT"`.
  + For **Business guardians** (Business events) the **event type** is set to `bizevents` and the **filter query** defaults to `event.type == "guardian.validation.triggered"`.
  + If the guardian has tags defined, they're used as additional filters in the **filter query** of the trigger.
* The only action of the workflow is the respective guardian validation action.

The guardian validation action generates the following output and passes it to the subsequent actions of the workflow.

Parameter

Description

`guardian_id`

The ID of the validated guardian

`guardian_name`

The name of the validated guardian

`guardian_tags`

An array of tags assigned to the validated guardian

`execution_context`

The execution context property of the trigger, if it was set

`validation_id`

The ID of all events generated by the validation

`validation_url`

The URL with the full validation details

`validation_status`

The status of the validation, indicating the overall result. The following values are possible:

* `info`
* `pass`
* `warning`
* `fail`
* `error`

`validation_summary`

The number of objectives for each status

To learn more about workflows for a guardian, select  >  **Get started with Automation**.

### 9. Validation

If a workflow is created, your guardian can be validated automatically, depending on the [trigger](/docs/analyze-explore-automate/workflows/trigger "Introduction to workflow automation triggers for workflows.") you chose. You can also perform the validation manually.

### Validation overview

By default, the **All guardians** page lists all the guardians.

For more information on the **All guardians** page, see [List and work with your guardians](/docs/deliver/site-reliability-guardian/guardian-list "List your guardians to view, compare, or delete them in bulk.").

### Automated validation

The event subscriptions in the workflow define when the validation of a guardian has triggered automatically.

### Manual validation

You can perform a validation of a guardian by selecting the  **Validate** button on the overview screen or within the validation details screen.

* Select the validation timeframe.
* Select the  **Validate** button.

### Individual objective result

For each objective, the validation returns the derived value and classification. The severity goes from the highest (1) to the lowest (5).

| Severity | Name | Description |
| --- | --- | --- |
| 1 | **Error** | The objective could not be validated due to an error deriving the indicator. |
| 2 | **Fail** | The value violates the failure threshold; the objective is not met. |
| 3 | **Warning** | The value is in the warning range; the objective is met, but close to failure. |
| 4 | **Pass** | The value is within the target range, the objective is met. |
| 5 | **Info** | No classification, but the objective's value can be used for informational purposes. |

### Overall validation result

After the validation of each objective is done, the guarding uses the most severe of individual validations as the overall validation result. Examples of this result usage include:

* Making a release decision in your delivery pipeline.
* Reporting on the current status of your service.

### 10. Segments

Leverage [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") in DQL-based objectives to logically structure and conveniently filter observability data.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Automated change impact analysis for your deployment and release processes

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/site-reliability-guardian/?internal_source=doc&internal_medium=link&internal_campaign=cross)

---
