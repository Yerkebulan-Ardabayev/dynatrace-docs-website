# Dynatrace Documentation: deliver/site-reliability-guardian

Generated: 2026-02-16

Files combined: 3

---


## Source: event-structure.md


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


## Source: execution-context.md


---
title: Guardian execution context
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/execution-context
scraped: 2026-02-16T21:31:49.228711
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


## Source: guardian-list.md


---
title: List and work with your guardians
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/guardian-list
scraped: 2026-02-15T21:23:04.462733
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
